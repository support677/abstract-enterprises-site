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
