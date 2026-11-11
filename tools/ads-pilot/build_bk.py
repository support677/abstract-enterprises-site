#!/usr/bin/env python3
"""AESS Brooklyn ads: 75 neighborhoods x 4 niches (+4 Brooklyn-wide catch-alls).
Outputs: site/lp/data/bk-ads.json (script data), site/lp/<niche>-<hood>.html landing pages, report."""
import json, os, re, sys, html, glob, csv

SITE, OUT = sys.argv[1], sys.argv[2]
BASE = "https://www.abstractenterprisessecuritysystems.com"
HOODS = json.load(open('/home/claude/hoods.json'))           # [slug, display]
BROOKLYN_GEO = 1022762
SHORT = {"Columbia Street Waterfront": "Columbia St", "Prospect Lefferts Gardens": "Lefferts Gardens",
         "Prospect Park South": "Prospect Park S", "Brooklyn Navy Yard": "Navy Yard", "Brooklyn Chinatown": "BK Chinatown",
         "Bedford-Stuyvesant": "Bed-Stuy", "Downtown Brooklyn": "Downtown BK", "Stuyvesant Heights": "Stuyvesant Hts",
         "Greenwood Heights": "Greenwood Hts", "East Williamsburg": "E Williamsburg", "South Williamsburg": "S Williamsburg",
         "Gerritsen Beach": "Gerritsen Beach", "Manhattan Beach": "Manhattan Beach"}
ALT = {"bedford-stuyvesant": ["bed stuy", "bedstuy", "bedford stuyvesant"], "dumbo": ["dumbo"], "downtown": ["downtown brooklyn"],
       "brooklyn-chinatown": ["brooklyn chinatown", "chinatown brooklyn"], "prospect-lefferts-gardens": ["lefferts gardens", "prospect lefferts"],
       "columbia-street-waterfront": ["columbia street waterfront", "columbia waterfront"], "brooklyn-navy-yard": ["brooklyn navy yard", "navy yard"],
       "borough-park": ["borough park", "boro park"], "east-new-york": ["east new york"], "starrett-city": ["starrett city", "spring creek towers"],
       "ditmas-park": ["ditmas park"], "sunset-park": ["sunset park"], "ocean-parkway": ["ocean parkway"],
       "madison": ["madison brooklyn"], "highland-park": ["highland park brooklyn"], "kensington": ["kensington brooklyn"],
       "city-line": ["city line brooklyn"], "wingate": ["wingate brooklyn"], "mapleton": ["mapleton brooklyn"],
       "ridgewood": ["ridgewood"], "new-lots": ["new lots"], "new-utrecht": ["new utrecht"]}

N = {
 "SCI": dict(name="Security Camera Installation", slug="security-camera-installation", budget=5, cpc=6,
   kw=["security camera installation {n}", "camera installation {n}", "cctv installation {n}", "security camera installer {n}", "security camera company {n}"],
   kw_all=["security camera installation brooklyn", "camera installation brooklyn", "cctv installation brooklyn", "security camera installers brooklyn",
           "security camera installation near me", "camera installation near me", "cctv installation near me"],
   h1=["{s} Camera Installation", "{s} Camera Install", "Cameras Installed {s}", "{s} Cameras"],
   heads=["Licensed & Insured Installers", "25+ Years in Security", "4K HD Camera Systems", "View Cameras on Your Phone",
          "Homes, Stores & Buildings", "Book Online 24/7", "Brooklyn Local Installers", "Indoor & Outdoor Cameras",
          "Night Vision Cameras", "NVR Recording & Playback", "2-Hour Arrival Windows", "No Monthly Fees",
          "Get Your Camera Quote", "NYS Licensed Contractor"],
   d=["Camera systems installed for {n} homes, shops and buildings. Book online.",
      "Licensed & insured NYS low-voltage contractor with 25+ years installing cameras.",
      "4K cameras, NVR recording and phone-app viewing set up by our own install crew.",
      "Tell us how many cameras you need. We confirm a 2-hour arrival window that fits you."],
   lp=dict(img="/images/tech-bucket-truck-install.png", h="Security Camera Installation in {n}, Brooklyn",
     sub="4K camera systems for {n} homes, shops and buildings — recording, playback and phone viewing set up by our own licensed crew.",
     pts=["Indoor and outdoor 4K cameras with night vision", "NVR recording with playback on your phone",
          "Homes, brownstones, stores, restaurants and multi-unit buildings", "Any camera brand you prefer, or our own system"],
     ask="Home or business? How many cameras? Anything already installed?",
     full="security-camera-installation-{slug}-brooklyn-ny", fallback="security-camera-installation-brooklyn-ny")),
 "SCR": dict(name="Security Camera Repair", slug="security-camera-repair", budget=5, cpc=6,
   kw=["security camera repair {n}", "camera repair {n}", "cctv repair {n}", "camera system repair {n}", "dvr repair {n}"],
   kw_all=["security camera repair brooklyn", "camera repair brooklyn", "cctv repair brooklyn", "dvr repair brooklyn",
           "security camera repair near me", "cctv repair near me", "camera system repair near me"],
   h1=["{s} Camera Repair", "Camera Repair {s}", "{s} CCTV Repair"],
   heads=["Camera System Not Working?", "DVR & NVR Troubleshooting", "Cameras Offline? We Fix It", "Repairs on Most Camera Brands",
          "Licensed & Insured Techs", "25+ Years in Security", "Phone App Setup & Fixes", "2-Hour Arrival Windows",
          "Book Online 24/7", "Brooklyn Local Techs", "Upgrade an Old System", "Recorder & Camera Repair",
          "No Picture? No Playback?", "NYS Licensed Contractor"],
   d=["Camera repair for {n} homes and businesses: offline cameras, recorders, apps.",
      "Licensed & insured NYS low-voltage contractor with 25+ years fixing camera systems.",
      "We fix cameras, DVRs, NVRs, cabling and phone-app viewing on most brands.",
      "Book your repair visit online and get a confirmed 2-hour arrival window."],
   lp=dict(img="/images/camera-repair/camera-no-signal-diagnosis.webp", h="Security Camera Repair in {n}, Brooklyn",
     sub="Cameras offline, no picture, recorder not saving, app won't connect — we fix camera systems on most brands.",
     pts=["Offline cameras and “no video” channels", "DVR / NVR recording and playback problems",
          "Phone-app viewing set up again", "Cable testing and camera replacement"],
     ask="What's going on with your system? How many cameras, and what brand if you know it?",
     full=None, fallback="security-camera-repair-brooklyn")),
 "DBI": dict(name="Door Buzzer Installation", slug="door-buzzer-installation", budget=5, cpc=6,
   kw=["door buzzer installation {n}", "buzzer installation {n}", "buzzer system installation {n}", "door buzzer system {n}", "apartment buzzer installation {n}"],
   kw_all=["door buzzer installation brooklyn", "buzzer system installation brooklyn", "apartment buzzer installation brooklyn",
           "door buzzer installation near me", "buzzer system installation near me", "apartment buzzer system installation"],
   h1=["{s} Door Buzzer Install", "{s} Buzzer Installation", "{s} Buzzer Install", "{s} Buzzer Systems", "{s} New Buzzers", "{s} Buzzers"],
   heads=["New Buzzer Systems Installed", "Apartment & Walk-Up Buzzers", "Brownstones & Multi-Units", "Audio & Video Buzzers",
          "Buzz Visitors In From Phone", "Licensed & Insured Installers", "25+ Years in Security", "2-Hour Arrival Windows",
          "Book Online 24/7", "Brooklyn Local Installers", "Landlords & Property Managers", "Replace Old Buzzer Panels",
          "Get Your Buzzer Quote", "NYS Licensed Contractor"],
   d=["Door buzzer systems installed for {n} brownstones, walk-ups and buildings.",
      "Licensed & insured NYS low-voltage contractor with 25+ years in security.",
      "Audio or video buzzers, with the option to answer the door from your phone.",
      "Tell us how many units you have. We confirm a 2-hour arrival window that fits you."],
   lp=dict(img="/images/access-control-gate-reader-installation.jpg", h="Door Buzzer Installation in {n}, Brooklyn",
     sub="New door buzzer systems for {n} brownstones, walk-ups and apartment buildings — installed by our own licensed crew.",
     pts=["Audio and video buzzer systems", "Answer the door from your phone", "Brownstones, walk-ups and multi-unit buildings",
          "Replace old, failing buzzer panels"],
     ask="How many units or apartments? Is there a buzzer system there now?",
     full=None, fallback="door-buzzer-installation-brooklyn-ny")),
 "DBR": dict(name="Door Buzzer Repair", slug="door-buzzer-repair", budget=5, cpc=6,
   kw=["door buzzer repair {n}", "buzzer repair {n}", "apartment buzzer repair {n}", "buzzer system repair {n}", "door buzzer not working {n}"],
   kw_all=["door buzzer repair brooklyn", "buzzer repair brooklyn", "apartment buzzer repair brooklyn",
           "door buzzer repair near me", "buzzer repair near me", "apartment buzzer repair near me"],
   h1=["{s} Door Buzzer Repair", "{s} Buzzer Repair", "Buzzer Repair {s}"],
   heads=["Buzzer Not Working?", "Apartment Building Buzzers", "Brownstones & Walk-Ups", "Repairs on Most Systems",
          "Licensed & Insured Techs", "25+ Years in Security", "2-Hour Arrival Windows", "Book Online 24/7",
          "Brooklyn Local Techs", "Landlords & Property Managers", "Audio & Video Buzzers", "Door Release Not Working?",
          "Upgrade an Old Buzzer", "NYS Licensed Contractor"],
   d=["Door buzzer repair for {n} brownstones, walk-ups and apartment buildings.",
      "Licensed & insured NYS low-voltage contractor with 25+ years in security.",
      "Buzzers that don't ring, can't hear, or won't let people in. We fix most systems.",
      "Book your repair visit online and get a confirmed 2-hour arrival window."],
   lp=dict(img="/images/access-control-panel-wiring-installation.jpg", h="Door Buzzer Repair in {n}, Brooklyn",
     sub="Buzzer not ringing, can't hear visitors, or the door won't release? We repair buzzer systems in {n} buildings.",
     pts=["Buzzers that don't ring or can't be heard", "Door release that won't unlock", "Brownstones, walk-ups and apartment buildings",
          "Upgrade options when a system is too old to fix"],
     ask="What's the problem, and how many units are in the building?",
     full="door-buzzer-repair-{slug}-brooklyn-ny", fallback="door-buzzer-repair-brooklyn-new-york")),
}
NEG = ["diy", "how to", "jobs", "job", "hiring", "salary", "career", "training", "course", "school",
       "amazon", "best buy", "home depot", "walmart", "costco", "dash cam", "dashcam", "car camera",
       "reddit", "youtube", "software download", "spy", "hidden camera", "toy", "rental", "used",
       "manual", "reset password", "login", "customer service", "adt", "simplisafe", "vivint",
       "new jersey", "nj", "connecticut", "philadelphia", "ring doorbell", "video doorbell", "wireless doorbell"]
BANNED = [r"same[- ]?day", r"\$", r"\bprice", r"\bcheap", r"\bfree\b", r"\d{3}[-) ]\d{3}-\d{4}", r"today\b"]
ISSUES = []

def pick(opts, lim, where):
    for o in opts:
        if len(o) <= lim: return o
    ISSUES.append(f"NO FIT {where}: {opts}"); return opts[-1][:lim]

def chk(t, lim, where):
    if len(t) > lim: ISSUES.append(f"LONG {len(t)}>{lim} {where}: {t}")
    for b in BANNED:
        if re.search(b, t, re.I): ISSUES.append(f"BANNED {b} {where}: {t}")

def names_for(slug, disp):
    base = disp.lower().replace('-', ' ')
    return list(dict.fromkeys(ALT.get(slug, [base])))

TEMPLATE = open('/home/claude/lp_template.html').read()

def lp_page(key, slug, disp, area_text):
    n = N[key]; L = n['lp']
    full = L['full'].format(slug=slug) if (L['full'] and slug != 'brooklyn' and os.path.exists(f"{SITE}/{L['full'].format(slug=slug)}.html")) else L['fallback']
    e = lambda s: html.escape(s.format(n=disp))
    rep = {"{{TITLE}}": e(L['h']) + " | Abstract Enterprises", "{{H1}}": e(L['h']), "{{SUB}}": e(L['sub']), "{{IMG}}": L['img'],
           "{{ALT}}": html.escape(f"{n['name']} in {disp}, Brooklyn by Abstract Enterprises"),
           "{{POINTS}}": "".join(f"<li>{e(p)}</li>" for p in L['pts']), "{{SERVICE}}": n['name'], "{{HOOD}}": html.escape(disp),
           "{{ZIPS}}": html.escape(area_text), "{{FULLPAGE}}": "/" + full, "{{CAMPAIGN}}": html.escape(f"{n['name']} | {disp}"),
           "{{CANON}}": f"{BASE}/{full}", "{{ASK}}": html.escape(L['ask']), "{{FULLLABEL}}": html.escape(f"{disp} {n['name'].lower()} page")}
    p = TEMPLATE
    for k, v in rep.items(): p = p.replace(k, v)
    assert '{{' not in p, re.findall(r'\{\{\w+\}\}', p)
    if not os.path.exists(SITE + L['img']): ISSUES.append("MISSING IMG " + L['img'])
    return p

camps = []
os.makedirs(f"{SITE}/lp", exist_ok=True)
for f in glob.glob(f"{SITE}/lp/*.html"): os.remove(f)          # replace this morning's pilot pages
all_names = []
for slug, disp in HOODS:
    nm = names_for(slug, disp); all_names += nm
    short = SHORT.get(disp, disp)
    for key, n in N.items():
        cname = f"AESS | BK | {n['name']} | {disp}"
        h1 = pick([o.format(s=short) for o in n['h1']], 30, cname)
        h2 = pick([f"Serving All of {short}", f"{short} Local Techs", f"Serving {short}", f"In {short}, Brooklyn"], 30, cname + ' H2')
        heads = [h1, h2] + [h for h in n['heads'] if not h.startswith('Brooklyn Local')][:13]
        descs = [d.format(n=disp) for d in n['d']]
        descs[3] = descs[3].replace('We confirm', f'Serving {disp}. We confirm') if len(descs[3].replace('We confirm', f'Serving {disp}. We confirm')) <= 90 else descs[3]
        descs = [d if len(d) <= 90 else d.replace(f"{disp} ", "") for d in descs]
        for i, t in enumerate(heads): chk(t, 30, f"{cname} H{i+1}")
        for i, t in enumerate(descs): chk(t, 90, f"{cname} D{i+1}")
        kws = list(dict.fromkeys(k.format(n=x) for k in n['kw'] for x in nm))
        url = f"{BASE}/lp/{n['slug']}-{slug}"
        camps.append({"n": cname, "b": n['budget'], "geo": "PRESENCE_OR_INTEREST", "loc": [BROOKLYN_GEO], "neg": NEG, "ag": [{"n": f"{n['name']} | {disp}", "cpc": n['cpc'], "kw": kws,
                      "ad": {"h": heads, "d": descs, "u": url, "p1": n['slug'].split('-')[0] + ('-' + n['slug'].split('-')[1] if n['slug'].count('-') > 1 else '')[:0], "p2": ""}}]})
        camps[-1]["ag"][0]["ad"]["p1"] = pick([slug.replace('-', '')[:15], "brooklyn"], 15, cname)
        camps[-1]["ag"][0]["ad"]["p2"] = pick([n['slug'].split('-')[-1], "service"], 15, cname)
        open(f"{SITE}/lp/{n['slug']}-{slug}.html", "w").write(lp_page(key, slug, disp, f"{disp} and across Brooklyn"))

# Brooklyn-wide catch-alls (one per niche): borough-named + near-me searches, neighborhood names blocked
for key, n in N.items():
    cname = f"AESS | BK | {n['name']} | Brooklyn (all)"
    h1 = pick([f"Brooklyn {n['name']}", n['name'], f"Brooklyn {n['name'].replace('Security ', '')}"], 30, cname)
    heads = [h1] + n['heads']; descs = [d.format(n="Brooklyn") for d in n['d']]
    for i, t in enumerate(heads): chk(t, 30, f"{cname} H{i+1}")
    for i, t in enumerate(descs): chk(t, 90, f"{cname} D{i+1}")
    camps.append({"n": cname, "b": 15, "geo": "PRESENCE", "loc": [BROOKLYN_GEO], "neg": NEG + sorted(set(all_names)),
                  "ag": [{"n": f"{n['name']} | Brooklyn", "cpc": n['cpc'], "kw": n['kw_all'],
                          "ad": {"h": heads, "d": descs, "u": f"{BASE}/lp/{n['slug']}-brooklyn", "p1": "brooklyn", "p2": n['slug'].split('-')[-1]}}]})
    open(f"{SITE}/lp/{n['slug']}-brooklyn.html", "w").write(lp_page(key, 'brooklyn', 'Brooklyn', "every Brooklyn neighborhood"))

os.makedirs(f"{SITE}/lp/data", exist_ok=True)
for f in glob.glob(f"{SITE}/lp/data/*.json"): os.remove(f)
json.dump(camps, open(f"{SITE}/lp/data/bk-ads.json", "w"), separators=(',', ':'))
with open(f"{OUT}/AESS-BK-ads-plan.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Campaign", "Budget/day", "Keywords", "Pinned headline 1", "Landing page"])
    for c in camps:
        a = c['ag'][0]; w.writerow([c['n'], c['b'], " ; ".join(a['kw']), a['ad']['h'][0], a['ad']['u']])
print("campaigns", len(camps), "keywords", sum(len(c['ag'][0]['kw']) for c in camps), "lp", len(glob.glob(f"{SITE}/lp/*.html")),
      "budget_total/day", sum(c['b'] for c in camps))
print("ISSUES", len(ISSUES)); [print(" ", i) for i in ISSUES[:40]]
