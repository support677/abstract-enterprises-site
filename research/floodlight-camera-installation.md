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
