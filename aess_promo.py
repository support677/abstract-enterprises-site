#!/usr/bin/env python3
"""AESS 15s vertical kinetic-type promo (1080x1920, 30fps) with a synthesized beat."""
import math, subprocess, wave, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

D = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, N = 1080, 1920, 30, 450
BLACK = (10, 10, 12); BLUE = (27, 74, 214); NAVY = (9, 22, 56); WHITE = (255, 255, 255)
SKY = (120, 160, 255); GREY = (150, 156, 170)
F_BLACK = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
F_BOLD = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
LOGO = Image.open(os.path.join(D, "aess-logo.png")).convert("RGB")

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def prog(f, start, dur): return clamp((f - start) / dur)
def e_out(t): return 1 - (1 - t) ** 3
def e_back(t, s=2.2):
    t -= 1
    return t * t * ((s + 1) * t + s) + 1
def e_inout(t): return 4*t*t*t if t < .5 else 1 - (-2*t + 2) ** 3 / 2

_cache = {}
def txt(s, size, fill, font=F_BLACK, squeeze=0.84):
    k = (s, size, fill, font, squeeze)
    if k in _cache: return _cache[k]
    fnt = ImageFont.truetype(font, size)
    l, t, r, b = fnt.getbbox(s)
    im = Image.new("RGBA", (r - l + 20, b - t + 20), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10 - l, 10 - t), s, font=fnt, fill=fill)
    if squeeze != 1:
        im = im.resize((max(1, int(im.width * squeeze)), im.height), Image.LANCZOS)
    _cache[k] = im
    return im

def place(cv, im, cx, cy, scale=1.0, alpha=1.0, rot=0, mblur=0):
    if alpha <= 0.01 or scale <= 0.01: return
    if scale != 1:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if rot:
        im = im.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1:
        a = im.getchannel("A").point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    if mblur:
        steps = 6
        ghost = im.copy(); ga = ghost.getchannel("A").point(lambda v: int(v * 0.28)); ghost.putalpha(ga)
        for i in range(1, steps + 1):
            cv.alpha_composite(ghost, (x - int(mblur * i / steps), y)) if 0 <= x else None
    cv.alpha_composite(im, (max(-10000, x), y)) if x >= 0 and y >= 0 and x + im.width <= W and y + im.height <= H else _paste_clip(cv, im, x, y)

def _paste_clip(cv, im, x, y):
    l, t = max(0, -x), max(0, -y)
    r, b = min(im.width, W - x), min(im.height, H - y)
    if r <= l or b <= t: return
    cv.alpha_composite(im.crop((l, t, r, b)), (x + l, y + t))

def slam(f, start, dur=9):
    """scale/alpha for a word slamming in"""
    t = prog(f, start, dur)
    if t <= 0: return 0, 0
    return 1.0 + 0.9 * (1 - e_back(t, 1.6)) if t < 1 else 1.0, clamp(t * 2.5)

def bg(c): return Image.new("RGBA", (W, H), c + (255,))

def wipe(cv, f, start, color, dur=6):
    """color panel sweeping up to reveal next scene"""
    t = prog(f, start, dur)
    if 0 < t < 1:
        h = int(H * e_out(t))
        ImageDraw.Draw(cv).rectangle((0, H - h, W, H), fill=color + (255,))

def shake(f, start, dur=8, amp=18):
    t = prog(f, start, dur)
    if 0 < t < 1:
        return int(math.sin(f * 2.7) * amp * (1 - t)), int(math.cos(f * 3.1) * amp * (1 - t))
    return 0, 0

# ---------------- icons ----------------
def icon(kind, s=200, col=WHITE):
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im); w = int(s * .07); c = col + (255,)
    if kind == "cam":
        d.rounded_rectangle((s*.12, s*.30, s*.78, s*.56), radius=int(s*.08), outline=c, width=w)
        d.ellipse((s*.66, s*.33, s*.86, s*.53), outline=c, width=w)
        d.line((s*.38, s*.56, s*.38, s*.74), fill=c, width=w); d.line((s*.22, s*.76, s*.54, s*.76), fill=c, width=w)
    elif kind == "intercom":
        d.rounded_rectangle((s*.30, s*.10, s*.70, s*.90), radius=int(s*.08), outline=c, width=w)
        d.ellipse((s*.42, s*.20, s*.58, s*.36), outline=c, width=w)
        for i in range(3):
            for j in range(3): d.ellipse((s*(.40+i*.08), s*(.46+j*.08), s*(.44+i*.08), s*(.50+j*.08)), fill=c)
        d.ellipse((s*.44, s*.72, s*.56, s*.84), fill=c)
    elif kind == "access":
        d.rounded_rectangle((s*.14, s*.36, s*.66, s*.74), radius=int(s*.06), outline=c, width=w)
        d.line((s*.24, s*.50, s*.44, s*.50), fill=c, width=w)
        for r in (.16, .26):
            d.arc((s*(.74-r), s*(.30-r), s*(.74+r), s*(.30+r)), 300, 60, fill=c, width=w)
    elif kind == "alarm":
        d.polygon([(s*.5, s*.10), (s*.84, s*.22), (s*.80, s*.58), (s*.5, s*.90), (s*.20, s*.58), (s*.16, s*.22)], outline=c, width=w)
        d.line([(s*.34, s*.50), (s*.46, s*.62), (s*.68, s*.38)], fill=c, width=w, joint="curve")
    elif kind == "lock":
        d.rounded_rectangle((s*.30, s*.08, s*.70, s*.92), radius=int(s*.08), outline=c, width=w)
        for i in range(3):
            for j in range(3): d.ellipse((s*(.38+i*.10), s*(.18+j*.10), s*(.44+i*.10), s*(.24+j*.10)), fill=c)
        d.ellipse((s*.40, s*.58, s*.60, s*.78), outline=c, width=w)
    elif kind == "cable":
        d.rounded_rectangle((s*.30, s*.14, s*.70, s*.56), radius=int(s*.04), outline=c, width=w)
        d.rectangle((s*.42, s*.06, s*.58, s*.16), outline=c, width=w)
        for i in range(4): d.line((s*(.38+i*.08), s*.24, s*(.38+i*.08), s*.36), fill=c, width=int(w*.6))
        d.line((s*.5, s*.56, s*.5, s*.92), fill=c, width=w)
    return im

TILES = [("cam", "CAMERAS", BLUE), ("intercom", "INTERCOMS", BLACK), ("access", "ACCESS", NAVY),
         ("lock", "SMART LOCKS", BLUE), ("alarm", "ALARMS", BLACK), ("cable", "CABLING", NAVY)]
_tile = {}
def tile(i):
    if i in _tile: return _tile[i]
    k, label, col = TILES[i]; tw, th = 420, 400
    im = Image.new("RGBA", (tw, th), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, tw - 1, th - 1), radius=44, fill=col + (255,))
    ic = icon(k, 210); im.alpha_composite(ic, ((tw - 210) // 2, 40))
    lb = txt(label, 58, WHITE, F_BLACK, 0.86); im.alpha_composite(lb, ((tw - lb.width) // 2, th - lb.height - 34))
    _tile[i] = im; return im

def pill(label, size, fg, bgc, pad=(44, 22), outline=None):
    t = txt(label, size, fg, F_BLACK, 0.88)
    w, h = t.width + pad[0] * 2, t.height + pad[1] * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=(bgc + (255,)) if bgc else None,
                        outline=(outline + (255,)) if outline else None, width=5)
    im.alpha_composite(t, (pad[0], pad[1])); return im

def van(s=1.0):
    w, h = int(150 * s), int(86 * s)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, h*.08, w*.74, h*.78), radius=int(10*s), fill=WHITE + (255,))
    d.rounded_rectangle((w*.70, h*.30, w*.98, h*.78), radius=int(10*s), fill=WHITE + (255,))
    d.rectangle((w*.78, h*.38, w*.92, h*.54), fill=BLUE + (255,))
    d.text((w*.08, h*.22), "AESS", font=ImageFont.truetype(F_BLACK, int(30*s)), fill=BLUE + (255,))
    for x in (.18, .80): d.ellipse((w*(x-.09), h*.64, w*(x+.09), h*.98), fill=BLACK + (255,))
    return im

def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
            u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1])

# ---------------- scenes ----------------
def frame(f):
    # S1 0-45 black: NEW YORK / NEVER / SLEEPS.
    if f < 45:
        cv = bg(BLACK)
        for word, st, y, col in (("NEW YORK", 0, 720, WHITE), ("NEVER", 8, 930, WHITE), ("SLEEPS.", 16, 1160, SKY)):
            s, a = slam(f, st); place(cv, txt(word, 205 if word == "NEW YORK" else 250, col), W/2, y, s, a)
        wipe(cv, f, 39, BLUE); return cv
    # S2 45-90 blue: ticker + NEITHER / DO WE.
    if f < 90:
        cv = bg(BLUE); lf = f - 45
        tick = txt("24/7 • SECURITY • 24/7 • SECURITY • 24/7 • SECURITY • ", 170, (60, 105, 235), F_BLACK, 0.84)
        for row, (y, d) in enumerate(((330, -1), (1590, 1))):
            off = (lf * 14 * d) % (tick.width // 2)
            _paste_clip(cv, tick, int(-off if d > 0 else off - tick.width // 2), y)
        t1 = e_out(prog(lf, 2, 9)); place(cv, txt("NEITHER", 270, BLACK), -400 + (W/2 + 400) * t1, 860, mblur=int(120*(1-t1)))
        t2 = e_out(prog(lf, 12, 9)); place(cv, txt("DO WE.", 300, WHITE), W + 400 - (W/2 + 400) * t2, 1110, mblur=int(120*(1-t2)))
        wipe(cv, f, 84, WHITE); return cv
    # S3 90-165 white: WE INSTALL + tiles
    if f < 165:
        cv = bg(WHITE); lf = f - 90
        s, a = slam(lf, 0); place(cv, txt("WE INSTALL", 190, BLACK), W/2, 300, s, a)
        for i in range(6):
            t = prog(lf, 8 + i * 5, 10)
            if t > 0:
                cx = W/2 + (-235 if i % 2 == 0 else 235); cy = 690 + (i // 2) * 440
                place(cv, tile(i), cx, cy + 60 * (1 - e_out(t)), e_back(t, 1.8) * 0.98, clamp(t * 3))
        wipe(cv, f, 159, BLUE); return cv
    # S4 165-240 blue: clock + route to your door
    if f < 240:
        cv = bg(BLUE); lf = f - 165; d = ImageDraw.Draw(cv)
        for i in range(-6, 14):  # faint street grid
            d.line((i * 140, 0, i * 140 + 700, H), fill=(44, 88, 224), width=6)
            d.line((0, i * 170, W, i * 170 - 300), fill=(44, 88, 224), width=6)
        mins = 480 + int(120 * e_inout(prog(lf, 10, 50)))
        hh, mm = mins // 60, mins % 60; clock = f"{hh if hh <= 12 else hh-12}:{mm:02d} AM"
        cp = pill(clock, 92, WHITE, BLACK, pad=(50, 24)); place(cv, cp, W/2, 250, *slam(lf, 0))
        place(cv, txt("YOU CALL", 70, WHITE, F_BLACK, 0.9), W/2, 400, 1, clamp(lf / 6))
        P = [(230, 620), (820, 760), (180, 1180), (800, 1420)]
        pts = [bez(*P, i / 80) for i in range(81)]
        prog_path = e_inout(prog(lf, 10, 50)); nshow = int(80 * prog_path)
        for i in range(0, 80, 3):
            if i <= nshow: d.line([pts[i], pts[min(i+1, 80)]], fill=WHITE + (255,), width=12)
        d.ellipse((P[0][0]-26, P[0][1]-26, P[0][0]+26, P[0][1]+26), fill=WHITE + (255,))
        place(cv, txt("AESS TECH", 54, WHITE, F_BLACK, .9), P[0][0] + 160, P[0][1] - 70)
        pin_t = prog(lf, 58, 8)
        if pin_t > 0:
            ps = e_back(pin_t); x, y = P[3]
            pin = Image.new("RGBA", (120, 160), (0, 0, 0, 0)); pd = ImageDraw.Draw(pin)
            pd.ellipse((0, 0, 120, 120), fill=BLACK + (255,)); pd.polygon([(18, 90), (102, 90), (60, 158)], fill=BLACK + (255,))
            pd.ellipse((38, 38, 82, 82), fill=WHITE + (255,))
            place(cv, pin, x, y - 70, ps)
            place(cv, txt("YOUR DOOR", 64, WHITE, F_BLACK, .9), x - 40, y + 60, 1, clamp(pin_t * 2))
        vx, vy = pts[nshow]; place(cv, van(1.25), vx, vy - 40)
        bt = prog(lf, 20, 10)
        place(cv, pill("2-HOUR ARRIVAL WINDOW", 64, BLUE, WHITE), W/2, 1700 + 80 * (1 - e_out(bt)), 1, clamp(bt * 2))
        wipe(cv, f, 234, BLACK); return cv
    # S5 240-300 black: INSTALLED stamp + LICENSED & INSURED
    if f < 300:
        cv = bg(BLACK); lf = f - 240; sx, sy = shake(lf, 6, 10, 26)
        t = prog(lf, 0, 7)
        if t > 0:
            stamp = pill("INSTALLED", 170, BLACK, WHITE, pad=(56, 30))
            place(cv, stamp, W/2 + sx, 820 + sy, 1 + 1.4 * (1 - e_out(t)), clamp(t * 2), rot=6)
        line = "LICENSED & INSURED"; n = int(len(line) * prog(lf, 16, 22))
        if n: place(cv, txt(line[:n], 110, SKY, F_BLACK, .86), W/2 + sx, 1120 + sy)
        if lf > 38:
            place(cv, txt("NYS LOW-VOLTAGE CONTRACTOR", 58, GREY, F_BOLD, .92), W/2, 1250, 1, clamp((lf - 38) / 8))
        wipe(cv, f, 294, NAVY); return cv
    # S6 300-345 navy: WE COVER + area pills
    if f < 345:
        cv = bg(NAVY); lf = f - 300
        place(cv, txt("WE COVER", 190, WHITE), W/2, 360, *slam(lf, 0))
        for i, lab in enumerate(("NYC", "LONG ISLAND", "HUDSON VALLEY")):
            t = prog(lf, 6 + i * 5, 9)
            place(cv, pill(lab, 112, WHITE, BLUE, pad=(60, 28)), W/2, 680 + i * 230, e_back(t) if t > 0 else 0, clamp(t * 3))
        small = [("BROOKLYN", "QUEENS", "BRONX"), ("MANHATTAN", "STATEN ISLAND"), ("NASSAU", "SUFFOLK", "WESTCHESTER"), ("ROCKLAND", "ORANGE", "PUTNAM")]
        for r, row in enumerate(small):
            pills = [pill(s, 40, SKY, None, pad=(26, 12), outline=SKY) for s in row]
            tw = sum(p.width for p in pills) + 20 * (len(pills) - 1); x = W/2 - tw/2
            for j, p in enumerate(pills):
                t = prog(lf, 20 + r * 3 + j, 6)
                place(cv, p, x + p.width/2, 1430 + r * 100, 1, clamp(t * 2)); x += p.width + 20
        wipe(cv, f, 339, BLUE); return cv
    # S7 345-390 blue: WE SECURE / EVERY DOOR.
    if f < 390:
        cv = bg(BLUE); lf = f - 345; sx, sy = shake(lf, 12, 8, 14)
        place(cv, txt("WE SECURE", 200, BLACK), W/2 + sx, 800 + sy, *slam(lf, 0))
        place(cv, txt("EVERY", 290, WHITE), W/2 + sx, 1030 + sy, *slam(lf, 8))
        place(cv, txt("DOOR.", 290, WHITE), W/2 + sx, 1290 + sy, *slam(lf, 13))
        wipe(cv, f, 384, WHITE); return cv
    # S8 390-450 white: logo + CTA
    cv = bg(WHITE); lf = f - 390
    t = prog(lf, 0, 12)
    lg = LOGO.resize((780, 780), Image.LANCZOS).convert("RGBA")
    place(cv, lg, W/2, 780, e_back(t, 1.9) if t > 0 else 0, clamp(t * 3))
    t2 = prog(lf, 12, 10)
    cta = pill("GET A FREE QUOTE  →", 78, WHITE, BLACK, pad=(64, 34))
    place(cv, cta, W/2, 1330 + 90 * (1 - e_out(t2)), 1, clamp(t2 * 2))
    t3 = prog(lf, 20, 10)
    place(cv, txt("(800) 486-0943", 110, BLUE), W/2, 1520, 1, clamp(t3 * 2))
    place(cv, txt("abstractenterprisessecuritysystems.com", 40, GREY, F_BOLD, .95), W/2, 1630, 1, clamp(t3 * 2))
    return cv

# ---------------- audio (120 BPM: beat = 0.5s = 15 frames) ----------------
def audio(path, sr=44100):
    n = int(sr * N / FPS); out = np.zeros(n)
    t = lambda d: np.arange(int(sr * d)) / sr
    def add(sig, at, g=1.0):
        i = int(at * sr); j = min(n, i + len(sig))
        if i < n: out[i:j] += sig[:j - i] * g
    tk = t(0.35); kick = np.sin(2*np.pi*(45 + 120*np.exp(-tk*30))*tk) * np.exp(-tk*9)
    th = t(0.06); hat = np.random.default_rng(1).standard_normal(len(th)) * np.exp(-th*70)
    ts = t(0.22); snare = (np.random.default_rng(2).standard_normal(len(ts)) * .7 + np.sin(2*np.pi*190*ts)) * np.exp(-ts*18)
    tb = t(0.48)
    bassnotes = [55, 55, 65.4, 49]  # A1 A1 C2 G1
    for b in range(30):
        at = b * 0.5
        if at >= 13.0: break
        add(kick, at, 0.9)
        add(hat, at + 0.25, 0.22)
        if b % 2 == 1: add(snare, at, 0.35)
        fq = bassnotes[(b // 4) % 4]
        add(np.sign(np.sin(2*np.pi*fq*tb)) * 0.5 * np.exp(-tb*4) * (1 - np.exp(-tb*200)), at, 0.22)
    def whoosh(at, dur=0.35, g=0.25):
        tw = t(dur); nz = np.random.default_rng(int(at*10)).standard_normal(len(tw))
        env = np.sin(np.pi * tw / dur) ** 2
        # crude rising filter: moving average shrinking over time
        sig = np.convolve(nz, np.ones(8)/8, mode="same") * env
        add(sig, at - dur * 0.6, g)
    for cut in (45, 90, 165, 240, 300, 345, 390): whoosh(cut / FPS)
    ti = t(1.2); boom = np.sin(2*np.pi*(38 + 60*np.exp(-ti*8))*ti) * np.exp(-ti*3)
    add(boom, 240 / FPS, 0.9); add(boom, 390 / FPS, 1.0)
    tc = t(1.6); chord = sum(np.sin(2*np.pi*fq*tc) for fq in (220, 277.2, 329.6, 440)) * np.exp(-tc*1.6) * 0.12
    add(chord, 390 / FPS)
    fade = np.ones(n); fl = int(sr * 0.6); fade[-fl:] = np.linspace(1, 0, fl); out *= fade
    out = out / (np.max(np.abs(out)) + 1e-9) * 0.89
    pcm = (out * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(pcm.tobytes())

if __name__ == "__main__":
    wav = os.path.join(D, "aess_beat.wav"); audio(wav)
    out = os.path.join(D, "aess-promo-15s.mp4")
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                          "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out],
                         stdin=subprocess.PIPE)
    for f in range(N):
        p.stdin.write(frame(f).convert("RGB").tobytes())
    p.stdin.close(); p.wait(); print("done", out)
