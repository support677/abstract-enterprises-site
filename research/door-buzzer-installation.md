# Door Buzzer Installation — silo research

Created 2026-10-18 by the REBUILD run for `door-buzzer-installation-ulster-county-ny` (first page of this silo rebuilt to blueprint v2.3; the other 15 silo pages are still the old near-duplicate template). Format per v2.3 §12.4: **exact query · platform · URL · finding · page + section used**. Unreachable sources are written `EMPTY (not accessible in build env)`. Shell curl is blocked; tools used: `mcp__Firecrawl__firecrawl_search` ("FC search", excerpts only unless "scraped"), `mcp__Firecrawl__firecrawl_scrape` ("FC scrape", query mode with direct quotes), `mcp__Firecrawl__firecrawl_gov_search` ("FC gov"), Firecrawl Alexandria `census-gov/census/data` ("Census API"). "Carried" = sourced by an earlier run in another research file in this repo (file named) and not re-fetched.

Section numbers (§) refer to blueprint v2.3 §4 elements as built on the page (§5 Neighborhood, §5.5 facts, §6 services, §7/§7.5 building types, §8/§8.5 commercial + compliance, §9 Q&A, §10 equipment, §10.5 AI reality check, §12 process, Town-by-town, §13 landmarks, §14 pricing, §15 packages/BYOE, §16 related, §17 FAQ, Sources).

## Silo-wide findings (door buzzer / multi-tenant entry — usable on every page of the silo)

### The 11 mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl does not open reddit.com threads). Silo-level rows S12–S14 below. Ulster/Hudson Valley buzzer threads: EMPTY (searches returned r/KingstonOntario — Kingston, Ontario, Canada — not usable). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). Page §10.5 says so on the page and uses claims from national cost guides / vendor blogs (S8–S11) as the "AI claims", each corrected with sourced facts. |
| 6 | Area landmarks | Ulster section U-rows |
| 7 | Area use cases / building stock | Ulster section (Census ACS B25024 etc.) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only one search backend available |
| 9 | Local news | Ulster section (Daily Freeman, Hudson Valley One, Times Union — carried and new) |
| 10 | Hyperlocal | Ulster section; door-buzzer-specific Ulster news (entry-door/intercom stories): EMPTY — search `Daily Freeman Kingston apartment tenants front door lock broken intercom building security complaints` returned only NYC/Facebook/other-state items, none used |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix — silo
| # | Exact query · platform | URL | Finding | Page + section used (Ulster page) |
|---|---|---|---|---|
| S1 | `New York Multiple Residence Law entrance door lock intercom buzzer requirement apartment` · FC search | https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a/ ; https://www.nyc.gov/assets/buildings/pdf/tenants_rights.pdf (excerpts); FC gov `Multiple Residence Law entrance door lock self-closing intercommunication system` → full §50-a text (justia result) | MDL §50-a: every Class A multiple dwelling erected/converted after Jan 1 1968 with eight or more apartments "shall also be equipped with an intercommunication system" at the self-locking main door allowing voice communication and remote release; pre-1968 buildings must install doors + intercom if tenants occupying a majority of apartments request/consent in writing (installation started within 90 days, completed within six months). | §8.5 bullet 1; §9 Q "NYC intercom law … Kingston or New Paltz"; §10.5 H3 3 |
| S2 | `New York Multiple Residence Law applies cities towns villages less than 325,000 population` · FC gov | https://nysenate.gov/legislation/laws/mdw/3 ; https://nysenate.gov/legislation/laws/mre/3 ; https://courtlistener.com/opinion/5827103/kase-v-city-of-rochester | MDL §3: "This chapter shall apply to all cities with a population of three hundred twenty-five thousand or more"; other cities/towns/villages may adopt by local law. MRL §3: "shall apply to all cities of less than three hundred twenty-five thousand population and to all towns and villages". Kase v Rochester: MRL multiple dwelling = "three or more families living independently" (MRL §4[33]). | §8.5 bullet 1; §9 NYC-law Q; §10.5 H3 3 |
| S3 | same FC gov search | https://nysenate.gov/legislation/laws/mre/57 | MRL §57: doors opening on entrance halls or other public halls "shall be self-closing, except where such dwelling is equipped throughout with an approved type automatic sprinkler or fire-detecting system"; unlawful to attach a device preventing self-closing. | §9 NYC-law Q para 2 ("self-closing doors on public halls") |
| S4 | `electrically locked egress doors building code sensor release magnetic lock fire alarm release 1010.2 requirements` · FC search | https://up.codes/s/sensor-release-of-electrically-locked-egress-doors ; https://codes.iccsafe.org/s/IBC2024P1/chapter-10-means-of-egress/IBC2024P1-Ch10-Sec1010.2.12 (excerpts) | IBC sensor release: sensor on egress side; unlock on sensor signal or loss of power to sensor; loss of power to lock unlocks; manual unlocking device 40–48 in above floor within 5 ft, sign "PUSH TO EXIT", direct interruption of power, unlocked ≥30 s; fire alarm / sprinkler activation unlocks; UL 294 listing. (2021 IBC numbering 1010.2.12; 2024 IBC 1010.2.11.) | §8.5 bullet 3; §9 Q "magnetic lock … main entrance"; §9 Q rental inspector; §10.5 H3 5 |
| S5 | `2020 Building Code of New York State based on 2018 International Building Code Uniform Code update 2025 effective date` · FC search | https://codes.iccsafe.org/codes/new-york ; https://codes.iccsafe.org/content/NYSBC2025P1 ; https://www.nysed.gov/facilities-planning/news/2025-nys-uniform-code-and-state-energy-code-will-take-effect-december-31-0 | 2025 Uniform Code effective Dec 31 2025 (transition Oct 1–Dec 30 2025); 2025 BCNYS "based on the 2024 International Building Code". | §8.5 bullet 3 |
| S6 | `fail safe vs fail secure electric strike explained power loss locked unlocked` · FC search | https://us.allegion.com/en/resources/education/leading-the-industry/decoded/fail-safe-vs-fail-secure.html (full excerpt returned) | "Fail safe products are unlocked when power is removed"; "Fail secure products are locked when power is removed"; with an electric strike "you can exit by turning the lever … regardless of whether the electric strike is fail safe or fail secure"; fire doors need fail-secure strikes (NFPA 80); "Electromagnetic locks are only available fail safe"; "Fail secure products are more common than fail safe due to security concerns". Also Avigilon / NIH bulletin excerpts corroborate. | §6 card; §9 Q Central Hudson power; §9 Q magnetic lock; §10 strikes card; §10.5 H3 5 |
| S7 | `Aiphone GT series 2-wire multi-tenant intercom system existing wire retrofit` · FC search → FC scrape https://www.aiphone.com/products/gt-series/ | https://www.aiphone.com/products/gt-series/ ; https://www.aiphone.com/blogs/upgrade-intercom-system/ (excerpt) | GT Series: "Multi-tenant intercom system for new builds and retrofit projects"; "5,000 Tenant stations"; door stations "designed to withstand harsh conditions such as rain and snow"; "Mobile app configuration via NFC"; "offers the advantage of using existing wire and infrastructure". Aiphone upgrade guide: "If the existing wires are in good condition, they can be reused". | §9 Q bell wire; §9 Q unheated porch; §9 Q six entrances; §10.5 H3 7 |
| S8 | `intercom system installation cost apartment building per unit Angi HomeAdvisor 2025` · FC search → FC scrape | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/ | "Installing an intercom system costs an average of $2,500"; "between $1,500 and $15,000"; wireless $150–$1,500, hard-wired $1,000–$15,000; "Wireless systems are the best option if you want to DIY"; whole-house five-room system $1,000–$1,500 installation; 1–2 hours per station. | §10.5 H3 1 & 2; §14 comparison sentence |
| S9 | same search → FC scrape | https://swiftlane.com/blog/apartment-intercom-installation-cost/ | "$1,000 to $5,000 or more per entry door for modern IP or video systems"; projects "$1,500 … up to $50,000 or more"; "Software subscriptions commonly add $5 to $15 per unit per month, or $30 to $100 per door per month". | §10.5 H3 6; §14 comparison sentence |
| S10 | `cellular intercom no internet no phone line apartment building entry LTE call box` · FC search | https://butterflymx.com/blog/apartment-call-box/ ; https://swiftlane.com/blog/telephone-entry-systems/ ; https://automaticgatemasters.com/cell-gate-intercoms/ (excerpts) | ButterflyMX: its Intercom "is both weatherproof and vandal-resistant and requires no building wiring"; Swiftlane: "Gated community / HOA — Cellular call box — No Ethernet required at perimeter"; CellGate: cellular video intercom "needs no internet at the gate". | §10.5 H3 4; §9 Q dead zone (cellular call boxes) |
| S11 | `2010 ADA Standards 308.2.1 unobstructed forward reach high 48 inches operable parts 309` · FC search | https://www.ada.gov/law-and-regs/design-standards/2010-stds/ ; https://www.access-board.gov/ada/chapter/ch03/ | "the high forward reach shall be 48 inches (1220 mm) maximum and the low forward reach shall be 15 inches (380 mm) minimum"; 309: operable parts within 308 reach ranges. | §8.5 bullet 6; §9 Q older residents |
| S12 | `reddit landlord small apartment building replace old buzzer intercom tenants phones 4 unit` · FC search | https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/ ; https://www.reddit.com/r/vancouverhousing/comments/1sxixrm/ ; https://www.reddit.com/r/VOIP/comments/16f3oma/ (excerpts) | Owners asking for "Affordable option to replace 6 unit building entry system" / "door buzzer/door locking system for a 4-unit apartment building"; tenant: "the intercom hasn't been working for several units". Background for pain points (cost of small-building replacement; partial outages). | §5 para 2 (pain points, paraphrased); §9 cluster framing — not quoted |
| S13 | `Aiphone GT … existing wire retrofit` (same as S7) · FC search | https://www.reddit.com/r/accesscontrol/comments/1scfk1y/2wire_intercom_systems_to_replace_aiphone/ (excerpt) | "This will allow you to keep the existing GT system, repair the damaged cable, and only upgrade those tenants that desire app connectivity". | §9 Q bell wire para 3; §10.5 H3 7 |
| S14 | `reddit hudsonvalley OR kingstonnewyork landlord intercom buzzer apartment door` · FC search | https://www.reddit.com/r/AskNYC/comments/17knzko/ ; https://www.reddit.com/r/OntarioLandlord/comments/qgzhvk/ (excerpts) | NYC tenant: buzzer "broken for nearly a year", reply cites 50-a; Ontario "talk, listen, door" panel non-functional. Not Ulster. Ulster/HV Reddit: EMPTY. | Not quoted; supports §9 NYC-law Q framing |
| S15 | `site:reddit.com kingstonnewyork OR NewPaltz apartment buzzer OR intercom OR "front door" packages stolen` · FC search | r/KingstonOntario threads (Kingston, Ontario) | Wrong Kingston — NOT used. | — |

### Silo pricing (existing AESS figures — never invent)
| Page | Figures (as published on the old template pages, 2026-10-18) |
|---|---|
| Brooklyn (base) | Audio / Small $400–$900; Video / Mid $700–$1,800; Multi-Unit $2,500–$10k+; online service call $250 applied toward work |
| Ulster (used) | Doorbell / Small $500–$1,100; Video / Mid $900–$2,300; Building / Large $3,000–$12k+; online service call $300 applied toward work; "travel built into the quote"; bundling "typically save $200–$400 in labor" |
**FLAG for Anwar:** the old Ulster figures are about 1.25–1.28× Brooklyn, not the blueprint §9 Ulster multiplier 1.53× (which would give $612–$1,377 / $1,071–$2,754 / $3,825–$15,300). The rebuilt page keeps the existing Ulster list (same approach as the Dahua Orange rebuild: "prices from old page"). Labour-only (BYOE) has no published AESS figure in this silo → page says "quoted flat at the walkthrough". The protected $195/hr, 3-hr minimum callback rate is not used on this page (the silo uses an online service call instead).

### Keyword plan (five layers, silo)
- Service: door buzzer installation, apartment buzzer system, intercom/entry system installation, video door entry, electric strike installation, buzzer upgrade over existing wiring, multi-tenant entry, door release.
- Problem: door propped open, tenants can't release door, buzzer works but door won't open, door doesn't latch, outage leaves door locked/unlocked, lost admin codes after building sale, packages, student turnover, landmark approval.
- Technology: two-wire multi-tenant systems (e.g. Aiphone GT), video monitors, handsets, phone/app answering, cloud management, cellular call box, keypad/code panels, fail-secure / fail-safe strikes, magnetic locks with sensor release, power supply + battery backup, surge protection, door closers.
- Industry: owners of 2–4 family houses, walk-ups, garden apartments, rent-stabilized buildings, student rentals, mixed-use main-street buildings, short-term rentals, senior housing, property managers/managing agents.
- Geographic: per page (Ulster list in the Ulster section).

## Ulster County

Page: `door-buzzer-installation-ulster-county-ny` (REBUILD 2026-10-18, was crawled-not-indexed). Area page, up-link `/door-buzzer-installation-hudson-valley-ny`. GBP Bronx (460 E Fordham Rd, schema `@id` #bronx). Direct line (845) 640-3835 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav chrome. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from every old sibling, which all share one template):** Ulster's buzzers serve *divided houses and small buildings, not lobbies* — ~31% of Kingston homes are in 2–4-unit buildings and the median Kingston home dates from 1939 or earlier — so the job is deciding which outside door gets controlled, testing the bell wire already running to each flat, fitting a fail-secure strike to the existing lockset, and dealing with Ulster's rule set (Kingston ETPA/rent stabilization, Kingston rental permits + 24-month inspections + in-county managing agent, New Paltz 30-day rental inspection, Multiple Residence Law not MDL §50-a, Kingston HLPC landmark districts) and setting (stone/brick facades, Central Hudson outages, lightning, Route 28/212 dead zones, new fiber).

### Research matrix — new for this page
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| U1 | Census API `census/data` dataset acs/acs5 vintage 2023, variables B25024_001E–010E, geography county:111 in state:36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36111 | Ulster County: 86,178 units; 1-unit detached 59,136; 1 attached 2,817; 2 units 6,143; 3–4 units 4,985; 5–9 3,202; 10–19 2,095; 20–49 1,180; 50+ 1,582; mobile home 5,019. (2–4 = 11,128; 5+ = 8,059.) | §5 para 1; §5.5 bullet 1 |
| U2 | Census API, same dataset, B25024 + B25035_001E + B25003_003E, geography place:39727,50551,23965 in state:36 (geographies resolved with `census/geographies` "Kingston city, New York", "New Paltz village, New York", "Ellenville village, New York") | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=1600000US3639727 (and …3650551, …3623965) | **Kingston city**: 11,049 units; detached 4,886; 2 units 2,111; 3–4 1,279; 5–9 901; 10–19 766; 20–49 241; 50+ 493; renter-occupied 5,126; median year built flagged "1939-" (= 1939 or earlier). **New Paltz village**: 2,519; detached 679; 2 units 220; 3–4 402; 5–9 395; 10–19 403; 20–49 79; 50+ 201 (5+ = 1,078 = 42.8%); renters 1,689; median built 1972. **Ellenville village**: 1,874; detached 965; 2 units 331; 3–4 445 (2–4 = 776 = 41.4%); 50+ 64; renters 656; median built 1954. | Hero sub; §5 paras 1–3; §5.5 bullets 2–4; Town by town (Kingston, New Paltz, Ellenville) |
| U3 | `Kingston NY Emergency Tenant Protection Act rent stabilization buildings six or more units built before 1974` · FC search → FC scrape (2) | https://nlihc.org/resource/kingston-becomes-first-city-upstate-new-york-adopt-rent-stabilization ; https://engagekingston.com/etpa ; excerpt https://www.facebook.com/KingstonNYgov/posts/…5365240033556294/ | NLIHC: Common Council declared a housing emergency and enacted ETPA on July 28 (2022); "An estimated 1,300 units are covered … buildings with six or more units that were constructed prior to 1974"; vacancy study April–May 2022 found 1.57% in qualifying units; title "First City in Upstate New York to Adopt Rent Stabilization". Engage Kingston: effective Aug 1 2022; Rent Guidelines Board; administered by NYS HCR; RA-84 "Decreased Building-Wide Service(s)" — "Areas of concern can include: Entrance, lobby, hall, staircase, elevator"; owner must comply with an order within 30 days; recommends tenants contact owner/representative before filing. City FB excerpt names Dutch Village, Stony Run, Fairview among covered complexes (excerpt only — NOT used on page). | §5 para 3; §5.5 bullet 5; §7 garden-apartment card; §9 Q rent-stabilized; Town by town (Kingston) |
| U4 | FC scrape (directQuote) | https://ecode360.com/12699947 (Kingston Code Ch. 332, L.L. 3-2004) | Owner must register rental property; "In the event the owner does not reside in Ulster County, then the owner must designate a managing agent" residing in Ulster; inspection "at a minimum of every 24 months … compliance with all applicable rules and regulations concerning safety and maintenance"; "No rental property … shall be occupied … without a valid rental permit". | §5 para 3; §8.5 bullet 5; §9 Q out-of-county owner; §9 Q rental inspector; Town by town |
| U5 | `Village of New Paltz rental permit inspection student housing off-campus SUNY New Paltz landlords` · FC search | https://www.villageofnewpaltz.gov/registered-rental-properties-list/ ; https://www.villageofnewpaltz.gov/rental-property-registration-and-inspection-forms/ (excerpts) | "the proposed rental property must also pass inspection within 30 days to be considered registered"; list of registered rentals and inspection checklist published. | §5 para 3; §8.5 bullet 5; §9 Q 30-day inspection; Town by town |
| U6 | `Kingston NY housing units two-family three-family four-family houses share of housing stock housing study` · FC search | https://kingston-ny.gov/filestorage/8399/8469/15358/City_of_Kingston_Housing_Study_10.15.20_final.pdf (excerpt) | 10,592 housing units; "over half of the housing units (5,000) in Kingston are over 80" [years old] (garbled excerpt); 2-family homes ~15% of residential sales 2019. | §5 para 2 |
| U7 | `Kingstonian apartments Uptown Kingston opened units 2025` · FC search | https://www.kingstonianny.com/ ; https://www.kingstonhousing.org/portfolio.aspx (FC scrape) | Kingstonian: "143 residential units • 10% affordable workforce housing. A 32-room boutique hotel" (developer site excerpt; build status not confirmed → page says "planned … described by its developer"). Kingston Housing Authority portfolio: six properties of 131, 98, 32, 60, 120, 40 units (Rondout Gardens = 131 per search excerpt). | Town by town (Kingston) — Kingstonian only; KHA not used on page except Sources list |
| U8 | `Ellenville village Canal Street apartments upstairs downtown housing Wawarsing renovation 2025` · FC search | https://www.ellenvilleha.org/ (excerpt) | "Our Senior Housing is located at 199 Canal Street, Ellenville". | §8 Ellenville card; Town by town; §13 Ellenville card |
| U9 | `Saugerties village Partition Street Main Street apartments above stores mixed-use buildings` · FC search | https://buildingsofnewengland.com/tag/main-street-saugerties/ ; https://www.coldwellbankerprime.com/p/211-Main-Street-Saugerties-NY-12477/dmgid_188993914 ; https://www.villagegreenrealty.com/blog/sale-of-prominent-commercial-building-in-saugerties-new-york-ensures-community-continuity.html (excerpts) | Main Street structure c.1870 "mixed use with retail at the street and offices above"; 211 Main St "7,219-square-foot brick mixed-use building"; 99–103 Partition St "three structures: two brick buildings". | §8 Saugerties card; §7 brick walk-ups card; Town by town (Saugerties) |
| U10 | `Central Hudson outage Ulster County customers storm 2025 OR 2026 Kingston` · FC search | https://www.cenhud.com/en/outages/outage-summary/ (excerpt) | "ULSTER … Customers Served: 93,190". | §5.5 bullet 6 |
| U11 | `Daily Freeman Kingston apartment tenants front door lock broken intercom building security complaints` · FC search | (results: Facebook/NYCHA/YouTube/Brownstoner/JustAnswer — none Ulster) | Ulster entry-security news: EMPTY. | — |

### Carried (verified Ulster sources fetched by earlier runs; not re-fetched)
| # | Finding | Source (as logged) | Research file | Page section |
|---|---|---|---|---|
| C1 | Kingston HLPC: CoA required for "material change in the appearance … visible from a public street or alley" in a landmark district; ordinary maintenance exempt; exterior desk reviews "generally turned around within one week"; districts Stockade, Rondout–West Strand, Chestnut Street, Fair Street | https://kingston-ny.gov/hlpc ; https://ecode360.com/6728919 ; https://engagekingston.com/27697/widgets/94955/documents/64622 | cat6-repair.md U8; sonos-installation.md U5 | §5 para 4; §6 card; §8 Uptown card; §8.5 bullet 2; §9 Q preservation commission |
| C2 | Stockade: 18th-c stone houses on all four corners of John & Crown; Senate House: single-storey Dutch stone dwelling built 1676, first NY Senate 1777 | Wikipedia Kingston Stockade District; parks.ny.gov | smart-lock-installation.md U13–U14 | §7 stone card; §13 Stockade card |
| C3 | Historic Huguenot Street: 10-acre NHL district, seven stone houses, 1678 settlement | huguenotstreet.org | cat6-repair.md R6 | §7 stone card; §13 card |
| C4 | Hurley Main Street private residences late 1600s–late 1800s | hurleyheritagesociety.org | smart-lock-installation.md U12 | §7 stone card; §9 stone-house Q |
| C5 | Rondout = D&H Canal tidewater terminus; $1.5M federal grant to raise East Strand/North Street against frequent tidal flooding (Times Union, Mar 29 2024) | en.wikipedia.org/wiki/Kingston,_New_York; timesunion.com …19373867.php | fiber-optic-installation.md (Ulster) | §13 Rondout card; §9 Q Rondout basement flooding |
| C6 | UPAC: 1927, 1,500 seats, Broadway, Midtown | hudsonvalleyone.com 2017/11/30 | fiber-optic-installation.md; sonos U2 | §8 Broadway card; §13 card |
| C7 | Lace Mill: 55 affordable apartments, artist preference, 100+-year-old lace curtain mill, Cornell St | rupco.org/property/the-lace-mill/ ; thelacemillarts.com | fiber-optic-installation.md | §7 mill card; §13 Broadway card |
| C8 | HealthAlliance Hospital, 105 Mary's Ave, opened 2022 | wmchealth.org press release Nov 19 2025 | fiber-optic-installation.md | §8 Broadway card |
| C9 | Former IBM campus (iPark 87), Enterprise Drive: East Campus hosts Ulster BOCES CTC and Archtop Fiber | ulstercountyny.gov newsroom 2026-02-27 | fiber-optic-installation.md; cat6-repair.md U3 | §8 Town of Ulster card |
| C10 | Uptown Kingston Wall Street and North Front lined with shops, restaurants, wine bars | goloveny.com | smart-lock-installation.md U22 | §8 Uptown card |
| C11 | New Paltz Main Street (Route 299) village shopping/restaurants | iloveny.com | smart-lock-installation.md U24 | §8 New Paltz card |
| C12 | SUNY New Paltz: 6,197 undergraduates, 1,036 graduate | newpaltz.edu/about/glance.html | smart-lock-installation.md U9 | §5.5 bullet 3; Town by town |
| C13 | Earth Networks 2020: Ulster 182,760 lightning pulses, 49 thunder days | get.earthnetworks.com 2021 State Lightning Report NY | smart-lock U19; fiber | §5 para 4; §9 Q lightning |
| C14 | Daily Freeman Sept 27 2026: nor'easter peak >14,000 Ulster outages; Central Hudson 93,209 Ulster customers | dailyfreeman.com/2026/09/27/noreaster-day-two-… | soundbar-installation.md | §5.5 bullet 6; §9 Q Central Hudson power |
| C15 | Cell dead zones: gaps along Routes 212 and 28; worst ZIPs 12464 Phoenicia, 12452 Lexington/Shandaken, 12477 Saugerties, 12458 West Hurley (HV1, Dec 29 2016) | hudsonvalleyone.com/2016/12/29/dead-zones-… | smart-lock-installation.md U8 | §5 para 4; §9 Q dead zone |
| C16 | Archtop Fiber HQ Kingston; turned on Kingston area (Mar 2024) and Saugerties (Apr 2024); construction in Woodstock (Oct 2024); Planet Networks in Saugerties/Kingston | archtopfiber.com blog 2024-10-01; hudsonvalleyone.com 2024/05/15 | fiber-optic-installation.md; cat6-repair.md U1 | §9 Q fiber; Town by town (Saugerties) |
| C17 | Ulster BEAD approval May 1 2026: all 1,293 unserved locations to get fiber | ulstercountyny.gov newsroom 2026-05-01 | fiber-optic-installation.md | §9 Q fiber |
| C18 | Kingston STR: form-based code 2023; STR-F capped at 1% (112 as of Sept 2026); inspection before permit and every two years | kingston-ny.gov STR fact sheet | smart-lock-installation.md U5 | NOT used on final page (the STR Q&A was dropped as a duplicate intent of the old siblings' STR question) |
| C19 | Woodstock STR law: non-owner-occupied STR needs a Host living within 10 miles | Woodstock L.L. 1 of 2019 (townofmarlboroughny.gov copy) | smart-lock-installation.md U4 | Town by town (Woodstock) |
| C20 | Ulster County Code Ch. 185: "Electrical work" includes wiring for "signaling, communication, alarm or data transmission"; master electrician licence for electrical permits | ecode360.com/35131702 ; wawarsingny.gov Electrical Licensing Board PDF | fiber-optic-installation.md | §8.5 bullet 4 (line-voltage outlet by county-licensed master electrician; page does NOT assert low-voltage buzzer work needs a county licence) |
| C21 | Opus 40: bluestone earthwork by Harvey Fite in an abandoned quarry; by 1898 ≥10,000 people in Ulster made a livelihood from bluestone | opus40.org | cat6-repair.md R8 | §13 Opus 40 card |
| C22 | Ellenville / Route 209; Shawangunk Ridge | ewcoc.com | cat6-repair.md R14 | §8 Ellenville card; §13 card |
| C23 | Walkway Over the Hudson west end in Highland | parks.ny.gov; walkway.org | sonos-installation.md U11 | Town by town (Highland) |

### EMPTY (not accessible in build env / not found)
Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★; Ulster/Hudson Valley Reddit threads on buzzers or intercoms (only Kingston, Ontario results); Daily Freeman / HV1 / Kingston Wire stories on apartment entry doors or intercoms; Village of New Paltz inspection checklist contents (page says ask the building department); Kingston rental inspection checklist items for entry doors (page says the code does not publish a separate buzzer checklist and gives general practice); municipal permit rules for low-voltage entry work in Ulster towns; a sourced Ulster buzzer job for Field Notes (written as practice, labelled so).

### House practices stated on the page without an external source (FLAG for Anwar)
Fail-secure strikes as the default on residential front doors; strikes over mag locks on residential doors; per-entrance pricing lines; leaving a one-page system description for inspectors; two administrator accounts + written installer code; mounting on solid framing / mortar joints, never stone faces; recording the existing directory before a factory reset; "most entry systems working again within one to two hours of arrival" (silo convention copied from repair-capture blocks); "travel folded into the quote" and "$200–$400 bundling saving" (both from the old Ulster page).

### Images (11) — Step C / permanent image rule
Drive "AESS Website Photos" has no door-buzzer folder (coordinator); CompanyCam not connected. **images/buzzer-repair/ (19 files) REJECTED as AI-generated** after viewing three (basement-buzzer-terminal-panel, lobby-directory-panel-diagnostics, weathered-entry-panel-weather-sealing): garbled tool/label text ("Tempo 200EF"), duplicated directory labels, uniform 1402×1122 renders, staged branded uniforms — the set should not be used anywhere. Used instead: 8 manufacturer product shots + 3 real AESS job photos from other jobs (cropped). All viewed before naming; captions say "Manufacturer product photo, not an installation photo" or "Example photo from another AESS job (not in Ulster County, no business named)".
| New file (images/door-buzzer-installation/) | Source | Notes |
|---|---|---|
| door-buzzer-installation-ulster-county-single-button-video-door-station.webp (hero, eager) | images/akuvox-video-door-station.webp | product shot |
| …-pill-shaped-video-intercom.webp | images/digital-watchdog-megapix-intercom.jpg | product shot |
| …-dome-camera-in-old-plaster-corner.webp | images/nassau-window-depot-storage-camera.jpeg | real job photo; cropped (0,0,730,700) to remove boxes with brand/handwritten "2024" text and clutter |
| …-keypad-entry-panel-with-camera.webp | images/intercom-keypad-akuvox.png | product shot (RGBA flattened on white) |
| …-black-video-doorbell-with-call-button.webp | images/akuvox-video-doorbell-black.webp | product shot |
| …-indoor-answering-monitor.webp | images/intercom-indoor-monitor.png | product shot |
| …-narrow-video-intercom-for-door-frame.webp | images/axis-i8116-video-intercom.webp | product shot |
| …-slim-black-video-entry-reader.webp | images/avigilon-video-door-entry.jpg | product shot (RGBA flattened on white) |
| …-touchscreen-directory-entry-panel.webp | images/intercom-touchscreen.png | product shot (was the old page's only image) |
| …-camera-covering-corridor-to-service-door.webp | images/rockland-toyota-hallway-camera.jpeg | real job photo; cropped (295,0,935,905) to remove a brand poster with QR code and a key tag |
| …-small-camera-on-plain-wall.webp | images/rockland-toyota-wall-camera.jpeg | real job photo; no text in frame |
DAILY-LOG note suggestion: `images: 8 manufacturer product shots + 3 real AESS photos from other jobs (no real door-buzzer photos; images/buzzer-repair/ rejected as AI-generated)`.

### Keyword notes (Ulster page)
- Service: door buzzer installation Ulster County, apartment buzzer Kingston NY, video entry New Paltz, electric strike installation, buzzer upgrade existing wiring, intercom for two-family house.
- Problem: shared front door propped open, separate doorbells per flat, dead release, door won't latch, outage, lost codes after sale, student turnover, STR guest entry, landmark approval.
- Technology: two-wire multi-tenant (Aiphone GT), handsets, monitors, phone answering, cloud vs local, cellular call box, fail-secure strike, magnetic lock + sensor release, battery backup, surge protection.
- Industry: two- to four-family owners, ETPA buildings, garden complexes, student rentals, Main Street mixed-use, STR hosts, senior housing, out-of-county owners and managing agents.
- Geographic: Ulster County; Kingston (Stockade/Uptown, Wall St, North Front St, Rondout/East Strand, Midtown/Broadway, Cornell St, Mary's Ave), New Paltz (Main St/Route 299, Huguenot St), Saugerties (Main & Partition Sts), Ellenville (Canal St, Route 209), Woodstock, Stone Ridge, Gardiner, Hurley, Rosendale, Highland, Lloyd, Marlborough, Phoenicia, Shandaken, West Hurley, Town of Ulster (Route 9W, Enterprise Dr).

### Masked-geo similarity (difflib, p/li/td/h2/h3/figcaption ≥8 words, geo names masked)
Measured against all 15 silo pages after the final edit round: mean best-block similarity 0.38 vs every sibling; maximum 0.61 (Westchester, Video/Small package card - since rewritten, re-measured 0.39), then 0.60 (hero sub-tagline 'Audio & Video Entry / Electric Strikes / ...' vs NYC/borough pages). No block >= 0.65. (First draft had one package-card block at 0.67 vs Dutchess; rewritten.) File size about 173 KB vs siblings 139,980-143,248 B (no 2 KB cluster).

### Build notes
- `tools/check_page.py door-buzzer-installation-ulster-county-ny` cannot run on this silo: `identify()` only matches area suffixes at the very end of the slug, and the door-buzzer silo's area pages end in `-ny` (e.g. `-ulster-county-ny`), so it prints "can't tell the area from slug". A patched copy (scratchpad) that strips the trailing `-ny` for county/hub pages, expects the up-link `/door-buzzer-installation-hudson-valley-ny`, and treats `<silo>-<area>-ny` siblings as area pages, reports PASS (including registration checks against the existing sitemap/_redirects entries).

## Question register

Every question (H2/H3/summary ending "?" and every FAQ item) on each page of the silo. The 15 non-Ulster pages are still the OLD template (pre-rebuild) and share nearly the same question set with the area name swapped; a rebuilt page must not repeat any intent below — check_page.py catches exact masked matches, meaning-level duplicates are checked by hand.

### door-buzzer-installation-ulster-county-ny (REBUILT 2026-10-18)

§9 Questions Answered — question H3s (plus the repair-capture H2 and BYOE H3):
- Front Door Won’t Release in Ulster County?
- The upstairs apartment in our converted house has its own outside stair and door. Does it need its own door station?
- Can each apartment in a divided house have a different kind of answering station?
- I own a Saugerties or Kingston building but live in the city. How do I run entry from a distance?
- What does a Kingston rental inspector look at on the entry door, and what should we have ready?
- We just bought a Kingston rental and nobody handed over the entry system codes. What now?
- Tenants want to see who called while they were out. Can the entry system keep a picture of each visitor?
- A house near SUNY New Paltz is let by the room to five students. Should every bedroom get its own call button?
- Our village rental has to pass inspection within 30 days. Will installing a buzzer delay registration?
- Students keep propping the front door. Will an entry system stop it?
- How do you bring cable into a stone house without drilling the stone?
- When Central Hudson loses power, does our front door lock or unlock?
- We are on a hill above Rosendale where lightning hits often. How do you protect the system?
- Fiber just reached our Kingston street. Should the new entry system run over the internet?
- How do you separate the store entrance from the apartment entrance on a Main Street building?
- Our Rondout building’s basement floods at the highest tides. Where should the power supply go?
- Our tenants are mostly older residents. What makes an entry panel easier for them to use?
- Already bought your entry panel?

§9 statement H3s (intents covered on the page, phrased as statements because an old sibling already asks a related question — do not reuse these intents as questions either): 
- Uptown Kingston: Wall Street and North Front Street
- What a real entry system adds to a Kingston two-family with one shared front door and a doorbell per flat
- Putting video on the thin bell wire stapled up a third-floor stair
- Kingston Apartments, Rent Rules and Inspections
- Rent-stabilized Kingston buildings: entry failures and the state’s service complaint forms
- Multiple Dwelling Law or Multiple Residence Law: which one governs a Kingston or New Paltz apartment house
- Kingston’s preservation commission and a new panel on a Stockade or Rondout facade
- A north-facing panel on an unheated porch through an Ulster winter
- Magnetic locks on an apartment-house main entrance: what the code asks for
- Phone answering for buildings in the Route 28 and Route 212 dead zones
- Six entrances on one garden-apartment complex, one controller

§17 FAQ (= FAQPage schema):
- Does a new entry system need its own electrical outlet?
- Can a tenant add their own smart doorbell at the apartment door upstairs?
- How long does the front door stay unlocked after someone presses release?
- Can couriers get into the hallway to leave packages when nobody is home?
- What do you need from us before the walkthrough?
- Why does our door still not lock after the buzzer was replaced?
- Can one apartment’s calls ring two roommates’ phones at once?
- Do you take out the old panel and patch the opening?
- What does the $300 service call booked online cover?
- Will the new system work if the building’s internet is off?

De-dup notes (meaning level, vs old siblings): two-family entry setup (old "I rent out the second unit in my two-family"), reuse of old 2-wire cable, tenant recourse ("My landlord won't fix…"), which law requires an intercom ("As a landlord, am I required…"), landmark work / permits, weather-damaged panels, strike-vs-maglock, Wi-Fi/rural doorbells and multi-building garden complexes were all turned into statement headings on the Ulster page; the Ulster STR question was dropped (old "How do I manage buzzer access for a short-term rental?") and the video-doorbell-vs-intercom FAQ was replaced (old "Is a video doorbell or a wired intercom better…").

### Old-template sibling pages (as on disk 2026-10-18, before their rebuilds)

#### door-buzzer-installation-bronx-ny 32
- How much does it cost to install a door buzzer in a Bronx apartment building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do you handle large Bronx co-op developments?
- Who fixes door buzzers in the Bronx — and do I need a licensed contractor?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a large Bronx building without rewiring?
- A whole line of apartments lost the buzzer — what causes that?
- Can I buzz my building’s door open from my phone?
- As a Bronx landlord, am I required to keep the buzzer working?
- My landlord won’t fix the broken buzzer — what can Bronx tenants do?
- One tenant won’t let us in to install their unit — the whole line is down. What now?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our lobby panel keeps getting vandalized — what holds up?
- Ready to secure your Bronx building’s entrance?
- 🔔 Buzzer Broken in the Bronx?
- Do you need a permit for a door buzzer in the Bronx?
- How long does buzzer installation take?
- Can old 2-wire cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of the Bronx do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Do you handle large co-op developments?
- Can you provide documentation for my co-op board?
- How do I book a buzzer service call?
- Do you work with supers and managing agents?
- Can you match new hardware to my existing system?
- Do you install ADA-compliant entry panels?
- Will a new buzzer disrupt my tenants?
- What payment do you accept?
- Can you install at multiple buildings in a portfolio?
#### door-buzzer-installation-brooklyn-ny 32
- How much does it cost to install a door buzzer in a Brooklyn apartment building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- How do people fix the intercom in a Brooklyn apartment?
- Do I need a licensed contractor to install a building buzzer in Brooklyn?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a Brooklyn brownstone without rewiring?
- Can you mount a panel on a landmark brownstone without damaging the facade?
- Can I buzz my building’s door open from my phone?
- As a Brooklyn landlord, am I required to keep the buzzer working?
- My landlord won’t fix the broken buzzer — what can Brooklyn tenants do?
- How do I handle buzzer access when tenants move out constantly?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our walk-up’s panel keeps getting vandalized — what holds up?
- Ready to secure your Brooklyn building’s entrance?
- 🔔 Buzzer Broken in Brooklyn?
- Do you need a permit for a door buzzer in Brooklyn?
- How long does buzzer installation take?
- Can old pre-war 2-wire cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of Brooklyn do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Can you do landmark-compliant work in historic districts?
- Can you provide documentation for my co-op board?
- How do I book a buzzer service call?
- Do you work with supers and managing agents?
- Can you match new hardware to my existing pre-war system?
- Do you install ADA-compliant entry panels?
- Will a new buzzer disrupt my tenants?
- What payment do you accept?
- Can you install at multiple buildings in a portfolio?
#### door-buzzer-installation-dutchess-county-ny 31
- How much does a door buzzer cost in Dutchess County?
- Is it cheaper to repair my old buzzer or replace it?
- Do you actually come out to Dutchess, or just route the lead?
- Do I need a licensed contractor for an apartment building buzzer?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to an older Dutchess building without rewiring?
- Can residents buzz the door open from a phone?
- How far can a gate intercom be from an estate house?
- What’s the best entry for a Beacon loft?
- What’s the best setup for a Rhinebeck or Millbrook estate?
- Can you do controlled entry for a Dutchess office or storefront?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Dutchess entrance?
- 🔔 Buzzer Broken in Dutchess?
- Do you need a permit for a door buzzer in Dutchess County?
- How long does installation take?
- Do you charge extra to travel to Dutchess?
- Can a buzzer work with my existing door lock?
- What areas of Dutchess County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Dutchess pricing different from NYC?
- Can you retrofit a Beacon mill or loft conversion?
- How do I book a service call?
- Do you work with apartment building managers?
- Can you install a gate intercom on an estate?
- Can you pre-wire entry into a new-construction home?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-hudson-valley-ny 32
- How much does door buzzer installation cost in the Hudson Valley?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do I need a licensed contractor to install a building buzzer in the Hudson Valley?
- Do you actually travel to the Hudson Valley, or just NYC?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a historic conversion without rewiring?
- Can I buzz my building’s door open from my phone?
- What’s the difference between an electric strike and a maglock?
- I own a single home in the Hudson Valley — do I need a building-style buzzer?
- What do commercial properties in the Hudson Valley need for entry?
- How do I manage buzzer access for a short-term rental?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our complex’s buzzer panel keeps getting weather-damaged — what holds up?
- Ready to secure your Hudson Valley entrance?
- 🔔 Buzzer Broken in the Hudson Valley?
- Do you need a permit for a door buzzer in the Hudson Valley?
- How long does buzzer installation take?
- Can old 2-wire intercom cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of the Hudson Valley do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Is there a trip charge for Hudson Valley jobs?
- How do I book a buzzer service call?
- Do you work with property managers and HOAs?
- Can you match new hardware to my existing system?
- Do you install ADA-compliant entry panels?
- How soon can you come out?
- Will a new buzzer disrupt my residents?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-long-island-ny 32
- How much does door buzzer installation cost on Long Island?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do I need a licensed contractor to install a building buzzer on Long Island?
- Do you actually serve all of Long Island, or just Nassau?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to an older complex without rewiring?
- Can I buzz my building or gate open from my phone?
- What’s the difference between an electric strike and a maglock?
- I own a single home or estate on Long Island — do I need a building-style buzzer?
- What do gated communities and HOAs need for entry?
- What do Long Island commercial properties need?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our complex’s buzzer panel keeps getting weather-damaged — what holds up?
- Ready to secure your Long Island entrance?
- 🔔 Buzzer Broken on Long Island?
- Do you need a permit for a door buzzer on Long Island?
- How long does buzzer installation take?
- Can old 2-wire intercom cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of Long Island do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Is there a trip charge for Long Island jobs?
- How do I book a buzzer service call?
- Do you work with property managers and HOAs?
- Can you match new hardware to my existing system?
- Do you install ADA-compliant entry panels?
- How soon can you come out?
- Can you install gate and driveway intercoms?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-manhattan-ny 32
- How much does it cost to install a door buzzer in a Manhattan apartment building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do I need a licensed contractor to install a building buzzer in Manhattan?
- How do I know a buzzer installer actually knows pre-war Manhattan buildings?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a pre-war Manhattan building without rewiring?
- My building’s audio goes to static when it rains — can that be fixed?
- Can I buzz my building’s door open from my phone?
- As a Manhattan landlord, am I required to keep the buzzer working?
- My landlord won’t fix the broken buzzer — what can tenants do?
- Can a Manhattan landlord switch us to a phone-based system that needs our cell?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our walk-up’s panel keeps getting vandalized — what holds up?
- Ready to secure your Manhattan building’s entrance?
- 🔔 Buzzer Broken in Manhattan?
- Do you need a permit for a door buzzer in Manhattan?
- How long does buzzer installation take?
- Can old pre-war 2-wire cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of Manhattan do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Can you provide documentation for my co-op board?
- Can you help clear an HPD violation for a broken buzzer?
- How do I book a buzzer service call?
- Do you work with supers and managing agents?
- Can you match new hardware to my existing pre-war system?
- Do you install ADA-compliant entry panels?
- Will a new buzzer disrupt my tenants?
- What payment do you accept?
- Can you install at multiple buildings in a portfolio?
#### door-buzzer-installation-nassau-county-ny 31
- How much does a door buzzer or video doorbell cost in Nassau County?
- Is a video doorbell or a wired intercom better for my Nassau home?
- Do you actually come out to Nassau, or just route the lead?
- Do I need a licensed contractor for a co-op or apartment building buzzer?
- Can I install a gate intercom myself on my estate property?
- Why not just buy a doorbell kit from a big-box store?
- How far can a gate intercom be from the house?
- Can you add video to a Long Beach co-op without rewiring?
- Can I see and open my door or gate from my phone?
- What’s the best entry setup for a North Shore estate?
- My battery video doorbell keeps dying in winter — what’s better?
- Can you do controlled entry for a Nassau office or storefront?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Nassau County entrance?
- 🔔 Buzzer or Doorbell Broken in Nassau?
- Do you need a permit for a door buzzer in Nassau County?
- How long does installation take?
- Do you charge extra to travel to Nassau?
- Can a buzzer work with my existing door or gate lock?
- What areas of Nassau County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Nassau pricing different from NYC?
- Can you install a gate intercom on a long driveway?
- How do I book a service call?
- Do you work with co-op boards and managing agents?
- Hardwired or battery video doorbell?
- Will coastal salt air damage the hardware?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-nyc 32
- How much does it cost to install a door buzzer in a NYC apartment building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do I need a licensed contractor to install a building buzzer in NYC?
- How do I know a buzzer installer actually knows NYC buildings?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a pre-war building without rewiring?
- Can I buzz my building’s door open from my phone?
- What’s the difference between an electric strike and a maglock for my door?
- As a NYC landlord, am I required to keep the buzzer working?
- My landlord won’t fix the broken buzzer — what can tenants do?
- How do I handle buzzer access when tenants move out constantly?
- Why does my buzzer let people in but I can’t hear who’s there?
- Our building’s buzzer panel keeps getting vandalized — what holds up?
- Ready to secure your building’s entrance?
- 🔔 Buzzer Broken in NYC?
- Do you need a permit for a door buzzer in NYC?
- How long does buzzer installation take?
- Can old 2-wire intercom cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas does Abstract Enterprises cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Can you provide documentation for my co-op board?
- How do I book a buzzer service call?
- Do you work with building supers and managing agents?
- Can you match new hardware to my existing system?
- Do you install ADA-compliant entry panels?
- How soon can you come out?
- Will a new buzzer disrupt my tenants?
- What payment do you accept?
- Can you install at multiple buildings in a portfolio?
#### door-buzzer-installation-orange-county-ny 31
- How much does a door buzzer or video doorbell cost in Orange County?
- Why does a farm or big-lot install cost more than a village home?
- Do you actually come out to Orange County, or just route the lead?
- Do I need a licensed contractor for an apartment building buzzer?
- Can I install a gate intercom myself on my farm or big lot?
- Why won’t a wireless video doorbell work on my rural property?
- How far can a gate intercom be from a farmhouse?
- Can you pre-wire entry into my new-construction home?
- Can I see and open my door or gate from my phone?
- My battery video doorbell keeps dying in winter — what’s better?
- What entry setup works best for a working farm?
- Can you do controlled entry for an Orange office, store, or winery?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Orange County entrance?
- 🔔 Buzzer or Gate Intercom Broken in Orange?
- Do you need a permit for a door buzzer in Orange County?
- How long does installation take?
- Do you charge extra to travel to Orange County?
- Can a buzzer work with my existing door or gate lock?
- What areas of Orange County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Orange County pricing different from NYC?
- Can you install a gate intercom on a long farm driveway?
- Can you pre-wire entry into a new-construction home?
- How do I book a service call?
- Will a wired system work where my Wi-Fi doesn’t reach?
- Do you work with apartment building managers?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-putnam-county-ny 31
- How much does a door buzzer or video doorbell cost in Putnam County?
- Why does a gate install cost more than a front-door doorbell?
- Do you actually come out to Putnam County, or just route the lead?
- Do I need a licensed contractor for a gate intercom?
- Can I install a gate intercom myself on my wooded lot?
- Why won’t a wireless video doorbell work on my rural property?
- How far can a gate intercom be from a Putnam house?
- Can I answer my lake house or weekend home from the city?
- Will a wired system work where my Wi-Fi doesn’t reach?
- What entry works best for a lakefront home?
- My battery video doorbell keeps dying in winter — what’s better?
- Can you do controlled entry for a Putnam office or storefront?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Putnam County entrance?
- 🔔 Buzzer or Gate Intercom Broken in Putnam?
- Do you need a permit for a door buzzer in Putnam County?
- How long does installation take?
- Do you charge extra to travel to Putnam County?
- Can a buzzer work with my existing door or gate lock?
- What areas of Putnam County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Putnam County pricing different from NYC?
- Can you install a gate intercom on a long wooded driveway?
- Can I manage entry to my weekend home from the city?
- How do I book a service call?
- Will waterfront exposure damage the hardware?
- Hardwired or battery video doorbell?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-queens-ny 32
- How much does it cost to install a door buzzer in a Queens apartment building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do you handle large multi-building garden complexes in Queens?
- Do I need a licensed contractor to install a building buzzer in Queens?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to a post-war Queens co-op without rewiring?
- Can a buzzer directory work for tenants who speak different languages?
- Can I buzz my building’s door open from my phone?
- As a Queens landlord, am I required to keep the buzzer working?
- My landlord won’t fix the broken buzzer — what can Queens tenants do?
- How do I manage buzzer access across a co-op complex with constant move-ins?
- Why does my buzzer let people in but I can’t hear who’s there?
- One building in our complex works but another doesn’t — why?
- Ready to secure your Queens building’s entrance?
- 🔔 Buzzer Broken in Queens?
- Do you need a permit for a door buzzer in Queens?
- How long does buzzer installation take?
- Can old post-war 2-wire cable be reused for a buzzer?
- Can a buzzer work with my existing door lock?
- What areas of Queens do you cover?
- Are you licensed and insured?
- Do you offer a warranty on buzzer installation?
- Can you wire a multi-building garden complex?
- Can you provide documentation for my co-op board?
- How do I book a buzzer service call?
- Do you work with supers and managing agents?
- Can you match new hardware to my existing post-war system?
- Do you install ADA-compliant entry panels?
- Will a new buzzer disrupt my tenants?
- What payment do you accept?
- Can you install at multiple buildings in a portfolio?
#### door-buzzer-installation-rockland-county-ny 31
- How much does a door buzzer or video doorbell cost in Rockland County?
- Is a video doorbell or a multi-station system better for my home?
- Do you actually come out to Rockland, or just route the lead?
- Do I need a licensed contractor for an apartment building buzzer?
- Can I install a gate intercom or apartment buzzer myself?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to an older Rockland building without rewiring?
- Can I see and open my door or gate from my phone?
- How do you set up a buzzer for a large multi-generational home?
- My battery video doorbell keeps dying in winter — what’s better?
- What entry works for a riverfront home in Nyack?
- Can you do controlled entry for a Rockland office or storefront?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Rockland entrance?
- 🔔 Buzzer Broken in Rockland?
- Do you need a permit for a door buzzer in Rockland County?
- How long does installation take?
- Do you charge extra to travel to Rockland?
- Can a buzzer work with my existing door or gate lock?
- What areas of Rockland County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Rockland pricing different from NYC?
- Can you set up a buzzer for a large multi-family home?
- How do I book a service call?
- Do you work with apartment building managers?
- Will river-air exposure damage the hardware?
- Hardwired or battery video doorbell?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-staten-island-ny 32
- How much does a door buzzer or video doorbell cost on Staten Island?
- Is a video doorbell or a wired intercom better for my SI home?
- Why not just buy a doorbell kit from a big-box store and install it myself?
- Do I need a licensed contractor for a North Shore apartment building buzzer?
- Can I install a gate intercom myself?
- Can I keep my old handsets and just upgrade the front panel?
- How far can a gate intercom be from the house?
- Can I see and open my door or gate from my phone?
- Can you add video to my North Shore building without rewiring?
- As a Staten Island landlord, am I required to keep the buzzer working?
- My landlord won’t fix the buzzer in my SI apartment — what can I do?
- I rent out the second unit in my two-family — what entry setup is best?
- My battery video doorbell keeps dying in winter — what’s better?
- Our North Shore building’s panel keeps getting weather-damaged — what holds up?
- Ready to secure your Staten Island entrance?
- 🔔 Buzzer or Doorbell Broken on Staten Island?
- Do you need a permit for a door buzzer on Staten Island?
- How long does installation take?
- Do you charge extra to come to Staten Island?
- Can a buzzer work with my existing door or gate lock?
- What areas of Staten Island do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- Do you charge a travel fee to Staten Island?
- Can you install a gate intercom on a long driveway?
- How do I book a service call?
- Can you do a two-family home setup?
- Hardwired or battery video doorbell?
- Do you work with North Shore building managers?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-suffolk-county-ny 31
- How much does a door buzzer or gate intercom cost in Suffolk County?
- Why does a Hamptons install cost more than a Huntington one?
- Do you actually come out to the East End, or just route the lead?
- Do I need a licensed contractor for a gated estate or condo system?
- Can I install a gate intercom myself on my estate driveway?
- Why not just use a battery video doorbell on my weekend home?
- How far can a gate intercom be from the house?
- Can I answer my Hamptons gate from the city?
- Can you integrate with my gated community’s existing access?
- What’s the best entry setup for a Hamptons estate?
- What entry works for a waterfront or Fire Island home?
- Can you do controlled entry for a Suffolk office or storefront?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Suffolk County entrance?
- 🔔 Buzzer or Gate Intercom Broken in Suffolk?
- Do you need a permit for a door buzzer in Suffolk County?
- How long does installation take?
- Do you charge extra to travel to the East End?
- Can a buzzer work with my existing door or gate?
- What areas of Suffolk County do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- How is Suffolk pricing different from NYC?
- Can you install a gate intercom on a long estate driveway?
- Can I manage entry to my seasonal home from the city?
- How do I book a service call?
- Do you work with gated communities and HOAs?
- Will coastal salt air damage the hardware?
- Hardwired or battery video doorbell?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?
#### door-buzzer-installation-westchester-county-ny 31
- How much does it cost to install a door buzzer in a Westchester building?
- Is it cheaper to repair my old buzzer or replace the whole system?
- Do you provide the documentation our co-op board requires?
- Do you actually come to Westchester, or just route the lead?
- Can I install a video door buzzer myself in my building?
- Can I keep my old handsets and just upgrade the front panel?
- Can you add a video buzzer to an older Westchester co-op without rewiring?
- Can residents buzz the door open from a phone in a high-rise?
- How far can a gate intercom be from an estate house?
- What’s the best entry for a Westchester co-op apartment?
- What’s the best setup for a Scarsdale or Bronxville estate?
- Can you do controlled entry for a White Plains office building?
- Can a buzzer manage entry for a multi-tenant commercial building?
- Ready to secure your Westchester entrance?
- 🔔 Buzzer Broken in Westchester?
- Do you need a permit for a door buzzer in Westchester?
- How long does buzzer installation take?
- Do you charge extra to travel to Westchester?
- Can a buzzer work with my existing door lock?
- What areas of Westchester do you cover?
- Are you licensed and insured?
- Do you offer a warranty on installation?
- Do you provide co-op board documentation?
- How is Westchester pricing different from NYC?
- How do I book a service call?
- Can you handle a downtown high-rise?
- Can you install a gate intercom on an estate?
- Can you match new hardware to my existing co-op system?
- Do you install ADA-compliant entry panels?
- What payment do you accept?
- Can you install at multiple properties in a portfolio?

## Bath Beach, Brooklyn — /door-buzzer-installation-bath-beach-brooklyn-ny (factory research, 2026-11-11)

- Bath Beach rental building at 8871 20th Avenue (11214) is listed with "42 units·6 floors·Built in 1948"; a tenant review's advice to the owners is "Get cameras people steal packages." No intercom/door violations listed on the page; 1 open violation, type not shown — https://www.openigloo.com/building/nyc/3328515-3064670012/brooklyn-bath-beach-8871-20-avenue-11214
- Small Bath Beach building at 77 Bay 7th Street (11228): "2 units·2 floors·Built in 1930", labelled rent-stabilized; no open violations — https://openigloo.com/building/nyc/3166016-3063580003/brooklyn-bath-beach-77-bay-7-street-11228
- Bay Vista, 8629 Bay Parkway (between 86th Street and Benson Avenue), Bath Beach: 38 units, 6 floors, "finished in 2016"; "video intercom" listed among amenities — https://www.cityrealty.com/nyc/bath-beach/bay-vista-8629-bay-parkway/85407
- Bayview Courtyard, 2286 Cropsey Avenue in Bath Beach: "a 23-story condominium" with 151 units, construction "commenced in 2019"; "Residents of Bayview Courtyard arrive to a sleek lobby with Amazon Hub package lockers." (doorman/intercom not mentioned) — https://www.cityrealty.com/nyc/market-insight/features/future-nyc/inside-bayview-courtyard-amenity-rich-brooklyn-condo-harbor-views-priced-530k/60905
- NYS Multiple Dwelling Law §50-a: buildings built or converted after 1968 with eight or more units must have an intercom linking the front door to each apartment (two-way voice); lawyer Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom"; courts treat failure to maintain intercoms as a breach of the warranty of habitability (Habitat, Feb 2024) — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- MDL §50-a covers "Class A multiple dwellings with eight or more units that were built or converted after January 1, 1968" — https://butterflymx.com/blog/nyc-intercom-law/
- BrickUnderground (Dec 18, 2014): buildings with at least eight apartments need a self-closing, self-locking front door and an intercom; pre-1968 buildings must offer them "if requested by a majority of tenants," paid for by tenants; one renter waited three months for a city inspector after a 311 complaint; repairs/installation quoted at about $2,000 to $50,000 by building size; tenant lawyer Sam Himmelstein: "That's the problem with market-rate tenants, you know what happens when they complain." — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- HPD ABCs of Housing (owners): Housing Maintenance Code violation classes — "Class A Non-Hazardous 90 Days", "Class B Hazardous 30 Days", "Class C: Self-Closing Doors | Immediately Hazardous | 14 Days"; "HPD does not wait for complaints to inspect for self-closing doors" — https://www.nyc.gov/assets/hpd/downloads/pdfs/services/abcs-of-housing-owners.pdf
- HPD press release, Nov 24, 2025: apartment and hallway doors "are required by law to close and latch automatically"; a door that won't self-close gets a "Class C immediately hazardous violation"; owners have 14 days to correct and certify; HPD issued 72,714 self-closing door violations in FY2025 and spent over $6.7 million on repairs owners did not make; Acting HPD Commissioner Ahmed Tigani: "the last thing you should have to worry about is whether your door will close behind you." — https://www.nyc.gov/site/hpd/news/079-25/self-closing-doors-save-lives
- Brownstoner forum (user nwilcke, ~2015): owner of a 3-unit home asked if a $2,000 estimate to replace a sporadically working buzzer entry system was reasonable; vendor said troubleshooting would cost about the same at $150/hour with a three-hour minimum; the owner had hoped for "a repair bill for a few hundred bucks." 0 replies — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Brownstoner forum, Oct 29, 2007 (sniec): Brooklyn house with glass-paneled double front doors and an intercom but no buzzer was told "there is no system to accomodate a buzzer"; reply from BKRed: adding one meant you'll need to "open up the walls," run wiring from doorbells to intercoms and doors and cut a channel in the doors; another reply asked if the poster didn't "want to just toss the key out the window" — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- CooperatorNews (Oct 28, 2021): Buzr Labs CEO Tony Liebel — "There is a correlation between the age of the system and how easy it is to replace," existing wiring is the biggest obstacle in older buildings, and "Fully 30 percent of packages are undelivered on the first attempt today"; a Washington Heights co-op that skipped rewiring got misrouted calls and failed audio/video and "had to rewire the entire system anyway, and at a much higher cost than we originally anticipated." — https://cooperatornews.com/article/updating-buzzer-intercom-systems
- Brooklyn Eagle, Aug 2019: Assemblymember William Colton said mail and identity theft are rampant in south Brooklyn, naming Bath Beach, Gravesend, Bensonhurst and Dyker Heights, and called for theft-proof mailboxes — https://brooklyneagle.com/articles/2019/08/16/assemblymember-says-mail-identity-theft-rampant-in-south-brooklyn/
- Brooklyn Paper 62nd Precinct blotter: Jan 30 theft of a box of wine from a delivery truck's side door at Shore Parkway and Bay 38th Street (delivery-related theft in Bath Beach) — https://www.brooklynpaper.com/62nd-pct-thief-steals-box-bath-beach-delivery-truck
- Brooklyn Eagle, Aug 12, 2019: Councilmember Justin Brannan's illegal-conversion task force (DOB, HPD, NYPD, FDNY, CB10); DOB got 5,411 Brooklyn reports of suspected illegal conversions in 2018; conversions split one- and two-family homes into more units. Bath Beach itself is not named (Bay Ridge, Dyker Heights, parts of Bensonhurst) — https://brooklyneagle.com/articles/2019/08/12/brannan-task-force-looks-to-stop-illegal-home-conversions/
- Con Edison asked southern Brooklyn (Bay Ridge, Dyker Heights, Bensonhurst and others; Bath Beach not named) to cut usage during feeder repairs, July 2020; more than 96,000 residents affected and voltage reduced 8% — https://www.amny.com/brooklyn/con-edison-calls-on-residents-of-southern-brooklyn-to-reduce-power-to-avoid-outages
- HPD / 311 / DOB intercom data specific to Bath Beach blocks: EMPTY (no building-level intercom violation found in searches)
- Reddit threads about buzzers in Bath Beach: EMPTY (searches returned no r/BathBeach or r/Brooklyn thread about Bath Beach buzzers)
- Yelp reviews of buzzer/intercom installers near Bath Beach: EMPTY (no Yelp pages returned)
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo panels: EMPTY (not accessible)

### Questions people ask — Door Buzzer Installation in Bath Beach
- Is $2,000 a reasonable estimate to install a new buzzer entry/intercom system for a 3-unit house? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Can an electric strike (buzzer) work on double front doors, and is there an alternative? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Who in Brooklyn can install a buzzer on a house that has an intercom but no door release? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Is there a video doorbell for the upper levels of a multi-family house? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- What intercom works for a three-family house? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- How do you install a video doorbell on a two-family home? — Ring community — https://community.ring.com/t/two-family-home-installation/4747
- Can two doorbells ring to one home? — Arlo community — https://community.arlo.com/t5/Arlo-Video-Doorbell-Wire-Free/Can-two-doorbells-ring-to-one-home/m-p/1871212
- What lock system do you recommend for the main entrance of a duplex? — BiggerPockets — https://www.biggerpockets.com/forums/52/topics/877598-what-lock-system-do-you-recommend-for-main-entrance-of-a-duplex
- What is an affordable option to replace a 6-unit building entry system? — Reddit r/accesscontrol — https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/
- How much does a buzzer system cost? — web search result titles — https://butterflymx.com/blog/apartment-buzzer/
- Broken buzzer in a small apartment building: repair or replace? — web search result — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Can a door buzzer be connected to my phone using the existing wires? — web search fan-out — https://butterflymx.com/blog/replace-buzzer-intercom-with-video-intercom-and-mobile-app/
- How do I get my landlord to fix a broken buzzer? — BrickUnderground — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- How do I prevent package theft in an NYC building? — BrickUnderground — https://brickunderground.com/live/how-to-prevent-package-theft-nyc
- Does a building have to have a self-closing, self-locking front door? — HPD / BrickUnderground — https://www.nyc.gov/site/hpd/news/079-25/self-closing-doors-save-lives

## Bay Ridge, Brooklyn — /door-buzzer-installation-bay-ridge-brooklyn-ny (factory research, 2026-11-11)

- HPD rule 28 RCNY §25-151 "Entrance Doors, Locks and Intercommunication Systems": (d) Class A multiple dwellings with eight or more apartments erected or converted after January 1, 1968 need automatic self-closing, self-locking entrance doors and an intercommunication system at the main entrance; (e) buildings of that kind erected or converted before January 1, 1968 must have the same from January 1, 1969 if a majority of tenants request or consent in writing; (f) self-locking doors readily openable from inside without keys; (g) "The minimal devices acceptable for the intercommunication system shall be a bell or buzzer system" (or a voice speaking-and-listening device) plus a return buzzer to release the lock; (h) intercom placed so a person can reach the door when the unlocking buzzer sounds; (i) push buttons no more than six feet off the floor, speaking-and-listening device between four and five feet off the floor; (j) apartment device readily accessible to the occupant; (k) devices approved by the Department of Buildings or previously by the BSA; previously installed devices in good working condition may be accepted — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-57173
- PLUTO (carried from the AESS door-buzzer-repair Bay Ridge research, NYC Open Data 64uk-42ks, ZIP 11209): 167 elevator-building (D-class) lots holding 12,380 units; only 8 of the 167 (715 units) built 1968 or later — so nearly all Bay Ridge apartment buildings fall under the pre-1968 "tenants request in writing" clause rather than the automatic post-1968 rule; elevator buildings concentrate on Shore Road (25 lots / 2,850 units), Fourth Avenue (25 / 1,674), Ridge Boulevard (22 / 1,269), Ovington Avenue (10 / 658) and Colonial Road (5 / 321); two-family B1 lots 2,057 (4,114 units); 8,094 residential lots, 32,764 units in the ZIP — https://data.cityofnewyork.us/resource/64uk-42ks.json
- HPD violations (carried, NYC Open Data wvxf-dwi5, ZIP 11209, descriptions containing INTERCOM): 221 intercom violations (Class A 53, B 165, C 3); 26 issued in 2026 to Oct 22, the highest year, vs 17 in 2025 and 5 in 2024; 80 open at 52 buildings — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- 311 (carried, NYC Open Data erm2-nwe9, ZIP 11209, descriptor BELL/BUZZER/INTERCOM): 2020 37, 2021 28, 2022 33, 2023 37, 2024 36, 2025 39, 2026 47 (to Oct 22) — https://data.cityofnewyork.us/resource/erm2-nwe9.json
- NYC311 "Apartment Maintenance Complaint" lists "Doorbells, buzzers, or intercoms that are broken or missing" for both apartments and public areas; "HPD investigates maintenance complaints and issues violations to owners who break the law" — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Habitat Magazine (Feb 26, 2024): courts treat a working intercom as an essential service under the warranty of habitability; Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom" — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brownstoner (Aug 12, 2024): 476 72nd Street, Bay Ridge, a tapestry brick row house "set up as a two-family" with "an apartment per floor"; builder Patrick J. Carley bought the block front in 1915; circa-1940 tax photo shows "the front door has been changed"; laundry and storage in the basement — https://www.brownstoner.com/real-estate-market/bay-ridge-476-72nd-street-two-family/
- Brownstoner (carried, Aug 26, 2026): 9437 Shore Road, six-story 55-unit Art Moderne co-op (rental 1940), listing caption "entry with lobby doors, intercom system" — https://www.brownstoner.com/real-estate-market/condo-co-op-of-the-day/bay-ridge-one-bedroom-9437-shore-road-normandy/
- City & State (Dec 16, 2024): City of Yes bars backyard ADUs in the Special Bay Ridge District (est. 1978, west of Ridge Boulevard and southwest of Marine Avenue); "The Bay Ridge carveout does not apply to basement units" — https://www.cityandstateny.com/policy/2024/12/justin-brannans-council-district-got-nifty-little-city-yes-carveout/401706/
- Lucid Rents Bay Ridge 11209 report card: renters 64% (Census ACS) — https://lucidrents.com/nyc/neighborhood/bay-ridge-11209
- Security Sales (Jun 15, 2016): Park Vanderbilt, Park Slope, seven-story 148-unit co-op built 1963, Aiphone video intercoms for $110,000; installer reused the old audio intercom cable except two units; Dan Arnold (Academy Mail Box): "By using the existing cable – with the exception of two units – we were able to save $20,000 on the job"; completed in three weeks — https://www.securitysales.com/access/brooklyn_housing_co_op_upgrades_security_with_video_intercom_system/
- CooperatorNews (Oct 28, 2021): Washington Heights 56-unit 1938 co-op replaced panel and monitors without rewiring; afterwards calls to one apartment rang another and audio/video failed, and the building had to rewire the whole system at higher cost; Tony Liebel (Buzr Labs): "Theoretically, any system can be replaced"; 30 percent of packages undelivered on first attempt — https://cooperatornews.com/article/updating-buzzer-intercom-systems
- Brick Underground (Nov 7, 2019): service-call quotes of $195 an hour and $250 an hour plus parts; wiring faults usually at the lobby base, apartment panel, door strike or power supply; Daniel Vasquez (Paragon Security and Locksmith): "It's all in the wire connections" — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- ButterflyMX (Oct 12, 2026): small-building replacement cited at "roughly $1,500 to $2,500" (its own guide) and Swiftlane's "roughly $2,200 to $5,000 or more" for a single-entrance project; "Do not replace a system based on age alone"; wiring reuse cannot be confirmed from a photo or building age; IP/cloud systems "may involve recurring fees" — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- ButterflyMX NYC intercom law page (updated Sep 10, 2026): "Buildings with fewer than eight units are not generally treated the same way under this rule"; "A pre-1968 building may not fall under the same general intercom requirement" — https://butterflymx.com/blog/nyc-intercom-law/
- UniFi Nerds (Jul 18, 2026): whether NYC low-voltage cabling needs a permit "depends on scope and how the project is filed"; "building management may still require documentation, insurance, and approved pathways" — https://unifinerds.com/low-voltage-wiring-codes-nyc-contractors/
- Brownstoner forum (Oct 29, 2007): owner asks whether an electric strike can go on double doors; BKRed: "You'll need to open up the walls, probably quite a bit" — wiring must run down the doors to the locks — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Brownstoner forum: 3-family owner wants "a smart buzzer/intercom system to buzz people in remotely"; Brownstone Home Inspection reply: older mortise locks open at the latch, while modern Schlage-style smart locks often use the lock side; hardwired systems need a low-voltage installer — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- Brownstoner forum: 6-apartment Brooklyn co-op installed ABB Welcome video/audio intercom — 6 internal stations, 1 outdoor main station with camera, two new door strikes — https://www.brownstoner.com/forum/renovation/recommendation-for-video-and-audio-intercom-system
- Reddit r/AskNYC (Jan 2026 snapshot): "New Apartment Has No Voice Intercom, Only a Doorbell" — "I can't see or hear who is at the front of the building, and I get buzzed all day for other apartments"; "The bell isn't even labeled on the outside of the building" — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- Reddit r/jerseycity (Apr 2026 snapshot, not NYC): a newly added second lock made the buzzers "100% unusable"; packages missed — https://reddit.sentinel-team.org/posts/1sp8bst/snapshots/2026-04-24T21%3A40%3A02.278891Z
- Bay Ridge-specific Reddit threads on buzzers/intercoms: EMPTY
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo question boxes: EMPTY (search tool returns links only)
- Yelp 1–3★ for Bay Ridge intercom installers: EMPTY
- Bay Ridge local news on intercom/buzzer installation: EMPTY (only police-blotter items without entry details)

### Questions people ask — Door Buzzer Installation in Bay Ridge
- Can an electric strike buzzer be installed on double doors? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Can we add a smart buzzer to a three-family so we can buzz people in remotely? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- Will a smart lock work with a buzzer release, or does it open the wrong side? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- Who installs a hardwired buzzer — an electrician, a low-voltage installer, or the homeowner? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- My apartment is the only one with a doorbell and no voice intercom — what can be done? — Reddit r/AskNYC — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- I get buzzed all day for other apartments because my button isn't labeled — how should the directory be set up? — Reddit r/AskNYC — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- Is a landlord required to provide a buzzer or doorbell? — Reddit r/jerseycity — https://reddit.sentinel-team.org/posts/1sp8bst/snapshots/2026-04-24T21%3A40%3A02.278891Z
- Does a building with fewer than eight apartments have to have an intercom? — ButterflyMX — https://butterflymx.com/blog/nyc-intercom-law/
- Does an older (pre-1968) building have to install an intercom? — ButterflyMX / 28 RCNY 25-151 — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-57173
- How high should the buzzer buttons and speaker be mounted? — 28 RCNY 25-151 — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-57173
- Can the old intercom cable be reused for a video system? — Security Sales / CooperatorNews — https://www.securitysales.com/access/brooklyn_housing_co_op_upgrades_security_with_video_intercom_system/
- Should we repair or replace an old buzzer system? — ButterflyMX — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Do video intercoms have monthly fees? — ButterflyMX — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Do I need a permit for low-voltage intercom wiring in NYC? — UniFi Nerds — https://unifinerds.com/low-voltage-wiring-codes-nyc-contractors/
- How much does it cost to install a buzzer system in a small apartment building? — search result titles (Swiftlane/ButterflyMX) — https://swiftlane.com/blog/apartment-intercom-installation-cost/

## Bedford-Stuyvesant, Brooklyn — /door-buzzer-installation-bedford-stuyvesant-brooklyn-ny (factory research, 2026-11-11)

- HPD intercom violations (novdescription contains INTERCOM), Brooklyn Community Board 3, by inspection year: 2017 130, 2018 114, 2019 135, 2020 108, 2021 118, 2022 128, 2023 109, 2024 120, 2025 139 (highest year on record), 2026 101 through early November. Before 2005 never more than 12 a year. (Query run Nov 11 2026; CB3 is close to but not exactly the neighborhood.) — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- HPD intercom/buzzer violations in CB3 since Jan 1 2020: 993 in total, of which 946 carry order 501 ("§ 27-2005 HMC: properly repair or replace the broken or defective ... intercom"). The owner's duty is "repair or replace" under Housing Maintenance Code § 27-2005. — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- Recent CB3 violation wording (Sept–Nov 2026) names the whole chain: "BELL BUZZER INTERCOM SYSTEM FROM BUILDING ENTRANCE DOOR TO THE WALL PANEL", "BUZZER AND RETURN VOICE INTERCOM SYSTEM FROM BUILDING ENTRANCE DOOR UP TO PANEL", "INTERCOM RELAY FROM BUILDING FRONT ENTRANCE", "BELL BUZZER / VOICE INTERCOM FROM VESTIBULE TO KITCHEN EAST WALL RETURN VOICE PANEL". Classes A and B both appear. — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- Phone-based entry systems are written up too: Sept 12 2026 Class B "REPAIR OR REPLACE THE BROKEN OR DEFECTIVE INTERCOM SYSTEM FROM BUILDING FRONT TO CELL PHONE"; July 8 2024 "...TO RETURN BUZZER AT TENANT CELL PHONE"; June 10 2023 Class A "...TO RETURN BUZZER AT TENANT'S PHONE". So an app/cell-call system is held to the same repair duty as a wired one. — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- 311 BELL/BUZZER/INTERCOM complaints, community board 03 BROOKLYN, by year: 2020 196, 2021 297, 2022 271, 2023 299, 2024 317, 2025 312, 2026 287 (to Nov 11). — https://data.cityofnewyork.us/resource/erm2-nwe9.json
- News 12 Brooklyn, March 18 2026: tenants of a four-story apartment building on Bedford Avenue in Bed-Stuy said the front door locks had been broken for at least four months; tenant Ethel Ellerbe: "We can't have people coming in and out of here." C+C Apartment Management said the access card reader was inoperable and needed replacement; HPD said it had issued violations and was using its Emergency Repair Program. — https://brooklyn.news12.com/bed-stuy-tenants-say-apartment-building-has-had-broken-locks-for-4-months
- NYC Local Law 63 of 2021 (Tenant Data Privacy Law): applies to owners of multiple dwellings that use keyless entry (fobs, apps, RFID cards, biometrics) for a Class A multiple dwelling, its common areas or units; "The smart access system must have robust security and safeguards"; owners must get express consent in writing or through an app before collecting reference data; data limited to a minimum set (name, unit and doors, contact method, lease dates, entry times/methods); authentication data deleted within 90 days unless anonymized; no selling data; no using it to harass or evict; owners cannot "require use of a smart access system to gain entry to the tenant's dwelling unit"; owners must "provide tenants with a data retention and privacy policy". — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- LPC Permit Guidebook ch. 11 (Health & Safety): "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; an intercom may go "on a fence or wall in front of the entranceway"; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; "Design, size, and finish of installations must be compatible with the architecture of the building"; staff can issue permits when criteria are met; equipment not "attached through cast iron or on any decorative surfaces"; security cameras max two per 25 feet of street frontage on small buildings. Relevant to Stuyvesant Heights, Bedford and other Bed-Stuy historic districts. — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Brownstoner forum (Oct 2007), brownstone owner with 3 ft x 10 ft glass double front doors, intercom but no buzzer, told the doors couldn't take a strike; reply (BKRed): "You'll need to open up the walls, probably quite a bit;" another: "We chose not to do the buzzer option for safety reasons." — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Brownstoner forum (c. 2012, no replies): owner of a "3 unit home" whose buzzer "works only sporadically" was quoted $2,000 for full replacement (no electrical work) or $150/hour, 3-hour minimum troubleshooting; "I was hoping for a repair bill for a few hundred bucks, not to have to spend $2000 to replace the whole thing." — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Brownstoner "From the Forum" (July 8 2019): a brownstone owner's doorbell wiring "is beyond repair, so a homeowner is going to have to rewire to get a working doorbell or find a wireless system"; "The electrician is advising that the thick walls of their brownstone might present an issue for some systems." — https://www.brownstoner.com/ask-brownstoner/wireless-doorbell-system-pros-cons
- ButterflyMX explainer: the call path and the door-release circuit are separate, "so a call can connect while the door fails to release"; the relay controls the lock electrically and doesn't physically open the door; wired audio systems typically don't need internet for basic calls; cloud video intercoms may carry recurring costs; existing analog wiring may be reused only after inspection; renters should get written permission before adding devices to shared equipment. — https://butterflymx.com/blog/apartment-buzzer/
- NYC DOB electrical permit page: "An electrical permit is required for most electrical work" by DOB-licensed electrical contractors; the page does not address low-voltage intercom/doorbell work specifically (line-voltage power for a transformer or power supply is electrician work). — https://www.nyc.gov/site/buildings/property-or-business-owner/electrical-permit.page
- National cost guides: HomeAdvisor intercom average $2,500, range $1,500–$15,000 (silo S8); Swiftlane $1,000–$5,000+ per entry door for IP/video, subscriptions $5–$15 per unit per month (silo S9). — https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/ ; https://swiftlane.com/blog/apartment-intercom-installation-cost/
- Reddit r/BedStuy buzzer/intercom install threads: EMPTY (none surfaced).
- Yelp 1–3★ for Bed-Stuy intercom installers: EMPTY (not accessible).
- Google PAA / PASF / AnswerThePublic / Bing / DuckDuckGo: EMPTY (not accessible); questions below come from forums, the explainer FAQ and city data instead.

### Questions people ask — Door Buzzer Installation in Bedford-Stuyvesant
- Can an electric strike buzzer be installed on tall glass double front doors of a brownstone? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Is it safer not to have a door-release buzzer at all? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Do the walls have to be opened to add a buzzer to a brownstone? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Is $2,000 a reasonable price to install a new 3-unit buzzer entry/intercom system? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Does a sporadic buzzer need replacing or just repair? — Brownstoner forum — same URL
- Will a wireless doorbell/buzzer work through thick brownstone walls when the old wiring is beyond repair? — Brownstoner Ask Brownstoner — https://www.brownstoner.com/ask-brownstoner/wireless-doorbell-system-pros-cons
- How can upper-floor units of a multi-family brownstone get a video doorbell? — Brownstoner forum (title only; page not readable) — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- Why does the call connect but the door won't release? — ButterflyMX FAQ/explainer — https://butterflymx.com/blog/apartment-buzzer/
- Can a renter add smart control to an existing buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- How can a property reduce buzzer bombing / strangers being buzzed in? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Can my landlord make me use an app or fob to get into my apartment, and what data can they keep? — HPD Tenant Data Privacy Law — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Where can an intercom panel go on a landmarked rowhouse, and how many are allowed? — LPC Permit Guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Does a phone/app-based intercom still count for HPD if it stops working? — HPD violation records — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- What happens when a building's card reader at the front door breaks and stays broken? — News 12 Brooklyn — https://brooklyn.news12.com/bed-stuy-tenants-say-apartment-building-has-had-broken-locks-for-4-months
- Do I need an electrician or a permit to install an intercom in NYC? — DOB electrical permit page — https://www.nyc.gov/site/buildings/property-or-business-owner/electrical-permit.page

## Bergen Beach, Brooklyn — /door-buzzer-installation-bergen-beach-brooklyn-ny (factory research, 2026-11-11)

- Bergen Beach housing for this service is house-scale: a custom-built two-family at 7119 Bergen Ct (built 2003) is zoned R3-1, has a private three-car driveway, garage, porch, terrace and a listed alarm; no intercom or doorbell system is mentioned in the listing — https://www.brownstoner.com/listing/BKMLS-6991525/7119-bergen-ct-bergen-beach-brooklyn-ny-11234
- 1242 E 68th St, Bergen Beach, is a "Brick Two Family Home": an owner's triplex plus a separate one-bedroom, one-bath rental unit "with its own private entrance", an interior garage and a private driveway for two more cars — two doors, two households, which is the typical two-family doorbell layout here — https://www.brownstoner.com/listing/BKMLS-7266595/1242-e-68th-st-bergen-beach-ny-11234
- Single-family Bergen Beach listing with "a full walk-out basement" with a half bath — a third, lower door that visitors may come to — https://www.nestseekers.com/5499366/wonderful-twobedroom-home-in-the-heart-of-the-bergen-beach/print/
- Mill Harbor, 1561 Royce St, Bergen Beach: built 2005, 208 units, 4 stories, listed as a gated community; "an intercom connects to the front desk" — condo entry is managed by the association, not individual owners — https://www.homes.com/building/mill-harbor-brooklyn-ny/xxw5gfdbrzc8s/
- NY Multiple Dwelling Law §4(6): a "private dwelling" is "any building or structure designed and occupied exclusively for residence purposes by not more than two families"; §4(7) a multiple dwelling is occupied by "three or more families living independently of each other" — so the MDL §50-a intercom mandate (8+ apartments) does not reach Bergen Beach one- and two-family houses; a buzzer there is the owner's choice — https://codes.findlaw.com/ny/multiple-dwelling-law/mdw-sect-4/
- Ring hardwired doorbells: Video Doorbell Wired needs "Hardwired transformer (10 to 24VAC, 50/60 Hz, 8VA to 40VA)"; Wired Doorbell Plus/Pro/2K Plus need "16 to 24VAC, 50/60 Hz, 10VA to 40VA"; Wired Doorbell 4K Pro and 2K Plus are "not compatible with existing chimes, unless Wired Doorbell 4K Pro is powered by PoE"; "Using incompatible power sources can damage your device and cause electric shock." — https://ring.com/us/en/support/articles/utvz2/Guidelines-for-Hardwiring-Your-Ring-Video-Doorbell
- Lorex wired video doorbells "require a constant power supply with a voltage between 16V-24V AC"; a 10V transformer is too weak; 16V-30VA and 24V-40VA listed as compatible — https://help.lorextechnology.com/link/portal/57356/57366/Article/3560/2k-video-doorbell-transformer
- Doorbell wiring is a Class 2 signaling circuit (IRC E4301.1); the transformer that converts 120V is regulated as standard electrical work and "requires a permit when installed or replaced" (IRC context, not NYC-specific) — https://www.jaspector.com/codes/irc-2018/ch43-class2-circuits/doorbell-wiring-class-2-code-irc-2018/
- Brownstoner thread (multi-family Brooklyn house, two apartments sharing an old buzzer): owner wants "to see who is at the door, not 24-7 video surveillance"; quote for a video system was over $1,500, later corrected to about $3,000; one commenter wired a SimpliSafe doorbell into the foyer and used plug-in chimes (about $40) because the old doorbell wiring was too deteriorated — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=desc
- Brownstoner thread: Brooklyn owner with glass double front doors was told they "can't accommodate an electric strike"; installer reply: "You'll need to open up the walls, probably quite a bit"; another: "Best to have tenants/owners open the door in person." — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- BiggerPockets: 3-unit owner found Ring/Wyze "consumer base and not commercial or durable enough" and worried about damaging his siding with a product that fails — https://www.biggerpockets.com/forums/52/topics/1074702-multi-unit-doorbell-suggestions
- BiggerPockets: NYC owner renovating a 3-family: "I'd like to start thinking about running a doorbell or intercom system" (no replies) — https://biggerpockets.com/forums/52/topics/734291-intercom-or-doorbell-system-for-3-family-home
- HomeServe cost guide: "Most homeowners spend between $2,085 and $2,478" for a home intercom; professional wired installation labor $1,193–$1,446 for about ten hours; wireless hardware $186–$229 — https://www.homeserve.com/blog/cost-guide/home-intercom-system
- ButterflyMX (NYC intercom repair): Connextivity estimates "$100 to $300 for diagnostics, $500 to $1,500 for component replacement, and $1,000 to $3,000 for limited wiring repairs"; article says nothing about two-family homes — https://butterflymx.com/blog/intercom-repair-nyc
- Weather: "Outdoor components usually show problems first because they face wind, snow, rain, ice, and repeated freeze-thaw cycles"; "Moisture can enter exterior panels, cable paths, and lock hardware, then condense or freeze during temperature swings" — https://butterflymx.com/blog/how-cold-weather-affects-apartment-intercoms/
- Flooding: News 12 "Bergen Beach neighbors fed up with ongoing flooding woes" (Apr 12, 2021, resident Rina Berman, water problem worse after DOT repaving); "Wet weather in Brooklyn causes flooding in Bergen Beach" (Dec 16, 2018) — https://bronx.news12.com/bergen-beach-neighbors-fed-up-with-ongoing-flooding-woes ; https://brooklyn.news12.com/wet-weather-in-brooklyn-causes-flooding-in-bergen-beach-39651184
- Video doorbells and neighbors: Habitat quotes David Amster, president of Prime Locations: "With these doorbells becoming more popular, we entered it into the house rules." — https://habitatmag.com/Publication-Content/Building-Operations/2019/2019-September/Video-Doorbell-Crime-Fighter-or-Big-Brother
- Two-button video door stations for two-tenant houses exist as standard products (e.g. DoorBird D2102V "IP Video Door Intercom for 2 Tenants, 2 Buttons") — https://www.absoluteautomation.com/products/doorbird-d2102v-mdu-ip-video-door-intercom-for-2-tenants-2-buttons-stainless-steel
- HPD violations, 311 buzzer complaints, DOB permits specific to Bergen Beach door buzzers — EMPTY
- LPC landmark rules in Bergen Beach — EMPTY (no district found)
- Reddit threads about door buzzers in Bergen Beach — EMPTY
- Yelp complaints about buzzer/doorbell installers near Bergen Beach — EMPTY
- Google PAA / PASF / AnswerThePublic / Bing / DuckDuckGo — EMPTY (no SERP feature data retrievable)

### Questions people ask — Door Buzzer Installation in Bergen Beach
- Can a battery video doorbell be mounted on top of an existing intercom, or does the intercom have to come out? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=desc
- Does each apartment in a two-family need its own video doorbell? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=desc
- Is a wired doorbell better than a battery one? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=desc
- Which video doorbells are secure and respect privacy? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=desc
- What if the old doorbell wiring is too deteriorated to use? — Brownstoner forum — same URL
- Can an electric strike be installed on double doors? What are the alternatives? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Is it safer to have people walk down and open the door themselves? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Are Ring/Wyze-type doorbells durable enough for a multi-unit house? — BiggerPockets — https://www.biggerpockets.com/forums/52/topics/1074702-multi-unit-doorbell-suggestions
- Will a failed doorbell damage my siding? — BiggerPockets — same URL
- When should I start planning the doorbell/intercom in a renovation? — BiggerPockets — https://biggerpockets.com/forums/52/topics/734291-intercom-or-doorbell-system-for-3-family-home
- How much does a home intercom cost to install? — HomeServe cost guide — https://www.homeserve.com/blog/cost-guide/home-intercom-system
- What transformer does a wired video doorbell need? — Ring / Lorex support — https://ring.com/us/en/support/articles/utvz2/Guidelines-for-Hardwiring-Your-Ring-Video-Doorbell
- Will my existing chime work with a new video doorbell? — Ring support — same URL
- Is a two-family house required by law to have an intercom? — derived from MDL §4 — https://codes.findlaw.com/ny/multiple-dwelling-law/mdw-sect-4/
- Can my tenant put up their own video doorbell? — BiggerPockets (search result "tenant asking to install a nest ring doorbell") — https://www.biggerpockets.com/forums/52/topics/839586-tenant-asking-to-install-a-nest-ring-doorbell
- Will cold and wet weather break an outdoor door station? — ButterflyMX — https://butterflymx.com/blog/how-cold-weather-affects-apartment-intercoms/

## Beverley Square, Brooklyn — /door-buzzer-installation-beverley-square-brooklyn-ny (factory research, 2026-11-11)

- City Planning Commission report N 260209 HKK (Jan 21, 2026) on the Beverley Square West Historic District: LPC designated it November 25, 2025 (LP-2692); Community District 14; along Marlborough, Rugby and Argyle Roads between Beverley and Cortelyou Roads; 118 free-standing houses, "114 of 118" built by 1906, on similarly sized 50-foot-wide lots; most have "full-width front porches", complex rooflines and angled bays; late Queen Anne, early Colonial Revival and Shingle style; zoned R3X (single- or two-family detached, 35 ft typical max height, FAR 0.75) — https://www.nyc.gov/assets/planning/download/pdf/about/cpc/260209.pdf
- LPC press release (2025): Beverley Square West = "118 houses built between 1894 and 1910" on three tree-lined streets between Beverley Road and Cortelyou Road; architects John J. Petit, John B. Slee, Benjamin Driesler; Brooklyn, Flatbush & Coney Island Railroad opened 1878 along the district's eastern boundary; LPC Vice Chair Angie Master: the districts "represent a remarkable period in Brooklyn's development"; Councilmember Rita Joseph: "we are honoring the rich architectural heritage that has shaped Flatbush for more than a century." — https://www.nyc.gov/site/lpc/about/pr2025/lpc-designates-two-new-historic-districts-in-flatbush.page
- LPC Permit Guidebook ch. 11 (Health & Safety): staff can issue permits for light fixtures and intercom panels meeting criteria; "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; intercom may also go on a fence or wall in front of the entranceway; max two light fixtures and one intercom panel per door opening; design, size and finish compatible with the building; attach at mortar joints, plain masonry, wood, metalwork or concrete paving, never through cast iron or on decorative surfaces; conduit concealed through plain masonry or cladding behind the installation, otherwise about ten inches of visible conduit painted to match; application = Portico filing, color photos, elevation drawings (not needed for in-kind replacement of existing intercoms), manufacturer cut sheets, paint cards; no permit for ordinary maintenance, repair and retrofitting; LPC 212-669-7817 — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Google Nest: wired Nest Doorbell needs a transformer "rated for 16-24 V AC, 10-40 VA"; transformer may be inside the chime box; Google recommends a licensed electrician to find, replace or install the transformer — https://support.google.com/googlehome/answer/12153643
- Ring: wired doorbells 16-24 VAC, 10-40 VA; multiple doorbells on one transformer need 16 VAC, 30 VA; Ring Hardwired Transformer is 16 VAC 30 VA; use 16- to 20-gauge wire; wrong power ratings can damage devices or stop the chime working — https://ring.com/support/articles/nrv6o/Troubleshooting-power-for-hardwired-doorbells
- Angi doorbell installation cost (2026 data): average $300, typical $250–$400, $150–$650 by type; wired $175–$375; wireless $150–$275; smart/camera $150–$650; intercom and multi-monitor systems up to $500 or more; new transformer $20–$35 plus $150–$250 electrician; video subscriptions $3–$10/month — https://angi.com/articles/doorbell-installation-cost.htm
- 1-800-Doorbell on wireless chime range: "each wall a signal passes through will diminish the signal by 20%"; solid concrete 30%–40%, steel 50%; brick harder to penetrate than glass; metal under the transmitter bounces signal, use a wooden shim — https://www.1800doorbell.com/door-chimes/choosing-range-of-wireless-door-chime/
- Brownstoner forum, "Video doorbell for upper levels of multi-fam brownstone?": owner of a two-apartment building with an old buzzer intercom wants to see visitors, quoted over $1,500 (later said closer to $3,000) for video; one reply wired a SimpliSafe doorbell and used plug-in chimes because the old doorbell wiring was too old; another said $1,500 for wired video sounded reasonable — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- Brownstoner forum, "Door Bell for 3-Fam Brownstone": owner's previous bell was removed by a former contractor during renovation; wants new doorbell and intercom with no door strike — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Brick Underground NYC intercom repair guide: problems usually in connections at the lobby base, apartment station, door strike or power supply, often in the basement or ceiling rather than inside walls; Daniel Vasquez (Paragon Security and Locksmith): "It's all in the wire connections."; older systems' core wiring often fine — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Bklyner (Nov 20, 2018): residents of one building near Cortelyou and Stratford Roads (ZIP 11218) reported more than 100 packages missing over six months; resident Eddie Shiomi: "There's just no accountability within the whole delivery pipeline."; a camera was installed in the mail area after residents pressed management — https://bklyner.com/a-thief-or-bad-postal-service-packages-are-missing-in-ditmas-park
- HPD Tenant Data Privacy Law (Local Law 63 of 2021): multiple dwellings using smart access (keyless) systems — key fobs, RFID cards, mobile apps, biometrics; owners must get express consent, give a data retention and privacy policy, destroy authentication data within 90 days, and may not require smart access to enter a tenant's dwelling unit — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- 6sqft (Nov 12, 2025): draft DOB/HPD rules for basement/cellar legalization under Local Law 126 — units in listed community districts, must have existed before April 20, 2024, upgrades incl. proper exits, smoke and gas alarms, sprinklers, flood sensors; apply by April 20, 2029; 10 years to comply. CD14 eligibility not stated — https://www.6sqft.com/nyc-releases-rules-for-legalizing-basement-and-cellar-apartments/
- NYC DOB electrical work guidance: "Minor Electrical Work" requires a permit but no inspection; document does not address low-voltage doorbell/intercom work — https://www.nyc.gov/assets/buildings/pdf/elect_work_guidance.pdf
- NYC Open Data live query (HPD violations, 311): EMPTY (data.cityofnewyork.us not reachable this session); earlier pack figures (67 intercom/buzzer, 290 self-closing violations on study-area lots) stand
- Bing / DuckDuckGo / Google PAA / PASF / AnswerThePublic: EMPTY
- Reddit r/BeverleySquare, r/Brooklyn buzzer threads for this area: EMPTY
- Yelp doorbell installation cost page: EMPTY (blocked)

### Questions people ask — Door Buzzer Installation in Beverley Square
- Can a battery video doorbell mount over an existing buzzer intercom, or does each apartment need its own unit? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- Is $1,500 (or $3,000) a reasonable price for a wired video doorbell system for two apartments? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- If the old doorbell wiring is too old, can plug-in chimes be used with a wired video doorbell? — Brownstoner forum — same URL
- Who can install a new doorbell and intercom in a three-family after a contractor removed the old one, without a door strike? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- How much does doorbell installation cost (wired vs wireless vs smart)? — Angi — https://angi.com/articles/doorbell-installation-cost.htm
- Does a smart doorbell need a subscription? — Angi FAQ — https://angi.com/articles/doorbell-installation-cost.htm
- How do I replace a doorbell transformer / does my transformer have enough power for a video doorbell? — Angi FAQ / Google Nest — https://support.google.com/googlehome/answer/12153643
- Can several video doorbells share one transformer? — Ring support — https://ring.com/support/articles/nrv6o/Troubleshooting-power-for-hardwired-doorbells
- Will a wireless chime reach the top floor through several walls? — 1-800-Doorbell — https://www.1800doorbell.com/door-chimes/choosing-range-of-wireless-door-chime/
- Do I need Landmarks approval to put a doorbell or intercom on a house in a historic district? — LPC guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- What does a smart access entry system have to do with tenants' data? — HPD — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- How do packages stop going missing in a building's lobby or mail area? — Bklyner — https://bklyner.com/a-thief-or-bad-postal-service-packages-are-missing-in-ditmas-park

## Bensonhurst, Brooklyn — /door-buzzer-installation-bensonhurst-brooklyn-ny (factory research, 2026-11-11)

- 8210 19th Avenue (11214), Bensonhurst: rental building listed as "53 units", "6 floors", built 1939, rent-stabilized; 24 open violations (21 Class C, 3 Class B); a former tenant's review says "The packages get stolen by outsiders who come in when you hold the door open"; another review ("Building management doesn't care") says the "door bell is not working since April" — https://www.openigloo.com/building/nyc/3164658-3063150034/brooklyn-bensonhurst-8210-19-avenue-11214
- 2430 63rd Street (11204), Bensonhurst: 23 units, 4 floors, built 1928 (building-level door/intercom violation text not shown on the free page) — https://www.openigloo.com/building/nyc/3172542-3065610019/brooklyn-bensonhurst-2430-63-street-11204
- 1673 66th Street (11204), Bensonhurst: 4 units, 2 floors, built 1931; no reviews or door/intercom records listed — https://www.openigloo.com/building/nyc/3133803-3055520056/brooklyn-bensonhurst-1673-66-street-11204
- 8418 17th Avenue (11214): listed as a "legal 4-family", built 1929, "four apartments", "two residential entrances in the front", plus "its own stairs in the front leading to a lovely basement entrance" (basement has a separate entrance; new boiler) — https://www.brownstoner.com/listing/BKMLS-6953675/8418-17th-ave-bensonhurst-brooklyn-ny-11214/
- Tower 85, 2066 85th Street between 20th and 21st Avenues: new development, 4 floors, 11 apartments, built 2022, "opened in 2025"; amenities list "Intercom" (not video, no package room listed) — https://www.cityrealty.com/nyc/bensonhurst/tower-85-2066-85th-street/187751
- Brownstoner (Cohn Brothers article): "Between 1915 and 1942, hundreds of new apartment buildings were built" in Brooklyn, most six-story Cohn buildings "built between 1926 and 1938"; "The larger the building, the larger and more ornate the lobby"; rooms "faced an interior courtyard or the street" (article does not name Bensonhurst; used only as era context for the 1928–1939 buildings above) — https://www.brownstoner.com/architecture/cohn-brothers-architects-brooklyn-apartment-buildings/
- Basement/cellar legalization (Local Law 126 of 2024) covers 15 community districts; "Brooklyn 11: Bensonhurst, Dyker Heights" is one of them; a basement must have at least one door leading outside, a ceiling at least 7 feet high, no immediate safety risk, and be outside the highest-risk flood zones — https://epicenter-nyc.com/basement-apartments-get-a-legal-path-in-nyc-but-only-in-these-15-neighborhoods/
- HPD, November 10, 2025: proposed rules for the temporary residence program "mandated by Local Law 126 of 2024"; owners must apply "before April 20, 2029" and have "over a ten-year period of time" to finish legalization; work includes sprinklers and flood water sensors; no intercom requirement mentioned — https://www.nyc.gov/site/hpd/news/074-25/adams-administration-publishes-new-proposed-rules-legalizing-basement-cellar-apartments
- Gothamist, May 8, 2024: the state plan covers 15 of the city's 59 community districts; Pratt Center and Chhaya CDC counted "more than 376,000 small properties with basements and cellars" and estimate about 500,000 New Yorkers may live in them — https://api-prod.gothamist.com/news/nys-basement-legalization-plan-inexplicably-misses-parts-of-city-that-need-it-most
- NYC Tenant Data Privacy Law (Local Law 63 of 2021): applies to "property owners of multiple dwellings that utilize smart access (keyless) systems"; owners "Must obtain express consent either in writing, or through a mobile application"; may collect only the minimum authentication and reference data (e.g. name, unit number, preferred contact method); must destroy authentication data "no later than 90 days" after collection unless anonymized; may not "require use of a smart access system to gain entry to the tenant's dwelling unit" — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Brownstoner forum, Nov 2008 ("Security and the Front Door"): Brooklyn townhouse owner wanted buzzers on both the exterior and interior front doors so delivery drivers could leave packages without walking down four flights; a commenter who had been robbed in the vestibule between two doors warned against an inner lock that is hard to open quickly; "Bklyn Fire Alarm Guy" cautioned about fire-code compliance and advised against tying a remote release to the inner door; the owner decided to "just do the first door" — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- ButterflyMX small-building guide: replacement "roughly $1,500 to $2,500" (ButterflyMX figure) vs "roughly $2,200 to $5,000 or more for a small single-entrance project" (Swiftlane figure); "There is no reliable universal price for replacing a small-building intercom"; "Do not replace a system based on age alone"; "In older or converted buildings, undocumented alterations should be treated as something to inspect"; "A reliable legacy audio intercom with one failed station may be worth repairing" — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- HPD / 311 intercom-violation counts for ZIPs 11214 and 11204: EMPTY (NYC Open Data not reachable; no building-level intercom violation text found on the free listing pages searched)
- Bensonhurst-specific local news about broken buzzers or entry doors: EMPTY (searches returned Bed-Stuy, Brownsville, Flatbush, Williamsburg and NYCHA stories only)
- Reddit threads (r/Bensonhurst, r/Brooklyn, r/AskNYC) about buzzers in Bensonhurst: EMPTY
- Yelp reviews of buzzer/intercom installers in Bensonhurst: EMPTY
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo panels: EMPTY (not accessible)

### Questions people ask — Door Buzzer Installation in Bensonhurst
- Can both the outer and inner front doors get buzzers so couriers can leave packages without me walking down? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- Is it a good idea to tie the remote release to the inner door as well? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- What stops outsiders from following residents in and taking packages? — openigloo tenant review — https://www.openigloo.com/building/nyc/3164658-3063150034/brooklyn-bensonhurst-8210-19-avenue-11214
- The doorbell to my apartment hasn't worked for months; what's wrong and who fixes it? — openigloo tenant review — https://www.openigloo.com/building/nyc/3164658-3063150034/brooklyn-bensonhurst-8210-19-avenue-11214
- Should a small building's broken intercom be repaired or replaced? — web search result — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- How much does it cost to replace a small-building intercom? — web search result — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Does legalizing a basement apartment require an intercom or buzzer? — derived from LL126 coverage of Brooklyn CD11 — https://epicenter-nyc.com/basement-apartments-get-a-legal-path-in-nyc-but-only-in-these-15-neighborhoods/
- What data can a keyless or app entry system keep about tenants? — HPD Tenant Data Privacy Law — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Can a landlord make tenants use an app to get in? — HPD Tenant Data Privacy Law — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- How do buzzers work in a house with two front entrances and a basement door? — listing context — https://www.brownstoner.com/listing/BKMLS-6953675/8418-17th-ave-bensonhurst-brooklyn-ny-11214/

## Brownsville, Brooklyn — /door-buzzer-installation-brownsville-brooklyn-ny (factory research, 2026-11-11)

- News 12 Brooklyn, November 14, 2018, headline "Broken buzzer sparks fear in tenants at Brownsville Houses": the intercom residents use to buzz visitors into the building was broken (article body, quotes and duration not retrievable; only headline and summary read) — https://brooklyn.news12.com/broken-buzzer-sparks-fear-in-tenants-at-brownsville-houses-39484545
- NYC Comptroller report FK23-069S (September 21, 2022), "Observations of Building Doors in NYCHA Developments": auditors visited 262 NYCHA developments between August 30 and September 8, 2022; 36.8% of residential building entrance doors were open and 40.1% of entrance door locks were broken; rear/side doors 37.5% open, 28.5% locks broken; share of entrance doors open and/or with broken locks rose from 23.5% in 2018 to 57.9% in 2022; residents and employees said intercoms, locks, keys and door release buttons often do not work, which contributes to doors being propped open; one resident said "the building's intercoms have been broken for 10 years"; some repaired doors and intercoms broke again soon after. Quote: "Exterior doors that are not securely locked enable intruders and unauthorized persons to gain access to buildings". No Brownsville development named. — https://comptroller.nyc.gov/reports/observations-of-building-doors-in-nycha-developments
- NYCHA Journal, November 28, 2023: NYCHA completed over $24.1 million in safety and security upgrades at 23 campuses (CCTV, layered access control "which allows remote changes to access permissions without replacing key fobs or locks", entrance upgrades incl. exterior lighting, intercom systems and stainless-steel or steel-reinforced aluminum doors); separate Entryways pilot: construction had started at Seth Low Houses (a Brownsville development). Brooklyn campuses listed: Farragut, Hughes, Kingsborough, Pink. — https://nychajournal.nyc/nycha-completes-over-24-million-in-safety-and-security-upgrades-at-23-campuses/
- NYCHA press release, October 15, 2026: ribbon cutting for the completed $636 million PACT renovation of Reid & Park Rock — 1,696 apartments, 87 buildings, 15 East Brooklyn developments (including Ocean Hill-Brownsville, Tapscott Street Rehab, 104-14 Tapscott Street, Sutter Avenue-Union Street, Ralph Avenue Rehab, Lenox Road-Rockaway Parkway, Howard Avenue), nearly 3,000 residents; work included "enhanced security infrastructure and access control", upgraded lobbies and common areas, lighting, elevators, accessibility. Ocean Hill-Brownsville Tenant Association President Shamica Moore spoke at the event. — https://www.nyc.gov/site/nycha/about/press/pr-2026/pr-20261015.page
- NYCHA PACT page for Howard Houses: resident engagement November 2024 to November 2025; Introduction to PACT meeting November 14, 2024; Visioning Workshop March 20, 2025; Existing Conditions Meeting November 5, 2025; Marvel Architects working with NYCHA; no partner named on the page — https://www.nyc.gov/site/nycha/about/pact/howard.page
- City Council Committee on Public Housing, April 15, 2025: asked what share of NYCHA front doors are secured, NYCHA's Lauren Gray said "I don't have that information available"; residents report broken doors by calling the CCC to open a work order; property management staff check doors daily during building cleanup — https://citymeetings.nyc/meetings/new-york-city-council/2025-04-15-1000-am-committee-on-public-housing/chapter/security-of-front-doors-at-nycha-buildings/
- City Limits, October 7, 2025: HPD began publishing NYCHA housing code violations (first time public) under a settlement approved in June 2025 in a NYLAG lawsuit; HPD inspectors generally enter NYCHA apartments only on housing-court order; NYCHA estimates about $78 billion of repair needs across roughly 2,500 buildings and had more than 614,000 open work orders as of August 2025 — https://citylimits.org/city-issued-violations-at-nycha-developments-are-now-public-following-legal-settlement/
- City Limits, October 16, 2024 (Mayor's Management Report data): citywide housing violations 895,457 in FY2024 vs 722,597 in FY2023 (24% rise); self-closing door violations 73,325 in FY2024, up from 49,897 — https://citylimits.org/2024/10/16/housing-violations-in-nyc-jumped-24-this-year-we-mapped-them-by-neighborhood/
- Urban Omnibus, "The Bible and the Billionaire": Nehemiah groundbreaking on a vacant Brownsville lot on Halloween 1982 with about 6,000 people and Mayor Koch; first residents June 1984 by lottery; first phase 20 blocks, 700 houses; about 1,000 more red brick houses later across Brownsville and East New York; each a two-story brick house 18 feet wide and 32 feet deep with a backyard and a front concrete parking pad; kitchens at the front so residents could watch the street; many have red or green aluminum awnings over the front doors; architect James T. Martino; sold for $40,000–$45,000; mandatory homeowners' association. Developer I.D. Robbins: "High-rises are fine on Park Ave., but not for poor people." — https://urbanomnibus.net/the-bible-and-the-billionaire
- New York YIMBY, March 2025: 326 Rockaway Avenue, 14-story mixed-use building with 215 residences (85 affordable), developers Slate Property Group and RiseBoro Community Partnership, architect Aufgang Architects; lottery applications due May 5, 2025 (no intercom or entry detail in article) — https://newyorkyimby.com/2025/03/housing-lottery-launches-for-326-rockaway-avenue-in-brownsville-brooklyn.html
- Brownstoner, April 16, 2026: Gail P. Duke Senior Residence, 350 Livonia Avenue, 13 stories, 142 senior apartments, 24-hour building super, elevator; certificate of occupancy April 2026; $143.4 million; Catholic Charities Progress of Peoples Development Corporation with Radson Development and Community Solutions; architect Magnusson Architecture and Planning — https://www.brownstoner.com/real-estate-market/affordable-housing-lottery-350-livonia-avenue-brownsville/
- Brownstoner, March 3, 2026: Glenmore Manor, 76 Christopher Avenue, 11 stories along Glenmore Avenue between Mother Gaston Boulevard and Christopher Avenue, 233 apartments (83 for formerly homeless residents and low-income seniors), 20,000 sq ft two-story B'Ville Hub commercial space; Brisa Builders, Lemle & Wolff, African American Planning Commission; Think! Architecture and Design — https://www.brownstoner.com/real-estate-market/affordable-housing-lottery-brownsville-glenmore-manor-76-christopher-avenue
- Openigloo building records: 361 Livonia Avenue (111 units, 14 floors, built 1948) and 429 Dumont Avenue (112 units, 14 floors, built 1958) — large mid-century towers; 898 Thomas S. Boyland Street a 2-unit, 2-floor building built 2005. Reviews read did not mention intercoms or doors. — https://www.openigloo.com/building/nyc/3328130-3037940001/brooklyn-brownsville-361-livonia-avenue-11212 ; https://openigloo.com/building/nyc/3328046-3037770001/brooklyn-brownsville-429-dumont-avenue-11212 ; https://www.openigloo.com/building/nyc/3393329-3036110145/brooklyn-brownsville-898-thomas-s-boyland-street-11212
- Mixed-use Pitkin Avenue stock: 1770 Pitkin Avenue listing — built 2002, three ground-floor commercial spaces and two three-bedroom apartments above — https://raveis.com/property/flyer/17466138
- Habitat Magazine, February 2024, "A Working Intercom Isn't an Amenity. It's Required by Law": MDL requires a two-way voice intercom from the front door to each apartment in buildings built or converted after 1968 with eight or more units; the housing maintenance code also requires a functioning intercom; courts have treated intercoms as an essential service (warranty of habitability); remedies include a 311 complaint and an HP proceeding in housing court. Attorney Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom." — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground (2014), broken buzzers: steps for tenants — notify the landlord in writing, enlist neighbors, call 311, get a repair estimate, rent-stabilized tenants can file a reduction-of-services complaint with HCR, last resort HP action; tenant lawyer Sam Himmelstein says written requests are useful documentation if the case reaches court — https://www.brickunderground.com/blog/2014/12/broken_buzzers
- Reddit threads specific to Brownsville buzzers/intercoms: EMPTY (search returned no Brownsville buzzer threads)
- HPD/311 open-data counts of intercom violations in ZIP 11212: EMPTY (NYC Open Data not reachable for this research run)
- Yelp 1–3★ for intercom/buzzer installers near Brownsville: EMPTY
- Local news on Pitkin/Belmont business entry doors: EMPTY

### Questions people ask — Door Buzzer Installation in Brownsville
- What should tenants do when the building buzzer is broken and the landlord will not fix it? — Bing/web results (Brick Underground "Get your landlord to fix that broken buzzer") — https://www.brickunderground.com/blog/2014/12/broken_buzzers
- Is a working intercom legally required, or just an amenity? — web results (Habitat) — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Who is responsible for intercom repair in NYC and when should it be replaced? — web results (ButterflyMX "Intercom Repair in NYC: Costs, Legal Duties, and When to Replace") — https://butterflymx.com/blog/intercom-repair-nyc
- How do apartment buzzer systems work, what types are there and what do they cost? — web results (ButterflyMX) — https://butterflymx.com/blog/apartment-buzzer/
- How does a video doorbell reach the upper floors of a multi-family house? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- How should the front door of a small building be secured (lock, strike, closer)? — Brownstoner forum "Security and the Front Door" — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- How does an electric door strike work with a buzzer? — Brownstoner forum "Electric Door Strike" — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- What are tenants' rights when building key fobs stop working in New York? — web results — https://tenant-rights.com/new-york/tenant-rights-when-building-fobs-stop-working-in-ny
- What does a commercial door buzzer system for a business involve? — web results (ButterflyMX) — https://butterflymx.com/blog/commercial-door-buzzer-system
- How do NYCHA residents report a broken entrance door or intercom? — web results (City Council hearing, MyNYCHA) — https://citymeetings.nyc/meetings/new-york-city-council/2025-04-15-1000-am-committee-on-public-housing/chapter/security-of-front-doors-at-nycha-buildings/
- Google PAA / PASF / AnswerThePublic / DuckDuckGo for "door buzzer installation Brownsville": EMPTY
- Reddit questions for Brownsville: EMPTY
- Yelp: EMPTY

## Brooklyn Navy Yard, Brooklyn — /door-buzzer-installation-brooklyn-navy-yard-brooklyn-ny (factory research, 2026-11-11)

- The Navy Yard is a commercial/industrial campus with no apartment buildings inside it; door buzzer work here is at tenant suite doors, studio doors, shop doors, staff doors and receiving doors, not apartment lobbies. Multiple Dwelling Law §50-a (intercom requirement) applies to Class A multiple dwellings, so it does not reach Yard tenant spaces — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf ; https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a/
- BNYDC Tenant Manual (2026): "Tenants and licensees are responsible for installing their own door locks upon taking possession of their leased space"; BNYDC does not keep or copy keys to tenant spaces — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- Tenant Manual: visitors registered through Eptura Visitor (Proxyclick) are emailed a QR code; the manual does not say how a visitor reaches a specific suite once through the gate — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- Tenant Manual: "Deliveries by all other couriers such as FedEx, UPS and Amazon are managed directly by the tenant or licensee"; packages must go to the tenant's space or mailbox and "are not allowed to be left in hallways or other shared public spaces"; campus mailroom in Building 6 near Clinton Gate, 8 a.m.–5 p.m. weekdays — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- Tenant Manual: "Any and all electrical work must be performed by a licensed electrician" and needs BNYDC approval before it begins; plans for alterations "must be submitted to and approved by BNYDC"; telecom: coordinate with the Property Manager on scope and access to the building's telecom closets; signage requests go to BNYDC for approval; no storage in common hallways — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- Tenant Manual: Building 77 "24/7 Access (Swipe card required for lobby entry between 10 PM and 6 AM)"; Building 3 24/7 pedestrian access; freight elevators shut 8 p.m.–5 a.m. weekdays and all weekend; after-hours freight $50/hr per car 8–11 p.m., four-hour minimum ($200) late nights and weekends; loading docks kept clear except while loading; "Ensure freight elevator doors are closed after use" — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- Tenant Manual: Fire Safety & Security role = "Local Fire Alarm contact for FDNY response/emergency contact"; after-hours emergencies go to BNYDC Security — https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf
- eWeek (July 6, 2020): Proxyclick cloud visitor management integrated with the Yard's S2 access control, which notifies hosts when visitors arrive; tenants pre-register visitors who scan a QR code at entrances; watchlists apply across all seven gates; tenants can run their own iPad visitor experience; delivery drivers often lack names, so pre-approving truck plates was being tested; quote from Marc Cecere, Director of Applications, BNYDC: "Proxyclick has been super helpful; I'm not sure what we would have done otherwise if we didn't have a system that was convenient and easy to use." — https://www.eweek.com/innovation/it-science-case-study-how-brooklyn-navy-yard-now-welcomes-visitors
- LenelS2 case study: BNYDC uses a LenelS2 NetBox access control system at Yard entrances; shuttle buses carry HID iClass readers that read cards and mobile credentials; quote from Pasquale Cirullo, VP of Technology, BNYDC: "The new system makes it is easy for us to ensure that the people who should be on the Yard, are on the Yard." — https://www.lenels2.com/en/media/LenelS2-Case-Study-BNYDC_tcm841-144396.pdf
- BNYDC Wayfinding FAQs: project started May 2026, about 6 months; buildings renumbered 0–400 from Kent Avenue (east) to Navy Street (west); Buildings 72, 77, 92, 212 and 303 keep their numbers; "All doors and loading docks are now numbered sequentially, and ADA entrances have been identified"; red interim "Former Building" signs for 6 months to a year; main road to be renamed Navy Yard Drive with cross streets "1st Row" to "13th Row"; tenants with in-house drivers or non-major carriers should give drivers the new address and the correct door or dock number; tenants keep prior addresses (63 Flushing, 141 Flushing, 399 Sands) with new building numbers until a new address is announced — https://www.brooklynnavyyard.org/wayfinding-faqs/
- Building 77 flyer (2023): 16 floors, floors 3–15 of 60,000–67,500 sf; slab-to-slab 10'–11' typical; four freight elevators (9' x 9' x 17', 16,000 lb) and eight passenger elevators; "Lobby desk, 24 / 7 security and keycard access"; fully sprinklered; example Suite 507 of 2,942 sf; "Perfect for light industrial, tech, R&D, and maker space" — https://www.brooklynnavyyard.org/wp-content/uploads/2023/07/BNY-BLDG-77_2023-Flyer-Final-507-Flyer.pdf
- Building 12 flyer: 55,000 sf manufacturing building, 20 ft ceilings, six drive-in gates, three gantry cranes, built-out mezzanine offices; 24/7 Navy Yard security — https://images.loopnet.fr/d2/DSN1AASCfIROENt8tf-0a46FOq929zMCKJ8nFmhAcCE/BLDG%2012%20Flyer.pdf
- Brownstoner (Sept 24, 2025): BNYDC and NYCEDC sought designers for Building 303's ninth floor, the last unfinished floor, planned as eight "subdivided suites", an R&D lab or clean room and shared amenities for life sciences, green economy, medtech and advanced manufacturing; Yard has 500+ businesses, 13,000+ people — https://www.brownstoner.com/interiors-renovation/brooklyn-navy-yard-building-303-rfp-2025
- Commercial Observer (June 15, 2021): Building 303 has four floors of parking and four of manufacturing; Building 77 penthouse/top floors marketed to creative office tenants; quote from Brad Gerla, CBRE: "People really make the Navy Yard their work home" — https://commercialobserver.com/2021/06/the-brooklyn-navy-yard-wants-to-appeal-to-creative-office-tenants
- Bisnow: Pratt Institute graduate program relocating to 63K sf at Dock 72 (Rudin/BXP office building) — https://www.bisnow.com/news/new-york/office/pratt-institute-moving-to-63k-sf-at-bxp-and-rudins-dock-72-122618
- NYC Building Code 1010.1.9.8 sensor release of electrically locked egress doors applies to Group A, B, E, M, R-1, R-2 occupancies and their tenant entrance doors: egress-side sensor, loss of power unlocks, manual "PUSH TO EXIT" device 40–48 in. above floor within 5 ft, cuts power directly and keeps door unlocked at least 30 seconds, fire alarm/sprinkler activation unlocks until reset, UL 294; 1010.1.9.9 electromagnetically locked egress doors (hardware with built-in switch) permitted in the same groups; Group F (factory) is not in either list — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173521
- NYC Building Code 1010.1.9.7 delayed egress needs special review and approval by the commissioner and is not permitted in Group A, E, F or H occupancies — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173521
- Aiphone warehouse showcase: knocking at locked warehouse doors went unheard in a loud space and "Drivers who did not have credentials would be forced to knock for several minutes"; fix: video intercoms at each entrance, "A bell and strobe were installed and activated by calls from the door stations", calls answered by any interior master station — https://www.aiphone.com/blogs/solution-showcase-adding-security-and-communication-to-a-bustling-warehouse/
- ButterflyMX: "A door buzzer system costs anywhere from $1,000 to $7,000 for the hardware" (excludes installation); "doorbells notify, while buzzers notify and grant access"; claims wired buzzer installs can take "several days if not many weeks" — https://butterflymx.com/blog/commercial-door-buzzer-system
- ButterflyMX small office: key fob systems "often priced around $1,000 to $3,000 per door installed"; small commercial video intercoms "about $2,500 to $7,000 installed"; final prices shift with door count, wiring, locking hardware, software fees and landlord rules — https://butterflymx.com/blog/cost-to-install-intercom-vs-key-fob-for-small-office/
- GoKeyless: a buzz-in setup on a cylindrical-lock door means swapping the jamb strike for an electric strike and adding a power supply and a release switch (receptionist button, concealed desk switch or intercom) — https://gokeyless.com/blogs/news/buzz-locks-buzzer-locks
- BiggerPockets: owner removing an unreliable buzzer was warned that without guest entry "the entrance doors would just get propped open using rocks, sticks, anything the residents could find" — https://biggerpockets.com/forums/52/topics/1194930-removing-access-control-system-intercom-door-buzzer-from-multi-unit-building
- HPD violations / 311 buzzer complaints for the Navy Yard: EMPTY (no residential buildings inside the Yard; not applicable).
- DOB permits specific to Navy Yard entry systems: EMPTY.
- LPC: the Yard is a National Register historic district (2014) and Dry Dock 1 is an NYC landmark; no LPC rule on tenant door stations found — EMPTY.
- Local news about door buzzers/intercoms in the Navy Yard: EMPTY.
- Reddit threads about buzzers/intercoms at the Navy Yard: EMPTY.
- Yelp reviews of buzzer installers near the Navy Yard: EMPTY (not accessible).
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo for "door buzzer installation Brooklyn Navy Yard": EMPTY (not accessible).

### Questions people ask — Door Buzzer Installation in Brooklyn Navy Yard
- How much does it cost to install a door buzzer system? — vendor FAQ (ButterflyMX) — https://butterflymx.com/blog/commercial-door-buzzer-system
- How do you buzz open a door? — vendor FAQ (ButterflyMX) — https://butterflymx.com/blog/commercial-door-buzzer-system
- How much does an intercom system cost for a small office? — vendor FAQ (ButterflyMX) — https://butterflymx.com/blog/cost-to-install-intercom-vs-key-fob-for-small-office/
- Which is more secure: intercom or key fob? — vendor FAQ (ButterflyMX) — https://butterflymx.com/blog/cost-to-install-intercom-vs-key-fob-for-small-office/
- Can intercom and key fob access work together? — vendor FAQ (ButterflyMX) — https://butterflymx.com/blog/cost-to-install-intercom-vs-key-fob-for-small-office/
- What should I tell my delivery drivers? — BNYDC Wayfinding FAQ — https://www.brooklynnavyyard.org/wayfinding-faqs/
- What is my new building number and address, and when can I use it? — BNYDC Wayfinding FAQ — https://www.brooklynnavyyard.org/wayfinding-faqs/
- Is it a problem to leave units without buzzer access and have guests call instead? — BiggerPockets forum — https://biggerpockets.com/forums/52/topics/1194930-removing-access-control-system-intercom-door-buzzer-from-multi-unit-building
- Affordable option to replace a small building entry system — Reddit r/accesscontrol (silo research S12) — https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/
- PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Yelp questions specific to the Navy Yard: EMPTY

## Cadman Plaza, Brooklyn — /door-buzzer-installation-cadman-plaza-brooklyn-ny (factory research, 2026-11-11)

- Whitman Close (75 Henry St): "there are only around 16" two-story townhouses; "The townhouses are an odd mix of public and private space, with the entrances and backyards right on public walkways always crowded with commuters and tourists"; houses facing Cadman Plaza West especially busy; adjacent 33-story tower (Brownstoner Building of the Day, July 18 2012) — https://www.brownstoner.com/architecture/building-of-the-day-draft-5
- One Clinton, 280 Cadman Plaza West: "The soaring, 38-story wedge", 133 units, year built 2020, "FT Doorman", "Concierge", "Amenities include a 24-hour attended lobby"; no intercom/package details on page — https://www.cityrealty.com/nyc/brooklyn-heights/one-clinton-280-cadman-plaza-west/68115
- Cadman Plaza N., Inc. v Botkin (Sup Ct Kings County, decided May 20 2025): the 140 Cadman Plaza West co-op is staffed by doormen including a relief doorman reached on a building phone; a resident walked down fifteen floors (personal details not used) — http://www.nycourts.gov/reporter/pdfs/2025/2025_31869.pdf (carried from the Cadman Plaza door buzzer repair research)
- NYC 311 Open Data, descriptor BELL/BUZZER/INTERCOM, ZIP 11201, Jan 1–Nov 2 2026: 22 complaints across the ZIP; none at 140 Cadman Plaza West, 75 Henry St, 101 Clark St, 10 Clinton St or 280 Cadman Plaza West — https://data.cityofnewyork.us/resource/erm2-nwe9.json (carried from the repair research pull of Nov 11 2026)
- HPD violations Open Data, full-text INTERCOM, ZIP 11201: roughly 110 intercom violation records back to 1984, none at the Cadman Plaza complex addresses or One Clinton — https://data.cityofnewyork.us/resource/wvxf-dwi5.json (carried from the repair research pull)
- Habitat Magazine, July 11 2018 "Intercom Job": six-story pre-war UWS co-op rejected a smartphone system ($3.50 per unit per month, needed internet, many residents without smartphones) and installed an Aiphone GT-1C7 video system for $20,000 reusing the existing wiring, paid from reserves; quote: "Most of the board felt more comfortable staying with a closed-circuit, hardwired system versus a cloud solution." — John Viesta, board secretary — https://habitatmag.com/Publication-Content/Bricks-Bucks/Intercom-Job
- Security Sales, June 15 2016: Park Vanderbilt, Park Slope, seven-story 148-unit co-op built 1963, Aiphone video intercoms at the two lobby entries and the service entrance, concierge station on the superintendent's desk, $110,000, three weeks, about $20,000 saved by reusing existing cable; quote: "By using the existing cable – with the exception of two units – we were able to save $20,000 on the job." — Dan Arnold, Academy Mail Box — https://www.securitysales.com/access/brooklyn_housing_co_op_upgrades_security_with_video_intercom_system/
- Habitat Magazine, Dec 2015 "The Doorman Who Wasn't There": virtual doorman services; 114-unit 1961 Ditmas Park co-op replaced a failing intercom with a phone-based DoorKing system; ButterflyMX then $2,500–$5,500 install plus $2.50 per apartment per month (postscript: prices outdated); service stops if building internet goes down; every release logged; shareholder quote: "I love that I can let UPS in the building when I'm not there." — Jessica Dowshen — https://habitatmag.com/Archive2/328-December-2015/The-Doorman-Who-Wasn-t-There
- Habitat Magazine, Dec 2020 "Making an Entrance": the Wellston (UWS, 15 stories, 130 units) automated two heavy entrance doors with push buttons inside and out and doorman remotes, about $114,000; quote: "People don't have to struggle anymore, especially when they've got packages." — Josh Wiener, board president — https://habitatmag.com/Archive2/383-December-2020/Making-an-Entrance
- Brick Underground, Nov 7 2019 NYC intercom guide: "while they may be outdated, the core wiring is typically fine" (Daniel Vasquez, Paragon Security and Locksmith); "Now everyone wants more security. They want a camera to see in front of the door before allowing someone in." (Vasquez); "a 100-unit building could be done in about two days" (Pete Carmello, Lock and Tech) — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- LPC Permit Guidebook ch. 11: intercom panels and doorbells "must be installed within or adjacent to a door opening"; intercom may go on a fence or wall in front of the entranceway; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; not attached through cast iron or decorative surfaces; conduit concealed, or about ten inches visible painted to match; small residential buildings no more than two cameras per 25 feet of frontage, large buildings three; filings through Portico with photos, cut sheets — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Brooklyn Heights Historic District: designated a NYC Landmark November 1965, "bounded by Cadman Plaza West (Old Fulton Street) on the north" — https://www.wikiwand.com/en/articles/Brooklyn_Heights_Historic_District ; Cadman Towers complex excluded from the 1965 district — https://www.nycurbanism.com/brutalnyc/2017/2/1/cadman-towers
- HPD Tenant Data Privacy Law (Local Law 63 of 2021): covers multiple dwellings using smart access (keyless) systems incl. key fobs, apps, biometrics; express consent in writing or via app; data retention and privacy policy; authentication data destroyed no later than 90 days unless anonymized; owners cannot "require use of a smart access system to gain entry to the tenant's dwelling unit" — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- HPD self-closing doors: apartment and hallway doors "required by law to swing closed and latch by themselves"; defects = class C immediately hazardous, correct within 14 days; HPD reinspects within 20 days; Local Law 71 of 2022 requires 300 proactive inspections a year — https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page
- ButterflyMX apartment buzzer guide: "The relay is the electrical control point; it doesn't physically swing the door open."; "The communication path and release circuit are connected, but they aren't the same circuit."; "Older analog systems often use dedicated conductors between the entrance and each unit."; "A fail-safe lock unlocks when power is removed." — https://butterflymx.com/blog/apartment-buzzer/
- Reddit r/nyc: resident of "a roughly 20 unit building in Brooklyn Heights" says "The front door to the building hydraulically locks when pushed open", thread on the door being propped open late at night — https://www.reddit.com/r/nyc/comments/dj0k3b/apartment_building_door_propped_open_late_at_night/
- Habitat Magazine Feb 26 2024: "As a result, the co-op has a legal obligation to repair or replace the intercom," — Nancy Kourland, Lasser Law Group — https://www.habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Silo sources reused: MDL §50-a, Aiphone GT (5,000 tenant stations, existing wire), HomeAdvisor ($2,500 avg, $1,500–$15,000), Swiftlane ($1,000–$5,000+ per door, $5–$15 per unit per month), IBC sensor release, Allegion fail-safe/fail-secure, 2010 ADA 48-inch reach — see silo-wide research
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo for "door buzzer installation Cadman Plaza": EMPTY
- Yelp complaints about buzzer installers near Cadman Plaza: EMPTY
- Local news on buzzer/intercom installation inside the Cadman Plaza complex: EMPTY (searches returned generic package-theft stories elsewhere in Brooklyn)

### Questions people ask — Door Buzzer Installation in Cadman Plaza
- What is an apartment buzzer system? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- How can a property reduce buzzer bombing? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Should a co-op choose a hardwired system or a cloud/smartphone system? — Habitat — https://habitatmag.com/Publication-Content/Bricks-Bucks/Intercom-Job
- Can existing cable be reused to save money on a video intercom in a large co-op? — Security Sales — https://www.securitysales.com/access/brooklyn_housing_co_op_upgrades_security_with_video_intercom_system/
- Can a concierge or super's desk station be part of the entry system? — Security Sales — same URL
- What happens to a phone/app entry system when the building internet goes down? — Habitat — https://habitatmag.com/Archive2/328-December-2015/The-Doorman-Who-Wasn-t-There
- Can I let a courier into the building when I'm not there? — Habitat — same URL
- Can heavy entrance doors be automated with push buttons? — Habitat — https://habitatmag.com/Archive2/383-December-2020/Making-an-Entrance
- How long does it take to replace an intercom in a 100-unit building? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Does the old wiring have to be replaced? — Brick Underground — same URL
- What is allowed for an intercom panel on a landmarked building? — LPC Permit Guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Does a co-op have a legal obligation to repair or replace the intercom? — Habitat — https://www.habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- The building door is propped open late at night. What can be done? — Reddit — https://www.reddit.com/r/nyc/comments/dj0k3b/apartment_building_door_propped_open_late_at_night/
- PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Yelp questions: EMPTY

## Canarsie, Brooklyn — /door-buzzer-installation-canarsie-brooklyn-ny (factory research, 2026-11-11)

- NYC Comptroller field review (Sept 21, 2022) of 262 NYCHA developments: 40.1% of entrance door locks broken (rear/side doors 28.5%); 36.8% of residential entrance doors found open; 57.9% of entrance doors propped open, broken-locked or both (23.5% in 2018). Brooklyn: 46.1% open, 39.7% broken locks, 66.0% unsecured in 2022 vs 17.0% in 2018. Residents said intercoms, locks, keys and door release buttons often failed, which led to doors being propped; one resident said a building's intercoms had been broken for 10 years. Comptroller Brad Lander: "Broken doors are a symbolic reminder that home safety starts at the entrance." Canarsie developments (Breukelen, Bay View) not named individually. — https://comptroller.nyc.gov/newsroom/comptrollers-auditors-find-40-1-of-nycha-entrance-doors-have-broken-locks-as-part-of-new-resident-powered-audit-initiative
- NYCHA "Bay View Resident Priorities – March 2023" (Bay View Houses, Canarsie): "Repair and replace all entrance and exit doors"; "Assign individual key fobs to residents"; "Key fobs issued to residents should not have the capacity or ability to be duplicated"; "All apartment entry doors must be made of durable material, and each must have a numeric identifier." Document does not mention intercoms. — https://www1.nyc.gov/assets/nycha/downloads/pdf/exhibite-residentprioritiesbv.pdf
- Breukelen Houses (Canarsie) News12 story April 9, 2019: seniors demanding issues in their units be addressed; body not retrievable, no door/intercom details — EMPTY for buzzer specifics. — https://brooklyn.news12.com/breukelen-houses-tenants-decry-deteriorating-conditions-lack-of-action-40280356
- 1625 Rockaway Parkway, Canarsie: 6-story postwar co-op built 1963, elevator, live-in super, no doorman (CityRealty). Example of Canarsie's mid-rise co-op stock where the lobby panel is the only gatekeeper. — https://www.cityrealty.com/nyc/canarsie/1625-rockaway-parkway/96021
- 704 East 103rd Street, Canarsie: 4 units, 3 floors, built 1996 (openigloo) — example of the small post-1968 multi-unit stock; itemized violations not shown. — https://www.openigloo.com/building/nyc/3341261-3081900069/brooklyn-east-new-york-704-east-103-street-11236
- HPD Housing Maintenance Code violations 2012–2023 mapped by ZIP (Datawrapper chart by Jaclyn Jeffrey-Wilensky): "Canarsie and East New York had the largest share of illegal basement violations across the city." — https://datawrapper.dwcdn.net/iKlsr/2
- Pratt Center study reported Oct 27, 2021: about 30,000 basement units unaccounted for citywide; East New York 5,086, the most of any area; 13 killed in Ida flooding, at least 10 in illegal units. (No Canarsie figure.) — https://www.audacy.com/1010wins/news/local/nyc-has-30k-unaccounted-for-basement-units-east-new-york-has-most-study
- Multiple Dwelling Law intercom rule as summarized by Landlord v. Tenant: buildings built or converted after Jan 1, 1968 must have some intercom system "even if it is only a bell and buzzer"; pre-1968 buildings may have to install one if a majority of tenants request or consent; DHCR opinion letter May 21, 1996 (LVT No. 11329); installing a bell-and-buzzer system may qualify for an MCI rent increase. — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- DHCR ruling March 14, 2003 (Koumbiadis, LVT No. 16543): for a three-apartment building, "there was no legal requirement to provide a buzzer system in a building containing fewer than eight apartments." — https://www.landlordvtenant.com/article/landlord-neednt-install-operating-buzzer-system
- Habitat Magazine, Feb 2024, "A Working Intercom Isn't an Amenity. It's Required by Law": post-1968 buildings with eight or more units must have a two-way voice intercom from the front door to each apartment; city housing maintenance code also requires a functioning intercom; courts have treated intercoms as an essential service (warranty of habitability); options include 311 complaint and an HP proceeding in housing court. Quote, Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom." — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground, Nov 7, 2019 (Mimi O'Connor): most failures are at connections — lobby base, apartment station, door strike or power supply; Daniel Vasquez (Paragon Security and Locksmith): "It's all in the wire connections"; Pete Carmello (Lock and Tech): "A lot of times it's user error"; a five-apartment building replacement could be finished in about a day, a 100-unit building about two days; repairs require authorization from the building. — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Brownstoner forum (about 12 years old): owner of a three-family wanted "Nothing fancy" — a buzzer and intercom in each unit; reply recommended calling a manufacturer (Aiphone) to design the system. — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- BiggerPockets: investor renovating a 3-family asked about "running a doorbell or intercom system" during the renovation; no replies. — https://www.biggerpockets.com/forums/52/topics/734291-intercom-or-doorbell-system-for-3-family-home
- Canarsie-specific Reddit threads about buzzers/intercoms: EMPTY (searches returned only BiggerPockets/Brownstoner/ButterflyMX results).
- Canarsie Courier buzzer/intercom stories: EMPTY.
- Yelp 1–3★ reviews of intercom installers in Canarsie: EMPTY (no Yelp pages returned; only MapQuest/Angi/Thumbtack listings).
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo panels: EMPTY (only organic results available through the search tool).
- HPD intercom violation counts for ZIP 11236 via NYC Open Data: EMPTY (dataset not reachable).

### Questions people ask — Door Buzzer Installation in Canarsie
- Is a landlord required to provide a working buzzer or intercom in a small house with only two or three apartments? — Landlord v. Tenant / DHCR ruling — https://www.landlordvtenant.com/article/landlord-neednt-install-operating-buzzer-system
- Does a plain bell and buzzer count as the required intercom, or must tenants be able to talk? — Landlord v. Tenant — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- Can a landlord raise the rent after installing a buzzer system (MCI)? — Landlord v. Tenant — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- What can a co-op shareholder do if the board does not fix the intercom? — Habitat Magazine — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Why does an intercom stop working — the buttons, the wiring, the strike or the power supply? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- How long does it take to replace a building's intercom? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Who has to authorize intercom repairs — can a tenant call a technician directly? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- What is the simplest buzzer and intercom setup for a three-family house, with no door opener? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- When should a doorbell or intercom be run during a renovation of a three-family? — BiggerPockets — https://www.biggerpockets.com/forums/52/topics/734291-intercom-or-doorbell-system-for-3-family-home
- Why do NYCHA entrance doors stay propped open, and does a broken door release cause it? — NYC Comptroller — https://comptroller.nyc.gov/newsroom/comptrollers-auditors-find-40-1-of-nycha-entrance-doors-have-broken-locks-as-part-of-new-resident-powered-audit-initiative
- Can key fobs be issued per resident and made so they cannot be copied? — NYCHA Bay View resident priorities — https://www1.nyc.gov/assets/nycha/downloads/pdf/exhibite-residentprioritiesbv.pdf

## Bushwick, Brooklyn — /door-buzzer-installation-bushwick-brooklyn-ny (factory research, 2026-11-11)

- NYC Department of City Planning, Bushwick Neighborhood Plan, housing chapter (early 2019; cites data through Feb 2019): about 90% of Bushwick households are renters and 10% owners; only 26% of households live in rent-stabilized apartments; over half of apartments are in buildings with fewer than six units; nearly 80% of buildings were built before 1947; roughly one in six homes has three or more maintenance deficiencies; 2015–2018 HPD did more than 37,000 inspections and issued over 50,000 violations; HPD spent over $3.6 million on emergency repairs; rents rose 60% 2000–2016 (Brooklyn 38%, citywide 32%); NYCHA to convert 1,315 Hope Gardens apartments to Section 8; Linden Court (NYCHA Bushwick II) 154 senior apartments, 13 stories; 1531 Broadway ~125 affordable/supportive units rezoned to 16 stories; Certification of No Harassment pilot (Sept 2018) for covered buildings before construction or demolition — https://www.nyc.gov/assets/planning/download/pdf/plans-studies/bushwick-neighborhood-plan/plan/04-bushwick-housing.pdf
- City Limits, July 24, 2019: Hope Gardens portfolio (Hope Gardens, Bushwick II, Palmetto Gardens) PACT/RAD conversion, about 1,315 apartments in 60–61 buildings, ~2,800 residents, $391 million, Pennrose LLC; planned work includes lobby, elevator camera, door entry and exit alarm, key entrance upgrades and broader lighting, camera and intercom overhauls, plus exterior entrances — https://citylimits.org/2019/07/24/bushwick-nycha-hope-gardens-repairs-pact-rad/
- New York YIMBY: 123 Melrose Street on the former Rheingold Brewery site (block bounded by Melrose St, Stanwix St, Noll St, Evergreen Ave), Read Property Group, Perkins Eastman; eight stories, 385 residential units, about 64 units per middle floor, 71 parking spaces, 169 bike storage; one of 10 planned buildings, nearly 1,000 apartments, 30% below market — https://www.newyorkyimby.com/?p=14174
- 1010 WINS (Audacy), April 25, 2022: at about 6:25 a.m. on Friday, April 24 a burglar entered 10 Goodwin Place in Bushwick "through forced entry by manipulating the front door with tools" and pried open multiple mailboxes — https://www.audacy.com/1010wins/news/local/burglar-breaks-into-mailboxes-in-bushwick-apartment-building
- Patch, Oct 21, 2019: on Sept 10 at 1:50 p.m. a man opened a gate next to the stoop of 11A Eldert St., Bushwick, and took three of about five packages left on the ground (about $2,200 in clothing) — https://patch.com/new-york/bushwick/package-swiping-bushwick-thief-stole-2k-clothes-cops-say
- News 12, Dec 14, 2022: "'There is no protection.' Bushwick tenant says building's doors won't latch, fears for safety" (headline only; body not retrievable; no address) — https://westchester.news12.com/there-is-no-protection-bushwick-tenant-says-buildings-doors-wont-latch-fears
- News 12, Oct 11, 2024: Starr Street building in Bushwick, tenants' union; 21 new violations since first report, 42 open; no entry-system issue mentioned — https://brooklyn.news12.com/starr-street-union-organizer-says-union-is-triggering-action-at-neglected-bushwick-building (background only, NOT used for buzzer claims)
- Bushwick Daily: Loft Law right to sue in Housing Court signed by Gov. Hochul (Dec 1, year not shown in fetched text; Governor's release dated Dec 7, 2021); lofts officially "interim multiple dwellings", many in Bushwick and Williamsburg; State Sen. Julia Salazar of Bushwick a sponsor — https://bushwickdaily.com/?p=40008 ; https://www.governor.ny.gov/news/governor-hochul-announces-enactment-law-significantly-increasing-protections-loft-residents
- NYC Loft Board Fact Sheet #1: Loft Law (MDL Article 7-C, §§ 280–287) created interim multiple dwellings (IMDs), former commercial/manufacturing buildings used as homes by at least three families; enacted to require owners "to bring converted occupancies into code compliance"; a § 281(5)/(6) unit must be at least 400 sq ft, not in a cellar, and "must have an entrance that does not require passage through another unit" — https://www.nyc.gov/assets/loftboard/downloads/pdf/fact-sheets/fact_sheet_no1.pdf
- Multiple Dwelling Law § 50-a (FindLaw text): class A multiple dwellings erected or converted after Jan 1, 1968 need automatic self-closing and self-locking entrance doors; with eight or more apartments also an intercommunication system at the main lobby door with voice communication and remote release; pre-1968 buildings must install doors and intercom when tenants occupying a majority of apartments request or consent in writing — start within ninety days, generally finish within six months; for rent-regulated dwellings the city housing rent agency sets the owner's cost-recovery terms — https://codes.findlaw.com/ny/multiple-dwelling-law/mdw-sect-50-a/
- NYS DHCR Fact Sheet #24 (04/2025) Major Capital Improvements: MCI increases prohibited for buildings with 35% or fewer rent-regulated units; capped at 2% per year; amortized over 12 years (35 or fewer units) or 12½ years (more than 35); removed from rent 30 years after taking effect; examples listed are boilers, windows, electrical rewiring, plumbing and roofs (intercoms not listed) — https://assets.noviams.com/novi-file-uploads/nyaa/pdfs-and-documents/DHCR_Fact_Sheets/fact-sheet-24-04-2025.pdf
- HPD Self-Closing Doors page: apartment doors and hallway doors must swing closed and latch by themselves; inspectors check hallways, stairways, building entrance; a door that fails to self-close, seal or latch is a class C immediately hazardous violation, correct within 14 days; Local Law 71 of 2022 — HPD proactively inspects 300 class A multiple dwellings a year; owner duty in HMC § 27-2041.1 — https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page
- Brick Underground, Nov 7, 2019 (Mimi O'Connor): service calls quoted $195/hour and $250/hour plus parts; Daniel Vasquez (Paragon Security and Locksmith): a five-apartment building could be finished in a day; Pete Carmello (Lock and Tech, Brooklyn): a 100-unit building about two days; repairs need building authorization; Vasquez: "Now everyone wants more security." — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Brownstoner forum (published 2024-03-21) "Smart Buzzer/Intercom Advice - 3 Family": reply says Wi-Fi relays can tie into existing latch contacts at the existing system's voltage (commonly 8–12 or 10–16, AC or DC); "unless the smart system is hardwired, an electrician does not install them"; smart locks drive the lock side while older systems release the latch — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- Brownstoner forum archive (Oct 2007) "Electric Door Strike": owner told "there is no system to accomodate a buzzer" on double doors; reply: "you will need to modify the doors a bit, as the wiring needs to run down the doors" and walls likely opened — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Brownstoner forum: "$2000 reasonable estimate to install new 3 unit buzzer entry/intercom system?" — vendor quoted $2,000 replacement, troubleshooting at $150/hour with a 3-hour minimum; no replies — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- r/AskNYC (about March 2025, via snapshot): "New Apartment Has No Voice Intercom, Only a Doorbell" — "I get buzzed all day for other apartments", "The bell isn't even labeled on the outside of the building", "I don't feel comfortable buzzing random people in"; replies suggest labelling the button with name/apartment, reporting to 311 — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- Arts in Bushwick: Bushwick Open Studios 2026 ran September 18–20, 2026 (Fri 6–10 PM, Sat 12–6 PM, Sun 1–4 PM); "hundreds of participating spaces" open their doors — https://artsinbushwick.org/bos2026/
- Bushwick Daily: 56 Bogart building "just steps away from the Morgan stop", houses artist studios and galleries (Momenta Art, Fuchs Projects) — https://bushwickdaily.com/bushwick/categories/arts-and-culture/1336-bos-isnt-complete-without-a-visit-to-56-bogart-building
- NY GBL Article 6-D § 69-l: engaging in the business of installing, servicing or maintaining security or fire alarm systems means offering to install, service or maintain a system "to detect intrusion, break-in, movement, sound or fire"; licensees under this article — https://law.justia.com/codes/new-york/2020/gbs/article-6-d/69-l/
- I Dig Hardware (Lori Greene), July 1, 2014 + 2017 reply: under the NYC code, mag-locks released by a motion sensor fall under the sensor-release section which requires unlocking on fire alarm activation; mag-locks released by door-mounted hardware fall under a separate section that does not require fire alarm release — https://idighardware.com/2014/07/nyc-code-update/
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DuckDuckGo for "door buzzer installation Bushwick": EMPTY
- Yelp 1–3★ reviews for Brooklyn intercom installers: EMPTY (search returned directory listings only)
- r/Bushwick threads specifically about installing a buzzer: EMPTY (only the r/Bushwick 2:30 a.m. stranger thread already in the shared background pack)

### Questions people ask — Door Buzzer Installation in Bushwick
- Is a $2,000 quote reasonable for a new three-unit buzzer entry system? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Can a smart buzzer be added so a three-family's owner can let people in remotely, and should each unit get its own station? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/smart-buzzer-intercom-advice-3-family
- Who installs a smart buzzer — an electrician or not? — Brownstoner forum — same URL
- Can double doors take an electric strike, and who in Brooklyn installs one? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- My new apartment has only a doorbell, not a voice intercom, and it isn't labelled — what can I do? — Reddit r/AskNYC — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- How long does an intercom install take for a small building versus a large one? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Do I need the building's authorization before intercom work? — Brick Underground — same URL
- Is a landlord required to put in an intercom? (MDL 50-a framing) — Reddit r/AskNYC (silo S14) — https://www.reddit.com/r/AskNYC/comments/17knzko/
- Can intercom cost be passed to rent-stabilized tenants? — derived from MDL 50-a(3) / DHCR FS-24 (own question)
- Does a Loft Law (IMD) building have to have an intercom? — derived from Loft Board fact sheet / MDL 50-a (own question)

## Boerum Hill, Brooklyn — /door-buzzer-installation-boerum-hill-brooklyn-ny (factory research, 2026-11-11)

- PLUTO (queried Nov 11 2026, Firecrawl scrape of SODA API, histdist like '%Boerum%'): Boerum Hill Historic District 297 lots / 704 residential units; Boerum Hill Historic District Extension 279 lots / 774 units; together 576 lots, 1,478 apartments (about 2.6 per lot) — https://data.cityofnewyork.us/resource/64uk-42ks.json
- PLUTO, same two districts, lots by residential units: 0 units 3; 1 unit 109; 2 units 260; 3 units 114; 4 units 50; 5 units 6; 6 units 5; 7 units 6; 8 units 16; 9 units 3; 10 units 1; 12 units 1; 14 units 2. So 23 lots have eight or more apartments; 533 of 576 have four or fewer — https://data.cityofnewyork.us/resource/64uk-42ks.json
- PLUTO building classes in the two districts: B9 two-family 115 lots; C0 three-family 94; B3 two-family converted from one-family 79; A4 one-family attached rowhouse 79; C3 four-family 37; B1 two-family brick 36; S2/S3/S9/S5/S1/S0 (residence with store or office, mixed-use) 51 lots in total; C1 walk-up over six families 19 lots/162 units; C6 walk-up co-op 12 lots/63 units; R1/R6/RM condos 13 lots — https://data.cityofnewyork.us/resource/64uk-42ks.json
- HPD housing maintenance code violations with INTERCOM in the description, Brooklyn Community Board 2, by inspection year (queried Nov 11 2026): 2020 20, 2021 37, 2022 34, 2023 18, 2024 33, 2025 24, 2026 26 (to Nov 11) — 192 since 2020; before 2012 never more than 13 a year. CB2 also covers Downtown Brooklyn, Brooklyn Heights, Fort Greene, Clinton Hill, DUMBO — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- HPD intercom violations since 2020 in CB2 by street, top: Clinton Ave 22, Greene Ave 13, Washington Ave 12, Carlton Ave 10, Lefferts Pl 9, Pacific St 8, Atlantic Ave 6, Nevins St 6, Bergen St 5, Wyckoff St 4, State St 3, Hoyt St 2, Smith St 2, Bond St 1, 3 Ave 1 (Boerum Hill streets are mid-table; the board's highest counts are in Clinton Hill/Fort Greene) — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- HPD intercom violation records on streets that run through Boerum Hill (Pacific, Atlantic, Nevins, Bergen, Wyckoff, State, Hoyt, Smith, Bond, 3 Ave, Dean, Schermerhorn, Warren, 4 Ave) since Jan 1 2020 within CB2: 38 records. One Nevins Street walk-up was cited six times between Aug 2023 and Oct 2026 (latest Class B Oct 5 2026, previous Aug 7 2026 status "NOT COMPLIED WITH"). A Wyckoff Street building cited three times (Aug 2024, Aug 2025, Apr 2026). Wording: "INTERCOM SYSTEM FROM BUILDING FRONT TO RETURN BUZZER AT WEST WALL IN THE FOYER", "BELL BUZZER/INTERCOM SYSTEM FROM BUILDING ENTRANCE TO THE SOUTH WALL IN THE PRIVATE HALLWAY", "FROM BUILDING ENTRANCE TO RETURN PANEL AT WEST WALL IN THE KITCHEN"; all under "§ 27-2005 HMC: PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE INTERCOM SYSTEM"; Classes A and B; statuses include "FIRST NO ACCESS TO RE- INSPECT VIOLATION" — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- NYC 311 complaints, descriptor BELL/BUZZER/INTERCOM, community board 02 BROOKLYN, by year: 2020 30, 2021 61, 2022 65, 2023 71, 2024 81, 2025 61, 2026 107 (to Nov 11) — 2026 is the highest year on record, already ahead of 2024 by 26. By street since 2020: Pacific St 19, Atlantic Ave 11, Hoyt St 7, Nevins St 6, Bergen St 5, State St 5, Schermerhorn St 4, Wyckoff St 4, 3 Ave 3 (CB2's top street is Clinton Ave, 55) — https://data.cityofnewyork.us/resource/erm2-nwe9.json
- DNAinfo, Jan 17 2013: 48 of the 141 burglaries in the 84th Precinct in 2012 happened when residents' doors were unlocked; Capt. Maximo Tolentino, 84th Precinct CO: "Even if you're home, you can't assume it's OK to leave your front door open." Howard Kolins, president of the Boerum Hill Association: "Don't become a crime victim because you encouraged a crime of opportunity." — https://www.dnainfo.com/new-york/20130117/boerum-hill/boerum-hill-residents-invite-burglars-by-leaving-doors-unlocked-police-say
- Habitat magazine, Feb 2024: Multiple Dwelling Law requires buildings built or converted after 1968 with eight or more units to have "a two-way voice intercom system linking the front door to each apartment"; scenario of a shareholder who lost intercom service after a downstairs renovation; Nancy Kourland (Lasser Law Group): "the co-op has a legal obligation to repair or replace the intercom"; courts treat intercoms as an essential service — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brownstoner forum "Door Bell for 3-Fam Brownstone": owner's former contractor "knocked out the previous bell that was working"; wants new bell and intercom with no door strike — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Brownstoner forum "Intercom for a three family": owner wanted only "a buzzer and intercom in each unit" with no automated door openers; reply recommended calling Aiphone to design the system — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Brownstoner forum archive "Security and the Front Door" (2008): townhouse owner wanted "a buzzer on both front doors" to let deliveries into the vestibule; another member described being trapped and robbed in the vestibule between the two doors and said the interior lock should not be "too difficult or time consuming to unlock"; a fire-alarm installer advised against "tying a remote release to the inner door" and noted typical strikes "rely on the door handle latch" — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- Brooklyn Paper: Bond Street townhouse parcel theft, front gate opened, about $3,500 in parcels including a Ring doorbell (carried from neighborhood pack) — https://www.brooklynpaper.com/84th-precinct-parcel-thief-hits-boerum-hill
- Reddit r/AskNYC (excerpt): renter considering "a newly built 3-unit building in Brooklyn with a first-time landlord" with no buzzer and one mailbox — https://www.reddit.com/r/AskNYC/comments/1t74q1e/is_no_buzzer_and_one_mailbox_for_3_apartments/
- Reddit r/AskNYC (excerpt): "I live in a building in Brooklyn, with only 4 units, which means the landlord isn't required to put in a buzzer system or a self-locking front door" — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Reddit r/NYCapartments (excerpt): "Intercoms are only legally required in buildings with 8 or more apartments built after 1968. A lot of brownstones just have them installed in..." — https://www.reddit.com/r/NYCapartments/comments/1gfytbz/building_buzzer_installation_rights/
- Reddit r/AskNYC (excerpt): landlord added extra locks to prevent package theft; a tenant "suggested installing a video intercom so residents could actually see who was at the door" — https://www.reddit.com/r/AskNYC/comments/1xruqah/nyc_landlord_installed_additional_locks_to/
- Reddit r/accesscontrol (excerpt): "We're a 13 unit (5 storey) condo in NYC with an existing analogue intercom system. We're looking to upgrade to video" — https://www.reddit.com/r/accesscontrol/comments/1phe7e7/its_almost_2026_whats_the_best_video_intercom/
- Reddit r/accesscontrol (excerpt): owner planning intercom and access for a 5-unit building still under construction — https://www.reddit.com/r/accesscontrol/comments/1ds3pjn/access_intercom_system_recommendations_for_small/
- Google PAA / PASF / AI Overview for "door buzzer installation Boerum Hill": EMPTY
- Answer the Public: EMPTY
- Bing / DuckDuckGo: EMPTY
- Yelp 1–3 star reviews for buzzer/intercom installers near Boerum Hill: EMPTY
- Boerum Hill-specific Reddit thread on buzzers: EMPTY

### Questions people ask — Door Buzzer Installation in Boerum Hill
- Is it normal for a newly built three-unit Brooklyn building to have no buzzer? — Reddit — https://www.reddit.com/r/AskNYC/comments/1t74q1e/is_no_buzzer_and_one_mailbox_for_3_apartments/
- My four-unit building has no buzzer; how much does a buzzer/intercom system cost? — Reddit — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Can tenants ask the landlord to install a buzzer, and do they have any rights to one? — Reddit — https://www.reddit.com/r/NYCapartments/comments/1gfytbz/building_buzzer_installation_rights/
- Can I install a buzzer for my apartment without the landlord's permission? — Reddit — https://www.reddit.com/r/AskNYC/comments/buirgq/missing_apartment_buzzer/
- My building has no doorbell or buzzer at all; what is the owner responsible for? — Reddit — https://www.reddit.com/r/nyc/comments/cr3om/my_apartment_building_doesnt_have_any/
- What is the best video intercom for a small NYC condo upgrading from analog? — Reddit — https://www.reddit.com/r/accesscontrol/comments/1phe7e7/its_almost_2026_whats_the_best_video_intercom/
- Which intercom should go into a small building that is still under construction? — Reddit — https://www.reddit.com/r/accesscontrol/comments/1ds3pjn/access_intercom_system_recommendations_for_small/
- Would a video intercom help with package theft better than extra locks? — Reddit — https://www.reddit.com/r/AskNYC/comments/1xruqah/nyc_landlord_installed_additional_locks_to/
- Our contractor knocked out the working doorbell during renovation; who can put in a new bell and intercom? — Brownstoner — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Can a three-family get a buzzer and intercom in each unit without an automatic door opener? — Brownstoner — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Should both front doors of a townhouse get a buzzer release? — Brownstoner — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- Who pays when a neighbor's renovation cuts the building intercom? — Habitat — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law

## City Line, Brooklyn — /door-buzzer-installation-city-line-brooklyn-ny (factory research, 2026-11-11)

- Brooklyn Community District 5 (East New York, Cypress Hills, City Line) has about 16,000 one-to-three family residential properties and nearly 9,000 two-family homes with below-grade spaces; of 102 homes assessed for the city's basement pilot, 34 were one-family (33%), 59 two-family (58%) and 9 three-family (9%); 70 of the 102 had cellars rather than basements — Citizens Housing & Planning Council, BACPP Interim Report, May 2023 — https://chpcny.org/wp-content/uploads/2023/05/CHPC_BACPP-Interim-Report_v3.pdf
- Same report: 35% of properties failed pre-screening because there was no existing door from the subgrade space to a public way; only 31% of assessed homes had at least one door exiting directly from the basement or cellar; under the pilot, cellar units require two egress doors; one single-family home broke ground in April 2023 and four two-family homes remained in pre-development; zero completed conversions reported — https://chpcny.org/wp-content/uploads/2023/05/CHPC_BACPP-Interim-Report_v3.pdf
- HPD's Basement Apartment Conversion Pilot Program (with Cypress Hills Local Development Corporation) covered East New York and Cypress Hills, Community District 5; owners of one-, two- or three-unit homes occupying it at least 270 days a year; loans up to $120,000; enabling legislation Intro. 1004 passed February 2019; program now "no longer considering applications at this time" — https://www.nyc.gov/site/hpd/services-and-information/basement-apartment-conversion-pilot-program.page
- 1 RCNY §42-01 (NYC rule on entrance doors, locks and intercommunication systems): Class A multiple dwellings with eight or more apartments must have an intercom; the minimum acceptable setup is "a bell or buzzer system" plus a return buzzer that unlocks the door, or a speaking and listening device; push buttons no more than six feet above the floor, speaking device between four and five feet up; devices must be approved; existing devices in good condition and working adequately may be accepted — https://www.nyc.gov/assets/buildings/rules/1_RCNY_42-01.pdf
- DHCR opinion letter (Charles Goldstein, May 21, 1996, LVT No. 11329): buildings built or converted after Jan. 1, 1968 must have "some type of intercom system," even "if only a bell and buzzer system, whether or not tenants ask for it"; older buildings when a majority of tenants request or consent; owner who installs one can apply for a Major Capital Improvement rent increase — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- HPD Self-Closing Door Proactive Program (Local Law 71 of 2022, after the Twin Parks fire), FY25 report: 300 buildings inspected Oct 2024–May 2025, 289 received at least one violation, 2,937 violations (2,033 apartment doors, 904 public-area doors), about 75% corrected by deadline; Brooklyn: 93 buildings, 4,833 units, 728 violations, 77% corrected; buildings selected must have more than six units; "Apartment and common area doors in multiple dwellings are required by law to swing closed and latch" — https://home4.nyc.gov/assets/hpd/downloads/pdfs/services/self-closing-doors-program-report-fy25.pdf
- Brick Underground (Mimi OConnor, Nov 7 2019): installer Pete Carmello of Lock and Tech: "A lot of times it's user error"; Daniel Vasquez of Paragon Security and Locksmith: "It's all in the wire connections" (lobby base, apartment station, door strike, power supply) and older systems' core wiring is "typically fine"; service calls quoted at $195 and $250 an hour plus parts; a five-apartment building could be replaced in a day; repairs need the building's authorization — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- ButterflyMX on how a buzzer works: call → transmission over dedicated wiring, phone/cellular or IP → conversation → release command to a controller or relay → relay changes the door-release circuit for a set time; the relay "doesn't physically swing the door open"; cites a $150–$250 limited-repair figure from a NYC installer — https://butterflymx.com/blog/apartment-buzzer/
- BK Reader, Jan 9 2025: NYCHA Boulevard Houses (East New York, outside City Line) resident Latoya Druck says the entrance door lock is broken and unsecured: "A lot of the kids come in, and the door is not fixed" — https://www.bkreader.com/in-other-brooklyn-news/nycha-resident-raises-alarm-over-broken-door-lock-at-boulevard-houses-10051288
- Openigloo lists 652 buildings in City Line, with addresses on Forbell Street, Crescent Street, Lincoln Avenue, Hemlock Street, Pitkin Avenue, Sheridan Avenue, Sutter Avenue, Glenmore Avenue, Euclid Avenue, Pine Street, Drew Street and Autumn Avenue, several marked rent-stabilized — https://www.openigloo.com/buildings/brooklyn/city-line/historic-and-modern?page=16
- Redfin, City Line multi-family for sale: 14 listings, median list price $1.09M (Nov 2026) — https://www.redfin.com/neighborhood/208630/NY/New-York/City-Line/multi-family-homes-for-sale
- Brownstoner forum (multi-family brownstone owner): a wired video doorbell quote of about $3,000; another owner wired a SimpliSafe doorbell into the foyer "switchbay" with plug-in chimes for upper floors — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- r/AskNYC "New Apartment Has No Voice Intercom, Only a Doorbell": tenant can't see or hear visitors, gets rung for other units, button unlabeled; replies suggest labeling the button and reporting to 311 — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- City Line-specific HPD intercom violation counts / 311 buzzer complaint counts: EMPTY (NYC Open Data not reachable)
- DOB permits for intercom/buzzer work in City Line: EMPTY
- LPC rules: EMPTY (no City Line historic district found)
- Local news about buzzers/intercoms inside City Line itself: EMPTY

### Questions people ask — Door Buzzer Installation in City Line
- Why does my apartment buzzer keep buzzing? — ButterflyMX FAQ (PAA-style) — https://butterflymx.com/blog/apartment-buzzer/
- Who is responsible for fixing a broken apartment buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Can a renter add smart control to an existing buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- How does a door buzzer actually unlock the door? — ButterflyMX — https://butterflymx.com/blog/apartment-buzzer/
- Must a landlord provide a bell and buzzer system in an older building? — DHCR / LandlordvTenant — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- Can the landlord raise the rent after installing a new intercom? — DHCR / LandlordvTenant — https://landlordvtenant.com/article/when-must-landlord-provide-bell-and-buzzer-system
- How high should intercom buttons be mounted? — 1 RCNY 42-01 — https://www.nyc.gov/assets/buildings/rules/1_RCNY_42-01.pdf
- How long does it take to replace an intercom in a small building? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Is a broken intercom usually the wiring or the equipment? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- My apartment only has a doorbell, no voice intercom; is that allowed? — Reddit r/AskNYC — https://reddit.sentinel-team.org/posts/1qcqqmd/snapshots/2026-01-14T23%3A30%3A47.074417Z
- How do upper floors of a multi-family house hear a video doorbell? — Brownstoner — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- Does a separate basement entrance need its own door to the street? — CHPC report (BACPP) — https://chpcny.org/wp-content/uploads/2023/05/CHPC_BACPP-Interim-Report_v3.pdf
- Google PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Yelp for "door buzzer installation City Line": EMPTY

## Carroll Gardens, Brooklyn — /door-buzzer-installation-carroll-gardens-brooklyn-ny (factory research, 2026-11-11)

- LPC Permit Guidebook ch. 11 (Health & Safety): staff can issue permits for intercom panels; "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; "An intercom can also be installed on a fence or wall in front of the entranceway"; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; design, size and finish "must be compatible with the architecture of the building" — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Same guidebook, general criteria: no equipment on or in front of a primary facade "unless no other option exists"; attach to mortar joints, plain masonry, wood, metalwork or concrete paving; "must not be attached through cast iron or on any decorative surfaces"; conduit concealed where possible, otherwise "a maximum of approximately ten inches of visible conduit"; surface conduit painted to match; equipment "as small as possible and painted to blend" — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Same guidebook, application materials: color photos of the whole building and close-ups, elevation drawings and details for visible installations (in-kind replacement of existing intercoms exempt from the drawing requirement), color specs/paint cards, manufacturer cut sheets, written explanation; "Ordinary maintenance, repair, and retrofitting of equipment do not require a permit"; guidebook does not address card readers, keypads, electric locks — LPC contact 212-669-7817 (not put on page) — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Brick Underground (Sept 6, 2023): about 95 percent of Carroll Gardens housing is single-family brownstones or brownstones converted into boutique condos or co-ops; agent: "It's not a neighborhood of big buildings"; boutique buildings named: 145 Carroll Gardens at 14 President St (7 stories, 2018, 17 units), 480 Degraw St (4 stories, 2019, 13 units), 98 Luquer St (1910 co-op, 8 units), 385 Clinton St (1920 limestone, 8 units), 443 Court St (1900, 4 stories, 8 units), 162 Huntington St (2000 condo, 6 units), 283 President St (3 condos in converted brownstone, listing mentions a "virtual doorman") — https://www.brickunderground.com/buy/your-next-move-carroll-gardens-brownstone-Brooklyn-boutique-coops-condos
- LPC designated the former Hans S. Christian Memorial Kindergarten, 236 President St (1897), and the adjoining 238 President St (1853, Anglo-Italian, converted into co-ops in 1984) as individual landmarks, Sept 18, 2018 — https://bklyner.com/lpc-designates-former-hans-s-christian-kindergarten-a-landmark
- LucidRents record for 423 Court St (4 units, 3 residential, built 1920): two HPD Class C violations, June 2, 2023 (closed), "REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING" — a permanently installed door stopper at the building entrance door — https://lucidrents.com/nyc/building/brooklyn/423-court-street-brooklyn-ny-11231
- DNAinfo (July 28, 2015): 84 newspapers worth $189 stolen from the vestibule of a Carroll Gardens residential building between Jan 3 and July 24, 2015; police report said the lobby "was open to the public" — https://www.dnainfo.com/new-york/20150728/carroll-gardens/84-ny-post-daily-news-newspapers-stolen-from-building-lobby-police-say
- News 12 (Feb 17, 2018), nearby Prospect Heights: man followed a delivery person into a building near St. Mark's Place and Vanderbilt Ave, masked up and burglarized an apartment (passport, checks, about $400) — https://newjersey.news12.com/amp/police-man-burglarized-prospect-heights-building-after-tailing-delivery-person-37529978
- Brownstoner forum, "Video doorbell for upper levels of multi-fam brownstone?": owner with "an old buzzer intercom in place for two of the apartments" was quoted "over $1500" (later corrected to "more like $3,000 and that was two years ago") for a video system; one reply: "The doorbell wiring was too old and we opted to get the plug in bells"; another said the quote "sounds cheap to me" for wired — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- Brownstoner forum, "Door Bell for 3-Fam Brownstone": owner's "old contractor and his crew knocked out the previous bell that was working"; wanted a new doorbell and intercom, no door strike — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Brownstoner forum, "Intercom for a three family": "Nothing fancy just a buzzer and intercom in each unit- no automated door openers" — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Brownstoner forum archive, "Electric Door Strike" (2007): installing buzzers on brownstone double doors meant opening walls and cutting a channel behind the astragal; poster told no system fits their double doors; tossing keys out the window mentioned as common alternative — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Habitat Magazine (Feb 2024): MDL — buildings built/converted after 1968 with 8+ units need two-way intercom; housing maintenance code requires a functioning intercom; courts treat it as an essential service; attorney Nancy Kourland: "As a result, the co-op has a legal obligation to repair or replace the intercom" — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground intercom repair guide (Nov 7, 2019): Daniel Vasquez (Paragon Security and Locksmith): "It's all in the wire connections"; points of failure = lobby base, apartment station, door strike, power supply in basement or lobby ceiling; even old Lee Dan systems usually have sound core wiring; five-apartment building replaced in about one day; Pete Carmello (Lock and Tech): "A lot of times it's user error" — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- NYC Tenant Data Privacy Law (Local Law 63 of 2021): owners of class A multiple dwellings using smart access must get express consent in writing or via app, destroy authentication data no later than 90 days after collection unless anonymized, and may not require use of smart access to enter the tenant's dwelling unit — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- HPD violation counts for intercom in ZIP 11231 via NYC Open Data — EMPTY (data.cityofnewyork.us not reachable)
- Reddit r/CarrollGardens / r/Brooklyn buzzer threads — EMPTY (no threads returned)
- Local news on door buzzers specifically in Carroll Gardens 2024–2026 — EMPTY

### Questions people ask — Door Buzzer Installation in Carroll Gardens
- Google People Also Ask / People Also Search For / Answer the Public / Bing / DuckDuckGo / Yelp — EMPTY
- Can a battery video doorbell be mounted over the old two-apartment buzzer intercom, or does the intercom have to be removed? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- Is $1,500 (or $3,000) a fair price to replace an old brownstone buzzer with a video system? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- What if the doorbell wiring is too old to reuse? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone/?sort_replies=asc
- Who can replace a doorbell and intercom that a renovation crew knocked out in a three-family brownstone? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Can a three-family get a buzzer and intercom in each unit without an automatic door opener? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Can a brownstone's double doors take an electric strike, and do the walls have to be opened? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Where can an intercom go on a landmarked house, and how many are allowed? — LPC Permit Guidebook (question framing) — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- What does Landmarks need to see before a new intercom panel goes on a district building? — LPC Permit Guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- What is a virtual doorman and does it replace a buzzer? — Brick Underground listing mention — https://www.brickunderground.com/buy/your-next-move-carroll-gardens-brownstone-Brooklyn-boutique-coops-condos

## Coney Island, Brooklyn — /door-buzzer-installation-coney-island-brooklyn-ny (factory research, 2026-11-11)

- NYC Comptroller resident-powered audit (site visits Aug 30–Sep 8 2022, 262 NYCHA developments, 100+ auditors, 600+ resident survey responses): 40.1% of NYCHA entrance-door locks citywide were broken, 28.5% of rear/side doors had broken locks; in Brooklyn 39.7% of entrance doors had broken locks. 57.9% of residential entrance doors were open or had broken locks in 2022, up from 23.5% in 2018; in Brooklyn the figure rose from 17.0% to 66.0%. Residents and staff said intercoms, locks, keys and door-release buttons often don't work, so residents prop doors open; one resident said their building's intercoms had been broken for 10 years; some repaired doors and intercoms broke again soon after. Quote, Comptroller Brad Lander: "Broken doors are a symbolic reminder that home safety starts at the entrance." Coney Island developments not named individually. — https://comptroller.nyc.gov/newsroom/comptrollers-auditors-find-40-1-of-nycha-entrance-doors-have-broken-locks-as-part-of-new-resident-powered-audit-initiative
- HPD violations at a Neptune Avenue building in ZIP 11224, all dated Aug 14 2026: Class A "PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE INTERCOM SYSTEM IN THE FOYER LOCATED AT APT 5M"; Class C "REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING METAL DOOR STOP ATTACHED TO VESTIBULE DOOR AT PUBLIC HALL, 1st STORY"; Class C self-closing apartment entrance door with missing/defective hinges. The listing summary shows 37 "Door/Lock" violations among 168 HPD violations for the building. — https://lucidrents.com/nyc/building/brooklyn/neptune-avenue-brooklyn-ny-11224/violations
- HPD self-closing doors: Local Law 71 of 2022 requires HPD to select 300 class A multiple dwellings a year for proactive inspection of all self-closing doors in common areas, hallways and apartment doors; owner duty HMC §27-2041.1; failing doors draw class C immediately hazardous violations, 14 days to correct; "Apartment doors and hallway doors are required by law to swing closed and latch by themselves"; tenants must not prop doors, tape latches or use wedges/door stops. — https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page
- 311: broken or missing doorbells, buzzers or intercoms can be reported as apartment complaints or public-area complaints; try owner/managing agent/super first (co-op/condo: board or management company); HPD contacts the managing agent, warns a violation may issue, calls the tenant back, and sends a Code Enforcement inspector if not fixed. — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Habitat Magazine, Feb 26 2024: under the Multiple Dwelling Law, buildings built or converted after 1968 with eight or more units must have a two-way voice intercom from the front door to each apartment; the city housing maintenance code also requires a functioning intercom; courts have treated intercoms as an essential service (warranty of habitability). Example: a 54-unit co-op shareholder lost intercom service after a downstairs neighbor's renovation. Quote, Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom," — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground NYC intercom repair guide (Nov 7 2019): problems usually sit at the lobby base, apartment station, door strike or power supply, not the wire inside walls; quote Daniel Vasquez (Paragon Security and Locksmith): "It's all in the wire connections."; Pete Carmello (Lock and Tech): "A lot of times it's user error"; replacement about one day for a five-apartment building, about two days for a 100-unit building; brands named 2N, Comelit, Siedle, Aiphone, ABB. — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- ButterflyMX small-building repair-vs-replace guide: vendor planning ranges about $1,500–$2,500 (ButterflyMX) and $2,200–$5,000+ (Swiftlane) for small single-entrance replacement; entrance count and controlled doors often matter more than unit count; "Do not replace a system based on age alone."; symptom map: continuous buzzing = stuck button/panel, no or one-way audio = station/audio path, static/hum = wiring/interference, door doesn't release = relay/power supply/strike/maglock/door hardware, building-wide outage = shared power or control. — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Coney Island Houses (NYCHA), 2926 W 25th St: Dec 29 2023 rain flooded the lobby and knocked out elevators; resident: "Every time it rains hard, it floods in the hallway, then it leads to the elevator and the elevator stops". — https://brooklyn.news12.com/coney-island-houses-tenants-dealing-with-flooded-lobby-inoperative-elevators
- Sea Park East (Mitchell-Lama, Coney Island, managed by GRC Management): HPD records 361 violations; tenant complaints about rodents, garbage, elevators, gas — doors/intercom not mentioned (context: large Mitchell-Lama complexes with ongoing HPD activity). — https://newyork.news12.com/coney-island-tenants-demand-action-over-rats-garbage-broken-elevators-and-lack-of-gas
- Amalgamated Warbasse Houses (Habitat, Sep 29 2021): five 24-story towers, 2,585 units, about 8,000 people, 26 acres, Mitchell-Lama co-op opened 1964, a Naturally Occurring Retirement Community; capital project done one building at a time. — https://habitatmag.com/Publication-Content/Bricks-Bucks/2021/September-2021/Amalgamated-Warbasse-Houses-Co-op-Tackles-a-Giant-Project
- Sea Gate: private gated community west of West 37th Street since 1892, about 850 single-family houses (Queen Anne, Mediterranean), most residents in single- and two-family houses, 54% of homes rentals, private Sea Gate Public Safety Department; Sandy flooded the neighborhood and destroyed numerous houses. — https://en.wikipedia.org/wiki/Sea_Gate,_Brooklyn
- Coney Island housing stock (Brick Underground, Aug 7 2014): mostly large high-rise complexes — NYCHA, rentals, co-ops and condos — plus single-family Victorians, 1960s high-rise co-ops, brick row houses, Art Deco co-ops and modern brick homes; Trump Village co-op at 2932 West 5th Street; 501 Surf Avenue (1964). — https://www.brickunderground.com/node/38295
- Build It Back (Gotham Gazette, Oct 24 2014): Seagate 47 homeowners severely affected by Sandy; a planned redesign would add a third floor and convert the first floor to a carport for flood protection; homeowner on 36th Street near Kaiser Park. — https://www.gothamgazette.com/government/5398-build-it-back-waiting-game-frustrates-coney-island-homeowners
- NYC intercom law summary (Connextivity, vendor article, not official): MDL §50-a eight-plus apartments post-1968 two-way intercom and remote release; partial outages treated as violations; maglocks need fire alarm release, marked exit device, fail-safe power; intercom controls ≤48 in. — https://connextivity.squarespace.com/insights/nyc-intercom-laws-building-requirements
- Reddit r/ConeyIsland door buzzer/intercom threads: EMPTY (none returned in searches).
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo for "door buzzer installation Coney Island": EMPTY (not accessible); question list below uses titles of real articles returned for the Brooklyn/NYC queries.
- Yelp complaints for buzzer/intercom installers near Coney Island: EMPTY.

### Questions people ask — Door Buzzer Installation in Coney Island
- How do I get my landlord to fix a broken buzzer? — Google results (Brick Underground) — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- Broken buzzer or intercom in a small apartment building: repair or replace? — Google results (ButterflyMX) — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- How much does a buzzer system cost? — Google results — https://mds.oandg.co.uk/posts/how-much-does-a-buzzer-system-cost
- How to buy an apartment intercom system with door release? — Google results (Nasdaq) — https://www.nasdaq.com/articles/how-to-buy-an-apartment-intercom-system-with-door-release-0
- How do apartment buzzer systems work, and what types are there? — Google results (ButterflyMX) — https://butterflymx.com/blog/apartment-buzzer/
- What are tenant rights when building fobs stop working in NY? — Google results — https://tenant-rights.com/new-york/tenant-rights-when-building-fobs-stop-working-in-ny
- Is a working intercom required by law in a co-op? — Google results (Habitat) — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- How do I report a broken buzzer or intercom to 311? — Google results (311) — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Why do NYCHA entrance doors keep getting propped open? — Google results (NYC Comptroller) — https://comptroller.nyc.gov/reports/observations-of-building-doors-in-nycha-developments
- How do I stop packages being stolen from my building lobby? — Google results (Brick Underground) — https://www.brickunderground.com/live/packages-stolen-from-building
- Can a doorstop on the vestibule door get a building an HPD violation? — HPD violation listing — https://lucidrents.com/nyc/building/brooklyn/neptune-avenue-brooklyn-ny-11224/violations

## Clinton Hill, Brooklyn — /door-buzzer-installation-clinton-hill-brooklyn-ny (factory research, 2026-11-11)

- LPC Permit Guidebook ch. 11 (Health & Safety): "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; "An intercom can also be installed on a fence or wall in front of the entranceway"; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; design, size and finish "compatible with the architecture of the building" (neutral and discreet); "Staff can issue permits approving light fixtures and intercom panels" — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Same chapter: conduit "must be concealed" by going through plain masonry or wall cladding behind the installation; if not possible staff may approve "a maximum of approximately ten inches of visible conduit"; surface conduit painted to match, not on decorative surfaces; equipment "must not be attached through cast iron or on any decorative surfaces"; "as small as possible"; mailboxes may be "Attached to a gate or door underneath the stoop, or on a plain stoop wall adjacent to the opening"; an existing historic gate below the stoop "must be retained"; work that doesn't meet the rules may go to a public hearing — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Clinton Hill Historic District "Designated November 10, 1981"; styles listed include Greek Revival, Italianate, Romanesque Revival, Art Moderne; building types include row houses, mansions, stables, apartment houses and institutional buildings — https://hdc.org/buildings/clinton-hill-historic-district/
- LPC rejected a proposed Lefferts Place Historic District (Washington Ave to Bedford Ave, Fulton St to Atlantic Ave), reported June 7, 2012; LPC spokesperson: "There are a number of empty lots or other intrusions that disrupt the cohesion of the streetscape." — https://www.bkmag.com/?p=424
- Clinton Hill South Historic District is a National Register district, "Added to the National Register of Historic Places July 17, 1986", "Roughly Lefferts and Brevoort Pl. between Washington Ave. and Bedford Pl.", "246 contributing buildings", Neo-Grec row houses and early-20th-century Colonial Revival apartment buildings — https://historypointer.com/nris/resource/86001675
- 70 Lefferts Place designated an individual NYC landmark by unanimous LPC vote, Dec 12, 2006 — https://hdc.org/alert-70-lefferts-place-designated/
- Willoughby Walk (Clinton Hill Co-ops): "a two-building complex" (195 Willoughby Ave and 185 Hall St), 195 Willoughby is a "16-story slab tower" "erected in 1958", "287 co-operative apartments" per building; listing cites "a full-time doorman, 24-7 security at their front entrances, a live-in superintendent" — https://www.cityrealty.com/nyc/clinton-hill/willoughby-walk-195-willoughby-avenue/review/41704
- 43 Putnam Avenue (11238): 3 units, 3 floors, built 1895 — example of the small rowhouse rentals — https://www.openigloo.com/building/nyc/3056891-3019830077/brooklyn-clinton-hill-43-putnam-avenue-11238
- Pratt Institute: "Of the approximately 5000 students that attend Pratt, only 40% reside on campus" — off-campus renters fill nearby apartments, turnover each year — https://www.pratt.edu/about/offices/residential-life-and-housing/off-campus-housing/
- Brownstoner, Dec 12 2024: 1870s Italianate Clinton Hill row house once "separated into weird apartments, with multiple families living there", gutted for one family; only entry and vestibule doors and one mantel salvaged; "Two pairs of original entry doors were restored and repainted", inner set got "new glass with a reeded texture" — https://www.brownstoner.com/interiors-renovation/clinton-hill-townhouse-gut-renovation-addition-the-brooklyn-studio
- Brownstoner, June 19 2025: Clinton Hill Italianate brownstone whose entry doors "came with the house" and are "nearly all glass"; architect replicated them for a thinner inner set — https://www.brownstoner.com/interiors-renovation/clinton-hill-brownstone-gut-renovation-ravi-raj-historic-restoration
- Brooklyn Paper (88th Precinct report, Nov 4, year not stated): armed robber "followed the victim into the building" on Clinton Avenue near DeKalb Avenue about 8:30 a.m. — https://www.brooklynpaper.com/88th-precinct-armed-robbery-in-apartment-building
- News12 Brooklyn, Jan 4 2026: man threw bricks through basement and ground-floor windows of a Clinton Hill building on Dec 29 around 5 a.m.; residents said the building had been targeted several times in recent months — https://brooklyn.news12.com/exclusive-video-shows-man-throwing-bricks-into-clinton-hill-building
- Brownstoner forum, three-family brownstone: "Nothing fancy just a buzzer and intercom in each unit", no automatic door openers; reply recommended Aiphone, which will "design the system for you for free" — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Brownstoner forum: 3-unit house's buzzer "works only sporadically"; replacement estimate $2,000 "without any electrical work"; troubleshooting at $150/hour with three-hour minimum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Brownstoner forum Nov 18-20 2008 "Security and the Front Door" (townhouse, UWS): owner wanted buzzer on outer door so couriers could leave packages in the vestibule; installer advised "highly recommend not tying a remote release to the inner door"; another poster was robbed in their own vestibule between the two doors — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- Habitat Magazine, May 2017 "The New Buzzer": smartphone intercoms; ButterflyMX install about $5,000-$7,000 plus $2.50 per unit per month (Nicholas Silvers); Dan Arnold (Academy Mailbox): "A lot of our calls now are people who want to abandon the hard-wired intercom units in their apartments"; installation easier with sheetrock, harder with marble or granite — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- HPD Tenant Data Privacy Law: applies to owners of multiple dwellings using smart access (keyless) systems; collect only minimum data such as name and "the time and method of access, solely for security purposes"; express consent in writing or via app; must give tenants a data retention and privacy policy; destroy authentication data "no later than 90 days" unless anonymized — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Akuvox case study (Brighton Beach Ave, not Clinton Hill): 8 buildings of 60+ apartments each replaced an analog intercom + RFID with 7" IP door phones, 10" indoor monitors and an app — https://cie-group.com/media/upload/files/Akuvox-Brooklyn-Apartments_Case-Study-2020%282%29.pdf
- Clinton Hill HPD intercom-violation counts / 311 buzzer counts: EMPTY (NYC Open Data not reached)
- Reddit threads about buzzers in Clinton Hill: EMPTY (search returned none)
- Yelp reviews of buzzer installers near Clinton Hill: EMPTY
- Google PAA / PASF / AnswerThePublic / Bing / DuckDuckGo panels: EMPTY (not accessible)

### Questions people ask — Door Buzzer Installation in Clinton Hill
- Can we just get a buzzer and intercom in each unit of a three-family, without an automatic door opener? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Is $2,000 a reasonable estimate to install a new three-unit buzzer system? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Should the buzzer release the vestibule (inner) door too, so couriers can leave packages inside? — Brownstoner forum 2008 — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- How many intercom panels does Landmarks allow at a door, and where can it go? — LPC Guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Can the panel go on the areaway fence or gate instead of the brownstone? — LPC Guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Do houses on Lefferts or Brevoort Place need a Landmarks permit for a door station? — BKMag / NRHP listing — https://www.bkmag.com/?p=424
- Can a smartphone intercom replace the hard-wired units in the apartments, and what does it cost monthly? — Habitat — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- What data can an app or fob entry system keep about tenants? — HPD — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Can a release be added to tall glass original entry doors? — Brownstoner (2024, 2025 renovations) — https://www.brownstoner.com/interiors-renovation/clinton-hill-brownstone-gut-renovation-ravi-raj-historic-restoration
- How do I stop strangers following residents in? — Brooklyn Paper — https://www.brooklynpaper.com/88th-precinct-armed-robbery-in-apartment-building
- Questions from PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Reddit / Yelp: EMPTY

## Cobble Hill, Brooklyn — /door-buzzer-installation-cobble-hill-brooklyn-ny (factory research, 2026-11-11)

- Home Buildings, 439 Hicks Street (11201): Openigloo lists 24 units across 6 floors, 1 open violation, 0 violations per unit; the single tenant review names a "Horrible outside intercom" and advises owners to "Improve intercom." — https://www.openigloo.com/building/nyc/3331327-3003107502/brooklyn-carroll-gardens-439-hicks-street-11201
- Cobble Hill Towers, 431 Hicks Street: CityRealty describes a "landmark nine-building apartment complex", 188 apartments, six stories, completed 1879, "open stairways", private entries off exterior corridors with ornate iron railings, two landscaped courtyards; converted to a condominium (CityRealty gives 2010). Intercom/package handling not mentioned. — https://www.cityrealty.com/nyc/cobble-hill/cobble-hill-towers-431-hicks-street/review/47311
- The Landmark at Strong Place, 58 Strong Place: former Baptist church by Minard Lafever, converted to 23 condominium units on 4 stories (CityRealty gives 2010 and 2011 in different fields); amenities list includes "Virtual Doorman", mail room, elevator, bike room; "Doorman: None". — https://www.cityrealty.com/nyc/cobble-hill/the-landmark-strong-place-58-strong-place/51892
- Verandah Place: Untapped New York (Apr 6 2015) — pre-Civil War service alley about 20 feet wide; south side is a row of small brick residences, mostly three stories, "built up to the sidewalk"; "Some of these structures were originally built as stables and later converted to residential use"; Cobble Hill Park opened across the street July 14 1965. — https://www.untappedcities.com/historic-verandah-place-and-cobble-hill-park-19th-century-mews-20th-century-views/
- Cobble Hill Historic District: Cobble Hill Association knowledge base — designated 1969, 796 buildings built 1830s–1920s, roughly Atlantic Ave / Degraw St / Hicks St / Court St; 1988 extension added 350, 354 and 356 Henry St; National Register 1976; exterior alterations generally require LPC pre-approval; "Even updating the stone on the sidewalk in front of your home requires a permit." — https://cobblehill.nyc/knowledge_base/landmarking-cobble-hill/
- LPC Permit Guidebook ch. 11 (Health & Safety): "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; "An intercom can also be installed on a fence or wall in front of the entranceway"; conduit "must be concealed by going through plain masonry or wall cladding behind the installation", otherwise staff may approve "a maximum of approximately ten inches of visible conduit", painted to match; equipment attached "at mortar joints, plain masonry, wood, or metalwork" and "must not be attached through cast iron or on any decorative surfaces"; "as small as possible and painted to blend". — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- 27 Strong Place (Cobble Hill HD), LPC hearing materials Mar 25 2025 (LPC-25-06592): front-door sheet "Wood door rebuilt to match existing", "Transom to Remain", existing and proposed mail slot ("Van Cronenberg Letter Plate Slim") and knob; intercom not shown. Shows LPC reviewing door hardware at the front door of a district house. — https://www.nyc.gov/assets/lpc/downloads/pdf/presentation-materials/20250325/27-Strong-Place.pdf
- Single-family reconversions: Brownstoner (Nov 11 2013, summarising NYT "Townhouse Turnaround") on "Converting formerly single family townhouses back into single family townhouses"; rental units "increasingly common to see ... labelled 'guest suite' on floor plans". — https://www.brownstoner.com/real-estate-market/trend-owners-developers-turn-townhouses-back-into-single-families/
- PincusCo (June 11 2026): "Vega sells single-family conversion for $16M in Cobble Hill, was $3.85M in 2020" (205 Clinton Street per caption; details paywalled). — https://www.pincusco.com/vega-sells-single-family-conversion-for-16m-in-cobble-hill-was-3-85m-in-2020/
- Brownstoner forum "Door Bell for 3-Fam Brownstone": owner of a three-family brownstone wanted a new doorbell and intercom "no door strike" after a previous contractor removed the working bell; replies recommend installers and a "flat rate quote"; no prices. — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Brownstoner forum (Oct 28 2010) "Landlord Installing Phone Intercom System": tenant with only cellphones objects that a phone-dialing system "forces us into either having our cellphones called every time somebody rings our apartment"; replies: systems "can call multiple phone numbers", one installer on a 40-unit co-op says "you don't need actual phone service". — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- Brownstoner forum (Sept 14 2009): Park Slope 12-apartment building where one tenant refused entry to the electrician; building intercom down three months; "the one station can just be bypassed." — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Habitat Magazine (May 14 2018, Kathryn Farrell): NYC Building Code (then §1008.4.4) requires buildings with eight or more dwelling units to have an intercom letting each unit talk to the main entrance and release the lock; DOB Construction Codes Team: wi-fi not prohibited but "The requirement is that each unit be provided with such a system"; Dan Arnold (Academy Mailbox): "there needs to be a device in that apartment that allows the babysitter to buzz in emergency personnel"; Ira Meister (Matthew Adam Properties): "What most of my buildings have done is installed, basically, hybrid systems". — https://habitatmag.com/layout/set/amphtml/Publication-Content/Building-Operations/2018/2018-May/Wifi-Hardwire
- Habitat Magazine (May 9 2017, Lisa L. Colangelo): ButterflyMX smartphone system about $5,000–$7,000 to install plus $2.50 per unit per month; Dan Arnold: "If it's sheetrock, you can make a few holes and snake it down to the basement." "But nothing is insurmountable." — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- Brick Underground (Nov 7 2019): "You can't hear your guest, they can't hear you, or the lobby door isn't unlocking"; Pete Carmello (Lock and Tech, Brooklyn): "A lot of times it's user error"; Daniel Vasquez (Paragon): "It's all in the wire connections"; service-call quotes "$195 an hour and $250 an hour plus parts". — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- ButterflyMX "Intercom Repair in NYC" (updated Oct 19 2026): HPD correction periods "90 days for Class A violations, 30 days for Class B violations, and 24 hours for most Class C"; a 2022 Bronx decision "recorded a Class B violation for an inoperable bell and return-buzzer system"; NYC311 lists broken or missing doorbells, buzzers and intercoms as reportable; MDL 50-a baseline "does not, by itself, require video, mobile access, or remote management". — https://butterflymx.com/blog/intercom-repair-nyc
- Brownstoner forum (Oct 29 2007) "Electric Door Strike": glass-paneled double doors; reply "You'll need to open up the walls, probably quite a bit"; another says tossing the key out the window is common in their area. (Double-door angle already used on sibling pages — background only.) — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Brownstoner forum (Nov 18–20 2008) "Security and the Front Door": townhouse owner planning buzzers on both outer and inner doors so deliveries can be left in the vestibule; "Bklyn Fire Alarm Guy": "The concern with typical strikes is that they rely on the door handle latch." (vestibule-trap angle already used by a sibling — background only) — https://www.brownstoner.com/forum-archive/2008/11/security-and-th
- Brooklyn Paper 76th Pct roundup: package with clothes stolen from a Huntington Street stoop (Carroll Gardens side, not Cobble Hill; year not stated) — not used as a Cobble Hill fact. — https://www.brooklynpaper.com/thief-swipes-package-from-stoop
- NYC Open Data HPD violations (intercom, ZIP 11201/11231): EMPTY — host blocked from the research environment.
- Reddit r/CobbleHill / r/Brooklyn door-buzzer threads specific to Cobble Hill: EMPTY (searches returned only generic NYC threads).
- Yelp 1–3★ for intercom installers near Cobble Hill: EMPTY (search returned directory listings only).
- Google PAA / PASF / Answer the Public / Bing / DuckDuckGo: EMPTY as separate surfaces; question titles below come from search-result titles and forum threads.

### Questions people ask — Door Buzzer Installation in Cobble Hill
- How much does it cost to install a buzzer system in a brownstone? — search results (PASF-style) — https://www.brownstoner.com/forum/general-discussion/video-doorbell-for-upper-levels-of-multi-fam-brownstone
- Can a landlord switch the building to a phone-dialing intercom when tenants only have cellphones? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- Does a phone-based intercom need a landline? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- What do I do when one tenant won't let the installer in and the whole building's intercom is down? — Brownstoner forum (already in register) — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Who can install a doorbell and intercom on a three-family brownstone without a door strike? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Is a wi-fi-only intercom legal in a building with eight or more apartments? — Habitat Magazine — https://habitatmag.com/layout/set/amphtml/Publication-Content/Building-Operations/2018/2018-May/Wifi-Hardwire
- How many intercom panels can go on a landmarked doorway, and where? — LPC guidebook (already in register in meaning) — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Can the intercom go on the fence or areaway wall instead of the house? — LPC guidebook (already in register) — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Is it cheaper to repair or replace a broken buzzer in a small building? — ButterflyMX search title — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- How does an apartment door buzzer work? — search titles (ButterflyMX, EngineerFix) — https://butterflymx.com/blog/apartment-buzzer/
- How fast does a landlord have to fix a broken buzzer after HPD writes it up? — ButterflyMX — https://butterflymx.com/blog/intercom-repair-nyc
- Can I report a broken buzzer to 311? — ButterflyMX — https://butterflymx.com/blog/intercom-repair-nyc
- What should I do about a "horrible" outside intercom in a large rental building? — Openigloo tenant review — https://www.openigloo.com/building/nyc/3331327-3003107502/brooklyn-carroll-gardens-439-hicks-street-11201
- What is a virtual doorman and does a condo still need a buzzer? — CityRealty amenity listing (already in register in meaning) — https://www.cityrealty.com/nyc/cobble-hill/the-landmark-strong-place-58-strong-place/51892

## Columbia Street Waterfront, Brooklyn — /door-buzzer-installation-columbia-street-waterfront-brooklyn-ny (factory research, 2026-11-11)

Method: one web search backend plus page fetches. Google PAA/PASF, AnswerThePublic, Bing, DuckDuckGo, Yelp and NYC Open Data (HPD/311/DOB) could not be queried directly; those rows say EMPTY.

### Building stock that a door buzzer job meets here
- Columbia Terrace, 42 Carroll Street: built 1986, 3 floors, townhouse condo, post-war, walk-up, amenity listed: "Voice Intercom" — https://www.nestseekers.com/Bldg/71468/Columbia-Terrace-42-Carroll-Street-Brooklyn-NY-11231
- First Columbia Terrace, 250 Columbia Street (six alternate addresses on President Street): "a post-war condominium building ... finished in 1986", 27 units, walk-up — https://cityrealty.com/nyc/carroll-gardens/first-columbia-terrace-250-columbia-street/54685
- Other Columbia Terrace addresses exist at 38 and 44 Carroll Street and a "Third Columbia Terrace" at 57 Carroll Street — https://www.corcoran.com/building/carroll-gardens/165445 ; https://www.corcoran.com/building/red-hook/22316 ; https://www.nestseekers.com/4551453/third-columbia-terrace-57-carroll-street-38a-brooklyn-ny-11231-usa
- "By 1984, an urban renewal project was completed, as well as a brand-new street, houses along which sold out quickly"; the 1975 sewer accident led to the demolition of 33 buildings — https://wikiwand.com/EN/Columbia_Street_Waterfront_District
- 181 Columbia Street: 1931 townhouse, 3 apartments, 3 floors, walk-up, "Voice intercom"; listing calls it "the last remaining townhouse property on the coveted Columbia Street Waterfront" — https://currentreadvisors.com/ListingDetails/2977784/181-Columbia-Street-Cobble-Hill-Brooklyn-NY-11231
- 129 Columbia Street: 1910 pre-war townhouse rental, 4 units, 4 floors, "Voice intercom", walk-up — https://www.nestseekers.com/Bldg/175158/129-columbia-street-brooklyn-ny-11231
- 219 Columbia Street: 1930 low-rise, mixed use, 2 units, 3 floors, walk-up — https://www.nestseekers.com/Bldg/164050/219-columbia-street-brooklyn-ny-11231
- 279 Columbia Street: 1931, 3 stories, building class "S2 Primarily Two Family with Store or Office" — https://streeteasy.com/building/279-columbia-street-brooklyn
- 222 Columbia Street: 2002 mid-rise condo with elevator, garage and "Video intercom" — https://www.nestseekers.com/Bldg/161945/222-columbia-street-brooklyn-ny-11231
- 255 Columbia Street: "six-story, 13-unit Passive House building" with "triple-paned windows and mechanical ventilation with heat recovery" (Brownstoner, July 3 2014) — https://www.brownstoner.com/brooklyn-life/passive-house-condos-look-ready-for-tenants-on-columbia-street/
- Columbia Commons, 110 Warren Street: 2010, 48-unit six-story elevator condo, intercom and a virtual doorman system rather than a doorman, underground garage — https://www.cityrealty.com/nyc/cobble-hill/columbia-commons-110-warren-street/58526
- Columbia Hicks and Columbia Commons (GACE project): three six-story residential buildings, 136 units, "just south of Atlantic Avenue", basement-level parking — https://gace.net/projects/columbia-hicks-and-columbia-commons
- 414 Hicks Street: 2009, 95 units, 6 floors (Openigloo) — https://www.openigloo.com/building/nyc/3394115-3003047501/brooklyn-carroll-gardens-414-hicks-street-11201
- 1 Tiffany Place: built 1921, 70 units, 5 floors, 1 open Class B violation, one tenant review lists "24h noise from the BQE" as a con — https://www.openigloo.com/building/nyc/3003595-3003207501/brooklyn-carroll-gardens-1-tiffany-place-11201
- 185 Columbia Street (Columbia and Degraw): six-story, ten-unit new building completed 2026 (YIMBY; page could not be re-read this session, carried from neighborhood research) — https://newyorkyimby.com/2026/07/185-columbia-street-completes-construction-in-brooklyns-columbia-street-waterfront-district.html

### Rules and city data that bear on it
- MDL §50-a as summarized by Habitat (Feb 26 2024): buildings built or converted after 1968 with eight or more units "must have a two-way voice intercom system linking the front door to each apartment"; Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom." — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- ButterflyMX NYC repair guide: one NYC integrator's estimates "$100 to $300 for diagnostics, $500 to $1,500 for component replacement, and $1,000 to $3,000 for limited wiring repairs"; NYC311 lists "broken or missing doorbells, buzzers, and intercoms"; HPD correction periods "90 days for Class A violations, 30 days for Class B violations"; "The aim isn't to replace a system simply because it's old." — https://butterflymx.com/blog/intercom-repair-nyc
- Habitat, "For Door Buzzers, the Future Has Arrived" (Lisa L. Colangelo, May 9 2017): Dan Arnold, Academy Mailbox: "If it's sheetrock, you can make a few holes and snake it down to the basement." / "If the walls are marble or granite, that's a little harder. But nothing is insurmountable."; ButterflyMX install roughly $5,000 to $7,000 with $2.50 per unit monthly; virtual doorman about $15,000 a year for a 28-unit building (Nicholas Silvers, paraphrased) — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- HPD violations / 311 intercom complaints for the district: EMPTY (NYC Open Data not reachable)
- DOB permits for entry work in the district: EMPTY
- LPC: no historic district found inside the district (searches returned only Carroll Gardens individual landmark hearings on President Street and Cobble Hill); EMPTY for any district-specific LPC rule — https://www.citylandnyc.org/search/Columbia%20Street,%20Brooklyn/page/2

### Local conditions that change how the work is done
- The B61 runs "north along Columbia Street and east along Atlantic Avenue into Downtown Brooklyn" — https://en.wikipedia.org/wiki/B61_and_B62_buses
- Streetsblog (Aug 21 2026): city floats a busway; "The revamp would also close off the block of Columbia north of Hamilton Avenue entirely"; Hank Gutman: "Why are we exempting trucks on Columbia Street?"; changes "still years off" — https://nyc.streetsblog.org/2026/08/21/red-hook-busway-proposal
- Streetsblog (Aug 24 2026): BQE cantilever rebuild via bypass, construction 2029/2030 to 2040, $4 billion; drivers take "shortcuts around the trenched section in Carroll Gardens and Cobble Hill" — https://nyc.streetsblog.org/2026/08/24/mamdani-bqe-plan-august-2026
- Brick Underground "Living Next To" (David Colon, 2018/2019): Columbia Street resident near a slaughterhouse and garbage truck depot: trucks "start clanging around at like 4 a.m."; "The construction next door caused a big crack down the front of the building" — https://www.brickunderground.com/live/columbia-street-slaughterhouse-trash-truck-living-next
- DNAinfo (Apr 22 2014): Warren Street home between Hicks and Columbia burglarized, police reported "no signs of forced entry" — https://www.dnainfo.com/new-york/20140422/columbia-street-waterfront-district/jewelry-cash-stolen-from-columbia-street-waterfront-home-police-say
- Red Hook Star-Revue (Jan 9 2022): 76th Precinct meeting; officers suggested Ring cameras for package theft — https://www.star-revue.com/build-the-block-discusses-theft-and-traffic-by-nathan-weiser/
- Local news or Reddit specifically about door buzzers in the district: EMPTY

### Questions people ask — Door Buzzer Installation in Columbia Street Waterfront
- PAA (Google): EMPTY (not accessible)
- PASF / related searches: EMPTY
- AnswerThePublic: EMPTY
- Bing / DuckDuckGo: EMPTY
- Yelp: EMPTY
- Reddit (r/Brooklyn, r/AskNYC, r/homesecurity): EMPTY for this district
- Who is legally responsible for a broken intercom in a co-op or condo? — Habitat (guide, not on list) — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- What does intercom repair cost in NYC, and when should it be replaced instead? — ButterflyMX guide (not on list) — https://butterflymx.com/blog/intercom-repair-nyc
- Can a new bell and intercom be installed after a contractor knocked out the old one in a brownstone? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/door-bell-for-3-fam-brownstone
- Can an electric strike go on brownstone double doors? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2007/10/electric-door-s
- Is a smartphone intercom cheaper than a virtual doorman for a condo? — Habitat (guide) — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer

## Cypress Hills, Brooklyn — /door-buzzer-installation-cypress-hills-brooklyn-ny (factory research, 2026-11-11)

- 2 Elton Street (Cypress Hills, 11208): openigloo lists "53 units", "6 floors", "Built in 1928"; a former tenant's review (3+ years old) lists as a con "The Intercom system for the entrance door does not work" and advises owners "They should redo the whole Intercom System"; pros "Building is nice, quiet and clean"; 25 open HPD violations over the past 10 years (types not broken out) — https://www.openigloo.com/building/nyc/3086534-3039080010/brooklyn-cypress-hills-2-elton-street-11208
- 222 Highland Boulevard (Cypress Hills, 11207): openigloo lists "87 units·6 floors·Built in 1940"; review titled "Nice building but exterior noisy"; a con "charged for keys"; no intercom mention — https://openigloo.com/building/nyc/3086213-3038860010/brooklyn-cypress-hills-222-highland-boulevard-11207
- Openigloo's Cypress Hills "historic and modern" filter shows 1,381 buildings; first page addresses include 209 Sunnyside Ave, 75 Lincoln Ave, 120 Crescent St, 79 Elton St, 2920 Fulton St, 2678 Fulton St, 3418 Fulton St, 386 and 464 Ridgewood Ave, 80 Schenck Ave, 3226 Fulton St (no unit counts given) — https://www.openigloo.com/buildings/brooklyn/cypress-hills/historic-and-modern
- 3371 Fulton Street, NW corner of Fulton & Hemlock St: "3-unit mixed-use building", "two one-bedroom apartments above a modern food market", full basement (typical Fulton Street store-with-apartments-above stock; residential entrance not described) — https://www.apartmentbuildings.com/properties/3371-fulton-street/
- Cypress Village Homes (CHLDC, architect Magnusson Architecture and Planning): three buildings, 29 affordable apartments — three-story walk-ups on Linwood Avenue and Jerome Avenue (18 units, modular) and a four-story elevator building on Van Siclen Avenue (11 units), via HPD New Foundations ownership program — https://thenyhc.org/projects/cypress-village-homes/
- Chestnut Commons: 274 below-market-rate units on the lot bounded by Atlantic Avenue, Chestnut Street and Dinsmore Place; developers MHANY Management, Urban Builders Collaborative and Cypress Hills Local Development Corporation (2017 article; construction then expected 2018) — https://www.dnainfo.com/new-york/20171031/cypress-hills/chestnut-commons-affordable-housing-hpd-latest-news
- NYC Comptroller field audit of NYCHA building doors (report FK23-069S, Sept 21 2022; observations Aug 30–Sept 8 2022, 262 developments): "40.1% of entrance door locks were broken", "28.5% of rear or side door locks were broken"; residents said doors were propped because "intercoms, locks, keys, and door release buttons do not work"; one resident said intercoms "have been broken for 10 years"; repaired intercoms "were soon broken again"; no borough or Cypress Hills breakdown — https://comptroller.nyc.gov/reports/observations-of-building-doors-in-nycha-developments
- NYC 311: "Doorbells, buzzers, or intercoms that are broken or missing" is a listed apartment and public-area maintenance complaint; 311 advises trying to resolve with the owner, managing agent or super first; owners "must keep apartment units and buildings in livable condition" — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- HPD self-closing doors: "Apartment doors and hallway doors are required by law to swing closed and latch by themselves"; owners must "make prompt repairs to door closing mechanisms or defective doors and door frames"; under Local Law 71 of 2022 HPD must "annually select 300 class A multiple dwellings for proactive inspections of self-closing doors"; inspectors check public areas incl. "building entrance" — https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page
- No NYC Landmarks Preservation Commission historic district found in Cypress Hills; the 2023 State/National Register nomination was the former English Evangelical Lutheran Church of the Reformation, 105 Barbey Street (1908, Gothic Revival); Brownstoner notes National Register listing, unlike local landmarking, brings no regulatory oversight over private owners — https://www.brownstoner.com/architecture/national-register-nominations-new-york-state-2023-cypress-hills
- Brooklyn owner forum: three-unit house whose buzzer works only sporadically in every unit; vendor quoted $2,000 to replace (no electrical work included) and said troubleshooting would cost about the same at "$150 per hour for the technicians, a minimum of 3 hours"; owner hoped for "a repair bill for a few hundred bucks"; no replies — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Brooklyn three-family owner asking for an installer: "Nothing fancy just a buzzer and intercom in each unit- no automated door openers or anything like that"; reply recommended Aiphone, which "will design the system for you for free" — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- ButterflyMX explainer: a buzzer system = "the entry panel and directory, resident endpoints, communication wiring or network service" plus power supply, controller/relay and electric locking hardware; the call path and release path are separate circuits; the relay releases the lock for a set interval and "does not physically open the door" — https://butterflymx.com/blog/apartment-buzzer/
- Area parcel/permit/311 counts for intercom violations in 11207/11208: EMPTY (NYC Open Data API not reachable).
- Local news story specifically about a Cypress Hills buzzer/intercom: EMPTY (searches returned Brownsville Houses, Bed-Stuy, Flatbush stories only).
- Yelp complaints about buzzer installers near Cypress Hills: EMPTY.

### Questions people ask — Door Buzzer Installation in Cypress Hills
- Google PAA / PASF / AnswerThePublic / Bing / DuckDuckGo for "door buzzer installation Cypress Hills": EMPTY (not accessible).
- Is $2,000 a reasonable price to install a new buzzer/intercom in a three-unit house? — Brownstoner forum — https://www.brownstoner.com/forum/general-discussion/2000-reasonable-estimate-to-install-new-3-unit-buzzer-entry-intercom-system
- Who sells and installs a simple buzzer and intercom in each unit of a three-family? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Why does my apartment buzzer keep buzzing? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Who is responsible for fixing a broken apartment buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Can a renter add smart control to an existing buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- How can a property reduce buzzer bombing? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Should the owners redo the whole intercom system when the entrance intercom doesn't work? — openigloo tenant review, 2 Elton St — https://www.openigloo.com/building/nyc/3086534-3039080010/brooklyn-cypress-hills-2-elton-street-11208
- How do I report broken or missing doorbells, buzzers or intercoms? — 311 — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Reddit (r/Brooklyn, r/AskNYC) threads about buzzers in Cypress Hills: EMPTY.

## Crown Heights, Brooklyn — /door-buzzer-installation-crown-heights-brooklyn-ny (factory research, 2026-11-11)

- 501 Lefferts Ave, Crown Heights (60-unit complex near Lamont Court): tenants rallied June 1, 2022 over "defective locks on doors to access the rest of the building"; tenant Lakeysha Harris-Godwin: "That front door is not secured properly."; another tenant: "They might change the lock, but the frame, they can kick it [open]."; complex had 87 open HPD violations including broken locks; young people sometimes break the locks to hang out in the lobby/hallways; landlord sends locksmiths and a security guard per broken-door call — https://patch.com/new-york/prospectheights/faulty-lock-just-start-problems-lefferts-complex-tenants
- Same building: gunpoint robbery of a delivery worker May 7, 2022 renewed anger; "The front door lock, which tenants say is decades old, has had problems since at least 2018, according to building records." — https://new.patch.com/new-york/prospectheights/gunpoint-robbery-renews-bk-tenants-outrage-over-long-broken-locks
- 240 Crown St, Crown Heights (135-unit building per residents): News 12, Aug 14, 2025 — security video "appears to show a man using a small child in a stroller to get someone to open the door for him," then he took a package from the lobby (entry by someone opening the door, not forced) — https://brooklyn.news12.com/man-appears-to-use-child-in-a-stroller-to-get-inside-crown-heights-building-and-steal-package
- 529 Brooklyn Ave (between Maple and Midwood Sts), Dec 26, 2019: "the thief broke the glass front door of the building with a heavy object, gaining entry and stealing a package." — https://crownheights.info/crime/692200/door-breaking-package-thief-strikes-again
- 456 Brooklyn Ave, Jan 2022: two thieves entered the lobby and took packages, escaped on electric bikes; article does not say how they got in — https://crownheights.info/crime/757989/package-thief-crew-clear-out-crown-heights-building-escape-on-electric-bikes
- r/crownheights thread titles (excerpts only): "package theft in large pre-war buildings ... random people buzz into our building and take packages" — https://www.reddit.com/r/crownheights/comments/1txm4uq/package_theft_in_large_prewar_buildings/
- LPC Permit Guidebook ch. 11: "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening."; "An intercom can also be installed on a fence or wall in front of the entranceway."; "A maximum of two light fixtures and one intercom panel can be installed per door opening."; design/size/finish "compatible with the architecture"; equipment attached at mortar joints, plain masonry, wood or metalwork, not through cast iron or decorative surfaces; conduit concealed through plain masonry, else staff may approve "a maximum of approximately ten inches of visible conduit", painted to match; staff-level permits available. Chapter does not cover keypads or card readers — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- LPC permits on Crown Heights North district houses show the routine permit path (e.g. 926 St Marks Ave, CHN HD III, stoop/areaway/gate metalwork repair, issued 10/23/2020; 1219 Dean St, CHN HD, rear work, issued 06/10/2024) — https://s-media.nyc.gov/agencies/lpc/Permits/PermitFiles/PMW-20-10621.pdf ; https://s-media.nyc.gov/agencies/lpc/Permits/PermitFiles/CNE-24-11201.pdf
- 311 lists "Doorbells, buzzers, or intercoms that are broken or missing" as both an apartment and a public-area maintenance complaint, and "Doors and locks that are broken or missing or not self-closing" — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Habitat Magazine, Feb 26, 2024, "A Working Intercom Isn't an Amenity. It's Required by Law.": MDL — buildings built/converted after 1968 with eight or more units must provide two-way voice intercom; courts treat intercoms as an essential service; options include a 311 complaint or HP proceeding; Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom," — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground (Dec 18, 2014): pre-1968 buildings must add self-locking doors and intercoms if requested by a majority of tenants; one renter reported waiting three months for an inspector after a 311 intercom complaint; costs quoted by an installer $2,000–$50,000; NYT figure about $500 per apartment for video in large buildings — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- Atlantic Avenue Mixed-Use Plan approved by City Council May 28, 2025: rezones 21 blocks of Atlantic Avenue and neighboring streets in Crown Heights and Bed-Stuy for 4,600 apartments incl. about 1,900 permanently affordable; "Since the 1960s, this area has been zoned for one- to two-story industrial buildings" — https://www.6sqft.com/4600-new-homes-coming-to-bed-stuy-and-crown-heights-after-nyc-council-approves-atlantic-ave-rezoning/
- Ebbets Field Apartments (Bedford Ave / Sullivan Pl): "The complex served as a home to 1,317 families."; "It was the largest state-subsidized housing complex in the five boroughs at that time." completed ~1962 — https://patch.com/new-york/new-york-city/history-ebbets-field-apartments-complex
- Crown Heights tenant-conditions stories without entry details (not usable for buzzers): 567 St Johns Pl (Jan 2024, 446 violations), 1933 Union St (Jun 2026, elevator/gas), 1193 Eastern Pkwy (Jul 2021) — https://www.brownstoner.com/real-estate-market/crown-heights-tenants-building-repairs-567-st-johns-place/ ; https://www.brownstoner.com/real-estate-market/crown-heights-tenants-sue-landlord-1833-union-street/ ; https://cbsnews.com/newyork/news/residents-of-crown-heights-apartment-building-protest-what-they-call-deplorable-conditions
- Brownstoner forum (Oct 28, 2010): tenant told landlord is replacing buzzers with a phone-dialing system; worried about needing a landline; replies: such systems can call several numbers; landline not strictly required — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- Brownstoner forum (Sep 14, 2009, Park Slope): one tenant refused the electrician, so the whole line's intercom stayed dead for months; lobby door propped — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Brownstoner forum: owner of a 3-family brownstone wants buzzer + intercom in each unit; reply: call the manufacturer for a free system design — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- HPD/311 open-data counts of intercom violations for 11213/11216/11225/11233/11238: EMPTY (Open Data API not reachable from here)
- Google PAA / PASF / Answer the Public / AI Overview: EMPTY
- Bing / DuckDuckGo: EMPTY
- Yelp 1–3★ for Crown Heights intercom/buzzer installers: EMPTY

### Questions people ask — Door Buzzer Installation in Crown Heights
- My building's front door lock keeps getting broken and replaced, but the frame is weak. Will a new buzzer fix that? — Reddit/news (tenants at 501 Lefferts Ave, Patch) — https://patch.com/new-york/prospectheights/faulty-lock-just-start-problems-lefferts-complex-tenants
- How do package thieves get into buildings with a buzzer, and what stops someone being let in by a neighbor? — Reddit / News 12 — https://www.reddit.com/r/crownheights/comments/1txm4uq/package_theft_in_large_prewar_buildings/ ; https://brooklyn.news12.com/man-appears-to-use-child-in-a-stroller-to-get-inside-crown-heights-building-and-steal-package
- Can a glass front door take a buzzer, and what if it gets smashed? — news (529 Brooklyn Ave) — https://crownheights.info/crime/692200/door-breaking-package-thief-strikes-again
- How many intercom panels can a landmarked house have, and where can it go? — LPC guidance — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Can the panel go on the areaway fence instead of the house? — LPC guidance — same URL
- Can a landlord replace the buzzer with a system that calls tenants' phones, and do I need a landline? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- One tenant won't allow access and the whole line is dead — what now? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Who designs an intercom for a three-family brownstone with a buzzer in each unit? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- How long does a 311 intercom complaint take, and is the landlord required to fix it? — Brick Underground / Habitat — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- What does a new building under the Atlantic Avenue rezoning need for entry? — news — https://www.6sqft.com/4600-new-homes-coming-to-bed-stuy-and-crown-heights-after-nyc-council-approves-atlantic-ave-rezoning/
- PAA / PASF / Answer the Public / Bing / DuckDuckGo / Yelp questions: EMPTY

## Ditmas Park, Brooklyn — /door-buzzer-installation-ditmas-park-brooklyn-ny (factory research, 2026-11-11)

- 570 Westminster Road (Ditmas Park/Flatbush, 11230): 185 units, 6 floors, built 1935, managed by Narrows Management; tenant review cons: "Buzzers and intercoms don't work."; advice to owners: "Fix elevator, buzzers/intercoms, and washing machines."; pros list "24 hour door person" / "Reasonably reliable door people." — https://www.openigloo.com/building/nyc/3120093-3051970040/brooklyn-flatbush-570-westminster-road-11230
- 770 Ocean Avenue (Ditmas Park, 11226): 41 units, 6 floors, built 1923, rent-stabilized, 47 open violations, 6 litigation cases; tenant review: "the people who don't live in here vandalizing our building because they don't respect it." — https://openigloo.com/building/nyc/3118532-3051500021/brooklyn-ditmas-park-770-ocean-avenue-11226
- 1250 Ocean Avenue (11230): 106 units, 6 floors, built 1953 (post-war six-storey stock on Ocean Avenue) — https://openigloo.com/building/nyc/3179161-3066940055/brooklyn-flatbush-1250-ocean-avenue-11230
- 377 Argyle Road (11218): 16 units, 4 floors, built 1925 (small pre-war walk-up on a Ditmas Park side street); review: "Hallways ARE ALWAYS DIRTY, Light in Hallways is DULL." — https://www.openigloo.com/building/nyc/3118670-3051560066/brooklyn-flatbush-377-argyle-road-11218
- Bklyner, Nov 20 2018 (Zainab Iqbal), "A thief or bad postal service? Packages are missing in Ditmas Park": a building near Cortelyou Road and Stratford Road reported over 100 packages missing in six months; resident Eddie Shiomi kept a spreadsheet ("In the month of August, it exploded"); dummy packages left in the lobby disappeared the next day; packages "left downstairs by the mailboxes or in the lobby"; management installed a camera in the mail area after residents pressed; a Kensington resident: "We do not have a camera and about 40% of the time the lock on the front door is broken."; a private-home resident: packages left "on the front stoop in the middle of the day so they're sitting ducks"; NYPD said no police reports had been filed — https://bklyner.com/a-thief-or-bad-postal-service-packages-are-missing-in-ditmas-park
- Patch Ditmas Park, Feb 12 2013: 70th Precinct outreach on a property-crime spike; "the front or back door is the most common point of entry for a burglar"; burglaries via fire escapes and unlocked side/rear windows; "Cancel or postpone deliveries until you return home." — https://patch.com/new-york/ditmaspark/70th-precinct-offers-safety-tips-to-offset-property-crime-spike
- LPC Permit Guidebook ch. 11 (Health & Safety): "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening"; intercom may go on a fence or wall in front of the entranceway; "A maximum of two light fixtures and one intercom panel can be installed per door opening"; "Design, size, and finish of installations must be compatible with the architecture of the building"; "Staff can issue permits approving light fixtures and intercom panels" if criteria met; manufacturer cut sheets required; in-kind intercom replacement does not need elevation/large-scale drawings; cameras: no more than two per 25 ft of frontage on small residential buildings; conduit concealed through plain masonry or cladding, otherwise "a maximum of approximately ten inches of visible conduit", painted to match; equipment "must not be attached through cast iron or on any decorative surfaces" — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Brooklyn CB14 FY2027 Statement of Needs (Housing & Land Use): housing code violations per 1,000 units "506 in 2010, 667 in 2019 and 879 in 2024"; "280/1000 are serious housing code violations"; "CB14 ranks 12th (up from 18th) of 59 community districts"; "Only 20% of renter occupied homes are adequately maintained by landlords"; "over 48% of the area of the district is comprised of 1-2 family homes"; asks for "more DOB action on illegal conversions in what would be single family homes"; Prospect Park South, Ditmas Park and Midwood Park-Fiske Terrace "comprise 6% of lots in the district" — https://cb14brooklyn.com/wp-content/uploads/2026/07/FY2027_Statement-of-Community-District-Needs-and-CB-Requests_BK14_Housing-and-Land-Use.pdf
- HPD Clear Violations page: Class A 90 days, Class B 30 days, Class C 24 hours from service; Class C self-closing doors 14 days; certification of correction is free; "HPD may audit any certification of correction"; false certification keeps the violation open — https://www.nyc.gov/site/hpd/services-and-information/clear-violations.page
- City Limits, Oct 16 2024: housing code violations citywide rose 24% in FY2024 (722,597 to 895,457); Class B "hazardous", Class C "immediately hazardous" — https://citylimits.org/2024/10/16/housing-violations-in-nyc-jumped-24-this-year-we-mapped-them-by-neighborhood/
- NYC 311 (KA-01074): broken or missing "Doorbells, buzzers, or intercoms" are filed as apartment or public-area maintenance complaints; HPD contacts the managing agent and warns a violation may be issued, calls the tenant back, sends an inspector if not fixed; owner is not told the inspection date — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Habitat Magazine, Feb 2024: a working intercom "isn't just a convenience ... it's a legal requirement"; post-1968 buildings with eight or more units "must have a two-way voice intercom system linking the front door to each apartment"; co-op "has a legal obligation to repair or replace the intercom" (Nancy Kourland, Lasser Law Group); a neighbor whose contractor damages the line "may be responsible for the repair, depending on the lease terms or the alteration agreement" — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Habitat Board Talk (Oct 2019–Jan 2021): co-op board asking whether in-unit panels can be billed to shareholders or need an assessment; reply: "the repairs and ongoing maintenance is a building responsibility" once upgrades are part of the building system; vendor quoting $49.99/month — https://habitatmag.com/Board-Talk/Co-op-Intercom-System-Upgrade
- Brick Underground, Nov 7 2019: "It's all in the wire connections" (Daniel Vasquez, Paragon); "the need for a total system overhaul is unlikely"; replacement about one day for a five-apartment building, about two days for 100 units; repair quotes "$195 an hour and $250 an hour plus parts" — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Brick Underground, Dec 18 2014: buildings with at least eight apartments need a self-closing, self-locking door and intercom; pre-1968 buildings "if requested by a majority of tenants"; a renter waited three months for a 311 inspector; landlord "could be held liable" if a crime follows a broken buzzer (NY AG guide) — https://www.brickunderground.com/blog/2014/12/broken_buzzers
- Brownstoner forum, Sep 14 2009: 12-apartment brownstone where one tenant refused entry for her new station and the whole line stayed dead; "Tenent sometimes have to leave lobby door open for deliveries" — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- ButterflyMX small-building guide: "Repair makes sense for a localized, serviceable fault"; "Do not replace a system based on age alone"; wiring reuse "cannot be confirmed from a photo, the age of the building, or the look of a wall station"; "A building-wide outage may indicate a shared power or control problem" — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- ButterflyMX apartment buzzer guide: "The relay is the electrical control point; it doesn't physically swing the door open."; "A wired system isn't automatically outdated, and a wireless system isn't free of wiring." — https://butterflymx.com/blog/apartment-buzzer/
- Brownstoner, May 21 2019: 551 Rugby Road, "one of three units in what was originally a two-family Edwardian home", fronted by "two tiers of columned porches" (houses divided into condos) — https://www.brownstoner.com/real-estate-market/condo-co-op-of-the-day/brooklyn-condos-for-sale-ditmas-park-551-rugby-road-garage-porch/
- Bing/DuckDuckGo, Google PAA/PASF, Answer the Public, Yelp: EMPTY
- Reddit threads specific to door buzzers in Ditmas Park: EMPTY

### Questions people ask — Door Buzzer Installation in Ditmas Park
- Why does my apartment buzzer keep buzzing? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Who is responsible for fixing a broken apartment buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Can a renter add smart control to an existing buzzer? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- How can a property reduce buzzer bombing? — ButterflyMX FAQ — https://butterflymx.com/blog/apartment-buzzer/
- Can only the apartment stations be replaced? — ButterflyMX FAQ — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- What should an owner gather before requesting a quote? — ButterflyMX FAQ — https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/
- Packages keep vanishing from our lobby by the mailboxes; does fixing the front door help? — Bklyner (residents) — https://bklyner.com/a-thief-or-bad-postal-service-packages-are-missing-in-ditmas-park
- Buzzers and intercoms don't work in our six-storey building; what do we tell the owner? — openigloo review — https://www.openigloo.com/building/nyc/3120093-3051970040/brooklyn-flatbush-570-westminster-road-11230
- How do I report a broken buzzer or intercom to the city, and what happens next? — 311 — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Is a co-op responsible for a dead intercom? — Habitat — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Can a co-op bill shareholders for new apartment panels? — Habitat Board Talk — https://habitatmag.com/Board-Talk/Co-op-Intercom-System-Upgrade
- How long does a building intercom replacement take? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Does the landmark district need to approve an intercom panel on our house? — LPC guidebook — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- How many violations does HPD give an owner to fix, and how fast? — HPD — https://www.nyc.gov/site/hpd/services-and-information/clear-violations.page

## Downtown Brooklyn, Brooklyn — /door-buzzer-installation-downtown-brooklyn-ny (factory research, 2026-11-11)

- The Bowen, 289 Schermerhorn Street: a "1925 brick office building" converted into a "71-residence boutique condominium"; "The transformation more than doubles the building's original height"; amenities listed are a residents' lounge, children's playroom and roof deck; no lobby/intercom details given (Untapped Cities, published Nov 4 2026) — https://www.untappedcities.com/the-bowen/
- 141 Willoughby Street: "The vacant 24-story building will feature 200 rental apartments"; office building finished in 2023 (developer Savanna); floors two through seven stay as offices (about 110,000 sq ft); 25 percent of the apartments affordable; "work scheduled to begin in 2026" (Commercial Observer, Aug 11 2025) — https://commercialobserver.com/2025/08/capstone-bh3-141-willoughby-street-conversion/
- Capstone Equities filed plans for a 233-unit conversion in Downtown Brooklyn, photo captioned 141 Willoughby Street (PincusCo, Dec 5 2025; body paywalled, address tie not confirmed) — https://www.pincusco.com/capstone-equities-files-plans-for-233-unit-conversion-in-dobro/
- 89 DeKalb Avenue (RXR with LIU): 30-story, 324-unit residential and academic tower on the LIU campus; 98 middle-income lottery units; first residents fall 2025; amenities list has no doorman/intercom detail (6sqft, July 14 2025) — https://www.6sqft.com/98-apartments-available-at-all-electric-downtown-brooklyn-tower-from-3000-month/
- RXR on 89 DeKalb: separate traffic flows for LIU's pharmacy school and the residences; quote: "The students are protected from the residents and vice versa." — Rebecca D'Eloia, EVP and project executive for development, RXR; resident app ("It's all controlled from the resident's app" — about smart windows); 24-hour concierge; nearby first phase The Willoughby, 476 units, 34 stories, completed 2021 (Mann Report, Sept 4 2024) — https://www.mannpublications.com/mannreport/2024/09/04/rxr-using-tech-to-build-the-future-of-building/
- Concord Village, 175 Adams Street: built 1950, 17 floors, 146 apartments, "FT Doorman", "Security guards" listed; other Concord Village addresses 195, 215, 225, 235 Adams Street (CityRealty) — https://www.cityrealty.com/nyc/downtown-brooklyn/concord-village-175-adams-street/38722
- The Addison, a 26-story Downtown Brooklyn rental: tenants (Michelle Beatty) say "even getting in and out of the building has become a daily challenge" because of elevator breakdowns; no intercom content (News 12, June 2 2026) — https://connecticut.news12.com/2026/06/02/tenants-in-downtown-brooklyn-luxury-building-demand-answers-over-elevator-issues-discolored-water/4VWqcuU4XDxZf5UNPAhuit
- NYC Tenant Data Privacy Law (Local Law 63 of 2021): owners of multiple dwellings using smart access systems must give tenants a data retention and privacy policy; express consent in writing or through a mobile application; only minimum data (name, unit and doors, contact method, credential IDs, lease dates, time and method of access "solely for security purposes"); authentication data destroyed "no later than 90 days" unless anonymized; may not "require use of a smart access system to gain entry to the tenant's dwelling unit"; no location tracking outside buildings; private right of action for unlawful sale of data (HPD) — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Habitat Magazine, Feb 26 2024 "A Working Intercom Isn't an Amenity. It's Required by Law": MDL — buildings built or converted after 1968 with eight or more units need a two-way voice intercom; courts treat intercoms as an essential service under the warranty of habitability; remedies 311 or an HP proceeding; 54-unit West Village co-op without intercom since 2019; quote: "As a result, the co-op has a legal obligation to repair or replace the intercom," — Nancy Kourland, Lasser Law Group — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Habitat Magazine, May 9 2017 "For Door Buzzers, the Future Has Arrived": three intercom categories (hard-wired, telephone-based needing a dedicated line with no video, smartphone-based needing internet); smartphone systems often need internet cabling at the entrance; ButterflyMX then $5,000–$7,000 installed plus $2.50 per unit per month (dated figures); virtual doorman about $15,000 a year for a 28-unit building (Nicholas Silvers, Tavros Capital); quote: "A lot of our calls now are people who want to abandon the hard-wired intercom units in their apartments." — Dan Arnold, Academy Mailbox — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- Brick Underground, Nov 7 2019 intercom guide: repairs usually at the lobby base, apartment station, door strike or power supply; "the core wiring is typically fine" (Daniel Vasquez, Paragon Security and Locksmith); five-apartment building replaced in one day, 100-unit building about two days (Pete Carmello, Lock and Tech); "Now everyone wants more security. They want a camera to see in front of the door before allowing someone in." (Vasquez); tenants need building authorization before any repair — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- ButterflyMX elevator guide: after approval "the entrance door can be unlocked and elevator access can be enabled based on the building's rules"; visitors limited to approved floors via floor access readers; the intercom "does not replace the elevator system"; review with installer, elevator contractor and local officials — https://butterflymx.com/blog/video-intercom-with-elevator-floor-access-for-apartment-buildings/
- StreetEasy Talk "new building intercom" (condo replacing an older intercom, asking about ButterflyMX): concern about "ongoing subscription-type costs" and the need for internet service in the lobby; a 12-unit building rejected a phone-only system because "needing to use your phone to buzz the door was not viable" (no wall screen option) — https://streeteasy.com/talk/discussion/45067-new-building-intercom
- 100 Willoughby Street, 11201 (Downtown Brooklyn): openigloo shows 40 reviews, 4.6 average; no entry-related text retrievable — https://www.openigloo.com/building/nyc/3424451-3001457502/brooklyn-dumbo-100-willoughby-street-11201 (not used on page)
- 311 / HPD Open Data pull for BELL/BUZZER/INTERCOM in 11201 and 11217: EMPTY (data.cityofnewyork.us not reachable from the research session)
- DOB permits, LPC rules specific to Downtown Brooklyn entry hardware: EMPTY beyond the silo LPC guidance (Borough Hall Skyscraper Historic District search returned no fetchable designation details)
- Local news on Downtown Brooklyn lobby intrusions / buzzer failures: EMPTY (search budget exhausted before results)
- Google PAA, PASF, Answer the Public, Bing, DuckDuckGo, Yelp 1–3★ for "door buzzer installation Downtown Brooklyn": EMPTY (not accessible)

### Questions people ask — Door Buzzer Installation in Downtown Brooklyn
- Is a ButterflyMX-type system good or bad for a condo replacing an older intercom? — StreetEasy Talk — https://streeteasy.com/talk/discussion/45067-new-building-intercom
- Does an app-based intercom carry ongoing subscription costs, and does the lobby need its own internet service? — StreetEasy Talk — https://streeteasy.com/talk/discussion/45067-new-building-intercom
- Is a phone-only system workable if residents want a screen on the wall? — StreetEasy Talk — https://streeteasy.com/talk/discussion/45067-new-building-intercom
- Our co-op has had no intercom for years; is the board obliged to repair or replace it, and what if a neighbor's renovation broke it? — Habitat Magazine reader question — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Can a tenant arrange the intercom repair, or does the building have to authorize it? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- How long does it take to replace an intercom in a 5-unit vs a 100-unit building? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Can a video intercom also control which elevator floors a visitor reaches? — ButterflyMX guide — https://butterflymx.com/blog/video-intercom-with-elevator-floor-access-for-apartment-buildings/
- What data can a keyless or app entry system keep on tenants and guests, and for how long? — HPD Tenant Data Privacy Law page — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Can a landlord require an app or fob to open my apartment door? — HPD Tenant Data Privacy Law page — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Should we choose hard-wired, telephone-based or smartphone-based entry? — Habitat Magazine — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- What does a virtual doorman cost compared with a buzzer system? — Habitat Magazine — https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-May/The-New-Buzzer
- How can a mixed building keep students or office users and residents on separate entries? — Mann Report (RXR, 89 DeKalb) — https://www.mannpublications.com/mannreport/2024/09/04/rxr-using-tech-to-build-the-future-of-building/
- PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Reddit (Downtown-specific) / Yelp — EMPTY

## Crown Heights, Brooklyn — /door-buzzer-installation-crown-heights-brooklyn-ny (factory research, 2026-11-11)

- 501 Lefferts Ave, Crown Heights (60-unit complex near Lamont Court): tenants rallied June 1, 2022 over "defective locks on doors to access the rest of the building"; tenant Lakeysha Harris-Godwin: "That front door is not secured properly."; another tenant: "They might change the lock, but the frame, they can kick it [open]."; complex had 87 open HPD violations including broken locks; young people sometimes break the locks to hang out in the lobby/hallways; landlord sends locksmiths and a security guard per broken-door call — https://patch.com/new-york/prospectheights/faulty-lock-just-start-problems-lefferts-complex-tenants
- Same building: gunpoint robbery of a delivery worker May 7, 2022 renewed anger; "The front door lock, which tenants say is decades old, has had problems since at least 2018, according to building records." — https://new.patch.com/new-york/prospectheights/gunpoint-robbery-renews-bk-tenants-outrage-over-long-broken-locks
- 240 Crown St, Crown Heights (135-unit building per residents): News 12, Aug 14, 2025 — security video "appears to show a man using a small child in a stroller to get someone to open the door for him," then he took a package from the lobby (entry by someone opening the door, not forced) — https://brooklyn.news12.com/man-appears-to-use-child-in-a-stroller-to-get-inside-crown-heights-building-and-steal-package
- 529 Brooklyn Ave (between Maple and Midwood Sts), Dec 26, 2019: "the thief broke the glass front door of the building with a heavy object, gaining entry and stealing a package." — https://crownheights.info/crime/692200/door-breaking-package-thief-strikes-again
- 456 Brooklyn Ave, Jan 2022: two thieves entered the lobby and took packages, escaped on electric bikes; article does not say how they got in — https://crownheights.info/crime/757989/package-thief-crew-clear-out-crown-heights-building-escape-on-electric-bikes
- r/crownheights thread titles (excerpts only): "package theft in large pre-war buildings ... random people buzz into our building and take packages" — https://www.reddit.com/r/crownheights/comments/1txm4uq/package_theft_in_large_prewar_buildings/
- LPC Permit Guidebook ch. 11: "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening."; "An intercom can also be installed on a fence or wall in front of the entranceway."; "A maximum of two light fixtures and one intercom panel can be installed per door opening."; design/size/finish "compatible with the architecture"; equipment attached at mortar joints, plain masonry, wood or metalwork, not through cast iron or decorative surfaces; conduit concealed through plain masonry, else staff may approve "a maximum of approximately ten inches of visible conduit", painted to match; staff-level permits available. Chapter does not cover keypads or card readers — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- LPC permits on Crown Heights North district houses show the routine permit path (e.g. 926 St Marks Ave, CHN HD III, stoop/areaway/gate metalwork repair, issued 10/23/2020; 1219 Dean St, CHN HD, rear work, issued 06/10/2024) — https://s-media.nyc.gov/agencies/lpc/Permits/PermitFiles/PMW-20-10621.pdf ; https://s-media.nyc.gov/agencies/lpc/Permits/PermitFiles/CNE-24-11201.pdf
- 311 lists "Doorbells, buzzers, or intercoms that are broken or missing" as both an apartment and a public-area maintenance complaint, and "Doors and locks that are broken or missing or not self-closing" — https://portal.311.nyc.gov/article/?kanumber=KA-01074
- Habitat Magazine, Feb 26, 2024, "A Working Intercom Isn't an Amenity. It's Required by Law.": MDL — buildings built/converted after 1968 with eight or more units must provide two-way voice intercom; courts treat intercoms as an essential service; options include a 311 complaint or HP proceeding; Nancy Kourland (Lasser Law Group): "As a result, the co-op has a legal obligation to repair or replace the intercom," — https://habitatmag.com/Publication-Content/Building-Operations/2024/February-2024/A-Working-Intercom-Isn-t-an-Amenity.-It-s-Required-by-Law
- Brick Underground (Dec 18, 2014): pre-1968 buildings must add self-locking doors and intercoms if requested by a majority of tenants; one renter reported waiting three months for an inspector after a 311 intercom complaint; costs quoted by an installer $2,000–$50,000; NYT figure about $500 per apartment for video in large buildings — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- Atlantic Avenue Mixed-Use Plan approved by City Council May 28, 2025: rezones 21 blocks of Atlantic Avenue and neighboring streets in Crown Heights and Bed-Stuy for 4,600 apartments incl. about 1,900 permanently affordable; "Since the 1960s, this area has been zoned for one- to two-story industrial buildings" — https://www.6sqft.com/4600-new-homes-coming-to-bed-stuy-and-crown-heights-after-nyc-council-approves-atlantic-ave-rezoning/
- Ebbets Field Apartments (Bedford Ave / Sullivan Pl): "The complex served as a home to 1,317 families."; "It was the largest state-subsidized housing complex in the five boroughs at that time." completed ~1962 — https://patch.com/new-york/new-york-city/history-ebbets-field-apartments-complex
- Crown Heights tenant-conditions stories without entry details (not usable for buzzers): 567 St Johns Pl (Jan 2024, 446 violations), 1933 Union St (Jun 2026, elevator/gas), 1193 Eastern Pkwy (Jul 2021) — https://www.brownstoner.com/real-estate-market/crown-heights-tenants-building-repairs-567-st-johns-place/ ; https://www.brownstoner.com/real-estate-market/crown-heights-tenants-sue-landlord-1833-union-street/ ; https://cbsnews.com/newyork/news/residents-of-crown-heights-apartment-building-protest-what-they-call-deplorable-conditions
- Brownstoner forum (Oct 28, 2010): tenant told landlord is replacing buzzers with a phone-dialing system; worried about needing a landline; replies: such systems can call several numbers; landline not strictly required — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- Brownstoner forum (Sep 14, 2009, Park Slope): one tenant refused the electrician, so the whole line's intercom stayed dead for months; lobby door propped — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Brownstoner forum: owner of a 3-family brownstone wants buzzer + intercom in each unit; reply: call the manufacturer for a free system design — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- Amazon Key for Business (AP, Jul 22, 2021): device installed on building buzzers for free, sometimes with a $100 gift card to whoever lets them in; drivers "can unlock doors only when they have a package in hand to scan"; "Tenants may not know that Amazon drivers have access to their building's front doors."; Ashkan Soltani: "You're essentially introducing a foreign internet-connected device into an otherwise internal network," — https://abcnews4.com/news/nation-world/amazons-mission-getting-a-key-to-your-apartment-building
- ABC7, Nov 5, 2024: man broke into a street-corner mailbox near Kingston Avenue and Carroll Street, took two bags of mail about 30 seconds after a USPS truck left; resident Anna Shaw: "It makes me feel very unsafe," — https://abc7ny.com/post/brooklyn-mail-theft-crime-caught-surveillance-video-leaves-crown-heights-community-edge/15513379/
- HPD/311 open-data counts of intercom violations for 11213/11216/11225/11233/11238: EMPTY (Open Data API not reachable from here)
- Google PAA / PASF / Answer the Public / AI Overview: EMPTY
- Bing / DuckDuckGo: EMPTY
- Yelp 1–3★ for Crown Heights intercom/buzzer installers: EMPTY

### Questions people ask — Door Buzzer Installation in Crown Heights
- My building's front door lock keeps getting broken and replaced, but the frame is weak. Will a new buzzer fix that? — Reddit/news (tenants at 501 Lefferts Ave, Patch) — https://patch.com/new-york/prospectheights/faulty-lock-just-start-problems-lefferts-complex-tenants
- How do package thieves get into buildings with a buzzer, and what stops someone being let in by a neighbor? — Reddit / News 12 — https://www.reddit.com/r/crownheights/comments/1txm4uq/package_theft_in_large_prewar_buildings/ ; https://brooklyn.news12.com/man-appears-to-use-child-in-a-stroller-to-get-inside-crown-heights-building-and-steal-package
- Can a glass front door take a buzzer, and what if it gets smashed? — news (529 Brooklyn Ave) — https://crownheights.info/crime/692200/door-breaking-package-thief-strikes-again
- How many intercom panels can a landmarked house have, and where can it go? — LPC guidance — https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf
- Can the panel go on the areaway fence instead of the house? — LPC guidance — same URL
- Can a landlord replace the buzzer with a system that calls tenants' phones, and do I need a landline? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2010/10/landlord-instal
- One tenant won't allow access and the whole line is dead — what now? — Brownstoner forum — https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2
- Who designs an intercom for a three-family brownstone with a buzzer in each unit? — Brownstoner forum — https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family
- How long does a 311 intercom complaint take, and is the landlord required to fix it? — Brick Underground / Habitat — https://new.brickunderground.com/rent/get-your-landlord-to-fix-that-broken-buzzer
- What does a new building under the Atlantic Avenue rezoning need for entry? — news — https://www.6sqft.com/4600-new-homes-coming-to-bed-stuy-and-crown-heights-after-nyc-council-approves-atlantic-ave-rezoning/
- PAA / PASF / Answer the Public / Bing / DuckDuckGo / Yelp questions: EMPTY

## East Williamsburg, Brooklyn — /door-buzzer-installation-east-williamsburg-brooklyn-ny (factory research, 2026-11-11)

Note: the live web-search budget for this build was exhausted before any new search ran. Every finding below was already gathered and sourced in the silo and neighborhood research (city open data pulls of Nov 11 2026, statute texts, published guides). Live surfaces are marked EMPTY rather than filled.

- HPD violations dataset, NTA "East Williamsburg", violations whose text mentions an intercom, by inspection year: 2020 7; 2021 12; 2022 10; 2023 5; 2024 7; 2025 9; 2026 to Nov 11: 11. Peak years 2015 (14) and 2016 (14) — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- 2026 intercom violations in the East Williamsburg NTA sit on Kingsland Ave, Skillman Ave, Metropolitan Ave (four), Thames St, Seigel St ("inoperative intercom system at 1st story building entrance to panel"), Bushwick Ave, Stagg St and Grand St — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- Violation wording names where stations sit: kitchens (Union Ave, Beadel St, Maujer St), foyers, private hallways (Meserole St); entrance language such as "voice intercom with returned door buzzer system from the building's vestibule" (Graham Ave, 2022) — a new installation has to put a working station at each of those points — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- HPD self-closing door violations in the East Williamsburg NTA: 154 (2020), 176 (2021), 242 (2022), 341 (2023), 232 (2024), 321 (2025), 302 (2026 to Nov 11); of the 623 written since Jan 1 2025, 111 also mention a vestibule, building entrance, front entrance or street door. A buzzer release is only as good as the door closing and latching behind it — https://data.cityofnewyork.us/resource/wvxf-dwi5.json
- 311 BELL/BUZZER/INTERCOM complaints, Brooklyn Community Board 1: 79 (2020), 127 (2021), 101 (2022), 236 (2023), 192 (2024), 131 (2025), 153 (2026 to Nov 11) — https://data.cityofnewyork.us/resource/erm2-nwe9.json
- Of the 153 CB1 complaints in 2026: 52 closed because the inspector could not gain access, 32 closed with no violation found, 21 closed with violations issued, 17 still open — https://data.cityofnewyork.us/resource/erm2-nwe9.json
- NY Multiple Dwelling Law §50-a: Class A multiple dwellings erected or converted after Jan 1 1968 with eight or more apartments must have a self-locking main entrance door and an intercommunication system allowing voice communication and remote release; older buildings must install one if tenants of a majority of apartments request it in writing (start within 90 days, finish within six months) — https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a/
- ButterflyMX NYC guide: the statute "does not, by itself, require video, mobile access, or remote management"; HPD correction periods 90 days class A, 30 days class B, 24 hours most class C — https://butterflymx.com/blog/intercom-repair-nyc
- Brick Underground: replacing a building intercom takes about a day for five apartments and about two days for 100 units; Lee Dan systems may be outdated while the core wiring is typically fine; don't work on the wiring yourself — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Aiphone GT Series: "Multi-tenant intercom system for new builds and retrofit projects", up to "5,000 Tenant stations", "offers the advantage of using existing wire and infrastructure"; Aiphone upgrade guide: "If the existing wires are in good condition, they can be reused" — https://www.aiphone.com/products/gt-series/
- Reddit r/accesscontrol on 2-wire upgrades: "This will allow you to keep the existing GT system, repair the damaged cable, and only upgrade those tenants that desire app connectivity" — https://www.reddit.com/r/accesscontrol/comments/1scfk1y/2wire_intercom_systems_to_replace_aiphone/
- Allegion: "Fail safe products are unlocked when power is removed"; "Fail secure products are locked when power is removed"; fire doors need fail-secure strikes; "Electromagnetic locks are only available fail safe" — https://us.allegion.com/en/resources/education/leading-the-industry/decoded/fail-safe-vs-fail-secure.html
- IBC sensor-release rules for electrically locked egress doors (mag locks): sensor on egress side, manual "PUSH TO EXIT" device 40–48 in above floor within 5 ft, unlock on fire alarm activation and loss of power — https://up.codes/s/sensor-release-of-electrically-locked-egress-doors
- HomeAdvisor: intercom installation "costs an average of $2,500", "between $1,500 and $15,000"; wireless $150–$1,500; hard-wired $1,000–$15,000; 1–2 hours per station — https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/
- Swiftlane: "$1,000 to $5,000 or more per entry door for modern IP or video systems"; software subscriptions "$5 to $15 per unit per month, or $30 to $100 per door per month" — https://swiftlane.com/blog/apartment-intercom-installation-cost/
- ButterflyMX: its intercom "requires no building wiring"; cellular call boxes need no Ethernet at the door — https://butterflymx.com/blog/apartment-call-box/
- 2010 ADA Standards 308: high forward reach 48 in maximum, low forward reach 15 in minimum; operable parts within those ranges — https://www.access-board.gov/ada/chapter/ch03/
- Openigloo review of 985 Metropolitan Ave (built 1920, 4 units, 3 floors): cons "Intercom system didn't work"; pros "Separate entrances" — https://www.openigloo.com/building/nyc/3070305-3029130051/brooklyn-east-williamsburg-985-metropolitan-avenue-11211
- News 12 (Dec 14 2022): Bushwick tenant says the building's doors won't latch — "There is no protection." — https://westchester.news12.com/there-is-no-protection-bushwick-tenant-says-buildings-doors-wont-latch-fears
- McKibbin Street lofts (248/255 McKibbin) were the subject of city illegal-hotel crackdowns in 2016–2017 (entry-code turnover matters in such buildings) — https://www.dnainfo.com/new-york/20160511/east-williamsburg/city-continues-crackdown-on-illegal-hotels-at-mckibbin-street-lofts
- Reddit threads from owners: "Affordable option to replace 6 unit building entry system"; a door buzzer/door locking system for a 4-unit apartment building — https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/
- DOB permits, LPC rules specific to buzzer installation in East Williamsburg: EMPTY
- Local news about buzzer installation in East Williamsburg: EMPTY
- Reddit threads specific to East Williamsburg buzzer installation: EMPTY
- Yelp reviews of buzzer installers mentioning East Williamsburg: EMPTY
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DuckDuckGo capture for this query: EMPTY; vendor-blog and cost-guide claims used instead

### Questions people ask — Door Buzzer Installation in East Williamsburg
- Can the existing buzzer wires be reused when a new system goes in? — Aiphone upgrade guide / ButterflyMX FAQ — https://www.aiphone.com/products/gt-series/
- Does an audio-only system satisfy the NYC intercom rule, or does it have to be video? — ButterflyMX FAQ — https://butterflymx.com/blog/intercom-repair-nyc
- How long does installing a new building buzzer system take? — Brick Underground — https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix
- Is there an affordable way to replace the entry system in a six-unit building? — Reddit r/accesscontrol — https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/
- What door buzzer and lock setup suits a four-unit building? — Reddit r/accesscontrol — https://www.reddit.com/r/accesscontrol/comments/1hyy23u/affordable_option_to_replace_6_unit_building/
- Can some tenants keep handsets while others get app answering? — Reddit r/accesscontrol — https://www.reddit.com/r/accesscontrol/comments/1scfk1y/2wire_intercom_systems_to_replace_aiphone/
- How much does an intercom installation cost? — HomeAdvisor — https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/
- Is a wireless or cellular call box a good idea for a building door? — ButterflyMX / Swiftlane — https://butterflymx.com/blog/apartment-call-box/
- Should the door strike be fail safe or fail secure? — Allegion — https://us.allegion.com/en/resources/education/leading-the-industry/decoded/fail-safe-vs-fail-secure.html
- Do tenants have to ask in writing before an older building must install an intercom? — MDL §50-a — https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a/
- Is there a monthly fee with a cloud intercom? — Swiftlane — https://swiftlane.com/blog/apartment-intercom-installation-cost/
- How high should the entry panel be mounted? — ADA Standards — https://www.access-board.gov/ada/chapter/ch03/

## Dyker Heights, Brooklyn — /door-buzzer-installation-dyker-heights-brooklyn-ny (factory research, 2026-11-11)

- Package theft from stoops and porches is a long-running Dyker Heights complaint: a Brooklyn Paper story (Aug 13 2019) describes a package thief who had "plagued her neighbors for nearly 20 years"; one package was taken from a stoop by 78th Street and 11th Avenue on July 27, 2019; she was arrested five times for petty larceny and trespassing in Dyker Heights and Bensonhurst in 2019 alone; resident quote: "My neighbors and I try to take in packages for each other so as to not have her come stealing, but it's hard sometimes"; another resident's surveillance cameras caught the thief taking packages off her porch — https://www.brooklynpaper.com/da-powerless-to-stop-notorious-dyker-heights-package-thief-residents-claim/
- Reddit r/Brooklyn thread "Beware: Dyker Heights Package stealer" (excerpt only): "There's a man going around the neighborhood stealing packages. He's seen with large tote bags and will swoop in to steal after it's delivered." — https://www.reddit.com/r/Brooklyn/comments/1ai4jqd/beware_dyker_heights_package_stealer/
- NYPD 68th Precinct covers Bay Ridge and Dyker Heights; Facebook Bay Ridge group post on 68th Precinct seeking a man stealing packages from porches (excerpt only) — https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/68th-precinct.page ; https://www.facebook.com/groups/bayRidgeTalk/posts/2797682493737037/
- NYU Furman Center, Bay Ridge/Dyker Heights (community district): 2024 homeownership rate 41.0% vs 32.7% citywide; 51,486 housing units (latest); 2025 sales volume 135 one-family, 168 two-to-four-family, 25 five-plus-family buildings, 57 condos; serious housing code violations 85.3 per 1,000 privately owned rental units (latest year) and total violations 291.0 per 1,000; public housing 0.0% of rental units; 2024 population 128,247, 22.3% Asian, 21.9% Hispanic — https://www.furmancenter.org/neighborhoods/bay-ridge-dyker-heights/
- New multi-unit buildings are being filed on Dyker Heights lots: 1302 83rd Street — three-story residential, 11 residences, cellar, eight open parking spaces, 33 ft, filed by WNS Development LLC, Simino Architect (NY YIMBY, Oct 3 2024) — https://newyorkyimby.com/2024/10/permits-filed-for-1302-83rd-street-in-dyker-heights-brooklyn.html
- 7924 13th Avenue (also 1283 80th Street), corner lot near the 79th Street D station: five-story mixed-use, 22 residences, 19,970 sq ft residential plus 5,005 sq ft commercial, 55 ft (NY YIMBY, Jan 18 2026) — https://newyorkyimby.com/2026/01/permits-filed-for-7924-13th-avenue-in-dyker-heights-brooklyn.html
- New condos on 13th Avenue listed for sale, e.g. 8315 13th Ave #3C and 8323 13th Ave #3D ("Brand-New 2-Bedroom Condo"); 6605 13th Avenue is a 1931 three-story mixed-use building with 6 units — https://www.homes.com/brooklyn-ny/dyker-heights-neighborhood/condos-for-sale/ ; https://streeteasy.com/building/6605-13-avenue-brooklyn
- Homes.com: housing in Dyker Heights "is defined by a limited inventory of single- and two-family homes" — https://www.homes.com/local-guide/brooklyn-ny/dyker-heights-neighborhood/
- NYC DOB defines an illegal conversion as altering a building "to create additional apartment units without first obtaining the proper permits", e.g. "Adding an apartment in the basement, attic or garage" — https://www.nyc.gov/site/buildings/tenant/illegal-conversion.page
- City & State (Jan 2023): the city's basement apartment pilot in parts of Brooklyn had only five active participants — https://www.cityandstateny.com/policy/2023/01/nycs-basement-apartment-pilot-draws-only-5-participants/382166/
- National cost guide (NYHLS): audio-only wired $450–$900 installed, wireless audio $350–$700, video wired $900–$1,900, multi-tenant commercial $3,500+ — https://nyhls.com/blog/door-buzzer-system
- Swiftlane: repair $150–$250, like-for-like audio replacement $1,000–$3,000 per door, or smart video upgrade — https://swiftlane.com/blog/apartment-buzzer-system/
- Reddit r/AskNYC (excerpt only): a tenant in a 4-unit Brooklyn building notes the landlord "isn't required to put in a buzzer system or a self-locking front door" and asks what a system costs — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Local HPD/311 intercom complaint counts for ZIP 11228: EMPTY (open data not queried in full)
- Yelp reviews for buzzer installers near Dyker Heights: EMPTY
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DuckDuckGo: EMPTY (only Firecrawl search available)
- Dyker Heights-specific Reddit thread about buzzers or intercoms: EMPTY (search returned nothing)

### Questions people ask — Door Buzzer Installation in Dyker Heights
- How much does a buzzer/intercom system cost (for a 4-unit Brooklyn building)? — Reddit — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Is a landlord of a small (under 8-unit) building required to put in a buzzer or self-locking door? — Reddit — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- How can I stop packages being stolen from my stoop/porch? — Reddit / news — https://www.reddit.com/r/Brooklyn/comments/1ai4jqd/beware_dyker_heights_package_stealer/
- Do door buzzer installations in NYC need a permit? — Bing-style result (linkedsecurityny) — https://linkedsecurityny.com/blog/professional-door-buzzer-system-installation-in-nyc-what-to-expect-2025-complete-guide/
- Can an old intercom panel be upgraded without rewiring the whole building? — vendor FAQ — https://security-systems.nyc/service/intercom-system-installation/
- Can an intercom be integrated with cameras and alarms? — vendor FAQ — https://security-systems.nyc/service/intercom-system-installation/
- Wired vs wireless buzzer: which costs less installed? — cost guide — https://nyhls.com/blog/door-buzzer-system
- Is it cheaper to repair a buzzer or replace it? — cost guide — https://swiftlane.com/blog/apartment-buzzer-system/
- Recommendations for door buzzer/intercom installation for a rental property — Facebook — https://www.facebook.com/groups/1508709089408538/posts/4405781583034593/

## East Flatbush, Brooklyn — /door-buzzer-installation-east-flatbush-brooklyn-ny (factory research, 2026-11-11)

- Hush Street's East Flatbush development tracker (published Sept 4 2026, updated Oct 17 2026) lists Sparrow Square & Utica Crescent at 681 Clarkson Avenue & 832 Rutland Road on the former Kingsboro Psychiatric Center campus (Utica Crescent 322 units, Sparrow Square Phase 1 261 units in two 10-story buildings, full build-out up to about 1,081 units, under construction, dated June 17 2026); the East 98th Street rezoning (31 lots on East 98th Street and Rockaway Parkway between Rutland Road and Kings Highway, nine 14-15-story buildings, 972 rental units or a 786-unit version, ULURP filed late April 2026, SEQR notice May 13 2026); Bethany Senior Terraces (610 East 40th Street between Avenue D and Foster Avenue, 57 units, 4 stories, completed mid-May 2026); and small infill filings in 2026 at 885 New York Ave (9 stories, 45 units), 750 E. 35th St (5 stories, 18 units), 258 E. 53rd St (4 stories, 20 units) and 4411 Avenue D — https://hushstreet.com/whats-being-built-in-east-flatbush/
- Breaking Ground: Sparrow Square Phase I has 261 affordable homes including 117 supportive apartments for formerly homeless New Yorkers, part of a plan for about 1,000 homes on the former Kingsboro Psychiatric Center campus on Clarkson Avenue — https://www.breakingground.org/news-events/sparrow-square-breaks-ground-in-brooklyn ; https://www.breakingground.org/press/governor-hochul-breaking-ground-douglaston-development-break-ground-phase-1-sparrow-square-brooklyn
- RiseBoro: Bethany Senior Terraces is a newly built four-story building with 58 apartments, 57 affordable senior rentals including 19 supportive units for formerly unhoused seniors (ESSHI), 38 affordable senior apartments at or below 50% AMI, plus one superintendent's unit — https://riseboro.org/housing/bethany-senior-terraces/
- NYS HCR lottery listing for Bethany Senior Terraces (604 East 40th Street, 11203) lists an attended lobby and an elevator among the amenities — https://hcr.ny.gov/lottery-bethany-senior-terraces
- New York YIMBY (May 2026) on Bethany Senior Terraces completion; reader comments asked "where is the ramp for the walkers and wheelchairs?" and said "Those steps do not seem so welcoming to the aged." — https://newyorkyimby.com/2026/05/bethany-senior-terraces-completes-construction-at-610-east-40th-street-in-east-flatbush-brooklyn.html
- Marketproof (Apr 21 2026): permits filed for a four-story, 32-unit building at 869 Linden Boulevard in East Flatbush with 5,174 sq ft of residential and 1,555 sq ft of commercial space — https://blog.marketproof.com/new-building-permit-filed-for-869-linden-boulevard-in-east-flatbush-brooklyn/
- News 12 (Apr 17 2026): tenants of a four-story apartment building on Linden Boulevard in East Flatbush showed collapsed ceilings, leaks, roaches and rats, more than 900 violations on HPD's website, and could not reach a new landlord; tenant Lore Dana Ross: "We tried calling them, and nobody answered"; Sharon Lee: "We don't mind paying our rent, but we want to know we are sending it to the right people." (no buzzer/intercom item mentioned) — https://connecticut.news12.com/tenants-raise-concerns-about-east-flatbush-apartment-buildings-new-landlord
- NY Multiple Dwelling Law §50-a text: every class A multiple dwelling erected or converted after Jan 1 1968 with eight or more apartments "shall also be equipped with an intercommunication system" at an automatic self-locking door to the main entrance hall, allowing voice communication with each apartment and release of the lock from the apartment; pre-1968 buildings must install the doors and intercom if tenants occupying a majority of apartments request or consent in writing (start within ninety days, complete within six months of receipt); for rent-regulated buildings the rent agency prescribes how the costs "may be recovered by the owner from the tenants" — https://codes.findlaw.com/ny/multiple-dwelling-law/mdw-sect-50-a/
- NYC Admin Code §28-105.4.7 (as of 12/21/2025, with the 2025 NYC Electrical Code effective December 21 2025): no electrical permit is required for wiring designed to operate at less than 50 volts for signaling, communication, alarm and data circuits, "provided that such work is performed by a licensed master electrician, special electrician, or qualified person as defined in the New York city electrical code"; listed exceptions must be done only by a master or special electrician — https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 ; https://www.nyc.gov/site/buildings/industry/obtain-a-master-and-special-electrician-license.page
- HPD Tenant Data Privacy Law (Local Law 63 of 2021): owners of multiple dwellings using smart access (key fobs, RFID cards, phone apps, biometrics) must give tenants a data retention and privacy policy, may not use the data for anything beyond granting access and monitoring entrances, may not limit time of entry or require the smart system for entry to the tenant's own unit, and may not use it to harass or evict — https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page
- Hinshaw summary: the law took effect July 29 2021 and bars using a smart access system to limit the time a tenant or guest can enter unless requested by a tenant — https://www.hinshawlaw.com/en/insights/privacy-cyber-and-ai-decoded-alert/privacy-law-essentials-new-york-citys-tenant-data-privacy-act
- Reddit r/AskNYC: Brooklyn renter in a 4-unit building says "the landlord isn't required to put in a buzzer system or a self-locking front door" and asks what one costs — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Reddit r/AskNYC: prospective tenant of "a newly built 3-unit building in Brooklyn with a first-time landlord" asks whether no buzzer and one mailbox for 3 apartments is normal — https://www.reddit.com/r/AskNYC/comments/1t74q1e/is_no_buzzer_and_one_mailbox_for_3_apartments/
- Reddit r/AskNYC "Landlord won't fix buzzer": intercom still works but "the wire connection to unlock the door ... apparently is expensive to fix" — https://www.reddit.com/r/AskNYC/comments/ilvvz3/landlord_wont_fix_buzzer/
- Reddit r/NYCapartments asks about tenants' rights to request the landlord install a buzzer — https://www.reddit.com/r/NYCapartments/comments/1gfytbz/building_buzzer_installation_rights/
- Reddit r/accesscontrol: a 3-year-old NYC condo with an Aiphone GT video intercom that stopped working asks for Wi-Fi intercom recommendations for a 10-unit building "under $6k all in" — https://www.reddit.com/r/accesscontrol/comments/1r6bzlg/wifi_intercom_recs_for_10unit_building_under_6k/
- Swiftlane cost guide: "$1,000 to $5,000 or more per entry door for modern IP or video systems", multifamily projects from $1,500 to $50,000 or more — https://swiftlane.com/blog/apartment-intercom-installation-cost/
- Competitor listing for Flatbush intercom repair advertises "Most repairs $150–$250, 30-day warranty" (competitor claim, not AESS pricing) — https://www.uasecurity.com/intercom-systems-flatbush-brooklyn-new-york.htm
- Yelp "Intercom Repair in Brooklyn" search lists Brooklyn Locksmith & Doors, MetroCom Security, Falcon Locksmith, BAB Communications (list only; review text not retrieved) — https://www.yelp.com/search?find_desc=Intercom+Repair&find_loc=Brooklyn%2C+NY
- NYT (Jan 20 2024) headline: "That Broken Intercom in Your Apartment Is Illegal. Here's What to Do"; snippet: a working intercom is "a legal requirement in most buildings" (full text not retrievable) — https://www.nytimes.com/2024/01/20/realestate/that-broken-intercom-in-your-apartment-is-illegal-heres-what-to-do.html
- Google PAA / PASF / Answer the Public / AI Overview / Bing / DuckDuckGo: EMPTY (not accessible in build env)
- East Flatbush-specific Reddit buzzer-installation thread: EMPTY
- Yelp 1–3★ review text: EMPTY

### Questions people ask — Door Buzzer Installation in East Flatbush
- How much does a buzzer/intercom system cost for a small Brooklyn building? — Reddit — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Is a landlord of a 4-unit building required to install a buzzer or self-locking front door? — Reddit — https://www.reddit.com/r/AskNYC/comments/3jrrqj/how_much_does_a_buzzerintercom_system_cost/
- Is no buzzer and one mailbox for 3 apartments normal for a new Brooklyn building? — Reddit — https://www.reddit.com/r/AskNYC/comments/1t74q1e/is_no_buzzer_and_one_mailbox_for_3_apartments/
- Can tenants ask the landlord to install a buzzer, and what rights do they have? — Reddit — https://www.reddit.com/r/NYCapartments/comments/1gfytbz/building_buzzer_installation_rights/
- Why is the door-release wire connection expensive to fix when the intercom talks fine? — Reddit — https://www.reddit.com/r/AskNYC/comments/ilvvz3/landlord_wont_fix_buzzer/
- What Wi-Fi intercom works for a 10-unit building on a budget, and should a failed Aiphone GT be replaced? — Reddit — https://www.reddit.com/r/accesscontrol/comments/1r6bzlg/wifi_intercom_recs_for_10unit_building_under_6k/
- How much does apartment intercom installation cost per door? — web cost guide — https://swiftlane.com/blog/apartment-intercom-installation-cost/
- Does a new senior building need a ramp and accessible entry for walkers and wheelchairs? — New York YIMBY comments — https://newyorkyimby.com/2026/05/bethany-senior-terraces-completes-construction-at-610-east-40th-street-in-east-flatbush-brooklyn.html
- PAA / PASF / AnswerThePublic / Bing / DuckDuckGo / Yelp questions: EMPTY
