"""Which pages get a hero video, and where it goes in each page."""
import glob, os, re

SKIP = {"index", "404", "about-us", "privacy-policy", "privacy", "terms", "terms-of-service", "thank-you",
        "free-quote", "contact", "contact-us", "sitemap", "blog", "careers", "reviews"}


def hero_span(s):
    m = re.search(r'<section[^>]*class="[^"]*\bhero\b[^"]*"', s) or re.search(r'<section[^>]*class="[^"]*hero[^"]*"', s)
    if not m:
        return None
    end = s.find("</section>", m.end())
    return (m.start(), end) if end > 0 else None


def hero_img(s):
    sp = hero_span(s)
    if not sp:
        return None
    for x in re.finditer(r"<img\b[^>]*>", s[sp[0]:sp[1]]):
        if "logo" not in x.group(0).lower():
            return (sp[0] + x.start(), sp[0] + x.end())
    return None


def candidates(site):
    out = []
    for f in sorted(glob.glob(os.path.join(site, "*.html"))):
        slug = os.path.basename(f)[:-5]
        if slug in SKIP or slug.startswith(("thank", "test")):
            continue
        s = open(f, encoding="utf-8", errors="ignore").read()
        if "<h1" not in s or 'data-hero-video="' in s or not hero_span(s):
            continue
        out.append(slug)
    return out
