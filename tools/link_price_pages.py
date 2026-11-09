#!/usr/bin/env python3
"""Brand price pages are "sticky" pages: the full-blueprint brand page ranks, and its
price list (calculator) is one click away. Anwar, Nov 2 2026.

  <brand>-camera-installation-<area>          main page (full blueprint, ranks)
  <brand>-camera-installation-prices-<area>   sticky price page (same area, links back up)

This script is idempotent. Run it after any build (the page factory runs it every cycle).
  1. Every price page gets an "up" link to its brand main page for the same area.
     Brooklyn stays in Brooklyn. If that page isn't built yet, it falls back to the brand hub
     (NYC / Long Island / Hudson Valley), then to the general security camera page for the area.
  2. Every brand main page gets a "<Brand> prices in <Area>" button that points to its price
     page. It is added to the sticky bar when the page has one, and also as an in-page link.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_page as c  # noqa: E402

A0, A1 = "<!-- price-up:start -->", "<!-- price-up:end -->"
B0, B1 = "<!-- brand-prices:start -->", "<!-- brand-prices:end -->"
AREA_NAME = {"nyc": "NYC", "manhattan": "Manhattan", "brooklyn": "Brooklyn", "queens": "Queens",
             "bronx": "the Bronx", "staten-island": "Staten Island", "long-island": "Long Island",
             "hudson-valley": "the Hudson Valley", "nassau-county": "Nassau County",
             "suffolk-county": "Suffolk County", "westchester-county": "Westchester County",
             "rockland-county": "Rockland County", "orange-county": "Orange County",
             "putnam-county": "Putnam County", "dutchess-county": "Dutchess County",
             "ulster-county": "Ulster County"}


def exists(slug):
    return os.path.isfile(os.path.join(ROOT, slug + ".html"))


def brand_name(html, brand):
    m = re.search(r"<h1>(.*?) camera installation prices", html, re.S | re.I)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else brand.replace("-", " ").title()


def generic(area):
    for s in (f"security-camera-installation-{area}-ny", f"security-camera-installation-{area}"):
        if exists(s):
            return s
    return "security-camera-installation-nyc"


def splice(html, start, end, block, anchor_re, after=True):
    html = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", html, flags=re.S)
    m = re.search(anchor_re, html, re.S)
    if not m:
        return None
    i = m.end() if after else m.start()
    return html[:i] + start + block + end + "\n" + html[i:]


def main():
    changed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*-camera-installation-prices-*.html"))):
        slug = os.path.basename(path)[:-5]
        brand, _, area = slug.partition("-camera-installation-prices-")
        if area not in c.AREAS:
            continue
        html = open(path, encoding="utf-8").read()
        name = brand_name(html, brand)
        hub = c.AREAS[area][2] or area
        main_slug = f"{brand}-camera-installation-{area}"
        target = next((s for s in (main_slug, f"{brand}-camera-installation-{hub}") if exists(s)), None)
        label = f"{name} camera installation in {AREA_NAME[area]}"
        if not target:
            target, label = generic(area), f"Security camera installation in {AREA_NAME[area]}"
        block = (f'<p class="price-up" style="margin:.6rem 0 0;font-weight:700">'
                 f'<a href="/{target}">&larr; {label}</a></p>')
        new = splice(html, A0, A1, block, r"<section class=\"hero\"><h1>.*?</h1>")
        if new and new != html:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1

        # the brand main page for this area points down to this price page
        if exists(main_slug):
            mp = os.path.join(ROOT, main_slug + ".html")
            mh = open(mp, encoding="utf-8").read()
            btn = (f'<p class="brand-prices" style="margin:1rem 0;font-weight:800">'
                   f'<a href="/{slug}">See every {name} camera price in {AREA_NAME[area]} '
                   f'and build your own system &rarr;</a></p>'
                   f'<script>window.addEventListener("load",function(){{setTimeout(function(){{var t=document.getElementById("spbLabelText");'
                   f'if(t)t.textContent="{name} prices";var c=document.getElementById("spbCta");'
                   f'if(c){{var a=document.createElement("a");a.href="/{slug}";'
                   f'a.textContent="{name} price list";a.className="spb-brand-prices";'
                   f'c.insertBefore(a,c.firstChild);}}}},300);}});</script>')
            nm = splice(mh, B0, B1, btn, r"</h1>")
            if nm and nm != mh:
                open(mp, "w", encoding="utf-8").write(nm)
                changed += 1
    # brand neighborhood pages (<brand>-camera-installation-<nbhd>-<borough>-ny) use their
    # borough's price page: one Brooklyn price page covers every Brooklyn neighborhood.
    for path in sorted(glob.glob(os.path.join(ROOT, "*-camera-installation-*-ny.html"))):
        slug = os.path.basename(path)[:-5]
        m = re.match(r"^(.+?)-camera-installation-(.+)-(" + "|".join(c.BOROUGHS) + r")-ny$", slug)
        if not m or "-prices-" in slug:
            continue
        brand, nb, borough = m.groups()
        price = f"{brand}-camera-installation-prices-{borough}"
        if not exists(price) or not exists(f"{brand}-camera-installation-{borough}"):
            continue          # only true brand silos, not "security-camera-installation-..." pages
        ph = open(path, encoding="utf-8").read()
        pname = brand_name(open(os.path.join(ROOT, price + ".html"), encoding="utf-8").read(), brand)
        nbname = nb.replace("-", " ").title()
        btn = (f'<p class="brand-prices" style="margin:1rem 0;font-weight:800">'
               f'<a href="/{price}">{pname} camera prices for {nbname} and all of {AREA_NAME[borough]} '
               f'&ndash; build your own system &rarr;</a></p>')
        nh = splice(ph, B0, B1, btn, r"</h1>")
        if nh and nh != ph:
            open(path, "w", encoding="utf-8").write(nh)
            changed += 1
    print(f"link_price_pages: {changed} files updated")
    return changed


if __name__ == "__main__":
    main()
