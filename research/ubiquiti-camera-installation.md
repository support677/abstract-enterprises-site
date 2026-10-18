# Ubiquiti Camera Installation — silo research

Silo: `ubiquiti-camera-installation-*` (16 area pages + the 16 separate `ubiquiti-camera-installation-prices-*` calculator pages, which are a different silo key for `tools/check_page.py` but were read for prices and questions).
Created 2026-10-18 by the REBUILD of `ubiquiti-camera-installation-putnam-county` (queue line: `REBUILD | ubiquiti-camera-installation-putnam-county | Ubiquiti Camera Installation | Putnam | up /ubiquiti-camera-installation-hudson-valley | (845) 640-3835 | GBP Bronx`).
Tools used: Firecrawl search / scrape (`mcp__Firecrawl__*`, incl. the Alexandria `census-gov` provider). Shell curl not used. Firecrawl refuses reddit.com, so Reddit is excerpt-only or EMPTY. "Carried" rows were fetched by an earlier run and recorded in another research file (file + row named); they were not re-fetched.

---

## Part 1 — Silo-wide findings (usable on any Ubiquiti / UniFi page)

### 1.1 Mandatory sources (blueprint v2.3 §3) — status

| # | Source | Result |
|---|---|---|
| 1 | Reddit (r/Ubiquiti, r/UNIFI, r/hudsonvalley…) | EMPTY for UniFi Protect threads (not accessible in build env — Firecrawl refuses reddit.com). Carried r/hudsonvalley second-home thread (U3, research/dvr-upgrade.md) used for Putnam context only. |
| 2 | Google PAA | EMPTY (not accessible in build env). |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says on-page that no AI summary could be captured and instead tests seven recurring claims against Ubiquiti's own documentation. |
| 6 | Landmarks | Putnam: carried L-rows (research/super-live-plus-app-support-repair.md §3 / dvr-upgrade.md). |
| 7 | Use cases / building stock | Putnam: new ACS 2023 pull (PC1) + carried H1–H4. |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env). |
| 9 | Local news | Putnam: carried Highlands Current, Westfair, Daily Voice, lohud, Mahopac News, Mid-Hudson News rows. New 2025–26 Putnam crime search (PN1) returned only social-media excerpts → not used. |
| 10 | Hyperlocal | Carried Highlands Current, Mahopac News, Town of Putnam Valley rows. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). |
| — | Ubiquiti primary sources | techspecs.ui.com, help.ui.com, store.ui.com — new this run (U-rows below). |
| — | Ubiquiti Community | community.ui.com excerpts on surge protection (UC1) — used only as "installers on Ubiquiti's own forum say…", never as Ubiquiti policy. |

### 1.2 Product and platform facts (U) — all from Ubiquiti's own sites

| ID | Exact query · platform | URL | Finding | Page + section used (ubiquiti-camera-installation-putnam-county) |
|---|---|---|---|---|
| U1 | `UniFi G6 Bullet tech specs operating temperature PoE power consumption` · Firecrawl search (includeDomains ui.com) | https://techspecs.ui.com/unifi/physical-security/uvc-g6-turret | G6 Turret: 4K 8MP 1/1.8", IR 30 m (98 ft), face + licence-plate recognition, smart detections (people, vehicles, animals), IP66, IK04, microphone, PoE, max 12.5 W, ambient operating −30 to 50 °C (−22 to 122 °F), NDAA compliant. | §6 cards; §7.5; §10 table; FAQ 10; §10.5 claim 3 |
| U2 | same search | https://techspecs.ui.com/unifi/physical-security/uvc-g6-bullet | G6 Bullet: 4K, IR 30 m, LPR + face recognition, IP66, IK04, PoE, max 9.9 W, pole-mount diameter 1.5–2" (38–50 mm) included, ambient operating −20 to 50 °C (−4 to 122 °F). | §10 table; FAQ 4; §7.5; §10.5 claim 3 |
| U3 | same search | https://techspecs.ui.com/unifi/physical-security/uvc-g6-ptz | G6 PTZ: 10× hybrid zoom, pan 350° tilt 100°, two-way audio, IP66, **PoE+**, max 24.5 W, supported voltage 42.5–57 V, −30 to 50 °C, microSD slot. | §9 Q1 (PoE budget); §10 table; §6 card |
| U4 | same search | https://techspecs.ui.com/unifi/physical-security/uvc-g6-pro-bullet ; https://ui.com/physical-security/bullet | G6 Pro Bullet: 1/1.2" sensor, 2.36× optical zoom, IR 40 m / 60 m with Vision Enhancer, PoE+, 15 W, −20 to 50 °C. ui.com bullet page: AI LPR "Optimized for recognizing license plates". | §9 Q12 (plates); §10 table |
| U5 | `techspecs.ui.com G5 Turret Ultra ambient operating temperature…` · Firecrawl search | https://techspecs.ui.com/unifi/physical-security/uvc-g5-turret-ultra | G5 Turret Ultra: 2K (4MP 2688×1512), IR 30 m, IP66, IK04, PoE, max 4 W, −30 to 50 °C. | §10 table; §15 Starter package; §7.5 |
| U6 | same search | https://techspecs.ui.com/unifi/cameras-nvrs/uvc-g6-dome | G6 Dome: 4K, IP66, **IK10**, PoE 9.25 W, −20 to 50 °C. | FAQ 10; §10 table |
| U7 | `UniFi NVR Instant tech specs PoE ports camera capacity storage UNVR` · Firecrawl search (techspecs.ui.com) | https://techspecs.ui.com/unifi/door-access/unvr-instant | UNVR Instant: managed cameras (15) HD / (8) 2K / (6) 4K; one 3.5" bay; 6 GbE PoE downlink ports + 1 uplink + HDMI (Viewport); PoE budget 40 W; 15.4 W max per port (PoE); ambient operating **0 to 40 °C (32 to 104 °F)**; 9 W max consumption; wall / DIN mount. | §9 Q1, Q2, Q4; FAQ 3; §10 table; §15 |
| U8 | same search | https://techspecs.ui.com/unifi/door-access/unvr | UNVR: (60) HD / (30) 2K / (18) 4K managed cameras; four 2.5/3.5" bays; 10G SFP+; no PoE; power redundancy. | §9 Q2; §10 table |
| U9 | same search | https://techspecs.ui.com/unifi/door-access/unvr-pro (excerpt) | UNVR Pro: 2U, 7 bays, "up to 60 days of storage for (24) 4K cameras". | §10 table |
| U10 | `UniFi Protect remote access unifi.ui.com local only account power outage help.ui.com` · Firecrawl search → scrape | https://help.ui.com/hc/en-us/articles/115012240067-Enabling-UniFi-Remote-Management | Remote management via Site Manager (unifi.ui.com), on by default at setup; needs **outbound** TCP 443 and 8883; "You do not need to open these ports for inbound traffic"; also DNS (UDP 53) and time (UDP 123) issues; keep UniFi OS updated. | §9 Q6; §10.5 claim 2; §12 step |
| U11 | same → scrape | https://help.ui.com/hc/en-us/articles/28457353760919-UniFi-Local-Management | Local management "essential … when users experience an Internet outage"; connect on the local network by browser or UniFi app; local-only default username admin; WiFiman Discovery finds the console. | §9 Q7; §10.5 claim 6 |
| U12 | same search (excerpt) | https://help.ui.com/hc/en-us/articles/14275946860311-UniFi-Password-Recovery-and-Ownership-Transfer | Local-only credentials "are unique to a specific UniFi instance and cannot be recovered unless an SMTP server was manually created". | §9 Q7 |
| U13 | same search (excerpt) | https://help.ui.com/hc/en-us/articles/28692158912279-Adding-Admins-in-UniFi | Local admins can be added when remote management is disabled. | §9 Q7 (context only) |
| U14 | `help.ui.com UniFi Protect recording retention storage hard drive full overwrite` · Firecrawl search → scrape | https://help.ui.com/hc/en-us/articles/29393161732119-Managing-Storage-and-Retention-in-UniFi-Protect | Storage Manager; Enhanced Retention (Protect 5.1+) keeps recent footage full-resolution then downgrades older footage to low quality (not reversible); Flag Clips prevents downgrade; Export/Archive; Case Manager stores footage indefinitely; per-camera retention; drives up to 24 TB. | §9 Q8, Q9; §6 card |
| U15 | same → scrape | https://help.ui.com/hc/en-us/articles/27723320017815-UniFi-Protect-Recording-Modes-Schedules | Recording modes Always / Detection Only / Never; schedules; pre-event and post-event buffers. | §9 Q8; §6 card |
| U16 | `UniFi Protect no subscription fees local storage; Dream Machine Pro runs UniFi Protect…` · Firecrawl search → scrape | https://help.ui.com/hc/en-us/articles/31234972188951-How-UniFi-Protect-Protects-Your-Data | Recordings stored locally on the UniFi OS console; "no cloud backup of your video by default"; Ubiquiti "cannot view, store, or access your video streams"; AI detection runs on the local network (G4, G5, AI series in-camera); optional stream encryption camera↔console (G4/G5/AI, Protect 5.2.42+). | FAQ 2; §10.5 claim 1; §9 Q10 |
| U17 | same → scrape | https://help.ui.com/hc/en-us/articles/12395343519639-Understanding-Drive-and-Storage-Health-in-UniFi | Drive statuses: Optimal / Drive Failure Detected / Drive at Risk of Failure (SMART, bad sectors); keep drives cool, avoid unexpected shutdowns; match drive sizes and RPM. | FAQ 5; §9 Q3 |
| U18 | same → scrape | https://help.ui.com/hc/en-us/articles/360037340954-UniFi-Storage-Requirements-and-Compatibility | 3.5" HDD consoles include UDM-Pro, UNVR-Pro, UNVR Instant; recommended official UniFi HDD 8/16/24 TB; CMR 7200 RPM; Dream Router uses microSD (min 128 GB). | FAQ 9; §10 table |
| U19 | `Ubiquiti outdoor ethernet surge protector grounding lightning…` · Firecrawl search | https://store.ui.com/us/en/products/ethernet-surge-protector | Ubiquiti sells ETH-SP-G2 "Ethernet Surge Protection Outdoor (10kA)", IPX5, protects against ESD and surge events; an indoor panel version also exists. | §9 Q11; §10 table |
| UC1 | same search (excerpts) | https://community.ui.com/questions/Best-practice-for-grounding-use-of-Ethernet-surge-protectors/f9548af4-9ecd-4333-9239-1586463a7995 ; https://community.ui.com/questions/ETH-SP-G2-Surge-Protector-is-totally-useless/e5d05738-b27b-4133-9068-c24c975985e2 | Community posters: surge protector at each end of an outdoor run; must be grounded and used with shielded cable with a drain wire and shielded connectors. (Community, not Ubiquiti policy.) | §9 Q11 (attributed as forum advice) |

### 1.3 Silo pricing (no invented prices)
Source: `ubiquiti-camera-installation-prices-putnam-county.html` (live calculator page for this silo, read 2026-10-18). Its calculator config holds per-zone labor: Brooklyn line $175 / jbox $25 / setup $150; **"Orange / Putnam" line $247 / jbox $32 / setup $195**. Published Putnam figures used on the page, verbatim:
- 4-camera UniFi system installed from **$2,472** (4 × G5 Turret Ultra, G5 Dome Ultra, G5 Bullet or G5 Flex + UNVR Instant, ≥ 2 weeks of recording); 4 × G6 Turret or G6 Bullet **$2,800**; 4 × G6 Dome **$3,176**; 4 × G6 180 / G6 Mini Dome / AI Theta / G5 PTZ **$3,268**; 4 × AI Theta Pro **$3,408**.
- Single cameras installed **$430** (G5 Turret Ultra) to **$2,624** (AI PTZ Precision); G6 Turret / G6 Bullet $512; G6 Dome $606; G6 PTZ $746; G6 Pro Bullet $840; AI LPR $863.
- Doorbells: Doorbell Lite $363; G4 Doorbell Pro $576; G4 Doorbell Pro PoE Kit $691.
- Recorders installed: UNVR Instant $414; UNVR $524; UNVR Pro $744; UNVR G2 $965.
- Hidden in-wall wiring **$200 per camera** (hollow drywall, up to 100 ft). Each camera price includes mounting and a Cat6 run up to 100 ft.
- Protected service/callback rate (blueprint §9): $195/hr, 3-hr minimum ($585) — repair visits on existing systems, not the install.
**Multiplier note (FLAG):** the calculator's Putnam labor zone is 1.41× Brooklyn (line 247/175), not the §9 1.45×. Blueprint §9 says camera-calculator multipliers apply to labor only, which is what the calculator does. Recomputing at 1.45× on labor would give e.g. G5 Turret Ultra ≈ $441 instead of $430. The page uses the **published** Putnam numbers so the site does not show two different Putnam prices; Anwar to confirm. The prices page also says "30-day warranty" and "extended warranty 1, 2 or 3 years" — conflicts with the one-year parts-only terms sentence; NOT used on the area page.

### 1.4 Keyword plan (five layers, silo)
- Service: Ubiquiti camera installation; UniFi camera installation; UniFi Protect installer; UniFi Protect setup; UniFi NVR installation; UNVR Instant install; UniFi doorbell installation.
- Problem: PoE budget exceeded; camera not powering; console offline; remote access not working; recorder overheating / too cold; lightning surge; alerts from trees / deer; retention too short; drive failure.
- Technology: PoE / PoE+ (802.3af/at), Cat6, shielded cable, ETH-SP-G2, UNVR / UNVR Instant / UNVR Pro, UDM-Pro, G5 Turret Ultra, G6 Turret / Bullet / Dome / PTZ / Pro Bullet, AI LPR, Enhanced Retention, Detection Only recording, Site Manager, local-only account, Viewport HDMI.
- Industry: homes, lake houses, second homes, short-term rentals, retail on Route 6/22, professional offices, contractors' yards, marinas.
- Geographic (Putnam page only): Putnam County; Carmel; Mahopac; Brewster; Kent; Patterson; Putnam Valley; Southeast; Philipstown; Cold Spring; Garrison; Nelsonville; Lake Carmel; Putnam Lake; Lake Peekskill; Route 6, 22, 52, 301, 312; I-84.

---

## QUESTION REGISTER — Ubiquiti Camera Installation silo

### Existing questions on the 15 other area pages + 16 prices pages (extracted 2026-10-18 with tools/check_page.py parser: `.faq-question` + every H2/H3/summary ending in "?")
Repeated on most or all pages (template questions): What is included in the installed price? · Can you hide the wires? · Is this an exact quote? · What warranty do I get? / Do you offer a warranty? / Is there a warranty? · I already bought UniFi cameras. Will you install them? · Why is my Ubiquiti camera offline or not recording? · How long does Ubiquiti footage stay recorded? · Are you licensed and insured? · Do you service Ubiquiti systems you didn't install? · How do I get started? · Where is the install? · Will it work without internet? / Will my Ubiquiti system work without internet? · Can I add more cameras later? · How much does it cost? / How much does Ubiquiti (UniFi) camera installation cost in <area>? · Can cameras avoid recording a neighbor's property? (+ variants) · Can you place cameras discreetly on a historic home? (+ historic-preservation variants) · What resolution do you recommend? · Do I need to post that the building/business/store is recorded? / Do I need to notify people they're being recorded? · Do you provide board documentation? (+ co-op/condo variants) · Do Ubiquiti cameras handle snow and ice? / work in winter / work in the cold / built for upstate or Catskills winters / <area> winters · Can you handle long rural cable runs? / long cable runs to outbuildings / on a big lot · Can the building manager and owner both view the cameras? / Can multiple people view the cameras? / Can the doorman and the board both view? · Do you cover full estate / property / home perimeters? · Are the cameras weatherproof (for the coast)? / coastal weather variants · Do you install for businesses (bodegas, restaurants, small businesses)? · Do you integrate Ubiquiti with access control or alarms? · How many Ubiquiti cameras do I need? / How many cameras does a <area> home/building need? · Can Ubiquiti cameras record audio? · What internet speed do Ubiquiti cameras need? · Can I view my property from anywhere? / from work or vacation / from the city / on my phone · Do you cover apartment and condo buildings / lobbies / garages? · Can I install Ubiquiti myself on my <area> home? · Which Ubiquiti camera(s) is/are best for <property type/area>? · Is Ubiquiti legal to install in <area>? · Ready for Ubiquiti in your <area> property? · What areas of <area> do you cover? / Do you cover all <area>? · Can you secure / set up a seasonal, vacation, weekender or Hamptons home? · Can you cover a farm, equestrian, winery, marina or agricultural property? · Wired or wireless for my <area> property? · Is Ubiquiti good value / cheaper than other brands / good for a small business? · Are Ubiquiti cameras good? · I forgot my Ubiquiti password — can it be reset? · Why does my night footage look blurry or washed out? · Is Ubiquiti banned in the US? · Can you upgrade my old cameras to Ubiquiti? · Is Ubiquiti OK near West Point? · Why does a <area> property cost more (than a city apartment)? · Can you mount on vinyl, stucco or cedar-shake siding? · Will you damage the walls in my pre-war building? · Can you install on a brownstone without damaging the brick? · Do you follow Landmarks rules? · Why Choose Ubiquiti Security Cameras?
(Full per-page list reproducible with the extraction script; 264 distinct strings.)

### ubiquiti-camera-installation-putnam-county (REBUILT 2026-10-18) — every question on the page
"?" H2s: none.
§9 Q&A (H3), clusters: Power and the PoE Budget · Where the Recorder Lives · The Internet Side · Recording for Long Absences · Weather, Lightning and Plates · Putnam Rules and Money:
1. We added a fourth camera to the UniFi NVR Instant at our Carmel house and it never powered on — why?
2. How many cameras can a single UniFi NVR Instant record before we need a bigger recorder?
3. When NYSEG drops the power at our Mahopac house, which pieces should the battery backup keep running?
4. Is the unheated garage at our Patterson place a reasonable home for the UniFi recorder?
5. Does the UniFi recorder have to sit beside the internet modem?
6. Do we have to open ports on the router for UniFi Protect to reach our phones in the city?
7. Should our UniFi console be tied to a UI account, or kept as a local-only login?
8. Should the cameras that face the woods record around the clock or only when something is detected?
9. How do we stop one important clip from being written over while an insurance claim drags on?
10. Will deer, wind and swaying branches flood our phones with UniFi alerts?
11. What stops a lightning surge from riding a camera cable back into the recorder?
12. Can a UniFi camera read the plate of a car turning into our driveway at night?
13. What does Putnam County's Chapter 145 mean for whoever runs our camera cable?
14. Can our Brewster shop get money back from New York State for adding UniFi cameras?
§17 FAQ (visible == FAQPage, 10):
1. Do the outdoor UniFi cameras each need an electrical outlet nearby?
2. Does UniFi Protect send our video to a cloud service we have to pay for?
3. Can the cameras be watched on a TV in the house as well as on our phones?
4. Can a UniFi camera go on a fence post or a lamp post along the driveway?
5. How does the system warn us that the recorder's hard drive is wearing out?
6. What should be ready at the house before the install day?
7. How long does a four-camera UniFi install usually take at a Putnam house?
8. Is half the price due before the work starts?
9. We already run a UniFi Dream Machine Pro for our Wi-Fi — can Protect record on it instead of a separate recorder?
10. How well does a UniFi camera within arm's reach on a porch stand up to being knocked or tampered with?
§10.5 claim H3s (quoted claims, not questions): "UniFi Protect is a cloud camera service" · "You have to forward ports for remote viewing" · "Any UniFi camera is fine for winter outdoors" · "PoE means you can hang as many cameras as the recorder has ports" · "A UniFi camera install is a DIY afternoon" (reframed to cable/ledge) · "If the internet is down, the system is useless" · "More megapixels always means better evidence".
De-dup notes: checked by meaning against the register above. Deliberately NOT asked as questions (already on siblings): winter/cold suitability (covered in body text and §10 table only), long runs to outbuildings, wired vs wireless, historic homes, multiple viewers, retention length, seasonal homes, cost-per-area, BYOE, password reset, works-without-internet, areas covered. Q7 is about choosing the account type, not resetting a password; Q6 is about ISP/port forwarding, not "view from anywhere"; FAQ 2 is about cloud fees/where video lives, not internet dependence.

---

## Putnam

Thesis: a UniFi system is a small IP network, and in Putnam that network is stretched across an old, detached, wooded house lot (median year built 1968; 17.9% built before 1940; 77.7% single-family detached) on a grid that fails town by town, for owners who are often somewhere else. So a Putnam UniFi install is decided by power budget, recorder placement (UNVR Instant rated 0–40 °C), camera cold ratings (−30 °C vs −20 °C models), surge protection on long outdoor runs, battery backup and local management when the internet or power drops, and retention planned for long absences. (Distinct from the old template's "lakefront estate" copy.)

### New this run
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| PC1 | Alexandria `census-gov` census/data, acs/acs5 2023, vars B25035_001E, B25034_001E/002E/003E/010E/011E, B25024_001E/002E, geography county:079 state:36 · Firecrawl scrape | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36079 (+ B25034, B25024) | Putnam: 38,369 housing units; median year built **1968**; built 1939 or earlier **6,857** (17.9%); 1940–49 2,993; 2010–19 960; 2020+ 93 (so 1,053 = 2.7% built since 2010); single-family detached **29,826** (77.7%). | §5 para 1–2; §5.5 bullets 1–2; §7 intro; Sources |
| PN1 | `Putnam County NY burglary OR break-in OR "car thefts" sheriff 2026 Carmel Kent Patterson cameras footage` · Firecrawl search (past year) | facebook.com / instagram.com Sheriff posts (excerpts) | Only social-media excerpts; no citable article → EMPTY, not used. | — |

### Carried rows used (not re-fetched; see research/super-live-plus-app-support-repair.md §3 and research/dvr-upgrade.md)
| ID | From | URL | Finding | Used |
|---|---|---|---|---|
| H1 | dvr-upgrade.md H1 | putnamcountyny.gov … Section-4-County-Profile-021815.pdf | >240 sq mi; 6 towns, 3 villages; forest 66.9%; Hudson Highlands bedrock; commerce along Routes 6, 9, 22, 52 and I-84. | §5 para 2; §8 intro; Town section |
| H2 | dvr-upgrade.md H2 | https://www.census.gov/quickfacts/putnamcountynewyork | Mean travel time to work 39.3 min. | §5 para 3; §5.5 |
| H3 | dvr-upgrade.md H3 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36079 | 1,757 seasonal/recreational/occasional-use units. | §5 para 3; §5.5 |
| H4 | dvr-upgrade.md H4 | historicpatterson.org (Putnam Lake exhibit) | Smadbeck lake colonies from 1928 (Lake Carmel, Lake Peekskill, Putnam Lake); 11,000 lots of 20 × 100 ft at Putnam Lake. | §7 card; Town (Patterson) |
| N4 | dvr-upgrade.md N4 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 5 2020 (Isaias): NYSEG 34,150 of 38,693 Putnam customers out (Carmel 12,717; Kent 5,815); Central Hudson 3,621 of 5,160. | §5 para 4; §5.5; §9 Q3 |
| P-W4 / P-W5 | security-camera-maintenance.md | lohud 2026-07-05; lohud 2026-08-03 | July 4 2026 storms left thousands without power in Westchester and Putnam; Aug 3 2026 outage hit 740 Central Hudson customers in Cold Spring / Garrison. | §5 para 4; Town (Philipstown) |
| W4 | dvr-upgrade.md W4 | putnamvalley.gov (state of emergency, July 29 2026) | Putnam Valley flash-flood emergency. | Town (Putnam Valley) |
| P1 | SLP §3 P1 | https://highlandscurrent.org/2016/05/27/new-towers-improve-ems-cell-service-putnam-county/ | "We do not have 254 square miles of coverage"; "Cold Spring is notorious for having blackout spots". | §5 para 3; §10.5 claim 6 |
| P2 | SLP §3 P2 | https://westfaironline.com/construction/verizon-sues-philipstown-for-permits-to-build-new-cell-tower/ | 2018 Verizon suit; McKeels Corners tower "where the topography obstructs the signal". | Town (Philipstown) |
| P8 / B1 | SLP §3 P8 | https://www.governor.ny.gov/news/governor-hochul-announces-broadband-projects-totaling-more-636-million-achieve-universal | $11,498,589 to Comcast to bring fiber to 390 Putnam locations. | §5 para 3; §5.5; §10.5 claim 6 |
| B2 | dvr-upgrade.md B2 | highlandscurrent.org 2023/05/05 | Optimum fiber build through Philipstown. | Town (Philipstown) |
| P5 | SLP §3 P5 | https://hudsonvalley.news12.com/2026/04/23/police-crack-down-on-reckless-after-hours-driving-at-putnam-county-shopping-center/4DFlUzd5vGe9JVPyeF3dut | April 2026: Carmel PD detail at Mahopac Village Shopping Center (Route 6) after after-hours speeding/burnouts; 3 reckless-driving arrests, 22 summonses. | §8 Route 6 card |
| M1 | nvr-installation.md M1 | https://www.midhudsonnews.com/2026/09/10/ (Sheriff, organized retail theft) | Sheriff: 22 vehicles linked to organized retail-theft rings travelling to Putnam stores. | §8 Route 22 card; §9 Q12 |
| N1 | floodlight N1 | Mahopac News, Aug 7 2026 | Vehicle break-ins ~3:37–5:05 a.m. Aug 5 around Lake Casse, Lake Drive, Ridge Road; residents asked to check footage. | Town (Carmel); §9 Q12 |
| P-C1 | security-camera-maintenance.md P-C1 | Mahopac News, Jul 23 2026 | Sheriff Hess: county courthouse cameras captured only portions of an incident; system relies on motion sensors. | §9 Q8 |
| P6 | SLP §3 P6 | https://highlandscurrent.org/2025/11/07/philipstown-debuts-str-law/ | Philipstown draft STR law: owner/agent able to respond within 20 minutes. | §7 card (rentals) |
| P7 | SLP §3 P7 | https://ecode360.com/9475947 ; https://highlandscurrent.org/2023/12/01/putnam-valley-adopts-short-term-rental-law/ | Putnam Valley STR local manager within 30 miles of Town Hall. | §7 card (rentals) |
| E1 / E2 | floodlight E1/E2 | https://ecode360.com/6607815 ; https://www.putnamcountyny.gov/consumer-affairs | Putnam Ch. 145 covers low-voltage / limited data communications incl. video surveillance; no one may engage in the trade without a license or registration; county publishes license lists. | §8.5; §9 Q13 |
| R4 | dvr-upgrade.md R4 | coldspringny.gov (Certificate of Appropriateness) | Cold Spring HDRB approval for exterior changes visible from the street. | §7 card; §8.5 |
| G1 / G3 / G4 | dvr-upgrade.md §1.6 | NY Civil Rights Law §52-a; Penal Law 250.05; NYS Commercial Security Tax Credit (≤ 50 employees, up to $3,000 per retail location, apply before Oct 31) | as silo | §8.5; §9 Q14 |
| L1–L6 | dvr-upgrade.md / SLP | Wikipedia Mahopac; Putnam County Courthouse; Cold Spring Historic District; NYC DEP West Branch Reservoir; Putnam Legislature Tilly Foster Farm; NYS Parks Fahnestock | Lake Mahopac ≈ 587 acres; Courthouse 1814 on Gleneida Ave; West Branch Reservoir in Kent/Carmel, in service 1895, split by Route 301; Cold Spring HD 691 acres, NR 1982; Tilly Foster Farm ≈ 199 acres, county-owned since 2002; Fahnestock State Park ≈ 15,000 acres across Putnam into Dutchess along Route 301 (dvr-upgrade.md L6, parks.ny.gov excerpt). | §13 cards |
| U3-r | dvr-upgrade.md U3 | reddit r/hudsonvalley (Oct 2026 second-home thread) | Second-home owners describe caretakers, neighbours with cameras, battery backup, cellular fallback. | §5 para 3 |

### Images (11) — permanent image rule
Drive "AESS Website Photos" has no Ubiquiti subfolder (checked by the main run this batch); CompanyCam not connected. Every source viewed before use (contact sheets + full size). No faces, plates, house numbers or readable documents (the monitor grid in #2 shows tiny unidentifiable figures and cars). Product shots chosen without the "Compare" checkbox artefacts present on several library files. Captions state "Real AESS job photo from another site, not a Putnam property" or "Ubiquiti product photo".
| images/ubiquiti-camera-installation/ubiquiti-camera-installation-putnam-county-… | Source | Kind | Placement |
|---|---|---|---|
| white-turret-camera-under-fascia-against-bare-winter-trees.webp | images/commercial-security-camera-installation/…-dutchess-county-white-dome-camera-under-storefront-fascia.webp | real AESS | Hero |
| unifi-g5-turret-ultra-black-product-photo.webp | images/ubiquiti-unifi-g5-turret-ultra-camera-black.jpg | product | §5 |
| dome-camera-on-steel-wall-arm-below-stone-windows.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-dome-camera-on-wall-arm-on-stone-facade.webp | real AESS | Town by town |
| unifi-network-video-recorder-four-bay-product-photo.webp | images/nvr-ubiquiti-unvr.png | product | §6 |
| two-small-cameras-on-high-wall-below-mezzanine-windows.webp | images/nvr-installation/nvr-installation-hudson-valley-small-cameras-on-high-wall-of-open-room.webp | real AESS | §7 |
| black-bullet-camera-on-drop-ceiling-mount.webp | images/residential-security-camera-installation/…-nassau-county-black-bullet-camera-on-ceiling-mount.webp | real AESS | §8 |
| small-dome-camera-in-corner-above-wall-sensor.webp | images/nvr-installation/nvr-installation-long-island-dome-camera-and-wall-sensor-high-on-office-wall.webp | real AESS | §9 |
| unifi-g6-bullet-black-product-photo.webp | images/ubiquiti-unifi-g6-bullet-4k-camera-black.jpg | product | §10 |
| unifi-g6-ptz-black-product-photo.webp | images/ubiquiti-unifi-g6-ptz-4k-camera-black.jpg | product | §13 |
| cable-bundles-above-sixteen-tile-camera-monitor.webp | images/commercial-security-camera-installation/…-dutchess-county-cable-bundles-above-recorder-monitor.webp | real AESS | §14 |
| unifi-g6-entry-doorbell-product-photo.webp | images/ubiquiti-unifi-g6-entry-doorbell.jpg | product | §15 |
DAILY-LOG note: `images: 11 reused from images/commercial-security-camera-installation/ (2), images/nvr-installation/ (2), images/residential-security-camera-installation/ (1), images/dvr-upgrade/ (1) and Ubiquiti product shots images/ubiquiti-unifi-*.jpg + images/nvr-ubiquiti-unvr.png (5) (no real Ubiquiti job photos yet)`.

### House practices stated without an external source (FLAG for Anwar)
- Summing camera maximum PoE draws against the recorder's 40 W budget and adding a PoE switch when the sum exceeds it (arithmetic from U1/U3/U5/U7; the policy is ours).
- Battery-backup order (modem, gateway/router, recorder, PoE switch) and pulled-plug test on every install.
- Recorder placement in a conditioned room; no recorder in unheated garages/sheds (follows from U7 rating; the rule is ours).
- Surge protector at both ends of runs that leave the building, bonded to the electrical service ground (UC1 community advice + U19 product; the rule is ours).
- Install-day duration ("most four-camera jobs are one working day"), two-hour arrival windows, same-business-day written quotes.
- Property-type and corridor cards are general descriptions, not per-card sourced.
- AESS's own Putnam Ch. 145 license/registration is NOT claimed; the page tells owners to check any installer against the county lists.
- Pricing: calculator zone 1.41× vs §9 1.45× (see 1.3).
- PoE conflict on the prices page: `ubiquiti-camera-installation-prices-putnam-county` sells "4 × G6 Turret + UNVR Instant" ($2,800). Ubiquiti lists the G6 Turret at 12.5 W max and the UNVR Instant's PoE budget at 40 W, so four turrets sum to 50 W at published maximum. This page's packages therefore use G5 Turret Ultra ($2,472, 16 W), G6 Bullet ($2,800, 39.6 W) and G6 Dome ($3,176, 37 W), all from the same published calculator. Anwar to decide whether the calculator's G6 Turret package should include a PoE switch.
- Field Notes section is installer practice in general terms (no specific dated job anecdote), to avoid a fabricated story.
- "UniFi vs cloud-subscription camera" comparison names no national brand (no sourced claims about ADT/Ring/SimpliSafe plans were gathered).

### Build checks (2026-10-18)
- `python3 tools/check_page.py ubiquiti-camera-installation-putnam-county` → PASS (12,329 rendered words; title 45; meta 160; 11 figures; 6 JSON-LD blocks; FAQ 10 = schema 10; 2 forms; tel 845 + 800 header only; 180,673 B, > 2 KB from every sibling — nearest is the hub at 152,049 B).
- Masked block similarity (word SequenceMatcher on ≥ 8-word p/li/td/h2/h3/figcaption blocks, check_page.mask): max 0.57 against all 31 `ubiquiti-camera-installation-*` pages (a doorbell price line vs the calculator pages); whole-page ≤ 0.04. Against the structural donor super-live-plus-app-support-repair-putnam-county and smart-pss-support-setup-ulster-county: only the protected warranty sentence ≥ 0.65 (1.00); everything else ≤ 0.64.
- Scratchpad note: the concurrent uniview-camera-installation-dutchess-county builder shares this session's scratchpad and overwrote a file named build.py; this page's build script was moved to `scratchpad/ubq-putnam/build_ubq.py`.
