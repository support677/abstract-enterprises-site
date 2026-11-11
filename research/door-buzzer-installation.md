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
