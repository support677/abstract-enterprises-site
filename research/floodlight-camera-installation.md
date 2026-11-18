# Floodlight Camera Installation — silo research

Created 2026-10-18 by the REBUILD run for `floodlight-camera-installation-brooklyn` (queue line: `REBUILD | floodlight-camera-installation-brooklyn | Floodlight Camera Installation | Brooklyn | up /floodlight-camera-installation-nyc | (347) 934-8335 | GBP Brooklyn`). First research file for this silo.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Tools used: WebSearch, WebFetch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`) and Firecrawl scrape (summary). Shell curl is blocked. Some facts were carried from `research/dvr-upgrade.md` (fetched 2026-10-18 by the DVR rebuild run) and are marked "carried from dvr-upgrade.md". "Excerpt" = search-result snippet only.

Page section labels: §Hero, §Quick (instant action block), §5 Neighborhood (+§5.5 facts), §Repair1, §6 Services, §7 Architecture (+§7.5), §8 Commercial (+§8.5 rules), §9 Q&A (cluster/H3), §10 Equipment (+ Ring/ADT/SimpliSafe comparison), §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+BYOE), §FN Field Notes, §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every floodlight page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl search snippets; Firecrawl scrape refuses reddit.com — "we do not support this site"). Rows R1–R6. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and frames each H3 as a claim published by cost guides, manufacturers and install blogs (rows A1–A6, P1–P4), then corrects it. |
| 6 | Area landmarks | Brooklyn section rows L1–L8. |
| 7 | Area use cases / building stock | Brooklyn section rows H1–H3, C1–C5. |
| 8 | Bing & DuckDuckGo (PAA / related / autocomplete) | EMPTY (not accessible in build env) — WebSearch returns result links only, no PAA/related/autocomplete panels. |
| 9 | Local news | Brooklyn rows N1–N8 (Brooklyn Eagle, CBS New York, NY1, News 12, Brownstoner). |
| 10 | Hyperlocal | Brownstoner (N1, N2), Brooklyn Paper (N6, C3), Brooklyn Eagle (N3), News 12 Brooklyn (N7, N8). |
| 11 | Yelp 1–3★ | Firecrawl search returned Yelp search-list excerpts only (no 1–3★ review text for floodlight or outdoor-light installers) → EMPTY (not accessible in build env). Not used. |

### 1.2 Reddit and forums (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit floodlight camera neighbor complaint too bright motion light angle` · Firecrawl search | https://www.reddit.com/r/HomeMaintenance/comments/1l8u4v5/ive_been_cited_for_my_ring_floodlight_shining/ | Excerpt (title): "I've been cited for my Ring floodlight shining into my neighbor's yard"; reply advises putting the light/camera "on the far side of YOUR yard facing YOUR windows… at a low enough height". Location unknown. Scrape refused. | Background for §9 cluster 2 and FAQ 3 (fence-post light facing the house); not quoted |
| R2 | same | https://www.reddit.com/r/AskSF/comments/1fg06qm/neighbor_shining_floodlight_directly_into_my/ | Excerpt: neighbor asked repeatedly "to adjust the angle of the light and fix the motion sensing" — nothing done. (San Francisco.) | Background §9 cluster 2 H3 2 (angle + motion are the usual causes) |
| R3 | same | https://www.reddit.com/r/homeowners/comments/1mxqrmr/nextdoor_neighbor_has_a_flood_light_that_shines/ | Excerpt: "Offer to buy a motion sensing adapter if security is their concern." | Background §9 cluster 2 |
| R4 | same | https://www.reddit.com/r/wyzecam/comments/s1238t/how_to_stop_my_neighbors_light_from_triggering_a/ | Excerpt: "Don't point your camera at your neighbor's house? … angle that guy down more." | Background §9 cluster 2 H3 3 |
| R5 | `site:reddit.com Brooklyn floodlight camera backyard brownstone` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/j1avtf/has_anyone_ever_tried_or_succeeded_to_break_in/ | Excerpt (fire-escape break-ins thread): "ask the landlord to install a flood light". | Background only |
| R6 | same | https://www.reddit.com/r/femalelivingspace/comments/17uejz2/for_women_who_live_alone_what_kind_of/ | Excerpt: resident in "a safe area of Brooklyn" — "motion sensor flood lights on any gate into my backyard. Motion sensor blink cameras." | Background §5 (rear gate is the floodlight spot) |

### 1.3 Cost guides / install blogs (feed §10.5)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `floodlight camera installation cost Angi HomeAdvisor electrician average` · WebSearch → WebFetch | https://inchcalculator.com/floodlight-cost-guide | Page last updated Aug 14, 2023 (title says 2026). National average ~$450; most projects $250–$800; installation ~$150–$350 per light; fixtures $75–$250; electrician $50–$200/hr; new wiring $100–$300 or $2–$4/ft; outdoor GFCI outlet ~$325; permits $20–$100 "may or may not be required"; advises against extension cords; professional "may be a legal requirement depending on your area". | §10.5 H3 1; §Sources |
| A2 | `reddit floodlight camera install brick wall no junction box NYC rowhouse` · WebSearch → WebFetch | https://www.homecamcafe.com/how-to-mount-a-floodlight-camera-without-a-junction-box/ | Plug-in mount connects to "a standard outdoor GFCI outlet via a weatherproof power cable"; "No electrical work required beyond confirming you have a working outdoor outlet nearby"; outlet "must be an outdoor-rated GFCI outlet"; cable "weatherproof but not armored"; electrician install "runs around $650 on average"; eufy E340 AC-cable version designed for no-box installs. | §10.5 H3 1, H3 2; §9 cluster 1 H3 1; §Sources |
| A3 | Angi / HomeAdvisor / Fixr floodlight-camera pages | — | Not reached (no Angi/HomeAdvisor/Fixr floodlight page surfaced in the searches run) → EMPTY. The old Brooklyn page's "Angi, HomeAdvisor and Fixr publish ~$400 a light" claim was unsourced and is NOT carried. | — |

### 1.4 Manufacturer / product facts
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `Ring Floodlight Cam Wired Pro 2000 lumens junction box requirements mounting height 9 feet` · WebSearch → WebFetch | https://ring.com/support/articles/b2io6/Installing-Your-Floodlight-Cam | Mount "about nine feet above ground level, if possible", motion sensor parallel to ground; turn off power at breaker/fuse; black-to-black, white-to-white, copper/green ground; attaches to "your junction box". | §10.5 H3 3; §10 comparison; §Sources |
| P2 | `floodlight camera installation cost …` · WebSearch → WebFetch | https://blog.arlo.com/home-security-tips/how-to-install-wired-floodlight-cameras/ | "choose a location with an existing junction box"; disconnect power at breaker; hot/neutral/ground; if "not comfortable with electrical work" → "look for a licensed electrician"; "choose a location with a strong Wi-Fi signal". | §10.5 H3 5, H3 6; §Sources |
| P3 | `Lorex 4K floodlight wired security camera PoE NVR specs lumens` · WebSearch → WebFetch | https://www.lorex.ca/products/lorex-fusion-4k-8-channel-2tb-wired-nvr-system-with-six-4k-ip-cameras-2k-indoor-wi-fi-security-camera-and-wi-fi-floodlight-camera | Lorex 1080p Wi-Fi floodlight: "2 × 2000 lumens light arrays"; 137° FOV; uses "existing wiring from your previous floodlight or outdoor house light"; 32 GB microSD; no monthly fee; can record to Fusion NVR (2 Wi-Fi devices max). | §10.5 H3 4; §9 cluster 2 H3 1; §Sources |
| P4 | `PoE floodlight camera 802.3at single Ethernet cable powers light and camera spec sheet` · WebSearch → WebFetch | https://reolink.com/product/reolink-duo-floodlight-poe/ | Spec: "IEEE 802.3at, 48V Active" (FAQ says 802.3af — page inconsistent); floodlight 1,800 lumens /15 W/4200K; "uses only one network cable to transmit power and data"; no subscription required. | §9 cluster 1 H3 1; §10.5 H3 4, H3 6; §Sources |
| P5 | same family · WebFetch | https://www.lorex.com/en-au/products/lorex-connect-v5-4k-poe-bullet-cameras-with-color-smart-security-lighting | Lorex CN502 4K PoE bullet with "color security lighting and siren"; no lumen rating. | Background §10 PoE spotlight card |
| P6 | `floodlight camera installation Brooklyn` · WebSearch | https://service.eufy.com/ca/article-description/Floodlight-Cam-Installation-FAQ → redirect https://service.anker.com/… | WebFetch: permission request not answered → EMPTY (not accessible in build env). | — |

### 1.5 Rules relevant to every NYC floodlight page
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `NYC licensed electrician required to install light fixture homeowner DOB electrical permit` · WebSearch → WebFetch | https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-electrical.page | "No installation and modification to any electrical systems can be performed without a permit and a Licensed Master Electrician." "Minor Electrical Work" includes "Replacing fixtures in existing outlets, no more that 5 fixtures; no increase in wattage" — still needs LME + permit, no RDP, no DOB inspection; general work is DOB-inspected. | §5 para 4; §5.5 bullet 3; §8.5 bullet 1; §9 cluster 4 H3 1; §10.5 H3 5; §Sources |
| G2 | same · WebFetch | https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-alt-1-2-family-buildings.page | 1–2 family: electrical work "shall be performed by a New York City licensed electrical contractor"; covers "new installation, alteration, or repair of electric wiring…". | §Sources (supports G1) |
| G3 | `Landmarks Preservation Commission rules light fixtures security cameras rowhouse facade permit` · WebSearch → WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Light fixtures (p.11.7): staff permit if "within or next to a door opening"; "no more than two light fixtures and one intercom panel per door opening"; design/size/finish compatible (neutral, discreet); in-kind replacement exempt from elevation drawings; bulb changes/maintenance need no permit. Cameras: ≤2 per 25 ft frontage (small bldgs), ≤3 (large). General: avoid primary facade unless no option; discreet spots "beneath a band course, under a stoop, behind an areaway wall or fence, or behind plantings"; attach at mortar joints/plain masonry/wood/metalwork, not cast iron or decorative surfaces; ~10 in visible conduit, painted, in mortar joints; cut sheets with application via Portico. | §5.5 bullet 4; §6 card; §8.5 bullet 2; §9 cluster 3 (all three H3); §10.5 H3 2; §17 FAQ 4, FAQ 9; §Sources |
| G4 | `NYC light trespass law outdoor lighting neighbor complaint 311 floodlight` · WebSearch → Firecrawl scrape (summary) | https://intro.nyc/0753-2024 (→ legistar.council.nyc.gov ID 6632268) | Int 0753-2024 "in relation to light pollution from light fixtures in a residential district": would prohibit non-government outdoor lights over **3,000 lumens** unless fully shielded; **$50** civil penalty; sponsors **Robert F. Holden, Kristy Marmorato**; referred to Committee on Environmental Protection, Resiliency and Waterfronts. (WebFetch of legistar URL: permission not answered — Firecrawl used instead.) Proposal, not law. | §10.5 H3 4; §9 cluster 2 H3 1; §Sources |
| G5 | same · WebSearch | https://cityrulelookup.com/outdoor-lighting/light-trespass/kings-county-ny | WebFetch error → EMPTY (not accessible in build env). No NYC light-trespass statute found → page claims none. | — |
| G6 | carried from dvr-upgrade.md (G1) | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a: private right of action vs person who installs video imaging device on adjoining property to record a residential backyard without written consent. | §8.5 bullet 3; §9 cluster 2 H3 3; §10.5 H3 7; §Sources |
| G7 | carried from dvr-upgrade.md (G2) | https://nysenate.gov/legislation/laws/pen/250.40 | Unlawful-surveillance definitions: place where a person could reasonably expect to disrobe in privacy. | §8.5 bullet 4; §Sources |
| G8 | carried from dvr-upgrade.md (G4) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: ≤50 employees; up to $3,000 per retail location; cameras eligible; apply by Oct 31. | §8.5 bullet 5; §Sources |
| G9 | `NYC DOT LED streetlight conversion completed 250,000 streetlights` · WebSearch → WebFetch | https://cbsnews.com/newyork/news/bright-lights-big-city-nyc-swapping-all-250000-street-lights-to-led | Oct 24, 2013: all 250,000 NYC street lights to LED by 2017 (four-year plan); ~$14M/yr savings; Sadik-Khan: "clearer, whiter and more attractive". (nyc.gov press page fetched empty.) | §5.5 bullet 5; §9 cluster 7 H3 1; §Sources |
| G10 | Con Edison | `Con Edison residential electricity rate per kWh 2025 …` · WebSearch | Only third-party rate pages surfaced; no Con Edison figure used → EMPTY for rates. Con Edison named only in FAQ 2 (power outage behaviour, no statistic). | §17 FAQ 2 (name only) |

### 1.6 Keyword plan (five layers, silo)
- **Service:** floodlight camera installation, floodlight cam install, floodlight security camera, outdoor floodlight camera, motion floodlight camera, hardwired floodlight camera, PoE floodlight camera, spotlight camera, floodlight replacement, yard light camera.
- **Problem:** no junction box, no outdoor power, light shining into neighbor's window, light trespass, floodlight stays on, floodlight not turning on, camera offline at night, washed-out faces, false motion alerts, rear-window burglary, backyard break-in, package theft, dark driveway, dark areaway.
- **Technology:** junction box, line voltage / 120 V, GFCI outlet, plug-in conversion kit, PoE (802.3af/at), lumens, colour temperature, PIR motion sensor, motion zones, privacy masking, WDR, pan-tilt, siren, microSD, NVR, mesh Wi-Fi / outdoor access point.
- **Industry:** brownstone and rowhouse owners, two-family landlords, detached-house owners, landmarked-house owners, warehouse and loading-dock operators, Navy Yard / Industry City tenants, retail rear doors.
- **Geographic (Brooklyn page):** Brooklyn; Bed-Stuy, Crown Heights, Park Slope, Prospect Heights, Clinton Hill, Fort Greene, Brooklyn Heights, Flatbush, East Flatbush, Midwood, Canarsie, Bushwick, Williamsburg, Greenpoint, Sunset Park, Red Hook, Gowanus, Bay Ridge, Dyker Heights, Bensonhurst, Gravesend, Sheepshead Bay, Marine Park, Mill Basin, Manhattan Beach, Windsor Terrace, Kensington, Carroll Gardens, Gerritsen Beach, East Williamsburg (Meadow Street), Nostrand Avenue, Fifth Avenue (Bay Ridge), Fulton Mall; Park Slope HD, Brooklyn Heights HD, Dyker Heights holiday lights, Industry City, Brooklyn Navy Yard; Troy Avenue office.

### 1.7 Silo pricing (no invented prices) — FLAG
Existing pages (pre-rebuild, read 2026-10-18):
| Page | Fixture swap | New wiring | 2–4 cams |
|---|---|---|---|
| brooklyn (old) / bronx / queens | $300–$575 | $575–$1,500 | $1,300–$3,800 |
| nyc hub | $275–$550 | $550–$1,200 | $1,100–$3,200 |
| long-island hub | $275–$550 | $550–$1,400 | $1,200–$3,600 |
| staten-island | $330–$630 | $630–$1,650 | $1,450–$4,200 |
| nassau-county | $330–$630 | $630–$1,700 | $1,500–$4,400 |
| rockland-county | $330–$640 | $620–$1,700 | $1,500–$4,400 |
| westchester-county | $330–$640 | $640–$1,900 | $1,550–$4,900 |
| manhattan, suffolk, orange, putnam, dutchess, ulster, hudson-valley | different card format (not parsed) | | |

Brooklyn rebuild keeps **$300–$575 / $575–$1,500 / $1,300–$3,800** as the §9 base (Brooklyn = 1.00×; Bronx parity matches; Staten Island ≈ ×1.10). **Inconsistencies to flag:** NYC hub is *below* the Brooklyn base; Queens equals Brooklyn (should be ×1.05); Nassau (×1.15 → $345–$661), Rockland (×1.30), Westchester (×1.25) do not follow the multipliers. Service rate $195/hr, 3-hr min ($585) per §9 (protected). Camera hardware extra; "custom system — quoted after walk-through" carried.

---
## Question register — every question on every Floodlight Camera Installation page

Rule: no new page may reuse any question below, by wording or by intent (geo-masked).

### floodlight-camera-installation-brooklyn — REBUILT 2026-10-18 (this run): 23 headings ending in '?' (21 Q&A H3 + repair H2 + comparison H3) + 10 FAQ
Q&A / headings (section §9 unless noted):
- Floodlight Dead, Stuck On or Flashing All Night?
- Our rowhouse has no outdoor fixture at the rear — what are the options besides cutting a new 120-volt circuit through the brick?
- The only exterior box at the back is on a switch inside the kitchen — will the camera keep recording when someone flips it off?
- Is the old porch-light box over our garden door strong enough to carry a heavier floodlight camera?
- How bright, and how warm a colour, should the light be for a twenty-foot Brooklyn yard?
- A neighbor has complained about our existing floodlight — what can be changed short of taking it down?
- Our fence is low — will the camera end up recording the yard next door?
- How many lights may go beside the front door of a landmarked Park Slope house, and can one of them carry a camera?
- Does a floodlight on the rear wall of a landmarked house need anything from the Commission?
- Our brownstone's areaway and under-stoop entrance are pitch dark — what fits there without breaking the facade rules?
- What does the DOB's “minor electrical work” category mean for a floodlight swap on a Brooklyn house?
- Which part of a floodlight job is low-voltage work, and why does that matter for a brick house?
- Can the floodlight camera run off the same network cable as our other cameras?
- Where should the floodlight sit on a Marine Park house whose driveway runs back to a rear garage?
- Do detached houses in Mill Basin or Dyker Heights need different hardware from rowhouses?
- Dyker Heights draws holiday crowds onto our block — should the camera record the sidewalk at all in December?
- Will a consumer floodlight camera hold up on a Sunset Park or Red Hook loading door?
- Our East Williamsburg unit shares a building with other tenants — who should own and control the yard light?
- Can the lot light stay on a schedule during business hours but switch to motion after closing?
- Our block's LED streetlight already lights the sidewalk — does a floodlight still add anything at the front?
- At the back of a rowhouse, should the light and the camera be one unit or two separate devices?
- Is it worth running a network cable to the back of a brownstone rather than relying on Wi-Fi?
- Ring, ADT or SimpliSafe — or a Brooklyn installer?
FAQ (§17, = FAQPage schema):
- How far ahead do we need to book a Brooklyn floodlight visit, and can it be on a weekend?
- Will a floodlight camera keep working during a Con Edison outage?
- Can the floodlight go on a wood fence or a post at the back of the yard instead of on the house?
- What happens to the old outdoor light we take down?
- Do we need to be home for the whole visit?
- Can the downstairs and upstairs households in our two-family both see the yard camera?
- Can the floodlight switch on when our burglar alarm goes off?
- Our bedroom is right above the garden door — will the floodlight light up our own room?
- Can the floodlight housing be painted to match our dark brick?
- We plan to sell the house next year — does the floodlight camera stay with it?

### floodlight-camera-installation-bronx — old template (pre-rebuild)
- How much does floodlight camera installation cost in the Bronx?
- Do you run new wiring out to a detached garage or backyard?
- Are you actually local to the Bronx?
- Can I install a floodlight camera myself in the Bronx?
- I own a two-family or walk-up in the Bronx — where can I put floodlight cams?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight keeps triggering on cars going by — can you fix that?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Will it survive a Bronx winter?

### floodlight-camera-installation-brooklyn — OLD TEMPLATE (pre-rebuild, all removed 2026-10-18; listed so they are not reused)
- How much does floodlight camera installation cost in Brooklyn?
- Do you run new wiring out to a rear yard or detached garage?
- Can I install a floodlight camera myself in Brooklyn?
- I rent in Brooklyn — can I install a floodlight camera outside?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight keeps triggering on people walking by — can you fix that?
- Does the floodlight record in color at night?
- Will it survive a Brooklyn winter?
- Can a floodlight camera scare off an intruder, not just record one?
- Do I need a licensed contractor for a floodlight camera in Brooklyn?

### floodlight-camera-installation-dutchess-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Dutchess County?
- Do you run new wiring out to a barn, detached garage, or driveway end?
- Can you cover a horse farm or a multi-building estate?
- Do I really need surge protection and winterizing up here?
- Do I need more than one floodlight for a long driveway?
- My floodlight triggers all night on deer — can you fix that?
- I live in a Rhinebeck or Hyde Park historic district — can you install one?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Do you cover the whole county, out to the Harlem Valley?

### floodlight-camera-installation-hudson-valley — old template (pre-rebuild)
- How much does floodlight camera installation cost in the Hudson Valley?
- Can you put a floodlight camera where there’s no power or Wi-Fi?
- Deer and animals trigger my cameras all night — can you fix that?
- Do you run new wiring out to a barn or detached garage?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- Will it survive a Hudson Valley winter?
- I’m only up on weekends — can I watch the place from the city?
- Can a floodlight camera scare off an intruder, not just record one?
- Do I need a licensed contractor for a floodlight camera?
- Can you cover a larger estate, farm, or multiple buildings?

### floodlight-camera-installation-long-island — old template (pre-rebuild)
- How much does floodlight camera installation cost on Long Island?
- Do you run new wiring out to a detached garage or shed?
- Can I install a floodlight camera myself?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight keeps triggering on cars going by — can you fix that?
- Does the floodlight record in color at night?
- Will it survive a Long Island winter?
- Can a floodlight camera scare off an intruder, not just record one?
- Do I need a licensed contractor for a floodlight camera?
- Can you cover a larger lot, an estate, or a seasonal home?

### floodlight-camera-installation-manhattan — old template (pre-rebuild)
- How much does floodlight camera installation cost in Manhattan?
- Do I need co-op or condo board approval for a floodlight camera?
- Can you run power to my rear garden, roof, or terrace?
- Why is my stoop or vestibule camera footage washed out at night?
- My camera keeps dropping offline — can you fix it?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- How high should a floodlight camera be mounted?
- Can a floodlight camera scare off an intruder, not just record one?
- Do I need a licensed contractor for a floodlight camera in Manhattan?
- Can you cover a whole townhouse — front, rear, and roof?

### floodlight-camera-installation-nassau-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Nassau County?
- Do you run new wiring out to a detached garage, pool house, or driveway end?
- Will a floodlight camera survive the salt air near Long Beach or the Five Towns?
- Can I install a floodlight camera myself in Nassau?
- Do I need two floodlights for a long driveway?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight triggers all night on passing cars — can you fix that?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- My village or HOA has exterior-hardware rules — can you work with that?

### floodlight-camera-installation-nyc — old template (pre-rebuild)
- How much does floodlight camera installation cost in NYC?
- Do you run new wiring if there’s no power where I want the floodlight?
- Can I install a floodlight camera myself?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight keeps triggering on cars — can you fix that?
- Does the floodlight record in color at night?
- Will it survive NYC weather?
- Can a floodlight camera scare off an intruder, not just record one?
- Do I need a licensed contractor for a floodlight camera?
- Can you install a floodlight cam on my business or apartment building?

### floodlight-camera-installation-orange-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Orange County?
- Do you run new wiring out to a barn, detached garage, or driveway end?
- Can you cover a working farm or horse property?
- Do I really need surge protection and winterizing up here?
- Do I need more than one floodlight for a long driveway?
- My floodlight triggers all night on deer — can you fix that?
- Can I install a floodlight camera myself in Orange County?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Do you cover the whole county, out to the far west?

### floodlight-camera-installation-putnam-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Putnam County?
- Do you run new wiring out to a detached garage, dock, or driveway end?
- Can I watch a weekend or seasonal home all week?
- Will a floodlight camera survive a Mahopac or Lake Carmel lakefront?
- Do I need more than one floodlight for a long driveway?
- My driveway floodlight triggers dozens of times a night on deer — can you fix that?
- Can I install a floodlight camera myself in Putnam?
- I live in a Cold Spring or Garrison historic district — can you install one?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?

### floodlight-camera-installation-queens — old template (pre-rebuild)
- How much does floodlight camera installation cost in Queens?
- Do you run new wiring out to a detached garage or backyard?
- Can I install a floodlight camera myself in Queens?
- I own a two or three-family in Queens — where can I put floodlight cams?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight keeps triggering on cars going by — can you fix that?
- Does the floodlight record in color at night?
- Will it survive a Queens winter?
- Can a floodlight camera scare off an intruder, not just record one?
- My home is in Forest Hills Gardens — are there special rules for exterior cameras?

### floodlight-camera-installation-rockland-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Rockland County?
- Do you run new wiring out to a detached garage or the far corner of the lot?
- Do I really need surge protection on a floodlight camera up here?
- Can two-family and multi-family buildings get floodlight cams?
- Will the floodlight light up my neighbor’s house on a tight lot?
- My floodlight triggers all night on deer out toward Stony Point — can you fix that?
- Can I install a floodlight camera myself in Rockland?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- How fast can you get to Rockland?

### floodlight-camera-installation-staten-island — REBUILT 2026-10-18: 18 Q&A H3 + 10 FAQ
Q&A (§9):
- Our house was raised after Sandy and the front door now sits at the top of a long stair — where does the floodlight belong?
- Can a light go under the raised floor where we now park the car?
- Where should the camera's switch and recorder live in a house whose ground floor is built to take water?
- Our house is vinyl-sided — how is a floodlight fixed without cracking the siding or letting water in behind it?
- The garage is built into the front of the house — will headlights pulling in blind a camera over the garage door?
- On a semi-attached house, should the floodlight go on the shared-driveway side or the open side?
- The streetlight on our block has been out for weeks — should our floodlight stay on all night until the city fixes it?
- How do we get the dark streetlight repaired, and can our camera help prove how long it has been out?
- Can a floodlight camera capture the license plate of a car that pulls into our driveway at night?
- What does the precinct actually need from our driveway footage, and how do we hand it over?
- We park work vans in the yard overnight — how do we light underneath them for catalytic converter thieves?
- Our back yard ends at the Greenbelt woods — how far toward the trees should the light reach?
- Our house sits well above the street — can a light at the top still show who is at the bottom of the steps or the gate?
- Our Victorian has a deep wraparound porch — can the light hang from the porch ceiling instead of the wall?
- The lot behind our Hylan Boulevard store backs onto houses — who handles a complaint about our lights?
- Does a floodlight camera make sense on a large West Shore truck yard, or does that need pole lighting?
- Would the proposed state Dark Skies bill make us switch the floodlight off at 11 p.m.?
- Does the City Council's 3,000-lumen bill affect a floodlight on a detached Staten Island house?
FAQ (§17, = FAQPage schema):
- We are about to raise or renovate the house — should the floodlight go up now or wait?
- Will our homeowner's insurance company give us anything for a floodlight camera?
- What does a floodlight camera need each year to keep working well?
- Can a floodlight be fixed to the gutter or the roof eave instead of the wall?
- A neighbor's floodlight shines into our bedroom — what can we actually do about it?
- How long does a floodlight installation take on a typical Staten Island house?
- If we replace our siding later, will you take the floodlight down and put it back?
- What happens to our floodlight camera if the company behind its app shuts down or changes its plans?
- The previous owner left a floodlight we do not want — can you take it down and make the wall good?
- Will a floodlight camera slow down our home internet?

### floodlight-camera-installation-staten-island — OLD TEMPLATE (pre-rebuild, all removed 2026-10-18; listed so they are not reused)
- How much does floodlight camera installation cost on Staten Island?
- Do you run new wiring out to a detached garage, pool house, or driveway end?
- Will a floodlight camera survive a South Shore flood zone or salt air?
- Can I install a floodlight camera myself on Staten Island?
- Do I need two floodlights for a long driveway?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- How high should a floodlight camera be mounted?
- My floodlight triggers all night on deer and cars — can you fix that?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Do you charge extra to come to Staten Island?

### floodlight-camera-installation-suffolk-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Suffolk County?
- Do you run new wiring out to a barn, detached garage, or driveway end?
- Can I watch a seasonal Hamptons or North Fork home in the off-season?
- Will a floodlight camera survive the North Fork or Hamptons salt air?
- Do I need more than one floodlight for a long driveway?
- Can I install a floodlight camera myself in Suffolk?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- My floodlight triggers all night on deer — can you fix that?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Do you cover the whole county, out to the East End?

### floodlight-camera-installation-ulster-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Ulster County?
- Do you run new wiring out to a barn, studio, or driveway end?
- My property has almost no cell signal — will the camera work?
- Can you cover a farm, vineyard, or mountain estate?
- Do I really need surge protection and winterizing up here?
- Do I need more than one floodlight for a long driveway?
- My floodlight triggers all night on deer and bear — can you fix that?
- I live in the Kingston Stockade District or on Huguenot Street — can you install one?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?

### floodlight-camera-installation-westchester-county — old template (pre-rebuild)
- How much does floodlight camera installation cost in Westchester County?
- Do you run new wiring out to a pool house, detached garage, or driveway head?
- Do I really need surge protection on a floodlight camera up here?
- Can you cover a big wooded estate with multiple buildings?
- Do I need more than one floodlight for a long driveway?
- I live in a Tarrytown or Sleepy Hollow historic district — can you install one?
- My floodlight triggers all night on deer and branches — can you fix that?
- What floodlight camera brands do you install?
- Which floodlight cameras have no monthly fee?
- Does the floodlight record in color at night?
- Can a floodlight camera scare off an intruder, not just record one?
- Do you cover the whole county, cities and estates alike?


---

## Brooklyn

Page: `floodlight-camera-installation-brooklyn` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Up-link `/floodlight-camera-installation-nyc`. GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`). Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis:** in Brooklyn a floodlight camera is a lighting decision before a camera decision — the dark that needs lighting is the rear yard of attached housing, twenty-odd feet from the next row's windows; the job is finding power on a bare brick wall (existing box vs PoE spotlight on one low-voltage cable vs plug-in vs a new box by a licensed master electrician under DOB rules), aiming and dimming the light so it stops at your fence (52-a, neighbour complaints, Int. 753), keeping landmarked fronts to the LPC door-opening rule, and handling the outliers (southern-Brooklyn driveways, industrial loading walls).

### Building stock (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | carried from dvr-upgrade.md H1 (Census API ACS 2023 5-yr, Kings County) | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36047 | 1,090,187 units; median year built 1943; 513,629 built ≤1939; 1-unit attached 93,812; 1-unit detached 52,359; 2-unit 175,805; 3–4 unit 170,655 (sum 346,460 → page says "346,000 or so"). | §5 para 1; §5.5 bullets 1–2; §Sources |
| H2 | `Mill Basin Brooklyn detached homes driveways waterfront Marine Park neighborhood houses` · WebSearch → WebFetch | https://www.bhsusa.com/neighborhood/new-york-city/brooklyn/mill-basin/ | "Housing in Mill Basin consists largely of detached and semi-detached homes"; "Many properties include driveways, private outdoor space, or waterfront access"; near Jamaica Bay, Marine Park nearby. | §7 card + §7.5; §9 cluster 5 H3 2; §13 card; §Sources |
| H3 | `Park Slope Historic District designated 1973 …` · WebSearch → WebFetch | https://hdc.org/hdc-across-nyc/brooklyn/deserving-designated/park-slope/ | Park Slope HD designated 1973; South Slope extension April 2012; "two- and three-story rowhouses with deep front yards". | §9 cluster 3 H3 1; §13 card; §Sources |

### Landmarks / LPC (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | see G3 (LPC Permit Guidebook ch. 11) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | door-opening light rule; under-stoop/areaway discreet locations; mortar-joint attachment. | §9 cluster 3; §FAQ 4, 9 |
| L2 | carried from dvr-upgrade.md L3 (excerpt) | https://shermanarchitects.com/navigating-the-landmarks-preservation-commission/ | "The LPC is most concerned with what's visible from the street. Rear-yard extensions… that aren't visible from public thoroughfares have an easier approval path". | §9 cluster 3 H3 2; §Sources |
| L3 | carried from dvr-upgrade.md L4 | https://thebha.org/neighborhood/ | Brooklyn Heights HD designated November 23, 1965, NYC's first. | §13 card; §Sources |
| L4 | `Dyker Heights Christmas lights 83rd to 86th Street 11th to 13th Avenue crowds residents` · WebSearch → WebFetch | https://longisland.news12.com/beloved-annual-holiday-lights-display-brings-crowds-to-dyker-heights | Nov 29, 2024: displays "from 11th to 13th avenues and 83rd to 86th streets"; draws crowds (no numbers, no resident concerns given). | §9 cluster 5 H3 3; §13 card; §Sources |
| L5 | carried from dvr-upgrade.md L7 | https://industrycity.com/ | "6-million-square-foot ecosystem" (former Bush Terminal). Acreage not used (sources conflict). | §8 card; §13 card; §Sources |
| L6 | carried from dvr-upgrade.md L6 | https://www.brooklynnavyyard.org/brooklyn-navy-yard-fy25-impact-report/ | >300 acres; >550 businesses. | §8 card; §13 card; §Sources |

### News / hyperlocal (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | `NYC light trespass law outdoor lighting neighbor complaint 311 floodlight` · WebSearch → WebFetch | https://www.brownstoner.com/brooklyn-life/in-the-city-of | Brownstoner, "In the City of Blinding Lights", Jan 9, 2007: reader says management of a four-storey building at 111 15th Street put up floodlights "ridiculously bright… aimed directly into my bedroom window"; "I can literally read by them, even with the blinds closed"; commenters: "Ask nicely"; "take photos and video, call 311". | §5 para 3; §9 cluster 2 H3 2; §10.5 H3 4; §Sources (street named, not the address number) |
| N2 | carried from dvr-upgrade.md N6 | https://www.brownstoner.com/forum/general-discussion/installing-security-cameras-lights-on-brownstone-exterior/ | Forum post: wants "a ring floodlight cam on the second floor of our brownstone" after "worrying security incidents"; asks "how difficult it is/how much it will cost to run a new wire"; 0 replies. (Direct WebFetch this run: permission not answered.) | §5 para 4; §Sources |
| N3 | `Brooklyn backyard break-in rear window burglary 2025 Patch` · WebSearch → WebFetch | https://brooklyneagle.com/articles/2018/06/25/cops-seek-crook-in-string-of-back-window-burglaries-in-bensonhurst-gravesend/ | June 25, 2018: suspect linked to at least 12 burglaries since Aug 2017, 61st/62nd precincts (Bensonhurst, Gravesend); "In all known incidents… forcing open a window in the rear of the house." | §5 para 2; §Sources |
| N4 | same · WebFetch | https://www.cbsnews.com/newyork/news/bushwick-burglary-victim-in-backyard | Oct 1, 2019 (published Oct 5): two people burglarized a Bushwick home near Central Avenue and George Street while the resident was in the backyard; "caught on surveillance footage". | §5 para 2; §Sources |
| N5 | `reddit r/Brooklyn neighbor floodlight shining into window backyard` · WebSearch → WebFetch | https://ny1.com/nyc/all-boroughs/ny1-for-you/2017/02/21/ny1-for-you--a-light-nuisance-solved-in-brooklyn-with-help-from-ny1 | Feb 21, 2017: Nostrand Avenue tenants vs a deli's bright flashing sign; DOB found no sign permit and an illuminated sign in a C1 overlay on a residential area → violations; owner turned lights down. | §5 para 3; §Sources |
| N6 | `Brooklyn Paper package theft stoop 2025 porch pirates Brooklyn` · WebSearch → WebFetch | https://www.brooklynpaper.com/package-thieves-running-rampant-in-sheepshead-bay-locals-claim | Sheepshead Bay (61st Pct) package thefts from porches/stoops incl. Bedford Ave; Aug 13 community meeting (year not stated). | Background only (year missing → not cited on page) |
| N7 | carried from dvr-upgrade.md N1 | https://brooklyn.news12.com/2025/12/03/porch-pirates-are-snatching-holiday-packages-heres-how-to-protect-yours/3vxg19mAstZxQsrDNpiWwR | Dec 3, 2025: ~90,000 packages stolen per day in NYC (DOT). | §5.5 bullet 6; §Sources |
| N8 | see L4 | News 12 Dyker Heights | — | §9 cluster 5 H3 3 |

### Corridors / commercial (C)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C1 | carried from dvr-upgrade.md C2 | https://www.bayridgebid.com/ | Bay Ridge 5th Avenue BID: 5th Ave 65th–85th Streets. | §8 card; §Sources |
| C2 | carried from dvr-upgrade.md C3 | https://en.wikipedia.org/wiki/Fulton_Street_(Brooklyn) | Fulton Mall on Fulton St between Flatbush Ave and Adams St. | §8 card; §Sources |
| C3 | `East Williamsburg Industrial Park Brooklyn warehouses Red Hook warehouses cargo theft` · WebSearch → WebFetch | https://www.brooklynpaper.com/warehouse-burglary-heightens-concern | Undated (likely Feb 2010): four burglary reports at 35 Meadow Street, a converted three-storey former factory of small units, East Williamsburg (90th Pct); no forced entry; Dep. Insp. Michael Kemper: security "very weak"; building had no security system. | §8 card; §Sources (no date given on page) |
| C4 | Red Hook / Gowanus warehouse facts | — | No specific sourced fact gathered → page describes them only generically (warehouses, workshops, studios, roll-up doors). FLAG: descriptive, unsourced. | §8 card; §9 cluster 6 |
| C5 | Sunset Park side-street description | — | "smaller warehouses, food producers and wholesalers… side streets that empty at night" — descriptive, unsourced. FLAG. | §8 card |

### Yelp (Y)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Y1 | `yelp Brooklyn electrician floodlight camera install review` · Firecrawl search | https://www.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Bay+Ridge%2C+Brooklyn%2C+NY+11209 (and Brooklyn electrician / low-voltage search lists) | Search-list excerpts only; no 1–3★ review text. → EMPTY (not accessible in build env). | Not used |

### Licensing / permits (Brooklyn)
- NYS low-voltage licence #12000287431 (AESS, protected content) — page says it covers the camera/network/recorder side, **not** new 120 V wiring.
- NYC DOB: any electrical installation/modification → permit + Licensed Master Electrician; fixture replacement in existing outlets = "minor electrical work" (still LME + permit; no DOB inspection). G1/G2.
- LPC: G3. Civil Rights Law §52-a: G6. Int. 753-2024 (proposal): G4.

### House practices stated on the page without an external source (FLAG for Anwar)
- **Line-voltage work done by a licensed master electrician; AESS does camera/network/app.** The page states this as how the job is split ("filed and connected by a licensed master electrician"). Confirm who supplies/pays the electrician and whether the $300–$575 swap price includes the electrician's permit — the page avoids saying so ("our written quote spells out which parts… and who does them").
- Old Brooklyn page said "we run a new circuit through brick" — not carried, because AESS's licence is low-voltage.
- Three power routes (existing box / PoE spotlight / plug-in GFCI / new box) and "we price all of them".
- Aiming practice: lamp heads down, brightness reduced in app, motion-only with short timer, motion zones to fence, privacy masks, after-dark check from the far fence; warm colour temperature preference.
- Switch-guard / permanent-live box advice; "some floodlight cameras let a quick off-and-on of the wall switch force the light on" (generic product behaviour, hedged "we check whether your model supports that").
- Commercial: commercial LED flood + separate wired camera, mounted high, recorder locked inside; schedule + motion after hours.
- Two-hour arrival windows, seven days a week to 8 PM; "lighting and recording again within one to two hours of arrival" (copied from live silo convention / blueprint §5 element 36).
- Field Notes = installer-voice description of standard practice (walk to the back fence first, find the network, check from the neighbour's line of sight) — no specific job story.
- FAQ practice answers: booking lead time "usually within a few days"; old fixture left with owner; app sharing for two-family tenants; painting housings not recommended; alarm integration "sometimes"; outage behaviour + UPS on PoE switch.

### Images (11) — Drive: no Floodlight Camera Installation folder; CompanyCam not connected
- **Step A (Drive):** folder `AESS Website Photos` (1hAcALEIANNRWVFVsbt4qqVder5_E4Bac) contains only Soundbar Installation, Cat6 Repair, Sonos Installation, Smart Lock Installation, Fiber Optic Installation subfolders (checked 2026-10-18 ~05:27Z); Drive-wide title search "Floodlight" → no results.
- **Step B (CompanyCam via Composio):** toolkit `companycam` has no active connection → not available in an unattended run.
- **Step C:** 4 real AESS job photos from other jobs (images/manhattan-deli-*.jpeg, images/nassau-window-depot-monitor.jpeg, images/rockland-toyota-wall-camera.jpeg; cropped to remove signs, text, people, house numbers, timestamp) + 7 manufacturer floodlight product shots from images/floodlight-*.png. All looked at with the Read tool. Filenames of the source PNGs do not always match the product shown (e.g. floodlight-aosu.png shows a Swann-badged unit, floodlight-ring-cam-pro.png an aosu-badged one, floodlight-alarmcom-adc-v729ac.png the same image as floodlight-reolink.png) — so captions name a brand only where it is legible in the frame (Lorex, Wyze). Avoided images/buzzer-repair/ and images/commercial-security/ (AI-looking risk).

| Output (images/floodlight-camera-installation/) | Source | Crop / note | Placement |
|---|---|---|---|
| floodlight-camera-installation-brooklyn-black-pan-tilt-camera-under-three-led-panels-with-wire-leads-product-photo.webp (900×765) | images/floodlight-olafus-2k.png | product shot; no legible brand used | Hero (eager) |
| …-camera-on-long-wall-arm-on-stone-facade.webp (228×372) | images/manhattan-deli-exterior.jpeg | crop (0,0,228,372): facade + arm; signs, address numbers, people, subway sign excluded | §5 |
| …-white-twin-panel-floodlight-camera-product-photo.webp (900×600) | images/floodlight-lorex.png | product shot; LOREX legible | §6 |
| …-white-round-lamp-floodlight-camera-product-photo.webp (900×495) | images/floodlight-google-nest.png | product shot; brand not named | §7 |
| …-dome-camera-under-fascia-beside-led-strip-lights.webp (917×647) | images/manhattan-deli-exterior-camera.jpeg | crop (330,288,1247,935): below sign text | §8 |
| …-recorder-tile-of-brick-wall-and-paved-lot.webp (460×295) | images/nassau-window-depot-monitor.jpeg | crop (700,145,1160,440): one tile; timestamp, house-number tile, people excluded | §9 |
| …-black-three-panel-floodlight-camera-product-photo.webp (900×966) | images/floodlight-wyze-pro.png | product shot; WYZE legible | §10 |
| …-small-black-camera-high-on-bare-wall-with-shadow.webp (800×570) | images/rockland-toyota-wall-camera.jpeg | crop (300,250,1100,820) | §12 |
| …-white-twin-lamp-floodlight-over-box-camera-product-photo.webp (900×900) | images/floodlight-blink-wired.png | product shot; brand not named | §14 |
| …-white-floodlight-with-dual-lens-pan-tilt-camera-product-photo.webp (900×900) | images/floodlight-eufy-e340.png | product shot; brand not named | §15 |
| …-white-floodlight-camera-with-glowing-colour-ring-product-photo.webp (500×500) | images/floodlight-alarmcom-color-led.png | product shot; brand not named | Field Notes |
All WebP q80, ≤1600 px. Alt/title unique, each contains "Brooklyn"; captions describe only what is visible and say "not an installed unit" / "not a Brooklyn property".

### Build notes
- Rendered words 13,302 (check_page.py). Title 55 chars, meta 159. 6 JSON-LD blocks; FAQ 10 = schema 10; HowTo 7 = process cards 7.
- Masked paragraph similarity (SequenceMatcher on ≥12-word paragraphs/li/td/h3/figcaption, geo masked) max **0.559** (vs nassau-county / hudson-valley — short question headings); typical max 0.521 (shared SMS-consent label).
- check_page.py: everything passes except the wiring items reserved for the main run (15 siblings + NYC hub don't link to /floodlight-camera-installation-brooklyn). Simulated with back-links added in a scratch hard-link copy → PASS (`--no-registration`). Registration (sitemap/_redirects) untouched by this run.
- Closest intents to the register (judged distinct): "A neighbor has complained about our existing floodlight…" (remediation) vs "Will the floodlight light up my neighbor's house on a tight lot?" (queens/nyc etc., prevention); "What does the DOB's minor electrical work category mean…" vs "Do I need a licensed contractor…?"; "Where should the floodlight sit on a Marine Park house whose driveway runs back to a rear garage?" vs "Do I need more than one floodlight for a long driveway?"; "Our rowhouse has no outdoor fixture… options besides a new 120-volt circuit" vs "Do you run new wiring if there's no power…?". Rewritten during build to avoid overlap: brightness/colour (was "how to light our yard without lighting their bedroom"), landmarked door-light count (was "can a floodlight replace the light beside our front door"), one-unit-vs-two-devices (was "why do faces come out white" — overlapped Manhattan's washed-out stoop question), network-cable-vs-Wi-Fi (was "will Wi-Fi reach the back" — overlapped "keeps dropping offline"), alarm integration FAQ (was spiders/moths false triggers — overlapped the deer/cars trigger questions).

---

## Staten Island

Page: `floodlight-camera-installation-staten-island` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Up-link `/floodlight-camera-installation-nyc`. GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`). Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359. Nothing from the old Staten Island template text reused.

**Thesis:** on Staten Island a floodlight camera lights a whole free-standing house, not a rear yard behind a row — driveway with cars, side door, built-in garage, back steps — and the island-specific problems are (1) houses raised or rebuilt after Sandy, where the door moved up a storey, the space below is flood-rule parking, and the switch/recorder must stay above the design flood elevation; (2) vinyl-sided frame walls that need a mounting block; (3) cars and back doors in the small hours (South Shore crowbar break-ins 2026, driveway car theft) and footage the precinct can use; (4) blocks where the streetlight has been dark for weeks (SI Advance Oct 2026); (5) Greenbelt/hillside lots and North Shore Victorian porches; (6) commercial lots that back onto houses; and (7) the state Dark Skies bill and the Council's 3,000-lumen bill, which both reward motion-only, aimed-down, dimmed lights.

Tools: WebSearch, WebFetch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (`mcp__Firecrawl__firecrawl_scrape` / `mcp__Fire_Crawl__firecrawl_scrape`, summary and directQuote modes). Shell curl blocked. Rows marked "carried from <file>" were fetched earlier on 2026-10-17/18 by other SI builds and re-used, not re-fetched.

### Sources status (§3) for this geo
| # | Source | Result |
|---|---|---|
| 1 | Reddit r/StatenIsland | `site:reddit.com r/StatenIsland security camera flood light backyard` · Firecrawl search → no r/StatenIsland floodlight thread (results: r/StatenIslandPulse red-light-camera repost, r/AskNYC stadium-lights thread, r/Ring raccoons, generic). → **EMPTY** (no matching thread; scrape of reddit refused per silo note). Not used. |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | **EMPTY (not accessible in build env)**. §10.5 says so on the page and tests seven published claims (A1, A2, P1–P4 + G1/G4/SI-B1). |
| 6–7 | Landmarks / building stock | rows SI-H, SI-L below |
| 8 | Bing / DDG | **EMPTY (not accessible in build env)** |
| 9–10 | Local news / hyperlocal | SI Advance (silive), Hoodline, ABC7, CBS New York — rows SI-N |
| 11 | Yelp 1–3★ | not re-searched; silo + apartment-building SI attempt returned listing pages only → **EMPTY (not accessible in build env)** |
| — | Census ACS (Richmond County) | `api.census.gov/data/2023/acs/acs5?...for=county:085&in=state:36` · WebFetch → permission not answered; Firecrawl scrape → "Missing Key" (API key now required) → **EMPTY (not accessible in build env)**. CHPC 83% figure used instead. |

### Building stock (SI-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-H1 | carried from cat6-repair.md (SI) — `Staten Island one- and two-family homes share of housing units NYC Planning Furman Center borough profile` · Firecrawl search (excerpt) | https://chpcny.org/visualization/housing-stock-visualization/ | "in Staten Island, 83 percent of units are in one- or two-family homes" (CHPC Taking Stock, Oct 2024) | §5 para 1; §5.5 bullet 1; Sources |
| SI-H2 | carried from apartment-building…md (SI) — Prodigy RE blog | https://prodigyre.com/blog/the-two-family-wealth-engine-how-staten-islands-most-common-home-type-built-middle-class-wealth | Great Kills up-and-down high-ranches; New Dorp/Dongan Hills side-by-side semi-attached; Charleston/Rossville newer semi-attached; North Shore older detached and converted Victorians | §7 cards (descriptive, no figures) |
| SI-H3 | carried from apartment-building…md — Nacmias Law | https://nacmiaslaw.com/practice-areas/closings/building-types/townhouse-condo-declaration/staten-island | low-rise condo townhouse communities (Annadale, Huguenot, Eltingville); one declaration per community; association often owns roads, parking, grounds | §7 card; §8 paragraph on associations/landlords |
| SI-H4 | `Build It Back elevated homes Staten Island raised houses Sandy number of homes elevated` · WebSearch → WebFetch | https://www.nyc.gov/site/housingrecovery/disaster-recovery/build-it-back.page | Staten Island 1,982 homeowners served; citywide 838 homes repaired and elevated above base flood elevation; 492 rebuilt incl. 103 modular; no borough split for elevations | §5 para 4; §5.5 bullet 3; Sources |
| SI-H5 | same search · WebFetch | https://www.cbsnews.com/newyork/news/staten-island-superstorm-sandy-anniversary | Oct 28 2015: 331 SI homes repaired or raised (then); New Dorp Beach home elevated; Midland Beach, Ocean Breeze, Oakwood named | §5 para 4 context; Sources (figure 331 not used — dated) |
| SI-H6 | carried from apartment-building…md — NYC SIRR | https://www.nyc.gov/site/sirr/rebuilding/east-and-south-shore-staten-island.page | 23 storm-related deaths on SI, all but one on East/South Shores; 11,700+ buildings in inundated area; 1–2 family = 90% of buildings | §5.5 bullet 2; Sources |
| SI-H7 | carried from cat6-repair.md — DVIDS (10.10.2024) | https://www.dvidshub.net/news/482917/seawall-will-raise-quality-life-shore-communities-staten-island-new-york | ~5-mile seawall, elev. 21 ft, Fort Wadsworth (just south of the Verrazzano) to Oakwood Beach | §13 card |
| SI-H8 | `Hurricane Sandy Staten Island Midland Beach Oakwood Beach homes flooded buyout` · WebSearch → WebFetch | https://cbsnews.com/newyork/news/oakwood-beach-homeowners-flooded-out-by-sandy-looking-forward-to-state-buyouts | Oct 24 2013: Oakwood Beach under up to 16 ft of water (per article); buyouts; quotes (Correa, Fradella) | Background only (not on page) |
| SI-H9 | carried from apartment-building…md — Wikipedia | https://en.wikipedia.org/wiki/Staten_Island | Hylan Blvd longest street in NYC; North Shore most urban (St. George, Tompkinsville, Stapleton); South Shore developed rapidly 1960s–70s | §8 Hylan card; §7.5 shore-by-shore; Sources |

### Rules (SI-R)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-R1 | carried from cat6-repair.md — UpCodes NYC BC 2022 App. G (directQuote) | https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction | utilities/equipment at or above design flood elevation or built to keep water out; only flood-damage-resistant materials below DFE; coastal high-hazard: space below limited to parking, building access, storage, crawl space | §8.5 bullet 2; §9 raised-house H3s 2–3; §10.5 H3 4, 6; Sources |
| SI-R2 | `silive.com Staten Island neighbor lights shining bright outdoor light complaint` · Firecrawl search (excerpt) | https://portal.311.nyc.gov/article/?kanumber=KA-02259 | "You can report light from a parking lot shining into a neighboring apartment or building to the Department of Buildings (DOB)" | §8.5 bullet 3; §9 Hylan lot H3; FAQ 5; Sources |
| SI-R3 | same search → Firecrawl scrape (summary + directQuote) | https://www.silive.com/news/2026/03/could-a-new-ny-law-shut-off-your-porch-light-overnight.html | Mar 17 2026 (Jillian Delaney): Dark Skies Protection Act (S5007), Sen. Brad Hoylman-Sigal; outdoor lighting off 11 p.m.–5 a.m.; exemptions listed incl. worker safety, emergency, certain streetlights, "Incandescent fixtures of one hundred fifty watts or less and other sources of less than seventy watts"; sitting in Senate Environmental Conservation Committee | §9 H3 Dark Skies; §10.5 H3 7; Sources |
| SI-R4 | silo G1 (DOB electrical), G4 (Int 753), G6 (52-a), G8 (tax credit), G3 (LPC) | see Part 1 | — | §8.5; §9 lumen-bill H3; §10.5 H3 2, 7 |
| SI-R5 | `St. George Historic District Staten Island designated Landmarks Preservation Commission year Stapleton Heights` · Firecrawl search (excerpts) | https://hdc.org/preservation-resources/expanding-historic-district-boundaries/expanding-historic-district-boundaries/ ; https://preserve.org/stgeorge/stgeorgedistrict.htm ; https://prodigyre.com/blog/staten-island-north-shore-victorian-belt | St. George/New Brighton HD designated 1994 (HDC); designation-report date given as June 19, 1994 (preserve.org) vs July 19, 1994 (Prodigy) — conflict → page says "1994" only | §9 porch H3; §13 card; Sources |

### News / hyperlocal (SI-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-N1 | `Staten Island burglary backyard caught on camera 2025 silive` · WebSearch → WebFetch | https://hoodline.com/2026/02/nypd-hunts-for-trio-suspected-in-staten-island-burglary-spree/ | Feb 8 2026 (incident early Feb 1): New Dorp, Dongan Hills, Todt Hill; ~2:36 a.m. crowbar on window frame near Benedict Rd & Circle Rd; key fob + ~$60 taken near East Entry Rd; ~3:25 a.m. back door approached with crowbar near Cromwell Circle & Farview Pl | §5 para 2; Sources |
| SI-N2 | same · WebFetch | https://www.cbsnews.com/amp/newyork/news/caught-on-video-man-wanted-in-nearly-2-dozen-burglaries-on-staten-island-police-say | Mar 29 2023: West Brighton, suspect in 23 business burglaries since Sept; latest Castleton Ave near Pelton Ave, through a shop's glass door | Background only (not on page) |
| SI-N3 | `Staten Island car thefts from driveways overnight 2025 key fob silive` · Firecrawl search → scrape (summary) | https://abc7ny.com/post/exclusive-video-car-theft-staten-island-key-fob/13546726/ | Jul 27 2023: thief steals unlocked car from SI driveway in under 15 s; Capt. Glorisel Lee: 90% of stolen vehicles had doors unlocked | §5 para 2; Sources |
| SI-N4 | same search (excerpts) | https://www.facebook.com/MikeReillyAssembly/… ; https://www.silive.com/crime-safety/2022/10/… | "Car thefts on Staten Island are up 22%" (2026, via FB repost of silive); 7 vehicles in 24 h (2022) | Not used (excerpt/FB only) |
| SI-N5 | same search as SI-R2 → Firecrawl scrape (summary + directQuote) | https://www.silive.com/news/2026/10/its-about-the-feeling-of-safety-staten-islanders-say-streetlight-outages-persist-despite-repeated-requests-for-repairs.html | Oct 15 2026 (Ravaioli, Bulik): outages > a month despite five 311 calls; 210 streetlight complaints in a recent 7-day period (189 "Street Light Out", 15 multiple); BP office blames delayed DOT contractor agreements; DOT: "Every reported outage is assessed within 10 days"; average close-out this year 15 days; Sunnyside resident, Cheshire Pl & Melrose Ave, months; photo caption Fairfield St, Great Kills | §5 para 3; §5.5 bullet 5; §9 streetlight H3s; Sources |
| SI-N6 | carried from apartment-building…md — CBS NY | https://www.cbsnews.com/newyork/news/staten-island-catalytic-converter-theft-prevention | Jul 15 2022 Graniteville etching event; >250 catalytic converter thefts on SI that year to date | §9 work-van H3; Sources |
| SI-N7 | `Staten Island deer population count 2024 vasectomy program white-tailed deer` · WebSearch → WebFetch | https://wildlife.org/in-nyc-officials-wrestle-with-controlling-deer-populations/ | Mar 2020: city credits sterilization with 15% reduction; no counts | Background |
| SI-N8 | `NYC Parks Staten Island deer aerial survey population estimate 2,053 decline` · Firecrawl search → scrape (directQuote) | https://www.nycgovparks.org/news/press-releases?id=21871 | Jul 7 2021: ~2,053 deer (Jan 2017) → ~1,616 (Jan 2021), ~21% reduction; 44% decrease in reported deer-vehicle collisions | §5.5 bullet 4; Sources (deer kept to body text — "triggers on deer" intent is registered) |

### Landmarks / corridors (SI-L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-L1 | `Staten Island Greenbelt acres NYC Parks Todt Hill Emerson Hill wooded homes` · Firecrawl search (excerpts) | https://www.nycgovparks.org/park-features/hiking/greenbelt ; https://www.homes.com/local-guide/staten-island-ny/todt-hill-neighborhood/ ; https://cityneighborhoods.nyc/emerson-hill | Greenbelt "2,800-acre park system"; runs along Todt Hill's western edge; Emerson Hill borders Reeds Basket Willow Swamp Park and the Greenbelt | §9 Greenbelt H3; §13 card; §6 card; Sources |
| SI-L2 | carried from cat6-repair.md — Freshkills | https://freshkillspark.org/the-park/faqs ; https://freshkillspark.org/ | 2,200 acres; restoring 360 acres of wetlands | §13 card |
| SI-L3 | carried from cat6-repair.md — SI Mall | https://www.silive.com/news/erry-2018/03/05c8690920/10_things_to_know_about_the_st.html | opened Aug 9 1973, Richmond Ave at Richmond Hill Rd | §8 card; §13 card |
| SI-L4 | carried from cat6-repair.md — Empire Outlets (Wikipedia excerpt) | https://en.wikipedia.org/wiki/Empire_Outlets | 350,000 sq ft, St. George | §8 card |
| SI-L5 | carried from apartment-building…md — City Limits | https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ | Bay Street rezoning approved June 26 2019 | §8 card |
| SI-L6 | carried from cat6-repair.md — Matrix (excerpts) | https://www.margulieshoelzli.com/projects/matrix-global-logistics-park/ ; https://www.dnainfo.com/new-york/20170619/bloomfield/matrix-global-logistics-park-gulf-avenue-amazon | 200-acre park on former oil-tank site; Building 1 975,000 sq ft | §8 card; §13 card |
| SI-L7 | carried from cat6-repair.md — SIUH | https://siuh.northwell.edu/ | 475 Seaview Avenue | §8 card |
| SI-L8 | Forest Avenue / Victory Blvd card | — | descriptive only (delis, pizzerias, auto shops, contractors) — **no source; FLAG** | §8 card |

### Licensing / permits (SI)
- NYS low-voltage license #12000287431 (protected) — camera/network/recorder side; line-voltage boxes/circuits/fixture swaps by a licensed master electrician under DOB permit (silo G1).
- NYC BC Appendix G for anything below the design flood elevation on raised houses (SI-R1).
- LPC for St. George/New Brighton and other designated districts (SI-R5, silo G3).

### Pricing — §9 multiplier applied, FLAG
- Brooklyn base (silo §1.7): $300–$575 / $575–$1,500 / $1,300–$3,800. × 1.10, round half-up: **$330–$633 / $633–$1,650 / $1,430–$4,180** (575×1.1 = 632.5 → 633; 1,300×1.1 = 1,430; 3,800×1.1 = 4,180). Service rate $195/hr, 3-hr min ($585) — protected, not multiplied.
- **FLAG:** the old Staten Island page published $330–$630 / $630–$1,650 / $1,450–$4,200, which is not Brooklyn × 1.10 (and the silo's NYC hub sits below the Brooklyn base). The rebuild follows the rule; Anwar to confirm.
- "No separate toll line or travel charge" on the invoice: carried from network-cable-repair-staten-island.html ("no separate travel charge"), via research/cat6-repair.md prices note.

### House practices stated without an external source (FLAG for Anwar)
- Mounting blocks on vinyl/aluminum siding; drip loops; framing fixings; switch/recorder/UPS kept on the living floor of raised houses.
- Two-light pattern on raised houses (landing + lower corner), side-of-garage placement on high-ranches, open-side placement on semi-attached houses, lower gate light on hillside lots.
- Temporary light during renovation/elevation; siding-job detach/reinstall; previous-owner unit removal; insurance answer hedged to "ask your insurer"; footage hand-over practice (export, keep originals) is general practice, not a NYPD source.
- Field Notes = installer-voice description of standard practice (curb first, stair, inside questions, across-the-street check) — no specific job story.
- Two-hour arrival windows, 8 AM–8 PM seven days, "one to two hours of arrival" — silo/live convention (blueprint §5 element 36).

### Images (11) — Drive: no Floodlight folder (per main run); CompanyCam not connected
Real AESS job photos first (5, from other jobs, re-cropped to exclude signs, logos, text, people), then 6 manufacturer floodlight product shots under the permanent image rule; none used on the Brooklyn page (Brooklyn used manhattan-deli-exterior*, nassau-window-depot-monitor, rockland-toyota-wall-camera and floodlight-olafus/lorex/google-nest/wyze/blink/eufy/alarmcom-color-led). All looked at with the Read tool before and after cropping. Known filename mismatches: `floodlight-aosu.png` shows a **Swann** unit; `floodlight-ring-cam-pro.png` shows an **aosu** unit; `floodlight-swann-4k.png` shows an Alarm.com-logo unit (not used). Captions name a brand only where legible (Swann, Ring, aosu, Tapo).

| Output (images/floodlight-camera-installation/) | Source | Crop | Placement |
|---|---|---|---|
| floodlight-camera-installation-staten-island-white-swann-floodlight-camera-with-twin-round-lamps-product-photo.webp (646×496) | images/floodlight-aosu.png | (0,150,646,646) — removes "4K ULTRA HD" badge | Hero (eager) |
| …-white-turret-camera-in-corner-under-water-stained-ceiling-tiles.webp (605×480) | images/nassau-window-depot-storage-camera.jpeg (real AESS job) | (330,280,935,760) — box labels excluded | §5 |
| …-white-ring-floodlight-camera-with-plug-in-power-cord-product-photo.webp (900×900) | images/floodlight-ring-cam-plus.png | none | §6 |
| …-white-floodlight-camera-with-square-lamp-and-hooded-lamp-product-photo.webp (900×900) | images/floodlight-night-owl-fwip3.png | none; brand not named | §7 |
| …-black-ball-camera-at-ceiling-edge-beside-light-panel.webp (535×400) | images/rockland-toyota-dome-camera.jpeg (real AESS job) | (400,0,935,400) — dealer logo/TV excluded | §8 |
| …-small-black-camera-on-ceiling-grid-between-recessed-lights.webp (555×170) | images/rockland-toyota-active-deterrent.jpeg (real AESS job) | (380,330,935,500) — exit sign, wall mural, banner excluded | §9 raised-house cluster |
| …-white-aosu-pan-tilt-floodlight-camera-with-twin-antennas-product-photo.webp (800×780) | images/floodlight-ring-cam-pro.png | (60,180,860,960) | §9 cars cluster |
| …-black-camera-high-on-white-wall-casting-two-shadows.webp (620×420) | images/rockland-toyota-bullet-camera.jpeg (real AESS job) | (185,380,805,800) — dealer sign and banner excluded | §10 |
| …-white-floodlight-with-wide-dual-lens-camera-product-photo.webp (400×300) | images/floodlight-reolink.png | none; brand not legible | §12 |
| …-bundled-blue-and-white-network-cables-along-ceiling-pipe.webp (700×210) | images/rockland-toyota-nvr-monitor.jpeg (real AESS job) | (120,0,820,210) — monitor/timestamp excluded | §14 |
| …-white-tapo-floodlight-camera-with-oval-lamps-product-photo.webp (447×447) | images/floodlight-tapo-c720.png | none | §15 |
All WebP q80, ≤1600 px. Alt/title unique, each contains "Staten Island"; captions describe only what is visible and say "not an installed unit" / "not a Staten Island property". DAILY-LOG note suggestion: `images: 5 real AESS job-photo crops from other jobs + 6 manufacturer floodlight product shots (no real floodlight photos yet)`.

### Build notes
- check_page.py: all page checks pass; remaining FAILs are wiring reserved for the main run (14 floodlight siblings + NYC hub do not yet link to /floodlight-camera-installation-staten-island). Simulated with back-links in a scratch hard-link copy → **PASS**. sitemap.xml (1 loc) and _redirects (2 rules) already present for this slug.
- Masked-geo block similarity (difflib SequenceMatcher, p/li/td/h2/h3/figcaption ≥12 words, geo masked via check_page.mask): max vs Brooklyn ≈0.61 on content blocks after a rewrite pass; ≥0.65 only on excluded constants (NAP line 0.67, the mandated warranty sentence block 0.88). Max vs every other silo page ≤0.43 (hudson-valley/orange/putnam measured against their pre-rebuild files on disk at 2026-10-18 ~07:30Z — re-run after the concurrent rebuild lands).
- File size 186 KB vs Brooklyn 183 KB (margin ~3.1 KB > 2 KB); re-check after the concurrent HV/Orange/Putnam rebuilds.
- Closest intents to the register (judged distinct): streetlight-out all-night Q vs Brooklyn "LED streetlight already lights the sidewalk"; FAQ "neighbor's floodlight shines into our bedroom" (recourse as the affected neighbor) vs Brooklyn "a neighbor has complained about our floodlight" (remediation as owner) and Rockland "light up my neighbor's house"; semi-attached side choice vs Brooklyn Marine Park driveway placement (different house type and decision: which wall vs which point along a driveway); raised-house Qs vs old SI "survive a South Shore flood zone" (placement and indoor-gear location, not device durability); Greenbelt reach vs "triggers all night on deer" (deer kept out of every question). Avoided: cost, DIY, brands, no-fee, mounting height, color at night, deter intruder, extra charge for SI, two lights for long driveway, wiring to detached garage, HOA rules, salt air.


## Hudson Valley hub

Page: `floodlight-camera-installation-hudson-valley` (REBUILD in place, 2026-10-18; was crawled-not-indexed as a near-duplicate template). Regional hub: phone (800) 486-0943 only, GBP Bronx (460 E Fordham Rd, `#bronx`), up-link Home (/), down-links to all six HV county pages, cross-links to NYC hub + 5 boroughs and LI hub + Nassau/Suffolk. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from Brooklyn = rowhouse rear yards; Orange sibling = farms/warehouses/long drives; Putnam sibling = lake houses/wooded lots/dark-sky/second homes):** a six-county overview of how the same floodlight job changes south to north — tight suburban lots with neighbour-sensitive aim and county-licensed electricians (Westchester, Rockland) → distance-to-power, outbuildings, network reach, solar/battery, wildlife triggers and utility outages (Orange, Putnam, Dutchess, Ulster); plus the county/town licensing map (Westchester trade licence, Rockland Ch. 250, Orange L.L. 8-2007/L.L. 1-2024 (+ Middletown board), Putnam electrical board + Ch. 145, Ulster Ch. 185, none found in Dutchess, third-party inspection, Newburgh owner-occupant permit), village/town lighting codes (New Paltz, Cold Spring, Chester, Irvington; Town of Ulster's withdrawn law) and the pending state Dark Skies bill, the four utilities (Con Ed, O&R, Central Hudson, NYSEG), and a county price table on §9 multipliers. County detail kept at overview level; each county card links down.

Format: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell curl blocked. "carried" = fact gathered and sourced by an earlier run in another research file (file + row named).

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/hudsonvalley via Firecrawl search, excerpts only (scrape of reddit.com refused in earlier runs): RD1–RD3. No r/hudsonvalley thread about residential floodlights / neighbour light found → background only. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and tests published cost-guide/manufacturer claims (silo rows A1, A2, P1–P4). |
| 6 | Landmarks | LM1–LM6 |
| 7 | Use cases / property types | descriptive overview (FLAG: property-type descriptions per county are general, not statistics) |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Lohud (D2), Hudson Valley One (D6), Daily Voice (U4), Times Union (U5), Central Hudson news (U6) |
| 10 | Hyperlocal | Hudson Valley One (D6); Teatown (W2) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not searched again; silo row Y1 already EMPTY |

### Licensing / permits (K)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| K1 | `Westchester County electrician license Department of Consumer Protection master electrician licensing board` · Firecrawl search → scrape | https://consumer.westchestercountyny.gov/trade-licenses | "Plumbers and Electricians must obtain a trade license from Westchester County in order to work in the county." Consumers should ask to see the county licence card; online licence search. (Search excerpt also: Electrical Licensing Board page, (914) 995-2657 — not used.) | §5 para 2; §5.5 bullet 1; Six Counties card + table; §8.5 bullet 1; Q&A "Westchester requires electricians…"; §10.5 H3 5; Sources |
| K2 | carried — research/apartment-building-security-camera-installation.md HV rows 6–7 | https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits ; https://ecode360.com/26997705 | Rockland Ch. 250 electrical contractor = wiring for light, heat, power or signaling on 50 V or more. | §5 para 2; Six Counties; §8.5 bullet 1; Q&A Rockland/Putnam/Ulster; §10.5 H3 5; Sources |
| K3 | carried — same file rows 3–4 | https://ecode360.com/6607815 ; https://www.putnamcountyny.gov/consumer-affairs | Putnam Ch. 145 low-voltage/limited-data communications technician: cabling incl. video surveillance, ≤90 V, from an outlet installed by a licensed electrician. | §5 para 2; Six Counties; §8.5 bullet 2; Q&A Rockland/Putnam/Ulster; §10.5 H3 5; Sources |
| K4 | carried — same file row 9 | https://ecode360.com/35131702 | Ulster Ch. 185 Electrical Licensing Law; electrical work includes signaling, communication, alarm or data transmission. | Six Counties; §8.5 bullet 1; Q&A; Sources |
| K5 | carried — research/apartment-building-security-camera-installation.md HV rows 10–11 (Dutchess only now) | Dutchess search (no official page) | No county contractor licence found in Dutchess → "none found". (Orange row 10 superseded by K5a.) | §5 para 2; Six Counties; Q&A; §10.5 H3 5 |
| K5a | CORRECTION 2026-10-18 from the Orange builder's research (coordinator message) | https://www.orangecountyny.gov/DocumentCenter/View/317/Electrician-Application-PDF ; https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF ; https://www.middletownny.gov/259/Electrical-Licensing-Board | "According to Local Law No. 8 of 2007, any person wishing to work as an electrician in Orange County must possess a county-issued license"; Local Law No. 1 of 2024 revised electrical licensing; City of Middletown has its own Electrical Licensing Board. Earlier "none found" for Orange was wrong and is removed from the page. | §5 para 2; Six Counties card + table; §8.5 bullet 1; Q&A "Five of the six counties…"; §10.5 H3 5; Sources |
| K6 | `New York town building department electrical inspection third-party agency homeowner install light fixture permit Dutchess OR Ulster OR Orange "electrical inspection"` · Firecrawl search → scrape (PDF) | http://www.fishkill-ny.gov/uploads/3/8/0/7/38072219/building_permit_package_2016_-_commerical___multi-family.pdf | Town of Fishkill: "All electrical work shall be inspected by an independent electrical inspection agency approved in accordance with the Code of the Town of Fishkill"; lists ~15 agencies; "Connection of electrical work without proper Inspection is a violation … subject to fines." (Package is labelled commercial/multi-family, 2016.) | §5 para 2; Six Counties (Dutchess); §8.5 bullet 3; Sources |
| K7 | same search → scrape (PDF) | https://www.cityofnewburgh-ny.gov/DocumentCenter/View/1254/Owner-Occupant-Electrical-Permit-Application-PDF | City of Newburgh owner-occupant electrical permit: owner-occupant of a single or two-family dwelling; work must comply with NEC and city code; inspection by an approved agency chosen before the permit; work must pass before permit closes. | §8.5 bullet 3; Q&A "Newburgh lets owner-occupants…"; §10.5 H3 5; Sources |
| K8 | same search (excerpts) | https://www.greenburghny.com/…NYEIS-PDF ; https://www.tarrytownny.gov/building-department/pages/third-party-electrical-inspection-applications ; https://www.portchesterny.gov/…Electrical-Systems-Packet-PDF ; https://allamericanelectricalservice.com/blog/electrical-permit-requirements-rockland-county-ny | Westchester/Rockland municipalities also use third-party inspection agencies (excerpts only). | Background for "many towns" wording |

### Lighting rules (D)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D1 | `"outdoor lighting" local law town New Paltz OR Woodstock OR Rhinebeck OR Philipstown OR Warwick shielded fixtures residential` · Firecrawl search → scrape (PDF, directQuote) | https://www.villageofnewpaltz.gov/wp-content/uploads/2014/10/Outdoor-Lighting-Standards.pdf | Village of New Paltz Outdoor Lighting Standards: all fixtures fully shielded (no light above horizontal plane through lowest part) except Table 1 lamps (incandescent ≤160 W; any source ≤50 W); "Floodlighting is discouraged and, if used, must be shielded" against glare and light trespass; unshielded wallpacks prohibited; light trespass ≤0.25 footcandle at property line; adjacent to residential no direct light source visible at the line; "Motion-sensor security lighting is recommended". | §5 para 3; §5.5 bullet 3; Six Counties (Ulster); Q&A "Our village asks for fully shielded…"; §10.5 H3 3; §13 card; Sources |
| D2 | same search → scrape Lohud (directQuote) | https://www.lohud.com/story/news/ny-news/2026/03/23/will-ny-dark-skies-bill-require-you-to-turn-off-lights-what-to-know/89194622007/ | Mar 23, 2026: Assemblymember Deborah Glick (Manhattan) proposed A4615 regulating outdoor lighting; would take effect in 2028 if passed. | §5 para 3; Q&A Dark Skies; Sources |
| D3 | same search → scrape LegiScan (directQuote) | https://legiscan.com/NY/text/A04615/id/3098558 | A4615 (2025–2026), text dated 2026-02-10, "reported referred to codes": §18-0201 all outdoor fixtures shielded after Jan 1, 2028 incl. residential; §18-0202 nonconforming allowed if extinguished 11 p.m.–sunrise or "motion-activated lights with a duration of less than fifteen minutes and equipped with an automatic shutoff device"; exemption incandescent ≤150 W and other sources <70 W; does not apply in a municipality with equal or stricter local law. Earlier versions: A5632A (2023, Fahy), A8644A (2021–22) per Assembly memo excerpt. | §5 para 3; §5.5 bullet 4; Q&A Dark Skies; FAQ 10; Sources |
| D4 | same search → scrape (directQuote) | https://ecode360.com/37299676 | Town of Chester (Orange) Ch. 69 Outdoor Lighting, L.L. 2-2021 adopted 2-24-2021: all lights shielded downward to prevent trespass; floodlighting must use full cut-off fixtures; ≤0.5 fc at residential property line; flood/spot >900 lm (any luminaire >1,800 lm) no direct light above horizontal and mounting height ≤ 3 + D/3 ft (D = distance to nearest property boundary), max 25 ft; ≤900 lm floods unrestricted except must be redirected if aimed at residential buildings or glaring at drivers on public ways; grandfathered fixtures must be aimed down/shielded within 60 days of notification; motion-sensor security lighting recommended. | §5 para 3; §5.5 bullet 3; Six Counties (Orange); §8.5 bullet 4; Q&A "Town of Chester ties floodlight height…" (worked examples 30 ft → 13 ft; 12 ft → 7 ft are arithmetic from the formula); Q&A road glare; §10.5 H3 3; Sources |
| D5 | `Dutchess County town code outdoor lighting residential floodlights shielded …` · Firecrawl search → scrape (PDF, stealth) | https://www.coldspringny.gov/DocumentCenter/View/1793/Ch-0081-Outdoor-Lighting-Standards-PDF | Village of Cold Spring Ch. 81: all permanent fixtures full cutoff incl. single-family and multifamily; security lighting aimed/shielded so direct illumination confined to the property; motion-sensing fixtures fully shielded and adjusted to turn off when motion ceases; fixtures on a structure below the eave or parapet; spotlights permitted for single-family if fully shielded and directed downward; single-family not subject to lumens-per-acre cap. | §5 para 3; §5.5 bullet 3; Six Counties (Putnam); Q&A fully shielded; §10.5 H3 3; §13 card; Sources |
| D6 | `Hudson Valley town outdoor lighting law light trespass dark sky ordinance residential floodlight` · Firecrawl search → scrape | https://hudsonvalleyone.com/2023/05/22/lights-out-on-proposed-lighting-law-in-the-town-of-ulster/ | May 22, 2023 (Crispin Kott): Town of Ulster proposed lighting law dropped; Supervisor James Quigley: "probably 50 percent of the town's population could file complaints against the other 50 percent"; proposal: lights shielded downward, floodlighting to use cut-off fixtures, fines $50–$1,000 individuals; arose from neighbour dispute incl. a motion-activated camera fixed on a backyard; residents cited Civil Rights Law 52-a; town attorney unsure cameras could be regulated (constitutional issues). | §5 para 3; §8.5 bullet 5; Sources |
| D7 | `Westchester town code outdoor lighting residential "light trespass" floodlight …` · Firecrawl search → scrape (PDF) | https://www.irvingtonny.gov/DocumentCenter/View/9785/2020-03---Lighting-Standards | Village of Irvington Local Law #3 of 2020 amends site plan Standards for Approval (§224-72.C): lighting dark-sky compliant, full cut off, ≤5 fc, ≤0.1 fc at a line abutting residential/ROW, ≤0.3 fc at non-residential; exceptions: low-voltage landscape lighting aimed away; lights on a vacancy sensor that turns off ≤15 min after vacated. Applies through site plan review (not every house). | Six Counties (Westchester) + table; §6 card; §8.5 bullet 4; Sources |
| D8 | `Rockland County town code outdoor lighting residential glare Clarkstown OR Ramapo OR Orangetown …` · Firecrawl search | (Orangetown Art. IV excerpt only, not lighting) | No Rockland municipal residential lighting rule found → EMPTY; table says "None found at county level". | Six Counties table |
| D9 | Dutchess town lighting rule | (search D5 returned Riverhead/out-of-area results) | EMPTY for Dutchess → table says "None used on this page". | Six Counties table |

### Utilities and outages (U)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| U1 | `Orange and Rockland Utilities service territory Rockland Orange Sullivan counties customers electric` · Firecrawl search (excerpt) | https://www.oru.com/en/about-us/media-center/corporate-facts | O&R and Rockland Electric serve ~300,000 electric customers in NY and northern NJ; serves Orange, Rockland and Sullivan counties in NY (+ Bergen, Passaic, Sussex NJ). | §5.5 bullet 2; Six Counties; Sources |
| U2 | `Central Hudson Gas & Electric service territory counties …` · Firecrawl search (excerpt) | https://www.cenhud.com/en/about-us/our-service-territory/ | ~315,000 electric and 90,000 gas customers; territory from northern suburbs of NYC to the Capital District. | §5.5 bullet 2; Sources |
| U3 | same → scrape (PDF) | https://www.cenhud.com/globalassets/pdf/serviceterritorymap.pdf | Villages in territory: Ulster (Saugerties, Ellenville, New Paltz); Orange (Montgomery, Maybrook, Cornwall, Highland Falls); Putnam (Cold Spring, Nelsonville); Dutchess (Fishkill, Wappingers Falls, Millbrook, Rhinebeck, Red Hook, Tivoli, Millerton); also Albany, Greene. | Six Counties cards + table; Sources |
| U4 | carried — research/dvr-upgrade.md Putnam N4 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 5, 2020 10:15 a.m.: NYSEG 34,150 of 38,693 Putnam customers out; Central Hudson 3,621 of 5,160 (Putnam). | §5.5 bullet 6; §10.5 H3 7; Sources |
| U5 | carried — research/cat6-repair.md (HV) | https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php | June 27, 2024: thunderstorm outages "affected a combined 60,000 Orange and Rockland and Central Hudson customers". | §5.5 bullet 6; Sources |
| U6 | carried — research/dvr-upgrade.md Ulster U5 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 26, 2026: crews restoring power to "more than 19,000 homes and businesses" after a slow-moving nor'easter. | §10.5 H3 7; Sources |
| U7 | carried — research/dvr-upgrade.md Westchester F-W4 (excerpt) | https://www.nyseg.com/documents/d/nyseg/psc120_section-1 | NYSEG tariff territory Westchester towns: Bedford, Lewisboro, North Salem, Poundridge, Somers. | §5.5 bullet 2; Six Counties; Q&A county line; Sources |
| U8 | Con Edison Westchester | (carried dvr-upgrade F-W2/F-W3 outage figures exist; not used) | Page says Con Edison serves "most of Westchester" / "much of" — no customer-count source used. FLAG (general knowledge, unsourced share). | §5.5 bullet 2; Six Counties |

### Wildlife (W)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| W1 | `NYS DEC black bear range Hudson Valley Catskills bears Orange Ulster Sullivan Putnam sightings increasing` · Firecrawl search → scrape (PDF, directQuote) | https://extapps.dec.ny.gov/docs/wildlife_pdf/bbnathis.pdf | DEC "Black Bear in New York": Southern Black Bear Range includes Catskills and extends "to southern Orange and Rockland Counties at the New Jersey border"; Taconic Highlands "from Washington County south into Putnam County"; forested parcels from NJ border along I-87 to the Hudson = "primary corridor for bear immigration from New Jersey"; populations increasing especially in southern NY; "bird seed/feeders is the most common attractant"; ECL 11-0903(8) bear feeding prohibited near buildings. | §5 para 4; §5.5 bullet 5; Six Counties (Rockland); Q&A bears/trash; §10.5 H3 6; Sources |
| W2 | same search → scrape Teatown (directQuote) | https://www.teatown.org/black-bears-are-back-in-westchester-what-you-need-to-know/ | Oct 8, 2025: Westchester reported bear sightings 2 (2019), 11 (2020), 16 (2021); securing garbage "the single most important step"; remove bird feeders April–November. | §5 para 4; Q&A bears; §10.5 H3 6; §13 card; Sources |
| W3 | same search (excerpts) | https://www.scenichudson.org/viewfinder/why-regional-black-bear-sightings-feel-like-theyre-on-the-rise/ ; https://hudsonvalleypost.com/record-bear-2026-hudson-valley/ | Excerpts only (bears expanding into historical range; Southern Zone harvest 1,202 record) | Not used |

### Reddit (RD)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| RD1 | `site:reddit.com/r/hudsonvalley security camera OR floodlight OR "motion light"` · Firecrawl search | https://www.reddit.com/r/hudsonvalley/comments/1wbto56/guy_put_flood_light_on_his_hood_blinding_drivers/ | Excerpt: "Guy put flood light on his hood. Blinding drivers. Wappengers Falls" — vehicle light, not a house. | Background only for the road-glare Q&A (not quoted) |
| RD2 | same | https://www.reddit.com/r/hudsonvalley/comments/1rp1a5r/flock_cameras_approved_in_secret_in_pine_plains/ ; …/1vr1b9l/flock_cameras_watching_plum_point_access_road/ ; …/1r6m5ne/flock_camera_spotted/ | Excerpts: residents uneasy about licence-plate (Flock) cameras in Pine Plains, Wappingers, Plum Point. | Background only (privacy sensitivity → aim at own ground) |
| RD3 | `site:reddit.com hudsonvalley neighbor floodlight motion light bears deer camera` and `reddit hudsonvalley neighbor's flood light shining into my house what can I do` · Firecrawl search | — | No r/hudsonvalley residential floodlight/neighbour-light thread returned (results out of area) → EMPTY. | — |

### Landmarks / places (LM)
| # | Source | Finding | Used |
|---|---|---|---|
| LM1 | carried — apartment-building research HV row 13 · https://www.newburghny.org/discover-newburghs-east-end-historic-district/ | "second largest designated historic site in New York State"; Italianate row houses; Washington's Headquarters. | §7.5 river-city; §13 card; Sources |
| LM2 | carried — same row 14 · https://kingston-ny.gov/hlpc | Five historic districts (Stockade 1974 local); exterior work visible from public ROW reviewed by HLPC before building permit. | §7.5; §13 card; Sources |
| LM3 | D1 (New Paltz) | — | §13 card |
| LM4 | D5 (Cold Spring) | — | §13 card |
| LM5 | W2 (Teatown) | — | §13 card |
| LM6 | carried — same row 15 · https://www.governor.ny.gov/news/governor-hochul-announces-development-partner-build-transit-oriented-housing-beacon-metro | 265 mixed-income units on the lot beside Beacon station. | §13 card; Sources |

Town list in §13 ("We also install … in …") is a list of real municipalities in each county (no facts attached).

### Silo facts reused (research/floodlight-camera-installation.md Part 1)
A1 (Inch Calculator $450 / $250–$800 / $150–$350), A2 (HomeCamCafe ~$650), P1 (Ring ~9 ft, black/white/ground), P2 (Arlo licensed electrician), P3 (Lorex 2×2,000 lm), P4 (Reolink 1,800 lm PoE), G6 (§52-a), G8 (Commercial Security Tax Credit). Ethernet 100 m (328 ft) channel limit = standard specification (no URL; FLAG as general technical fact).

### Pricing used (§9 — no invented prices)
Brooklyn base (silo §1.7): swap $300–$575; no power $575–$1,500; 2–4 cams $1,300–$3,800. × multipliers, round half-up:
- Westchester 1.25: $375–$719 / $719–$1,875 / $1,625–$4,750
- Rockland 1.30: $390–$748 / $748–$1,950 / $1,690–$4,940
- Orange 1.40: $420–$805 / $805–$2,100 / $1,820–$5,320
- Putnam 1.45: $435–$834 / $834–$2,175 / $1,885–$5,510
- Dutchess & Ulster 1.53: $459–$880 / $880–$2,295 / $1,989–$5,814
Packages show lowest county–highest county ranges ($375–$880; $719–$2,295; $1,625–$5,814). Service $195/hr, 3-hr min ($585), not multiplied. Solar/cellular, fibre/wireless links, full systems, commercial lots: "quoted after a walk-through" (no price).
**FLAG:** the old hub page's prices ($300–$600 swap; $650–$1,800 new wiring; $700–$1,600 off-grid solar + 4G) were not consistent with §9 and were NOT carried. The old child pages (not edited) still show prices that do not follow §9 (e.g. Orange/Putnam/Dutchess $340–$660, Ulster $345–$670, Westchester $330–$640).

### House practices stated without an external source (FLAG for Anwar)
- Line-voltage work by an electrician licensed for the county/town; AESS does low-voltage (camera, PoE, recorder, app) under NYS #12000287431; written quote names who does what.
- "Two devices" (full-cutoff fixture + separate camera) recommended in lighting-code villages; cut sheets brought for building department.
- Recovery test by switching the house off at the main breaker; retry settings; UPS on router/switch; generator circuit check.
- Light tied to person detection, camera records animals; zones drawn to people's paths; after-dark check from neighbour's line and road.
- Solar viability judged on winter sun/shade; PoE extender/fibre/point-to-point bridge beyond 328 ft; wireless bridge needs line of sight (leaf season).
- Lantern-post feed often on switch/photocell → needs permanent supply (electrical work).
- Seasonal re-zoning when trees leaf out; snow on fixtures; Starlink/cellular data-cap advice; rental-guest disclosure ("many rental platforms require exterior cameras to be disclosed" — general, unsourced); sunset-following schedules.
- County-line advice: county = tax-bill municipality; postal towns cross lines (general, unsourced).
- Two-hour arrival windows 7 days to 8 PM; "lighting and recording again within one to two hours of arrival" (silo convention).
- Field Notes = installer-voice standard practice (walk the visitor's route, pace distance, check from neighbour line) — no specific job story.

### Images (11) — Drive: no Floodlight folder; CompanyCam not connected
- **Step A (Drive):** folder `AESS Website Photos` (1hAcALEIANNRWVFVsbt4qqVder5_E4Bac) checked 2026-10-18 ~06:38Z: only Cat6 Repair, Sonos Installation, Soundbar Installation, Smart Lock Installation, Fiber Optic Installation subfolders (second page empty); Drive-wide title search "Floodlight" → no results.
- **Step B (CompanyCam via Composio):** toolkit `companycam` — "No Active connection" → not available unattended.
- **Step C:** 4 real AESS job photos from other jobs (cropped; no faces, signs, house numbers, plates or readable text) + 7 manufacturer floodlight product shots already in the repo; all looked at before naming. None of the 11 source files is one the Brooklyn page used except that both pages draw on the same product-shot folder (different files). Avoided images/buzzer-repair/ and images/commercial-security/.

| Output (images/floodlight-camera-installation/floodlight-camera-installation-hudson-valley-…webp) | Source | Crop / note | Placement |
|---|---|---|---|
| white-pan-tilt-floodlight-camera-with-two-antennas-product-photo (900×1125) | images/floodlight-ring-cam-pro.png (shows aosu-badged unit; brand not named) | none | Hero (eager), og:image |
| network-cable-bundles-above-equipment-rack (600×300) | images/rockland-toyota-nvr-monitor.jpeg | crop (0,0,600,300): cables + rack only; monitor tiles/timestamps excluded | §5 |
| white-round-lamp-floodlight-camera-with-motion-sensor-product-photo (646×486) | images/floodlight-aosu.png (Swann badge legible) | crop (0,160,646,646): "4K ULTRA HD" badge removed | §6 |
| white-twin-panel-floodlight-camera-with-black-camera-face-product-photo (447×447) | images/floodlight-tapo-c720.png | none; brand not named | Six Counties |
| white-twin-lamp-plug-in-floodlight-camera-with-power-cord-product-photo (900×900) | images/floodlight-ring-cam-plus.png (Ring legible) | none | §7 |
| black-bullet-camera-on-bracket-under-drop-ceiling (735×580) | images/rockland-toyota-ceiling-bullet.jpeg | crop (200,120,935,700): monitors below excluded | §8 |
| turret-camera-high-in-corner-of-storage-room (685×620) | images/nassau-window-depot-storage-camera.jpeg | crop (250,0,935,620): handwritten box labels excluded | §9 |
| white-box-camera-under-two-angled-light-panels-product-photo (900×900) | images/floodlight-night-owl-fwip3.png | none; brand not named | §10 |
| black-eyeball-camera-in-corner-below-ceiling-light (605×330) | images/rockland-toyota-dome-camera.jpeg | crop (330,60,935,390): dealership logo/sign and TV excluded | §12 |
| white-floodlight-with-two-square-panels-product-photo (900×900) | images/floodlight-swann-4k.png (shows alarm.com-style logo; not named) | none | §14 |
| white-wide-panel-floodlight-with-black-wide-lens-camera-product-photo (400×400) | images/wireless-camera-reolink-floodlight.webp | none; brand not named | §15 |
All WebP q80, ≤1600 px; captions say "Manufacturer product photo (not an installed unit)" or "Example photo from another AESS job (not a Hudson Valley property)". Alt/title unique, each contains "Hudson Valley".

### Question register additions

#### floodlight-camera-installation-hudson-valley — REBUILT 2026-10-18: 18 Q&A H3 + 1 repair H2 ending in '?' + 10 FAQ (old-template HV questions above are retired but stay in the register)
Q&A / headings (§9 unless noted):
- Floodlight Dark Since the Last Valley Storm? (repair H2)
- Our house sits right on the Westchester–Putnam line — which county's rules and price apply to the floodlight?
- Why does the same floodlight cost more to install in Kingston than in White Plains?
- We own a house in Rockland and a cabin in Ulster — can both floodlights live in one app and be installed by one crew?
- Is a solar floodlight camera bright enough to be worth it on a shaded Hudson Valley slope in December?
- How far from the house can a network-powered floodlight go before the cable stops working?
- Can the floodlight run off the lantern post at the end of our front walk?
- Our village asks for fully shielded fixtures — do any floodlight cameras actually qualify?
- If Albany passes the Dark Skies Protection Act, will the floodlight we install this year have to come down in 2028?
- The Town of Chester ties floodlight height to the property line — how does that work out on an ordinary lot?
- Our light sits on a rise above a curving road — what keeps it from glaring at drivers on the bend below?
- Bears have started visiting our trash in Westchester — will a floodlight help, or should the money go elsewhere first?
- Is it better to let the light come on for animals so the camera always gets a colour picture, or keep it dark and rely on infrared?
- After a long Central Hudson or NYSEG outage, why do some floodlight cameras come back on their own while others sit dark?
- Is a whole-house standby generator enough to keep the yard light and camera running through a storm?
- Westchester requires electricians to hold a county trade licence — does that cover the person who connects our floodlight?
- Five of the six counties license electricians themselves — which part of a floodlight job does that reach, and what is different in Putnam and Dutchess? (reworded 2026-10-18 after the Orange licensing correction; distinct from the Orange page's Middletown-licence question)
- Newburgh lets owner-occupants pull their own electrical permit — can we do the line-voltage part ourselves and have you do the rest?
- Will a wireless bridge between the house and the garage carry floodlight video reliably through the trees?
(Comparison heading "Ring, ADT and SimpliSafe Against a Local Installer" deliberately not a question.)
FAQ (§17, = FAQPage schema):
- Can one visit cover properties in two different Hudson Valley counties on the same day?
- Is a photo or video call enough for a first estimate on a property two hours north?
- What happens to the floodlight's motion settings when the trees leaf out in spring?
- Snow piles up on the light in a nor'easter — does that block the camera?
- Can the floodlight be tied to a driveway sensor down at the road?
- Will the floodlight camera work on a Starlink or cellular-router connection?
- Can you take down an old unshielded floodlight and leave the box ready for a compliant fixture?
- We rent the house out on weekends — what should guests be told about the floodlight camera?
- How long does a typical Hudson Valley floodlight installation take on site?
- Can the yard light follow sunset automatically as the days shorten?

#### Intents deliberately avoided (already in register)
Cost-how-much (old templates) → reframed as "why the county gap"; no-power-or-Wi-Fi / run wiring to barn (old HV, all old county pages) → split into solar-in-winter, PoE distance limit, lantern-post feed, wireless bridge; deer/animal false triggers (old HV, Dutchess, Orange, Putnam, Rockland, Ulster) → bear attractant priority + light-for-animals-vs-IR trade-off; surge/winterizing; long driveway "more than one floodlight"; historic district "can you install"; Con Edison outage (Brooklyn FAQ) → recovery-after-outage behaviour and generator coverage; neighbour complaint / brightness & colour (Brooklyn) → village shielding, Chester height formula, road glare; licensed contractor (old templates) → county-specific licence questions; weekend-home watching (old HV) → guest disclosure FAQ only; fence/post mounting, old fixture disposal, painting housing, sale of house (Brooklyn FAQ) not used.

### Build notes
- After Orange licensing correction: rendered words 13,968; file 189,595 bytes; check_page.py PASS (main run had wired back-links). Before correction: words 13,885; file 188,665 bytes (band 187,500–189,500; Brooklyn 182,974). Title 60 chars, meta 159. 6 JSON-LD blocks (compact, unindented); FAQ 10 = schema 10; HowTo 7 = process cards 7; 11 figures.
- Masked similarity (SequenceMatcher on ≥12-word p/li/td/h3/figcaption, geo masked, nav/scripts excluded; Jaccard ≥0.3 prefilter) vs all 15 silo pages incl. the in-progress Orange/Putnam rebuilds as they stood ~07:20Z: max **0.627** (Putnam, the "two-hour slots / licence" bullet); vs Brooklyn max 0.616. Rewritten during build to get under 0.65: Sources product list (was 1.000 vs Brooklyn), warranty paragraph (0.886 vs Putnam — contains the protected sentence), repair paragraph, closing CTA, NAP/licence lines, tax-credit and §52-a bullets, AI-check intro and H3 1/H3 3 openers, packages, BYOE, form intro/success text, pricing intro, landmarks intro, home-page link paragraph, real-photo caption prefixes, HowTo step 5.
- Removed for length: "Does a mesh Wi-Fi node in the garage do the same job as a cable…" Q&A and the "Farms, barns and second homes" §7.5 subsection.
- check_page.py: all page items pass; remaining FAILs = 8 back-link items (bronx, long-island, manhattan, nassau-county, nyc, queens, staten-island, suffolk-county do not link to /floodlight-camera-installation-hudson-valley) — wiring for the main run. Registration items (sitemap/_redirects) pass already.


## Orange

Page: `floodlight-camera-installation-orange-county` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Up-link `/floodlight-camera-installation-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (845) 640-3835 in body, CTAs, sticky bar, form JS and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from Brooklyn = rowhouse rear walls/LPC/DOB; HV hub = six-county overview; Putnam = lakes, wooded lots, second homes):** in Orange County the dark spot is rarely on the house wall — it is a driveway end, a barn on its own meter, an equipment yard, a trailer gate or a builder coach light on vinyl siding — and several towns literally measure the light at the property line (Chester L.L. 2-2021: 0.5 fc, floods >900 lm no up-light, height ≤ 3 + D/3 ft, max 25 ft; Goshen §97-50: 0.5 fc; Greenwood Lake Ch.119: 0.20 fc, floods discouraged, agricultural exemption). Power comes from three utilities (O&R, Central Hudson, NYSEG) with storm outages and brownouts; new 120 V work needs a county-licensed electrician (Local Law No. 8 of 2007; Middletown has its own board). Building stock: subdivisions (Chester/Monroe/KJ/Blooming Grove/Woodbury), older city/village houses (Newburgh East End, Middletown, Port Jervis), farms (Black Dirt, Warwick orchards), I-84/17K/Route 300 warehouses, Route 17M/211/94 retail.

Format: exact query · platform · URL · finding · page+section used. FC = mcp__Firecrawl__firecrawl_search / _scrape; GOV = mcp__Firecrawl__firecrawl_gov_search; WS/WF = WebSearch/WebFetch; RD = Composio Reddit (account "AESS Reddit", active).

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | RD searches run (rows R1–R6); one usable Orange thread (Washingtonville brownouts), one Newburgh news share (Flock). No local floodlight/light-trespass thread found. |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 states this on the page; H3s are published claims (rows A1–A7). |
| 6 | Landmarks | rows L1–L7 (mostly carried from earlier Orange research). |
| 7 | Building stock / use cases | rows H1–H4, C1–C5. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env). |
| 9–10 | Local news / hyperlocal | Mid Hudson News (N4), Times Herald-Record (H2, C2 carried), NYSP/New Windsor PD releases (N1–N3). Times Herald-Record / Mid-Hudson News floodlight or light-trespass items: EMPTY (none found). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env); FC search returned a Yelp Newburgh list page only (no review text). |

### Reddit (R)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `subreddit:hudsonvalley floodlight OR "flood light" OR "motion light"` · RD | (results) | Only hit on topic: Wappingers/Fishkill (Dutchess) driver with a flood light on his hood — not Orange, not used. | — |
| R2 | `subreddit:Newburgh camera OR theft OR lights` · RD | https://www.reddit.com/r/newburgh/comments/1wpw4yj/newburgh_to_terminate_contract_for_flock_license_plate_readers/ | r/newburgh share (Sept 2026) of Mid Hudson News Flock story; comments "Now let's do the town", "Rare Newburgh W". | Led to N4 (§9 cluster 7 Q2) |
| R3 | `subreddit:hudsonvalley "Orange County" neighbor light OR stolen OR cameras` · RD | https://www.reddit.com/r/hudsonvalley/comments/1x10qf8/fyi_orange_county_subreddit_is_back/ | r/OrangeCountyNY revived Oct 2026 (new mods). | Background only |
| R4 | `subreddit:hudsonvalley "Central Hudson" OR "Orange and Rockland" outage` · RD → REDDIT_RETRIEVE_POST_COMMENTS (1r76dw0) | https://www.reddit.com/r/hudsonvalley/comments/1r76dw0/why_are_there_power_outages_in_my_area_every/ | Feb 17 2026, Washingtonville resident: "since the second half of 2025, it feels like my house has a brown out every month"; replies: "frozen tree branches falling and knocking over lines, or a car hitting a pole"; "someone hitting a pole with a car". (OP also contains an offensive aside — not quoted.) | §9 power cluster Q2 (brownouts); §Sources |
| R5 | `subreddit:OrangeCountyNY camera OR theft OR stolen OR light OR package` · RD | (25 results) | No floodlight/theft/lighting threads (events, pets, local news shares). EMPTY for topic. | — |
| R6 | `subreddit:hudsonvalley package stolen OR "porch pirate"…` / `neighbor floodlight OR "bright light" OR "light pollution"` / `warehouse lights…` · RD | (results) | Nothing Orange-specific on topic. EMPTY. | — |

### Lighting law (G)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `"Town of Newburgh" OR "Town of Monroe" OR "Town of Chester" NY zoning code exterior lighting "shall be shielded" glare adjoining property` · FC search → FC scrape (directQuote) | https://ecode360.com/37299676 | Town of Chester Ch. 69 Outdoor Lighting, adopted 2-24-2021 by L.L. No. 2-2021. All lights shielded toward the ground, no trespass onto adjacent properties; floodlighting must use full cut-off fixtures; ≤0.5 fc at residential line, 1.0 fc at nonresidential; luminaires >1,800 lm and floods/spots >900 lm: no direct light above horizontal and height ≤ 3 + (D/3), max 25 ft; floods ≤900 lm exempt unless aimed at residential buildings or causing glare to drivers (then redirect); warmer colour, lowest intensity; applies to all public and private outdoor lighting; pre-existing fixtures grandfathered but must be aimed down/shielded within 60 days of notification; notice by hand or certified mail, 30 days to abate; civil penalty $50–$1,000 individual ($10,000 entity), each day after 30 days a separate offense. | §5 para 4; §5.5 bullet 3; §6 card; §8.5 bullet 2; §9 cluster 1 (all 3 Qs); §9 Q glare/farm; §10.5 H3 3, 4; Town-by-town; §Sources |
| G2 | `Orange County New York town code exterior lighting glare residential floodlight Warwick Wallkill Montgomery Monroe Woodbury Blooming Grove` · GOV | https://ecode360.com/9942622 | Town of Goshen §97-50 Environmental performance standards: no glare beyond boundaries >0.5 fc; "All exterior lighting, including security lighting… shall be directed away from adjoining streets and properties"; Planning Board may require limited hours, screening or shields. | §5 para 4; §8.5; §9 Q1, Q (after closing); §10.5 H3 4; Town-by-town; §Sources |
| G3 | same · GOV → FC scrape (directQuote) | https://ecode360.com/14876381 | Village of Greenwood Lake Ch. 119 Lighting, adopted 2-1-2010 by L.L. No. 1-2010: "Floodlighting is discouraged and, if used, must be shielded" (glare for drivers/pedestrians, trespass, light above 90°); trespass ≤0.20 fc at line; nonessential lighting (display, aesthetic, parking, sign) off after business hours, security lighting reduced to minimum; "Motion-sensor security lighting is recommended"; exemptions incl. "Lighting associated with agricultural pursuits, including harvest activities, unless such lighting is permanent and/or creates a safety hazard". | §5 para 4; §9 Q1, farm Q, after-closing Q; §10.5 H3 4; Town-by-town; §Sources |
| G4 | same (G1 search) · FC search excerpt | https://www.zoneomics.com/code/newburgh-NY/chapter_11 | Third-party reproduction of Newburgh City zoning: exterior fixtures shielded to prevent light shining onto neighboring properties. Excerpt only, third-party → NOT used. | — |
| G5 | same (G1 search) · FC search excerpt | https://chester-ny.gov/wp-content/uploads/2020/07/LL-6-of-2026-Zoning-Amendments-Local-Law-Final-FULL-As-Adopted-7-8-2026.pdf | Excerpt: "(12) All exterior lighting shall be shielded and/or directed away from residential…" — context unknown → removed from page draft, not used. | — |
| G6 | `Town of Warwick NY code outdoor lighting glare shielded fixtures residential` · FC search | (results: Shelter Island, Warwick Twp PA, etc.) | No Town of Warwick NY lighting chapter found → EMPTY. | — |
| G7 | carried (silo G6) | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a. | §8.5; §9 cluster 7 Q2; §Sources |
| G8 | carried (silo G8) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit (≤50 employees, ≤$3,000/location, Oct 31). | §8.5; §Sources |

### Licensing / contracts (K)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| K1 | carried from research/fiber-optic-installation.md + dahua-camera-installation.md (FC search excerpts) | https://www.orangecountyny.gov/DocumentCenter/View/317/Electrician-Application-PDF ; https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF ; https://www.middletownny.gov/259/Electrical-Licensing-Board | "According to Local Law No. 8 of 2007, any person wishing to work as an electrician in Orange County must possess a county-issued license"; LL 1 of 2024 electrical licensing exists; City of Middletown has its own Electrical Licensing Board. | §8.5 bullet 1; §9 cluster 5 Q1; §10.5 H3 7; Town-by-town; §Sources |
| K2 | `Orange County NY Department of Consumer Affairs home improvement contractor license required Local Law` · GOV | (results Nassau/Suffolk/NYC only) | No Orange County home-improvement licence found → EMPTY; page makes no licence claim. | — |
| K3 | carried from research/cat6-repair.md (FC scrape) | https://www.orangecountyny.gov/DocumentCenter/View/951/Consumer-Law-Help-Manual---Home-Improvements-PDF | Contracts >$500 written, plain English, signed; name/address/phone/licence no.; work + materials incl. makes/models; progress payments. | §8.5 bullet 3; §9 cluster 5 Q2; §Sources |
| K4 | carried from research/fiber-optic-installation.md (WebFetch) | https://www.cenhud.com/en/my-energy/safety/dig-safely | 811 / UDig NY; "at least two—but no more than 10—days before you dig"; free and required by NYS law; utilities and municipalities mark their lines. | §9 cluster 2 Q3 (trench) |

### Utilities / weather (U)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| U1 | `Orange and Rockland Utilities Central Hudson service territory Orange County NY towns which utility Newburgh Middletown` · FC search (excerpt) | https://dps.ny.gov/system/files/documents/2022/10/nys-electric-and-gas-utilities-by-county.pdf | Orange County electric utilities: NYSEG, Central Hudson, Orange and Rockland. | §5.5 bullet 2; §9 power cluster; §Sources |
| U2 | same · FC search (excerpt) | https://www.facebook.com/OrangeCountyEmergencyManagement/posts/power-outagesorange-county-continues-to-have-significant-power-outages-in-and-ar/1555743324473551/ | "Central Hudson: 1138 customers without power Primary areas impacted: T. Montgomery, T. Newburgh…" (undated excerpt). | Town-by-town (Newburgh); §Sources (excerpt) |
| U3 | same · FC scrape | https://www.cenhud.com/en/about-us/our-service-territory/ | ~315,000 electric customers, mid-Hudson Valley; no Orange town list in text. | Background |
| U4 | carried from research/dahua-camera-installation.md (FC scrape) | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k | July 6 2026: >47,000 customers affected since July 1 (heat, thunderstorms, heavy rain); Orange County outages incl. Warwick Town and Goshen Town. | Town-by-town (Warwick); §Sources. (A Q&A that used it was replaced in de-dup.) |
| U5 | carried from research/fiber-optic-installation.md (WebFetch) | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | 2020: Orange 275,059 pulses, #1 NY county. | §5.5 bullet 5; §9 barn-meter Q; §Sources |

### Building stock / population (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | (direct) · FC scrape (directQuote) | https://censusreporter.org/profiles/05000US36071-orange-county-ny/ | ACS 2024 1-yr: pop 411,767; 152,422 (housing units); occupied 93%; owner-occupied 66%; single unit 69%; $426,900 (median value, not used); travel 35.3 min. | §5 para 1; §5.5 bullet 1; §Sources |
| H2 | carried from research/cat6-repair.md (FC scrape) | https://www.recordonline.com/story/news/local/2021/08/13/census-kiryas-joel-grew-leads-orange-population/8115187002/ | KJ 32,954 (+63%), ~half county growth; families to Blooming Grove, Woodbury, Monroe. | §5 para 2; Town-by-town; §Sources |
| H3 | carried (fiber/cat6 research) | https://en.wikipedia.org/wiki/East_End_Historic_District_(Newburgh,_New_York) ; https://ecode360.com/30538879 | East End HD ~445 acres, >2,200 buildings, Italianate brick; Newburgh ARC certificate of appropriateness for exterior alterations in historic districts (excerpt). | §7 card/H3; Town-by-town; §Sources |
| H4 | carried (cat6 research, excerpt) | https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36071.pdf | 613 farms, 65,706 acres in farms (2022). | §5.5 bullet 4; §Sources |

### Commercial corridors (C)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| C1 | carried (fiber research, WebFetch) | https://hgar.com/two-of-the-largest-commercial-projects-in-orange-county-history-begin-construction | May 2020: Amazon 1,015,740 sq ft at Rte 17K/747; Medline 1.2M sq ft; Town of Montgomery. | §5 para 2; §8 card; Town-by-town; §Sources |
| C2 | carried (dahua research, FC scrape) | https://www.recordonline.com/story/news/2022/01/20/orange-county-warehouse-development-plans/9028976002/ | ~40 warehouse projects; Goshen village, Wawayanda, Montgomery, Wallkill; Matrix 927,041 + 215,200 sq ft on 90 acres at Rte 300 & I-84. | §5.5 bullet 6; §8 card; §Sources |
| C3 | carried (dahua research, FC scrape) | https://www.timeshudsonvalley.com/mid-hudson-times/mid-hudson-times/stories/warehouse-proposed-for-17k-corridor-near-airport,55587 | Dec 2022: Matrix I-84 DC across from Stewart, 116 loading docks. | §8 card; §Sources |
| C4 | carried (fiber research) | Woodbury Common / LEGOLAND / Port Jervis / Galleria at Crystal Run (Wikipedia) | 1985, ~220 stores; LEGOLAND Goshen 2021, 250-room hotel, Exit 125 rework; Tri-States Monument 1882; only NY county bordering NJ and PA. | §8, §13, Town-by-town |
| C5 | descriptive, unsourced | — | Route 17M/211/94/32 retail strips; "Hamptonburgh, Blooming Grove, Cornwall, Tuxedo and Greenville back roads" long drives; Montgomery/Crawford dairy & horse farms. FLAG: descriptive only. | §7 cards, §8 |

### News / police (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | carried (dahua research, FC scrape) | https://newwindsor-ny.gov/Police/Press-Releases/new-windsor-police-warn-residents-of-international-organized-theft-groups | Jan 20 2025: residential burglaries tied to international organized theft groups; advice "Consider installing surveillance cameras and/or an alarm system." | §5 para 3; §Sources |
| N2 | `"Town of Wallkill" OR "Town of Montgomery" OR "Town of Newburgh" police tractor-trailer theft warehouse lot Orange County NY` · WS → WF | https://troopers.ny.gov/news/poughkeepsie-man-arrested-town-wallkill-burglary-charges | Sept 7 2025: 2016 Ford dump truck stolen from a maintenance garage at Garnet Health Medical Center, East Main St, Town of Wallkill (recovered Town of Poughkeepsie). | §5 para 3 (hospital not named); §Sources |
| N3 | same · WS → WF | https://www.aol.com/news/windsor-man-steals-20k-lawn-181500624.html | Nov 2025: New Windsor man arrested; >$20,000 in outdoor power equipment and tools from Tractor Supply stores in New Windsor and Crawford. | §5 para 3 ("farm-supply stores", brand not named); §Sources |
| N4 | (from R2) · FC scrape (directQuote) (WebFetch: permission not answered) | https://midhudsonnews.com/2026/09/25/newburgh-to-terminate-contract-for-flock-license-plate-readers/ | Sept 25 2026: Newburgh City Council expected to end Flock LPR contract at year end; resolution: "no longer consistent with the city's policy priorities regarding privacy, civil liberties, public accountability and community trust". | §9 cluster 7 Q2; §Sources |
| N5 | `Orange County NY farm theft stolen equipment Warwick OR "Pine Island"…` · WS → WF | https://westchester.news12.com/beloved-goats-stolen-from-orange-county-farm-41074507 | Sept 2019: goats stolen from an Orange County farm (no town, no detail). Too thin/old → not used. | — |
| N6 | `Times Herald-Record Orange County package theft porch…` · FC search | https://www.facebook.com/urbanupdatez/posts/newburgh-ny-a-newburgh-resident-is-warning-the-community-after-surveillance-foot/1637608831713716/ | Excerpt: "Newburgh 'Porch Pirate' caught on Ring doorbell video in 3rd reported package theft in town this month - per police" (undated, aggregator) → not used. Other "Orange County" results were CA/FL. Orange County NY package-theft news: EMPTY. | — |
| N7 | `midhudsonnews.com Orange County stolen trailer OR tractor…` · FC search | (results CA/FL/Sullivan) | Orange County farm-equipment / trailer theft: EMPTY. | — |

### Landmarks (L) — carried, not re-fetched
L1 Washington's Headquarters SHS (parks.ny.gov; first publicly owned historic site, 1850) · L2 Storm King Art Center (stormking.org; 500 acres, 1960) · L3 Goshen Historic Track (goshenhistorictrack.com; 1838, NHL, half-mile) · L4 Woodbury Common (Wikipedia; 1985, ~220 stores) · L5 Black Dirt region (pineislandny.com; western Warwick, Pine Island, ditches and farm roads) · L6 Tri-States Monument, Port Jervis (Wikipedia; 1882, I-84 viaduct) → §13 cards; §Sources.

### Reality-check claims (A)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | silo A1 | https://inchcalculator.com/floodlight-cost-guide | install $150–$350/light; avg ~$450; electrician $50–$200/hr; permits $20–$100 "may or may not". | §10.5 H3 1, 7 |
| A2 | `floodlight camera installation Newburgh OR Middletown OR Monroe NY cost electrician` · FC search → FC scrape (directQuote) | https://www.thumbtack.com/ny/newburgh/security-camera-install | "anywhere from $100 for a single-camera line installation to $1,000-$2,200 for an entire system." | §10.5 H3 2 |
| A3 | same search (excerpts) | https://www.facebook.com/groups/492214672469283/posts/1110790187278392/ ; https://www.reddit.com/r/wyzecam/comments/1j9zye5/whats_the_average_cost_for_installation/ | "$350 and $400… outdoor outlet" (group location unclear, mentions Farmingdale); "$250 per camera"/"$275… over the garage" (location unknown) → not used. | — |
| A4 | silo P1 | https://ring.com/support/articles/b2io6/Installing-Your-Floodlight-Cam | ~9 ft; breaker off; junction box. | §10 comparison; §10.5 H3 3 |
| A5 | silo P3 | Lorex Fusion bundle | 2 × 2,000-lumen arrays. | §10.5 H3 4 |
| A6 | silo P2 | https://blog.arlo.com/home-security-tips/how-to-install-wired-floodlight-cameras/ | existing junction box, strong Wi-Fi, licensed electrician. | §10.5 H3 5 |
| A7 | silo A2 | https://www.homecamcafe.com/how-to-mount-a-floodlight-camera-without-a-junction-box/ | plug-in, GFCI, cord not armored. | §10.5 H3 6 |
| A8 | carried (fiber research) | https://fischsolutions.com/solutions/structured-wiring/ | New Windsor firm: "Low-voltage cabling under 50 volts typically does not require an electrical permit in Hudson Valley municipalities". Firm not named on page. | §10.5 H3 7 |
| A9 | Angi / HomeAdvisor / Fixr | — | EMPTY (none surfaced); page says so. | §10.5 intro |

### Pricing (§9 Orange 1.40× on the Brooklyn base in research Part 1.7)
$300–$575 → **$420–$805**; $575–$1,500 → **$805–$2,100**; $1,300–$3,800 → **$1,820–$5,320**; service $195/hr, 3-hr min ($585) unchanged (protected). Schema offers 420 / 805 / 1820 / 585.
**FLAG:** the old Orange page showed $340–$660 / $680–$2,200 / $1,650–$5,200 — not consistent with §9 (old base × ~1.13–1.47); not reused.

### House practices stated on the page without an external source (FLAG for Anwar)
- Line-voltage work by a county-licensed electrician, itemised on our quote or hired by the owner; AESS does camera/network/recorder/app.
- Light-meter reading at the property line on request, recorded in paperwork.
- Siding mounting blocks on vinyl/fiber-cement; switch guard or permanently-live box on coach-light circuits.
- Wireless bridges or fiber (not copper) between separately metered buildings; PoE + UPS where brownouts are common.
- Breaker off/on restart test at handover; after-dark check from the road/neighbor's line.
- Conduit depth/pull string for trench runs; private lines not marked by 811 (inference from "utilities and municipalities mark their lines").
- "Most Orange County floodlights are lighting and recording again within one to two hours of arrival" (silo/blueprint §5 element 36 convention).
- FAQ practice answers (home battery/backed-up circuits, card retention, fieldstone fixing, alert schedules, livestock aim, prep list, 50% deposit per terms sentence, bus-stop schedule).
- Field Notes = installer-voice standing routine, no specific job story.

### Images (11) — Drive: no Floodlight folder; CompanyCam not connected
- **Step A (Drive):** `AESS Website Photos` (1hAcALEIANNRWVFVsbt4qqVder5_E4Bac) children = Cat6 Repair, Sonos Installation, Soundbar Installation, Smart Lock Installation, Fiber Optic Installation (checked 2026-10-18 ~06:35Z); Drive title search "Floodlight" → no results.
- **Step B (CompanyCam via Composio):** toolkit `companycam` has no active connection → not available unattended.
- **Step C / permanent rule:** 6 real AESS job photos from other jobs (cropped) + 5 manufacturer floodlight product shots. Sources chosen to avoid the files used by the Brooklyn page and (as far as visible on disk at build time) the HV hub / Putnam drafts. All viewed before naming; WebP q80, ≤1600 px.

| Output (images/floodlight-camera-installation/floodlight-camera-installation-orange-county-…) | Source | Crop / note | Placement |
|---|---|---|---|
| …white-floodlight-with-two-angled-square-lamps-over-box-camera-product-photo.webp (900×900) | images/floodlight-night-owl-fwip3.png | product shot, brand not named | Hero (eager) |
| …small-camera-on-short-arm-high-on-plain-wall.webp (735×700) | images/rockland-toyota-bullet-camera.jpeg | crop (200,0,935,700): dealership sign and plant excluded | §5 |
| …white-two-oval-lamp-floodlight-over-round-black-faced-camera-product-photo.webp (447×447) | images/floodlight-tapo-c720.png | product shot, brand not named | §6 |
| …white-twin-panel-floodlight-with-small-camera-and-round-wall-plate-product-photo.webp (225×225) | images/cam-floodlight.jpeg | product shot (Dahua badge, not named) | §7 |
| …ceiling-camera-and-device-beside-red-lit-exit-sign.webp (845×620) | images/rockland-toyota-active-deterrent.jpeg | crop (90,0,935,620): mural/people excluded | §8 |
| …white-dome-camera-in-corner-on-black-bracket.webp (535×640) | images/nassau-window-depot-office-camera.jpeg | crop (400,0,935,640): signage and framed documents excluded | §9 |
| …white-wide-panel-floodlight-over-wide-lens-camera-product-photo.webp (400×400) | images/wireless-camera-reolink-floodlight.webp | product shot, brand not named | §10 |
| …black-dome-camera-at-ceiling-corner-beside-light-panel.webp (555×430) | images/rockland-toyota-dome-camera.jpeg | crop (380,0,935,430): dealership logo/sign excluded | §12 Process |
| …lorex-twin-panel-floodlight-with-black-camera-product-photo.webp (263×192) | images/lorex-dual-floodlight-camera-installation-orange-county.jpg | product shot, LOREX legible | §14 |
| …ceiling-grid-with-small-dome-cameras-and-light-panels.webp (1230×430) | images/manhattan-deli-interior-cameras.jpeg | crop (0,0,1230,430): people and product labels excluded | §15 |
| …white-dome-camera-on-ceiling-tile-near-light-panel.webp (935×560) | images/rockland-toyota-office-camera.jpeg | crop (0,0,935,560): banner text and people excluded | Field Notes |
Alt/title unique, each contains "Orange County"; captions describe only what is visible and say "not an installed unit" / "not an Orange County property". DAILY-LOG note: `images: 11 reused (6 real AESS job photos from other jobs, cropped; 5 manufacturer floodlight product shots) — no real floodlight photos yet`.

### Build notes
- check_page.py (repo): FAIL (12) — only "live sibling … doesn't link back to /floodlight-camera-installation-orange-county" for bronx, dutchess-county, long-island, manhattan, nassau-county, nyc, queens, rockland-county, staten-island, suffolk-county, ulster-county, westchester-county (main-run wiring). Simulated with back-links added in a scratch hard-link copy → PASS (full, incl. registration: sitemap/_redirects/hub link-down already present).
- 13,843 rendered words; title 55; meta 160; 6 JSON-LD blocks; FAQ 8 = FAQPage 8; HowTo 7 = process cards 7; 193,214 B (HV hub draft 188,713; Putnam draft 177,928; Brooklyn 182,974 at check time).
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥12 masked words, word SequenceMatcher) vs every floodlight-camera-installation-* page on disk: max **0.590** (vs Brooklyn: recorder service card; Ring nine-foot claim). Warranty paragraph rewritten around the fixed sentence (<0.58).
- De-dup vs concurrent HV hub / Putnam drafts (read 2026-10-18 ~07:20Z), replaced: Chester height-formula Q (HV owns "Chester ties height to the property line") → "Which towns put a number on outdoor light?"; road-glare Q (HV "rise above a curving road") → 811 trench Q; O&R restart Q (HV "after a long outage why do some come back") → shared-circuit/freezer Q; licence-check Q (Putnam "check… Putnam County license") → Middletown city-vs-county licence Q; FAQs removed: generator transfer switch (HV standby generator), driveway-entrance sensor (HV "driveway sensor at the road"), spring/fall checks (Putnam lens cleaning; HV leaf-out); repair H2 renamed (HV "Floodlight Dark Since the Last Valley Storm?").
- **FLAG (conflict with HV hub draft):** HV hub Q "Which parts of a floodlight job need a county licence in Rockland, Putnam or Ulster but not in Orange or Dutchess?" implies Orange has no county electrician licence; Orange's own application cites Local Law No. 8 of 2007 requiring a county-issued licence (K1). Coordinator should reconcile.

### Question register additions
### floodlight-camera-installation-orange-county — REBUILT 2026-10-18: 20 headings ending in '?' (19 Q&A H3 + repair H2) + 8 FAQ
Q&A / headings:
- Light Out at the Barn, the Gate or the Garage?
- Which Orange County towns and villages actually put a number on outdoor light?
- How do you prove a floodlight stays under half a footcandle at the neighbor's line?
- We got a notice from the town code enforcement officer about our floodlight — what is the deadline, and what will satisfy the inspector?
- Can a light on the house actually show a face at a gate or barn door 200 feet away?
- The barn has its own electric meter — can the floodlight camera out there still reach our house Wi-Fi and recorder?
- Before you trench a cable out to our gate post, who has to mark what is already buried?
- Does a working farm get any leeway under the local lighting rules?
- Our tractors and wagons sit outside overnight in an equipment yard — where does the light go so the camera sees a person, not glare off the machinery?
- Our only outdoor circuit also feeds the garage freezer and the door opener — is it a problem to add the floodlight to it?
- Our house sees short brownouts — can low voltage damage a floodlight camera or make it reboot all the time?
- Who do we call when the outdoor box itself has no power — the utility, an electrician or you?
- Does work inside the City of Middletown need a different electrician licence from the rest of Orange County?
- What should a written contract for floodlight work in Orange County include?
- Our trailer yard off Route 17K is already lit by tall pole lights — does a floodlight camera add anything?
- Does a brighter floodlight make it easier or harder to read a truck's number at the gate after dark?
- Can our town make us turn the parking-lot floodlights off after closing?
- Our builder used vinyl siding everywhere — how is a floodlight camera mounted without cracking it or letting water in?
- Newburgh is ending its city plate-reader contract — does that change what our own camera should record of the street?
- The outdoor box on our older house has no ground wire — can a floodlight camera still go there?
FAQ (§17, = FAQPage schema):
- Our house has solar panels and a home battery — will the floodlight keep working when the grid goes down?
- How long does footage stay on the camera's memory card before it records over itself?
- Can a floodlight camera go on the fieldstone or block wall of an old farmhouse or barn?
- Can we stop the floodlight sending alerts while the farm crew is working in the yard?
- Will a floodlight bother horses or livestock in the barn at night?
- What do we need to have ready before the installer arrives?
- What is due when we book, and when is the balance paid?
- Can a floodlight camera light the spot where our children wait for the school bus in the dark?
Old-template Orange questions (pre-rebuild) are already in the register and were all removed from the page.


## Putnam

Page: `floodlight-camera-installation-putnam-county` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Queue line: `REBUILD | floodlight-camera-installation-putnam-county | Floodlight Camera Installation | Putnam | up /floodlight-camera-installation-hudson-valley | (845) 640-3835 | GBP Bronx`. Up-link `/floodlight-camera-installation-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (845) 640-3835 in body, CTAs, sticky bar, form error text and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (+ footer text).

**Thesis (distinct from Brooklyn rear yards, the HV six-county hub and Orange farms/warehouses/I-84–Route 17):** in Putnam a floodlight camera has three rule books before it has a brand — (1) Putnam's own Electrical Licensing Law (Ch. 145: hardwired = Putnam-licensed master electrician; the low-voltage/limited-data technician's licence covers video surveillance cabling only from an outlet or connection a licensed electrician already installed; plug-in of ordinary devices with no splicing is outside the chapter; Kent issues no electrical permits; inspection agencies SWIS/NYEIS), (2) town lighting codes written to keep wooded hillsides and lakes dark (Patterson 0.2 fc at a residential property line and a motion-light exemption under four minutes; Philipstown 0.5 fc, floodlights shielded or baffled, >2,000 lumens full cutoff, PAR lamps and wall packs banned; Carmel 0.1 fc and "must not permit light trespass"), and (3) the dark itself — long wooded drives, lake-colony lots, watershed and preserve land, deer and bears, NYSEG/Central Hudson outages. The job is lighting the 30 feet that matter (door, parking spot, garage, path) with a light that switches on briefly, stays inside the lot, and survives the power coming back.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page + section used**. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`, directQuote/query mode, PDF parser). Shell curl blocked. "Excerpt" = search-result snippet only. Rows marked "carried" were fetched by earlier Putnam runs (research/dvr-upgrade.md Putnam section and the files it cites) and not re-fetched.

### Mandatory sources (§3) — Putnam status
| # | Source | Result |
|---|---|---|
| 1 | Reddit (r/hudsonvalley, Putnam) | `site:reddit.com hudsonvalley floodlight neighbor OR motion light deer bear camera Putnam` · Firecrawl search → no results. `reddit hudson valley motion floodlight deer triggering all night camera` → only generic, non-Putnam threads (r/homedefense, r/Ring bugs, r/ringdoorbell false motion) — background only. Putnam Reddit = EMPTY. |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and uses the silo's sourced published claims (A1, A2, P1–P4). |
| 6 | Landmarks | carried L1–L8 (dvr-upgrade.md Putnam) + Cold Spring dock (N3). |
| 7 | Use cases / building stock | carried H1–H5. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env). |
| 9 | Local news | Mahopac News (Halston), The Examiner, Highlands Current, PCNR (carried), Daily Voice (carried). |
| 10 | Hyperlocal | Highlands Current, Mahopac News, PCNR, Putnam Sheriff (carried). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). |

### New this run (Firecrawl, 2026-10-18)
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| E1 | `Putnam County Electrical Licensing Board master electrician license required Putnam County NY` · Firecrawl search → scrape (directQuote, 3 passes) | https://ecode360.com/6607815 | Ch. 145 "Putnam County Electrical Licensing Law" (L.L. 2-1992, amended in entirety 9-5-2017 by L.L. 9-2017). Low-voltage/limited-data communications technician = 8,000 hours' experience + exam; installs "cabling systems for computer networking, telecommunications, cable television, intercom, audio/video, fiber optics, video surveillance systems and any other system operating at 90 volts or less and a maximum of five amperes where such work commences at an outlet receptacle or connection previously installed by a person holding the proper electrical license." No person shall engage in the trade "within the County of Putnam unless duly licensed or registered". Exemption B: "The attachment or plug in of ordinary electrical appliances and devices to existing electrical circuits, provided that no joining and/or splicing of electrical conductors is required." Civil penalty up to $5,000 per violation; unlicensed master-electrician business = Class A misdemeanor (up to 1 year, fine up to $1,000). Licensees: $25,000 bond, workers' comp, GL $1M/$2M naming Putnam County. No homeowner exemption found in the text read. | §5 para 4; §5.5 bullet 3; §8.5 bullets 1–2; §9 cluster A (all three H3); §10.5 H3 5; §Sources |
| E2 | same search (excerpt) → scrape (directQuote) | https://www.putnamcountyny.gov/consumer-affairs | Electrical Board licenses Master, Special & Reciprocal Electricians, Limited Data Communication Technicians, Journeymen, Helpers; downloadable lists of licensed master electricians and licensed low-voltage technicians (as of August 11, 2026); Town of Patterson filing instructions name State Wide Inspection Services (SWIS, Fishkill) and New York Electrical Inspection Services (NYEIS, Tarrytown); Home Improvement Board: mandatory contractor registration (insured, bonded, workers' comp); "no new reciprocal licenses". | §8.5 bullet 2; §9 cluster A H3 1–2; §Sources |
| E3 | same search (excerpt) | https://www.putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/electrical/Master-Elec-Application-Step-One-Aug-2020.pdf | Excerpt: pass the test → Putnam County Licensed Master Electrician; "annual license fee of $500". | Not used (fee not needed) |
| E4 | same search (excerpt) | https://forums.mikeholt.com/threads/hi-licensing-nys.7699/ | Forum excerpt: "Putnam County does have a county wide licence. Just recently they abolished the homeowner being able to do their own electrical work." Undated forum post, unverified. | Not used as fact (FLAG: homeowner position unconfirmed — page avoids stating it) |
| E5 | `Town of Kent NY code exterior lighting OR Town of Putnam Valley code outdoor lighting glare neighboring property` · Firecrawl search (excerpts) | https://www.townofkentny.gov/faq | Excerpt: "The Town of Kent does not issue Electrical permit at this time. Please contact Putnam County Comsumer Affairs". | §9 cluster A H3 2; Town-by-town (Kent); §Sources |
| E6 | same (excerpt) | https://ecode360.com/9476508 | Putnam Valley Art. XV Property Maintenance excerpt: "Required exterior lighting shall be maintained in operating condition. No offensive glare from lighting shall be transmitted so as to endanger the public…" | Town-by-town (Putnam Valley); §Sources |
| E7 | same (excerpt) | https://www.townofkentny.gov/DocumentCenter/View/2271/Town-of-Kent-Code-Chapter-77 | Kent Ch. 77 excerpt: "Commercial District and IOC District lighting… Wall pack outdoor light fixtures oriented toward an adjacent residential property…" | Background (§8 note on commercial wall packs, general) |
| D1 | `Philipstown outdoor lighting zoning code dark sky shielded fixtures light trespass` → `Town of Philipstown zoning outdoor lighting "light trespass" OR "shielded" ecode360` · Firecrawl search → scrape (directQuote) | https://ecode360.com/6319176 | Philipstown Ch. 175 Art. VII: lighting "the minimum needed… for safety, convenience and security"; no glare beyond the property "in excess of 0.5 footcandle"; all exterior lighting "including security lighting" directed away from adjoining streets and properties; fixtures "shielded and directed downward…" not "upward into the night sky"; PAR lamps and wall packs prohibited; "Floodlights, when used, shall be shielded or baffled so that they illuminate only the object intended to be lighted"; "All lighting above 2,000 lumens shall be restricted to full cutoff luminaires"; trespass lighting prohibited. | §5 para 3; §5.5 bullet 4; §9 cluster B H3 3; §10.5 H3 4; Town-by-town (Philipstown); §Sources |
| D2 | `Town of Carmel OR Kent OR Southeast OR Patterson NY code outdoor lighting glare residential floodlight shielded` · Firecrawl search → scrape (directQuote) | https://ecode360.com/49400453 | Carmel Ch. 156 Art. VI "Outdoor lighting standards": purpose to minimize light pollution; lights "must not permit light trespass past the property line", must not emit above 90° horizontal; "Illumination from light fixtures shall not exceed 0.1 foot-candle at the property line"; Planning Board may limit hours / require timers "during site plan, special use permit, and subdivision plan review". Search excerpt: "Floodlighting is discouraged and, if used, must be: Shielded…". Applicability to a single existing house not confirmed → page hedges. | §5 para 3; §9 cluster B intro; §10.5 H3 4; Town-by-town (Carmel); §Sources |
| D3 | same search → scrape (PDF parser, directQuote; text partly garbled by PDF layout) | https://www.pattersonny.org/ZoningRegs/Chapter154ZoningAmended7-22-09.pdf | Patterson § 154-22.1 Lighting Standards (version amended 7-22-09 — may be superseded; FLAG): purpose incl. "prevent light trespass"; applies to new fixtures and replacements ("change of fixture type, or change to the mounting height or location"); luminaires on a single-family residence "shall comply with the standards… but shall not be subject to review by the Planning Board"; prohibited: spot or flood luminaires aimed toward residential buildings on adjacent land or skyward; exemption: "Motion detector security lights which are normally off, and which when activated upon motion being detected are on for less than four (4) minutes"; max 0.2 fc at the property line in residential zones (measured 30 in above ground), 0.5 fc nonresidential; "All exterior lighting shall have full shielding". | §5.5 bullet 4; §9 cluster B H3 1–2; §10.5 H3 4; Town-by-town (Patterson); §Sources |
| D4 | `Philipstown outdoor lighting…` · Firecrawl search (excerpt) → scrape (PDF, directQuote) | https://www.coldspringny.gov/DocumentCenter/View/2049/Current-Chapter-PDF | Cold Spring zoning: nonresidential lots within 25 ft of a residence district — "floodlighting shall be so arranged that there will be no glare of lights toward such district boundary"; search excerpt: lighting "be indirect, with all light sources shielded from the view of adjacent lots and streets" (context not confirmed). | Town-by-town (Philipstown/Cold Spring); §8.5 bullet 4 |
| N1 | `Putnam County NY package theft car break-ins sheriff warns residents lock cars Carmel Mahopac` · Firecrawl search → scrape (directQuote) | https://news.halstonmedia.com/mahopac-news/mahopac-news/stories/police-warn-mahopac-residents-after-string-ofcar-break-ins,91083 | Mahopac News, Aug 7, 2026: Carmel PD — seven unlocked vehicles on four streets entered ~3:37–5:05 a.m. Wed Aug 5 (Lake Casse, Lake Drive, Ridge Road neighborhoods of Mahopac); advice incl. "park in well-lit areas, close garage doors"; residents "with doorbell, driveway or dash cameras" asked to review overnight footage. | §5 para 2; §5.5 bullet 6; §9 cluster F (both H3); §Sources |
| N2 | same search → scrape (directQuote) | https://www.theexaminernews.com/police-warn-of-increased-vehicle-break-ins-in-putnam/ | The Examiner, Oct 9, 2020: State Police (Brewster barracks) — 10 vehicle break-ins and one stolen vehicle in Carmel, Patterson and Southeast over the Oct 3 weekend; lock vehicles "even in their driveways at home". | §5 para 2; §Sources |
| N3 | `Highlands Current dark sky light pollution Philipstown Cold Spring outdoor lighting` · Firecrawl search → scrape (directQuote) | https://highlandscurrent.org/2012/10/24/dark-skies-lighting-fence-dedicated-at-cold-spring-dock/ | Oct 2012: Cold Spring riverfront dock's 'dark skies' bollard lights dedicated after a ~five-year effort; lights "diminish light pollution and glare, making the stars, river, and Hudson Highlands hills visible after dark". | §5 para 3; §13 card; §Sources |
| N4 | same search (excerpt) | https://highlandscurrent.org/2010/07/23/effort-to-restore-historic-dark-skies-view-of-mountains-at-night-bogs-down-in-questions/ | 2010 excerpt on dark-skies streetlight effort "bogs down". | Background only |
| N5 | same search (excerpts) | https://putnamsheriff.com/ ; Sheriff/Carmel PD Facebook posts | Sheriff site "Highlights" (e.g. Southeast: money stolen from a vehicle); FB lock-your-car reminders (undated excerpts). | Not used (undated/social) |
| N6 | `NYSEG Putnam County outages 2025 OR 2026 storm customers without power Carmel Mahopac` · Firecrawl search (excerpts) | https://poweroutage.us/area/county/822 | Excerpt: "44,840 customers we track in the county" (live snapshot). | Not used (live/third-party); outage figures carried from H5/N4 rows below |
| W1 | `PCNR Putnam County package theft porch pirates OR deer population Putnam County OR bear sightings 2025` · Firecrawl search | (results were Putnam County, Indiana/Tennessee) | No Putnam NY package-theft item found → EMPTY. | — |
| W2 | `reddit hudson valley motion floodlight deer triggering all night camera` · Firecrawl search (excerpt) | https://www.homesandgardens.com/gardens/do-outdoor-security-lights-deter-animals | Excerpt: "Security lights keep humans at bay, but they won't work on raccoons, deer, or bears. According to a wildlife expert…" | §9 cluster C H3 (attributed as excerpt); §Sources |
| W3 | same (excerpt) | https://www.reddit.com/r/Ring/comments/o81zrf/how_can_i_make_my_floodlights_not_be_constantly/ | Excerpt: Ring path "Light Settings > Motion Zones for Lights" to cut bug triggers. Not Putnam. | Background (motion zones for lights) |

### Carried Putnam facts used (from research/dvr-upgrade.md "Putnam County", not re-fetched)
| # | Source | URL | Finding | Page + section used |
|---|---|---|---|---|
| H1 | county hazard-mitigation profile | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | >240 sq mi; 6 towns + 3 villages; ~3/4 in NYC watershed; forest 66.9% (2011); commercial along Routes 6, 9, 22, 52 and I-84 | §5 para 1; §5.5 bullets 1–2; §8 intro |
| H2 | Census QuickFacts | https://www.census.gov/quickfacts/putnamcountynewyork | 38,713 housing units; owner-occupied 83.8% | §5 para 1; §5.5 bullet 2 |
| H3 | ACS B25004 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36079 | 1,757 seasonal/recreational/occasional-use units | §5.5 bullet 2; §7 lake card |
| H4 | Historic Patterson | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Smadbeck lake colonies Lake Carmel, Lake Peekskill, Putnam Lake from 1928; 11,000 Putnam Lake lots mapped, 20'×100' for $50 | §7 lake-colony card + §7.5; §13 card |
| H5 | Daily Voice (Isaias) | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ ; https://dailyvoice.com/article/isaias-outage-update-these-putnam-county-towns-are-most-affected-five-days-after-storm/ | Aug 5, 2020: NYSEG 34,150 of 38,693 Putnam customers out; Central Hudson 3,621 of 5,160; Aug 9: 1,733 NYSEG still out | §5 para 4; §5.5 bullet 5; §9 cluster D; §10.5 H3 6 |
| P1 | Sheriff Dark House Check | https://putnamsheriff.com/dark-house-check/ | patrol check for residents away; "does not guarantee protection"; advises light timers | Field Notes; §17 FAQ (none) — §5 para 2 |
| P2 | Highlands Current | https://highlandscurrent.org/2024/09/10/police-investigating-philipstown-burglaries/ | Sept 2024 break-ins Old Albany Post Rd / Indian Brook Rd, Philipstown | Town-by-town (Philipstown) |
| B1 | PCNR bear alert | https://www.pcnr.com/articles/bear-alert/ | May 2024: large bear in a Carmel backyard < ½ mile from the historic courthouse; DEC: secure food sources | §9 cluster C; §Sources |
| R2 | Carmel / Kent wetlands | https://www.townofcarmelny.gov/DocumentCenter/View/456/Wetland-Permit-Application-PDF ; https://www.townofkentny.gov/286/Building-permit-requirements | Carmel regulates wetlands ≥1/8 acre + 100-ft buffer; Kent flags work within 100 ft of ponds/streams | §9 cluster G H3; §Sources |
| R4 | Cold Spring HDRB | https://www.coldspringny.gov/DocumentCenter/View/2074/Certificate-of-Appropriateness-PDF ; https://highlandscurrent.org/2025/08/08/the-history-patrol/ | since 1976 exterior changes in the historic district need HDRB approval; work not visible from the street not reviewed | §7 village card; Town-by-town; §8.5 bullet 4 |
| L1–L6 | Lake Mahopac (Wikipedia), Putnam County Courthouse (Wikipedia), West Branch Reservoir (NYC DEP), Cold Spring HD (Wikipedia), Tilly Foster Farm (county PDF excerpt), Fahnestock State Park (parks.ny.gov excerpt) | see dvr-upgrade.md L1–L6 | ~587-acre lake; courthouse 1814 on Gleneida Ave; West Branch in Kent & Carmel, 1895, two basins separated by Route 301; Cold Spring HD 691 acres, NRHP 1982; Tilly Foster ~199 acres, Southeast; Fahnestock 15,000 acres | §13 landmark cards |
| G6 | Civil Rights Law §52-a (silo G6) | https://www.nysenate.gov/legislation/laws/CVR/52-A | backyard recording without consent | §8.5 bullet 5; §9 cluster E H3 1 |

### Pricing (§9) — FLAG
Brooklyn base (silo §1.7): $300–$575 swap · $575–$1,500 new power · $1,300–$3,800 two-to-four. Putnam ×1.45, round half-up: **$435–$834 · $834–$2,175 · $1,885–$5,510**. Service rate $195/hr, 3-hr min ($585) (protected, not multiplied). **Old Putnam page published $340–$660 / $680–$2,200 / $1,650–$5,200 and a "$250 service call"** — not consistent with §9; NOT carried. Anwar to confirm the 1.45× figures.

### House practices stated without an external source (FLAG for Anwar)
- Line-voltage connections by a Putnam-licensed master electrician; AESS does camera/network/app/recorder. Page does NOT claim AESS holds a Putnam limited-data technician licence — it tells owners to check names (including ours) on the county list. **Anwar: confirm AESS's Putnam Ch. 145 status; if licensed, the page can say so.**
- Practices: motion-only with short timers (≤ ~1–3 min), lamp heads below horizontal, warm colour, dim-glow mode where model supports it; post rather than tree mounting; lamp heads not under snow-shed eaves; UPS on PoE switch/router/recorder; router auto-recovery advice; two-hour windows seven days to 8 PM; "lighting and recording again within one to two hours of arrival" (blueprint §5 el. 36).
- Field Notes = installer-voice standard practice (walk the drive at dusk, stand at the neighbour's/lake side), no specific job story.

### Images (11) — Drive: no Floodlight folder; CompanyCam not connected
- Step A: `AESS Website Photos` (1hAcALEIANNRWVFVsbt4qqVder5_E4Bac) lists only Cat6 Repair, Sonos Installation, Soundbar Installation, Smart Lock Installation, Fiber Optic Installation (checked 2026-10-18); Drive title search "Floodlight" → none.
- Step B: Composio `companycam` list → 0 accounts (connection only "initiated", not active).
- Step C / permanent rule: 4 real AESS job photos from other jobs (Rockland Toyota ×3, Nassau Window Depot storage) cropped to exclude signs, text, people, monitors; 7 manufacturer product shots not used on the Brooklyn page. All viewed before naming. Library `aess-*`/astoria photos avoided (flagged AI-looking by earlier runs); buzzer-repair/ and commercial-security/ avoided.

| Output (images/floodlight-camera-installation/) | Source | Crop / note | Placement |
|---|---|---|---|
| …putnam-county-white-twin-panel-floodlight-on-pan-tilt-camera-with-antennas-product-photo.webp (763×729) | floodlight-ring-cam-pro.png (shows aosu-badged unit) | trimmed | Hero (eager) |
| …-white-turret-camera-in-corner-under-water-stained-ceiling-tiles.webp (935×600) | nassau-window-depot-storage-camera.jpeg | crop (0,0,935,600): boxes/handwriting excluded | §5 |
| …-white-plug-in-floodlight-camera-with-power-cord-product-photo.webp (619×601) | floodlight-ring-cam-plus.png (Ring logo legible) | trimmed | §6 |
| …-round-twin-ring-floodlight-camera-with-motion-sensor-product-photo.webp (637×396) | floodlight-aosu.png (Swann-badged) | "4K ULTRA HD" badge painted out; trimmed | §7 |
| …-black-bullet-camera-on-ceiling-tile-mount.webp (835×700) | rockland-toyota-ceiling-bullet.jpeg | crop (100,0,935,700): monitors excluded | §8 |
| …-white-two-lobe-floodlight-camera-product-photo.webp (436×385) | floodlight-tapo-c720.png (tapo legible) | trimmed | §9 |
| …-white-floodlight-with-wide-dual-lens-camera-product-photo.webp (345×247) | floodlight-reolink.png | trimmed; brand not named | §10 |
| …-black-bullet-camera-high-above-grey-hallway-door.webp (615×1000) | rockland-toyota-hallway-camera.jpeg | crop (320,0,935,1000): cabinet sign excluded | §12 |
| …-white-square-panel-floodlight-with-box-camera-product-photo.webp (822×769) | floodlight-night-owl-fwip3.png | trimmed; brand not named | §14 |
| …-white-twin-panel-floodlight-over-black-front-camera-product-photo.webp (715×577) | floodlight-swann-4k.png (unit shows a house-shaped logo, no legible brand) | trimmed | §15 |
| …-small-camera-on-plain-grey-wall-casting-two-shadows.webp (685×500) | rockland-toyota-bullet-camera.jpeg | crop (250,200,935,700): banner + dealer sign excluded | Field Notes |

### Question register additions — floodlight-camera-installation-putnam-county (REBUILT 2026-10-18)

### Additional carried row used
| # | Source | URL | Finding | Page + section used |
|---|---|---|---|---|
| N13c | research/dvr-upgrade.md Putnam N13 (Swann support, excerpt) | https://support.swann.com/hc/en-us/articles/22392860080409-Preventing-Insects-from-Triggering-Your-Security-Cameras | "When insects fly close to the camera, they can trigger motion detection sensors, leading to false alerts and recordings." | §9 moths H3 (not listed in on-page Sources — FLAG: add if wanted) |
| L8b | Wikipedia Putnam County (re-scraped this run, query mode) | https://en.wikipedia.org/wiki/Putnam_County,_New_York | villages Brewster, Cold Spring, Nelsonville; CDPs incl. Carmel, Lake Carmel, Mahopac, Peach Lake, Putnam Lake; hamlets incl. Farmers Mills, Garrison, Lake Peekskill, Ludingtonville, Tompkins Corners; mentions Boyds Corner Reservoir, Mahopac Falls, Continental Village, NY Route 311 | §13 "we also install" line; Town-by-town (Kent, Patterson); Service areaServed |

### Question register additions — floodlight-camera-installation-putnam-county (REBUILT 2026-10-18): 19 headings ending in '?' (18 Q&A H3 + emergency H2) + 10 FAQ
Q&A / headings (section §9 unless noted):
- Floodlight Out After the Storm, or Lighting Up for Every Deer?
- Where can we check that the people wiring our floodlight hold a Putnam County license?
- Kent's building department says it issues no electrical permits — so who signs off a new outdoor box at our house?
- Is a plug-in floodlight on an existing outdoor outlet treated differently under Putnam's licensing law than a hardwired one?
- Patterson's zoning sets a light limit at the property line — does that apply to a floodlight on a single-family house?
- Our motion light in Patterson stays on for five minutes after it triggers — does the timer setting matter?
- Philipstown’s code bans PAR lamps and wall packs — what goes on the barn instead?
- Our land backs onto Fahnestock and we moved here for the stars — can a floodlight camera still do its job?
- A bear is on the deck and the floodlight just came on — how should we use the camera before anyone opens the door?
- Moths swarm the lamp heads on July nights — will they keep setting the floodlight off?
- Our detached garage gets power through a cable buried decades ago — can the garage floodlight run off it?
- Our well line and septic field run under the lawn we would have to cross — how is a cable route planned around them?
- The lake association owns the beach and dock next to our lot — can our floodlight camera look over it?
- We shut off the power at the panel when we close the lake cottage for winter — can a floodlight camera do anything while we're gone?
- After the Mahopac car break-ins, police asked for driveway camera footage — what makes a driveway clip actually useful to them?
- Where should the light go so a car parked in our driveway isn't just a silhouette on the footage?
- Snow slides off our metal roof right where the floodlight would go — where else can it mount?
- Can a floodlight camera be mounted on a tree instead of a post?
- Our driveway crosses a wetland buffer — does trenching a cable out to a light post need a town permit?
FAQ (§17, = FAQPage schema):
- Can the floodlight stay off when our own car comes up the drive at night?
- Our house sits on a slope and the best wall is two storeys up — do some jobs need a lift?
- Can the floodlight also light our house number sign so emergency crews find us?
- Can we switch the floodlight on from the app when we hear something outside?
- How do we keep the lens and lamp covers clean when spring pollen and road dust coat them?
- Can you give us the fixture details and settings in writing for our insurance company?
- We are re-siding the house next year — should the floodlight wait until then?
- Can the light stay at a soft glow all night and only go to full brightness when someone walks up?
- Can the floodlight's built-in siren be turned off so it never sounds by mistake?
- Can the steps down to our dock be lit without throwing light across the lake?

### Build notes
- check_page.py (`--no-registration`, real repo): only failures are 13 "live sibling … doesn't link back to /floodlight-camera-installation-putnam-county" (bronx, dutchess, long-island, manhattan, nassau, nyc, orange, queens, rockland, staten-island, suffolk, ulster, westchester) — main-run wiring. Simulated in a hard-linked scratch copy with those back-links added → **PASS** both with and without registration (sitemap entry and both _redirects rules already present; HV hub already links down).
- 12,760 rendered words; title 59; meta 160; 11 figures; 6 JSON-LD blocks (compact, no indent); FAQ 10 = FAQPage 10; HowTo 7 = process cards 7; 178,084 B (Brooklyn 182,974; HV 188,713; Orange rebuilt 195,651; others ≤157,679).
- Masked-geo similarity (word-level SequenceMatcher, p/li/h2/h3/td/figcaption ≥8 masked words) vs all 15 siblings incl. rebuilt Brooklyn and HV hub: ≥0.65 only on the blueprint-fixed H2 "What AI Gets Wrong About … in [Area]" and the protected warranty paragraph; highest other block 0.642 (image-caption opener "Example photo from another AESS job (not a … property)").
- Semantic de-dup vs register + rebuilt HV hub (read by hand): replaced my bear-deterrence Q (HV "will a floodlight help with bears"), outage/router-recovery Q (HV "why do some cameras come back"), generator Q (HV "is a standby generator enough"), Philipstown "which cameras qualify as full cutoff" (HV "do any floodlight cameras qualify as fully shielded"), visit-duration FAQ (HV "how long does installation take"), away-for-a-month FAQ (register "watch a weekend home"). Borderline, judged distinct, for coordinator: plug-in-vs-hardwired-under-county-law Q vs HV "Which parts of a floodlight job need a county licence in Rockland, Putnam or Ulster…" (mine = the plug-in exemption specifically); moths Q vs register deer-trigger Qs (different cause/fix); emergency H2 "…Lighting Up for Every Deer?" vs register deer-trigger Qs (repair-capture banner); snow-slide mount Q vs HV "Snow piles up on the light" (mine = mounting location under a shedding roof). Orange County was still the old template at final check — main run should re-check Orange's new questions against this list.
- Rebuilt Orange page checked at the end (195,651 B): per-sibling max masked similarity Putnam↔Orange 0.753 only on the protected warranty paragraph; all old-template siblings ≤0.385. Replaced my mailbox FAQ (overlapped Orange "deliveries left at the end of a long driveway") with the dock-steps FAQ. Borderline vs Orange, judged distinct: my "Where can we check that the people wiring our floodlight hold a Putnam County license?" vs Orange "Our electrician works in both Newburgh and Middletown — whose licence covers him in each, and how do we check it?" (both include "how to check a licence"); my lens-cleaning FAQ vs Orange "What should we check on the floodlight each spring and fall?".
- Process note: the scratchpad directory is shared with the concurrent Orange/HV builders; a sibling's build.py/sim.py overwrote mine mid-run (no effect on the Putnam page — verified by diff). Putnam sources now live in scratchpad/putnam/ (build_putnam.py, body1–4.html, faq.json).
