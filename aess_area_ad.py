#!/usr/bin/env python3
"""AESS per-area 60s Facebook ad (1080x1920, 30fps). Usage: python aess_area_ad.py <slug> [outdir]"""
import os, sys, glob, subprocess, wave, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aess_promo as A
from aess_promo import (W, H, FPS, BLACK, BLUE, NAVY, WHITE, SKY, GREY, F_BLACK, F_BOLD, LOGO,
                        place, slam, bg, wipe, shake, prog, e_out, e_back, e_inout, clamp, icon, tile, van, bez, _paste_clip)

N = 1800
SITE = os.environ.get("AESS_SITE", "/home/claude/abstract-enterprises-site")
CS = os.path.join(SITE, "images/commercial-security")
SL = os.path.join(SITE, "images/smart-lock-installation")

def txt(s, size, fill, font=F_BLACK, squeeze=0.84, maxw=W - 90):
    im = A.txt(s, size, fill, font, squeeze)
    while im.width > maxw and size > 36:
        size -= 6; im = A.txt(s, size, fill, font, squeeze)
    return im

def pill(label, size, fg, bgc, pad=(44, 22), outline=None):
    t = txt(label, size, fg, F_BLACK, 0.88, maxw=W - 90 - 2 * pad[0])
    w, h = t.width + pad[0] * 2, t.height + pad[1] * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=(bgc + (255,)) if bgc else None,
                        outline=(outline + (255,)) if outline else None, width=5)
    im.alpha_composite(t, (pad[0], pad[1])); return im

NYC_PHONE, NAS, SUF, WES, HV, TOLL = "(917) 268-3951", "(516) 261-7110", "(631) 570-5699", "(914) 436-5218", "(845) 262-4137", "(800) 486-0943"
AREAS = {
 "brooklyn":      dict(name="BROOKLYN", short="BROOKLYN", inn="IN BROOKLYN", phone=NYC_PHONE, rate=150, cs="brooklyn",
                       towns=["BED-STUY", "PARK SLOPE", "FLATBUSH", "CANARSIE", "CROWN HEIGHTS", "WILLIAMSBURG", "BAY RIDGE", "EAST NEW YORK"],
                       trio=["BROWNSTONES.", "STOREFRONTS.", "WAREHOUSES."]),
 "queens":        dict(name="QUEENS", short="QUEENS", inn="IN QUEENS", phone=NYC_PHONE, rate=150, cs="queens",
                       towns=["ASTORIA", "FLUSHING", "JAMAICA", "BAYSIDE", "LONG ISLAND CITY", "JACKSON HEIGHTS", "FOREST HILLS", "OZONE PARK"],
                       trio=["HOMES.", "STOREFRONTS.", "WAREHOUSES."]),
 "bronx":         dict(name="THE BRONX", short="BRONX", inn="IN THE BRONX", phone=NYC_PHONE, rate=175, cs="bronx",
                       towns=["FORDHAM", "RIVERDALE", "PELHAM BAY", "MOTT HAVEN", "THROGGS NECK", "PARKCHESTER", "NORWOOD", "CO-OP CITY"],
                       trio=["APARTMENTS.", "STORES.", "WAREHOUSES."]),
 "manhattan":     dict(name="MANHATTAN", short="MANHATTAN", inn="IN MANHATTAN", phone=NYC_PHONE, rate=205, cs="manhattan",
                       towns=["HARLEM", "UPPER WEST SIDE", "UPPER EAST SIDE", "MIDTOWN", "CHELSEA", "EAST VILLAGE", "TRIBECA", "WASHINGTON HEIGHTS"],
                       trio=["CO-OPS.", "OFFICES.", "STOREFRONTS."]),
 "staten-island": dict(name="STATEN ISLAND", short="STATEN ISLAND", inn="ON STATEN ISLAND", phone=NYC_PHONE, rate=175, cs="staten-island",
                       towns=["ST. GEORGE", "TOTTENVILLE", "GREAT KILLS", "NEW DORP", "PORT RICHMOND", "STAPLETON", "ANNADALE", "WESTERLEIGH"],
                       trio=["HOMES.", "STORES.", "WAREHOUSES."]),
 "nyc":           dict(name="NEW YORK CITY", short="NYC", inn="IN NYC", phone=NYC_PHONE, rate=150, cs="nyc",
                       towns=["BROOKLYN", "QUEENS", "THE BRONX", "MANHATTAN", "STATEN ISLAND"],
                       trio=["HOMES.", "BUILDINGS.", "BUSINESSES."]),
 "nassau-county": dict(name="NASSAU", short="NASSAU", inn="IN NASSAU COUNTY", phone=NAS, rate=175, cs="nassau",
                       towns=["HEMPSTEAD", "GARDEN CITY", "GREAT NECK", "LEVITTOWN", "FREEPORT", "VALLEY STREAM", "MASSAPEQUA", "MINEOLA"],
                       trio=["HOMES.", "OFFICES.", "WAREHOUSES."]),
 "suffolk-county":dict(name="SUFFOLK", short="SUFFOLK", inn="IN SUFFOLK COUNTY", phone=SUF, rate=190, cs="suffolk",
                       towns=["HUNTINGTON", "SMITHTOWN", "BRENTWOOD", "ISLIP", "BABYLON", "RIVERHEAD", "SELDEN", "SOUTHAMPTON"],
                       trio=["HOMES.", "OFFICES.", "WAREHOUSES."]),
 "long-island":   dict(name="LONG ISLAND", short="LONG ISLAND", inn="ON LONG ISLAND", phone=TOLL, rate=175, cs="long-island",
                       towns=["NASSAU", "SUFFOLK", "HEMPSTEAD", "HUNTINGTON", "GARDEN CITY", "ISLIP"],
                       trio=["HOMES.", "OFFICES.", "WAREHOUSES."]),
 "westchester-county": dict(name="WESTCHESTER", short="WESTCHESTER", inn="IN WESTCHESTER", phone=WES, rate=180, cs="westchester",
                       towns=["YONKERS", "WHITE PLAINS", "NEW ROCHELLE", "MOUNT VERNON", "SCARSDALE", "PEEKSKILL", "RYE", "OSSINING"],
                       trio=["HOMES.", "OFFICES.", "BUILDINGS."]),
 "rockland-county": dict(name="ROCKLAND", short="ROCKLAND", inn="IN ROCKLAND COUNTY", phone=HV, rate=180, cs="rockland",
                       towns=["NYACK", "NEW CITY", "SPRING VALLEY", "NANUET", "SUFFERN", "PEARL RIVER", "HAVERSTRAW", "ORANGEBURG"],
                       trio=["HOMES.", "OFFICES.", "WAREHOUSES."]),
 "orange-county": dict(name="ORANGE COUNTY", short="ORANGE COUNTY", inn="IN ORANGE COUNTY", phone=HV, rate=190, cs="orange",
                       towns=["NEWBURGH", "MIDDLETOWN", "GOSHEN", "MONROE", "WARWICK", "PORT JERVIS", "CORNWALL", "CHESTER"],
                       trio=["HOMES.", "FARMS.", "BUSINESSES."]),
 "putnam-county": dict(name="PUTNAM", short="PUTNAM", inn="IN PUTNAM COUNTY", phone=HV, rate=190, cs="putnam",
                       towns=["CARMEL", "BREWSTER", "MAHOPAC", "COLD SPRING", "PATTERSON", "KENT", "PUTNAM VALLEY", "GARRISON"],
                       trio=["HOMES.", "COTTAGES.", "BUSINESSES."]),
 "dutchess-county": dict(name="DUTCHESS", short="DUTCHESS", inn="IN DUTCHESS COUNTY", phone=HV, rate=215, cs="dutchess",
                       towns=["POUGHKEEPSIE", "BEACON", "FISHKILL", "WAPPINGERS FALLS", "HYDE PARK", "RHINEBECK", "MILLBROOK", "RED HOOK"],
                       trio=["HOMES.", "FARMS.", "BUSINESSES."]),
 "ulster-county": dict(name="ULSTER", short="ULSTER", inn="IN ULSTER COUNTY", phone=HV, rate=215, cs="ulster",
                       towns=["KINGSTON", "NEW PALTZ", "SAUGERTIES", "WOODSTOCK", "ELLENVILLE", "HIGHLAND", "MARLBORO", "PHOENICIA"],
                       trio=["HOMES.", "FARMS.", "BUSINESSES."]),
 "hudson-valley": dict(name="HUDSON VALLEY", short="HUDSON VALLEY", inn="IN THE HUDSON VALLEY", phone=HV, rate=180, cs="hudson-valley",
                       towns=["WESTCHESTER", "ROCKLAND", "ORANGE", "PUTNAM", "DUTCHESS", "ULSTER"],
                       trio=["HOMES.", "FARMS.", "BUSINESSES."]),
}

CAPTIONS = [("video-intercom", "VIDEO INTERCOMS"), ("entrance-camera-intercom", "ENTRY CAMERAS"), ("access-reader", "ACCESS CONTROL"),
            ("alarm-keypad", "ALARM SYSTEMS"), ("credential-programming", "KEY CARDS SET UP"), ("crew-van", "ON OUR WAY"),
            ("dock-cameras", "LOADING DOCK CAMS"), ("loading-dock", "LOADING DOCK CAMS"), ("electric-strike", "DOOR HARDWARE"),
            ("glass-break", "GLASS-BREAK SENSORS"), ("integration-rack", "ONE CONNECTED SYSTEM"), ("lpr", "PLATE-READING CAMS"),
            ("nvr-poe-rack", "RECORDING & STORAGE"), ("panic-button", "PANIC BUTTONS"), ("warehouse", "WAREHOUSE CAMERAS"),
            ("building-cameras", "BUILDING CAMERAS"), ("secured-lobby", "LOBBY SECURITY"), ("entrance-crew", "ENTRANCE SECURITY"),
            ("conduit-pull", "CLEAN CABLE RUNS"), ("maglock", "MAGLOCKS"), ("exterior-enclosures", "WEATHERPROOF GEAR"),
            ("office-cat6", "OFFICE CABLING"), ("dashboard-training", "APP TRAINING"), ("access-control-panels", "ACCESS PANELS"),
            ("door-contact", "DOOR SENSORS"), ("door-controller", "DOOR CONTROLLERS"), ("camera", "SECURITY CAMERAS")]
PRIORITY = ["hero", "video-intercom", "entrance-camera", "access-reader", "alarm-keypad", "lpr", "warehouse", "dock", "building-cameras",
            "credential", "nvr", "electric-strike", "panic", "glass-break", "crew-van", "integration", "secured-lobby", "entrance-crew", "maglock"]

def caption(fn):
    b = os.path.basename(fn).lower()
    for k, c in CAPTIONS:
        if k in b: return c
    return "REAL AESS INSTALLS"

def area_photos(cs_slug, n=7):
    fs = [f for f in glob.glob(os.path.join(CS, f"*-{cs_slug}-*.jpg"))]
    fs = [f for f in fs if not re.search(r"(hudson-valley|long-island)", f) or cs_slug in ("hudson-valley", "long-island")]
    def rank(f):
        b = os.path.basename(f)
        for i, k in enumerate(PRIORITY):
            if k in b: return i
        return 99
    fs.sort(key=rank)
    seen, out = set(), []
    for f in fs:
        c = caption(f)
        if c in seen: continue
        seen.add(c); out.append((f, c))
        if len(out) == n: break
    return out

DOORBELL = os.path.join(SL, "aess-smart-lock-installation-video-doorbell-and-smart-lock.webp")
RES = [("office-glass-door-smart-lock", "OFFICES"), ("apartment-door-smart-lock-app", "APARTMENTS"),
       ("suburban-front-door-smart-lock-van", "HOMES"), ("programming-access-code-app", "CODES SET UP"),
       ("fingerprint-unlock-demo-app", "SMART LOCKS"), ("replacing-smart-lock-batteries", "SERVICE & REPAIR"),
       ("keypad-smart-deadbolt-brownstone-door", "KEYLESS ENTRY")]

_ph = {}
def photo(path):
    if path in _ph: return _ph[path]
    im = Image.open(path).convert("RGB"); s = (H * 1.12) / im.height
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS); _ph[path] = im; return im

_grad = None
def grad():
    global _grad
    if _grad is None:
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
        for y in range(H):
            a = int(230 * ((y - H * .55) / (H * .45)) ** 1.3) if y > H * .55 else 0
            if y < 300: a = max(a, int(160 * (1 - y / 300)))
            d.line((0, y, W, y), fill=(5, 10, 30, a))
        _grad = g
    return _grad

def photo_frame(path, label, top, lf, dur, idx):
    im = photo(path); z = 1.0 + 0.10 * (lf / dur)
    cw, ch = int(W / z), int(H / z); maxx = im.width - cw
    pan = (lf / dur) if idx % 2 == 0 else 1 - (lf / dur)
    x = int(maxx * (0.30 + 0.40 * pan)); y = int((im.height - ch) / 2)
    cv = im.crop((x, y, x + cw, y + ch)).resize((W, H), Image.BILINEAR).convert("RGBA"); cv.alpha_composite(grad())
    t = prog(lf, 2, 8)
    place(cv, pill(label, 92, WHITE, BLUE, pad=(54, 26)), W / 2, 1560 + 70 * (1 - e_out(t)), 1, clamp(t * 2))
    place(cv, txt(top, 52, WHITE, F_BLACK, .9), W / 2, 170)
    place(cv, badge(), W - 170, 380, 1, 1, rot=12)
    if lf < 3: cv.alpha_composite(Image.new("RGBA", (W, H), (255, 255, 255, int(170 * (1 - lf / 3)))))
    return cv

_badge = None
def badge():
    global _badge
    if _badge is None:
        b = Image.new("RGBA", (250, 250), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
        d.ellipse((0, 0, 249, 249), fill=WHITE + (255,)); d.ellipse((12, 12, 237, 237), fill=BLUE + (255,))
        for word, y, sz in (("FREE", 78, 76), ("VIDEO", 140, 44), ("DOORBELL", 184, 40)):
            t = A.txt(word, sz, WHITE, F_BLACK, .86); b.alpha_composite(t, ((250 - t.width) // 2, int(y - t.height / 2)))
        _badge = b
    return _badge

def montage(items, top, lf, total):
    per = total / len(items); i = min(len(items) - 1, int(lf // per))
    return photo_frame(items[i][0], items[i][1], top, lf - i * per, per, i)

class Ad:
    def __init__(self, slug):
        self.c = AREAS[slug]; self.slug = slug
        self.m1 = area_photos(self.c["cs"], 7)
        self.m2 = [(os.path.join(SL, f"aess-smart-lock-installation-{s}.webp"), c) for s, c in RES]

    def frame(self, f):
        c = self.c; NAME, SHORT = c["name"], c["short"]
        if f < 45:  # hook
            cv = bg(BLACK)
            for w_, st, y, col in ((NAME, 0, 700, WHITE), ("DOESN'T", 8, 930, WHITE), ("WAIT.", 16, 1160, SKY)):
                place(cv, txt(w_, 250, col), W / 2, y, *slam(f, st))
            wipe(cv, f, 39, BLUE); return cv
        if f < 90:
            cv = bg(BLUE); lf = f - 45
            tick = A.txt(f"{SHORT} • SECURITY • {SHORT} • SECURITY • {SHORT} • SECURITY • ", 170, (60, 105, 235), F_BLACK, 0.84)
            for (y, d) in ((330, -1), (1590, 1)):
                off = (lf * 14 * d) % max(1, tick.width // 2)
                _paste_clip(cv, tick, int(-off if d > 0 else off - tick.width // 2), y)
            t1 = e_out(prog(lf, 2, 9)); place(cv, txt("NEITHER", 270, BLACK), -400 + (W/2 + 400) * t1, 860, mblur=int(120*(1-t1)))
            t2 = e_out(prog(lf, 12, 9)); place(cv, txt("DO WE.", 300, WHITE), W + 400 - (W/2 + 400) * t2, 1110, mblur=int(120*(1-t2)))
            wipe(cv, f, 84, WHITE); return cv
        if f < 180:  # WE INSTALL tiles
            lf = f - 90; cv = A.frame(90 + min(lf, 68)); wipe(cv, lf, 84, BLACK); return cv
        if f < 420:  # area jobs
            lf = f - 180
            if lf < 30:
                cv = bg(BLACK)
                place(cv, txt("REAL TECHS.", 200, WHITE), W / 2, 820, *slam(lf, 0))
                place(cv, txt(f"REAL {SHORT} JOBS.", 200, SKY), W / 2, 1060, *slam(lf, 8))
                return cv
            cv = montage(self.m1, f"AESS {c['inn']}", lf - 30, 210); wipe(cv, lf, 234, BLUE); return cv
        if f < 540:  # route
            lf = f - 420; cv = bg(BLUE); d = ImageDraw.Draw(cv)
            for i in range(-6, 14):
                d.line((i * 140, 0, i * 140 + 700, H), fill=(44, 88, 224), width=6)
                d.line((0, i * 170, W, i * 170 - 300), fill=(44, 88, 224), width=6)
            for (tx, ty), town in zip(((760, 560), (300, 930), (300, 1520)), c["towns"][:3]):
                place(cv, txt(town, 44, (110, 150, 245), F_BLACK, .9, maxw=420), tx, ty)
            pr = e_inout(prog(lf, 10, 70))
            mins = 480 + int(120 * pr); hh, mm = mins // 60, mins % 60
            place(cv, pill(f"{hh if hh <= 12 else hh - 12}:{mm:02d} AM", 92, WHITE, BLACK, pad=(50, 24)), W / 2, 250, *slam(lf, 0))
            place(cv, txt("YOU CALL", 70, WHITE, F_BLACK, 0.9), W / 2, 400, 1, clamp(lf / 6))
            P = [(230, 620), (820, 760), (180, 1180), (800, 1420)]
            pts = [bez(*P, i / 80) for i in range(81)]; nshow = int(80 * pr)
            for i in range(0, 80, 3):
                if i <= nshow: d.line([pts[i], pts[min(i + 1, 80)]], fill=WHITE + (255,), width=12)
            d.ellipse((P[0][0]-26, P[0][1]-26, P[0][0]+26, P[0][1]+26), fill=WHITE + (255,))
            place(cv, txt("AESS TECH", 54, WHITE, F_BLACK, .9), P[0][0] + 160, P[0][1] - 70)
            pin_t = prog(lf, 78, 8)
            if pin_t > 0:
                x, y = P[3]
                pin = Image.new("RGBA", (120, 160), (0, 0, 0, 0)); pd = ImageDraw.Draw(pin)
                pd.ellipse((0, 0, 120, 120), fill=BLACK + (255,)); pd.polygon([(18, 90), (102, 90), (60, 158)], fill=BLACK + (255,))
                pd.ellipse((38, 38, 82, 82), fill=WHITE + (255,))
                place(cv, pin, x, y - 150, e_back(pin_t))
                lab = txt(f"YOUR {SHORT} DOOR", 60, WHITE, F_BLACK, .9, maxw=900)
                place(cv, lab, min(W - 50 - lab.width / 2, max(50 + lab.width / 2, x - 40)), y + 70, 1, clamp(pin_t * 2))
            vx, vy = pts[nshow]; place(cv, van(1.25), vx, vy - 40)
            bt = prog(lf, 20, 10)
            place(cv, pill("2-HOUR ARRIVAL WINDOW", 64, BLUE, WHITE), W / 2, 1700 + 80 * (1 - e_out(bt)), 1, clamp(bt * 2))
            wipe(cv, lf, 114, BLUE); return cv
        if f < 660:  # how it works
            lf = f - 540; cv = bg(BLUE)
            place(cv, txt("HOW IT WORKS", 170, WHITE), W / 2, 330, *slam(lf, 0))
            for i, s in enumerate(["CALL OR TEXT US", "GET YOUR QUOTE", "PICK A 2-HR WINDOW", "INSTALLED & TESTED"]):
                t = prog(lf, 10 + i * 12, 9)
                if t <= 0: continue
                y = 640 + i * 270; x0 = 150 + 120 * (1 - e_out(t))
                cc = Image.new("RGBA", (170, 170), (0, 0, 0, 0)); cd = ImageDraw.Draw(cc)
                cd.ellipse((0, 0, 169, 169), fill=(BLACK if i < 3 else WHITE) + (255,))
                n = A.txt(str(i + 1), 110, WHITE if i < 3 else BLUE, F_BLACK, 1); cc.alpha_composite(n, ((170 - n.width) // 2, (170 - n.height) // 2))
                place(cv, cc, x0, y, e_back(t), clamp(t * 2))
                lab = txt(s, 76, WHITE, F_BLACK, .86, maxw=760); place(cv, lab, x0 + 110 + lab.width / 2, y, 1, clamp(t * 2))
            wipe(cv, lf, 114, BLACK); return cv
        if f < 780:  # OFFER: free video doorbell
            lf = f - 660; sx, sy = shake(lf, 14, 8, 18)
            im = photo(DOORBELL); z = 1.0 + 0.08 * (lf / 120); cw, ch = int(W / z), int(H / z)
            x = int((im.width - cw) * 0.62); y = int((im.height - ch) / 2)
            cv = im.crop((x, y, x + cw, y + ch)).resize((W, H), Image.BILINEAR).convert("RGBA")
            cv.alpha_composite(Image.new("RGBA", (W, H), (5, 10, 30, 175)))
            place(cv, txt("GET A", 120, WHITE), W / 2, 470, *slam(lf, 0))
            place(cv, txt("FREE", 420, SKY, F_BLACK, .9), W / 2 + sx, 760 + sy, *slam(lf, 6))
            place(cv, txt("VIDEO DOORBELL", 170, WHITE), W / 2 + sx, 1040 + sy, *slam(lf, 14))
            t = prog(lf, 26, 9)
            place(cv, pill("WITH ANY CAMERA SYSTEM INSTALL", 62, BLACK, WHITE), W / 2, 1290 + 60 * (1 - e_out(t)), 1, clamp(t * 2))
            place(cv, txt(f"FOR {SHORT} CUSTOMERS", 60, SKY, F_BLACK, .9), W / 2, 1420, 1, clamp(prog(lf, 36, 8) * 2))
            wipe(cv, lf, 114, BLACK); return cv
        if f < 900:  # installed stamp
            lf = f - 780; cv = A.frame(240 + min(lf, 53)); wipe(cv, lf, 114, NAVY); return cv
        if f < 1140:  # any door montage
            lf = f - 900
            if lf < 30:
                cv = bg(NAVY)
                place(cv, txt("ANY DOOR.", 220, WHITE), W / 2, 820, *slam(lf, 0))
                place(cv, txt("ANY PROPERTY.", 170, SKY), W / 2, 1060, *slam(lf, 8))
                return cv
            cv = montage(self.m2, "REAL AESS INSTALLS", lf - 30, 210); wipe(cv, lf, 234, NAVY); return cv
        if f < 1260:  # warranty
            lf = f - 1140; cv = bg(NAVY); t = prog(lf, 0, 14)
            place(cv, icon("alarm", 420, SKY), W / 2, 640, e_back(t) if t > 0 else 0, clamp(t * 2))
            place(cv, txt("EVERY PART", 170, WHITE), W / 2, 1010, *slam(lf, 14))
            place(cv, txt("WARRANTIED.", 190, WHITE), W / 2, 1210, *slam(lf, 22))
            t2 = prog(lf, 40, 10)
            place(cv, pill("EXTENDED PLANS AVAILABLE", 64, NAVY, WHITE), W / 2, 1460 + 60 * (1 - e_out(t2)), 1, clamp(t2 * 2))
            wipe(cv, lf, 114, BLACK); return cv
        if f < 1380:  # hours
            lf = f - 1260; cv = bg(BLACK); sx, sy = shake(lf, 10, 8, 14)
            place(cv, txt("OPEN", 200, WHITE), W / 2 + sx, 720 + sy, *slam(lf, 0))
            place(cv, txt("7 DAYS", 330, SKY), W / 2 + sx, 990 + sy, *slam(lf, 8))
            t = prog(lf, 22, 9)
            place(cv, pill("8 AM – 8 PM", 96, BLACK, WHITE, pad=(60, 28)), W / 2, 1300 + 60 * (1 - e_out(t)), 1, clamp(t * 2))
            wipe(cv, lf, 114, NAVY); return cv
        if f < 1500:  # coverage in this area
            lf = f - 1380; cv = bg(NAVY)
            place(cv, txt("WE COVER", 170, WHITE), W / 2, 330, *slam(lf, 0))
            place(cv, pill(NAME, 120, WHITE, BLUE, pad=(64, 30)), W / 2, 560, *slam(lf, 8))
            towns = c["towns"]; rows = [towns[i:i + 2] for i in range(0, len(towns), 2)]
            for r, row in enumerate(rows):
                ps = [pill(s, 54, SKY, None, pad=(34, 16), outline=SKY) for s in row]
                tw = sum(p.width for p in ps) + 26 * (len(ps) - 1)
                if tw > W - 80:
                    ps = [pill(s, 44, SKY, None, pad=(28, 14), outline=SKY) for s in row]; tw = sum(p.width for p in ps) + 26 * (len(ps) - 1)
                x = W / 2 - tw / 2
                for j, p in enumerate(ps):
                    t = prog(lf, 18 + r * 5 + j * 2, 7)
                    place(cv, p, x + p.width / 2, 820 + r * 170, e_back(t) if t > 0 else 0, clamp(t * 2)); x += p.width + 26
            wipe(cv, lf, 114, WHITE); return cv
        if f < 1620:  # property trio
            lf = f - 1500; cv = bg(WHITE)
            for w_, st, y, col in zip(c["trio"], (0, 12, 24), (680, 960, 1240), (BLACK, BLUE, BLACK)):
                place(cv, txt(w_, 230, col), W / 2, y, *slam(lf, st))
            wipe(cv, lf, 114, BLUE); return cv
        if f < 1680:  # close
            lf = f - 1620; cv = bg(BLUE); sx, sy = shake(lf, 14, 8, 14)
            place(cv, txt("WE SECURE", 180, BLACK), W / 2 + sx, 760 + sy, *slam(lf, 0))
            place(cv, txt(SHORT + ".", 290, WHITE), W / 2 + sx, 1030 + sy, *slam(lf, 9))
            wipe(cv, lf, 54, WHITE); return cv
        lf = f - 1680; cv = bg(WHITE)  # end card
        t = prog(lf, 0, 12)
        place(cv, LOGO.resize((740, 740), Image.LANCZOS).convert("RGBA"), W / 2, 660, e_back(t, 1.9) if t > 0 else 0, clamp(t * 3))
        t2 = prog(lf, 12, 10)
        place(cv, pill("GET A FREE QUOTE  →", 78, WHITE, BLACK, pad=(64, 34)), W / 2, 1170 + 90 * (1 - e_out(t2)), 1, clamp(t2 * 2))
        t3 = prog(lf, 20, 10)
        place(cv, txt(c["phone"], 120, BLUE), W / 2, 1370, 1, clamp(t3 * 2))
        place(cv, txt(f"SERVING {NAME}", 64, BLACK, F_BLACK, .9), W / 2, 1490, 1, clamp(t3 * 2))
        tb = prog(lf, 4, 12)
        place(cv, badge(), W - 190, 260, e_back(tb) if tb > 0 else 0, clamp(tb * 2), rot=12)
        place(cv, txt("abstractenterprisessecuritysystems.com", 40, GREY, F_BOLD, .95), W / 2, 1600, 1, clamp(t3 * 2))
        t4 = prog(lf, 34, 10)
        place(cv, txt("OPEN 7 DAYS  •  8 AM – 8 PM", 46, BLACK, F_BOLD, .95), W / 2, 1700, 1, clamp(t4 * 2))
        return cv

def audio(path, sr=44100):
    n = int(sr * N / FPS); out = np.zeros(n); t = lambda d: np.arange(int(sr * d)) / sr
    def add(sig, at, g=1.0):
        i = int(at * sr); j = min(n, i + len(sig))
        if 0 <= i < n: out[i:j] += sig[:j - i] * g
    tk = t(0.35); kick = np.sin(2*np.pi*(45 + 120*np.exp(-tk*30))*tk) * np.exp(-tk*9)
    th = t(0.06); hat = np.random.default_rng(1).standard_normal(len(th)) * np.exp(-th*70)
    ts = t(0.22); snare = (np.random.default_rng(2).standard_normal(len(ts)) * .7 + np.sin(2*np.pi*190*ts)) * np.exp(-ts*18)
    tb = t(0.48); tp = t(2.0); notes = [55, 55, 65.4, 49]; brk0, brk1 = 1140 / FPS, 1260 / FPS
    for b in range(int(56 / 0.5)):
        at = b * 0.5; fq = notes[(b // 4) % 4]
        if brk0 <= at < brk1:
            if b % 4 == 0: add(sum(np.sin(2*np.pi*m*fq*4*tp) for m in (1, 1.26, 1.5)) * np.sin(np.pi*tp/2.0)**2 * 0.08, at)
            if b % 2 == 0: add(hat, at + 0.25, 0.12)
            continue
        add(kick, at, 0.9); add(hat, at + 0.25, 0.22)
        if b % 2 == 1: add(snare, at, 0.35)
        if b % 8 == 7: add(hat, at + 0.125, 0.15); add(hat, at + 0.375, 0.15)
        add(np.sign(np.sin(2*np.pi*fq*tb)) * 0.5 * np.exp(-tb*4) * (1 - np.exp(-tb*200)), at, 0.22)
    def whoosh(at, dur=0.35, g=0.2):
        tw = t(dur); nz = np.random.default_rng(int(at*10)).standard_normal(len(tw))
        add(np.convolve(nz, np.ones(8)/8, mode="same") * np.sin(np.pi*tw/dur)**2, at - dur*0.6, g)
    cuts = [45, 90, 180, 210, 420, 540, 660, 780, 900, 930, 1140, 1260, 1380, 1500, 1620, 1680]
    cuts += [210 + i * 30 for i in range(1, 7)] + [930 + i * 30 for i in range(1, 7)]
    for cu in cuts: whoosh(cu / FPS)
    ti = t(1.2); boom = np.sin(2*np.pi*(38 + 60*np.exp(-ti*8))*ti) * np.exp(-ti*3)
    for b in (666, 780, 1260, 1680): add(boom, b / FPS, 0.9)
    tc = t(2.5); add(sum(np.sin(2*np.pi*fq*tc) for fq in (220, 277.2, 329.6, 440)) * np.exp(-tc*1.2) * 0.12, 1680 / FPS)
    fl = int(sr * 1.0); out[-fl:] *= np.linspace(1, 0, fl)
    out = out / (np.max(np.abs(out)) + 1e-9) * 0.89
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    slug = sys.argv[1]; outdir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(A.D, "ads")
    os.makedirs(outdir, exist_ok=True)
    wav = os.path.join(outdir, f".beat-{slug}.wav"); audio(wav)
    out = os.path.join(outdir, f"aess-fb-ad-{slug}-60s.mp4"); ad = Ad(slug)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for f in range(N): p.stdin.write(ad.frame(f).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); os.remove(wav); print("done", out, [c for _, c in ad.m1])
