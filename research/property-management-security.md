# Research — Property Management Security silo (`property-management-security-*`)

Silo opened Nov 27 2026 with the NYC hub (`/property-management-security-nyc`). Audience hub for property managers, managing agents, landlords and building owners (same page type as co-op-security-systems-* and condo-security-systems-*). Rules: `keywords/property-management-security.md` (top section binding).

Every entry: exact query · platform · URL · finding · page + section used (v2.3 §12.4). Unreachable sources are marked EMPTY — never filled in.

## Silo-wide sources

| # | Query · platform | URL | Finding | Used on (NYC hub) |
|---|---|---|---|---|
| S1 | `HPD property registration managing agent required multiple dwelling three or more units annual registration` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page | Owners must register annually with HPD if the property is a multiple dwelling (3+ residential units); registration lists the managing agent's name, address and phone and a metro-area phone; deadline Sept 1 (FAQ says May 21–Sept 1); updates within 5 days of a managing-agent change; $13 fee billed by DOF; LL 71 penalties $500–$1,500 (≤5 units) / $1,000–$5,000 (>5 units) (page's FAQ lists different amounts); unregistered buildings can't certify violations or bring nonpayment actions. | §5 facts list; Q&A "building information before first visit"; vendor-onboarding section |
| S2 | `NYC landlord access to apartment notice 24 hours inspection one week improvements HPD rule 28 RCNY 25-101` · WebSearch → WebFetch | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-57154 | 28 RCNY §25-101: 24 hours' notice for inspections; written notice not less than one week ahead for repairs or improvements; urgent/emergency repairs need no written notice (phone, email or knock instead); access limited to 9 a.m.–5 p.m., not Saturdays, Sundays or legal holidays, unless the tenant agrees. | §5 facts list; Q&A tenant notice; occupied-building section; process step 5 |
| S3 | same query · WebFetch | https://askalawlibrarian.nycourts.gov/legalresearch/faq/425220 | NY Courts "Ask a Law Librarian": confirms §25-101 written notice generally one week ahead for repairs to units and public areas; urgent repairs by other means. | Corroborates S2 |
| S4 | `NYC Local Law 111 of 2018 self-closing doors apartment entrance doors HPD notice tenants` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | "apartment doors and hallway doors are required by law to swing closed and latch by themselves"; owners "must make prompt repairs to door closing mechanisms"; HMC §27-2041.1; Local Law 71 of 2022 has HPD proactively inspect self-closing doors in 300 class A multiple dwellings a year; 14 days to correct after NOV. (Page does not mention LL 111/2018 — not used.) | §5 facts list; Q&A self-closing doors + access control; door hardware section |
| S5 | `HPD 2023 Housing and Vacancy Survey ...` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/news/007-24/hpd-2023-housing-vacancy-survey-selected-initial-findings | 2023 NYCHVS: citywide rental vacancy 1.4%, lowest since the 1968 survey. Page gives no total rental-unit count (not used). | §5 facts list; turnover paragraph |
| S6 | `NYC Tenant Data Privacy Act Local Law 63 2021 ...` · WebFetch | https://intro.nyc/local-laws/2021-63 | LL 63/2021, Admin Code ch. 30 (§26-3001 ff.): "smart access system" for class A multiple dwellings, common areas or units; reference data only with express consent (writing or app); plain-language privacy policy (§26-3004); encryption, password changes, firmware updates (§26-3005); no sale of data (§26-3003(a)(1)); owners may not require tenants to use smart access to enter their own unit (§26-3003(b)(3)); authentication data destroyed within 90 days unless anonymized; moved-out tenants' reference data removed/anonymized within 90 days; statutory damages $200–$1,000 per unlawful sale (§26-3006); existing buildings not liable until Jan 1 2023. | Access control section; Q&A "require fobs for own apartment"; AI check #5; compliance callouts |
| S7 | reused from research/co-op-security-systems.md row L5 (verified there) | https://www.nysenate.gov/legislation/laws/MDW/50-A | MDL §50-a: class A multiple dwellings erected/converted after Jan 1 1968 with 8+ apartments need self-closing, self-locking entrance doors and a two-way voice intercom from each apartment to the lobby door with release from the apartment; pre-1968 buildings when tenants of a majority of apartments request in writing. | §5 facts list; intercom section; compliance callouts |
| S8 | reused from research/co-op-security-systems.md row D1 (NYC Open Data SODA query, verified there) | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5 | 2025 HPD violations whose description mentions an intercom: Bronx 1,637 · Brooklyn 1,157 · Manhattan 1,020 · Queens 342 · Staten Island 24 (total 4,180). | §5 facts + table; Q&A HPD violation |
| S9 | reused from research/co-op-security-systems.md row L9 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173505 | NYC BC 1010.1.9.8 sensor-release electric locks (egress sensor, unlock on power loss, push-to-exit 40–48 in., unlock on fire alarm/sprinkler activation); 1010.1.9.9 mag locks released by door hardware with built-in switch. | Door hardware section; compliance callouts |
| S10 | reused from research/co-op-security-systems.md row L10 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 | Admin Code §28-105.4.7: no electrical permit for signaling/communication/alarm/data wiring under 50 volts (life-safety exceptions). | Cabling section |
| S11 | reused from research/co-op-security-systems.md row L11 | https://cooperatornews.com/article/qa-camera-placement | Cooperator Q&A (Newman Ferrara): audio recording may implicate NY Penal Law §250 (eavesdropping). | Q&A audio recording |
| S12 | reused from research/co-op-security-systems.md row L12 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | HomeAdvisor intercom install "Normal Range: $1,200 - $8,500", residential framing. | AI check #1 |
| S13 | `Stuyvesant Town Peter Cooper Village 110 buildings 11,250 apartments rental complex Manhattan` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Stuyvesant_Town%E2%80%93Peter_Cooper_Village | 110 red-brick buildings (55 buildings with 110 street addresses) on 80 acres, First Ave to Avenue C, 14th–23rd Sts; 11,250 apartments. | §13 landmark card |
| S14 | `Starrett City Spring Creek Towers 46 buildings 5,881 apartments Brooklyn` · Firecrawl search (excerpt) | https://www.springcreektowers.com/aboutus.html | "a 5,881 apartment rental complex" (building count not confirmed — not used). | §13 landmark card |
| S15 | `LeFrak City Queens 20 buildings ...` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/LeFrak_City | Twenty apartment towers on 40 acres, 4,605 apartments, over 14,000 people. | §13 landmark card |
| S16 | `Parkchester Bronx 171 buildings ...` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Parkchester,_Bronx ; https://communityp.com/parkchester/ | 171 brick buildings, 8 or 13 stories; MetLife built the 129-acre complex 1938–1942. | §13 landmark card |
| S17 | reused from research/co-op-security-systems.md row N2 | https://chpcny.org/visualization/housing-stock-visualization/ | ~54% of NYC housing built before 1947; 62% of units in buildings with 6+ apartments (2023 NYCHVS via CHPC). | §5 facts list; §7 building types |
| S18 | Partner product photos (Reolink, authorized partner) · curl of product pages reolink.com/us/product/<model>/ | https://reolink.com/us/product/reolink-home-hub/ ; https://reolink.com/us/product/rln16-410/ ; https://reolink.com/us/product/cx810/ ; https://reolink.com/us/product/e1-outdoor-pro/ ; https://reolink.com/us/product/rlc-811a/ etc. | 10 manufacturer product photos; captions describe only what is visible and label them manufacturer photos. Luminys product images (luminyscorp.com) blocked by the build-env proxy (403) — not used. | Images 2–11 |

### Surfaces not reachable in this build environment
| Source | Status |
|---|---|
| Google PAA / PASF / AI Overview for "property management security NYC" | EMPTY (not accessible in build env) |
| Answer the Public | EMPTY (not accessible in build env) |
| Reddit r/NYCapartments, r/landlord, r/PropertyManagement | EMPTY (not accessible in build env) — no thread quoted on page |
| Yelp 1–3★ for NYC security/intercom vendors | EMPTY (not accessible in build env) |
| Bing / DuckDuckGo related searches | EMPTY (not accessible in build env) |
| Wikipedia direct fetch (Stuy Town, Starrett City, LeFrak, Parkchester) | WebFetch blocked (permission prompt unanswered); facts taken from Firecrawl search excerpts S13–S16 only |

AI Reality Check section on the page paraphrases common claims found in national cost guides (S12) and generic vendor marketing; it does not quote an AI Overview, since that surface was not reachable.

## Prices used on the NYC hub (all already live on the site)
- $250 service call — START_PRICES (tools/check_page.py, Anwar Nov 25 2026); /door-buzzer-repair-nyc.
- Apartment station swap $250–$525 · transformer $325–$650 · strike with alignment $450–$950 · riser repair in occupied prewar stock $850–$2,400 — /door-buzzer-repair-nyc.
- Lobby panel + transformer $1,200–$2,800 · most single-issue intercom repairs $250–$1,500 — /intercom-repair-nyc.
- Elevator access from $1,500 per car (Level 1, Brooklyn/Bronx), $1,875 Manhattan, $2,500 per car Level 2 — /elevator-access-control-installation-nyc.
- Access control from $1,500 per door (single door) — /access-control-installation-nyc.
- Four-camera systems from $950 (Brooklyn per BLUEPRINT §15.5 override, Queens, Bronx), $999 Staten Island, $1,099 Manhattan — /security-camera-pricing-nyc.
- Alarm central-station monitoring $30/month keypad-only, $45/month with app — /alarm-installation-nyc.
- Structured cabling $150–$300 per drop — /structured-cabling-installation-nyc.
- Maintenance agreements: no price (quoted per portfolio after survey). Fire alarm: no price (Hard Rule 13).

## Question register (every Q&A/FAQ question on any page of this silo)

Checked by meaning against co-op-security-systems-nyc and condo-security-systems-nyc question sets — none repeats.

### /property-management-security-nyc — Q&A (§9)
1. How do you price service across a portfolio when every building has a different system?
2. Can each building's work be invoiced to the entity that owns it?
3. What should a manager do after HPD writes an intercom violation?
4. What does it take to set Abstract Enterprises Security Systems up as a vendor in our management system?
5. Will you sign our master service agreement?
6. How much notice must tenants get before a technician enters an apartment for intercom work?
7. Can a landlord make tenants use a fob or app to get into their own apartment?
8. Do self-closing door rules change how you install locks and readers on apartment and stair doors?
9. Can our office staff add and remove fobs without calling a technician?
10. Can one technician cover several of our buildings on the same day?
11. Should cameras in a rental building record sound?
12. Can we watch the cameras for every building from one app?
13. Can a portfolio with five different intercom brands be standardized?
14. How do we protect a vacant apartment or an empty building between tenants?
15. What building information should we send before the first visit?

### /property-management-security-nyc — FAQ (§17)
1. Do you also cover buildings our company manages on Long Island and in the Hudson Valley?
2. Is there a set tier or minimum portfolio size for a maintenance agreement?
3. Do you offer guaranteed response times or a service level agreement?
4. Can tenants call you directly when the intercom stops working?
5. What deposit do you need before a visit or a project is scheduled?
6. Do you train supers and office staff on the systems you install?
7. Can you survey and document the systems already installed across our buildings?
8. Do you install smart locks for furnished or short-term rental units?
9. Do you work on weekends in occupied rental buildings?
10. Can a management company buy equipment through you for buildings it handles itself?


## Manhattan (property-management-security-manhattan) — built 2026-11-27, batch subagent

Phone (929) 560-0737 · GBP Bronx (460 E Fordham Rd) · start price $250 service call (START_PRICES). No other prices used.

### Research matrix
| Source | Exact query | Platform | URL | Finding | Used in |
|---|---|---|---|---|---|
| HPD registration | HPD property registration managing agent multiple dwelling three or more units requirement | Web search + fetch | https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page | Registration for 3+ unit multiple dwellings and non-owner-occupied 1-2 family; managing agent = natural person over 21, NYC business address, reachable at all times; $13/yr | Neighborhood paras + facts list |
| HPD ABCs of Housing (owners) | NYC Housing Maintenance Code 27-2043 intercom ... | Web search + fetch | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/abcs-of-housing-owners.pdf | Owners must "provide and maintain security measures, heat, hot and cold water, and good lighting" (p.4); TDPL section p.17 | Neighborhood para 2 (quote) |
| MDL §50-a | Multiple Dwelling Law 50-a intercom eight or more apartments ... | Web search + fetch | https://www.nysenate.gov/legislation/laws/MDW/50-A | Self-closing/self-locking entrance doors; intercom for 8+ apts built/converted after 1/1/1968; older buildings on majority tenant request | Facts list |
| Admin Code §27-2043 | (same search) | Web search + fetch | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-60480 | Key lock + key per unit; class A: heavy-duty latch set, deadbolt, chain guard | Facts list |
| HPD self-closing doors | (same search) | Web search + fetch | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | LL71/2022, 300 bldgs/yr, class C, 14 days | Not used on page (context only) |
| Tenant Data Privacy Law | NYC HPD Tenant Data Privacy Law smart access systems owners requirements 90 days | Web search + fetch | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Policy, express consent, minimum data, delete auth data within 90 days unless anonymized, no sale, cannot require smart access for unit entry | Facts list, Access Control, Q&A, AI check, Tenants |
| HPD 2023 HVS | 2023 NYC Housing and Vacancy Survey Manhattan rental units ... | Web search + fetch | https://www.nyc.gov/site/hpd/news/007-24/new-york-city-s-vacancy-rate-reaches-historic-low-1-4-percent-demanding-urgent-action-new-affordable-housing | 1.4% vacancy, ~33,000 units available, Feb 8 2024 | Access Control (turnover) |
| LPC Permit Guidebook ch.11 | Landmarks Preservation Commission permit security camera intercom installation ... | Web search + fetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Staff permits for intercom panels within/adjacent to door opening, max one per opening; not on primary facade unless no option; cameras 2 per 25 ft (small) / 3 (large); ordinary repair exempt | Building types (landmarked) |
| LPC About | LPC protects more than 37,000 buildings ... | Web search + fetch | https://www.nyc.gov/site/lpc/about/about-lpc.page | 38,000+ landmark properties, 157 historic districts | Facts list |
| Manhattan BP e-commerce report | NYC DOT packages delivered per day ... | Web search + fetch | https://www.manhattanbp.nyc.gov/wp-content/uploads/2022/10/MBPO-Report-Tackling-the-E-Commerce-Delivery-Crisis-2.pdf | 2.4M packages/weekday; ~80% residential vs ~40% pre-pandemic | Facts list, Package Rooms |
| The Cooperator, Sep 6 2018 | Manhattan building service entrance delivery ... package rooms | Web search + fetch | https://cooperatornews.com/article/delivery-overload | Package rooms overflowing; doormen pulled from door; quotes Greg Cohen (Impact Management): "It could be 1,000 percent..." and "We have security cameras, so we saw it" | Package Rooms (real quote) |
| Our Town, Jan 9 2025 | Manhattan apartment building package room thief arrested 2025 ... | Web search + fetch | https://ourtownny.com/news/cops-nab-career-burglar-on-east-89th-street-DH4081476 | Dec 29 2024 arrest on E 89th St, packages fell from jacket; earlier mailroom/basement entries | Package Rooms |
| NYC DEP construction noise | NYC noise code construction work permitted hours ... | Web search + fetch | https://www.nyc.gov/site/dep/environment/construction-noise-rules-regulations.page | Weekdays 7am–6pm without after-hours authorization | Elevator/freight, Commercial compliance |
| NYC DOB elevator licenses | NYC DOB elevator work must be performed by licensed elevator agency ... | Web search + fetch | https://www.nyc.gov/site/buildings/industry/elevator-licenses-and-helper-card.page | NYS Elevator Safety Act eff. 1/1/2022; Elevator Agency Director; technicians under director supervision | Elevator section, AI check |
| Reddit / PAA / PASF / ATP / AI Overview / Yelp / Bing-DDG | reddit NYC property manager intercom vendor key fob ... | Web search | — | EMPTY (not accessible in build env); search returned vendor blogs only | — |
| Hyperlocal news beyond Our Town | — | — | — | EMPTY beyond the items above | — |

### Question register additions (property-management-security-manhattan)
- Q&A: When several of our buildings are failing at once, which do we fix first?
- Q&A: What happens to the system logins if the owner sells a building or moves it to another management firm?
- Q&A: What should a security scope of work for a Manhattan building contain so that several bids can be compared?
- Q&A: Do keyless entry systems change what we have to give tenants under city law?
- Q&A: How do we give porters, contractors and outside vendors access without handing out a master key?
- Q&A: Should leasing agents be able to show vacant apartments without someone from the building letting them in?
- Q&A: Which system settings should only a technician change?
- Q&A: How should delivery drivers get through a service entrance without using the residents' intercom?
- Q&A: Can the elevator limit movers to one floor on a move-in day?
- Q&A: How do we give a ground-floor restaurant's staff the shared cellar without giving them the residential lobby?
- Q&A: How should we present a security proposal to an owner who wants one number for the whole portfolio?
- Q&A: What documentation should we get at the end of an install so the next super is not starting from scratch?
- Q&A: Why does the same intercom fault keep returning after other vendors fix it?
- Q&A: What happens to the intercom, doors and cameras during a power outage?
- FAQ: Does the super or another staff member need to be at the building for every visit?
- FAQ: Should we keep spare parts on site for the systems in our buildings?
- FAQ: Can you repair a system whose original installer is out of business?
- FAQ: Can you build to the security requirements in an insurance policy or a loan agreement?
- FAQ: How far ahead should we plan a building-wide installation?
- FAQ: Do you take out the old equipment when you replace a system?
- FAQ: Can new entry panels match the finish of a renovated lobby?
- FAQ: How long does a typical service call take once the technician arrives?
- FAQ: Can you work alongside our elevator and fire alarm contractors on the same project?
- FAQ: Do you provide security guards or patrol services?
- FAQ: Do you give us a written report after maintenance visits?
### Images (11, permanent image rule; no unused real job photos remained — every library job photo was already in the co-op/condo/apartment-camera folders)
Library product photos copied: ubiquiti-unifi-g6-turret-4k-camera-black.jpg, alarm-com-vdb775-video-doorbell.webp, ubiquiti-unifi-g5-pro-4k-bullet-camera-white.jpg, cam-eyeball-warm.jpeg, floodlight-night-owl-fwip3.png, nvr-installation/...avycon-sixteen-channel-recorder-product-photo.webp, floodlight-tapo-c720.png, lorex-wifi-ptz-camera-installation-westchester-county.jpg. Partner (Reolink) product photos via Firecrawl/CDN: Video Doorbell PoE + chime (hero), dual-lens floodlight, dual-lens bullet. Checked by sha256, ORB feature matching and normalized correlation against co-op/condo/co-op-camera/condo-camera/apartment-camera folders and the NYC PM images.


## Brooklyn (property-management-security-brooklyn) — built 2026-11-27, batch subagent

Phone (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, `#brooklyn`) · start price $250 service call (START_PRICES). Other prices only as already published on Brooklyn pages (cited below).

### Research matrix
| Source | Exact query | Platform | URL | Finding | Used in |
|---|---|---|---|---|---|
| NYC IBO, May 2026 | `Rent Guidelines Board rent stabilized units by borough Brooklyn number 2024 housing supply report` | WebSearch → WebFetch | https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/housing-and-buildings/2026/2026-may-segments-of-the-rent-stabilized-housing-stock.pdf | "Brooklyn and the Bronx have the largest number of rent stabilized apartments, with 279,000 and 233,000 apartments respectively"; ~1 million stabilized citywide = 41% of rentals | Neighborhood para 2; facts list |
| CHPC housing stock | `Brooklyn small multifamily buildings 3 to 10 units share of housing stock report walk-up brownstone landlords` | WebSearch → WebFetch | https://chpcny.org/visualization/housing-stock-visualization/ | Brooklyn "has the most even distribution of building sizes among the boroughs" (no Brooklyn unit-size %, not used) | Neighborhood para 1 (quote) |
| Furman Center small rentals | same query | WebFetch | https://furmancenter.org/research/publication/maintenance-and-investments-in-small-rental-properties-findings-from-new-yo | 2013 working paper; no Brooklyn figures | Not used |
| NYS HCR living conditions | `HCR DHCR owner application to modify services rent stabilized building intercom key card entry system RA-2 fact sheet` | WebSearch → WebFetch | https://hcr.ny.gov/living-conditions-and-essential-services | Owners "are required to maintain all required services and equipment in good working order"; "broken door locks" example of decreased service; RA-81 (apartment) / RA-84 (building-wide) complaints; RA-84.2 covers doorman/security | Facts list; Rent-stabilized section |
| HCR Fact Sheet #3 | same query | WebFetch | https://hcr.ny.gov/system/files/documents/2024/11/fact-sheet-03-11-2024.pdf | No intercom/lock mention; refers to Operational Bulletin 2024-2 and IAI | Not quoted |
| HCR IAI/MCI page | (search result, same query) | WebSearch | https://hcr.ny.gov/apartment-iai-and-building-mci-improvements | Link only, for owner/counsel on improvement rent increases | Rent-stabilized para 3 (link, no claim) |
| Legal Services NYC, May 1 2019 | `Atlantic Plaza Towers Brownsville facial recognition tenants landlord Nelson Management 2019` | WebSearch → WebFetch | https://legalservicesnyc.org/?p=1612 | Atlantic Plaza Towers (2 buildings, Brownsville, rent-stabilized); owner applied to HCR July 2018 for StoneLock facial-recognition entry; 130+ tenants filed opposition May 1 2019. Outcome not reported on that page (not stated on our page) | Access control para 3; Q&A face recognition; landmark card |
| LPC press release Apr 12 2016 | `Brooklyn historic districts count Landmarks Preservation Commission Park Slope Historic District number of buildings` | WebSearch → WebFetch | https://home4.nyc.gov/site/lpc/about/pr2016/04-12b.page | Park Slope HD Extension II = 292 buildings; brings total protected buildings in Park Slope to 2,853 | Facts list; landmark card |
| Spring Creek Towers | reused from silo row S14 | Firecrawl excerpt | https://www.springcreektowers.com/aboutus.html | "a 5,881 apartment rental complex" | Landmark card (landmark only, not client) |
| HPD intercom violations | reused from silo row S8 / co-op D1 | NYC Open Data | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5 | 2025 Brooklyn 1,157 intercom-mention violations (2nd after Bronx 1,637) | Neighborhood para 3 |
| MDL §50-a, 28 RCNY §25-101, LL 63/2021, HPD self-closing doors, BC §1010.1.9, Admin Code §28-105.4.7, LPC Guidebook ch.11, Cooperator audio Q&A, HomeAdvisor | reused from silo rows S2, S4, S6, S7, S9, S10, S11, S12 and Manhattan LPC row | — | (see silo table) | as recorded there | Facts list, doors, cabling, commercial callouts, tenants, AI check |
| NYC Open Data live query (registrations by borough) | `tesw-yqqr` SODA count by boroid | curl | https://data.cityofnewyork.us/resource/tesw-yqqr.json | EMPTY (not accessible in build env: proxy 403) | — |
| Reddit / PAA / PASF / ATP / AI Overview / Yelp / Bing-DDG for Brooklyn property managers | — | — | — | EMPTY (not accessible in build env) | — |

### Prices used (all already on Brooklyn pages)
- $250 service call — START_PRICES; /door-buzzer-repair-brooklyn-new-york.
- Station $250–$525, relay (not used), transformer $325–$650, strike $450–$950, lobby panel $650–$1,800, riser $850–$2,400 — /door-buzzer-repair-brooklyn-new-york (same as /door-buzzer-repair-pricing).
- Single-door lobby fob reader $1,500–$2,500 installed — /access-control-installation-brooklyn.
- Elevator reader $1,500/car Level 1, $2,500/car Level 2 — /elevator-access-control-installation-brooklyn.
- Monitoring $30/mo keypad, $45/mo app — /alarm-installation-brooklyn.
- Maintenance agreements and new systems: no price (quoted after survey/assessment). Fire alarm: no price.

### Question register additions (property-management-security-brooklyn)
Checked by meaning against NYC + Manhattan registers above and the parallel Bronx and Queens drafts on disk (overlapping drafts replaced: smartphone-less tenants, propped doors, weather faults, walk-up vs big-building equipment, two-family service, package lockers, electrician, hallway footage requests).
- Q&A: For a twelve-unit walk-up, is a directory keypad or a row of call buttons the better panel?
- Q&A: Which of our small buildings can get by with video doorbells instead of an entry panel?
- Q&A: How do you handle a brownstone where the original buzzer plate is part of the landmarked facade?
- Q&A: Should a building with a part-time super be set up differently from one with a live-in super?
- Q&A: Can a rent-stabilized building keep its old audio intercom instead of upgrading?
- Q&A: Should we put face recognition on the front door of a rent-stabilized building?
- Q&A: Should we install the new apartment station while a unit is vacant, before the building-wide upgrade?
- Q&A: Who should pay for the alarm and cameras in a ground-floor store, the owner or the store tenant?
- Q&A: Should the building rely on the store's cameras to cover the residential entrance?
- Q&A: How do you work in a garden-apartment complex where several buildings share one courtyard and gates?
- Q&A: Can a large complex move to new fobs one building at a time without tenants getting confused?
- Q&A: What should the entry panel show when tenants do not want their names posted outside?
- Q&A: How do we stop strangers from slipping in behind tenants at the street door?
- Q&A: What happens when one tenant will not let the technician in for intercom work?
- Q&A: Can a camera read license plates in a Brooklyn building's parking lot?
- Q&A: Can the super get an alert on his phone when the cellar or roof door is opened at night?
- Q&A: How do we add new equipment without cutting off tenants' internet and TV wiring in the riser?
- FAQ: Do you work in Brooklyn buildings outside the brownstone neighborhoods, such as Canarsie, Coney Island and East New York?
- FAQ: Will new readers work with the fobs our tenants already carry?
- FAQ: Can you cancel the old vendor's cloud subscription when we switch a building to your system?
- FAQ: Do you install entry readers and call boxes on gates and fences around Brooklyn buildings?
- FAQ: Can the intercom ring the super's phone when no one answers the office line?
- FAQ: Can you add a camera to a system another company installed?
- FAQ: Can we buy spare fobs and cards from you so the office can issue them itself?
- FAQ: Who pays when a tenant damages a new intercom station or reader?
- FAQ: Is financing available for upgrading several Brooklyn buildings at once?
- FAQ: Can footage be kept longer than the recorder's default setting?
- FAQ: Can you give us the addresses of other Brooklyn buildings you work in?

### Images (11, permanent image rule — partner Reolink product photos, no unused real job photos found)
Library scan: dHash + sha256 over all 18,090 library images; every real job photo not already in the six excluded folders was either a re-crop of a scene used there, AI-generated (staff/van/school scenes, `ai/`, `gbp-photos/`), a text carousel, or showed a business sign. Partner (Reolink, authorized partner) product photos pulled from reolink.com product pages (home-cdn.reolink.us): Video Doorbell WiFi (hero), Chime, CX410, RLN36, RLK16-1200D8-A, RLK8-800B4, Lumus (x2), Home Hub Pro, Duo 3 WiFi, RLK8-1200D4-A. Each checked by sha256, normalized correlation and ORB matching against images/property-management-security/*, co-op-security-systems/*, condo-security-systems/*, co-op-security-camera-installation/*, condo-security-camera-installation/*, apartment-building-security-camera-installation/* — 16 other Reolink shots rejected as already used there. Also compared with the parallel Bronx/Queens images: no shared photo; Bronx uses a different bullet camera and a plain product shot of the same Home Hub Pro (ours is the on-cabinet lifestyle shot). Captions say "Partner product photo" and describe only what is visible. Lorex (lorex.com/cdn.shopify.com) and Luminys blocked by the build-env proxy.
DAILY-LOG note: `images: 11 partner (Reolink) product photos via reolink.com (no unused real property-management photos)`.


## Queens (property-management-security-queens) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd) · start price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| Q1 | `Rent Guidelines Board housing supply report rent stabilized units Queens number 2024` · WebSearch → Firecrawl scrape (PDF, directQuote) | https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2026/05/2026-HSR.pdf | 2026 HSR: Queens newly completed units up 17.9% to 9,608 (2025); average new building 33.7 units in Queens; newly certified 421-a units Queens 5,913 (20.6% of city); Queens 421-a rental certifications up 104.0%. (Borough rent-stabilized count not in the extract — not used.) | §Neighborhood para 2; stamp |
| Q2 | `Queens County foreign born percent language other than English spoken at home Census QuickFacts` · Firecrawl search (excerpts) | https://www.census.gov/quickfacts/fact/table/queenscountynewyork,newyorkcitynewyork/PST045225 | Queens foreign-born 47.6% (2020–2024); language other than English at home 55.4% (Queens) vs 47.7% (NYC). | §Neighborhood para 3; mailroom "Notices" H3 |
| Q3 | reused: research/condo-security-systems.md Queens row D1 + co-op Queens row Q10 (NYC Open Data SODA, verified there) | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5 | Queens 2025 HPD violations mentioning intercom: 342 (A 79 · B 261 · C 2); by CB: 3=48, 7=49, 8=50 highest. | §Neighborhood para 4; Q&A class B/C |
| Q4 | `HPD violation classes Class A non-hazardous 90 days Class B hazardous 30 days Class C immediately hazardous 24 hours nyc.gov` · Firecrawl search (excerpt) | https://www.nyc.gov/site/hpd/services-and-information/clear-violations.page | Class A 90 days; B 30 days; most C 24 hours; C self-closing doors 14 days; C heat/hot water no time. | §Neighborhood para 4; facts list; Q&A class B/C |
| Q5 | `Hurricane Ida 2021 Queens basement apartments deaths flooding nyc.gov report` · Firecrawl search (excerpts) | https://www.nyc.gov/assets/em/downloads/pdf/hazard_mitigation/Impacts_of_PTC_Ida.pdf ; https://www.nyc.gov/assets/cdbgdr/documents/Executive_Summary.pdf | 13 New Yorkers died in flash floods, 11 by drowning in basement apartment flooding; damaged properties concentrated in Queens, Brooklyn and the Bronx. | facts list; alarms/backup power para; AI check "flood damage" |
| Q6 | `Queens apartment building package thief lobby 2026 NYPD Flushing OR Jamaica OR Astoria OR "Forest Hills"` · Firecrawl search (news) → Firecrawl scrape (directQuote) | https://qns.com/2025/10/suspect-wanted-burglary-forest-hills/ | QNS, Bill Parry, Oct 10 2025: 112th Pct; man entered building near 112th St & 73rd Ave through front door ~4:15 p.m. Tue Oct 7; on video sitting on lobby couch; entered an apartment, took $600 phone, fled through courtyard; NYPD released surveillance images. Location given only as the cross streets QNS published; no building named. | Cameras section para 2; AI check "cameras deter crime" |
| Q7 | `LeFrak City Queens apartment complex 20 buildings 4,605 apartments built 1960s Corona Elmhurst` · WebSearch → Firecrawl scrape (directQuote) | https://en.wikipedia.org/wiki/LeFrak_City | 4,605 apartments; Junction Blvd (W), 57th Ave (N), 99th St (E), LIE (S); twenty 17-story towers on 40 acres, 14,000+ residents; built 1962–1971. Landmark only, not a client. | Landmarks card 1 |
| Q8 | reused: research/apartment-building-security-camera-installation.md row 16 (verified there) | https://hdc.org/borough/jackson-heights/ | Jackson Heights HD designated Oct 19 1993; built mainly 1914–1939; "first and remains the largest garden-apartment community in the United States". | Building types "Landmarked" H3; Landmarks card 2 |
| Q9 | reused silo rows S2, S6, S7, S9, S10, S11 + Manhattan rows (DOB elevator licenses, DEP construction noise, LPC permit guidebook) | 28 RCNY §25-101; intro.nyc LL63/2021; nysenate MDL §50-a; NYC BC 1010.1.9.8/9; Admin Code §28-105.4.7; cooperatornews.com/article/qa-camera-placement; nyc.gov DOB elevator licenses; nyc.gov DEP construction noise | As in silo/Manhattan register. | facts list; access control; elevator; cameras (audio); alarms/cabling; commercial compliance list; tenants section |
| Q10 | reused silo row S1 | https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page | HPD registration for 3+ unit multiple dwellings; managing agent listed; updates on agent change. | facts list |
| R1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG | — | EMPTY (not accessible in build env). AI check section corrects claims typical of national cost guides and AI summaries; no AI quote invented. | — |

### Prices used (all already on Queens pages)
- $250 service call — START_PRICES; /door-buzzer-repair-queens-new-york, /intercom-installation-queens-ny.
- Apartment station $250–$525 · strike with alignment $450–$950 · riser repair $850–$2,400 — /door-buzzer-repair-queens-new-york.
- Single door reader + strike $1,500–$2,500 — /access-control-installation-queens.
- Elevator access from $1,575 per car (Level 1), $2,625 per car (Level 2) — /elevator-access-control-installation-queens.
- Four-camera 1080p systems starting at $950 — /security-camera-pricing-queens.
- Alarm monitoring $30/mo keypad-only, $45/mo with app — /alarm-installation-queens.
- No maintenance-contract, package, per-unit or fire alarm prices.

### Question register additions (property-management-security-queens)
- Q&A: Our portfolio runs from two-family rentals in Ridgewood to a large tower in Long Island City. Can one contractor really service both ends of that range?
- Q&A: Is it better to replace a failing system at one building now, or wait and replace a group of buildings together next year?
- Q&A: Can one management login cover buildings that are owned by different LLCs?
- Q&A: Should a multi-building rental campus record everything on one central recorder or keep a recorder in each building?
- Q&A: Our complex's parking lot is next to a shopping strip. How do we keep tenant spaces for tenants?
- Q&A: A store tenant on the ground floor has its own alarm company. Can its system and ours share the building's doors?
- Q&A: Several tenants in one building have no smartphone. Can the intercom still ring their apartments?
- Q&A: A tenant asked for hallway footage after a dispute with a neighbor. Do we have to hand it over?
- Q&A: Our walk-up has no elevator and no live-in super. What is the minimum that keeps the front door dependable?
- Q&A: A new Long Island City rental came with a cloud intercom and a monthly platform fee. Can we keep the hardware and change the subscription?
- Q&A: When does repairing an old intercom stop making financial sense in a rental building?
- Q&A: What fails first after a power surge or a nearby lightning strike, and how is it prevented?
- Q&A: What should a fall walk-through of our buildings check before the heating season?
- Q&A: Is a class C intercom violation handled differently from a class B one?
- FAQ: Can you meet the owner's architect or engineer on site during a renovation?
- FAQ: Do you repair intercoms and cameras damaged by flooding?
- FAQ: Is the assessment free when we ask you to look at several buildings at once?
- FAQ: Do you install electronic package lockers?
- FAQ: Will our electrician need to be involved?
- FAQ: Can you set up a virtual doorman for one of our buildings?
- FAQ: How do we reach you when a building problem comes up after 8 p.m.?
- FAQ: Do you service intercoms in two- and three-family rental houses?
- FAQ: Can a new entry system use the wiring already in the walls?
- FAQ: How will our super know your technician is legitimately from you?

Intent check (by meaning) against PM NYC + Manhattan registers and the Queens co-op, condo, co-op camera, condo camera and apartment-camera question sets: avoided repeats of — triage of several failing buildings, logins on sale/transfer, scope for bid comparison, TDPA tenant duties, vendor/contractor access, leasing self-tours, delivery-driver service entrance, cellar flooded recorder relocation, multilingual notice wording, landline shareholders, internet outage, documenting existing systems, one-app viewing, standardizing brands, invoicing per entity, guaranteed response, COI timing, out-of-business installer. Brooklyn/Bronx PM drafts on disk at check time: `check_page.py` found no duplicated question with them.

### Images (11, permanent image rule; no Drive/CompanyCam check in this run)
Library job photos and library product photos were tested first by perceptual hash (dHash) and ORB feature matching (RANSAC inliers) against images/property-management-security/*, co-op-security-systems/*, condo-security-systems/*, co-op-security-camera-installation/*, condo-security-camera-installation/*, apartment-building-security-camera-installation/*: every PM-relevant job photo and recorder/floodlight product photo already appears there (inliers 60–650), so none was usable. All 11 are Reolink (authorized partner) manufacturer product photos fetched from reolink.com product pages (Firecrawl image lists / og:image, home-cdn.reolink.us), flattened on white, WebP. Each checked: sha256 unique; ORB inliers vs the six folders ≤ 29 except the four-antenna recorder (52, false match on a bullet camera, visually distinct); re-checked against the parallel Brooklyn/Bronx PM images — the Bronx builder used the same spotlight dome photo, so that one and a near-identical varifocal dome were dropped and replaced. No faces, house numbers, phone numbers or "AESS".
| File (images/property-management-security/) | Source | Where |
|---|---|---|
| …-queens-pan-tilt-poe-camera-for-courtyards.webp | reolink.com/us/product/e1-outdoor-se-poe/ (og:image) | hero (eager), og/twitter image |
| …-queens-four-antenna-recorder-for-small-buildings.webp | reolink RLN12W product image (reolink.com/wp-content/uploads/2023/09/260249431695696583.3194.png, listed on business.reolink.com/us/product/rln12w/) | §Neighborhood |
| …-queens-turret-camera-for-side-and-rear-doors.webp | home-cdn …/2025/06/RP-PCT12M-1Pack@1x.png | Intercom section |
| …-queens-turret-camera-with-size-callouts.webp | home-cdn …/assets/tespecs/rlc-1224a-1.png | Access control section |
| …-queens-sixteen-channel-poe-recorder.webp | home-cdn …/2025/07/RP-PN16-400@1x.png | Elevator section |
| …-queens-zoom-bullet-camera-for-parking-and-driveways.webp | home-cdn …/2025/06/RP-PCB8MZ-1pack.png | Cameras section |
| …-queens-wifi-recorder-rear-panel.webp | home-cdn …/2023/11/150717011700032621.3754.png (RLN12W rear) | Alarms/infrastructure section |
| …-queens-turret-camera-aiming-range.webp | home-cdn …/assets/tespecs/rlc-1224a-2.png | Building types section |
| …-queens-sixty-four-channel-recorder-front.webp | home-cdn …/2026/05/BOX-RP-N64-1@2x.jpg (cropped) | Commercial section |
| …-queens-plug-in-camera-power-adapter.webp | reolink RLN12W page in-box accessory image (reolink.com/wp-content/uploads/2023/11/150840081700037608.1126.png) | Service section |
| …-queens-sixty-four-channel-recorder-rear-ports.webp | home-cdn …/2026/05/BOX-RP-N64-2@2x.jpg (cropped) | Q&A section |

### FLIPs on the page (plain text + comment)
/property-management-security-staten-island, -long-island, -nassau-county, -suffolk-county, -hudson-valley, -westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county; /apartment-building-security-systems-queens.


## Bronx (property-management-security-bronx) — built 2026-11-27, batch subagent

Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd) · start price $250 service call (START_PRICES). Other prices used are only those already published on Bronx pages: door-buzzer-repair-bronx-new-york (station $250–$525, transformer $325–$650, strike with alignment $450–$950, branch riser $850–$2,400); elevator-access-control-installation-bronx (Level 1 from $1,500/car, Level 2 from $2,500/car); alarm-installation-bronx ($30/mo keypad-only, $45/mo app); structured-cabling-installation-bronx ($150–$300 per drop). No fire alarm prices. Maintenance agreements: no price.

### Research matrix
| Source | Exact query | Platform | URL | Finding | Used in |
|---|---|---|---|---|---|
| HPD 2023 NYCHVS initial findings | "Bronx" share of households that rent percent renter-occupied 2023 Housing and Vacancy Survey borough Bronx vacancy rate | WebSearch → WebFetch | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | Bronx renter-occupied 436,800 (Table 7, p.18); Bronx occupied units 529,900, 26% with 3+ reported housing problems, Bronx highest prevalence of problems (Table 12, pp.37–38); Bronx rental vacancy 0.82% (Table 9, p.23, flagged high variability) | §5 paras 1–2, facts list |
| NYC Open Data HPD violations (reused, research/co-op-security-systems.md D1 / silo S8) | — | — | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5 | 2025 violations mentioning intercom: Bronx 1,637, Brooklyn 1,157 (highest borough) | §5 para 2, facts list |
| Bronx Times, Marina Samuel, May 22 2026 | Bronx renters share of households rent stabilized units Furman Center borough profile Bronx | WebSearch → WebFetch | https://www.bxtimes.com/our-forgotten-borough-rent-stabilized-buildings/ | Avg Bronx stabilized rent $1,190 (2024), ~$500 below citywide (CPC data); Bronx only borough with NOI decline (RGB 2026 I&E); CD 4, 5, 7 concentrations of pre-1974 stabilized buildings; manager quote ~20% of buildings in foreclosure/default/restructuring; Highbridge tenant: "persistent security issues" and quote "We cannot go on paying rent, not getting the services that we deserve." | §5 paras 3–4 (real quote), Regulated section, landmark card Highbridge |
| UNHP blog, Nov 18 2025 (summarizing ANHD + Enterprise/NEF) | Bronx nonprofit housing owners affordable housing portfolio Bronx share of HPD financed units | WebSearch → WebFetch | https://unhp.org/blog/2-reports-confirm-affordable-housing-struggles/ | "The Bronx emerges as the clear epicenter" of at-risk affordable housing; >50% of 428 regulated developments negative cash flow | §5 para 3 |
| CityLand, Grand Concourse HD | Grand Concourse Historic District Landmarks Preservation Commission designation report apartment buildings Art Deco | WebSearch → WebFetch | https://citylandnyc.org/new-grand-concourse-historic-district-approved | Designated unanimously Oct 25 2011; 78 buildings along/near Concourse, 153rd–167th Sts; Art Deco/Moderne 1930s | Facts list, Building Specialists, landmark card |
| LPC Permit Guidebook ch.11 (reused from Manhattan research row) | — | — | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Staff permits for intercom panels within/adjacent to door opening | Building Specialists (Concourse method), Q&A store cameras |
| THE CITY, Jan 23 2022 | Twin Parks North West fire January 2022 self-closing door failed 17 killed East 181st Street Bronx | WebSearch → WebFetch | https://www.thecity.nyc/2022/01/23/damaged-doors-fire-risks-thousands-buildings-nyc/ | 17 died (smoke inhalation); fire-apartment self-closing door "didn't function properly"; 15th-floor stair door open; 18,305 open self-closing-door violations in 10,610 buildings as of Jan 11 2022, concentrated in lower-income Bronx neighborhoods | Doors section, Q&A Twin Parks |
| HPD penalties and fees | HPD intercom violation class B owner must maintain intercom ... | WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/penalties-and-fees.page | Self-closing doors Class C, 14 days, $250–$500 + $250/day | Facts list, Doors section, Q&A stair door |
| HPD self-closing doors page (silo S4) | — | — | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | Quote "are required by law to swing closed and latch by themselves" | Doors section |
| HPD AEP 2025 release, Mar 25 2025 | HPD Alternative Enforcement Program 2025 buildings selected Bronx number of buildings round | WebSearch → WebFetch | https://www.nyc.gov/site/hpd/news/010-25/hpd-sharpens-enforcement-against-nyc-s-worst-apartment-buildings | 250 buildings, 6,830 homes, 53,986 open violations, 15,463 immediately hazardous; no borough breakdown on page | Regulated section |
| News 12 Bronx, Sep 24 2024 | Bronx Times package theft apartment building lobby 2025 OR 2026 thieves mailroom Bronx | WebSearch → WebFetch | https://bronx.news12.com/mount-eden-apartment-tenants-say-mail-is-being-stolen-due-to-broken-mailboxes | Mount Eden building, unlocked mailbox panel; tenant: lack of cameras made police report hard; quote "I've spoken to the management company about this issue, and they haven't fixed it, it's a problem," (building/HDFC name and street NOT used on page) | Cameras section |
| NYC SBS CDNA Fordham | The Hub 149th Street Third Avenue Bronx BID retail corridor Fordham Road BID | WebSearch → WebFetch | https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/avenyc-cdna-fordham.pdf | 657 storefronts; safety top merchant change 82% (assessment Sep 2021–Jun 2022) | Commercial section, landmark card |
| NYC SBS CDNA The Hub/Melrose | (same) | WebFetch | https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/avenyc-cdna-thehub-melrose.pdf | 613 storefronts, 107 vacant (17.5%); safety 73%; merchant quote "Too many thefts, need cops present always." (data Sep 2024–Jun 2025) | Commercial section |
| Silo sources reused: MDL §50-a (S7), HPD registration (S1), 28 RCNY §25-101 (S2), Tenant Data Privacy Law (S6 + HPD page from Manhattan row), Admin Code §28-105.4.7 (S10), Parkchester 171 buildings MetLife 1938–1942 (S16), DEP construction noise hours and DOB elevator licenses (Manhattan rows) | — | — | see silo table | as cited | Facts list, Access, Occupied, Elevator, Commercial compliance, landmark card |
| Reddit / PAA / PASF / ATP / AI Overview / Yelp / Bing-DDG | — | — | — | EMPTY (not accessible in build env) | AI Reality Check paraphrases common national-guide claims, does not quote an AI Overview |

### Question register additions (property-management-security-bronx)
Checked by meaning against NYC + Manhattan registers above, the parallel Brooklyn and Queens drafts on disk at build time (three questions swapped to avoid overlap: footage requests, package lockers, electrician), and the co-op-security-systems-bronx / condo-security-systems-bronx question sets.
- Q&A: A stair door with a fob reader has an open self-closing door violation. Who fixes which part?
- Q&A: After the Twin Parks fire, what should a manager check on doors that have locks or readers?
- Q&A: How should an intercom be handled in apartments where tenants removed or painted over the station?
- Q&A: Tenants want a bike room and storage cages in the cellar. Can they get in without reaching the boiler room?
- Q&A: How do we stop a courtyard gate or rear door from being propped open all day?
- Q&A: With a small camera budget in a walk-up, which spots should be covered first?
- Q&A: How long can entry records about a tenant be kept after the tenant moves out?
- Q&A: Which staff should be able to watch live cameras, and who should be able to export video?
- Q&A: Our previous vendor still holds the administrator password. How do we get control back?
- Q&A: Should cameras and the intercom share the building's internet with the office and the laundry machines?
- Q&A: Why does the intercom in an older building act up after heavy rain?
- Q&A: The elevator is old and the elevator company is reluctant to connect anything to it. Can we still restrict floors?
- Q&A: Do the small walk-ups in our portfolio get the same equipment as the large buildings?
- Q&A: A store tenant wants to put its own cameras on our building's facade. Should we allow it?
- FAQ: Will you work alongside our own porters and maintenance staff on the same job?
- FAQ: Can you start work in a building that has open HPD violations?
- FAQ: Can a technician be at the building when an HPD inspector comes back?
- FAQ: Can a large upgrade be split across two budget years?
- FAQ: Do you set up security for supportive housing with a staffed front desk?
- FAQ: Do you replace the intercom wiring inside tenants' apartments?
- FAQ: Will you install cameras or an intercom the owner already bought?
- FAQ: What warranty comes with your repairs and installations?
- FAQ: What time of day do your technicians usually arrive?
- FAQ: Do you install security systems in buildings still under construction or gut renovation?

### Images (11, permanent image rule)
No unused real job photos remained: every candidate real photo in the library (lobby ceiling cameras, corridors, fascia domes, cable racks) matched an image already in the co-op/condo/apartment-camera/PM folders (ORB + correlation + visual check), and the one distinct rack photo looked AI-generated, so not used. All 11 are Reolink (authorized partner) manufacturer product photos fetched from reolink.com/us/product/* pages (models: Video Doorbell WiFi, RLC-843A, Duo 3V PoE, FE-P, CX820, Home Hub Pro drive + hub, RLC-1240A (cropped, memory-card door), RLN16-410 (cropped recorder), RLC-81PA, RLC-840A; two RLC-1212A bullets were dropped because the parallel Brooklyn page used a near-identical shot). Each checked by sha256, dHash, ORB feature matching and correlation, plus visual side-by-side, against images/property-management-security/* (incl. parallel Brooklyn/Queens files present at build time, rechecked after they appeared), co-op-security-systems, condo-security-systems, co-op-security-camera-installation, condo-security-camera-installation, apartment-building-security-camera-installation. Captions say "partner product photo" and describe only what is visible. Lorex CDN and Luminys not reachable from the build env.


## Staten Island (property-management-security-staten-island) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Phone (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, `#brooklyn`) · start price $250 service call (START_PRICES). Other prices only as already published on Staten Island pages (listed below). Angle: house-based portfolios (two-family rentals), garden complexes, lots/driveways/detached garages, storm and flood placement of support gear, North Shore apartment buildings and Bay Street corridor; the MDL "three or more families" line decides which entry/TDPA rules reach a property.

HOLD-THIN test: passed. Staten Island rental stock is measurably different (MapPLUTO: 31,505 two-family lots vs 83 elevator lots), so the page is written around houses, lots and garages rather than lobbies. Kept apart from co-op-security-systems-staten-island (garden co-ops, Mitchell-Lama, shareholder issues), condo-security-systems-staten-island (townhouse HOAs, gates, pools) and apartment-building-security-camera-installation-staten-island (camera prices/coverage).

### Research matrix (format: exact query · platform · URL · finding · page + section used)
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| SIPM-1 | SODA `$select=bldgclass,count(*) as n,sum(unitsres) as u&$where=borough='SI' AND (starts_with(bldgclass,'B') OR starts_with(bldgclass,'C') OR starts_with(bldgclass,'D') OR starts_with(bldgclass,'S'))&$group=bldgclass` · NYC Open Data MapPLUTO (64uk-42ks) via Firecrawl scrape (raw JSON), Nov 27 2026 | https://data.cityofnewyork.us/resource/64uk-42ks.json (dataset https://data.cityofnewyork.us/City-Government/Primary-Land-Use-Tax-Lot-Output-PLUTO-/64uk-42ks) | Two-family B1/B2/B3/B9 = 1,512+20,141+2,879+6,973 = 31,505 lots, 63,010 units; C0 three-family 873 lots/2,619 u; C2 131/733 + C3 400/1,600 = 531 lots/2,333 u; C9 garden apartments 86/3,032; C1 125/1,927; C6 24/901; C7 25/333; elevator D0–D9 = 83 lots/13,585 u (avg ~164); mixed-use S0–S9 = 1,267 lots/2,237 u. | §5 para 1, facts list |
| SIPM-2 | `NYC Department of Finance building classification codes C0 three families C9 garden apartments B2 two family` · Firecrawl search (excerpt) | https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html | DOF codes: B two-family dwellings; C0 three families; C9 garden apartments (class definitions for SIPM-1). | §5 facts list |
| SIPM-3 | `New York Multiple Dwelling Law section 4 definition "multiple dwelling" three or more families living independently` · Firecrawl search (excerpt) | https://www.nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf | MDL §4(7): multiple dwelling = "occupied as the residence or home of three or more families living independently of each other". | §5 para 3 (quote); Rented Houses para 5; Q&A 1; AI check #1 |
| SIPM-4 | `HPD property registration one- and two-family homes owner does not reside required register` · Firecrawl search (excerpts) | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/abcs-of-housing-owners.pdf ; https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page | Registration annually for 3+ unit buildings and 1–2 family homes if neither owner nor owner's immediate family resides there. | §5 para 3; facts list; Q&A 1 |
| SIPM-5 | `silive Staten Island car break-ins thefts driveways garages 2025 police precinct` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.silive.com/crime-safety/2026/07/staten-island-car-thefts-spike-47-in-2026-heres-what-law-enforcement-is-doing-about-it.html | SILive, Maura Grunlund, July 24 2026: thefts up ~47%, "163 incidents this year through July 19 compared to 111 incidents during the same time period last year" (NYPD CompStat); up 65% over prior four weeks; slowing July 13–19. | Lots & Garages para 1 (quote); Q&A "car thefts" |
| SIPM-6 | `Staten Island buildings in floodplain number of buildings 100-year flood zone NYC Planning Resilient Neighborhoods East Shore` · Firecrawl search (excerpt; full PDF query failed) | https://www.nyc.gov/assets/em/downloads/pdf/hazard_mitigation/risklandscape2.0_2019_r2_digital_lowres.pdf | NYCEM Risk Landscape 2.0 excerpt: 1% annual chance floodplain includes 67,600 buildings (~175,000 residential units); high-risk areas concentrated on Staten Island's East Shore and parts of Brooklyn and Queens. | §5 facts list |
| SIPM-7 | reused co-op SI row SI-W1 | https://www.nad.usace.army.mil/Media/News-Releases/Article/3928401/seawall-will-raise-quality-of-life-for-shore-communities/ | "Sandy resulted in 24 deaths on Staten Island, more than any other borough"; "nearly 7,300 residential and commercial properties"; seawall Fort Wadsworth to Oakwood Beach. | Storms section para 1 (quotes); landmark card 6 |
| SIPM-8 | reused apartment-building camera SI row (City Limits) | https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ | Council approved Bay Street Corridor rezoning June 26 2019; ~20 blocks of the North Shore; ~1,800 new units incl. ~1,300 income-targeted; Stapleton and Tompkinsville. | North Shore para 1; landmark card 2 |
| SIPM-9 | reused silo S8 / co-op SI-H1 | https://data.cityofnewyork.us/Housing-Development/Housing-Maintenance-Code-Violations/wvxf-dwi5 | 2025 HPD violations mentioning intercom: Staten Island 24, Bronx 1,637. | §5 para 4 |
| SIPM-10 | reused silo S6 + Manhattan HPD TDPL row | https://intro.nyc/local-laws/2021-63 ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | TDPL: smart access in class A MDs; policy, consent, no sale, deletion deadlines, cannot require smart access for own unit. | Access Control para 3; Q&A rekeying |
| SIPM-11 | reused silo S7, S2, S9, S10, S11; co-op SI-G2 | MDL §50-a (nysenate); 28 RCNY §25-101 (amlegal); NYC BC §1010.1.9 (amlegal 0-0-0-173505); Admin Code §28-105.4.7; cooperatornews.com/article/qa-camera-placement; GBL §69-m (nysenate) | As recorded in silo/co-op rows. | Commercial compliance list; Alarms/cabling para 2; Occupied Rentals; AI check #7 |
| SIPM-12 | landmark geography (no counts beyond cited rows; no buildings named) | — | St. George Ferry Terminal; Bay Street/Stapleton/Tompkinsville; Forest Ave/Port Richmond; Staten Island Mall/Richmond Ave (Heartland Village, New Springville); New Dorp Lane/Hylan Blvd; Midland Beach/East Shore seawall. Commercial corridors: Bay St, Victory Blvd, Forest Ave, Richmond Ave, Hylan Blvd, New Dorp Lane, Richmond Rd. | §13 cards; §8 list |
| R1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG | — | EMPTY (not accessible in build env). AI Reality Check corrects claims typical of national guides and consumer marketing; no AI quote invented. | — |
| R2 | Hyperlocal beyond SILive (SI Advance print, Patch, News12 SI) | — | EMPTY (not searched separately) | — |

### Prices used (all already published on Staten Island pages)
- $250 service call — START_PRICES; /door-buzzer-repair-staten-island-new-york.
- Station $250–$525 · relay/button $250–$475 · transformer $325–$650 · strike with alignment $450–$950 · panel $650–$1,800 · riser $850–$2,400 — /door-buzzer-repair-staten-island-new-york.
- Building intercom 5–20 units $1,200–$4,500+ — /intercom-installation-staten-island-ny.
- Pedestrian gate keypad $1,500–$2,000 · combined vehicle + pedestrian gate $4,000–$7,000 — /access-control-installation-staten-island.
- Elevator Level 1 from $1,650/car, Level 2 from $2,750/car — /elevator-access-control-installation-staten-island.
- Four-camera installed from $999 — /security-camera-pricing-staten-island (A1).
- Cabling $150–$300 per drop — /structured-cabling-installation-staten-island.
- Monitoring $30/mo keypad, $45/mo app — /alarm-installation-staten-island.
- No maintenance-contract, package, per-unit or fire alarm prices. Not used: /intercom-repair-staten-island ranges (they differ from the buzzer repair page).

### Question register additions (property-management-security-staten-island)
Checked by meaning against the NYC, Manhattan, Brooklyn, Queens and Bronx PM registers above and the Staten Island co-op and condo question sets (avoided: one-app viewing, vacancy protection, parking-lot "what should cameras see", plate reading, recorder near the shore, salt air, weekend work, tenant calls, financing, vendor setup, COI, slope cameras, police footage, photos-only quotes, light-pole mounts, one fob for gate/pool). Parallel Long Island / Hudson Valley drafts were not on disk at build time — the main run should re-check.
- Q&A: Which entry rules apply to a two-family house, and which only begin at three apartments?
- Q&A: Once the owner moves out of a two-family and both floors are rented, what should change?
- Q&A: The basement apartment has its own side door. Should it get its own doorbell and camera?
- Q&A: Rekeying every time a tenant leaves one of our houses is getting expensive. What are the options?
- Q&A: Tenants keep putting up their own doorbell cameras on our houses. Should we allow it?
- Q&A: Does a camera aimed down a driveway shared with the neighbor's house cause problems?
- Q&A: Our complex has a row of detached garages with no power or internet. Can they be covered?
- Q&A: Car thefts are up on Staten Island this year. What can cameras on a rental lot really do?
- Q&A: Keypad codes or fobs: which suits a garden building with several small entrances?
- Q&A: Battery cameras on our frame houses keep dying in winter. Should they be wired instead?
- Q&A: We bought a building that came with the old owner's alarm still under contract. Can we take it over or replace it?
- Q&A: One of our North Shore buildings faces a busy sidewalk. Should the entry panel sit at the street or inside the vestibule?
- Q&A: We just took over management of a property from its owner. Which security items should be checked first?
- Q&A: Should each apartment in a two-family get its own alarm, or should the house share one?
- FAQ: Which office sends technicians to Staten Island properties?
- FAQ: Do you work for owners who manage one or two rental houses themselves?
- FAQ: Can you mount cameras and doorbells on vinyl or aluminum siding without causing leaks?
- FAQ: Do you work on houses that were raised after Hurricane Sandy?
- FAQ: Can our rental office's own door get a reader and a camera?
- FAQ: Can the owner see the outdoor cameras while each tenant sees only their own doorbell?
- FAQ: Can our houses have cameras without a monthly subscription?
- FAQ: A tenant cannot hear the doorbell from the top floor. Can a second chime or a light be added?
- FAQ: Will you come out for one doorbell or one camera at a single house?
- FAQ: Can you add lighting where our yards and lots are too dark for cameras?

### Images (11, permanent image rule — partner Reolink product photos; no unused real job photos, same finding as the Brooklyn/Queens/Bronx PM builds)
Pulled from reolink.com/us/product/* pages (home-cdn.reolink.us), flattened on white, WebP q80, max 1600px. Candidates checked by sha256 (none in the repo), ORB/RANSAC inliers and dHash against images/property-management-security/*, co-op-security-systems/*, condo-security-systems/*, co-op-security-camera-installation/*, condo-security-camera-installation/*, apartment-building-security-camera-installation/*, plus visual side-by-side. Rejected as already used there (inliers 128–700): RLC-520A dome, RLN8-410 kit, RLC-810A, RLC-820A, RLC-823S2 pendant, RLC-830A, RLC-833A; also dropped Video Doorbell 2nd Gen and Home Hub 2 (look-alikes of doorbell/hub shots on the Bronx/Brooklyn PM pages). Kept (max inliers ≤ 31):
| File (images/property-management-security/) | Source product | Where |
|---|---|---|
| …-staten-island-dual-lens-camera-under-dark-eave-over-lawn.webp | Omvi 3i PoE lifestyle | hero (eager), og/twitter |
| …-staten-island-black-battery-camera-front-view.webp | Argus 3 Pro | §5 |
| …-staten-island-battery-bullet-camera-with-spotlight.webp | Argus Eco Ultra (og:image) | Rented Houses |
| …-staten-island-white-pan-tilt-camera-with-antenna-and-spotlight.webp | Argus PT Ultra product (swapped from Omvi 3i product shot, which the parallel Hudson Valley page also used) | Intercoms |
| …-staten-island-compact-pan-tilt-camera-on-wall-bracket.webp | TrackFlex WiFi product | Access Control |
| …-staten-island-pan-tilt-camera-with-solar-panel-on-roof-edge.webp | Argus PT Ultra lifestyle | Lots & Garages |
| …-staten-island-pan-tilt-camera-under-eave-at-sunset.webp | TrackFlex WiFi lifestyle | Storms |
| …-staten-island-small-white-network-video-recorder.webp | RLN4E | Alarms & Infrastructure |
| …-staten-island-solar-pan-tilt-camera-on-white-side-wall.webp | Argus PT Ultra lifestyle | Building Specialists |
| …-staten-island-four-pan-tilt-cameras-with-recorder-and-cable-reels.webp | RLK8-800PT4 | Commercial |
| …-staten-island-bullet-camera-with-solar-panel-on-top.webp | Argus Solar | Seasonal checklist |
DAILY-LOG note: `images: 11 partner (Reolink) product photos via reolink.com (no unused real property-management photos)`.

### FLIPs on the page (plain text + comment)
/property-management-security-nassau-county, -suffolk-county, -westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county; /apartment-building-security-systems-staten-island. Direct links (built in parallel): /property-management-security-long-island, /property-management-security-hudson-valley.


## Long Island (property-management-security-long-island) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Hub page: Nassau + Suffolk · phone (800) 486-0943 only · GBP Brooklyn (`#brooklyn`, 1282 Troy Ave) · up-link / (Home) · start price $250 service call (START_PRICES). Thesis (kept apart from co-op LI = garden co-ops/board law, and condo LI = gatehouses/55+/HOA layering): horizontal rental portfolios — garden-apartment complexes with many entrances, LIRR station-area rentals, village mixed-use downtowns, small multifamily under town rental permits; distance (100 m cable limit, links between buildings), county alarm permits, town rental permits, ETPA in Nassau, NYC rules not applying.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| LIP1 | `Town of Islip rental permit requirements landlord rental property permit` · WebSearch → WebFetch | https://ecode360.com/11752170 | Town of Islip Code ch. 68 (added 5-22-2007): owner needs a rental occupancy permit; on-site inspection by Code Enforcement; permit valid two years, renewal filed 60 days ahead; CO alarm requirements (UL 2034). | §5 facts list; §7 small multifamily; Q&A rental-permit inspection; §8 permits |
| LIP2 | `Town of Brookhaven rental permit Chapter 76 rental dwelling permit requirements` · WebSearch → WebFetch | https://ecode360.com/8596302 | Brookhaven rental registration (sections numbered §82-x; chapter title not shown): registration before rental occupancy; inspection within 90 days of temporary registration by Chief Building Inspector or licensed engineer/architect/certified home inspector; smoke detector + CO alarms; valid 15 months. | same as LIP1 |
| LIP3 | `Nassau County rent guidelines board 2026 rent stabilized units Nassau ETPA villages number of apartments` · Firecrawl search (excerpt) | https://therealdeal.com/new-york/tristate/2026/06/25/nassau-rent-board-oks-modest-increases-for-regulated-units/ | "apply to the county's roughly 8,100 rent-stabilized units" (rates effective Oct. 1). Full article fetch failed (client_error); excerpt only. | §5 facts list |
| LIP4 | same search (excerpt) | https://hcr.ny.gov/rent-stabilization-and-emergency-tenant-protection-act | Municipalities adopt ETPA after a vacancy study of residential properties with six or more units built before Jan 1, 1974. | §5 facts list; §8 rent-stabilized H3; Q&A removed (overlap with HV) |
| LIP5 | `Long Island apartments near LIRR station transit-oriented development Mineola Farmingdale Patchogue units built Newsday` · Firecrawl search (excerpts) | https://www.newsday.com/real-estate/mineola-apartments-eden-blue-jse0fb11 | Jonathan LaMantia, Sept 23 2026: 172-unit Eden Blue, short walk from Mineola LIRR; "more than 1,100 rental units have opened since 2010 and approximately 1,000 more are planned" (Mayor Paul Pereira); developer Pergament quote "The model of Mineola will eventually grow in other villages and towns." | §5 para 3 (real quote), facts list, §13 Mineola card |
| LIP6 | same search | https://www.newsday.com/real-estate/baldwin-apartments-sunrise-highway-qcszqqes | LaMantia, Nov 23 2026: One Harrison, 215-unit building in Baldwin near the train station, construction started, opens mid-2028. (Building name NOT used.) | §5 para 3; §13 Baldwin card |
| LIP7 | same search | https://www.newsday.com/business/patchogue-carriage-house-luxury-apartments-wbz7wtrl | 262-unit development on West Main Street, Patchogue, half a mile from the train station. (Name NOT used.) | §5 para 3; §13 Patchogue card |
| LIP8 | `Suffolk County Police false alarm registration alarm permit fee Suffolk County code alarm systems` · Firecrawl search → Firecrawl scrape (directQuote) | https://suffolkpd.org/Precincts-and-Specialized-Units/Specialized-Units/Alarm-Management-Program ; https://ecode360.com/14943946 | Registration $50 residences / $100 commercial; registered locations get two false alarms without a service fee; unregistered charged from first; list of towns/villages not covered (e.g., all of Riverhead, Southampton, East Hampton, Southold, Shelter Island; villages incl. Northport, Amityville, Ocean Beach). Ch. 290: "No alarm owner shall operate an alarm system within the Suffolk County Police District without first obtaining a permit". | §5 facts; §6 alarm H3; Q&A alarm permit + false alarm; AI check #5; compliance list |
| LIP9 | `Nassau County police alarm permit false alarm ordinance registration fee commercial alarm Nassau County` · Firecrawl search (excerpts) | https://www.pdcn.org/343/Alarm-Permit-Section-Communication-Burea ; https://alarm.pdcn.org/applynewpermit.aspx | Residence $100, business $200, valid two years; "The Nassau County Police are requested to respond to over 125,000 false alarms each year." | same as LIP8 |
| LIP10 | `Census QuickFacts Nassau County Suffolk County owner-occupied housing unit rate 2020-2024 renter` · Firecrawl search (excerpts) | https://www.census.gov/quickfacts/nassaucountynewyork ; http://censusreporter.org/profiles/31400US3562035004-nassau-county-suffolk-county-ny-metro-division/ | Nassau owner-occupied housing unit rate 2020–2024: 81.9%; Nassau–Suffolk metro division owner occupied 82%. (Suffolk alone not retrieved.) | §5 para 2; facts list |
| LIP11 | `Nassau County 64 incorporated villages two cities three towns; Suffolk County ten towns villages number` · Firecrawl search (excerpts) | https://www.nassaucountyny.gov/3406/Cities-Towns-Villages ; https://en.wikipedia.org/wiki/Nassau_County,_New_York | "Nassau County there are 2 cities, 3 towns, 64 incorporated villages"; Suffolk's ten towns listed (Babylon … Southold). Suffolk village count not sourced → page says "its own villages" only. | §5 para 4; facts list |
| LIP12 | Firecrawl scrape (PDF, directQuote) | https://ag.ny.gov/sites/default/files/tenants_rights.pdf | AG tenants' rights guide summarizes MDL §50-a (intercom 8+ apts post-1968; pre-1968 on majority request); warranty of habitability RPL §235-b. | AI check #1 |
| LIP13 | reused co-op LI rows LI8/LI8b/LI9a (verified there) | https://newyork.public.law/laws/n.y._multiple_residence_law_section_3 ; nysenate MDL §3/§50-a ; https://dos.ny.gov/legal-memorandum-lg03-nys-uniform-fire-prevention-and-building-code-what-elected-officials-need | MRL applies to cities <325,000 and all towns/villages; MDL to cities 325,000+; no MRL intercom requirement found (page makes no such claim); DOS quote "automatically in effect in each city, town, and village in the State (except New York City)". | §5 para 5; §8 permits H3 (quote); compliance list; AI check #1 |
| LIP14 | reused silo S2, S6, S11, S12 | 28 RCNY §25-101; intro.nyc LL63/2021; cooperatornews camera Q&A; HomeAdvisor intercom cost | City notice rule and TDPA are NYC-only (contrast); audio raises eavesdropping questions; HomeAdvisor normal range $1,200–$8,500. | §6 access; §8 occupied rentals; AI checks #2, #4; compliance list |
| LIP15 | repo: fire-alarm-installation-long-island-ny + memory rule (no Nassau FM number; Suffolk in scope) | /fire-alarm-installation-long-island-ny | Suffolk via local fire marshal review; Nassau not taken; no fire alarm prices. | §6 fire alarm H3; AI check #6; FAQ #1; compliance list |
| LIP16 | TIA-568 100 m channel limit (industry standard; also on site's cabling pages) | — | ~100 m (328 ft) between active devices. | §6 cabling H3; Q&A distance; FAQ none |
| R | Reddit r/longisland / PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG | — | EMPTY (not accessible in build env). Package-theft news search (Firecrawl news) returned nothing usable for LI apartment complexes → not used. AI Reality Check corrects claims typical of national cost guides (Angi/HomeAdvisor/Fixr named generically); no AI quote invented. | — |

### Prices used (all already on Long Island pages)
- $250 service call — START_PRICES; /door-buzzer-repair-long-island-ny, /intercom-installation-long-island-ny.
- Station $250–$525 · transformer $325–$650 · strike with alignment $450–$950 · lobby panel $650–$1,800 · riser $850–$2,400 — /door-buzzer-repair-long-island-ny.
- Multi-unit intercom $1,200–$4,500+ — /intercom-installation-long-island-ny.
- Single-door reader + strike $1,500–$2,500 installed; gate with vehicle reader + barrier arm $3,500–$12,000 installed — /access-control-installation-long-island.
- Elevator Level 1 from $1,725/car Nassau, $1,800 Suffolk; Level 2 $2,875 / $3,000 — /elevator-access-control-installation-long-island.
- Four-camera from $999 Nassau, $1,099 Suffolk — /security-camera-pricing-long-island.
- Cabling $150–$300 per drop — /structured-cabling-installation-long-island.
- Monitoring $30/mo keypad, $45/mo app; small-business alarm from $1,500 — /alarm-installation-long-island.
- NOT used: /intercom-repair-long-island ranges (differ from the buzzer page). No maintenance-contract, package, per-unit or fire alarm prices.

### Question register additions (property-management-security-long-island)
Checked by meaning against NYC, Manhattan, Brooklyn, Queens, Bronx registers above, and the parallel Staten Island and Hudson Valley pages on disk at check time (dropped/replaced for overlap: vendor split by county vs HV multi-county proposal; far-corner lot camera vs HV lot far from power; garden doors opening outdoors vs HV townhouse doorbell-vs-shared-entry; Nassau ETPA entry change vs HV ETPA lobby upgrade; keypad locks vs SI rekeying; tenant doorbell vs SI/HV tenant doorbells; lighting FAQ vs SI/HV lighting; detached outbuildings FAQ vs SI detached garages; national alarm takeover FAQ vs SI old owner's alarm). Also checked against co-op LI and condo LI question sets.
- Q&A: Why do camera quotes for our Suffolk properties come out higher than for the Nassau ones?
- Q&A: Can you survey a property's security systems before our client closes on the purchase?
- Q&A: The town is inspecting one of our rentals for its rental permit. Does the security equipment come into it?
- Q&A: Which of our Long Island buildings need an alarm permit, and whose name goes on it?
- Q&A: Who pays when the police bill a false alarm at a building we manage?
- Q&A: How far apart can two buildings be before a camera or intercom cable cannot run between them?
- Q&A: What happens to the old buzzer wiring once a garden building moves to phone-based entry?
- Q&A: Can the basement laundry room in each garden building be limited to that building's tenants?
- Q&A: When a vacant apartment is found damaged, can the system show who went into that building?
- Q&A: What should be working before the first tenants move into a new building near the train station?
- FAQ: Can you take on fire alarm work for the buildings we manage in Nassau County?
- FAQ: Do you set up entry systems for senior rental communities on Long Island?
- FAQ: Do you work in student rentals near campuses such as Stony Brook and Hofstra?
- FAQ: Can you price a complex from the site plan without walking it?
- FAQ: Will you work alongside the locksmith our properties already use?
- FAQ: Is there a volume discount for bringing all of our Long Island properties to you?
- FAQ: What happens when a panel or reader for one of our properties has to be special-ordered?
- FAQ: Will you give our owner's insurance carrier a description of the security systems at a property?

### Similarity
Masked paragraph similarity (difflib, p/li/h3/td ≥12 words, top-5 Jaccard candidates; proof strip, form thank-you and mandated terms sentence excluded): max 0.637 (HV), 0.613 (NYC), 0.608 (co-op LI), 0.571 (Manhattan), 0.566 (condo LI), 0.545 (Queens), 0.538 (apartment-camera LI), 0.529 (SI), 0.521 (Bronx), 0.500 (Brooklyn).

### Images (11, permanent image rule; no Drive/CompanyCam check in this run)
Library scan: dHash grouping over 11,002 library images; ORB/RANSAC + dHash vs images/property-management-security/* (incl. parallel SI/HV files), co-op-security-systems, condo-security-systems, co-op-security-camera-installation, condo-security-camera-installation, apartment-building-security-camera-installation. Only one unused real job photo found that is not AI-looking or a tiny crop (grey door); the others either matched those folders or looked AI-generated (cat6/staff sets, brick-wall conduit boxes) and were rejected. 10 Reolink (authorized partner) product photos pulled from reolink.com product pages (home-cdn.reolink.us), each with no match (ORB inliers ≤17, sha256 unique). A PTZ speed-dome shot was dropped after it matched condo-security-camera-installation-queens (same product angle) and replaced.
| File (images/property-management-security/property-management-security-long-island-…) | Source | Where |
|---|---|---|
| floodlight-pan-tilt-camera-under-eave-at-dusk (hero, og/twitter) | reolink.com/us/product/trackflex-floodlight-wifi/ gallery | hero |
| grey-steel-door-at-end-of-tiled-hall | library job photo images/alarm-installation/alarm-installation-fort-hamilton-grey-door-at-end-of-tiled-passage.webp | §5 |
| dome-camera-with-mounting-screw-and-cable-tab | reolink rlc-520a page (home-cdn, 900x500) | §6 |
| wifi-bullet-camera-with-antennas-on-blue-siding | reolink rlc-811wa page | §7 |
| wifi-dome-camera-with-antennas-on-dark-ceiling | reolink rlc-840wa page | §9 |
| eight-port-poe-switch-with-power-labels | reolink rla-ps1 page | §10 |
| fisheye-ceiling-camera-front-view | reolink fe-w page | §10 |
| floodlight-camera-and-open-mounting-box-on-clapboard | reolink trackflex-floodlight-wifi page | §12 |
| floodlight-camera-on-siding-in-rain | reolink trackflex-floodlight-wifi page | §13 |
| two-pan-tilt-cameras-with-size-markings | reolink rlc-830a page | §15 |
| fisheye-camera-side-view-with-numbered-parts | reolink fe-w page | §19 |
DAILY-LOG note: `images: 10 partner (Reolink) product photos via reolink.com + 1 reused library job photo (no unused real property-management photos)`.

### Links
- Linked once each: /property-management-security-nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -hudson-valley (all in §19); /co-op-security-systems-long-island, /condo-security-systems-long-island, /apartment-building-security-camera-installation-long-island, /co-op-security-camera-installation-long-island, /condo-security-camera-installation-long-island, /co-op-board-intercom-upgrade, /condo-intercom-replacement; LI service pages: /intercom-installation-long-island-ny, /intercom-repair-long-island, /door-buzzer-repair-long-island-ny, /door-buzzer-installation-long-island-ny, /access-control-installation-long-island, /elevator-access-control-installation-long-island, /apartment-building-security-camera-installation-long-island, /commercial-security-camera-installation-long-island, /security-camera-pricing-long-island, /structured-cabling-installation-long-island, /alarm-installation-long-island, /fire-alarm-installation-long-island-ny, /smart-lock-installation-long-island, /cctv-installation-long-island, /security-cameras-long-island, /warranty, /free-quote, /.
- FLIP (plain text + comment, §19): /property-management-security-nassau-county, /property-management-security-suffolk-county, /apartment-building-security-systems-long-island.
- Link backs needed (main run): NYC hub + Manhattan, Brooklyn, Queens, Bronx PM pages (their FLIP comments for -long-island); per keyword rules one contextual link back from /intercom-installation-long-island-ny and /apartment-building-security-camera-installation-long-island.

### Mobile
Rendered at 390×844 with Playwright (local http.server): scrollWidth 390, no element past the viewport.


## Hudson Valley (property-management-security-hudson-valley) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Hub page: up-link /, phone (800) 486-0943 only, GBP Bronx (460 E Fordham Rd, `#bronx`), start price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (distinct from the city PM pages and the HV co-op/condo hubs): a management firm's HV list mixes downtown Westchester towers, village walk-ups, garden complexes, townhouse rentals and HOA contracts; distance/routing, grounds/lots far from power, weather (freeze, storms, outages) and suburban rules (MRL, PMCNYS, RPL 235-b, ETPA, county licensing) drive the work.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| PV1 | `Westchester County rental housing multifamily new apartments downtown White Plains Yonkers New Rochelle units built 2024 2025 report` · WebSearch → WebFetch | https://thebcw.org/wp-content/uploads/2025/01/Westchester_Development_2024.pdf | RM Friedland report (via Business Council of Westchester): ~12,500 residential units delivered since late 2021, ~15,000 under construction; Yonkers, New Rochelle, White Plains, Mount Vernon delivered 9,413 units, 13,114 more under construction | §5 para 3; hero stamp |
| PV2 | `Emergency Tenant Protection Act municipalities Westchester Yonkers New Rochelle Mount Vernon White Plains Kingston rent stabilization HCR` · WebSearch → WebFetch | https://homes.westchestercountyny.gov/rent-control | 18 ETPA municipalities: Croton, Dobbs Ferry, Eastchester, Greenburgh, Harrison, Hastings, Irvington, Larchmont, Mamaroneck Town, Mount Kisco, Mount Vernon, New Rochelle, Pleasantville, Port Chester, Sleepy Hollow, Tarrytown, White Plains, Yonkers | facts list; building types (ETPA); rules list; Q&A ETPA |
| PV3 | same search · WebFetch | https://hcr.ny.gov/city-of-kingston-adopts-etpa | Kingston adopted ETPA July 28, 2022; buildings of six or more units built before Jan 1, 1974 | facts list; building types; county table (Ulster) |
| PV4 | `Property Maintenance Code of New York State "304.18" building security doors deadbolt dwelling units` · Firecrawl search (excerpt) | https://codes.iccsafe.org/content/NYSPMC2025P1/chapter-3-general-requirements (also dos.ny.gov 2020 PMCNYS PDF) | 2025 PMCNYS §304.18: doors, windows, hatchways "shall be provided with devices designed to provide security for the occupants and property within"; §304.18.1 deadbolts on rented units openable from egress side without key, min 1-inch throw, sliding bolt not acceptable | facts list; rules list; Q&A deadbolt (locksmith) |
| PV5 | WebFetch | https://www.nysenate.gov/legislation/laws/RPP/235-B | RPL §235-b warranty of habitability (premises and areas used in connection fit for habitation, no conditions dangerous to life, health or safety) | facts list; rules list |
| PV6 | `Orange & Rockland Utilities storm outages customers restored 2026 Rockland Orange County` · WebSearch → WebFetch | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k | July 6 2026: >47,000 customers impacted since July 1 by extreme heat, thunderstorms, heavy rain; >45,000 restored (no lightning mention — page says "storms", not lightning) | facts list |
| PV7 | WebFetch | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 applies to "all cities of less than three hundred twenty-five thousand population" and all towns/villages | §5 para 4; facts list; rules; AI check #1 |
| R1 | reused, research/co-op-security-systems.md HV9 | census.gov / osc.ny.gov | Yonkers 2020 Census 211,569 | facts list |
| R2 | reused, condo H4 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 26 2026: >19,000 out after nor'easter | facts list |
| R3 | reused, co-op HV10 | https://www.coned.com/en/about-us/media-center/news/2026/06-06/con-edison-restoring-power--to-customers-affected-by-storm | June 2026: >5,000 Westchester customers out | facts list |
| R4 | reused, co-op HV11 | https://dailyvoice.com/article/packages-stolen-from-apartment-complex-found-inside-haverstraw-home-man-35-charged-cops-say/ | Apr 2026 Haverstraw complex package thefts recovered via search warrant (no names used) | facts list |
| R5 | reused, co-op HV12/HV13/HV14/HV15 | Westchester Consumer Protection; Ch. 863; ecode360 Rockland Ch. 250; Cortlandt Ch. 113; GBL §69-m | trade licensing, alarm business licensing, 50 V electrical-contractor definition, Cortlandt alarm permit (>4 false alarms in 6 months), state alarm installer licensing | facts list; alarms section; rules; AI check #4 |
| R6 | reused, co-op HV16 | https://intro.nyc/local-laws/2021-63 | TDPA is NYC-only | §5 para 4; access control section; AI check #5 |
| R7 | reused, co-op L11 / silo S11 | cooperatornews.com/article/qa-camera-placement | audio recording / eavesdropping caution | privacy settings section |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-hudson-valley-ny, /intercom-installation-hudson-valley-ny, /access-control-installation-hudson-valley, /elevator-access-control-installation-hudson-valley, /security-camera-installation-hudson-valley-ny, /structured-cabling-installation-hudson-valley, /alarm-installation-hudson-valley | $250 service call; station $250–$525; transformer $325–$650; strike $450–$950; lobby panel $650–$1,800; riser $850–$2,400; multi-unit video intercom $1,200–$5,000; single door access from $1,500; elevator from $1,875/car (Westchester L1); 4-camera from $1,099; cabling $150–$300/drop; monitoring $30/$45 | hero quick answer; services; cost table; packages. No $195/hr, no same-day used. |
| E1 | Reddit / PAA / PASF / ATP / AI Overview / Yelp / Bing-DDG | — | EMPTY (not accessible in build env). AI check corrects common generic claims; no AI quote invented | — |
| E2 | codes.iccsafe.org direct WebFetch | — | blocked (permission prompt unanswered); PV4 text taken from Firecrawl search excerpt | — |

### Question register additions (property-management-security-hudson-valley)
Checked by meaning against the NYC/Manhattan/Brooklyn/Queens/Bronx registers, co-op-security-systems-hudson-valley and condo-security-systems-hudson-valley registers, and the finished Staten Island and Long Island PM pages (6 drafts swapped after comparing: tenant doorbell cameras, lighting, single-owner landlords, insurance write-ups, inspector records, solar in winter, winter takeover).
- Q&A: A garden complex has a dozen separate entrances and no lobby. Where should the first fob readers go?
- Q&A: Our townhouse rentals each have their own front door. Should every unit get a video doorbell, or should the complex share one entry system?
- Q&A: When should a camera go on a pole instead of a building wall?
- Q&A: A parking lot sits far from any building with power. How do you get a camera out there?
- Q&A: Our complex pool opens on Memorial Day weekend and closes after Labor Day. Can pool access turn on and off with the season?
- Q&A: After the utility restores power to a building, why do some cameras come back and others stay dark?
- Q&A: Older two-story garden buildings have intercom wire stapled along the outside. Can it be replaced or protected?
- Q&A: Can the coax cable from an old analog camera system be reused when the cameras are replaced?
- Q&A: Our Westchester building is rent-stabilized under the ETPA. Does that change how we plan a lobby upgrade?
- Q&A: How do you keep outdoor camera cable from being cut by landscaping crews and string trimmers?
- Q&A: The property maintenance code mentions deadbolts on apartment doors. Is that your work or a locksmith's?
- Q&A: Our new downtown rental opened with only some of the amenity doors on the fob system. Can the rest be added later?
- Q&A: Plowed snow buries the view from our entrance camera every winter. Where should it be mounted instead?
- Q&A: Our complex's maintenance garage holds tools, equipment and spare parts. What does it need?
- FAQ: Is a service call at a Hudson Valley property priced the same as one in the city?
- FAQ: Can one proposal cover properties in several different counties?
- FAQ: Does the town need to issue a permit before cameras or an intercom go in?
- FAQ: Do you install wireless links between buildings in winter, or wait for spring?
- FAQ: Do cellular cameras need a data plan, and who pays for it?
- FAQ: Can a camera be mounted on the utility company's pole in our parking lot?
- FAQ: Should camera and gate wiring go in while our parking lot is being repaved?
- FAQ: Do you also work for the HOAs and condominium boards our firm manages?
- FAQ: Can you replace an entry panel or call box that a snowplow knocked over?
- FAQ: Can a fob reader control the gate to a dog run, playground or tennis court?

### Images (11, permanent image rule — no unused real job photos; no Drive/CompanyCam check in this run)
All Reolink (authorized partner) manufacturer product photos from reolink.com product pages (home-cdn.reolink.us), converted to WebP into images/property-management-security/ with `-hudson-valley-`. Each checked by sha256 + dHash + ORB/RANSAC inliers against images/property-management-security/* (incl. Staten Island and Long Island files), co-op-security-systems, condo-security-systems, co-op-security-camera-installation, condo-security-camera-installation, apartment-building-security-camera-installation (max 31 inliers, no matches) plus visual contact sheet. Rejected as already used: Altas/solar PTZ on roof edge (taken by Staten Island), RLN36 front, under-eave domes/PTZ night shots, bullet beside modern house, dimension diagrams. No faces, house numbers, phone numbers or "AESS".
| File | Source page / image | Where |
|---|---|---|
| …-pan-tilt-camera-on-wall-bracket-facing-lawn | reolink-trackmix-wifi · shop/public/media/1795412044410-WW7t.png | hero (eager), og/twitter |
| …-bullet-camera-strapped-to-steel-pole | reolink-go-ultra · 2023/10/120339001697081940.2475.jpg.webp | §5 |
| …-black-video-doorbell-with-lit-ring-button | reolink-video-doorbell-2nd-gen · shop/public/media/1783332797431-JRQc.png | services (access) |
| …-cellular-bullet-camera-on-wall-mount | reolink-go-ultra · 2023/10/120322531697080973.6701.png | services (internet) |
| …-solar-dual-lens-pan-tilt-camera | omvi-2i-ultra · shop/public/media/1785754157480-VTJy.png | building types |
| …-white-local-storage-hub | home-hub-2 · shop/public/media/1789625125240-Tkkk.png | equipment |
| …-dual-lens-pan-tilt-camera-on-black | omvi-x16-poe · shop/public/media/1792579447051-kk1w.png (top line cropped) | equipment |
| …-white-corner-mounting-bracket | omvi-2i-ultra · shop/public/media/1791430239810-ZH5w.png | process |
| …-bullet-camera-with-red-light-beside-door-at-night | reolink-go-ultra · 2023/10/120339201697081960.6661.jpg.webp | coverage |
| …-doorbell-wire-leads-and-twist-connectors | reolink-video-doorbell-2nd-gen · 2024/04/290622171714371737.2276.png | cost |
| …-coiled-gray-network-cable | rlk8-800pt4 · 2022/07/290726281659079588.2987.png | all areas |
DAILY-LOG note: `images: 11 partner (Reolink) product photos via reolink.com (no unused real property-management photos)`.

### FLIPs on the page (plain text + `<!-- FLIP: /slug -->`)
/property-management-security-westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county (coverage cards); /apartment-building-security-systems-hudson-valley (coverage para). Linked directly: /property-management-security-nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island (one areas section).

### Links left for the main run
Back-links needed from the five live PM pages (+ SI, LI); keyword-file back-links from /intercom-installation-hudson-valley-ny and /apartment-building-security-camera-installation-hudson-valley at the main run's discretion.

### For Anwar to confirm
- "Crews head north each morning from the Bronx office" and routing visits by county.
- Wireless links in winter, conduit before repaving, snowplow-damaged call box replacement, amenity gate readers — written as services we do.
- 30-day labor warranty + one-year parts sentence side by side (matches site).
