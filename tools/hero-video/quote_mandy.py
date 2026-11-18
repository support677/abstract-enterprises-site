#!/usr/bin/env python3
"""Quote video: Mandy, 668 Eastern Pkwy, Brooklyn - 4 or 6 camera home system.
Vertical 1080x1920 kinetic type + voiceover, same style as the other /quote/ videos."""
import math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw

D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import aess_promo as A
import hero_video as HV

W, H, FPS = 1080, 1920, 30
A.W, A.H = W, H; HV.W, HV.H = W, H
from aess_promo import BLACK, BLUE, NAVY, WHITE, SKY, F_BLACK, F_BOLD, LOGO, place, slam, prog, e_out, clamp

SITE = os.path.abspath(os.path.join(D, "..", ".."))
IMG = "images/cctv-installation/"
P_SOF = IMG + "cctv-installation-brooklyn-installer-fitting-dome-camera-under-brick-house-soffit.webp"
P_BRICK = IMG + "cctv-installation-nyc-installer-mounting-bullet-camera-on-brick-wall.webp"
P_MON = IMG + "cctv-installation-long-island-office-monitor-four-camera-split.webp"
P_REC = IMG + "cctv-installation-nyc-recorder-live-view-time-stamp.webp"
P_CAM = "images/cam-eyeball-white.png"
SR = HV.SR

def txt(s, size, fill, font=F_BLACK, maxw=W - 120): return HV.txt(s, size, fill, font, 0.84, maxw)
def pill(s, size, fg, bg): return HV.pill(s, size, fg, bg)
def bgc(c): return Image.new("RGBA", (W, H), c + (255,))

_ph = {}
def kb(src, t, dark=0.55):
    if src not in _ph:
        im = Image.open(os.path.join(SITE, src)).convert("RGB")
        r = max(W * 1.15 / im.width, H * 1.15 / im.height)
        _ph[src] = im.resize((int(im.width * r), int(im.height * r)), Image.LANCZOS)
    im = _ph[src]; z = 1 + 0.10 * t
    cw, ch = int(W * 1.12 / z), int(H * 1.12 / z)
    x0 = (im.width - cw) // 2 + int(30 * t); y0 = (im.height - ch) // 2
    fr = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR).convert("RGBA")
    fr.alpha_composite(Image.new("RGBA", (W, H), (9, 22, 56, int(255 * dark))))
    return fr

def stack(cv, words, lf, colors, size=150, cy=None, every=7, gap=14, start=0):
    ims = [txt(w, size, colors[i % len(colors)]) for i, w in enumerate(words)]
    tot = sum(i.height for i in ims) + gap * (len(ims) - 1); y = (cy or H // 2) - tot // 2
    for i, im in enumerate(ims):
        place(cv, im, W // 2, y + im.height // 2, *slam(lf, start + i * every)); y += im.height + gap

def cone(d, cx, cy, ang, t, al, col=(120, 160, 255)):
    L = 150 + 40 * math.sin(t * 3)
    a1, a2 = math.radians(ang - 28), math.radians(ang + 28)
    d.polygon([(cx, cy), (cx + L * math.cos(a1), cy + L * math.sin(a1)), (cx + L * math.cos(a2), cy + L * math.sin(a2))],
              fill=col + (int(90 * al),))

def house_plan(lf, n):
    """Animated home: 2 outdoor cams on the facade, 2 indoor; then +2 for the 6-camera option."""
    cv = bgc(NAVY); ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    place(cv, txt("YOUR HOME. COVERED.", 80, WHITE), W // 2, 170, *slam(lf, 0))
    t = e_out(clamp(prog(lf, 4, 16)))
    x0, x1, y0, y1 = 140, 940, 620, 1380
    d.polygon([(x0 - 40, y0), (W // 2, y0 - 260 * t), (x1 + 40, y0)], outline=WHITE + (230,), width=8)
    d.rectangle((x0, y0, x0 + (x1 - x0) * t, y1), outline=WHITE + (230,), width=8)
    d.rectangle((480, 1140, 600, 1380), outline=SKY + (200,), width=6)
    place(cv, txt("668 EASTERN PKWY", 50, SKY), W // 2, 820, *slam(lf, 10))
    cams = [(x0 - 10, 700, 200, "OUT", 20), (x1 + 10, 700, -20, "OUT", 28),
            (330, 1000, 30, "IN", 36), (750, 1000, 150, "IN", 44),
            (330, 1300, 330, "+", 60), (750, 1300, 210, "+", 66)]
    for cx, cy, ang, kind, st in cams:
        sc, al = slam(lf, st)
        if al <= 0: continue
        col = (255, 200, 80) if kind == "+" else (120, 160, 255)
        cone(d, cx, cy, ang, (lf - st) / FPS, al, col)
        d.ellipse((cx - 30, cy - 30, cx + 30, cy + 30), fill=WHITE + (int(255 * al),))
        d.ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=(BLUE if kind != "+" else (230, 150, 20)) + (int(255 * al),))
    cv.alpha_composite(ov)
    place(cv, pill("2 OUTSIDE · WEATHERPROOF", 46, WHITE, BLUE), W // 2, 1540, *slam(lf, 30))
    place(cv, pill("6-CAMERA OPTION: +2 MORE", 46, BLACK, WHITE), W // 2, 1680, *slam(lf, 64))
    return cv

SCENES = [
    dict(kind="hook", vo="Hi Mandy, it's Abstract Enterprises Security Systems. Here's the camera quote you asked for, for your home on Eastern Parkway."),
    dict(kind="problem", vo="You want to see who's at your door and around your home, day or night, right from your phone."),
    dict(kind="plan", vo="Here's the plan. Two weatherproof cameras outside, two inside. Or go with six cameras for even more coverage."),
    dict(kind="gear", vo="You get five megapixel fixed lens cameras, a 4K recorder, a monitor, all the wiring up to a hundred feet per camera, and full professional installation."),
    dict(kind="setup", vo="We mount every camera, run and hide the wire, set up the recorder, and put the cameras on your phone before we leave."),
    dict(kind="price", vo="Four cameras, one thousand three hundred sixty-three dollars, plus tax. Six cameras, one thousand eight hundred forty-seven dollars, plus tax. Installation included."),
    dict(kind="next", vo="Text us four or six to pick your system. We send your secure pay link, and once it's paid, we lock in your install date with a two-hour arrival window."),
    dict(kind="end", vo="Questions? Text us at nine one seven, two six eight, three nine five one. Let's get your home protected."),
]

def scene(sc, lf, n):
    k = sc["kind"]
    if k == "hook":
        cv = kb(P_SOF, lf / n, 0.6)
        stack(cv, ["MANDY,", "YOUR CAMERA", "QUOTE IS", "READY."], lf, [SKY, WHITE, WHITE, WHITE], size=150, cy=H // 2 - 80)
        place(cv, pill("EASTERN PARKWAY · BROOKLYN", 48, WHITE, BLUE), W // 2, H - 260, *slam(lf, 32))
    elif k == "problem":
        cv = bgc(BLUE)
        stack(cv, ["SEE YOUR", "DOOR.", "DAY OR NIGHT.", "FROM YOUR PHONE."], lf, [WHITE, WHITE, WHITE, BLACK], size=130)
    elif k == "plan":
        cv = house_plan(lf, n)
    elif k == "gear":
        cv = kb(P_MON, lf / n, 0.74)
        place(cv, txt("WHAT YOU GET", 90, SKY), W // 2, 240, *slam(lf, 0))
        items = ["5MP FIXED-LENS CAMERAS", "4K RECORDER + MONITOR", "WIRING UP TO 100 FT EACH", "PRO INSTALLATION"]
        for i, it in enumerate(items):
            place(cv, pill(it, 52, WHITE if i != 1 else BLACK, BLUE if i != 1 else WHITE), W // 2, 600 + i * 210, *slam(lf, 8 + i * 9))
    elif k == "setup":
        seg = n / 2; src = P_BRICK if lf < seg else P_REC
        cv = kb(src, (lf % seg) / seg, 0.62)
        stack(cv, ["MOUNTED.", "WIRED.", "SET UP.", "ON YOUR PHONE."], lf, [WHITE, WHITE, WHITE, SKY], size=150)
    elif k == "price":
        cv = bgc(WHITE)
        stack(cv, ["YOUR OPTIONS"], lf, [BLACK], size=110, cy=360)
        place(cv, pill("4 CAMERAS", 60, WHITE, BLACK), W // 2, 620, *slam(lf, 6))
        place(cv, txt("$1,363", 200, BLUE), W // 2, 800, *slam(lf, 10))
        place(cv, pill("6 CAMERAS", 60, WHITE, BLACK), W // 2, 1080, *slam(lf, 18))
        place(cv, txt("$1,847", 200, BLUE), W // 2, 1260, *slam(lf, 22))
        place(cv, pill("PLUS TAX · INSTALLATION INCLUDED", 44, WHITE, BLUE), W // 2, 1520, *slam(lf, 30))
    elif k == "next":
        cv = bgc(NAVY)
        stack(cv, ["TEXT US", "“4” OR “6”"], lf, [WHITE, SKY], size=150, cy=H // 2 - 300)
        place(cv, pill("PAY = INSTALL DATE LOCKED", 52, WHITE, BLUE), W // 2, H // 2 + 20, *slam(lf, 14))
        place(cv, txt("2-HOUR ARRIVAL WINDOW", 74, SKY), W // 2, H // 2 + 200, *slam(lf, 22))
    else:
        cv = bgc(WHITE)
        lg = LOGO.convert("RGBA"); lg = lg.resize((520, int(lg.height * 520 / lg.width)), Image.LANCZOS)
        place(cv, lg, W // 2, 520, *slam(lf, 0))
        place(cv, pill("QUESTIONS? TEXT US", 60, WHITE, BLACK), W // 2, 1000, *slam(lf, 8))
        place(cv, txt("(917) 268-3951", 130, BLUE), W // 2, 1180, *slam(lf, 14))
        place(cv, txt("Abstract Enterprises Security Systems", 46, BLACK, F_BOLD, W - 100), W // 2, 1360, *slam(lf, 20))
    return cv

def wipe(cv, lf, color):
    t = prog(lf, 0, 7)
    if 0 < t < 1:
        ImageDraw.Draw(cv).rectangle((0, int(H * e_out(t)), W, H), fill=color + (255,))

def main(out):
    vos = [HV.tts(s["vo"]) for s in SCENES]
    lead, tail = 0.35, 0.5
    lens = [max(int((lead + len(v) / SR + tail) * FPS), 60) for v in vos]
    if SCENES[2]["kind"] == "plan": lens[2] = max(lens[2], 100)
    total = sum(lens); n = int(total / FPS * SR) + SR // 2
    starts = np.cumsum([0] + lens[:-1])
    mus = HV.music(n, [s / FPS for s in starts[1:]])
    duck = np.ones(n) * .40; voice = np.zeros(n)
    for s, v in zip(starts, vos):
        i = int((s / FPS + lead) * SR); voice[i:i + len(v)] += v[:max(0, n - i)]
        duck[max(0, i - 3000): i + len(v) + 4000] = .12
    duck = np.convolve(duck, np.ones(2400) / 2400, mode="same")
    fade = np.ones(n); fl = int(SR * .7); fade[-fl:] = np.linspace(1, 0, fl)
    mix = (mus * duck + voice) * fade; mix = mix / (np.max(np.abs(mix)) + 1e-9) * .92
    with wave.open(out + ".wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    proc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                             "-r", str(FPS), "-i", "-", "-i", out + ".wav", "-c:v", "libx264", "-preset", "veryfast",
                             "-crf", "26", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-shortest",
                             "-movflags", "+faststart", out + ".mp4"], stdin=subprocess.PIPE)
    poster = None
    for si, (sc, ln) in enumerate(zip(SCENES, lens)):
        for lf in range(ln):
            cv = scene(sc, lf, ln)
            if si: wipe(cv, lf, [BLUE, BLACK, NAVY, WHITE][si % 4])
            if si == 0 and lf == min(ln - 1, 45): poster = cv.convert("RGB")
            proc.stdin.write(cv.convert("RGB").tobytes())
    proc.stdin.close(); proc.wait(); os.remove(out + ".wav")
    # poster with play button
    d = ImageDraw.Draw(poster); cx, cy, r = W // 2, H // 2 + 380, 120
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(27, 74, 214))
    d.polygon([(cx - 40, cy - 60), (cx - 40, cy + 60), (cx + 65, cy)], fill=(255, 255, 255))
    poster.save(out + ".jpg", quality=84)
    print(out, round(total / FPS, 1), "s")

if __name__ == "__main__":
    main(sys.argv[1])
