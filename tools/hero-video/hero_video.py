#!/usr/bin/env python3
"""AESS website hero video (16:9 kinetic type + voiceover), built from a page's own content.

Asked for by Anwar Nov 5 2026: every page on the site gets a kinetic video at the top instead of
the hero photo, autoplaying, talking about that page's service in that page's area.

Usage:  python3 hero_video.py <site>/<page>.html [outdir]
Writes  <outdir>/<slug>.mp4 and <outdir>/<slug>.jpg (poster) plus <slug>.json (script + metadata).

Everything on screen and in the narration comes from the page itself (H1, area, hero price line,
phone, the page's own photos) or from fixed AESS facts (licensed & insured, 25+ years, 2-hour
arrival windows, open 7 days 8 AM-8 PM). Nothing is invented: no price shows unless the page
already states it.
"""
import html as H_, json, os, re, subprocess, sys, wave, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
import aess_promo as A

W, H, FPS = 1280, 720, 30
A.W, A.H = W, H                      # the shared helpers read these module globals
from aess_promo import BLACK, BLUE, NAVY, WHITE, SKY, F_BLACK, F_BOLD, LOGO, place, slam, prog, e_out, e_back, clamp

SITE = os.environ.get("AESS_SITE", os.path.abspath(os.path.join(D, "..", "..")))
KOKORO = os.environ.get("KOKORO_DIR", os.path.expanduser("~/kokoro"))
VOICE = os.environ.get("AESS_VOICE", "am_michael")
SR = 24000

AREA_WORDS = [  # (slug fragment, display, spoken)
    ("staten-island", "STATEN ISLAND", "Staten Island"), ("brooklyn", "BROOKLYN", "Brooklyn"),
    ("queens", "QUEENS", "Queens"), ("bronx", "THE BRONX", "the Bronx"), ("manhattan", "MANHATTAN", "Manhattan"),
    ("nassau", "NASSAU COUNTY", "Nassau County"), ("suffolk", "SUFFOLK COUNTY", "Suffolk County"),
    ("long-island", "LONG ISLAND", "Long Island"), ("westchester", "WESTCHESTER", "Westchester"),
    ("rockland", "ROCKLAND COUNTY", "Rockland County"), ("orange", "ORANGE COUNTY", "Orange County"),
    ("putnam", "PUTNAM COUNTY", "Putnam County"), ("dutchess", "DUTCHESS COUNTY", "Dutchess County"),
    ("ulster", "ULSTER COUNTY", "Ulster County"), ("hudson-valley", "THE HUDSON VALLEY", "the Hudson Valley"),
    ("nyc", "NEW YORK CITY", "New York City"),
]

# Problem / promise scene per service family (first match on the slug wins)
FAMILIES = [
    ("camera-repair", ["CAMERA DOWN?", "NO PICTURE?", "WE FIX IT."],
     "Camera down, no picture, or a recorder that stopped recording? We fix it."),
    ("camera-maintenance", ["CLEAN.", "TESTED.", "RECORDING."],
     "Lenses cleaned, drives checked, and every camera confirmed recording."),
    ("intercom", ["DOOR WON'T", "BUZZ?", "WE GOT IT."],
     "Buzzer dead, no audio, or a door that won't release? We take care of it."),
    ("buzzer", ["DOOR WON'T", "BUZZ?", "WE GOT IT."],
     "Buzzer dead, no audio, or a door that won't release? We take care of it."),
    ("access", ["WHO GETS IN.", "WHEN.", "YOU DECIDE."],
     "Control who gets in and when, from your phone."),
    ("mag-lock", ["LOCK IT DOWN.", "ONE BUTTON.", "DONE."],
     "Lock your door down with one button, installed and tested."),
    ("lock", ["NO MORE", "KEYS.", "JUST CODES."],
     "No more lost keys. Codes, cards and your phone."),
    ("alarm", ["IF THEY TRY,", "EVERYONE", "KNOWS."],
     "If someone tries to get in, you know, and so does the central station."),
    ("tv", ["CLEAN WALL.", "NO WIRES.", "DONE RIGHT."],
     "A clean wall, hidden wires, and a TV mounted level the first time."),
    ("cabl", ["EVERY RUN.", "TESTED.", "LABELED."],
     "Every cable run pulled, terminated, tested and labeled."),
    ("wiring", ["EVERY RUN.", "TESTED.", "LABELED."],
     "Every cable run pulled, terminated, tested and labeled."),
    ("wifi", ["DEAD ZONES?", "NOT ANYMORE.", ""],
     "Dead zones gone. Strong Wi-Fi in every room."),
    ("video-wall", ["BIG SCREENS.", "ONE PICTURE.", "ZERO GAPS."],
     "Big screens, one seamless picture, installed and calibrated."),
    ("doorbell", ["SEE WHO'S", "AT THE DOOR.", "ANYWHERE."],
     "See who is at your door from anywhere."),
    ("camera", ["NO MORE", "BLIND SPOTS.", "SEE IT ALL."],
     "No more blind spots. See everything, day and night, from your phone."),
    ("repair", ["BROKEN?", "WE FIX IT.", "FAST."],
     "If it's broken, we find the problem and fix it, usually on the first visit."),
    ("fire", ["CODE-READY.", "INSPECTED.", "PROTECTED."],
     "Installed to code and ready for inspection."),
    ("smart-home", ["ONE APP.", "EVERY ROOM.", "DONE."],
     "Lights, locks, cameras and thermostats, all in one app."),
    ("sound", ["EVERY ROOM.", "ONE TAP.", "CRYSTAL CLEAR."],
     "Music in every room, controlled with one tap."),
]
GENERIC = (["DONE RIGHT.", "THE FIRST", "TIME."], "Done right the first time, and tested before we leave.")

ONES = "zero one two three four five six seven eight nine".split()


def spoken_phone(p):
    d = re.sub(r"\D", "", p)[-10:]
    say = lambda s: " ".join("oh" if c == "0" else ONES[int(c)] for c in s)
    if d.startswith("800"):
        return f"eight hundred, {say(d[3:6])}, {say(d[6:])}"
    return f"{say(d[:3])}, {say(d[3:6])}, {say(d[6:])}"


def fmt_phone(p):
    d = re.sub(r"\D", "", p)[-10:]
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else p


def strip(s):
    return H_.unescape(re.sub(r"<[^>]+>", " ", s)).replace(" ", " ").strip()


END = {"installation", "installer", "installers", "repair", "repairs", "maintenance", "prices", "pricing", "mounting",
       "wiring", "cabling", "upgrade", "upgrades", "service", "services", "systems", "system", "monitoring",
       "replacement", "programming", "setup", "design", "inspection", "company", "contractor", "contractors",
       "installations", "installs", "install", "cost", "costs", "integration"}
UPPER = {"tv": "TV", "cctv": "CCTV", "nvr": "NVR", "dvr": "DVR", "poe": "PoE", "cat6": "Cat6", "cat5e": "Cat5e",
         "led": "LED", "lpr": "LPR", "ip": "IP", "wifi": "Wi-Fi", "zosi": "ZOSI", "ens": "ENS", "avycon": "AVYCON",
         "unv": "UNV", "adt": "ADT", "eufy": "eufy", "unifi": "UniFi", "ptz": "PTZ", "ny": "NY", "nyc": "NYC"}


def nice(words):
    return " ".join(UPPER.get(w, w.capitalize()) for w in words)


def slug_parts(slug, h1):
    t = [w for w in re.sub(r"-(ny|new-york|nys)$", "", slug).split("-") if w]
    ends = [i for i, w in enumerate(t) if w in END]
    if not ends:
        return h1, None, None
    e = ends[-1]
    svc_t, rest = t[:e + 1], t[e + 1:]
    while len(svc_t) > 1 and svc_t[-1] in ("prices", "pricing", "cost", "costs", "company", "contractor", "contractors"):
        svc_t = svc_t[:-1]
    rest_s = "-".join(rest)
    area, pos = None, -1
    for frag, disp, sp in AREA_WORDS:
        q = rest_s.rfind(frag)
        if q > pos or (q == pos and q >= 0 and area and len(frag) > len(area[0])):
            area, pos = (disp, sp), q
            cut = q
    nb = None
    if area:
        before = rest_s[:cut].strip("-")
        before = re.sub(r"-?(county|new-york|ny)$", "", before).strip("-")
        if before:
            nb = nice(before.split("-"))
    elif rest:
        nb = nice([w for w in rest if w not in ("county", "new", "york")])
    return nice(svc_t), area, nb


def parse(path):
    raw = open(path, encoding="utf-8", errors="ignore").read()
    slug = os.path.splitext(os.path.basename(path))[0]
    if slug == "index":
        slug = os.path.basename(os.path.dirname(path)) or "home"
    m = re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.S | re.I)
    h1 = re.sub(r"\s+", " ", strip(m.group(1))) if m else slug.replace("-", " ").title()
    service, area, nb = slug_parts(slug, h1)
    pm = re.search(r'class="rh-price"[^>]*>(.*?)</div>', raw, re.S)
    price = None
    if pm:
        mp = re.search(r"\$\s?([\d,]+)", strip(pm.group(1)))
        if mp:
            price = mp.group(1).replace(",", "")
    hero = raw[raw.find('class="hero'):][:12000] if 'class="hero' in raw else raw
    tel = re.search(r'href="tel:\+?1?(\d{10})"', hero) or re.search(r'href="tel:\+?1?(\d{10})"', raw)
    phone = fmt_phone(tel.group(1)) if tel else "(800) 486-0943"
    imgs = []
    for src in re.findall(r'<img[^>]+src="(/images/[^"]+)"', raw):
        if "logo" in src or src in imgs:
            continue
        p = os.path.join(SITE, src.lstrip("/"))
        if os.path.exists(p):
            imgs.append(src)
    if len(imgs) < 4:   # page is short on (working) photos: borrow the best-matching real job photos from the library
        svc_words = [w for w in service.lower().replace("-", " ").split() if len(w) > 2 and w not in
                     ("installation", "install", "repair", "service", "services", "system", "systems", "and")] or service.lower().split()
        lib = os.path.join(SITE, "images")
        seed = int(hashlib.md5(slug.encode()).hexdigest(), 16)
        scored = []
        for d in os.listdir(lib):
            dp = os.path.join(lib, d)
            if not os.path.isdir(dp) or d.startswith(("gbp", "logo")):
                continue
            for f in os.listdir(dp):
                if not f.lower().endswith((".jpg", ".jpeg", ".webp", ".png")):
                    continue
                name = (d + "-" + f).lower()
                fl = f.lower()
                if fl.startswith(d.lower() + "-"):
                    fl = fl[len(d) + 1:]
                sc_ = sum(2 for w in svc_words if w in fl) + sum(1 for w in svc_words if w in d)
                if "camera" not in " ".join(svc_words) and any(c in fl for c in ("camera", "dome", "bullet", "recorder", "nvr", "ptz")):
                    sc_ -= 4
                if sc_ > 0:
                    scored.append((sc_, (hash(name) ^ seed) & 0xffff, "/images/%s/%s" % (d, f)))
        for _, _, cand in sorted(scored, key=lambda x: (-x[0], x[1]))[:8]:
            if cand not in imgs:
                imgs.append(cand)
    lead = re.search(r'<p class="lead">(.*?)</p>', raw, re.S)
    towns = []
    if lead:
        for t in re.findall(r"\b([A-Z][a-z]+(?:[- ][A-Z][a-z]+)?)\b", strip(lead.group(1))):
            if t not in towns and t.lower() not in ("same", "most", "firm", "already", "our", "we", "no", "brooklyn",
                                                     "queens", "bronx", "manhattan", "hikvision", "dahua", "lorex",
                                                     "speco", "uniview", "amcrest", "the", "and", "home", "atlantic",
                                                     "avenue", "street", "navy", "yard", "brighton", "beach"):
                towns.append(t)
    body = strip(re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S))
    streets = []
    for m_ in re.finditer(r"\b((?:[0-9]+(?:st|nd|rd|th) |[A-Z][a-z]+ ){1,2}(?:Avenue|Street|Place|Road|Boulevard|Parkway|Turnpike|Highway|Lane|Drive))\b", body):
        st = m_.group(1).strip()
        if st.split()[0] in ("The", "A", "On", "In", "At", "From", "Our", "And", "Of", "To", "Main", "Each"):
            continue
        streets.append(st)
    from collections import Counter
    streets = [st for st, _ in Counter(streets).most_common(8)]
    badges = []
    hb = re.search(r'class="hbadge"[^>]*>(.*?)</div>', raw, re.S)
    if hb:
        badges = [b.strip() for b in re.split(r"[·|]", strip(hb.group(1))) if 3 < len(b.strip()) < 60 and "," not in b]
    heads = []
    for h in re.findall(r"<h3(?:\s[^>]*)?>([^<]{4,40})</h3>", raw):
        h = strip(h)
        if re.search(r"quote|price|form|faq|call|ready|request|why|how|what|who|\?", h, re.I):
            continue
        if len(h.split()) < 2 or h.isupper() or "/" in h or sum(c.isupper() for c in h) > len(h) * 0.35:
            continue
        if any(w in h.lower() for w in service.lower().split() if len(w) > 4):
            continue
        if h not in heads:
            heads.append(h)
    return dict(slug=slug, h1=h1, service=service, area=area, neighborhood=nb, price=price, phone=phone,
                images=imgs[:8], towns=towns[:6], streets=streets[:6], badges=badges[:3], heads=heads[:9], url="/" + slug)


def _pick(pool, seed, k=0):
    return pool[(seed >> (k * 5)) % len(pool)]


def _join(xs):
    xs = [x for x in xs if x]
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def _lc(h):
    return " ".join(w if (w.isupper() and len(w) > 1) else w.lower() for w in h.split())


def build_script(p):
    s = p["slug"]
    seed = int(hashlib.md5(s.encode()).hexdigest(), 16)
    fam = next(((w, v) for k, w, v in FAMILIES if k in s), GENERIC)
    place_disp = (p["neighborhood"] or (p["area"][0] if p["area"] else "NEW YORK")).upper()
    place_sp = p["neighborhood"] or (p["area"][1] if p["area"] else "New York")
    svc = p["service"]
    sv = svc.lower()
    hook_vo = _pick([
        f"Need {sv} in {place_sp}? Abstract Enterprises Security Systems has you covered.",
        f"{place_sp}, this one's for you. {svc}, done by licensed local techs.",
        f"Looking for {sv} in {place_sp}? Here's how we do it.",
        f"{svc} in {place_sp}, from the team that's been doing it for over twenty-five years.",
    ], seed, 0)
    lines = [dict(kind="hook", words=svc.upper().split(), tag=f"IN {place_disp}", vo=hook_vo)]
    mid = [dict(kind="problem", words=fam[0], vo=fam[1])]
    # what the page itself says we do
    if len(p["heads"]) >= 3:
        hs = [p["heads"][(seed >> (3 * k)) % len(p["heads"])] for k in range(6)]
        hs = list(dict.fromkeys(hs))[:3]
        if len(hs) == 3:
            mid.append(dict(kind="list", title=_pick(["WHAT WE HANDLE", "ON EVERY JOB", "WE COVER IT ALL"], seed, 1),
                            items=[h.upper() for h in hs],
                            vo=("We handle " + _join([_lc(x) for x in hs]) + ".").replace("&", "and")))
    # local: streets for neighborhood pages, towns for borough/county pages
    if p["neighborhood"] and len(p["streets"]) >= 2:
        st = p["streets"][:4]
        mid.append(dict(kind="local", title=f"ALL OVER {place_disp}", items=[x.upper() for x in st],
                        vo=_pick([f"We know {place_sp} block by block, from {st[0]} to {st[1]}.",
                                  f"{st[0]}, {st[1]}, and every street in between. We work all over {place_sp}."], seed, 2)))
    elif not p["neighborhood"] and not p["towns"] and len(p["streets"]) >= 2:
        st = p["streets"][:4]
        mid.append(dict(kind="local", title=f"ALL OVER {place_disp}", items=[x.upper() for x in st],
                        vo=f"From {st[0]} to {st[1]}, we cover all of {place_sp}."))
    elif len(p["towns"]) >= 2:
        tw = p["towns"][:5]
        mid.append(dict(kind="local", title=_pick([f"ALL OVER {place_disp}", f"EVERY CORNER OF {place_disp}"], seed, 2),
                        items=[x.upper() for x in tw],
                        vo=f"We cover all of {place_sp}, including {_join(tw[:3])}."))
    if p["badges"]:
        mid.append(dict(kind="badges", items=[b.upper() for b in p["badges"]],
                        vo=f"{_join(p['badges'][:3])}. We've wired them all."))
    mid.append(dict(kind="proof", vo=_pick(["Real techs on real jobs.",
                                            "Real techs. Real jobs. Done right.",
                                            "Real jobs, done by real AESS techs."], seed, 3)))
    # shuffle the middle by the page's seed so pages don't share one order
    order = sorted(range(len(mid)), key=lambda k: (seed >> (k * 4)) % 97)
    keep = [k for k in order if mid[k]["kind"] == "local"][:1]          # the local scene always stays
    keep += [k for k in order if k not in keep][:3 - len(keep)]       # 3 middle scenes max keeps it ~35s
    lines += [mid[k] for k in order if k in keep]
    if p["price"]:
        lines.append(dict(kind="price", price=p["price"],
                          vo=f"Already have a system? Our service call is {p['price']} dollars."))
    lines += [
        dict(kind="window", vo=_pick([
            "Pick a two-hour arrival window. We answer seven days a week, from eight in the morning to eight at night.",
            "You pick a two-hour arrival window, and we show up inside it. Our phones are open seven days, eight in the morning to eight at night.",
        ], seed, 4)),
        dict(kind="trust", vo=_pick(["Licensed, insured, and in the security business for over twenty-five years.",
                                     "Fully licensed and insured, with more than twenty-five years in the business."], seed, 5)),
        dict(kind="end", vo=f"Get your free quote today. Call {spoken_phone(p['phone'])}."),
    ]
    return lines


# ---------------- voice ----------------
_k = None
def tts(text):
    global _k
    if _k is None:
        from kokoro_onnx import Kokoro
        _k = Kokoro(os.path.join(KOKORO, "kokoro-v1.0.onnx"), os.path.join(KOKORO, "voices-v1.0.bin"))
    a, sr = _k.create(text, voice=VOICE, speed=1.08, lang="en-us")
    a = np.asarray(a, dtype=np.float64)
    nz = np.where(np.abs(a) > 0.01)[0]
    if len(nz):
        a = a[max(0, nz[0] - 800): nz[-1] + 1600]
    if sr != SR:
        a = np.interp(np.arange(int(len(a) * SR / sr)) * sr / SR, np.arange(len(a)), a)
    return a


def music(n, cuts):
    out = np.zeros(n); T = lambda d: np.arange(int(SR * d)) / SR
    def add(sig, at, g=1.0):
        i = int(at * SR); j = min(n, i + len(sig))
        if 0 <= i < n: out[i:j] += sig[:j - i] * g
    tk = T(.35); kick = np.sin(2 * np.pi * (45 + 120 * np.exp(-tk * 30)) * tk) * np.exp(-tk * 9)
    th = T(.06); hat = np.random.default_rng(2).standard_normal(len(th)) * np.exp(-th * 70)
    tb = T(.48); bass = [55, 65.4, 49, 58.3]
    for b in range(int(n / SR / .5)):
        at = b * .5
        add(kick, at, .75 if b % 2 == 0 else .45); add(hat, at + .25, .16)
        add(np.sign(np.sin(2 * np.pi * bass[(b // 4) % 4] * tb)) * .5 * np.exp(-tb * 4) * (1 - np.exp(-tb * 200)), at, .18)
    for c in cuts:
        tw = T(.35); nz = np.random.default_rng(int(c * 100)).standard_normal(len(tw))
        add(np.convolve(nz, np.ones(8) / 8, mode="same") * np.sin(np.pi * tw / .35) ** 2, c - .2, .22)
    return out / (np.max(np.abs(out)) + 1e-9)


# ---------------- drawing ----------------
def txt(s, size, fill, font=F_BLACK, squeeze=0.84, maxw=W - 120):
    im = A.txt(s, size, fill, font, squeeze)
    while im.width > maxw and size > 28:
        size -= 4; im = A.txt(s, size, fill, font, squeeze)
    return im


def pill(label, size, fg, bgc, pad=(30, 14)):
    t = txt(label, size, fg, F_BLACK, 0.88, maxw=W - 160)
    w, h = t.width + pad[0] * 2, t.height + pad[1] * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=bgc + (255,))
    im.alpha_composite(t, (pad[0], pad[1])); return im


_ph = {}
def photo(src):
    if src not in _ph:
        im = Image.open(os.path.join(SITE, src.lstrip("/"))).convert("RGB")
        r = max(W * 1.15 / im.width, H * 1.15 / im.height)
        im = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
        _ph[src] = im
    return _ph[src]


def kenburns(src, t, dark=0.45):
    im = photo(src)
    z = 1.0 + 0.12 * t
    cw, ch = int(W * 1.12 / z), int(H * 1.12 / z)
    x0 = (im.width - cw) // 2 + int(20 * t); y0 = (im.height - ch) // 2
    fr = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR).convert("RGBA")
    if dark:
        fr.alpha_composite(Image.new("RGBA", (W, H), (9, 22, 56, int(255 * dark))))
    return fr


def bgc(c): return Image.new("RGBA", (W, H), c + (255,))


def stack(cv, words, lf, colors, size=150, start=0, gap=10, cy=None, every=7):
    ims = [txt(w, size, colors[i % len(colors)]) for i, w in enumerate(words) if w]
    tot = sum(i.height for i in ims) + gap * (len(ims) - 1)
    y = (cy or H // 2) - tot // 2
    for i, im in enumerate(ims):
        sc, al = slam(lf, start + i * every)
        place(cv, im, W // 2, y + im.height // 2, sc, al)
        y += im.height + gap


def scene(sc, lf, n, p, seed):
    k = sc["kind"]
    if k == "hook":
        cv = kenburns(p["images"][0], lf / n, 0.62) if p["images"] else bgc(BLACK)
        words = sc["words"]
        rows, row = [], ""
        for w in words:
            if len(row) + len(w) > 16 and row:
                rows.append(row); row = w
            else:
                row = (row + " " + w).strip()
        rows.append(row)
        stack(cv, rows, lf, [WHITE], size=132 if len(rows) < 3 else 104, cy=H // 2 - 40)
        sc_, al = slam(lf, 7 * len(rows) + 4)
        place(cv, pill(sc["tag"], 46, WHITE, BLUE), W // 2, H - 150, sc_, al)
    elif k == "problem":
        cv = bgc([BLUE, BLACK, NAVY][seed % 3])
        stack(cv, sc["words"], lf, [WHITE, WHITE, SKY], size=150)
    elif k == "proof":
        imgs = p["images"][1:4] or p["images"][:1]
        if imgs:
            seg = n / len(imgs); i = min(len(imgs) - 1, int(lf / seg))
            cv = kenburns(imgs[i], (lf - i * seg) / seg, 0.25)
        else:
            cv = bgc(NAVY)
        place(cv, pill("REAL TECHS. REAL JOBS.", 44, WHITE, BLUE), W // 2, 90, *slam(lf, 2))
    elif k in ("list", "local", "badges"):
        cv = bgc([NAVY, BLUE, BLACK][(seed >> 7) % 3]) if k != "local" or not p["images"] else kenburns(p["images"][min(1, len(p["images"]) - 1)], lf / n, 0.72)
        title = sc.get("title") or "BUILT FOR"
        place(cv, txt(title, 76, SKY if k != "list" else WHITE), W // 2, 120, *slam(lf, 0))
        items = sc["items"]
        gap = min(110, (H - 260) // max(1, len(items)))
        y0 = 250 + (H - 260 - gap * len(items)) // 2
        for i_, it in enumerate(items):
            place(cv, pill(it, 40 if len(items) > 3 else 46, WHITE if k != "badges" else BLACK,
                           BLUE if k != "badges" else WHITE), W // 2, y0 + i_ * gap, *slam(lf, 6 + i_ * 6))
    elif k == "price":
        cv = bgc(WHITE)
        stack(cv, ["SERVICE CALL"], lf, [BLACK], size=96, cy=H // 2 - 110)
        sc_, al = slam(lf, 8)
        place(cv, txt(f"${sc['price']}", 260, BLUE), W // 2, H // 2 + 60, sc_, al)
        place(cv, pill("ALREADY HAVE A SYSTEM?", 34, WHITE, BLACK), W // 2, H - 80, *slam(lf, 16))
    elif k == "window":
        cv = bgc(NAVY)
        t = clamp(lf / max(1, n * 0.6))
        hr = 8 + 2 * e_out(t)
        clock = txt(f"{int(hr)}:{int((hr % 1) * 60):02d} AM", 120, WHITE)
        place(cv, clock, W // 2, H // 2 - 120, *slam(lf, 0))
        place(cv, pill("2-HOUR ARRIVAL WINDOW", 54, WHITE, BLUE), W // 2, H // 2 + 40, *slam(lf, 8))
        place(cv, txt("OPEN 7 DAYS · 8AM–8PM", 54, SKY), W // 2, H // 2 + 160, *slam(lf, 16))
    elif k == "trust":
        cv = kenburns(p["images"][-1], lf / n, 0.7) if p["images"] else bgc(BLACK)
        stack(cv, ["LICENSED.", "INSURED.", "25+ YEARS."], lf, [WHITE, WHITE, SKY], size=130)
    else:  # end card
        cv = bgc(WHITE)
        lg = LOGO.convert("RGBA"); r = 300 / lg.width
        lg = lg.resize((300, int(lg.height * r)), Image.LANCZOS)
        place(cv, lg, W // 2, 170, *slam(lf, 0))
        place(cv, pill("GET A FREE QUOTE →", 52, WHITE, BLACK), W // 2, 360, *slam(lf, 6))
        place(cv, txt(p["phone"], 92, BLUE), W // 2, 480, *slam(lf, 12))
        place(cv, txt("abstractenterprisessecuritysystems.com", 34, BLACK, F_BOLD, 1.0), W // 2, 580, *slam(lf, 18))
    return cv


def wipe(cv, lf, color):
    t = prog(lf, 0, 7)
    if 0 < t < 1:
        x = int(W * e_out(t))
        ImageDraw.Draw(cv).rectangle((x, 0, W, H), fill=color + (255,))


def render(path, outdir):
    p = parse(path)
    lines = build_script(p)
    seed = int(hashlib.md5(p["slug"].encode()).hexdigest(), 16)
    os.makedirs(outdir, exist_ok=True)
    vos = [tts(l["vo"]) for l in lines]
    lead, tail = 0.35, 0.45
    lens = [max(int((lead + len(v) / SR + tail) * FPS), 45) for v in vos]
    total = sum(lens)
    n = int(total / FPS * SR) + SR // 2
    starts = np.cumsum([0] + lens[:-1])
    mus = music(n, [s / FPS for s in starts[1:]])
    duck = np.ones(n) * .40
    voice = np.zeros(n)
    for s, v in zip(starts, vos):
        i = int((s / FPS + lead) * SR); voice[i:i + len(v)] += v[:max(0, n - i)]
        duck[max(0, i - 3000): i + len(v) + 4000] = .12
    duck = np.convolve(duck, np.ones(2400) / 2400, mode="same")
    fade = np.ones(n); fl = int(SR * .7); fade[-fl:] = np.linspace(1, 0, fl)
    mix = (mus * duck + voice * 1.0) * fade
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * .92
    base = os.path.join(outdir, p["slug"])
    with wave.open(base + ".wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    proc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-i", base + ".wav", "-c:v", "libx264", "-preset", "veryfast",
                             "-crf", "26", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-shortest",
                             "-movflags", "+faststart", base + ".mp4"], stdin=subprocess.PIPE)
    wipes = [BLUE, BLACK, NAVY, WHITE]
    poster = None
    for si, (sc, s, ln) in enumerate(zip(lines, starts, lens)):
        for lf in range(ln):
            cv = scene(sc, lf, ln, p, seed)
            if si:
                wipe(cv, lf, wipes[(si + seed) % 4])
            if si == 0 and lf == min(ln - 1, 40):
                poster = cv.convert("RGB")
            proc.stdin.write(cv.convert("RGB").tobytes())
    proc.stdin.close(); proc.wait()
    os.remove(base + ".wav")
    (poster or Image.new("RGB", (W, H), NAVY)).save(base + ".jpg", quality=82)
    meta = dict(p, seconds=round(total / FPS, 1), script=[l["vo"] for l in lines])
    json.dump(meta, open(base + ".json", "w"), indent=1)
    return meta


if __name__ == "__main__":
    out = sys.argv[2] if len(sys.argv) > 2 else "hero-out"
    m = render(sys.argv[1], out)
    print(json.dumps({k: m[k] for k in ("slug", "service", "area", "price", "phone", "seconds")}))
    print("\n".join(m["script"]))
