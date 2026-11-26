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
