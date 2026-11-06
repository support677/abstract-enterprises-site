#!/usr/bin/env python3
"""Put each rendered hero video into its page. Usage: python inject.py results_dir
Videos are referenced on our own domain under /v/ (Netlify forwards /v/* to Cloudflare R2)."""
import glob, json, os, sys, re, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pages

D = os.path.dirname(os.path.abspath(__file__))
SITE = os.environ.get("AESS_SITE", os.path.abspath(os.path.join(D, "..", "..")))
DOM = "https://www.abstractenterprisessecuritysystems.com"
TODAY = os.environ.get("HV_DATE", "2026-11-06")
done = 0
for rf in sorted(glob.glob(os.path.join(sys.argv[1], "*.json"))):
    for r in json.load(open(rf))["ok"]:
        if r.get("v") != 2:          # results from the first (pre-fix) script are not put in pages
            continue
        p = os.path.join(SITE, r["slug"] + ".html")
        s = open(p, encoding="utf-8").read()
        if 'data-hero-video="' in s:
            continue
        mp4, jpg = f"/v/hero/{r['slug']}.mp4", f"/v/hero/{r['slug']}.jpg"
        im = pages.hero_img(s)
        if im:
            tag = s[im[0]:im[1]]
            s = s[:im[0]] + f'<div class="hv-box" data-hero-video="{mp4}">{tag}</div>' + s[im[1]:]
        else:
            sp = pages.hero_span(s)
            if not sp:
                continue
            alt = html.escape(f"{r['service']} in {r['place']} - Abstract Enterprises Security Systems video", quote=True)
            box = (f'<div class="hv-box" data-hero-video="{mp4}" style="max-width:760px;margin:36px auto 0;border-radius:14px;'
                   f'overflow:hidden;box-shadow:0 18px 50px rgba(0,0,0,.35)"><img src="{jpg}" alt="{alt}" width="1280" '
                   f'height="720" loading="lazy" style="display:block;width:100%;height:auto"></div>\n')
            cut = s.rfind("</div>", sp[0], sp[1])
            cut = cut if cut > 0 else sp[1]
            s = s[:cut] + box + s[cut:]
        name = f"{r['service']} in {r['place']}".strip() if r["place"] else r["service"]
        desc = f"{r['service']} by Abstract Enterprises Security Systems" + (f" in {r['place']}" if r["place"] else "") + \
               ". Licensed and insured, 2-hour arrival windows, 25+ years in security."
        vo = {"@context": "https://schema.org", "@type": "VideoObject",
              "name": f"{name} | Abstract Enterprises Security Systems", "description": desc,
              "thumbnailUrl": [DOM + jpg], "uploadDate": TODAY + "T12:00:00-05:00",
              "duration": f"PT{int(round(r['seconds']))}S", "contentUrl": DOM + mp4, "embedUrl": DOM + "/" + r["slug"],
              "publisher": {"@type": "Organization", "name": "Abstract Enterprises Security Systems",
                            "logo": {"@type": "ImageObject", "url": DOM + "/images/logo.png"}}}
        add = '<script type="application/ld+json">' + json.dumps(vo) + "</script>\n"
        if "/js/hero-video.js" not in s:
            add += '<script src="/js/hero-video.js" defer></script>\n'
        if s.count("</head>") != 1:
            continue
        s = s.replace("</head>", add + "</head>", 1)
        open(p, "w", encoding="utf-8").write(s)
        done += 1
print("injected", done)
