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
