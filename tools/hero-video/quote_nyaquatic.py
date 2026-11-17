#!/usr/bin/env python3
"""Quote video: NYAquatic (Benjamin Stern), 145 Saw Mill River Rd, Yonkers - Wi-Fi coverage, invoice #3466.
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
IMG = "images/network/network-installation-westchester-county-"
P_AP = IMG + "wireless-access-point-ceiling-install.webp"
P_SW = IMG + "managed-poe-switch-rack-install.webp"
P_PULL = IMG + "two-tech-corridor-cable-pull.webp"
P_JH = IMG + "jhook-ceiling-pathway-bundles.webp"
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

def rings(d, cx, cy, t, col=(120, 160, 255)):
    for k in range(3):
        ph = (t * 1.2 + k / 3) % 1
        r = 30 + ph * 150; a = int(200 * (1 - ph))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=col + (a,), width=6)

def floor_plan(lf, n):
    """Animated 2-floor plan of the shop: 3 access points on floor 1, 1 on floor 2, coverage rings."""
    cv = bgc(NAVY); ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    place(cv, txt("YOUR SHOP. FULL COVERAGE.", 74, WHITE), W // 2, 170, *slam(lf, 0))
    floors = [("2ND FLOOR", 470, [(540,)]), ("1ST FLOOR", 1130, [(250,), (540,), (830,)])]
    order = 0
    for label, top, aps in floors:
        t = clamp(prog(lf, 6, 14))
        x0, x1, y0, y1 = 110, 970, top, top + 520
        d.rounded_rectangle((x0, y0, x0 + (x1 - x0) * e_out(t), y1), radius=28, outline=WHITE + (230,), width=8)
        place(cv, txt(label, 56, SKY), W // 2, top - 60, *slam(lf, 8))
        for (ax,) in aps:
            st = 22 + order * 9; order += 1
            sc, al = slam(lf, st)
            if al > 0:
                ay = top + 260
                rings(d, ax, ay, (lf - st) / FPS)
                d.ellipse((ax - 34, ay - 34, ax + 34, ay + 34), fill=WHITE + (int(255 * al),))
                d.ellipse((ax - 14, ay - 14, ax + 14, ay + 14), fill=BLUE + (int(255 * al),))
    cv.alpha_composite(ov)
    place(cv, pill("4 ACCESS POINTS · 3 DOWN · 1 UP", 46, WHITE, BLUE), W // 2, H - 150, *slam(lf, 58))
    return cv

SCENES = [
    dict(kind="hook", vo="Hi Benjamin, it's Abstract Enterprises Security Systems. Here's your Wi-Fi plan for NYAquatic on Saw Mill River Road."),
    dict(kind="problem", vo="No more dead spots dropping your live streams. Strong, steady Wi-Fi in every corner of both floors."),
    dict(kind="plan", vo="Here's the layout we mapped on our walkthrough today. Three access points on the first floor, and one on the second floor."),
    dict(kind="gear", vo="You're getting Ubiquiti UniFi WiFi 7 access points, each on its own dedicated Cat6 cable, all powered by a Ubiquiti PoE switch at your network location."),
    dict(kind="setup", vo="We mount every access point on the ceiling, run and terminate every cable, set up the network, and test it before we leave."),
    dict(kind="price", vo="Your total is two thousand, five hundred seventy-two dollars and sixty-four cents, tax included."),
    dict(kind="next", vo="Pay the invoice from the link we sent you, and we'll lock in your install date with a two-hour arrival window."),
    dict(kind="end", vo="Questions? Just text us at nine one four, four three six, five two one eight. We'll get your shop streaming without a hiccup."),
]

def scene(sc, lf, n):
    k = sc["kind"]
    if k == "hook":
        cv = kb(P_AP, lf / n, 0.6)
        stack(cv, ["BENJAMIN,", "YOUR WI-FI", "PLAN IS", "READY."], lf, [SKY, WHITE, WHITE, WHITE], size=150, cy=H // 2 - 80)
        place(cv, pill("NYAQUATIC · YONKERS", 50, WHITE, BLUE), W // 2, H - 260, *slam(lf, 32))
    elif k == "problem":
        cv = bgc(BLUE)
        stack(cv, ["DEAD SPOTS?", "DROPPED", "STREAMS?", "NOT ANYMORE."], lf, [WHITE, WHITE, WHITE, BLACK], size=140)
    elif k == "plan":
        cv = floor_plan(lf, n)
    elif k == "gear":
        cv = kb(P_SW, lf / n, 0.72)
        place(cv, txt("WHAT YOU GET", 90, SKY), W // 2, 260, *slam(lf, 0))
        items = ["4× UBIQUITI UNIFI", "WIFI 7 ACCESS POINTS", "OWN CAT6 RUN EACH", "UBIQUITI PoE SWITCH"]
        for i, it in enumerate(items):
            place(cv, pill(it, 54, WHITE if i != 1 else BLACK, BLUE if i != 1 else WHITE), W // 2, 620 + i * 210, *slam(lf, 8 + i * 9))
    elif k == "setup":
        seg = n / 2; src = P_PULL if lf < seg else P_JH
        cv = kb(src, (lf % seg) / seg, 0.62)
        stack(cv, ["MOUNTED.", "WIRED.", "SET UP.", "TESTED."], lf, [WHITE, WHITE, WHITE, SKY], size=160)
    elif k == "price":
        cv = bgc(WHITE)
        stack(cv, ["YOUR TOTAL"], lf, [BLACK], size=110, cy=H // 2 - 220)
        place(cv, txt("$2,572.64", 230, BLUE), W // 2, H // 2, *slam(lf, 8))
        place(cv, pill("TAX INCLUDED · INVOICE #3466", 44, WHITE, BLACK), W // 2, H // 2 + 230, *slam(lf, 16))
    elif k == "next":
        cv = bgc(NAVY)
        stack(cv, ["PAY THE", "INVOICE."], lf, [WHITE, WHITE], size=150, cy=H // 2 - 300)
        place(cv, pill("WE LOCK IN YOUR DATE", 56, WHITE, BLUE), W // 2, H // 2 + 20, *slam(lf, 14))
        place(cv, txt("2-HOUR ARRIVAL WINDOW", 74, SKY), W // 2, H // 2 + 200, *slam(lf, 22))
    else:
        cv = bgc(WHITE)
        lg = LOGO.convert("RGBA"); lg = lg.resize((520, int(lg.height * 520 / lg.width)), Image.LANCZOS)
        place(cv, lg, W // 2, 520, *slam(lf, 0))
        place(cv, pill("QUESTIONS? TEXT US", 60, WHITE, BLACK), W // 2, 1000, *slam(lf, 8))
        place(cv, txt("(914) 436-5218", 130, BLUE), W // 2, 1180, *slam(lf, 14))
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
    if SCENES[2]["kind"] == "plan": lens[2] = max(lens[2], 80)
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
