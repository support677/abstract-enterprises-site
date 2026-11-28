#!/usr/bin/env python3
"""Mechanical post-build check for one service x area page.

Usage:
    python tools/check_page.py <slug | page.html> [--root DIR] [--no-registration] [--stats] [--legacy]

Prints PASS, or FAIL followed by one line per failure. Exit code 0 = PASS, 1 = FAIL.

Rules come from blueprint-v2_3-full.md (the consolidated blueprint) and the
conventions the live silos actually use. Where they disagree, the most recent
live silo (Network Cable Repair, Sept 2026) wins, per Anwar 2026-09-28, and
the rule is marked "LIVE CONVENTION" below:
  - canonical and sitemap <loc> are extensionless (v2.3 section 4 says .html)
  - phones follow the Network Cable Repair map below (v2.3 section 8 is older)
  - warranty text is the Network Cable Repair terms sentence (one-year
    parts-only), not the Cat6 three-year block
  - rating 4.7 / 201

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
# A size match alone is no longer a fail: a silo of 150 pages fills every 2 KB slot of the normal
# 12-14k-word range (Oct 25 2026). Near-same size + this much shared 8-word phrasing = clone.
CLONE_TEXT_SHARE = 0.30
REQUIRED_SCHEMA = ("LocalBusiness", "Service", "FAQPage", "BreadcrumbList", "ImageObject", "HowTo")

# LIVE CONVENTION, verbatim: the warranty/terms sentence on 13 of the 16
# Network Cable Repair area pages (e.g. network-cable-repair-bronx.html).
WARRANTY = (
    "Full terms — including 50% deposit, one-year parts-only warranty on Abstract Enterprises Security Systems-supplied products, "
    "and the late-fee schedule — are set out in the service agreement."
)

TOLL_FREE = "8004860943"
WHATSAPP = "7186790359"          # only ever as a wa.me link, never tel: or visible digits
SECONDARY_DOMAIN_PHONE = "9297305331"

BROOKLYN_GBP = {"id": "#brooklyn", "street": "1282 Troy"}
BRONX_GBP = {"id": "#bronx", "street": "460 E"}

# LIVE CONVENTION phone map (Network Cable Repair silo, Sept 2026): hubs carry only the
# toll-free line; children carry their direct CallRail line in body/CTAs/schema, and the
# toll-free line is also allowed (it appears in the shared header chrome on every child).
# area suffix: (aliases for geo checks, kind, parent suffix, GBP, primary phone, other allowed phones)
CHILD = {TOLL_FREE}
AREAS = {
    "nyc":                (("NYC", "New York City"), "hub", None, "brooklyn", TOLL_FREE, set()),
    "manhattan":          (("Manhattan",), "child", "nyc", "bronx", "9295600737", CHILD),
    "brooklyn":           (("Brooklyn",), "child", "nyc", "brooklyn", "3479348335", CHILD),
    "queens":             (("Queens",), "child", "nyc", "bronx", "3474346392", CHILD),
    "bronx":              (("Bronx",), "child", "nyc", "bronx", "6464900629", CHILD),
    "staten-island":      (("Staten Island",), "child", "nyc", "brooklyn", "3479348335", CHILD),
    "long-island":        (("Long Island",), "hub", None, "brooklyn", TOLL_FREE, set()),
    "hudson-valley":      (("Hudson Valley",), "hub", None, "bronx", TOLL_FREE, set()),
    "nassau-county":      (("Nassau",), "child", "long-island", "brooklyn", "5163465778", CHILD),
    "suffolk-county":     (("Suffolk",), "child", "long-island", "brooklyn", "6314072884", CHILD),
    "westchester-county": (("Westchester",), "child", "hudson-valley", "bronx", "9148772578", CHILD),
    "rockland-county":    (("Rockland",), "child", "hudson-valley", "bronx", "8456403835", CHILD),
    "orange-county":      (("Orange County", "Orange"), "child", "hudson-valley", "bronx", "8456403835", CHILD),
    "putnam-county":      (("Putnam",), "child", "hudson-valley", "bronx", "8456403835", CHILD),
    "dutchess-county":    (("Dutchess",), "child", "hudson-valley", "bronx", "8456403835", CHILD),
    "ulster-county":      (("Ulster",), "child", "hudson-valley", "bronx", "8456403835", CHILD),
}
BOROUGHS = ("staten-island", "manhattan", "brooklyn", "queens", "bronx")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
        self.metas = {}                 # og:* / twitter:* / other named metas -> [contents]
        self._seen_h1 = False
        self.p_after_h1 = []            # first visible <p> texts after the H1 (answer-first check)

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
        if tag == "meta" and (a.get("property") or a.get("name")):
            self.metas.setdefault((a.get("property") or a.get("name")).lower(), []).append(a.get("content", ""))
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
                else "heading" if tag in ("h2", "h3", "summary")
                else "p_after" if tag == "p" and self._seen_h1 and len(self.p_after_h1) < 6 and not self._hidden()
                else None)
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
        elif tag == "h1":
            self._seen_h1 = True
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
                    {"faq_q": self.faq_q, "faq_a": self.faq_a, "heading": self.headings,
                     "p_after": self.p_after_h1}[c[0]].append(value)

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


def shingle_set(text, n=8):
    w = re.findall(r"[a-z0-9']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


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
    # Nov 26 2026: the two root board guides (PAGE-QUEUE "NYC hub", up /) carry no area suffix
    if slug in ("co-op-board-intercom-upgrade", "condo-intercom-replacement"):
        return slug, "nyc"
    for suffix in sorted(AREAS, key=len, reverse=True):
        if slug.endswith("-" + suffix):
            return slug[: -len(suffix) - 1], suffix
    for suffix in sorted(AREAS, key=len, reverse=True):
        # silos that name counties without "-county" (dvr-upgrade-putnam, dvr-upgrade-orange)
        if suffix.endswith("-county") and slug.endswith("-" + suffix[:-7]):
            return slug[: -len(suffix[:-7]) - 1], suffix
    if slug.endswith("-ny"):
        # county/hub area pages of the older "-ny" silos (door-buzzer-installation-ulster-county-ny);
        # borough suffixes stay with the neighbourhood rule below, so nothing else changes
        base = slug[:-3]
        for suffix in sorted(AREAS, key=len, reverse=True):
            if suffix not in BOROUGHS and base.endswith("-" + suffix):
                return base[: -len(suffix) - 1], suffix
    m = re.match(r"^(.*)-(" + "|".join(BOROUGHS) + r")-ny$", slug)
    if m:
        # silo = the longest prefix that has a live borough page (multi-word silos like
        # soundbar-installation); falls back to the shortest prefix (legacy behaviour)
        parts, borough = m.group(1).split("-"), m.group(2)
        for i in range(len(parts) - 1, 0, -1):
            cand = "-".join(parts[:i])
            if os.path.isfile(os.path.join(REPO_ROOT, f"{cand}-{borough}.html")):
                return cand, borough
            # silos whose borough hubs are named <silo>-<borough>-new-york (door-buzzer-repair)
            if os.path.isfile(os.path.join(REPO_ROOT, f"{cand}-{borough}-new-york.html")):
                return cand, borough
            # silos whose borough hubs are named <silo>-<borough>-ny (fire-alarm-installation,
            # security-camera-installation, intercom-installation Bronx) - Oct 25 2026 fix: these
            # used to fall through to the one-word prefix ("fire"), so siblings were never compared
            # Nov 15 2026: the candidate must also have a hub in another borough, otherwise a
            # neighbourhood page (…-kingsbridge-bronx-ny) is mistaken for the silo of
            # …-kingsbridge-heights-bronx-ny and no siblings get compared
            if (f"{cand}-{borough}-ny" != slug and os.path.isfile(os.path.join(REPO_ROOT, f"{cand}-{borough}-ny.html"))
                    and any(os.path.isfile(os.path.join(REPO_ROOT, f"{cand}-{b}{sfx}.html"))
                            for b in BOROUGHS if b != borough for sfx in ("-ny", "-new-york", ""))):
                return cand, borough
        # the borough hub itself (<silo>-<borough>-ny), recognised by a sibling hub in another borough
        base = m.group(1)
        if any(os.path.isfile(os.path.join(REPO_ROOT, f"{base}-{b}{sfx}.html"))
               for b in BOROUGHS if b != borough for sfx in ("-ny", "-new-york", "")):
            return base, borough
        return parts[0], borough
    # Nov 15 2026: older silos also use a "-new-york" suffix (fire-alarm-installation-queens-new-york,
    # -westchester-county-new-york) and duplicate NYC hubs named <silo>-new-york / <silo>-ny.
    # Only slugs that fell through everything above reach this, so nothing already identified changes.
    if slug.endswith("-new-york"):
        s, a = identify(slug[:-9] + "-ny")
        if a:
            return s, a
    for sfx in ("-new-york", "-ny"):
        if slug.endswith(sfx):
            base = slug[: -len(sfx)]
            if os.path.isfile(os.path.join(REPO_ROOT, f"{base}-nyc.html")):
                return base, "nyc"
    return None, None


def area_slug(silo, area, root=None):
    """Slug of a silo's area/hub page: <silo>-<area>, or <silo>-<area>-ny for the older -ny silos."""
    base = f"{silo}-{area}"
    cands = [base, base + "-ny", base + "-new-york"]
    if area.endswith("-county"):
        cands.append(f"{silo}-{area[:-7]}")
    for c in cands:
        if os.path.isfile(os.path.join(root or REPO_ROOT, c + ".html")):
            return c
    return base


def is_neighbourhood(slug):
    return bool(re.match(r"^.*-(" + "|".join(BOROUGHS) + r")-ny$", slug))


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


_TRACKED = {}


def tracked_files(root):
    """Every file git tracks under root. A slim (sparse) checkout - the page runner skips the
    photo folders - still counts a tracked file as existing even when it isn't on disk."""
    if root not in _TRACKED:
        import subprocess
        try:
            out = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True,
                                 check=True).stdout.decode("utf-8", "replace")
            _TRACKED[root] = set(filter(None, out.split("\0")))
        except (OSError, subprocess.CalledProcessError):
            _TRACKED[root] = set()
    return _TRACKED[root]


def resolves(root, href):
    """Internal link target exists as a file, a .html page, or a folder index."""
    path = href.split("#", 1)[0].split("?", 1)[0]
    if path in ("", "/"):
        return True
    local = os.path.join(root, path.lstrip("/").replace("/", os.sep))
    if (os.path.isfile(local) or os.path.isfile(local + ".html")
            or os.path.isfile(os.path.join(local, "index.html"))):
        return True
    rel = path.lstrip("/")
    t = tracked_files(root)
    return rel in t or rel + ".html" in t or rel.rstrip("/") + "/index.html" in t


# ------------------------------------------------------------------ checks

# ------------------------------------------------------------------ AI-search items (Anwar, Nov 19 2026)
# From the Nov 19 2026 audit: ChatGPT read 30+ Brooklyn pages but named us in 2 of 25 answers,
# Google AI Mode in 0 of 25. Every NEW page and every REBUILD must carry: answer-first sentence
# with the area's starting price, Service (provider/areaServed/offers) + BreadcrumbList schema,
# a visible "Last updated" date = schema dateModified, and Open Graph + Twitter tags.
# Prices come ONLY from the area's price page (or a price Anwar set in START_PRICES).

NO_PRICE_SILOS = ("fire-alarm",)      # BLUEPRINT Hard Rule 13: no prices, no price schema
# silo -> price-page prefix; the page is <prefix>-<area>.html and its starting price is the lowest
# "price" in its MODELS list. Hub pages start at the lowest price of their child areas.
PRICE_PAGES = {
    "security-camera-installation": "security-camera-pricing",
    "cctv-installation": "security-camera-pricing",       # DAILY-RUN: same prices as the camera pages
    "condo-security-camera-installation": "security-camera-pricing",  # Nov 25 2026: camera-by-audience silo, area camera prices
    "co-op-security-camera-installation": "security-camera-pricing",  # Nov 25 2026: camera-by-audience silo, area camera prices
}
# Services with no price page: {silo: {area: starting price}} - ONLY numbers Anwar has set.
# Nov 25 2026 (Anwar): the co-op / condo / property-management / apartment-building audience hubs,
# the two board guides and every intercom / access-control brand page start at the $250 service call
# that's already on /intercom-pricing and /door-buzzer-repair-pricing (repairs start with a $250 service
# call; new systems are quoted after the free on-site assessment). Same in every area.
_SERVICE_CALL_SILOS = (
    "co-op-security-systems", "condo-security-systems", "property-management-security",
    "apartment-building-security-systems", "co-op-board-intercom-upgrade", "condo-intercom-replacement",
    "butterflymx-installation", "comelit-intercom", "aiphone-intercom", "akuvox-intercom",
    "avigilon-intercom", "2n-intercom", "doorbird-intercom", "siedle-intercom",
    "swiftlane-access-control", "brivo-access-control", "unifi-access-control",
)
START_PRICES = {s: {a: 250 for a in (
    "nyc", "manhattan", "brooklyn", "queens", "bronx", "staten-island", "long-island", "hudson-valley",
    "nassau-county", "suffolk-county", "westchester-county", "rockland-county", "orange-county",
    "putnam-county", "dutchess-county", "ulster-county")} for s in _SERVICE_CALL_SILOS}
# Starting prices Anwar set that the price page doesn't show yet. They win over the price page.
#   Brooklyn $950 (Anwar, Nov 19 2026). security-camera-pricing-brooklyn.html still starts at $850
#   (A Series) until he decides on the A Series. Remove this line once that page starts at $950.
PRICE_PAGE_OVERRIDES = {"security-camera-pricing-brooklyn": 950}
TZ_NAME = "America/New_York"


def _models_min(path):
    key = os.path.basename(path)[:-5] if path.endswith(".html") else path
    if key in PRICE_PAGE_OVERRIDES:
        return PRICE_PAGE_OVERRIDES[key]
    try:
        raw = open(path, encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r"var\s+MODELS\s*=\s*(\[.*?\]);", raw, re.S)
    if not m:
        return None
    try:
        prices = [x.get("price") for x in json.loads(m.group(1)) if isinstance(x, dict)]
    except ValueError:
        return None
    prices = [int(p) for p in prices if isinstance(p, (int, float)) and p > 0]
    return min(prices) if prices else None


def start_price(root, silo, area):
    """(price, source) or (None, reason). Never guesses a number."""
    if silo in START_PRICES and area in START_PRICES[silo]:
        return int(START_PRICES[silo][area]), "START_PRICES (set by Anwar)"
    prefix = PRICE_PAGES.get(silo)
    if not prefix:
        return None, (f"no price page is mapped for silo '{silo}' - get the starting price from Anwar "
                      f"and add it to START_PRICES (or map its price page in PRICE_PAGES)")
    if AREAS[area][1] == "hub":
        kids = [(a, _models_min(os.path.join(root, f"{prefix}-{a}.html")))
                for a, v in AREAS.items() if v[2] == area]
        vals = [v for _, v in kids if v]
        if not vals:
            return None, f"no readable child price pages for hub {prefix}-{area}"
        return min(vals), f"lowest of the {area} area price pages ({prefix}-*)"
    v = _models_min(os.path.join(root, f"{prefix}-{area}.html"))
    if v is None:
        return None, f"can't read a starting price from {prefix}-{area}.html (no MODELS list)"
    return v, f"/{prefix}-{area}"


def money(n):
    return f"${n:,}"


def _texts(v):
    if isinstance(v, str):
        return [v]
    if isinstance(v, dict):
        return [x for k in ("name", "@id", "address") for x in _texts(v.get(k, ""))]
    if isinstance(v, list):
        return [x for i in v for x in _texts(i)]
    return []


def _is_modified(root, path):
    import subprocess
    rel = os.path.relpath(path, root)
    try:
        tracked = subprocess.run(["git", "-C", root, "ls-files", "--error-unmatch", rel],
                                 capture_output=True).returncode == 0
        if not tracked:
            return True
        return subprocess.run(["git", "-C", root, "diff", "--quiet", "HEAD", "--", rel],
                              capture_output=True).returncode != 0
    except OSError:
        return False


def check_ai_search(root, slug, silo, area, kind, page, nodes, local, text, path, fail):
    import datetime
    try:
        from zoneinfo import ZoneInfo
        today = datetime.datetime.now(ZoneInfo(TZ_NAME)).date()
    except Exception:
        today = datetime.date.today()
    aliases = AREAS[area][0]
    if is_neighbourhood(slug) and slug.startswith(silo + "-"):
        # neighbourhood pages name the neighbourhood (Canarsie), the borough name also counts
        nb = re.sub(r"-(%s)-ny$" % "|".join(BOROUGHS), "", slug[len(silo) + 1:]).replace("-", " ")
        aliases = tuple(aliases) + (nb,)
    canonical = f"{DOMAIN}/{slug}"
    priced = not silo.startswith(NO_PRICE_SILOS)
    price, source = start_price(root, silo, area) if priced else (None, "")
    if priced and price is None:
        fail(f"starting price unknown: {source}")
    service_words = silo.replace("-", " ").lower()

    # 1. answer first: first sentence under the H1 = service + area + starting price
    # the hero kicker/tag line ("DVR · NVR · PoE") is not a sentence - skip it
    paras = [p for p in page.p_after_h1 if len(p.split()) >= 8 and "·" not in p and re.search(r"[.!?]", p)]
    if not paras:
        fail("answer-first: no sentence under the H1 (hero subhead) to check")
    else:
        first = re.split(r"(?<=[.!?])\s+", paras[0], maxsplit=1)[0]
        low = first.lower()
        if service_words not in low:
            fail(f"answer-first: first sentence under the H1 doesn't name the service ({service_words!r}): {first[:110]!r}")
        if not any(a.lower() in low for a in aliases):
            fail(f"answer-first: first sentence under the H1 doesn't name the area ({'/'.join(aliases)}): {first[:110]!r}")
        if priced and price:
            amounts = [int(x.replace(",", "")) for x in re.findall(r"\$(\d[\d,]*)", first)]
            if price not in amounts:
                fail(f"answer-first: first sentence must give the starting price {money(price)} from {source}: {first[:110]!r}")

    # 2. Service schema: provider = LocalBusiness, areaServed = this area, offers = starting price
    services = [n for n in nodes if "Service" in types_of(n)]
    local_ids = {str(n.get("@id")) for n in local if n.get("@id")}
    if services:
        sv = services[0]
        prov = sv.get("provider")
        provs = prov if isinstance(prov, list) else [prov]
        if not any(isinstance(p, dict) and (str(p.get("@id")) in local_ids or types_of(p) & {
                "LocalBusiness", "HomeAndConstructionBusiness", "Electrician", "ProfessionalService"}) for p in provs):
            fail("Service schema: provider must be the page's LocalBusiness (its @id or a LocalBusiness node)")
        if not any(a.lower() in " ".join(_texts(sv.get("areaServed"))).lower() for a in aliases):
            fail(f"Service schema: areaServed must name the page's area ({'/'.join(aliases)})")
        offers = sv.get("offers")
        offers = offers if isinstance(offers, list) else [offers] if isinstance(offers, dict) else []
        if priced:
            got = []
            for o in offers:
                for key in ("price", "lowPrice"):
                    try:
                        got.append(int(float(str(o.get(key)).replace(",", ""))))
                    except (TypeError, ValueError):
                        pass
                spec = o.get("priceSpecification")
                if isinstance(spec, dict):
                    try:
                        got.append(int(float(str(spec.get("price")))))
                    except (TypeError, ValueError):
                        pass
            if not offers:
                fail("Service schema: no offers (Offer with the area's starting price)")
            elif price and price not in got:
                fail(f"Service schema: offers price {got or 'missing'} must be the starting price {money(price)} from {source}")
            elif not any(str(o.get("priceCurrency", (o.get("priceSpecification") or {}).get("priceCurrency", ""))) == "USD"
                         for o in offers if isinstance(o, dict)):
                fail("Service schema: offers needs priceCurrency USD")
        elif any("price" in json.dumps(o) for o in offers):
            fail("Service schema: offers carries a price on a no-price (fire alarm) page - Hard Rule 13")

    # 3. BreadcrumbList: Home > hub > borough/county > page
    crumbs = [n for n in nodes if "BreadcrumbList" in types_of(n)]
    if crumbs:
        items = [i for i in crumbs[0].get("itemListElement") or [] if isinstance(i, dict)]
        items.sort(key=lambda i: int(i.get("position") or 0))
        if [int(i.get("position") or 0) for i in items] != list(range(1, len(items) + 1)):
            fail("BreadcrumbList: positions must run 1, 2, 3 ... with no gaps")
        urls = []
        for i in items:
            it = i.get("item")
            urls.append((it.get("@id") if isinstance(it, dict) else it) or "")
        want = [f"{DOMAIN}/"]
        if kind == "child" or is_neighbourhood(slug):
            want.append(f"{DOMAIN}/{area_slug(silo, AREAS[area][2] or area, root)}")
        if is_neighbourhood(slug):
            want.append(f"{DOMAIN}/{area_slug(silo, area, root)}")
        want.append(canonical)
        if urls != want:
            fail(f"BreadcrumbList must be {' > '.join(w.replace(DOMAIN, '') or '/' for w in want)} "
                 f"(found {' > '.join(u.replace(DOMAIN, '') or '/' for u in urls) or 'nothing'})")

    # 4. visible "Last updated" date = schema dateModified, refreshed when the page changes
    m = re.search(r"Last updated:?\s+([A-Z][a-z]+ \d{1,2}, \d{4})", text)
    shown = None
    if not m:
        fail('no visible "Last updated <Month D, YYYY>" date')
    else:
        try:
            shown = datetime.datetime.strptime(m.group(1), "%B %d, %Y").date()
        except ValueError:
            fail(f'"Last updated" date is not a real date: {m.group(1)!r}')
    mods = sorted({str(n["dateModified"])[:10] for n in nodes if n.get("dateModified")})
    if not mods:
        fail("no dateModified in schema")
    elif len(mods) > 1:
        fail(f"schema dateModified values disagree: {', '.join(mods)}")
    elif shown and mods[0] != shown.isoformat():
        fail(f'visible "Last updated" {shown.isoformat()} != schema dateModified {mods[0]}')
    if mods and len(mods) == 1:
        if mods[0] > today.isoformat():
            fail(f"dateModified {mods[0]} is in the future")
        elif _is_modified(root, path) and mods[0] != today.isoformat():
            fail(f"page changed but dateModified is {mods[0]} - refresh it and the visible date to {today.isoformat()}")

    # 5. Open Graph + Twitter
    meta = {k: v for k, v in page.metas.items()}
    for k in ("og:title", "og:description", "og:url", "og:image", "og:type",
              "twitter:card", "twitter:title", "twitter:description", "twitter:image"):
        vals = [v for v in meta.get(k, []) if v.strip()]
        if not vals:
            fail(f"missing <meta> {k}")
        elif len(meta.get(k, [])) > 1:
            fail(f"{len(meta[k])} <meta> {k} tags (exactly one)")
    if meta.get("og:url") and meta["og:url"][0] != canonical:
        fail(f"og:url {meta['og:url'][0]} != canonical {canonical}")
    if meta.get("og:type") and meta["og:type"][0] != "website":
        fail(f"og:type is {meta['og:type'][0]!r} (required 'website')")
    page_imgs = {local_path(i["src"]) or i["src"] for i in page.images}
    for k in ("og:image", "twitter:image"):
        if meta.get(k):
            u = meta[k][0]
            lp = local_path(u) if not u.startswith(DOMAIN) else u[len(DOMAIN):]
            if not lp or not resolves(root, lp):
                fail(f"{k} doesn't resolve to an image file in the repo: {u}")
            elif lp not in page_imgs:
                fail(f"{k} must be the hero job photo used on the page (not found among page images): {u}")

    # 6. prices match the price page: no "from / starts at $X" below the area's starting price
    if priced and price:
        blobs = [text, page.title, page.meta_description or ""] + [v for k in (
            "og:title", "og:description", "twitter:title", "twitter:description") for v in meta.get(k, [])]
        for b in blobs:
            for x in re.findall(r"(?i)(?:\bstart(?:s|ing)?(?:\s+at)?|\bfrom)\s+(?:just\s+|only\s+)?\$(\d[\d,]*)", b):
                n = int(x.replace(",", ""))
                if n < price:
                    fail(f"price {money(n)} is below the starting price {money(price)} on {source} - prices must match the price page")


def check(root, slug, registration=True, stats=False, ai_search=True):
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
    # Form placeholder attributes like "(555) 123-4567" are fine; a 555 number in text or a link is not.
    if re.search(r"\b555[-. ]\d{4}\b|\(555\)", text) or any("555" in digits(h) for h in page.hrefs
                                                          if h.lower().startswith("tel:")):
        fail("placeholder 555 phone number in text or a tel: link")

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
        # LIVE CONVENTION: the footer shows "WhatsApp (718) 679-0359" as text (never tel-linked).
        if d == WHATSAPP:
            continue
        if d in COMPANY_PHONES and d not in allowed:
            fail(f"visible phone {fmt(d)} is not approved for {area}")

    # --- rating, license, warranty
    if not re.search(r"4\.7\s*(?:/|·|★|out of 5)?[^0-9]{0,25}201", text):
        fail("rating 4.7 / 201 not shown in visible text")
    if LICENSE not in text:
        fail(f"NYS license #{LICENSE} not shown")
    if norm_space(WARRANTY) not in text:
        fail("exact warranty text missing or altered (see WARRANTY in tools/check_page.py)")
    # Anwar, Nov 14 2026: "No AESS" — never the abbreviation in published text, titles, alt text or schema
    _pub = re.sub(r'(?is)<script(?![^>]*ld\+json)[^>]*>.*?</script>|<style.*?</style>|<input[^>]*type="hidden"[^>]*>|(?:href|src)="[^"]*"', ' ', raw)
    if re.search(r"\bAESS\b", _pub):
        fail('"AESS" appears on the page — write "Abstract Enterprises Security Systems" (BLUEPRINT rule 12)')
    if re.search(r"three-year warranty", text, re.I):
        fail("page states a three-year warranty; live convention is the one-year parts-only terms sentence")

    # --- forms
    # Forms post to /api/contact (spam gate in netlify/functions/contact.mjs),
    # which forwards real leads to Web3Forms. Never post straight to Web3Forms.
    if any("web3forms.com" in f["attrs"].get("action", "") for f in page.forms) or "api.web3forms.com/submit" in raw:
        fail("form posts straight to Web3Forms; use /api/contact (spam gate)")
    forms = [f for f in page.forms if f["attrs"].get("action", "") == "/api/contact"]
    if len(forms) != 2:
        fail(f"{len(forms)} /api/contact forms (hero + detail required)")
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

    # --- AI-search items (Nov 19 2026): answer first, Service/Breadcrumb detail, Last updated, OG/Twitter, prices
    if ai_search:
        check_ai_search(root, slug, silo, area, kind, page, nodes, local, text, path, fail)

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

    # --- host: every absolute self-link must use https://www. (non-www makes Google crawl/canonicalise the wrong host)
    raw = open(path, encoding="utf-8").read()
    for bad in sorted(set(re.findall(r"https?://abstractenterprisessecuritysystems\.com[^\"'\s<>]*", raw)))[:5]:
        fail(f"non-www self URL (use https://www.abstractenterprisessecuritysystems.com): {bad}")

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
    mine = None
    for sib in siblings:
        sslug = os.path.basename(sib)[:-5]
        ssize = os.path.getsize(sib)
        sp, _ = parse(sib)
        if abs(ssize - size) <= SIZE_CLUSTER_BYTES:
            mine = mine if mine is not None else shingle_set(visible_text(page))
            share = len(mine & shingle_set(visible_text(sp))) / max(len(mine), 1)
            if share >= CLONE_TEXT_SHARE:
                fail(f"file size {size:,} B is within 2 KB of sibling {sslug} ({ssize:,} B) and shares "
                     f"{share:.0%} of its wording - clone signature")
        for q in sp.faq_q + [h for h in sp.headings if h.endswith("?")]:
            if mask(q) in my_q:
                fail(f"question duplicated on sibling {sslug}: {my_q[mask(q)][:90]!r}")
        for a in sp.faq_a:
            if mask(a) in my_a:
                fail(f"FAQ answer duplicated on sibling {sslug}: {my_a[mask(a)][:70]!r}")
        s_silo, s_area = identify(sslug)
        if s_area in AREAS and sslug == area_slug(silo, s_area, root):         # area pages cross-link each other
            if f"/{sslug}" not in hrefs:
                fail(f"no cross-link to live sibling /{sslug}")
            if f"/{slug}" not in link_set(sp.hrefs):
                fail(f"live sibling {sslug} doesn't link back to /{slug}")

    # --- hub and spoke
    if is_neighbourhood(slug):                       # neighbourhood spoke: up-link = its borough page
        parent = area
    if kind == "child":
        up = f"/{area_slug(silo, parent, root)}"
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
            hub = os.path.join(root, area_slug(silo, parent, root) + ".html")
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
    ap.add_argument("--legacy", action="store_true",
                    help="skip the Nov 19 2026 AI-search checks - ONLY for small edits (title/meta/link tweaks) to a "
                         "page not yet rebuilt; never for a new page or a rebuild")
    args = ap.parse_args()
    slug = os.path.basename(args.page)
    slug = slug[:-5] if slug.endswith(".html") else slug
    fails, info = check(args.root, slug, registration=not args.no_registration, ai_search=not args.legacy)
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
