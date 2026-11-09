# Research — Parking Lot Camera Installation silo

Created 2026-10-18 by the REBUILD of `parking-lot-camera-installation-queens` (area page, up-link `/parking-lot-camera-installation-nyc`, direct line (347) 434-6392, Bronx GBP 460 E Fordham Rd / `#bronx`). This is the first rebuild in the silo; every other `parking-lot-camera-installation-*` page is still the old template at the time of writing.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Shell curl is blocked in the build environment; tools used: `WebSearch` (result titles/URLs only), `WebFetch` (page read through a summariser — quotes below are what that tool returned from the page), `mcp__Firecrawl__firecrawl_search` (excerpts). Where only a search excerpt was seen, the entry says "excerpt". Sources that could not be opened are written `EMPTY (not accessible in build env)`. Nothing below is invented.

---

## 1. Source matrix (blueprint v2.3 §3, all 11 sources)

| # | Source | Status for this silo build |
|---|---|---|
| 1 | Reddit | Excerpts only via Firecrawl search (rows R1–R5). Thread pages themselves not opened. |
| 2 | Google PAA | **EMPTY (not accessible in build env)** — no Google SERP surface is reachable. |
| 3 | Google PASF | **EMPTY (not accessible in build env)**. |
| 4 | Answer the Public | **EMPTY (not accessible in build env)**. |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)**. The Queens page §10.5 says so on the page and tests seven claims that recur in national cost guides (rows A1–A2) and forum answers against primary sources; it does not quote an AI Overview. |
| 6 | Area landmarks | Queens section (sourced, rows Q-L*). |
| 7 | Area-specific use cases | Queens section (sourced, rows Q-U*). |
| 8 | Bing & DuckDuckGo | **EMPTY (not accessible in build env)** — the `WebSearch` tool's backend is not identified as Bing or DDG, so its results are logged under the source they point to, not as a Bing/DDG cross-check. |
| 9 | Local news | Queens section (Queens Eagle, CBS New York, ABC7, Fox 5, Gothamist, PIX11, QNS). |
| 10 | Hyperlocal | Queens section (Queens Eagle, QNS, Queens Chronicle, Flushing Post/Queens Post via search titles). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — search for Queens camera installers returned directory pages (Thumbtack, vendor blogs), no Yelp review text. Substitute: ABC7 "7 On Your Side" and CBS reporting on complaints against two JFK-area long-stay lots (rows Q-N5, Q-N6) — complaints about lots, not about installers. |

---

## 2. Silo-wide findings

### 2.1 Reddit (excerpts)
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com r/Queens parking lot car stolen camera footage` · Firecrawl search (excerpt) | https://www.reddit.com/r/Queens/comments/14rrg41/my_car_was_stolen_on_atlantic_ave_and_113_st/ | r/Queens poster, car stolen at Atlantic Ave & 113 St (Richmond Hill), describes trying to get surveillance footage and calling to ask whether it was a towing. | Queens §9 tow H3 (framing only: owners first have to work out whether a car was stolen or towed); Sources |
| R2 | same (excerpt) | https://www.reddit.com/r/astoria/comments/1py4737/carhouse_theft_in_astoria_37th_street/ | r/astoria: car entered at 4:45 a.m. during a snowstorm, "caught on camera". | Queens §5 para 2 (residents already post camera stills); Sources |
| R3 | same (excerpt) | https://www.reddit.com/r/nyc/comments/20eei6/car_vandalismtheft_in_queens/ | r/nyc (Queens): "I'm considering putting cameras in front of my house … I can't even park my car in front of my house." | Sources list only |
| R4 | `site:reddit.com JFK off-site parking lot car damaged Queens review` · Firecrawl search (excerpt) | https://www.reddit.com/r/AskNYC/comments/8tdf25/parking_while_away_for_an_extended_time/ | r/AskNYC on long-term lots near JFK: "some of the reviews are pretty crazy. (Hundreds of extra miles on the odometer, damage, etc.)" | Queens §8 Rockaway Blvd corridor; §9 "never left the lot" H3; Sources |
| R5 | same (excerpt) | https://www.reddit.com/r/longisland/comments/1g06djm/lga_parking/ | r/longisland on LGA parking: "I have read reviews about scratches and minor cosmetic damage in parking lots." | Queens §8 (airport lots, framed as forum reports); Sources |

### 2.2 Cost claims that recur in search summaries (for §10.5 Reality Check)
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `Fixr security camera installation cost per camera` · WebSearch → WebFetch | https://cost-guide-ssr.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera | HomeAdvisor: national average $1,298, typical $593–$2,040, full range $125–$3,500; one camera with labor $125–$450; specialists $50–$200 per camera. No commercial/parking figures. | Queens §10.5 H3 1; Sources |
| A2 | `Angi cost to install security cameras 2026 commercial` · WebSearch → WebFetch | https://getsafeandsound.com/blog/cctv-camera-installation-cost/ | Commercial guide: PTZ for parking lots and large open areas $1,200–$2,500 installed; 4–6 camera projects $2,800–$10,000; outdoor placement adds $50–$200 per camera; no separate pole, trenching or LPR price ("you'll need a site survey"). | Queens §10.5 H3 1 and 2; Sources |
| A3 | (Angi article itself) | — | Not opened this build. | — |

### 2.3 Rules that apply across the silo (verify per area)
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `NYC DCWP garage and parking lot license requirements sign capacity rates` · WebSearch → WebFetch | https://www.nyc.gov/site/dca/businesses/license-checklist-garage-parking.page | DCWP licence for any business that "accommodates, stores, or keeps five or more vehicles for a fee"; exempt: lots used only by the business's own customers/employees and lots run by a multiple dwelling's owner for its residents. 2-year licence, expires March 31 of odd years; fee example $300 (5–25 cars) to $600 (101+) when filed Apr 1–Sep 30 of an odd year. DOB document stating maximum capacity (C of O, TCO, LNO or Letter of Verification). Garagekeepers liability ≥ $300,000 CSL, City as certificate holder. Bicycle parking if 51+ autos: 1 per 10 auto spaces up to 200. No camera requirement on the page. | NYC pages; Queens §8.5, §9 DCWP H3, §7 cards; Sources |
| G2 | same → WebFetch | https://www.nyc.gov/site/dca/consumers/shopping-services-garages-parking-lot.page | Signs "conspicuously at each public entrance": business name, address, DCWP licence number, capacity, bicycle minimum, hours; "Capacity Full" sign with 6-inch letters. Garages must "take care to prevent damage to customers' vehicles…" and "cannot post signs or require you to sign anything that waives their responsibility for damage." | Queens §5, §8.5, §9 DCWP H3; Sources |
| G3 | same → WebFetch | https://rules.cityofnewyork.us/wp-content/uploads/2024/12/DCWP-NOA-Parking-Lots-and-Parking-Garages.pdf | DCWP rule (proposed Aug 22, 2024; hearing Sept 23, 2024): rates by payment method must be shown at entrance; monthly-rate sheet 8"×10"; capacity documents for new premises; insurance now "$300,000 combined single limit per accident"; premises "must be adequately attended at all times during operation". No camera provision. | Queens §8.5, §9 DCWP H3; Sources |
| G4 | `NYC biometric identifier information law commercial establishments sign DCWP` · WebSearch → WebFetch | https://rules.cityofnewyork.us/rule/biometric-identifier-information/ ; https://www.hinshawlaw.com/en/insights/privacy-cyber-and-ai-decoded-alert/privacy-law-essentials-new-york-city-biometric-identifier-law-goes-into-effect | Local Law 3 of 2021 (in effect July 9, 2021; DCWP sign rule effective Jan 15, 2022). "Commercial establishment" = "a place of entertainment, retail store, or food and drink establishment"; sign "near all of its entrances"; sale/trade of biometric data prohibited; private right of action $500 per sign violation, $500 negligent / $5,000 intentional or reckless sale violation. | Queens §8.5, §9 face-recognition H3; Sources |
| G5 | `New York Penal Law 250.05 eavesdropping mechanical overhearing conversation one-party consent audio` · WebSearch (titles only) + carried from research/nvr-installation.md G8 | https://www.nysenate.gov/legislation/laws/PEN/250.00 | Mechanical overhearing = recording a conversation without consent of at least one party; eavesdropping is a class E felony (carried row). | Queens §8.5, §9 audio H3; Sources |
| G6 | `14 CFR 77.9 notice construction 20,000 feet runway 100 to 1 slope` · WebSearch → WebFetch | https://www.law.cornell.edu/cfr/text/14/77.9 | Notice to FAA for anything "more than 200 ft. AGL" (a), or anything exceeding a surface sloping 100:1 for 20,000 ft from the nearest runway of an airport with a runway over 3,200 ft (b)(1). | Queens §8.5, §9 FAA H3; Sources |
| G7 | `New York retail theft prevention tax credit small business security cameras $3,000` · WebSearch → WebFetch | https://www.securityindustry.org/2024/04/29/state-of-new-york-provides-retailers-with-tax-credit-for-security-improvements ; https://criminaljustice.ny.gov/nys%20cstc.html | NYS Commercial Security Tax Credit (DCJS): "$3,000 credit per retail location"; ≤50 employees statewide; spend >$4,000 per location (≤25 employees) or >$6,000 (26–50); eligible expenses include surveillance cameras and "Exterior license plate readers (LPRs)"; applications "by October 31 of each year"; program cap $5 million per year. SIA (Apr 29, 2024) describes it as for tax years 2024 and 2025. DCJS page does not state whether later years are covered. | Queens §8.5, §9 tax-credit H3; Sources |
| G8 | `NYC flood resistant construction Appendix G building code electrical equipment design flood elevation below grade garage` · WebSearch → WebFetch | https://www.nyc.gov/assets/planning/download/pdf/about/dcp-priorities/data-expertise/resilient-construction-info-brief.pdf | DCP brief: in the 1% annual-chance floodplain, DFE = BFE + freeboard (typically 1–2 ft); "Elevating mechanical equipment such as electrical…" is the resilient practice; for residential buildings space below DFE only "for parking, storage or building access" and "Mechanical systems must be elevated." | Queens §7.5 below-grade garage; §8.5; Sources |

### 2.4 Keyword layers (five layers, blueprint Appendix A)
- **Service:** parking lot camera installation, parking garage cameras, license plate recognition (LPR) camera, PTZ camera, pole camera, lot surveillance system, NVR for parking lot, remote viewing.
- **Problem:** car theft from lot, catalytic converter theft, tire and rim theft, break-ins, unauthorized use of a parked car, damage claims, tow disputes, car meets/takeovers, power cut before theft, flooded garage, headlight glare.
- **Technology:** PoE, Cat6, fiber, wireless bridge, UPS, NVR, LPR, PTZ, WDR, IR, varifocal, cloud backup, ONVIF.
- **Industry:** DCWP-licensed public garages and lots, airport long-stay lots, dealerships, auto repair/body shops, shopping-center and supermarket lots, building garages (co-op/condo/rental), fleet and truck yards, houses of worship and schools.
- **Geographic:** per area section.

### 2.5 Silo pricing base (no invented prices) — FLAGS
| Figure | Source in repo |
|---|---|
| Packages (Brooklyn base 1.00×): Starter **$850–$1,500**, Standard **$1,500–$2,500**, Premium **$2,800–$4,500** installed | `parking-lot-camera-installation-brooklyn.html` and `-bronx.html` (Packages section); blueprint v2.3 §9 "Parking-silo package base (Brooklyn) = 850 / 1,500 / 2,500 / 2,800 / 4,500". |
| Service/callback **$195/hr, 3-hr min ($585)** | blueprint v2.3 §9 (protected); all silo pages. |
| Queens ×1.05 → Starter **$893–$1,575**, Standard **$1,575–$2,625**, Premium **$2,940–$4,725** (850×1.05 = 892.5 → 893 half-up; others exact) | Matches the pre-rebuild Queens page. |

FLAGS: (1) `parking-lot-camera-installation-nyc.html` publishes $850–$1,935 / $1,500–$3,225 / $2,800–$5,805 — upper bounds are Brooklyn × 1.29, a multiplier that is not in §9. (2) `parking-lot-camera-installation-manhattan.html` publishes $1,097–$1,935 / $1,935–$3,225 / $3,612–$5,805 — ×1.29, not the §9 Manhattan 1.25 (which gives $1,063–$1,875 / $1,875–$3,125 / $3,500–$5,625). (3) Every old silo page still carries three-year warranty wording; the rebuilt Queens page uses the one-year parts-only terms sentence only. (4) No per-camera, per-pole, trenching or LPR line prices exist in the silo; the Queens page publishes none and says those are quoted after survey. Anwar to decide whether a silo line-item sheet should exist.

---

## 3. Images (silo)
Step A — Google Drive "AESS Website Photos" has no Parking Lot folder (per main-run brief). Step B — CompanyCam not connected. Step C — `images/parking/` holds 12 distinct images under ~190 file names; every one viewed for this build is AI-generated (garbled sign text such as "KEEP KEZEAR" and "VIOLATORS…", rendered vans with the 800 number, a mock "The Home Depot" storefront). **All existing `images/parking/*.webp` rejected — not only the `*hudson-valley*` ones. They are live on all 15 old sibling pages: flag for Anwar.** Queens page uses the permanent image rule (see Queens section §Q-IMG).

---
## 4. Question register (every FAQ / Q&A question on all 16 parking-lot-camera-installation-* pages)
Extracted programmatically on 2026-10-18 (before the Queens rebuild landed) with `tools/check_page.py`'s parser: every `.faq-question`, every H2/H3/summary ending in "?", and every `Question` name in JSON-LD, de-duplicated per page. 406 entries. The old Queens questions (4.11) are retired with the old page but stay listed so no rebuilt page reuses their intents.

### 4.1 `parking-lot-camera-installation-bronx` (23)
- Can cameras cut down on overnight break-ins in a resident garage?
- Our garage attendants have been threatened for keys during a theft — can cameras help?
- We keep losing catalytic converters and rims — what actually gets a usable identification?
- Assigned resident spots at our complex get taken — can cameras support enforcement?
- Can a plate camera read cars going up a gated garage ramp?
- Can one reader cover a Hunts Point yard gate with trucks moving all night?
- Do ceiling domes in a garage under a building work as well as poles on an open lot?
- Part of our lot backs onto the water on the Sound side — does that change the hardware?
- There's an elevated 4 or 2/5 line directly over the lot — does that affect mounting?
- Our north-Bronx lot is on rock — can poles still be set?
- The lot fills up on Yankee Stadium game nights — does that change the plan?
- Can we keep the recorder we have and add cameras to it?
- A managing agent runs several of our buildings — who holds the login?
- At a NYCHA or Mitchell-Lama development, who approves a lot camera plan first?
- Can a garage callbox or door intercom tie into the camera system later?
- Can cameras also cover the dumpster corral and compactor area?
- Do we have to post signs that the lot and garage are recorded?
- Will winter road salt and plowing damage low cameras at a garage entrance?
- Can we share a single clip with the local precinct without exposing the whole system?
- Can a temporary camera cover the lot while a ramp or building is under construction?
- If the property changes managing agents, how do we keep control of the recorder?
- Does the plan need to keep FDNY fire lanes and hydrant access clear at a big complex?
- How fast can a failed camera on a busy ramp be swapped out?

### 4.2 `parking-lot-camera-installation-brooklyn` (26)
- Can cameras stop people from parking in my lot without permission?
- Can I mount cameras on the building next door?
- My lot is behind a store on a busy avenue. Is that harder?
- Will an elevated train line affect the cameras?
- What happens if trenching hits something unexpected?
- My lot floods. Where should the equipment go?
- Our lot is only used on certain days. Does that change anything?
- Can existing cameras be kept if we upgrade?
- Can a shared plaza lot run one system for several tenants?
- Will cameras work on a lot with no building alongside it?
- How is footage handed to police if we need to?
- Does an old analog system have to be scrapped?
- What happens to coverage when snow is piled in the lot?
- Can cameras be moved if the lot is restriped?
- Does a Brooklyn co-op or condo board usually approve the camera plan first?
- Can cameras on a Brooklyn lot also cover a sidewalk shed or scaffolding out front?
- Can one system cover a Brooklyn lot that turns into a weekend market or event space?
- Can a Brooklyn lot system add a camera at a rear or basement service entrance?
- Can a plate be read at a narrow Brooklyn curb cut?
- How much recording history will a Brooklyn lot actually hold?
- Who in the building can pull up the lot remotely?
- How is coverage handled when Con Edison or a street reconstruction tears up the block?
- Can cameras cover a below-grade garage as well as the lot?
- Our lot is shared with other tenants. How does that work?
- If we gate the lot next year, what should be done now?
- What does AESS cover after a Brooklyn lot install?

### 4.3 `parking-lot-camera-installation-dutchess-county` (27)
- What happens if the trench hits rock in Dutchess?
- Will cameras stop the auto thefts the Sheriff keeps warning about?
- How deep do camera pole footings need to be in Dutchess?
- Why do the Poughkeepsie and Wassaic commuter lots need longer retention?
- My lot is at the Poughkeepsie station or a large commuter garage — can you handle that scale?
- My lot is in Rhinebeck, Beacon or a historic district — does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Route 9 entrance?
- Can one system cover a garage and the surface lot next to it?
- A Route 9 dealership keeps getting hit overnight. What helps?
- Who owns the poles in my lot?
- Can a system cover an apartment, HOA or campus lot with privacy rules?
- Can you cover a fairground or estate lot that surges on event days?
- Can you cover a horse-country or far-out eastern lot without trenching power to it?
- How does a multi-parcel campus like a hospital, college or the chip plant stay on one system?
- How long does a parking lot camera install take in Dutchess?
- Do parking lot cameras need a permit in Dutchess?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does a Dutchess parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover the eastern Harlem Valley — Millbrook, Amenia, Dover?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?

### 4.4 `parking-lot-camera-installation-hudson-valley` (26)
- What happens if the trench hits rock?
- Can one system cover a Hudson Valley lot a church uses on Sundays and a business uses on weekdays?
- How deep do camera pole footings need to be here?
- Will deer and wildlife set off the camera alerts?
- My property is in a historic district. Does that affect a camera project?
- The internet at my property is slow. Will the cameras still work?
- Why do Metro-North lots need longer retention than retail?
- What about a lot that is only busy a few weekends a year?
- Can you cover a Hudson Valley municipal or village parking lot?
- Can one system cover a Hudson Valley hospital or medical-campus lot with several entrances?
- Does leaf-on and leaf-off season change what a Hudson Valley camera sees?
- Can cameras reach a Hudson Valley lot set far back on a hillside or a long approach?
- Does a Hudson Valley scenic or viewshed area limit where a camera pole can go?
- How does a multi-parcel campus stay on one system?
- Can you cover a Hudson Valley winery, brewery or distillery lot?
- Do you cover college and campus lots in the Hudson Valley?
- Can a Hudson Valley lot on well and septic still run a camera system?
- Can a Hudson Valley system cover a lot plus an adjacent barn, garage or outbuilding?
- How is a Hudson Valley lot install scheduled around frozen ground or winter weather?
- Can plates be read at a driveway off a state route?
- How much recording history does a Valley property retain?
- How does remote viewing work on a rural Valley property?
- Can cameras cover a Hudson Valley state-park or trailhead overflow lot with no attendant?
- Can one plan cover a Hudson Valley farm stand or orchard that only fills in fall?
- Is it worth running gate conduit before the ground closes?
- What does the AESS warranty cover on Valley equipment?

### 4.5 `parking-lot-camera-installation-long-island` (26)
- Can cameras watch a Long Island lot's fence line and landscaped buffer?
- Why does a Long Island lot need more cameras than a city lot the same size?
- Do I need to trench, or can the system be wireless?
- Will salt air destroy cameras on a south shore property?
- How do snow piles affect a camera system?
- My lot has three entrances. Do I need plate cameras at all of them?
- How long should a commuter lot keep footage?
- Who approves camera work on a lot in an incorporated village?
- How is a Long Island lot handled when it shares a driveway with the building?
- Who owns the poles at the edge of my property?
- What does salt exposure actually damage first?
- Can one Long Island system also cover a boat, RV or trailer storage yard on the property?
- Do seasonal properties need year-round coverage?
- Can the system tell the difference between a person and a car?
- Can a Long Island lot system alert someone if a gate is forced or left open after hours?
- Do you cover municipal beach and marina lots on the South Shore?
- Can one plan cover an East End estate or vineyard lot that is only busy in season?
- How is a Long Island shopping-center lot with several anchor stores covered?
- Can a Long Island lot's camera system be added to in phases as the property grows?
- What keeps a Long Island lot recording when a storm knocks out power?
- How long is footage kept on a commuter lot versus a retail lot?
- Can one login show a Long Island owner several lots across Nassau and Suffolk at once?
- Can cameras cover overflow that spills onto a grass or gravel field on Long Island?
- How are cameras handled where a Long Island lot backs onto the LIRR or a parkway?
- Should gate hardware go in during the camera project or afterward?
- What is covered after the install, and what happens when the warranty ends?

### 4.6 `parking-lot-camera-installation-manhattan` (26)
- Can cameras be installed in a garage with a seven-foot ceiling?
- Will my building let you drill through the slab?
- Why not use wireless cameras between garage levels?
- Who owns the cameras if a parking operator runs the garage?
- Can the system document damage in a valet or attended garage?
- How often do garage cameras need cleaning?
- Where should the recorder go if the building has no spare room?
- How disruptive is the installation to garage operations?
- Who needs to approve a garage camera project?
- Can cameras be installed without drilling the slab?
- Will cellular-based equipment work below grade?
- What does coverage look like in a valet operation?
- Can the cameras cover a car elevator or ramp between garage levels?
- Can a garage system integrate with building access control?
- Can cameras cover a Manhattan stacker or automated parking garage?
- How is the bright-to-dark transition at a Manhattan garage mouth handled?
- Can a Manhattan garage system cover the pedestrian stairwells and elevator lobbies?
- Can you work around fire protection and posted clearances?
- Can a Manhattan garage system flag a vehicle parked far longer than allowed or abandoned?
- Can a Manhattan garage system feed the building's existing security desk?
- How much history does a Manhattan garage recorder hold?
- Can residents or a managing agent view the cameras remotely?
- Can cameras document flooding in a below-grade Manhattan garage?
- Can an old analog garage system be upgraded without new cable?
- Can access control or plate-based entry be added later?
- What is covered after a Manhattan garage installation?

### 4.7 `parking-lot-camera-installation-nassau-county` (22)
- Commuters leave cars in our lot all day near the train — can cameras support enforcement?
- Our Sunrise Highway strip-mall lot keeps getting cars broken into — what actually helps?
- We keep losing catalytic converters off trucks in the lot — what gets a usable identification?
- Can I mount cameras on the building next door on a crowded downtown lot?
- Can a plate camera read cars entering the mall or a big-box lot off Old Country Road?
- Our lot is a wide open field with no building nearby — will cameras still work?
- Cars with out-of-state plates keep sitting in our lot for weeks — can cameras help get them towed?
- Part of our lot is on low South Shore ground — does that change trenching?
- The ground on our North Shore lot is shallow rock — does that rule out camera poles?
- Our Long Beach lot flooded during Sandy — where should the equipment go?
- Our lot backs onto the Woodcleft Canal — does the salt air matter?
- Can we keep the cameras we already have and just upgrade the system?
- Can one system cover a shared strip-mall lot with several tenants?
- For a resident lot behind a co-op or condo building, who signs off on the design?
- Can one system cover a below-grade garage and the surface lot together?
- Our marina lot is busy in summer and quiet all winter — does that change the system?
- Can a camera cover a rear or service door that opens onto the lot?
- What happens to coverage when the DOT or a utility tears up the street outside?
- If an entry gate gets added later, how should the wiring be prepped up front?
- Can the cameras cover a dealership inventory row along a Nassau auto corridor?
- How is snow handled when plows pile it in the lot?
- Can a school or house-of-worship lot run tighter rules during quiet weeks?

### 4.8 `parking-lot-camera-installation-nyc` (26)
- How many cameras does a parking lot need?
- Can parking lot cameras read license plates?
- Do parking lot cameras need Wi-Fi or internet?
- How high should parking lot cameras be mounted?
- Do I need a pole, or can cameras go on the building?
- How long is parking lot camera footage kept?
- Can cameras be added to a lot that already has a system?
- What maintenance do parking lot cameras need?
- Who owns the footage once a NYC lot system is installed?
- Can one recorder cover a surface lot and a garage on the same property?
- What happens to the cameras if the internet goes down?
- How disruptive is installation to a working lot?
- Do posted signs need to go up with the cameras?
- What is the first thing that fails on an outdoor camera system?
- Do you install parking lot cameras throughout New York City?
- How is a parking lot camera quote produced?
- What does a parking lot camera system cost?
- Do you pull the electrical permits a NYC parking lot camera install needs?
- Can NYC parking lot footage be given to the NYPD or produced under a subpoena?
- How are NYC parking lot cameras protected from tampering and vandalism?
- How is pedestrian and neighbor privacy handled on a NYC lot system?
- Can I watch the lot from my phone?
- Is AESS licensed and insured to install parking lot cameras in NYC?
- Do NYC parking lot cameras record continuously or only when they detect motion?
- Can access control or a gate be added later?
- What warranty comes with the work?

### 4.9 `parking-lot-camera-installation-orange-county` (27)
- What happens if the trench hits rock — or muck?
- Will cameras actually stop catalytic-converter theft in my lot?
- How deep do camera pole footings need to be in Orange?
- Why do Port Jervis Line commuter lots need longer retention than a store?
- My lot is at an outlet or mall the size of Woodbury Common — can you handle that scale?
- My lot is in a historic district like Goshen or Newburgh — does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Route 17 entrance?
- Can one system cover a garage and the surface lot next to it?
- Can you cover a Stewart Airport-style long-stay lot?
- Which utility owns the poles in my lot — O&R or Central Hudson?
- Can a system cover an apartment or HOA lot with resident privacy rules?
- A warehouse or fleet yard off I-84 keeps getting hit overnight. What helps?
- Can you cover a theme-park or event lot that surges seasonally?
- How does a multi-parcel corporate campus stay on one system?
- How long does a parking lot camera install take in Orange?
- Do parking lot cameras need a permit in Orange?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does an Orange parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover the western towns like Warwick and Port Jervis?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?

### 4.10 `parking-lot-camera-installation-putnam-county` (27)
- What happens if the trench hits rock — or a watershed buffer?
- Will cameras actually stop auto theft and break-ins in my lot?
- How deep do camera pole footings need to be in Putnam?
- Why do Harlem Line commuter lots need longer retention than a store?
- My lot is at the Southeast station or a large commuter garage — can you handle that scale?
- My lot is in Cold Spring or a historic river village — does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Route 6 entrance?
- Can one system cover a garage and the surface lot next to it?
- A dealership or plaza off Route 6 keeps getting hit overnight. What helps?
- Which utility owns the poles in my lot — NYSEG or Central Hudson?
- Can a system cover an apartment, HOA or lake-community lot with resident privacy rules?
- My lot is inside the NYC watershed — does that change the install?
- Can you cover a Cold Spring tourist or trailhead lot that surges on weekends?
- How does a multi-parcel campus like a hospital or county complex stay on one system?
- How long does a parking lot camera install take in Putnam?
- Do parking lot cameras need a permit in Putnam?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does a Putnam parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover the river towns like Cold Spring and Garrison?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?

### 4.11 `parking-lot-camera-installation-queens` (25)
- Can you cover a car dealership or vehicle-inventory lot in Queens?
- Can you protect EV charging stations in a Queens parking lot?
- Can cameras help with stolen mopeds and delivery bikes at a Queens lot?
- Do cameras stop illegal dumping at a Queens lot or yard?
- Do you cover shuttle and airport-adjacent parking near LaGuardia or JFK?
- Can you secure a truck or fleet yard in Long Island City or Maspeth?
- Are there monthly fees?
- Do the cameras work at night?
- Can you cover a drive-through or fast-food lot on a Queens avenue?
- Can the cameras also show which spaces are open in a Queens commuter lot?
- How do you cover an open event lot near Citi Field or Aqueduct?
- What actually stops tire and rim theft in a Queens lot?
- Do you install temporary or solar cameras for Queens overflow parking?
- What kinds of Queens parking properties do you work on?
- Do you offer 24/7 monitored cameras or record-only systems for a Queens lot?
- Can cameras stop gate-running or non-payment at a paid Queens lot?
- Can footage help defend a slip-and-fall or injury claim in a Queens retail lot?
- Can you cover a for-hire-vehicle or taxi base in Long Island City?
- What documentation and training do I get at handover?
- Can you cover a Queens gas station or car wash lot?
- Can cameras deter smash-and-grab break-ins of parked cars in Queens?
- Can you install cameras I already own?
- Can cameras document a hit-and-run in a Queens parking lot?
- Can one system cover a Queens lot used for business by day and events at night?
- Can you cover the loading docks and delivery bays behind a Queens warehouse?

### 4.12 `parking-lot-camera-installation-rockland-county` (27)
- What happens if the trench hits rock?
- Will cameras actually stop catalytic-converter theft in my lot?
- How deep do camera pole footings need to be in Rockland?
- Why do Metro-North commuter lots need longer retention than a store?
- My lot is in a historic village like Nyack or Piermont. Does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Route 59 entrance?
- Can one system cover a mall deck and the surface lot next to it?
- Can you cover a Rockland municipal or village parking lot?
- Can one system cover a hospital or college campus with several entrances?
- My lot is on the Hudson shore. Does salt or flooding affect the equipment?
- Who owns the poles in my lot, and can you attach a camera to one?
- Can a system cover an apartment or HOA lot with resident privacy rules?
- A fleet yard off Route 303 keeps getting hit overnight. What helps?
- How does a multi-parcel corporate campus stay on one system?
- How long does a parking lot camera install take in Rockland?
- Do parking lot cameras need a permit in Rockland?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does a Rockland parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover the Ramapo-west towns like Suffern and Sloatsburg?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?

### 4.13 `parking-lot-camera-installation-staten-island` (22)
- Commuters leave cars in our lot all day near the ferry — can cameras support enforcement?
- Our Forest Avenue strip-mall lot keeps getting cars broken into — what actually helps?
- We keep losing catalytic converters off trucks in the lot — what gets a usable identification?
- Can I mount cameras on the building next door on a crowded North Shore lot?
- Can a plate camera read cars entering the mall or a big-box lot off Richmond Avenue?
- Our lot is a wide open field with no building nearby — will cameras still work?
- Cars with out-of-state plates keep sitting in our lot for weeks — can cameras help get them towed?
- Part of our lot is on the West Shore wetlands — does that change trenching?
- The ground on our hillside lot is shallow bedrock — does that rule out camera poles?
- Our South Beach lot flooded during Sandy — where should the equipment go?
- Our lot backs onto Great Kills Harbor — does the salt air matter?
- Can we keep the cameras we already have and just upgrade the system?
- Can one system cover a shared strip-mall lot with several tenants?
- For a resident lot behind a co-op or condo building, who signs off on the design?
- Can one system cover a below-grade garage and the surface lot together?
- Our marina lot is busy in summer and quiet all winter — does that change the system?
- Can a camera cover a rear or service door that opens onto the lot?
- What happens to coverage when the DOT or a utility tears up the street outside?
- If an entry gate gets added later, how should the wiring be prepped up front?
- Can the cameras cover a dealership inventory row along Hylan Boulevard?
- How is snow handled when plows pile it in the lot?
- Can a school or house-of-worship lot run tighter rules during quiet weeks?

### 4.14 `parking-lot-camera-installation-suffolk-county` (22)
- Commuters and beachgoers leave cars in our lot all day near the ferry — can cameras support enforcement?
- Cars in our South Shore strip-mall lot keep getting broken into — what coverage actually helps?
- Converters keep getting cut off trucks in our Suffolk lot — what footage actually identifies the crew?
- On a tight downtown Suffolk lot, can I put cameras on the neighbouring building?
- Can a plate camera read cars entering the mall or a big-box lot off Route 58?
- Our lot is a wide Suffolk field with no building close by — can cameras still cover it?
- Out-of-state cars sit abandoned in our lot near the LIRR for weeks — can cameras help move them along?
- Part of our lot sits on low, wet South Shore ground — does that complicate the trenching?
- Our North Shore lot hits rock a foot down — does that rule out setting camera poles?
- Our Lindenhurst lot flooded during Sandy — where should the equipment go?
- Our lot backs onto the Great South Bay — does the salt air matter?
- Can we reuse the cameras and cable we already have and just modernise the Suffolk system?
- Can one system serve a shared Suffolk plaza lot split among several tenants?
- On a Suffolk co-op or HOA lot, who has to approve the camera design before it goes in?
- Can a single recorder handle both a parking deck and the open lot beside it on one Suffolk property?
- Our bayfront boatyard is packed all summer and dead through winter — should the system be built around that?
- Can a camera watch a back or service door that opens onto a Suffolk lot?
- If the state DOT or a utility digs up the road outside for months, what happens to the entrance coverage?
- We may gate the lot down the road — how should the cabling be set up now so that is cheap later?
- Can the cameras cover a dealership inventory row along a Suffolk auto corridor?
- How do you keep plow snowbanks from blocking a camera through a Suffolk winter?
- Can a Suffolk school or congregation lot run stricter analytics during its long quiet stretches?

### 4.15 `parking-lot-camera-installation-ulster-county` (27)
- What happens if the trench hits rock in Ulster?
- Will cameras stop the auto thefts the Sheriff keeps warning about?
- How deep do camera pole footings need to be in Ulster?
- Why do Kingston garages and Thruway park-and-ride lots need longer retention?
- My lot is at the Kingston station or a large commuter garage — can you handle that scale?
- My lot is in Woodstock, New Paltz or a historic district — does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Route 9W entrance?
- Can one system cover a garage and the surface lot next to it?
- A Route 9W dealership keeps getting hit overnight. What helps?
- Who owns the poles in my lot?
- Can a system cover an apartment, HOA or campus lot with privacy rules?
- Can you cover a fairground or estate lot that surges on event days?
- Can you cover a horse-country or far-out eastern lot without trenching power to it?
- How does a multi-parcel campus like a hospital, college or the chip plant stay on one system?
- How long does a parking lot camera install take in Ulster?
- Do parking lot cameras need a permit in Ulster?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does a Ulster parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover the western Catskills and Rondout Valley — Phoenicia, Ellenville and Stone Ridge?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?

### 4.16 `parking-lot-camera-installation-westchester-county` (27)
- What happens if the trench hits rock?
- Will cameras actually stop catalytic-converter theft in my lot?
- How deep do camera pole footings need to be in Westchester?
- Why do Metro-North commuter lots need longer retention than a store?
- My lot is in a historic village like Tarrytown or Bronxville. Does that affect the project?
- The internet at my property is slow. Will the cameras still work?
- Can plate cameras read at a busy Central Avenue entrance?
- Can one system cover a parking deck and the surface lot next to it?
- Can you cover a Westchester municipal or village parking lot?
- Can one system cover a hospital or college campus with several entrances?
- My lot is near the Sound or the Hudson. Does salt affect the equipment?
- Who owns the poles in my lot, and can you attach a camera to one?
- Can a system cover an apartment or HOA lot with resident privacy rules?
- A fleet yard on Warehouse Lane keeps getting hit overnight. What helps?
- How does a multi-parcel corporate campus stay on one system?
- How long does a parking lot camera install take in Westchester?
- Do parking lot cameras need a permit in Westchester?
- Can you take over and fix the cameras already on my lot?
- Does the system need a monitoring subscription, or do I own it outright?
- How many cameras does a Westchester parking lot usually need?
- Can a far corner of the lot be covered without trenching power to it?
- Will the cameras keep working in a power outage?
- Do you cover northern-county lots in Bedford, Katonah and Yorktown?
- Can footage be shared with the police or an insurer easily?
- How is winter maintenance and camera cleaning handled?
- Is it worth running conduit now for a future gate or more cameras?
- What does the AESS warranty cover?


### 4.17 `parking-lot-camera-installation-queens` — REBUILT 2026-10-18 (24 questions; all checked by meaning against 4.1–4.16)
§9 Q&A (H3):
- Does a DCWP garage or parking lot licence say anything about cameras?
- Does a camera pole close to JFK or LaGuardia need FAA notice?
- Can we switch on face recognition for the lot cameras?
- Is it legal for the lot cameras to record sound?
- How can footage show that a customer's car never left the lot while they were away?
- Can the recordings settle a dispute when a car is towed off our private lot?
- If someone cuts the power to the lot, how does the footage of them doing it survive? *(nearest register intent: "Will the cameras keep working in a power outage?" (HV counties) — that is an accidental outage; this one is deliberate sabotage and evidence of it. Judged distinct; reviewer may disagree.)*
- Our lot lights run on a photocell — can the cameras borrow that power?
- Will headlights coming off Queens Boulevard blind the entrance camera at night? *(nearest: Manhattan "bright-to-dark transition at a garage mouth" — daytime exposure vs oncoming headlights; judged distinct.)*
- Can the cameras see through the chain-link and privacy slats around our lot?
- Can a Queens retailer claim the state's commercial security tax credit for lot cameras?
- Our lot may be redeveloped in a few years — is a camera system still worth buying?
- Can the cameras work with the pay station or parking app that runs our lot?
- Car meets keep taking over our lot after closing — what can cameras realistically do?
Section headings ending in "?" (CTA headings, not Q&A): "Lot Cameras Dark, Recorder Silent or a Car Gone in Queens?"; "Not Sure Your Lot Would Prove Anything?"
§17 FAQ (= FAQPage schema):
- Do you send a certificate of insurance naming the lot owner and the parking operator?
- Should the cameras be on their own network, apart from customer Wi-Fi and the payment terminals?
- How is payment handled on a Queens lot camera job?
- Will you take down the dead cameras a previous operator left on the poles and walls?
- Can the attendant’s booth show live cameras without giving the attendant playback or export?
- Can a copy of the recordings be kept somewhere other than the lot itself?
- What should we have ready when you come to survey the lot?
- How soon after we approve the estimate can work begin?

---

## Queens

Page: `parking-lot-camera-installation-queens` · up `/parking-lot-camera-installation-nyc` · (347) 434-6392 · Bronx GBP (460 E Fordham Rd, `#bronx`) · prices = silo base × 1.05.
**Thesis:** In Queens the lot usually holds someone else's car (DCWP-licensed garages, JFK/LGA long-stay lots, dealerships and repair rows, building garages), so the system is designed as a custody record — arrival, keys, movement, departure — and built to survive the two ways Queens footage has been lost: a crew cutting the power (Elmhurst dealership, 2022) and water in below-grade garages (Ida, 2021).

### Q-L Landmarks, corridors, places
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Q-L1 | `Queens Boulevard "Boulevard of Death" Vision Zero bike lane redesign 2025 2026` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Queens_Boulevard | 7.5 mi Queens Plaza → Jamaica Ave; ~200 ft wide, 12 lanes, 16 at Yellowstone Blvd; three-lane service roads each side between Roosevelt Ave and Union Tpke; passes Sunnyside, Woodside, Elmhurst, Rego Park, Forest Hills, Kew Gardens, Briarwood; 7 train elevated over it in Sunnyside/Woodside. | §8 Queens Blvd H3; §9 headlights H3 |
| Q-L2 | `Queens Center mall Elmhurst Queens Boulevard parking garage wikipedia` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Queens_Center_Mall | 90-15 Queens Blvd, between 57th Ave and Woodhaven Blvd; opened Sept 12, 1973; 967,000 sq ft GLA; mid-2020s renovation upgraded "the parking lots"; Macerich. | §8 Queens Blvd; §13 card |
| Q-L3 | `Jamaica station AirTrain JFK Sutphin Boulevard wikipedia ridership` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Jamaica_station | 93-02 Sutphin Blvd; junction of LIRR's three main trunk routes; "weekday ridership exceeding 200,000"; "the largest transit hub on Long Island"; AirTrain Jamaica station opened Dec 17, 2003. | §5.5; §8 Jamaica H3; §13 card |
| Q-L4 | `LaGuardia airport new terminal B parking garage Terminal C garage spaces` · WebSearch → WebFetch | https://enr.com/articles/45225-laguardia-airport-terminal-b-garage-airportstransit-best-project-2018 | Terminal B garage: "seven-floor, 1.14-million-sq-ft precast structure providing 3,100 parking spaces" (ENR 2018 Best Projects). | §5.5; §13 card |
| Q-L5 | `Willets Point Iron Triangle auto repair shops history redevelopment 2026` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Willets_Point | 2006 Hunter College study: 225 businesses, 1,400–1,800 employees; "Iron Triangle"; 25,000-seat NYCFC stadium, construction began Dec 2024, expected 2027; 250-room hotel; housing. | §5.5; §8 Willets H3; §13 card |
| Q-L6 | same → WebFetch | https://tollbit.gothamist.com/news/as-nyc-unveils-new-willets-point-redevelopment-auto-repair-shop-owners-gear-up-for-another-fight | Gothamist Nov 16, 2022: city says ~a dozen businesses remain; mechanics say 90+; earlier ~$7M settlement relocated some to Hunts Point. | §8 Willets H3 |
| Q-L7 | `Citi Field parking lots spaces Willets Point Flushing Meadows` · WebSearch → WebFetch | https://www.qchron.com/editions/queenswide/mets-parking-may-come-to-willets-pt/article_a876f562-6035-5751-8e50-e483edf5cf1c.html | Queens Chronicle (year not shown on page): FAA plan — AirTrain construction staging in Citi Field lots, mainly the Southfield lot south of Roosevelt Ave. | §8 Willets H3 |
| Q-L8 | `Resorts World ...` (Wikipedia via WebFetch) | https://en.wikipedia.org/wiki/Resorts_World_New_York_City | 110-00 Rockaway Blvd; opened Oct 28, 2011 on 72.6 acres; Gaming Commission final licence approval Dec 15, 2025; Aqueduct closed June 2026; expansion construction from July 2026. | §13 card |
| Q-L9 | `Northern Boulevard auto row Queens car dealerships corridor Long Island City Woodside` · WebSearch → WebFetch | https://www.brownstoner.com/history/the-carridor-then-and-now | "Carridor" (author's own coinage) on Northern Blvd from Queens Plaza; Ford service station now Center Building, 33-00 Northern Blvd; Pierce-Arrow, Packard, Brewster, Standard. | §8 Northern Blvd H3 |
| Q-L10 | same → WebFetch | https://old.nyc.streetsblog.org/?p=347541 | Streetsblog (undated on page): Jackson Heights dealerships using Northern Blvd sidewalks and curb lanes as showrooms. | §8 Northern Blvd H3 |
| Q-L11 | `Flushing Commons Municipal Parking Lot 1 Flushing history garage spaces` · WebSearch → WebFetch | https://www.citylandnyc.org/conversion-of-flushings-municipal-parking-lot-okd/ | 5.5-acre municipal lot, 37th–39th Aves, Union–138th Sts, 1,101 spaces; Council approved July 29, 2010; 1,600-space underground garage. | §8 Flushing H3; §9 redevelopment H3 |
| Q-L12 | `Queens Business Improvement Districts list …` · WebSearch → WebFetch | https://citymeetings.nyc/city-council/2024-02-29-0100-pm-committee-on-small-business/chapter/which-business-improvement-districts-bids-exist-in-queens-and-what-efforts-are-being-made-to-revitalize-certain-areas | SBS (Feb 29, 2024) names Queens BIDs incl. 160th St, 180th St, 82nd Street Partnership, Bayside Village, Downtown Flushing, Gateway JFK, Jamaica Center, LIC Partnership, Myrtle Ave Queens. | §8 Flushing H3 (Downtown Flushing BID) |
| Q-L13 | WebFetch | https://en.wikipedia.org/wiki/Jackson_Heights,_Queens | Jackson Heights HD designated Oct 19, 1993, ~600 buildings, 76th–88th Sts, Roosevelt Ave to near Northern Blvd, aesthetic protections; Linden Court (1919) first development with resident parking, single-storey garages via narrow driveways. | §7 garage-court card; §7.5 historic-district H3 |
| Q-L14 | carried from research/apartment-building-security-camera-installation.md item 14 | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | LPC staff-level camera permits: limits per 25 ft frontage; fix at mortar joints/plain surfaces; avoid primary facade; conduit concealed or short and painted. | §7.5 historic-district H3 |

### Q-U Use cases / building stock / demographics
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Q-U1 | `Queens Census 2020 population 2,405,464 land area square miles` · WebSearch → WebFetch | https://www.census.gov/quickfacts/fact/table/queenscountynewyork | 2020: 2,405,464; land 108.72 sq mi; owner-occupied rate 2020–2024: 44.9%; foreign-born 47.6%; language other than English 55.4%. | §5.5 bullet 1 |
| Q-U2 | carried from research/nvr-installation.md BX1 | https://www.furmancenter.org/neighborhoods/the-bronx/ | Bronx homeownership 19.7% (2024). | §5.5 bullet 1 (comparison) |
| Q-U3 | DCWP rows G1–G3 (silo) | — | Licence scope/exemptions, capacity docs, insurance, signs, "adequately attended". | §5 para 2; §5.5; §8.5; §9 |

### Q-N News, hyperlocal, Reddit
| Row | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Q-N1 | `Queens stolen cars 2025 parked lot thieves Jamaica Flushing news` · WebSearch → WebFetch | https://www.fox5ny.com/news/luxury-vehicles-stolen-from-queens-dealership | Fox 5, Nov 8, 2022: Carsiri dealership, Queens Blvd & Kneeland St, Elmhurst; 26 vehicles; thieves cut power first so "no surveillance video", forced gate, took keys from office, multiple trips. | hero; §5 para 3; §7 dealership; §8 Queens Blvd; §9 power-cut H3; §10.5 H3 4; custody table |
| Q-N2 | `Hurricane Ida Queens basement garage flooding cars 2021` · WebSearch → WebFetch | https://queenseagle.com/all/unimaginable-loss-eleven-from-queens-die-in-storm | Queens Eagle, Sept 2, 2021: 11 of 12 deaths in Queens; Elmhurst maintenance worker: "We’ve got 31 garage doors here, I’d say half of them are damaged"; flooded BMW under LIRR tracks in Elmhurst; Central Park 3.15 in. in one hour. | §5 para 3 |
| Q-N3 | `Hurricane Ida underground parking garage flooded cars Queens Forest Hills Rego Park building garage` · WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/first-alert-weather-heavy-rain-causes-flooding-on-area-roadways-for-tuesday-morning-commute | CBS NY, Sept 13, 2022: Rego Park basements flooded overnight; cars stuck in Cooper Ave underpass. | §5.5 last bullet |
| Q-N4 | `reddit Queens parking lot car broken into security cameras` · WebSearch → WebFetch | https://digital-release.pix11.com/news/local-news/queens/seven-men-sought-for-stealing-4-cars-from-queens-parking-garage-nypd/amp/ | PIX11, Nov 27, 2023: residential garage 22-44 Jackson Ave, LIC; seven men, four vehicles, ~3:45 a.m. | §8 LIC H3; §10.5 H3 4 |
| Q-N5 | `JFK airport off-airport parking lots Jamaica Rockaway Boulevard theft cars stolen lot` · WebSearch → WebFetch | https://abc7ny.com/traffic/7-on-your-side-investigates-vehicle-damage-and-parking-tickets-at-long-term-lot/5445168/ | ABC7, Aug 9, 2019: Airlot JFK Long-Term Parking, 133-98 142nd St, Jamaica; damaged car, tickets dated while customer abroad; DCA: lacked proper licence, $500 fine. | §8 Rockaway Blvd H3 (lot not named on page) |
| Q-N6 | same → WebFetch | https://www.cbsnews.com/amp/newyork/news/nyc-unlicensed-parking-lot-toll-violation | CBS NY, Nov 22, 2024: JFK Econopark, 147th Ave; GWB toll notice while owner's flight approached Europe; DCWP three violation notices; city sued Way app (Aug 2024) over 46 unlicensed lots. | §8 Rockaway Blvd H3 (lot not named on page); §9 "never left" H3 |
| Q-N7 | `Queens parking lot car meet drifting takeover police 2025` · WebSearch → WebFetch | https://abc7ny.com/18914361/ | ABC7: Apr 18, 2026, 69th St & Elliott Ave, Maspeth, near a gas station; nearly 100 cars; donuts around a fire; CM Phil Wong: "they are fake plates." | §8 LIC/Maspeth H3; §9 car-meet H3 |
| Q-N8 | same → WebFetch | https://www.carscoops.com/2026/05/nypd-queens-takeover-arrests/ | Arrests Apr 23/May 1; two Infinitis impounded; NYPD: "These car meets will not go away unless there are real repercussions…" | §9 car-meet H3 |
| Q-N9 | same (title only) | https://ny1.com/nyc/all-boroughs/public-safety/2026/04/28/nypd-makes-arrests--seizes-cars-at-car-meetups-citywide | NY1 headline (Apr 28, 2026): NYPD makes arrests, seizes cars at car meetups citywide. | §9 car-meet H3 |
| Q-N10 | `Queens tire rim theft crew Queens DA parking lot cars on crates` · WebSearch → WebFetch | https://queensda.org/tire-and-rim-street-crew-busted-for-swiping-expensive-wheels-and-leaving-cars-on-crates-in-queens/ | Queens DA Dec 17, 2020: crew charged with stealing tires/rims (13 neighborhoods) Nov 2019–May 2020, ~$42,000; surveillance video placed defendants near cars. | Not used on page (topic already a register question) |
| Q-N11 | same search | https://qns.com/2026/01/auto-theft-crew-car-flushing-ten-week-crime-spree/ | QNS Jan 5, 2026: Honda Odyssey/Pilot thefts from parked cars in Flushing, Fresh Meadows, Kew Gardens Hills, Forest Hills (Oct–Dec 2025). | Not used on page (street thefts, NYPD-sourced) |
| R1–R5 | silo §2.1 | — | r/Queens, r/astoria, r/AskNYC, r/longisland excerpts. | §5 para 2; §8 Rockaway; §9 tow H3 |

Not used by rule: NYPD precinct grand-larceny-auto statistics (Queens Post / Flushing Post "crunching the Queens crime numbers" search titles) — blueprint Appendix B keeps NYPD crime-data citations to the six NYC solar pages.

### Q-IMG Images (11, in images/parking/)
Permanent image rule — every existing images/parking/*.webp viewed sample (queens garage, 4K bullet, lot installation) is AI-generated → none used. Sources viewed with Read before use; crops exclude signs, logos, people, plates, house numbers.
| File | Source | What it shows |
|---|---|---|
| parking-lot-camera-installation-queens-recorder-grid-service-bays-and-lot.webp (hero, og) | images/rockland-toyota-nvr-monitor.jpeg (crop) | recorder grid: service bays, offices, parked cars, bitrate table |
| …-home-runs-above-equipment-rack.webp | images/rockland-toyota-nvr-monitor.jpeg (second crop) | cable bundles into a rack beside the monitor |
| …-side-lot-camera-tile-brick-wall.webp | images/nassau-window-depot-monitor.jpeg (CAM 2 tile only) | paved side lot along a brick wall |
| …-bullet-camera-high-wall-above-ceiling.webp | images/rockland-toyota-wall-camera.jpeg (crop) | bullet camera high on a wall |
| …-bullet-camera-on-ceiling-mount.webp | images/rockland-toyota-ceiling-bullet.jpeg (top crop) | bullet on ceiling mount |
| …-camera-aimed-down-corridor-to-steel-door.webp | images/rockland-toyota-hallway-camera.jpeg (crop, poster/QR removed) | camera down corridor to steel door |
| …-dome-camera-under-fascia-bare-tree.webp | images/manhattan-deli-exterior-camera.jpeg (crop below sign text) | dome under fascia, mural edge, tree |
| …-turret-camera-corner-stained-ceiling.webp | images/nassau-window-depot-storage-camera.jpeg (top crop) | turret in corner under stained tiles |
| …-small-camera-beside-exit-sign-ceiling.webp | images/rockland-toyota-active-deterrent.jpeg (top crop, mural/banners removed) | small ceiling camera near exit sign |
| …-lpr-bullet-camera-product-photo.webp | images/ubiquiti-unifi-ai-lpr-bullet-4k-camera-black.jpg | manufacturer product shot |
| …-ptz-camera-product-photo.webp | images/ubiquiti-unifi-ai-ptz-industrial-4k-camera-black.jpg (cropped off "Compare" label) | manufacturer product shot |
images: 11 = 9 real AESS job photos from other jobs + 2 manufacturer product shots.

### Q-FLAG Unsourced house practices on the Queens page (Anwar to confirm)
- Default microphones off; face recognition off by default; continuous recording on lanes; retention-by-lot-type table; pre-record buffer; separate camera network segment; off-site copy of lane/key channels; recorder placement away from booth; UPS on separate circuit; night survey for glare; fence-mount/IR advice; COI naming multiple parties; removing abandoned cameras; start-window wording; install-day staging.
- ADT/Ring/SimpliSafe comparison table (general product knowledge, not sourced this build).
- Field Notes is installer-voice method, not a specific Queens job (no anecdote invented).
- Similarity (masked, 5-word shingle Jaccard / paragraph SequenceMatcher vs all 15 siblings): page ≤ 0.012; max paragraph 0.61 (Premium package card vs NYC hub Premium card).
