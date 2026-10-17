#!/usr/bin/env python3
"""AESS per-area 60s ALARM Facebook ad. Usage: python aess_alarm_ad.py <slug> [outdir]
Offer: $30 central station / $45 with app · $5 off every month per referral (refer 6 = $0 on the $30 plan)
· sign-up gift: free video doorbell OR first month free · monitored alarm may lower homeowners insurance."""
import os, sys, glob, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aess_promo as A
import aess_area_ad as AA
from aess_promo import (W, H, FPS, BLACK, BLUE, NAVY, WHITE, SKY, GREY, F_BLACK, F_BOLD, LOGO,
                        place, slam, bg, wipe, shake, prog, e_out, e_back, clamp, icon, _paste_clip)
from aess_area_ad import AREAS, txt, pill, photo, grad

N = 1800
RED = (230, 50, 60)
GREEN = (40, 200, 120)
IMGS = os.path.join(AA.SITE, "images")
G2 = os.environ.get("AESS_2GIG", "/home/user/aess/2gig")
GEAR = [("panel_edge.png", "SMART PANEL"), ("contact_dw20.png", "DOOR & WINDOW"), ("motion.jpg", "MOTION DETECTOR"),
        ("smoke.png", "SMOKE & HEAT"), ("glass.jpg", "GLASS-BREAK"), ("fob.jpg", "KEY FOB")]
_cards = {}
def gear_card(i):
    if i in _cards: return _cards[i]
    fn, label = GEAR[i]; w, h = 460, 400
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=40, fill=WHITE + (255,))
    path = os.path.join(G2, fn)
    if os.path.exists(path):
        im = Image.open(path).convert("RGBA")
        bb = im.getbbox()
        if bb: im = im.crop(bb)
        im.thumbnail((380, 270), Image.LANCZOS)
        card.alpha_composite(im, ((w - im.width) // 2, 24 + (270 - im.height) // 2))
    t = A.txt(label, 50, NAVY, F_BLACK, .86)
    if t.width > w - 30: t = A.txt(label, 40, NAVY, F_BLACK, .86)
    card.alpha_composite(t, ((w - t.width) // 2, h - t.height - 22))
    _cards[i] = card; return card

def fine(cv, s, y=1830):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        if A.txt(test, 30, GREY, F_BOLD, .95).width > W - 100 and cur: lines.append(cur); cur = w_
        else: cur = test
    lines.append(cur)
    for i, l in enumerate(lines): place(cv, A.txt(l, 30, GREY, F_BOLD, .95), W / 2, y + i * 40)

_b = None
def ref_badge():
    global _b
    if _b is None:
        b = Image.new("RGBA", (250, 250), (0, 0, 0, 0)); d = ImageDraw.Draw(b)
        d.ellipse((0, 0, 249, 249), fill=WHITE + (255,)); d.ellipse((12, 12, 237, 237), fill=BLUE + (255,))
        for word, y, sz in (("REFER", 70, 52), ("FRIENDS", 122, 44), ("$5 OFF", 180, 58)):
            t = A.txt(word, sz, WHITE, F_BLACK, .86); b.alpha_composite(t, ((250 - t.width) // 2, int(y - t.height / 2)))
        _b = b
    return _b
AA.badge = ref_badge  # montage badge becomes the referral badge

def alarm_photos(slug, cs):
    out = []
    root = "new-york-city" if slug == "nyc" else f"{slug}-ny"
    wh = os.path.join(IMGS, f"warehouse-alarm-system-installation-{root}.webp")
    want = [("alarm-keypad", "ALARM KEYPADS"), ("glass-break", "GLASS-BREAK SENSORS"), ("door-contact", "DOOR SENSORS"),
            ("panic-button", "PANIC BUTTONS"), ("crew-van", "ON OUR WAY"), ("integration-rack", "ONE CONNECTED SYSTEM")]
    files = glob.glob(os.path.join(AA.CS, f"*-{cs}-*.jpg"))
    for key, cap in want:
        m = sorted(f for f in files if key in os.path.basename(f))
        if m: out.append((m[0], cap))
    if os.path.exists(wh): out.insert(1, (wh, "ALARM INSTALLS"))
    return out[:6]

def phone_ui(t):
    w, h = 520, 1000
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=70, fill=(20, 20, 24, 255))
    d.rounded_rectangle((22, 22, w - 23, h - 23), radius=54, fill=NAVY + (255,))
    d.rounded_rectangle((w/2 - 70, 40, w/2 + 70, 66), radius=13, fill=(20, 20, 24, 255))
    hdr = A.txt("AESS SECURITY", 40, WHITE, F_BLACK, .9); im.alpha_composite(hdr, ((w - hdr.width) // 2, 100))
    armed = t > 0.35
    col = GREEN if armed else SKY
    d.ellipse((w/2 - 150, 190, w/2 + 150, 490), outline=col + (255,), width=16)
    sh = icon("alarm", 200, col); im.alpha_composite(sh, (int(w/2 - 100), 240))
    st = A.txt("ARMED AWAY" if armed else "DISARMED", 62, col, F_BLACK, .88); im.alpha_composite(st, ((w - st.width) // 2, 520))
    for i, lab in enumerate(("DISARM", "STAY", "AWAY")):
        x0 = 50 + i * 145; on = armed and lab == "AWAY"
        d.rounded_rectangle((x0, 630, x0 + 130, 700), radius=35, fill=(BLUE if on else (30, 45, 90)) + (255,))
        l = A.txt(lab, 30, WHITE, F_BLACK, .9); im.alpha_composite(l, (int(x0 + 65 - l.width / 2), int(665 - l.height / 2)))
    for i, (a, b2) in enumerate((("Front door closed", "6:41 PM"), ("System armed — Away", "6:42 PM"), ("Back door sensor OK", "6:42 PM"))):
        if t > 0.45 + i * 0.12:
            y = 740 + i * 70
            d.rounded_rectangle((44, y, w - 44, y + 58), radius=16, fill=(30, 45, 90, 255))
            l = A.txt(a, 24, WHITE, F_BOLD, .9); im.alpha_composite(l, (60, int(y + 29 - l.height / 2)))
            r = A.txt(b2, 22, SKY, F_BOLD, .9); im.alpha_composite(r, (int(w - 64 - r.width), int(y + 29 - r.height / 2)))
    return im

def person(col):
    p = Image.new("RGBA", (120, 120), (0, 0, 0, 0)); d = ImageDraw.Draw(p)
    d.ellipse((0, 0, 119, 119), fill=col + (255,))
    d.ellipse((40, 22, 80, 62), fill=WHITE + (255,)); d.pieslice((22, 64, 98, 140), 180, 360, fill=WHITE + (255,))
    return p

def plan_card(title, price, lines, hi):
    w, h = 900, 400
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=44, fill=(BLACK if hi else WHITE) + (255,))
    fg = WHITE if hi else BLACK
    t = A.txt(title, 64, fg, F_BLACK, .86); im.alpha_composite(t, (50, 40))
    p = A.txt(price, 130, SKY if hi else BLUE, F_BLACK, .86); im.alpha_composite(p, (50, 120))
    mo = A.txt("/MO", 50, fg, F_BLACK, .86); im.alpha_composite(mo, (60 + p.width, 120 + p.height - mo.height - 10))
    for i, l in enumerate(lines):
        lt = A.txt("✓ " + l if False else "•  " + l, 40, fg, F_BOLD, .95); im.alpha_composite(lt, (54, 290 + i * 50))
    return im

class AlarmAd:
    def __init__(self, slug):
        self.slug = slug; self.c = AREAS[slug]; self.m = alarm_photos(slug, self.c["cs"])

    def frame(self, f):
        c = self.c; NAME, SHORT = c["name"], c["short"]
        if f < 45:  # hook with siren flash
            cv = bg(BLACK)
            if (f // 4) % 2 == 0 and f > 6: cv.alpha_composite(Image.new("RGBA", (W, H), RED + (60,)))
            place(cv, txt("YOUR ALARM", 220, WHITE), W / 2, 800, *slam(f, 0))
            place(cv, txt("GOES OFF.", 250, RED), W / 2, 1050, *slam(f, 10))
            wipe(cv, f, 39, BLUE); return cv
        if f < 90:
            cv = bg(BLUE); lf = f - 45
            tick = A.txt(f"{SHORT} • 24/7 MONITORING • {SHORT} • 24/7 MONITORING • ", 150, (60, 105, 235), F_BLACK, .84)
            for (y, d) in ((330, -1), (1590, 1)):
                off = (lf * 14 * d) % max(1, tick.width // 2)
                _paste_clip(cv, tick, int(-off if d > 0 else off - tick.width // 2), y)
            place(cv, txt("WHO", 300, BLACK), W / 2, 860, *slam(lf, 2))
            place(cv, txt("ANSWERS?", 280, WHITE), W / 2, 1110, *slam(lf, 12))
            wipe(cv, f, 84, BLACK); return cv
        if f < 210:  # WE DO. 24/7 central station
            lf = f - 90; cv = bg(BLACK); sx, sy = shake(lf, 8, 8, 16)
            t = prog(lf, 0, 12)
            pulse = 1 + 0.06 * np.sin(lf / 3)
            place(cv, icon("alarm", 380, SKY), W / 2, 560, (e_back(t) if t > 0 else 0) * pulse, clamp(t * 2))
            place(cv, txt("WE DO.", 300, WHITE), W / 2 + sx, 960 + sy, *slam(lf, 8))
            place(cv, txt("24/7", 300, SKY), W / 2 + sx, 1220 + sy, *slam(lf, 18))
            t2 = prog(lf, 34, 9)
            place(cv, pill("PROFESSIONAL CENTRAL STATION", 62, BLACK, WHITE), W / 2, 1460 + 60 * (1 - e_out(t2)), 1, clamp(t2 * 2))
            place(cv, txt("THEY CALL YOU — AND SEND HELP", 58, GREY, F_BLACK, .9), W / 2, 1580, 1, clamp(prog(lf, 46, 8) * 2))
            wipe(cv, lf, 114, BLACK); return cv
        if f < 420:  # area alarm jobs
            lf = f - 210
            if lf < 30:
                cv = bg(BLACK)
                place(cv, txt("REAL ALARMS.", 200, WHITE), W / 2, 820, *slam(lf, 0))
                place(cv, txt(f"REAL {SHORT} JOBS.", 200, SKY), W / 2, 1060, *slam(lf, 8))
                return cv
            cv = AA.montage(self.m, f"AESS {c['inn']}", lf - 30, 180); wipe(cv, lf, 204, BLUE); return cv
        if f < 600:  # plans
            lf = f - 420; cv = bg(BLUE)
            place(cv, txt("PICK YOUR PLAN", 160, WHITE), W / 2, 300, *slam(lf, 0))
            t1 = e_out(prog(lf, 12, 12)); t2 = e_out(prog(lf, 30, 12))
            place(cv, plan_card("CENTRAL STATION", "$30", ["24/7 professional monitoring", "Police & fire dispatch"], False),
                  W / 2 + (1 - t1) * 900, 720, 1, clamp(t1 * 2))
            place(cv, plan_card("CENTRAL STATION + APP", "$45", ["Everything above", "Arm & disarm from your phone"], True),
                  W / 2 - (1 - t2) * 900, 1180, 1, clamp(t2 * 2))
            fine(cv, "Monthly monitoring. Installation quoted separately.", 1500)
            wipe(cv, lf, 174, NAVY); return cv
        if f < 720:  # app on phone
            lf = f - 600; cv = bg(NAVY)
            place(cv, txt("RUN IT FROM", 140, WHITE), W / 2, 220, *slam(lf, 0))
            place(cv, txt("YOUR PHONE.", 170, SKY), W / 2, 380, *slam(lf, 8))
            tp = prog(lf, 10, 14)
            place(cv, phone_ui(prog(lf, 20, 80)), W / 2, 1100 + 200 * (1 - e_out(tp)), 1, clamp(tp * 2))
            wipe(cv, lf, 114, WHITE); return cv
        if f < 960:  # referral counter
            lf = f - 720; cv = bg(WHITE)
            if lf < 36:
                place(cv, txt("REFER A FRIEND.", 170, BLACK), W / 2, 760, *slam(lf, 0))
                place(cv, txt("$5 OFF.", 300, BLUE), W / 2, 1010, *slam(lf, 8))
                place(cv, txt("EVERY MONTH.", 170, BLACK), W / 2, 1240, *slam(lf, 16))
                return cv
            k = min(6, max(0, int((lf - 40) // 22) + 1)) if lf >= 40 else 0
            price = 30 - 5 * k
            place(cv, txt("YOUR MONTHLY BILL", 80, GREY, F_BLACK, .9), W / 2, 330)
            st = prog(lf, 40 + (k - 1) * 22, 6) if k else 1
            col = GREEN if price == 0 else BLUE
            place(cv, txt(f"${price}", 460, col, F_BLACK, .9), W / 2, 640, 1 + 0.25 * (1 - e_out(st)) if k else 1)
            for i in range(6):
                x = W / 2 + (i - 2.5) * 150
                if i < k:
                    pt = prog(lf, 40 + i * 22, 8)
                    place(cv, person(BLUE), x, 1060, e_back(pt) if pt > 0 else 0, clamp(pt * 2))
                    place(cv, txt("-$5", 40, BLUE, F_BLACK, .9), x, 1150, 1, clamp(pt * 2))
                else:
                    ImageDraw.Draw(cv).ellipse((x - 60, 1000, x + 60, 1120), outline=(200, 205, 215, 255), width=6)
            if k >= 6:
                tt = prog(lf, 40 + 5 * 22 + 8, 10)
                place(cv, txt("REFER 6. PAY $0.", 170, BLACK), W / 2, 1380, *slam(lf, 40 + 5 * 22 + 8))
            fine(cv, "Based on the $30 plan. $5/mo credit per referred customer while they stay active; caps at $0. Not redeemable for cash.", 1700)
            wipe(cv, lf, 234, BLUE); return cv
        if f < 1080:  # sign-up gift choice
            lf = f - 960; cv = bg(BLUE)
            place(cv, txt("SIGN UP NOW", 170, WHITE), W / 2, 330, *slam(lf, 0))
            place(cv, txt("& PICK ONE FREE:", 110, BLACK), W / 2, 480, *slam(lf, 8))
            for i, (a, b2) in enumerate((("FREE VIDEO", "DOORBELL"), ("FIRST MONTH", "FREE"))):
                t = prog(lf, 18 + i * 12, 10); y = 820 + i * 520
                card = Image.new("RGBA", (880, 380), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
                d.rounded_rectangle((0, 0, 879, 379), radius=44, fill=(WHITE if i == 0 else BLACK) + (255,))
                fg = BLACK if i == 0 else WHITE
                ic = icon("intercom" if i == 0 else "alarm", 240, BLUE if i == 0 else SKY); card.alpha_composite(ic, (40, 70))
                l1 = A.txt(a, 92, fg, F_BLACK, .86); l2 = A.txt(b2, 92, BLUE if i == 0 else SKY, F_BLACK, .86)
                card.alpha_composite(l1, (310, 90)); card.alpha_composite(l2, (310, 200))
                place(cv, card, W / 2, y, e_back(t) if t > 0 else 0, clamp(t * 2))
                if i == 0 and t > 0.5: place(cv, txt("OR", 90, WHITE), W / 2, 1080, 1, clamp((t - .5) * 4))
            fine(cv, "With a new monitored alarm system. One gift per new customer.", 1720)
            wipe(cv, lf, 114, NAVY); return cv
        if f < 1200:  # insurance
            lf = f - 1080; cv = bg(NAVY); t = prog(lf, 0, 12)
            place(cv, icon("alarm", 300, SKY), W / 2, 450, e_back(t) if t > 0 else 0, clamp(t * 2))
            place(cv, txt("A MONITORED ALARM", 120, WHITE), W / 2, 760, *slam(lf, 8))
            place(cv, txt("CAN LOWER YOUR", 120, WHITE), W / 2, 900, *slam(lf, 14))
            place(cv, txt("HOME INSURANCE.", 170, SKY), W / 2, 1080, *slam(lf, 20))
            t2 = prog(lf, 34, 9)
            place(cv, pill("WE PROVIDE YOUR ALARM CERTIFICATE", 56, NAVY, WHITE), W / 2, 1320 + 60 * (1 - e_out(t2)), 1, clamp(t2 * 2))
            fine(cv, "Discounts vary by insurer and policy. Ask your insurance company.", 1720)
            wipe(cv, lf, 114, BLACK); return cv
        if f < 1320:  # WHAT YOU GET: real 2GIG equipment
            lf = f - 1200; cv = bg(NAVY)
            place(cv, txt("WHAT YOU GET", 170, WHITE), W / 2, 260, *slam(lf, 0))
            place(cv, txt("PRO-GRADE EQUIPMENT", 70, SKY, F_BLACK, .9), W / 2, 400, 1, clamp(prog(lf, 6, 6) * 2))
            for i in range(6):
                t = prog(lf, 12 + i * 6, 9)
                cx = W / 2 + (-245 if i % 2 == 0 else 245); cy = 700 + (i // 2) * 430
                place(cv, gear_card(i), cx, cy + 50 * (1 - e_out(t)), e_back(t, 1.7) if t > 0 else 0, clamp(t * 3))
            wipe(cv, lf, 114, NAVY); return cv
        if f < 1440:  # coverage
            lf = f - 1320; cv = bg(NAVY)
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
            wipe(cv, lf, 114, BLACK); return cv
        if f < 1560:  # hours + window
            lf = f - 1440; cv = bg(BLACK); sx, sy = shake(lf, 10, 8, 14)
            place(cv, txt("OPEN", 200, WHITE), W / 2 + sx, 640 + sy, *slam(lf, 0))
            place(cv, txt("7 DAYS", 330, SKY), W / 2 + sx, 910 + sy, *slam(lf, 8))
            t = prog(lf, 22, 9)
            place(cv, pill("8 AM – 8 PM", 96, BLACK, WHITE, pad=(60, 28)), W / 2, 1210 + 60 * (1 - e_out(t)), 1, clamp(t * 2))
            t2 = prog(lf, 32, 9)
            place(cv, pill("2-HOUR ARRIVAL WINDOWS", 64, WHITE, BLUE), W / 2, 1380 + 60 * (1 - e_out(t2)), 1, clamp(t2 * 2))
            place(cv, txt("LICENSED & INSURED", 70, GREY, F_BLACK, .9), W / 2, 1530, 1, clamp(prog(lf, 40, 8) * 2))
            wipe(cv, lf, 114, BLUE); return cv
        if f < 1680:  # close
            lf = f - 1560; cv = bg(BLUE); sx, sy = shake(lf, 20, 8, 14)
            place(cv, txt("PROTECT YOUR", 170, BLACK), W / 2 + sx, 700 + sy, *slam(lf, 0))
            place(cv, txt(SHORT, 300, WHITE), W / 2 + sx, 960 + sy, *slam(lf, 10))
            place(cv, txt("HOME.", 300, WHITE), W / 2 + sx, 1230 + sy, *slam(lf, 18))
            wipe(cv, lf, 114, WHITE); return cv
        lf = f - 1680; cv = bg(WHITE)
        t = prog(lf, 0, 12)
        place(cv, LOGO.resize((700, 700), Image.LANCZOS).convert("RGBA"), W / 2, 600, e_back(t, 1.9) if t > 0 else 0, clamp(t * 3))
        tb = prog(lf, 4, 12); place(cv, ref_badge(), W - 190, 250, e_back(tb) if tb > 0 else 0, clamp(tb * 2), rot=12)
        t2 = prog(lf, 12, 10)
        place(cv, pill("GET A FREE ALARM QUOTE  →", 72, WHITE, BLACK, pad=(60, 32)), W / 2, 1090 + 90 * (1 - e_out(t2)), 1, clamp(t2 * 2))
        t3 = prog(lf, 20, 10)
        place(cv, txt(c["phone"], 120, BLUE), W / 2, 1290, 1, clamp(t3 * 2))
        place(cv, txt(f"SERVING {NAME}", 64, BLACK, F_BLACK, .9), W / 2, 1410, 1, clamp(t3 * 2))
        place(cv, txt("$30 MONITORING  •  $45 WITH APP", 52, BLUE, F_BLACK, .9), W / 2, 1510, 1, clamp(t3 * 2))
        place(cv, txt("abstractenterprisessecuritysystems.com", 40, GREY, F_BOLD, .95), W / 2, 1610, 1, clamp(t3 * 2))
        place(cv, txt("OPEN 7 DAYS  •  8 AM – 8 PM", 46, BLACK, F_BOLD, .95), W / 2, 1700, 1, clamp(prog(lf, 34, 10) * 2))
        return cv

def audio(path, sr=44100):
    n = int(sr * N / FPS); out = np.zeros(n); t = lambda d: np.arange(int(sr * d)) / sr
    def add(sig, at, g=1.0):
        i = int(at * sr); j = min(n, i + len(sig))
        if 0 <= i < n: out[i:j] += sig[:j - i] * g
    tk = t(0.35); kick = np.sin(2*np.pi*(45 + 120*np.exp(-tk*30))*tk) * np.exp(-tk*9)
    th = t(0.06); hat = np.random.default_rng(1).standard_normal(len(th)) * np.exp(-th*70)
    ts = t(0.22); snare = (np.random.default_rng(2).standard_normal(len(ts)) * .7 + np.sin(2*np.pi*190*ts)) * np.exp(-ts*18)
    tb = t(0.48); notes = [55, 55, 65.4, 49]
    # siren-style riser in the hook (first 1.5s)
    tsr = t(1.5); siren = np.sin(2*np.pi*(700 + 300*np.sin(2*np.pi*2.5*tsr))*tsr) * 0.10 * np.exp(-tsr*0.8)
    add(siren, 0.0)
    for b in range(int(56 / 0.5)):
        at = b * 0.5; fq = notes[(b // 4) % 4]
        add(kick, at, 0.9); add(hat, at + 0.25, 0.22)
        if b % 2 == 1: add(snare, at, 0.35)
        if b % 8 == 7: add(hat, at + 0.125, 0.15); add(hat, at + 0.375, 0.15)
        add(np.sign(np.sin(2*np.pi*fq*tb)) * 0.5 * np.exp(-tb*4) * (1 - np.exp(-tb*200)), at, 0.22)
    def whoosh(at, dur=0.35, g=0.2):
        tw = t(dur); nz = np.random.default_rng(int(at*10)).standard_normal(len(tw))
        add(np.convolve(nz, np.ones(8)/8, mode="same") * np.sin(np.pi*tw/dur)**2, at - dur*0.6, g)
    for cu in [45, 90, 210, 240, 420, 600, 720, 960, 1080, 1200, 1320, 1440, 1560, 1680] + [240 + i * 30 for i in range(1, 6)]:
        whoosh(cu / FPS)
    tdg = t(0.25); ding = np.sin(2*np.pi*1320*tdg) * np.exp(-tdg*14) * 0.25
    for k in range(6): add(ding, (720 + 40 + k * 22) / FPS)
    ti = t(1.2); boom = np.sin(2*np.pi*(38 + 60*np.exp(-ti*8))*ti) * np.exp(-ti*3)
    for b in (98, 720 + 40 + 5 * 22 + 8, 1200, 1680): add(boom, b / FPS, 0.9)
    tc = t(2.5); add(sum(np.sin(2*np.pi*fq*tc) for fq in (220, 277.2, 329.6, 440)) * np.exp(-tc*1.2) * 0.12, 1680 / FPS)
    fl = int(sr * 1.0); out[-fl:] *= np.linspace(1, 0, fl)
    out = out / (np.max(np.abs(out)) + 1e-9) * 0.89
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    slug = sys.argv[1]; outdir = sys.argv[2] if len(sys.argv) > 2 else os.path.join(A.D, "alarm-ads")
    os.makedirs(outdir, exist_ok=True)
    wav = os.path.join(outdir, f".beat-{slug}.wav"); audio(wav)
    out = os.path.join(outdir, f"aess-fb-alarm-ad-{slug}-60s.mp4"); ad = AlarmAd(slug)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for f in range(N): p.stdin.write(ad.frame(f).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); os.remove(wav); print("done", out, [c for _, c in ad.m])
