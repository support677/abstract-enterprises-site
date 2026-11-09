# Residential Security Camera Installation — silo research

Created 2026-10-18 by the REBUILD run for `residential-security-camera-installation-nassau-county` (queue line: `REBUILD | residential-security-camera-installation-nassau-county | Residential Security Camera Installation | Nassau | up /residential-security-camera-installation-long-island | (516) 346-5778 | GBP Brooklyn`). First rebuild in this silo; the other 15 pages are still the pre-rebuild template.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: `mcp__Firecrawl__firecrawl_search` (web), `mcp__Firecrawl__firecrawl_scrape` (markdown / query mode). Shell curl blocked. Reddit and Yelp pages refuse scraping ("we do not support this site"), so Reddit rows are search-result excerpts only. "Excerpt" = read only as a search-result snippet. Rows marked "carried" were fetched earlier today by the DVR Upgrade run (research/dvr-upgrade.md) and are reused with their original URL.

Section labels (Nassau page): §Hero, §Quick, §5 Neighborhood (+5.5 facts), §Repair, §6 Services, §7 Architecture (+7.5), §8 Commercial (+8.5 rules), §9 Q&A (cluster/H3), §10 Equipment, §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks, §14 Pricing (+comparison), §15 Packages (+BYOE), §Field Notes, §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every residential camera page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (search snippets; reddit.com scrape refused). Rows R1–R5. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and quotes published cost guides / brand pages / forum posts instead (rows A1–A6). |
| 6 | Area landmarks | Nassau section rows L1–L6 |
| 7 | Area use cases / building stock | Nassau section rows H1–H5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl's search backend available |
| 9 | Local news | Nassau rows N1–N8 (CBS New York, ABC7 ×2, StateScoop, NY Senate, LIPA, county/NCPD bulletins) |
| 10 | Hyperlocal | Herald Community Newspapers (liherald.com) rows N9–N10; Patch/Newsday not opened (Newsday only as a Facebook excerpt, row N11) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — m.yelp.com search result returned only the listing headline ("TOP 10 BEST Security Camera Installation in Nassau County, NY"); scrape refused. |

### 1.2 Reddit (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit longisland home security cameras recommendations Nassau` · Firecrawl search | https://www.reddit.com/r/longisland/comments/1kc5ygw/home_security_cameras/ | Excerpt: "Simple Ring camera doorbell and Wyze cameras are as good as you can find. They are plug and play and not expensive." | Nassau §10.5 H3 2 (quoted); §Sources |
| R2 | same | https://www.reddit.com/r/longisland/comments/1h8ygon/what_cameraalarm_system_do_you_use_andor/ | Excerpt: "Eufy cameras, lots of options for indoor/outdoor surveillance. Easy to set up and use…" | Nassau §10.5 H3 2 (paraphrased); §Sources |
| R3 | same | https://www.reddit.com/r/longisland/comments/1wvcny4/house_security_systems/ | Excerpt: "Ubiquiti cameras. Top notch. No subscription. Great quality." (also names an Islip alarm company — not used) | Nassau §10.5 H3 2 (paraphrased "Ubiquiti for having no subscription") |
| R4 | same | https://www.reddit.com/r/homeowners/comments/1v72n8m/what_are_some_good_security_cameras/ | Excerpt: "PoE reolink have been fantastic for me. I had the same complaints with Wi-Fi 'detection' cameras. They'd alert me to nothing…" | Background for §10 "Why wired cameras do better" (not quoted) |
| R5 | same | https://www.reddit.com/r/longisland/comments/1pb2r5m/former_nyc_business_owner_louis_rossmann/ | Excerpt: thread criticising Nassau's Flock plate-reader cameras as "privacy invasive warrant-less mass surveillance" | Background only (not used; political) |

### 1.3 Published claims for the AI Reality Check (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `professional home security camera installation cost per camera 2025 Angi HomeAdvisor` · Firecrawl search | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | Excerpt: professional installation "$100 and $200 per camera on top of the camera's purchase price"; DIY saves "up to $150 per camera" | §10.5 H3 1; §Sources |
| A2 | same | https://www.homeadvisor.com/cost/safety-and-security/security-camera-installation-cost/ | Excerpt: "Professional security camera installation costs between $593 and $2,040 for your complete home setup project." | §10.5 H3 1; §Sources |
| A3 | `Ring Home subscription plan price per month 2026 Basic Standard Premium` · Firecrawl search | https://ring.com/plans ; https://ring.com/explore-ring-home | Excerpt: Ring Protect "$4.99/mo or $49.99/yr … for one device"; "Ring Home plans were renamed Ring Protect plans in 2026" | §10.5 H3 3; §14 comparison; §Sources |
| A4 | `SimpliSafe monitoring plan price per month 2026` · Firecrawl search | https://www.security.org/home-security-systems/simplisafe/ ; https://www.safehome.org/security-systems/simplisafe/monitoring/ | Excerpt: self-monitoring with camera recordings $9.99/mo; professional monitoring $22.99–$79.99/mo | §10.5 H3 3; §14 comparison |
| A5 | `ADT monitoring cost per month 2026 professional installation contract 36 months` · Firecrawl search | https://www.adt.com/own-vs-rent-security/self-setup | Excerpt: "ADT Security monitoring starting at $24.99/mo" (self setup); "pro install w/36-month monitoring contract starting at $56.99/mo" | §10.5 H3 3; §14 comparison (36-month term stated, $56.99 not shown) |
| A6 | same | https://www.security.org/home-security-systems/adt/ | Excerpt: ADT Pro Install monitoring from $49.99/mo; ADT Blu camera-only self-monitoring $9.99 | Cross-check only |

### 1.4 New York State law (every NY page) — carried from research/dvr-upgrade.md rows G1–G5
| # | Source | URL | Finding | Used (Nassau) |
|---|---|---|---|---|
| G1 | carried (DVR G1) | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a: private right of action against a person who installs a video imaging device on adjoining property to record recreational activity in the backyard without written consent, with intent to harass, annoy or alarm | §8.5 bullet 1; §10.5 H3 6; §Sources |
| G2 | carried (DVR G2) | https://nysenate.gov/legislation/laws/pen/250.40 | Penal Law §250.40: "place and time when a person has a reasonable expectation of privacy" = where a person could reasonably expect to fully disrobe in privacy | §8.5 bullet 2 |
| G3 | carried (DVR G3) | https://nysenate.gov/legislation/laws/PEN/250.05 | Penal Law §250.05 eavesdropping; "mechanical overhearing" = recording a conversation without consent of at least one party by someone not present | §8.5 bullet 3 |
| G4 | carried (DVR G4/G5) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit (FY2025 budget): small businesses, up to $3,000 per retail location, cameras among eligible costs | §8.5 bullet 7 |

### 1.5 Keyword plan (five layers, silo)
- **Service:** residential security camera installation, home security camera installation, home camera system, doorbell camera installation, driveway camera, porch camera, indoor home camera, wired home cameras, NVR for home.
- **Problem:** package theft / porch pirates, car break-ins and stolen cars from driveways, burglary, false alarms, blurry faces, cameras too high, recorder clock wrong, footage overwritten, cameras offline after outage, inherited system / previous owner access, neighbour privacy complaints.
- **Technology:** wired PoE cameras, video doorbell on transformer, turret, bullet, narrow lens, floodlight camera, network video recorder, surveillance drive, UPS battery backup, NTP time server, person detection, privacy masks, user permissions, alarm interface, point-to-point wireless bridge, export to USB / share link.
- **Industry:** homeowners, two-family owners / small landlords, home offices, trade yards behind houses, flats over shops, condo/co-op owners.
- **Geographic (Nassau page):** Nassau County; Levittown, Hicksville, Plainview, Syosset, Bethpage, East Meadow, Garden City, Rockville Centre, Manhasset, Port Washington, Massapequa Park, Massapequa, Wantagh, Baldwin, Freeport, Oceanside, Island Park, Long Beach, the Bellmores, Merrick, Elmont, Valley Stream, Franklin Square, West Hempstead, Uniondale, Floral Park, New Hyde Park, Great Neck Plaza, Sea Cliff, Glen Cove, Old Westbury, Muttontown, the Brookvilles, Lattingtown, Mill Neck, Hewlett Harbor, Lawrence, Five Towns; Hempstead Turnpike, Sunrise Highway, Old Country Road, Northern Boulevard, Eastern Parkway (Baldwin), Long Beach Road / Suffolk Road (Island Park), Stewart Avenue (Garden City).

### 1.6 Silo pricing (no invented prices)
Base = the pre-rebuild Brooklyn page (`residential-security-camera-installation-brooklyn.html`, Brooklyn = §9 1.00×): Co-op/Apartment 1–3 cameras $950–$2,000 · Row house/Two-family 4–8 $2,000–$4,500 · Brownstone (full) 6–10 $3,500–$7,000 · Detached/Semi-detached 6–12 $3,500–$8,000; "$0 monthly fees". Service rate $195/hr, 3-hr minimum ($585) per blueprint §9 (protected; not on the initial install). No BYOE price published in the silo → BYOE paragraph links to /install-your-own-camera-system without a figure.
Nassau = ×1.15, round half-up: $1,092.50→**$1,093**; $2,000→**$2,300**; $4,500→**$5,175**; $3,500→**$4,025**; $7,000→**$8,050**; $8,000→**$9,200**.
FLAG (inconsistency): the pre-rebuild Nassau and Long Island pages showed $1,117–$2,000 / $2,000–$4,200 / $3,000–$6,500 (Nassau) and $1,117–$2,500 for "4 to 8 cameras" on the LI hub — not the §9 multiplier of the Brooklyn base (1,117/950 = 1.176; upper bounds unscaled; LI hub FAQ range contradicts its own table). Not carried. The old Brooklyn page's JS chips ($250 service call, $175/drop, $600 alarm) are site-wide widget values, not silo prices — not used.

---

## Question register — every question on every residential-security-camera-installation page

Extracted programmatically (tools/check_page.py parser: `.faq-question` items + every H2/H3/summary ending in "?") from the 16 files as they stood before this rebuild. 193 questions. The Nassau block below the pre-rebuild list is the rebuilt page.

### residential-security-camera-installation-bronx — pre-rebuild (12)
- How much does home security camera installation cost in the Bronx?
- Do you handle co-op and condo board documentation?
- Can a Bronx renter install a camera without landlord permission?
- Where can my camera legally point in an apartment building?
- Are there monthly fees for a home camera system?
- Can you wire a pre-war Bronx building without disturbing the walls?
- How many cameras does my Bronx property need?
- Do you protect cameras near the water from salt-air corrosion?
- Do the cameras record in color at night?
- Can I watch my cameras from my phone, and can tenants have their own access?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-brooklyn — pre-rebuild (12)
- How much does home security camera installation cost in Brooklyn?
- Can you mount cameras on brick without damaging it or breaking Landmarks rules?
- Do you cover the stoop, rear yard, and cellar?
- Will the cameras work on my poorly lit side street and back yard?
- How do you stop a busy block from triggering alerts all night?
- Are there monthly fees for a home camera system?
- How many cameras does my Brooklyn home need?
- Wired or wireless for a Brooklyn house?
- Do the cameras record in color at night?
- Can I watch my home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-dutchess-county — pre-rebuild (12)
- How much does home security camera installation cost in Dutchess County?
- Can you install on a historic estate or 1800s farmhouse without spoiling the look?
- Can you cover a horse farm — barns, paddocks, arena, and a quarter-mile drive?
- My driveway is a quarter-mile and the Wi-Fi won’t reach the barn — can you fix that?
- Will the cameras survive a Dutchess winter?
- Are there monthly fees for a home camera system?
- I’m only up on weekends — can I watch the estate from the city?
- How many cameras does my Dutchess home need?
- Do the cameras record in color at night?
- How do you keep deer and wildlife from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-hudson-valley — pre-rebuild (12)
- How much does home security camera installation cost in the Hudson Valley?
- Do you cover long driveways, barns, and wooded acreage?
- Can you stop the deer and wildlife from triggering my cameras?
- Can you monitor a weekend or seasonal home that sits empty?
- Are there monthly fees for a home camera system?
- Will the cameras hold up to upstate winters?
- How many cameras does my home need?
- Wired or wireless for a rural property?
- Do the cameras record in color at night?
- Can I watch my home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-long-island — pre-rebuild (12)
- How much does home security camera installation cost on Long Island?
- Do you cover the whole property — driveway, pool, and detached garage?
- Can you monitor a seasonal or waterfront home that sits empty?
- Are there monthly fees for a home camera system?
- Will the cameras hold up to Long Island winters and salt air?
- How many cameras does my home need?
- Wired or wireless for a house out here?
- Will the cameras stop package theft?
- Do the cameras record in color at night?
- Can I watch my home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-manhattan — pre-rebuild (12)
- How much does home security camera installation cost in Manhattan?
- Do I need board approval to install cameras in my co-op or condo?
- Do you handle the COI and building requirements?
- I rent — can I install cameras without drilling?
- Where can my camera legally point?
- Why do my Wi-Fi cameras keep dropping offline?
- Are there monthly fees for a home camera system?
- Can you wire a pre-war apartment without damaging the walls?
- How many cameras does my apartment need?
- Can I watch my cameras from my phone?
- Do I need a licensed contractor for an apartment install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-nassau-county — pre-rebuild (12)
- How much does home security camera installation cost in Nassau County?
- Can you read license plates at the driveway or gate?
- Will the cameras hold up on a coastal or South Shore home?
- Do you cover long driveways, pools, and outbuildings?
- Are there monthly fees for a home camera system?
- How many cameras does my Nassau home need?
- Do the cameras keep recording if my internet goes out?
- Wired or wireless for a Nassau property?
- Do the cameras record in color at night?
- Can you avoid recording my neighbor’s yard on a tight lot?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-nyc — pre-rebuild (13)
- Renting, Owning, or on a Co-op Board?
- How much does home security camera installation cost in NYC?
- Can you install cameras on a brownstone without damaging the brick?
- I rent — what can I install without drilling or landlord approval?
- Can you get my co-op or condo board to approve the install?
- Are there monthly fees for a home camera system?
- How many cameras does my home need?
- Will the cameras actually stop package theft?
- Do the cameras record in color at night?
- Wired or wireless for a house?
- Can I watch my home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-orange-county — pre-rebuild (12)
- How much does home security camera installation cost in Orange County?
- Can you cover a long driveway, a barn, and a field?
- My property is too big for Wi-Fi to reach the barn — can you fix that?
- My rural road is pitch dark — will the cameras see at night?
- Will the cameras survive an Orange County winter?
- Are there monthly fees for a home camera system?
- Can I watch my property from the city while I commute?
- How many cameras does my Orange County home need?
- Do the cameras record in color at night?
- How do you keep deer and wildlife from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-putnam-county — pre-rebuild (12)
- How much does home security camera installation cost in Putnam County?
- Can you cover a dock, a long driveway, and a tree line?
- My place sits empty most of the week — can I keep an eye on it?
- My battery doorbell is always dead when I drive up to my weekend house — can you fix that?
- Will the cameras survive a Putnam winter and the waterfront?
- Are there monthly fees for a home camera system?
- Can I watch my property from the city while I’m away?
- How many cameras does my Putnam home need?
- Do the cameras record in color at night?
- How do you keep deer and wildlife from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-queens — pre-rebuild (12)
- How much does home security camera installation cost in Queens?
- Can a camera legally cover my shared driveway?
- How do I stop porch pirates from stealing packages?
- Can you cover the driveway and read license plates?
- Can I install cameras if I live in a Queens co-op?
- Are there monthly fees for a home camera system?
- How many cameras does my Queens home need?
- Will the cameras keep recording during a blackout?
- Do the cameras record in color at night?
- Can I watch my home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-rockland-county — pre-rebuild (12)
- How much does home security camera installation cost in Rockland County?
- Can you install on a historic river-town home without spoiling the look?
- Can you cover a gated estate or a whole apartment building?
- My Wi-Fi won’t reach the detached garage across the lot — can you fix that?
- Will the cameras survive a Rockland winter?
- Are there monthly fees for a home camera system?
- Can I watch my home from the city while I commute?
- How many cameras does my Rockland home need?
- Do the cameras record in color at night?
- How do you keep deer and wildlife from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-staten-island — pre-rebuild (12)
- How much does home security camera installation cost on Staten Island?
- Will the cameras survive a coastal winter and the Sandy flood zone?
- Do you cover long driveways, detached garages, and outbuildings?
- Can you read license plates at the driveway?
- Are there monthly fees for a home camera system?
- How many cameras does my Staten Island home need?
- Wired or wireless for a Staten Island property?
- Do the cameras record in color at night?
- Can I watch my home cameras from my phone?
- Do you take over a Ring or Wyze kit that didn’t hold up?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-suffolk-county — pre-rebuild (12)
- How much does home security camera installation cost in Suffolk County?
- Can you monitor my Hamptons or North Fork home while it sits empty?
- Can the system record if my vacation home has no internet in the off-season?
- Can you reach a barn or outbuilding hundreds of feet from the house?
- Are there monthly fees for a home camera system?
- How do you keep deer and wildlife from triggering alerts all night?
- How many cameras does my Suffolk property need?
- Will the cameras hold up on a waterfront home?
- Do the cameras record in color at night?
- Can I watch my Suffolk home cameras from my phone?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-ulster-county — pre-rebuild (12)
- How much does home security camera installation cost in Ulster County?
- My parcel has no cell signal and no utility power — can you still cover it?
- Can you install on a historic stone house without marring it?
- My driveway is long and the Wi-Fi won’t reach the barn — can you fix that?
- Will the cameras survive an Ulster winter?
- Are there monthly fees for a home camera system?
- I’m only up on weekends — can I watch the mountain house from the city?
- How many cameras does my Ulster home need?
- Do the cameras record in color at night?
- How do you keep deer and bears from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?
### residential-security-camera-installation-westchester-county — pre-rebuild (12)
- How much does home security camera installation cost in Westchester County?
- Can you install on a historic home without spoiling the architecture?
- Can you cover an estate — long driveway, pool house, barn, and grounds?
- My Wi-Fi won’t reach the detached garage or pool house — can you fix that?
- Will the cameras survive a Westchester winter?
- Are there monthly fees for a home camera system?
- Can I watch my home from the office while I commute?
- How many cameras does my Westchester home need?
- Do the cameras record in color at night?
- How do you keep deer and wildlife from triggering alerts all night?
- Do I need a licensed contractor for a home install?
- Do you fix or take over a system another company installed?

### residential-security-camera-installation-nassau-county — REBUILT 2026-10-18 (29: 19 Q&A H3 + 10 FAQ; replaces the 12 pre-rebuild questions above)
- When an officer knocks asking for video, what should I be able to hand over within a few minutes?
- Why does the recorder's clock matter so much to a detective?
- From how far away will a door camera still show a recognisable face?
- How many days of recordings should a Nassau house keep?
- Garden City runs a private camera registry. Does signing up let police look through my cameras?
- Our village set up a neighbour footage-sharing scheme like Hewlett Harbor's. Can a wired system take part, or only Ring?
- Can I give a detective one clip without handing over my password or live access?
- If we only put up cameras and no alarm panel, do we still need a Nassau County police permit?
- Floral Park charges for false alarms. Can the cameras help us check before police are sent?
- Can the alarm siren and the cameras run from one app?
- Police keep warning about cars left unlocked with the fob inside. What should our driveway camera be watching at 3 a.m.?
- Packages in Massapequa Park vanished minutes after FedEx drop-offs. How quickly can an alert reach us after a box lands?
- Our car sits on the street because the driveway is short. Can a house camera cover it legally?
- In a slab-built Levitt house with no basement, where does the recorder go?
- A split-level has doors on three levels. How do you avoid blind spots between them?
- Our house was lifted after Sandy. What should a camera watch underneath it?
- Who in the family should be able to delete footage or change settings?
- Should there be cameras inside the house at all?
- When we sell the house, do the cameras stay and how do we hand them over?
- How long does installation take on a typical Nassau house?
- Can cameras go on vinyl or aluminium siding without letting water in?
- Will the doorbell we already own work alongside a new recorder?
- Can we see the cameras on the television in the den?
- What do we need to redo if we switch internet provider or replace the router?
- Does someone need to be home for the whole visit?
- Can more cameras be added in a year or two without starting over?
- Could someone hack into the recorder from the internet?
- Should we turn on face recognition so the system knows the family?
- Will you take down the old cameras and fill the holes they leave?

De-dup note: checked by meaning against all 193 pre-rebuild questions. Generic intents already held by other pages (overall cost, monthly fees, camera count, wired vs wireless, colour night vision, phone viewing, licensed contractor, takeover of another installer's system, plate reading, coastal/winter survival, long driveways/pools/outbuildings, internet/blackout recording, neighbour-yard avoidance, renters, board approval, package-theft deterrence, shared driveway, wildlife alerts, remote watching while away) are not asked on the rebuilt Nassau page; where the body touches them it is in passing, not as a question.

---

## Nassau County

Thesis: a Nassau home camera system is judged the morning after an incident — by what the owner can hand an NCPD officer, a village detective, an alarm-permit office or an insurer — so placement (faces at the step, movement between parked cars), recorder time, retention, sharing and alarm integration are planned backwards from that moment, across a housing range from 60×100 Levitt slab lots to two-acre North Shore zoning. Differs from lorex-camera-installation-long-island (house-style / cable-route thesis) and dvr-upgrade-nassau-county (recorder swap on existing coax).

### Housing and county structure (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | carried (DVR N2: `Nassau County population 2020 census 1,395,774` · Firecrawl search + scrape) | https://www.census.gov/quickfacts/nassaucountynewyork | 1,395,774 (2020); owner-occupied 81.9%; median owner-occupied value $684,700 | §5 para 1; §5.5 bullet 1 |
| H2 | carried (DVR N1: `Nassau County three towns two cities 64 incorporated villages` · Firecrawl search) | https://www.ny.gov/counties/nassau | 2 cities, 3 towns, 64 villages, 60+ hamlets | §5 para 4; §5.5 bullet 2 |
| H3 | carried (DVR N3) | https://en.wikipedia.org/wiki/Levittown,_New_York | 17,447 homes by 1951; concrete slabs, no basement | §5.5 bullet 3; §7 card 1; §7.5; §9 "slab-built Levitt house"; §13 Levittown |
| H4 | `Levittown houses lot size 60 by 100 feet original Levitt homes` · Firecrawl search | https://realestate.wharton.upenn.edu/wp-content/uploads/2017/03/556.pdf ; https://www.nytimes.com/1983/11/27/realestate/if-you-re-thinking-of-living-in-levittown.html | Excerpts: "Levittown house was a 750-square-foot cottage … (Typical lots were 60 feet by 100 feet.)"; NYT 1983: "plot, which averaged 60 by 100 feet" | §5.5 bullet 3; §7 card 1; §10.5 H3 6; §9 street-parking answer ("narrow Levittown lots") |
| H5 | `Old Westbury Muttontown Brookville village minimum lot size two acres zoning` · Firecrawl search | https://www.muttontownny.gov/wp-content/uploads/2019/11/VM-Village-Comprehensive-Master-Plan.pdf (also excerpts: irenerallisrealtor.com — Old Westbury BB district 87,120 sq ft / two acres per family; patriciasantella.com — Upper Brookville 2- and 5-acre zones) | Muttontown master plan: "Residence A-1 (2 Acres)" districts; low-density 2+ acres per family | §5.5 bullet 3; §7 card 5 ("two-acre or larger zoning"); §7.5 "Two-acre lots" |

### Theft, burglary and police (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | `Nassau County package theft porch pirates arrests 2025` · Firecrawl search → scrape (query) | https://www.cbsnews.com/newyork/news/police-warn-about-porch-pirates-stealing-packages-in-nassau-county/ | CBS NY (Nov 2023, image dated 2023/11/07): Massapequa Park, Massapequa, Wantagh; "six times in 11 days mobile devices were stolen right after a FedEx delivery"; thieves "appear to work as pair"; Crime Stoppers reward | §5 para 2; §9 Driveways H3 2; §13 Massapequa Park card |
| N2 | same search → scrape (query) | https://abc7ny.com/post/porch-pirate-package-thief-robber-caught-on-camera-ring-cam/14040321/ | ABC7 Nov 10 2023: box taken from a 72-year-old man's porch on Eastern Parkway, Baldwin; "captured on Ring surveillance video"; arrested at Baldwin train station about two hours later; petit larceny (suspect not named on page) | §5 para 2; §8 Sunrise Hwy card; §10.5 H3 2; §13 Baldwin card |
| N3 | carried (DVR N4) | https://abc7ny.com/post/nassau-county-police-task-force-burglaries-long-island/14337932/ | Jan 2024 NCPD burglary task force; "burglars are attracted by cars in people's driveways" | §5 para 2 |
| N4 | carried (DVR N6) | https://www.nassaucountyny.gov/CivicAlerts.asp?AID=10038&ARC=11790 | LD14 bulletin 4/8/2022 relaying NCPD: cars left unlocked with key fob; thieves look for unfolded side mirrors; "License plate numbers are extremely valuable for the police" | §5 para 2; §9 Driveways H3 1 |
| N5 | `Nassau County car thefts 2024 2025 police key fob driveway stolen vehicles increase` · Firecrawl search → scrape (query) | https://www.nassaucountyny.gov/CivicAlerts.asp?AID=9023&ARC=11138 | NCPD tips (posted 4/21/2021): "Always lock your vehicle, even when it's parked in your driveway or garage"; take keys/fob; park in well-lit areas | §9 Driveways H3 1; §Sources |
| N6 | same search → scrape | https://www.governor.ny.gov/news/during-vehicle-theft-prevention-month-governor-hochul-advises-drivers-how-protect-themselves | July 10 2026: statewide vehicle thefts down ~15% 2024→2025; "Do not leave your key fob in the vehicle" | Not used on page (statewide, kept for siblings) |
| N7 | `Nassau County police license plate reader cameras Flock 2025 Long Island` · Firecrawl search → scrape (query) | https://statescoop.com/nassau-county-new-york-mamdani-surveillance-tech/ | Nov 2025: county executive ordered NCPD to install facial-recognition cameras and licence-plate readers along the NYC border | §10.5 H3 5 (stated neutrally; no politics) |
| N8 | same search | https://www.facebook.com/newsday/videos/police-departments-across-nassau-have-installed-nearly-70-license-plate-reading-/495523773524211/ ; https://www.licriminallaw.com/blog/flock-cameras-in-nassau-county-what-long-island-drivers-need-to-know-about-license-plate-readers/ | Excerpts: "Police departments across Nassau have installed nearly 70 license plate reading cameras in recent months"; "47 documented automated license plate reader cameras in the Village of Hempstead" | §10.5 H3 5 ("village police departments have added plate readers of their own"); §Sources (Newsday excerpt) |
| N9 | `liherald.com burglaries residents security cameras footage police village 2025` · Firecrawl search → scrape (query) | https://www.liherald.com/stories/increasing-home-security-in-hewlett-harbor,114732 | Herald, May 16 2019: Hewlett Harbor "Operation Private Eyes", resident-controlled virtual neighbourhood watch built on Ring; residents may send footage to village security or NCPD; "nobody has to share any footage that they don't want to" | §5 para 4; §9 Registries H3 2; §13 Five Towns card |
| N10 | same search → scrape (query) | https://www.liherald.com/stories/smile-youre-on-crime-cameralawrence-proposes-security-cams-at-18-sites,10242 | Herald, 2005: Lawrence proposed cameras at 18 village entrances after a May 4 armed home invasion (4th in the Five Towns since December) | §13 Five Towns card |
| N11 | `Nassau County police security camera registration program residents` · Firecrawl search → scrape | https://gardencitypolice.net/private-camera-reg | Garden City PD voluntary Private Camera Registration Program; "does NOT provide us access"; officers canvass door to door; detectives "may ask to inspect your surveillance video recorded during a finite period"; Detective Division 349 Stewart Ave. NOTE: other search hits for "Nassau County camera registry" were Nassau County, **Florida** (Sheriff's Office) — rejected. | §5 para 4; §9 Morning-after H3 4; §9 Registries H3 1; §10.5 H3 5; §13 Garden City card |

### Alarm permits and licensing (P)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `village alarm permit registration false alarm fee Nassau County NY village code` · Firecrawl search → scrape | https://alarm.pdcn.org/applynewpermit.aspx | NCPD burglar alarm permit: $100 residence / $200 business; valid two years, renewable two more; certificate posted at or near the panel; not for fire alarms; application asks for central monitoring company | §5.5 bullet 4; §8.5 bullet 4; §9 Alarm H3 1 |
| P2 | same search → scrape | https://www.cityalarmpermit.us/Pages/CustomPage.html?CityID=50&ScreenName=Permit_Form | Village of Floral Park alarm code amended Jan 15 2013; permit new residential $50 / renewal $25, valid 1 year; false alarm fees $25, $50, $100, $200, $250 (5th+); robbery/panic/burglary-in-progress false alarm $150 each | §5 para 4; §5.5 bullet 4; §9 Alarm H3 1–2 |
| P3 | same search | https://www.kirschenbaumesq.com/article/nassau-county-alarm-permit-false-alarm-ordinance | Excerpt: Nassau local law (2007) amending the Administrative Code re false alarm transmissions | Background only |
| P4 | `Nassau County Department of Consumer Affairs home improvement license required who needs` · Firecrawl search (scrape of /1566 and /1563 returned no body) | https://www.nassaucountyny.gov/1547/Consumer-Affairs | Excerpt: "All Licensed Home Improvement Contractors must be fingerprinted"; licensing of home improvement businesses | §8.5 bullet 5 |
| P5 | same search | https://www.nycbar.org/why-all-home-improvement-contractors-need-to-be-licensed-some-useful-information-for-contractors-and-their-clients/ | Excerpt (older table): Nassau $200 two-year licence; City of Long Beach requires Nassau licence first | Not used (date unclear) |
| P6 | carried (DVR N18/N19) | https://hempsteadny.gov/191/Building-Department ; https://www.lowvoltagenation.com/posts/nassau-county-new-york-security-camera-permit-requirements | Town/village building departments decide permits; contact before work | §8.5 bullet 6 |

### Storms and flooding (W)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| W1 | carried (DVR N10) | https://www.lipower.org/wp-content/uploads/2020/09/LIPA-Isaias-30-Day-Report-Final.pdf | Isaias: ~645,000 customer outages; full restoration eight days | §5.5 bullet 5; §9 clock H3; §10.5 H3 7 |
| W2 | carried (DVR N13) | https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York | Sandy: Nassau evacuation of surge zone south of Sunrise Highway; Long Beach ~$150M damage | §5.5 bullet 6 |
| W3 | `Superstorm Sandy Nassau County homes damaged Island Park Oceanside Five Towns flooding` · Firecrawl search → scrape (query) | https://www.nysenate.gov/newsroom/in-the-news/2021/todd-kaminsky/13-million-island-park-project-address-chronic-flooding | 2021: "most of Island Park was underwater from Superstorm Sandy"; $1.3M state project; $33M FEMA drainage project "to help protect 1,100 homes and 118 businesses"; ≥15 tidal valves; streets incl. Long Beach Road, Suffolk Road | §5.5 bullet 6; §13 Island Park card; §7.5 raised houses (Reynolds Channel named in source) |
| W4 | same search | https://www.liherald.com/stories/assessing-the-damage-in-oceanside-and-island-park,44697 ; https://abc7ny.com/post/long-beach-sandy-superstorm-memories/12380694/ | Excerpts only (damage assessments, Long Beach recollections) | Not used |

### Landmarks used in §13 (L)
| # | Landmark | Source row | Used |
|---|---|---|---|
| L1 | Garden City / 349 Stewart Ave (police HQ) | N11 | §13 card 1 |
| L2 | Levittown / Hempstead Turnpike / Levittown Public Library | H3 + carried DVR N14 (https://en.wikipedia.org/wiki/New_York_State_Route_24) | §13 card 2 |
| L3 | Baldwin, Eastern Parkway, Baldwin train station | N2 | §13 card 3; §8 Sunrise Hwy card |
| L4 | Massapequa Park / Massapequa / Wantagh | N1 | §13 card 4 |
| L5 | Island Park, Long Beach Road, Suffolk Road | W3 | §13 card 5 |
| L6 | Five Towns: Lawrence, Hewlett Harbor | N9, N10 | §13 card 6 |
Corridor names in §8 cards (Hempstead Turnpike through Elmont/Franklin Square/West Hempstead/Uniondale/East Meadow; Sunrise Highway through Valley Stream/Lynbrook/Rockville Centre to Merrick) = carried DVR N14/N15 (https://en.wikipedia.org/wiki/New_York_State_Route_24 ; https://en.wikipedia.org/wiki/New_York_State_Route_27).

### Local sources EMPTY
- r/longisland Nassau-specific camera threads opened in full: EMPTY (not accessible in build env — scrape refused; excerpts R1–R3 only).
- Patch / Newsday articles: EMPTY (not accessible in build env — not opened; Newsday seen only as Facebook excerpt N8).
- Yelp 1–3★ Nassau camera installers: EMPTY (not accessible in build env).
- PAA / PASF / Answer the Public / AI Overview / Bing / DDG for "residential security camera installation Nassau": EMPTY (not accessible in build env).

### House practices stated without an external source (FLAG for Anwar)
- Two-hour arrival windows, seven days to 8 PM; "most faults fixed within one to two hours on site" (company constants copied from live pages).
- Recorder set to an internet time server; drive sized for ≥30 days; drive-failure alert; export rehearsal at handover; power-cycle test (installer practice).
- Face-identification distance "roughly two to four metres" for a typical wide lens (rule of thumb, not sourced to a spec).
- Network cable 100 m per run (Ethernet standard, not separately sourced here).
- Install duration (FAQ 1: a few hours / one day / second day for larger houses).
- Mounting on siding via mounting block, drip loops; old-camera removal and hole sealing; face recognition off by default; no router port-forwarding.
- Field Notes describe a standing walk-through practice in Anwar's voice, not a specific dated job.
- The page does not claim AESS holds a Nassau County home improvement licence (only NYS low-voltage #12000287431) — Anwar to confirm whether AESS holds one.

### Images (11) — Drive has no residential-camera folder; CompanyCam not connected
Silo had no image directory (all 16 old pages used only /images/cam-dual-lens-active.jpeg). New dir `images/residential-security-camera-installation/`. Real job photos captioned "Example photo from another AESS job (not a Nassau home), cropped"; crops exclude signage, people, the "1096" house number and timestamps. Product shots captioned "Manufacturer product photo (not an installed unit)". All 11 inspected; none AI-looking.

| Output | Source | Note |
|---|---|---|
| …-white-4k-turret-camera-product-photo.webp (hero) | images/ubiquiti-unifi-g6-turret-4k-camera-white.jpg | product, white border trimmed |
| …-wide-lens-recorder-tile-of-sidewalk-and-curb.webp | images/nassau-window-depot-monitor.jpeg | real; left part of CAM 4 tile only (house number, people, timestamp excluded) |
| …-black-poe-video-doorbell-product-photo.webp | images/ubiquiti-unifi-g6-entry-doorbell.jpg | product |
| …-small-black-camera-high-on-white-wall.webp | images/rockland-toyota-wall-camera.jpeg | real; cropped |
| …-blue-and-white-network-cables-along-ceiling-pipe.webp | images/rockland-toyota-nvr-monitor.jpeg | real; top strip only, screen excluded |
| …-black-narrow-view-bullet-camera-product-photo.webp | images/ubiquiti-unifi-ai-lpr-bullet-4k-camera-black.jpg | product |
| …-black-bullet-camera-on-ceiling-mount.webp | images/rockland-toyota-ceiling-bullet.jpeg | real; cropped |
| …-white-video-doorbell-product-photo.webp | images/arlo-2k-video-doorbell.jpg | product |
| …-black-desktop-network-video-recorder-product-photo.webp | images/nvr-reolink-nvs8.png | product (maker logo visible) |
| …-white-twin-floodlight-camera-product-photo.webp | images/floodlight-swann-4k.png | product (file named Swann; small logo on unit — caption names no brand) |
| …-white-compact-indoor-camera-product-photo.webp | images/ubiquiti-unifi-g5-flex-compact-camera-white.jpg | product; grey bar cropped off |

### Pricing used
§9 Nassau ×1.15 on the Brooklyn base (row 1.6): $1,093–$2,300 (1–3 cams) · $2,300–$5,175 (4–8) · $4,025–$8,050 (6–10 full coverage) · $4,025–$9,200 (6–12 large detached) · $195/hr, 3-hr min ($585). Packages = the 1–3, 4–8 and 6–12 tiers.

### Similarity (masked geo, digits → 0)
Page vs each of the 15 siblings: difflib word-sequence ratio 0.060–0.076; 5-word-shingle Jaccard ≤ 0.016. Max paragraph ratio 0.538 (pricing table cell vs rockland-county / 0.517 westchester). Also checked vs lorex-camera-installation-long-island (seq 0.086), dvr-upgrade-nassau-county (0.179, shared chrome/NAP/warranty), smart-lock- and sonos-installation-nassau-county (≤0.090).
