# Research — Apartment Building Security Camera Installation (silo)

Silo: `apartment-building-security-camera-installation-*` (NYC hub + 5 boroughs + LI hub/Nassau/Suffolk + HV hub/6 counties).
Created 2026-10-18 (UTC) by the Brooklyn REBUILD builder. Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. A source that could not be opened from the build environment is written `EMPTY (not accessible in build env)` — nothing below is invented.

Silo-wide pricing (already published identically on every silo page before the rebuild, Brooklyn = 1.00× base per §9): per camera installed all-in **$500–$1,500**; Small walk-up 4–8 cameras **$5,000–$12,000**; mid-size elevator building 12–20 cameras **$12,000–$25,000**; large/high-rise 24–40 cameras **$25,000–$45,000+**; multi-building portfolio 50+ cameras custom. Service/callback rate (v2.3 §9, protected): **$195/hr, 3-hr minimum ($585)**. Other areas multiply per §9 (Queens 1.05, SI 1.10, Nassau 1.15, Manhattan 1.25, Suffolk 1.20, Westchester 1.25, Rockland 1.30, Orange 1.40, Putnam 1.45, Dutchess/Ulster 1.53).

---

## 1. Silo-wide research matrix

| # | Source | Exact query | Platform | URL | Finding | Used on (page · section) |
|---|---|---|---|---|---|---|
| 1 | Reddit | `subreddit:Brooklyn building cameras super footage packages` | Reddit API (Composio REDDIT_SEARCH_ACROSS_SUBREDDITS) | https://www.reddit.com/r/Brooklyn/comments/1v5vuus/package_theft_from_our_building_is_out_of_control/ | Jul 25 2026 post: package theft "100% guaranteed from the lobby"; landlord "won't act or install cameras", tells tenants to get a P.O. box; majority of residents seniors; poster asks if a peephole/door camera is allowed on a shared hallway. Top replies: get your own camera; ask building to host a package locker (GoLocker/Quadient pilot); one says lobby cameras in an old building "did nothing to deter"; one says some landlords make tenants remove video doorbells. | brooklyn · Neighborhood; Q&A "packages"; Reality Check H3 "cameras don't deter" |
| 1b | Reddit | (same search) | Reddit API | https://www.reddit.com/r/Brooklyn/comments/rxy4q8/someone_in_my_building_stole_my_package_what/ | Jan 2022, Bed-Stuy 12-unit building: "virtual security guy" pulled the entrance camera; footage showed nobody came in from outside, but the package corner "at the end of the hallway with no camera" — so theft was internal and unprovable. | brooklyn · Neighborhood (blind-spot story); Q&A "corner without a camera" |
| 1c | Reddit | `site:reddit.com landlord cameras hallway Brooklyn apartment building` | Firecrawl search → Reddit API comments | https://www.reddit.com/r/Brooklyn/comments/yrlptj/is_the_landlord_required_by_law_to_install/ | Nov 2022: "Is the landlord required by law to install security cameras?" — answers: "Nope"; alternatives = deliver to work, UPS/FedEx store, schedule delivery. | brooklyn · Q&A "can tenants force cameras" |
| 1d | Reddit | (same) | Reddit API | https://www.reddit.com/r/Brooklyn/comments/zn1mfa/if_you_live_in_an_apartment_building_check_for/ | Dec 2022: South Brooklyn condominium found an intruder living in the basement "only noticed after the intruder was caught on camera wandering around the hallways". Reply: check back doors, laundry rooms, emergency exits; a weak basement lock was jimmied repeatedly. Another: East Williamsburg storage cages occupied. | brooklyn · Neighborhood; Building Specialists (cellar); Q&A "cellar intruder" |
| 1e | Reddit | `subreddit:NYCapartments landlord cameras footage police` | Reddit API | https://www.reddit.com/r/NYCapartments/comments/1up433d/beware_of_goose_property_management/ | Jul 2026: tenant asked for camera footage after a theft and was told viewing costs a $500 fee. | brooklyn · Q&A "footage requests"; Recording section |
| 1f | Reddit | (same) | Reddit API | https://www.reddit.com/r/NYCapartments/comments/1p3fnwy/landlord_suddenly_installed_a_smarthome_door_its/ | Nov 2025, two-unit Queens house: landlord swapped lock-and-key door for camera + face recognition + fingerprint smart door with no notice. | silo · (Queens context — not used on Brooklyn page beyond Local Law 63 point) |
| 1g | Reddit | `reddit landlord installed cameras hallway NYC apartment legal` | Firecrawl search excerpt | https://www.reddit.com/r/AskNYC/comments/1bfjfdu/is_there_a_way_to_force_a_landlord_to_show_me_the/ | Excerpt: landlord unlikely to show feed; "file a police report… tell the investigating officers that the building has cameras." | brooklyn · Q&A "footage requests" |
| 2 | Google PAA | `apartment building security camera installation cost` / `security cameras apartment building hallway legal New York` | Google | — | EMPTY (not accessible in build env) | — |
| 3 | Google PASF | same | Google | — | EMPTY (not accessible in build env) | — |
| 4 | Answer the Public | `apartment building security cameras` | answerthepublic.com | — | EMPTY (not accessible in build env) | — |
| 5 | Google AI Overview | `how much do apartment building security cameras cost` | Google SGE | — | EMPTY (not accessible in build env). Substituted the national cost guides an AI Overview typically cites (rows 5a/5b) for the Reality Check. | — |
| 5a | Cost guide (AI-Overview substitute) | `security camera installation cost per camera Angi Fixr HomeAdvisor 2026` | Firecrawl search | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | Angi 2026: national average $1,289 (4,027 projects), typical $589–$2,040; pro install "$100 and $200 per camera"; wired $150–$500 per camera; labor 50–70% of project. | brooklyn · AI Overview Reality Check H3 1–2; Pricing |
| 5b | Cost guide | same | Firecrawl search | https://www.fixr.com/costs/install-video-surveillance-cameras | Fixr: surveillance camera installation $400–$800, national average $600. | brooklyn · Reality Check H3 1 |
| 6 | Law — unlawful surveillance | `NY Penal Law 250.45 unlawful surveillance second degree bedroom bathroom` | Firecrawl search | https://www.nysenate.gov/legislation/laws/PEN/250.45 | Class E felony to install an imaging device for no legitimate purpose to surreptitiously record a person in a bedroom, changing room, restroom, bathroom, shower, etc. | brooklyn · Commercial compliance callout; FAQ |
| 7 | Law — installer licence | `New York General Business Law 69-l definition security or fire alarm system closed circuit television installer license` | Firecrawl search | https://www.law.cornell.edu/regulations/new-york/19-NYCRR-195.2 ; https://www.kirschenbaumesq.com/article/business-of-installing-servicing-or-maintaining-security-or-fire-alarm-systems-new-yorks-license-law ; https://dos.ny.gov/security-or-fire-alarm-installer | 19 NYCRR 195.2: installer licence required for a CCTV system used full- or part-time to detect/monitor intrusion, break-in, theft, movement; owner installing on own property with own employees is exempt (GBL 69-m(2)). | brooklyn · Commercial compliance; Q&A "who can install" |
| 8 | Law — NYC low-voltage permit | `NYC Department of Buildings electrical permit not required low voltage security camera wiring Class 2` | Firecrawl scrape (amlegal) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 | Admin Code §28-105.4.7 (L.L. 2024/128): no electrical permit for wiring under 50 V for signaling, communication, alarm and data circuits, if performed by a licensed master electrician, special electrician or "qualified person"; life-safety system wiring and connections to light/heat/power control circuits excepted. | brooklyn · Commercial compliance; Q&A "DOB permit" |
| 9 | Law — firestopping | `NYC Building Code section 714 penetrations through-penetration firestop systems` | Firecrawl search | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-169620 ; https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/7/fire-and-smoke-protection-features | BC 714 governs penetrations of fire-resistance-rated assemblies; through-penetrations protected by an approved firestop system tested to ASTM E 814 / UL 1479. | brooklyn · Building Specialists (riser), Process step |
| 10 | Law — intercom/entrance | `New York Multiple Dwelling Law 50-a intercom self-locking entrance door eight or more apartments` | Firecrawl search | https://www.nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf | MDL §50-a: class A multiple dwellings erected or converted after Jan 1 1968 with 8+ apartments must have an intercommunication system at an automatic self-locking door to the main entrance hall/lobby. No state/city law found requiring cameras (consistent with r/Brooklyn answers, row 1c). | brooklyn · Q&A "is a camera legally required" |
| 11 | Law — Tenant Data Privacy | `NYC Tenant Data Privacy Act Local Law 63 of 2021 smart access multiple dwelling cameras` | Firecrawl scrape | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | L.L. 63/2021 (HPD): owners using smart-access (fob, app, biometric) entry in class A multiple dwellings must give tenants a data retention/privacy policy, get express consent, collect minimum data, destroy authentication data within 90 days unless anonymized, never sell data, never use it to harass or evict, no tracking of relationship status. | brooklyn · Commercial compliance; Q&A "camera + fob together"; Reality Check H3 |
| 12 | Rent regulation precedent | `DHCR landlord install security cameras rent stabilized building service modification tenants` | Firecrawl scrape | https://www.nycourts.gov/reporter/3dseries/2018/2018_06737.htm | Matter of Bazile v Rubin, 2018 NY Slip Op 06737 (2d Dept, from Queens County): DHCR rationally found a video surveillance system an adequate substitute for part-time lobby attendants in a rent-stabilized building (owner applied for a service modification). | brooklyn · Q&A "replacing a lobby attendant" (framed as a Queens case) |
| 13 | Co-op guidance | `HDFC co-op Brooklyn security cameras board shareholders` | Firecrawl scrape | https://cooperatornews.com/article/qa-security-cameras-and-the-right-to-privacy | Cooperator Q&A (Nov 2012, Christian Paul Daglieri): cameras in a co-op community room are not an intrusion — "the community room remains the property of the corporation". | brooklyn · Building Specialists (co-op) |
| 14 | HDFC stock | same | Firecrawl search | https://www.nyc.gov/site/hpd/services-and-information/hdfc.page ; https://www.uhab.org/our-work/coop-support/whats-an-hdfc/ | HPD: "over 1,100 HDFC coops"; UHAB: ~1,200 HDFC co-ops housing 25,000 low-income households across the Bronx, Brooklyn, Manhattan and Queens. | brooklyn · Building Specialists (HDFC); Stats |
| 15 | Rent-stabilized stock | `Brooklyn housing stock built before 1940 percent rent stabilized units Brooklyn number` | Firecrawl scrape | https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/housing-and-buildings/2026/2026-may-segments-of-the-rent-stabilized-housing-stock.pdf | IBO May 2026: ~928,000 stabilized apartments in ~43,000 buildings; Brooklyn largest with 279,000; pre-1974 stabilized buildings median construction year 1924; in Williamsburg, Greenpoint and Downtown Brooklyn districts more than half of stabilized units are in post-1973 buildings. | brooklyn · Stats; Building Specialists |
| 16 | Landmarks | `Landmarks Preservation Commission rules "security cameras" staff level permit facade conduit` | Firecrawl scrape | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook%20_Chapter11_HealthSafety.pdf | LPC staff can approve cameras that are "well spaced"; small residential/commercial buildings max two cameras per 25 ft of street frontage; large buildings max three per 25 ft. | brooklyn · Commercial compliance; Q&A "landmark facade" |
| 17 | Tenement history | `Tenement House Act 1901 new law tenements air shafts` | Firecrawl search | https://www.nypl.org/blog/2018/06/07/tenement-homes-new-york-history-cramped-apartments | Tenement House Acts 1867/1879/1901/1919; pre-1901 = "old law", after = "new law"; Multiple Dwelling Law took shape 1929. | brooklyn · Building Specialists (walk-ups) |
| 18 | Bing / DuckDuckGo | `apartment building security camera installation Brooklyn` | Bing, DDG | — | EMPTY (not accessible in build env) | — |
| 19 | Yelp 1–3★ | `security camera installation Brooklyn` 1–3★ | Yelp | — | EMPTY (not accessible in build env). Substitute pain point: footage-access fee (row 1e), uncovered hallway corner (row 1b). | — |
| 20 | Package lockers | `NYC DOT package locker pilot private buildings Quadient GoLocker` | Firecrawl scrape | https://www.nyc.gov/html/dot/html/pr2025/lockernyc-milestone.shtml | DOT 2025: LockerNYC passed 10,000 deliveries; 22 sites in Manhattan, Brooklyn and Queens; new GoLocker outdoor site at 5009 Sixth Avenue, Sunset Park; a LockerNYC location in Bushwick. | brooklyn · Q&A "packages beyond cameras" |

---

## 2. Question register (every FAQ / Q&A question on a silo page — check before writing)

### Pre-rebuild template questions (still live on Bronx, Manhattan, Queens, SI, Nassau, Suffolk, Westchester, Rockland, Orange, NYC hub; HV and LI hubs being rebuilt in the same batch)
Each of these exists on every old page with the area name swapped — **do not reuse any of these intents verbatim**:
- How much does apartment building camera installation cost in [area]?
- Are there monthly fees for a building camera system?
- How many cameras does an apartment building need?
- Which camera brands do you install?
- What resolution and retention should a building use?
- NVR or cloud — which should I choose?
- Can building cameras record audio?
- Do we have to notify residents about cameras?
- Do you serve all of [area] / all five boroughs?
- Do we need a licensed contractor for building cameras?
- Can you integrate cameras with the intercom and door access?
- Do you service buildings that already have cameras?
- (heading) Ready to Secure Your Building?

### apartment-building-security-camera-installation-brooklyn (REBUILD 2026-10-18)
Q&A (§9):
1. Our stoop has eight steps and the door is set back under the parlor-floor landing — where does the entry camera go so it sees faces, not hat brims?
2. Packages go missing from the vestibule of our walk-up. Will one camera on the door settle whose hand took them?
3. The carriers leave boxes in a hallway corner the old camera never covered. How do we close that kind of gap?
4. Can a Brooklyn tenant make the landlord put cameras in, or add their own at the apartment door?
5. Somebody was sleeping in our cellar for weeks before anyone knew. What would a camera plan for the cellar and rear yard look like?
6. Our building is in a Brooklyn historic district. Does a camera on the front of a brownstone or limestone need Landmarks approval?
7. We're a small HDFC co-op with a volunteer board and a tight reserve. How do we phase a system so we're not paying for everything at once?
8. Our rent-stabilized building wants to swap a part-time lobby attendant for cameras. Is that allowed?
9. We want fob entry on the front door along with the cameras. What changes under the Tenant Data Privacy law?
10. Who in a co-op or rental building should be allowed to pull footage, and how should a request from a resident be handled?
11. The recorder in our cellar keeps losing days of video. Is that the recorder, the drive or the cable?
12. Our building has a ground-floor store with its own cameras. Can the two systems share a recorder?
13. Do you need a DOB electrical permit to run camera cable up a Brooklyn walk-up?
FAQ (§17):
1. How long does a typical Brooklyn walk-up camera install take, and do residents need to be home?
2. Can you run camera cable without opening the plaster in a pre-war stairwell?
3. Will the cameras still record if Con Edison power or the internet goes out?
4. Do you supply the insurance certificate our managing agent or co-op board asks for?
5. Can the super check the cameras from a phone without giving everyone the password?
6. What happens if a camera stops working after the install?
7. Can you put a camera in the elevator cab of a Brooklyn mid-rise?
8. Do you work in occupied buildings with tenants coming and going all day?
9. Is there a separate charge for coming back to adjust a camera angle later?
10. Can we see a sample layout before the board votes?
11. Do you install in Brooklyn condo buildings where each owner has a vote?
12. How far ahead do we need to book for a building in Brooklyn?

(Hudson Valley hub and Long Island hub builders add their own sections here after the batch merge.)

---

### Register additions 2026-10-18
The Hudson Valley hub and Long Island hub questions are listed in full in their merged sections below (### C. Question register / ### Questions used on this page). Treat them as part of this register.

## Brooklyn

Local research for `apartment-building-security-camera-installation-brooklyn` (REBUILD — old page was crawled-not-indexed as a near-duplicate template). Thesis: **Brooklyn's building stock is mostly pre-war walk-ups, brownstone multi-families, HDFC co-ops and a band of post-2005 waterfront towers, so the camera problem is the stoop, the vestibule, the stair-hall corner and the cellar — and the rules that sit on top: Landmarks frontage limits, rent-stabilization service rules, the Tenant Data Privacy law.**

| Source | Exact query | Platform | URL | Finding | Used on (section) |
|---|---|---|---|---|---|
| Local news (Brownsville) | `Atlantic Plaza Towers Brownsville tenants facial recognition landlord cameras` | WebSearch → Firecrawl scrape | https://www.bkreader.com/news/brownsville-residents-alarmed-by-landlords-plan-to-install-facial-recognition-system-6543619 | BK Reader, Apr 2 2019: Atlantic Plaza Towers, 700-unit rent-stabilized complex at 249 Thomas S. Boyland St and 216 Rockaway Ave; Nelson Management applied to HCR (July 2018) for StoneLock facial-recognition entry; tenants objected in Jan 2019 with Brooklyn Legal Services; residents said existing cameras were used to watch tenants bringing packages in and emails described their packages; HCR said it evaluates service-modification applications. | Neighborhood; Reality Check H3 "more is better"; Q&A 9; Field Notes context |
| Local news | `Atlantic Plaza Towers landlord drops facial recognition plan November 2019` | WebSearch | https://www.securitysales.com/emerging-tech/brooklyn-fight-facial-recognition/ | SSI May 2019: landlord's application to replace key fobs with facial recognition "yet to be approved". (Outcome after 2019 not confirmed in a source opened here — page does not state an outcome.) | Q&A 9 |
| Local news (Flatbush) | `Brooklyn package theft apartment building vestibule news 2025` | WebSearch → Firecrawl scrape | https://hoodline.com/2025/11/brooklyn-superintendent-dies-after-confrontation-with-suspected-package-thief-on-ocean-avenue/ | Hoodline Nov 13 2025 (citing ABC7, CBS New York): building superintendent Burim Havolli, 41, died after a confrontation while trying to detain a suspected package thief at his building on Ocean Avenue, Flatbush. | Neighborhood (why staff shouldn't be the camera); Q&A 2 |
| Local news | same | WebSearch | https://www.cbsnews.com/newyork/news/lobby-packages-stolen-brooklyn | CBS NY: police released video of a man stealing packages from a Brooklyn apartment building lobby (headline only used). | Neighborhood (footage is what police release) |
| Reddit | see silo rows 1, 1b, 1c, 1d | Reddit API | (above) | Lobby theft with landlord refusing cameras (2026); Bed-Stuy uncovered hallway corner (2022); South Brooklyn condo basement intruder (2022); Sunset Park neighbour theft + battery doorbell (comment, 2026 thread). | Neighborhood; Q&A 2, 3, 4, 5 |
| Rent-stabilized stock | (silo row 15) | IBO | (above) | Brooklyn has 279,000 stabilized apartments — most in the city; pre-1974 stabilized buildings median year 1924; Williamsburg/Greenpoint/Downtown Brooklyn majority post-1973. | Stats; Building Specialists |
| HDFC | (silo row 14) | HPD / UHAB | (above) | 1,100–1,200 HDFC co-ops, Brooklyn among the four boroughs listed. | Building Specialists; Q&A 7 |
| Landmarks | (silo row 16) | LPC | (above) | Two cameras per 25 ft frontage (small buildings) / three (large) for staff approval. A typical Brooklyn rowhouse lot is often 20–25 ft wide (not separately sourced — page says "a 25-foot frontage" only as the LPC unit). | Q&A 6; Commercial compliance |
| Package lockers | (silo row 20) | NYC DOT | (above) | LockerNYC sites in Brooklyn incl. Bushwick and 5009 Sixth Ave, Sunset Park. | Q&A 2/3 supplementary |
| Hyperlocal (Brooklyn Paper / BK Eagle / News12 BK) | `Brooklyn apartment building break-in caught on surveillance video 2026 NYPD` | Firecrawl search (past year) | https://www.facebook.com/News12BK/posts/news-12-exclusive-newly-obtained-surveillance-video-shows-a-man-hurling-bricks-i/1297065412467124/ ; https://www.facebook.com/News12BK/videos/home-invasion-a-resident-at-a-midwood-apartment-building-was-awoken-in-the-early/1324734133023421/ | News 12 Brooklyn social posts: surveillance video of a man hurling bricks into the basement level of a Clinton Hill building; Midwood apartment-building home invasion. Dates not shown in excerpt — used only as "recent News 12 Brooklyn reports", no dates/addresses claimed. | Neighborhood (one line) |
| Brooklyn Paper / BK Eagle direct | `site:brooklynpaper.com apartment building cameras` | — | — | EMPTY (no relevant result returned in build env) | — |
| Local Reddit r/Bushwick, r/parkslope, r/bedstuy | — | — | — | EMPTY (not searched separately; r/Brooklyn covered) | — |
| Licensing/permits | silo rows 7–11 | — | — | NYS installer licence (AESS #12000287431), NYC §28-105.4.7, BC 714, MDL 50-a, L.L. 63/2021 apply borough-wide. | Commercial compliance; Q&A 13 |

Landmarks/corridors named on the page (well-known public places; descriptions limited to what's verifiable): Atlantic Plaza Towers (sourced above), Ocean Avenue Flatbush (sourced), Sunset Park / Sixth Avenue (DOT), Bushwick (DOT), Williamsburg / Greenpoint / Downtown Brooklyn (IBO), Brownsville. Commercial corridors listed (Flatbush Ave, Fulton St, Nostrand Ave, Fifth Ave Sunset Park, Kings Highway, Knickerbocker Ave) are named only as mixed-use corridors with storefronts under apartments — no stats attached.

Page images: 11 borrowed (permanent image rule) — 10 from `images/commercial-security/`, 1 from `images/parking/`; Drive folder `AESS Website Photos/Apartment Building Security Camera Installation` does not exist (checked 2026-10-18 01:00Z, parent folder lists only Cat6 Repair, Sonos, Soundbar, Smart Lock, Fiber Optic); CompanyCam has no active Composio connection.

## Hudson Valley hub (merged from batch builder, 2026-10-18)

## Research — Apartment Building Security Camera Installation · Hudson Valley hub (REBUILD)

Built 2026-10-18 for the REBUILD of `/apartment-building-security-camera-installation-hudson-valley` (was "Crawled – currently not indexed").
Silo-wide research for this silo is being written in parallel to `research/apartment-building-security-camera-installation.md` by the Brooklyn builder; this file holds the hub-level findings this page used plus the Hudson Valley local research. Main run merges it.

Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Unreachable surfaces are written `EMPTY (not accessible in build env)`.

**Page thesis (differs from the NYC/Brooklyn page = risers, stair halls, landlord rules under the NYC Multiple Dwelling Law; Long Island = its own page):** Hudson Valley multifamily is *horizontal and outdoors* — garden-apartment complexes of two- and three-storey buildings spread over acres, with surface parking, detached laundry and trash enclosures, so the work is trenching, pole mounts, building-to-building links and weather/power resilience rather than vertical riser pulls. It sits under a different legal map: the NYS Multiple Residence Law (not the NYC Multiple Dwelling Law), Good Cause Eviction adopted locally by 12 Hudson Valley municipalities, ETPA rent stabilization upheld for Kingston, county home-improvement licensing (Westchester, Putnam, Rockland), and a county-run code office in Spring Valley.

---

### A. Research matrix (11 sources)

| # | Source | Status | Notes |
|---|---|---|---|
| 1 | Reddit | Partial | r/hudsonvalley-specific threads on apartment cameras: none surfaced → EMPTY for HV. General multifamily package-theft threads found (below, H13) — used only as general tenant pain points, not attributed to HV. |
| 2 | Google PAA | EMPTY (not accessible in build env) | |
| 3 | Google PASF | EMPTY (not accessible in build env) | |
| 4 | Answer the Public | EMPTY (not accessible in build env) | |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — substituted with the aggregator cost pages AI answers draw on (HomeAdvisor, H16) | |
| 6 | Landmarks | Done | H18–H21 |
| 7 | Building types / use cases | Done | H7, H8, H9, H22 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env); WebSearch tool + Firecrawl search used instead | |
| 9 | Local news | Done | News 12 HV/Westchester, ABC7, Governor's office, Schumer press office (H10–H14) |
| 10 | Hyperlocal | Done | Hudson Valley Press, River Journal, Rockland Business Journal, LSHV (H1–H3) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) | |

---

### B. Findings (Hudson Valley local + hub-level)

**H1 — Good Cause Eviction local adoption.**
- Query: `Good Cause Eviction law opt-in Hudson Valley cities Kingston Beacon Newburgh Poughkeepsie 2025` · WebSearch → WebFetch https://www.nysenate.gov/newsroom/press-releases/2025/julia-salazar/1-year-later-good-cause-eviction-adopted-17-ny
- Finding: 17 municipalities statewide adopted stronger Good Cause; Hudson Valley ones listed: City of Kingston, City of Hudson, Village of New Paltz, City of Poughkeepsie, Town of Poughkeepsie, City of Beacon, Town of Fishkill, City of Newburgh, City of Middletown, City of White Plains, Village of Croton-on-Hudson, Village of Nyack (plus Village of Catskill, Greene County). About one million renters protected statewide.
- Also seen: https://riverjournalonline.com/around-town/for-the-local-good/good-cause-eviction-law-goes-into-effect-in-croton-on-hudson/201495 ; https://hudsonvalleypress.com/?p=64001 (Newburgh adoption) — titles only.
- Used: §5 para 3; §5.5 bullet; §8.5 callout; §9 "Good Cause" Q (Law & tenants cluster); FAQ Q on Good Cause cities.

**H2 — Kingston ETPA upheld.**
- Query: `Emergency Tenant Protection Act Westchester municipalities rent stabilization Kingston ETPA court ruling` · WebSearch → WebFetch https://lshv.org/in-the-news-kingston-rent-control-15-rent-reduction-upheld-by-nys-highest-court/
- Finding: article published June 18 2025: Court of Appeals unanimously upheld Kingston's 2022 housing-emergency declaration, its ETPA adoption and a 15% rent reduction ordered by the Kingston Rent Guidelines Board; vacancy below the 5% ETPA threshold. Court PDF: https://www.nycourts.gov/CTAPPs/Decisions/2025/Jun25/59opn25-Decision.pdf ; HCR notice https://hcr.ny.gov/nys-court-appeals-decision-hudson-valley-property-owners-inc-et-al-v-city-kingston-et-al
- Used: §5 para 3; §5.5 bullet; §9 rent-regulated Q.

**H3 — Rockland rents (Pattern for Progress).**
- Query: `Hudson Valley Pattern for Progress rental housing report vacancy rate multifamily 2024` · WebSearch → WebFetch https://rcbizjournal.com/2024/07/23/pattern-for-progress-annual-wage-housing-data-report-paints-a-bleak-picture-for-the-region/
- Finding: Rockland two-bedroom fair market rent $1,831 (2019) → $2,752 (2024); Rockland tied with Putnam for highest 2BR FMR of nine counties studied; $400/month above Westchester.
- Used: §5.5 bullet; §10.5 H3 (who pays / tenant expectations).

**H4 — NY unlawful surveillance (Penal Law 250.45).**
- Query: `New York unlawful surveillance Penal Law 250.45 hidden camera bathroom apartment landlord` · WebSearch → WebFetch https://newyork.public.law/laws/n.y._penal_law_section_250.45
- Finding: covers recording without consent in "a bedroom, changing room, fitting room, restroom, toilet, bathroom, washroom, shower"; installing a device there creates a rebuttable presumption of no legitimate purpose; class E felony.
- Used: §8.5 callout; §9 "laundry/restroom" Q; §10.5 H3 on privacy.

**H5 — NY audio recording, one-party consent.**
- Query: `New York eavesdropping one-party consent Penal Law 250.05 audio recording security camera` · WebSearch → WebFetch https://www.rcfp.org/?p=61695
- Finding: NY is one-party consent; recording an in-person conversation you are not party to, without any participant's consent, is a felony (Penal Law §§ 250.00, 250.05), up to four years and a $5,000 fine per RCFP.
- Used: §8.5 callout; §9 audio Q.

**H6 — NYS Security or Fire Alarm Installer licence (GBL Art. 6-D).**
- Query: `New York Department of State security or fire alarm installer license General Business Law Article 6-D` · WebSearch → WebFetch https://dos.ny.gov/security-or-fire-alarm-installer-application
- Finding: licence required to be in the business of installing/servicing systems that detect intrusion, break-in, movement, sound or fire; 81 hours qualifying study; passive non-detecting devices exempt; the DOS page does not address camera-only systems.
- Used: §8.5 callout (stated carefully: page does not claim cameras-only need the licence); §9 licensing Q.

**H7 — Westchester home-improvement licence.**
- Query: `Westchester County Department of Consumer Protection home improvement license security system installer` · WebSearch → WebFetch https://www.westchestercountyny.gov/all-press-releases/westchester-county-consumer-protection-department-warns-residents-as-spring-contracting-season-approaches
- Finding: home-improvement contractors need a licence from the Westchester County Consumer Protection Department under Article XVI; licensed list online; green bumper sticker; (914) 995-2155. Low-voltage/security not specifically mentioned.
- Used: §8.5 callout; §9 licensing Q (advice to verify).

**H8 — Putnam and Rockland home-improvement applications exist.**
- Query: `Rockland County Putnam County home improvement contractor license consumer protection requirement` · WebSearch
- Finding (titles/URLs only, not opened): Putnam County Consumer Affairs "Home Improvement New First Time Application 1-28-2025" https://putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/Home%20Improvement%20New%20First%20Time%20Application%201-28-2025.pdf ; Rockland County published documents https://www.rocklandcountyny.gov/home/showpublisheddocument/6348/639026169869900000
- Used: §8.5 callout ("Putnam and Rockland run their own home-improvement licensing; ask to see the card"). No requirements quoted beyond existence.

**H9 — Multiple Residence Law scope.**
- Query: `New York Multiple Residence Law applies cities less than 325,000 towns villages Multiple Dwelling Law applies cities 325,000 or more` · WebSearch → WebFetch https://newyork.public.law/laws/n.y._multiple_residence_law_section_3
- Finding: MRL §3(1) "shall apply to all cities of less than three hundred twenty-five thousand population" and "to all towns and villages".
- Also fetched https://newyork.public.law/laws/n.y._multiple_dwelling_law_section_50-a : MDL §50-a self-closing/self-locking doors + intercom for class A buildings with 8+ apartments (NYC rule — used only as the contrast).
- Used: §5 para 3; §8.5 callout; §9 "NYC rules" Q; §10.5 H3.

**H10 — Yonkers lobby package theft on video.**
- Query: `Hudson Valley apartment complex package thefts mailroom police Rockland Orange 2025` · WebSearch → WebFetch https://hudsonvalley.news12.com/3-arrested-for-stealing-packages-from-yonkers-lobby
- Finding: Dec 2 2024: three arraigned for stealing packages from a building lobby at 345 Bronx River Rd, Yonkers; 911 caller said suspects also tried building entries and car doors; officials obtained footage appearing to show them entering and removing packages.
- Used: §5 para 2; §5.5 bullet; §9 package Q.

**H11 — Haverstraw housing-complex package arrest.**
- Same query → WebFetch https://hudsonvalley.news12.com/2026/04/13/haverstraw-man-charged-after-police-recover-stolen-packages/7JATdEC12NE5OUR1Vi5iYd
- Finding: Apr 13 2026: Haverstraw man charged; police recovered multiple packages reported stolen within a housing complex. Surveillance not mentioned.
- Used: §5 para 2.

**H12 — New Rochelle lot break-in, resident asks for night cameras.**
- Query: `apartment complex security cameras Westchester lohud car break-ins 2025` · WebSearch → WebFetch https://abc7ny.com/post/thieves-smash-car-windows-steal-airbag-string-crimes-new-rochelle-parking-lot/15897965/
- Finding: Feb 12 2025: car in a John Street, New Rochelle parking lot broken into overnight, airbag stolen; residents said cars in the area hit three times that week; victim: "I would like some cameras in the nighttime." No existing cameras mentioned.
- Used: §5 para 2; §9 night-lot Q; Field Notes context.

**H13 — Lower Westchester car break-ins, key fobs.**
- Firecrawl search `reddit hudsonvalley apartment complex cameras landlord package stolen car broken into` → result → WebFetch https://westchester.news12.com/police-in-the-hudson-valley-urge-residents-to-lock-their-cars-amid-rise-in-break-ins
- Finding: May 30 2024: Yonkers (Wakefield Park) footage of a man trying car doors; Rye footage; Scarsdale two break-ins in a week; thieves seek key fobs which can be reprogrammed; Det. Lt. Brendan Kellaher: "With all but one that I recall in the last four years, it's all unlocked vehicles."
- Reddit results from same search (general, not HV): r/NYCapartments "Landlord is saying that the security camera systems are down" (https://www.reddit.com/r/NYCapartments/comments/1bjwldr/); r/AskNYC "landlord won't check them without a police report" (https://www.reddit.com/r/AskNYC/comments/100v3n5/); r/legaladvice tenant got footage from manager (https://www.reddit.com/r/legaladvice/comments/lhi85q/). Excerpts only.
- Used: §5.5 bullet (Kellaher quote context); §9 footage-request Q (general tenant pain point "cameras down", "won't check without police report" — not attributed to HV); §10.5 H3.

**H14 — Newburgh city camera network (history).**
- Query: `housing authority security cameras installed Yonkers OR Newburgh OR Poughkeepsie OR Peekskill public housing 2024 2025` · WebSearch → WebFetch https://www.schumer.senate.gov/newsroom/press-releases/after-major-push-by-schumer-and-maloney-department-of-justice-agrees-allow-city-of-newburgh-to-repurpose-152k-for-new-security-cameras
- Finding: Sept 22 2016: DOJ let Newburgh repurpose $152,031 of a Project Safe Neighborhoods grant to repair non-working cameras and install new digital cameras in the city's highest-crime areas.
- Used: §5.5 bullet (cameras that stop working is a known municipal problem); county section (Orange).

**H15 — Rockland Office of Buildings and Codes in Spring Valley.**
- Query: `Rockland County Spring Valley apartment building fire code enforcement multifamily inspections Ramapo 2024` · WebSearch → WebFetch https://hudsonvalley.news12.com/rocklands-office-of-buildings-and-codes-reflects-on-2-year-anniversary-of-taking-over-inspections-code-enforcement-in-village-of-spring-valley
- Finding: Feb 14 2024 = two years since the county office took over Spring Valley inspections (state-designated since Feb 14 2022); 2,000+ inspections, 12,400+ alleged violations, ~500 complaints, nearly $500,000 fines.
- Used: §8.5 callout; county section (Rockland); §5.5 bullet.

**H16 — Aggregator cost claims (AI Overview substitute).**
- Query: `apartment building security camera system cost per camera installation Angi OR Fixr OR HomeAdvisor` · WebSearch → WebFetch https://cost-guide-ssr.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera
- Finding: national average $1,298; typical $593–$2,040; $125–$450 per camera incl. labor; 4-camera CCTV ~$1,300; labor 50–70% of total; page updated Oct 18 2022.
- Fixr page redirected (https://www.fixr.com/costs/install-video-surveillance-cameras) — not fetched → not used.
- Used: §10.5 H3 1 (quoted then corrected).

**H17 — Census QuickFacts, owner-occupancy and median gross rent (2020–2024 ACS).**
- WebFetch https://www.census.gov/quickfacts/fact/table/{county}countynewyork/HSG445223 for each county.
- Findings: Westchester 61.8% owner-occupied, median gross rent $1,951, 372,883 households; Rockland 67.9%, $1,901, 103,879; Orange 67.8%, $1,680, 138,608; Putnam 83.8%, $1,775, 35,545; Dutchess 69.2%, $1,582, 116,275; Ulster 69.9%, $1,425, 74,278.
- Used: §5.5 bullets; county-by-county section; §14 pricing context.

**H18 — Palisades Center.** WebFetch https://en.wikipedia.org/wiki/Palisades_Center — West Nyack; opened March 4 1998; 2,217,322 sq ft. → §13 card.
**H19 — Woodbury Common.** WebFetch https://en.wikipedia.org/wiki/Woodbury_Common_Premium_Outlets — Central Valley section of Woodbury, Orange County; opened 1985; 220 stores. → §13 card.
**H20 — Stewart International Airport.** WebFetch https://en.wikipedia.org/wiki/Stewart_International_Airport — in towns of Newburgh and New Windsor, ~60 miles north of Manhattan; 1930s West Point cadet airfield; Port Authority-operated since 2007; 105th Airlift Wing. → §13 card.
**H21 — Beacon Metro-North TOD.** Query `Metro-North Poughkeepsie station OR Beacon station transit oriented apartments new construction Hudson Valley 2025 units` · WebSearch → WebFetch https://www.governor.ny.gov/news/governor-hochul-announces-development-partner-build-transit-oriented-housing-beacon-metro — July 30 2025: 265 mixed-income homes on state-owned lot next to Beacon station, at least 10% affordable, new parking garage. → §7 new-construction card; §13 card.
**H18b — reused from soundbar HV research (research/soundbar-installation.md):** Walkway Over the Hudson 212 ft above river, 1.28 miles; Kingston Stockade District = NHL district on site of Dutch settlement Wiltwyck. → §13 cards (text rewritten).

**H22 — Garden apartment definition + Poughkeepsie example.**
- Query: `"garden apartment" complex Westchester OR Rockland OR Orange OR Dutchess built 1950s 1960s units news` · WebSearch → WebFetch https://www.fireengineering.com/fire-safety/building-construction/building-comprehension-for-the-fire-service-understanding-garden-apartments/ — suburban garden apartments are low-rise complexes in green space, generally up to three storeys, without standpipes and elevators, nearby parking; mid-1960s+ Type V wood frame; older Type III masonry; late-1940s–1970s often precast concrete plank and block walls; stair types: sidewall entry return stairs (~2 units/floor), center hall, balcony type; garden level half below grade.
- WebFetch https://re-nj.com/kislak-pairs-longtime-clients-inks-sale-of-poughkeepsie-apartments-for-8-4-million/ — Jan 28 2026: Hamilton Garden Apartments, 92-96 South Hamilton St, Poughkeepsie: 58 units, seven two-storey brick buildings built 1925–1965, 2.55 acres, four laundry rooms, 70 parking spaces, resident super; ~98% occupied; not rent-controlled; buyer plans capital improvements.
- Used: §5 para 1; §7 garden-complex card + 7.5 table; §9 coverage cluster; §10.5 H3. (Page does NOT claim AESS worked there.)

**H23 — reused from cat6-repair HV research (research/cat6-repair.md):**
- Times Union June 27 2024 (https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php): storms left a combined 60,000 Orange & Rockland and Central Hudson customers without power; winds about 60 mph. → §5.5 bullet; §9 power Q.
- Stacker (Census) Sept 25 2025: Westchester 28% of homes built 1939 or earlier; Rockland 11.5%; Dutchess 18.0%; Ulster 25.3%. → §7 river-town card.
- Ulster ConnectALL: $20.8M, ~1,300 unserved locations (Sept 25 2025). → §9 remote-viewing Q.
- Central Hudson Dig Safely / 811 notice before excavation. → §8.5 trenching callout; §9 trenching Q.

---

### C. Question register — this page (all Hudson Valley-specific)

§9 Questions Answered (H3):
1. What does a garden-apartment complex in the Hudson Valley budget for cameras, county by county?
2. Why does the same camera count cost more in Dutchess or Ulster than in Westchester?
3. Our complex has eight buildings spread over several acres — do we need a recorder in every building?
4. Which spots on a garden complex get covered first when the budget is tight?
5. Can cameras cover the half-below-grade garden-level entrances and the breezeways between buildings?
6. Our surface lot has no conduit — do you trench, go wireless, or mount on the light poles?
7. Will cameras actually read plates in an unlit lot off Route 59 or Route 9 at 2 a.m.?
8. Do you have to call 811 before trenching across our property?
9. What happens to the cameras when Central Hudson or O&R loses power for a day?
10. Our building is on a slow rural line — can owners still watch cameras remotely?
11. How do cameras handle ice storms and drifting snow on the north side of the buildings?
12. We're in a Good Cause Eviction city — does adding cameras change anything with our tenants?
13. Our Kingston building is rent-stabilized under ETPA — is a camera system a service change for tenants?
14. Outside New York City, which state law covers our apartment building — the Multiple Dwelling Law or something else?
15. Can a camera go in a laundry room or a shared restroom at a Hudson Valley complex?
16. A tenant asked for footage of a car break-in — do we have to hand it over?
17. Do cameras in a Hudson Valley lobby or mailroom need audio turned off?
18. Does our county require a home-improvement licence for a camera installer?
19. Our Spring Valley building gets county code inspections — will cameras be looked at?
20. We inherited an analog system from the last owner — can it be reused?
21. Can you take over a system another installer left with no passwords?
22. Will the cameras work with the Akuvox or ButterflyMX intercom at our lobby door?

§17 FAQ (accordion + FAQPage):
1. Do you install in all six Hudson Valley counties, including the rural parts of Ulster and Dutchess? (distinct from old "Do you serve all six Hudson Valley counties?" — reworded intent: rural reach + scheduling)
2. How quickly can you walk a complex in Westchester or Rockland compared with upstate?
3. Which Hudson Valley municipalities have adopted Good Cause Eviction?
4. Do you work with HOA, condo and co-op boards in the valley, or only landlords?
5. Can one app show several complexes in different counties?
6. Do you install cameras on new transit-oriented buildings while they are under construction?
7. Can the super or a management company get alerts after hours?
8. What warranty comes with a Hudson Valley apartment camera system?
9. Can you add cameras to a detached garage, carport row or storage building?
10. Do you remove the old cameras and cable when you replace a system?

Questions deliberately avoided (already in silo register): "How many cameras does an apartment building need?", "Which camera brands do you install?", "NVR or cloud", "Can building cameras record audio?", "Do we have to notify residents", "Do we need a licensed contractor", "Do you service buildings that already have cameras?", "How much does … cost in the Hudson Valley?", "Do you serve all six Hudson Valley counties?".

---

### D. Not found / EMPTY (stated honestly, nothing invented)
- Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★: EMPTY (not accessible in build env).
- r/hudsonvalley threads specifically about apartment-complex cameras: EMPTY.
- A sourced, real AESS Hudson Valley apartment job anecdote: none in the build env → Field Notes written as general installer practice and labelled so.
- Drive folder `AESS Website Photos/Apartment Building Security Camera Installation`: does not exist (Drive search 2026-10-18). CompanyCam via Composio: no active connection. → images borrowed under the permanent rule (see DAILY-LOG note).
- Whether NYS DOS treats camera-only systems as covered by GBL Art. 6-D: not stated on DOS page → page does not claim it.

---

### E. Build notes
- Pricing: silo Brooklyn base from the live Brooklyn/NYC pages of this silo ($500–$1,500 per camera; 4–8 cams $5,000–$12,000; 12–20 cams $12,000–$25,000; 24–40 cams $25,000–$45,000+) × v2.3 §9 county multipliers (Westchester 1.25, Rockland 1.30, Orange 1.40, Putnam 1.45, Dutchess/Ulster 1.53). Service rate $195/hr, 3-hr min ($585) per v2.3 §9. No other prices used.
- Images: 11 borrowed under the permanent rule — 7 from images/parking/, 4 from images/commercial-security/, converted to WebP and renamed into images/apartment-building-security-camera-installation/ with -hudson-valley- filenames; alt/title/caption describe only what is visible.
- Extra sections (Problem to Camera, Before We Arrive, Seasonal Upkeep, Retention and Export, Phasing, Who Calls Us, Footage Policy) are installer practice, no external facts.

## Long Island hub (merged from batch builder, 2026-10-18)

## Research — Apartment Building Security Camera Installation · Long Island hub

Page: `apartment-building-security-camera-installation-long-island` (REBUILD, in place). Built 2026-10-17 by a parallel batch builder.
Silo-wide research file `research/apartment-building-security-camera-installation.md` is being written by the Brooklyn builder in the same batch — this file holds the hub-level silo research done for this page plus the Long Island local research, for the main run to merge as a `## Long Island` section.

Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used.

### Surfaces not reachable in this build environment

| # | Source | Status |
|---|---|---|
| 1 | Google PAA for "apartment building security cameras long island" | EMPTY (not accessible in build env) |
| 2 | Google PASF | EMPTY (not accessible in build env) |
| 3 | Answer the Public | EMPTY (not accessible in build env) |
| 4 | Google AI Overview (live SGE panel) | EMPTY (not accessible in build env). §10.5 "Reality Check" is framed around the generic claims repeated across the cost-guide pages that rank for the query (see S1–S3) and the old template text this rebuild replaces, not a quoted live AI panel. |
| 5 | Yelp 1–3★ for Long Island camera installers | EMPTY (not accessible in build env) |
| 6 | Bing / DuckDuckGo PAA | EMPTY (not accessible in build env); WebSearch results used as cross-check (S1). |
| 7 | Reddit threads (full text) | Excerpts only via Firecrawl search (R1–R3); full threads not opened. |

### Silo / hub-level findings

| ID | Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|---|
| S1 | `apartment building security camera installation Long Island cost per camera` | WebSearch | https://blog.zositech.com/security-camera-installation-cost/ ; https://www.123securityproducts.com/blogs/post/what-is-the-average-security-camera-installation-cost.html ; https://www.eufy.com/blogs/security-camera/security-camera-installation-cost-is-it-worth-it | Ranking results for the query are national, single-family/DIY cost guides and manufacturer blogs, not multifamily-specific. | §10.5 H3 "national per-camera averages" (framing only; no figures quoted) |
| S2 | `New York Labor Law 203-c video recording restroom locker room; Penal Law 250.45 unlawful surveillance apartment` | WebSearch → Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/LAB/203-C | "No employer may cause a video recording to be made of an employee in a restroom, locker room, or room designated by an employer for employees to change their clothes, unless authorized by court order." | §8.5 compliance callout; Q&A "super's office / staff room" question |
| S3 | same query | WebSearch | https://www.womenslaw.org/laws/ny/statutes/sec-25045-unlawful-surveillance-second-degree | Penal Law § 250.45 (unlawful surveillance, second degree) — recording a person where they have a reasonable expectation of privacy. | §8.5; §10.5 H3 on placement inside units |
| S4 | `New York Penal Law 250.05 eavesdropping mechanical overhearing of a conversation one-party consent` | Firecrawl search (gov) | https://nysenate.gov/legislation/laws/PEN/250.05 ; https://nycourts.gov/reporter/3dseries/2016/2016_02556.htm | Eavesdropping is a class E felony; "mechanical overhearing" = recording a conversation "without the consent of at least one party thereto, by a person not present thereat" (Penal Law § 250.00[2], quoted in People v Badalamenti, 2016). | Q&A audio question; §8.5; FAQ |
| S5 | `Suffolk County Department of Consumer Affairs license home improvement contractor low voltage security alarm installer licensing requirement` | Firecrawl search | https://dos.ny.gov/get-security-or-fire-alarm-installer-license ; https://www.nsca.org/resources/guide-to-state-licensing/ | NYS DOS licenses Security or Fire Alarm Installers (18+, at least 81 hours qualifying education). NSCA summary: NY license covers CCTV "if such system is used, either full-time or part-time, for the detection or monitoring of intrusion, break-in, theft, movement, sound, or fire". | §8.5 licensing callout; Q&A licensing question; §10.5 H3 |
| S6 | same query | Firecrawl search | https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License ; https://ecode360.com/14947425 | Suffolk Consumer Affairs "licenses over 15,000 vendors"; "Over 50% of the licenses issued or renewed each year are home improvement licenses"; consumer line (631) 853-4600 [not printed on page — non-AESS phone]. Suffolk Code Ch. 563 Art. II: unlawful to engage in home improvement contracting on residential property without a license. | §8.5 callout; Nassau-vs-Suffolk section |
| S7 | same query | Firecrawl search | https://www.liconstructionlaw.com/construction/licensing-requirements-for-home-improvement-contractors-subcontractors-in-new-york-state/ | Both Nassau and Suffolk require county home-improvement licensing for many classes of residential work; towns/villages add their own registration, insurance and permitting. | §8.5; Nassau-vs-Suffolk section |

### Long Island local research

| ID | Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|---|
| L1 | carried from research/smart-lock-installation.md (LI hub rows) and research/sonos-installation.md | Census QuickFacts | https://www.census.gov/quickfacts/nassaucountynewyork ; https://www.census.gov/quickfacts/suffolkcountynewyork | Owner-occupied 81.9% Nassau / 82.2% Suffolk (2020–2024); housing units 480,591 / 583,777 (July 1 2025); households 458,166 / 512,565; persons per household 2.99 / 2.93. Renter share derived as roughly 18% (100 − owner-occupied). | §5 para 1; §5.5 bullets 1–3 |
| L2 | `Nassau County Emergency Tenant Protection Act villages rent stabilized apartments Glen Cove Great Neck Plaza Long Beach` → `HCR list of municipalities ETPA Nassau County …` | WebSearch → Firecrawl search | https://hcr.ny.gov/housing-services | HCR lists ETPA localities in Nassau: Cities of Glen Cove, Long Beach; Town of North Hempstead; Villages of Cedarhurst, Floral Park, Flower Hill, Freeport, Great Neck, Great Neck Plaza … | §5 para 3; §13 landmark cards (Glen Cove, Long Beach, Great Neck Plaza); Q&A rent-stabilized question; FAQ |
| L3 | same | Firecrawl scrape (directQuote) | https://rentcheckme.com/articles/rent-stabilization-in-nassau-county-ny | ETPA coverage: buildings with 6+ units built Feb 1 1947 – Jan 1 1974 in opted-in municipalities; administered by DHCR; Nassau County Rent Guidelines Board sets annual increases. (Its claim that the Town of Hempstead opted in is NOT used — HCR list shows North Hempstead.) | §5 para 3; Q&A rent-stabilized question |
| L4 | `Town of Hempstead accessory apartment permit owner occupied rules` | WebSearch → Firecrawl scrape | https://liherald.com/stories/curbing-illegal-housing-through-accessory-apartments,65361 | Herald: unincorporated Town of Hempstead has "more than their fair share of illegal rentals"; Hempstead's accessory-apartment policy applies only to immediate family and senior citizens; Town of Huntington allows anyone if owner-occupied, permits since 1992, 1,593 accessory apartments at time of article, permit $175/yr, lot min 7,500 sq ft / 75 ft frontage, unit 300–650 sq ft. | §7 building card "two-family & accessory apartments"; Q&A accessory apartment question |
| L5 | `Newsday apartment complex Long Island package thefts OR catalytic converter thefts …` | Firecrawl search → Firecrawl scrape | https://www.cbsnews.com/newyork/news/catalytic-converter-thefts-on-long-island-more-than-quadrupled-from-2021-to-2022/ | Nassau catalytic converter thefts: 2019: 1; 2020: 100; 2021: 472; 2022: 2,292. Suffolk: 2021: 282; 2022: 1,581 (CBS New York, Jan 30 2023). | §5 para 2; §5.5 bullet; parking-lot Q&A |
| L6 | same search | Firecrawl search | https://www.fox5ny.com/news/massive-spike-catalytic-converter-thefts-long-island | Suffolk: 819 stolen Jan–late Aug vs 289 the prior full year (excerpt; year per article). | Not used (year not confirmed in excerpt) |
| L7 | `Wyandanch Rising Ronkonkoma Hub Patchogue New Village apartments transit-oriented development Long Island` | WebSearch → Firecrawl scrape | https://www.cnu.org/node/1458 | Town of Babylon's Wyandanch Rising: 40-acre first phase, 750–1,050 dwelling units planned around a new plaza at the Wyandanch LIRR station; plan included a 2,000-car garage (2011 RFQ article). | §13 landmark card; §7 TOD building type |
| L8 | `New Village at Patchogue apartments units; Ronkonkoma Hub apartments units; …` | Firecrawl search | https://tritecre.com/project/new-village/ | New Village at Patchogue: 291 apartment homes. | §13 landmark card; §8 corridors |
| L9 | same | Firecrawl search | https://www.newsday.com/business/patchogue-carriage-house-luxury-apartments-wbz7wtrl | A new 262-unit luxury apartment development underway in Patchogue village (excerpt). | §8 Patchogue corridor |
| L10 | same → governor release | Firecrawl scrape (directQuote) | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Oct 22 2024: Station Yards (Ronkonkoma Hub), 53 acres around the Ronkonkoma LIRR station; phase 1 Alston Station Yards delivered 489 units in 2020; phase 2 "The Core" adds 388 homes, 67,000 sq ft retail, 16,500 sq ft office, a public plaza and 1,200+ parking spaces; release headline: more than 1,400 housing units. | §13 landmark card; §7 TOD mid-rise card; §8 corridor |
| L11 | `reddit r/longisland apartment complex security cameras landlord` | Firecrawl search (excerpts) | https://www.reddit.com/r/longisland/comments/10plgip/catalytic_converter_thefts_on_long_island_more/ | r/longisland commenter: "People say you can steal one in like 30 seconds. Can be difficult to catch. My neighborhood implemented no on street parking from 11pm-5am." | §5 para 2 (paraphrased resident concern) |
| L12 | same | Firecrawl search (excerpt) | https://www.reddit.com/r/Landlord/comments/1t0ef4d/landlord_usny_can_i_have_cameras_in_the_outside/ | NY landlord thread: "It is normal to have security cameras in apartment complexes. Having ones that record sound bring another element into it." | Q&A audio question (framing) |
| L13 | same | Firecrawl search (excerpt) | https://www.reddit.com/r/legal/comments/1j02505/is_this_legal_in_ny/ | NY tenant surprised by landlord installing a camera in the common area during a repair visit. | Q&A tenant-notice question (framing: tell residents first) |
| L14 | `Long Island garden apartment complexes built 1950s 1960s Hempstead Freeport Hicksville history` | WebSearch | (Levittown/Levitt list, LI History Journal review) | No usable garden-apartment-specific facts returned. | EMPTY for specific complex histories — page describes garden-apartment building form generically, names no private complex. |
| L15 | `Long Island garden apartments shortage multifamily housing Nassau Suffolk percentage rental units` | WebSearch → Firecrawl scrape | https://rauchfoundation.org/news-resources/archive/why-is-it-so-hard-to-build-multifamily-housing-on-long-island ; https://s3.documentcloud.org/documents/24494313/long-island-index-findings-on-status-of-multifamily-housing.pdf | Rauch page 404; LI Index PDF unreachable by scraper. | EMPTY (not accessible in build env) — no multifamily-share stat used. |

### Questions used on this page (add to the silo question register)

#### §9 Questions Answered (H3)
1. Our garden apartment complex has eight separate two-storey buildings — does every building need its own recorder?
2. How do you get camera cable from building to building across a Long Island complex without tearing up the lawns?
3. What should the cameras in a garden-complex parking lot actually be able to show after a catalytic converter theft?
4. Can a co-op board in Nassau put cameras in the hallways without a shareholder vote?
5. Who should hold the passwords in a condo where the managing agent changes every few years?
6. Does a rent-stabilized building in an ETPA village have to tell DHCR or tenants before adding cameras?
7. Can a homeowner with a legal accessory apartment put a camera on the shared side entrance?
8. Is it legal to point a camera at the laundry room or the super's workshop in a New York building?
9. Our property straddles a village line — whose permit rules apply to the camera work?
10. Does a mid-rise near an LIRR station need different cameras than a garden complex?
11. How long should a Long Island apartment property keep footage before it records over?
12. How do we hand footage to Nassau or Suffolk police without giving them our whole system?
13. Can the old analog cameras on a 1960s complex be kept while we upgrade?
14. What happens to the cameras when a nor'easter knocks out power to the complex?

#### §17 FAQ
1. Do you install apartment building cameras in every Nassau and Suffolk town?
2. Is the Long Island hub price the same as the Nassau or Suffolk county page?
3. Can our managing agent approve the work, or does the board have to sign?
4. Will you work around tenants who are home during the day in a garden complex?
5. Do you supply a certificate of insurance naming the co-op, condo association or owner LLC?
6. Can residents view the cameras from their phones?
7. Do you charge a monthly fee for the camera system?
8. What does the warranty cover on a Long Island building system?
9. Can you add cameras to a building intercom or entry system you did not install?
10. How quickly can you come out if a camera or recorder fails?
11. Do you need access to every apartment during the install?
12. What do you need from us before the first walkthrough?
</content>
</invoke>
