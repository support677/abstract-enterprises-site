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


## Nassau County (property-management-security-nassau-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

County page · phone (516) 346-5778 (body, CTAs, schema; 800 only in shared header) · GBP Brooklyn (`#brooklyn`, 1282 Troy Ave) · up-link /property-management-security-long-island · start price $250 service call (START_PRICES). Thesis (kept apart from LI hub = horizontal two-county portfolios/distance/Suffolk permits; co-op and condo Nassau = boards): Nassau landlords and managing agents — 71 local governments, town rental permits (Hempstead, North Hempstead), ETPA municipalities, accessory units/two-families, village walk-ups over stores, garden complexes, station-area new buildings (Westbury/Lynbrook), shore-block rentals (Long Beach).

### Research matrix (exact query · platform · URL · finding · section used)
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| NP1 | `Town of Hempstead rental permit landlord registration law code chapter inspection` · Firecrawl search → Firecrawl scrape | https://hempsteadtown.com/buildingforms/RentalPropMobile.aspx (code: https://ecode360.com/32556484, https://ecode360.com/15511003) | TOH Code §99-12 rental occupancy; "Transient rentals, or property rented for a period of less than 28 days is not permitted"; permits two years, must be renewed; application fee $300 (applied to permit); single unit $500; multi-unit $500 first + $200 each additional; renewal $450 / $200; owners outside Nassau must designate a Nassau-resident agent for service; §99-15 compliance with Town, county, state law. | §5 para 2 + facts list; §7 accessory units; §8 out-of-county owners + permit renewals + compliance list; Q&A permit renewal |
| NP2 | `Town of North Hempstead rental permit law landlords apartments inspection requirement` · Firecrawl search → Firecrawl scrape (directQuote) | https://ecode360.com/9294160 | Ch. 2 art. VI (L.L. 12-1996): on-site inspection by Code Enforcement Officer; "All permits issued pursuant to this article shall be valid for a period of two years"; "No permit shall be issued or renewed until the Code Enforcement Officer shall inspect the rental dwelling unit to determine that it is equipped with a functioning smoke detector device and carbon monoxide alarm". | §5 para 2 + facts list; §7 accessory units; §8 permit renewals |
| NP3 | same search (excerpt) | https://ecode360.com/9296656 | North Hempstead ch. 2 art. V: "Every occupant of a dwelling or dwelling unit shall give the owner thereof, or his agent or employee, access to any part of such dwelling … at all reasonable times for the purpose of making such repairs or alterations". | §8 occupied apartments; AI check #3 |
| NP4 | `Nassau County ETPA municipalities rent stabilization Glen Cove Long Beach Freeport villages opted in list` · Firecrawl search → Firecrawl scrape (directQuote) | https://hcr.ny.gov/office-rent-administration-ora | Nassau ETPA list: Cities of Glen Cove, Long Beach; Town of North Hempstead; Villages of Cedarhurst, Floral Park, Flower Hill, Freeport, Great Neck, Great Neck Plaza, Hempstead, Lynbrook, Mineola, Rockville Centre, Russell Gardens, Thomaston, Baxter Estates (13 villages). | §5 para 4; §7 ETPA H3; §13 landmark cards; AI check #5 |
| NP5 | same search (excerpt) | https://hcr.ny.gov/2022-23-nassau-county-rgb-explanatory-statement | "As of April 1, 2021, NYS HCR's annual registration data indicates there were approximately 6,650 apartments registered as subject to the ETPA in Nassau County." | §5 para 4 + facts list; AI check #5 |
| NP6 | `Census QuickFacts Nassau County New York population 2024 housing units renter` · Firecrawl search (excerpts) | https://www.socialexplorer.com/places/new-york/nassau-county ; https://censusreporter.org/profiles/14000US36059407600-census-tract-4076-nassau-ny/ | Median gross rent $2,179 (±$120) (ACS via Social Explorer); Nassau County housing units 479,044 (Census Reporter comparison column). | §5 para 3 + facts list |
| NP7 | reused LI row LIP10 | https://www.census.gov/quickfacts/nassaucountynewyork | Owner-occupied housing unit rate 2020–2024: 81.9%. | §5 para 3 + facts list |
| NP8 | reused LI row LIP11 | https://www.nassaucountyny.gov/3406/Cities-Towns-Villages | 2 cities, 3 towns, 64 incorporated villages. | §5 heading + para 1 + facts list |
| NP9 | reused LI row LIP9 | https://www.pdcn.org/343/Alarm-Permit-Section-Communication-Burea | Nassau police alarm permit $100 residence / $200 business, two years; "over 125,000 false alarms each year". | §5 facts list; §6 alarm H3; compliance list |
| NP10 | `Newsday 2026 Nassau apartments rental units downtown Westbury Hicksville Freeport Lynbrook new building near LIRR` · Firecrawl search (excerpts) | https://www.newsday.com/real-estate/westbury-apartments-yhixmu5g | MTA board approved lease for 184 apartments on a long-closed commuter lot by Westbury station; five-story building; "one of several new apartment buildings planned for the area around the Westbury train station". (Building names NOT used on page.) | §5 para 5; §13 Westbury card |
| NP11 | same search (excerpt) | https://www.newsday.com/real-estate/baldwin-apartments-sunrise-highway-qcszqqes | A recently opened apartment building across from the Lynbrook station "is nearly fully occupied after leasing faster than the company expected." (Name NOT used.) | §5 para 5; §13 Lynbrook card |
| NP12 | same search (Facebook/Instagram excerpts of a Newsday post) | https://www.facebook.com/newsday/posts/a-new-apartment-complex-in-hicksville-where-tenants-can-walk-out-their-door-to-c/1577427531095157/ | 189-unit building opened near Hicksville LIRR station. Social-post excerpt only → used only as "new buildings near Hicksville station" in building-type cards, no number on page. | §7 card + H3 heading |
| NP13 | reused LI row LIP13 + silo S7 | https://www.nysenate.gov/legislation/laws/MDW/50-A ; https://dos.ny.gov/legal-memorandum-lg03-nys-uniform-fire-prevention-and-building-code-what-elected-officials-need | MDL §50-a intercom/self-locking doors (8+ apts); MDL §3 applies to cities ≥325,000; MRL for smaller cities, towns, villages; DOS quote "automatically in effect in each city, town, and village in the State (except New York City)". | §8 compliance list; AI check #1 |
| NP14 | reused silo S2, S11, S12 | 28 RCNY §25-101; cooperatornews camera Q&A; HomeAdvisor intercom cost | NYC notice rule is city-only (contrast); audio may implicate Penal Law §250; HomeAdvisor normal range $1,200–$8,500. | §8 occupied apartments; privacy H3; compliance list; AI checks #3, #4 |
| NP15 | memory rule (no Nassau FM number) + repo | — | We do not take Nassau fire alarm work; door-release coordination with fire alarm company of record only. No fire alarm link/price. | §6 fire alarm H3; AI check #6 |
| R | Reddit r/longisland, r/landlord / PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG for "property management security Nassau County" | — | EMPTY (not accessible in build env). No Reddit thread or AI Overview quoted; AI Reality Check corrects claims typical of national cost guides and chatbot answers. | — |

### Prices used (all already on Nassau pages)
- $250 service call — START_PRICES; /door-buzzer-repair-nassau-county-new-york.
- Station $250–$525 · transformer $325–$650 · strike with alignment $450–$950 · lobby panel $650–$1,800 · riser $850–$2,400 — /door-buzzer-repair-nassau-county-new-york.
- Multi-unit intercom $1,200–$4,500+ — /intercom-installation-nassau-county-new-york.
- Networked card reader, single door $1,500–$3,500 — /access-control-installation-nassau-county.
- Single-door keypad or card reader with electric strike $1,725–$2,875 installed — /smart-lock-installation-nassau-county.
- Elevator Level 1 from $1,725/car; Level 2 from $2,875/car — /elevator-access-control-installation-nassau-county.
- Four-camera from $999 — /security-camera-pricing-nassau-county.
- Cabling $150–$300 per drop — /structured-cabling-installation-nassau-county.
- Monitoring $30/mo keypad, $45/mo app — /alarm-installation-nassau-county.
- NOT used: /intercom-repair-nassau-county ranges (differ from buzzer page); alarm package prices; no maintenance-contract, per-unit, package or fire alarm prices. No "free" assessment/walk wording (task rule).

### Question register additions (property-management-security-nassau-county)
Checked by meaning against the NYC, Manhattan, Brooklyn, Queens, Bronx, Staten Island, Long Island and Hudson Valley registers and the Westchester/Suffolk pages on disk at check time; checker found no masked duplicates.
- Q&A: Our Town of Hempstead rental permit renews next month. Should security work wait until after the inspection?
- Q&A: An owner who lives out of state wants to approve every dollar. How do you write a scope for someone who has never seen the building?
- Q&A: Tenants in an ETPA building may see phone-based entry as a cut in service. How do you plan the change?
- Q&A: Which lock can go on a basement apartment door that is also the tenant's only way out?
- Q&A: In a walk-up over stores, the buzzer wire shares a chase with the shops' lines. Can you sort out which pair goes to which apartment?
- Q&A: Which accounts and documents should we collect from a developer's installer before they leave a new building?
- Q&A: Can tenants send a one-time entry code to a guest who arrives before they get home?
- Q&A: After a storm floods a Long Beach basement, what should be checked before the entry system is powered again?
- Q&A: Is a stainless entry panel worth the extra cost on a building a few blocks from the ocean?
- Q&A: Can a tenant be locked out of the gym or roof deck while still getting into their own apartment?
- FAQ: Which phone number should our Nassau office use for service requests?
- FAQ: Do you work in the cities of Long Beach and Glen Cove as well as the three towns?
- FAQ: Does a village design review board have to approve a new entry panel on the front of a building?
- FAQ: Can you install a call box at the entrance to a private driveway shared by several rental houses?
- FAQ: Does a cloud intercom keep working when the building's internet service goes down?
- FAQ: Can the managing agent approve the work, or does the owner have to sign?
- FAQ: Can one entry panel serve two neighboring buildings that belong to the same landlord?
- FAQ: When a basement apartment is legalized, can it be added to the existing intercom?

### Similarity
Masked paragraph similarity (difflib, p/li/h3/td ≥12 words after the mega nav, top-5 Jaccard candidates; proof strip, consent, stamp and mandated terms sentence excluded) vs every property-management-security-* page on disk (incl. parallel Westchester and Suffolk) + co-op/condo security systems Nassau + apartment-building camera Nassau: every paragraph < 0.60 after rewrites (initial build mirrored LI hub wording in ~20 short items; all rewritten).

### Images (11)
Hero = real job photo supplied for this page; 6 library job photos, 1 Lorex and 3 Reolink partner images (fetched with curl from reolink.com product pages, `rlc-1212a` and `rlc-81ma`), none used on any other property-management-security page (dHash vs the 96 existing files + visual contact sheets). Five first-pick library photos were swapped out after a visual check showed the parallel Suffolk page used the same shots (cornice arm, two-story wall bullet, drop-ceiling bullet, glass-entrance dome, rack + monitor).
| File (images/property-management-security/property-management-security-nassau-county-…) | Source | Where |
|---|---|---|
| job-photo-four-bay-recorder-on-closet-shelf (hero, og/twitter, eager) | /tmp/pi2/photos/rec9ERhLmpAQMifWJ_0.jpg → WebP q80, 1024×768 | hero |
| dome-camera-under-roof-fascia-against-winter-sky | images/access-control-installation/…kingsbridge-heights-dome-camera-under-fascia-against-winter-sky.webp | §5 |
| reolink-bullet-camera-on-white-wall-in-rain | Reolink (authorized partner) product photo, https://reolink.com/us/product/rlc-81ma/ (home-cdn.reolink.us/wp-content/uploads/2025/08/040927221754299642.1415.jpg.webp) | §6 |
| dome-camera-in-ceiling-corner-beside-flag | images/access-control-installation/…harding-park-white-dome-camera-in-corner-beside-star-pattern-fabric.webp | §7 |
| small-camera-above-lit-lobby-soffit | images/access-control-installation/…kingsbridge-heights-mini-camera-above-lit-lobby-soffit.webp | §9 Q&A |
| reolink-night-view-of-lit-yard-and-path | Reolink sample night image, https://reolink.com/us/product/rlc-1212a/ (home-cdn.reolink.us/wp-content/uploads/2025/05/160929541747387794.8768.png) | §10 equipment |
| reolink-dual-light-bullet-camera-on-concrete-wall | Reolink product photo, https://reolink.com/us/product/rlc-81ma/ (home-cdn.reolink.us/wp-content/uploads/2025/08/040853281754297608.0075.jpg.webp) | §10 equipment |
| night-camera-view-of-open-back-door | images/access-control-installation/…kingsbridge-heights-night-camera-view-of-open-back-door.webp | process |
| camera-view-of-brick-walk-and-gravel-lot | images/access-control-installation/…kingsbridge-heights-wide-camera-view-of-brick-walk-and-lot.webp | coverage |
| lorex-twin-floodlight-camera-with-lamps-lit | images/access-control-installation/…indian-village-twin-floodlight-camera-with-lights-on.webp (Lorex manufacturer photo, partner) | packages |
| two-small-cameras-on-tall-wall-below-mezzanine-windows | images/access-control-installation/…dumbo-two-small-cameras-on-tall-wall-below-mezzanine-windows.webp | FAQ |
DAILY-LOG note: `images: 1 real job photo (hero) + 6 reused library job photos (access-control-installation) + 1 Lorex + 3 Reolink partner images`.

### Links
- Up: /property-management-security-long-island (breadcrumb + body). Siblings linked: -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -hudson-valley, -long-island, and the parallel -westchester-county and -suffolk-county (files existed on disk at check time; checker required the cross-link).
- FLIP comments (plain text): /property-management-security-rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county.
- Nassau pages linked once: /co-op-security-systems-nassau-county, /condo-security-systems-nassau-county, /door-buzzer-repair-nassau-county-new-york, /intercom-installation-nassau-county-new-york, /intercom-repair-nassau-county, /door-buzzer-installation-nassau-county-ny, /access-control-installation-nassau-county, /elevator-access-control-installation-nassau-county, /smart-lock-installation-nassau-county, /apartment-building-security-camera-installation-nassau-county, /security-camera-pricing-nassau-county, /co-op-security-camera-installation-nassau-county, /condo-security-camera-installation-nassau-county, /parking-lot-camera-installation-nassau-county, /alarm-installation-nassau-county, /structured-cabling-installation-nassau-county, /commercial-security-camera-installation-nassau-county, /security-cameras-nassau-county, /cctv-installation-nassau-county; plus /co-op-board-intercom-upgrade, /condo-intercom-replacement, /warranty, /free-quote, /.
- Not linked: /fire-alarm-installation-nassau-county-ny (we don't take Nassau fire alarm work).
- Link backs needed (main run): every live PM sibling (checker), parent hub LI (flip its FLIP comment), and per keyword rules one contextual link back from /intercom-installation-nassau-county-new-york and /apartment-building-security-camera-installation-nassau-county.


## Suffolk County (property-management-security-suffolk-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Phone (631) 407-2884 · GBP Brooklyn (`#brooklyn`, 1282 Troy Ave) · up-link /property-management-security-long-island · start price $250 service call (START_PRICES). Thesis (kept apart from the LI hub and the parallel Nassau page): distance (86 miles end to end), East End seasonal rentals (weekly turnover, closed winters, caretakers/rental agents, East Hampton and Southampton registries/permits), outbuildings and long runs (pool houses, barns, docks, driveway gates), plus year-round garden complexes, Ronkonkoma station-area buildings and main-street mixed use. NYC rules (MDL 50-a, HPD, 28 RCNY 25-101, TDPA) stated as not applying.

### Research matrix (exact query · platform · URL · finding · section used)
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| SF1 | `Suffolk County land area square miles largest county New York State 86 miles long Montauk` · WebSearch → Firecrawl scrape (directQuote) | https://suffolkcountyny.gov/Elected-Officials/County-Executive/PgrID/2624/PageID/9 | "Suffolk County comprises 1000 square miles of eastern two-thirds of Long Island. The distance from the Nassau County border to Montauk Point is 86 miles. At Suffolk County's widest point the distance from Long Island Sound to the southern shore is 26 miles." | §Neighborhood para 1; facts list; "Scheduling across 86 miles" |
| SF2 | `Suffolk County New York QuickFacts owner-occupied housing unit rate 2020-2024 housing units` · WebSearch → Firecrawl scrape | https://fred.stlouisfed.org/data/HOWNRATEACS036103 | Homeownership Rate (5-year estimate) for Suffolk County, 2024-01-01: 84.884 (%). (census.gov QuickFacts returned 503 — EMPTY (not accessible in build env)) | §Neighborhood para 2; facts list |
| SF3 | `Suffolk County seasonal recreational occasional use housing units share East Hampton Southampton census` · WebSearch → Firecrawl scrape (PDF, directQuote) | https://southamptontownny.gov/DocumentCenter/View/26835/Southampton-Housing-Plan---Final-Oct-2022 | "Almost half of the housing units in Southampton are occupied on a seasonal basis." "The share of housing units that were known to be occupied by renters in Southampton in 2018 was 22.3%." | §Neighborhood para 3 (quote); facts list; landmark card South Fork |
| SF4 | `Town of East Hampton rental registry law requirements registration number listing` · WebSearch → Firecrawl scrape (directQuote) | https://ecode360.com/30841753 | Ch. 199 Rental Registry, adopted 12-17-2015 (L.L. 38-2015): unlawful to rent rental/seasonal rental property without registering with Building Dept and obtaining a registry number; form incl. notarized inspection checklist sworn by owner or licensed architect/engineer/home inspector; registration expires two years after deemed complete; failure to publish registry number: fine $150–$1,500 or up to 15 days. | facts list; Seasonal section "Rental registries"; compliance list; AI check #5 |
| SF5 | `Town of Southampton rental permit law short-term rental permit requirements inspection` · WebSearch → Firecrawl scrape (directQuote). (Rental FAQs PDF: Firecrawl proxy tunnel error — EMPTY (not accessible in build env)) | https://ecode360.com/8697312 | Ch. 270 Rental Properties: applies to rental properties in the unincorporated area of the Town; permits valid two years; enforcement authority makes on-site inspection unless owner provides certification from licensed architect or engineer (§270-5B(10)); valid rental permit is a condition precedent to collecting rent. | facts list; Seasonal section; compliance list |
| SF6 | `PSEG Long Island 2026 storm outages customers restored Suffolk` · WebSearch → Firecrawl scrape (directQuote) | https://www.psegliny.com/Newsroom/2025/070626-StormUpdate1000 | PSEG LI Storm Update, Monday July 6 (2026), 10 AM: restored power to more than 34,800 customers since 8 PM Saturday; 4,170 of 1.2 million customers still affected; storm gusts up to 84 MPH, hail, heavy rain. | §Neighborhood para 5 |
| SF7 | `Ronkonkoma Hub apartments units built Brookhaven transit-oriented development 2025 2026` · WebSearch → Firecrawl scrape (directQuote) | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Station Yards (Ronkonkoma Hub): 53 acres around Ronkonkoma LIRR station; 1,450 residential units at completion; first phase delivered 489 units in 2020; second phase (The Core) 388 homes; Ronkonkoma station is "Suffolk County's busiest". | §Neighborhood para 4; facts list (489+388 = 877); landmark card |
| SF8 | Firecrawl scrape (directQuote) | https://suffolkpd.org/Precincts-and-Specialized-Units/Specialized-Units/Alarm-Management-Program | Registration $50 residences / $100 commercial; registered locations get two occasions not assessed a service fee. Towns/villages outside the program (all of Riverhead, Southampton, East Hampton, Southold, Shelter Island; villages incl. Northport, Amityville, Ocean Beach) reused from LI row LIP8 (ecode360.com/14943946, ch. 290). | facts list; Alarms section; compliance list |
| SF9 | reused LI rows LIP1 (Islip ch. 68, ecode360.com/11752170) and LIP2 (Brookhaven rental registration, ecode360.com/8596302) | — | Islip rental occupancy permit after inspection, two years; Brookhaven registration 15 months, inspection within 90 days by town or licensed professional; smoke/CO focus. | Building Specialists (accessory units); compliance list; AI check #5 |
| SF10 | reused LI row LIP13 / silo S7 (MRL §3, MDL §50-a) and S6 (TDPA intro.nyc), S2 (28 RCNY §25-101), S11 (Cooperator audio Q&A) | nysenate MDL §50-a; newyork.public.law MRL §3; intro.nyc/local-laws/2021-63 | MDL covers cities ≥325,000; towns/villages under MRL; NYC notice + TDPA city-only; audio/eavesdropping caution. | §Neighborhood para 6; access control; occupied rentals; compliance list; AI checks #1, #5 |
| SF11 | LIP5/LIP7 reused (Newsday Patchogue 262-unit near station) | https://www.newsday.com/business/patchogue-carriage-house-luxury-apartments-wbz7wtrl | Station-area construction in Patchogue (used only as "station-area buildings near Ronkonkoma and Patchogue"). | Elevator section; landmark card Patchogue |
| SF12 | TIA-568 100 m channel limit (industry standard; also on site cabling pages; LI row LIP16) | — | ~100 m / 328 ft between active devices. | Cable section |
| R | Reddit r/longisland / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG | — | EMPTY (not accessible in build env). AI Reality Check corrects claims typical of national guides (Angi/HomeAdvisor/Fixr named generically); no AI quote invented. | — |

### Prices used (all already published on Suffolk pages)
- $250 service call — START_PRICES; /door-buzzer-repair-suffolk-county-new-york.
- Station $250–$525 · relay/button $250–$475 · transformer $325–$650 · strike with alignment $450–$950 · lobby panel $650–$1,800 · riser $850–$2,400 — /door-buzzer-repair-suffolk-county-new-york.
- House/small building intercom $400–$1,800 · multi-unit $1,200–$4,500+ — /intercom-installation-suffolk-county-new-york.
- Lobby fob reader $1,600–$2,800 · gate with RFID + video intercom $2,500–$5,500 · multi-door $4,500–$16,000 — /access-control-installation-suffolk-county.
- Elevator Level 1 from $1,800/car, Level 2 from $3,000/car — /elevator-access-control-installation-suffolk-county.
- Four-camera from $1,099 — /security-camera-pricing-suffolk-county (MODELS min).
- Cabling $150–$300 per drop — /structured-cabling-installation-suffolk-county.
- Small-business alarm $1,500–$3,000; monitoring $30/mo keypad, $45/mo app — /alarm-installation-suffolk-county.
- NOT used: /intercom-repair-suffolk-county ranges (inconsistent with buzzer page), the access-control page's "$195/hr callback" and "+10% surcharge" lines. No maintenance-contract, package, per-unit or fire alarm prices.

### Question register additions (property-management-security-suffolk-county)
Checked by meaning against NYC, Manhattan, Brooklyn, Queens, Bronx, Staten Island, Long Island, Hudson Valley registers above; `check_page.py` also compared against the parallel Nassau and Westchester drafts on disk (no duplicated question).
- Q&A: Which systems should be switched off, and which left running, when a summer rental closes for the winter?
- Q&A: How do weekly summer guests get in without anyone handing them a physical key?
- Q&A: Can the system show us when the cleaners finished at each house on changeover day?
- Q&A: How do we keep renters out of the owner's locked closet and storage areas during a stay?
- Q&A: Renters ask whether there are cameras at the house. What should the owner be ready to tell them?
- Q&A: A farmhouse rental on the North Fork has no cable internet. Can it still have cameras the owner can check from away?
- Q&A: A pool house, a barn and a detached studio sit behind the main house. Which of them really need cameras?
- Q&A: After a thunderstorm the driveway gate stopped opening. Is that a job for you or for the gate company?
- Q&A: Visitors at our garden complex near Ronkonkoma park far from the buildings. Where should the call box go?
- Q&A: A homeowners association inside our portfolio wants its own control over the gate codes. How do we split control?
- Q&A: A store on the ground floor of our Patchogue building stays open late. How do we keep the apartment stair door secure after hours?
- Q&A: Is battery backup worth paying for when most outages here are fixed within a day?
- Q&A: Which equipment fails first in buildings near the water, and what do you put in instead?
- FAQ: Which phone number should our Suffolk office use for every property?
- FAQ: Do you cover properties on both forks and out to Montauk?
- FAQ: Can a caretaker meet the technician instead of someone from our office?
- FAQ: Can the alarm at a closed-up house alert both the owner and our office?
- FAQ: Can renters switch off the outdoor cameras during their stay?
- FAQ: Do you install cameras that cover a dock or a boathouse?
- FAQ: Do you take on installs at East End rentals in July and August?
- FAQ: Do you work for owners who list their houses with a rental agent rather than a management company?
- FAQ: Can a keypad control a gate to a private beach path or a shared dock?
- FAQ: Is the service call priced differently for a house on the East End?

### Similarity
Masked paragraph similarity (difflib, p/li/h3/td/figcaption ≥12 words, Jaccard prefilter; terms sentence, consent and form text excluded): max 0.621 (apartment-camera Suffolk, Station Yards fact line), 0.605 (LI hub), everything else ≤0.56 except the shared template proof strip ("Owner-operated since 2002 · …", identical sitewide). Fifteen draft paragraphs that were ≥0.65 vs LI hub / parallel Nassau / Westchester were rewritten.

### Images (11)
- Hero (eager, og/twitter): real job photo /tmp/pi2/photos/rec3xI4CkGmeninlV_0.jpg (Airtable photo meta: "Equipment rack with TP-Link 24-port gigabit switch above a black NVR and cables") → `…-suffolk-county-job-photo-24-port-switch-above-network-video-recorder.webp` (867×1156).
- 2 real job photos reused from images/cctv-installation/: cctv-installation-suffolk-county-storage-dome-high-in-wall-corner.webp → `…-dome-camera-high-in-stained-storage-room-corner.webp`; cctv-installation-suffolk-county-wall-camera-on-bare-stucco-wall.webp → `…-small-camera-on-bare-stucco-wall.webp`.
- 8 Reolink (authorized partner) product photos via Firecrawl image lists of reolink.com/us/product/reolink-trackmix-poe/, /rln8-410/, /reolink-duo-3-poe/ (home-cdn.reolink.us): `…-partner-photo-daytime-camera-view-of-palms-and-low-wall`, `…-recorder-with-continuous-recording-graphic`, `…-pan-tilt-camera-with-split-sample-views`, `…-camera-view-of-garden-path-and-greenhouse`, `…-two-white-storage-hubs`, `…-smart-display-showing-camera-view-of-lawn`, `…-recorder-with-16tb-storage-graphic`, `…-house-and-pool-behind-16mp-graphic`.
- Collision note: 8 real job photos first chosen (intercom-repair SI/Putnam + cctv Suffolk scenes) turned out to be picked at the same time by the parallel Westchester and Nassau PM builders, so they were dropped and replaced by the partner photos above. Final check: ORB/RANSAC inliers vs every other file in images/property-management-security/ ≤ 37 (16TB recorder vs Westchester recorder-on-pedestal, different shot), others ≤ 26; ORB vs co-op/condo/co-op-camera/condo-camera/apartment-camera folders ≤ 36 for the 8 partner photos.
DAILY-LOG note: `images: 1 real job photo hero + 2 reused cctv-installation job photos + 8 partner (Reolink) product photos via reolink.com`.

### FLIPs on the page (plain text + comment)
/property-management-security-nassau-county; /property-management-security-westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county. Direct links: LI hub (up), nyc, manhattan, brooklyn, queens, bronx, staten-island, hudson-valley.

### For Anwar to confirm (CONFIRM)
- Coverage out to Montauk and Orient; ferry-only properties (Shelter Island, Fishers Island) "scheduled case by case".
- Seasonal-house services written as things we do: per-booking keypad codes set up for the office, opening (spring) and closing (fall) visits, temperature/water sensors on the alarm panel, cellular routers/cameras where no internet, wireless bridges to outbuildings, dock/boathouse cameras.
- "In summer we avoid putting technicians on the roads east of the canal at peak traffic hours" (scheduling practice).
- Fire alarm: page says only that fire alarm is a separate trade "this page does not cover" (per build instruction); the LI hub still says Suffolk fire alarm work is taken.


## Westchester County (property-management-security-westchester-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page: up-link /property-management-security-hudson-valley, phone (914) 877-2578 (body, CTAs, schema; 800 only in shared header), GBP Bronx (460 E Fordham Rd, `#bronx`), start price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (distinct from the HV hub, which leads with distance/routing, garden complexes, weather and six counties; and from the Westchester co-op/condo hubs): a Westchester managing agent's list runs from prewar Yonkers/Mount Vernon walk-ups to postwar ETPA elevator buildings, new downtown New Rochelle/White Plains towers (platform and login takeovers, garages, elevator readers), garden apartments in the central towns, Sound Shore mixed-use and two- to four-family rentals. Angles unique to this page: county renter/housing-age data, the NYS Lead Rental Registry ZIPs (10550/10801/10701/10705) as a chance to bundle apartment-access days, login ownership and unknown devices in panels (Habitat Yonkers story), garage gates, salt air on the Sound, hill buildings with two entrance levels, White Plains false-alarm fees for leasing offices, Con Ed outages in the south of the county.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| WC1 | `Westchester County renter-occupied housing units percent renters census median year built housing` · WebSearch → WebFetch (PDF) | https://health.westchestercountyny.gov/images/stories/Data-Stats/Data%20Brief%20202509%20Housing%2020250912%20Final.pdf | WCDH Community Health Data Report 2025.09 "Housing in Westchester County, 2019-2023" (ACS 2019–2023): "Total Renter Occupied: 139,962", "Total Owner Occupied: 230,294"; year-built chart: 27.7% "1939 or earlier" (cumulative); cumulative through 1970–79 = 76.4% (derived from chart — page says "roughly three-quarters") | §County para 3; facts list (first two bullets); hero source stamp |
| WC2 | `Yonkers rental registry law landlords register rental units city of Yonkers` · WebSearch → WebFetch | https://health.westchestercountyny.gov/news/newsroom/westchester-county-highlights-new-state-lead-rental-registry-to-protect-children-and-families | NYS Lead Rental Registry: residential buildings with 2+ units incl. owner-occupied, built before 1980, in ZIPs 10550 (Mount Vernon), 10801 (New Rochelle), 10701 and 10705 (Yonkers); "registration is now required and participation is mandatory"; visual inspections every three years; EPA-certified inspectors; owners must inform tenants since apartment access is needed. No deadline on page (not stated on our page). | facts list; county table (Yonkers, Mount Vernon, New Rochelle rows); §Working with your office "lead registry" para; rules list; Q&A (Mount Vernon lead ZIP); coverage card Yonkers |
| WC3 | `New Rochelle rental registration program multiple dwelling inspection landlords` · WebSearch → WebFetch | https://ecode360.com/31298859 | New Rochelle student-rental business registration chapter (3+ students) — not relevant to PM security; NOT used | — |
| WC4 | `Mount Vernon NY rental property registration landlord certificate of compliance` · WebSearch → WebFetch | https://ecode360.com/45905318 | EMPTY (not accessible in build env — ecode360 client error) | — |
| WC5 | WebFetch | https://westchester.news12.com/new-legislation-would-expand-responsibilities-of-yonkers-landlords-40425619 | May 6 2019: only "Landlords in Yonkers could soon face stiffer penalties..." — no detail; NOT used | — |
| R1 | reused, silo PV2 | https://homes.westchestercountyny.gov/rent-control | 18 ETPA municipalities (Croton, Dobbs Ferry, Eastchester, Greenburgh, Harrison, Hastings, Irvington, Larchmont, Mamaroneck Town, Mount Kisco, Mount Vernon, New Rochelle, Pleasantville, Port Chester, Sleepy Hollow, Tarrytown, White Plains, Yonkers) | §County para 4; facts list; rules list |
| R2 | reused, silo PV7 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3: "all cities of less than three hundred twenty-five thousand population" + towns/villages | §County para 4; facts list; rules list |
| R3 | reused, silo PV4 | https://codes.iccsafe.org/content/NYSPMC2025P1/chapter-3-general-requirements | 2025 PMCNYS §304.18 security devices; §304.18.1 deadbolts | facts list; rules list |
| R4 | reused, silo PV5 | https://www.nysenate.gov/legislation/laws/RPP/235-B | RPL §235-b warranty of habitability | facts list; rules list |
| R5 | reused, co-op HV9 | https://www.osc.ny.gov/files/local-government/publications/pdf/2020-census-municipal-population-shifts-in-new-york-state.pdf | Yonkers 2020 Census 211,569 | facts list |
| R6 | reused, silo PV1 | https://thebcw.org/wp-content/uploads/2025/01/Westchester_Development_2024.pdf | RM Friedland via BCW: ~12,500 units delivered since late 2021; Yonkers, New Rochelle, White Plains, Mount Vernon 9,413 delivered, 13,114 under construction | §County para 3 |
| R7 | reused, condo WC-3 | https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster | New Rochelle form-based downtown zoning (council approval Dec 8, 2015); "boom in residential and mixed-use development across 279 acres" | facts list; coverage card New Rochelle |
| R8 | reused, co-op W5 | https://habitatmag.com/Publication-Content/Building-Operations/2022/2022-February/Westchester-s-Biggest-Co-op-Tackles-a-Security-Breach | Habitat (Feb 17 2022): large Yonkers co-op; delivery-access devices installed inside intercoms without authorization by a local vendor, agreements "signed by somebody with no authority", found by the agent's intercom company. No names used. | §Services "Keeping unknown devices out"; field notes (first hour) |
| R9 | reused, co-op W7 | https://westchester.news12.com/data-shows-porch-pirate-thefts-down-in-westchester-county-still-a-concern-throughout-the-year | News 12 Westchester (June 9 2026): Yonkers 50% decrease in package thefts at First Precinct; White Plains ~13 reports vs 18 same period 2025; Deputy Commissioner (White Plains Public Safety) quote "Cameras are still good." | §Services cameras (package para); AI check #6 |
| R10 | reused, co-op W8 | https://www.coned.com/en/about-us/media-center/news/2026/07-04/con-edison-restoring-power-to-customers-impacted-by-severe-storms | Con Ed July 2026: Westchester "experienced the greatest impact"; greatest outages in Greenburgh, Yonkers, Elmsford, Dobbs Ferry and Rye | facts list; §Power para |
| R11 | reused, co-op W21 / silo R3 | https://www.coned.com/en/about-us/media-center/news/2026/06-06/con-edison-restoring-power--to-customers-affected-by-storm | June 2026: >5,000 Westchester customers out | facts list; §Power para |
| R12 | reused, condo WC-8 | https://whiteplainspublicsafety.com/alarm-permits/ | White Plains Sec. 4-18-3(c): per false alarm in a calendar year $25 (1st), $50, $75, $100, $250 (12+) | §Services alarms; rules list |
| R13 | reused, silo R5 / co-op W14, W22 | https://consumer.westchestercountyny.gov/ ; Westchester County Code Ch. 863 ; https://www.nysenate.gov/legislation/laws/GBS/69-M | County trade license for plumbers/electricians; county alarm business licensing; GBL §69-m state alarm installer licensing | rules list; AI check #7 |
| R14 | reused, silo S6 | https://intro.nyc/local-laws/2021-63 | TDPA = NYC LL 63/2021, class A multiple dwellings in NYC only | §Services access control; AI check #2 |
| R15 | reused, silo S11 | https://cooperatornews.com/article/qa-camera-placement | Audio recording / NY eavesdropping caution | §Working with your office (footage) |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-westchester-county; /intercom-installation-westchester-county-ny; /access-control-installation-westchester-county; /elevator-access-control-installation-westchester-county; /security-camera-pricing-westchester-county; /structured-cabling-installation-westchester-county; /alarm-installation-westchester-county | Prices used — see below. Buzzer page also lists a "Sound Shore marine-grade enclosure" add-on (used in the Port Chester Q&A, no price). Access page notes tax varies by municipality (FAQ sales tax). | hero quick answer; services; cost table; packages; AI check #5 |
| E1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing-DDG for "property management security Westchester" | — | EMPTY (not accessible in build env). AI check section paraphrases common generic claims; no AI or Reddit quote invented. | — |

### Prices used (all already on Westchester pages)
$250 service call · apartment station $250–$525 · transformer $325–$650 · strike with alignment $450–$950 · lobby panel/faceplate $650–$1,800 · riser $850–$2,400 (door-buzzer-repair-westchester-county) · video intercom 4–8 units $1,200–$3,500; larger app-connected $2,500–$8,000+ (intercom-installation-westchester-county-ny) · single door $1,500–$2,500; multi-door $4,000–$15,000; full building with elevator $15,000–$40,000+ (access-control-installation-westchester-county) · elevator L1 $1,875/car, L2 $3,125/car (elevator-access-control-installation-westchester-county) · four-camera system from $1,099 (security-camera-pricing-westchester-county, A1) · Cat6 data drop $175 and up (structured-cabling-installation-westchester-county) · monitoring $30/$45 (alarm-installation-westchester-county). NOT used: $195/hr, $625–$1,875 per camera, "free on-site assessment", any maintenance-agreement price.

### Question register additions (property-management-security-westchester-county)
Checked by meaning against all 8 live PM pages (parsed with check_page.parse) and the co-op/condo Westchester registers. Dropped drafts that overlapped: propped doors (Bronx), tenants without smartphones (Queens), ETPA lobby upgrade (HV), alarm permit holder (LI), lender/insurer documentation (Manhattan/LI), spare parts (Manhattan), weekend work (NYC), commuter parking (Queens), landmarked facade (Brooklyn), delivery device in panel (co-op Westchester — kept as body text only).
- Q&A: The developer's contractor still holds the warranty on our new tower's entry hardware. Will your work void it?
- Q&A: Our New Rochelle building's garage gate and lobby panel come from different platforms. Can residents use one credential for both?
- Q&A: Can a prospect touring with a leasing agent get a code that stops working when the tour ends?
- Q&A: Our building's internet provider changed and the cloud intercom went offline. Why did that happen, and how do we stop it next time?
- Q&A: Our Mount Vernon building is in a lead-registry ZIP code. Can intercom work be booked on the same days the inspectors are in the apartments?
- Q&A: A Yonkers walk-up has a sidewalk cellar entrance that the oil company uses. How do we secure it without blocking deliveries?
- Q&A: Our Port Chester building is two blocks from Long Island Sound. Does the salt air change what goes on the front door?
- Q&A: Which entrance should get the visitor panel when a building on a hill has a street door and a garage-level door?
- Q&A: Our Greenburgh garden complex has a separate laundry building. Should it be on the same system as the apartment doors?
- Q&A: Deer and wind keep setting off motion alerts at our northern Westchester complex. How do we cut down the false alerts?
- Q&A: A tenant's home health aide comes every morning. How do we give access without a fob that never expires?
- Q&A: Our building has a doorman until midnight. What should the entry system do after the desk closes?
- Q&A: What should happen to the superintendent's credentials and app logins when the super leaves the job?
- Q&A: Can one dashboard show which entry panels across our Westchester buildings are offline right now?
- FAQ: Do you charge more to send a technician to northern Westchester towns such as Somers or Bedford?
- FAQ: Is sales tax added to security work in Westchester?
- FAQ: Can our office look up which door a tenant's fob opened on a particular night?
- FAQ: Can a reader be added to the garage roll-up door at a rental building?
- FAQ: Do you replace batteries in wireless door sensors and keypads during maintenance visits?
- FAQ: How do new tenants get their fobs when they move in on a weekend?
- FAQ: Can our cameras send video straight to the police when something happens?
- FAQ: Can the lobby panel call a concierge desk instead of ringing apartments directly?
- FAQ: Can different people at our firm get different alerts from the same building?
- FAQ: Can every exterior door at a building be locked at once if there is an incident nearby?

### Similarity (masked geo; 8-word shingle share / difflib word-sequence ratio)
HV hub 0.068 / 0.321 (max) · NYC 0.029 / 0.190 · LI 0.031 / 0.138 · Bronx 0.026 / 0.120 · Brooklyn 0.025 / 0.119 · Queens 0.026 / 0.119 · SI 0.026 / 0.063 · Manhattan 0.025 / 0.061 · Nassau 0.031 / 0.153 · Suffolk 0.031 / 0.145 · co-op Westchester 0.029 / 0.121 · condo Westchester 0.028 / 0.094. All < 0.65.

### Images (11: 5 real job photos + 6 Reolink partner product photos)
WebP (quality 80, max 1200 px) in images/property-management-security/. A first pick of 8 library job photos (images/cctv-installation/*westchester-county*, images/intercom-repair/*staten-island*) was dropped because the parallel Nassau and Suffolk PM builds used the same scenes; the library's real job scenes are a small pool repeated under many filenames. Final set dHash-checked against every other file in images/property-management-security/ (min Hamming distance 68/256 — no reuse) and viewed. No faces, plates, house numbers, readable documents or "AESS".
| File (property-management-security-westchester-county-…) | Source | Where |
|---|---|---|
| job-photo-stainless-electric-strike-in-painted-wood-frame | /tmp/pi2/photos/recX1GTVv4v0RS8Bp_0.jpg (photo library, access-control) | hero (eager), og/twitter |
| white-bullet-camera-on-pale-stone-wall | Reolink (partner) · reolink.com/us/product/rlc-81ma/ page asset 2025/08/040853411754297621.3911.jpg.webp | §County |
| job-photo-electric-strike-with-black-faceplate-and-wire-raceway | /tmp/pi2/photos/reczp0wY8VCBLJfOk_0.jpg | §Services door hardware |
| job-photo-small-dome-on-drop-ceiling-between-light-panels | images/access-control-installation/access-control-installation-gowanus-dome-camera-beside-track-lights.webp | §Services cameras |
| two-dome-cameras-at-wall-and-ceiling-corner | Reolink · rlc-1240a page 2024/04/070839221712479162.7779.jpg.webp | §Services alarms |
| wall-monitor-with-recorder-and-router-below | Reolink · product page asset 2026/01/08104510914fc16773e34bc5.jpg.webp | §Services cabling |
| white-dome-camera-with-rain-drops-under-dark-ceiling | Reolink · rlc-1240a page 2024/04/070838501712479130.0081.jpg.webp | §Building types |
| job-photo-dome-camera-over-shop-shelving-and-wood-panel-wall | images/access-control-installation/access-control-installation-gowanus-dome-camera-over-wood-panel-shop-wall.webp | §Building types (commercial) |
| job-photo-slim-black-plate-on-dark-door-frame-beside-brick | /tmp/pi2/photos/recyWmzbbEmWpuwjw_0.jpg | §Equipment |
| monitor-and-phone-showing-camera-software | Reolink · rlc-1240a page 2024/04/080349131712548153.6441.jpg.webp | §Process |
| black-network-video-recorder-on-pale-pedestal | Reolink · rln8-410 page 2024/11/070925081730971508.9166.jpg.webp | §Coverage |
(Exact page-to-asset mapping for the Reolink files comes from curl of reolink.com/us/product/{rlc-1240a,rln8-410,rlc-1224a,rlc-81ma}/; the asset URLs are exact.)
DAILY-LOG note: `images: 5 real job photos (3 photo library, 2 from images/access-control-installation/) + 6 Reolink partner product photos`.

### FLIPs on the page (plain text + `<!-- FLIP: /slug -->`)
/property-management-security-rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county (coverage section). Linked live: -nassau-county, -suffolk-county (built in parallel, on disk at finish), /property-management-security-hudson-valley (up), -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island; Westchester co-op/condo hubs and co-op/condo/apartment-building camera pages.

### Links left for the main run
Back-links needed from the live PM pages (all except Nassau, which already links) (HV hub must flip its Westchester card FLIP to a live link). Suggested contextual back-links: /co-op-security-systems-westchester-county, /condo-security-systems-westchester-county, /apartment-building-security-camera-installation-westchester-county, /intercom-installation-westchester-county-ny, /access-control-installation-westchester-county.

### For Anwar to confirm
- $250 service call charged the same in northern Westchester towns (FAQ) — HV hub already states the same $250 across counties.
- Leasing-tour expiring codes, scheduled lockdown command, desk-hours/after-hours panel switching, per-user alerts, offline-status dashboards: written as "on most/many platforms", not tied to a brand.
- Office issues fobs itself and we "set the office up with a stock of blank fobs" (FAQ weekend move-in) — implies we sell spare fobs (Brooklyn PM FAQ already asks about buying spare fobs).
- 30-day workmanship warranty + one-year parts sentence side by side (matches HV hub and memory).
- "Crews leave our Bronx office at 460 East Fordham Road" and "booked within 2 hours … seven days a week".
- Marine-grade enclosure for Sound Shore buildings (taken from the Westchester buzzer page add-on).
- Site survey for new systems/portfolios: page does NOT say it is free (HV hub says "free on-site assessment"; left out per rules).


## Rockland County (property-management-security-rockland-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page: up-link /property-management-security-hudson-valley, phone (845) 640-3835 (body, CTAs, sticky bar, schema; 800 only in the shared header), GBP Bronx (460 E Fordham Rd, `#bronx`), start price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thesis (kept apart from the HV hub = distance/six counties; Westchester = towers/ETPA-18/lead ZIPs in Yonkers etc.; co-op Rockland = garden co-ops/county code enforcement; condo Rockland = resale churn/HOA amenities; apartment-camera Rockland = cameras only): Rockland landlords and managing agents with mostly SMALL rentals — two-families and converted houses (Spring Valley, Haverstraw, Suffern), village main-street walk-ups (Haverstraw, Nyack, Pearl River), garden complexes and Route 59 multifamily (Nanuet, Spring Valley), station-area proposals (Pearl River 109 units, Nanuet Town Centre); layered rental paperwork (county Multiple Dwelling Rental Registry at 3+ units with new certificate after each sale, Haverstraw village two-year rental permits for every unit, Orangetown 2025 landlord registry, Lead Rental Registry in 10977), ETPA only in Town of Haverstraw + Village of Spring Valley (Nyack opted out Jan 2024); inspection/renewal/closing dates used as security checkpoints; property-sale inventory of logins.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| RKP1 | `Rockland County rental registry law landlord permit Spring Valley Haverstraw Nyack Clarkstown Orangetown` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.rocklandcountyny.gov/departments/health/center-for-rockland-codes-investigations/housing-mdrr | "All multiple dwellings with 3 or more rental units, and all rooming houses, must register and obtain a Multiple Dwelling Rental Certificate. A new Certificate is required after each change of property ownership. Failure to comply ... may result in penalties of $2,000.00 per day." One-time fee $25 per dwelling/rooming unit; deed and CO uploaded. | §County para 4; facts list; Working-with "Registration…checkpoints" + "When a property changes hands"; Q&A (three-unit certificate); FAQ (filing); AI check #3 |
| RKP2 | same search · Firecrawl scrape (directQuote) | https://ecode360.com/14676566 | Village of Haverstraw Ch. 171: rental permit required for all rental units ("No housing unit shall be let ... by someone other than the owner or his immediate family until a rental permit has been obtained"); permit valid two years; landlord registration $50/property; permit fee $25 incl. inspection; reinspection $50 / $100. (Fee amounts not printed on page.) | §County para 4; facts list; table (Haverstraw row); coverage card; AI check #3 |
| RKP3 | same search · Firecrawl scrape (directQuote) | https://rocklandtimes.com/2025/06/13/landlord-registry-passes-in-orangetown/ | Rockland County Times, June 13 2025: Orangetown adopted Landlord Registry; 1–4 units $75, 5+ units $150 per year; owner living on the property (e.g., two-family) not required to register; yearly registration. Excerpt of https://forms.orangetown.com/Forms/Rentalregistry: "For Properties with 1 to 4 Units, the fee is $75 per year." | §County para 4; facts list; table (Orangetown row); coverage card Pearl River; AI check #3; FAQ (filing) |
| RKP4 | `Emergency Tenant Protection Act Rockland County municipalities adopted rent stabilization` · Firecrawl search → Firecrawl scrape PDF (directQuote) | https://hcr.ny.gov/system/files/documents/2024/11/fact-sheet-08-11-2024.pdf | HCR Fact Sheet #8 (11/2024): Rockland ETPA municipalities listed: "Town of Haverstraw Village of Spring Valley"; "ETPA covers buildings of six or more units that were built before 1974." | §County para 5; facts list; building types (ETPA H3); services (entry habits); AI check #2 |
| RKP5 | same search · Firecrawl scrape (directQuote) | https://hcr.ny.gov/rent-stabilization-and-emergency-tenant-protection-act | "On January 11, 2024, the Village of Nyack Board of Trustees ... voted to declare an end to the local housing emergency, opt out of the ETPA". | §County para 5; facts list; AI check #2 |
| RKP6 | `New York State lead rental registry Spring Valley Rockland communities of concern pre-1980 two or more units` · Firecrawl search (excerpt) | https://www.health.ny.gov/environmental/lead/lead_rental_registry/property_owners.htm | Lead Rental Registry in effect in 25 communities of concern as of Nov 3 2025 (list includes Spring Valley); pre-1980 rental housing with two or more units; applies even if owner-occupied (press release excerpt https://www.health.ny.gov/press/releases/2025/2025-12-03_lead_rental_registry_program.htm). | §County para 4; facts list; AI check #3 |
| RKP7 | same search · Firecrawl scrape (directQuote) | https://www.rocklandcountyny.gov/departments/health/programs-services/lead-poisoning-prevention-program | "rental properties with 2 or more units, built before 1980 in 10977 ... inspected for lead hazards every 3 years, or after a property is sold"; visual checks inside/outside and dust wipe sampling by RCDOH. | §County para 4; facts list; building types (two-families); Working-with checkpoints |
| RKP8 | `Rockland County new apartment complex Route 59 Nanuet Spring Valley Pearl River units approved 2025 2026` · Firecrawl search → Firecrawl scrape (directQuote) | https://rocklandtimes.com/2026/05/21/new-apartments-proposed-for-pearl-river/ | May 19 2026 Orangetown board: Sidetrack Properties LLC concept for "109 housing units for Pearl River, on West Jefferson Ave, in walking distance to the Pearl River Metro North train station and the downtown area" — presented as a question/concept. (Developer name not used on page.) | Building types (Route 59 / stations H3) |
| RKP9 | same search · Firecrawl scrape (directQuote) | https://prodealre.com/blog/the-nanuet-mall-is-becoming-an-apartment-complex-and-the-fine-print-changes-what-you-should-expect-from-the-market | Nanuet Town Centre (former mall): Yahoo News reported two phases planned, roughly 160 units behind the former Sears and 120 at the former Sears Automotive Center; no formal site plans filed with Clarkstown Planning Board at last update. Page says "plans reported … formal site plans had not been filed at last report". (Secondary source — CONFIRM if a primary source is preferred.) | Building types (Route 59 H3); coverage card Nanuet |
| R1 | reused co-op Rockland R3 (Wikipedia via Firecrawl) | https://en.wikipedia.org/wiki/Rockland_County,_New_York | 199.34 sq mi, smallest county by area outside NYC; 5 towns; 18 villages; New City seat; Mario M. Cuomo Bridge; Pascack Valley Line (Pearl River, Nanuet, Spring Valley); Port Jervis Line (Suffern, Sloatsburg). | §County para 3; facts list; Q&A (Pascack Valley commuters) |
| R2 | reused co-op Rockland R5 | https://www.census.gov/quickfacts/rocklandcountynewyork | 2020 Census 338,329; 109,999 housing units; owner-occupied 67.9% (2020–2024). "Roughly one occupied home in three is rented" = derived (100 − 67.9). | §County para 3; facts list |
| R3 | reused co-op Rockland R6 | https://hudsonvalley.news12.com/rocklands-office-of-buildings-and-codes-reflects-on-2-year-anniversary-of-taking-over-inspections-code-enforcement-in-village-of-spring-valley | County Office of Buildings and Codes took over Spring Valley inspections Feb 14 2022 under state order; >2,000 inspections, >12,400 alleged violations in two years. | §County para 5; facts list; AI check #1 |
| R4 | reused co-op Rockland R8 | https://dos.ny.gov/notice-adoption | 2025 NYS Uniform Code effective Dec 31 2025. | Services (door hardware exit safety) |
| R5 | reused co-op Rockland R9 | https://ecode360.com/26997705 | Rockland Code ch. 250 electrical contractor: light, heat, power or signaling ≥50 V. | Facts list; services (cabling); AI check #6 |
| R6 | reused apartment-camera research row 8 | https://ecode360.com/9666538 | Rockland ch. 286 (adopted 4-14-2026): home improvement license, dwellings of not more than three units. | Facts list (stated only as a fact; no license claim made) |
| R7 | reused co-op Rockland R10 | https://ecode360.com/6704537 | Clarkstown ch. 91: alarm users "shall obtain an alarm user permit from the Police Department". | Services (alarms); Q&A (Clarkstown leasing office alarm) |
| R8 | reused co-op Rockland R11 | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k | O&R: >47,000 customers impacted since July 1 2026. | Facts list; AI check #5 |
| R9 | reused co-op Rockland R12 | https://rocklandtimes.com/2026/07/09/massive-storm-sweeps-through-rockland/ | 6,466 Rockland customers out 11:30 p.m. July 4 2026; New City neighborhood without power >36 hours. | Facts list; AI check #5 |
| R10 | reused condo Rockland RC-W3 | https://www.rocklanddaily.com/news/piermont-experiences-worst-flooding-since-hurricane-sandy | Jan 2024 tidal flooding in Piermont, worst since Sandy. | Process field notes (spring water) |
| R11 | reused co-op Rockland R20 / silo HV11 | https://dailyvoice.com/article/packages-stolen-from-apartment-complex-found-inside-haverstraw-home-man-35-charged-cops-say/ | Apr 2026 Haverstraw: packages taken from several buildings within one complex recovered after search warrant (no name used). | Services (packages) |
| R12 | reused condo Rockland RC-G14 | https://udigny.org/resources/nys-code-rule-753/ | Code Rule 753: notice at least two but not more than ten working days before digging. | Services (cabling); process timelines |
| R13 | reused condo Rockland RC-G10 | https://www.nysenate.gov/legislation/laws/GBS/395-B | GBL §395-b: no viewing devices in restrooms, bathrooms, showers, fitting rooms etc. | FAQ (laundry room cameras) |
| R14 | reused silo HV15 | https://www.nysenate.gov/legislation/laws/GBS/69-M | State alarm installer licensing. | AI check #6 |
| R15 | reused silo PV7 / HV8 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 applies to all towns and villages and cities under 325,000. | Facts list; AI check #1 |
| R16 | reused silo S6 | https://intro.nyc/local-laws/2021-63 | TDPA = NYC Local Law 63/2021, class A multiple dwellings in NYC only. | AI check #7 |
| R17 | reused silo S12 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500". | AI check #4 |
| R18 | reused silo S11 | https://cooperatornews.com/article/qa-camera-placement | Audio recording / eavesdropping caution. | Services (cameras: audio off); FAQ (laundry) |
| R19 | industry standard (TIA-568, as on site cabling pages; LI row LIP16) | — | ~100 m channel limit between active devices. | Services (cabling) |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-rockland-county; /intercom-installation-rockland-county-ny; /access-control-installation-rockland-county; /elevator-access-control-installation-rockland-county; /security-camera-pricing-rockland-county; /structured-cabling-installation-rockland-county; /alarm-installation-rockland-county | Prices used — see below. | Hero quick answer; services; cost table |
| E1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG for "property management security Rockland County" | — | EMPTY (not accessible in build env). Earlier Rockland builders found no relevant r/rocklandcounty thread. AI Reality Check corrects claims typical of chatbot/cost-guide answers; no AI or Reddit quote invented. | — |

### Prices used (all already published on Rockland pages)
$250 service call (START_PRICES; buzzer repair page) · station $250–$525 · relay/button $250–$475 · 24 V transformer $325–$650 · strike with alignment $450–$950 · lobby panel/faceplate $650–$1,800 · riser $850–$2,400 (/door-buzzer-repair-rockland-county) · video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+ (/intercom-installation-rockland-county-ny) · single door/gate $1,700–$5,000; multi-door $4,500–$15,000 (/access-control-installation-rockland-county cost section) · elevator L1 $1,950/car, L2 $3,250/car · four-camera from $1,099 (/security-camera-pricing-rockland-county, A1) · cabling $150–$300 per drop · monitoring $30/$45. NOT used: access-control page's "$195/hr", "15% surcharge", "$1,500–$2,500 plus surcharge"; intercom page "free on-site assessment", "$200–$400 savings"; alarm package prices; any maintenance/portfolio price; fire alarm prices (none).

### Question register additions (property-management-security-rockland-county)
Checked by meaning against all PM pages on disk (incl. parallel Orange/Putnam at check time, checker found no masked duplicates) and the co-op/condo/apartment-camera Rockland pages. Dropped drafts that overlapped: rental-permit-renewal timing (Nassau), lead-ZIP same-day booking (Westchester), store/stair-door separation (Suffolk), alarm permit holder (LI), Sabbath options (condo/co-op Rockland), least-used entrances (co-op Rockland), shared-driveway camera (SI), pre-purchase survey (LI).
- Q&A: Our building has three apartments, so the county says it needs a rental certificate. Does the entry system have anything to do with that registration?
- Q&A: A converted house in Spring Valley now holds four apartments behind one street door. How does each tenant let in their own visitors?
- Q&A: Our building's mailboxes sit outside the locked door. Should a camera watch them, and who repairs a damaged mailbox?
- Q&A: Tenants keep losing the little fobs. Would keypad codes or phone credentials cost less to run?
- Q&A: Our complex sits on Route 59 between a shopping center and a bus stop, and people cut through the grounds. Where do cameras help, and where do they not?
- Q&A: Our garden complex has buildings on both sides of a town road. Can the cameras and readers on each side work as one system?
- Q&A: Our maintenance crew covers properties in four towns. Can one credential open the boiler and meter rooms at all of them?
- Q&A: A former tenant still has a remote for our complex gate. How do we shut it off without reprogramming everyone else's?
- Q&A: Water pools at the call box at the bottom of our sloped driveway every spring. Is there a better spot or housing for it?
- Q&A: Our tenants commute on the Pascack Valley Line and are gone all day. If the entry panel calls their phones, do visitors still get stuck at the door?
- Q&A: An elevator building we manage still uses a key switch for the top floor. Can that become a fob?
- Q&A: The entry panel on our west-facing building is hard to read in afternoon sun. Can that be fixed without moving it?
- Q&A: A tenant says the hallway camera is pointed at her apartment door. How should we answer?
- Q&A: Our Clarkstown leasing office alarm keeps bringing the police for nothing. What usually causes that?
- FAQ: Do you work in the hamlets such as Nanuet, Valley Cottage and Congers, or only in the villages?
- FAQ: Does the service call cover a second problem the technician finds at the same property?
- FAQ: Can you file our county rental registration or town registry form for us?
- FAQ: A tenant put a smart lock on their own apartment door. Does that interfere with the building's system?
- FAQ: Can the entry panel's screen and prompts be set in a language other than English?
- FAQ: Can cameras go inside the laundry room of a rental building?
- FAQ: Can a tenant's gate remote and building fob be the same device?
- FAQ: Tenants change often in our buildings. How do we keep the buzzer labels matched to the right apartments?
- FAQ: Can our leasing office door unlock on a schedule during business hours and lock itself after?
- FAQ: Can tenants see who is at the front door before they let them in?

### Similarity (masked geo; 8-word shingle share / difflib word-sequence ratio / max paragraph ratio)
Westchester 0.070 / 0.258 · HV hub 0.040 / 0.174 · NYC 0.031 / 0.143 · LI 0.033 / 0.151 · Nassau 0.033 / 0.151 · Suffolk 0.035 / 0.139 · Bronx 0.027 / 0.109 · Brooklyn 0.028 / 0.122 · Queens 0.028 / 0.123 · SI 0.028 / 0.064 · Manhattan 0.027 / 0.068 · parallel Orange 0.062 / 0.231 · parallel Putnam 0.051 / 0.204 · co-op Rockland 0.030 / 0.100 · condo Rockland 0.030 / 0.103 · apartment-camera Rockland 0.017 / 0.060. All < 0.65. Paragraph level: every p/li/td/h3/figcaption ≥12 words < 0.62 after rewriting ~30 short cards/steps/CTA lines that echoed Westchester/HV/Orange/Putnam template phrasing.

### Images (11: 5 real job photos + 6 Reolink partner product photos)
WebP q80 in images/property-management-security/. Each checked by phash/dhash against every other file in images/property-management-security/ (no match) and visually via contact sheets. Excluded as same scene already on a PM page: cctv Rockland black bullet on white wall (= Suffolk stucco wall), wall camera by exit sign + tall windows (= Nassau mezzanine wall), intercom-repair Putnam dome + motion sensor (= Nassau corner dome by flag / parallel Putnam), shop-canopy dome (= Nassau fascia dome), corridor grey door (= LI). A first-pick "cable bundles above recorder monitor" was swapped out after the parallel Putnam page used the same monitor scene. No faces, plates, house numbers, readable documents or "AESS".
| File (property-management-security-rockland-county-…) | Source | Where |
|---|---|---|
| job-photo-turret-dome-on-ceiling-over-glass-entrance (hero, eager, og/twitter) | images/cctv-installation/cctv-installation-rockland-county-turret-dome-over-glass-storefront-and-lot.webp | hero |
| job-photo-camera-on-steel-arm-below-stone-facade-windows | images/intercom-repair/intercom-repair-staten-island-stone-apartment-facade-with-camera-on-steel-arm.webp | §County |
| job-photo-bullet-camera-on-ceiling-mount-in-drop-tile-grid | images/cctv-installation/cctv-installation-rockland-county-ceiling-mount-bullet-on-drop-tile-grid.webp | §Services cameras |
| partner-photo-bullet-camera-and-red-strobe-wired-to-recorder-back | Reolink (partner) · https://reolink.com/us/product/rln36/ page asset home-cdn.reolink.us/…/160744551747381495.8039.jpg.webp | §Services cabling |
| partner-photo-camera-view-of-courtyard-with-wooden-door | Reolink · https://reolink.com/us/product/rlc-520a/ asset 2025/07/090356361752033396.4414.jpg | §Building types (garden complexes) |
| job-photo-dome-camera-where-drop-ceiling-meets-tall-wall | images/cctv-installation/cctv-installation-rockland-county-corner-dome-where-ceiling-meets-tall-wall.webp | §Working with your office |
| partner-photo-white-turret-camera-on-black | Reolink · rlc-520a asset 2023/03/200425451679286345.2149.png | §Equipment |
| job-photo-small-camera-high-on-blue-wall-above-drop-ceiling | images/cctv-installation/cctv-installation-rockland-county-high-bullet-and-mini-dome-over-entry-ceiling.webp | §Process |
| partner-photo-white-turret-camera-on-wall-above-lake | Reolink · rlc-520a asset 2025/07/090349121752032952.7475.jpg.webp | §Coverage |
| partner-photo-white-dome-camera-on-black | Reolink · https://reolink.com/us/product/rlc-833a/ asset 2023/12/110241451702262505.8584.png | §Cost |
| partner-photo-night-camera-view-of-porch-steps-and-railing | Reolink · rlc-520a asset 2025/07/090357051752033425.5765.jpg | §Packages |
DAILY-LOG note: `images: 5 real job photos (4 images/cctv-installation Rockland, 1 images/intercom-repair) + 6 Reolink partner product photos via reolink.com`.
Collision note for the main run: parallel Putnam "camera-monitor-above-shop-shelves" and parallel Orange "wall-monitor-with-camera-grid-over-store-shelves" look like the same scene (their issue, not this page's).

### FLIPs on the page (plain text + `<!-- FLIP: /slug -->`)
/property-management-security-orange-county, -putnam-county, -dutchess-county, -ulster-county (coverage section). Linked live: /property-management-security-hudson-valley (up, breadcrumb + body), -westchester-county, -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island, -nassau-county, -suffolk-county.

### Rockland pages linked once
/condo-security-systems-rockland-county, /co-op-security-systems-rockland-county, /door-buzzer-repair-rockland-county, /intercom-repair-rockland, /intercom-installation-rockland-county-ny, /intercom-installation-rockland-county-new-york, /co-op-board-intercom-upgrade, /condo-intercom-replacement, /smart-lock-installation-rockland-county, /access-control-installation-rockland-county, /elevator-access-control-installation-rockland-county, /security-camera-pricing-rockland-county, /apartment-building-security-camera-installation-rockland-county, /condo-security-camera-installation-rockland-county, /co-op-security-camera-installation-rockland-county, /parking-lot-camera-installation-rockland-county, /security-camera-repair-rockland-county, /alarm-installation-rockland-county, /structured-cabling-installation-rockland-county, /fire-alarm-installation-rockland-county-ny, /door-buzzer-installation-rockland-county-ny, /doorbell-camera-installation-rockland-county, /security-cameras-rockland-county, /cctv-installation-rockland-county, /low-voltage-installation-rockland-county, /commercial-security-systems-rockland, /commercial-security-camera-installation-rockland-county, /network-installation-rockland-county, /floodlight-camera-installation-rockland-county, /wireless-camera-installation-rockland-county, /nvr-installation-rockland-county, /security-camera-maintenance-rockland-county, /free-quote.

### For Anwar to confirm (CONFIRM)
- Fire alarm: page says door releases are coordinated with the fire alarm company of record and links /fire-alarm-installation-rockland-county-ny ("priced from approved drawings") — confirm Rockland fire alarm work is in scope.
- Rockland ch. 286 home improvement license (dwellings ≤3 units) is stated only as a county fact; page makes no claim about whether Abstract Enterprises Security Systems holds it — confirm whether it applies/is held.
- Wireless bridges across a road, call-box relocation/hoods, privacy masking, scheduled leasing-office unlock, multilingual panel display, combined gate/fob credentials, individually enrolled gate remotes: written as things we do (on "most/many" platforms, no brand).
- Package delivery code for the outer door and parcel room on a reader: written as setups we do; locker vendor left to owner.
- "Photos attached to each scope" for remote owners and the per-property "building record" emailed to the office — confirm this is current practice.
- Nanuet Town Centre unit counts come from a secondary source quoting Yahoo News; swap for a primary source if preferred.


## Orange County (property-management-security-orange-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page · up-link /property-management-security-hudson-valley · phone (845) 640-3835 (body, CTAs, sticky bar, schema; 800 only in shared header) · GBP Bronx (`#bronx`, 460 E Fordham Rd) · start price $250 service call (START_PRICES). Format: exact query · platform · URL · finding · section used.

Thin-page check (an Orange co-op camera page was held as too thin): PASSED. Orange has enough distinct, sourced landlord material — three city rental laws (Newburgh license, Middletown permit, Port Jervis vacant-building registry), the state Lead Rental Registry in Newburgh and Middletown, the voided Newburgh ETPA, tenure/age/structure data for Newburgh, Middletown, Port Jervis and Kiryas Joel, college and Port Jervis Line rental demand, three electric utilities.

Thesis (kept apart from the HV hub = routing/garden complexes/weather; Westchester = ETPA towers/downtown takeovers; Orange co-op/condo = boards): an Orange County landlord list is small owners plus managers across very different places — Newburgh pre-1940 rowhouses under an annual rental license, Middletown multi-entrance houses under two-year rental permits, Port Jervis small/vacant buildings under a 30-day inspection rule, Kiryas Joel/Palm Tree apartment blocks with very large households, garden complexes, student and commuter rentals.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| O1 | `Newburgh NY rental registration law landlords inspection` · WebSearch → WebFetch | https://ecode360.com/44151840 ; https://ecode360.com/44151860 | City of Newburgh Ch. 240 rental license, L.L. No. 1-2024 (adopted 1-22-2024): unlawful to offer/rent a unit in a non-owner-occupied building without a license; no license issued/renewed until municipal officer finds code compliance based on inspection (§240-6; PE certification alternative if consent refused); annual renewal; "compliant landlords" may get 2-year term; not transferable to another person/property; application must state whether structure has a fire alarm system; fees in Ch. 163 (not used); 5%/day delinquency penalty (not used) | §5 laws para; rules list; Q&A fire alarm on application; AI check #5; logins para; building types (Newburgh) |
| O2 | `Middletown NY rental dwelling registration inspection ordinance` · WebSearch → WebFetch | https://ecode360.com/13413477 | City of Middletown rental permit (DPW) for single-family and owner-occupied two-family units; no listing/advertising/showing/accepting rent or deposit without permit or complete application; applications and renewals granted only after inspection (also on change of occupancy); two-year term; fines $250–$1,000, up to 15 days, each day separate offense; amendments 2012/2019 | §5 laws para; rules list; building types (converted houses) |
| O3 | `Port Jervis NY rental registry law landlords code enforcement` · WebSearch → WebFetch | https://ecode360.com/37170903 | City of Port Jervis vacant/abandoned (incl. foreclosure) property law: register and secure within 30 days; proof of inspection at least every 30 days after vacancy; building official, fire inspector, police may inspect; fines up to $500 / 30 days; unpaid charges on tax bill. NOT a rental registry. | §5 laws para; vacant-units service; Q&A Port Jervis register; field notes; rules list |
| O4 | ACS 5-year 2023, tables B25003/B25024/B25034/B25064 · Firecrawl Alexandria provider census-gov (census/data) | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&ucgid=0500000US36071 (and B25024/B25034/B25064; places 1600000US3650034, 3647042, 3659388, 3639853) | Orange Co: 137,311 occupied, 93,959 owner, 43,352 renter; 148,460 units, 29,991 built ≤1939; median gross rent $1,602. Newburgh city: 10,335 occ / 6,689 renter; 11,624 units / 5,747 ≤1939; rent $1,363. Middletown: 10,182 / 4,841; 11,018 / 3,563 ≤1939; rent $1,614. Port Jervis: 3,533 / 1,702; 3,896 / 2,110 ≤1939; rent $1,247. Kiryas Joel: 6,869 / 4,462; 7,383 units, 215 detached, 5–9: 2,708, 10–19: 2,239, 20–49: 1,400, 50+: 0 (6,347 in 5+ = 86%); rent $1,575 | §5 paras 3–4; facts list; county table; building types; AI check #4; Q&A rents; coverage cards |
| O5 | censusreporter profiles · Firecrawl scrape (query) | https://censusreporter.org/profiles/16000US3639853-kiryas-joel-ny/ (+ county, Middletown, Port Jervis profiles for cross-check) | Kiryas Joel ACS 2024 5-year: pop 38,916; persons per household 5.1; median age 15.7 (age not used) | facts list; building types (KJ); Q&A KJ door hardware |
| O6 | `New York State lead rental registry communities of concern ZIP codes Orange County Newburgh 12550 Middletown Port Jervis` · Firecrawl search → scrape | https://www.health.ny.gov/press/releases/2025/2025-12-03_lead_rental_registry_program.htm ; https://www.health.ny.gov/environmental/lead/lead_rental_registry/property_owners.htm | Registry in effect in 25 communities of concern as of Nov 3 2025, incl. Middletown and Newburgh; covers rentals built before 1980 with 2+ units; lead hazard inspection at least every 3 years by qualified inspector; tenants given names, dates and times ahead of inspections/repairs | facts list; lead registry para; working-with-office (lead days); rules list; AI check #3 |
| O7 | same search · Firecrawl scrape | https://citizenportal.ai/articles/8901192/New-York/Orange-County/County-accepts-728600-for-Lead-Rental-Registry-reports-1000-properties-registered | Apr 21 2026: county accepts $728,600 (4/1/2026–3/31/2027); "over 1,000 properties registered to date, which is 25% of the properties required to register" | lead registry para |
| O8 | `Newburgh city council Emergency Tenant Protection Act vacancy study rent stabilization` · Firecrawl search (excerpts) | https://hcr.ny.gov/rent-stabilization-and-emergency-tenant-protection-act ; https://www.cityandstateny.com/policy/2023/12/newburgh-adopts-emergency-tenant-protection-act/392864/ | Council voted unanimously Dec 18 2023 to adopt ETPA for pre-1974 buildings with 6+ units; study found 3.93% vacancy; Apr 19 2024 NYS Supreme Court, Orange County ruled study flawed; adoption "null and void" | ETPA para; rules list; AI check #1 |
| O9 | `Central Hudson service territory counties Orange County Newburgh; Orange and Rockland Utilities service area Orange County` · Firecrawl search (excerpt) | https://dps.ny.gov/system/files/documents/2022/10/nys-electric-and-gas-utilities-by-county.pdf | Orange County electric utilities: NYSEG, Central Hudson, Orange and Rockland | facts list; power section; Q&A three utilities |
| O10 | reused, silo research PV6 (HV hub) | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k | O&R: >47,000 customers impacted July 1–6 2026 by heat, storms, heavy rain | power section |
| O11 | reused, silo research R2 (HV hub; condo H4) | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Central Hudson: >19,000 out after Sept 26 2026 nor'easter | power section |
| O12 | `Metro-North Port Jervis Line stations Harriman Salisbury Mills Campbell Hall Middletown Otisville Port Jervis` · Firecrawl search (excerpts) | https://www.mta.info/schedules/metro-north/port-jervis ; https://en.wikipedia.org/wiki/Port_Jervis_Line | Orange County stations: Harriman, Salisbury Mills(–Cornwall), Campbell Hall, Middletown/Town of Wallkill, Otisville, Port Jervis | facts list; building types (commuters); coverage cards |
| O13 | `Mount Saint Mary College Newburgh enrollment students; SUNY Orange Newburgh campus Middletown campus` · Firecrawl search (excerpts) | https://www.princetonreview.com/college/mount-saint-mary-college-1023737 ; https://www.instagram.com/suny_orange/ | MSMC at 330 Powell Ave, Newburgh; SUNY Orange "Campuses in Middletown and Newburgh". Enrollment counts not used | building types (students); Q&A bedroom rentals |
| O14 | `Town of Palm Tree New York formed 2019 Kiryas Joel separated from Town of Monroe` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Palm_Tree,_New_York | Palm Tree coterminous with village of Kiryas Joel, formerly part of Town of Monroe, created Jan 1 2019 | §5 para 1; coverage card |
| O15 | reused, silo S11 | https://cooperatornews.com/article/qa-camera-placement | audio recording / eavesdropping caution | footage para |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-orange-county-new-york ; /intercom-installation-orange-county-ny ; /access-control-installation-orange-county ; /elevator-access-control-installation-orange-county ; /apartment-building-security-camera-installation-orange-county ; /security-camera-installation-orange-county-ny + /security-camera-pricing-orange-county (MODELS min $1,199) ; /structured-cabling-installation-orange-county ; /alarm-installation-orange-county | See "Prices used" | hero quick answer; services; cost table; packages |
| E1 | census.gov QuickFacts direct · Firecrawl/WebFetch | https://www.census.gov/quickfacts/... | EMPTY (not accessible in build env) — 503/client error; api.census.gov blocked by proxy (403); data taken via Alexandria census-gov provider (O4) | — |
| E2 | orangecountyny.gov Lead Rental Registry page | https://www.orangecountyny.gov/2693/Lead-Rental-Registry | EMPTY (not accessible in build env) — page body not rendered (scripts only) | — |
| E3 | Google PAA / PASF / AI Overview / Answer the Public / Reddit / Yelp / Bing-DDG for "property management security Orange County NY" | — | EMPTY (not accessible in build env). AI check corrects generic/NYC claims; no AI quote invented | — |

### Prices used (all already published on Orange County pages)
$250 service call; apartment station $250–$525; release relay/button $250–$475; transformer $325–$650; strike + alignment $450–$950; lobby panel/faceplate $650–$1,800; riser $850–$2,400 (door-buzzer-repair-orange-county-new-york). Video intercom 4–8 units $1,200–$3,500; multi-unit building $1,200–$5,000; IP/app $2,500–$8,000+ (intercom-installation-orange-county-ny). Access control single door/gate $1,700–$5,000; multi-door $4,500–$15,000; campus/complex $15,000–$50,000+ (access-control-installation-orange-county). Elevator $2,100/car L1, $3,500/car L2. 4-camera from $1,199 (price page MODELS min). Apartment-building cameras ~$500–$1,500 per camera. Cat6 drop $175+ per drop. Monitoring $30/$45. Not used (conflicting/old): intercom-repair-orange "$198–$396 diagnostic", "$150–$300 diagnostic", access-control "$195/hr callbacks" and "15% surcharge", "free written diagnostics", "free walk-through" (condo page).

### Question register additions (property-management-security-orange-county)
Checked by meaning against the full silo register plus the parallel Rockland and Putnam PM pages (2 drafts swapped after comparing: entry-panel languages ≈ Rockland; mailbox-cluster camera ≈ Rockland/Putnam).
- Q&A: Our Port Jervis building is on the city's vacant-property register. Can sensors and a camera back up the inspection the city asks for every 30 days?
- Q&A: The Newburgh rental license application asks whether the building has a fire alarm system. What should we have on file before we answer it?
- Q&A: Our Newburgh rowhouse still has its original wood front door and frame. Can an electric strike go in without replacing the door?
- Q&A: A converted Middletown house has apartments on the front entrance and a side stair. Does it need one call panel or two?
- Q&A: Families in our Kiryas Joel buildings average more than five people per apartment. How does that change the lobby door hardware?
- Q&A: Our house near Mount Saint Mary College rents by the bedroom. Should each bedroom door get its own lock or code?
- Q&A: Our office is in Goshen and our buildings are an hour apart. What can be fixed remotely before anyone drives out?
- Q&A: Rents in Newburgh are lower than the county median. How do we keep security spending in proportion to the rent roll?
- Q&A: Our buildings are spread across three electric utilities. Should outage planning differ from building to building?
- Q&A: The recorder in our walk-up's boiler room keeps failing. Where else can it go?
- Q&A: Melting snow refreezes on the threshold of our garden-building doors and the doors won't latch. Is that a hardware problem?
- Q&A: We may sell one of our Port Jervis buildings within a year. Is it worth putting in cameras and a new entry panel now?
- FAQ: Will the office get an alert if someone pries open a lobby entry panel?
- FAQ: Do card and fob readers keep working at exposed garden-building doors in winter?
- FAQ: Can a lobby panel be mounted where a wheelchair user can reach it?
- FAQ: Can part of a camera's view be blacked out so it never records a neighbor's windows?
- FAQ: In a shared student apartment, can the intercom ring every roommate's phone?
- FAQ: Can keypads at dim side entrances have lit buttons?
- FAQ: When a recorder's hard drive fills up, does it stop recording?
- FAQ: Will an old telephone-entry panel stop working if the building's landline is cancelled?
- FAQ: Can our office export a month of door events for an owner's report?
- FAQ: Can a tenant's fob be set to stop working on the last day of the lease?

### Similarity
Masked-geo 8-word shingles vs every PM sibling incl. parallel Rockland and Putnam: max containment 0.118 (Westchester), Putnam 0.083, Rockland 0.064; Jaccard ≤ 0.062. All < 0.65.

### Images (11) — all Reolink (authorized partner) product photos; no unused real job photos remained
Real job photos checked in images/cctv-installation/, access-control-installation/, intercom-repair/ (phash/dhash clustering + visual contact sheets). Every remaining scene was already on a PM page (same scenes under many filenames): Juice-bar sign dome, flag-corner dome, soffit cameras, mezzanine wall, drop-ceiling domes, storage corner, store shelving, monitor wall, gravel-lot view, back-door night view, stucco-wall mini bullet, glass-vestibule turret, stone-facade arm camera, corridor to steel door, ceiling-grid bullet. The monitor-over-snack-shelves scene was picked first, then dropped because the parallel Putnam build saved the same scene (`…putnam-county-job-photo-camera-monitor-above-shop-shelves`). Reolink images via Firecrawl image lists of reolink.com/us/product/reolink-duo-floodlight-poe/ (cache miss = not previously pulled) and home-cdn.reolink.us; RLC-1240A and RLC-81MA pages skipped (already pulled by other builders). Rejected as already used: monitor+phone detection-zone render (= Westchester), bullet on stone wall (= Westchester), storage hubs / smart display with lawn / 24/7 recorder (= Suffolk), rain/white-wall bullets (= Nassau). No faces, house numbers or "AESS".
| File (`property-management-security-orange-county-…`) | Source | Where |
|---|---|---|
| partner-photo-floodlight-camera-lamps-lit-on-wall-at-dusk | duo-floodlight-poe · 2026/01/080623293ccbd0a0180c9c77.jpg.webp | hero (eager), og/twitter |
| partner-photo-floodlight-camera-with-two-lamps-on-white-wall | duo-floodlight-poe · 2025/08/180950181755510618.767.jpg.webp | §5 county |
| partner-photo-smart-display-showing-dog-on-lawn | duo-floodlight-poe · 2025/08/180953201755510800.5959.jpg.webp | services (door hardware) |
| partner-photo-phone-app-wide-view-of-lawn-and-palms | duo-floodlight-poe · 2025/08/180940521755510052.8911.jpg.webp | services (cameras) |
| partner-photo-180-degree-screen-view-of-yard-and-pool | duo-floodlight-poe · 2025/08/180938031755509883.0309.jpg | building types (KJ) |
| partner-photo-cutaway-house-with-four-camera-icons-and-recorder | duo-floodlight-poe · 2025/08/180946501755510410.0453.jpg.webp | building types |
| partner-photo-lit-house-at-night-with-camera-cable-and-router-labels | rlc-81ma · 2025/08/040918521754299132.635.jpg.webp | working with office |
| partner-photo-floodlight-camera-parts-with-512gb-graphic | duo-floodlight-poe · 2025/12/260607442e980e0f5db76c80.jpg.webp | equipment |
| partner-photo-phone-app-night-view-of-dark-yard | duo-floodlight-poe · 2025/08/180941061755510066.0758.jpg.webp | process |
| partner-photo-house-shown-from-daylight-to-night-in-strips | duo-floodlight-poe · 2025/08/180950131755510613.5768.jpg.webp | coverage |
| partner-photo-microsd-card-with-256gb-graphic | rlc-81ma · 2025/08/040922341754299354.5495.jpg.webp | cost |
(Source URLs verified against the download map; all from home-cdn.reolink.us product-page image lists.)
DAILY-LOG note: `images: 11 partner (Reolink) product photos via reolink.com (no unused real job photos; monitor-over-shelves scene taken by parallel Putnam build)`.

### Links / FLIPs
Direct: /property-management-security-hudson-valley (up), -westchester-county, -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island, -nassau-county, -suffolk-county. FLIP comments (plain text): /property-management-security-rockland-county, -putnam-county, -dutchess-county, -ulster-county (coverage section). Orange pages linked: condo-security-systems-, co-op-security-systems-, condo-security-camera-installation-, apartment-building-security-camera-installation-, intercom-installation-orange-county-ny, intercom-repair-orange, door-buzzer-repair-orange-county-new-york, door-buzzer-installation-orange-county-ny, access-control-, elevator-access-control-, security-camera-installation-orange-county-ny, security-camera-pricing-, security-camera-repair-, parking-lot-camera-, alarm-installation-, fire-alarm-installation-orange-county-ny, structured-cabling-installation-, doorbell-camera-, smart-lock-, commercial-security-systems-orange, cctv-installation-, network-installation-, security-cameras-orange-county.

### For Anwar to confirm (CONFIRM)
- Fire alarm work stated as in scope in Orange County (as on Westchester PM page), no prices.
- Vacant-unit alarm package (contacts, motion, camera, cellular communicator where no internet) written as a service we do.
- Remote diagnostics (restart recorder, check panels online, change codes) offered for networked systems.
- Bedroom code/fob locks for by-the-room student rentals (smart lock silo).
- Wireless links between garden-complex buildings and pole-mounted cameras for mailbox areas.
- "Book the visit a week or two ahead of a rental license/permit inspection" scheduling suggestion.


## Putnam County (property-management-security-putnam-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page: up-link /property-management-security-hudson-valley, phone (845) 640-3835 (body, CTAs, sticky bar, schema; 800 only in shared header), GBP Bronx (460 E Fordham Rd, `#bronx`), start price $250 service call (START_PRICES). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used.

Thin-page check (done first): PASSED, page built. Putnam is ~83% owner-occupied, but there is enough distinct, sourced landlord material: ACS tenure by town/village (Brewster village 79% renter), structure mix (mostly 2–4 unit buildings), 1,757 seasonal units and the 1928 lake colonies, Carmel's 2025 accessory-apartment law (§156-15), Cold Spring/Philipstown short-term-rental rules (incl. the 20-minute response draft, Oct 2026), town alarm laws (Carmel Ch. 37 15-min cutoff; Patterson false-alarm fines; Putnam Valley/Southeast permits), county contractor registration vs state Article 6-D licensing, NYSEG Brewster Division storm outages (July 4 2026), Sheriff's Dark House Check.

Thesis (distinct from the HV hub — distance/routing, garden complexes, six counties; from Westchester — ETPA, lead registry, towers; from the Putnam co-op page — tiny single-building co-ops with volunteer officers; and from the Putnam condo page — 55+ owners, caregivers, amenity buildings): Putnam property management is small-landlord work — Brewster Main Street walk-ups over shops, Carmel/Mahopac hamlet buildings, owner-occupied houses with accessory apartments, winterized lake-colony cottages, Philipstown village rentals and STR hosts — so the page is about separating two households in one house, seasonal changeovers, links to outbuildings, power/outage protection, town alarm rules and licensing layers, not enterprise access platforms.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| PT1 | `Putnam County NY renter-occupied housing units percent census Carmel Brewster` · WebSearch → WebFetch (PDF) | https://pad.human.cornell.edu/profiles/Putnam.pdf | Cornell PAD profile, ACS 2011–2015: 38,289 units; renter-occupied 6,144 (18.0%). Superseded by PT2 (newer); NOT quoted on page. | — |
| PT2 | census-gov `census/data` acs/acs5 2023 · Firecrawl Alexandria (api.census.gov direct = proxy 403 / key required) | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&ucgid=0500000US36079 ; …group(B25004)… ; …group(B25002)… | Putnam County ACS 2019–2023: occupied 35,054; owner 29,105; renter 5,949; total units 38,369; vacant 3,315; seasonal/recreational/occasional 1,757. | §County paras 1, 4; facts list; AI check #5 context |
| PT3 | same provider, county subdivisions of Putnam | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&for=county%20subdivision:*&in=state:36%20county:079 | Renter/occupied: Carmel 1,879/11,945 (seasonal 403); Kent 589/4,641 (259); Patterson 628/3,666 (113); Philipstown 880/3,878 (384); Putnam Valley 425/3,985 (451); Southeast 1,548/6,939 (147). | §County paras 3–4; town table; coverage cards |
| PT4 | same provider, places in NY (filtered) | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&for=place:*&in=state:36 | Brewster village 775/977 renter; Carmel CDP 695/2,806; Mahopac CDP 709/3,403; Lake Carmel CDP 385/2,907; Cold Spring village 301/835 (97 seasonal); Nelsonville 69/250; Brewster Hill CDP 40/929. | §County para 3; facts list; town table; FAQ (Brewster Hill) |
| PT5 | same provider, B25024 units in structure, Putnam County | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36079 | Total 38,369: 1-detached 29,826; 1-attached 3,076; 2 units 1,684; 3–4 1,024; 5–9 987; 10–19 573; 20–49 568; 50+ 372; mobile 246. | §County paras 1, 3; facts list; AI check #1 |
| PT6 | `Brewster village NY renter occupied percent housing units census` · Firecrawl search | https://data.census.gov/table/ACSDT5Y2024.B25003?g=160XX00US3608070 ; http://censusreporter.org/profiles/16000US3608070-brewster-ny/ | ACS 2024 5-yr: Brewster 877 renter of 1,115 (~79%). Cross-check only; page uses the 2023 vintage (PT4) for consistency. | — |
| PT7 | `Town of Carmel NY accessory apartment law rental permit code` · WebSearch → Firecrawl scrape | https://haven-adu.pages.dev/city-guideline/carmel-ny/ (cites https://www.townofcarmelny.gov/DocumentCenter/View/767/NEW-TOC-ZONING-CODE-2025 and the Putnam DOH accessory apartment form) | Carmel §156-15 (L.L. 1-2025; code update adopted June 2025): ADUs by right in LDR/MDR single-family detached; one per property; within the house or a pre-existing accessory building ≤500 ft away; one front entrance, extra entrances on the side; owner must live in house or ADU; short-term rental prohibited; Putnam County DOH water/sewage approval before building permit; 3-year permit then annual renewal with owner-occupancy certification; ADU removed within 30 days if owner vacates. (Secondary summary of primary town code; primary PDF not fetched.) | §Rental types (accessory apartments); facts list; rules list; Q&A side entrance; FAQ removal; AI check #2 |
| PT8 | `Village of Cold Spring short-term rental law permit Chapter 100` · Firecrawl search → scrape (directQuote) | https://highlandscurrent.org/2022/05/20/cold-spring-to-revise-str-law/ | May 20 2022: Mayor Kathleen Foley — only four permit applications; about 35 STRs operate in the village; quote "it's not working." | §Rental types (Cold Spring) |
| PT9 | `Cold Spring village short-term rental permit law 2023 2024 …` · Firecrawl search (site highlandscurrent.org) → scrape | https://highlandscurrent.org/2026/02/20/registration-lax-on-short-term-rentals/ | Feb 20 2026: Cold Spring enacted STR law in 2021, began review three years later; mayor says updating STR code is a priority for 2026; Philipstown discussing annual permits/inspections and a party ban. | §Rental types (Cold Spring); rules list |
| PT10 | same search → scrape PDF (directQuote) | https://highlandscurrent.org/wp-content/uploads/2026/10/10-09-26.pdf | Oct 9 2026 issue: Philipstown draft STR rules — owner or representative must respond within 20 minutes; STRs limited to zones allowing single-family homes, in 1–2 family dwellings or accessory apartments with a CO; permit renewable every two years; $90 application, $100 Building Department inspection; hearing continued to November. | facts list; §Rental types (Cold Spring); §Working (STR hosts); Q&A 20-minute; AI check #6 |
| PT11 | `Lake Carmel Putnam Lake summer colony bungalows …` · Firecrawl search → scrape (directQuote) | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Three communities from 1928 (Lake Carmel/Kent, Lake Peekskill/Putnam Valley, Putnam Lake/Patterson) as summer-bungalow communities on man-made lakes; Putnam Lake 11,000 lots mapped, 20'×100' lots, 2,000 homes by 1932. | §County para 4; facts list; §Rental types (lake cottages) |
| PT12 | same search → scrape | https://en.wikipedia.org/wiki/Lake_Carmel_(New_York) | Lake Carmel cottages built as weekend/summer homes; postwar year-round exurb; cottages "expanded and winterized". | §Rental types (lake cottages) |
| PT13 | `Putnam County NY home improvement contractor license Consumer Affairs $300 two-year` · Firecrawl search → scrape | https://www.putnamcountyny.gov/consumer-affairs ; https://www.putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/Home%20Improvement%20New%20First%20Time%20Application%201-28-2025.pdf ; https://www.putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/homeimprovement/Home%20Improvement%20First%20Time%20Application%201-9-2023.pdf | "mandatory contractor registration program to assure that all contractors who work on residential properties in Putnam County are insured, bonded and have workers' compensation insurance"; $300 covers two-year registration (application excerpt). | §Working (licensing); rules list; Q&A registration; AI check #4 |
| PT14 | reused, research/co-op-security-systems.md PU7 | https://www.putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/electrical/2025/5_L_Low%20Voltage%20and%20Limited%20Data%20Comm%20Tech%20Application%20STEP%20ONE_04%2030%202025.pdf | Board of Electrical Examiners low-voltage/limited data comm tech license; "does not include installation of Fire & Burglar Alarm Systems, CCTV and Access Control as that is licensed by the state" (Article 6-D). | §Working (licensing); rules list; Q&A registration; AI check #4 |
| PT15 | reused, co-op PU25 | https://dos.ny.gov/security-or-fire-alarm-installer-license-law | DOS Article 6-D license to install/service/maintain security or fire alarm systems. | §Working (licensing); rules list |
| PT16 | `Putnam County NYSEG outages … 2025 OR 2026 news` · Firecrawl search → scrape (directQuote) | https://news.halstonmedia.com/mahopac-news/mahopac-news/stories/westchester-north-salem-yorktown-bedford-somers-lewisboro-storm-july-4,86693 | Mahopac News, July 5 2026: NYSEG Brewster Division serves parts of Dutchess, Putnam, Westchester; ~25,000 outages at peak, 234 downed lines, 31 broken poles; Patterson and Southeast among hardest hit. | facts list; §Services (power); AI check #5 |
| PT17 | reused, co-op PU11 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 2020 Isaias: 34,150 of 38,693 NYSEG Putnam customers out. | §Services (power); AI check #5 |
| PT18 | same outage search (excerpt) | https://poweroutage.us/area/county/822 ; https://outagebulletin.com/new-york/outage/nyseg-rge-1749485/nyseg-rge-putnam-county-2026-11-26/ | poweroutage.us tracks 44,846 Putnam customers; Nov 26 2026 NYSEG outages listed in Putnam. Used only to support "most of Putnam is served by NYSEG" (38,693 of ~44,846). | §Services (power) |
| PT19 | `ecode360 5066448` · Firecrawl scrape (directQuote) | https://ecode360.com/5066448 | Carmel Ch. 37 Alarm Devices and Systems (L.L. 6-1992): alarm permit; external audible/visible alarm must have automatic cutoff within 15 minutes; dialers must go to a central station/answering service; fines per false alarm on a schedule set annually by Town Board resolution. | §Services (alarms); rules list; FAQ siren |
| PT20 | reused, co-op PU17 | https://mail.pattersonny.org/PDFs/Codes/Chapter43-Alarms.pdf ; https://ecode360.com/9473178 ; https://ecode360.com/9063548 | Patterson fines properties with >2 false alarms in 12 months; Putnam Valley permit before installing an alarm calling the FD; Southeast annual permit. Fee amounts not used. | §Services (alarms); rules list; Q&A Patterson |
| PT21 | `Putnam County Sheriff dark house check` · Firecrawl scrape (directQuote) | https://putnamsheriff.com/dark-house-check/ | Dark House Check for residents away for an extended period; extra patrols and exterior checks for forced entry; deputies attempt to contact the homeowner. | §Rental types (lake cottages) |
| PT22 | reused, co-op PU9 / PU10 | https://putnamcountyny.gov/images/Departments/Planning_Dev_Transport/PDF_Documents/chapter3.pdf ; …/chapter4.pdf | County Main Street study: Brewster "a long established mixed-use Main Street, with a Metro North train station at its terminus"; doorway to a staircase up to a second-floor apartment above street-level businesses. | §Rental types (Main Street walk-ups) |
| PT23 | reused, co-op PU4 | https://www.putnamcountyny.gov/component/zoo/item/all-aboard-next-stop-putnam-county?Itemid=591 | Harlem Line: Brewster, Southeast, Patterson; Hudson Line: Cold Spring, Garrison. | §Services (intercom, commuters); coverage cards |
| PT24 | reused, co-op PU8 | https://hudsonvalley.news12.com/police-make-3-arrests-in-carmelmail-thefts | News 12 HV, Dec 2022: three arrests; car stopped near Route 6N in Mahopac; occupants appeared to be stealing mail. No names used. | §Services (cameras, mail); maintenance route (Route 6N) |
| PT25 | reused, co-op PU16 | https://highlandscurrent.org/2025/08/08/the-history-patrol/ | Cold Spring HDRB reviews exterior changes visible from the street in the historic district (since 1976). | §Rental types (Cold Spring); rules list |
| PT26 | reused, co-op PU5 | https://www.putnamhousing.com/gleneida-senior-apartments-get-started/ | PCHC senior complex: "A two-story garden apartment complex with 24 units". Complex not named on page. | §Rental types (senior and affordable) |
| PT27 | reused, silo HV8 / co-op PU20 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 covers all towns and villages and cities <325,000. | §County para 5; rules list |
| PT28 | reused, silo S6 / co-op PU22 | https://intro.nyc/local-laws/2021-63 | TDPA = NYC Local Law 63/2021 (city only). AI-check item using it was cut when trimming to the word limit — NOT used. | — |
| PT29 | reused, silo S11 / co-op PU24 | https://cooperatornews.com/article/qa-camera-placement | Audio recording / NY eavesdropping caution. | §Working (footage) |
| PT30 | Wikipedia structured contents (Alexandria `wikipedia/articles/structured-contents`) | https://en.wikipedia.org/wiki/Putnam_County,_New_York | Transportation: I-84 enters near Ludingtonville and connects to I-684 in Southeast; Taconic State Parkway north–south through central Putnam; NY 52 ends at US 6 south of Carmel; US 6 joins US 202 east of Brewster; historic turnpike route ≈ Route 301 from Cold Spring. | §Working (maintenance routes); coverage card Southeast |
| PT31 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-putnam-county-new-york ; /intercom-installation-putnam-county-ny ; /access-control-installation-putnam-county ; /security-camera-pricing-putnam-county ; /security-camera-installation-putnam-county-ny ; /alarm-installation-putnam-county ; /structured-cabling-installation-putnam-county | Prices used — see below. NOT used: /intercom-repair-putnam-county diagnostic $218–$435 and its ×1.45 lines, $195/hr return visits (conflict with $250 / rules); access-control page's "25% HV surcharge" and $195/hr callbacks; intercom page's "free on-site quote"; any "same-day" wording on the buzzer page. | hero quick answer; services; cost table |
| E1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing-DDG for "property management security Putnam County" | — | EMPTY (not accessible in build env). AI-check section paraphrases common generic claims; no AI or Reddit quote invented. | — |
| E2 | `Brewster village apartments development Main Street rezoning new rental units Putnam` · Firecrawl search | (Facebook group posts, listing sites only) | No usable primary source for new Brewster rental construction — NOT used. | — |
| E3 | `Village of Brewster rental housing registration inspection law` · WebSearch → Firecrawl scrape | https://ecode360.com/39811921 | Turned out to be Village of Sands Point Ch. 127 (Nassau), not Brewster — NOT used. No Brewster rental-registration law found. | — |
| E4 | `api.census.gov` direct (curl) | — | EMPTY (not accessible in build env — proxy 403; Firecrawl fetch returned "Missing Key"); used the Alexandria census provider instead (PT2–PT5). | — |

### Prices used (all already published on Putnam pages)
$250 service call · apartment station $250–$525 · relay/button $250–$475 · transformer $325–$650 · strike with alignment $450–$950 · panel/faceplate $650–$1,800 · riser $850–$2,400 (door-buzzer-repair-putnam-county-new-york) · residential intercom $500–$2,500; video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP/app $2,500–$8,000+ (intercom-installation-putnam-county-ny) · single door/gate $1,900–$6,000; multi-door $5,000–$18,000; full property $18,000–$50,000+ (access-control-installation-putnam-county) · four-camera system starting at $1,199 (security-camera-pricing-putnam-county A series; security-camera-installation-putnam-county-ny) · basic residential alarm starting at $600; monitoring $30/$45 (alarm-installation-putnam-county) · Cat6 data drop $175 and up (structured-cabling-installation-putnam-county). Wisetack only as "Financing is available through Wisetack, subject to approval." Elevator prices not used (few elevator rentals in Putnam).

### Question register additions (property-management-security-putnam-county)
Checked against every question on the 13 PM pages on disk (incl. parallel Rockland and Orange) with check_page.parse (no masked duplicates) and by meaning against the silo register and the Putnam co-op/condo registers. Dropped drafts that overlapped: private-road directions (co-op Putnam), gloves on keypads (co-op Putnam), rock between buildings (condo Putnam), tenant doorbell cameras / owner-vs-tenant views (Staten Island), basement-apartment exit lock (Nassau), battery-backup worth it (Suffolk), farmhouse without cable internet (Suffolk), deer false alerts (Westchester), sales tax (Westchester), phone number per county (Nassau/Suffolk).
- Q&A: A tenant rents the accessory apartment in a Carmel house, and the town's rules keep a single front entrance. How does the tenant get an entry of their own?
- Q&A: Can visitors at a shared front door ring the accessory apartment without also ringing the owner?
- Q&A: The converted garage apartment behind our Mahopac house is out of Wi-Fi range. How should it connect to the main house's system?
- Q&A: The bungalows we rent around Putnam Lake sit on narrow lots, close to the neighbors. Where can cameras go without looking into the house next door?
- Q&A: A lake cottage alternates between weekly summer guests and a winter tenant on a lease. What has to change on the system when the lease starts?
- Q&A: Philipstown's draft short-term rental rules would require an owner or representative to respond within 20 minutes. What can the equipment handle, and what still needs a person?
- Q&A: Our Putnam Valley rental sits in a hollow with a weak cell signal. How do we find out before buying whether a cellular camera will connect?
- Q&A: Our Brewster building's stair door opens straight onto Main Street between two shops. Where does the call panel go when the entry is only a doorway wide?
- Q&A: Do wireless cameras work through the thick stone walls of older Cold Spring buildings?
- Q&A: Our Southeast complex has a standby generator. Which security devices belong on it?
- Q&A: A rental we manage in Patterson has had three false alarms this year. What does the town's alarm law mean for us, and how do we stop the next one?
- Q&A: Is a Putnam County home improvement registration enough for the company that installs our cameras and alarms?
- Q&A: Our rental houses share a row of mailboxes at the end of the road. Can a camera watch them without running power all the way down the hill?
- Q&A: A tenant bought their own camera for the apartment they rent from us. Will you install it?
- FAQ: Can cameras be mounted on cedar shingles or fieldstone without damaging them?
- FAQ: Do you cover the hamlets along the Connecticut line, such as Putnam Lake and Brewster Hill?
- FAQ: Can the accessory apartment's side door take a keypad lock that the owner can reset between tenants?
- FAQ: Should a rental with outdoor cameras tell tenants and visitors that it records?
- FAQ: Is financing available for a landlord with only one or two Putnam rentals?
- FAQ: What happens to the apartment's keypad and doorbell if a Carmel accessory apartment stops being a rental?
- FAQ: If a rental's internet goes out, does the recorder keep saving video?
- FAQ: Does a homeowners association have to approve a doorbell camera on a rented townhouse?
- FAQ: How quickly is a visit to a Putnam rental booked after we call?
- FAQ: How long can an outdoor alarm siren sound at a rental in the Town of Carmel?

### Similarity (masked geo; 8-word shingle share / difflib word-sequence ratio)
Westchester 0.100 / 0.298 (max) · Orange (parallel) 0.080 / 0.253 · Rockland (parallel) 0.050 / 0.173 · HV hub 0.038 / 0.136 · NYC 0.027 / 0.116 · LI 0.029 / 0.109 · Suffolk 0.031 / 0.104 · Nassau 0.029 / 0.098 · SI 0.026 / 0.092 · Queens 0.026 / 0.082 · Brooklyn 0.025 / 0.081 · Bronx 0.025 / 0.080 · Manhattan 0.025 / 0.066 · condo Putnam 0.026 / 0.073 · co-op Putnam 0.028 / 0.064. All < 0.65.

### Images (11: 5 real job photos + 4 Lorex + 2 Reolink partner product photos)
WebP (quality 80, max 1200 px) in images/property-management-security/. Library scenes were checked visually (contact sheets) and by 16×17 dHash against every file in images/property-management-security/ (incl. parallel Rockland/Orange) — min Hamming 62/256. Two first picks were dropped as same scene as existing PM photos: cctv-installation-putnam-county-storeroom-dome-above-leaning-trim-boards (same storeroom as Suffolk's "dome-camera-high-in-stained-storage-room-corner") and cctv-installation-putnam-county-bullet-over-hallway-door-frame (likely same ceiling bullet as Rockland's "bullet-camera-on-ceiling-mount-in-drop-tile-grid"). Also avoided: Putnam lot/brick-wall tile (= Nassau), awning dome with bare trees (= Nassau fascia), soffit camera (= Nassau), showroom mezzanine (= Nassau), glass vestibule turret (= Rockland), Akuvox/Axis intercom-repair product shots (not partner brands). No faces, plates, house numbers, readable documents or "AESS".
| File (property-management-security-putnam-county-…) | Source | Where |
|---|---|---|
| job-photo-corner-dome-camera-above-motion-sensor | images/cctv-installation/cctv-installation-putnam-county-wall-corner-dome-and-motion-sensor.webp | hero (eager), og/twitter |
| lorex-partner-photo-white-turret-camera-under-dark-roof-edge | Lorex (partner) · lorex.com/products/e842cd-4k-ip-wired-dome-camera asset https://cdn.lorex.com/images/products/E842CD/E842-weatherproof.jpg | §County |
| job-photo-ceiling-camera-near-lit-exit-sign | images/access-control-installation/access-control-installation-morris-heights-camera-and-lit-exit-sign-in-lobby-ceiling.webp | §Services (doors/exit) |
| job-photo-camera-monitor-above-shop-shelves | images/access-control-installation/access-control-installation-melrose-camera-monitor-above-shop-shelves.webp | §Services (cameras) |
| reolink-partner-photo-wide-angle-camera-beside-solar-panel | Reolink (partner) · reolink.com/us/product/argus-4-pro/ asset https://home-cdn.reolink.us/wp-content/uploads/2024/06/argus-4-pro-whitesolar-panel-2-white.png | §Services (mail) |
| lorex-partner-photo-white-video-doorbell | images/access-control-installation/access-control-installation-eastchester-white-video-doorbell-with-lit-bell-ring.webp (Lorex product photo) | §Services (doorbells) |
| reolink-partner-photo-wide-angle-camera-on-gray-siding | Reolink · argus-4-pro page asset https://home-cdn.reolink.us/wp-content/uploads/2024/06/070424371717734277.7248.jpg | §Rental types (lake cottages) |
| job-photo-recorder-screen-with-camera-tiles-and-channel-table | images/cctv-installation/cctv-installation-putnam-county-recorder-spare-channels-and-zero-bitrate-columns.webp | §Equipment |
| job-photo-recorder-view-of-sidewalk-and-curb | images/access-control-installation/access-control-installation-indian-village-recorder-screen-view-of-sidewalk-and-curb.webp | §How it works |
| lorex-partner-photo-white-indoor-cube-camera-on-stand | images/access-control-installation/access-control-installation-marine-park-white-indoor-cube-camera-on-stand.webp (Lorex) | §Coverage |
| lorex-partner-photo-white-bullet-camera-with-spotlight | images/access-control-installation/access-control-installation-gowanus-white-spotlight-bullet-camera-product-photo.webp (Lorex) | §Packages |
Counts: 5 real job photos + 4 Lorex + 2 Reolink = 11. Three Lorex library photos are small (151–286 px wide).
DAILY-LOG note: `images: 5 real job photos (2 images/cctv-installation/, 3 images/access-control-installation/) + 4 Lorex + 2 Reolink partner product photos`.

### FLIPs on the page (plain text + `<!-- FLIP: /slug -->`)
/property-management-security-rockland-county, -orange-county, -dutchess-county, -ulster-county (coverage section). Linked live: /property-management-security-hudson-valley (up, ×3), -westchester-county, -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island, -nassau-county, -suffolk-county; Putnam condo/co-op hubs and Putnam service pages.

### Links left for the main run
Back-links needed from every live PM page (all 11) and the parallel Rockland/Orange pages; HV hub must flip its Putnam card FLIP to a live link; Westchester must flip its Putnam FLIP. Suggested contextual back-links: /condo-security-systems-putnam-county, /co-op-security-systems-putnam-county, /intercom-installation-putnam-county-ny, /access-control-installation-putnam-county, /door-buzzer-repair-putnam-county-new-york, /smart-lock-installation-putnam-county, /doorbell-camera-installation-putnam-county.

### For Anwar to confirm (CONFIRM)
- "Booked within 2 hours … seven days a week" and "technician arrives within that window, never earlier" (FAQ) — from sibling pages and the crew rule.
- Coverage of all six Putnam towns + three villages incl. hamlets on the Connecticut line (FAQ).
- Mounting method on cedar shingles / fieldstone (backing block, mortar-joint anchors) (FAQ).
- Labor-only install of a tenant-bought camera with the owner's approval (Q&A) — matches the owner-supplied equipment rule; not seen on siblings for tenant-bought gear.
- "We program the Carmel 15-minute siren cutoff … town's alarm permit stays in the owner's name" (FAQ).
- Point-to-point wireless links, fiber between buildings, solar cameras, cellular signal testing on site — written as services we do.
- Site survey for new systems/lists is NOT called free (HV hub and Putnam intercom page say "free"; left out per rules).
- 30-day workmanship warranty deliberately omitted (Westchester page has it); only the one-year parts-only sentence + paid add-on.


## Dutchess County (property-management-security-dutchess-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page · up-link /property-management-security-hudson-valley · phone (845) 640-3835 (body, CTAs, sticky bar, schema; 800 only in shared header) · GBP Bronx (`#bronx`, 460 E Fordham Rd) · start price $250 service call (START_PRICES). Format: exact query · platform · URL · finding · section used.

**Thin-page check: PASSED.** Dutchess has distinct, sourced landlord material: a renting county with renting cities (ACS: 31% rented countywide, ~61% City of Poughkeepsie, ~41% Beacon), ~39% pre-1940 stock in both cities, the county's own annual Rental Housing Survey of complexes (unit counts and vacancy by municipality: Town of Poughkeepsie, Fishkill, Wappinger, City, Hyde Park, Beacon), Beacon's landlord registration / 15-mile managing-agent law, City of Poughkeepsie February vacancy statement + vacant/foreclosed building registration and $5,000 bond, the 12601 lead rental registry, Good Cause adoptions (City, Beacon, Town of Poughkeepsie), the voided City ETPA, Marist/Bard off-campus housing (Vassar 99% on campus), municipal alarm laws, July 2026 storm outages.

Thesis (kept apart from HV hub = six-county routing/weather; Putnam = small owner-occupied/lake rentals; Orange = Newburgh/Middletown/Port Jervis rental laws; Rockland = county MDRR registry; Ulster = Kingston ETPA/STR; co-op & condo Dutchess = boards): Dutchess landlords and managing agents split between pre-1940 small city buildings (Poughkeepsie two/three-families, Beacon walk-ups) and full Route 9 garden complexes (Town of Poughkeepsie, Fishkill, Wappinger), with student turnover near Marist/Bard and city paperwork (Beacon managing agent, Poughkeepsie vacancy statement, vacant-building permits, lead registry, Good Cause access) shaping how and when work is scheduled.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| DP1 | ACS 2023 5-year B25003, B25034, B25064, B25024 for county 36027 and places 3659641, 3605100 · Firecrawl Alexandria provider census-gov (census/data) | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&ucgid=0500000US36027 (+ B25034/B25064/B25024; ucgid 1600000US3659641, 1600000US3605100) | Dutchess: 115,184 occupied / 35,900 renter; 122,636 units / 22,056 built ≤1939; median gross rent $1,522; units in structure 2: 7,441; 3–4: 9,135; 5–9: 6,522; 10–19: 4,379; 20–49: 3,190; 50+: 4,118. City of Poughkeepsie: 13,442 / 8,174 renter; 14,254 units / 5,603 ≤1939; rent $1,370; 2: 2,302; 3–4: 2,757; 50+: 1,727. Beacon: 6,320 / 2,562 renter; 6,658 / 2,617 ≤1939; rent $1,675 | County §paras 1–2; facts list; county table; rental types (city houses, downtown); AI check none |
| DP2 | `Dutchess County Housing Needs Assessment renter households rental vacancy rate multifamily apartments Route 9` · Firecrawl search → Firecrawl scrape (PDF, directQuote) | https://www.dutchessny.gov/Departments/Planning/Docs/2024-Rental-Housing-Survey-Report.pdf | 2024 Rental Housing Survey: 149 complexes contacted, 89 responded (60%), 10,128 units, complexes of 20+ units; market-rate vacancy 1.6% (125 of 8,028); 2023 2.1%, 2022 2.1%, 2021 0.6%, 2020 0.9%; below 5% for over 25 years (search excerpt); market-rate units by location: Town of Poughkeepsie 2,177 (27.1%), Town of Fishkill 1,830 (22.8%), Town of Wappinger 1,395 (17.4%), City of Poughkeepsie 950 (11.8%), Hyde Park 673 (8.4%), Beacon 129 (1.6%); vacancy Beacon 0.0%, City 2.1%, East Fishkill 1.4%, Fishkill 1.0%, Hyde Park 1.9%, Town of Pok 2.0%, Wappinger 0.7%; avg 2BR Beacon $3,373, City $2,252, Fishkill $2,443, Town Pok $2,253, Wappinger $2,352; 1BR +6.4%, 2BR +11.1%, 3BR +7.6% 2023–24; tax credit/inclusionary complexes listed separately (names not used) | County paras 3–4; facts list; county table; rental types (Route 9, Fishkill/Wappinger, Beacon, subsidized) |
| DP3 | same search (excerpt) | https://www.fishkill-ny.gov/uploads/3/8/0/7/38072219/comprehensive_plan_combined_volumes.pdf | Town of Fishkill Comprehensive Plan Update: 6 market-rate complexes, 1,791 apartments, 82.7% 1–2 BR; 0% vacancy (citing 2021 county survey) | County para 3 |
| DP4 | `City of Beacon NY rental registry law landlords register rental units inspection` · Firecrawl search → Firecrawl scrape (directQuote) | https://ecode360.com/38637192 | Beacon Code Ch. 173 Art. II: owner of non-owner-occupied property files sworn Landlord Registration Statement; if owner not within 15-mile radius, managing agent = natural person 18+ residing within 15 miles, written consent; changes in ownership/agent within 15 days; review within 3 business days; copy annexed to tenant agreements; permit fee once every three years | County para 6; facts list; Working-with "Beacon's registration statement"; rules list; Q&A (Beacon agent leaving); AI check #6 |
| DP5 | same search → Firecrawl scrape (directQuote) | https://beaconny.gov/index.php/departments/community-resources/housing-resources/ | Beacon opted into Good Cause Aug 19 2024; exemptions (345% FMR, small landlords of one unit); grounds include "Unreasonable refusal of access for necessary repairs"; all landlords must register; STR must be owner's primary residence and permitted (§223-26.5) | Working-with "Good Cause"; rules list; AI check #6 |
| DP6 | `City of Poughkeepsie Good Cause Eviction law adopted Common Council 2024 OR 2025` · Firecrawl search (excerpts) | https://www.nysar.com/advocacy/new-york-states-good-cause-eviction-law/ ; https://housingjusticeforall.org/poughkeepsie-becomes-3rd-city-to-opt-into-good-cause/ | NYSAR: Poughkeepsie (City) adopted July 2024; Beacon August 2024; Poughkeepsie (Town) April 2025. HJ4A: "On June 18, 2024 the Poughkeepsie Common Council voted to adopt the Emergency Tenant Protection Act" | County para 6; Working-with Good Cause; rules list; AI check #2 |
| DP7 | reused, research/apartment-building-security-camera-installation.md (HCR page query scrape) | https://hcr.ny.gov/rent-stabilization-and-emergency-tenant-protection-act | Poughkeepsie ETPA adopted Jun 18 2024, voided Nov 22 2024 (Dutchess Sup. Ct.) | rules list; AI check #2 |
| DP8 | `ecode360 City of Poughkeepsie code rental dwelling units registration multiple dwelling inspection periodic` · Firecrawl search → Firecrawl scrape (directQuote) | https://ecode360.com/27006425 | City of Poughkeepsie Ch. 6 Art. I: applies to rental properties with 4+ residential units; owner/property manager files sworn statement by Feb 20 (baseline Feb 1): total units, sizes, occupants per unit, vacant available/unavailable and reasons; discrepancies found at inspections incl. fire department tri-annual inspection (§8-23); fines $500–$2,000 per unit, each month a separate violation. Vacant structures registered within 30 days; foreclosed/foreclosing registered; renewed every six months; out-of-county owner names property manager; vacant property permit valid six months; $5,000 cash bond | County para 6; facts list; Working-with (Feb statement; vacant/foreclosed); rules list; Q&A (fire department inspection; vacancy statement) |
| DP9 | `City of Poughkeepsie rental dwelling registration inspection law landlords certificate of occupancy rental permit` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.dutchessny.gov/Departments/DBCH/Rental-Registry-Program.htm | City of Poughkeepsie 12601, 2+ units, built before 1980: register, lead safety certificate; lead inspection each unit (visual paint/soil check, dust wipe); certificate renewed every three years | County para 6; Working-with "Lead-safe registry days"; rules list; Q&A (lead-safe mounting) |
| DP10 | `Vassar College percent of students live on campus residential college housing` · Firecrawl search (excerpt) | https://www.collegedata.fyi/schools/vassar-college/2024-25 | Vassar Common Data Set 2024-25: 99% live in college-owned, -operated or -affiliated housing (secondary site reproducing CDS) | County para 5 |
| R1 | reused smart-lock Dutchess D10 | https://www.marist.edu/admission/intl/orientation/rental-housing | Marist: graduate students live off campus, in complexes and private homes throughout Poughkeepsie | County para 5; rental types (students) |
| R2 | reused smart-lock Dutchess D9 | https://en.wikipedia.org/wiki/Marist_University | Main campus on US 9, Town of Poughkeepsie | County para 5; Q&A (Marist house) |
| R3 | reused smart-lock Dutchess D11 | https://www.bard.edu/reslife/offcampus/ | Majority of off-campus Bard students live in Red Hook, Tivoli or Rhinebeck | County para 5; rental types; coverage card |
| R4 | reused co-op Dutchess D7 | https://www.dutchessny.gov/Departments/County-Executive/Severe-Summer-Storm-Wreaks-Havoc-Across-Dutchess-County.htm | July 4 2026 storm: Central Hudson 33,000+ outages, NYSEG 7,400+; worst City/Town of Poughkeepsie, East Fishkill, LaGrange, Beekman, Union Vale, Pawling | facts list; services (power); AI check #5; coverage card (eastern towns); Q&A (gate) |
| R5 | reused co-op Dutchess D4 | https://ecode360.com/7062505 | Beacon Ch. 77: alarm user permit from Police Department; false-alarm schedule to revocation; residential notifications include attempted central-station callback before police | services (alarms); rules list; Q&A (Beacon callback) |
| R6 | reused condo Dutchess DC-A1 | https://ecode360.com/8298811 | Village of Fishkill: permit revoked at 10+ avoidable alarms in a permit year | services (alarms); rules list; coverage card |
| R7 | reused condo Dutchess DC-A2 | https://ecode360.com/7070191 | Town of East Fishkill: separate alarm registration per alarm site | services (alarms); rules list; coverage card |
| R8 | reused co-op Dutchess D10 | https://ecode360.com/6320489 | Town of Poughkeepsie Ch. 91 (L.L. 1-2026): permit to install/alter wiring for light, heat or power | services (cabling); AI check #4 |
| R9 | reused co-op Dutchess D5 | https://ecode360.com/7063677 | Beacon Ch. 134: alteration excludes minor, accessory, utility or security-related changes that do not substantially detract | rental types (Beacon) |
| R10 | reused co-op Dutchess D8 | https://www.dutchessny.gov/Departments/Sheriff/Academy-Recruits-Help-Apprehend-Larceny-Suspect.htm | Dec 2025 Parker Ave porch package theft; doorbell footage helped (no names) | services (cameras) |
| R11 | reused co-op Dutchess D9 | https://hudsonvalley.news12.com/police-porch-pirates-arrested-in-connection-with-package-larcenies-in-poughkeepsie | Dec 2024 two arrests, porch thefts on South Hamilton Street (no names) | services (cameras) |
| R12 | reused smart-lock Dutchess D8 | https://www.nysenate.gov/legislation/laws/RPA/768 | RPAPL 768: changing entrance lock without supplying a key unlawful | services (locks); rules list |
| R13 | reused silo PV7 / co-op D12 | https://www.nysenate.gov/legislation/laws/MRE/3 | MRL §3 applies to cities <325,000 and all towns/villages | County para 7; rules list; AI check #1 |
| R14 | reused silo S6 / co-op D14 | https://intro.nyc/local-laws/2021-63 | TDPA = NYC local law, class A multiple dwellings | AI check #1 |
| R15 | reused silo PV4 | https://codes.iccsafe.org/content/NYSPMC2025P1/chapter-3-general-requirements | PMCNYS §304.18.1 deadbolts on rented units | services (locks: deadbolts are locksmith territory) |
| R16 | reused silo PV5 | https://www.nysenate.gov/legislation/laws/RPP/235-B | RPL §235-b warranty of habitability | rules list |
| R17 | reused silo HV15 / co-op D13 | https://www.nysenate.gov/legislation/laws/GBS/69-M | State licensing of security/fire alarm installers | rules list; AI check #4 |
| R18 | reused Rockland R13 | https://www.nysenate.gov/legislation/laws/GBS/395-B | No viewing devices in bathrooms etc. | services (cameras); rules list |
| R19 | reused silo S11 | https://cooperatornews.com/article/qa-camera-placement | Audio recording / eavesdropping caution | services (cameras) |
| R20 | reused Rockland R12 / condo DC-G7 | https://udigny.org/resources/nys-code-rule-753/ | Code Rule 753: notice 2–10 working days before digging | services (cabling) |
| R21 | reused silo S12 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | "Normal Range: $1,200 - $8,500" | AI check #3 |
| R22 | industry standard (TIA-568, as on site cabling pages) | — | ~100 m channel limit | services (cabling) |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-dutchess-county-new-york; /intercom-installation-dutchess-county-ny; /access-control-installation-dutchess-county; /elevator-access-control-installation-dutchess-county; /security-camera-pricing-dutchess-county; /structured-cabling-installation-dutchess-county; /alarm-installation-dutchess-county | Prices used — below | hero quick answer; services; cost table |
| E1 | Reddit / Google PAA / PASF / Answer the Public / AI Overview / Yelp 1–3★ / Bing–DDG for "property management security Dutchess County" | — | EMPTY (not accessible in build env). AI check corrects claims typical of chatbot/cost-guide answers; no AI or Reddit quote invented | — |

### Prices used (all already published on Dutchess pages)
$250 service call (START_PRICES; buzzer repair page) · station $250–$525 · relay/button $250–$475 · transformer $325–$650 · strike $450–$950 · lobby panel/faceplate $650–$1,800 · riser $850–$2,400 (/door-buzzer-repair-dutchess-county-new-york) · video intercom 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+ (/intercom-installation-dutchess-county-ny) · single door/gate $1,900–$6,000; multi-door $5,000–$18,000 (/access-control-installation-dutchess-county cost section) · elevator L1 from $2,295/car, L2 from $3,825/car · four-camera from $1,299 (/security-camera-pricing-dutchess-county, A1) · cabling $150–$300 per connection point · monitoring $30/$45. NOT used: access page "$195/hr", "25% surcharge", "$1,500–$2,500 lobby fob", "$3,000/year saved" story; intercom page "free on-site assessment", "$200–$400 savings", audio $500–$800; alarm package prices; campus $18,000–$55,000; any maintenance/portfolio price; fire alarm prices (none).

### Question register additions (property-management-security-dutchess-county)
Checked by meaning against all PM pages on disk (NYC, 5 boroughs, LI, Nassau, Suffolk, HV, Westchester, Rockland, Orange, Putnam and the parallel Ulster page at check time) and co-op/condo Dutchess. Dropped drafts that overlapped: tenant refuses entry (Brooklyn), managing agent vs owner approval (Nassau), freight elevator moving day (Manhattan), basement recorder location (Orange), footage retention (Brooklyn), per-building recorder (Queens), propped doors (Bronx), directory names (Brooklyn), remove old equipment (Manhattan), electrician involvement (Queens), contract takeover (SI), hearing-impaired chime (SI), lighting (SI), separate student codes and May–August reset (parallel Ulster), county coverage question (Ulster/Rockland), Wisetack FAQ (moved to cost section).
- Q&A: Our 1920s three-family house in the City of Poughkeepsie has painted wood trim around the front door. Do lead-safe rules change how a new call station gets mounted?
- Q&A: Our three-family house has no room in the front hall for a call panel. Can the buttons go out on the porch?
- Q&A: The City of Poughkeepsie fire department inspects our building on its cycle. Should we have the door hardware checked before the inspection?
- Q&A: We file the City of Poughkeepsie's vacancy statement every February. Will an entry-system project leave apartments off the market?
- Q&A: Our Beacon building's registration lists a managing agent who is leaving the company. Does anything on the security system need to change?
- Q&A: Our Beacon conversion has tall original factory windows on the ground floor. Do those need alarm sensors?
- Q&A: Beacon's alarm law calls for the central station to try a phone callback before police are sent. How does that work for an empty apartment with nobody to answer?
- Q&A: Our Wappinger complex added fob readers from three different companies over ten years. Can they be brought onto one system without replacing every reader?
- Q&A: Residents reserve our Fishkill clubhouse for parties. Can a reservation open the door only for that resident's time slot?
- Q&A: Our complex receives packages for a few hundred apartments. Where do cameras do the most good around the package room?
- Q&A: After the July 2026 storm our complex's entrance gate sat open for most of a day. How do we make sure it fails the right way next time?
- Q&A: Our house near Marist is rented by the bedroom, and each bedroom door has its own lock. Do those locks belong on the same system as the front door?
- Q&A: Student tenants in our Red Hook house keep adding friends to the doorbell app. Can the owner limit who gets added?
- Q&A: Our Hyde Park building has an apartment over a pizza shop. Should the shop's alarm and the apartment entry share any equipment?
- FAQ: Can you give our office a list of every fob and code that works at a building?
- FAQ: Can tenants at our complex open the entrance gate from their phones?
- FAQ: Do you install cameras in the parking garage under a downtown Poughkeepsie building?
- FAQ: How do you keep an entry panel working in an unheated vestibule through a Dutchess winter?
- FAQ: Can the leasing office see who is at a building door and talk to them from the front desk?
- FAQ: Can one call panel serve two small buildings that share a walkway?
- FAQ: Can a panel show the directory in large print for older tenants and their visitors?
- FAQ: Can a camera read license plates at our complex entrance?
- FAQ: Can the system tell the office which fob opened a door?
- FAQ: Can tenants view the building's cameras from their own phones?

### Similarity (masked geo; 8-word shingle share / difflib word-sequence ratio / max paragraph ratio excl. the required warranty sentence)
Putnam 0.055 / 0.229 / 0.60 · Westchester 0.043 / 0.205 / 0.60 · Rockland 0.043 / 0.151 / 0.61 · Orange 0.051 / 0.150 / <0.60 · HV hub 0.031 / 0.151 / <0.60 · parallel Ulster 0.040 / 0.197 / <0.63 · NYC 0.027 / 0.132 · LI 0.028 / 0.088 · Nassau 0.028 / 0.093 · Suffolk 0.029 / 0.091 · Bronx 0.025 / 0.109 · Brooklyn 0.026 / 0.124 · Queens 0.025 / 0.107 · SI 0.025 / 0.117 · Manhattan 0.025 / 0.074 · co-op Dutchess 0.028 / 0.076 · condo Dutchess 0.026 / 0.082. All < 0.65. ~20 short cards/steps/CTA lines rewritten after paragraph-level comparison.

### Images (11: Reolink partner product photos; no unused real job photos)
Checked images/cctv-installation/*dutchess* (12) visually against every PM job photo: every usable scene is already on a PM page (deterrent ceiling camera = Putnam exit-sign ceiling; aisle dome = Westchester shop shelving; ceiling turret = Rockland hero; mezzanine = Nassau; NVR tiles = Putnam; office dome+sensor = Putnam hero; recorder split lot = Nassau brick walk/gravel lot; corridor bullet = Rockland drop-tile; storeroom dome = Suffolk; TV grid = Putnam/Orange; canopy dome = Nassau; staff-at-desk = AI image with a face, rejected). Partner photos fetched by curl from reolink.com/us/product/<model>/ pages (home-cdn.reolink.us), WebP q80 ≤1600 px, checked by phash+dhash against every image on any PM/co-op/condo page (min distance >20) and visually via contact sheets; rejected: black PoE doorbell beside door handle (same product scene as Bronx/Brooklyn, also used by parallel Ulster), Wi-Fi bullet on stone wall (too close to Westchester), pigtail cable (= NYC), any image with people's faces. Checked against the parallel Ulster files at save time: no overlap.
| File (property-management-security-dutchess-county-…) | Source | Where |
|---|---|---|
| partner-photo-bullet-camera-beside-front-door-on-gray-siding (hero, eager, og/twitter) | rlc-1212a · home-cdn.reolink.us/wp-content/uploads/2026/07/住宅入口@2x.jpg.webp | hero |
| partner-photo-pan-tilt-dome-over-row-of-houses | rlc-823a · …/2025/07/230858561753261136.045.jpg.webp | §County |
| partner-photo-white-video-doorbell-on-gray-wall-in-rain | reolink-video-doorbell-poe · …/2024/07/310120471722388847.5027.jpg.webp | §Services (cameras) |
| partner-photo-camera-view-of-brick-house-and-lawn | rlc-823a · …/2025/07/310105321753923932.4366.jpg | §Rental types |
| partner-photo-bullet-camera-under-white-roof-eave | rlc-1212a · …/2026/07/住宅吊装@2x.jpg.webp | §Working with us |
| partner-photo-bullet-camera-on-siding-above-wood-fence | rlc-1212a · …/2026/07/住宅侧路@2x.jpg.webp | §Q&A |
| partner-photo-network-video-recorder-on-blue-glow | rlc-1212a · …/2025/05/190149571747619397.0656.jpg.webp | §Equipment |
| partner-photo-pan-tilt-dome-on-wood-wall-at-night | rlc-823a · …/2025/07/230852291753260749.7058.jpg | §AI check |
| partner-photo-bullet-camera-on-pale-wall-at-dusk | rlc-1212a · …/2025/05/160921551747387315.3529.jpg.webp | §Process |
| partner-photo-camera-view-of-cars-at-curb | rlc-823a · …/2025/07/310105021753923902.0975.jpg | §Coverage |
| partner-photo-two-dual-lens-cameras-on-blue | reolink-duo-3-poe · …/2024/01/300836001706603760.6624.jpg | §Packages |
DAILY-LOG note: `images: 11 partner (Reolink) product photos via reolink.com (no unused real property-management photos)`.

### FLIPs on the page
`<!-- FLIP: /property-management-security-ulster-county -->` in the Coverage section (plain text "The Ulster County page … is being written"). The Ulster page appeared on disk during this build; checker reports "no cross-link to live sibling /property-management-security-ulster-county" until the main run flips it.

### Dutchess pages linked once
/condo-security-systems-dutchess-county, /co-op-security-systems-dutchess-county, /door-buzzer-repair-dutchess-county-new-york, /intercom-repair-dutchess-county, /intercom-installation-dutchess-county-ny, /door-buzzer-installation-dutchess-county-ny, /smart-lock-installation-dutchess-county, /access-control-installation-dutchess-county, /elevator-access-control-installation-dutchess-county, /security-camera-pricing-dutchess-county, /security-camera-repair-dutchess-county, /parking-lot-camera-installation-dutchess-county, /doorbell-camera-installation-dutchess-county, /alarm-installation-dutchess-county, /fire-alarm-installation-dutchess-county-ny, /structured-cabling-installation-dutchess-county, /cctv-installation-dutchess-county, /security-camera-maintenance-dutchess-county, /wireless-camera-installation-dutchess-county, /floodlight-camera-installation-dutchess-county, /low-voltage-installation-dutchess-county, /network-installation-dutchess-county, /commercial-security-systems-dutchess, /lorex-camera-installation-dutchess-county, /reolink-camera-installation-prices-dutchess-county, /luminys-camera-installation-prices-dutchess-county, /security-cameras-dutchess-county, /co-op-board-intercom-upgrade, /condo-intercom-replacement, /free-quote. (No apartment-building or condo/co-op camera Dutchess pages exist yet.)

### For Anwar to confirm (CONFIRM)
- Fire alarm: page says entry/access work ties into fire alarm systems and links /fire-alarm-installation-dutchess-county-ny ("priced per building from approved drawings") — confirm Dutchess fire alarm work is in scope.
- Lead-safe practice wording (contained drilling and clean-up in pre-1980 units; door/frame replacement handed to a lead-safe-certified renovation contractor).
- Written per-property record sent to the office after the first visit and after changes; footage-export training for office staff; per-property invoices under the owner's entity.
- Clubhouse reservation access, reader consolidation (keeping compatible readers, swapping controllers), gate phone credentials, plate-reading camera as an add-on, limited tenant camera view of one camera — written as things we do.
- Bedroom-lock advice (keep independent of the front-door system) and doorbell ownership moves for student houses.
- Vassar 99% figure is from collegedata.fyi reproducing the Common Data Set; swap for Vassar's own CDS PDF if preferred.


## Ulster County (property-management-security-ulster-county) — built 2026-11-27, batch subagent (part file; merge into research/property-management-security.md)

Child page · up-link /property-management-security-hudson-valley · phone (845) 640-3835 (body, CTAs, sticky bar, schema; 800 only in the shared header) · GBP Bronx (`#bronx`, 460 E Fordham Rd) · start price $250 service call (START_PRICES). Format: exact query · platform · URL · finding · section used.

### Thin-page check: PASSED
Ulster has enough distinct, sourced landlord/manager material for a genuinely different page: Kingston ETPA history (2022 adoption, 1.57% vacancy, 15% rollback, Court of Appeals June 2025, 2025 survey 7.04% with the >22-unit exception, Council override Jan 2026, new suit Mar 2026), HCR required-services rules, Kingston rental registry (ch. 332) and HLPC review, Village of New Paltz annual rental registration/inspection with a 15-mile manager rule, SUNY New Paltz enrollment/housing, Village of Saugerties landlord registration (ch. 148), Town of Saugerties STR law (2-hour response), Woodstock STR definitions (180 days/26 weekends, local host), Kingston STR permit cap (106), County Comptroller STR report 2025 (2,827 STRs, 3.28%, town table), county occupancy-tax registration, Sheriff alarm law, Central Hudson storm, ACS tenure/age/seasonal/rent tables for county, Kingston, Saugerties village and all towns.

Thesis (kept apart from HV hub = six-county routing; Putnam = lake colonies/accessory apartments; Orange = city rental licenses; Rockland = county MDRR/Spring Valley; Westchester = ETPA towers; Dutchess parallel; condo Ulster = associations): Ulster is three rental markets in one county — Kingston's old, half-rented city stock with ETPA rent stabilization and historic districts; New Paltz student rentals under annual village inspection; and a very large whole-house short-term-rental/seasonal-cabin market in Woodstock, Saugerties and the Catskill towns regulated town by town.

### Research matrix
| # | Exact query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| U1 | `Kingston NY Emergency Tenant Protection Act rent stabilization 2022 vacancy rate 15% rent reduction court` · WebSearch → Firecrawl scrape | https://hcr.ny.gov/city-of-kingston-adopts-etpa | Kingston voted to adopt ETPA July 28, 2022 after a vacancy study of 6+ unit buildings built before Jan 1, 1974 (<5%); KRGB Nov 9, 2022 guideline: 15% reduction for leases Aug 1, 2022–Sep 30, 2023; Ulster County Supreme Court challenge; Court of Appeals June 18, 2025 (HVPOA v. City of Kingston) upheld vacancy study and ETPA adoption and let the 15% guideline stand; owners must keep filing annual registrations with ORA; maintenance-of-services protections remain | §County para 4; facts list; §Kingston paras 1–2; Kingston "what we do differently"; Q&A Kingston; AI check #1 |
| U2 | `https://hcr.ny.gov/fact-sheet-3` · Firecrawl scrape (PDF) | https://hcr.ny.gov/system/files/documents/2024/11/fact-sheet-03-11-2024.pdf | Owners must provide and maintain services/equipment (repairs, heat, water, maintenance, janitorial, elevator service, ancillary services); ETPA base date outside NYC = May 29, 1974 or day before local effective date, whichever later; new equipment in occupied apartment → IAI increase only with tenant's voluntary written consent; vacant → no consent needed (OB 2024-2); tenants file decreased-services complaints, see Fact Sheet #14 | §Kingston para 3; "replacement planned around consent"; Q&A ETPA cost pass-through |
| U3 | `59opn25-Decision.pdf` · Firecrawl scrape (query) | https://www.nycourts.gov/CTAPPs/Decisions/2025/Jun25/59opn25-Decision.pdf | Common Council declared vacancy ≤5% July 28, 2022, opted in effective Aug 1, 2022 | corroborates U1 |
| U4 | `Kingston rental registry ... vacancy survey` · Firecrawl search → scrape PDF (query) | https://kingston-ny.gov/filestorage/8399/8469/48370/City_of_Kingston_2025_Rental_Vacancy_Survey.pdf | 2022 vacancy study 1.57%; 2025 survey net vacancy 7.04% for sampled ETPA properties, above 5% threshold except buildings >22 units (below 5%); search excerpt: administrative determinations leave ETPA coverage "now under 20%" of city rental units; sample 88 units | §Kingston paras 1–2 |
| U5 | `Kingston Common Council vote ETPA housing emergency end 2025 ...` · Firecrawl search (excerpts) → scrape | https://kingston-ny.gov/news/?FeedID=3534 (excerpt: Dec 22, 2025 mayor statement returning Resolution 202 of 2025) ; https://housingjusticeforall.org/kingston-tenants-vow-to-fight-yet-another-landlord-lawsuit/ (Mar 19, 2026) | Mayor vetoed Council's ETPA resolution Dec 2025; Council overrode veto Jan 6, 2026; landlords filed new suit in Ulster Supreme Court Mar 18, 2026 (attributed on page to Housing Justice for All, a tenant advocacy group) | §Kingston para 2; Working-with (removed list); AI check #1 context |
| U6 | `Kingston NY rental registry law landlords register rental units inspection` · Firecrawl search → scrape (query) | https://ecode360.com/12699947 | City of Kingston ch. 332: register rental property (residential or mixed use); owner not residing in Ulster designates managing agent (natural person 18+, resides in Ulster County), update within 15 days; inspection at least every 24 months; fines up to $500, each week separate | §County "managing agent"; §Kingston ch. 332 para; Q&A out-of-county owner |
| U7 | `Kingston NY Historic Landmarks Preservation Commission certificate of appropriateness Stockade District Rondout` · Firecrawl search (excerpts) | https://kingston-ny.gov/hlpc ; https://engagekingston.com/32415/widgets/115576/documents/81283 | CLG since 1986; exterior projects on historic properties visible from public ROW reviewed by HLPC before building permit; Rondout-West Strand district 1979; Stockade district (Dutch-vernacular buildings) | §Kingston historic para; Q&A Stockade |
| U8 | `City of Kingston NY short-term rental law permit non-owner occupied` · Firecrawl search → scrape PDF | https://kingston-ny.gov/filestorage/8399/8469/48370/STR_Fact_Sheet_2024_-_City_of_Kingston_Form-Based_Code.pdf | Form-Based Code effective Aug 2, 2023; STR-F capped at 1% of housing units = 106 permits (Aug 2023), only T5/T4 transects; STR-RO and STR-L uncapped; one STR per property; none in ADUs; license number on listings; fees $650/$125/$125 (fees not used); fines $1,000/$5,000/$7,500 per day (not used) | §Rental types STR para |
| U9 | `Village of New Paltz rental permit inspection law student housing` · Firecrawl search → scrape | https://ecode360.com/7237600 | Ch. 129 Art. II: every rental registered and inspected annually; owner not within 15 miles appoints property manager within 15 miles; new owner notifies within 15 days; inspection checklist; conditions (windows in sleeping spaces, smoke/CO detectors, etc.) bar renting; tenant list required; public rental index incl. history of violations, fires, incidents | §County managing agent; facts list; §Student rentals; Q&A inspection |
| U10 | `SUNY New Paltz enrollment students fall 2025 residence halls capacity` · Firecrawl search (excerpts) | https://www.usnews.com/best-colleges/suny-new-paltz-2846/student-life ; https://www.newpaltz.edu/reslife/halls.html ; https://oracle.newpaltz.edu/increased-enrollment-in-suny/ | 6,113 undergraduates (fall 2025, US News); 14 residence halls (college); housing capacity ≈3,250 (The Oracle) | §Student rentals |
| U11 | `Town of Saugerties short-term rental law permit local law` · Firecrawl search → scrape (query) | https://ecode360.com/44738484 | Ch. 194 (L.L. 2-2022): permit only for single-family homes/permitted accessory apartments; copy of Ulster County registration with application; yearly fire/safety inspection; owner or designated host addresses complaints within two hours; directory with emergency contacts, egress plan, quiet hours from 10 p.m.; fines ≤$500/$750/$1,000; revocation after 3 violations in 12 months (fines/revocation not used) | §County local host; §Rental types STR; Q&A two-hour rule; AI check |
| U12 | same search · Firecrawl scrape (query) | https://ecode360.com/28615969 | Village of Saugerties ch. 148 (L.L. 1-2014): all rental property registered; STRs by Mar 31, 2024; sworn landlord registration statement incl. insurance; owners outside Ulster designate managing agent residing in Ulster; update within 15 days; fines $250–$500 per day | §County managing agent; facts list |
| U13 | `Town of Woodstock NY short-term rental law permit cap` · Firecrawl search → scrape (query) | https://ecode360.com/110303 | Woodstock ch. 260 definitions: STR registration from town, posted number on listings, one calendar year, one per person/entity; non-owner-occupied STR needs designated local host, ≤180 days/yr with ≤26 weekends; ≤2 guests per bedroom | §County local host; §STR services; §Rental types STR; Q&A 180 nights |
| U13x | same search (rejected) | https://www.townofwoodstock.org/fileadmin/files/Archive/2024/03/STR-FAQ.pdf | This FAQ is Woodstock, **Vermont** — NOT used | — |
| U14 | `Ulster County short-term rental registry hotel occupancy tax` · Firecrawl search (excerpts) | https://www.ulstercountyny.gov/Departments/Finance/Tax-Information/Occupancy-Tax ; .../HotelMotelSTR-Registration | Operators of hotels, motels, STRs must register with Finance; booking service may collect/remit, operator still files occupancy return | §Rental types STR para 3 |
| U15 | same search · Firecrawl scrape (page + PDF query) | https://comptroller.ulstercountyny.gov/publication/ulster-county-comptrollers-short-term-rental-report-2025/ ; https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf | 2,827 STRs (May 2025) = 3.28% of housing; 98% entire homes; avg 942 (2015) → 3,013 (2024); table: Shandaken 267/2,675, Woodstock 378/4,289, Village of Saugerties 106/2,026, Kingston 150/11,049, Village of New Paltz 24; 16 municipalities regulate; ≥10 platforms vs 4 in 2020; enforcement a challenge | §County para 3; facts list; place table; §STR para 3 |
| U16 | `NY State Senate Bill 2025-S820` · Firecrawl search (excerpt) | https://www.nysenate.gov/legislation/bills/2025/S820 | County-based STR registry chapter amendment (context only — NOT used on page) | — |
| U17 | ACS 5-year 2023 tables B25001/B25003/B25004/B25034/B25064 · Firecrawl Alexandria provider census-gov (census/data) | https://api.census.gov/data/2023/acs/acs5?get=group(B25003)&ucgid=0500000US36111 (and B25001/B25004/B25034/B25064; place 1600000US3639727 Kingston, 1600000US3665288 Saugerties village; county subdivisions pseudo(0500000US36111$0600000)) | Ulster: 86,178 units; 73,105 occupied; 21,942 renter; 6,545 seasonal; 21,829 built ≤1939; median gross rent $1,335. Kingston city: 11,049 units; 9,951 occ; 5,126 renter; 5,979 ≤1939; rent $1,323. Saugerties village: 2,026; 1,897 occ; 1,200 renter; 1,118 ≤1939. Seasonal: Shandaken 886, Woodstock 813, Wawarsing 702, Rochester 676, Marbletown 506. Renter: New Paltz town 2,340; Ulster town 1,770; Lloyd 1,316; Plattekill 1,372; Esopus 595 | §County paras 1–3; facts list; place table; §Cabins |
| U18 | census.gov QuickFacts direct · Firecrawl scrape | https://www.census.gov/quickfacts/fact/table/ulstercountynewyork,kingstoncitynewyork/PST045224 | EMPTY (not accessible in build env) — 503; data taken via U17 | — |
| U19 | reused, research/condo-security-systems.md UL-A1 (Ulster Sheriff) | https://www.ulstersheriffny.gov/falsealarm | LL 13 of 2015: permit per structure, owner or controlling tenant applies, one-time $10; penalties none 1st/2nd, $50 3rd, $200 4th+; unpermitted warning + 14 days then $100/$200; unpaid → tax bill; exempt: City of Kingston; Towns of Esopus, Marlborough, New Paltz, Saugerties, Shandaken, Ulster, Wawarsing, Woodstock; Villages of Ellenville, New Paltz, Saugerties | §Services alarms; Q&A Hurley; AI check #3 |
| U20 | reused, condo UL-A3 | https://ecode360.com/13643763 | Town of Saugerties ch. 62 alarm permit | §Services alarms ("own alarm permit rules") |
| U21 | reused, condo UL-A4 | https://ecode360.com/35131702 | Ulster County ch. 185: master electrician license via county Electrical Licensing Board | §Services cabling; Working-with licensing |
| U22 | reused, condo UL-W1 / silo H4 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 26, 2026: >19,000 homes/businesses; hardest hit Woodstock, Shawangunk, Plattekill, Hurley | facts list; §Services power |
| U23 | reused, silo (condo UL-G3) | https://www.nysenate.gov/legislation/laws/GBS/395-B ; https://www.nysenate.gov/legislation/laws/GBS/69-M | No viewing devices in restrooms etc.; state alarm installer licensing | §Services cameras; AI check #2; Working-with licensing |
| U24 | reused, silo S11 | https://cooperatornews.com/article/qa-camera-placement | Audio recording / eavesdropping caution | Working-with footage |
| U25 | Reddit r/hudsonvalley / r/Kingston, Google PAA/PASF, Answer the Public, AI Overview, Yelp 1–3★, Bing/DDG for "property management security Ulster County" | — | EMPTY (not accessible in build env). No Reddit/AI quote used; AI Reality Check corrects generic claims only | — |
| G1 | map geography (not separately sourced) | — | Thruway/9W river corridor; Routes 32/299 to New Paltz; Route 28 west; Route 209 Rondout Valley to Ellenville; Route 212 to Woodstock; Highland in Town of Lloyd | Working-with routing; Q&A Highland/9W |
| P1 | site pages (internal), read Nov 27 2026 | /door-buzzer-repair-ulster-county-new-york ; /intercom-installation-ulster-county-ny ; /access-control-installation-ulster-county ; /elevator-access-control-installation-ulster-county ; /security-camera-pricing-ulster-county ; /alarm-installation-ulster-county ; /structured-cabling-installation-ulster-county | See prices below | hero quick answer; services; cost table |

### Prices used (all already published on Ulster pages)
$250 service call (START_PRICES; buzzer repair page) · station $250–$525 · relay/button $250–$475 · 24 V transformer $325–$650 · strike + alignment $450–$950 · lobby panel/faceplate $650–$1,800 · riser $850–$2,400 (/door-buzzer-repair-ulster-county-new-york) · intercom house $500–$2,500; video 4–8 units $1,200–$3,500; multi-unit $1,200–$5,000; IP $2,500–$8,000+ (/intercom-installation-ulster-county-ny) · access single door/gate $2,100–$6,500; multi-door $5,500–$20,000; full property $20,000–$55,000+ (/access-control-installation-ulster-county) · elevator L1 from $2,295/car, L2 from $3,825/car · four-camera from $1,299 (/security-camera-pricing-ulster-county) · basic residential alarm from $600; monitoring $30/$45 (/alarm-installation-ulster-county) · cabling $150–$300 per connection point (/structured-cabling-installation-ulster-county). NOT used: access page "$195/hr callbacks", "35% HV surcharge" and (347) phone; door-buzzer-installation "$300 service call" (conflicts with $250); buzzer repair "same day" wording; smart-lock "$275 setup"; intercom "$200–$400 bundle savings"; condo page "free walk-through".

### Question register additions (property-management-security-ulster-county)
Checked by meaning against all PM pages on disk (incl. parallel Dutchess at check time) and condo Ulster; checker reports no masked duplicates. Dropped/reworded drafts that overlapped: per-bedroom locks (Orange MSMC), store alarm sharing internet (Queens), weak-cell cabin cameras (Putnam hollow), internet-out recorder (Putnam FAQ), phone-vs-handset entry (no-smartphone Q), one-app multi-site (NYC), laundry building on system (Westchester).
- Q&A: Our Kingston building is stabilized under the ETPA. If we replace the old audio intercom with video, can that cost be passed on to tenants?
- Q&A: A tenant in our stabilized building filed a decrease-in-services complaint about the front door. What should our repair paperwork show?
- Q&A: Our walk-up is in the Stockade district. Does a new call panel or a camera on the front need the landmarks commission's review?
- Q&A: We own rentals in Kingston but live in another county. Who answers for the building, and does that person need access to the entry system?
- Q&A: Our New Paltz tenants sign one joint lease for the whole house. Does it still make sense to give each of them a separate door code?
- Q&A: Students leave in May and the next group arrives in August. What should happen to the codes and cameras over the empty summer?
- Q&A: The village inspects our New Paltz rental every year. Can the security work we do cause us to fail the inspection?
- Q&A: The Town of Saugerties expects the owner or host to deal with complaints within two hours. How can the equipment help the host do that?
- Q&A: Our Woodstock house is a non-owner-occupied rental limited to 180 nights a year. Can the keypad log help us keep track of the nights it was used?
- Q&A: Our Shandaken cabin sits at the end of a long private drive. Where should the first camera go?
- Q&A: Can a guest's door code at a short-term rental expire on its own at checkout?
- Q&A: Our garden complex off Route 9W has six apartment buildings spread across one lot. Where should the recorder and the network equipment go?
- Q&A: Our tenant arms and disarms the alarm in a house we rent out in Hurley. Who applies for the alarm permit?
- Q&A: Our Highland building has a street entrance and a rear entrance from the lot. Should both doors have a call panel?
- FAQ: Do you work in the western mountain towns such as Shandaken, Denning and Hardenburgh, or only near Kingston?
- FAQ: Can you register our short-term rental with the town or the county for us?
- FAQ: Will a battery keypad lock keep working through a winter at an unheated cabin?
- FAQ: Do guests at our short-term rental need to download an app to get in?
- FAQ: Is financing available for an owner with one or two Ulster rentals?
- FAQ: Will a guest's door code still work if the internet at the rental goes down?
- FAQ: Is there a monthly fee after the system is installed?
- FAQ: Do you serve rentals in the southern towns, such as Shawangunk, Plattekill and Marlborough?

### Similarity (masked geo; 8-word shingle share / difflib word-sequence ratio)
Putnam 0.055 / 0.279 · Westchester 0.036 / 0.202 · Orange 0.038 / 0.198 · parallel Dutchess 0.039 / 0.192 · Rockland 0.036 / 0.177 · HV hub 0.029 / 0.159 · Suffolk 0.031 / 0.117 · Nassau 0.030 / 0.126 · NYC 0.026 / 0.115 · SI 0.025 / 0.110 · Brooklyn 0.025 / 0.107 · Queens 0.025 / 0.103 · Bronx 0.025 / 0.100 · Manhattan 0.025 / 0.098 · LI 0.030 / 0.092 · condo Ulster 0.026 / 0.083. Paragraph level (p/li/td/h3/figcaption ≥8 words, nav/warranty/consent excluded): max 0.63 (hero license/address line vs Orange/Putnam, mostly address + phone constants); every other paragraph < 0.60 after rewriting ~55 template-like lines.

### Images (11: 2 real job photos + 9 Reolink partner product photos)
WebP q80 in images/property-management-security/, prefix `property-management-security-ulster-county-`. Each phash/dhash-checked against every other file in the folder (incl. parallel Dutchess at save time); visually compared against contact sheets of all 127 non-partner PM images. Real job photos whose scene is already on a PM page were excluded (LI office four-split monitor = views already on Putnam/Queens sidewalk/door pages; red deterrent camera = Putnam "exit sign" ceiling; stockroom corner dome, steel-arm facade, juice-bar dome, store shelving ceilings, corridor grey door, mezzanine wall, cable bundles over monitor). Reolink night-yard view swapped out (same scene as Nassau `reolink-night-view-of-lit-yard-and-path`).
| File (…ulster-county-) | Source | Where |
|---|---|---|
| job-photo-fire-escapes-on-masonry-apartment-front (hero, eager, og/twitter) | images/access-control-installation/access-control-installation-washingtonville-fire-escapes-on-masonry-apartment-front.webp | hero |
| reolink-partner-photo-house-cutaway-with-cameras-and-cable-path | Reolink · https://reolink.com/us/product/rlc-1240a/ page asset (rlc-1240a_15) | §County |
| reolink-partner-photo-doorbell-cable-into-recorder-poe-port | Reolink · https://reolink.com/us/product/reolink-video-doorbell-poe/ asset | §Services (access control) |
| reolink-partner-photo-turret-camera-under-white-eave | Reolink · https://reolink.com/us/product/rlc-833a/ asset | §Services cameras |
| reolink-partner-photo-dome-camera-with-memory-card-slot-open | Reolink · rlc-1240a asset | §Services power/internet |
| reolink-partner-photo-lawn-and-pool-seen-from-wall-camera | Reolink · rlc-833a asset | §Rental types |
| reolink-partner-photo-camera-view-of-hillside-and-bay | Reolink · rlc-833a asset | §Rental types (STR) |
| job-photo-recorder-live-view-grid-with-time-stamp | images/cctv-installation/cctv-installation-nyc-recorder-live-view-time-stamp.webp | §Equipment |
| reolink-partner-photo-hooded-figure-under-camera-light-at-night | Reolink · https://reolink.com/us/product/rlc-81ma/ asset | §How it works |
| reolink-partner-photo-dome-camera-under-eave-at-night | Reolink · rlc-1240a asset | §Coverage |
| reolink-partner-photo-black-video-doorbell-beside-door-handle | Reolink · reolink-video-doorbell-poe asset | §Packages |
DAILY-LOG note: `images: 2 real job photos (1 images/access-control-installation, 1 images/cctv-installation) + 9 Reolink partner product photos via reolink.com; no Drive/CompanyCam check in this run`.

### FLIPs on the page (plain text + `<!-- FLIP: /slug -->`)
/property-management-security-dutchess-county (coverage section). Linked live: /property-management-security-hudson-valley (up, breadcrumb, body ×2), -westchester-county, -rockland-county, -orange-county, -putnam-county, -nyc, -manhattan, -brooklyn, -queens, -bronx, -staten-island, -long-island, -nassau-county, -suffolk-county.

### Ulster pages linked once
/condo-security-systems-ulster-county, /door-buzzer-repair-ulster-county-new-york, /door-buzzer-installation-ulster-county-ny, /intercom-installation-ulster-county-ny, /access-control-installation-ulster-county, /smart-lock-installation-ulster-county, /elevator-access-control-installation-ulster-county, /security-camera-installation-ulster-county-ny, /security-camera-pricing-ulster-county, /alarm-installation-ulster-county, /fire-alarm-installation-ulster-county-ny, /structured-cabling-installation-ulster-county, /security-camera-repair-ulster-county, /doorbell-camera-installation-ulster-county, /wireless-camera-installation-ulster-county, /floodlight-camera-installation-ulster-county, /residential-security-camera-installation-ulster-county, /commercial-security-systems-ulster, /parking-lot-camera-installation-ulster-county, /lorex-camera-installation-ulster-county, /reolink-camera-installation-prices-ulster-county. (Not existing: intercom-repair-ulster-*, co-op-security-systems-ulster-county (HOLD-THIN), apartment-building-security-camera-installation-ulster-county.)

### For Anwar to confirm (CONFIRM)
- Fire alarm: page says fire alarm work for larger rental buildings is in scope in Ulster and links /fire-alarm-installation-ulster-county-ny (priced from approved drawings).
- Cameras inside short-term rentals: page "recommends" none where guests stay (not stated as a company prohibition) — confirm wording.
- Booking-length guest codes, cleaner-only turnover codes, door contact on owner's storage closet, cellular alarm communicators, temperature sensors "where the panel supports one", wireless bridges between buildings, per-camera account limits: written as things we set up (no brand).
- Per-property "file" and labeled equipment/one-page guide at handover, ETPA repair invoices naming report date/visit date/parts — confirm this is current practice.
- Kingston ETPA status after the March 18, 2026 lawsuit is attributed to a tenant advocacy group (Housing Justice for All); swap for a court/city source if preferred, and re-check status before any refresh.
- Hero/og image is a small (207×360) real job photo; replace with a larger real Ulster rental job photo when one is available.
- Route numbers in the routing paragraph and "Highland"/"Route 9W" in Q&A are map geography, not separately sourced.

### Mobile / design
Not rendered at 390px in this run (no browser in build env); layout uses only the shared template classes copied from the Putnam page (tables already carry the template's 600px fixed-layout rule).

### Back-links needed (main run)
All 14 live PM siblings + HV hub (flip any Ulster FLIP comment to /property-management-security-ulster-county), parallel Dutchess page; one contextual link back from /condo-security-systems-ulster-county and optionally /intercom-installation-ulster-county-ny and /door-buzzer-repair-ulster-county-new-york.
