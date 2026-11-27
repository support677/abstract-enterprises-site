# Research — Condo Security Systems silo (condo-security-systems-*)

Created Nov 26 2026 by the NYC hub builder (batch: condo-security-systems-nyc, -manhattan, -brooklyn). Silo-wide research and the **question register** live here. Area builders: add a `## <area>` section with local research and append your page's questions to the register. Before writing any Q&A/FAQ question, check the register AND the co-op register in `research/co-op-security-systems.md`: no repeated question or intent within the silo, and never copy co-op wording (BLUEPRINT §12.3).

Keyword lists and rules: `keywords/condo-security-systems.md` (+ intercom-section phrasing from `keywords/condo-intercom-replacement.md`).

---

## Silo-wide research (v2.3 §3, §12.4 format: exact query · platform · URL · finding · used)

### Live SERP / question surfaces
| # | Source | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|---|
| S1 | Google PAA | — | — | EMPTY (not accessible in build env) | — |
| S2 | Google PASF | — | — | EMPTY (not accessible in build env) | — |
| S3 | Answer the Public | — | — | EMPTY (not accessible in build env) | — |
| S4 | Google AI Overview | — | — | EMPTY (not accessible in build env). The NYC page's "What AI gets wrong" section answers recurring generic claims from vendor/aggregator/chatbot content, not a captured AI Overview. | — |
| S5 | Bing / DuckDuckGo | — | — | EMPTY (not accessible in build env) | — |
| S6 | Yelp 1–3★ | — | — | EMPTY (not accessible in build env) | — |
| S7 | Reddit | `condo security systems NYC intercom access control condo board` · Firecrawl search | https://www.reddit.com/r/accesscontrol/comments/1ilrbey/help_access_control_system_recommendations_for/ | Search snippet only (page scrape failed — blocked): small condo association asking for access control + intercom recommendations; replies list brand options. Thread body EMPTY (not accessible in build env). | Angle only: small/boutique condo boards want simple admin (NYC §7 boutique card, size tiers) |
| S8 | SERP head term | same query · Firecrawl search | imperasecurity.com/co-op-condo-security; paxsecurity.com/industries/multi-family; connextivity.com (apartment/condo access control guide); paragonsecurityny.com (video intercoms for condos/HOAs); uasecurity.com blog; nimbio.com | Ranking pages are vendor service pages combining co-op+condo; none gives a starting price, condo-law definitions (RPL 339-e/339-v), sponsor-handover advice or credential-cloning detail. | NYC hub angle: $250 answer-first, Condominium Act citations, sponsor transition, encrypted-credential upgrade |
| S9 | Press | `condo board intercom upgrade New York unit owners habitatmag OR cooperatornews` · Firecrawl search | habitatmag.com (Forest Hills co-op video intercom 2019), cooperatornews.com/article/the-old-fashioned-intercom-is-getting-a-makeover, avvo.com (condo intercom responsibility Q&A) | Avvo snippet: responsibility for a condo intercom "would depend upon a review of" the governing documents → supports "depends on declaration and bylaws" answer (not cited on page). | Q&A who pays for in-unit handset (framing) |

### Condo law, governance and housing facts
| # | Exact query · platform | URL | Finding | Used (NYC page) |
|---|---|---|---|---|
| L1 | `New York Real Property Law 339-d definitions common elements unit condominium` · WebSearch → Firecrawl scrape | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | RPL §339-e (2025 text). "Common elements," unless the declaration provides otherwise, include "(b) ... halls, corridors, lobbies, stairs, stairways, fire escapes, and entrances and exits of the building; (c) The basements, cellars, yards, gardens, recreational or community facilities, parking areas and storage spaces; ... (f) ... all apparatus and installations existing for common use". "Operation of the property" = administration/operation and "the maintenance, repair and replacement of, and the making of any additions and improvements to, the common elements". "Unit owner" = person owning a unit in fee simple. (339-d is only the short title; nysenate.gov/legislation/laws/RPP/339-D WebFetch was blocked, Firecrawl returned no body.) | §5 para 2 quote + facts list; rules list; AI check #1 |
| L2 | `law.justia.com 339-v` · Firecrawl scrape | https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | RPL §339-v: bylaws must provide for the board of managers' election, "the powers and duties of the board", "whether or not the board may engage the services of a manager or managing agent", methods of calling unit owners' meetings and the percentage "necessary to adopt decisions binding on all unit owners", "Method of adopting and of amending administrative rules and regulations governing ... the common elements"; may provide for "reserves, to provide for major and minor maintenance, repairs, additions, improvements, replacements". | §5 para 4 + facts; rules list; Q&A funding + owner vote; AI check #5 |
| L3 | `number of condo units New York City` · Firecrawl scrape (query mode) | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-homeowner-housing-market/ | NYC Comptroller, March 12, 2024: "there are 450,000 occupied apartments in cooperative buildings and another 318,000 in condominiums, together accounting for 22% of the city's occupied housing stock." "18% of condo units citywide are owned by LLC's; in Manhattan, the corresponding figure is 21%." (NYCHVS 2023; DOF tax records) | §5 paras 1 and 3 + facts list |
| L4 | reused, verified in research/co-op-security-systems.md L5 (→ research/intercom-repair.md G1/G2) | https://www.nysenate.gov/legislation/laws/MDW/50-A ; https://nysenate.gov/legislation/laws/mdw/3 | MDL §50-a intercom/self-locking door requirement for class A multiple dwellings erected/converted after Jan 1 1968 with 8+ apartments; older on majority written request; MDL §3: cities of 325,000+. | Facts list; rules list |
| L5 | reused, verified in research/co-op-security-systems.md L3/L4 | https://intro.nyc/local-laws/2021-63 ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Tenant Data Privacy Law (LL 63/2021): smart access building = class A multiple dwelling; privacy policy, express consent, no requirement to use smart access to enter own unit, 90-day destruction unless anonymized; text has no co-op/condo exemption. Page says application to owner-occupied condo units is for counsel. | Facts list; rules list; Q&A privacy law |
| L6 | reused, verified in research/co-op-security-systems.md L9/L10 | NYC BC 1010.1.9.8/1010.1.9.9 and Admin Code §28-105.4.7 (amlegal links in co-op file) | Electrically locked egress door rules; no electrical permit for <50 V signaling/data wiring (life-safety exceptions). | Rules list; cabling section; equipment table |
| L7 | same Firecrawl search as S9 → Firecrawl scrape | https://cooperatornews.com/article/the-old-fashioned-intercom-is-getting-a-makeover | CooperatorNews, John Zurz, Aug 3 2016. Joe Cioffi III (VP, Bergen Protective Systems): "There's a company out there that doesn't offer inside stations and is only web-based," ... "I find that to be a downside." Mike Brenner (Advance Security & Intercoms, Yonkers): "Intercoms have become a lot more reliable, and the access features are expanded to include things like fingerprints and key fobs." | RFP section quote (Cioffi) |
| L8 | reused, verified in research/co-op-security-systems.md L7 | https://cooperatornews.com/article/replacing-intercom-systems | CooperatorNews Nov 14 2025 (wiring lifespan / retain infrastructure). | Background only for the cable-reuse guidance; not quoted or cited on the condo page |

### Prices used (site-internal, verified by reading the pages Nov 26 2026)
- $250 service call — /intercom-pricing, /door-buzzer-repair-pricing; START_PRICES in tools/check_page.py (Anwar Nov 25 2026).
- $1,200–$5,000+ multi-unit intercom, 5–30 units — /intercom-installation-nyc.
- $3,000–$8,000 installed, 30-unit building, 125 kHz → encrypted/mobile credentials — /access-control-installation-nyc (also the source of the "fixed ID can be read and copied" fob-cloning point).
- $45/mo app, $30/mo keypad monitoring — site monitoring tiers (profile).
- Financing: "available through Wisetack, subject to approval" (one line). No maintenance-contract, camera, elevator or fire alarm prices.

### Silo keyword plan (five layers)
- **Service:** condo security systems, condo building security, condominium security systems, condo intercom system / replacement / upgrade / modernization (intercom section), condo access control / key fobs, condo elevator access control, condo door buzzer, condo security cameras (short; links to condo camera silo when live), condo alarm, maintenance, integration, RFP.
- **Problem:** stale fobs from renters/sellers, cloneable 125 kHz fobs, sponsor accounts never transferred, panel dark / units silent / door release fails, package theft, guest/short-term access, amenity misuse.
- **Technology:** video/IP/app intercom, two-wire/multi-wire reuse, encrypted credentials, mobile credentials, long-range garage tags, mag lock vs strike, REX, NVR, PoE, UPS, cloud vs on-site management.
- **Industry/audience:** condo boards of managers, HOA boards, unit owners, renters of owners, managing agents, resident managers/supers, sponsors/developers; luxury towers, conversion condos, boutique condos, townhouse/HOA communities, mixed-use condos, multi-building complexes.
- **Geographic:** NYC hub uses NYC/New York City + borough mentions in the borough paragraph; each area page uses only its own area.

### Images (NYC page)
11 images copied into images/condo-security-systems/ with -nyc- filenames from images/access-control-installation/ (olinville doorbell station, bensonhurst video door station, bath-beach surface door station, ridgewood patch cables, pelham-bay mini dome + speaker, ridgewood walkway view) and images/apartment-building-security-camera-installation/ (westchester turret between light panels, suffolk mini dome, long-island bullet + sensor, queens turret under yellow fascia, staten-island recorder split view). sha256 checked: none matches any file in images/co-op-security-systems/, images/co-op-board-intercom-upgrade/ or the condo Brooklyn images present at build time; contact-sheet compared visually to avoid the co-op photos (storeroom, back-hall door, stone-facade arm, lobby soffit, touchscreen directory, keypad card-band station). Product photos show manufacturer logos (Akuvox on the surface door station); no faces, house numbers, phone numbers or "AESS". DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + images/apartment-building-security-camera-installation/ (no real condo photos yet)`.

---

## Question register (every Q&A / FAQ / "?" heading used on any condo-security-systems page)

### condo-security-systems-nyc (Q&A §9)
- What will a building-wide condo security upgrade cost, and why can't anyone price it over the phone?
- How do condo boards usually fund an intercom or access control replacement?
- Is financing available for a condominium security project?
- Does a condo board need a unit owner vote to replace the building intercom?
- What should a condo board send unit owners before the work starts?
- Who pays to fix the intercom handset inside a condo unit: the owner or the association?
- Can a condo replace its intercom without wiring work inside every unit?
- How do we know our condo intercom is due for replacement rather than another repair?
- What happens to fobs and app access when a condo owner sells or a renter moves out?
- Does New York City's smart-access privacy law apply to condominium buildings?
- Can an owner add a video doorbell or camera at their own unit door?
- Who should be allowed to view and export condo camera footage?
- How do you keep residents getting in while the entrance system is being replaced?
- What records should a condo association keep once the new system is in?
- What paperwork does a managing agent typically ask a condo security contractor for?

### condo-security-systems-nyc (FAQ §17)
- Do you install and repair condo security systems in all five boroughs?
- Are you licensed and insured to work in New York City condominium buildings?
- What warranty does a condo security installation carry?
- Can you take over a condo system that the sponsor or another company installed?
- Do you provide a virtual doorman or remote concierge service for condos?
- Will our condo association pay a monthly fee after the new system goes in?
- Can you prepare a proposal in the format of our condo board's RFP?
- Can you share references from other condo buildings you have worked in?
- How soon can a technician come out to a condo whose entrance door or intercom has failed?
- Do you run the electrical circuits for new condo security equipment?
- Do you work on fire alarm systems in NYC condominiums?
- Can our condo buy the equipment and hire you only to install it?

---

## nyc

NYC hub (up-link /, phone (800) 486-0943 only, Brooklyn GBP). Uses the silo research above; no neighborhood-level research needed for the hub. Local items used:

| # | Item | Source | Used |
|---|---|---|---|
| N1 | Borough condo character (Manhattan towers/conversions; Brooklyn waterfront/downtown towers + brownstone/loft conversions; Queens LIC high-rises + low-rise/attached communities; Bronx postwar/infill/Riverdale; Staten Island townhouse/HOA communities) | General building-stock description, no statistics claimed; the 21% Manhattan LLC-owned figure is the only borough number (L3) | Coverage section borough paragraphs |
| N2 | Landmark cards: Hudson Yards & West Chelsea, Financial District (office-to-residential conversions), Long Island City waterfront, Downtown Brooklyn & Williamsburg/Greenpoint waterfront, Riverdale, Staten Island townhouse communities | Real, well-known districts; described by building type only, no client addresses, no counts | Coverage cards |
| N3 | Offices 1282 Troy Ave (Brooklyn GBP) and 460 E Fordham Rd | Site NAP | Coverage + FAQ 1 + footer |

FLIP links left as plain text on the NYC page: /condo-intercom-replacement, /condo-security-camera-installation-nyc, /condo-security-systems-queens, /condo-security-systems-bronx, /condo-security-systems-staten-island, /condo-security-systems-long-island, /condo-security-systems-hudson-valley.


## brooklyn

## Brooklyn — local research for `condo-security-systems-brooklyn` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: WebSearch, Firecrawl search, Firecrawl scrape (directQuote query mode, PDF parser, raw JSON from the NYC Open Data SODA API). Rows marked "reused" were verified by co-op silo builders (research/co-op-security-systems.md) and re-read here only where noted.

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | R1–R2 (excerpts via Firecrawl search). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects claims typical of national cost guides / AI summaries (Angi, HomeAdvisor, Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | L1–L6 (general geography; rezoning context from Z1–Z3) |
| 7 | Building stock / use cases | Z1–Z4, field observation (brownstone conversions, boutique walk-ups: described qualitatively, no statistic claimed) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | CBS New York (Z2), 6sqft (Z3), Planetizen (Z1b) |
| 10 | Hyperlocal | EMPTY — searched Brownstoner for small brownstone condo conversions; only listings/forum threads, nothing citable; not used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env); not used. |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| G1 | `New York Real Property Law Article 9-B condominium act 339-v bylaws board of managers contents` · WebSearch → Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/RPP/339-V | Bylaws must provide for "the powers and duties of the board"; "whether or not the board may engage the services of a manager or managing agent or both"; "Operation of the property, payment of the common expenses and determination and collection of the common charges"; "Method of adopting and of amending administrative rules and regulations governing the details of the operation and use of the common elements"; reserves for "major and minor maintenance, repairs, additions, improvements, replacements". | §5 para 2; stamp |
| G2 | (same search, result) · Firecrawl scrape PDF | https://ag.ny.gov/sites/default/files/2022-08/how_to_handle_problems_with_a_condo_board.pdf | "Boards of Managers in condominiums have two basic legal obligations. The Board must follow the condo's internal rules (as set forth in the by-laws, the condominium declaration and the house rules)"; declaration, by-laws, floor plans, rules "available for inspection". | §5 para 3 |
| Z1 | `Downtown Brooklyn 2004 rezoning residential towers condos NYC Department of City Planning` · WebSearch → Firecrawl scrape PDF | https://www.nyc.gov/assets/planning/download/pdf/about/press-releases/pr051004b.pdf | May 10 2004 CPC approval; "as much as 5.4 million square feet of new commercial space and about 1,000 units of housing". | §5 "younger stock"; facts list |
| Z1b | same search · Firecrawl scrape | https://www.planetizen.com/news/2019/09/106422-2004-rezoning-didnt-predict-wave-residential-development-downtown-brooklyn | 2016 BP report: "more than 11,000 housing units had gone up in the area in the first dozen years since the rezoning, while the city had anticipated only 979." | §5; facts list |
| Z2 | `Greenpoint-Williamsburg rezoning approved May 2005 "175 blocks" waterfront` · Firecrawl search (excerpt) | https://www.cbsnews.com/newyork/news/williamsburg-greenpoint-rezoning-20-years-later/ | "The 2005 rezoning of 175 blocks along Brooklyn's waterfront reshaped the skyline and the community." (DCP FEIS exec summary scraped too: CD1 proposal; no unit count extracted.) | §5; facts list; §13 Domino Park card |
| Z3 | `Gowanus neighborhood rezoning 2021 approved City Council 8,000 homes` · WebSearch → Firecrawl scrape | https://www.6sqft.com/nyc-council-approves-sweeping-gowanus-rezoning/ | Article dated Nov 24 2021, vote "on Tuesday" (Nov 23 2021); "upzone 82 blocks of Gowanus"; "nearly 8,500 units of housing". | §5; facts list; §13 Gowanus card |
| Z4 | `421-a tax exemption expired June 15 2022 485-x condominium nyc.gov` · Firecrawl search (excerpts) | https://www.nyc.gov/site/hpd/services-and-information/tax-incentives-485-x.page ; https://www.nysenate.gov/legislation/laws/RPT/485-X | 485-x benefits "available to Multiple Dwellings or Homeownership Projects that contain six or more dwelling units, commenced after June 15, 2022". Page says only that earlier projects fell under 421-a; no claim on how many Brooklyn condos used 421-a. | facts list |
| D1 | SODA `$select=communityboard,count(*)&$where=boro='BROOKLYN' AND upper(novdescription) like '%INTERCOM%' AND novissueddate between '2025-01-01T00:00:00' and '2025-12-31T23:59:59'&$group=communityboard` · NYC Open Data via Firecrawl scrape | https://data.cityofnewyork.us/resource/wvxf-dwi5.json (dataset https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5) | 2025 Brooklyn intercom violations by CB: 3=151, 14=125, 17=117, 9=113, 4=96, 8=91, 5=80, 16=64, 12=54, 1=45, 15=36, 7=34, 6=29, 10=27, 11=26, 2=25, 13=24, 18=20; total 1,157 (matches co-op row D1). CB→neighborhood labels are standard CB geography. Page caveat: mostly rental complaints, not a count of condo intercoms. | §5 "What fails…" + table; facts list |
| R1 | `reddit Brooklyn condo building package theft lobby intercom HOA board` · Firecrawl search (excerpt) | https://www.reddit.com/r/Brooklyn/comments/1v5vuus/package_theft_from_our_building_is_out_of_control/ | Title "Package theft from our building is out of control.. what can I do?"; reply suggests a parcel drop and distributing keys. | §5 "What Brooklyn unit owners say" |
| R2 | same | https://www.reddit.com/r/AskNYC/comments/h9hcsj/tips_for_packages_being_stolen_from_apt_lobby/ | "My apt building has a major problem with package theft. The condo board is asking for suggestions for solutions…" | §5 same para |
| G3 | reused (co-op G1) | https://www.nysenate.gov/legislation/laws/MDW/50-A | MDL §50-a: post-1968 class A, 8+ apartments; quoted phrases. | §8.5; facts list |
| G4 | reused (co-op G2) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-130977 ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Local Law 63 of 2021 "smart access system" definition; HPD: written data retention/privacy policy. No legal advice; applicability left to the association's attorney. | §8.5; §10 credentials |
| G5 | reused (co-op G3) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | Intercom panel "installed within or adjacent to a door opening", "one intercom panel" per opening, "neutral and discreet"; facade camera caps. | §7 brownstone subsection; §13 Park Slope card |
| L1–L6 | landmark geography (no building named) | — | Fulton Street Mall; Barclays Center / Atlantic Ave; Brooklyn Bridge Park; Domino Park; Gowanus Canal; Park Slope Historic District. | §13 cards |
| P1 | site price pages (internal) | /door-buzzer-repair-pricing , /intercom-pricing , /security-camera-pricing-brooklyn | $250 service call; ranges $250–$525, $250–$475, $325–$650, $450–$950, $650–$1,800, $850–$2,400 (verified in the price page HTML Nov 26). | §14 table; §15 cards |

### Brooklyn question register (this page) — add to the silo register
§9 Q&A (H3): Does a Brooklyn condo board need a vote of the unit owners to replace the lobby intercom? · Should a new Brooklyn condo pay for security from reserves or an assessment? · Is a broken apartment handset the owner's bill or the association's? · Can a unit owner hire you directly for something at their own door? · The sponsor still controls our building's intercom account. What can the board do? · Our Brooklyn condo's intercom app stopped ringing some owners. Is the panel broken? · Can renters in a Brooklyn condo get their own intercom access? · Is there an entry system for our Brooklyn condominium with no per-apartment monthly charge? · Will residents be locked out while the new entry panel goes in? · How do Brooklyn condos give couriers access without handing out the door code? · Can the gym and roof deck be scheduled differently from the lobby? · What should a Brooklyn condo do with fobs held by owners who sold years ago? · Who can view the camera footage in a Brooklyn condo? · May an owner mount a doorbell camera facing the shared corridor? · Our Brooklyn condo garage door is stuck open. When can someone come? · Do you work in Brooklyn condo towers that require union labor or after-hours work? · We are three owners in a converted brownstone with no agent. Will you take a job that small?

§17 FAQ: Do you set up virtual doorman service for Brooklyn condos? · Can a Brooklyn condo association finance a security project? · What warranty covers a condo security system you install in Brooklyn? · Which intercom and access brands do you service in Brooklyn condominiums? · Can you share references from other Brooklyn condo buildings? · Do you answer RFPs from Brooklyn managing agents? · Do you handle the electrical side of a condo intercom or lock install? · Do you schedule condo work on Saturdays and Sundays in Brooklyn? · Is the walk-through free for a Brooklyn condominium? · Do you work with HOA townhouse communities and gated condo developments in Brooklyn? · Can our Brooklyn condo book regular maintenance visits? · How far into Brooklyn does your Troy Avenue office travel for condo work?

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-brooklyn-` names. Job photos (5, sha256 AND visually not used on any co-op page): common-corridor-camera-beside-lit-exit-sign (hero/og; from access-control-installation …westchester-square…), mini-dome-camera-beside-ceiling-light-and-vent (…gowanus…), cable-bundles-above-equipment-rack (…south-williamsburg…), desktop-network-video-recorder (…westchester-square… product), date-stamped-camera-tiles-on-monitor (door-buzzer-repair …bay-ridge…; tiny tiles, no identifiable faces). Manufacturer product photos (6) — the co-op silo already used every intercom/reader product photo in the library, so these duplicate files on OTHER co-op pages (none on co-op Brooklyn): tall-face-and-card-lobby-entry-panel (co-op Queens), touchscreen-video-door-station-with-dual-cameras (co-op Nassau), access-controller-enclosure (co-op Nassau), keypad-card-reader-for-amenity-doors (co-op Staten Island), dark-keypad-entry-panel-with-directory-screen (co-op Queens), stainless-keypad-and-display-entry-station (co-op Nassau). Rejected: smart-lock-installation/aess-* and astoria door-hardware shots (look AI-generated; one shows branded gloves), elevator-access-control set, face-showing E18C panel.

### Links left for the main run (FLIP comments in the page)
- `/condo-intercom-replacement` (§6 intercom section)
- `/condo-security-camera-installation-brooklyn` (§6 cameras)
- `/condo-security-systems-queens`, `/condo-security-systems-bronx`, `/condo-security-systems-staten-island` (§19)
- Link back needed from /co-op-security-systems-brooklyn, /condo-security-systems-nyc, /condo-security-systems-manhattan; rules also ask for one contextual link back from /intercom-installation-brooklyn-new-york and /apartment-building-security-camera-installation-brooklyn.


## manhattan

# condo-security-systems-manhattan — local research + question list (part file)

Builder: batch subagent, Nov 26 2026. Silo research and the silo question register belong to research/condo-security-systems.md (NYC builder); the main run merges this part file into it.

## Research matrix (v2.3 §12.4)

| # | Source | Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|---|---|
| 1 | Reddit | not searched | Reddit | EMPTY (not accessible in build env) | — | — |
| 2 | Google PAA | not captured | Google | EMPTY (not accessible in build env) | — | — |
| 3 | PASF | not captured | Google | EMPTY (not accessible in build env) | — | — |
| 4 | Answer the Public | not captured | ATP | EMPTY (not accessible in build env) | — | — |
| 5 | AI Overview | not captured | Google | EMPTY (not accessible in build env); §10.5 written from common generic-answer claims, each corrected with sourced or first-hand facts | — | AI Overview Reality Check |
| 6 | Statute | "New York Real Property Law Article 9-B condominium act 339-v bylaws board of managers" | WebSearch + WebFetch | https://www.nysenate.gov/legislation/laws/RPP/339-V | Bylaws must cover election of board of managers, powers/duties, managing agent, "operation of the property, payment of the common expenses and determination and collection of the common charges" (1(f)); may provide funds for "major and minor maintenance, repairs, additions, improvements, replacements" (2(b)) | The Neighborhood ¶2 |
| 7 | Statute | Firecrawl scrape of MDL §50-a | Firecrawl | https://www.nysenate.gov/legislation/laws/MDW/50-A | Class A MDs erected/converted after 1/1/1968 with 8+ apartments need lobby intercom with voice + release; older buildings when majority of tenants request/consent in writing | Facts list; FAQ 1 |
| 8 | Local law | "NYC Tenant Data Privacy Act Local Law 63 of 2021 smart access building condominium applies owners 90 days" | WebSearch + Firecrawl | https://intro.nyc/local-laws/2021-63 | "Smart access building" = class A MD using smart access; written plain-language policy; express consent in writing or via app; destroy authentication data within 90 days unless anonymized; reference data of vacated tenant removed within 90 days | Facts list; Access Control ¶4; Q&A (unit sold); Board checklist #5 |
| 9 | Gov guide | "NY Attorney General condominium offering plan declaration bylaws board of managers common elements guide" | WebSearch + WebFetch | https://ag.ny.gov/sites/default/files/2022-08/how_to_handle_problems_with_a_condo_board.pdf | Declaration, bylaws, floor plans and rules "shall be available for inspection"; AG may intervene where sponsor still controls the board or breaks offering plan promises | Board checklist #1, #2 |
| 10 | Market data | "Manhattan condo sales co-op sales 2026 third quarter Miller Samuel Elliman report median condo price" | WebSearch + WebFetch | https://www.brickunderground.com/sell/manhattan-co-op-condo-sales-market-report-nyc-second-quarter-2026 | Q2 2026: median condos+co-ops $1.25M (Miller Samuel); new-dev condo median $2.5M (SERHANT); Jennifer White Karp, Jul 2 2026 | Facts list |
| 11 | Market data | same query | WebFetch | https://inhabit.corcoran.com/manhattan-condo-co-op-sales-june-2026/ | June 2026: condo avg $2,054/sf; co-op $1,384/sf; co-op contracts +16% YoY vs condo +9% (Corcoran, Jul 9 2026) | Facts list |
| 12 | Market data | "\"third quarter\" 2026 Manhattan condo sales median new development Miller Samuel October 2026" | WebSearch + WebFetch | https://www.credaily.com/?p=223715 | Q3 2026 Manhattan new-dev contracts 240 vs 331 a year earlier; ~3,000 new-dev units on market, 30% below 10-yr avg; BHSDM data via The Real Deal; CRE Daily Oct 7 2026 | Facts list |
| 13 | Market data | "Manhattan office to residential conversion condominium 2026 condo conversion project" | WebSearch + WebFetch | https://www.bisnow.com/new-york/news/office/alignment-of-stars-cause-nyc-conversions-to-double-in-2026-132414 | Corcoran Sunshine: ~2,000 rentals and 317 condo units from conversions (office/hotel/industrial) reaching market in 2026; C&W 9.5M SF of conversions to start in 2026; Bisnow, Dec 17 2025 | Facts list |
| 14 | Local news/trade | "Habitat magazine condo board intercom security cameras Manhattan condominium" | WebSearch + WebFetch | https://habitatmag.com/Publication-Content/Building-Operations/2023/2023-August/Q-A-Can-a-Condo-Board-Spy-on-Staff-and-Unit-Owners | Midtown East condo: cameras above doorman desk + elevators; attorney Andrew Lieb: "A house rule that is unauthorized by these foundational documents is unenforceable"; audio recording without consent unlawful (one-party consent state); Aug 28 2023 | Cameras ¶2; AI Reality Check #5 |
| 15 | Trade | Firecrawl scrape | Firecrawl | https://habitatmag.com/Publication-Content/Board-Operations/2023/2023-February/Video-Doorbells-Present-a-Conundrum-for-Co-op-and-Condo-Boards | Hallways are common space; Debra Guzov (Manhattan lawyer for co-op/condo boards): "you can't just unilaterally do what you'd like to do in the common hallways"; Feb 20 2023 | Cameras ¶3; AI Reality Check #1 |
| 16 | News | "90,000 packages stolen or disappear every day New York City New York Times 2019" + Firecrawl search for URL | WebSearch / Firecrawl | https://www.nytimes.com/2019/12/02/nyregion/online-shopping-package-theft.html (verified via parcelpending.com summary + search snippet; NYT page itself not opened) | ~90,000 packages disappear daily in NYC without explanation (Hu & Haag, Dec 2019) | The Neighborhood ¶4 |
| 17 | Hyperlocal | not searched | Patch/West Side Rag etc. | EMPTY (no condo-specific Manhattan security story verified this run) | — | — |
| 18 | Yelp 1–3★ | not searched | Yelp | EMPTY (not accessible in build env) | — | — |
| 19 | Landmarks | general knowledge of real places (Hudson Yards, High Line, West 57th St "Billionaires' Row", Tribeca/SoHo lofts, Battery Park City, FiDi, Riverside Blvd/Lincoln Square, Harlem/Central Park North, 125th St, Madison/Lexington Aves) | — | no statistics attached to any landmark | Coverage Area; Commercial section |

Blocked during build (WebFetch permission not answered): nyc.gov HPD Tenant Data Privacy page (used intro.nyc law text instead), nysenate MDL 50-a via WebFetch (re-fetched via Firecrawl), newyorkyimby conversion article (site error), bhsusa.com blog (site error).

## Question list used on this page (add to the silo register)

### Q&A (H3)
- Our sponsor installed the intercom and we have no administrator login. Can the condo take control of it?
- Should a new condo board replace the developer's security system right after turnover?
- Who should hold the master credentials for a Manhattan condo's security systems?
- What happens to fobs and app access when a Manhattan condo unit is sold?
- Can renters in condo units get their own credentials?
- How do couriers get into a non-doorman Manhattan condo without a resident letting them in?
- Can the concierge desk and residents' phones both answer the same lobby call?
- Is a condo security system a common charge or the unit owner's cost?
- What ongoing costs come with a modern condo intercom?
- Will you work under our managing agent's vendor rules and insurance requirements?

### FAQ (visible + FAQPage)
- Does a Manhattan condo intercom have to meet a state requirement?
- Can the condo keep its existing fob readers when it replaces the intercom?
- Can unit owners open the lobby door for guests from their phones?
- How do Manhattan condo boards usually pay for a security upgrade?
- Do you work for sponsor-controlled condo boards in new developments?
- Can you integrate with the building's package lockers?
- What does the $250 service call cover in a Manhattan condo?
- Will you install a security system inside an individual condo unit?
- Can the security network be kept separate from residents' Wi-Fi?
- How much notice do you need before a board meeting to deliver a proposal?
- Do you offer service agreements for condo security systems?
- Can you give us the names of other Manhattan condos you have worked in?

## Images (11, permanent image rule, reused from images/access-control-installation/ and images/apartment-building-security-camera-installation/; none share a sha256 with any co-op-security-systems, co-op-board-intercom-upgrade or condo-security-systems image present at build time; checked by eye against those sets)
lobby-camera-at-bulkhead-over-coffered-ceiling (hero/og), double-height-amenity-hall-with-mezzanine-windows, narrow-dark-grey-video-door-station, cellar-storage-room-dome-camera-under-stained-ceiling, white-wired-video-doorbell-for-unit-door, stainless-pendant-ptz-dome-camera-for-garage, two-dome-cameras-in-tiled-ceiling-grid, mailroom-corner-turret-camera-above-motion-sensor, 16-channel-network-video-recorder, recorder-view-of-sidewalk-and-curb, night-camera-view-of-open-service-door.


## queens

## queens

## Queens — local research for `condo-security-systems-queens` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: WebSearch, Firecrawl search, Firecrawl scrape (directQuote query mode, PDF parser, rawHtml of the NYC Open Data SODA API). Rows marked "reused" were verified by other silo builders.

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | R1–R2 (Firecrawl search excerpts, r/longislandcity) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects claims typical of national cost guides / AI summaries (Angi, HomeAdvisor, Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | Gantry Plaza State Park, Court Square/Queens Plaza, Main St/Roosevelt Ave, Astoria Park/Ditmars Blvd, Queens Blvd (Forest Hills/Rego Park), Jamaica Center/Sutphin Blvd — real places named as general geography, no stats attached |
| 7 | Building stock / use cases | Z1–Z5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | The Real Deal (Z3), QNS (M1) |
| 10 | Hyperlocal | QNS/LIC Post (M1) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| Z1 | `Long Island City rezoning 2001 residential towers condos Hunters Point Queens West units built` · WebSearch → Firecrawl scrape PDF (directQuote) | https://www.nyc.gov/assets/planning/download/pdf/about/press-releases/pr52301.pdf | Release #16-01, May 23 2001: CPC "unanimously approved the Department's proposal to create special zoning regulations for 37 centrally located blocks in Long Island City in Queens." | §5 LIC subsection; facts list; stamp |
| Z2 | `Hunters Point South Long Island City housing units waterfront towers completed nyc.gov` · Firecrawl search → Firecrawl scrape PDF (40 of 125 pages) | https://www.nyc.gov/assets/planning/download/pdf/about/cpc/250176.pdf | CPC report C 250176 ZMQ (LIC Neighborhood Plan): "construction of over 21,000 housing units within a half-mile radius from the project area since 2010"; Hunters Point South: five parcels "developed into 3,249 housing units"; "When complete, Hunters Point South will contain approximately 5,000 units of housing, over 60 percent of which would be income-restricted"; "the establishment of the LIC Special District in 2001 spurred significant development". | §5 LIC subsection; facts list |
| Z2b | same search, Hunters Point Subdistrict PDF (checked, not used) | https://www.nyc.gov/assets/planning/download/pdf/plans/hunters-point-subdistrict/hunters-point.pdf | 2008 subdistrict rezoning ~300 units — too small/old to matter; not used. | — |
| Z3 | `Flushing Queens new condo developments Skyview Parc Tangram One Fulton Square condominium units` · WebSearch → Firecrawl scrape (directQuote) | https://therealdeal.com/new-york/2022/12/29/how-flushing-became-a-hotbed-for-development/ | Pat Ralph & Adam Farence, Dec 29 2022: "Because its residents prefer to own real estate, Flushing has become a hotbed for condominium projects"; Sky View Parc "on 13 acres between Roosevelt Avenue, College Point Boulevard and 40th Road ... includes a pair of condominiums with nearly 1,200 units, a 1.2 million-square-foot shopping center and a wellness center"; special waterfront district "13 buildings with more than 1,700 residential units"; "29-acre rezoning". (Sky View Parc named only as a development cited by the press, not as a client.) | §5 Flushing subsection; facts list |
| Z4 | `Jamaica Plan rezoning 2007 City Council approved 368 blocks housing Downtown Jamaica` · Firecrawl search (excerpt) | https://www.nyc.gov/assets/planning/download/pdf/about/cpc/080022.pdf | "On September 10, 2007, the Jamaica Plan, a comprehensive zoning and planning strategy for 368 blocks in Jamaica, Queens, was adopted". | §5 Jamaica subsection; §7 Jamaica card; facts list |
| M1 | `Queens new development condo market report 2025 Long Island City Flushing share of sales` · WebSearch → Firecrawl scrape (directQuote) | https://qns.com/2025/07/lic-condo-activity-climbs-in-q2-2025-with-surge-in-sales-and-contracts/ | Ethan Marshall, Jul 14 2025, citing SERHANT: LIC condo closed sales "from 106 in the second quarter of 2024 to 173 in the second quarter of 2025"; "One-bedroom units accounted for the majority ... with 104". | §5 LIC; facts list; AI check #1 |
| M1b | Corcoran LIC & Astoria 1H 2025 report · Firecrawl scrape | https://inhabit.corcoran.com/long-island-city-astoria-market-report-1h-2025/ | Redirected to report archive; no data extracted. EMPTY; not used. | — |
| D1 | SODA `$select=communityboard,count(*)&$where=boro='QUEENS' AND upper(novdescription) like '%INTERCOM%' AND novissueddate between '2025-01-01T00:00:00' and '2025-12-31T23:59:59'&$group=communityboard` · Firecrawl scrape (rawHtml); direct curl from build env timed out | https://data.cityofnewyork.us/resource/wvxf-dwi5.json (dataset https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5) | 2025 Queens intercom violations by CB: 1=20, 2=26, 3=48, 4=29, 5=10, 6=35, 7=49, 8=50, 9=14, 10=2, 11=4, 12=35, 13=3, 14=17; total 342 (matches co-op Queens row Q10 class total). CB→neighborhood labels = standard CB geography. Page caveat: mostly rental complaints, not a condo count. | §5 table + caveat paragraph; facts list |
| R1 | `reddit Long Island City condo building package room intercom fob HOA board LIC` · Firecrawl search (excerpt) | https://www.reddit.com/r/longislandcity/comments/1vic0mf/halo_lic_gave_our_spare_key_to_a_stranger_who/ | Title/excerpt: building staff "handed our spare key to a stranger who broke into our home". Rental building; building name NOT used on page (URL slug contains it — link kept as the source). | §5 "What Queens condo residents complain about" |
| R2 | same search | https://www.reddit.com/r/longislandcity/comments/1vmeeos/vera_a_44story_condo_building_breaks_ground_in_lic/ | Title: "Vera, a 44-story condo building, breaks ground in LIC". Project name not used on page. | same paragraph |
| G1 | reused (silo L1) | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | RPL §339-e common elements incl. "halls, corridors, lobbies, stairs, stairways, fire escapes, and entrances and exits of the building"; "recreational or community facilities, parking areas and storage spaces"; "all apparatus and installations existing for common use"; operation of the property definition. | §5 para 2; AI check #4 |
| G2 | reused (silo L2 / Brooklyn G1) | https://www.nysenate.gov/legislation/laws/RPP/339-V | Bylaws: "the powers and duties of the board"; percentage "necessary to adopt decisions binding on all unit owners"; reserves for "major and minor maintenance, repairs, additions, improvements, replacements". | §5 para 3 |
| G3 | reused (silo L4) | https://www.nysenate.gov/legislation/laws/MDW/50-A | MDL §50-a: post-1968 class A, 8+ apartments, self-locking door + intercom with release. | §8 rules list |
| G4 | reused (silo L5) | https://intro.nyc/local-laws/2021-63 | Local Law 63 of 2021 smart access rules; applicability to owner-occupied condo units left to counsel. | §8 rules list |
| G5 | reused (silo L6) | NYC BC 1010.1.9.8/9; Admin Code §28-105.4.7 (amlegal links in research/co-op-security-systems.md) | Egress locking release; low-voltage permit exemption. Described without links. | §8 rules list |
| P1 | site price pages (internal) | /door-buzzer-repair-pricing , /intercom-pricing , /security-camera-pricing-queens | $250 service call; ranges $250–$525, $250–$475, $325–$650, $450–$950, $650–$1,800, $850–$2,400 (same table as co-op Queens). No other prices. | §14 table; §15 cards; hero; FAQ |

Neighborhood/street names used as general geography only (no stats): Sunnyside, Woodside, Elmhurst, Jackson Heights, Astoria/Ditmars, Steinway St, 30th Ave, Jackson Ave, Court Square, Queens Plaza, Main St, Roosevelt Ave, Queens Blvd, Jamaica Ave, Sutphin Blvd, Bell Blvd, Bayside, Douglaston, Little Neck, Whitestone. Building-type descriptions in §7 are field observation, no statistic claimed.

### Queens question register (this page) — add to the silo register
§9 Q&A (H3): Our building still has unsold units held by the sponsor. Who signs off on security work? · Our ground-floor commercial owner uses the same service door as residents. Who pays for its hardware? · How should our board compare three security bids that propose different equipment? · Can the work start while the building is still under the developer's construction warranty? · Our management office is in Manhattan and the building has no full-time staff. Who needs to be on site? · Some owners want a screen on the wall and others only want the app. Can one system do both? · Many of our owners spend months overseas. Can they still answer the lobby from abroad? · Can a visitor at the garage level call up to an apartment? · Will our doors stay locked or swing open if the power fails? · Can owners reserve the party room or guest suite and have the door open only for their booking? · How do we stop dog walkers and cleaners from keeping fobs after an owner lets them go? · Our package room overflows in November and December. Should we add lockers or a second room? · Can bike room access be limited to owners who registered a bike? · How long should a Queens condo keep its camera recordings? · What should the board do when police ask for a video clip?

§17 FAQ: Can you match the entry hardware already installed in the other buildings of our Queens condo complex? · Will someone from your company present the proposal at our condo board meeting? · Can the condo association pay by check from its operating account? · Can you put a reader on the trash room or recycling area door in a Queens condo? · Do you install license plate cameras at a condo garage entrance? · Do you take away the old intercom panels and equipment when you replace them? · How long does a lobby entry replacement take once the equipment has arrived? · Do you train the resident manager and board officers to run the software? · Is there a charge to review another company's security proposal for our Queens condo? · Can you help our board write house rules for fobs, guests and camera footage? · Can the roof door sound an alarm if someone props it open? · Can individual owners order extra fobs directly from you?

Intent check vs register (NYC/Manhattan/Brooklyn condo + co-op Queens): owner vote, funding, handset bill, sponsor login, renters, couriers, stale owner fobs, footage access, unit doorbell cams, virtual doorman, financing, warranty, brands, references, RFP format, electrical, weekends, free walk-through, maintenance visits, coverage radius, multi-building single fob (co-op Queens), landline shareholders, internet outage — all answered in body only or avoided; none repeated as a question.

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-queens-` names. SHA-256: none matches any file in images/condo-security-systems/ (nyc/manhattan/brooklyn, plus the parallel bronx/staten-island files present at check time), images/co-op-security-systems/ or images/co-op-board-intercom-upgrade/. Visual check: the library's distinct job photos are nearly all already used somewhere in the condo/co-op silos under other encodings; these 11 were chosen as the least-used scenes and none appears on co-op Queens. Viewed before naming: no faces, house numbers, phone numbers or "AESS"; no buzzer-repair/*.jpg, elevator-access-control, network-installation, low-voltage, commercial-security, smart-lock or AI images.
| Page file | Source |
|---|---|
| …-queens-camera-above-steel-door-at-end-of-back-hall (hero/og) | access-control-installation/…-olinville-camera-over-grey-steel-service-door |
| …-queens-keypad-entry-station-with-reader-and-camera (product) | door-buzzer-installation/…-allerton-keypad-door-station-with-card-reader-and-camera |
| …-queens-dark-touchscreen-directory-panel-with-keypad (product, Akuvox) | access-control-installation/…-bedford-park-dark-touchscreen-panel-with-numeric-keypad |
| …-queens-rounded-single-door-video-intercom (product) | door-buzzer-installation/…-ulster-county-pill-shaped-video-intercom |
| …-queens-white-dome-in-corner-above-motion-sensor | access-control-installation/…-new-utrecht-white-dome-in-hall-corner-above-motion-sensor |
| …-queens-dome-camera-in-drop-ceiling-beside-light-panel | access-control-installation/…-gowanus-dome-camera-beside-track-lights |
| …-queens-exterior-dome-under-fascia-against-winter-sky | access-control-installation/…-throggs-neck-dome-camera-under-fascia-against-winter-sky |
| …-queens-low-voltage-cable-bundles-over-ceiling-beam | door-buzzer-installation/…-allerton-low-voltage-cable-bundles-over-ceiling-beam |
| …-queens-ground-floor-shop-ceiling-over-shelves | access-control-installation/…-melrose-shop-ceiling-over-stocked-shelves |
| …-queens-dome-camera-over-wood-slat-retail-wall | access-control-installation/…-gowanus-dome-camera-over-wood-panel-shop-wall |
| …-queens-recorder-per-channel-status-readout | access-control-installation/…-laconia-recorder-screen-per-channel-readout |

DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + images/door-buzzer-installation/ (no real condo photos yet)`.

### Links left for the main run
- FLIP (plain text + comment): `/condo-intercom-replacement` (§6 intercom), `/condo-security-camera-installation-queens` (§6 cameras), `/condo-security-systems-long-island`, `/condo-security-systems-hudson-valley` (§19).
- Linked directly though built in parallel: `/condo-security-systems-bronx` (file not present at last check → checker "broken link" until it lands), `/condo-security-systems-staten-island`.
- Link backs needed: /condo-security-systems-nyc, -manhattan, -brooklyn (FLIP comments already there), /co-op-security-systems-queens (one link back), and per keyword rules one contextual link back from /intercom-installation-queens-ny and /apartment-building-security-camera-installation-queens.


## bronx

## bronx

## Bronx — local research for `condo-security-systems-bronx` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search, Firecrawl scrape (directQuote query mode). Rows marked "reused" were verified by earlier silo builders.

Thesis (why this is not a borough swap): the Bronx's condo stock is dominated by converted prewar complexes (Parkchester), Riverdale elevator condos inside a co-op neighborhood, east Bronx garden/townhouse/gated waterfront communities, and only a few boutique condos in the South Bronx, where new construction is mostly rental. The page is built around campus-wide credentials, parking lots and gates, package theft, renters in owner units and shoreline exposure.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched this run; resident voice taken from Bronx Times / Parkchester Times instead) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims from national cost guides / AI-style summaries (Angi, HomeAdvisor, Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | X1, X4–X7 |
| 7 | Building stock / use cases | X1–X6 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Bronx Times (N1) |
| 10 | Hyperlocal | Parkchester Times (N2), The Riverdale Press (N3) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| X1 | (direct) · Firecrawl scrape directQuote | https://en.wikipedia.org/wiki/Parkchester,_Bronx | Planned community by Metropolitan Life; scale model at 1939 World's Fair; "51 groups of buildings were planned to house 12,000 families"; ~1/3 converted to condominiums 1974, remainder (Parkchester South Condominium) 1986; "171 four-sided brick buildings, either eight or 13 stories"; 2-acre Aileen B. Ryan Oval; "Parkchester special patrolmen are issued a pistol license by the New York City Police Department". | §5 Parkchester subsection + facts list; §7 card A; AI check #1; §13 card 1; FAQ 1 |
| N1 | `Parkchester condominium security cameras intercom package theft Bronx Times` · Firecrawl search → scrape | https://www.bxtimes.com/parkchester-residents-plan-second-rally-in-four-weeks-demanding-safety-improvements/ | Bronx Times, Emily Swanson, Oct 7 2024: residents' "call for more lighting, cameras and increased law enforcement engagement"; resident realized her door "is hollow and quite easy to break"; sign: "I should not have to rely on my neighbor's Ring Doorbell [camera]". | §5 Parkchester para 2; Q&A (flimsy unit doors; lighting before cameras); AI checks #1, #2 |
| N2 | same search → scrape | https://parkchestertimes.com/2025/06/18/lets-stop-package-theft-together-says-parkchester-resident-as-community-urged-to-stay-alert/ | Parkchester Times, June 18 2025: Parkchester South resident on package theft; urged "downloading security footage before it auto-deletes" and "only buzz in people you know or deliveries you are expecting". | §5 Parkchester para 2–3; Q&A (clip request timing); AI check #3 |
| N3 | `Riverdale Press condo board Riverdale condominium building intercom OR security OR lobby` · Firecrawl search → scrape | https://www.riverdalepress.com/stories/riverdale-cooperatives-association-re-elects-board-continues-community-advocacy,151840 | The Riverdale Press, July 12 2024: association membership "more than 100 co-operatives and condominiums"; workshops on "code compliance, legal parameters, green energy and local law 11". | §5 Riverdale subsection + facts list |
| X2 | `Throggs Neck condominium development Bronx Times condo townhouses waterfront gated` · Firecrawl search → scrape | https://nyc.marketproof.com/neighborhood-guides/nyc/bronx/throggs-neck | "Condo developments have arrived on Schurz Avenue, as well as gated co-op communities with single family homes." | §5 east Bronx subsection; §13 card 3; §8 corridor list |
| X3 | (direct) · Firecrawl scrape | https://nyc.marketproof.com/neighborhood-guides/nyc/bronx/pelham-bay | "tree-lined homes brushing up against newer apartments"; "Pelham Bay Park ... the city's largest park"; "the 6 train spurring on apartment building development". | §5 east Bronx subsection; §13 card 4; §8 Westchester Ave |
| X4 | `Lower Concourse rezoning 2009 Mott Haven Port Morris City Planning residential waterfront` · Firecrawl search → scrape | https://edc.nyc/project/lower-concourse-infrastructure-investment-strategy | "In 2009, this 30-block stretch along the Harlem River was rezoned to allow for residential and commercial development"; Bronx Point phase 1 "Approximately 540 units of 100% permanently affordable housing". | §5 South Bronx subsection + facts list; §13 card 5 |
| X5 | `Bronx condominium buildings Riverdale condos Mott Haven new development condo Throggs Neck condo complex` · Firecrawl search (excerpt) | https://www.6sqft.com/new-rental-buildings-in-the-bronx/ | "7 notable new rental buildings in the Bronx": Mott Haven rentals incl. 12-story Bruckner House at 40 Bruckner Blvd and the seven-tower Bankside waterfront complex. (Buildings not named on the page.) | §5 South Bronx subsection; AI check #5; §8 Bruckner/Third Ave |
| X6 | (direct) · Firecrawl scrape directQuote | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-homeowner-housing-market/ | Citywide only: 318,000 occupied condo apartments; "18% of condo units citywide are owned by LLC's"; owners may have "subsequently vacated and are renting out their units". No Bronx-specific figure (page says so). | §5 "Rented units" subsection + facts list |
| X7 | landmark geography (no client building named) | — | Aileen B. Ryan Oval (X1), Riverdale hillsides, Schurz Ave (X2), Pelham Bay Park (X3), Harlem River / Lower Concourse (X4), Fordham Road (office NAP). East Tremont Ave, Johnson/Riverdale Aves, Westchester Ave, Bruckner Blvd/Third Ave named as corridors only (Bronx Times mentions E Tremont Ave; Marketproof X2/X3; 6sqft X5). | §8 corridor list; §13 cards |
| G1 | `New York Real Property Law 339-d definitions common elements` (reused, silo L1) · Firecrawl scrape | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | Common elements quoted (halls, corridors, lobbies ... entrances and exits; basements, cellars, yards, gardens ... parking areas and storage spaces; "all apparatus and installations existing for common use"). | §5 para 2 |
| G2 | reused (silo L2 / Brooklyn G1) | https://www.nysenate.gov/legislation/laws/RPP/339-V | Bylaws contents; decisions "binding on all unit owners"; reserves. | §5 para 3 |
| G3 | reused (silo L4) | https://www.nysenate.gov/legislation/laws/MDW/50-A | MDL §50-a: post-1968 class A, 8+ apartments, voice communication + release "from the apartment"; majority written request for older buildings; misdemeanor to "wilfully destroy, damage, or jam". | §8 rules; facts list |
| G4 | reused (silo L5) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-130977 ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL 63/2021 smart access systems; written data policy. Applicability to condo associations left to counsel. | §8 rules; §10 credentials |
| P1 | site price pages (internal, read Nov 26 2026) | /door-buzzer-repair-bronx-new-york ; /door-buzzer-repair-pricing ; /intercom-installation-bronx-ny ; /access-control-installation-bronx ; /security-camera-pricing-bronx ; /intercom-pricing | $250 service call; station $250–$525, transformer $325–$650, amplifier $450–$900, strike w/ alignment $450–$950, branch riser $850–$2,400 (Bronx buzzer page); multi-unit intercom $1,200–$4,500 (Bronx intercom page); single-door fob $1,500–$2,500, multi-door $4,000–$10,000, full building with elevator restriction $15,000–$40,000+ (Bronx access control page). No camera numbers quoted (link only). | §14 tables; §15 cards |

### Bronx question register (this page) — add to the silo register
§9 Q&A (H3): Our condo is one section of a big multi-building complex. Does our board decide on security, or someone above it? · How should a Bronx condo board compare three security bids that don't match line for line? · Can a large condo add cameras one building at a time without buying a new recorder for each? · Half of our entrance doors don't close and latch on their own. Is that an intercom problem or a door problem? · Our residents say their apartment doors feel flimsy. What can a security contractor actually do about that? · How many entrances can one condo intercom system run in a garden-style complex? · Can the lobby panel ring residents who only have a landline? · Can our private patrol officers and porters have their own credentials and a record of where they've been? · Where can a package room go in a walk-up condo with no spare room? · Can the parking lot gate and the building doors work from the same fob? · An owner's package was taken from the lobby. How quickly do they need to ask for the video? · Should a condo fix its lighting before adding more cameras? · Does salt air near the Throgs Neck shore shorten the life of outdoor readers and cameras? · A repair needs every apartment on the line, and several are rented out. How do we get in? · Is there an added charge for condos at the far edges of the borough, like Riverdale or City Island?

§17 FAQ: Do you work on security in Parkchester's condominium buildings? · Can the entrance panel show visitor instructions in Spanish? · Can you mount cameras on our parking lot light poles? · Will you coordinate with our guard service or patrol company? · Do you take out the old equipment and patch the holes it leaves? · Can we keep the fobs residents already have when the access system is upgraded? · What should we send ahead of the free walk-through? · If the building replaces the intercom, can an owner pay to upgrade the equipment in their own apartment? · Can a board member meet the estimator after work? · Can the managing agent get one proposal and one invoice for several buildings in a complex? · What happens if a panel or reader has to be special ordered? · Do you monitor alarms or cameras for condo owners?

(Checked by meaning against the nyc/manhattan/brooklyn condo register and the live queens/staten-island drafts; co-op Bronx questions on caregivers, footage retention length, facade timing and power supplies were deliberately avoided. Masked-geo paragraph similarity vs condo nyc/manhattan/brooklyn/queens/staten-island and co-op Bronx: max 0.59 apart from the mandated proof strip.)

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-bronx-` names; sha256 not present in images/condo-security-systems, images/co-op-security-systems or images/co-op-board-intercom-upgrade at build time, and checked by eye against those sets (several library files are re-crops of scenes already used; those were rejected).
- from images/access-control-installation/: parkchester-camera-over-corridor-to-grey-steel-door → ceiling-camera-over-hallway-to-grey-steel-door (hero/og, job photo); soundview-turret-camera-above-glass-entrance-wall → turret-camera-above-glass-lobby-entrance (job); williamsbridge-camera-arm-under-cornice → camera-on-steel-arm-under-stone-cornice (job; no house number visible); eastchester-white-bullet-camera-with-wall-mount-box → white-bullet-camera-with-junction-box (Hikvision product photo); edenwald-black-video-doorbell-with-blue-lit-bell-button → black-video-doorbell-with-lit-bell-button (Lorex product photo); clason-point-bronx-white-and-black-dual-lens-doorbell → dual-lens-video-doorbell-for-unit-entry (Uniview product photo); cobble-hill-brooklyn-white-indoor-touchscreen-answering-monitor → white-indoor-touchscreen-answering-monitor (Akuvox product photo)
- from images/apartment-building-security-camera-installation/: hudson-valley-stainless-box-camera-housing-on-bracket-product-photo → stainless-camera-housing-for-shoreline-air (Dahua product photo); staten-island-black-vandal-dome-camera-product → black-vandal-dome-camera-for-garage-levels (Uniview product photo); westchester-county-white-eyeball-turret-camera-product-photo → white-eyeball-turret-camera (product photo); queens-colorvu-bullet-camera-product-photo → color-night-bullet-camera-for-parking-lots (Hikvision product photo)
- Rejected as visual repeats of condo/co-op Bronx photos: parkchester network cables, parkchester lobby exit sign, bedford-park keypad panel, kingsbridge-heights lobby soffit, fieldston/harding-park recorder monitor, pelham-bay/morris-heights recorder views, pelham-parkway double-height wall. Never used: images/buzzer-repair/*.jpg, elevator-access-control, network-installation, low-voltage, commercial-security, smart-lock sets.
- Swapped out after comparing with the parallel queens/staten-island drafts (same scenes, different crops): throggs-neck bullet on bracket, pelham-gardens dome under eave, indian-village dome + sensor. Still shared by scene with the queens draft: the hero hallway (parkchester crop vs queens 'camera-above-steel-door-at-end-of-back-hall'); with staten-island: the Akuvox indoor monitor product photo (same product, different crop).
- DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + images/apartment-building-security-camera-installation/ (no real condo photos yet)`

### Links left for the main run
- FLIP comments in the page: `/condo-intercom-replacement` (§6 intercom), `/condo-security-camera-installation-bronx` (§6 cameras), `/condo-security-systems-long-island`, `/condo-security-systems-hudson-valley` (§19).
- Links back needed from /condo-security-systems-nyc, -manhattan, -brooklyn (and -queens, -staten-island if not already), /co-op-security-systems-bronx (one contextual link), plus per keyword rules one contextual link back from /intercom-installation-bronx-ny and /apartment-building-security-camera-installation-bronx.


## staten-island

## staten-island

## Staten Island — local research for `condo-security-systems-staten-island` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Format per blueprint v2.3 §12.4. Tools: Firecrawl scrape (raw JSON from the NYC Open Data SODA API; directQuote query mode), Firecrawl search, WebSearch.

HOLD-THIN test: passed. Staten Island's condo stock is genuinely different from the other boroughs (63% of condo homes in 1-3 story class R3 townhouse-style lots, 43% in ZIP 10314, 1980s peak, two-layer HOA + condo governance), so the page is written around entrance drives, call boxes, pools/clubhouses, parking courts and mail kiosks rather than lobbies. Angle kept apart from co-op-security-systems-staten-island (multi-building garden co-ops, Mitchell-Lama, Sandy/seawall, HPD violations).

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched this run; no Staten Island condo thread verified) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims seen in national cost guides/summaries (Angi, HomeAdvisor, Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | SIC-L1 |
| 7 | Building stock / use cases | SIC-P1–SIC-P4, SIC-C1 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | SILive (SIC-N1, SIC-N2) |
| 10 | Hyperlocal | SILive used; no condo-specific intercom/gate story found |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| SIC-P1 | SODA `$select=bldgclass,count(*) as n,sum(unitsres) as u,min(yearbuilt),max(yearbuilt)&$where=borough='SI' AND starts_with(bldgclass,'R')&$group=bldgclass` · NYC Open Data (MapPLUTO, 64uk-42ks) via Firecrawl scrape | https://data.cityofnewyork.us/resource/64uk-42ks.json (dataset https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks) | SI condo classes: R3 141 lots/7,233 res. units; RM 29/1,550; R6 18/34; R4 17/1,948; R2 6/483; RD 2/194; R1 3/16 (R0, R5, RB, RC, RK, RW, R8, RA non-residential/zero units). Residential classes total 216 lots / 11,458 units; R3 = 63%. | §5 para 2, facts list; §6 lobby-intercom para (R4+R2 ≈ 2,400) |
| SIC-P2 | SODA `$select=zipcode,count(*),sum(unitsres)&$where=borough='SI' AND bldgclass in('R2','R3','R4','RM','R1','R6','RD')&$group=zipcode` · same | same | 10314: 72 lots/4,947; 10304 13/1,500; 10306 17/845; 10305 30/831; 10301 13/714; 10309 11/654; 10312 15/624; 10303 14/586; 10308 15/438; 10310 6/172; 10307 4/125; 10302 4/20; no ZIP 2/2. ZIP→neighborhood labels are standard USPS geography. | §5 ZIP table + "Mid-Island first"; facts list |
| SIC-P3 | SODA `$select=bldgclass,yearbuilt,unitsres,zipcode,numfloors&$where=borough='SI' AND bldgclass in('R2','R3','R4','RM','RD')&$order=yearbuilt&$limit=300` · same | same | Of dated lots: 11 pre-1970, 12 in 1970s, 63 in 1980s (peak), 7 in 1990s, 43 from 2004 on (mostly 2–6 unit lots; a few large RM: 467 u 2014, 270 u 2022 12 fl, 116 u 2016 16 fl, 104 u 2014); ~58 lots year 0. R4: 1931/1937 6-fl (10301); 1961–64 7–8 fl; 1980s 3–7 fl. R3 mostly 2–3 floors. | §5 "1980s communities"; §6 buzzers; §7 cards D–F + elevator subsection; §8 corridors |
| SIC-P4 | `NYC building class R3 condo residential unit 1-3 story` · WebSearch → Firecrawl scrape (directQuote) | https://www.propertyshark.com/info/class-r-buildings-condominiums/ | "R2 – Condo; Residential Unit In Walk-Up Bldg.", "R3 – Condo; Residential Unit In 1-3 Story Bldg.", "R4 – Condo; Residential Unit In Elevator Bldg", "R6 – Condo; Resid.Unit Of 1-3 Unit Bldg-Orig Class 1" (DOF class list; nyc.gov glossary page 404'd). | §5 para 2 quote |
| SIC-G1 | reused silo L1 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | RPL §339-e common elements incl. "basements, cellars, yards, gardens, recreational or community facilities, parking areas and storage spaces"; "all apparatus and installations existing for common use". | §5 "Two layers of governance" |
| SIC-G2 | `New York Attorney General homeowners association offering plan regulations 13 NYCRR Part 22 HOA common areas` · Firecrawl search (excerpt) | https://ag.ny.gov/sites/default/files/regulatory-documents/13_nycrr_22.3.pdf | §22.3(f): plan must describe common areas incl. "the land, buildings, lots, parking facilities, recreational facilities". | §5 governance; §10.5 #4 |
| SIC-G3 | reused silo L4/L5/L6 + co-op SI-G2 | MDL §50-a; LL 63/2021 (intro.nyc); Admin Code §28-105.4.7; GBL Art. 6-D | as in silo rows | §5 facts; §6 cabling; §8.5 rules list |
| SIC-C1 | reused silo L3 | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-homeowner-housing-market/ | 318,000 occupied condo apartments citywide. | facts list |
| SIC-N1 | `silive Staten Island condo complex homeowners association security cameras gate break-ins cars` · Firecrawl search (excerpt) | https://www.silive.com/crime-safety/2022/09/residents-of-this-staten-island-community-say-thieves-are-accessing-locked-cars-are-high-tech-devices-at-work.html | Headline + excerpt: "For more than two years, police have been imploring borough residents to lock their car doors amid a surge in car break-ins and grand larceny". | §5 "What residents complain about" |
| SIC-N2 | same search (excerpt) | https://www.silive.com/crime-safety/2025/08/we-have-cameras-and-still-homeowner-decries-package-thefts-on-staten-island.html | Another household member: "It's unfortunate that people are having to set up lock boxes because of people (who steal)." | §5 same para |
| SIC-L1 | landmark geography (no building named, no counts) | — | Staten Island Mall/Richmond Ave; College of Staten Island (Willowbrook); Freshkills Park; Staten Island Greenbelt; Bay Street, Stapleton; Conference House Park, Tottenville. Corridors: Bay St, St. George, Richmond Ave, Hylan Blvd, Victory Blvd, Forest Ave. | §13 cards; §8 list |
| SIC-PR | site pages (internal, read Nov 26 2026) | /intercom-pricing; /door-buzzer-repair-pricing; /intercom-installation-staten-island-ny; /access-control-installation-staten-island; /alarm-installation-staten-island | $250 service call; repair ranges $250–$525, $250–$475, $325–$650, $450–$950, $650–$1,800, $850–$2,400; SI multi-unit intercom $1,200–$4,500+ (5–20 units); pedestrian gate keypad $1,500–$2,000; encrypted fob reader on lobby door $1,500–$2,500 installed; vehicle + pedestrian gate $4,000–$7,000; monitoring $30/mo keypad, $45/mo app. | §6, §14 tables, FAQ 5 |

### Staten Island question register (this page) — add to the silo register
§9 Q&A (H3): Our townhouse condo has no lobby. What does a building intercom even mean for a community like ours? · Our development has a master HOA and a separate condo association. Which one signs the contract with you? · Can a volunteer officer run the gate and pool access from a phone, without a managing agent? · Visitors keep slipping in behind residents at our entrance gate. Is the fix a camera, a second arm or something else? · The plow knocks over our keypad post every winter. What are the options? · What should our entrance gate do when the power goes out? · How should pool fobs work for a season that runs only from late May to early September? · Can guest passes for the pool or clubhouse expire on their own? · Can the clubhouse party room open only for the owner who reserved it? · Where should a townhouse community put its first two cameras? · Several of our garages open onto a shared lane. Can a camera watch the lane without looking into the garages? · Our townhouses get packages on dozens of separate stoops. Does a central parcel room make sense for a community like ours? · The original low-voltage cable runs underground from the gate to the clubhouse. Can a new system reuse it? · How long does a gate, clubhouse and pool access project take in a community of about 100 homes? · We are a mixed-use condo with stores downstairs. Can the residential board and the store owners share one system?

§17 FAQ: Can the gate directory list owners without showing their full names? · Can one fob open the vehicle gate, the pool and the clubhouse? · Can the board see who opened the pool gate after closing time? · Can the entrance gate open for ambulances and fire trucks? · What does alarm monitoring cost for a townhouse owner in the community? · Can an owner's own doorbell tie in to the community gate system? · Can the gate stay open during the day and lock at night? · Can you add cameras to a recorder our association already owns? · Our community has narrow private lanes and little visitor parking. Does that affect the visit? · Does winter weather delay outdoor gate and camera work on Staten Island? · Can a mixed-use condo keep its residential entrance separate from the stores below? · Do you also work in Staten Island's elevator condo buildings?

### Images (11, permanent image rule; no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-staten-island-` names; sha256 differs from every file in images/condo-security-systems/ (incl. the parallel Queens/Bronx sets), co-op-security-systems/, co-op-board-intercom-upgrade/; checked by eye against condo/co-op sets (a recorder-screen photo was dropped because Queens used a crop of it).
- black-bullet-camera-on-drop-ceiling-by-white-wall (hero/og; job photo) ← images/access-control-installation/access-control-installation-dumbo-black-bullet-camera-on-drop-ceiling-over-white-wall.webp
- one-button-door-station-with-card-symbol (product) ← access-control-installation-city-line-brooklyn-one-button-door-station-with-card-symbol.webp
- white-touchscreen-indoor-answering-monitor (product) ← access-control-installation-city-line-brooklyn-white-indoor-answering-monitor.webp
- wired-video-doorbell-with-green-ring-button (product) ← security-camera-maintenance-brooklyn-video-doorbell-product-photo.webp
- floodlight-camera-with-two-square-lamps (product) ← floodlight-camera-installation-hudson-valley-white-floodlight-with-two-square-panels-product-photo.webp
- twin-lens-dome-camera-for-parking-courts (product) ← apartment-building-security-camera-installation-hudson-valley-white-twin-lens-dome-camera-product-photo.webp
- white-turret-camera-with-twin-illuminators (product) ← security-camera-maintenance-bronx-turret-camera-twin-illuminators-product-photo.webp
- ptz-dome-camera-on-pendant-mount (product) ← apartment-building-security-camera-installation-manhattan-ptz-dome-camera-on-pendant-mount.webp
- ceiling-360-fisheye-camera (product) ← apartment-building-security-camera-installation-suffolk-county-360-fisheye-camera-product-photo.webp
- four-turret-cameras-with-network-recorder (product) ← security-camera-maintenance-brooklyn-four-dome-camera-recorder-kit-product-photo.webp
- rack-recorder-with-vented-front (product) ← security-camera-maintenance-bronx-rack-recorder-vented-front-product-photo.webp
Rejected: images/parking/* (AI-generated, branded shirts/phone numbers), recorder-screen (Queens crop), tiny <200px shots. Product photos show maker logos (Akuvox, Lorex, Uniview, Hikvision, Dahua, Alarm.com); no faces, house numbers, phone numbers or "AESS".
DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + images/security-camera-maintenance/ + images/apartment-building-security-camera-installation/ + images/floodlight-camera-installation/ (no real condo photos yet)`.

### Links left for the main run
- FLIP comments: /condo-intercom-replacement (§6), /condo-security-camera-installation-staten-island (§6), /condo-security-systems-long-island and /condo-security-systems-hudson-valley (§19).
- Link back needed from /condo-security-systems-nyc, -manhattan, -brooklyn (and -queens/-bronx if not already), /co-op-security-systems-staten-island; per rules one contextual link back from /intercom-installation-staten-island-ny and /apartment-building-security-camera-installation-staten-island.


## long-island

## long-island

## Long Island — local research for `condo-security-systems-long-island` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Hub page: Nassau + Suffolk. GBP Brooklyn, (800) 486-0943 only. Starting price $250 service call (START_PRICES). Built by a batch subagent; format per blueprint v2.3 §12.4. Angle kept apart from co-op-security-systems-long-island (garden co-ops, Kenwood Gardens/Great Neck, Roslyn, Nassau board-decision law): this page is written around gatehouse/townhouse communities, 55-plus clubhouse communities, waterfront condos, village-center buildings, master HOA + condo layering, buried cable and distance.

### Mandatory sources (§3) — status
| # | Source | Status |
|---|---|---|
| 1 | Reddit | LIC-R1, LIC-R2 (Firecrawl search excerpts) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims seen in cost guides (Angi/HomeAdvisor/Fixr named generically; HomeAdvisor $1,200–$8,500 range reused from co-op silo L12) and NYC-sourced content applied statewide (MDL §50-a, TDPA). No AI quote invented. |
| 6 | Landmarks | LIC-L1 (places as general locations; no client buildings) |
| 7 | Use cases / building stock | LIC-G1, LIC-55, LIC-W1, LIC-PJ |
| 8 | Bing/DDG | EMPTY (not accessible in build env) |
| 9 | Local news | Newsday (LIC-W1), The Cool Down/Yahoo (LIC-W2), Habitat (LIC-W3) |
| 10 | Hyperlocal | Village of Port Jefferson newsletter (LIC-PJ); Patch/LI Herald not searched — EMPTY |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| LIC-G1 | `Long Island gated condominium community 55+ clubhouse gatehouse security Nassau Suffolk` · Firecrawl search → Firecrawl scrape (directQuote) | https://activerain.com/blogsview/5031514/melville-long-island-has-gated-communities | ActiveRain, Apr 7 2017: Melville (Route 110, LIE Exit 49): HOA + condo community opened 2006 "with a 24 hour security gatehouse by its entrance"; townhouse community built 1986 with "a 24 hour attended gatehouse"; 55+ community opened 2003, "a gated community featuring 24 hour security"; another 24-hour guard-gated community with 193 detached homes + townhouses. Community names NOT used on page. | §5 para 2; §8 Route 110 card; §13 Route 110 card |
| LIC-55 | same search → Firecrawl scrape (directQuote) | https://www.55places.com/blog/7-popular-gated-communities-on-east-long-island | 55places (Ellen Kershner, May 26 2021, modified Jan 27 2024): Manorville 512 attached + single-family homes; Coram 195 attached; St. James 653 homes "with the majority being condos", two outdoor pools + indoor pool; Riverhead communities completed 2005 (194) and 2002 (196); Setauket completed 2007 (150), clubhouse indoor pool; Eastport 240. Names NOT used on page. | §5 para 3; facts list; §8 Riverhead card; §13 Setauket and Riverhead cards |
| LIC-W1 | `Glen Cove Garvies Point waterfront condominiums units Newsday OR Herald` · Firecrawl search (excerpts) | https://www.newsday.com/long-island/nassau/garvies-point-model-condos-open-in-glen-cove-b31613 ; https://www.newsday.com/real-estate/glen-cove-garvies-point-new-apartments-rkevy0cy | Newsday: "167 condos in the five-story Beacon"; Feb 2 2026 (Celia Young): RXR's "$1.3 billion Garvies Point waterfront development". thebeacongp.com: "The first waterfront condominiums on Long Island's Garvies Point." Building name NOT used on page. | §5 para 4; §8 North Shore card; §13 Garvies Point card |
| LIC-W2 | `Long Beach NY oceanfront condominium boardwalk condo building Sandy flooding repairs` · Firecrawl search (excerpts) | https://www.thecooldown.com/green-business/long-beach-historic-boardwalk-repair-cost/ (also yahoo.com syndication) | "After three major storms tore away sections of Long Beach's historic Peninsula boardwalk and bulkhead, the city said repairs could cost as much as $3.6 million." | §5 para 4; §13 Long Beach card |
| LIC-W3 | reused from research/co-op-security-systems.md LI4 | https://www.habitatmag.com/Publication-Content/Building-Operations/2015/2015-May/Neptune-Towers-Replaces-Generator | Habitat, May 11 2015: Long Beach building raised generator ~30 inches "just in case the area [got] flooded"; can carry security systems. Building name NOT used; described as "one Long Beach apartment building". | §5 para 4 |
| LIC-PJ | `Port Jefferson village condominium apartments harbor new development units approved` · Firecrawl search (excerpt) | https://www.portjeffny.gov/428 | Village newsletter (PJVV Issue 9): "Zone change request for a proposed 79-unit condominium development on nearly 10 acres" (hearing resumes Sept 25, 2025). Address NOT used on page. | §5 para 5; §13 Port Jefferson card |
| LIC-R1 | `reddit r/longisland condo HOA common charges gate clubhouse board` · Firecrawl search (excerpt) | https://www.reddit.com/r/longisland/comments/1obpdf0/condo_owners_that_eventually_became_homeowners/ | "Happy family of 4 living in a Sachem area condo here. Sure we are short of space, but the roof will never need to be replaced on our dime." | §5 para 5 |
| LIC-R2 | same search (excerpt) | https://www.reddit.com/r/longisland/comments/smpafg/why_are_condoapt_hoa_fees_so_high/ | "...Then you have water, heating, snow removal, lawn/garden maintenance where..." | §5 para 5 |
| LIC-G2 | reused silo L1/L2 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | RPL §339-e common elements; §339-v bylaws + reserves quote. | facts list; §8.5 rules; AI check #4 |
| LIC-G3 | reused condo SI row SIC-G2 | https://ag.ny.gov/sites/default/files/regulatory-documents/13_nycrr_22.3.pdf | 13 NYCRR §22.3(f): HOA plan describes common areas incl. "the land, buildings, lots, parking facilities, recreational facilities". | facts list; §8.5; AI check #4 |
| LIC-G4 | reused co-op LI rows LI8/LI8b/LI9a + silo L4/L5 | https://newyork.public.law/laws/n.y._multiple_residence_law_section_3 ; nysenate MDL §§3, 50-a ; https://dos.ny.gov/legal-memorandum-lg03-nys-uniform-fire-prevention-and-building-code-what-elected-officials-need ; https://intro.nyc/local-laws/2021-63 | MRL applies to cities <325,000 and all towns/villages; MDL §50-a is NYC-only; no MRL intercom requirement found (page makes no such claim); Uniform Code "automatically in effect in each city, town, and village in the State (except New York City)"; TDPA is NYC local law. | facts list; §8.5; AI checks #1, #6 |
| LIC-FA | Anwar rule (batch instructions, Nov 26 2026) + /fire-alarm-installation-long-island-ny | — | No Nassau Fire Marshal FM number yet: page says LI fire alarm work is in Suffolk; Nassau = ask first; no fire alarm prices. | §6 fire alarm; §8.5; AI check #7 |
| LIC-PR | site pages (internal, read Nov 26 2026) | /intercom-installation-long-island-ny; /door-buzzer-repair-long-island-ny; /access-control-installation-long-island; /elevator-access-control-installation-long-island; site monitoring tiers | $250 service call; multi-unit intercom $1,200–$4,500+; buzzer components $250–$525 station, $325–$650 transformer, $450–$950 strike, $650–$1,800 panel; single-door encrypted reader $1,500–$2,500 installed; encrypted credential upgrade $3,000–$8,000 (most LI single-building properties); gate access w/ vehicle reader + barrier arm $3,500–$12,000 installed; elevator Level 1 from $1,725/car Nassau, $1,800/car Suffolk; monitoring $45/$30. | hero box; §6; §14 table; §15 |
| LIC-L1 | landmark geography (no client buildings, no counts beyond sourced rows) | — | Route 110 Melville; Garvies Point Glen Cove; Long Beach boardwalk; Port Jefferson Harbor; Stony Brook/Setauket; Route 58 Riverhead; central Nassau station towns (Mineola, Garden City, Hicksville, Westbury) described generally. | §8 cards; §13 cards |

### Long Island question register (this page) — add to the silo register
§9 Q&A (H3): Can you price the shared gatehouse equipment separately from each condo association's own buildings? · Our board wants to restrict pool access for owners who are behind on common charges. Can the system do that? · Commuters cut through our condo's parking lot to reach the train. What actually helps? · Our condo shares a private entrance road with a neighboring community. Can both associations use one gate? · Windshield tags or handheld remotes: which is better for resident cars at a condo gate? · Can a new access system work with the gate operator motor we already have? · Residents get stuck behind visitors at our entrance every evening. Is a second lane worth it? · The officer in our guard booth cannot see the resident lane. What fixes that? · Our complex has condo buildings and rental buildings side by side. Can one system serve both owners? · What kind of credential works at a pool gate where people arrive in swimsuits with wet hands? · Should a 55-plus community have a call station at the pool or the clubhouse? · Our clubhouse has an indoor pool. Can the pool room lock itself when no lifeguard or attendant is on duty? · Our waterfront building is in a flood zone. Where should the intercom and access control equipment go? · Our pool sits far from any building. How do you connect a gate or reader that is hundreds of feet away? · What does a security survey of a gated condo community actually cover?

§17 FAQ: Can tennis and pickleball court gates get their own reader and schedule? · Can a condo put a reader on the gate to its private beach, dock or waterfront walkway? · Will the board receive a written survey report even if it hires someone else? · Can the clubhouse and management office get a burglar alarm with separate codes for staff? · Our community is repaving the entrance drive. Should conduit for a future gate system go in now? · How should a community secure a developer's sales office or model home that is still open inside the gates? · Can the visitor call box be reached from a driver's seat without leaving the car? · Do you schedule work around a community's quiet hours and clubhouse calendar? · Can you help our board decide between a staffed gatehouse and a resident-only gate? · Do you also install the clubhouse TVs and sound system? · Can the RV, boat or trailer storage lot get its own gate access? · Can entry records show the board how much each amenity is actually used?

Intent check (by meaning) against the silo register (nyc, manhattan, brooklyn, queens, bronx, staten-island) AND the parallel nassau-county / hudson-valley drafts: dropped during the build because they matched a sibling: part-day gatehouse (Nassau + HV), staffed vs unstaffed second entrance (Nassau), older owners' entry features (Nassau, HV), cellular call box (Nassau, HV), event-space zoning (Nassau, Queens/SI reservations), first-phase planning (Nassau), stone-pillar mounting (HV), rental-to-condo replacement timing (Manhattan turnover). Kept in body only: virtual doorman, references, financing, warranty, electrical, weekends, RFPs, landscapers/plow access, snowbirds, fire alarm, TDPA/MDL jurisdiction, master-HOA signatory.

### Similarity
Masked-geo paragraph similarity (difflib on p/li/h3 ≥12 words, top-5 Jaccard candidates) vs condo nyc/manhattan/brooklyn/queens/bronx/staten-island, co-op long-island, condo nassau-county and hudson-valley drafts: max 0.641 apart from the mandated warranty terms sentence (1.0, required verbatim).

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied (already WebP) into images/condo-security-systems/ with `-long-island-` names. SHA-256: none matches any file in images/condo-security-systems/ (incl. the parallel nassau-county/hudson-valley files present at check time) or images/co-op-security-systems/. Sources chosen as hash-unused anywhere in the condo/co-op silos and used once in their own source folder; viewed on a contact sheet: no faces, house numbers, phone numbers or "AESS"; nothing from buzzer-repair/*.jpg, elevator-access-control, network-installation, low-voltage, commercial-security, smart-lock or AI sets.
| Page file (`condo-security-systems-long-island-…`) | Source |
|---|---|
| turret-camera-above-glass-entry-wall (hero, og:image; job photo) | alarm-installation/alarm-installation-spring-creek-ceiling-turret-above-glass-entry-vestibule.webp |
| camera-view-of-brick-walk-and-paved-lot (job/recorder view) | access-control-installation/access-control-installation-kingsbridge-heights-wide-camera-view-of-brick-walk-and-lot.webp |
| low-voltage-cable-bundles-above-ceiling-grid (job photo) | alarm-installation/alarm-installation-new-lots-low-voltage-cable-bundles-under-ceiling.webp |
| solar-powered-cellular-ptz-camera-with-sim-card (product) | alarm-installation/alarm-installation-ocean-parkway-cellular-camera-with-sim-card-and-solar-panel-product-photo.webp |
| keypad-door-station-with-card-zone-and-camera (Akuvox product) | alarm-installation/alarm-installation-carroll-gardens-akuvox-keypad-door-station-product-photo.webp |
| white-indoor-video-monitor-for-units (Akuvox product) | alarm-installation/alarm-installation-spring-creek-white-indoor-touchscreen-monitor-product-photo.webp |
| rack-mount-network-video-recorder-front (product) | alarm-installation/alarm-installation-manhattan-beach-black-nvr-front-panel-product-photo.webp |
| dark-metal-video-door-station-with-lit-button (Axis product) | alarm-installation/alarm-installation-madison-black-metal-door-station-product-photo.webp |
| pan-tilt-floodlight-camera-with-twin-lamps (product) | alarm-installation/alarm-installation-sea-gate-pan-tilt-floodlight-camera-product-photo.webp |
| two-tone-single-button-video-door-station (Akuvox product) | alarm-installation/alarm-installation-madison-two-tone-door-station-product-photo.webp |
| twin-panel-floodlight-camera (Lorex product) | alarm-installation/alarm-installation-locust-point-twin-panel-floodlight-camera-product-photo.webp |
Caveat: the hero (glass-entry turret) and the lot view may be the same scenes as differently-cropped files used elsewhere in the silo (Brooklyn/NYC used a "ceiling camera above glass entry vestibule" and a "walkway view" from other folders); hashes differ. The Akuvox indoor monitor is the same product type Bronx/SI show.
DAILY-LOG note: `images: 11 reused from images/alarm-installation/ + images/access-control-installation/ (no real condo photos yet)`.

### Links
- Linked directly: /condo-security-systems-nassau-county, /condo-security-systems-hudson-valley (§13), all six live NYC condo pages (§19), /co-op-security-systems-long-island (§6, once), /intercom-installation-long-island-ny, /intercom-repair-long-island, /access-control-installation-long-island, /elevator-access-control-installation-long-island, /door-buzzer-repair-long-island-ny, /apartment-building-security-camera-installation-long-island, /alarm-installation-long-island, /fire-alarm-installation-long-island-ny, /structured-cabling-installation-long-island, /av-sound-installation-long-island (FAQ), / (home).
- FLIP comments (plain text beside each): `/condo-intercom-replacement` (§6 intercom), `/condo-security-camera-installation-long-island` (§6 cameras), `/condo-security-systems-suffolk-county` (§13 Suffolk paragraph).
- Links back needed (main run): all six live condo siblings + nassau-county/hudson-valley; one contextual link from /co-op-security-systems-long-island; per keyword rules one contextual link back from /intercom-installation-long-island-ny and /apartment-building-security-camera-installation-long-island.

### Mobile
Rendered at 390×844 with Playwright (local http.server): scrollWidth 390, no element past the viewport.


## hudson-valley

## hudson-valley

## Hudson Valley — local research for `condo-security-systems-hudson-valley` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Hub page (up-link /, phone (800) 486-0943 only, Bronx GBP #bronx / 460 E Fordham Rd). Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Rows marked "silo" were verified by earlier condo/co-op builders and reused as noted.

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY — `reddit hudsonvalley OR Westchester condo HOA board gate packages security cameras` (Firecrawl search, reddit.com only) returned only non-local threads (r/HOA, r/fuckHOA, r/orangecounty = California). Nothing used. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects claims typical of national cost guides / chatbot summaries (Angi, HomeAdvisor, Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | General geography only (no building named): downtown White Plains / Mamaroneck Ave / Metro-North; Rye, Mamaroneck, Port Chester (Sound Shore); Tarrytown, Sleepy Hollow, Mario M. Cuomo Bridge; Route 59 Nanuet/Spring Valley/New City; Route 9 Fishkill–Poughkeepsie, I-84; Route 17 Middletown/Monroe/Chester; Carmel/Mahopac/Brewster; Kingston/New Paltz/Saugerties. Described by corridor and building type, no counts. |
| 7 | Building stock / use cases | Field description (gated townhouse HOAs, garden complexes, downtown elevator condos, riverfront/station condos, 55+ communities, office/medical condos) — qualitative, no statistic claimed. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Central Hudson press release (H4). Search `Hudson Valley condo complex package theft OR car break-ins OR gate HOA Westchester Rockland Orange 2025 2026` (Firecrawl) returned only Facebook/YouTube clips (Yonkers car break-ins, Port Chester) — not citable, not used. |
| 10 | Hyperlocal | EMPTY — nothing citable on condo security found. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| H1 | Firecrawl scrape (PDF parser, directQuote "condominium figures") | https://corporate.onekeymls.com/s/WestchesterCounty-65z6.pdf | OneKey MLS Westchester County Q3-2026: "Condos Closed Sales were up 4.9 percent to 341." "Condos Median Sales Price increased 17.1 percent to $615,000." | §5 para 1; facts list; §13 Westchester para |
| H2 | `OneKey MLS Q3 2026 Dutchess County ... condos` · Firecrawl search (corporate.onekeymls.com) → Firecrawl scrape PDF | https://corporate.onekeymls.com/s/DutchessCounty-mrmd.pdf | OneKey MLS Dutchess County Q3-2026: "Condos Closed Sales were up 8.3 percent to 91." "Condos Median Sales Price increased 21.5 percent to $395,000." | §5 para 1; facts list; §13 Dutchess para |
| H3 | Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3: "This chapter shall apply to all cities of less than three hundred twenty-five thousand population and to all towns and villages." | facts list; §8.5 rules; AI check #1 |
| H4 | `Central Hudson storm power outages customers restored 2026` · Firecrawl search → Firecrawl scrape | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 26, 2026 (4 p.m.): crews "working to restore power to more than 19,000 homes and businesses that were impacted by powerful winds and heavy rain from a slow-moving nor'easter. The hardest-hit areas include Woodstock, Shawangunk, Plattekill and Hurley in Ulster County." | §5 para 4; facts list; AI check #6; §13 Ulster para |
| H5 | `New York Attorney General homeowners association offering plan 13 NYCRR Part 22` · Firecrawl search → Firecrawl scrape PDF (directQuote) | https://ag.ny.gov/sites/default/files/regulatory-documents/homeowners_association_offering_plan_questionnaire.pdf | "QUESTIONNAIRE FOR HOMEOWNERS ASSOCIATION OFFERING PLANS (Pursuant to 13 NYCRR Part 22...)"; items: "(g) if sponsor in control of board, sponsor will procure fire and casualty insurance for HOA property?"; "(d) that certified financial statements will be provided to HOA members while sponsor is in control?" | §5 para 3; §8 developers subsection; §8.5 rules; AI check #5 |
| L1 | silo (research/condo-security-systems.md L1) | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | RPL §339-e common elements text (halls, corridors, lobbies, stairs; entrances and exits; recreational or community facilities, parking areas and storage spaces; all apparatus and installations existing for common use). | §5 para 3; facts list |
| L2 | silo (Brooklyn G1) | https://www.nysenate.gov/legislation/laws/RPP/339-V | RPL §339-v reserves "for major and minor maintenance, repairs, additions, improvements, replacements". | facts list |
| L3 | silo (Brooklyn G2) | https://ag.ny.gov/sites/default/files/2022-08/how_to_handle_problems_with_a_condo_board.pdf | Boards "must follow the condo's internal rules (as set forth in the by-laws, the condominium declaration and the house rules)". | §8.5 rules list |
| L4 | silo (L4) | https://www.nysenate.gov/legislation/laws/MDW/50-A ; MDL §3 | MDL applies to cities of 325,000+ (contrast for AI check #1). | AI check #1; §8.5 |
| Q1 | silo (L7) | https://cooperatornews.com/article/the-old-fashioned-intercom-is-getting-a-makeover | CooperatorNews, Aug 3 2016, Mike Brenner (Advance Security & Intercoms, Yonkers): "Intercoms have become a lot more reliable, and the access features are expanded to include things like fingerprints and key fobs." (Not used on any other page at build time — grep checked.) | §8 RFP subsection (the page's one real quote) |
| P1 | site pages (internal), read Nov 26 2026 | /door-buzzer-repair-hudson-valley-ny, /intercom-installation-hudson-valley-ny, /elevator-access-control-installation-hudson-valley, /intercom-pricing, /door-buzzer-repair-pricing | $250 service call; $250–$525 station, $250–$475 relay/button, $325–$650 transformer, $450–$950 strike, $650–$1,800 lobby panel, $850–$2,400 riser; multi-unit intercom $1,200–$5,000; elevator access from $1,875 per car (Westchester, Level 1). Monitoring $45/mo app, $30/mo keypad (site tiers). | hero quick answer; §6; §14 table; §15 cards |

### Hudson Valley question register (this page) — add to the silo register
§9 Q&A (H3): Our gate call box has no landline and the cell signal at the entrance is weak. What are the options? · Will a gate actually make our condo community safer, or just slower? · When a car damages our gate arm, can the cameras show who did it? · Should our entrance camera record the town road outside the gate? · Most of our owners leave for the winter. Should their fobs and app access be switched off while they're away? · We're a 55+ community. What makes the entrance easier for older owners and their caregivers? · Our landscaping and snow contractors come and go all year. How should their access be set up? · Can our owner list sync from the management company's software instead of being typed in twice? · The developer is still building our later phases. Can the system we buy now reach buildings that don't exist yet? · During a two-year phased replacement, can old and new entry panels share one directory? · Deer, wind and swaying branches keep setting off our entrance camera alerts. Can that be fixed? · Can we put a camera on the cluster mailboxes by our entrance?

§17 FAQ: Which Hudson Valley towns does your Bronx office send crews to for condo work? · Do you supply security guards or gatehouse attendants for condo communities? · If the association later hires a different installer, can they service what you put in? · Will we know if a camera or reader stops working before an owner complains? · We're an HOA rather than a condominium under the Condominium Act. Does that change what you install? · Can you mount a call box or keypad on the stone pillars at our entrance? · Do you also work in office and medical condominiums? · Will you give our engineer or attorney cut sheets for the proposed equipment? · What deposit does a condo association put down, and when is the rest due? · If the internet goes down, will fobs still open our doors? · Can a camera stop non-residents from dumping trash in our condo's dumpster enclosure? · Our gatehouse is staffed only part of the day. Can a call box cover the rest?

Checked by meaning against every question on condo-security-systems-nyc/-manhattan/-brooklyn/-queens/-bronx/-staten-island and co-op-security-systems-hudson-valley (extracted with tools/check_page.py's parser at build time).

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-hudson-valley-` names; none shares a sha256 with any file in images/condo-security-systems/, images/co-op-security-systems/ or images/co-op-board-intercom-upgrade/ at build time; contact sheets compared by eye to prefer scenes/products not already shown on condo/co-op pages.
- clubhouse-ceiling-dome-above-glass-window-wall (hero/og) ← apartment-building-security-camera-installation …manhattan-dome-camera-on-ceiling-over-glass-entrance (job photo)
- eave-dome-camera-against-bare-winter-branches ← access-control-installation …indian-village-dome-camera-at-fascia-corner-by-bare-branches (job photo; similar scene to a co-op crop, different file)
- recorder-screen-camera-tiles-and-bitrate-table ← access-control-installation …harding-park-recorder-screen… (job photo; tiles tiny, no identifiable faces)
- one-button-gate-call-station-with-card-reader ← door-buzzer-repair …beverley-square-silver-one-button-door-station-with-card-reader (product)
- white-video-door-station-with-speaker-grille ← door-buzzer-repair …bedford-stuyvesant-white-video-door-station… (product)
- wall-mount-ptz-dome-for-entrance-roads ← apartment-building… westchester-county-pendant-ptz-speed-dome (product, UNV logo)
- hooded-bullet-camera-for-gate-lanes ← apartment-building… hudson-valley-black-hooded-bullet… (product)
- stainless-bullet-camera-for-parking-areas ← apartment-building… staten-island-stainless-anti-corrosion-bullet… (product)
- compact-indoor-camera-for-clubhouse-rooms ← access-control-installation …country-club-bronx-white-compact-camera-on-tilting-stand (product)
- recorder-front-and-rear-with-poe-ports ← access-control-installation …laconia-recorder-front-and-rear… (product, Swann logo visible)
- four-bay-rack-storage-appliance ← access-control-installation …new-utrecht-four-bay-rack-appliance (product)
Rejected: images/camera-repair/* (several look AI-generated), door-buzzer-repair technician shots with faces/branded shirts, buzzer-repair/*.jpg, elevator-access-control, smart-lock aess-/Astoria sets. DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + images/apartment-building-security-camera-installation/ + images/door-buzzer-repair/ (no real condo photos yet)`.

### Links left for the main run
- FLIP (plain text + `<!-- FLIP: /slug -->`): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-hudson-valley (§6 cameras), /condo-security-systems-westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county (§13 county paragraphs).
- Linked directly: /condo-security-systems-long-island (§13), /condo-security-systems-nassau-county (§19), /co-op-security-systems-hudson-valley (§13, once).
- Link backs needed: all six live condo siblings (+ LI hub, Nassau) → /condo-security-systems-hudson-valley; /co-op-security-systems-hudson-valley has a FLIP comment for this page in its §13; rules also ask for one contextual link back from /intercom-installation-hudson-valley-ny and /apartment-building-security-camera-installation-hudson-valley.


## nassau-county

## nassau-county

## Nassau County — local research for `condo-security-systems-nassau-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. GBP Brooklyn (1282 Troy Ave, #brooklyn); phone (516) 346-5778; up-link /condo-security-systems-long-island.

Thesis (kept apart from co-op-security-systems-nassau-county, which leads with garden co-ops, Long Beach Sandy damage, flood-zone lobbies and commuter lots): Nassau condos are campuses of 2–3-story wood-frame buildings, gated 55+ planned communities with guard booths/clubhouses/pools, and new concrete transit-oriented elevator condos near LIRR stations. The page is built around gatehouses and call boxes, amenity access (pool enclosure law), garage-to-lobby/elevator control, wood-frame cable paths and village/town jurisdiction.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched this run; no Nassau condo security thread verified) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects claims typical of generic AI/cost-guide answers (Angi/HomeAdvisor/Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | NC-L1 |
| 7 | Building stock / use cases | NC-N1, NC-N3, NC-N4, NC-N5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Newsday (NC-N1–NC-N5) |
| 10 | Hyperlocal | EMPTY for condo security specifically (Garden City EPOA page seen in search, not used) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| NC-N1 | `Mineola condo LIRR station transit-oriented development luxury condominium Newsday` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.newsday.com/business/mineola-condos-apartments-bridge-n0g8y0ri | Newsday, Jonathan LaMantia, updated Apr 12 2026: 101-unit condo "steps from the Long Island Rail Road", set to open 2028; empty nesters + young professionals; "More than 1,100 rental apartments have opened in Mineola since 2010" (LI Regional Economic Development Council); 10,000 sq ft ground-floor event space; rooftop pool; borders station plaza; developer: concrete and metal construction "will stand out from existing condo communities made up of two- to three-story buildings with wood construction"; village issued housing permits at 27 per 1,000 (2015–2022) vs 1.7 on rest of LI (RPA). Building name/address NOT used on page. | §5 para 1 (quote), facts list; §7 card D + transit subsection; §8 mixed-use; §13 card 1 |
| NC-N2 | Firecrawl scrape (directQuote) | https://www.newsday.com/real-estate/condos-nassau-suffolk-rajgq33c | Newsday, Arielle Dollinger, updated Apr 1 2026 (OneKey MLS): Nassau 41 closed condo sales in February, median $920,000, up from 12-month median $815,000. | §5 "Prices", facts list |
| NC-N3 | `Newsday 55-and-over condominium Nassau "gated" community Woodbury OR Plainview OR "North Hills" OR "East Meadow" condos` · Firecrawl search (excerpts) | https://www.newsday.com/classifieds/real-estate/plainview-nassau-m84715 | Development under construction on Plainview–Old Bethpage border: 143-acre gated community, 660 units (condo suites, villas, townhouses), guarded gatehouse, roving security car, 29,000 sq ft clubhouse, two outdoor heated pools. Name NOT used on page. ("24/7" wording in source deliberately not repeated.) | §5 "Three kinds" para; §13 card 6 |
| NC-N4 | same search (excerpt) | https://www.newsday.com/classifieds/real-estate/li-condos-q97939 | Same community: 135 units age-unrestricted, 80% of remainder 55+, 20% 62+; 55+ condo community in East Meadow also listed. | Background for §7 card C (55+ communities) |
| NC-N5 | `Garvies Point Glen Cove waterfront condominiums units Newsday` · Firecrawl search (excerpt) | https://www.newsday.com/long-island/nassau/garvies-point-condos-to-go-on-sale-soon-in-glen-cove-x70568 | "The entire Garvies Point project is set to include, when complete, 1,110 condos and apartments, several parks, stores, offices, restaurants". | facts list; §8 mixed-use; §13 card 5 |
| NC-G1 | reused, verified in research/co-op-security-systems.md N1 | https://www.ny.gov/counties/Nassau | Two cities, three towns, 64 incorporated villages, 60+ hamlets. | §5 "Villages, towns and the two cities" |
| NC-G2 | reused (co-op N2) | https://www.nassaucountyny.gov/DocumentCenter/View/2827/Police-Departments | Some villages run own police departments; others NCPD precincts. | §5 same para |
| NC-G3 | reused (co-op G1) | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 applies to cities under 325,000 and all towns and villages. | facts list; §8.5; §10.5 #2 |
| NC-G4 | reused (silo L1/L2) | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | Common elements incl. entrances/exits, recreational facilities, parking, "all apparatus and installations existing for common use"; bylaws may provide reserves "for major and minor maintenance, repairs, additions, improvements, replacements". | facts list; §8.5; §14 budgeting |
| NC-G5 | reused (co-op G3) | https://dos.ny.gov/security-or-fire-alarm-installer-license-law | GBL Art. 6-D license requirement. | §8.5 |
| NC-G6 | `New York State Residential Code swimming pool barrier gate self-closing self-latching requirement` · Firecrawl search (excerpts) | https://www.nysenate.gov/legislation/laws/EXC/378 ; https://law.justia.com/codes/new-york/exc/article-18/378/ | Exec. Law §378(14): gates in a swimming pool enclosure "shall be self-closing and self-latching, and shall be securely locked with a key, combination or other child proof lock sufficient to prevent access ... when such swimming pool is not in use or supervised." | facts list; §6 pools; §8.5; FAQ 5 |
| NC-G7 | `New York General Business Law 395-b viewing device fitting room restroom locker room` · Firecrawl search (excerpt) | https://www.nysenate.gov/legislation/laws/GBS/395-B | Owner/manager guilty if knowingly permits a device "for the purpose of surreptitiously observing the interior of any fitting room, restroom, toilet, bathroom, washroom, shower". (Locker rooms NOT claimed as named in statute; page lists only the named rooms + "similar rooms".) | §8 clubhouse; §8.5; FAQ 4 |
| NC-G8 | `Nassau County police false alarm ordinance alarm permit registration burglar alarm` · Firecrawl search (excerpt) | https://www.nassaucountyny.gov/DocumentCenter/View/17813/Administrative-Code-as-of-January-15-2021 | "An alarm permit holder shall advise the alarm company that monitors the permit holder's alarm system of the Nassau County Police Department permit number". No fee amounts used. | facts list; §6 alarms; §8.5; FAQ 2 |
| NC-F1 | site page (internal) | /fire-alarm-installation-nassau-county-ny | Fire Marshal path; page says exactly "we don't take Nassau fire alarm permits ourselves at this time; ask us first"; no fire alarm prices. | §6 fire alarm |
| NC-PR | site pages (internal, read Nov 26 2026) | /intercom-pricing; /door-buzzer-repair-pricing; /intercom-installation-nassau-county-new-york; /access-control-installation-nassau-county; /elevator-access-control-installation-nassau-county; /alarm-installation-nassau-county | $250 service call; repair ranges $250–$525, $250–$475, $325–$650, $450–$950, $650–$1,800, $850–$2,400; Nassau multi-unit intercom $1,200–$4,500+; encrypted fob/card reader $1,500–$3,500 per door; estate gate access (LPR + intercom) $8,000–$25,000 per gate; elevator L1 from $1,725/car, L2 from $2,875/car; monitoring $30/$45. (/intercom-repair-nassau-county inconsistent ranges not used.) | §6, §14 tables |
| NC-L1 | landmark geography (no buildings named, no counts beyond sourced rows) | — | Mineola LIRR station; Garden City/Franklin Ave; Great Neck Plaza (co-op N4: most Great Neck co-ops/condos in Great Neck Plaza and Great Neck Estates); Long Beach boardwalk; Garvies Point, Glen Cove; Old Country Road corridor (Westbury–East Meadow–Plainview). | §13 cards |

### Nassau County question register (this page) — add to the silo register
§9 Q&A (H3): Can the gate system keep a record of which owner let each visitor in? · Our guard booth is a small wooden structure with no closet. Where does the gate equipment go? · Can owners call the gatehouse from inside their homes? · Can the guard booth check a visitor against a list the owner filled in ahead of time? · Can an owner with a hearing or vision impairment get a different in-home station from the rest of the building? · What happens to our directory and credentials if the platform company goes out of business? · Can our cameras show whether the plowing contractor cleared the lanes when the invoice says it did? · Our buildings are two-story wood-frame with finished hallways. How is new cable run without opening every wall? · Our new building near the train has a ground-floor event space open at night. How do we keep its guests off the residential floors? · We are a small condo in a village downtown with one front door. Is an intercom enough, or do we need fobs as well? · Does our village or town building department have to approve a new call box, gate reader or camera pole? · What does a sensible first phase look like for a gated condo community? · The developer put consumer Wi-Fi cameras on our amenity deck. Should the association keep them?

§17 FAQ: Can the guard open the vehicle gate from inside the booth without stepping out? · Does an owner's alarm in a Nassau County condo need a police permit? · Can readers and cameras be mounted on vinyl siding without causing leaks? · Can cameras be installed in the clubhouse locker rooms or restrooms? · Can a fob reader go on the pool gate without removing its self-closing latch? · How do owners receive their new fobs, tags or app invitations when the system changes over? · Can you add a reader to the door between the parking garage and the elevator lobby? · Can a fob send the elevator only to the owner's own floor? · Our insurer's loss-control report lists security items. Can you price exactly what it asks for? · Can the clubhouse front desk let visitors in as well as the guard booth? · Can the clubhouse lights or heat come on when the first resident unlocks the door? · Can delivery trucks get a separate call box so they stop blocking the main gate?

Intent check: against the silo register (nyc, manhattan, brooklyn, queens, bronx, staten-island) and the co-op Nassau register; also against the parallel condo-security-systems-long-island and -hudson-valley drafts — dropped/replaced drafts that overlapped them: part-time gatehouse staffing, staffed + residents-only second entrance, older-owner entry features, winter fob suspension, contractor/landscaper scheduled access, cellular call box. Those topics are covered on the hubs.

### Images (11, permanent image rule; Drive/CompanyCam not checked by this subagent)
All product photos. sha256 differs from every file in images/condo-security-systems/, co-op-security-systems/, co-op-board-intercom-upgrade/ at build time; pixel dimensions also checked against those sets to catch re-encoded copies of the same photo (the Akuvox keypad station, single-button station, UniFi lit-ring reader, solar PTZ, dual-lens turret-with-warning-lights and corridor job photos were rejected for that reason). Two "job" photos from images/alarm-installation/ (Fulton Ferry weatherproof boxes, Fort Hamilton conduit pull) rejected as apparently AI-generated (garbled tool/box text). No faces, house numbers, phone numbers or "AESS"; maker logos visible (Axis, Digital Watchdog, Akuvox, Alarm.com, Ubiquiti, TP-Link VIGI, Hikvision, Dahua-style turret kit).
- black-video-door-station-with-round-call-button (hero/og) ← images/access-control-installation/access-control-installation-park-slope-video-door-station-for-brownstone-vestibule-product-photo.webp
- rounded-video-intercom-with-reader-symbol ← images/digital-watchdog-megapix-intercom.jpg (converted to WebP)
- black-keypad-and-card-reader-for-amenity-doors ← images/akuvox-vs-butterflymx/akuvox-vs-butterflymx-nyc-akuvox-a02-keypad-card-reader-product-photo.webp
- compact-door-station-with-call-button-and-reader ← images/intercom-mini-panel.jpeg (converted to WebP)
- bronze-video-doorbell-for-townhouse-entries ← images/2gig-vs-qolsys/2gig-vs-qolsys-nyc-alarm-com-white-doorbell-with-black-camera-face-product-photo.webp
- white-floodlight-camera-for-carports-and-lots ← images/residential-security-camera-installation/residential-security-camera-installation-nassau-county-white-twin-floodlight-camera-product-photo.webp
- white-flat-dome-camera-for-clubhouse-ceilings ← images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-long-island-white-flat-dome-camera-product-photo.webp
- compact-network-video-recorder ← images/access-control-installation/access-control-installation-new-utrecht-compact-network-recorder-product-photo.webp
- zoom-bullet-camera-for-entrance-drives ← images/warehouse-security-camera-installation/warehouse-security-camera-installation-dutchess-county-varifocal-bullet-camera-product-photo.webp
- dual-lens-turret-camera-for-pool-decks ← images/alarm-installation/alarm-installation-park-slope-dual-lens-turret-camera-product-photo.webp
- four-turret-cameras-recorder-and-monitor-kit ← images/security-camera-maintenance/security-camera-maintenance-rockland-county-four-full-color-turret-cameras-recorder-and-monitor-kit-product-photo.webp
DAILY-LOG note: `images: 11 reused from images/access-control-installation/ + akuvox-vs-butterflymx/ + 2gig-vs-qolsys/ + residential-, apartment-building-, warehouse-security-camera-installation/ + alarm-installation/ + security-camera-maintenance/ + 2 top-level product photos (no real condo photos yet)`.

### Links left for the main run
- FLIP comments (plain text): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-nassau-county (§6 cameras), /condo-security-systems-suffolk-county (§19).
- Linked live: /condo-security-systems-long-island (breadcrumb, schema, §19) and /condo-security-systems-hudson-valley (§19), both built in parallel.
- Link back needed from all six live condo pages + the LI hub (down-link) + /co-op-security-systems-nassau-county; per keyword rules one contextual link back from /intercom-installation-nassau-county-new-york and /apartment-building-security-camera-installation-nassau-county.


## suffolk-county

## Suffolk County — local research for `condo-security-systems-suffolk-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Area page, up-link /condo-security-systems-long-island, phone (631) 407-2884, GBP Brooklyn. Starting price $250 service call (START_PRICES). Angle kept apart from the LI hub (gatehouses, 55+ clubhouse layouts, snowbirds), Nassau (gatehouse/booth, wood-frame garden condos, village approvals, police alarm permit) and co-op Suffolk (false alarms, half-empty East End co-op, fire marshal inspection, coax, face recognition): this page is built on distance + remote administration/diagnosis, second-home owners (leak/temperature sensors, lockbox replacement), storms/outages/lightning (battery sizing, surge protection, hurricane prep), summer season timing, glare/insects, resort condos with rental desks, office/industrial condos, maintenance yards, fire alarm plan path via town/village fire marshal.

### Mandatory sources (§3) — status
| # | Source | Status |
|---|---|---|
| 1 | Reddit | EMPTY (not searched for this page; LI hub rows LIC-R1/R2 cover r/longisland) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims (Angi/HomeAdvisor/Fixr named generically); no AI quote invented. |
| 6 | Landmarks | SFK-L1 (general places, no client properties) |
| 7 | Use cases / building stock | SFK-55, SFK-NC, SFK-EH1, SFK-EH2 |
| 8 | Bing/DDG | EMPTY (not accessible in build env) |
| 9 | Local news | Suffolk County News (SFK-S1), Fire Island News (SFK-S2), 27east (SFK-EH2) |
| 10 | Hyperlocal | Town of East Hampton documents (SFK-EH1, SFK-RR), Town of Brookhaven (SFK-FA) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| SFK-G1 | `Suffolk County 10 towns 33 incorporated villages` · Firecrawl search (excerpts) | https://www.suffolkcountyny.gov/Visiting/Towns-and-Villages ; https://suffolk.my.site.com/SCCRMKnowledge/s/article/Suffolk-County-Villages | County "Towns and Villages" page lists the ten towns (Babylon … Shelter Island); county knowledge article: "Listing of 32 Suffolk County Villages." | §5 para 2; facts list |
| SFK-55 | `Suffolk County condo townhouse community 55 and over Newsday Riverhead Smithtown Huntington condominium development` · Firecrawl search (excerpt) | https://thedevitoteam.com/coops-and-condos/suffolk-county-condos/55-plus/ | "Age-restricted condo developments in Suffolk County — 74 where the MLS records show the community is 55-and-over." | §5 "What Suffolk condos look like"; facts list |
| SFK-NC | `Newsday new condominium development Suffolk 2025 2026 townhouse condos approved units …` · Firecrawl search (full excerpt) | https://phases-spaces.com/post/new-condos-melville-port-jefferson-suffolk | Nov 12 2026 (Stephanie McNeil, broker; from public filings): Huntington created Melville Town Center district late 2024; town board approved 4–1 in April with 110 condominiums as proposed; Port Jefferson 77 condominiums "coming in spring 2027"; "Most of what has gone up near Route 110 in recent years has been rentals or age-restricted communities." Project names NOT used on page. | §5 para 4; facts list |
| SFK-EH1 | `East Hampton Southampton town seasonal housing units percent vacant seasonal use census second homes` · Firecrawl search (excerpt) | https://www.ehamptonny.gov/DocumentCenter/View/28279/Route-114-Affordable-Housing-Market-Study-and-Update | Town of East Hampton market study (interim draft, 2023 data): study area 44,227 housing units; 17,993 (41%) owner-occupied primary; 20,952 (47%) seasonal, recreational or occasional use. | §5 "Second homes"; facts list |
| SFK-EH2 | same search (excerpt) | https://www.27east.com/east-hampton-press/article_610622df-48d8-5b94-808f-bc8666d4c52f.html | East Hampton Press: "In East Hampton Town, the number of vacant homes climbed from 58 percent to 60 percent over the past decade." | §5 "Second homes" |
| SFK-RR | `East Hampton town rental registry law registration required short-term rental code` · Firecrawl search (excerpts) | https://ecode360.com/30841753 ; https://www.ehamptonny.gov/DocumentCenter/View/13535/TOEH-pr-rel-Airbnb-rental-June-29-2022- | Town Code Chapter 199 Rental Registry (registration required). Town press release June 29 2022: code "allows a maximum of only two short-term rentals of less than two weeks within a six-month period." | §5 "Summer renters"; §8.5 rentals callout |
| SFK-FA | `Town of Brookhaven fire marshal fire alarm plan review permit Division of Fire Prevention` · Firecrawl search (excerpt) | https://www.brookhavenny.gov/DocumentCenter/View/1021/Permits-Submission-Requirement-PDF | Division of Fire Prevention: permits applied for on online portal; Fire Detection Systems new installations/significant alterations — installer "must have either NYS Fire Alarm License or Registration per NYS DOS." | §6 fire alarm; §8.5; facts list; Q&A fire alarm plans |
| SFK-S1 | `Superstorm Sandy Suffolk County homes damaged Fire Island Mastic Beach storm surge figures` · Firecrawl search (snippet); scrape returned no body (paywall) | https://www.suffolkcountynews.net/stories/superstorm-sandy-10-years-later,91271 | Snippet: "by the end of the week about 35 percent of homes were still without power." Area not visible in snippet → page says "South Shore communities it covers", no town named. | §5 storms; facts list |
| SFK-S2 | same search (snippet) | https://www.fireislandnews.com/eye-on-fi/7vn3inl2yuhmle182apc7ed7a6y9h4/ | Sandy "damaged hundreds of the about 4,000 structures on the island". | §5 storms |
| SFK-G2 | reused silo L1/L2, LIC-G4 | law.justia.com RPL 339-e / 339-v; MRL §3 | Common elements; bylaws/reserves; MRL applies to all towns and villages. | facts list; §8.5; pricing budget para |
| SFK-PR | site pages (internal, read Nov 26 2026) | /intercom-installation-suffolk-county-new-york; /access-control-installation-suffolk-county; /elevator-access-control-installation-suffolk-county; /door-buzzer-repair-suffolk-county-new-york; /alarm-installation-suffolk-county | $250 service call; multi-unit intercom $1,200–$4,500+; single door/gate $1,600–$5,500; lobby fob reader $1,600–$2,800; gate RFID + video intercom $2,500–$5,500; multi-door $4,500–$16,000; elevator L1 from $1,800/car, L2 from $3,000/car; buzzer parts $250–$525 / $250–$475 / $325–$650 / $450–$950 / $650–$1,800 / $850–$2,400; monitoring $30/$45. Not used: $325 door-buzzer-installation figure, intercom-repair-suffolk ranges (conflicting). | hero; §14 tables; §15 |
| SFK-L1 | landmark geography (no client properties, no unsourced counts) | — | Huntington village + Northport Harbor; Smithtown/St. James (25A); Ronkonkoma station/Lake Ronkonkoma; Bay Shore + Fire Island ferry terminals; Peconic Riverfront, Riverhead; Montauk + South Fork villages. | §13 cards |

### Suffolk County question register (this page) — add to the silo register
§9 Q&A (H3): Our condo is near the end of the North Fork. Can a problem be diagnosed before anyone drives out? · Most of our units are second homes. Can an owner's alarm warn them about a leak or a cold unit over the winter? · Owners leave keys in a lockbox for cleaners and contractors while they are away. What should replace that? · Should outdoor entry panels and cameras come down before a hurricane? · How long should the batteries keep our entry panels and readers running when the power goes out? · Lightning hit near our entrance and took out the call station and a camera. Can surge protection prevent a repeat? · How far ahead should we book pool gate and clubhouse access work before the season opens? · Our entrance faces west. Why are evening clips from the gate camera washed out, and what fixes it? · Bugs and spider webs keep blurring our cameras on summer nights. Is something wrong with them? · Our condo rents units for owners through a front desk. Can the desk issue access for each stay? · Our maintenance yard holds mowers, utility carts and fuel. What is the best way to secure it? · Who designs and files the plans when a Suffolk condo replaces its fire alarm? · The access log shows an owner's fob opening the pool while they were out of state. What happened? · Our managing agent runs several condos in the same town. Can visits be grouped to save trip time?

§17 FAQ: Will the entry panel's screen be readable in direct summer sun? · Can the system alert the board when a fob is tried at a door it doesn't open? · Can a solar-powered camera cover a lot where there is no electricity? · Can the association mount cameras on the outside walls of owners' townhouses? · Can the board require a PIN as well as a fob on the management office door? · Can the gate stop one resident tag from letting in two cars in a row? · Can the board check the backup batteries without cutting the power to test them? · Can cameras record in color at night without floodlights on every building? · Can the board see a record of who changed settings in the access system? · How do you keep rodents from chewing low-voltage cable in crawl spaces and garages? · Can owners set quiet hours for calls from the entry panel? · Will the board get a record of where every device and cable run ended up?

Intent check (by meaning) against the silo register + co-op Suffolk/LI registers + parallel westchester/rockland drafts. Dropped during build: standby generator (Rockland, Westchester), icy reader (Rockland, Westchester, HV), elevator company coordination (Westchester), reserve-study device life (Rockland), ring order / two phones (Rockland), renters' own credentials (Brooklyn, Manhattan), police alarm permit (Nassau), town approval for call box (Nassau), East End winter monitoring (co-op Suffolk), deer alerts (HV).

### Similarity
Masked-geo paragraph similarity (difflib, p/li/h3/td/figcaption ≥12 words, Jaccard prefilter) vs the nine live condo pages, co-op-security-systems-suffolk-county and the parallel westchester/rockland drafts: max 0.64 apart from the mandated warranty terms sentence (1.0, required verbatim).

### Images (11, permanent image rule; Drive/CompanyCam not checked by this subagent)
All manufacturer product photos; none shares a sha256 with any condo/co-op/co-op-board image at build time; checked by eye against the condo + co-op Suffolk/LI contact sheets and the parallel Rockland/Westchester sets (a GOSU doorbell+chime collided with Rockland and was swapped out).
- steel-keypad-entry-station-with-card-reader (hero/og) ← images/alarm-installation/alarm-installation-bath-beach-steel-keypad-entry-station-product-photo.webp (Akuvox logo; same product family appears on other condo pages — accepted, no unused intercom panel left)
- solar-panel-pan-tilt-camera-for-remote-lots ← door-buzzer-repair/…edenwald-solar-panel-and-white-pan-tilt-camera-product-photo.webp
- rack-recording-server-for-clubhouse-closet ← alarm-installation/…sunset-park-exacqvision-rack-server-product-photo.webp
- turret-camera-with-colored-led-ring ← door-buzzer-repair/…madison-white-turret-camera-with-red-and-blue-warning-lights-product-photo.webp (Uniview logo)
- bullet-camera-with-sun-hood-for-west-facing-gates ← door-buzzer-repair/…madison-white-bullet-camera-with-sun-hood-product-photo.webp (Dahua logo)
- ceiling-fisheye-camera-for-clubhouse-rooms ← door-buzzer-repair/…brooklyn-navy-yard-black-ceiling-fisheye-camera-product-photo.webp
- four-dual-lens-bullet-cameras-for-parking-courts ← door-buzzer-repair/…gowanus-four-dual-lens-bullet-cameras-on-wall-brackets-product-photo.webp
- white-dual-lens-video-doorbell ← door-buzzer-repair/…new-lots-white-and-black-dual-lens-video-doorbell-product-photo.webp (UNV logo)
- desktop-network-video-recorder ← alarm-installation/…mapleton-unv-desktop-recorder-product-photo.webp
- twin-ring-floodlight-camera-with-motion-sensor ← door-buzzer-repair/…east-flatbush-twin-ring-floodlight-camera-with-motion-sensor-product-photo.webp (Swann logo)
- pan-tilt-camera-with-red-blue-deterrence-lights ← alarm-installation/…gerritsen-beach-dahua-pan-tilt-camera-red-blue-deterrence-lights-product-photo.webp
DAILY-LOG note: `images: 11 reused from images/alarm-installation/ + images/door-buzzer-repair/ (no real condo photos yet)`.

### Links
- FLIP (plain text + `<!-- FLIP: /slug -->`): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-suffolk-county (§6 cameras).
- Linked directly: all nine live condo siblings + /condo-security-systems-westchester-county and /condo-security-systems-rockland-county (parallel batch) in §19; /co-op-security-systems-suffolk-county (§6, once); Suffolk service pages: intercom installation, intercom repair, door buzzer repair, access control, elevator access, apartment-building cameras, alarm installation, fire alarm installation, network installation, camera maintenance, smart lock installation, door buzzer installation, CCTV, security camera installation (-ny), doorbell camera, camera pricing; /intercom-pricing, /door-buzzer-repair-pricing, /warranty.
- Links back needed (main run): all nine live condo pages (Nassau and LI hub have FLIP comments for this slug; LI hub needs its down-link), /co-op-security-systems-suffolk-county (one contextual link), and per keyword rules one contextual link back from /intercom-installation-suffolk-county-new-york and /apartment-building-security-camera-installation-suffolk-county.

### Mobile
Playwright (Chrome) at 390×844: documentElement scrollWidth 390, no element past the viewport edge.


## westchester-county

## Westchester County — local research for `condo-security-systems-westchester-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Child of /condo-security-systems-hudson-valley; GBP Bronx (460 E Fordham Rd, #bronx); phone (914) 877-2578 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (kept apart from co-op-security-systems-westchester-county, which leads with co-ops outselling condos, the Yonkers intercom-panel breach, package-theft data, Con Ed heat outages and Yonkers alarm/fire codes; and from the condo HV hub's gate/grounds angle): Westchester condos are commuter buildings whose real lobby is the garage; four landscapes (station-area towers, river/Sound waterfront, village condos, northern townhouse condo groups); nested associations (master + condo groups) → partitioned permissions; resales via right of first refusal (no buyer interview) → credential hygiene at closing; Ida/Mamaroneck flooding → head-end placement; White Plains false-alarm fee schedule; county electrician trade license; MRL not MDL.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY — not searched this run (HV hub and co-op Westchester searches found no local condo-security thread). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 answers generic claims (Angi/HomeAdvisor/Fixr named generically); no AI quote invented. |
| 6 | Area landmarks | WC-3, WC-4, WC-5, WC-9 + general geography (White Plains station area, Yonkers waterfront/Getty Square, Tarrytown, Mamaroneck/Rye/Port Chester, Somers/Yorktown/Cortlandt; no buildings named) |
| 7 | Building stock / use cases | WC-1, WC-3, WC-4, WC-5, WC-9; field description (qualitative, no stats) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | The Journal News (WC-4, WC-6, WC-7, WC-9) |
| 10 | Hyperlocal | EMPTY for condo security specifically |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| WC-1 | Firecrawl scrape (PDF parser, directQuote "every figure for condos") | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_10_Westchester_County.pdf | OneKey MLS Westchester, Oct 2026 condos: closed sales Oct 114 (+1.8%), 12-mo 1,250 (+4.5%); median Oct $542,500, 12-mo $560,000 (+6.7%); DOM 12-mo 47; inventory Oct 303. | §5 para 2; facts list; hero stamp |
| WC-2 | `Heritage Hills Somers condominium community units townhouse condos Westchester` · Firecrawl search (excerpt) | https://www.heritagehills.com/ | Listings site: "consists of 2600 condos, clustered into 30 Condo groups with 53 models". Community name NOT used on page. | §5 nested associations; facts list; §7 townhouse groups; Q&A partition question |
| WC-3 | `New Rochelle downtown redevelopment units built since 2015 rezoning condos towers` · Firecrawl search (excerpts) | https://newrochelleny.gov/DocumentCenter/View/17662/2022-Year-End-Financial-Report ; https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster | Form-based zoning adopted 2015 (council approval Dec 8, 2015); "boom in residential and mixed-use development across 279 acres of the downtown"; 31 projects with site plan approval. Mostly rental (2018 affordable housing report excerpt: 1,200 market-rate apartments approved). | facts list; §8 mixed-use; §13 New Rochelle card |
| WC-4 | `Edge-on-Hudson Sleepy Hollow former GM plant condominiums townhouses units` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.lohud.com/story/news/local/westchester/sleepy-hollow/2025/06/03/edge-on-hudson-development-site-transforms-sleepy-hollow-westchester-ny-former-gm-plant/83675434007/ | Helu Wang, June 3 2025, updated Mar 18 2026: former GM assembly plant; "village within a village"; 70 acres; 1,177 townhomes, condos and apartments; 140-room hotel; 135,000 sq ft retail; 35,000 sq ft office; 16 acres parkland. Development name NOT used on page. | facts list; §7 riverfront (quote); §8 shared sites; §13 card |
| WC-5 | `Yonkers waterfront condominium Hudson River downtown redevelopment condos lohud` · Firecrawl search (excerpts) | lohud Modera (2018), Hudson Piers (2025) excerpts | New waterfront construction is mainly rental → page says condos "sit among rental towers"; no numbers used. | §13 Yonkers card; §5 landscapes |
| WC-6 | `Mamaroneck Ida flooding 2021 village damage buildings lohud Mamaroneck River` · Firecrawl search (excerpts) | https://www.lohud.com/picture-gallery/news/2021/09/02/cars-stranded-and-flooding-throughout-hudson-valley/5693416001/ ; https://www.lohud.com/picture-gallery/news/local/2021/09/03/storm-damage-aftermath-and-clean-up/5717253001/ | Sept 2 2021: "A family wades in the water as they evacuate along Mamaroneck Avenue"; Sept 3: "Mamaroneck Avenue ... is lined with items ruined by the flood waters from what was left of Hurricane Ida". | §5 storms para; facts list; §10.5 #3 |
| WC-7 | same search → Firecrawl scrape (directQuote) | https://www.lohud.com/story/news/2022/10/27/westchester-flood-history-disclosure-law-forum/69593744007/ | Eduardo Cuevas, Oct 27 2022: "In 2021, Ida devastated Mamaroneck" (search excerpt); county law requires landlords to disclose flood history before a lease (not used on page — not a security topic). | §5 storms para (quote) |
| WC-8 | `City of White Plains alarm system permit false alarm ordinance code chapter` · Firecrawl search → Firecrawl scrape | https://whiteplainspublicsafety.com/alarm-permits/ | Sec. 4-18-3(c): per false alarm in a calendar year $25 (1st), $50 (2nd–3rd), $75 (4th–5th), $100 (6th–11th), $250 (12+); FAMS portal from July 1 2025 for registration/renewal; definition quote "It includes all alarm signal activation in which investigation by police or fire personnel reveals no evidence of an emergency condition." | §6 alarms; §8.5; §10.5 #6 (page's real quote); FAQ 1 |
| WC-9 | `downtown White Plains condominium towers residential growth Metro-North TransCenter lohud` · Firecrawl search (excerpts) | https://www.lohud.com/story/news/local/westchester/white-plains/2026/11/14/white-plains-ny-construction-begins-on-development-apartments/92744274007/ | Nov 14 2026: construction began on a 296-apartment mixed-use development near North White Plains Metro-North station (rental). Background only; not cited on page. | — |
| WC-10 | `New York condominium right of first refusal board cannot reject buyer unlike co-op` · Firecrawl search (excerpts) | https://www.skybriz.com/insights/nyc-condo-board-approval-process/ ; https://www.benjamestaylor.com/resources-and-insights/right-of-first-refusal-in-nyc-condos-how-it-differs-from-co-op-board-approval | Condo boards generally exercise a right of first refusal (must buy the unit) rather than approve/reject like co-ops. Page words it as "typically", governed by the declaration; no legal advice. | §5 resales; §10.5 #2 |
| WC-11 | `USPS arrow lock apartment building entry door postal lock box carrier access` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Arrow_lock | "key keepers secured with an arrow lock allow postal carriers to access the lobby of unstaffed multifamily buildings". | Q&A mail carrier |
| WC-12 | silo L1/L2 (reused) | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://www.nysenate.gov/legislation/laws/RPP/339-V | Common elements text; reserves phrase. | §5 nested associations; facts list; §8.5 |
| WC-13 | silo H3 (reused) | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL applies to cities < 325,000 and all towns and villages. | facts list; §8.5 |
| WC-14 | co-op W14 / silo HV12 (reused) | https://consumer.westchestercountyny.gov/ | "Plumbers and electricians must obtain a trade license in order to work in Westchester County". | §6 cabling; §8.5; §10.5 #5; FAQ 2 |
| WC-15 | silo NC-G5 (reused) | https://dos.ny.gov/security-or-fire-alarm-installer-license-law | GBL Art. 6-D state license for security/fire alarm installers. | §8.5; FAQ 2 |
| WC-P | site pages (internal, read Nov 26 2026) | /intercom-installation-westchester-county-ny; /access-control-installation-westchester-county; /elevator-access-control-installation-westchester-county; /door-buzzer-repair-westchester-county; /apartment-building-security-camera-installation-westchester-county; /alarm-installation-westchester-county; /intercom-pricing; /door-buzzer-repair-pricing | $250 service call; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+; single-door access $1,500–$2,500; multi-door $4,000–$15,000; full building with elevator restriction $15,000–$40,000+; gate with video intercom + transponders $2,500–$7,000; elevator L1 from $1,875/car, L2 from $3,125/car; cameras $625–$1,875 per camera; repair ranges $250–$525 / $250–$475 / $325–$650 / $450–$950 / $650–$1,800 / $850–$2,400; monitoring $30/$45. NOT used: access page "$195/hr" callbacks, intercom page "audio $500–$800", "same-day" wording on older Westchester pages (flag for Anwar, as the co-op builder did). | hero; §6; §14 tables; §15 |

### Westchester question register (this page) — add to the silo register
§9 Q&A (H3): Our garage is shared with the rental building next door. How do we keep its tenants off our elevators? · Our community is several condo groups under one master association. Can each group keep its own codes while the master association runs the shared gates? · Our building backs onto a public waterfront park. How do we stop park visitors from using our side doors? · Construction crews for the next phase use our road every day. How do we keep them out of finished buildings? · Our riverfront lobby is mostly glass. Where can an entry panel and readers go? · Can a reader go on a fire-rated stair or corridor door without voiding its rating? · Each townhouse in our community has its own garage door. Should those openers be part of the association's access system? · Will a fob reader on our mailroom door lock out the mail carrier? · Owners who commute want the lobby door to open as they walk up from the train. Is hands-free entry safe? · Can the association charge owners for replacement fobs? · Do residential corridors need cameras, or are entrances enough? · Non-residents keep using the EV chargers in our garage. Can access control help?

§17 FAQ: What does a false alarm cost a condo owner or clubhouse in the City of White Plains? · Does your company need a Westchester County license for this work? · Who coordinates with the elevator maintenance company when a reader goes into a car? · How high should the lobby entry panel be mounted so every visitor can reach it? · Can the managing agent get a monthly access report by email without logging in? · Can the lobby screen that shows visitors also display building notices to residents? · Can the board run the intercom, fobs and cameras from one login? · Can courier delivery codes work only during daytime hours? · Can an owner see the record of who entered with their own fob? · Will elevator card readers get in the way of firefighters during an emergency? · Can the board try a new reader on one door before buying for the whole building? · Can new readers go in while our lobby or facade is being renovated?

Intent check (by meaning) against the silo register (nyc, manhattan, brooklyn, queens, bronx, staten-island, long-island, hudson-valley, nassau-county), the parallel suffolk-county and rockland-county pages (parsed from their HTML at build time) and co-op-security-systems-westchester-county. Dropped/replaced during the build because they matched a sibling: post-flood device triage (Rockland storm check), generator connection (Rockland), auto door opener with fob (Rockland wheelchair door), garage tailgating/close timer (Suffolk two cars per tag), surge warranty (Suffolk lightning surge), outdoor readers in winter (Rockland freezing rain), takeover of another installer's system (NYC), $250 visit contents (Manhattan). Checker reports no exact masked duplicates.

### Similarity
Masked-geo paragraph similarity (difflib on word sequences, protected warranty sentence / proof strip / SMS consent excluded): max 0.60 (nassau-county); all other condo pages ≤ 0.59; co-op-security-systems-westchester-county 0.54.

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied byte-for-byte into images/condo-security-systems/ with `-westchester-county-` names. sha256 of each differs from every file in images/condo-security-systems/ (incl. parallel suffolk/rockland files), images/co-op-security-systems/, images/co-op-board-intercom-upgrade/; 16×16 average-hash ≥ 47 bits from all of them. After the parallel Rockland page landed, four first-choice job photos turned out to be other encodings of the same scenes Rockland used (unfinished storage room dome, short-pole bullet, turret on beige tile, camera by exit sign); those four were swapped. Rejected: fiber-optic-installation and parking "job" photos (AI-generated, branded shirts/vans), smart-home, video-wall, warehouse Manhattan lobby (car-dealer ads readable), buzzer-repair/*.jpg, elevator-access-control, network-installation, low-voltage, commercial-security, smart-lock sets. No faces, house numbers, phone numbers or "AESS"; maker logos on product photos (UNV, Honeywell, Hikvision, Ubiquiti).
| Page file (…westchester-county-) | ← Source | Kind | Where |
|---|---|---|---|
| ceiling-dome-above-glass-lobby-windows (hero/og) | images/alarm-installation/alarm-installation-flatbush-ceiling-dome-over-glass-lobby-entrance.webp | job | hero |
| four-dome-cameras-above-slim-recorder | images/school-security-camera-installation/school-security-camera-installation-orange-county-four-dome-cameras-above-slim-recorder-product-photo.webp | product | §5 |
| cable-bundles-over-recorder-monitor | images/access-control-installation/access-control-installation-soundview-cable-bundles-above-recorder-monitor.webp | job | §12 |
| white-dome-camera-beside-ceiling-light-panel | images/access-control-installation/access-control-installation-harding-park-white-dome-camera-beside-ceiling-light-panel.webp | job | §9 |
| recorder-views-of-side-path-and-storeroom-door | images/access-control-installation/access-control-installation-morris-heights-recorder-views-of-brick-side-path-and-storeroom-door.webp | job | §7 end |
| mini-ptz-dome-camera-for-garage-ramps | images/hikvision-security-camera-installation/hikvision-security-camera-installation-westchester-county-mini-ptz-dome-product-photo.webp | product | §7 riverfront |
| small-domes-across-ground-floor-shop-ceiling | images/access-control-installation/access-control-installation-morris-heights-small-domes-spread-across-shop-drop-ceiling.webp | job | §8 |
| black-video-doorbell-with-bell-button | images/alarm-installation/alarm-installation-fort-greene-dark-video-doorbell-with-bell-button-product-photo.webp | product | §10 |
| compact-network-video-recorder-with-usb-ports | images/nvr-installation/nvr-installation-westchester-county-compact-recorder-with-front-usb-ports-product-photo.webp | product | §6 |
| clear-dome-camera | images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-westchester-county-clear-dome-camera-product-photo.webp | product | §10 |
| white-bullet-camera-with-blue-lens-ring | images/unifi-protect-vs-hikvision/unifi-protect-vs-hikvision-nyc-unifi-white-bullet-camera-blue-lens-ring-product-photo.webp | product | §14 |

DAILY-LOG note: `images: 11 reused from images/alarm-installation/ + access-control-installation/ + school-security-camera-installation/ + hikvision-security-camera-installation/ + nvr-installation/ + apartment-building-security-camera-installation/ + unifi-protect-vs-hikvision/ (no real condo photos yet)`.

### Links
- Linked live: up /condo-security-systems-hudson-valley (breadcrumb, §6, §19); all 9 earlier condo pages + parallel /condo-security-systems-suffolk-county and /condo-security-systems-rockland-county (§19); /co-op-security-systems-westchester-county (§6, once); /intercom-installation-westchester-county-ny, /intercom-repair-westchester, /door-buzzer-repair-westchester-county, /access-control-installation-westchester-county, /elevator-access-control-installation-westchester-county, /apartment-building-security-camera-installation-westchester-county, /alarm-installation-westchester-county, /fire-alarm-installation-westchester-county-new-york, /structured-cabling-installation-westchester-county, /door-buzzer-installation-westchester-county-ny, /cctv-installation-westchester-county, /security-camera-maintenance-westchester-county, /network-installation-westchester-county, /security-camera-installation-westchester-county-ny, /door-buzzer-repair-pricing, /intercom-pricing.
- FLIP comments (plain text): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-westchester-county (§6 cameras), /condo-security-systems-orange-county, -putnam-county, -dutchess-county, -ulster-county (§19).
- Link backs needed (main run): all 9 earlier condo pages (checker lists them) + the HV hub's existing FLIP for this page; /co-op-security-systems-westchester-county (one contextual link); per keyword rules one contextual link back from /intercom-installation-westchester-county-ny and /apartment-building-security-camera-installation-westchester-county.

### Mobile
390px overflow check not run: launching a local server + headless Chrome was denied by the environment's permission classifier. Layout is the same template/classes as the passing condo siblings (tables wrapped in overflow-x containers).


## rockland-county

## Rockland County — local research for `condo-security-systems-rockland-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Child of /condo-security-systems-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx); phone (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (kept apart from co-op-security-systems-rockland-county, which leads with garden co-ops in Suffern/Spring Valley, county code enforcement and abandoned facade cable, and from condo-security-systems-nassau-county, which leads with gatehouses/guard booths and transit elevator condos): Rockland condos are mostly townhouse loops with private roads, pools, clubhouses and courts (Valley Cottage, New City, Nanuet, Congers, Pomona), plus phased riverfront elevator condos (Nyack, Piermont, Haverstraw) and 55+ communities (Stony Point, Pearl River). The page is built around resale turnover and credential churn (543 sales/12 mo, inventory up 69%), showing-agent access, river flooding and long storm outages, long site runs (trenching / wireless links) and amenity control.

Not thin: OneKey shows 543 condo sales in 12 months (vs 71 co-op sales), Redfin 177 active condo listings across 15 ZIPs — substantive, distinct stock.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched separately this run; co-op Rockland builder found no r/rocklandcounty thread on the topic) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims typical of chatbot/cost-guide answers (Angi/HomeAdvisor/Fixr named generically; HomeAdvisor range reused from silo). No AI quote invented. |
| 6 | Area landmarks | RC-G1 (towns/villages/stations/ferry/bridge), Palisades Center = Rockland (blueprint Appendix B) |
| 7 | Building stock | RC-M1, RC-M2, RC-M3, RC-M4, RC-M5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | RC-W1–RC-W4 (O&R, Rockland County Times, Rockland Daily), RC-N1 (Daily Voice, reused), RC-N2 (News 12, reused) |
| 10 | Hyperlocal | Rockland County Times, Rockland Daily (RC-W2–W4) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| RC-M1 | Firecrawl scrape (PDF parser, directQuote "Condos ... closed sales, median, inventory") | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_10_Rockland_County.pdf | OneKey MLS Rockland, Oct 2026, Condos: closed sales Oct 52 (54 prior); 12 mo thru 10-2026 = 543 (552 prior, −1.6%); DOM 12-mo 41; median 12-mo $475,000 (+8.2% from $439,000); Oct median $431,500; inventory Oct 193 (114 prior, +69.3%). | §5 para 2 + facts; Q&A showings; hero intro context |
| RC-M2 | Firecrawl scrape (freeform query) | https://www.redfin.com/county/1988/NY/Rockland-County/condos | Nov 26 2026: 177 condos for sale, median list $449K; listings in Pomona, Valley Cottage, Spring Valley, Nanuet, Suffern, New City, Tappan, West Nyack, Congers, Haverstraw, Piermont, Stony Point, Pearl River, Monsey, Bardonia; amenity notes: clubhouse (Pomona, country-club road), pool + clubhouse (Valley Cottage), gated community (Nanuet), community pool / clubhouse / tennis courts (New City), community pool (Piermont), 55+ (Stony Point, billiards, BBQ; Pearl River, private elevator), gated + garage parking (Piermont). Addresses NOT used on page. | §5 three types + facts; §7 golf/country-club card (conditional wording); §13 cards |
| RC-M3 | `Haverstraw waterfront condominium complex Hudson River condos ferry Rockland` · Firecrawl search → Firecrawl scrape (directQuote) | https://hvmag.com/home-real-estate/this-luxury-waterfront-condo-development-boasts-river-views-in-haverstraw/ | Hudson Valley Magazine, Virginia Croft, Sept 19 2019: phase one two buildings, sixteen units; "At completion, the final phases will result in 40 total units in five buildings."; two swimming pools, fitness center, indoor basketball court, café. Development name NOT used on page. | §5 three types (quote); §7 riverfront card |
| RC-M4 | `Nyack condominium riverfront condos elevator building Nyack NY 10960 condo association` · Firecrawl search (excerpts) | https://www.facebook.com/ClermontCondos/ ; https://www.rivertownsrealty.com/property/784-968821-6-burd-street-2406-nyack-NY-10960 ; https://commonelements.com/directory/associations/nyack-mews-condominium-cacc9265 | Riverfront gated condo complex in Nyack with elevators and fitness center; other Nyack condo associations listed. Names NOT used on page (described as "riverfront elevator condos, some gated"). | §5; §7 riverfront; §13 Nyack card |
| RC-M5 | `Rockland County townhouse HOA condominium New City Pomona Stony Point Nanuet Pearl River condos for sale` · Firecrawl search (excerpts) | https://www.realtor.com/realestateandhomes-search/Rockland-County_NY/show-55-plus ; https://www.realestatehudsonvalleyny.com/rockland-towns/new-city-townhouses-new-city-condos/ | 55+ community listings in Rockland (townhouses and condos, New City etc.); New City townhouse condo complex with monthly HOA fee. Background only. | §5 / §7 55+ card (background) |
| RC-G1 | reused, co-op Rockland R3 (Wikipedia) | https://en.wikipedia.org/wiki/Rockland_County,_New_York | 199.34 sq mi, "smallest county by area in New York outside New York City"; 5 towns (Clarkstown, Haverstraw, Orangetown, Ramapo, Stony Point); 18 villages; county seat New City; Mario M. Cuomo Bridge; Port Jervis Line (Suffern, Sloatsburg), Pascack Valley Line (Pearl River, Nanuet, Spring Valley); NY Waterway Haverstraw–Ossining ferry. | §5 towns/villages; §10.5 #6 bridge; §13 cards |
| RC-G2 | reused, co-op Rockland R5 | https://www.census.gov/quickfacts/rocklandcountynewyork | 109,999 housing units; owner-occupied 67.9%. | §5 facts list |
| RC-G3 | reused, co-op Rockland R6 | https://hudsonvalley.news12.com/rocklands-office-of-buildings-and-codes-reflects-on-2-year-anniversary-of-taking-over-inspections-code-enforcement-in-village-of-spring-valley | County Office of Buildings and Codes took over code enforcement in Village of Spring Valley Feb 14 2022 under state order. | §5 towns/villages para |
| RC-G4 | reused, co-op Rockland R8 | https://dos.ny.gov/notice-adoption | 2025 NYS Uniform Code effective December 31, 2025. | §8.5 compliance list |
| RC-G5 | reused, co-op Rockland R9 | https://ecode360.com/26997705 | Rockland County Code Ch. 250: electrical contractor = wiring for light, heat or power or signaling systems on 50 volts or more under a master electrician. | §5 facts; §8.5; §10.5 #2 |
| RC-G6 | reused, co-op Rockland R10 | https://ecode360.com/6704537 | Clarkstown Ch. 91: alarm users "shall obtain an alarm user permit from the Police Department". (Penalties not used.) | §5 facts; §6 alarms |
| RC-G7 | reused, silo HV3 / co-op R14 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 applies to cities under 325,000 and all towns and villages. | §5 towns/villages |
| RC-G8 | reused, silo L1/L2 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | Common elements incl. entrances/exits, recreational facilities, parking, "all apparatus and installations existing for common use"; reserves "for major and minor maintenance, repairs, additions, improvements, replacements". | §5 facts; §14 budgeting |
| RC-G9 | reused, Nassau NC-G6 | https://www.nysenate.gov/legislation/laws/EXC/378 | Exec. Law §378(14): pool enclosure gates self-closing, self-latching, locked when not in use or supervised. | §5 facts; §6 amenities; §8.5; equipment locks |
| RC-G10 | reused, Nassau NC-G7 | https://www.nysenate.gov/legislation/laws/GBS/395-B | No surreptitious viewing devices in restrooms, bathrooms, showers, fitting rooms etc. | §8.5; §10.5 #7 |
| RC-G11 | reused, co-op R15 | https://www.nysenate.gov/legislation/laws/GBS/69-M | State licensing of security/fire alarm installers. | §5 facts; §10.5 #2 |
| RC-G12 | reused, co-op R21 / silo L11 | https://cooperatornews.com/article/qa-camera-placement | Audio recording may implicate Penal Law eavesdropping provisions. | §8.5; §10.5 #7 |
| RC-G13 | reused, co-op R19 | https://intro.nyc/local-laws/2021-63 | TDPA is NYC Local Law 63/2021 — city law, not Rockland. | §8.5 |
| RC-G14 | `Dig Safely New York 811 call before you dig required by law two working days excavators 16 NYCRR 753` · Firecrawl search (excerpt) | https://udigny.org/resources/nys-code-rule-753/ (also https://dps.ny.gov/underground-damage-prevention) | Code Rule 753: notice "shall be served at least two but not more than ten working days, not including the date of the call". | Q&A trenching |
| RC-W1 | reused, co-op R11 | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k | O&R July 6 2026: storms since July 1 impacted more than 47,000 customers. | §5 storms; §6 cable/backup; §10.5 #4 |
| RC-W2 | reused, co-op R12 | https://rocklandtimes.com/2026/07/09/massive-storm-sweeps-through-rockland/ | Rockland County Times July 9 2026: 6,466 Rockland customers out 11:30 p.m. July 4; New City neighborhood "had no power for over 36 hours". | §5 storms; §10.5 #4 |
| RC-W3 | `Piermont Nyack Haverstraw Hudson River flooding storm surge Sandy waterfront Rockland` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.rocklanddaily.com/news/piermont-experiences-worst-flooding-since-hurricane-sandy | Rockland Daily, Jan 14 2024: "The Village of Piermont was hit hard by tidal flooding from Friday night's storm" — headline: worst flooding since Hurricane Sandy. | §5 storms; Q&A post-flood check; §10.5 #5; field notes |
| RC-W4 | same search (excerpt) | https://rocklandtimes.com/2012/11/02/the-impact-of-hurricane-sandy/ | Rockland County Times, Nov 2 2012: "Rockland residents living near the Hudson River got the worst of Sandy." | §5 storms; §10.5 #5 |
| RC-N1 | reused, co-op R20 / silo HV11 | https://dailyvoice.com/article/packages-stolen-from-apartment-complex-found-inside-haverstraw-home-man-35-charged-cops-say/ | Apr 2026: packages taken from several buildings within a Haverstraw complex, later recovered in a search (suspect not named). | §5 complaints; §6 packages |
| RC-Q1 | reused, co-op R18 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500". | §10.5 #3 |
| RC-P1 | site pages (internal), read Nov 26 2026 | /intercom-installation-rockland-county-ny ; /access-control-installation-rockland-county ; /elevator-access-control-installation-rockland-county ; /door-buzzer-repair-rockland-county ; /intercom-pricing ; /door-buzzer-repair-pricing | $250 service call; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+; access single door/gate $1,700–$5,000; multi-door $4,500–$15,000; elevator L1 from $1,950/car, L2 from $3,250/car; buzzer parts: station $250–$525, transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400. Monitoring $30/$45 (site tiers). NOT used: /intercom-installation-rockland-county-new-york ranges (conflict, as flagged by co-op builder). | hero; §6; §14 tables; §15; §10.5 #3 |

### Rockland question register (this page) — add to the silo register
§9 Q&A (H3):
- With so many units listed for sale, how do we let showing agents into the building and amenities without giving out a master code?
- An owner is renovating for three months. How should the contractor's crew get in each day?
- We're switching management companies. What has to be handed over so the new agent can run the access system?
- Prospective buyers keep asking what security the community has. What can the board safely share?
- Our longtime superintendent is retiring, and only he knows how the system works. What should we capture before he leaves?
- Non-residents have been using the electric vehicle chargers in our parking area. Can access control stop that?
- Before you trench cable across our lawn, who checks for buried gas, water and irrigation lines?
- Is a wireless link between two of our buildings reliable through heavy rain and snow?
- Can the pool's chemical storage room have its own lock and record, separate from the pool gate?
- Can your proposal give each device an expected service life we can drop into our reserve study?
- Some owners avoid operating electronic devices on the Sabbath. Are there entry options that work for them?
- Can the freight or passenger elevator be held for a move-in without someone riding it all day?

§17 FAQ:
- How long is your written quote valid while our board waits for its next meeting?
- Is an emailed approval from the board president enough to start a repair, or do you need a signed proposal?
- How will owners know the people working in the building are your technicians?
- Can you work from the developer's as-built drawings, or do you survey the property yourselves?
- The developer left empty conduit between buildings for future wiring. Can you use it?
- Can you test our existing cable before the board decides whether to replace it?
- Can the intercom ring two phones for one unit, such as both owners' cell phones?
- How do you protect hallway carpets, floors and finished walls during the work?
- Can the clubhouse and pool doors lock on command when the board closes the grounds for a storm?
- Can the entry panel screen show our community's name and logo?
- Can readers and entry panels be mounted at a height that works for residents who use wheelchairs?
- If the board doesn't hire you after the free assessment, does the association owe anything?

Checked by meaning against every question on the nine live condo pages (nyc, manhattan, brooklyn, queens, bronx, staten-island, long-island, hudson-valley, nassau-county), the parallel suffolk-county page as it stood on disk, and co-op-security-systems-rockland-county (parsed with tools/check_page.parse). Dropped for overlap: police alarm permit (Nassau), flood-zone equipment placement (Long Island — kept only as the post-flood inspection question), power-failure lock behavior (Queens/Staten Island), guest pass expiry (Staten Island), closing shut-off of seller credentials (Manhattan), insurer loss-control (Nassau), village approval for poles (Nassau), far-pool connection (Long Island), registered-bike amenity (Queens), travel surcharge (Bronx), Sabbath scheduling (co-op Rockland — this page's question is about entry options, not work scheduling). Also checked against the parallel westchester-county and suffolk-county pages once they appeared on disk: dropped my drafts on generator power, post-flood device check, winter keypad durability and automatic door openers (Westchester covers those intents).

### Images (11) — permanent image rule; no Drive/CompanyCam check in this run
Pool screened by SHA-256 + 16×16 average hash against every file in images/condo-security-systems/, images/co-op-security-systems/, images/co-op-board-intercom-upgrade/ and every image referenced on a condo-*/co-op-* page at build time; after a final cross-check against the parallel Westchester/Suffolk files, two first picks were dropped as the same scenes as live condo photos (the Toyota hallway camera = Bronx condo hallway image; the Mott Haven double-height hall = Manhattan amenity hall). All candidate intercom/keypad/door-reader photos in fiber-optic-installation/, social/, ai/, smart-home/ and the top-level access-control-*.jpg were REJECTED (AI-generated, faces, "ABSTRACT" branded shirts/vans). Rockland Toyota / Nassau window-depot job photos with dealer or store signage were rejected or cropped. No faces, house numbers, plates, readable documents or "AESS" text in any kept image (visible marks: LOREX on the recorder, aosu on the doorbell and floodlight camera).
| Page file (images/condo-security-systems/condo-security-systems-rockland-county-…) | ← Source | Kind | Where |
|---|---|---|---|
| small-camera-high-on-curved-wall-above-drop-ceiling.webp (1247×935) | images/rockland-toyota-wall-camera.jpeg | real Rockland job photo | hero (eager), og/twitter |
| small-domes-spread-across-drop-ceiling-grid.webp | images/door-buzzer-repair/door-buzzer-repair-morrisania-small-domes-across-drop-ceiling-grid.webp | job photo | §5 |
| small-camera-on-ceiling-grid-beside-red-exit-sign.webp | images/door-buzzer-repair/door-buzzer-repair-east-flatbush-lobby-ceiling-camera-beside-lit-exit-sign.webp | job photo | §6 cameras |
| white-turret-camera-on-ceiling-tile.webp | images/door-buzzer-repair/door-buzzer-repair-brownsville-white-turret-camera-on-beige-ceiling-tile.webp | job photo | §7 garden |
| battery-video-doorbell-with-plug-in-chime.webp | images/door-buzzer-repair/door-buzzer-repair-beverley-square-battery-video-doorbell-with-plug-in-chime.webp | product (aosu) | §7 55+ |
| black-bullet-camera-on-short-ceiling-pole-mount.webp | images/door-buzzer-repair/door-buzzer-repair-mount-eden-black-bullet-camera-on-short-pole-mount-at-ceiling.webp | job photo | §8 |
| dome-camera-in-unfinished-storage-room-corner.webp | images/door-buzzer-repair/door-buzzer-repair-new-lots-unfinished-room-corner-with-lumber-and-dome-camera.webp | job photo | §9 |
| four-white-bullet-cameras-on-wall-brackets.webp | images/door-buzzer-repair/door-buzzer-repair-edenwald-four-white-bullet-cameras-on-wall-brackets-product-photo.webp | product | §10 |
| recorder-front-panel-with-playback-keys.webp | images/door-buzzer-repair/door-buzzer-repair-highbridge-lorex-recorder-front-panel-with-playback-keys.webp | product (Lorex) | §10 |
| white-dome-camera-beside-ceiling-light-panel.webp | images/door-buzzer-repair/door-buzzer-repair-brooklyn-navy-yard-white-dome-camera-beside-ceiling-light-panel.webp | job photo | §12 process |
| twin-floodlight-pan-tilt-camera-with-antennas.webp | images/door-buzzer-repair/door-buzzer-repair-fordham-white-twin-panel-floodlight-pan-tilt-camera-with-antennas.webp | product (aosu) | §14 |

DAILY-LOG note: `images: 11 reused (1 real Rockland job photo + 6 job photos + 4 product shots) from top-level rockland-toyota-* and images/door-buzzer-repair/ (no real condo photos yet)`.

### Links left for the main run
- FLIP (plain text + `<!-- FLIP: /slug -->`): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-rockland-county (§6 cameras), /condo-security-systems-orange-county, -putnam-county, -dutchess-county, -ulster-county (All Areas).
- Linked directly (parallel builds): /condo-security-systems-westchester-county (broken until it ships — remove the anchor if Westchester fails), /condo-security-systems-suffolk-county.
- Intercom page: linked /intercom-installation-rockland-county-ny (both -ny and -new-york are self-canonical; -ny is the one whose prices the condo and co-op pages use).
- Link backs needed: all live condo siblings + /condo-security-systems-hudson-valley (hub link down) → this page; /co-op-security-systems-rockland-county → this page once; keyword-file rule: one contextual link back from /intercom-installation-rockland-county-ny and /apartment-building-security-camera-installation-rockland-county.

### Mobile
390px render check not run: the headless browser launch was denied in the build environment. Main run should render at 390px.

### Similarity
Masked-geo paragraph similarity (difflib, p/li/td ≥12 words) against all condo-security-systems pages on disk (incl. Suffolk, Westchester) and co-op-security-systems-rockland-county: max < 0.65 apart from the standard trust row ("Owner-operated since 2002 · Thousands of jobs …"), which is shared template text.


## orange-county

## Orange County — local research for `condo-security-systems-orange-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Child of /condo-security-systems-hudson-valley; GBP Bronx (460 E Fordham Rd, #bronx); phone (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Built by a batch subagent. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (kept apart from co-op-security-systems-orange-county, which leads with the tiny $167,000 co-op market, 1960s garden courts, single-family co-ops, long drives and the New Windsor theft-ring warning; and from the Rockland condo page's turnover/river/Sabbath angle): Orange County condos are mostly 1970s–80s garden and townhouse complexes around Newburgh/New Windsor/Middletown with pools and courts and tired developer-era stair-hall intercoms (many small separate systems), newer phased garage-under townhouse sections (Monroe, Highland Mills, Washingtonville, Chester) with builder-held accounts, a Village of Warwick 55+ neighborhood, and a large elevator-condo district at Kiryas Joel (4–5 story buildings, commercial building on campus). Modest HOA fees ($120–$584 in listings) make recurring subscriptions the board's key question; inventory up 51.8% means more showings and credential churn.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY — not searched this run (co-op Orange search `reddit r/Newburgh apartment building buzzer intercom package stolen` returned no reddit.com result). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims (doorman model, NYC MDL intercom rule, HomeAdvisor range, consumer devices, unlicensed installers, cloud-always, same-day); no AI quote invented. |
| 6 | Area landmarks | General geography (no customer property): Newburgh waterfront / Newburgh-Beacon Bridge, Stewart International Airport, Middletown + Port Jervis Line station (OR6), Woodbury Common / Harriman station, Goshen county seat / Legoland New York, West Point / Bear Mountain Bridge / Route 9W. |
| 7 | Building stock / use cases | OR2, OR3, OR4, OR5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Times Herald-Record (OR3, OR4); News 12 (OR7, reused) |
| 10 | Hyperlocal | Firecrawl search `Orange County NY condo complex packages stolen OR break-ins OR car thefts police 2026 ...` (news+web) returned only the New Windsor theft-ring item already used on the co-op page, social-media clips and unrelated stories. Nothing new used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| OR1 | `OneKey MLS Orange County October 2026 condos closed sales median price report` · WebSearch → Firecrawl scrape (PDF parser, directQuote). (WebFetch of the Q3 PDF on the same host was blocked — permission prompt not answered.) | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_10_Orange_County.pdf | Condos: new listings Oct 42 (+27.3%), 12-mo 502 (+14.9%); closed sales Oct 33 (+37.5%), 12-mo 359 (+3.8%); DOM Oct 46 (−25.8%), 12-mo 45; median Oct $329,000 (+12.5%), 12-mo $320,000 (+1.6%); inventory Oct 126 vs 83 (+51.8%). | §5 para 2; facts list; hero stamp |
| OR2 | Firecrawl scrape (query: towns, prices, years, amenities, no addresses) | https://www.redfin.com/county/1980/NY/Orange-County/condos | Nov 26 2026: 126 condos for sale, median list $325K. Towns: Newburgh, Middletown (one "Gated community"), Monroe (built 2023), New Windsor, Southfields, Montgomery, Chester (pools, tennis, gym, playground), Highland Mills, Washingtonville (clubhouse, pool, tennis, basketball), Harriman (pool, tennis, playground), Palm Tree (built 2022), Fort Montgomery. Built 1973 and 1978 (Newburgh). HOA fees listed ~$120–$584/mo. Community names NOT used on page. | §5 "What the listings say"; facts list; §7 cards; §13 cards |
| OR3 | `Kiryas Joel Palm Tree condominium buildings housing multifamily condos Times Herald-Record` · Firecrawl search (snippet) | https://www.recordonline.com/story/news/2017/12/10/kj-board-oks-1-600/16862695007/ | Dec 10 2017: Kiryas Joel approved construction of 1,600 apartments (condos) on 70 acres. | §5 elevator district para; facts list |
| OR4 | same search → Firecrawl scrape (directQuote) | https://www.recordonline.com/story/news/local/2022/05/19/kiryas-joel-move-into-veyoel-moshe-gardens-condo-apartment-complex/9735978002/ | Times Herald-Record, Chris McKenna, May 19 2022: families moving into "the four- and five-story buildings completed so far" of a 1,600-unit condo complex on 70 acres; ~500 homes built or nearly done, ≥300 sold; units sold $260,000–$575,000 since February; 3 of 69 residential buildings replaced by a six-story building for a supermarket, stores and rentable offices. Complex name NOT used on page. | §5; §7 elevator districts; §8 stores on campus |
| OR5 | `Orange County NY 55 and over active adult condominium community ...` · Firecrawl search → Firecrawl scrape | https://www.realestatehudsonvalleyny.com/orange-towns/orange-county-adult-55-plus/ | Village of Warwick 55+ community with condos, townhomes and 165 single-family homes, walkable to downtown Warwick. (Other listed 55+ communities are single-family → not used.) Community name NOT used. | hero; §5 para 1; §7 55+ card |
| OR6 | reused co-op OC4 | https://www.njtransit.com/abc_PORT_JERVIS | Port Jervis Line stations incl. Middletown NY, Harriman, Salisbury Mills, Campbell Hall, Otisville, Port Jervis. | §13 cards |
| OR7 | reused co-op OC7 | https://westchester.news12.com/2026/01/26/orange-county-digging-out-after-one-of-the-heaviest-snowfalls-in-years/5EGxAQpDFUcIljIxmGnlrS | News 12, Jan 26 2026: ~18 in. in Monroe (county high cited), up to 24 in. in some areas. | §5 winter para |
| OR8 | `Town of Wallkill OR Town of New Windsor OR Town of Monroe alarm permit false alarm code ecode360` · Firecrawl search → Firecrawl scrape (directQuote) | https://ecode360.com/6189204 | Town of New Windsor Ch. 86 "Automated Alarm System Law" (L.L. 1-2007): automatic dialers may not connect directly to police/fire emergency lines; external audible alarms must auto-cut off after ≤15 min; fines $0–$50 first, $25–$100 second, $50–$500 and/or ≤15 days third+; each false alarm a separate offense. | facts list; §6 alarms; §8.5 rules; FAQ siren |
| OR9 | reused co-op OC1 | https://www.census.gov/quickfacts/orangecountynewyork | 812.32 sq mi land. | §5 "Three cities" para |
| L1/L2 | silo L1/L2 | law.justia.com 339-e; nysenate RPP 339-V | Common elements; reserves. | facts list; §14 funding |
| H3 | silo (HV H3) | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL applies to cities <325,000 and all towns and villages. | §5; AI check #2 |
| X1 | silo (Rockland) | Executive Law §378 | Pool enclosure gates self-closing/self-latching, locked when unsupervised. | facts list; §8.5; Q&A chain-link |
| X2 | silo | GBL §69-m; GBL §395-b | Installer licensing; no cameras in restrooms etc. | facts; §8.5; AI check #5 |
| X3 | reused co-op OC17 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | Normal range $1,200–$8,500. | AI check #3 |
| P1 | site pages (internal), read Nov 26 2026 | /intercom-installation-orange-county-ny; /door-buzzer-repair-orange-county-new-york; /access-control-installation-orange-county; /elevator-access-control-installation-orange-county; /alarm-installation-orange-county; /intercom-pricing; /door-buzzer-repair-pricing | $250 service call; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+; access single door/gate $1,700–$5,000, multi-door $4,500–$15,000; elevator L1 from $2,100/car, L2 from $3,500/car; buzzer repairs station $250–$525, relay $250–$475, transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400; monitoring $30/$45. NOT used: /intercom-repair-orange diagnostic "$198–$396" ranges and /door-buzzer-installation-orange-county-ny "$300 service call" (both conflict with the $250 start price — flag for Anwar). Camera prices from the apartment-building camera page not used (camera section kept short). | §6, §14 tables, §15 |

### Orange County question register (this page) — add to the silo register
§9 Q&A (H3): Children wait for the school bus at our entrance. Should a camera cover the stop? · Drivers speed through our private loop road. Can cameras help the board enforce its rules? · Our complex has guest spaces where non-residents leave cars for days. Can cameras help? · Can a lifeguard or attendant see the photo of the owner whose fob just opened the pool gate? · Our pool is fenced with chain link. Can a reader and lock go on that kind of gate? · Our clubhouse has a standby generator. Can the security equipment run from it? · Do outdoor readers and keypads keep working through single-digit winter cold? · Families push strollers through our lobby doors all day. Can a powered door opener work with the fob system? · In a complex with many buildings, should every owner's fob open every building? · Our complex sits across a town line. Which building department do we deal with? · Can our cameras and intercom run without sending anything to an outside cloud service? · Our maintenance staff wants to pull some of the cable to save money. Can the work be split?

§17 FAQ: If your crew finds a wiring problem that belongs to an electrician, what happens next? · An agent left a lockbox hanging on our lobby door railing. Is that a security problem? · Some owners want the fitness room open overnight. Can that be done safely? · Is there a way to tell which unit a lost fob found in the parking lot belongs to? · Can owners switch off their own lost fob from an app? · Can a camera at the pool speak a warning to people who climb the fence after hours? · An owner's outdoor siren keeps sounding while they are away. What do local rules expect? · Can a buyer's fobs be ready before closing so they can get in on moving day? · Does the board need an engineer's drawings for an access control job? · Will you price both a repair-only plan and a full replacement so the board can compare? · Can owners view the building entrance on their smart TV instead of a phone? · Should the association keep spare readers and fobs on hand?

Checked by meaning against every question on the 12 live condo pages, the parallel Putnam and Dutchess condo drafts present at build time, and co-op-security-systems-orange-county (extracted with tools/check_page.py's parser). Dropped as too close: school-pickup/landline call box (HV), first-phase plan (Nassau), delivery-truck damage (HV gate arm), travel to western towns (HV/Bronx), fobs per apartment (co-op Orange), pool-gate latch (Nassau).

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `-orange-county-` names. None shares a sha256 with any file in images/condo-security-systems/, images/co-op-security-systems/ or images/co-op-board-intercom-upgrade/; 16×17 difference-hash compared against all of them (including the parallel Putnam/Dutchess sets at finish) and contact-sheet viewed. A first pick (gowanus dark-grey PTZ on pendant arm) matched the parallel Putnam set exactly and was swapped for the morris-heights bullet on ball mount. No faces, house numbers, plates or "AESS"; small brand marks visible on some product photos (Lorex on the twin-light bullet, Dahua-style speed dome).
| Page file (…-orange-county-…) | Source | Kind | Section |
|---|---|---|---|
| video-door-station-with-light-bar-and-card-symbol (hero, og) | door-buzzer-repair/…coney-island-doorbell-with-bright-light-ring-and-card-icon | product | hero |
| recorder-view-along-brick-wall-to-paved-lot | door-buzzer-repair/…kensington-recorder-view-along-brick-wall-to-paved-yard | job photo | §5 |
| two-small-cameras-high-on-wall-below-upper-windows | door-buzzer-repair/…fort-greene-two-small-cameras-on-tall-wall-under-mezzanine-windows | job photo | §6 |
| ceiling-pendant-dual-lens-camera-with-light-bar | door-buzzer-repair/…morris-heights-pendant-dual-lens-camera | product | §7 |
| two-white-pan-tilt-domes-with-warm-white-lights | door-buzzer-repair/…gowanus-two-white-pan-tilt-domes-with-warm-lights | product | §7 |
| dual-lens-overhead-doorway-counting-camera | door-buzzer-repair/…fordham-dual-lens-overhead-doorway-camera | product | §8 |
| white-bullet-camera-on-ball-mount | door-buzzer-repair/…morris-heights-white-bullet-camera-on-ball-mount | product | §9 |
| white-bullet-camera-with-twin-lights | door-buzzer-repair/…highbridge-white-lorex-bullet-camera-with-twin-lights | product | §10 |
| slim-recorder-and-flat-monitor | door-buzzer-repair/…east-tremont-slim-recorder-above-black-monitor | product | §10 |
| stainless-steel-pendant-speed-dome | door-buzzer-repair/…highbridge-stainless-steel-pendant-ptz-dome | product | §12 |
| twin-lamp-floodlight-above-box-camera | door-buzzer-repair/…city-island-white-vented-twin-lamp-floodlight-over-black-box-camera | product | §14 |
DAILY-LOG note: `images: 11 reused from images/door-buzzer-repair/ (no real condo photos yet)`. Several are small (132–275 px wide) product shots; real condo job photos should replace them when available.

### Links
- FLIP (plain text + `<!-- FLIP: /slug -->`): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-orange-county (§6 cameras), /condo-security-systems-ulster-county (§19).
- Linked directly: /condo-security-systems-hudson-valley (breadcrumb + §19), all 12 live condo siblings + /condo-security-systems-putnam-county and -dutchess-county (parallel batch) in §19; /co-op-security-systems-orange-county (§8, once); Orange service pages: intercom repair (/intercom-repair-orange), intercom installation (-ny), door buzzer repair (-new-york), door buzzer installation (-ny), access control, elevator access control, apartment-building cameras, alarm installation, fire alarm installation (-ny), network installation, camera maintenance, smart lock, CCTV, security camera installation (-ny), structured cabling; /intercom-pricing, /door-buzzer-repair-pricing, /warranty.
- Links back needed (main run): all 12 live condo pages (HV hub down-link; Rockland/HV have FLIP comments for this slug), /co-op-security-systems-orange-county (one contextual link), and per keyword rules one contextual link back from /intercom-installation-orange-county-ny and /apartment-building-security-camera-installation-orange-county.

### Mobile
390px render check NOT run: the headless Chrome launch was denied by the environment's permission classifier. Page uses the Rockland template markup and CSS unchanged (copied full head CSS from condo-security-systems-brooklyn.html; `:root{--a` count = 1); widest new element is the 3-column equipment table inside `overflow-x:auto` with the template's ≤600px fixed-layout rule.


## putnam-county

## Putnam County — local research for `condo-security-systems-putnam-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Child of /condo-security-systems-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx); phone (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (kept apart from co-op-security-systems-putnam-county, which is about a handful of small single-building co-ops with volunteer officers, and from condo-security-systems-rockland-county, which is about resale turnover and river flooding): Putnam's condo market is real (171 closings/12 mo vs 2 co-op closings in Q3) and concentrated in Carmel (20 of 31 listings), with a large age-restricted share (four 55+ condo communities, one of 312 homes; 55 condos for older residents at Cold Spring's Butterfield site). The page is built around older owners and caregiver/family access, amenity buildings detached from homes, rock/wetland cable routing, and lightning/outage protection.

Not thin: see M1–M5. Decision: build (not HOLD-THIN).

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched separately; co-op Putnam builder found no thread) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic chatbot/cost-guide claims; no AI quote invented. |
| 6 | Area landmarks | G3 (stations), Lake Gleneida/Lake Mahopac/Route 6N/Route 22 (general geography; Route 6N from N1) |
| 7 | Building stock | M1–M5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | N1 (News 12), N2 (Daily Voice), N3 (NYSEG), N4 (Patch) |
| 10 | Hyperlocal | Highlands Current (M5) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| M1 | Firecrawl scrape (PDF parser, query "Condos closed sales, median, DOM, inventory") | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_10_Putnam_County.pdf | OneKey MLS Putnam, Oct 2026, Condos: closed sales Oct 14; 12 mo thru 10-2026 = 171; median Oct $674,000, 12-mo $440,000; DOM Oct 57, 12-mo 39; inventory Oct 26. | §5 para 1 + facts; §10.5 #1 |
| M2 | reused, co-op Putnam PU1 | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_Q3_Putnam_County.pdf | Q3-2026: co-op closed sales 2; condos Q3 51. | §5 para 1 + facts; §10.5 #1 |
| M3 | Firecrawl scrape (query) | https://www.redfin.com/county/1984/NY/Putnam-County/condos | Nov 26 2026: 31 condos for sale, median list $417K; Carmel 20, Brewster 7, Cold Spring 2, Mahopac 1, Patterson 1; amenity notes: clubhouse + tennis (Brewster), community pools (Carmel, Brewster), lake views (Mahopac), soccer field + pool (Patterson), Brewster Metro-North (Carmel listing), HOA $370–$785. Addresses NOT used. | §5 para 2 + facts; §7 cards; §10.5 #1; §13 cards |
| M4 | `55 and over active adult community Putnam County NY condominium Carmel Patterson Brewster` · WebSearch → Firecrawl scrape | https://www.55places.com/new-york/communities/the-retreat-at-carmel ; https://www.thehirerealty.com/active-adult-55-plus/ | 55places: Carmel 55+ community, 312 homes, single-family/attached/condos, built 2008–2018, clubhouse, fitness center, outdoor pool. Hire Realty: four 55+ condo communities in Putnam (three in Carmel, one in Cold Spring PO/Philipstown, 2019). Community names NOT used on page. | §5 55+ subsection + facts; §7 card 1; §10.5 #1 |
| M5 | `Highlands Current Butterfield Cold Spring condominiums senior center post office` · Firecrawl search → scrape (directQuote) | https://highlandscurrent.org/2017/05/26/cold-spring-asks-court-dismiss-butterfield-suit/ | June 2015 site plan: office-retail building with county-run senior center; "two buildings with 55 market-rate condominiums for older residents"; Lahey Pavilion medical offices; later plan to move senior center and a U.S. Post Office branch to Lahey Pavilion. Development not named as a client; described as public news. | §5 (quote); §7 mixed-use card; §8 shared sites; Q&A shared lot |
| M6 | same Firecrawl search as M3 (excerpt) | https://www.katonahmgmt.com/community-association-management/cold-spring-ny | Firm offers community association management in Cold Spring "across the Hudson Valley since 1988". Firm not named on page. | §10.5 #7 |
| G1 | reused, co-op PU3 | https://www.census.gov/quickfacts/putnamcountynewyork | 38,713 housing units; owner-occupied 83.8%. | facts; §10.5 #1 |
| G2 | reused, co-op PU6 | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | >240 sq mi; six towns + three villages; ~3/4 NYC watershed; >9/10 Hudson Highlands bedrock; forest 66.9%. | §5 geography; Q&A rock |
| G3 | reused, co-op PU4 | https://www.putnamcountyny.gov/component/zoo/item/all-aboard-next-stop-putnam-county?Itemid=591 | Harlem Line: Brewster, Southeast, Patterson; Hudson Line: Cold Spring, Garrison. | §7 station card; §13 |
| G4 | reused, co-op PU15 | https://www.townofcarmelny.gov/DocumentCenter/View/456/Wetland-Permit-Application-PDF | Carmel regulates wetlands ≥1/8 acre + 100-ft buffer. | §5 geography; §8.5 |
| G5 | reused, co-op PU16 | https://highlandscurrent.org/2025/08/08/the-history-patrol/ | Cold Spring HDRB review of exterior changes in historic district since 1976. | §7 mixed-use |
| G6 | reused, co-op PU17 | https://ecode360.com/5066448 ; https://mail.pattersonny.org/PDFs/Codes/Chapter43-Alarms.pdf ; https://ecode360.com/9473178 ; https://ecode360.com/9063548 | Carmel alarm permit from Building Dept + sounder cutoff; Patterson >2 false alarms/12 mo fees; Putnam Valley permit before alarm calling FD; Southeast annual permit + licensed-agent inspection. Fee amounts NOT used. | §6 alarms; §8.5 |
| G7 | reused, silo HV / co-op PU20 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL applies to cities <325,000 and all towns and villages. | §5; §8.5; §10.5 #6 |
| G8 | reused, silo L1/L2 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | Common elements incl. "all apparatus and installations existing for common use"; reserves for "major and minor maintenance, repairs, additions, improvements, replacements". | facts; §14 |
| G9 | reused, Rockland RC-G9 | https://www.nysenate.gov/legislation/laws/EXC/378 | Pool enclosure gates self-closing/self-latching, locked when unattended. | facts; §6; §8.5 |
| G10 | reused, Rockland RC-G10 | https://www.nysenate.gov/legislation/laws/GBS/395-B | No viewing devices in restrooms/locker rooms etc. | §8.5; FAQ hidden cameras; §10.5 #6 |
| G11 | reused, co-op PU25 / RC-G11 | https://dos.ny.gov/security-or-fire-alarm-installer-license-law ; https://www.nysenate.gov/legislation/laws/GBS/69-M | State license for security/fire alarm installers. | facts; §8.5; §10.5 #6 |
| G12 | reused, Rockland RC-G14 | https://udigny.org/resources/nys-code-rule-753/ | Code Rule 753: notice 2–10 working days before excavation. | §6 cable; §8.5 |
| G13 | reused, co-op PU22 | https://intro.nyc/local-laws/2021-63 | TDPA = NYC LL 63/2021. | §10.5 #6 |
| W1 | reused, co-op PU13 | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | Putnam 2020: 75,093 lightning pulses, 35 thunder days. | §5 weather; facts; §10.5 #5 |
| N1 | reused, co-op PU8 | https://hudsonvalley.news12.com/police-make-3-arrests-in-carmelmail-thefts | Dec 2022: three arrests; car stopped near Route 6N in Mahopac; occupants appeared to be stealing mail. No names used. | §5 complaints |
| N2 | reused, co-op PU11 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 2020: 34,150 of 38,693 NYSEG Putnam customers out. | §5 weather; facts |
| N3 | reused, co-op PU12 | https://www.nyseg.com/w/brewster-nyseg-continues-restoration-effort-6-pm | Dec 25 2020: 27,375 Brewster-division customers out; gusts 71 mph. | §5 weather |
| N4 | `Putnam County NY package theft OR break-in condo complex …` · Firecrawl search (excerpt) | https://patch.com/new-york/southeast/over-river-through-woods-car-theft-suspects-hiding-space-we-go | Nov 2026: stolen-vehicle suspects searched for off Chestnut Ridge Road, Carmel; Westchester-Putnam Real Time Crime Center assisted. Background only (no condo link) — NOT used on page. | — |
| N5 | reused, co-op PU18 | Schumer press release (2015) on Northern Westchester/Putnam coverage maps | Carriers "wrongly claiming quality reception"; areas "often dead zones". | §10.5 #3 |
| Q1 | reused, Rockland RC-Q1 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500". | §10.5 #4 |
| P1 | site pages (internal), read Nov 26 2026 | /intercom-installation-putnam-county-ny (canonical Putnam intercom page) ; /access-control-installation-putnam-county ; /elevator-access-control-installation-putnam-county ; /door-buzzer-repair-putnam-county-new-york ; /intercom-pricing ; /door-buzzer-repair-pricing | $250 service call; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+; access single door/gate $1,900–$6,000, multi-door $5,000–$18,000; elevator L1 from $2,175/car, L2 from $3,625/car; buzzer parts: station $250–$525, relay/button $250–$475, transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400. Monitoring $30/$45 (site tiers). NOT used: /intercom-repair-putnam-county ranges ($218–$435 diagnostic, $195/hr callbacks, etc. — conflict with the $250 rule), /door-buzzer-installation-putnam-county-ny $300 booking, /alarm-installation-putnam-county $49/mo contract text. | hero; §14 tables; §10.5 #4; Q&A prewire |

### Putnam question register (this page) — add to the silo register
§9 Q&A (H3):
- The home-care agency sends different aides to several of our owners every week. How do we keep track of who can get in?
- An owner passed away and the estate's executor needs to get into the unit to prepare it for sale. What should happen to the unit's fobs and app accounts?
- One of our owners has memory loss and has walked out of the building at night. Can a door let the family know without locking anyone in?
- When an owner falls inside a locked building, can a son or daughter who lives out of state let the ambulance crew through the front door?
- Can the fitness room have a button that reaches someone if an owner gets hurt exercising alone?
- Can the clubhouse defibrillator cabinet tell the board when it has been opened?
- Our cameras would look over a parking lot we share with a neighboring medical office. Can the association record land it doesn't own?
- Our buildings sit on solid rock. How does cable get from one building to the next?
- Several owners objected at the annual meeting when the board proposed clubhouse cameras. How do other boards settle that?
- One owner won't let the crew into his unit for the intercom upgrade. Can the project go ahead without that unit?
- Our clubhouse party room has a posted occupancy limit. Can the access system tell the board how many people are inside during an event?
- The builder prewired every unit for an alarm, but nobody ever activated it. Can an owner use that wiring now?

§17 FAQ:
- What format should our owner list be in when you load it into a new system?
- Our owners' alarms are monitored by another company. Do they have to switch for you to work on the common areas?
- Our pool house is unheated from fall to spring. Can intercom or camera equipment live there through the winter?
- Can residents get a text when a package lands in the package room?
- How long does your crew need inside each unit when in-unit stations are replaced?
- Will you put hidden cameras in the clubhouse to catch whoever keeps damaging it?
- Is your proposal priced per door, per unit or as one total?
- Can the keypad code for vendors change on a schedule without anyone reprogramming it by hand?
- If a reader fails, can owners still open the door with a key?
- Our pool fence posts shift every winter. Will a gate reader stay lined up?
- Once the board votes yes, how soon does the work begin?
- Can visitors scan a code at the entrance to call an owner instead of scrolling a directory?

Checked by meaning against every question on the 12 live condo pages and co-op-security-systems-putnam-county (parsed with tools/check_page.parse). Also checked against parallel orange-county and dutchess-county pages once on disk (dropped a footage-for-rule-enforcement question that overlapped Orange). Avoided intents already taken: caregivers at 55+ entrance (HV — this page's question is agency staff rotation), winter-away fobs (HV/Suffolk), lightning surge (Suffolk/co-op Putnam), outage lock behavior (Queens/co-op Putnam), wheelchair height (Rockland/Westchester/co-op), cellular gate call box (HV), police clip requests (Queens), owner vote (NYC/Brooklyn), sponsor login (Manhattan), trenching near wetlands (co-op Putnam), Carmel alarm permit (co-op Putnam), fire alarm "do you do it" (NYC — covered in body only).

### Images (11) — permanent image rule; external manufacturer downloads blocked by the egress proxy (403), so library product photos used
Pool: dHash screen of 4,665 files in candidate folders against all 308 files in images/condo-security-systems/, images/co-op-security-systems/, images/co-op-board-intercom-upgrade/ (distance ≤14 rejected); network-installation, low-voltage, commercial-security, elevator, smart-lock and AI/branded-crew images excluded; survivors compared by eye with their nearest used images. None shares a sha256 with any condo/co-op image at build time. All are manufacturer product photos (visible marks: blink, eufy, univ, LOREX, Ubiquiti "U"); no faces, house numbers, phone numbers or "AESS".
| Page file (images/condo-security-systems/condo-security-systems-putnam-county-…) | ← Source | Where |
|---|---|---|
| white-video-doorbell-for-townhouse-unit-doors.webp | images/access-control-installation/access-control-installation-bensonhurst-white-and-black-video-doorbell-product-photo.webp | hero (eager), og/twitter |
| black-turret-camera-with-blue-lens-ring.webp | images/ubiquiti-unifi-g6-pro-turret-camera-black.jpg | §5 |
| compact-ptz-dome-for-entrance-drives.webp | images/uniview-ptz-positioning-dome-camera-white.jpg | §6 |
| slim-black-battery-doorbell-for-unit-entries.webp | images/access-control-installation/access-control-installation-brighton-beach-brooklyn-blink-black-video-doorbell.webp | §7 |
| low-profile-black-dome-camera-housing.webp | images/ubiquiti-unifi-g5-dome-camera-black-rear.jpg | §8 |
| black-bullet-camera-with-deterrence-lights.webp | images/lorex-mini-ptz-active-deterrence-camera-installation-nyc.jpg | §9 |
| small-white-indoor-cube-camera.webp | images/lorex-indoor-ptz-dome-camera-installation-nyc.jpg | §10 |
| white-pan-tilt-camera-on-pendant-mount.webp | images/ubiquiti-unifi-g6-ptz-4k-camera-white.jpg | §10.5 |
| compact-black-network-video-recorder.webp | images/nvr-uniview-nvr501.png | §12 |
| black-pan-tilt-camera-on-wall-arm.webp | images/ubiquiti-unifi-g6-ptz-4k-camera-black.jpg | §14 |
| battery-doorbell-with-blue-ring-button.webp | images/access-control-installation/access-control-installation-clason-point-bronx-black-battery-doorbell-with-blue-ring.webp | §15 |
Note: co-op-security-systems-putnam-county uses the white G6 Pro turret and G6 Pro bullet; this page's turret is the black colour variant (different photo). DAILY-LOG note: `images: 11 manufacturer product photos reused from the top-level library + images/access-control-installation/ (no real condo photos yet; external product-photo downloads blocked)`.

### Links left for the main run (FLIP comments in the page)
`/condo-intercom-replacement` (§6 intercom), `/condo-security-camera-installation-putnam-county` (§6 cameras), `/condo-security-systems-ulster-county` (siblings). Orange and Dutchess condo pages linked directly (not on disk at finish). Back-links needed from all 12 live condo pages; one contextual link back from /intercom-installation-putnam-county-ny (no Putnam apartment-building camera page exists).


## dutchess-county

## Dutchess County — local research for `condo-security-systems-dutchess-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Child of /condo-security-systems-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx); phone (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Starting price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

HOLD-THIN test: passed. Dutchess condos far outnumber co-ops (307 vs 42 sales in 12 months) and are a distinct stock: 41 named condo/townhouse complexes concentrated in Fishkill (13), Beacon (9), Poughkeepsie area (7), Wappingers Falls (5), built 1965–2019+, mostly townhouse/garden communities with clubhouses, pools and courts, three gated communities in current listings (one 55+), a few station-area/downtown lobby buildings, and slow new supply (116-unit riverfront proposal, 37-townhouse Beacon project).

Thesis (kept apart from co-op-security-systems-dutchess-county, which leads with the small co-op market, city walk-ups, Beacon historic overlay for co-op entrances, winter door failures and Bronx travel; and from the Rockland/Westchester/Nassau condo pages): Dutchess condos are townhouse communities where the clubhouse, pool gate, management office, maintenance garage and utility buildings are the shared "front doors"; six decades of construction in one county (mixed eras within phased associations); municipal alarm rules that differ town by town (Beacon permit + callback, Village of Fishkill revocation at 10 avoidable alarms, East Fishkill separate registration per alarm site + first two false alarms free); Town of Poughkeepsie 2026 electrical permit law; long Central Hudson/NYSEG outages; remote management for rural associations.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY — not searched separately this run (co-op Dutchess builder found no r/Poughkeepsie / r/hudsonvalley thread on the topic) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 corrects generic claims typical of chatbot/cost-guide answers (Angi/HomeAdvisor/Fixr named generically; HomeAdvisor range reused from silo). No AI quote invented. |
| 6 | Area landmarks | DC-L1 (general geography, no client properties) |
| 7 | Building stock | DC-M1, DC-M2, DC-M3, DC-N1, DC-N2 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Westfair Communications (DC-N1), The Highlands Current (DC-N2), Dutchess County press release (DC-W1) |
| 10 | Hyperlocal | The Highlands Current (DC-N2); municipal codes (DC-A1–A4) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| DC-M1 | reused, co-op Dutchess D1 (OneKey MLS Q3 2026 PDF; the Oct 2026 PDF `2026_10_Dutchess_County.pdf` returned 403 to Firecrawl this run) | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_Q3_Dutchess_County.pdf | Condos 12 mo thru 9-2026: 307 (295 prior, +4.1%), median $355,000 (from $318,000). Co-ops 42, median $114,000. | §5 para 2; facts list; hero stamp |
| DC-M2 | `Dutchess County condos townhouse HOA communities Fishkill Wappingers Falls Poughkeepsie Beacon condominium` · Firecrawl search → Firecrawl scrape (freeform) | https://www.realestatehudsonvalleyny.com/dutchess-towns/dutchess-condos/ | Directory of Dutchess condo/townhouse complexes by town: Fishkill 13, Beacon 9, Poughkeepsie 7, Wappingers Falls 5, Beekman 2, Pawling 2, Hyde Park 2, Rhinebeck 1 (41 total); build years 1965 to 2019+; two Fishkill complexes flagged 55+, a Wappinger "Regency" 2018, Rhinebeck community 2013+. Complex names NOT used on page. | §5 "Where Dutchess condos actually sit"; §7 cards; §10.5 #1; §13 cards |
| DC-M3 | Firecrawl scrape (freeform, no addresses) | https://www.redfin.com/county/1958/NY/Dutchess-County/condos | Nov 26 2026: 71 condos for sale, median list $279K; listings in Fishkill 12524, Wappingers Falls 12590, Poughkeepsie 12601/12603, LaGrangeville 12540, Pawling 12564, Beacon 12508, Hyde Park 12538; notes: gated + fitness + clubhouse 55+ (Fishkill), gated (Poughkeepsie 12601), gated + clubhouse + pool (Poughkeepsie 12603), community pools, tennis courts, "scenic natural pond", HOA $296–$586, built 1968/1971/1985/1988, "near train" tags, "close to hospitals". Search-result excerpt also described a Fishkill community as a gated 55+ active-adult condominium built by a national homebuilder (builder not named on page). | §5 listings para; facts list; §7 gated 55+ card/subsection; §13 cards |
| DC-N1 | `Dutchess County townhouse condominium development approved planning board units Fishkill OR Wappinger OR Poughkeepsie 2025 2026` · Firecrawl search (news) → Firecrawl scrape (directQuote) | https://westfaironline.com/latest-news/fishkill-landing-condo-project-being-planned/ | Westfair Communications, Peter Katz, Dec 1 2023: proposed Fishkill Landing on the Hudson in Fishkill — 116 condo units in four buildings, 2.5 and 3 stories, 7.5 acres for the complex, 10-acre town park, 100 underwater acres; park with restrooms, public parking, Riverfront Esplanade. | §5 "What is being built now"; §7 riverfront card/subsection |
| DC-N2 | same search (news excerpt) | https://highlandscurrent.org/2025/05/30/booming-beacon-7/ | The Highlands Current, May 30 2025: "Beacon Views — 37 townhouses"; Planning Board granted two 90-day extensions, "at least the sixth and seventh extensions the project has received since 2022." Project name NOT used on page. | §5 "What is being built now" |
| DC-W1 | reused, co-op Dutchess D7 | https://www.dutchessny.gov/Departments/County-Executive/Severe-Summer-Storm-Wreaks-Havoc-Across-Dutchess-County.htm | July 4 2026 storm: Central Hudson 33,000+ outages, NYSEG 7,400+; worst in City/Town of Poughkeepsie, East Fishkill, LaGrange, Beekman, Union Vale, Village/Town of Pawling. | §5 storms; §10 batteries; §10.5 #7 |
| DC-W2 | `Central Hudson outage Dutchess County winter storm ice 2025 OR 2026 customers without power` · Firecrawl search (excerpt) | https://outagemap.cenhud.com/ | "Total Customers Served 315,545" (outage map, Nov 26 2026). | §5 storms |
| DC-A1 | `Town of Fishkill code alarm systems chapter permit false alarms ecode360` · Firecrawl search (excerpt) | https://ecode360.com/8298811 | Village of Fishkill Code Ch. 37: "An alarm user permit shall be revoked whenever 10 or more avoidable alarms are recorded for a system in any one permit year." (Town of Fishkill Ch. 42 exists, https://ecode360.com/10584873 — definitions only seen; not cited for any rule.) | §5 towns para; §8.5; §10.5 #6 |
| DC-A2 | same search (excerpts) | https://ecode360.com/7070191 ; https://ecode360.com/7070218 | Town of East Fishkill: "A separate alarm registration is required for each alarm site." Art. IV: "No fee shall be assessed for the first two false alarms at the same premises responded to by the Fire or Police Department during each …" (excerpt truncated; page words it without the period). | §5 towns para; §8.5; §9 Q&A East Fishkill registration; §10.5 #6 |
| DC-A3 | reused, co-op Dutchess D4 | https://ecode360.com/7062505 | City of Beacon Ch. 77: alarm user permit from Police Department; residential notifications include attempted callback by central station before police. | §5 towns; §8.5; §10.5 #6 |
| DC-A4 | reused, co-op Dutchess D10 | https://ecode360.com/6320489 | Town of Poughkeepsie Ch. 91 Electrical Inspections (L.L. 1-2026, adopted 2-18-2026): permit required to install/alter wiring for light, heat or power. | §5 towns; §8.5; §10.5 #5 |
| DC-A5 | reused, co-op Dutchess D5 | https://ecode360.com/7063677 | Beacon Ch. 134: "alteration excludes … any minor, accessory, utility or security-related changes that do not substantially detract from the historic property". | §7 station-area subsection |
| DC-G1 | reused, co-op Dutchess D3 | https://www.citypopulation.de/en/usa/newyork/admin/36027__dutchess/ | 2020 Census: county 297,018; Town of Poughkeepsie 45,574; City of Poughkeepsie 31,596; Town of Wappinger 28,204; Town of Fishkill 23,605; City of Beacon 14,380. | facts list |
| DC-G2 | reused, co-op Dutchess D6 | https://en.wikipedia.org/wiki/Poughkeepsie_station | Poughkeepsie = northern terminus of Metro-North Hudson Line. | facts list |
| DC-G3 | reused, silo L1/L2 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; https://law.justia.com/codes/new-york/rpp/article-9-b/339-v/ | Common elements text; reserves phrase. | facts list; §8.5; §14 funding |
| DC-G4 | reused, silo HV / co-op D12 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3: cities < 325,000 and all towns and villages. | §5 towns; §8.5; §10.5 #3 |
| DC-G5 | reused, Nassau NC-G6 | https://www.nysenate.gov/legislation/laws/EXC/378 | Pool enclosure gates self-closing, self-latching, locked when not in use or supervised. | facts list; §6 amenities; §8.5 |
| DC-G6 | reused, co-op D13 | https://www.nysenate.gov/legislation/laws/GBS/69-M | State licensing of security/fire alarm installers. | facts list; §8.5; §10.5 #5 |
| DC-G7 | reused, Rockland RC-G14 | https://udigny.org/resources/nys-code-rule-753/ | Code Rule 753: notice two to ten working days before excavation. | §6 cabling; §8.5 |
| DC-G8 | reused, Rockland RC-G12 | https://cooperatornews.com/article/qa-camera-placement | Audio recording may implicate Penal Law eavesdropping provisions. | §9 Q&A audio |
| DC-G9 | reused, silo L5 | https://intro.nyc/local-laws/2021-63 | TDPA is NYC law only. | §8.5; §10.5 #3 |
| DC-Q1 | reused, silo / RC-Q1 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500". | §10.5 #2 |
| DC-P1 | site pages (internal), read Nov 26 2026 | /intercom-installation-dutchess-county-ny (canonical; /intercom-installation-dutchess-county 301s to it) ; /access-control-installation-dutchess-county ; /elevator-access-control-installation-dutchess-county ; /door-buzzer-repair-dutchess-county-new-york ; /intercom-pricing ; /door-buzzer-repair-pricing | $250 service call; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP smartphone $2,500–$8,000+; access single door/gate $1,900–$6,000; multi-door $5,000–$18,000 (pricing table); elevator L1 from $2,295/car, L2 from $3,825/car; buzzer parts station $250–$525, relay/button $250–$475, transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400; monitoring $30/$45 (site tiers). NOT used: intercom page "audio $500–$800", access page "$1,500–$2,500 lobby fob + 25% surcharge" and "$195/hr" callbacks, buzzer page "same day" wording, /intercom-repair-dutchess-county ranges (conflicting; flagged by co-op builder). | hero; §6; §14 tables; §15 |
| DC-L1 | landmark geography (no client properties) | — | Route 9 / I-84 Fishkill interchange area; Beacon station + Main Street; Walkway Over the Hudson (Poughkeepsie); Wappingers Falls / Route 9D; Hyde Park Roosevelt sites; Rhinebeck village. | §13 cards |

### Dutchess question register (this page) — add to the silo register
§9 Q&A (H3): The clubhouse and several owners all have alarms in East Fishkill. Can they share one registration? · Can the board cap how many fobs and app users each unit gets? · Should cameras watch the association's pond and walking path? · After a divorce, one former spouse still has fobs for a unit the other now owns alone. Who can have them turned off? · An owner's car was keyed twice in the same space. Can we point a camera at that spot? · Owners want to check the pool camera from their phones to see if it is crowded. Is that a good idea? · Can our clubhouse cameras record sound as well as video? · Many owners rent to tenants on twelve-month leases. Can a tenant's fob turn itself off when the lease ends? · Can owners use their phones instead of fobs at the pool and clubhouse? · Our community runs its own water treatment building. Should it be on the same access system as the clubhouse? · What happens to our camera recordings if someone steals the recorder from the clubhouse? · Who keeps the cameras' and entry panels' software up to date after installation?

§17 FAQ: Our pool gate lock fails but the rest of the access system works. Can you replace just that lock? · Can the board remove items from your proposal and keep the other prices the same? · Can a reader go on the sliding glass door between the clubhouse and the pool deck? · Will owners lose power or water while you work? · Will our existing door closers and handles work with new electric locks? · Should the association post signs saying cameras are recording? · Our clubhouse exit door has a panic bar. Can it take a reader on the outside? · Do owners need Wi-Fi in their unit for the intercom or access app? · Can the management company view our cameras from its office in another town? · Can the system text board members when the clubhouse alarm goes off? · Do readers and entry stations come in finishes that match our trim? · Can the local police watch our cameras live?

Intent check (by meaning) against every question on the 12 live condo pages, the parallel orange-county and putnam-county pages (parsed from their HTML at build time) and co-op-security-systems-dutchess-county / -hudson-valley. Dropped/replaced during the build because they matched a sibling: speeding on private roads (Orange), mailing-address/town-line jurisdiction (Orange "complex sits across a town line"), chain-link/picket pool gate mounting (Orange), scheduled code changes (Putnam vendor keypad code), lost phone self-service (Orange lost fob), clubhouse alarm permit/readiness (co-op Dutchess management-office permit). Checker reports no exact masked duplicates.

### Similarity
Masked-geo paragraph similarity (difflib on word sequences; protected warranty sentence, proof strip, SMS consent and forms excluded): max 0.63 (condo-security-systems-orange-county), all other condo pages ≤ 0.62; co-op-security-systems-dutchess-county 0.44. Process/pricing/package paragraphs that first came out close to the Rockland/Orange/Putnam wording (0.7–0.96) were rewritten.

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied byte-for-byte into images/condo-security-systems/ with `-dutchess-county-` names. sha256 differs from every file in images/condo-security-systems/ (incl. parallel orange/putnam files present at finish), images/co-op-security-systems/, images/co-op-board-intercom-upgrade/. Five first picks collided with files the parallel Orange/Putnam builders took (same sha256 or same product photo: stainless pendant PTZ, slim recorder + monitor, Speco-style doorbell with card icon, white Lorex bullet, Lorex indoor cube) and were swapped. Closest remaining: the doorbell is the same Alarm.com model family as the Nassau bronze doorbell (different finish/photo); the twin-light turret resembles the Staten Island turret (different model). Rejected: AI-looking job photos (alarm-installation Fulton Ferry boxes, Fort Hamilton conduit, cat6/structured-cabling technician shots with branded shirts), corridor-to-grey-door scenes (same corridor as co-op Dutchess image), camera-arm-below-cornice scenes (co-op Dutchess), Juice Bar signage, buzzer-repair/*.jpg, elevator-access-control, network-installation, low-voltage, commercial-security, smart-lock sets. Manufacturer photos via Firecrawl (2N) were blocked by the egress proxy. No faces, house numbers, phone numbers or "AESS"; maker logos visible on product photos (Alarm.com, Hikvision, Luminys, Digital Watchdog).
| Page file (…dutchess-county-) | ← Source | Kind | Where |
|---|---|---|---|
| dome-camera-in-office-ceiling-corner-beside-flag (hero/og) | images/door-buzzer-repair/door-buzzer-repair-brownsville-white-dome-camera-in-wall-corner-beside-flag.webp | job | hero |
| mini-dome-camera-and-cable-over-wood-slat-wall | images/door-buzzer-repair/door-buzzer-repair-bushwick-mini-dome-and-cable-runs-over-wood-slat-wall.webp | job | §5 |
| black-and-white-video-doorbell-with-lit-bell-button | images/door-buzzer-repair/door-buzzer-repair-fort-greene-black-and-white-video-doorbell-with-lit-bell-button.webp | product | §6 |
| white-turret-camera-with-twin-lights-for-parking-courts | images/door-buzzer-repair/door-buzzer-repair-gowanus-white-turret-camera-with-twin-lights-product-photo.webp | product | §7 |
| wifi-dome-camera-with-two-antennas | images/door-buzzer-repair/door-buzzer-repair-fordham-wifi-dome-camera-with-two-antennas.webp | product | §8 |
| flat-dark-grey-network-video-recorder | images/door-buzzer-repair/door-buzzer-repair-madison-flat-dark-grey-recorder-product-photo.webp | product | §9 |
| white-turret-camera-with-blue-light-ring | images/door-buzzer-repair/door-buzzer-repair-mott-haven-white-turret-camera-with-blue-light-ring-product-photo.webp | product | §10 |
| white-indoor-cube-camera-with-black-base | images/door-buzzer-repair/door-buzzer-repair-claremont-white-indoor-cube-camera-product-photo.webp | product | §10.5 |
| black-network-recorder-with-orange-badge | images/door-buzzer-repair/door-buzzer-repair-mount-eden-black-network-recorder-with-orange-badge-product-photo.webp | product | §12 |
| pan-tilt-camera-with-two-antennas-for-entrance-drives | images/door-buzzer-repair/door-buzzer-repair-gowanus-pan-tilt-camera-with-two-antennas-and-stacked-lenses-product-photo.webp | product | §13 |
| pan-tilt-camera-under-three-floodlight-panels | images/door-buzzer-repair/door-buzzer-repair-brownsville-black-pan-tilt-camera-under-three-led-panels-product-photo.webp | product | §14 |

DAILY-LOG note: `images: 11 reused from images/door-buzzer-repair/ (no real condo photos yet)`.

### Links
- Linked live: up /condo-security-systems-hudson-valley (breadcrumb, schema, §19); all 12 live condo pages + parallel /condo-security-systems-orange-county and /condo-security-systems-putnam-county (§19, once each); /co-op-security-systems-dutchess-county (§6, once); /intercom-installation-dutchess-county-ny, /intercom-repair-dutchess-county, /door-buzzer-repair-dutchess-county-new-york, /door-buzzer-installation-dutchess-county-ny, /access-control-installation-dutchess-county, /smart-lock-installation-dutchess-county, /elevator-access-control-installation-dutchess-county, /security-camera-installation-dutchess-county-ny, /parking-lot-camera-installation-dutchess-county, /cctv-installation-dutchess-county, /alarm-installation-dutchess-county, /fire-alarm-installation-dutchess-county-ny, /doorbell-camera-installation-dutchess-county, /structured-cabling-installation-dutchess-county, /network-installation-dutchess-county, /security-camera-maintenance-dutchess-county, /akuvox-vs-butterflymx, /intercom-pricing, /door-buzzer-repair-pricing, /warranty.
- No /apartment-building-security-camera-installation-dutchess-county page exists, so that keyword-rule link was skipped.
- FLIP comments (plain text): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-dutchess-county (§6 cameras), /condo-security-systems-ulster-county (§19).
- Link backs needed (main run): all 12 live condo pages (checker lists them; the HV hub needs its down-link/FLIP flipped); parallel Orange/Putnam pages; /co-op-security-systems-dutchess-county (one contextual link); per keyword rules one contextual link back from /intercom-installation-dutchess-county-ny.

### Mobile
390px check: headless Chrome (old mode) rendering the page in a 390px iframe (file://, so /js/mega-nav.js not loaded): scrollWidth = clientWidth (375 with scrollbar), no element extends past the viewport.


## ulster-county

## Ulster County — local research for `condo-security-systems-ulster-county` (part file, Nov 26 2026; merge into research/condo-security-systems.md)

Built by a batch subagent. Child of /condo-security-systems-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx); phone (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav. Starting price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

HOLD-THIN test: PASSED (build). Unlike co-ops (1 sale/12 mo, county's first co-op unbuilt → HOLD-THIN), Ulster has a real if small condo stock: 24 condo closings/12 mo, inventory 12 (OneKey Q3 2026); Redfin/Compass listings in New Paltz (1970 and 1986 garden complexes, a 46-unit net-zero mixed-use building converting to condos since March 2025), Highland (2018 elevator building; townhouse community with clubhouse/pool/tennis/dog park), Kingston (townhouse HOA communities, one listed as 1981), Port Ewen (pool community), Woodstock (small condo). Distinct local material not on any sibling: Ulster County False Alarm Reduction Act (county Sheriff permit, exempt-municipality list), Ulster County master electrician licensing (Ch. 185), Cooper St townhomes switching from condo to fee-simple, conversion with remaining regulated tenants, all-electric/net-zero buildings, Sept 2026 nor'easter (Woodstock/Shawangunk/Plattekill/Hurley). Risk noted for Anwar: search demand for "condo security systems Ulster County" is likely very low given ~24 sales/yr.

Thesis: small, scattered, mostly staff-less associations of six types (village garden complexes, newer elevator buildings, conversions with mixed occupancy, townhouse associations, riverfront pool communities, mountain-town/second-home condos); turnover/credential control for renters (SUNY New Paltz); county-vs-local alarm permits; outages and batteries; solar does not carry security in a blackout.

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY — not searched this run |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env); §10.5 corrects generic chatbot claims; HomeAdvisor range reused from silo |
| 6 | Area landmarks | UL-L1 (general geography, no client properties) |
| 7 | Building stock | UL-M1–UL-M5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Hudson Valley One (UL-N1, UL-N2), Central Hudson (UL-W1) |
| 10 | Hyperlocal | Ulster Sheriff / county law (UL-A1, UL-A2), Saugerties code (UL-A3), county electrical law (UL-A4) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Rows
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| UL-M1 | reused, co-op Ulster U3 (OneKey MLS Q3 2026 PDF) | https://irp.cdn-website.com/a5e60d20/files/uploaded/2026_Q3_Ulster_County.pdf | Condos 12 mo thru 9-2026: 24 (25 prior), median $285,000 → $317,500, inventory 6 → 12; co-ops 1; single-family 929, median $469,200 | §5 paras 2–3; facts; §10.5 #1; hero quick answer |
| UL-M2 | Firecrawl scrape (json) | https://www.redfin.com/county/2000/NY/Ulster-County/condos | Nov 26 2026: page lists 19 incl. out-of-county (Wappingers Falls, Newburgh, Fishkill, Hyde Park); Ulster ones New Paltz/Highland/Port Ewen; New Paltz 1970 HOA $242; New Paltz 1986 "steady rental income"; Highland 2018 HOA $448 and $686; Highland clubhouse/tennis/pool/dog park; New Paltz rooftop terrace/fitness/elevator HOA $584; Port Ewen pool | §5 "Where Ulster condos sit"; facts; §7 |
| UL-M3 | `Ulster County NY condo complexes Kingston New Paltz Saugerties condominium townhouse HOA` · WebSearch → Firecrawl scrape | https://gristmillrealestate.com/blog/considering-a-condo-or-townhome-in-new-paltz | March 2026 New Paltz listings: complexes 1970s–1990s plus new infill; HOA low $200s–mid $400s, some incl. heat/hot water; draws: village, Wallkill Valley Rail Trail, SUNY New Paltz; Village prohibits most non-owner-occupied STRs in residential zones (NOT stated as law on page) | §5 para; hero stamp |
| UL-M4 | Firecrawl scrape (compass Ulster condos) | https://www.compass.com/homes-for-sale/ulster-county-ny/condos/ | Listing addresses in New Paltz (N Chestnut, Huguenot St), Highland (Vineyard Ave, Gregory Ct), Kingston (Twin Ponds Dr, Broadway), Port Ewen (Riverview), Woodstock (Pond Park Rd). Addresses/names NOT used on page | building-stock confirmation only |
| UL-M5 | `"Twin Ponds" condominium Kingston NY ...` · WebSearch → Firecrawl scrape (json) | https://thylan.com/?p=387 | Kingston townhouse HOA community listed by its owner/manager as built 1981 (weak extraction; flagged) | §7 townhouse para ("one dating to 1981") |
| UL-N1 | `87 North Chestnut New Paltz condominium` · WebSearch → Firecrawl scrape (json) | https://hudsonvalleyone.com/2025/10/28/new-paltzs-latest-developments-in-housing-tourism-and-infrastructure/ | Zac Shaw, Oct 28 2025: 46-unit net-zero mixed-use New Paltz building; "In March 2025, owners began converting the apartments into condominiums for sale"; regulated tenants could remain as renters if they qualify and pay. Building name NOT used | §5 conversion; §7 conversions |
| UL-N2 | Firecrawl scrape (json) | https://hudsonvalleyone.com/2025/10/14/david-shepler-presents-subdivision-changes-for-net-zero-townhomes-in-new-paltz/ | Crispin Kott, Oct 14 2025: six net-zero townhomes on Cooper Street, own solar + geothermal; initially a condominium, changing to individual lots "to avoid the complications of a condominium association" (extraction summary, not verbatim; page paraphrases it without quote marks) | §5; §7 townhouse; §10.5 #7; Q&A shared camera |
| UL-H1 | reused, co-op Ulster U1/U2 | https://www.ulstercountyny.gov/Government/News/Newsroom/2025-07-03-Affordable-Housing-Initiative-at-Elizabeth-Manor-Property-in-Kingston | 15-unit Kingston limited-equity co-op, "first cooperative ownership structure in the County" | §5 para 2 |
| UL-A1 | `ecode360 alarm permit ... Ulster ...` · Firecrawl search → Firecrawl scrape | https://www.ulstersheriffny.gov/falsealarm | LL 13 of 2015: permit for every structure with alarm, owner or tenant who controls system applies; one-time $10 registration per structure; penalties $0 1st/2nd, $50 3rd, $200 4th+ per calendar year; unpermitted: warning + 14 days, then $100/$200; unpaid → tax bill; exempt: City of Kingston; Towns of Esopus, Marlboro, New Paltz, Saugerties, Shandaken, Ulster, Wawarsing, Woodstock; Villages of Ellenville, New Paltz, Saugerties | §5 alarm law; §6 alarms; §8 compliance; §9 Q&A 1–2; §10.5 #4; §13 Kingston/Esopus |
| UL-A2 | Firecrawl scrape (PDF json) | https://legislature.ulstercountyny.gov/wp-content/uploads/2025/10/Local-Law-No.-13-of-2015-False-Alarm.pdf | Law text: monitoring company must ensure current permit before commencing service; penalty on owner of real property; law PDF lists $50 permit fee (Sheriff page lists $10 one-time — page uses Sheriff figure) | §9 Q&A 2 |
| UL-A3 | same search (excerpt) | https://ecode360.com/13643763 | Town of Saugerties Ch. 62: "No person shall operate, maintain, monitor or install an alarm system without first obtaining a permit" | §5; §8 compliance |
| UL-A4 | `Ulster County Electrical Licensing Board ...` · Firecrawl search (excerpts) | https://ecode360.com/35131702 ; https://www.wawarsingny.gov/DocumentCenter/View/274/Electrical-Licensing-Board-PDF | Ch. 185 Electrical Standards (LL 3 of 2019, amended 8-2021): Master Electrician license from county Board; Wawarsing notice: master electrician licenses required to obtain building permits for electrical work | §5 electricians; §8; §10.5 #6 |
| UL-W1 | reused, silo H4 + Firecrawl search | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 2026: >19,000 homes and businesses out; hardest hit Woodstock, Shawangunk, Plattekill, Hurley | §5 weather; §7 mountain towns; §10.5 #5; §13 Woodstock |
| UL-G1 | Firecrawl scrape (json) | https://www.citypopulation.de/en/usa/newyork/admin/36111__ulster/ | County 181,835; New Paltz 14,399; Lloyd 11,143; Saugerties 19,038 (page rounds: ~182,000 / 14,400 / 11,100 / 19,000) | facts list |
| UL-G2 | reused, silo L1/L2 | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ ; .../339-v/ | common elements phrase; reserves phrase | facts; §8; §14 |
| UL-G3 | reused, silo | https://www.nysenate.gov/legislation/laws/MRE/3 ; /EXC/378 ; /GBS/69-M ; /GBS/395-B | MRL scope; pool gates; installer licensing; no viewing devices in restrooms/changing rooms | facts; §6; §7; §8; §10.5 |
| UL-G4 | reused, silo | https://udigny.org/resources/nys-code-rule-753/ | notice 2–10 working days before excavation | §8 |
| UL-G5 | reused, silo L5 | https://intro.nyc/local-laws/2021-63 | TDPA NYC only | §10.5 #3 |
| UL-Q1 | reused, silo | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500" | §10.5 #2 |
| UL-P1 | site pages (internal), read Nov 26 2026 | /intercom-installation-ulster-county-ny ; /access-control-installation-ulster-county ; /elevator-access-control-installation-ulster-county ; /door-buzzer-repair-ulster-county-new-york | intercom 4–8 units $1,200–$3,500, multi-unit $1,200–$5,000, IP $2,500–$8,000+; access single $2,100–$6,500, multi-door $5,500–$20,000; elevator L1 from $2,295/car, L2 from $3,825/car; buzzer repair station $250–$525, relay $250–$475, transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400; monitoring $30/$45. NOT used: intercom "audio $500–$800", access page "Brooklyn base + 35%" and "$195/hr" callbacks and (347) phone, buzzer repair "same day" wording, door-buzzer-installation $300 service call (conflicts with $250) | hero; §6; §14 tables |
| UL-L1 | landmark geography (no client properties) | — | New Paltz Main St/Huguenot St; Walkway Over the Hudson (Highland end); Wallkill Valley Rail Trail; Kingston Rondout/Uptown; Woodstock/Catskill towns; Port Ewen/Esopus riverfront | §13 |

### Ulster question register (this page) — add to the silo register
§9 Q&A (H3): Our complex is in a town that has no alarm law of its own. Whose permit rules apply to the clubhouse alarm? · When an owner's alarm causes a false dispatch, does the penalty fall on that owner or on the association? · Can the access log show the board whether an owner is renting a unit by the night? · Our building is all-electric with rooftop solar. Will the solar keep the entry system running in a blackout? · Should our clubhouse alarm report over the internet, a cellular radio or both? · Our building was built to passive-house standards. Can new cable go in without breaking the air seal? · Our six townhouses are separate lots with no condo association. Can we still share an entry camera and pay for it together? · When the fire alarm goes off, should our front doors unlock by themselves? · Can cameras watch the heat pumps and solar equipment on our roof? · Our lobby door is an aluminum-and-glass storefront door. What kind of electric lock suits it? · Can the indoor intercom monitor move when an owner renovates the kitchen? · Does SUNY New Paltz's calendar matter when we schedule work in a building full of student renters?

§17 FAQ: Can you mount a key box for the fire department at our entrance? · Is damage from a lightning strike or power surge covered by the warranty? · Will new cameras work over the old coax cable from our first camera system? · One owner's indoor handset broke and the building's intercom model is discontinued. Can it still be replaced? · Can the entry system work with owners' smart speakers or home hubs? · Can the fitness room or storage room use a battery-powered lock instead of a wired one? · Can we see a sample proposal before booking the free assessment? · After storm damage, can you document the security equipment for the association's insurance claim? · Will our access system and cameras keep working if the association changes internet providers? · Our building is still framed and open. Can you rough in security cable before the drywall goes up? · Can the building's handyman add fobs without being able to change the system settings? · Can the association order the same video doorbell for every townhouse?

Intent check (by meaning) against every question on the 15 live condo pages and co-op HV/Dutchess (parsed at build time). Avoided overlaps: owner alarm police permit (Nassau), false-alarm cost (Westchester), shared registration (Dutchess), lease-end fob expiry (Dutchess), overseas/weekender owners (Queens/HV), cloud-free cameras (Orange), handset billing (Brooklyn), master credentials (Manhattan), renovation contractor access (Rockland), wireless link reliability (Rockland), surge protection value (Suffolk/co-op HV; FAQ here is warranty coverage). Checker reports no exact masked duplicates.

### Similarity
Masked-geo paragraph similarity (difflib on masked word sequences, p/li/td/h3/figcaption ≥8 words; warranty sentence, proof strip and forms excluded): max 0.63 (staten-island, heading "...the pool is the front door" vs "...the drive is the front door"), 0.61 dutchess (hero stamp/opening constants), all others ≤ 0.59.

### Images (11, permanent image rule — no Drive/CompanyCam check in this run)
Copied into images/condo-security-systems/ with `condo-security-systems-ulster-county-` prefix. sha256 differs from every file in images/condo-security-systems/, images/co-op-security-systems/, images/co-op-board-intercom-upgrade/, images/condo-intercom-replacement/, images/condo-security-camera-installation/ (parallel builds at finish). Perceptual check (trimmed 24x24 grayscale + contact-sheet review) against the same dirs. Swapped during build: Samsung storeroom monitor view, Ulster bullet-on-ceiling grid (crop of co-op Putnam photo), tp-link VIGI NVR (= condo Nassau), UniFi G6 Entry (= used UniFi doorbell), turret kit + red DVR and Dahua multi-sensor panoramic (taken by parallel condo-security-camera-installation-nyc build). Rejected: AI-looking crew photos (fiber/soundbar/sonos/cat6/parking/video-wall sets, branded-shirt technicians), monitor grids showing people, Juice Bar signage, storeroom corner dome scene (used). No faces, house numbers, phone numbers or "AESS"; maker logos visible on product photos (Lorex, Ring, Ubiquiti, Hikvision-style).
| Page file (…ulster-county-) | ← Source | Kind | Where |
|---|---|---|---|
| video-entry-panel-being-fitted-to-tile-wall (hero/og, cropped, converted jpg→webp) | images/social/video-intercom-installation-sheepshead-bay-brooklyn-ny-20261122.jpg | job | hero |
| black-turret-camera-for-entrances | images/lorex-camera-installation/lorex-camera-installation-brooklyn-black-lorex-turret-camera-product-photo.webp | product | §5 |
| black-wired-video-doorbell-with-lit-ring | images/alarm-installation/alarm-installation-cypress-hills-napco-video-doorbell-product-photo.webp | product | §6 |
| bullet-cameras-with-red-and-blue-warning-lights | images/security-camera-maintenance/security-camera-maintenance-rockland-county-bullet-cameras-with-red-and-blue-warning-lights-product-photo.webp | product | §7 |
| ceiling-domes-over-shop-counter-and-shelves | images/security-cameras/security-cameras-orange-county-ceiling-domes-over-store-counter-and-shelves.webp | job | §8 |
| four-vandal-dome-cameras-over-recorder | images/security-camera-maintenance/security-camera-maintenance-rockland-county-four-vandal-dome-cameras-over-dvr-product-photo.webp | product | §9 |
| white-compact-indoor-camera | images/alarm-installation/alarm-installation-starrett-city-white-compact-indoor-camera-product-photo.webp | product | §10 |
| four-turret-cameras-with-red-and-blue-deterrent-lights | images/school-security-camera-installation/school-security-camera-installation-orange-county-four-turret-cameras-with-red-and-blue-lights-product-photo.webp | product | §10.5 |
| turret-camera-under-shop-awning-band | images/security-cameras/security-cameras-ulster-county-turret-dome-at-corner-of-yellow-sign-band-and-sky.webp | job | §11 |
| dual-lens-panoramic-pan-tilt-camera | images/wireless-camera-installation/wireless-camera-installation-westchester-county-dual-lens-panoramic-ptz-camera-product-photo.webp | product | §13 |
| wired-floodlight-camera-with-two-lamps | images/super-live-plus-app-support-repair/super-live-plus-app-support-repair-ulster-county-white-plug-in-floodlight-camera-with-power-cord-product-photo.webp | product | §14 |

DAILY-LOG note: `images: 11 reused from images/social/, security-cameras/, super-live-plus-app-support-repair/, security-camera-maintenance/, school-security-camera-installation/, lorex-camera-installation/, alarm-installation/, wireless-camera-installation/ (no real condo photos yet)`.

### Links
- Linked live: up /condo-security-systems-hudson-valley (breadcrumb, schema, §19); all 15 live condo pages once each (§19); Ulster service pages once each: /intercom-installation-ulster-county-ny, /door-buzzer-repair-ulster-county-new-york, /door-buzzer-installation-ulster-county-ny, /access-control-installation-ulster-county, /smart-lock-installation-ulster-county, /elevator-access-control-installation-ulster-county, /security-camera-installation-ulster-county-ny, /parking-lot-camera-installation-ulster-county, /alarm-installation-ulster-county, /fire-alarm-installation-ulster-county-ny, /structured-cabling-installation-ulster-county, /network-installation-ulster-county, /doorbell-camera-installation-ulster-county, /security-camera-maintenance-ulster-county, /security-camera-repair-ulster-county.
- Not linked (do not exist): /intercom-repair-ulster-county, /apartment-building-security-camera-installation-ulster-county, /co-op-security-systems-ulster-county (HOLD-THIN).
- FLIP comments (plain text): /condo-intercom-replacement (§6 intercom), /condo-security-camera-installation-ulster-county (§6 cameras; note: no queue line seen for this slug).
- Link backs needed (main run): all 15 live condo pages (HV hub + every sibling that carries an Ulster FLIP comment); per keyword rule one contextual link back from /intercom-installation-ulster-county-ny.

### Mobile
390px check: headless Chrome (old mode), page in a 390px iframe (file://, mega-nav.js not loaded): scrollWidth = clientWidth (375), no element past the viewport (after shortening form select options).
