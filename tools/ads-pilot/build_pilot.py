#!/usr/bin/env python3
"""Builds the AESS Brooklyn security-camera neighborhood pilot:
   - Google Ads Editor import CSV (all campaigns PAUSED)
   - /lp/ landing pages in the site repo (noindex)
   - validation report (char limits, banned words)"""
import csv, html, os, re, sys

SITE = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
BASE = "https://abstractenterprisessecuritysystems.com"

# slug, display name, short name (for tight headlines), ZIPs (canonical names resolved via Google Ads geo API), full neighborhood page
HOODS = [
    ("williamsburg", "Williamsburg", "Williamsburg", [("11211", 9004347), ("11249", 9073497), ("11206", 9004342)]),
    ("bushwick", "Bushwick", "Bushwick", [("11221", 9004357), ("11237", 9004372)]),
    ("bed-stuy", "Bed-Stuy", "Bed-Stuy", [("11216", 9004352), ("11233", 9004368)]),
    ("crown-heights", "Crown Heights", "Crown Heights", [("11213", 9004349), ("11225", 9004361)]),
    ("east-flatbush", "East Flatbush", "East Flatbush", [("11203", 9004339)]),
    ("flatbush", "Flatbush", "Flatbush", [("11226", 9004362)]),
    ("canarsie", "Canarsie", "Canarsie", [("11236", 9004371)]),
    ("east-new-york", "East New York", "East New York", [("11207", 9004343), ("11208", 9004344)]),
    ("park-slope", "Park Slope", "Park Slope", [("11215", 9004351), ("11217", 9004353)]),
    ("bay-ridge", "Bay Ridge", "Bay Ridge", [("11209", 9004345)]),
    ("sheepshead-bay", "Sheepshead Bay", "Sheepshead Bay", [("11229", 9004364), ("11235", 9004370)]),
    ("borough-park", "Borough Park", "Borough Park", [("11219", 9004355)]),
]
# existing full-blueprint neighborhood pages the LP links up to
FULLPAGE = {
    "williamsburg": "security-camera-installation-williamsburg-brooklyn-ny",
    "bushwick": "security-camera-installation-bushwick-brooklyn-ny",
    "bed-stuy": "security-camera-installation-bedford-stuyvesant-brooklyn-ny",
    "crown-heights": "security-camera-installation-crown-heights-brooklyn-ny",
    "east-flatbush": "security-camera-installation-east-flatbush-brooklyn-ny",
    "flatbush": "security-camera-installation-flatbush-brooklyn-ny",
    "canarsie": "security-camera-installation-canarsie-brooklyn-ny",
    "east-new-york": "security-camera-installation-east-new-york-brooklyn-ny",
    "park-slope": "security-camera-installation-park-slope-brooklyn-ny",
    "bay-ridge": "security-camera-installation-bay-ridge-brooklyn-ny",
    "sheepshead-bay": "security-camera-installation-sheepshead-bay-brooklyn-ny",
    "borough-park": "security-camera-installation-borough-park-brooklyn-ny",
    "brooklyn": "security-camera-installation-brooklyn-ny",
}
ALT_NAMES = {"bed-stuy": ["bedford stuyvesant", "bed stuy"], "east-new-york": ["east new york"],
             "borough-park": ["borough park", "boro park"]}
BROOKLYN = ("brooklyn", "Brooklyn", "Brooklyn", [("Brooklyn", 1022762)])

BUDGET_HOOD = 10.00   # placeholder daily budgets -- Anwar sets real numbers
BUDGET_CATCH = 20.00
MAX_CPC = 6.00        # placeholder ad group default bid (Manual CPC)

BANNED = [r"same[- ]?day", r"\$", r"\bprice", r"\bcheap", r"\bfree\b", r"\d{3}[-) ]\d{3}-\d{4}", r"today\b"]

def pick(options, limit):
    for o in options:
        if len(o) <= limit:
            return o
    raise ValueError(f"nothing fits {limit}: {options}")

GROUPS = {
  "Install": dict(
    lp="security-camera-installation", svc="Security Camera Installation",
    h1=lambda n: pick([f"{n} Security Camera Install", f"{n} Camera Installation", f"{n} Camera Installers", f"{n} Camera Install", f"{n} Cameras Installed"], 30),
    heads=["Licensed & Insured Installers", "25+ Years in Security", "4K HD Camera Systems",
           "View Cameras on Your Phone", "Homes, Stores & Buildings", "Book Online 24/7",
           "Brooklyn Local Installers", "Indoor & Outdoor Cameras", "Night Vision Cameras",
           "NVR Recording & Playback", "2-Hour Arrival Windows", "No Monthly Fees", "Get Your Camera Quote",
           "NYS Licensed Contractor"],
    descs=lambda n: [
        f"Camera systems installed for {n} homes, shops and buildings. Book online.",
        "Licensed & insured NYS low-voltage contractor with 25+ years installing cameras.",
        "4K cameras, NVR recording and phone-app viewing set up by our own install crew.",
        "Tell us how many cameras you need. We confirm a 2-hour arrival window that fits you."],
    kws=lambda ns: [f"security camera installation {x}" for x in ns] + [f"camera installation {x}" for x in ns] +
        [f"cctv installation {x}" for x in ns] + [f"security camera installer {x}" for x in ns] +
        ["security camera installation", "security camera installation near me", "camera installation near me",
         "security camera installers near me", "cctv installation near me", "home security camera installation"]),
  "Repair": dict(
    lp="security-camera-repair", svc="Security Camera Repair",
    h1=lambda n: pick([f"{n} Security Camera Repair", f"{n} Camera Repair", f"Camera Repair in {n}"], 30),
    heads=["Camera System Not Working?", "DVR & NVR Troubleshooting", "Cameras Offline? We Fix It",
           "Repairs on Most Camera Brands", "Licensed & Insured Techs", "25+ Years in Security",
           "Phone App Setup & Fixes", "2-Hour Arrival Windows", "Book Online 24/7", "Brooklyn Local Techs",
           "Upgrade an Old System", "Recorder & Camera Repair", "No Picture? No Playback?", "NYS Licensed Contractor"],
    descs=lambda n: [
        f"Camera repair for {n} homes and businesses: offline cameras, recorders, apps.",
        "Licensed & insured NYS low-voltage contractor with 25+ years fixing camera systems.",
        "We troubleshoot cameras, DVRs, NVRs, cabling and phone-app viewing on most brands.",
        "Book your repair visit online and get a confirmed 2-hour arrival window."],
    kws=lambda ns: [f"security camera repair {x}" for x in ns] + [f"camera repair {x}" for x in ns] +
        [f"cctv repair {x}" for x in ns] +
        ["security camera repair", "security camera repair near me", "cctv repair near me",
         "camera system repair", "dvr repair", "nvr repair", "security camera not working"]),
  "Business": dict(
    lp="business-security-cameras", svc="Business Security Cameras",
    h1=lambda n: pick([f"{n} Business Cameras", f"{n} Commercial CCTV", f"{n} Store Cameras"], 30),
    heads=["Store & Restaurant Cameras", "Office & Warehouse Cameras", "Bodega Camera Systems",
           "Watch Your Shop From Anywhere", "NYS Licensed Contractor", "25+ Years in Security",
           "4K Commercial Cameras", "Multi-Location Viewing", "Building & Lobby Cameras",
           "2-Hour Arrival Windows", "Book Online 24/7", "Insured for Commercial Work",
           "Cameras for Landlords", "Retail Theft Deterrence"],
    descs=lambda n: [
        f"Commercial camera systems for {n} stores, restaurants, offices and buildings.",
        "Licensed & insured NYS low-voltage contractor with 25+ years of commercial installs.",
        "4K cameras, recorders and remote viewing so owners can check in from any phone.",
        "Tell us about your space and get a quote. Install visits in 2-hour arrival windows."],
    kws=lambda ns: [f"business security cameras {x}" for x in ns] + [f"commercial camera installation {x}" for x in ns] +
        [f"commercial cctv {x}" for x in ns] +
        ["business security camera installation", "commercial security camera installation",
         "commercial cctv installation", "store security cameras", "restaurant security cameras",
         "security cameras for business near me"]),
  "Doorbell": dict(
    lp="doorbell-camera-installation", svc="Doorbell Camera Installation",
    h1=lambda n: pick([f"{n} Doorbell Cameras", f"{n} Video Doorbells", f"Doorbells in {n}"], 30),
    heads=["Video Doorbell Installation", "All Major Doorbell Brands", "See Who's at the Door",
           "Wired Doorbell Installs", "Doorbell + Camera Packages", "Licensed & Insured",
           "25+ Years in Security", "Phone Alerts & Two-Way Talk", "2-Hour Arrival Windows",
           "Book Online 24/7", "Brooklyn Local Installers", "House & Apartment Doorbells",
           "Package Theft Protection", "NYS Licensed Contractor"],
    descs=lambda n: [
        f"Video doorbell installation for {n} houses, brownstones and apartment doors.",
        "Licensed & insured NYS low-voltage contractor with 25+ years in security.",
        "See and talk to visitors from your phone. Add cameras to cover the whole property.",
        "Book your doorbell install online and get a confirmed 2-hour arrival window."],
    kws=lambda ns: [f"doorbell camera installation {x}" for x in ns] + [f"video doorbell installation {x}" for x in ns] +
        ["doorbell camera installation", "video doorbell installation", "doorbell camera installation near me",
         "ring doorbell installation", "doorbell installation near me", "video doorbell installer"]),
}

NEGATIVES = ["diy", "how to", "jobs", "job", "hiring", "salary", "career", "training", "course", "school",
             "amazon", "best buy", "home depot", "walmart", "costco", "dash cam", "dashcam", "car camera",
             "reddit", "youtube", "software download", "spy", "hidden camera", "toy", "rental", "used",
             "manual", "reset password", "login", "customer service", "adt", "simplisafe", "vivint"]
# never advertise in places he doesn't serve
NEGATIVES += ["new jersey", "nj", "connecticut", "philadelphia"]

ROWS, ISSUES = [], []
HDR = ["Campaign", "Campaign Type", "Networks", "Budget", "Budget type", "Bid Strategy Type", "Campaign Status",
       "Targeting method", "Exclusion method", "Language", "Ad Group", "Max CPC", "Ad Group Status",
       "Keyword", "Criterion Type", "Location", "Location ID", "Ad type", "Status"] + \
      [f"Headline {i}" for i in range(1, 16)] + ["Headline 1 position"] + \
      [f"Description {i}" for i in range(1, 5)] + ["Final URL", "Path 1", "Path 2", "Labels"]

def row(**k):
    r = {h: "" for h in HDR}
    for a, v in k.items():
        r[a.replace("_", " ")] = v
    ROWS.append(r)

def check(text, limit, where):
    if len(text) > limit:
        ISSUES.append(f"TOO LONG ({len(text)}>{limit}) {where}: {text}")
    for b in BANNED:
        if re.search(b, text, re.I):
            ISSUES.append(f"BANNED '{b}' {where}: {text}")

def lp_url(slug, grp):
    return f"{BASE}/lp/{GROUPS[grp]['lp']}-{slug}"

def build_campaign(h, catch_all=False):
    slug, name, short, zips = h
    camp = "AESS | Cameras | Brooklyn | Rest of Brooklyn" if catch_all else f"AESS | Cameras | Brooklyn | {name}"
    row(Campaign=camp, Campaign_Type="Search", Networks="Google search", Budget=f"{BUDGET_CATCH if catch_all else BUDGET_HOOD:.2f}",
        Budget_type="Daily", Bid_Strategy_Type="Manual CPC", Campaign_Status="Paused",
        Targeting_method="Location of presence", Exclusion_method="Location of presence", Language="en",
        Labels="Neighborhood Pilot")
    for z, gid in zips:
        canon = "Brooklyn,New York,United States" if z == "Brooklyn" else f"{z},New York,United States"
        row(Campaign=camp, Location=canon, Location_ID=str(gid))
    for n in NEGATIVES:
        row(Campaign=camp, Keyword=n, Criterion_Type="Campaign negative phrase")
    names = [name.lower()] + ALT_NAMES.get(slug, [])
    if not catch_all:
        names += [f"{name.lower()} brooklyn"]
    for gname, g in GROUPS.items():
        ag = f"{name} | {gname}"
        row(Campaign=camp, Ad_Group=ag, Max_CPC=f"{MAX_CPC:.2f}", Ad_Group_Status="Enabled")
        seen = set()
        for kw in g["kws"](names):
            if kw in seen:
                continue
            seen.add(kw)
            row(Campaign=camp, Ad_Group=ag, Keyword=kw, Criterion_Type="Phrase", Status="Enabled")
        h1 = g["h1"](short)
        heads = [h1] + g["heads"]
        descs = g["descs"](name)
        assert len(heads) == 15, (gname, len(heads))
        r = dict(Campaign=camp, Ad_Group=ag, Ad_type="Responsive search ad", Status="Enabled",
                 Final_URL=lp_url(slug, gname), Path_1=pick([slug.replace("-", "")[:15], "brooklyn"], 15),
                 Path_2=pick([gname.lower(), "cameras"], 15))
        for i, t in enumerate(heads, 1):
            check(t, 30, f"{ag} H{i}")
            r[f"Headline_{i}"] = t
        r["Headline_1_position"] = "1"
        for i, t in enumerate(descs, 1):
            check(t, 90, f"{ag} D{i}")
            r[f"Description_{i}"] = t
        # names must actually be in the pinned headline
        if short.lower() not in h1.lower():
            ISSUES.append(f"PINNED HEADLINE MISSING NEIGHBORHOOD {ag}: {h1}")
        row(**r)

for h in HOODS:
    build_campaign(h)
build_campaign(BROOKLYN, catch_all=True)

with open(f"{OUT}/AESS-Brooklyn-Camera-Pilot-EDITOR-IMPORT.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=HDR)
    w.writeheader()
    w.writerows(ROWS)

# catch-all exclusions: every pilot ZIP, so each searcher lands in exactly one campaign
with open(f"{OUT}/AESS-Brooklyn-Camera-Pilot-CATCHALL-EXCLUDED-LOCATIONS.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Location", "Location ID", "Criterion Type"])
    for _, _, _, zips in HOODS:
        for z, gid in zips:
            w.writerow(["AESS | Cameras | Brooklyn | Rest of Brooklyn", f"{z},New York,United States", gid, "Excluded"])

# ---------------- landing pages ----------------
LP_COPY = {
  "Install": dict(img="/images/tech-bucket-truck-install.png",
     alt="AESS installer mounting a security camera from a bucket truck in {n}, Brooklyn",
     h="Security Camera Installation in {n}, Brooklyn",
     sub="4K camera systems for {n} homes, shops and buildings — recording, playback and phone viewing set up by our own licensed crew.",
     pts=["Indoor and outdoor 4K cameras with night vision", "NVR recording with playback on your phone",
          "Homes, brownstones, stores, restaurants and multi-unit buildings", "Any camera brand you prefer, or our own system"]),
  "Repair": dict(img="/images/camera-repair/camera-no-signal-diagnosis.webp",
     alt="AESS technician diagnosing a security camera with no signal in {n}, Brooklyn",
     h="Security Camera Repair in {n}, Brooklyn",
     sub="Cameras offline, no picture, recorder not saving, app won't connect — we troubleshoot and fix camera systems on most brands.",
     pts=["Offline cameras and “no video” channels", "DVR / NVR recording and playback problems",
          "Phone-app viewing set up again", "Cable testing and camera replacement"]),
  "Business": dict(img="/images/commercial-cctv-camera-installer-brooklyn-ny.webp",
     alt="Commercial CCTV camera installation for a {n}, Brooklyn business",
     h="Business Security Cameras in {n}, Brooklyn",
     sub="Commercial camera systems for {n} stores, bodegas, restaurants, offices, warehouses and buildings.",
     pts=["Register, entrance, stockroom and sidewalk coverage", "Watch every location from one phone app",
          "Lobby, hallway and package-room cameras for landlords", "Insured for commercial work"]),
  "Doorbell": dict(img="/images/lorex-video-doorbell-camera-installation-brooklyn.jpg",
     alt="Video doorbell camera installed at a {n}, Brooklyn front door",
     h="Doorbell Camera Installation in {n}, Brooklyn",
     sub="Video doorbells installed on {n} houses, brownstones and apartment doors — see and talk to visitors from your phone.",
     pts=["Wired video doorbells installed and connected", "Phone alerts and two-way talk set up",
          "Add cameras to cover the yard, gate and packages", "All major doorbell brands"]),
}

TEMPLATE = open(os.path.join(os.path.dirname(__file__), "lp_template.html")).read()

def render(slug, name, zips, gname):
    c = LP_COPY[gname]
    e = lambda s: html.escape(s.format(n=name))
    full = FULLPAGE.get(slug)
    ziptext = ", ".join(z for z, _ in zips) if slug != "brooklyn" else "every Brooklyn neighborhood"
    page = TEMPLATE
    rep = {
        "{{TITLE}}": e(c["h"]) + " | Abstract Enterprises",
        "{{H1}}": e(c["h"]),
        "{{SUB}}": e(c["sub"]),
        "{{IMG}}": c["img"], "{{ALT}}": e(c["alt"]),
        "{{POINTS}}": "".join(f"<li>{e(p)}</li>" for p in c["pts"]),
        "{{SERVICE}}": GROUPS[gname]["svc"], "{{HOOD}}": html.escape(name),
        "{{ZIPS}}": html.escape(ziptext),
        "{{FULLPAGE}}": f"/{full}" if full else "/security-camera-installation-brooklyn-ny",
        "{{CAMPAIGN}}": html.escape(f"{name} | {gname}"),
        "{{CANON}}": f"{BASE}/{full}" if full else BASE,
    }
    for k, v in rep.items():
        page = page.replace(k, v)
    assert "{{" not in page, [m for m in re.findall(r"\{\{\w+\}\}", page)]
    for b in [r"same[- ]?day", r"within the hour"]:
        if re.search(b, page, re.I):
            ISSUES.append(f"LP BANNED '{b}' {slug} {gname}")
    return page

os.makedirs(f"{SITE}/lp", exist_ok=True)
count = 0
for slug, name, _, zips in HOODS + [BROOKLYN]:
    for gname, g in GROUPS.items():
        img = LP_COPY[gname]["img"]
        if not os.path.exists(SITE + img):
            ISSUES.append(f"MISSING IMAGE {img}")
        with open(f"{SITE}/lp/{g['lp']}-{slug}.html", "w", encoding="utf-8") as f:
            f.write(render(slug, name, zips, gname))
        count += 1

kw = sum(1 for r in ROWS if r["Criterion Type"] == "Phrase")
ads = sum(1 for r in ROWS if r["Ad type"])
print(f"campaigns={len(HOODS)+1} ad_groups={ads} rsas={ads} keywords={kw} landing_pages={count}")
print("ISSUES:", len(ISSUES))
for i in ISSUES:
    print("  ", i)
