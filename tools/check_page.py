#!/usr/bin/env python3
"""Mechanical post-build check for one service x area page.

Usage:
    python tools/check_page.py <slug | page.html> [--root DIR] [--no-registration] [--stats]

Prints PASS, or FAIL followed by one line per failure. Exit code 0 = PASS, 1 = FAIL.

Rules come from blueprint-v2_3-full.md (the consolidated blueprint) and the
conventions the live silos actually use (MANIFEST-site-rebuild-186/187, the
Cat6 and Network Cable Repair silos). Where the two disagree, the live
convention is used and the rule is marked "LIVE CONVENTION" below:
  - canonical and sitemap <loc> are extensionless (v2.3 section 4 says .html)
  - phones follow the per-area CallRail map below (v2.3 section 8 is older)
  - the warranty block is the three-year text used on the Cat6 silo
    (the Network Cable Repair silo still carries one-year text - open decision)

This checks only what can be checked mechanically. Research accuracy,
meaning-level duplicate intents, local facts and design still need a human
(or builder) review per blueprint section 7.

Standard library only.
"""

import argparse
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

DOMAIN = "https://www.abstractenterprisessecuritysystems.com"
FORM_KEY = "88890030-1770-483e-a622-0e054d8e14b1"
LICENSE = "12000287431"
WORDS_MIN, WORDS_MAX = 12000, 14000
TITLE_MAX = 60
META_MIN, META_MAX = 150, 160
FIGURES = 11
SIZE_CLUSTER_BYTES = 2048
REQUIRED_SCHEMA = ("LocalBusiness", "Service", "FAQPage", "BreadcrumbList", "ImageObject", "HowTo")

# Protected, verbatim (blueprint v2.3 Appendix A; text as published on the Cat6 silo).
WARRANTY = (
    "Abstract Enterprises Security Systems provides a three-year warranty on products supplied by AESS "
    "for normal wear and tear. It does not cover existing or customer wiring, customer-supplied equipment, "
    "lightning or other acts of God, power outages or surges, physical damage or unplugging, internet, "
    "router or phone changes, or camera readjustments requested after completion. After the warranty "
    "period, service is $195 per hour with a three-hour minimum ($585)."
)

TOLL_FREE = "8004860943"
WHATSAPP = "7186790359"          # only ever as a wa.me link, never tel: or visible digits
SECONDARY_DOMAIN_PHONE = "9297305331"

BROOKLYN_GBP = {"id": "#brooklyn", "street": "1282 Troy"}
BRONX_GBP = {"id": "#bronx", "street": "460 E"}

# LIVE CONVENTION phone map (Cat6 + Network Cable Repair silos, Sept 2026):
# children carry only their direct line; hubs carry the toll-free line (plus the listed direct line).
# area suffix: (aliases for geo checks, kind, parent suffix, GBP, primary phone, other allowed phones)
AREAS = {
    "nyc":                (("NYC", "New York City"), "hub", None, "brooklyn", TOLL_FREE, {"3479348335"}),
    "manhattan":          (("Manhattan",), "child", "nyc", "bronx", "9295600737", set()),
    "brooklyn":           (("Brooklyn",), "child", "nyc", "brooklyn", "3479348335", set()),
    "queens":             (("Queens",), "child", "nyc", "bronx", "3474346392", set()),
    "bronx":              (("Bronx",), "child", "nyc", "bronx", "6464900629", set()),
    "staten-island":      (("Staten Island",), "child", "nyc", "brooklyn", "3479348335", set()),
    "long-island":        (("Long Island",), "hub", None, "brooklyn", TOLL_FREE, set()),
    "hudson-valley":      (("Hudson Valley",), "hub", None, "bronx", TOLL_FREE, {"8456403835"}),
    "nassau-county":      (("Nassau",), "child", "long-island", "brooklyn", "5163465778", set()),
    "suffolk-county":     (("Suffolk",), "child", "long-island", "brooklyn", "6314072884", set()),
    "westchester-county": (("Westchester",), "child", "hudson-valley", "bronx", "9148772578", set()),
    "rockland-county":    (("Rockland",), "child", "hudson-valley", "bronx", "8456403835", set()),
    "orange-county":      (("Orange County", "Orange"), "child", "hudson-valley", "bronx", "8456403835", set()),
    "putnam-county":      (("Putnam",), "child", "hudson-valley", "bronx", "8456403835", set()),
    "dutchess-county":    (("Dutchess",), "child", "hudson-valley", "bronx", "8456403835", set()),
    "ulster-county":      (("Ulster",), "child", "hudson-valley", "bronx", "8456403835", set()),
}
BOROUGHS = ("staten-island", "manhattan", "brooklyn", "queens", "bronx")
COMPANY_PHONES = {a[4] for a in AREAS.values()} | {p for a in AREAS.values() for p in a[5]} | {
    TOLL_FREE, WHATSAPP, SECONDARY_DOMAIN_PHONE}
GEO_WORDS = sorted({w for a in AREAS.values() for w in a[0]} | {
    "New York", "NY", "County", "Borough", "the Bronx", "Long Island", "Hudson Valley"}, key=len, reverse=True)

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
SKIP = {"script", "style", "noscript", "template", "svg", "head"}
BALANCED = ("section", "div", "details", "form", "figure")


# ------------------------------------------------------------------ parsing

class Page(HTMLParser):
    """One pass over the HTML: visible text, head fields, forms, figures,
    links, JSON-LD, FAQ items and question headings."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []                 # (tag, hidden)
        self.text = []
        self.title = ""
        self.meta_description = None
        self.canonicals = []
        self.h1 = 0
        self.opens, self.closes = {t: 0 for t in BALANCED}, {t: 0 for t in BALANCED}
        self.forms, self._form = [], None
        self.figure_depth, self.figures, self.images = 0, [], []
        self.hrefs = []
        self.jsonld, self._jsonld = [], None
        self.cache_versions = []
        self._capture = []              # [kind, depth, parts]
        self.faq_q, self.faq_a, self.headings = [], [], []
        self._in_title = False

    def _hidden(self):
        return any(h for _, h in self.stack)

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        cls = a.get("class", "").split()
        if tag in BALANCED:
            self.opens[tag] += 1
        if tag == "title":
            self._in_title = True
        elif tag == "meta" and a.get("name", "").lower() == "description":
            self.meta_description = a.get("content", "")
        elif tag == "link" and a.get("rel", "").lower() == "canonical":
            self.canonicals.append(a.get("href", ""))
        elif tag == "h1":
            self.h1 += 1
        elif tag == "form":
            self._form = {"attrs": a, "inputs": []}
            self.forms.append(self._form)
        elif tag in ("input", "textarea", "select") and self._form is not None:
            self._form["inputs"].append(dict(a, _tag=tag))
        elif tag == "figure":
            self.figure_depth += 1
            self.figures.append([])
        elif tag == "img":
            img = {"src": a.get("src", ""), "alt": a.get("alt"), "title": a.get("title"),
                   "in_figure": self.figure_depth > 0}
            self.images.append(img)
            if self.figure_depth > 0 and self.figures:
                self.figures[-1].append(img)
        elif tag == "a":
            self.hrefs.append(a.get("href", ""))
        elif tag == "script":
            if a.get("type", "").lower() == "application/ld+json":
                self._jsonld = []
            m = re.search(r"mega-nav\.js\?v=([A-Za-z0-9_-]+)", a.get("src", ""))
            if m:
                self.cache_versions.append(m.group(1))

        kind = ("faq_q" if "faq-question" in cls else "faq_a" if "faq-answer" in cls
                else "heading" if tag in ("h2", "h3", "summary") else None)
        if kind and tag not in VOID:
            self._capture.append([kind, tag, 1, []])
        elif tag not in VOID:
            for c in self._capture:
                if c[1] == tag:
                    c[2] += 1

        if tag not in VOID:
            hidden = (tag in SKIP or "hidden" in a or a.get("aria-hidden") == "true"
                      or re.search(r"display\s*:\s*none", a.get("style", "")) is not None)
            self.stack.append((tag, hidden))
        if tag in ("br", "p", "li", "td", "th", "div", "section", "h1", "h2", "h3", "h4", "button"):
            self.text.append(" ")

    def handle_endtag(self, tag):
        if tag in BALANCED:
            self.closes[tag] += 1
        if tag == "title":
            self._in_title = False
        elif tag == "form":
            self._form = None
        elif tag == "figure":
            self.figure_depth = max(0, self.figure_depth - 1)
        elif tag == "script" and self._jsonld is not None:
            self.jsonld.append("".join(self._jsonld))
            self._jsonld = None

        for c in list(self._capture):
            if c[1] == tag:
                c[2] -= 1
                if c[2] == 0:
                    self._capture.remove(c)
                    value = norm_space("".join(c[3]))
                    {"faq_q": self.faq_q, "faq_a": self.faq_a, "heading": self.headings}[c[0]].append(value)

        if any(t == tag for t, _ in self.stack):
            while self.stack:
                t, _ = self.stack.pop()
                if t == tag:
                    break
        self.text.append(" ")

    def handle_data(self, data):
        if self._jsonld is not None:
            self._jsonld.append(data)
            return
        if self._in_title:
            self.title += data
        for c in self._capture:
            c[3].append(data)
        if not self._hidden():
            self.text.append(data)


def norm_space(s):
    return re.sub(r"\s+", " ", s or "").strip()


def visible_text(page):
    return norm_space("".join(page.text))


def count_words(text):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.,:/$%&+-]*", text))


def mask(s):
    """Lower-case, geo names removed, punctuation stripped - for duplicate checks."""
    s = html.unescape(s or "")
    for w in GEO_WORDS:
        s = re.sub(r"\b" + re.escape(w) + r"\b", " ", s, flags=re.I)
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    return norm_space(s)


def digits(s):
    d = re.sub(r"\D", "", s or "")
    return d[1:] if len(d) == 11 and d.startswith("1") else d


def parse(path):
    p = Page()
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    p.feed(raw)
    p.close()
    return p, raw


def walk_schema(node, out):
    if isinstance(node, dict):
        out.append(node)
        for v in node.values():
            walk_schema(v, out)
    elif isinstance(node, list):
        for v in node:
            walk_schema(v, out)


def types_of(node):
    t = node.get("@type")
    return set(t) if isinstance(t, list) else {t} if isinstance(t, str) else set()


# ------------------------------------------------------------------ identity

def identify(slug):
    """(silo, area suffix) for a page slug; neighbourhood pages (…-<nbhd>-<borough>-ny)
    take their borough's rules."""
    for suffix in sorted(AREAS, key=len, reverse=True):
        if slug.endswith("-" + suffix):
            return slug[: -len(suffix) - 1], suffix
    m = re.match(r"^(.*?)-[a-z0-9-]+-(" + "|".join(BOROUGHS) + r")-ny$", slug)
    if m:
        return m.group(1), m.group(2)
    return None, None


def silo_pages(root, silo, slug):
    """Every other page file in the same silo (area pages and neighbourhood pages)."""
    out = []
    for name in os.listdir(root):
        if name.endswith(".html") and name.startswith(silo + "-") and name[:-5] != slug:
            s, _ = identify(name[:-5])
            if s == silo:
                out.append(os.path.join(root, name))
    return sorted(out)


def local_path(href):
    """Site-internal path for a relative or same-domain absolute link, else None."""
    h = (href or "").strip()
    m = re.match(r"^https?://(?:www\.)?abstractenterprisessecuritysystems\.com(/[^\s]*)?$", h, re.I)
    if m:
        h = m.group(1) or "/"
    if not h.startswith("/") or h.startswith("//"):
        return None
    return h


def link_set(hrefs):
    return {p.split("#")[0].split("?")[0].rstrip("/") or "/" for p in map(local_path, hrefs) if p}


def resolves(root, href):
    """Internal link target exists as a file, a .html page, or a folder index."""
    path = href.split("#", 1)[0].split("?", 1)[0]
    if path in ("", "/"):
        return True
    local = os.path.join(root, path.lstrip("/").replace("/", os.sep))
    return (os.path.isfile(local) or os.path.isfile(local + ".html")
            or os.path.isfile(os.path.join(local, "index.html")))


# ------------------------------------------------------------------ checks

def check(root, slug, registration=True, stats=False):
    fails = []
    fail = fails.append
    path = os.path.join(root, slug + ".html")
    if not os.path.isfile(path):
        return [f"page file not found: {path}"], {}
    silo, area = identify(slug)
    if not area:
        return [f"can't tell the area from slug '{slug}' (expected a suffix like -nyc, -bronx, -nassau-county)"], {}
    aliases, kind, parent, gbp, primary, extra = AREAS[area]
    page, raw = parse(path)
    text = visible_text(page)
    words = count_words(text)

    # --- length, title, meta, headings, structure
    if not WORDS_MIN <= words <= WORDS_MAX:
        fail(f"rendered word count {words:,} (required {WORDS_MIN:,}-{WORDS_MAX:,})")
    title = norm_space(html.unescape(page.title))
    if not title:
        fail("no <title>")
    elif len(title) > TITLE_MAX:
        fail(f"title is {len(title)} chars (max {TITLE_MAX}): {title}")
    if title and not any(a.lower() in title.lower() for a in aliases):
        fail(f"title doesn't name the area ({' / '.join(aliases)}): {title}")
    md = norm_space(html.unescape(page.meta_description or ""))
    if not md:
        fail("no <meta name=\"description\">")
    elif not META_MIN <= len(md) <= META_MAX:
        fail(f"meta description is {len(md)} chars (required {META_MIN}-{META_MAX})")
    if page.h1 != 1:
        fail(f"{page.h1} <h1> elements (exactly one required)")
    for t in BALANCED:
        if page.opens[t] != page.closes[t]:
            fail(f"unbalanced <{t}>: {page.opens[t]} open vs {page.closes[t]} close")
    if "${" in raw:
        fail("unresolved template token '${' in the HTML")
    if re.search(r"\b555[-. ]\d{4}\b|\(555\)", raw):
        fail("placeholder 555 phone number")

    # --- canonical
    want = f"{DOMAIN}/{slug}"
    if len(page.canonicals) != 1:
        fail(f"{len(page.canonicals)} canonical tags (exactly one required)")
    elif page.canonicals[0] != want:
        fail(f"canonical is {page.canonicals[0]} (required {want})")

    # --- phones (approved per-area map)
    allowed = {primary} | extra
    tels = [digits(h[4:]) for h in page.hrefs if h.lower().startswith("tel:")]
    if primary not in tels:
        fail(f"approved phone {fmt(primary)} for {area} is not tel-linked")
    for t in sorted(set(tels) - allowed):
        fail(f"phone {fmt(t)} is tel-linked but not approved for {area} (allowed: {', '.join(fmt(p) for p in sorted(allowed))})")
    for m in re.finditer(r"\(?\b(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})\b", text):
        d = m.group(1) + m.group(2) + m.group(3)
        if d in COMPANY_PHONES and d not in allowed:
            fail(f"visible phone {fmt(d)} is not approved for {area}")

    # --- rating, license, warranty
    if not re.search(r"4\.7\s*(?:/|·|★|out of 5)?[^0-9]{0,25}201", text):
        fail("rating 4.7 / 201 not shown in visible text")
    if LICENSE not in text:
        fail(f"NYS license #{LICENSE} not shown")
    if norm_space(WARRANTY) not in text:
        fail("exact warranty text missing or altered (see WARRANTY in tools/check_page.py)")
    if "/warranty" not in link_set(page.hrefs):
        fail("no link to /warranty")

    # --- forms
    forms = [f for f in page.forms if "web3forms.com" in f["attrs"].get("action", "")]
    if len(forms) != 2:
        fail(f"{len(forms)} Web3Forms forms (hero + detail required)")
    for i, f in enumerate(forms, 1):
        inputs = f["inputs"]
        byname = {x.get("name"): x for x in inputs if x.get("name")}
        label = f["attrs"].get("id") or f"form {i}"
        if byname.get("access_key", {}).get("value") != FORM_KEY:
            fail(f"{label}: Web3Forms access_key missing or wrong")
        lp = byname.get("landing_page", {}).get("value")
        if lp != slug:
            fail(f"{label}: landing_page is {lp!r} (required {slug!r}, extensionless)")
        for need in ("name", "phone"):
            if need not in byname:
                fail(f"{label}: no '{need}' field")
        if "botcheck" not in byname:
            fail(f"{label}: no botcheck honeypot")
        if not any(x.get("type") == "checkbox" for x in inputs):
            fail(f"{label}: no consent checkbox")

    # --- JSON-LD
    nodes = []
    for i, block in enumerate(page.jsonld, 1):
        if re.search(r"&(?:[A-Za-z]+|#\d+|#x[0-9A-Fa-f]+);", block):
            fail(f"JSON-LD block {i} contains an HTML entity (Unicode only)")
        try:
            walk_schema(json.loads(block), nodes)
        except ValueError as err:
            fail(f"JSON-LD block {i} doesn't parse: {err}")
    found = set().union(*(types_of(n) for n in nodes)) if nodes else set()
    local = [n for n in nodes if types_of(n) & {"LocalBusiness", "HomeAndConstructionBusiness",
                                                "Electrician", "ProfessionalService", "Organization"}
             and ("address" in n or "@id" in n)]
    for t in REQUIRED_SCHEMA:
        if t == "LocalBusiness":
            if not local:
                fail("no LocalBusiness schema")
        elif t not in found:
            fail(f"no {t} schema")
    agg = [n for n in nodes if "AggregateRating" in types_of(n)]
    if not any(str(n.get("ratingValue")) == "4.7" and str(n.get("reviewCount")) == "201" for n in agg):
        fail("schema AggregateRating is not ratingValue 4.7 / reviewCount 201")
    want_gbp, other_gbp = (BROOKLYN_GBP, BRONX_GBP) if gbp == "brooklyn" else (BRONX_GBP, BROOKLYN_GBP)
    lb_text = json.dumps(local)
    if want_gbp["street"] not in lb_text and not any(str(n.get("@id", "")).endswith(want_gbp["id"]) for n in local):
        fail(f"LocalBusiness schema is not the {gbp.title()} GBP ({want_gbp['street']} / {want_gbp['id']})")
    if other_gbp["street"] in lb_text:
        fail(f"LocalBusiness schema carries the wrong GBP address ({other_gbp['street']})")
    for n in nodes:
        tel = n.get("telephone")
        if isinstance(tel, str) and digits(tel) not in allowed:
            fail(f"schema telephone {tel} not approved for {area}")

    # --- FAQ visible == FAQPage schema
    faq_schema = []
    for n in nodes:
        if "FAQPage" in types_of(n):
            for q in n.get("mainEntity") or []:
                if isinstance(q, dict):
                    ans = q.get("acceptedAnswer") or {}
                    faq_schema.append((norm_space(q.get("name", "")),
                                       norm_space(re.sub(r"<[^>]+>", " ", ans.get("text", "") if isinstance(ans, dict) else ""))))
    visible_faq = list(zip(page.faq_q, page.faq_a))
    if not visible_faq:
        fail("no visible FAQ (.faq-question / .faq-answer)")
    elif len(visible_faq) != len(faq_schema):
        fail(f"visible FAQ has {len(visible_faq)} items but FAQPage schema has {len(faq_schema)}")
    else:
        for (vq, va), (sq, sa) in zip(visible_faq, faq_schema):
            if vq != sq:
                fail(f"FAQ question differs from schema: {vq[:70]!r} vs {sq[:70]!r}")
            elif norm_space(va) != sa:
                fail(f"FAQ answer differs from schema for: {vq[:70]!r}")

    # --- images
    figs = [imgs[0] for imgs in page.figures if imgs]
    if len(figs) != FIGURES:
        fail(f"{len(figs)} figure images (exactly {FIGURES} required)")
    for label, key in (("alt", "alt"), ("title", "title")):
        vals = [norm_space(i.get(key) or "") for i in figs]
        if any(not v for v in vals):
            fail(f"{sum(1 for v in vals if not v)} figure image(s) with no {label}")
        dups = {v for v in vals if v and vals.count(v) > 1}
        for v in sorted(dups):
            fail(f"duplicate image {label}: {v[:80]!r}")
    for i in figs:
        alt = i.get("alt") or ""
        if alt and not any(a.lower() in alt.lower() for a in aliases):
            fail(f"image alt has no geo ({'/'.join(aliases)}): {alt[:80]!r}")
    for i in page.images:
        src = i["src"]
        if src.startswith(("http://", "https://", "data:", "//")):
            continue
        if not resolves(root, src):
            fail(f"broken image path: {src}")
    srcs = [i["src"] for i in figs]
    for s in sorted({s for s in srcs if srcs.count(s) > 1}):
        fail(f"same image file used twice: {s}")

    # --- internal links
    for h in filter(None, map(local_path, page.hrefs)):
        if re.search(r"\.html(?:[#?]|$)", h):
            fail(f".html internal link (use the clean URL): {h}")
        elif not resolves(root, h):
            fail(f"broken internal link: {h}")

    # --- silo: size cluster, cross-links, duplicate questions/answers
    siblings = silo_pages(root, silo, slug)
    size = os.path.getsize(path)
    my_q = {mask(q): q for q in page.faq_q + [h for h in page.headings if h.endswith("?")] if mask(q)}
    my_a = {mask(a): a for a in page.faq_a if len(mask(a).split()) >= 8}
    hrefs = link_set(page.hrefs)
    for sib in siblings:
        sslug = os.path.basename(sib)[:-5]
        ssize = os.path.getsize(sib)
        if abs(ssize - size) <= SIZE_CLUSTER_BYTES:
            fail(f"file size {size:,} B is within 2 KB of sibling {sslug} ({ssize:,} B) - clone signature")
        sp, _ = parse(sib)
        for q in sp.faq_q + [h for h in sp.headings if h.endswith("?")]:
            if mask(q) in my_q:
                fail(f"question duplicated on sibling {sslug}: {my_q[mask(q)][:90]!r}")
        for a in sp.faq_a:
            if mask(a) in my_a:
                fail(f"FAQ answer duplicated on sibling {sslug}: {my_a[mask(a)][:70]!r}")
        s_silo, s_area = identify(sslug)
        if s_area in AREAS and sslug == f"{silo}-{s_area}":         # area pages cross-link each other
            if f"/{sslug}" not in hrefs:
                fail(f"no cross-link to live sibling /{sslug}")
            if f"/{slug}" not in link_set(sp.hrefs):
                fail(f"live sibling {sslug} doesn't link back to /{slug}")

    # --- hub and spoke
    if kind == "child":
        up = f"/{silo}-{parent}"
        if up not in hrefs:
            fail(f"no link up to parent hub {up}")
    elif "/" not in hrefs:
        fail("hub doesn't link up to Home (/)")

    # --- registration (sitemap, _redirects, parent links down)
    if registration:
        sm_path = os.path.join(root, "sitemap.xml")
        sm = open(sm_path, encoding="utf-8").read() if os.path.isfile(sm_path) else ""
        n = sm.count(f"<loc>{DOMAIN}/{slug}</loc>")
        if n != 1:
            fail(f"sitemap.xml has {n} <loc> entries for /{slug} (exactly one, extensionless)")
        if not sm.rstrip().endswith("</urlset>"):
            fail("sitemap.xml tail is not </urlset>")
        rd_path = os.path.join(root, "_redirects")
        rules = [l.split() for l in open(rd_path, encoding="utf-8").read().splitlines()
                 if l.strip() and not l.lstrip().startswith("#")] if os.path.isfile(rd_path) else []
        clean = [r for r in rules if r and r[0] == f"/{slug}"]
        if [r[1:3] for r in clean] != [[f"/{slug}.html", "200"]]:
            fail(f"_redirects needs exactly one '/{slug} /{slug}.html 200' rule (found {len(clean)} rule(s) for /{slug})")
        dot = [r for r in rules if r and r[0] == f"/{slug}.html"]
        if [r[1:3] for r in dot] != [[f"/{slug}", "301!"]]:
            fail(f"_redirects needs exactly one '/{slug}.html /{slug} 301!' rule (live convention)")
        if kind == "child":
            hub = os.path.join(root, f"{silo}-{parent}.html")
            if os.path.isfile(hub):
                hp, _ = parse(hub)
                if f"/{slug}" not in link_set(hp.hrefs):
                    fail(f"parent hub {silo}-{parent} doesn't link down to /{slug}")

    info = {"slug": slug, "silo": silo, "area": area, "kind": kind, "words": words, "title_len": len(title),
            "meta_len": len(md), "figures": len(figs), "jsonld_blocks": len(page.jsonld),
            "schema_types": sorted(t for t in found if t), "faq": len(visible_faq),
            "faq_schema": len(faq_schema), "forms": len(forms), "tel": sorted(set(tels)),
            "siblings_checked": len(siblings), "bytes": size, "cache": sorted(set(page.cache_versions))}
    return fails, info


def fmt(d):
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else d


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("page", help="page slug (fiber-optic-installation-nyc) or path to the .html file")
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="site root (default: the repo this script lives in)")
    ap.add_argument("--no-registration", action="store_true",
                    help="skip sitemap / _redirects / parent-hub checks (for drafts)")
    ap.add_argument("--stats", action="store_true", help="also print what was measured")
    args = ap.parse_args()
    slug = os.path.basename(args.page)
    slug = slug[:-5] if slug.endswith(".html") else slug
    fails, info = check(args.root, slug, registration=not args.no_registration)
    if args.stats and info:
        for k, v in info.items():
            print(f"  {k}: {v}")
    if fails:
        print(f"FAIL ({len(fails)})")
        for f in fails:
            print(f"- {f}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
