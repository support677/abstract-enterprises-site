# Research — Apartment Building Security Camera Installation silo

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Unreachable sources are written `EMPTY (not accessible in build env)`.

## Silo-wide findings

### Gathered while building the Manhattan page (2026-10-18)

### Surfaces that could not be opened in this environment
| # | Source | Status |
|---|---|---|
| 1 | Reddit (r/AskNYC, r/NYCapartments, r/landlord, r/homedefense) | Query `reddit co-op board cameras hallway Manhattan shareholder privacy footage request` · WebSearch restricted to reddit.com · **EMPTY (not accessible in build env — proxy rejected the request, HTTP 400)**. Substituted with Brick Underground reader Q&As and local news below. |
| 2 | Google People Also Ask | **EMPTY (not accessible in build env)** — no live Google SERP surface. |
| 3 | Google PASF | **EMPTY (not accessible in build env)**. |
| 4 | Answer the Public | **EMPTY (not accessible in build env)**. |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — live AI Overview cannot be rendered. The page's Reality Check instead quotes the published aggregator claims that AI Overviews typically summarise (Angi, HomeAdvisor — below), labelled as aggregator claims, not as a quoted AI Overview. |
| 8 | Bing / DuckDuckGo autocomplete & related | **EMPTY (not accessible in build env)** — only one search backend available. |
| 11 | Yelp 1–3★ | Query `yelp security camera installation Manhattan reviews never came back wires exposed` · WebSearch · no Yelp result returned → **EMPTY (not accessible in build env)**. HomeAdvisor Manhattan listing fetched instead: no 1–3★ reviews visible (EMPTY for complaints). Thumbtack Manhattan page: **EMPTY (robots disallowed)**. |

### Aggregator / "AI-style" cost claims (feeds AI Overview Reality Check)
- `security camera installation cost` (allowed_domains angi/homeadvisor/fixr) · WebSearch → https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera/ny/new-york · Angi: New York, NY average **$1,509**, typical **$797–$2,222**; installation **$100–$350 per camera** on top of camera price; pros **$30–$80/hour**; wireless cameras $30–$325, wired $150–$500; DIY "can void your camera's warranty". · Used: §10.5 Reality Check H3 1–2; Pricing intro.
- same query · https://www.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera/ · HomeAdvisor national average **$1,289** ($589–$2,040); labor **$80–$200 per camera**, **$50–$100/hour**; labor 50–70% of total; four-camera wired IP system $500–$1,500; Ring "5–8 camera setups" $500–$1,000+. · Used: §10.5 H3 1, 3, 6 (ADT/Ring comparison context).
- `"apartment building" security camera system cost per camera NYC Angi Fixr 2026` · WebSearch → https://ipvm.com/discussions/surveillance-cameras-spreading-in-nyc-residences · IPVM summary (Oct 5, 2013) of a New York Times feature (Oct 6, 2013): co-op/condo boards protected by business judgment rule; footage helped police; perimeter-camera footage helped get an $8 million slip-and-fall suit dismissed; a security firm then estimated full systems at $3,000–$20,000. · Used: §5 Neighborhood para 3; Reality Check H3 7 (dated figure, flagged as 2013).
- Fixr: no Fixr page surfaced in the restricted search → EMPTY.

### Legal / licensing (silo-wide NY rules)
- `New York State Department of State security and fire alarm installer license Article 6-D requirements` · WebSearch → https://dos.ny.gov/get-security-or-fire-alarm-installer-license · NYS DOS licence: 81 hours qualifying education (four 15-hr modules + one 21-hr module, incl. "security systems"), fingerprinting, fees ($200/$185 initial, $100 renewal), master-electrician waiver; no CE currently. Page does not say whether CCTV alone is covered. · Used: §8.5 compliance callouts; Q&A "licence" question; Sources.
- same query → https://ur.nyc-business.nyc.gov/nycbusiness/description/license-to-install-service-or-maintain-security-or-fire-alarm-systems · NYC Business portal: NYSDOS issues the licence; "You need a license to install or maintain security or fire alarm systems." · Used: §8.5; Sources.
- `NYC law security cameras residential buildings tenants notice HPD lobby cameras` · WebSearch → https://tenant-rights.com/new-york/new-york-laws-on-security-cameras-in-building-common-areas · Common-area cameras generally allowed (hallways, lobbies, laundry); never where reasonable expectation of privacy (apartments, bathrooms, locker rooms); NY one-party consent for audio; notice "builds trust" though not always required. The page's claim about "NYC Local Law 3 of 2019" requiring camera quality could NOT be verified → **not used**. · Used: Q&A privacy cluster.
- `apartment building security camera installation Manhattan co-op board alteration agreement` · WebSearch → https://cooperatornews.com/article/qa-camera-placement · Newman Ferrara attorney: "New York does not recognize a common law right of privacy in public or common areas"; condo owners generally need board approval to alter common areas; camera seeing into another unit and audio raise risk; boards protected by business judgment rule. · Used: Q&A "shareholder doorbell camera" + FAQ.
- same search → https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops · FirstService Residential: footage typically kept **30 to 90 days**; access limited to manager/security provider with a log of requests and viewers; residents shouldn't get copies without board+counsel approval; no cameras in employee restrooms/locker rooms (NY Labor Law §203-c); audio uncommon, eavesdropping risk; "avoid installing dummy cameras"; resident doorbell rules (board approval, not facing another unit, audio off). · Used: Q&A retention + footage-access cluster; Reality Check H3 5; FAQ.
- same search → https://www.brickunderground.com/live/ask-condo-co-op-lawyer-board-apartment-complaints-video-doorbell-privacy-legal-ban-harassment-pullman-nyc · Brick Underground, June 23, 2022: a co-op board can restrict/ban video doorbells in common hallways via house rule without shareholder vote; footage may be evidence in a Pullman proceeding. · Used: Q&A doorbell question.
- `reddit AskNYC building cameras lobby footage super won't show packages stolen` · WebSearch → https://www.brickunderground.com/rent/stolen-packages-security-camera · Brick Underground, Aug 26, 2019: no city law requires rental buildings to have working cameras; attorney Jeffrey Reich: landlord aware of crime may have a duty to take reasonable steps; tenants should write to management listing items/dates/broken camera. · Used: Q&A "broken lobby camera in a rental"; Reality Check H3 4.

### Building paperwork
- `Manhattan co-op alteration agreement contractor certificate of insurance additional insured managing agent work hours 9 to 5` · WebSearch → https://hauseit.com/co-op-renovation-rules-nyc · Typical co-op work hours 9am–5pm (vs citywide 7am–6pm); many bar loud noise until 10am; most prohibit weekend/holiday work; COI typically at least $1,000,000 naming co-op, managing agent, unit owner, board as additional insured; alteration agreement from managing agent; refundable deposit + processing fee. · Used: "Paperwork" section; Process step 2; Q&A.
- same search → https://habitatmag.com/Publication-Content/Bricks-Bucks/2023/2023-September/Alert-Condo-Super-Spots-Fake-Certificate-of-Insurance · Habitat, Sept 20, 2023: resident manager at The Future, a 165-unit condo in Kips Bay, caught a fake COI (broker details mismatched, handwritten check marks, policy expired); lessons: broker should send the COI directly, verify with carrier, name building/board/agent as additional insureds. · Used: Paperwork section; Q&A COI question.

### Elevator cabs
- `camera inside elevator cab NYC installation elevator contractor DOB permit traveling cable` · WebSearch → https://ipvm.com/reports/elevator-surveillance-guide · Options: traveling cable (UTP unreliable for Ethernet on ~300 ft travelers in 12–14 storey buildings), RF wireless bridge (alignment/interference), optical; elevator contractors hesitant; third-party changes to traveling cable "void warranties and service contracts in most cases"; hoistway cables must be listed (type E). · Used: Q&A elevator question; Building specialists (towers); Equipment card.

### Keyword layers (five layers, for this silo)
- Service: apartment building security camera installation; building CCTV; lobby camera installation; NVR install; camera upgrade; footage retrieval.
- Problem: package theft; mailroom break-in; tailgating; broken lobby camera; blurry footage; trespassers in stairwells; furniture stolen from lobby.
- Technology: PoE IP cameras, NVR, turret/dome/bullet, PTZ, dual-lens, floodlight camera, video intercom, access control, elevator wireless bridge, fiber riser.
- Industry: co-op, condo, rental, managing agent, doorman building, walk-up, tenement, mixed-use, parking garage.
- Geographic (Manhattan only on this page): Manhattan, Upper West Side, Central Park West, Manhattan Valley, Washington Heights, Hudson Heights, Harlem, Lower East Side, Kips Bay, Stuyvesant Town, Greenwich Village/Hudson Square.

### Gathered while building the Queens page (2026-10-18)

### Google PAA / PASF / Answer the Public / Google AI Overview
- PAA for "apartment building security camera installation Queens NY" · Google · EMPTY (not accessible in build env — no live Google SERP surface; WebSearch returns links only).
- PASF · Google · EMPTY (not accessible in build env).
- Answer the Public · answerthepublic.com · EMPTY (not accessible in build env).
- Google AI Overview (SGE) · Google · EMPTY (not accessible in build env). The page's "AI Overview Reality Check" therefore quotes claims that appear verbatim in sources that DO surface for the same queries (aggregator cost pages, vendor blogs, tenant-rights explainer) and labels them as "the kind of answer AI summaries assemble", never as a captured AI Overview.

### Bing / DuckDuckGo-equivalent web search (WebSearch + Firecrawl search)
1. "apartment building security camera installation Queens NY" · WebSearch · results: thumbtack.com/ny/queens/home-security-camera-installers, swiftlane.com/cctv-camera-installation/ny/new-york/, thehabitatgroup.com/articles/2558, nyc.gov 282-14 (NYCHA camera program release), hometechnologyreview.com · finding: SERP is dominated by marketplaces (Thumbtack) and vendors, nothing Queens-building-specific · used: AI Reality Check H3 "marketplace" section (general characterization only).
2. "how much does it cost to install security cameras in an apartment building NYC" · WebSearch · https://www.handoff.ai/construction-costs/install-a-security-camera-system/bronx-ny (fetched) · finding: "$344.00/EA and $814.00/EA", average total $2,448 for a 4-camera sample (cameras $200 × 4, labor $140 × 8 hrs, 20% markup) · used: AI Reality Check "per-camera averages" H3 (quoted as an online estimator figure, then corrected).
3. same query · homeadvisor.com/tloc/South-Ozone-Park-NY/Surveillance-Cameras-Install-or-Repair/ · finding: HomeAdvisor publishes cost pages down to Queens neighborhood level (South Ozone Park) — excerpt only · used: AI Reality Check (named Angi/HomeAdvisor as aggregator sources).
4. "apartment building security camera installation cost per camera multifamily" · Firecrawl search · avigilon.com/blog/apartment-building-security-cameras (excerpt: "wireless security cameras for apartment buildings may offer lower initial installation costs by avoiding extensive cabling"), safehome.org/home-security-cameras/best/apartments/ (excerpt: SimpliSafe "Packages starting at $250.96", Nest "Pricing starts at $99.99") · used: AI Reality Check "wireless is cheaper" and "consumer kit" H3s.
5. "yelp security camera installer Queens 1 star..." · Firecrawl search · m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Queens%2C+NY (excerpt only: listing page "Rating 4.5 (883)"; individual 1–3★ review text not retrievable) · Yelp 1–3★ review text: EMPTY (not accessible in build env). Pain points used on the page are taken from Reddit/Habitat/Brick Underground items below, not Yelp.

### Reddit
6. "site:reddit.com Queens apartment packages stolen lobby cameras super" · Firecrawl search (excerpts; Reddit scrape blocked: "we do not support this site") ·
   - reddit.com/r/AskNYC/comments/vsg8yz/ · excerpt: "The only time my mid-size apartment building (in Queens) has had significant package theft was during last year's holiday season" · used: Neighborhood section (package theft seasonality, paraphrased, attributed to "a Queens resident on r/AskNYC").
   - reddit.com/r/NYCapartments/comments/1bjwldr/ · excerpt: "Landlord is saying that the security camera systems are down and that there is nothing they can do about a stolen package." · used: Q&A on recorder health checks / Neighborhood.
   - reddit.com/r/AskNYC/comments/ru521e/ · excerpt: tenants concluded "the super & building workers were the likely thieves" · used: Q&A on who controls footage access/audit log.
   - reddit.com/r/Brooklyn/comments/1ox1y84/ · excerpt: "We replaced our buildings intercom with one that has video to discourage folks looking to steal" · used: equipment section (video intercom as deterrent), attributed generically.
   - reddit.com/r/AskNYC/comments/1959k2t/ (Ring camera in apartment building) · excerpt: tenant deals with stolen packages · used: Q&A on tenants' own doorbell cameras.
   - full thread text: EMPTY (not accessible in build env).

### Trade / co-op press
7. "reddit Queens building package theft landlord won't install cameras" · WebSearch → https://habitatmag.com/Archive2/413-September-2023/Thwarting-Theft (fetched) · finding: property manager (Vikash Shingwani) with ~125 buildings "most of them in Queens"; ~20% full-time doormen, 10% part-time; package theft "a major issue" in part-time/non-doorman buildings; cameras outside, in vestibules, hallways; vestibule signs "This building is no-go. We're going to get you on camera."; doors surveyed for screwdriver-forceable locks and given lock plates; package cages under stairways; ButterflyMX lockers; deliveries left at back of lobby out of view of doorway · used: Neighborhood section, Q&A (package theft cluster), Field notes framing, Equipment (lock plates/latch guards cross-sell).
8. same search → https://www.brickunderground.com/rent/realty-bites-package-thief-landlord-security-camera (fetched) · finding: attorney Jennifer Rozen: landlord "isn't obligated to share surveillance footage" outside police request/court order; buildings are not required to have working cameras; attorney Catherine Grad on possible negligence if ongoing theft not reviewed; tenant association suggested · used: Q&A (footage requests), FAQ (tenant association asking landlord).
9. "NYC law security cameras residential building tenants landlord rules HPD" · WebSearch → https://tenant-rights.com/new-york/new-york-laws-on-security-cameras-in-building-common-areas (fetched) · finding: common-area cameras (hallways, lobbies, entryways, laundry rooms) generally allowed; none where reasonable expectation of privacy; no audio without consent; notice "should" be given though "not always strictly required" · used: Q&A on laundry room cameras + notices. NOTE: its "Local Law 3 of 2019" camera claim could not be verified → NOT used.

### Law / licensing (primary sources)
10. "New York State Department of State security and fire alarm installer license requirement" · WebSearch → https://dos.ny.gov/get-security-or-fire-alarm-installer-license (fetched) · finding: requires application + fee, age 18, fingerprints, "at least 81 hours of qualifying education", "Passage of an alarm installer examination"; page does not itself define whether CCTV is in scope · used: Q&A on who may install (stated carefully: AESS holds NYS license #12000287431; page describes DOS requirements only as listed).
11. https://ar.nyc-business.nyc.gov/nycbusiness/description/license-to-install-service-or-maintain-security-or-fire-alarm-systems · WebSearch result title only ("Security or Fire Alarm Systems, License to Install, Service or Maintain") · content: EMPTY (not fetched) · used: not used beyond noting the license exists at state level.
12. "Multiple Dwelling Law 50-a self-closing self-locking door intercom eight or more apartments" · WebSearch → https://www.nysenate.gov/legislation/laws/MDW/50-A (fetched) · finding: class A multiple dwellings erected/converted after Jan 1 1968 need automatic self-closing, self-locking entrance doors; 8+ apartments need voice intercom with door release from each apartment; pre-1968 buildings upgrade if tenants of a majority of apartments request in writing; no mention of CCTV · used: Q&A (garden co-op entrance doors + intercom), Commercial/compliance callout.
13. "New York Penal Law 250.05 eavesdropping..." · Firecrawl search → nysenate.gov/legislation/laws/PEN/250.00, codes.findlaw.com PEN 250.00 (excerpt: "Mechanical overhearing of a conversation" = recording a conversation "without the consent of at least one" party), law.justia.com 250.05 (excerpt: eavesdropping is a class E felony) · used: Q&A on audio in laundry rooms/lobbies; FAQ answer.
14. "Landmarks Preservation Commission rules security cameras historic district permit staff-level installation" · WebSearch → https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf (fetched) · finding: staff can approve camera permits meeting criteria; small residential bldgs max two cameras per 25 ft of street frontage, large residential max three per 25 ft; attach at mortar joints, plain masonry, wood or metalwork, not through cast iron or decorative surfaces; not on primary facade unless no other option; conduit concealed or max ~10 in. visible, painted to match; application via Portico with photos, elevations, cut sheets · used: Building Specialists (Jackson Heights HD / Sunnyside Gardens), Q&A landmark cluster, Process step.
15. https://www.nyc.gov/assets/lpc/downloads/pdf/pubs/ssg_manual_september_09.pdf (fetched) · finding: Sunnyside Gardens manual: Commission must approve in advance any alteration incl. "work on all facades"; light-fixture rules; does not mention cameras · used: Q&A (Sunnyside Gardens courts).

### Gathered while building the Staten Island page (2026-10-18)

### Google PAA / PASF / Answer the Public / Google AI Overview
- PAA for "apartment building security camera installation" · Google · — · EMPTY (not accessible in build env: no Google SERP surface available) · —
- PASF · Google · — · EMPTY (not accessible in build env) · —
- Answer the Public · answerthepublic.com · — · EMPTY (not accessible in build env) · —
- Google AI Overview · Google · — · EMPTY (not accessible in build env). The page's "AI Overview Reality Check" says plainly that the Overview could not be displayed and instead tests common search-answer / cost-guide assumptions, citing HomeAdvisor's published figures (below). · AI Overview Reality Check intro.
- Query `"people also ask" how much does it cost to install security cameras in an apartment building` · WebSearch · result list (handoff.ai, thumbtack, homeadvisor, bobvila, security.org) · Only cost-guide pages surfaced; no PAA box text. · used via HomeAdvisor entry below.

### Cost guides (feeds AI Overview Reality Check)
- `"people also ask" how much does it cost…` → WebFetch · HomeAdvisor · https://cost-guide-ssr.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera · National average $1,298; typical $593–$2,040; "$125 to $450 per camera, including labor"; outdoor cameras $20–$55 more to install; labor 50–70% of total; wireless cameras must be within Wi-Fi range. · AI Reality Check H3 1 and H3 2; Pricing "why web averages mislead".

### Law / rules (silo-wide, NY)
- `NYC law security cameras apartment building tenants landlord rules common areas` · WebSearch → WebFetch · tenant-rights.com · https://tenant-rights.com/new-york/new-york-laws-on-security-cameras-in-building-common-areas · "Cameras in public or common areas are generally permitted"; never where tenants have a reasonable expectation of privacy (apartments, bathrooms, locker rooms); landlords "must not record audio without consent"; NY one-party consent for audio; notice "builds trust, even if it is not always strictly required"; DHCR form RA-81 for rent-regulated privacy complaints. · Compliance callouts (§8.5); Q&A "audio"; FAQ.
- same search → WebFetch · Cooperator News Q&A "Camera Placement" · https://cooperatornews.com/article/qa-camera-placement · Six-unit condo where two owners put cameras outside their doors without the board; condos "typically prohibit unit owners from unilaterally altering… common areas"; board consent first; audio may implicate ECPA and NY Penal Law §250; cameras that see into a unit raise privacy issues; business judgment rule protects good-faith board decisions. · HOA/condo section; Q&A on owner-installed hallway cameras.
- `reddit statenisland security cameras landlord building package theft` · WebSearch → WebFetch · Brick Underground · https://www.brickunderground.com/rent/realty-bites-package-thief-landlord-security-camera · Attorney Jennifer Rozen: "your landlord isn't obligated to share surveillance footage with you"; must hand to police or under court order; city buildings aren't required to have working cameras; tenant association joint requests suggested. · Q&A on footage requests; small-landlord section.
- `New York State Department of State security alarm installer license requirement video surveillance` · WebSearch → WebFetch · NYS DOS · https://dos.ny.gov/system/files/documents/2024/05/security_0.pdf · 19 NYCRR §195.2(b)(1): license required for work on a "closed circuit television system (CCTV), or video surveillance system, if such system is used" for detecting/monitoring intrusion, break-in, theft, movement etc. (Article 6-D GBL). · Compliance callout; Q&A licence; AI Reality Check H3 7.
- same · NYS DOS · https://dos.ny.gov/get-security-or-fire-alarm-installer-license · Requirements: 18+, fingerprints, 81 hours qualifying education, exam. · Compliance callout.
- same · NYC Business · https://ar.nyc-business.nyc.gov/nycbusiness/description/license-to-install-service-or-maintain-security-or-fire-alarm-systems · Licence for NYC businesses is issued by NYS DOS (no separate city licence). · Compliance callout.
- same · iptechview (vendor) · https://iptechview.com/node/512 · vendor claim only; not used as authority. · not used.

### Outdoor / weather engineering
- `outdoor security camera salt air coastal corrosion stainless mount IP67 beach house` · WebSearch → WebFetch · Home Security Guide (readthedocs) · https://home-security-guide.readthedocs.io/en/latest/cctv/18-outdoor-cctv-camera-weatherproofing-guide/ · IP66 minimum, IP67 for unsheltered; "IP67 housing but an unsealed cable entry point has effective weather protection of zero"; salt air within ~5 miles of coast accelerates corrosion; 316 stainless rather than 304; dielectric grease, self-amalgamating tape; condensation the main winter problem; desiccant, anti-fog domes. · Weather/salt section; Equipment; Reality Check H3 4.

### Reddit
- `reddit r/statenisland security camera recommendations house` · WebSearch · (gummysearch aggregators only) · no r/statenisland thread returned · EMPTY.
- `site:reddit.com statenisland cameras building parking lot car break-ins` · Firecrawl search · https://www.reddit.com/r/statenisland/comments/1vlcn52/flock_cameras/ · excerpt only: resident questions Flock cameras at a store lot "if they already have cameras in the store, security guards, and police constantly parked in that lot". Full thread: scrape refused (site unsupported) → EMPTY (not accessible in build env) beyond excerpt. · Used only as context in LPR Q&A (no quote reproduced as resident testimony beyond the excerpt).

### Yelp 1–3★
- `yelp security camera installation Staten Island reviews never showed up` · Firecrawl search · https://www.yelp.com/search?find_desc=Cctv+System+Installation&find_loc=Staten+Island%2C+NY · only listing pages/excerpts; individual 1–3★ review text not reachable · EMPTY (not accessible in build env). Also surfaced Island Condo Management Corp listing rated 1.9 (17) — a management company, not an installer; not used.

### Bing / DuckDuckGo
- EMPTY (not accessible in build env — no Bing/DDG surface).

### Keywords — five layers (planned, placed naturally)
- Service: apartment building security camera installation; apartment security camera system; building CCTV installation; multi-family camera installation; condo complex cameras; landlord camera installation.
- Problem: package theft; car break-ins in parking lot; catalytic converter theft; vandalism; trespassing; dumping; cameras failing after storms; footage requests.
- Technology: PoE, NVR, Cat6, outdoor-rated cable, fiber/point-to-point wireless bridge between buildings, LPR, IR/colour night, IP66/IP67, 316 stainless, surge protection, UPS.
- Industry: small landlords, two-family owners, condo/HOA boards, property managers, mixed-use owners.
- Geographic: Staten Island; North Shore (St. George, Tompkinsville, Stapleton); Victory Blvd, Hylan Blvd, Richmond Ave, Bay Street, Forest Ave; South Shore (Annadale, Huguenot, Eltingville, Great Kills, Tottenville); East Shore (Midland Beach, Ocean Breeze, New Dorp Beach, Oakwood Beach).

### Silo pricing (existing AESS figures, not invented)
- Source: apartment-building-security-camera-installation-brooklyn.html and -nyc.html (current files on disk, 2026-10-18). Brooklyn base: $500–$1,500 per camera installed; Small walk-up 4–8 cameras $5,000–$12,000; Mid-size elevator 12–20 cameras $12,000–$25,000; Large 24–40 cameras $25,000–$45,000+; labor $75–$150/hr; cloud platforms $20–$80/camera/month (third-party, not multiplied).
- Applied Staten Island multiplier 1.10× (blueprint v2.3 §9): $550–$1,650 per camera; $5,500–$13,200; $13,200–$27,500; $27,500–$49,500+; labor $82.50–$165/hr. Service/callback $195/hr, 3-hr minimum ($585) per §9 (protected, not multiplied).

## Manhattan

### Local news / hyperlocal (package & lobby crime)
- `Manhattan package theft apartment building lobby mailroom 2025 2026` · WebSearch → https://pix11.com/news/local-news/manhattan/mailroom-burglar-ignores-warning-sign-strikes-same-building-3-times-in-a-week/amp/ · PIX11, May 17, 2017: basement mailroom near Central Park West & Manhattan Avenue (Manhattan Valley) hit three times in about a week (Apr 15, ~Apr 18, Apr 21); door forced with a card and shoulder; sign "Warning: Security cameras in use" ignored; manager added latch protectors and a steel inside door; NYPD released video. · Used: §5 Neighborhood; Q&A mailroom question; Field-notes context.
- same → https://www.cbsnews.com/amp/newyork/news/suspect-sought-in-upper-west-side-mail-room-thefts · CBS NY, May 17, 2017, same incident (card used to open mailroom door). · Used: corroboration, Sources.
- same → https://amny.com/news/thieving-duo-swipes-packages-manhattan-apartment-building · amNY, Nov 23, 2020: two people entered a building near Charlton St & Sixth Ave through a secured front door, took lobby packages Nov 9, 2020 ~9:30pm; NYPD released photos/video. · Used: §5; Q&A tailgating.
- `Upper West Side building package room theft camera West Side Rag` · WebSearch → https://www.westsiderag.com/2015/12/14/holiday-alert-tis-the-season-for-package-swiping · West Side Rag, Dec 14, 2015: 243 West 98th St, man let in by a resident, took packages; vestibule and foyer cameras caught him leaving. · Used: §5 facts list; Q&A buzz-in.
- same → https://www.westsiderag.com/2019/02/14/alleged-uws-package-thief-wishes-he-hadnt-opened-this-box · West Side Rag, Feb 14, 2019: 101 West 85th St lobby broken into three times Jan 30–Feb 6, 2019 by manipulating the front-door lock; mail-room packages incl. a laptop; 20th Precinct used a bait package. · Used: §5 facts list; Q&A front-door lock.
- same search → https://www.cbsnews.com/amp/newyork/news/furniture-stolen-harlem-apartment-building-lobby-robeson · CBS NY, Dec 21, 2023: four men on camera carrying a chair and couch out of the lobby of The Robeson on Lenox Avenue, Harlem, ~2:30am. · Used: §5 facts list; Commercial/corridors (Lenox).
- same search → https://villageview.nyc/2025/03/03/your-package-wasnt-stolen-it-was-mis-delivered/ · Village View (resident publication), Mar 3, 2025: superintendent says ~99% of the time footage shows a "stolen" package never reached the building; posts thief photos on the door; first holiday season with no packages taken. · Used: Q&A "is it really stolen" question; Reality Check H3 4.

### Building stock / neighborhoods
- `Washington Heights art deco apartment buildings Hudson Heights prewar elevator buildings history` · WebSearch → https://untappedcities.com/10-pre-war-apartment-house-gems-of-washington-heights · "one of New York City's great concentrations of pre-war apartment house buildings"; 1904 subway along Broadway triggered building boom; Beaux-Arts then Art Deco/Tudor between the wars; ground floors often altered; The Vauxhall, 780 Riverside Dr at W 155th (1914) in Audubon Park Historic District (designated 2009); Rio Grande/Rio Vista, 15 & 21 Fort Washington Ave (1912); The Ravenwood, Broadway & W 180th (1909). · Used: Building specialists (prewar elevator); Landmarks card; Q&A Washington Heights.
- `Lower East Side tenement buildings old law tenement 1879 1901 Tenement House Act dumbbell` · WebSearch → https://en.wikipedia.org/wiki/Old_Law_Tenement · Old Law (1879) dumbbell tenements on 25×100 ft lots, typically six storeys, four apartments per floor; narrow airshafts; superseded by the 1901 New Law; ~82,000 by 1900. · Used: Building specialists (walk-up tenement); Q&A LES; facts list.
- `Stuyvesant Town Peter Cooper Village number of apartments buildings security cameras` · WebSearch → https://en.wikipedia.org/wiki/Stuyvesant_Town%E2%80%93Peter_Cooper_Village · 11,250 apartments; 110 red-brick buildings / 110 street addresses; First Ave to Avenue C, 14th to 23rd St; first tenants Aug 1, 1947. · Used: Landmarks card; Building specialists (post-war complexes).
- `LPC historic districts Manhattan number of designated historic districts Upper West Side Central Park West historic district` · WebSearch → https://hdc.org/buildings/upper-west-sidecentral-park-west-historic-district/ · Designated April 24, 1990; storefronts, row houses, tenements, apartment towers; developed 1880s–1930s. · Used: §5; Landmarks card.
- same → https://en.wikipedia.org/wiki/Central_Park_West_Historic_District · San Remo (1930, 27 storeys, twin-towered), El Dorado (1931), Century (1931), Majestic (1930), Beresford (1929), Dakota (1884); NYC landmark designation April 24, 1990. · Used: Landmarks card (named as landmarks only; no claim of AESS work there).
- Wikipedia "Manhattan" article · WebFetch → **EMPTY (not accessible in build env — permission request timed out)**. No borough-wide population/housing statistics used.

### Facades, landmarks, permits
- `Landmarks Preservation Commission rules security cameras facade permit historic district` · WebSearch → https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf · LPC Permit Guidebook ch.11: equipment not on/in front of primary facade unless no other option; cameras "well spaced to avoid a cluttered, haphazard appearance"; per 25 ft of street frontage max two cameras (small residential/commercial) or three (large residential/commercial/institutional); attach at mortar joints, plain masonry, wood or metalwork, not through cast iron or decorative surfaces; finish to match; ~10 inches max visible conduit; staff-level permits available when criteria met. · Used: Building specialists (landmark facades); §8.5; Q&A LPC question; Reality Check H3.
- `NYC Local Law 11 FISP facade inspection sidewalk shed duration Manhattan buildings` · WebSearch → https://www.nyc.gov/site/buildings/safety/facade-local-law.page · Buildings taller than six storeys: exterior walls inspected every five years by a QEWI; sidewalk sheds installed when unsafe conditions found. · Used: Q&A sidewalk-shed question.
- Fire-stopping query `NYC Fire Code fire-stopping penetrations low voltage cable through rated floor riser building code 714` → results were spec documents (Columbia, DASNY) — used only for the general statement that penetrations through rated floors are fire-stopped; no specific code section cited on the page.

### Co-op/condo governance (Manhattan context)
- Habitat Board Talk "Cameras" (https://www.habitatmag.com/Board-Talk/Security-Camera-s/Cameras) and Habitat May 2013 "Creating a Safe House" — both concern **Queens** complexes (Forest Hills; Kew Village Estates) → **not used on the Manhattan page** (wrong geography).

## Pricing used (no invented prices) (Manhattan page)

Silo base (Brooklyn = 1.00×, from the silo's existing published tiers on -brooklyn/-nyc): per camera $500–$1,500; small walk-up 4–8 cams $5,000–$12,000; mid elevator 12–20 cams $12,000–$25,000; large/high-rise 24–40 cams $25,000–$45,000+; portfolio 50+ custom. Manhattan ×1.25 (v2.3 §9): per camera $625–$1,875; small $6,250–$15,000; mid $15,000–$31,250; large $31,250–$56,250+; portfolio custom. Protected service/callback rate $195/hr, 3-hr minimum ($585) (v2.3 §9) — not multiplied. Manhattan parking $150 per visit (AESS published Manhattan list: security-camera-pricing-manhattan.html, sonos-installation-tribeca-manhattan-ny.html).

## Queens

### Building stock and neighborhoods
16. "Jackson Heights Historic District garden apartments courtyards landmark" · WebSearch → https://hdc.org/borough/jackson-heights/ (fetched) · finding: designated October 19, 1993; built primarily 1914–1939; "the first and remains the largest garden-apartment community in the United States" · used: Neighborhood, Building Specialists, landmarks card.
17. "Jackson Heights Queensboro Corporation garden apartments 1917 interior gardens co-op history" · WebSearch → https://www.jhbg.org/history-of-jackson-heights (fetched) · findings: Queensboro Corporation (Edward A. MacDougall); 1914 Laurel Court first apartment building; 1917 elevated line on Roosevelt Ave + "Garden Apartments" (later Greystone) coined term "garden apartment"; interior gardens often the full length of a block; 1919 Linden Court first offered under Cooperative Ownership Plan; 1920–1925 eight block-long garden complexes; The Chateau (1923), The Towers (1924, 96 apartments); 1980s at least 60 buildings converted to co-ops/condos adding 5,000+ owner units; HD ≈36 blocks bounded by 76th St, 88th St, Roosevelt Ave, Northern Blvd · used: Neighborhood stats list, Building Specialists, Landmarks, Q&A.
18. Kew Gardens: http://6tocelebrate.org/wp-content/uploads/2023/03/Kew-Gardens_draft-03_web_s.pdf (Firecrawl) · findings: Kew Hall (1922) five-story steel-and-brick, half block, interior garden court, multiple entrances so only two apartments per landing — "This courtyard plan became a favorite among Kew Gardens developers throughout the 1920s"; Hampton Court mid-1930s four six-story Georgian Revival H-plan buildings, 316 apartments; Lefferts Blvd main commercial corridor after 1909 LIRR station; The Homestead mixed-use (stores below, apartments above); Kew Bolmer 120-10 Queens Blvd (1922-23) · used: Building Specialists (multiple-entrance courtyard buildings), Commercial corridors (Lefferts Blvd), Landmarks.
19. Forest Hills: https://www.habitatmag.com/.../Going-Up-How-a-Queens-Co-op-Finally-Got-Rid-of-Its-Scary-Old-Elevators (fetched) · finding: 76-66 Austin Street co-op — 98 units, six stories, built 1931; elevator modernization ~$330,000, nine weeks; swing hall doors replaced with automatic sliding doors · used: Q&A on elevator cab cameras (traveling cable coordinated with elevator contractor/modernization).
20. Rego Park: https://www.qchron.com/qboro/i_have_often_walked/rego-park-s-deluxe-apartments-in-the-sky/article_014a8e5c-... (fetched) · finding: Howard complex (Queens Blvd/102nd St/66th Rd/67th Ave), 1952, three 12-story buildings, developer Alfred Kaskel, architect Philip Birnbaum, 70% of site lawns/gardens/playgrounds, now a co-op; The Anita on 63rd Road: three buildings with "an additional story" beyond typical six · used: Building Specialists (mid-rise along Queens Blvd), Landmarks.
21. Rego Park Wikipedia scrape · Firecrawl · "information not on page" → EMPTY (not accessible in build env — query returned nothing usable).
22. Glen Oaks: https://www.glenoaksvillage.com/about (fetched) · finding: built 1947; 134 buildings; 2,904 garden-style apartments; 110 acres; co-op conversion 1981 · used: Neighborhood stats, Building Specialists (multi-building campus), Q&A (campus backbone).
23. Sunnyside Gardens: https://www.citylandnyc.org/sunnyside-gardens-designated-a-historic-district/ (fetched) · finding: LPC designated June 26, 2007 (LP-2258); ~600 buildings; 1920s; Clarence Stein and Henry Wright; large landscaped courtyards · used: Building Specialists, Landmarks, Q&A.
24. Long Island City: https://www.6sqft.com/?p=122732 (fetched; article March 14, 2016) · finding: 28 developments under construction/proposed; LIC Partnership projected 24,500 units; Court Square City View Tower (later renamed Skyline Tower) 774 units proposed; Queens Plaza Park 930 units proposed · used: Neighborhood, Building Specialists (new towers), Commercial.
25. LIC rentals: https://www.cityrealty.com/nyc/market-insight/rental-building-offers/long-island-city/long-island-city039s-top-30-luxury-rental-buildings/8502 (Firecrawl search excerpt) · finding: Link Apartments QPN 26 stories above Queensboro Plaza station with attended lobby; Aura LIC "keyless entry"; Aurora 29-11 Queens Plaza North, 132 apartments, includes a garage · used: Building Specialists (new-construction rentals: keyless entry, garages, amenity floors) — general only, no claims of AESS work.
26. Flushing: https://en.wikipedia.org/wiki/Flushing,_Queens (Firecrawl) · finding: Main St–Roosevelt Ave intersection "third-busiest in New York City"; ZIPs 11354/11355/11358; 109th Precinct; Tangram and Skyview Parc mixed-use · used: Commercial corridors, Landmarks, mixed-use building Q&A.
27. Languages: https://www.babbel.com/en/magazine/the-languages-of-queens-diversity-capital-of-the-world (fetched) · finding: "at least 138 languages" (attributed to Nonstop Metropolis atlas); 56.3% of residents 5+ spoke a language other than English at home (2015 Census) · used: Neighborhood stats list, Q&A on multilingual camera notices.
28. Housing-stock stat search · Firecrawl → chpcny.org Taking Stock (scraped): only "Half of all NYC's housing is found in Brooklyn and Queens" for Queens; 83% figure is Staten Island → used only the "half of all NYC housing in Brooklyn and Queens" line. Queens two-family share: EMPTY (no sourced figure found) → page describes two- and three-family homes qualitatively only.

### Local news / hyperlocal
29. "Queens package theft apartment building lobby vestibule news" · WebSearch → https://www.cbsnews.com/amp/newyork/news/queens-package-theif-caught-on-video/ (fetched) · finding: Astoria building near 36th Ave & 31st St, ~12:40 a.m. Nov. 30 (article Dec. 18, 2020); man "used a screwdriver to disable a lock on the door", took more than $400 in deliveries from the lobby; "seen on video" · used: Neighborhood section, Q&A vestibule cluster.
30. https://www.fox5ny.com/news/man-robs-mailroom-at-queens-apartment-building (fetched) · finding: Elmhurst, 73rd Street, just after 2 a.m. Sunday April 17, 2022; video shows man forcing lobby door with a screwdriver, took mail and packages from mailroom · used: Neighborhood, Q&A mailroom.
31. https://qns.com/2025/04/serial-burglar-hits-mail-rooms-in-five-queens-neighborhoods-nypd/ (Firecrawl; WebFetch blocked) · finding: April 16, 2025 (Bill Parry): serial burglar hit mail rooms in Jackson Heights (83-10 35th Ave, three times in March: March 8, four days later, March 14), Elmhurst, Flushing (Sanford Ave), Woodside (40-33 69th St), LIC (108th Pct); NYPD released surveillance image taken in the Jackson Heights building · used: Neighborhood, Q&A (mailroom repeat targets), AI Reality Check.
32. https://qns.com/2022/11/suspect-wanted-for-stealing-package-from-forest-hills-apartment-building-nypd/ (Firecrawl; WebFetch blocked) · finding: Nov. 4, 2022: near 67th Road & Booth Street, Forest Hills, Oct. 26 — suspect picked the lock of the outer door, then picked the lock of a large mailbox, took a package; police released video and images · used: Neighborhood, Q&A (outer door + mailbox camera angles).
33. https://www.qchron.com/editions/queenswide/mail-thieves-targeting-downtown-flushing/article_cd18ad8e-... (fetched) · finding: at least nine USPS relay boxes compromised in Flushing between Oct 1 and Nov 1 (year not stated); Postal Inspection Service: reports "specially in 11358 ZIP code"; no mention of cameras · used: Commercial/Flushing paragraph (street mail theft context; we do not claim cameras on USPS boxes).
34. "Queens apartment parking lot car break-ins garden complex cameras co-op board" · Firecrawl search → https://pix11.com/news/local-news/car-break-ins-spark-fear-among-rego-park-residents/ (scraped) · finding: Sept 4, 2026: string of car break-ins along 62nd Drive, Rego Park, surveillance video shows people breaking into vehicles; resident quote "They come multiple times, it's unbelievable" · used: Neighborhood, Q&A (parking lot / curbside cameras).
35. https://queenspost.com/man-broke-into-astoria-apartment-building-and-stole-multiple-packages-police → redirect to qns.com; WebFetch blocked → EMPTY (not accessible in build env).
36. "Queens Chronicle apartment building security cameras tenants burglary laundry room" · WebSearch · results all out-of-area (WeHo, Seattle, Cincinnati) → Queens laundry-room news: EMPTY.
37. "Flushing Main Street mixed-use buildings..." · WebSearch → newyorkyimby.com 42-76 Main Street seven-story mixed-use (title only) · used: mixed-use mention only in general terms.
38. NYC.gov 282-14 (de Blasio / NYCHA camera program) · WebSearch title only · not fetched → not used.

### Local Reddit
- r/Queens / r/astoria / r/jacksonheights specific threads on building cameras: EMPTY (Reddit not scrapeable; search surfaced only r/AskNYC & r/NYCapartments items above).

### Pricing
- Silo base (existing Brooklyn page, apartment-building-security-camera-installation-brooklyn.html, read from repo): Small walk-up 4–8 cameras $5,000–$12,000; Mid-size elevator 12–20 cameras $12,000–$25,000; Large/high-rise 24–40 cameras $25,000–$45,000+; all-in $500–$1,500 per camera.
- Queens ×1.05 (blueprint v2.3 §9): $5,250–$12,600; $12,600–$26,250; $26,250–$47,250+; $525–$1,575 per camera.
- Service/callback rate verbatim per §9: $195/hr, 3-hr minimum ($585) — not multiplied (protected).

### Keywords (five layers)
- Service: apartment building security camera installation, building CCTV, co-op camera system, NVR install, camera upgrade.
- Problem: package theft, mailroom break-in, vestibule door forced, laundry room theft, parking lot car break-ins, courtyard trespass, blind spots.
- Technology: PoE IP cameras, NVR, fiber/Cat6 backbone between buildings, video intercom, latch guards, mailbox camera angle, retention days.
- Industry: co-op boards, condo boards, managing agents, landlords of rent-stabilized buildings, two-/three-family owners, new-construction rental managers.
- Geographic: Queens, Jackson Heights, Forest Hills, Rego Park, Kew Gardens, Long Island City, Astoria, Flushing, Elmhurst, Woodside, Sunnyside Gardens, Glen Oaks, Queens Boulevard, Roosevelt Avenue, 35th Avenue, Lefferts Boulevard, Main Street.

## Staten Island

### Building stock
- `Staten Island housing stock two-family homes share of housing units low-rise` · WebSearch → WebFetch · Prodigy RE · https://prodigyre.com/blog/the-two-family-wealth-engine-how-staten-islands-most-common-home-type-built-middle-class-wealth · "Eighty-three percent of Staten Island's housing units sit inside one- or two-family buildings"; two-family stock concentrated South Shore / Mid-Island; configurations: Great Kills up-and-down high-ranches, New Dorp/Dongan Hills side-by-side semi-attached, Charleston/Rossville newer semi-attached, North Shore (St. George, Stapleton) older detached and converted Victorians, investor-heavy; R3/R3X zoning allows two-family attached/semi/detached. · §5 Neighborhood; facts list; Building Specialists.
- `Staten Island condo association security cameras Hylan Boulevard Richmond Avenue townhouse complex` · Firecrawl search → scrape · Nacmias Law · https://nacmiaslaw.com/practice-areas/closings/building-types/townhouse-condo-declaration/staten-island · Staten Island holds more low-rise condo units than any other borough, almost all planned attached townhouse communities (Annadale, Huguenot, Eltingville); one declaration covers a community; association often owns roads, parking, drainage, grounds; East Shore flood requirements affect alterations. · §5 facts; HOA section; Building Specialists; Q&A.
- `Staten Island garden apartment complexes South Shore…` · WebSearch · listing sites only · not used.

### North Shore development
- `Staten Island housing stock…` (same search) → WebFetch · Commercial Observer (Jan 2026) · https://commercialobserver.com/2026/01/staten-island-multifamily-development-2026/ · Lighthouse Point (St. George) 115 units; The Pearl, 475 Bay Street, Stapleton, 100% affordable, opened Nov 2025, first project under Bay Street Corridor plan; Urby at 7 Navy Pier Court; rezonings 1987–2003 cut areas where apartments could be built; Stuart Saft quote "the zoning on Staten Island makes it virtually impossible to build multifamily housing"; pipeline: SI 1,238 units end-2024 vs Brooklyn 40,247; average SI rent Q4 2025 $1,909 (CoStar). · §5; Landmarks (St. George); facts list.
- `Bay Street Corridor rezoning Stapleton Tompkinsville St. George apartments approved 2019` · WebSearch → WebFetch · City Limits · https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ · Council approved June 26, 2019 (44–2); 20 blocks of North Shore; ~1,800 new units incl. 1,300 income-targeted; Stapleton and Tompkinsville. · §5; Commercial corridors (Bay Street).

### Borough facts
- Firecrawl scrape · Wikipedia · https://en.wikipedia.org/wiki/Staten_Island · Population 495,747 (2020); 58.5 sq mi; least densely populated, most suburban borough; North Shore (St. George, Tompkinsville, Clifton, Stapleton) most urban, with St. George and St. Paul's Avenue–Stapleton Heights historic districts of large Victorian houses; East Shore FDR Boardwalk 2½ miles; South Shore developed rapidly from 1960s–70s; Staten Island Railway St. George–Tottenville; only borough not on subway; ferry from St. George; 12,300 acres protected parkland; Fresh Kills; Hylan Boulevard the longest street in NYC; neighborhood lists by shore. · §5; landmarks; facts; corridors. (WebFetch of the same URL was blocked: PROVENANCE_REQUIRED — Firecrawl used instead.)

### Storm / flood
- `Hurricane Sandy Staten Island flooding Midland Beach Oakwood Beach New Dorp Beach…` · WebSearch → WebFetch · NYC SIRR · https://www.nyc.gov/site/sirr/rebuilding/east-and-south-shore-staten-island.page · 23 storm-related deaths on SI, all but one on East and South Shores; 11,700+ buildings in inundated areas; 1- and 2-family homes = 90% of area buildings, 84% of housing units; East Shore low elevation; South Shore bluffs eroded, surge up creeks; Hylan Blvd and SIR affected. · Weather/flood section; facts; Q&A flood.
- same · WNYC · https://wnyc.org/story/271288-tricked-topography-how-staten-island-neighborhood-became-so-dangerous-during-sandy/ · Square mile bounded by Midland Ave, Father Capodanno Blvd, Seaview Ave, Hylan Blvd (Midland Beach, Ocean Breeze, part of Dongan Hills) — deadliest place in NYC that night; streets several feet below Father Capodanno Blvd ("a bowl"); ~11 drowned. · Flood section.
- `Staten Island coastal flood zone FEMA flood maps … Appendix G…` · Firecrawl search · UpCodes NYC BC 2022 Appendix G · https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction · Mechanical equipment and outside appliances elevated to or above design flood elevation; electrical wiring permitted below DFE if it conforms to NYC Electrical Code; DFE = BFE + 2 ft (many classes). · Flood section (recorder placement), compliance callout.
- same · Rebuild by Design "NYC's Floodplain by the Numbers" · https://rebuildbydesign.org/wp-content/uploads/2022/03/floodplain-by-numbers.pdf · Staten Island Build It Back: 5,900 detached, 4,100 semi-detached, 1,200 attached; New Dorp Beach and Oakwood Beach pictured. · Flood section.

### Local news / crime context
- `SILive Staten Island surveillance cameras installed parking lot thefts catalytic converter` · WebSearch → WebFetch · CBS New York · https://www.cbsnews.com/newyork/news/staten-island-catalytic-converter-theft-prevention · July 15, 2022 event in Graniteville by police auto crime unit; more than 250 catalytic converter thefts on SI that year to date; ~200 attended etching. · Parking-lot section; facts list.
- `Staten Island Advance silive package thefts apartment building surveillance video NYPD 120th precinct` · Firecrawl search → scrape · SILive (Aug 7, 2025) · https://www.silive.com/crime-safety/2025/08/we-have-cameras-and-still-homeowner-decries-package-thefts-on-staten-island.html · Elm Park homeowner had porch theft on camera (Morningstar Rd / Dixon Ave area, Aug 2, 2025); found it two days later because of a notification issue; "More and more Staten Islanders are using locked options to receive packages." · §5; Q&A on alerts; Reality Check H3.
- same search · Facebook excerpt (SI Advance) · DA McMahon: 126 vehicles reported stolen from the 123rd Precinct in 2022, up from 65 in 2021 · excerpt only — used with "excerpt" label in sources. · Parking section.

### Local licensing / permits
- NYS DOS licence (above) applies on Staten Island; no separate NYC DCWP installer licence found (NYC Business page routes to NYS DOS). · Compliance.
- Hyperlocal (SI Advance via Firecrawl excerpts) used above; Patch/News12 Staten Island — not searched separately → EMPTY.

## Suffolk County

Local research for apartment-building-security-camera-installation-suffolk-county (2026-10-18). Silo-wide findings (cost guides, NYS DOS licence, privacy/audio, FirstService retention, salt-air weatherproofing guide) are reused from research/apartment-building-security-camera-installation.md and not repeated here. Format: exact query · platform · URL · finding · page+section used.

### Unreachable surfaces (local)
- Google PAA / PASF / Answer the Public / Google AI Overview for "apartment building security cameras Suffolk County" · EMPTY (not accessible in build env — no live Google SERP surface). Reality Check says so and tests aggregator claims instead.
- Bing / DuckDuckGo · EMPTY (not accessible in build env).
- Yelp 1–3★ Suffolk installers · not searched separately; individual review text not reachable in this env (silo precedent) · EMPTY (not accessible in build env).
- Newsday article bodies · paywalled · EMPTY (not accessible in build env); only Newsday headlines surfaced via Facebook excerpts — not used.
- Reddit full thread text · EMPTY (not accessible in build env); search excerpts only.

### Licensing / jurisdiction
1. `Suffolk County Consumer Affairs security alarm systems installer license low voltage Chapter 563` · Firecrawl search · https://ecode360.com/14947319 · Chapter 563 "Licensed Occupations", adopted 7-9-1974 (L.L. 21-1974). Article list not returned by scrape. · Compliance callouts; Sources.
2. `Suffolk County electrician license "low voltage" OR "security systems" ...` · Firecrawl search + scrape · https://ecode360.com/14948079 · Ch. 563 Art. XI "Electricians and Plumbers": "electrical field" = installation/maintenance of wire, cable … equipment which "generates, transforms, transmits or uses electrical energy for light, heat, power or other purposes"; no mention of low-voltage, alarm, signal, or TV wiring; applicability clause: "This article shall not be applicable within any town or village which has hereinbefore enacted legislation regulating the licensing of business, trade or enterprise …" (town/village carve-out). · §8.5 compliance; Q&A on county vs town licensing; Reality Check H3.
3. same · Firecrawl scrape · https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License · Licence types listed: Home Improvement, Master Electrician, Restricted Electrical, Electrical Inspector, Sign Hanger, etc. — no low-voltage, security, alarm or camera licence on the list. Verification phone (631) 853-4600 shown (not used on page). · §8.5; Q&A; Reality Check.
4. NYS DOS Article 6-D / 19 NYCRR 195.2(b)(1) CCTV coverage — reused from silo file (Staten Island section). · §8.5.

### Building stock / development
5. `Suffolk County transit-oriented apartments LIRR Ronkonkoma Hub Wyandanch Rising Patchogue downtown apartments units` · Firecrawl search + scrape · https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more · Oct 22, 2024: Station Yards (Ronkonkoma Hub), 53 acres, $1.2 billion, "more than 1,400 housing units" (1,450 cap), first phase 489 residential units, more than 1,200 parking spaces; Ronkonkoma "Suffolk County's busiest and Long Island's second-busiest" LIRR station, 17,000 daily commuters. · §5; §7 TOD card; Landmarks; Q&A.
6. same search · https://lirpc.org/economic-development/wyandanch-rising-models-transit-oriented-development/ (excerpt) · Wyandanch Rising: 177 residential units incl. 123 affordable; https://thenyhc.org/projects/wyandanch-village-wyandanch-rising/ (excerpt): new LIRR station house and 500-car MTA commuter parking garage, park with ice rink. · §7; Landmarks.
7. same search · https://www.suffolkcountyny.gov/Portals/0/formsdocs/planning/scplanningcommission/2020/BR-20-06%20%20Ronkonkoma%20Hub%20Phase%202A.pdf (excerpt) · Planning Commission: Hub total not to exceed 1,450 units; abuts Railroad Ave and the station. · corroboration only.
8. `Patchogue village downtown apartments ...` · Firecrawl search · https://tritecre.com/project/new-village/ (excerpt) · New Village at Patchogue on Main Street; "a total of 714 multi-family units were added to Patchogue". · §5 facts; §8 corridor; Landmarks.
9. same · https://www.governor.ny.gov/news/governor-hochul-announces-groundbreaking-160-million-carriage-house-development-downtown (excerpt) · Carriage House, $160 million, 262 units on W. Main St., two buildings (108 units occupancy spring 2027; 154 units fall 2027), ground-floor retail, more than 400 structured parking spaces. · §5; §8; Q&A garage.
10. same · https://www.artspace.org/patchogue (excerpt) · Artspace Patchogue Lofts: 45 affordable live/work units with commercial space. · §8.
11. `Riverhead downtown Main Street apartments mixed-use ...` · Firecrawl search · https://www.townofriverheadny.gov/DocumentCenter/View/1037/... (excerpt) · Woolworth Apartments, 128 East Main St: 19 units; Riverpoint Apartments, 821 East Main St: 134 units. https://riverheadlocal.com/2015/02/01/move-day-new-woolworth-apartments-downtown-riverhead/ (excerpt): move-in Feb 2015, mixed-use building. · §8 corridor; Landmarks; Q&A.
12. `Bay Shore Main Street downtown apartments ...` · Firecrawl search · https://greenviewny.com/apartments-category/urban-and-garden-style-living/ (excerpt) · renovated mixed-use building on Main Street, downtown Bay Shore, 26 rental apartments. https://greaterlongisland.com/plan-for-apartments-restaurant-at-closed-islip-cinemas-inches-forward/ (excerpt): Islip Cinemas, 410 Main Street → 23 apartments + restaurant (proposal). · §8.
13. `Long Island multifamily housing share ...` · Firecrawl search · https://rpa.org/work/reports/long-islands-rental-housing-crisis (excerpt) · Long Island rental vacancy 4.3%, lowest of suburban areas in NY region. https://www.sjny.edu/files/images/mapping-long-islands-rentals-2016-li-index.pdf (excerpt): Long Island Index mapped 1,456 rental buildings and 882 co-ops and condos across both counties. https://rauchfoundation.org/... (excerpt): "Long Island contains 809,000 single-family detached" homes. · §5.5 facts.

### Accessory apartments / seasonal rentals
14. `Suffolk County accessory apartment law town permit ...` · Firecrawl search · https://www.townofbabylonny.gov/faq.aspx?TID=50 (official, excerpt) · Babylon accessory apartment permit: dwelling owner-occupied and primary residence; off-street parking for four cars. https://ecode360.com/7707363 (Islip Art. XLVII, §68-603 owner occupancy required, excerpt). https://www.huntingtonny.gov/accessory-apartments (Accessory Apartment Bureau exists). Secondary (contractor blog, alecsconstructionli.com) claims about Brookhaven §85-258 one-bedroom limit and Huntington one-year renewals — NOT used (not primary). · §7 accessory card; Q&A accessory apartment.
15. `East Hampton OR Southampton rental registry law ...` · Firecrawl search · https://www.ehamptonny.gov/DocumentCenter/View/1342/... (official excerpt) · East Hampton Town: owners renting by week, month, season or year must register with the Town. https://ecode360.com/30841753 (Ch. 199 Rental Registry). https://easthamptonvillage.gov/documents/rental-registry/ (official excerpt): registry form for Village rentals under 120 days; rentals under two weeks not permitted. Southampton Town Ch. 270 rental permit (via secondary bnbcalc excerpt citing ecode360.com/8697294) — mentioned only as "rental permit chapter" without fee figures. · §7 seasonal card; Q&A seasonal.

### Local news / crime / cameras
16. `Suffolk County 55 and over community condo security cameras clubhouse pool mailbox theft TBR News Media OR Patch` · Firecrawl search + scrape · https://patch.com/new-york/longisland/6-750-checks-stolen-suffolk-mailboxes-4-8m-scheme-da · Patch, July 8, 2026: Suffolk DA — three people charged; 6,750 checks, $4.8 million; "fishing" device (glue trap on a belt) at USPS collection boxes in Melville, Huntington Station, East Northport, Commack, Smithtown, St. James, Nesconset, Hauppauge, Centereach, Holbrook, Bohemia, Farmingville, Brentwood, Medford, Patchogue, Blue Point, Bayport, Sayville, West Sayville and Oakdale. · §5; Q&A mailbox kiosk; Reality Check.
17. same search · https://longisland.news12.com/2026/07/09/many-long-island-post-offices-lack-outdoor-surveillance-cameras-despite-mail-theft-issues/... (title/excerpt) · News 12, July 9, 2026: many Long Island post offices lack outdoor surveillance cameras despite mail theft. · §5 facts.
18. same search · https://nypost.com/2026/10/04/us-news/suffolk-county-more-than-doubles-number-of-big-brother-flock-cameras-in-past-year/ · NY Post, Oct 4, 2026: county-operated Flock plate cameras rose from 25 to about 60; 35 bought with $542,500 state grant approved Aug 2025, 16 on the East End (Southampton, Riverhead, Southold, Route 114 Sag Harbor, East Hampton Village, near LIE Exit 71); "hundreds more" via towns, villages and "even private living communities". · Q&A gate/plate camera; Reality Check.
19. `site:reddit.com r/longisland apartment complex cameras car break in OR package stolen Suffolk` · Firecrawl search (excerpts only) · https://www.reddit.com/r/longisland/comments/18yebx6/patchogue_village_hit_with_car_break_ins/ (excerpt: car on a driveway broken into, Democratic Hill area, police with lights); https://www.reddit.com/r/longisland/comments/1en242v/catalytic_converter_stolen/ (excerpt: poster says police told them thieves used a signal jammer to block the WiFi from Ring cameras); https://www.reddit.com/r/longisland/comments/1vduoms/flock_camera_megathread/ (megathread exists). Full threads EMPTY (not accessible in build env). · §5 (attributed as r/longisland posts, paraphrased); Q&A on wired vs Wi-Fi; Reality Check H3 wireless.
20. `Suffolk County garden apartment complex security cameras parking lot car break-ins Newsday` · Firecrawl search · only out-of-area results (Rochester, Suffolk VA, Maryland) and a SCPD Facebook "lock your car" reminder excerpt · EMPTY for Suffolk NY apartment-complex incidents. Not used (Suffolk, VA results explicitly excluded).

### Storm / coastal exposure
21. `Superstorm Sandy Suffolk County damage Lindenhurst Mastic Beach ...` · Firecrawl search · https://www.suffolkcountyny.gov/mend/index.html (official excerpt) · Sandy: "16' Storm Surge on Fire Island; Over 31,000 homes flooded"; https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York (excerpt): mandatory evacuations for Fire Island and surge zones in Babylon, Brookhaven, Islip, Riverhead, Southampton, Southold; coastal damage heaviest in Mastic and Moriches. · Weather section; Q&A recorder placement on the bay side.

### Pricing used
Silo Brooklyn base (research file "Silo pricing") × 1.20 (v2.3 §9 Suffolk): per camera $600–$1,800; small 4–8 cams $6,000–$14,400; mid 12–20 cams $14,400–$30,000; large 24–40 cams $30,000–$54,000+; campus/portfolio custom. Service $195/hr, 3-hr min ($585) — not multiplied.

## Westchester County

Page: apartment-building-security-camera-installation-westchester-county (REBUILD in place, 2026-10-18). Silo-wide findings reused from research/apartment-building-security-camera-installation.md (NYS DOS 19 NYCRR 195.2, tenant-rights.com, Cooperator, FirstService 30–90 days, Brick Underground, Penal Law 250, IPVM elevator, Angi/HomeAdvisor, weatherproofing guide). Only Westchester-local research below. Format: exact query · platform · URL · finding · page+section used.

### Surfaces not reachable
- Google PAA / PASF / Answer the Public / Google AI Overview / Bing-DDG autocomplete · EMPTY (not accessible in build env). Reality Check says so on the page and tests aggregator claims instead.
- Reddit full threads (r/Westchester, r/yonkers) · EMPTY (not accessible in build env) beyond search excerpts. Query `site:reddit.com r/Westchester apartment building packages stolen landlord cameras` · Firecrawl search · no r/Westchester/r/yonkers apartment-camera thread returned → EMPTY.
- Yelp 1–3★ Westchester installers · not searched separately; EMPTY (not accessible in build env per silo note).
- lohud articles are paywalled ("content_tier locked"): only search-result excerpts used, labelled "(excerpt)" in Sources.

### Licensing / permits
1. `Westchester County Department of Consumer Protection home improvement license security camera installer requirement` · Firecrawl search → scrape · https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors · county licence required for home-improvement contractors; DCP phone (914) 995-2155; links to licensing law · §"Who Signs Off" (county code), Q&A licence cluster.
2. Firecrawl scrape (query) · https://library.municode.com/ny/westchester_county/codes/code_of_ordinances?nodeId=PTVIIRUREDEENFA_CH863COPRCO_ARTXVILIPEENHOIMBU · Ch. 863 Art. XVI: "home improvement" = work on a private residence, townhouse, condominium, apartment or dwelling "of not more than three units"; excludes electrical work and alarm work "by a county-licensed alarm business or alarm agent" · Neighborhood facts list, Who Signs Off, Q&A "40-unit Yonkers".
3. `"Westchester County" "alarm business" license Chapter 863 ...` · Firecrawl search → scrape · https://ecode360.com/7692228 (Town of Cortlandt Ch. 113) · county alarm business/agent licence under Ch. 863 Art. XV for "installing and/or servicing police or fire alarm devices"; local alarm permit from Director of Code Enforcement, issued only if installer is an alarm licensee · Who Signs Off (alarm permits), Q&A New Rochelle alarm licence, Q&A Croton fire-panel permit.
4. Municode Art. XV node scrape · EMPTY (page returned no text). Camera-only scope NOT stated in any text reached → page tells boards to ask DCP.
5. Same search · https://www.lowvoltagenation.com/posts/westchester-county-new-york-security-camera-permit-requirements · claims a "Westchester County Low Voltage License" and alarm permits for monitored camera systems · NOT verified on county site → used only as a tested claim in AI Reality Check H3 3 ("could not find").

### Rent regulation / tenants
6. `Emergency Tenant Protection Act Westchester municipalities opted in ...` · Firecrawl search → scrape · https://homes.westchestercountyny.gov/rent-control · 18 ETPA municipalities with minimum units (Croton 6, Dobbs Ferry 6, Eastchester 6, Greenburgh 6, Harrison 6, Hastings 6, Irvington 20, Larchmont 6, Mamaroneck Town 6, Mount Kisco 16, Mount Vernon 6, New Rochelle 6, Pleasantville 20, Port Chester 12, Sleepy Hollow 10, Tarrytown 6, White Plains 6, Yonkers 6); rent-control municipalities; ORA White Plains office (914) 948-4434 · Neighborhood para 4 + facts, rent-stabilized section, Q&A cluster 2, Reality Check H3 4.
7. same search · https://hcr.ny.gov/fact-sheet-8 (excerpt) · ETPA Westchester localities; Westchester rent office 75 South Broadway, White Plains · Sources.
8. same search → scrape · https://www.villageofossiningny.gov/planning-department/pages/faqs-etpa · ETPA only for buildings built before 1974 with six or more units; if Ossining adopted, ≥1,200 units potentially covered · facts list, intro "built before 1974".
9. `Mount Vernon NY apartment building ... lohud` · Firecrawl search → scrape · https://homes.westchestercountyny.gov/code-enforcement-tenants · tenants may call local building inspector for "broken doors, windows elevators, locks and mail boxes"; RPL §235-b warranty of habitability quoted · Q&A Mount Vernon lock, rent-stabilized section.

### Co-op boards
10. `Westchester County co-ops ... lohud` · Firecrawl search → scrape · https://humanrights.westchestercountyny.gov/resources/cooperative-housing-disclosure · §700.21-a (eff. Aug 1, 2021): acknowledge application within 15 days, decide within 60; 2 hours fair-housing training every 2 years · facts list, Who Signs Off, board packet section.
11. same search · https://www.reddit.com/r/Westchester/comments/1k56tsp/thoughts_on_coops/ (excerpt) · poster bought two co-ops in Hartsdale, "a pain to apply to" but positive · Garden Complexes section.
12. same search · lohud 2020 co-op rejections (excerpt) · not used.

### Local incidents / hyperlocal
13. `Yonkers apartment building package theft lobby surveillance video police` · Firecrawl search → scrape · https://abc7ny.com/post/yonkers-package-theft-woman-santa-hat-2-masked-men-accused-stealing-packages-ny/15614198/ · Dec 2, 2024: Nov 23 ~9am, packages taken from lobby of 345 Bronx River Road, Yonkers; three arrested (petit larceny, possession of stolen property, burglary tools); Lt. Ken Lacey: "The sooner we get the information, the sooner we can react…" · Neighborhood para 2, Reality Check H3 5. (Suspect names not used.)
14. same search → scrape · https://yonkerstimes.com/porch-pirates-moved-indoors-how-yonkers-apartment-buildings-are-rethinking-package-rooms/ · Oct 16, 2026 (note: reads partly as sponsored content linking a parcel-software vendor): theft "moved indoors"; Yonkers mix of older walk-ups, prewar and waterfront developments; some older buildings have no package room; "Footage can show someone entering a room, but without delivery records…" · Neighborhood para 3, Package Rooms section, Reality Check H3 5.
15. `White Plains apartment building lobby burglary mailroom surveillance video police Patch` · Firecrawl search · results were house burglary / business burglary / suspicious device — no apartment-camera incident · EMPTY for White Plains apartment incidents.

### Building stock / development
16. `New Rochelle downtown apartment towers ... lohud` · Firecrawl search (excerpts) · lohud May 3, 2023: 14 apartment buildings since 2018 added 2,456 units; 12 under construction (2,677); lohud Apr 25, 2025: >10,500 rental units and 500 condos authorized in a decade; Governor's release: Highgarden Tower 219 affordable units · Neighborhood facts, Commercial (New Rochelle), Landmarks. lohud full text: EMPTY (paywall).
17. https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster · scrape returned only navigation → EMPTY (search excerpt: up to 6,370 housing units permitted — not used).
18. `Yonkers waterfront downtown apartment towers ... Larkin Plaza` · Firecrawl search (excerpts) · Multi-Housing News: Larkin Plaza 439 units in 25- and 17-storey buildings (RXR); Mayor's FB post re Hudson Piers 250 apartments (not used — social post) · Neighborhood, Commercial, Landmarks.
19. `White Plains downtown apartment towers near Metro-North ...` · Firecrawl search (excerpts) · GDC: The Metro at City Square, 34 South Lexington Ave, directly across from Metro-North station; WPBID: 25 North Lex 500-unit residence near station · Commercial, Landmarks.
20. `Peekskill downtown apartment buildings ...` · Firecrawl search (excerpts) · NYHC/HCR: Lofts on Main, $28M, 75 apartments in two four-storey buildings, downtown arts district · Commercial, Landmarks.
21. `Bronxville co-op apartment buildings prewar Lawrence Park ...` · Firecrawl search → PDF scrape · https://www.villageofbronxville.gov/DocumentCenter/View/243/An-Illustrated-History-of-Bronxville-PDF · 1910s suburban apartment buildings by W. V. Lawrence (Gramatan Court, Alger Court), apartments above shops, Kensington Terrace first town houses in county; one square mile; granite outcroppings; Lawrence Park National Historic District; Tuckahoe marble found 1822; Pondfield Road/Kraft Ave retail district · Neighborhood para 5, Building Specialists (rock), Q&A Lawrence Park garage, Landmarks.
22. `Hartsdale co-ops garden apartment complexes ...` · Firecrawl search · listing sites only (Hartsdale Gardens etc.) · used only qualitatively ("dozens of co-op listings at any time" — based on Zillow 33 / Homes.com 23 / Compass 18 listing excerpts).

### Aggregator cost claims (Reality Check)
23. `security camera installation cost Yonkers OR "White Plains" NY homeadvisor OR angi OR thumbtack` · Firecrawl search (excerpt) · https://www.thumbtack.com/ny/yonkers/security-camera-install · "$100 for a single-camera line installation to $1,000-$2,200 for an entire system"; Angi NY $1,509 ($797–$2,222) · Reality Check H3 1.

### Pricing used
Brooklyn base (research file "Silo pricing") × 1.25: per camera $625–$1,875; 4–8 cams $6,250–$15,000; 12–20 cams $15,000–$31,250; 24–40 cams $31,250–$56,250+; portfolio custom. Service $195/hr, 3-hr min ($585), not multiplied. No parking/travel line (none published for Westchester).

## Question register

Every question (Q&A headings and FAQ) used on any rebuilt page of this silo. New pages must not repeat any of these (geo names are masked by the duplicate check).

### apartment-building-security-camera-installation-manhattan

### Q&A headings (§9 "Questions Answered", H3)
1. What does a Manhattan managing agent usually ask for before a camera contractor can start work in the building? — §9
2. Our co-op's alteration agreement says work only 9 to 5 on weekdays — can a lobby camera job fit inside that window? — §9
3. How do we check that a camera installer's certificate of insurance is real before the super lets them in? — §9
4. Does a condo board vote need to happen before cameras go into common hallways, or can the managing agent approve it? — §9
5. How do you get camera cable from a basement recorder to the upper floors of a prewar Upper West Side elevator building with no spare conduit? — §9
6. Can a six-storey Lower East Side walk-up tenement with no elevator be wired for hallway cameras without surface raceway on every landing? — §9
7. Will drilling through the brick and terra-cotta floors of a Washington Heights apartment house need fire-stopping? — §9
8. Where should the recorder live when a building's only closet space is the super's office and the boiler room? — §9
9. Which camera angles actually identify someone who forces the mailroom door with a card, like the Manhattan Valley break-ins? — §9
10. How should cameras be set up at a doorman desk so the overnight attendant can watch the door and the package room together? — §9
11. Can the vestibule camera record who a resident buzzes in, so a tailgater can be traced after a package goes missing? — §9
12. Is a locked package room with one camera enough, or do Manhattan buildings need a camera on the delivery hand-off too? — §9
13. How does video get out of a moving elevator cab in a 20-storey Manhattan tower without touching the traveling cable? — §9
14. What cameras work in an underground residential garage with a ramp onto a Manhattan side street? — §9
15. Can cameras go on the roof bulkhead to watch roof doors and terraces? — §9
16. Does a camera over the entrance of a building in a landmark district need an LPC permit? — §9
17. Our building is wrapped in a Local Law 11 sidewalk shed — where do the entrance cameras go until it comes down? — §9
18. Who in a co-op should be allowed to pull footage, and how should requests be logged? — §9
19. A shareholder wants a video doorbell facing the hallway — can the board say no? — §9
20. How long should a Manhattan doorman building keep recordings? — §9
21. Can a rental building's tenants force the landlord to fix a dead lobby camera? — §9
22. Can you take over an analog system left by a previous managing agent's vendor and reuse the coax runs? — §9
23. Can the lobby video intercom and the cameras share one recorder and one riser? — §9
24. Do ground-floor retail tenants in a mixed-use building need to be on the building's camera system? — §9

### Visible FAQ (§17, mirrored exactly in FAQPage schema)
1. Do you deal with the managing agent, the board president or the super day to day? — §17
2. Can the work be staged so that the lobby never goes a night without a recording camera? — §17
3. Will you need the boiler room, meter room and roof bulkhead keys on the walkthrough? — §17
4. How do you protect the lobby floor and the elevator while equipment is coming in? — §17
5. Will you give us wording for a camera notice to shareholders and a rule for the house rules? — §17
6. Can cameras be added to the laundry room, bike room and storage cages in a prewar co-op cellar? — §17
7. Who receives the invoice for a new condominium where the sponsor still controls the board? — §17
8. If the board turns the proposal down, is anything owed for the walkthrough? — §17
9. Can footage be exported the same day for detectives from the local NYPD precinct? — §17
10. Do you cover buildings from Battery Park City to Inwood, and how is parking handled? — §17

Duplicate check: tools/check_page.py reported no duplicated question vs any sibling on disk (incl. the -queens and -staten-island rebuilds present at 2026-10-18 build time).

### apartment-building-security-camera-installation-queens

### Q&A headings (section 9, "Questions Answered") — page: apartment-building-security-camera-installation-queens
- Recorder Down After a Break-In in Queens?
- How do you cover a Jackson Heights garden co-op whose interior garden runs the full length of the block?
- Can a building inside the Jackson Heights Historic District put cameras on its street facade at all?
- Our Sunnyside Gardens court is shared by several owners — who has to agree before cameras go up?
- What carries camera video between the separate buildings of a Glen Oaks Village–type campus?
- Does each building in a Queens garden complex need its own recorder, or can the management office hold them all?
- What camera angle actually identifies someone forcing a vestibule door with a screwdriver, as in the Astoria and Elmhurst cases?
- A Jackson Heights mailroom was hit three times in March — how do cameras change things for a repeat target?
- Where should a camera sit to catch someone picking an outer-door lock and then a mailbox, like the Forest Hills case near 67th Road?
- Our Queens Boulevard building has no doorman — where should couriers leave packages so the camera sees them but passers-by don't?
- Is a camera allowed in the basement laundry room of a Rego Park six-story building, and can it record sound?
- Kew Gardens courtyard buildings have several separate entrances — does every entrance need its own camera?
- How do you cover the rear alley or service lane behind a Queens Boulevard apartment house at night?
- After the 62nd Drive car break-ins in Rego Park, what can a building's own cameras realistically capture on the street?
- Can cameras read plates at the entrance to a Long Island City tower's garage?
- A new Long Island City rental already has keyless entry and a video intercom — what do cameras add?
- The developer left a camera system in our Court Square building — can the new managing agent take it over?
- I own a two-family house in Woodside with a rental upstairs — where can my cameras point without crossing into my tenant's space?
- A Flushing building has stores on Main Street below and apartments above — can the shops and the residential entrance share one recorder?
- Who approves cameras in a Forest Hills co-op, and how is that different in an Elmhurst rental building?
- Should camera notices in a Jackson Heights or Flushing building be posted in more than one language?
- Can a camera be added inside the elevator cab of a six-story 1930s co-op on Austin Street?

### Visible FAQ (section 17) = FAQPage schema — page: apartment-building-security-camera-installation-queens
- Do the Landmarks Preservation Commission's camera limits apply building by building on a block-long Jackson Heights garden complex?
- Can tenants in a Woodside or Sunnyside rental building watch the building cameras on their own phones?
- Will the cameras keep recording when the power drops in a Glen Oaks or Rego Park basement?
- What happens when the local precinct asks for video of a mailroom break-in in our Jackson Heights building?
- Can a camera cover the bike room or storage cages in the cellar of a Long Island City rental?
- Can a Kew Gardens co-op reuse the coaxial cable from its old analog cameras?
- How can a Sunnyside Gardens homeowner watch the shared court without filming a neighbour's windows?
- Can installation work be scheduled so the lobby of an occupied Rego Park building is never blocked?
- What does a yearly check-up of an existing Queens Boulevard building system involve, and how is it billed?
- If our co-op board and the managing agent disagree about who should hold the recorder password, what do you suggest?

### Images (11) — REPLACED per coordinator 2026-10-18: earlier commercial-security/ picks were AI-generated and were deleted.
4 real AESS job photos (not Queens jobs; captions say "example photo ... not a Queens job", business names cropped out) + 7 manufacturer product shots (captioned as product photos):
- images/manhattan-deli-exterior-camera.jpeg (cropped below the sign text) → images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-queens-turret-camera-under-yellow-fascia-corner.webp (hero)
- images/manhattan-deli-monitor.jpeg → …-queens-camera-grid-on-ceiling-hung-monitor.webp
- images/nassau-window-depot-office-camera.jpeg (cropped to remove the business banner, its face and framed licences) → …-queens-turret-camera-in-ceiling-corner-above-motion-sensor.webp
- images/rockland-toyota-ceiling-bullet.jpeg (bottom trimmed) → …-queens-black-bullet-camera-on-drop-ceiling-mount.webp
- images/ubiquiti-unifi-g6-bullet-4k-camera-white.jpg → …-queens-white-4k-bullet-camera-product-photo.webp
- images/ubiquiti-unifi-g6-turret-4k-camera-white.jpg → …-queens-white-4k-turret-camera-product-photo.webp
- images/ubiquiti-unifi-g6-entry-doorbell.jpg → …-queens-video-entry-doorbell-product-photo.webp
- images/ubiquiti-unifi-ai-360-fisheye-camera-black.webp → …-queens-black-360-fisheye-camera-product-photo.webp
- images/hikvision-colorvu-bullet-camera.jpg → …-queens-colorvu-bullet-camera-product-photo.webp
- images/nvr-hikvision-ds7616ni.png → …-queens-16-channel-nvr-recorder-product-photo.webp
- images/hikvision-acusense-mini-dome-camera.jpg → …-queens-mini-dome-camera-product-photo.webp

### apartment-building-security-camera-installation-staten-island

### Q&A headings (§9 "Questions Answered")
1. Our two-family in Great Kills has the tenant upstairs — whose phone gets the camera app, and who sees the rental unit's door?
2. Can one recorder cover a front house and a detached rear garage across the driveway, or does each building need its own?
3. What do you use to cross a shared driveway or parking court between two townhouse rows when trenching isn't allowed?
4. How do you keep cameras working within sight of the water in Midland Beach, South Beach or Tottenville, where salt spray eats metal?
5. Where should the recorder sit in an East Shore building that took water in Sandy?
6. Will the cameras keep recording when a nor'easter knocks out power along Hylan Boulevard?
7. How do we light and cover a surface lot behind a Victory Boulevard walk-up so night footage shows faces, not glare?
8. Is a plate-reading camera worth it at the entrance of a South Shore townhouse community with its own private road?
9. Our condo association owns the roads and parking in Annadale — who has to approve cameras, and how do we take it to the board?
10. A unit owner in our Huguenot complex put a camera over their own door aimed at the walkway — can the HOA make them move it?
11. For a mixed-use building on Bay Street with a store below and apartments above, should the shop and the residents share one camera system?
12. A tenant in our Stapleton building asked to see last night's footage after a package went missing — do we have to show it?
13. Can cameras in the shared hallway of a converted Victorian in St. George record sound?
14. Does a Staten Island landlord need a licensed installer, or can the handyman mount the cameras?

### FAQ (§17)
1. How long does a Staten Island installation take when the parking lot is behind a separate garage building?
2. Can you reuse the coax already strung between buildings at an older North Shore garden complex?
3. What happens to our cameras when the Staten Island Railway or a utility crew digs up the trench line beside the property?
4. Do you cross the Verrazzano for a single small job on Staten Island, and is there a bridge or travel line on the invoice?
5. Can our HOA spread the camera cost over two budget years in a South Shore townhouse community?
6. Does wooded Greenbelt-edge property on Staten Island change where cameras can go?
7. Our board wants to see footage from home — will remote viewing work on the internet service most Staten Island complexes already have?
8. Can a camera system on Staten Island help with illegal dumping at the back of a lot near Fresh Kills or the West Shore industrial edge?
9. Who looks after the system if the property manager for our Staten Island complex changes?
10. Will snow plows clearing a private community road damage pole-mounted cameras at the entrance?

### apartment-building-security-camera-installation-suffolk-county

Final list as published (an earlier draft list was revised to avoid intents already registered for Manhattan, Queens and Staten Island: recorder-per-building, inter-building links, salt spray, surge-zone recorder, tenant footage requests, shop+apartments shared system, two-family tenant privacy, plate readers at private roads, power-outage recording, condo board vote, remote viewing on existing internet, snow plows, management change).

### Q&A headings (§9)
1. Our Ronkonkoma garden complex has a parking field the size of a football field — how many cameras does that take? — §9
2. Can the existing underground conduit for a Suffolk complex's site lighting be used for camera cable? — §9
3. Can a single camera on a light pole cover a whole row of carports at a Holbrook or Medford complex? — §9
4. How many cameras does a typical two-storey Suffolk garden building need, stairwell by stairwell? — §9
5. Our Lake Grove complex backs onto a county recharge basin behind a chain-link fence — can cameras cover that fence line? — §9
6. What camera setup actually helps at the cluster mailbox kiosk in a Suffolk condo, given the Suffolk collection-box thefts reported in 2026? — §9
7. Can the clubhouse, pool gate and fitness room of a Suffolk 55-plus community be on cameras without residents feeling watched? — §9
8. Our Brookhaven 55-and-over HOA was pitched a Flock camera that shares plates with police — how is that different from a camera the HOA owns? — §9
9. Can the cameras at a Commack or Smithtown condo help the board enforce parking rules on boats, trailers and work vans? — §9
10. Our Patchogue Main Street building's rear lot is shared with the restaurant next door — whose cameras cover it? — §9
11. Our Riverhead East Main Street building's apartment entrance is a side door off an alley — how do you cover it? — §9
12. How do cameras work at a new transit-oriented rental by a Suffolk LIRR station where the garage is shared with commuters? — §9
13. Does adding cameras to a house with a permitted Babylon or Islip accessory apartment affect the town's accessory apartment permit? — §9
14. Are cameras allowed inside or outside an East Hampton or Southampton seasonal rental, and what should the rental registry paperwork mention? — §9
15. Suffolk licenses home improvement contractors and electricians — which of those licences, if any, covers a camera job? — §9
16. Do camera poles in a Suffolk parking lot need a town building permit? — §9

### Visible FAQ (§17) = FAQPage schema
1. How are cameras fixed to vinyl siding and cedar shingles on Suffolk garden buildings without causing leaks? — §17
2. Can the HOA schedule installation so the Suffolk complex’s pool season and summer move-ins aren’t disrupted? — §17
3. Can the cameras at a Suffolk complex send an alert when someone opens the pool gate after hours? — §17
4. Can a property manager who runs several Suffolk complexes watch them all from one app? — §17
5. Will you meet a Suffolk HOA’s architectural review committee about how the cameras will look? — §17
6. Do residents of a Suffolk senior community get an explanation of the cameras, or only the office staff? — §17
7. What happens if a camera fails at a Suffolk complex during the first year? — §17
8. Is there a charge when a Suffolk property manager calls with a problem on a system you installed? — §17
9. Do you take away the old cameras and DVR when a Suffolk complex upgrades? — §17
10. Can the Suffolk complex’s maintenance staff change a camera’s angle after installation? — §17

### Images (11) — source → target (images/apartment-building-security-camera-installation/)
Real AESS job photos (captioned "Example photo from an AESS installation"; no business named, no Suffolk/apartment claim):
- rockland-toyota-dome-camera.jpeg (cropped to ceiling corner; dealership logo, TV and "Guest Services" sign removed) → …-suffolk-county-black-mini-dome-camera-at-ceiling-corner.webp (hero, og:image)
- rockland-toyota-bullet-camera.jpeg (cropped above the dealership sign/posters) → …-suffolk-county-bullet-camera-on-high-wall-above-drop-ceiling.webp
- manhattan-deli-interior-cameras.jpeg (ceiling strip only; people, menu boards and product brands removed) → …-suffolk-county-two-ceiling-dome-cameras-in-tiled-grid.webp
- rockland-toyota-hallway-camera.jpeg (left cabinet, QR-code poster and key tag cropped out; bottom trimmed — differs from Manhattan's crop) → …-suffolk-county-bullet-camera-aimed-at-grey-service-door.webp
Manufacturer product photos (captioned as product photos, natural width, not upscaled):
- ubiquiti-unifi-g5-bullet-5mp-camera-white.jpg ("Compare" checkbox text cropped) → …-compact-white-bullet-camera-product-photo.webp
- ubiquiti-unifi-g5-turret-ultra-camera-white.jpg → …-white-turret-camera-product-photo.webp
- ubiquiti-unifi-g5-ptz-outdoor-camera-white.jpg → …-outdoor-ptz-camera-product-photo.webp
- uniview-fisheye-360-panoramic-camera-white.jpg → …-360-fisheye-camera-product-photo.webp
- hikvision-varifocal-bullet-camera.jpg → …-varifocal-bullet-camera-product-photo.webp
- nvr-hanwha-wisenet-arn1610s.png → …-16-channel-nvr-recorder-product-photo.webp
- dahua-full-color-2-bullet-camera-white.png (file actually shows a PTZ speed dome on a dark background; described as such) → …-ptz-speed-dome-on-dark-background-product-photo.webp

### apartment-building-security-camera-installation-westchester-county

### Q&A headings (§9 "Questions Answered", H3)
1. Does Westchester County's home-improvement licence cover camera work in a 40-unit Yonkers apartment building? — §9
2. Westchester's consumer-protection code licenses alarm businesses — does a camera-only system in a New Rochelle tower fall under that? — §9
3. Will the White Plains building department want a permit before cameras go into our Mamaroneck Avenue rental? — §9
4. Our Croton-on-Hudson co-op already holds an alarm permit for the fire panel — does adding cameras change it? — §9
5. In a rent-stabilized Yonkers building, what should tenants be told before new hallway cameras start recording? — §9
6. A tenant in our Port Chester building says the hallway camera sees into her apartment when she opens her door — what do we change? — §9
7. Tenants in a Mount Vernon walk-up keep calling the building inspector about the broken front-door lock — should cameras come before the lock repair? — §9
8. Someone keeps propping open the side door of our White Plains rental near the station — can cameras show who? — §9
9. Sleepy Hollow applies ETPA only to buildings of ten or more units — our nine-unit building is outside it, so do any camera rules change? — §9
10. How should cameras cover the garage under a downtown White Plains tower where residents and retail customers share the ramp? — §9
11. Which cameras belong on the amenity floor and roof deck of a new Getty Square high-rise, and which do not? — §9
12. Commuters from the New Rochelle station cut through our lobby to reach the street behind — how do cameras help the front desk? — §9
13. The developer of our New Rochelle building installed cloud cameras with a monthly fee per camera — can the managing agent move them onto a recorder the building owns? — §9
14. The west-facing entrance of our Hastings-on-Hudson building looks straight at the river at sunset — why is the face always a silhouette, and what fixes it? — §9
15. Our building in Mount Kisco is a short walk from the Metro-North platform — can our cameras cover the path commuters use beside the lot? — §9
16. How do we get cable to the upper floors of a 1920s Bronxville apartment building with plaster walls and no hung ceilings? — §9
17. Our Hartsdale co-op shares its parking court with the neighbouring co-op — where should our cameras stop? — §9
18. Our building in the Lawrence Park area sits on rock — how do cameras reach the detached garage without trenching through granite? — §9
19. Our Scarsdale co-op board meets only four times a year — how do we get cameras approved without losing a season? — §9
20. The lobby attendant in our Tuckahoe co-op works days only — how should the cameras behave after the desk closes? — §9
21. Our Pelham co-op wants a camera on the street side, and the village reviews exterior changes — what do we bring to that review? — §9
22. Can the cameras for the rear parking lot of our Tarrytown building stay on the building wall, or do they need a pole? — §9
23. How will the board of our Rye condo know a camera has failed without someone checking the screen every day? — §9
24. In a Peekskill walk-up above a Main Street storefront, where can the residential entrance camera go without filming the shop's customers? — §9
25. A hillside building in Ossining has entrances on two different street levels — how many cameras does that take? — §9
26. The basement boiler and meter room of our Mount Vernon six-family keeps being broken into — where does the camera go? — §9

### Visible FAQ (§17) = FAQPage schema
1. Our Cortlandt condo complex hired a new super after the cameras went in — can you train him months later? — §17
2. Can a board member or the owner join the walkthrough of our Larchmont building? — §17
3. Our Yonkers tower already has building-wide Wi-Fi run by an outside provider — will the cameras interfere with it? — §17
4. Do you remove the old cameras and abandoned cable when we upgrade a New Rochelle building? — §17
5. Can cameras be added later when our White Plains building finishes its lobby renovation? — §17
6. A property manager runs buildings in Yonkers, Mount Vernon and Port Chester — can one account see all of them? — §17
7. Our Mount Vernon building needs one camera replaced — is there a minimum charge? — §17
8. What is due when a Westchester co-op board signs the proposal? — §17
9. Do you photograph the lobby and hallways of a Bronxville co-op before work starts? — §17
10. If our Ossining building later hires a different contractor, do we keep the drawings and passwords? — §17
11. Does the recorder for our Greenburgh garden co-op need its own internet line? — §17

Checked by meaning against the Manhattan, Queens and Staten Island registers: retention, coverage-area, install-duration and budget-phasing FAQs were replaced to avoid intent overlap.

### Images (11)
Real AESS photos (captioned "Example photo from an AESS installation, not a Westchester apartment building"): rockland-toyota-showroom.jpeg (cropped to upper wall: no people, no banners/signage) → …-westchester-county-two-small-cameras-on-tall-white-wall-below-mezzanine-windows.webp (hero/og:image); rockland-toyota-office-camera.jpeg (ceiling only) → …-white-turret-camera-between-ceiling-light-panels.webp; nassau-window-depot-storage-camera.jpeg (top 620px, boxes/labels removed) → …-turret-camera-in-corner-under-stained-ceiling-tiles.webp; rockland-toyota-ceiling-bullet.jpeg (ceiling only, monitors removed) → …-black-bullet-camera-on-ceiling-grid-beside-air-vent.webp.
Product shots (tight crops, native size, never upscaled): ubiquiti-unifi-g6-pro-turret-camera-white.jpg → …-white-turret-camera-with-blue-ring-product-photo.webp; ubiquiti-unifi-g5-dome-ultra-camera-white.jpg → …-clear-dome-camera-product-photo.webp; uniview-turret-network-camera-white.jpg → …-white-eyeball-turret-camera-product-photo.webp; hikvision-ptz-speed-dome-camera.jpg → …-pendant-ptz-speed-dome-product-photo.webp; nvr-uniview-nvr501.png → …-black-desktop-network-video-recorder-product-photo.webp; ubiquiti-unifi-g6-instant-4k-camera-white.jpg → …-white-compact-indoor-camera-product-photo.webp; dahua-wizsense-ai-varifocal-bullet-camera-white.png (file actually shows a white PTZ speed dome on black, not a bullet) → …-white-speed-dome-on-black-product-photo.webp.
