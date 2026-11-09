"""Which pages get a hero video, and where it goes in each page."""
import glob, os, re

# Policy, form and tool pages get no video. The homepage does (Nov 6 2026).
SKIP = {"404", "about-us", "privacy-policy", "privacy", "terms", "terms-of-service", "terms-and-conditions", "thank-you",
        "free-quote", "contact", "contact-us", "sitemap", "blog", "careers", "reviews", "generate-invoice", "sms-consent",
        "tv-installation-policies", "build-cabling-system"}


def hero_span(s):
    """The page's hero block: <section> or <header> whose class contains 'hero', up to its closing tag."""
    m = re.search(r'<(section|header)\b[^>]*class="[^"]*\bhero\b[^"]*"', s) or \
        re.search(r'<(section|header)\b[^>]*class="[^"]*hero[^"]*"', s)
    if not m:
        return None
    end = s.find("</%s>" % m.group(1), m.end())
    return (m.start(), end) if end > 0 else None


def _heading(s):
    return re.search(r"<h1\b[^>]*>.*?</h1>", s, re.S | re.I) or re.search(r"<h2\b[^>]*>.*?</h2>", s, re.S | re.I)


def hero_img(s):
    sp = hero_span(s)
    if not sp:   # no hero block: a photo sitting right under the page heading counts as the hero photo
        h = _heading(s)
        if not h:
            return None
        nxt = re.search(r"<h[1-3]\b", s[h.end():])
        sp = (h.end(), h.end() + min(nxt.start() if nxt else 2500, 2500))
    for x in re.finditer(r"<img\b[^>]*>", s[sp[0]:sp[1]]):
        if "logo" not in x.group(0).lower():
            return (sp[0] + x.start(), sp[0] + x.end())
    return None


def insert_point(s):
    """Where a video box goes on a page whose hero has no photo to swap."""
    sp = hero_span(s)
    if sp:
        cut = s.rfind("</div>", sp[0], sp[1])
        return cut if cut > 0 else sp[1]
    h = _heading(s)
    if not h:
        return None
    p = s.find("</p>", h.end(), h.end() + 1500)
    return p + 4 if p > 0 else h.end()


def candidates(site, force=False):
    out = []
    for f in sorted(glob.glob(os.path.join(site, "*.html"))):
        slug = os.path.basename(f)[:-5]
        if slug in SKIP or slug.startswith(("thank", "test", "google")):
            continue
        s = open(f, encoding="utf-8", errors="ignore").read()
        if (not force and 'data-hero-video="' in s) or insert_point(s) is None:
            continue
        out.append(slug)
    return out
