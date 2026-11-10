# Intercom Repair — silo research

Created 2026-10-18 by the REBUILD run for `intercom-repair-putnam-county` (queue line: `REBUILD | intercom-repair-putnam-county | Intercom Repair | Putnam | up /intercom-repair-hudson-valley | (845) 640-3835 | GBP Bronx`). No `research/intercom-repair.md` existed before this run.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. "Excerpt" = read only as a search-result snippet, not opened. Tools: WebSearch (Claude), WebFetch (several fetches were blocked by the permission gate — listed as such), Firecrawl search (`mcp__Firecrawl__firecrawl_search`, web + `gov` category), Firecrawl scrape (`mcp__Fire_Crawl__firecrawl_scrape`, query mode, PDF parser). Shell curl is blocked.

Page section labels (Putnam page): §Hero, §Quick (instant action), §5 Neighborhood (+5.5 facts), §Emergency, §6 Services, §7 Architecture (+7.5), §8 Commercial (+8.5 rules), §9 Q&A (clusters A–F), §10 Equipment (+ comparison), §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks + town table, §14 Pricing, §15 Packages (+BYOE), §16 Services grid, Field Notes, §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every Intercom Repair page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows R1–R3). No Putnam/Hudson Valley intercom thread found. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 states this on-page and corrects claims published by the cost guides, manufacturers and vendor blogs that such answers draw on (rows A1–A5). |
| 6 | Area landmarks | Putnam section L*. |
| 7 | Area use cases / building stock | Putnam section B*. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — the only search backends available were WebSearch and Firecrawl. |
| 9 | Local news | NEWS10 (Verizon copper), Daily Voice / NYSEG / WAMC (outages, reused), Putnam Press Times (excerpt), Planetizen (excerpt). |
| 10 | Hyperlocal | Highlands Current, PCNR, Town of Putnam Valley, Putnam County Main Streets study (reused + new). |
| 11 | Yelp 1–3★ | Firecrawl `site:yelp.com` search returned only Yelp category pages for other cities with 4–5★ snippets; no 1–3★ intercom-repair review text readable → EMPTY (not accessible in build env). Not used on page. |

### 1.2 Reddit and forums
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit intercom buzzer apartment not working "door release" landlord fix` · Firecrawl search (reddit.com) | https://www.reddit.com/r/OntarioLandlord/comments/qgzhvk/apartment_intercom_and_door_buzzer_broken_for/ | Excerpt title: "Apartment intercom and door buzzer broken for months, landlord in no hurry to fix". | Background for §9 cluster D (responsibility is set by lease/bylaws); not quoted |
| R2 | same | https://www.reddit.com/r/fixit/comments/ucpu3x/apartment_buzzer_system_not_working_nobody_taking/ | Excerpt title: "Apartment Buzzer System Not Working - Nobody Taking Responsibility". | §9 cluster D background; not quoted |
| R3 | `electric strike door release buzzer intercom fail-safe fail-secure 12V 24V AC DC wrong voltage buzzing` · Firecrawl search | https://www.reddit.com/r/accesscontrol/comments/18fhi5q/door_strike_not_working_through_power_outage/ | Excerpt (r/accesscontrol): strikes set fail-safe so that in an outage, when 12 V batteries die, behaviour changes — thread on strikes in power outages. | §17 FAQ "what happens to the door if the intercom loses power" (background; not quoted) |
| R4 | `reddit intercom buzzer stopped working apartment door release fix` · WebSearch | https://www.brownstoner.com/forum-archive/2006/01/broken-buzzerin ; https://communityforums.rogers.com/t5/Home-Phone/Building-Intercom-Buzzer-Stopped-Working-After-Upgrading-to/m-p/497806 | Titles only: Brownstoner "Broken Buzzer/Intercom System"; Rogers forum "Building Intercom (Buzzer) Stopped Working After Upgrading to Rogers Ignite" (phone-line-dialing entry stopped after a home-phone technology change). | §10.5 H3 3 background (phone service change breaks telephone-entry dialing); not quoted |

### 1.3 Failure modes (manufacturers / vendors)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F1 | `intercom repair common problems no audio buzzer not working door release` · WebSearch → WebFetch | https://butterflymx.com/blog/intercom-not-working/ | No audio/video: "a power issue, damaged wiring, or a problem with the microphone or camera"; power: "a tripped circuit breaker, a damaged transformer, or a disconnected power source"; wires "corroded, frayed, or even chewed through by pests"; door won't unlock: "a malfunction in the electric strike" or "a communication error between the intercom and the door system"; static: "faulty wiring, low power, or interference"; telephone callboxes: calls not reaching residents from "incorrect phone numbers in the directory, service outages, or carrier-level blocking"; old parts unavailable → replace the entire unit. | §9 clusters C/F; §10.5 H3 4 (quote "replace the entire intercom unit" corrected); §12 step 2 |
| F2 | same · WebSearch → WebFetch | https://butterflymx.com/blog/how-cold-weather-affects-apartment-intercoms/ | "Metal parts contract in the cold" (latch/strike fit); "Moisture can enter exterior panels, cable paths, and lock hardware"; aging transformers, brittle wiring, loose connections most at risk; batteries perform worse in low temperatures; advice: "Test the system during temperature swings, when intermittent faults are easier to spot"; "Review strike alignment and look for doors that need extra pressure to latch or release". | §5 para 3; §9 Q (January door needs a shove); §9 Q (lake house dead in April); Field Notes |
| F3 | `Aiphone intercom no audio troubleshooting power supply PS-1820 voltage check` · Firecrawl search | https://www.aiphone.com/products/ps-1820ul/ ; https://www.aaaremotes.com/aiphone-telephone-intercom-entry-system-access-control-troubleshooting/ | Excerpts: PS-1820UL is "a UL Listed 18V DC, 2A Power Supply for Aiphone systems… temperature rating of 0 to 40 degrees"; troubleshooting: "Not enough power at the monitor, power supply is too far away, or there are too many monitors on one power supply (three monitors maximum on one PS-1820UL)." | §9 Q (monitors lit but door won't release) power reasoning; §10 power card; §10.5 H3 5 |
| F4 | `electric strike … fail-safe fail-secure 12V 24V AC DC` · Firecrawl search | https://doorcontrolsdirect.co.uk/blog/post/172-electric-strikes-faqs-and-troubleshooting ; https://www.trineonline.com/trouble_shooting.php | Excerpts: "Match the 12V/24V rating and AC/DC type to the strike. A click with no release could indicate…"; Trine: "a strike without the proper amperage at the rated voltage will often create a weak or erratic buzz sound on AC power. Is the strike a fail-safe (lock…" | §9 Q (strike vs intercom); §17 FAQ power-loss; §10 strike card |
| F5 | `2-wire intercom vs IP intercom system upgrade reuse existing wiring Aiphone` · WebSearch → WebFetch | https://aiphone.com/?p=19238 (Aiphone "Question of the Week") | Luke Romero: "a lot of times we can reuse the cable and save much of the cost by just installing new equipment"; "If the product is discontinued, we must start completely fresh with wire and product." Karlis Praulins: "Phase 1 would be upgrading all the back-end equipment to IP using 2wire convertors or running new cable." Paul Hefty: "you can install an IP intercom anywhere" (analog limited by wire distance; IP needs PoE network). | §9 cluster F; §10 converter card; §10.5 H3 4 |
| F6 | same (excerpts) | https://becintegrated.com/aiphone-ipw-1vc-analog-to-ip-converter-set ; https://www.dnake-global.com/news/2-wire-intercom-systems-vs-ip-intercoms-whats-best-for-your-home-or-apartment/ | Aiphone IPW-1VC analog-to-IP converter set exists; DNAKE 2-wire vs IP article. | §10 converter card (product category only) |

### 1.4 Telephone-entry and copper retirement
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `reddit gate intercom landline Verizon copper retirement cellular call box DoorKing` · WebSearch → WebFetch | https://www.securityinfowatch.com/access-identity/intercom-solutions/product/12105735/doorking-inc-doorking-4g-lte-cellular-telephone-entry-systems | 2015 vendor promotion: DoorKing cellular add-on on AT&T 4G LTE; "need to run phone lines, Ethernet cables or other data wiring is completely eliminated"; cites "the end-of-life for copper phone lines is 2020". | §10.5 H3 3 (the 2020 claim, corrected); §10 cellular card |
| T2 | `FCC copper retirement Verizon New York landline discontinuance 2025 alarm elevator lines` · WebSearch → WebFetch | https://www.alarmgrid.com/blog/2026/10 | Sept 28, 2026: FCC paused automatic approval of Verizon's copper discontinuance filings; first filing Sept 9, 2026 (~277,000 lines), second mid-Sept (~750,000 customers in nine more states plus D.C., NY, CA, PA); later dates Oct 23 and Nov 30, 2026 mentioned; no new target date; Catskill region of NY residents filed comments. | §10.5 H3 3; §9 cluster A body text (not a Q) |
| T3 | `Verizon copper retirement New York wire centers Carmel Mahopac Brewster Cold Spring Peekskill 2026 FCC filing landline` · Firecrawl search | https://www.news10.com/news/verizon-moving-away-from-copper-landlines-what-customers-need-to-know/ | NEWS10 (Albany), Sept 22, 2026: Verizon seeking FCC approval to retire copper landlines; "less than 3% of Verizon customers nationwide who still use copper-wire landlines"; "If Verizon can't provide a viable replacement at your location, the company says your copper service will remain in place." | §10.5 H3 3 |
| T4 | same | https://saugertiesny.gov/verizons-proposal-retire-copper ; https://www.fauquiercounty.gov/government/departments-a-g/county-administration/verizon-copper-line-phase-out | Excerpt: Saugerties (Ulster) — proposed discontinuance "on or after November 30, 2026" for portions of New York. Fauquier County VA: Sept 25, 2026 FCC public notice that the application "was not automatically granted"; CopperAlerts map to check ZIPs. | §10.5 H3 3 (Saugerties as the nearest named NY town; NO claim that Putnam exchanges are listed) |
| T5 | `Verizon … wire centers Carmel Mahopac …` | — | No source found naming a Putnam County wire center in the filings → page says "check your own line", never that Putnam is affected. EMPTY for Putnam specifics. | §10.5 H3 3 |

### 1.5 Cost aggregators (feed §10.5)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `intercom repair cost 2025 average price Angi HomeAdvisor` · WebSearch → WebFetch | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system | Installation (not repair) cost: national average $2,500; header "Normal Range: $1,200 - $8,500" but overview "$1,500 and $15,000" (page does not reconcile); audio-only $50–$450; audio+video $600–$15,000; wired $1,000–$15,000; labor for complete system $1,000–$1,500; repair cost not stated. | §10.5 H3 1 |
| A2 | same (excerpts) | https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ ; https://getsafeandsound.com/blog/intercom-installation-cost/ | Vendor cost guides (titles only). | Not used |

### 1.6 New York State rules (every NY page)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `New York Multiple Dwelling Law section 50-a intercom two-way voice communication eight or more apartments applies cities 325,000` · Firecrawl search (gov) | https://nysenate.gov/legislation/laws/MDW/50-A ; https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a | §50-a: class A multiple dwellings erected or converted after Jan 1, 1968 with eight or more apartments must have an intercommunication system for voice communication between each apartment and a person at the self-locking lobby door, and to release the door from the apartment. | §8.5 bullet 1; §9 Q (MDL outside NYC); §10.5 H3 6 |
| G2 | same | https://nysenate.gov/legislation/laws/mdw/3 | MDL §3: "This chapter shall apply to all cities with a population of three hundred twenty-five thousand or more." Any other city, town or village may adopt it by local law. | §8.5 bullet 1; §9 Q (MDL outside NYC); §10.5 H3 6 |
| G3 | `New York Real Property Law 235-b warranty of habitability text` · Firecrawl search (gov) | https://law.justia.com/codes/new-york/rpp/article-7/235-b ; https://nysenate.gov/legislation/laws/RPP/235-B | Every residential lease carries a warranty that the premises "and all areas used in connection therewith in common with other tenants" are fit for habitation and free of conditions dangerous to life, health or safety. | §8.5 bullet 2; §9 cluster D |
| G4 | same | https://ag.ny.gov/sites/default/files/tenants_rights.pdf | NY AG Residential Tenants' Rights Guide: public areas covered; "Owners of cooperative apartments can raise the warranty of habitability but not owners of condominiums. Tenants and sub-tenants in cooperatives and condominiums can raise the warranty of habitability." | §9 Q (condo who pays); §8.5 bullet 2 |

### 1.7 Keyword plan (five layers, silo)
- **Service:** intercom repair, intercom service, door intercom repair, video intercom repair, gate intercom repair, telephone entry repair, call box repair, buzzer and door release repair, intercom troubleshooting, intercom replacement, intercom upgrade, intercom maintenance.
- **Problem:** no audio, one-way audio, hum/static, door release not working, strike buzzes but door stays locked, ghost calls, monitor black, power supply failed, transformer burnt, corroded door station, water in the call box, frozen latch, directory not dialing, app offline, phone line cut, lightning/surge damage, chewed cable.
- **Technology:** 2-wire, 4-wire, IP/PoE, SIP, cellular LTE call box, telephone entry, electric strike (fail-safe / fail-secure), mag lock, transformer 12/16/24 V, 18 V DC supply, surge protector, two-wire-to-IP converter; brands Aiphone (JO, GT, IX), Comelit, ButterflyMX, Akuvox, 2N, DoorBird, DoorKing.
- **Industry:** single-family homes, lake houses, private-road associations, condo complexes, 55+ communities, senior apartments, mixed-use Main Street buildings, small offices/practices, retail plazas.
- **Geographic (Putnam page):** Putnam County; Carmel, Mahopac, Mahopac Falls, Brewster, Southeast, Patterson, Putnam Lake, Kent, Lake Carmel, Putnam Valley, Lake Oscawana, Lake Peekskill, Oregon Corners, Philipstown, Cold Spring, Nelsonville, Garrison; Route 6, Route 22, Route 52, Route 301, Route 312, Gleneida Avenue, Main Street Brewster, Main Street Cold Spring, Oscawana Lake Road, Peekskill Hollow Road.

### 1.8 Silo pricing (no invented prices) + FLAGS
Base table (identical on intercom-repair-brooklyn / -bronx / -nyc; Brooklyn = §9 1.00×): diagnostic $150–$300; apartment handset $250–$600; residential video monitor swap $300–$750; lobby/entry panel component repair $400–$1,200; panel retrofit in existing opening $1,500–$3,500; transformer/power supply $300–$800; door release strike $350–$900; bus wiring repair (limited) $1,000–$3,000; small building full system $4,500–$12,000; mid-size IP $12,000–$28,000; maintenance $600–$2,400/yr. Service/callback rate $195/hr, 3-hr minimum ($585) (blueprint §9, protected).
**Putnam ×1.45 (round half-up):** diagnostic $218–$435; handset $363–$870; video monitor swap $435–$1,088; panel component $580–$1,740; panel retrofit $2,175–$5,075; transformer $435–$1,160; strike $508–$1,305; wiring repair $1,450–$4,350; small building $6,525–$17,400; mid-size IP $17,400–$40,600; maintenance $870–$3,480/yr.
FLAGS:
- The old Putnam, Westchester, Dutchess (and Rockland/Orange/Suffolk) intercom pages publish the Brooklyn base table unchanged — no §9 multiplier — and even carry Brooklyn-only rows ("Brownstone video intercom monitor swap", "Luxury new construction IP… Williamsburg waterfront, Downtown BK luxury", "Mircom TX3 directory rebuild… doorman building", "Marine-grade coastal panel"). Not carried.
- The Hudson Valley hub uses ≈1.30× (e.g. retrofit $1,950–$4,550) but its diagnostic ($200–$400) and monitor swap ($325–$800) do not follow 1.30×; the Long Island hub is inconsistent the same way.
- Gate-only rows (button/relay $350–$900, SIM swap $400–$800, landline-to-cellular $1,800–$3,500, long-driveway cable $3,500–$15,000+, HOA gate overhaul $18,000–$35,000+) exist only on the HV/LI hubs with no Brooklyn base, so no ×1.45 figure can be derived. Putnam page quotes these as "published on the Hudson Valley hub" and says Putnam gate work is priced after a site test.
- Our own live page /door-buzzer-repair-putnam-county-new-york says (search excerpt): "For rental multi-family in Brewster, Carmel and Mahopac, State MDL requires post-1968 buildings with eight or more units to have a two-way voice intercom." MDL §3 limits the law to cities of ≥325,000 unless a town or village adopts it by local law; no such Putnam adoption was found. Looks wrong — needs Anwar's review (not edited; outside this run's scope).

---

## Putnam

### Building stock and places (new this run)
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| B1 | `Putnam County senior housing apartments Carmel Mahopac Brewster apartment complex Putnam County Housing Corporation` · Firecrawl search | https://www.putnamhousing.com/ (excerpt) | PCHC incorporated 1982 as a non-profit Rural Preservation Company; has built "120 units of senior housing". | §7 senior card; §5.5 bullet |
| B2 | same | https://www.putnamcountyny.gov/osr (excerpt) | County Office for Senior Resources list: Gleneida Court Apartments (62+ or disabled), Carmel; Gleneida Sr. Apts. (60+), 20 Gleneida Court, Carmel; Sr. Housing @ Mahopac Hills (62+), 170 Rt. 6, Mahopac; Putnam Community Foundation, 50 Main Street, Brewster (62+). | §7 senior card; §13 town table |
| B3 | same | https://www.putnamhousing.com/gleneida-senior-apartments-get-started/ ; https://www.putnamhousing.com/wp-content/uploads/2018/04/Senior-Housing-at-Mahopac-Hills-2018.pdf (excerpts) | Gleneida Senior Apartments: 24 one-bedroom units, 60+; Mahopac Hills: 24 one-bedroom units, non-smoking, 62+; PCHC senior page excerpt: "A two-story garden apartment complex with 24 units, each are 650 square feet". | §7 senior card; §5.5 bullet |
| B4 | `Putnam County NY condominium complex Carmel Brewster Mahopac condo association gated community` · WebSearch → Firecrawl scrape (query) | https://www.weichert.com/133706987/ | Listing, 3012 Summit Loop, Carmel: condo built 2026 "nestled within a serene 55+ community"; subdivision "Overlook by Toll Brothers - Carriages"; association covers exterior maintenance, grounds, snow removal; clubhouse, fitness center, pool. (Address not printed on page.) | §7 condo/55+ card (named as "Overlook, Toll Brothers' 55-and-over community in Carmel") |
| B5 | `Brewster village Main Street apartments above stores mixed-use buildings Putnam County news` · Firecrawl search | https://putnamcountyny.gov/images/Departments/Planning_Dev_Transport/PDF_Documents/chapter3.pdf (excerpt) | Putnam County Main Street Partnership Planning Study: "The Village of Brewster has a long established mixed-use Main Street, with a Metro North train station at its terminus." | §7 mixed-use card; §8 Brewster card |
| B6 | same | https://www.planetizen.com/news/2021/11/115384-main-street-redevelopment-hopes-lure-nyc-commuters-village-brewster (excerpt; WebFetch blocked by permission gate) | Nov 2021: plans include "408 rental units and artist lofts fanned across three new 5- to 6-story buildings". | §8 Brewster card ("plans reported in 2021") |
| B7 | same | https://www.putnampresstimes.com/post/brewster-village-oks-zone-change-for-garden-street (excerpt) | Brewster village zone change for Garden Street raises height limit "from two and a half stories to five stories". Undated in excerpt. | §8 Brewster card (no date given) |
| B8 | same | https://www.apartments.com/50-main-st-brewster-village-ny/st70py5/ (excerpt) | 50 Main St, Brewster: studio apartment "handicap accessible close to train station". | Background (B2 carries the address) |
| B9 | `Putnam County NY gated community private road association gate Mahopac Putnam Valley Lake Oscawana` · Firecrawl search → Firecrawl scrape (PDF, freeform) | https://putnamcountyny.gov/images/Departments/Planning_Dev_Transport/PDF_Documents/chapter4.pdf | "Putnam County Main Streets": Oregon Corners (Oscawana Lake Rd × Peekskill Hollow Rd / Hollowbrook Rd / Old Oregon Rd, Putnam Valley); two-story buildings with a salon and spa, deli and restaurant, Putnam Valley Restaurant at street level; "a doorway to a staircase that leads up to a second floor apartment. The tenants currently exit the building into the roadway." Hardware store, post office, medical office, shopping plaza. | §7 mixed-use card; §8 Oregon Corners card; §9 Q (apartment over a storefront) |
| B10 | same → Firecrawl scrape | https://lakeoscawana.net/civic-associations | Lake Oscawana Civic Association; Town created the Lake Oscawana Advisory Committee in 1988; lake tax district. | §7 lake card; §13 town table (Putnam Valley) |
| B11 | `Putnam County NY gated community …` · Firecrawl search | https://www.homes.com/property/589-oscawana-lake-rd-putnam-valley-ny/c1zfg03jqvtjr/ (excerpt) | Listing: built 1975, "10+ acres of complete privacy", association amenities. | Background only (no address used) |
| B12 | `reddit Putnam County NY Mahopac Carmel Brewster condo gate intercom OR buzzer OR callbox` · Firecrawl search | (no Reddit result; only AESS pages and Zillow) | Reddit for Putnam intercoms: EMPTY. Found our own /door-buzzer-repair-putnam-county-new-york MDL claim (FLAG above). | FLAG |

### Licensing (new + reused)
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| P1 | `Putnam County NY Consumer Affairs home improvement license contractor requirement` · WebSearch → WebFetch | https://putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/Home%20Improvement%20New%20First%20Time%20Application%201-28-2025.pdf | Putnam Consumer Affairs home-improvement registration application (Jan 28, 2025): $300 fee "covers your two-year registration"; ACORD liability certificate naming the County as additionally insured, with scope of work; workers' comp form or CE-200 exemption; license and permit bond "IN THE AMOUNT OF $25,000.00"; no exam mentioned. | §8.5 bullet 3; §10.5 H3 7 |
| P2 | Reused: research/dvr-upgrade.md R1 (from fiber/smart-lock) | https://putnamcountyny.gov/laws/item/local-law-no-10-of-2013-amend-chapter-135-code-of-putnam-county-entitled-contractors ; https://www.putnamcountyny.gov/consumer-affairs ; https://ecode360.com/6607815 | Ch. 135 home-improvement registration; Electrical Board licenses Limited Data Communication Technicians; Ch. 145 (electricians); county list of licensed low-voltage technicians; electrical permits for Carmel, Patterson, Putnam Valley filed with those towns. | §8.5 bullets 3–4; §10.5 H3 7 |
| P3 | Reused: research/dvr-upgrade.md R4 | https://highlandscurrent.org/2025/08/08/the-history-patrol/ (excerpt) ; https://www.coldspringny.gov/DocumentCenter/View/2074/Certificate-of-Appropriateness-PDF | Since 1976 exterior changes in Cold Spring's historic district need the five-member HDRB's approval; work not visible from the street is not reviewed. | §7 village card; §8 Cold Spring card; §8.5 bullet 5 |
| P4 | Reused: research/dvr-upgrade.md R2 | https://www.townofcarmelny.gov/DocumentCenter/View/456/Wetland-Permit-Application-PDF | Carmel regulates wetlands ≥1/8 acre + 100-ft buffer. | §8.5 bullet 6 (trenching a gate cable) |

### Reused sourced Putnam research (from research/dvr-upgrade.md Putnam section — not re-fetched)
| # | URL | Finding | Page + section used |
|---|---|---|---|
| H1 | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | >240 sq mi; six towns + three villages; ~3/4 in NYC watershed; >9/10 Hudson Highlands bedrock; forest 66.9%; commercial along Routes 6, 9, 22, 52 and I-84 | §5 para 1; §5.5; §8 intro |
| H2 | https://www.census.gov/quickfacts/putnamcountynewyork | 38,713 housing units; owner-occupied 83.8% | §5 para 2; §5.5 |
| H3 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36079 | 1,757 seasonal/recreational/occasional-use units | §5 para 2; §5.5 |
| H4 | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Lake Carmel, Lake Peekskill, Putnam Lake laid out from 1928; 11,000 lots at Putnam Lake | §7 lake card |
| H5 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 5, 2020: NYSEG 34,150 of 38,693 Putnam customers out | §5 para 3; §5.5; §10.5 H3 2 |
| W1 | https://www.nyseg.com/w/brewster-nyseg-continues-restoration-effort-6-pm | Dec 25, 2020: 27,375 Brewster-division customers; gusts to 71 mph | §5 para 3 |
| W2 | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | Putnam 2020: 75,093 lightning pulses, 35 thunder days | §5.5; §9 surge Q; §10.5 H3 2 |
| W4 | https://www.putnamvalley.gov/state-of-emergency-declared-in-the-town-of-putnam-valley-effective-at-4-pm-on-wednesday-july-29-2026/ | State of emergency 4 PM July 29, 2026 for flash flooding | §13 town table (Putnam Valley) |
| N1 | https://www.schumer.senate.gov/newsroom/press-releases/schumer-cell-phone-wireless-carriers-are-wrongly-claiming-quality-reception-on-coverage-maps-for-northern-westchester-and-putnam-counties-in-reality-areas-are-often-dead-zones-schumer-calls-for-feds-to-immediately-investigate-deceptive-coverage-maps | Oct 5, 2015 dead-zones quote | §10.5 H3 3 (cellular call boxes) |
| N7 | https://putnamsheriff.com/dark-house-check/ | Sheriff Dark House Check | §9 Q (lake house closed) background |
| L1–L6 | Mahopac (Wikipedia); Putnam County Courthouse (Wikipedia); NYC DEP West Branch Reservoir; Cold Spring Historic District (Wikipedia); Tilly Foster Farm (county PDF excerpt); Fahnestock State Park (parks.ny.gov excerpt) | as in dvr-upgrade.md L1–L6 | §13 landmark cards (rewritten for intercom context) |

### EMPTY for Putnam
Reddit Putnam intercom/gate threads; Yelp 1–3★ for Putnam intercom companies; Patch/lohud/News 12 Hudson Valley stories about intercom or entry-system failures in Putnam; any list naming Putnam wire centers in Verizon's copper filings; any Putnam town or village adoption of the Multiple Dwelling Law; the number of gated or private-road associations in the county; a sourced Putnam intercom job for Field Notes (written as practice, labelled so).

### House practices stated on the page without an external source (FLAG for Anwar)
Fault-finding order (power → door station → wire → handsets → strike); measuring voltage at the far end under load; using a tone/TDR-style fault locator on long gate runs; surge protection at each building entry on gate runs; moving supplies to a heated space; replacing wasp/ant-packed speaker modules; "most entry systems working again within one to two hours of arrival" (silo convention from repair-capture blocks); seven-day booking in two-hour windows to 8 PM (copied from dvr-upgrade-putnam). Page does not claim AESS holds Putnam Ch. 135 registration or a Putnam low-voltage licence — tells owners to ask installers "including us" and check the county lists.

### Pricing used
Putnam ×1.45 figures from §1.8. HV-hub-only gate figures quoted as published there. Packages = (1) single-entry repair visit = diagnostic + one component (derived ranges shown as the two rows they come from, not a new number), (2) panel retrofit row, (3) small-building system row. $195/hr callback.

### Images (11) — Drive has no Intercom folder; CompanyCam not connected
Permanent image rule. 3 real AESS job photos from other jobs (cropped; captions say "example photo from another AESS job, not a Putnam property") + 8 manufacturer product shots (all intercom/door stations). `images/buzzer-repair/*` not used (rejected as AI-generated on door-buzzer-installation run); `digital-watchdog-megapix-intercom.jpg` rejected (CGI render look); `access-control-*.jpg` (1024² renders) not used. All viewed with Read before naming; none used on any intercom-repair sibling (siblings carry no figures).
| Output (images/intercom-repair/) | Source | Crop / note |
|---|---|---|
| intercom-repair-putnam-county-single-button-video-door-station.webp (423×562, hero) | images/akuvox-video-door-station.webp | product shot |
| …-black-video-door-station-with-lit-call-button.webp (675×900) | images/axis-i8116-video-intercom.webp | product shot |
| …-slim-black-video-doorbell-with-ring-button.webp (915×915) | images/avigilon-video-door-entry.jpg | product shot, flattened on white |
| …-steel-keypad-door-station-with-card-reader.webp (803×1429) | images/intercom-keypad-akuvox.png | product shot |
| …-white-indoor-answering-monitor.webp (456×456) | images/intercom-indoor-monitor.png | product shot; on-screen contact-name list blurred |
| …-touchscreen-keypad-entry-panel.webp (456×456) | images/intercom-touchscreen.png | product shot |
| …-dark-touchscreen-directory-panel-with-keypad.webp (456×456) | images/intercom-keypad-dark.png | product shot ("Main Office" generic screen text) |
| …-silver-and-black-door-station-with-card-symbol.webp (456×456) | images/intercom-akuvox-round.png | product shot |
| …-white-dome-camera-on-shop-canopy-corner.webp (547×532) | images/manhattan-deli-exterior-camera.jpeg | real job photo; crop (700,288,1247,820) — sign lettering, phone number and address excluded |
| …-turret-camera-above-glass-entry-vestibule.webp (755×820) | images/rockland-toyota-office-camera.jpeg | real job photo; crop (180,0,935,820) — signage, person, trophies excluded |
| …-dome-camera-and-motion-sensor-in-ceiling-corner.webp (400×500) | images/nassau-window-depot-office-camera.jpeg | real job photo; crop (400,300,800,800) — banner, flag, framed licences excluded |
DAILY-LOG note suggestion: `images: 8 manufacturer intercom product shots + 3 real AESS photos from other jobs (no real intercom photos; images/buzzer-repair/ rejected as AI-generated)`.

---

## Question register — every question on every Intercom Repair page (extracted from HTML 2026-10-18, before this rebuild)
Includes H2/H3/H4 headings, `.qa-q` cards, and FAQPage schema names. Category tags (Cost, Technical…) are part of the old card text. `intercom-repair-putnam-county` below is the OLD page (replaced by this rebuild; its questions stay listed so no sibling re-uses them by accident).

### intercom-repair-bronx — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Bronx Intercom Repair Today?
- How much to fix a broken buzzer in a Mott Haven or Fordham walk-up? Cost
- Why do Bronx intercom repair quotes vary so wildly? Cost
- My Tremont landlord says intercom repair is "too expensive" — what do I push for? Cost
- How do I find a licensed Bronx intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Bronx handyman for a quick fix? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Co-op City panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors can hear me but I can't hear them in our Fordham building — what part is dead? Technical
- Why does my City Island intercom keep dying every 3 years? Technical
- My Bronx landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
- I'm a small Bronx landlord with a 14-unit Wakefield walk-up — what do I owe tenants? Landlord/Tenant
- Tech showed up in Parkchester, charged $400, intercom still broken — recourse? Complaints
- Got quoted $40k to "completely replace" our Co-op City building system when one apt died. Reasonable? Complaints
- Why is my Bronx apartment intercom not working?
- Where can I get my Bronx intercom fixed?
- How fast is same-day in the Bronx?
- Can Co-op City buildings be upgraded without full rewiring?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in the Bronx?
- Do you service Co-op City and Parkchester?
- Do you service pre-war Lee Dan and M&S in Bronx walk-ups?
- Can you upgrade my Bronx building without rewiring?
- My Bronx landlord ignored the broken intercom — what is HPD role?
- Do you handle Riverdale estate gated entry intercoms?
- What does Bronx intercom repair typically cost?
- Do you fix coastal-corroded intercoms in City Island and Throgs Neck?
- Are your repairs guaranteed?
- What brands do you repair in the Bronx?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in the Bronx?
- [schema] Do you service Co-op City and Parkchester?
- [schema] Do you handle Grand Concourse Art Deco pre-war buildings?
- [schema] Do you service pre-war Lee Dan and M&S in Bronx walk-ups?
- [schema] Do you fix coastal-corroded intercoms in City Island and Throgs Neck?
- [schema] My Bronx landlord ignored the broken intercom — what is HPD role?
- [schema] Do you handle Riverdale estate gated entry intercoms?
- [schema] What does Bronx intercom repair typically cost?
- [schema] Can you upgrade my Bronx building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in the Bronx?
- [schema] Do you provide HPD Certificate of Correction documentation?

### intercom-repair-brooklyn — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Brooklyn Intercom Repair Today?
- How much to fix a broken buzzer in a Bay Ridge or Sunset Park walk-up? Cost
- Why do Brooklyn intercom repair quotes vary so wildly? Cost
- My Bushwick landlord says intercom repair is "too expensive" — what do I push for? Cost
- How do I find a licensed Brooklyn intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Brooklyn handyman for a quick fix? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors can hear me but I can't hear them — what part is dead? Technical
- Why does my Brighton Beach intercom keep dying every 3 years? Technical
- My Brooklyn landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
- I'm a small Brooklyn landlord with a 14-unit Crown Heights walk-up — what do I owe tenants? Landlord/Tenant
- Tech showed up in Williamsburg, charged $400, intercom still broken — recourse? Complaints
- Got quoted $16k to "completely replace" our 22-unit Crown Heights system when one apt died. Reasonable? Complaints
- Why is my Brooklyn apartment intercom not working?
- Where can I get my Brooklyn intercom fixed?
- How fast is same-day response in Brooklyn?
- Can a brownstone intercom be upgraded without damaging brickwork?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Brooklyn?
- Do you service Brooklyn brownstones and townhouses?
- Do you service pre-war Lee Dan and M&S in Brooklyn walk-ups?
- Can you upgrade my Brooklyn building without rewiring?
- My Brooklyn landlord ignored the broken intercom — what's HPD's role?
- Do you handle Brooklyn co-op boards?
- What does Brooklyn intercom repair typically cost?
- Do you fix coastal-corroded intercoms in Brighton Beach / Coney Island?
- Are your repairs guaranteed?
- What brands do you repair in Brooklyn?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Brooklyn?
- [schema] Do you service Brooklyn brownstones and townhouses?
- [schema] Do you service pre-war Lee Dan and M&S in Brooklyn walk-ups?
- [schema] Can you upgrade my Brooklyn building without rewiring?
- [schema] My Brooklyn landlord ignored the broken intercom — what's HPD's role?
- [schema] Do you handle Brooklyn co-op boards?
- [schema] What does Brooklyn intercom repair typically cost?
- [schema] Do you fix coastal-corroded intercoms in Brighton Beach / Coney Island?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Brooklyn?
- [schema] Do you provide HPD Certificate of Correction documentation?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-dutchess-county — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Dutchess County Intercom Repair Today?
- How much to fix a video intercom on my Fishkill or Wappingers home? Cost
- Why do Dutchess County intercom repair quotes vary so wildly? Cost
- I'm a Dutchess homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Dutchess County intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Dutchess handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Poughkeepsie walk-up lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Poughkeepsie building — what is dead? Technical
- Why does my Beacon or Poughkeepsie Hudson-facing intercom keep dying every 3 years? Technical
- I run a Dutchess commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Dutchess small commercial property owner with an 18-unit Poughkeepsie walk-up — what do I owe tenants? Residential/Commercial
- Tech showed up in Rhinebeck, charged $400, intercom still broken — recourse? Complaints
- Got quoted $19k to "completely replace" our 22-unit Poughkeepsie system when one apt died. Reasonable? Complaints
- Why is my Dutchess home intercom not working?
- Where can I get my Dutchess intercom fixed?
- How fast is same-day in Dutchess?
- Can my Rhinebeck or Millbrook estate gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Dutchess County?
- Do you service Dutchess County single-family homes?
- Do you service Poughkeepsie city and Vassar/Marist college rentals?
- Can you upgrade my Dutchess building without rewiring?
- Do you service Beacon arts-district mixed-use and historic buildings?
- Do you service Rhinebeck and Millbrook estate / horse-country properties?
- What does Dutchess County intercom repair typically cost?
- Do you handle Fishkill and Wappingers suburban + commercial corridors?
- Are your repairs guaranteed?
- What brands do you repair in Dutchess County?
- Do you service eastern Dutchess Harlem Valley rural towns?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Dutchess County?
- [schema] Do you service Dutchess County single-family homes?
- [schema] Do you service Poughkeepsie city and Vassar/Marist college rentals?
- [schema] Do you service Beacon arts-district mixed-use and historic buildings?
- [schema] Do you service Rhinebeck and Millbrook estate / horse-country properties?
- [schema] Do you handle Fishkill and Wappingers suburban + commercial corridors?
- [schema] What does Dutchess County intercom repair typically cost?
- [schema] Can you upgrade my Dutchess building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Dutchess County?
- [schema] Do you service Hyde Park, the CIA and FDR/Vanderbilt corridor?
- [schema] Do you service eastern Dutchess Harlem Valley rural towns?

### intercom-repair-hudson-valley — 47 questions
- Broken Intercom or Gate? Real Quote in 60 Seconds.
- 🚨 Need Intercom or Gate Repair Today?
- What does it really cost to fix a gate intercom in Bedford or Mahopac? Cost
- Why is HV intercom repair more expensive than NYC pricing I see online? Cost
- My intercom died after the ice storm — is repair worth it or just replace? Cost
- How do I find a real licensed HV intercom guy and not get burned? Quality/Trust
- Is it worth the extra cost vs hiring a local handyman in Kingston or Newburgh? Quality/Trust
- Can I just program my DoorKing 1812 directory myself? DIY/Pro
- My handyman "fixed" the gate intercom and now nothing works — recoverable? DIY/Pro
- Why does my gate intercom ring but no one's pressing the button? Technical
- Visitors can hear me but I can't hear them at the gate — what's dead? Technical
- My residential video intercom monitor went black after a thunderstorm. Fixable? Technical
- We bought a property in Rhinebeck with an old Nutone intercom — can it be saved? Residential/Commercial
- Our medical office in White Plains needs HIPAA-aware intercom — does that exist? Residential/Commercial
- Show up, charge $400, intercom still broken — what's my recourse? Complaints
- Got a $22k quote to "completely replace" our community gate system. Is that real? Complaints
- Why is my gate intercom not calling my phone?
- Where do I get an intercom repaired in Westchester?
- How much to convert a landline gate intercom to cellular?
- Can I use a video doorbell for my driveway gate?
- Why is the gate intercom directory full?
- How long does HV intercom repair take?
- How fast can you respond to intercom repair in the Hudson Valley?
- Do you service gated driveway intercoms?
- Can you fix my gate intercom if Verizon shut off our landline?
- What brands do you repair in the Hudson Valley?
- My intercom died after a nor'easter — does my home insurance cover it?
- Do you service estates with long driveways and gate-to-house intercoms?
- What does Hudson Valley intercom repair typically cost?
- Do you work with co-op boards, condo associations, and HOAs?
- Are your repairs guaranteed?
- Can you repair school and municipal intercoms?
- Do you offer maintenance contracts for HV properties?
- Can my video intercom connect to my smartphone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in the Hudson Valley?
- [schema] Do you service gated driveway intercoms?
- [schema] Can you fix my gate intercom if Verizon shut off our landline?
- [schema] What brands do you repair in the Hudson Valley?
- [schema] My intercom died after a nor'easter — is that covered by my home insurance?
- [schema] Do you service estates with long driveways and gate-to-house intercoms?
- [schema] What does Hudson Valley intercom repair typically cost?
- [schema] Do you work with co-op boards, condo associations, and HOAs in the Hudson Valley?
- [schema] Are your repairs guaranteed?
- [schema] Can you repair school and municipal intercoms in Westchester and beyond?
- [schema] Do you offer maintenance contracts for Hudson Valley properties?
- [schema] Can my video intercom connect to my smartphone after repair?

### intercom-repair-long-island — 47 questions
- Broken Intercom or Gate? Real Quote in 60 Seconds.
- 🚨 Need Intercom or Gate Repair Today?
- What does it cost to fix a gate intercom in Old Westbury or Brookville? Cost
- Why is Hamptons intercom repair more expensive than Nassau? Cost
- My intercom died after Hurricane Henri / Hurricane Lee / the latest nor'easter — repair or insurance claim? Cost
- How do I find a real licensed LI intercom guy and not get burned? Quality/Trust
- Is it worth more than hiring a Babylon or Patchogue handyman? Quality/Trust
- Can I just reprogram my DoorKing 1812 directory myself? DIY/Pro
- My handyman "fixed" the gate and now nothing works — can it be reversed? DIY/Pro
- Why does my gate panel keep dying every 3 years near the beach? Technical
- Visitors can hear me but I can't hear them at the gate — what's dead? Technical
- Why is my Aiphone JO black-screen after a thunderstorm? Technical
- We bought a Garden City house with a Nutone intercom from 1978 — save it? Residential/Commercial
- Our medical office in Lake Success needs HIPAA-compatible intercom — exists? Residential/Commercial
- Tech showed up in Sag Harbor, charged $500, intercom still broken — recourse? Complaints
- Got a $28k quote to "modernize" our HOA gate system. Real or rip-off? Complaints
- Why is my Long Island gate intercom not calling my phone?
- Where do I get an intercom repaired in Nassau or Suffolk?
- Can salt air really kill my intercom?
- How much to convert a landline gate intercom to cellular?
- Why is the gate intercom directory full?
- Can I keep my existing wiring during an upgrade?
- How fast can you respond to intercom repair on Long Island?
- Do you service gated driveway intercoms on Long Island?
- Can you fix coastal salt-air corrosion damage?
- What brands do you repair on Long Island?
- My intercom died after a nor'easter — does insurance cover it?
- Do you service Gold Coast estates with long driveways?
- What does Long Island intercom repair typically cost?
- Do you work with HOAs, condo boards, and co-op boards on LI?
- Are your repairs guaranteed?
- Can you repair LI school and municipal intercoms?
- Do you offer maintenance contracts for LI properties?
- Can my video intercom connect to my smartphone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair on Long Island?
- [schema] Do you service gated driveway intercoms on Long Island?
- [schema] Can you fix coastal salt-air corrosion damage on intercoms?
- [schema] What brands do you repair on Long Island?
- [schema] My intercom died after a nor'easter — is that covered by insurance?
- [schema] Do you service Gold Coast estates with long driveways?
- [schema] What does Long Island intercom repair typically cost?
- [schema] Do you work with HOAs, condo boards, and co-op boards on Long Island?
- [schema] Are your repairs guaranteed?
- [schema] Can you repair Long Island school and municipal intercoms?
- [schema] Do you offer maintenance contracts for LI properties?
- [schema] Can my video intercom be connected to my smartphone after repair?

### intercom-repair-manhattan — 47 questions
- Broken Intercom? Real Quote in 60 Seconds.
- 🚨 Need Manhattan Intercom Repair Today?
- How much to fix a broken buzzer in a UWS pre-war co-op? Cost
- Why do Manhattan intercom repair quotes vary so wildly? Cost
- My Manhattan landlord says intercom repair is "too expensive" — what do I push for? Cost
- How do I find a licensed Manhattan intercom guy approved for my co-op? Quality/Trust
- Is it worth more than hiring a building handyman for a quick fix? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my UES intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them — what part is dead? Technical
- Door release works for some apartments, not mine — wiring or station? Technical
- My Manhattan landlord ignored my intercom complaint 6 weeks. HPD next steps? Landlord/Tenant
- I'm a small Manhattan landlord with a 12-unit Inwood walk-up — what do I legally owe tenants? Landlord/Tenant
- Tech showed up in SoHo, charged $400, intercom still broken — recourse? Complaints
- Got quoted $18k to "upgrade" our pre-war system when one station died. Reasonable? Complaints
- Why is my Manhattan apartment intercom not working?
- Where can I get my Manhattan intercom fixed?
- How long does Manhattan co-op approval take for intercom work?
- Can a doorman building intercom be upgraded without disrupting service?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Manhattan?
- Do you have experience with Manhattan co-op boards?
- Can you work in doorman buildings without disrupting residents?
- Do you service pre-war Lee Dan and M&S systems still in Manhattan walk-ups?
- Can you upgrade my Manhattan intercom without rewiring the whole building?
- My Manhattan landlord ignored the broken intercom — what's HPD's role?
- Do you provide HPD Certificate of Correction documentation?
- What does Manhattan intercom repair typically cost?
- Are your repairs guaranteed?
- What brands do you repair in Manhattan?
- Can you preserve landmark-protected facades when replacing lobby panels?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Manhattan?
- [schema] Do you have experience with Manhattan co-op boards?
- [schema] Can you work in doorman buildings without disrupting residents?
- [schema] Do you service pre-war Lee Dan and M&S systems still in Manhattan walk-ups?
- [schema] Can you upgrade my Manhattan intercom without rewiring the whole building?
- [schema] My Manhattan landlord ignored the broken intercom for weeks — what's HPD's role?
- [schema] Do you provide HPD Certificate of Correction documentation?
- [schema] What does Manhattan intercom repair typically cost?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Manhattan?
- [schema] Can you preserve landmark-protected facades when replacing lobby panels?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-nassau-county — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Nassau County Intercom Repair Today?
- How much to fix a video intercom on my Five Towns or Hewlett home? Cost
- Why do Nassau intercom repair quotes vary so wildly? Cost
- I'm a Nassau homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Nassau intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Nassau handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Great Neck co-op lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Long Beach building — what is dead? Technical
- Why does my Long Beach barrier island intercom keep dying every 3 years? Technical
- I run a Nassau commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Nassau small commercial property owner with a 12-unit Hempstead mixed-use — what do I owe tenants? Residential/Commercial
- Tech showed up in Garden City, charged $400, intercom still broken — recourse? Complaints
- Got quoted $18k to "completely replace" our 20-unit Hempstead system when one apt died. Reasonable? Complaints
- Why is my Nassau home intercom not working?
- Where can I get my Nassau intercom fixed?
- How fast is same-day in Nassau?
- Can my Gold Coast gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Nassau County?
- Do you service Nassau County single-family and 2-family homes?
- Do you handle Nassau commercial buildings and office parks?
- Can you upgrade my Nassau building without rewiring?
- Do you service Gold Coast estate gate intercoms?
- Do you fix coastal-corroded intercoms in Long Beach and the South Shore?
- What does Nassau County intercom repair typically cost?
- Are post-Hurricane Sandy 2013-2015 systems aging out in Nassau?
- Are your repairs guaranteed?
- What brands do you repair in Nassau County?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Nassau County?
- [schema] Do you service Nassau County single-family and 2-family homes?
- [schema] Do you handle Nassau commercial buildings and office parks?
- [schema] Do you service Gold Coast estate gate intercoms?
- [schema] Do you fix coastal-corroded intercoms in Long Beach and the South Shore?
- [schema] Are post-Hurricane Sandy 2013-2015 systems aging out in Nassau?
- [schema] What does Nassau County intercom repair typically cost?
- [schema] Can you upgrade my Nassau building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Nassau County?
- [schema] Do you work with Nassau co-op and condo boards?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-nyc — 47 questions
- Broken Intercom? Get a Real Quote in 60 Seconds.
- 🚨 Need Intercom Repair Today?
- How much does it really cost to fix a broken buzzer in a Brooklyn walk-up? Cost
- Why are NYC intercom repair quotes so wildly different from each other? Cost
- My landlord says intercom repair is "too expensive" — what should I push for? Cost
- How do I find a licensed NYC intercom repair guy who won't ghost me? Quality/Trust
- Is it worth paying more for an NYS-licensed contractor vs an unlicensed handyman? Quality/Trust
- Can I just rewire the apartment station myself with a multimeter? DIY/Pro
- My super "fixed" the lobby panel and now nothing works — can a pro reverse it? DIY/Pro
- Why does my intercom buzz constantly even when nobody's pressing the button? Technical
- Visitors can hear me but I can't hear them — what part is dead? Technical
- Door release works for some apartments but not mine — wiring or station? Technical
- My NYC landlord ignored my intercom complaint for 6 weeks. What's HPD's role? Landlord/Tenant
- I'm a small NYC landlord with a 12-unit Bushwick walk-up — what do I legally owe tenants? Landlord/Tenant
- A tech showed up, charged me $300, intercom still broken. What's my recourse? Complaints
- Got quoted $14k for a "full upgrade" when one apartment station died. Reasonable? Complaints
- Why is my apartment intercom not working?
- Where can I get my intercom fixed in NYC?
- When should I replace instead of repair?
- What does an NYC intercom repair cost on average?
- How long does an intercom repair take?
- Who is responsible — tenant or landlord?
- How fast can you respond to an intercom repair call in NYC?
- Do you service Aiphone, Comelit, Mircom, ButterflyMX, and Lee Dan?
- Can you repair my building's intercom if replacement parts are discontinued?
- Do you work with co-op boards and property managers?
- Is intercom repair covered under my original installation warranty?
- What's the difference between repair and replacement for old systems?
- Can you keep my existing wiring during an upgrade?
- Do you provide an HPD Certificate of Correction after repair?
- Are your intercom repairs guaranteed?
- Do you handle commercial intercom repair for offices, warehouses, and schools?
- Can my video intercom be connected to my phone after repair?
- Do you offer maintenance contracts for buildings?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to an intercom repair call in NYC?
- [schema] Do you service Aiphone, Comelit, Mircom, ButterflyMX, and Lee Dan?
- [schema] Can you repair my building's intercom if replacement parts are discontinued?
- [schema] Do you work with co-op boards and property managers?
- [schema] Is intercom repair covered under my original installation warranty?
- [schema] What's the difference between repair and replacement for old systems?
- [schema] Can you keep my existing wiring during an upgrade?
- [schema] Do you provide an HPD Certificate of Correction after repair?
- [schema] Are your intercom repairs guaranteed?
- [schema] Do you handle commercial intercom repair for offices, warehouses, and schools?
- [schema] Can my video intercom be connected to my phone after repair?
- [schema] Do you offer maintenance contracts for buildings?

### intercom-repair-orange — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Orange County Intercom Repair Today?
- How much to fix a video intercom on my Cornwall or Warwick home? Cost
- Why do Orange County intercom repair quotes vary so wildly? Cost
- I'm an Orange homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Orange County intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Orange handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Kiryas Joel walk-up lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Newburgh building — what is dead? Technical
- Why does my Newburgh waterfront or Cornwall-on-Hudson intercom keep dying every 3 years? Technical
- I run an Orange commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm an Orange small commercial property owner with a 16-unit Newburgh walk-up — what do I owe tenants? Residential/Commercial
- Tech showed up in Goshen, charged $400, intercom still broken — recourse? Complaints
- Got quoted $18k to "completely replace" our 20-unit Newburgh system when one apt died. Reasonable? Complaints
- Why is my Orange home intercom not working?
- Where can I get my Orange intercom fixed?
- How fast is same-day in Orange?
- Can my Tuxedo Park or Warwick gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Orange County?
- Do you service Orange County single-family and 2-family homes?
- Do you service Newburgh Hudson historic district properties?
- Can you upgrade my Orange building without rewiring?
- Do you service Kiryas Joel, Monroe, Woodbury Orthodox multi-family?
- Do you service Tuxedo Park gated estate properties?
- What does Orange County intercom repair typically cost?
- Do you service Middletown and Goshen commercial corridors?
- Are your repairs guaranteed?
- What brands do you repair in Orange County?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Orange County?
- [schema] Do you service Orange County single-family and 2-family homes?
- [schema] Do you service Newburgh Hudson historic district properties?
- [schema] Do you service Kiryas Joel, Monroe, Woodbury Orthodox multi-family?
- [schema] Do you service Tuxedo Park gated estate properties?
- [schema] Do you service Middletown and Goshen commercial corridors?
- [schema] Do you service Warwick wineries and Black Dirt agricultural commercial?
- [schema] What does Orange County intercom repair typically cost?
- [schema] Can you upgrade my Orange building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Orange County?
- [schema] Do you service West Point area and Highland Falls?

### intercom-repair-putnam-county — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Putnam County Intercom Repair Today?
- How much to fix a video intercom on my Mahopac or Carmel home? Cost
- Why do Putnam County intercom repair quotes vary so wildly? Cost
- I'm a Putnam homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Putnam County intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Putnam handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Brewster walk-up lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Brewster building — what is dead? Technical
- Why does my Cold Spring or Garrison Hudson-facing intercom keep dying every 3 years? Technical
- I run a Putnam commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Putnam small commercial property owner with a 12-unit Brewster walk-up — what do I owe tenants? Residential/Commercial
- Tech showed up in Mahopac, charged $400, intercom still broken — recourse? Complaints
- Got quoted $15k to "completely replace" our 14-unit Brewster system when one apt died. Reasonable? Complaints
- Why is my Putnam home intercom not working?
- Where can I get my Putnam intercom fixed?
- How fast is same-day in Putnam?
- Can my Garrison or rural Putnam gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Putnam County?
- Do you service Putnam County single-family and lake-community homes?
- Do you service Cold Spring and Garrison Hudson historic villages?
- Can you upgrade my Putnam building without rewiring?
- Do you service Garrison Hudson River estate properties?
- Do you service Putnam Valley, Kent, Patterson rural watershed properties?
- What does Putnam County intercom repair typically cost?
- Do you handle Brewster commercial and Metro-North area?
- Are your repairs guaranteed?
- What brands do you repair in Putnam County?
- Do you set up remote door monitoring for weekend/seasonal homes?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Putnam County?
- [schema] Do you service Putnam County single-family and lake-community homes?
- [schema] Do you service Cold Spring and Garrison Hudson historic villages?
- [schema] Do you service Garrison Hudson River estate properties?
- [schema] Do you service Putnam Valley, Kent, Patterson rural watershed properties?
- [schema] Do you handle Brewster commercial and Metro-North area?
- [schema] What does Putnam County intercom repair typically cost?
- [schema] Can you upgrade my Putnam building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Putnam County?
- [schema] Do you service lake-community and seasonal/weekend homes?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-queens — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Queens Intercom Repair Today?
- How much to fix a broken buzzer in an Astoria or Sunnyside walk-up? Cost
- Why are Queens intercom repair quotes so wildly different? Cost
- My Jackson Heights landlord says intercom repair is "too expensive" — what do I push for? Cost
- How do I find a licensed Queens intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Queens handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the lobby panel in our Forest Hills building and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors can hear me but I can't hear them in our Astoria walk-up — what part is dead? Technical
- Why does my Belle Harbor intercom keep dying every 3 years? Technical
- My Queens landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
- I'm a small Queens landlord with a 12-unit Corona walk-up — what do I owe tenants? Landlord/Tenant
- Tech showed up in Flushing, charged $400, intercom still broken — recourse? Complaints
- Got quoted $19k to "completely replace" our 24-unit Astoria system when one apt died. Reasonable? Complaints
- Why is my Queens apartment intercom not working?
- Where can I get my Queens intercom fixed?
- How fast is same-day in Queens?
- Can my LIC ButterflyMX be fixed without replacing it?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Queens?
- Do you service Queens co-ops in Jackson Heights, Forest Hills, and Rego Park?
- Do you service pre-war Lee Dan and M&S in Queens walk-ups?
- Can you upgrade my Queens building without rewiring?
- My Queens landlord ignored the broken intercom — what's HPD's role?
- Do you work in LIC luxury new construction?
- What does Queens intercom repair typically cost?
- Do you fix coastal-corroded intercoms in Far Rockaway and Breezy Point?
- Are your repairs guaranteed?
- What brands do you repair in Queens?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Queens?
- [schema] Do you service Queens co-ops in Jackson Heights, Forest Hills, and Rego Park?
- [schema] Do you service pre-war Lee Dan and M&S in Queens walk-ups?
- [schema] Do you work in LIC luxury new construction?
- [schema] Do you fix coastal-corroded intercoms in Far Rockaway and Breezy Point?
- [schema] My Queens landlord ignored the broken intercom — what is HPD role?
- [schema] What does Queens intercom repair typically cost?
- [schema] Can you upgrade my Queens building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Queens?
- [schema] Do you provide HPD Certificate of Correction documentation?
- [schema] Can my video intercom connect to my phone after repair?

### intercom-repair-rockland — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Rockland County Intercom Repair Today?
- How much to fix a video intercom on my New City or Nanuet home? Cost
- Why do Rockland intercom repair quotes vary so wildly? Cost
- I'm a Rockland homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Rockland intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Rockland handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Spring Valley walk-up lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Nyack building — what is dead? Technical
- Why does my Nyack or Piermont Hudson-facing intercom keep dying every 3 years? Technical
- I run a Rockland commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Rockland small commercial property owner with a 14-unit Spring Valley walk-up — what do I owe tenants? Residential/Commercial
- Tech showed up in Pearl River, charged $400, intercom still broken — recourse? Complaints
- Got quoted $17k to "completely replace" our 18-unit Monsey system when one apt died. Reasonable? Complaints
- Why is my Rockland home intercom not working?
- Where can I get my Rockland intercom fixed?
- How fast is same-day in Rockland?
- Can my Pomona or Wesley Hills gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Rockland County?
- Do you service Rockland County single-family and 2-family homes?
- Do you service Ramapo, Monsey, Spring Valley multi-family housing?
- Can you upgrade my Rockland building without rewiring?
- Do you service Hudson River village properties (Nyack, Piermont, Tappan)?
- Do you service Pomona, Wesley Hills, Tallman estate properties?
- What does Rockland County intercom repair typically cost?
- Do you handle Pearl River commercial corridor and office parks?
- Are your repairs guaranteed?
- What brands do you repair in Rockland County?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Rockland County?
- [schema] Do you service Rockland County single-family and 2-family homes?
- [schema] Do you service Ramapo, Monsey, Spring Valley multi-family housing?
- [schema] Do you service Hudson River village properties (Nyack, Piermont, Tappan)?
- [schema] Do you service Pomona, Wesley Hills, Tallman estate properties?
- [schema] Do you handle Pearl River commercial corridor and office parks?
- [schema] What does Rockland County intercom repair typically cost?
- [schema] Can you upgrade my Rockland building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Rockland County?
- [schema] Do you service Stony Point and Haverstraw northern Rockland?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-staten-island — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Staten Island Intercom Repair Today?
- How much to fix a video intercom on my Tottenville or Annadale home? Cost
- Why do Staten Island intercom repair quotes vary so wildly? Cost
- My St. George landlord says intercom repair is "too expensive" — what do I push for? Cost
- How do I find a licensed Staten Island intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Staten Island handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the St. George lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Hylan Blvd building — what is dead? Technical
- Why does my Great Kills outdoor intercom keep dying every 3 years? Technical
- My Staten Island landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
- I'm a small Staten Island landlord with a 10-unit Stapleton walk-up — what do I owe tenants? Landlord/Tenant
- Tech showed up in New Springville, charged $400, intercom still broken — recourse? Complaints
- Got quoted $14k to "completely replace" our 16-unit Hylan Blvd system when one apt died. Reasonable? Complaints
- Why is my Staten Island home intercom not working?
- Where can I get my Staten Island intercom fixed?
- How fast is same-day on Staten Island?
- Can my single-family home video intercom be upgraded easily?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair on Staten Island?
- Do you service Staten Island 1-2 family homes?
- Do you handle Hylan Blvd commercial and mixed-use buildings?
- Can you upgrade my Staten Island building without rewiring?
- My Staten Island landlord ignored the broken intercom — what is HPD role?
- Do you service Todt Hill / Emerson Hill estate gate intercoms?
- What does Staten Island intercom repair typically cost?
- Do you fix Hurricane Sandy-zone coastal intercom damage?
- Are your repairs guaranteed?
- What brands do you repair on Staten Island?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair on Staten Island?
- [schema] Do you service Staten Island 1-2 family homes?
- [schema] Do you handle Hylan Blvd commercial and mixed-use buildings?
- [schema] Do you fix Hurricane Sandy-zone coastal intercom damage?
- [schema] Do you service Todt Hill and Emerson Hill estate gate intercoms?
- [schema] My Staten Island landlord ignored the broken intercom — what is HPD role?
- [schema] What does Staten Island intercom repair typically cost?
- [schema] Can you upgrade my Staten Island building without rewiring?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair on Staten Island?
- [schema] Do you provide HPD Certificate of Correction documentation?
- [schema] Can my video intercom be connected to my phone after repair?

### intercom-repair-suffolk-county — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Suffolk County Intercom Repair Today?
- How much to fix a video intercom on my Bay Shore or Smithtown home? Cost
- Why do Suffolk intercom repair quotes vary so wildly? Cost
- I'm a Suffolk homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Suffolk intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Suffolk handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Stony Brook co-op lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them on our Hamptons rental property — what is dead? Technical
- Why does my Fire Island or Westhampton Beach intercom keep dying every 3 years? Technical
- I run a Suffolk commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Suffolk small commercial property owner with a 10-unit Patchogue mixed-use — what do I owe tenants? Residential/Commercial
- Tech showed up in Huntington, charged $400, intercom still broken — recourse? Complaints
- Got quoted $20k to "completely replace" our 18-unit Bay Shore system when one apt died. Reasonable? Complaints
- Why is my Suffolk home intercom not working?
- Where can I get my Suffolk intercom fixed?
- How fast is same-day in Suffolk?
- Can my Lloyd Harbor or Hamptons gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Suffolk County?
- Do you service Suffolk County single-family and 2-family homes?
- Do you service the Hamptons and East End?
- Can you upgrade my Suffolk building without rewiring?
- Do you service Lloyd Harbor and Cold Spring Harbor Sound waterfront estates?
- Do you fix coastal-corroded intercoms in Westhampton Beach and Fire Island?
- What does Suffolk County intercom repair typically cost?
- Are post-Hurricane Sandy 2013-2015 systems aging out in Suffolk?
- Are your repairs guaranteed?
- What brands do you repair in Suffolk County?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Suffolk County?
- [schema] Do you service Suffolk County single-family and 2-family homes?
- [schema] Do you service the Hamptons and East End?
- [schema] Do you service Lloyd Harbor and Cold Spring Harbor Sound waterfront estates?
- [schema] Do you fix coastal-corroded intercoms in Westhampton Beach and Fire Island?
- [schema] Are post-Hurricane Sandy 2013-2015 systems aging out in Suffolk?
- [schema] What does Suffolk County intercom repair typically cost?
- [schema] Can you upgrade my Suffolk building without rewiring?
- [schema] Do you handle Stony Brook University and medical campus intercoms?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Suffolk County?
- [schema] Do you work with Suffolk co-op and condo boards?

### intercom-repair-westchester — 47 questions
- Broken Buzzer? Real Quote in 60 Seconds.
- 🚨 Need Westchester County Intercom Repair Today?
- How much to fix a video intercom on my Scarsdale or Bronxville home? Cost
- Why do Westchester intercom repair quotes vary so wildly? Cost
- I'm a Westchester homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
- How do I find a licensed Westchester intercom guy who won't ghost me? Quality/Trust
- Is it worth more than hiring a local Westchester handyman? Quality/Trust
- Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
- My super "fixed" the Yonkers co-op lobby panel and now nothing works — recoverable? DIY/Pro
- Why does my intercom buzz constantly with no one pressing the button? Technical
- Visitors hear me but I can't hear them in our Larchmont building — what is dead? Technical
- Why does my Larchmont or Mamaroneck Sound Shore intercom keep dying every 3 years? Technical
- I run a Westchester commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
- I'm a Westchester small commercial property owner with a 16-unit Yonkers walk-up — what do I owe tenants? Residential/Commercial
- Tech showed up in White Plains, charged $400, intercom still broken — recourse? Complaints
- Got quoted $19k to "completely replace" our 24-unit Yonkers system when one apt died. Reasonable? Complaints
- Why is my Westchester home intercom not working?
- Where can I get my Westchester intercom fixed?
- How fast is same-day in Westchester?
- Can my Bedford or Pound Ridge gate intercom be converted from landline to cellular?
- What's the cost difference between repair and full upgrade?
- Who's responsible — tenant or landlord?
- How fast can you respond to intercom repair in Westchester County?
- Do you service Westchester County co-ops and condos?
- Do you service Bedford, Pound Ridge, and North Salem horse country estates?
- Can you upgrade my Westchester building without rewiring?
- Do you handle Sound Shore Larchmont and Mamaroneck waterfront properties?
- Do you service Hudson River town properties (Tarrytown, Sleepy Hollow, Irvington)?
- What does Westchester County intercom repair typically cost?
- Do you service White Plains commercial buildings and office parks?
- Are your repairs guaranteed?
- What brands do you repair in Westchester County?
- Do you provide HPD Certificate of Correction documentation?
- Can my video intercom connect to my phone after repair?
- Still Have Questions? Talk to a Tech, Not a Sales Rep.
- [schema] How fast can you respond to intercom repair in Westchester County?
- [schema] Do you service Westchester County co-ops and condos?
- [schema] Do you service Bedford, Pound Ridge, and North Salem horse country estates?
- [schema] Do you handle Sound Shore Larchmont and Mamaroneck waterfront properties?
- [schema] Do you service Hudson River town properties (Tarrytown, Sleepy Hollow, Irvington)?
- [schema] What does Westchester County intercom repair typically cost?
- [schema] Can you upgrade my Westchester building without rewiring?
- [schema] Do you service White Plains commercial buildings and office parks?
- [schema] Are your repairs guaranteed?
- [schema] What brands do you repair in Westchester County?
- [schema] Do you service Scarsdale, Bronxville, and Rye affluent residential?
- [schema] Can my video intercom be connected to my phone after repair?


## Question register — intercom-repair-putnam-county (REBUILT 2026-10-18) — final
Q&A (section "Intercom Repair in Putnam County: Questions Answered"), 19 H3 + emergency H2 "Putnam Gate or Door Station Dead After the Storm?":
*Gates, Call Boxes and Long Cable Runs*
1. Our road association has one call box at the gate for nine houses, and it now rings every house except one. Where is the fault likely to be?
2. A plow keeps clipping the post our gate call box stands on. What mounting holds up to a Putnam winter?
3. The cable from the house to the gate runs about 600 feet underground. Can a break be found without digging up the whole driveway?
4. The gate opens when someone enters a code at the keypad, but pressing the call button on the same box does nothing. Why would one half work and not the other?
*Lake Houses and Weekend Homes*
5. Every spring when we open the lake house, the door station has stopped working. What does a winter in an empty house do to it?
6. Should the intercom’s power be switched off when we close the house for the season?
7. Water runs down the face of our porch door station after every heavy rain. Is it already damaged inside?
8. Ants and wasps keep moving into the door station on our deck. What stops them?
*Storms, Power Cuts and Lightning*
9. Since the power came back after the storm, the indoor monitors light up but the front door will not release. How can one part survive and not the other?
10. Our standby generator takes a few seconds to start, and the intercom comes back confused every time. Can it ride through the switchover?
11. The garage is a separate building and its door station died in a thunderstorm. What protection actually helps on a run between buildings?
*Condos, Senior Buildings and Shared Street Doors*
12. In our condo complex, does the association or the unit owner pay when one resident’s monitor fails?
13. Several residents in our senior building say the caller at the lobby is too faint to understand. What can be adjusted before anything is replaced?
14. Can a resident who is hard of hearing get a light or a screen alert when the lobby calls?
15. Our apartment sits over a shop on Main Street and we share the street door. Can the shop’s daytime door release be kept separate from our buzzer?
16. Does the New York City intercom rule for apartment buildings apply to a rental building in Brewster or Carmel?
*Doors, Strikes and Cold Weather*
17. When the door will not buzz open, how do you tell whether the intercom or the door strike is to blame?
18. In January our building door only opens if someone shoves it while the buzzer sounds. Is that the strike or the door?
*Network and Cloud-Connected Panels*
19. Our cloud-connected entry panel shows offline in the manager’s portal although its screen is lit. What usually causes that out here?
20. The intercom app shows the door camera, but the picture freezes whenever two of us open it at once. Is the panel failing?

FAQ (visible == FAQPage schema):
1. What should we gather before calling so the visit is shorter?
2. Can the entry stay secure while you work on a building’s intercom?
3. Do we need an electrician as well as an intercom technician?
4. Will you leave a record of the wiring for whoever works on it next?
5. Can you add temporary entry codes for a contractor or dog walker and remove them later?
6. We have spare handsets in a box from the original installation. Are they worth keeping?
7. Can the intercom also open a garage door or a side gate?
8. Can the system show us who was let in and when?
9. What happens to the door if the intercom loses power?
10. Can you look at the intercom at a property we are about to buy?

### Semantic de-dup notes (read by meaning against the register above)
Deliberately NOT asked as questions because siblings already carry the intent: cost/"typical cost", response time, brands, guarantee, phone/app connection after repair, repair vs replace, upgrade without rewiring, discontinued parts, landline-to-cellular gate conversion ("Verizon shut off our landline" — HV hub), gate "not calling my phone" (HV hub), ghost rings / buzzing with no one pressing, can hear me but can't hear them, monitor black after thunderstorm, insurance after nor'easter, HPD/landlord, tenant vs landlord responsibility, DIY handset swap, handyman recourse, licensing for commercial work, maintenance contracts, HOA/condo service, seasonal-home remote monitoring, landmark facades. Those topics appear only in body text (pricing table, §8.5, §10.5) or are omitted.
Borderline pairs for the coordinator: "monitors light up but door won't release after the power came back" vs HV "monitor went black after a thunderstorm" (different symptom and part); "garage door station died in a thunderstorm — what protection helps" vs HV same storm topic (prevention vs fixability); "condo: association or unit owner pays for a failed monitor" vs old-Putnam/Bronx "Who's responsible — tenant or landlord?" (condo common-element split, not landlord-tenant); "ants and wasps in the door station — what stops them" vs HV ghost-ring answer that mentions insects (prevention vs symptom); "cloud panel shows offline" vs HV "gate intercom not calling my phone" (panel/server connection vs phone delivery).

### Build notes
- check_page.py: PASS (full, with registration — existing sibling back-links and hub link already point to /intercom-repair-putnam-county). 13,924 rendered words; title 56; meta 158; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 194,158 B (siblings 80–96 KB).
- Masked-geo block similarity (p/li/h2/h3/td/figcaption ≥8 masked words, word-level SequenceMatcher) vs all 14 intercom-repair siblings: only block ≥0.65 is the blueprint-fixed H2 "What AI Gets Wrong About Intercom Repair in [Area]" (0.62–0.78 vs "What Google AI Overview gets wrong about … pricing"). Next highest 0.57 (diagnostic table cell). Thesis: Putnam intercoms are gate call boxes, lake-house door stations, condo/55+/senior entries and shared Main Street doors — repair is about distance, cold, power/lightning, phone-line changes, and the fact that NYC's MDL/HPD regime does not apply by default.


## Staten Island — merged 2026-10-18 from the Staten Island build (silo findings, question register incl. this page's questions, local section)

## Intercom Repair — silo research (INCOMING, from the Staten Island rebuild)

Created 2026-10-18 by the REBUILD subagent for `intercom-repair-staten-island` (queue line: `REBUILD | intercom-repair-staten-island | Intercom Repair | Staten Island | up /intercom-repair-nyc | (347) 934-8335 | GBP Brooklyn`).

**Why this file is named `_incoming-…`:** `research/intercom-repair.md` did not exist when this run started, and a concurrent run (`intercom-repair-putnam-county`) may create it. To avoid a write collision this run writes here; the main run should merge Part 1 + the question register + the `## Staten Island` section into `research/intercom-repair.md`.

Tools used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (`mcp__Firecrawl__firecrawl_scrape`, markdown / summary / directQuote). Shell curl blocked. Rows marked "carried from <file>" were fetched by earlier 2026-10-17/18 Staten Island builds and re-used, not re-fetched.

---

### Part 1 — Silo-wide findings (usable on every intercom-repair page)

#### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only via Firecrawl search (scrape of reddit.com refused for this silo per earlier runs). Rows R1–R6. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP panels. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). Page §10.5 says so and tests seven published claims instead (rows A1–A7). |
| 6–7 | Landmarks / building stock | `## Staten Island` rows SI-H, SI-L. |
| 8 | Bing & DuckDuckGo | `https://html.duckduckgo.com/html/?q=intercom+repair+staten+island` · Firecrawl scrape → "All scraping engines failed". Bing not reachable either. → EMPTY (not accessible in build env). |
| 9–10 | Local news / hyperlocal | SI Advance (silive.com), NYC Comptroller (via silive), NYCEDC, New York YIMBY — rows SI-N. |
| 11 | Yelp 1–3★ | `yelp intercom repair Staten Island review technician never showed buzzer` · Firecrawl search → Yelp search-list pages only (Jericho NY, Burr Ridge IL, Lighthouse Hill SI list, a Yelp Q&A page); no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

#### 1.2 Reddit (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit intercom buzzer not working apartment landlord won't fix NYC` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/10uzqs0/landlord_wont_fix_my_intercom_is_there_any_legal/ | Excerpt: "Call 311 every day until fixed. Landlords are required to keep buzzers in working order if the building has more than 8 units and was built or …" | SI §9 cluster D (tenant side, paraphrased as "residents' advice is to call 311"); not quoted |
| R2 | same | https://www.reddit.com/r/AskNYC/comments/ilvvz3/landlord_wont_fix_buzzer/ | Excerpt: advice to fix it and withhold the cost from rent after a deadline | Background only (legal risk — not repeated on page) |
| R3 | same | https://www.reddit.com/r/AskNYC/comments/17knzko/front_door_buzzer_broken_at_walkup_apartment/ | Excerpt: "File initial complaint with agency. Call 311 …" | Background |
| R4 | `reddit StatenIsland intercom OR buzzer apartment building` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/196ra0z/cost_to_upgrade_buzzer_system_for_low_ride/ | Excerpt: "We have a brand new Internet connected intercom system that pings our phones … Packages are stolen weekly" | SI §9 package-theft H3 (paraphrased, attributed to a NYC renter on r/AskNYC) |
| R5 | same | https://www.reddit.com/r/AskNYC/comments/dcbtmb/apartment_buzzer_wiring/ | Excerpt: "You should not be altering the building intercom without explicit permission in writing from the landlord." | SI §9 two-family H3 (owner-permission point) |
| R6 | same | (no r/StatenIsland thread in results) | r/StatenIsland: no intercom thread surfaced → EMPTY for the local sub | — |

#### 1.3 Law, code and agency (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `NYC Multiple Dwelling Law intercom requirement eight or more apartments HPD intercom violation` · Firecrawl search → scrape (directQuote, pdf) | https://www.nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf | MDL §50-a: class A multiple dwellings erected/converted after Jan 1 1968 with 8+ apartments "shall also be equipped with an intercommunication system" at the self-locking main-entrance door, voice communication and door release from each apartment; pre-1968 class A buildings must install doors + intercom if tenants occupying a majority of apartments request/consent in writing (installation start within 90 days, complete within six months; one year for a municipal housing authority); owner who fails to install and maintain, and any person who wilfully damages/jams the equipment, is guilty of a misdemeanor | SI §5 para 3; §5.5 bullet 3; §8.5 bullet 1; §9 pre-1968 H3; §10.5 H3 3; Sources |
| G2 | same search (excerpt) | https://butterflymx.com/blog/nyc-intercom-law/ | Rule "generally applies to Class A multiple dwellings with eight or more units built or converted after January 1, 1968"; buildings before 1968 "require closer review" | §10.5 H3 3 (as the claim being refined) |
| G3 | `HPD intercom violation class B "intercom" Housing Maintenance Code inoperative` · Firecrawl search → scrape (directQuote) | https://weverit.com/building/ny/new-york/1440-richmond-terrace-staten-island-10310 | Open HPD Class B violation on a Richmond Terrace, Staten Island building, issued 2014-10-06: "§ 27-2005 ADM CODE PROPERLY REPAIR THE BROKEN OR DEFECTIVE INOPERATIVE INTERCOM WITH RETURN BUZZER SYSTEM …" — open about 12 years | SI §5 para 3 (address not named on page); §5.5 bullet 4; Sources |
| G4 | same search (excerpt) | http://www.nycourts.gov/reporter/3dseries/2021/2021_50805.htm | Anumudu v Bennett (2021): court assessed civil penalty for a broken-intercom violation (HMC § 27-2115) | Background (not on page) |
| G5 | `silive.com tenants intercom broken building Staten Island 2025 OR 2026` · Firecrawl search (excerpt) | https://portal.311.nyc.gov/article/?kanumber=KA-01074 | 311 Apartment Maintenance Complaint covers "Doorbells, buzzers, or intercoms that are broken or missing" (apartment and public area) | SI §9 NYCHA/rental H3; §8.5 bullet 2; Sources |
| G6 | `NYCHA how to report repair intercom door MyNYCHA app Customer Contact Center 718-707-7771` · Firecrawl search (excerpts) | https://www.nyc.gov/site/nycha/residents/nycha-repairs-process.page ; https://www.nyc.gov/site/nycha/residents/customer-contact-center.page | Building repairs incl. broken lobby doors and locks: CCC (718) 707-7771 or MyNYCHA app/website; CCC 24/7 for emergencies, routine scheduling Mon–Fri 6 AM–midnight | SI §9 NYCHA H3; Sources |
| G7 | carried from floodlight-camera-installation.md (silo G1) | https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-electrical.page | Line-voltage electrical work in NYC needs a licensed master electrician + DOB permit | SI §8.5 bullet 3 (120-V feed to a transformer or strike power supply) |

#### 1.4 Equipment, phone lines, cost guides (feed §10.5)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `intercom repair cost apartment building handset lobby panel` · Firecrawl search (excerpt) | https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ | "Apartment intercom replacement often starts around $2,200 to $5,000 for a small building, while minor repairs typically run $150 to $400." | §10.5 H3 1 |
| A2 | same (excerpt) | https://www.uasecurity.com/intercom-repair-cost-nyc.htm | NYC competitor: "many qualifying common, accessible apartment intercom and buzzer repairs … fall within a $150–$250 flat-rate range" | §10.5 H3 2 (competitor not named on page; "flat-rate" claim tested) |
| A3 | same (excerpt) | https://www.connextivity.com/insights/intercom-repair-replacement-nyc | "Component replacements for apartment stations, panel components, or power supplies typically run $500 to $1,500." | Background |
| A4 | `Aiphone discontinued intercom models replacement GT JK LEF compatible` · Firecrawl search → scrape (summary) | https://www.seclock.com/education/entry/aiphone-discontinuing-jk-series | Aiphone JK Series discontinued effective Sept 30 2019; no direct component replacements; JO and IS series named as alternatives | §10.5 H3 5; §9 high-ranch H3 (no — kept to §10.5); Sources |
| A5 | `Verizon copper landline retirement New York 2025 PSC elevator gate call box phone lines` · Firecrawl search → scrape | https://saugertiesny.gov/verizons-proposal-retire-copper | Sept 28 2026: Verizon seeking FCC approval to retire POTS for portions of New York; discontinuance "on or after November 30, 2026", not a single statewide date; customers get notice of their specific date; FCC Docket No. 26-252; POTS line powered from the central office | SI §9 call-box H3 (statement heading); §10.5 H3 6; Sources |
| A6 | same (excerpt) | https://www.news10.com/news/verizon-moving-away-from-copper-landlines-what-customers-need-to-know/ | Fewer than 3% of Verizon customers nationwide still on copper; if no viable replacement, copper stays | §9 call-box section |
| A7 | `cloud video intercom stops working when building internet goes down cellular backup ButterflyMX offline` · Firecrawl search (excerpts) | https://butterflymx.com/blog/cloud-based-video-intercom/ ; https://butterflymx.com/blog/butterflymx-bluetooth/ | Whether a cloud intercom works during an internet outage "depends on the system's documented local-fallback design"; ButterflyMX offers Bluetooth fallback for swipe-to-open on compatible hardware | §9 internet-down H3; §10.5 H3 7 |
| A8 | same search (excerpt) | https://butterflymx.com/blog/intercom-not-working/ | Manufacturer troubleshooting: disconnected power or weak Wi-Fi first | §10.5 H3 4 |

#### 1.5 Five keyword layers (silo)
- **Service:** intercom repair, buzzer repair, door entry repair, video intercom repair, call box repair, door release repair, intercom service.
- **Problem:** intercom not working, buzzer not ringing, door won't unlock from apartment, no audio / one-way audio, constant buzzing, panel dead after storm, app not ringing, gate call box dead after phone-line change.
- **Technology:** 2-wire / multi-wire audio, transformer and power supply, electric strike, maglock, mullion keypad, telephone-entry call box (POTS / cellular), IP/SIP video door station, cloud intercom app, PoE, Bluetooth fallback.
- **Industry / property:** two-family houses, townhouse condominium associations, garden apartments, walk-ups (8+ units, MDL §50-a), public housing (NYCHA — refer out), new rental buildings, medical offices and storefronts.
- **Geographic (SI only):** Staten Island, North Shore (St. George, Tompkinsville, Stapleton, New Brighton, West Brighton, Port Richmond, Mariners Harbor), Mid-Island, East Shore, South Shore, Bay Street, Richmond Terrace, Hylan Boulevard, Forest Avenue, Victory Boulevard, Richmond Avenue.

#### 1.6 Prices (silo) — basis for every area page
Brooklyn page (`intercom-repair-brooklyn.html`) and NYC hub (`intercom-repair-nyc.html`) carry the **same base** for the common lines: diagnostic $150–$300; apartment handset $250–$600; lobby panel component $400–$1,200; lobby panel retrofit $1,500–$3,500; transformer/power supply $300–$800; door release strike $350–$900; bus wiring repair $1,000–$3,000; small building full system $4,500–$12,000; mid-size IP system $12,000–$28,000; maintenance contract $600–$2,400/yr. Brooklyn-only lines: house/brownstone video monitor swap $300–$750; marine-grade coastal panel $1,400–$3,800; Mircom TX3 directory rebuild $350–$750. Service/callback rate $195/hr, 3-hr min ($585) — protected, not multiplied.
**FLAG:** old Staten Island page said "pricing matches NYC base" plus a "~$25" Verrazzano toll surcharge on diagnostics — not §9 (1.10×). Rebuild applies §9.

---

### Question register — every question on every Intercom Repair page

Extracted 2026-10-18 from the files on disk (headings, FAQ items and bold Q&A labels containing "?"). The putnam-county entry is the pre-rebuild file (a concurrent run is rebuilding it).

<!-- register -->
### intercom-repair-bronx 18
  - Why do Bronx intercom repair quotes vary so wildly? Cost
  - My Tremont landlord says intercom repair is "too expensive" — what do I push for? Cost
  - How do I find a licensed Bronx intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Bronx handyman for a quick fix? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Co-op City panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors can hear me but I can't hear them in our Fordham building — what part is dead? Technical
  - Why does my City Island intercom keep dying every 3 years? Technical
  - My Bronx landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
  - I'm a small Bronx landlord with a 14-unit Wakefield walk-up — what do I owe tenants? Landlord/Tenant
  - Tech showed up in Parkchester, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $40k to "completely replace" our Co-op City building system when one apt died. Reasonable? Complaints
  - Where can I get my Bronx intercom fixed? Licensed NYS low-voltage contractor based in the Bronx — same-day from our 460 E Fordham Rd HQ. Avoid out-of-state chains.
  - How fast is same-day in the Bronx? 1–3 hours typical — closest possible response since our HQ is in the Bronx. HPD-cited buildings prioritized.
  - Can Co-op City buildings be upgraded without full rewiring? Yes. Aiphone GT and Mircom TX3 retrofit kits reuse existing 2-wire and 6-wire cable. Critical for the 35-building scale.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-brooklyn 18
  - Why do Brooklyn intercom repair quotes vary so wildly? Cost
  - My Bushwick landlord says intercom repair is "too expensive" — what do I push for? Cost
  - How do I find a licensed Brooklyn intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Brooklyn handyman for a quick fix? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors can hear me but I can't hear them — what part is dead? Technical
  - Why does my Brighton Beach intercom keep dying every 3 years? Technical
  - My Brooklyn landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
  - I'm a small Brooklyn landlord with a 14-unit Crown Heights walk-up — what do I owe tenants? Landlord/Tenant
  - Tech showed up in Williamsburg, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $16k to "completely replace" our 22-unit Crown Heights system when one apt died. Reasonable? Complaints
  - Where can I get my Brooklyn intercom fixed? Licensed NYS low-voltage contractor based in Brooklyn — same-day from our Crown Heights shop. Avoid out-of-state chains.
  - How fast is same-day response in Brooklyn? 2–4 hours typical — fastest in NYC since our shop is in Crown Heights. HPD-cited buildings prioritized.
  - Can a brownstone intercom be upgraded without damaging brickwork? Yes. Aiphone JO and Comelit Mini retrofit kits reuse existing vestibule conduit and concealed wiring.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-dutchess-county 15
  - Why do Dutchess County intercom repair quotes vary so wildly? Cost
  - I'm a Dutchess homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Dutchess County intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Dutchess handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Poughkeepsie walk-up lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Poughkeepsie building — what is dead? Technical
  - Why does my Beacon or Poughkeepsie Hudson-facing intercom keep dying every 3 years? Technical
  - I run a Dutchess commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Dutchess small commercial property owner with an 18-unit Poughkeepsie walk-up — what do I owe tenants? Residential/Commercial
  - Tech showed up in Rhinebeck, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $19k to "completely replace" our 22-unit Poughkeepsie system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-hudson-valley 16
  - Why is HV intercom repair more expensive than NYC pricing I see online? Cost
  - My intercom died after the ice storm — is repair worth it or just replace? Cost
  - How do I find a real licensed HV intercom guy and not get burned? Quality/Trust
  - Is it worth the extra cost vs hiring a local handyman in Kingston or Newburgh? Quality/Trust
  - Can I just program my DoorKing 1812 directory myself? DIY/Pro
  - My handyman "fixed" the gate intercom and now nothing works — recoverable? DIY/Pro
  - Why does my gate intercom ring but no one's pressing the button? Technical
  - Visitors can hear me but I can't hear them at the gate — what's dead? Technical
  - My residential video intercom monitor went black after a thunderstorm. Fixable? Technical
  - We bought a property in Rhinebeck with an old Nutone intercom — can it be saved? Residential/Commercial
  - Our medical office in White Plains needs HIPAA-aware intercom — does that exist? Residential/Commercial
  - Show up, charge $400, intercom still broken — what's my recourse? Complaints
  - Got a $22k quote to "completely replace" our community gate system. Is that real? Complaints
  - How much to convert a landline gate intercom to cellular? $1,800–$3,500 for the new LTE-capable gate station and installation; cellular service runs $15–$35/mo per panel.
  - Why is the gate intercom directory full? Older DoorKing 1812 and Linear AE-100 have hard caps on directory entries. Upgrade to 1838 or AE-1000 (or IP cloud) for unlimited entries.
  - How long does HV intercom repair take? 30 min to 2 hours for component swaps; 4–8 hours for gate panel replacements; 2–5 days for full HOA gate system overhauls.
### intercom-repair-long-island 17
  - Why is Hamptons intercom repair more expensive than Nassau? Cost
  - My intercom died after Hurricane Henri / Hurricane Lee / the latest nor'easter — repair or insurance claim? Cost
  - How do I find a real licensed LI intercom guy and not get burned? Quality/Trust
  - Is it worth more than hiring a Babylon or Patchogue handyman? Quality/Trust
  - Can I just reprogram my DoorKing 1812 directory myself? DIY/Pro
  - My handyman "fixed" the gate and now nothing works — can it be reversed? DIY/Pro
  - Why does my gate panel keep dying every 3 years near the beach? Technical
  - Visitors can hear me but I can't hear them at the gate — what's dead? Technical
  - Why is my Aiphone JO black-screen after a thunderstorm? Technical
  - We bought a Garden City house with a Nutone intercom from 1978 — save it? Residential/Commercial
  - Our medical office in Lake Success needs HIPAA-compatible intercom — exists? Residential/Commercial
  - Tech showed up in Sag Harbor, charged $500, intercom still broken — recourse? Complaints
  - Got a $28k quote to "modernize" our HOA gate system. Real or rip-off? Complaints
  - Can salt air really kill my intercom? Yes — coastal LI properties within 1,000 feet of saltwater see standard panels corroded inside 5–8 years. Marine-grade replacements last 4–5× longer.
  - How much to convert a landline gate intercom to cellular? $2,100–$4,000 for a new LTE gate station + installation; cellular service $15–$35/mo per panel.
  - Why is the gate intercom directory full? Older DoorKing 1812 and Linear AE-100 have hard caps. Upgrade to 1838 / AE-1000 or IP cloud for unlimited entries.
  - Can I keep my existing wiring during an upgrade? In most LI walk-ups and condos, yes. Comelit Ultra, Aiphone GT, and Akuvox retrofit kits are designed to reuse legacy cable.
### intercom-repair-manhattan 18
  - Why do Manhattan intercom repair quotes vary so wildly? Cost
  - My Manhattan landlord says intercom repair is "too expensive" — what do I push for? Cost
  - How do I find a licensed Manhattan intercom guy approved for my co-op? Quality/Trust
  - Is it worth more than hiring a building handyman for a quick fix? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my UES intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them — what part is dead? Technical
  - Door release works for some apartments, not mine — wiring or station? Technical
  - My Manhattan landlord ignored my intercom complaint 6 weeks. HPD next steps? Landlord/Tenant
  - I'm a small Manhattan landlord with a 12-unit Inwood walk-up — what do I legally owe tenants? Landlord/Tenant
  - Tech showed up in SoHo, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $18k to "upgrade" our pre-war system when one station died. Reasonable? Complaints
  - Where can I get my Manhattan intercom fixed? Licensed NYS low-voltage contractor with Manhattan co-op experience — same-day from our Bronx shop. Avoid out-of-state chains.
  - How long does Manhattan co-op approval take for intercom work? Usually 2–10 business days for routine repairs once COI is on file. We pre-stage paperwork so you don't lose time on documentation.
  - Can a doorman building intercom be upgraded without disrupting service? Yes — after-hours and weekend work is standard for doorman buildings. We coordinate with concierge for access.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical single-issue. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems are landlord responsibility. Tenants handle damage they personally caused inside the apartment unit.
### intercom-repair-nassau-county 17
  - Why do Nassau intercom repair quotes vary so wildly? Cost
  - I'm a Nassau homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Nassau intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Nassau handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Great Neck co-op lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Long Beach building — what is dead? Technical
  - Why does my Long Beach barrier island intercom keep dying every 3 years? Technical
  - I run a Nassau commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Nassau small commercial property owner with a 12-unit Hempstead mixed-use — what do I owe tenants? Residential/Commercial
  - Tech showed up in Garden City, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $18k to "completely replace" our 20-unit Hempstead system when one apt died. Reasonable? Complaints
  - Where can I get my Nassau intercom fixed? Licensed NYS low-voltage contractor — same-day dispatch from Brooklyn shop via Belt Pkwy/Southern State/LIE. Skip the lead-aggregator surcharge.
  - How fast is same-day in Nassau? 2–4 hours for Five Towns and Long Beach; 3–5 hours for Hempstead/Garden City; 4–6 hours for Gold Coast estates. Calls before 10 AM get same-day.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-nyc 18
  - Why are NYC intercom repair quotes so wildly different from each other? Cost
  - My landlord says intercom repair is "too expensive" — what should I push for? Cost
  - How do I find a licensed NYC intercom repair guy who won't ghost me? Quality/Trust
  - Is it worth paying more for an NYS-licensed contractor vs an unlicensed handyman? Quality/Trust
  - Can I just rewire the apartment station myself with a multimeter? DIY/Pro
  - My super "fixed" the lobby panel and now nothing works — can a pro reverse it? DIY/Pro
  - Why does my intercom buzz constantly even when nobody's pressing the button? Technical
  - Visitors can hear me but I can't hear them — what part is dead? Technical
  - Door release works for some apartments but not mine — wiring or station? Technical
  - My NYC landlord ignored my intercom complaint for 6 weeks. What's HPD's role? Landlord/Tenant
  - I'm a small NYC landlord with a 12-unit Bushwick walk-up — what do I legally owe tenants? Landlord/Tenant
  - A tech showed up, charged me $300, intercom still broken. What's my recourse? Complaints
  - Got quoted $14k for a "full upgrade" when one apartment station died. Reasonable? Complaints
  - Where can I get my intercom fixed in NYC? Local NYS-licensed low-voltage contractor like Abstract Enterprises — same-day, all five boroughs. Avoid out-of-state national chains.
  - When should I replace instead of repair? System over 15 years old, parts discontinued, three repairs in 12 months, or repeated tenant complaints. Otherwise repair.
  - What does an NYC intercom repair cost on average? $250–$600 for a single-apartment fix, $1,200–$3,000 for lobby panel + wiring, $4,500–$15,000+ for full building replacement.
  - How long does an intercom repair take? 30 minutes to 2 hours for component replacement; 4–8 hours for lobby panel + retrofit; 2–5 days for full building system replacement.
  - Who is responsible — tenant or landlord? In NYC, building-wide intercom systems are the landlord's responsibility. Tenant only handles damage they personally caused inside the unit.
### intercom-repair-orange 15
  - Why do Orange County intercom repair quotes vary so wildly? Cost
  - I'm an Orange homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Orange County intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Orange handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Kiryas Joel walk-up lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Newburgh building — what is dead? Technical
  - Why does my Newburgh waterfront or Cornwall-on-Hudson intercom keep dying every 3 years? Technical
  - I run an Orange commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm an Orange small commercial property owner with a 16-unit Newburgh walk-up — what do I owe tenants? Residential/Commercial
  - Tech showed up in Goshen, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $18k to "completely replace" our 20-unit Newburgh system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-putnam-county 15
  - Why do Putnam County intercom repair quotes vary so wildly? Cost
  - I'm a Putnam homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Putnam County intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Putnam handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Brewster walk-up lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Brewster building — what is dead? Technical
  - Why does my Cold Spring or Garrison Hudson-facing intercom keep dying every 3 years? Technical
  - I run a Putnam commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Putnam small commercial property owner with a 12-unit Brewster walk-up — what do I owe tenants? Residential/Commercial
  - Tech showed up in Mahopac, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $15k to "completely replace" our 14-unit Brewster system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-queens 18
  - Why are Queens intercom repair quotes so wildly different? Cost
  - My Jackson Heights landlord says intercom repair is "too expensive" — what do I push for? Cost
  - How do I find a licensed Queens intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Queens handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the lobby panel in our Forest Hills building and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors can hear me but I can't hear them in our Astoria walk-up — what part is dead? Technical
  - Why does my Belle Harbor intercom keep dying every 3 years? Technical
  - My Queens landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
  - I'm a small Queens landlord with a 12-unit Corona walk-up — what do I owe tenants? Landlord/Tenant
  - Tech showed up in Flushing, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $19k to "completely replace" our 24-unit Astoria system when one apt died. Reasonable? Complaints
  - Where can I get my Queens intercom fixed? Licensed NYS low-voltage contractor — same-day from our Bronx shop via Triboro/RFK. Avoid out-of-state chains.
  - How fast is same-day in Queens? 2–4 hours typical for Astoria/LIC; 3–5 hours for Forest Hills/Flushing/Jamaica; 4–6 hours for Rockaways.
  - Can my LIC ButterflyMX be fixed without replacing it? Yes — firmware reflashes, account-level resets, and re-pairing solve most LIC luxury IP intercom lockouts in 1–2 hours.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-rockland 15
  - Why do Rockland intercom repair quotes vary so wildly? Cost
  - I'm a Rockland homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Rockland intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Rockland handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Spring Valley walk-up lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Nyack building — what is dead? Technical
  - Why does my Nyack or Piermont Hudson-facing intercom keep dying every 3 years? Technical
  - I run a Rockland commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Rockland small commercial property owner with a 14-unit Spring Valley walk-up — what do I owe tenants? Residential/Commercial
  - Tech showed up in Pearl River, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $17k to "completely replace" our 18-unit Monsey system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-suffolk-county 15
  - Why do Suffolk intercom repair quotes vary so wildly? Cost
  - I'm a Suffolk homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Suffolk intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Suffolk handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Stony Brook co-op lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them on our Hamptons rental property — what is dead? Technical
  - Why does my Fire Island or Westhampton Beach intercom keep dying every 3 years? Technical
  - I run a Suffolk commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Suffolk small commercial property owner with a 10-unit Patchogue mixed-use — what do I owe tenants? Residential/Commercial
  - Tech showed up in Huntington, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $20k to "completely replace" our 18-unit Bay Shore system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-westchester 15
  - Why do Westchester intercom repair quotes vary so wildly? Cost
  - I'm a Westchester homeowner — when should I repair my video intercom vs replace it? Residential/Commercial
  - How do I find a licensed Westchester intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Westchester handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the Yonkers co-op lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Larchmont building — what is dead? Technical
  - Why does my Larchmont or Mamaroneck Sound Shore intercom keep dying every 3 years? Technical
  - I run a Westchester commercial property — what are the NY State licensing rules for intercom work? Residential/Commercial
  - I'm a Westchester small commercial property owner with a 16-unit Yonkers walk-up — what do I owe tenants? Residential/Commercial
  - Tech showed up in White Plains, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $19k to "completely replace" our 24-unit Yonkers system when one apt died. Reasonable? Complaints
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.
### intercom-repair-staten-island (OLD page, replaced 2026-10-18) 17
  - Why do Staten Island intercom repair quotes vary so wildly? Cost
  - My St. George landlord says intercom repair is "too expensive" — what do I push for? Cost
  - How do I find a licensed Staten Island intercom guy who won't ghost me? Quality/Trust
  - Is it worth more than hiring a local Staten Island handyman? Quality/Trust
  - Can I swap my apartment Aiphone handset myself with a multimeter? DIY/Pro
  - My super "fixed" the St. George lobby panel and now nothing works — recoverable? DIY/Pro
  - Why does my intercom buzz constantly with no one pressing the button? Technical
  - Visitors hear me but I can't hear them in our Hylan Blvd building — what is dead? Technical
  - Why does my Great Kills outdoor intercom keep dying every 3 years? Technical
  - My Staten Island landlord ignored my intercom complaint 6 weeks — HPD next steps? Landlord/Tenant
  - I'm a small Staten Island landlord with a 10-unit Stapleton walk-up — what do I owe tenants? Landlord/Tenant
  - Tech showed up in New Springville, charged $400, intercom still broken — recourse? Complaints
  - Got quoted $14k to "completely replace" our 16-unit Hylan Blvd system when one apt died. Reasonable? Complaints
  - How fast is same-day on Staten Island? 2–4 hours typical for North Shore; 3–5 hours for Mid-Island and East Shore; 4–6 hours for far South Shore. Calls before 11 AM get same-day.
  - Can my single-family home video intercom be upgraded easily? Yes. Aiphone JO, Comelit Mini, DoorBird, Ring upgrades are 30-min to 2-hour installs. Smartphone app pairing included.
  - What's the cost difference between repair and full upgrade? Repair: $250–$1,500 typical. Full pre-war retrofit: $4,500–$15,000. Building-wide IP system upgrade: $25,000+.
  - Who's responsible — tenant or landlord? Building-wide intercom systems = landlord responsibility. Tenants handle damage they personally caused inside their unit.

#### New questions on `intercom-repair-staten-island` (rebuild 2026-10-18, final wording)
§9 Questions Answered (H3):
1. One owner in our townhouse complex wants the gate fixed today, but the board has not voted — what can happen in the meantime?
2. I live in a NYCHA development on the island — can I hire a private company to fix our lobby intercom?
3. Our 1920s eight-family on the North Shore never had an intercom — can the tenants make us install one?
4. Our two-family has a separate bell for each floor but one front door — why did both stop at the same time?
5. When the side-door bell is pressed, the wrong floor rings — what crosses the calls?
6. Can a basement apartment get its own button on the shared front door?
7. Since our house was raised, visitors press a button by the parking space and then climb a flight — should the station move to the top of the stair?
8. After the lift, which parts of the intercom have to move upstairs, and which can stay below?
9. Ever since the stair hall was painted and re-carpeted, the top-floor stations are dead — what did the work touch?
10. Delivery drivers get buzzed in by whoever answers and parcels vanish from the lobby — can the entry be set up differently?
11. The lobby screen works but nobody's phone rings when a visitor calls — what usually broke?
12. Residents who moved out years ago still show up on the lobby directory — how is it cleaned up?
13. When the building's internet goes down, should the front door still open for residents?
14. Our Hylan Boulevard dental office buzzes patients in from the front desk — why does the door sometimes stay locked after the release is pressed?
§17 FAQ (visible == FAQPage, 9 items):
15. What should I write down or photograph before calling, so the first visit can fix it?
16. Can one visit cover the intercom, the door closer and the lock on the same entrance?
17. Is a battery backup worth adding to a building intercom on the island?
18. After a key or fob goes missing, can access be changed without replacing the whole system?
19. Will replacing one apartment's station change the sound or picture for everyone else?
20. Can you take out an old, dead intercom panel and patch the wall or door frame?
21. Can the intercom let in a home aide or a dog walker while nobody is home?
22. Who keeps the installer codes and admin login once the repair is finished?
23. Can intercom work be scheduled around a re-siding job or a stoop rebuild?
Statement headings (no question): "Telephone-entry call boxes and the copper switch-over".

Closest register intents and why they are judged distinct:
- #1 vs NYC/HV "Do you work with co-op boards / condo associations / HOAs?" — theirs: whether AESS serves boards; mine: interim access while an association has not yet authorised a repair.
- #3 vs "My landlord ignored my intercom complaint — HPD's role?" and "small landlord — what do I owe tenants?" — mine is the pre-1968 tenant-majority-consent clause of MDL §50-a (installation where none exists), not repair enforcement.
- #4/#5 vs "Door release works for some apartments but not mine" and "buzz constantly" — mine: shared-component failure in a two-door two-family; crossed call lines.
- #7/#8 vs "Hurricane Sandy-zone coastal damage", "post-Sandy systems aging out", "salt air kill my intercom", "keeps dying every 3 years" — mine are placement decisions (door station height on a lifted house; where power equipment sits relative to the design flood elevation), not durability/corrosion.
- #9 vs the NYC body note on renovation-cut bus wiring (not a question) — kept. #12 (stale directory entries) vs HV/LI "Why is the gate intercom directory full?" (capacity) — different intent. #14 (release timing / door pressure at a buzz-in office door) vs old SI "Do you handle Hylan Blvd commercial…?" (service availability) — different. #6 (third household button) — new; answer defers legality of the unit to DOB/architect.
- #11 vs "Can my video intercom connect to my phone after repair?" and Queens "Can my LIC ButterflyMX be fixed without replacing it?" — mine is diagnosis of a working panel whose app calls fail.
- #13 is new (local fallback design). Call-box/copper topic kept as a statement heading because HV/LI ask "fix gate intercom if Verizon shut off our landline?" and "convert to cellular cost?".
- FAQ #17 battery backup, #18 credential change, #19 mixed generations, #20 decommissioning, #21 temporary access, #22 admin hand-over, #23 contractor scheduling — none in the register. Raised-house questions were reworded after a cross-silo check against floodlight-camera-installation-staten-island (0.68/0.70 → reworded).
Avoided entirely: cost/quotes vary, response time, brands, guarantee, HPD certificate of correction, phone app connection, DIY handset swap, super broke it, one-way audio, constant buzz, responsibility tenant vs landlord, upgrade without rewiring, repair-vs-replace, maintenance contracts, insurance after a storm, estate gates.

---

### Staten Island

Page: `intercom-repair-staten-island` (REBUILD in place 2026-10-18; was crawled-not-indexed). Up-link `/intercom-repair-nyc`. GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`). Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359. Nothing from the old page text reused.

**Thesis:** on Staten Island the first question in an intercom repair is *who owns the door*. With 83% of homes in one- and two-family buildings, island intercoms are mostly house door stations shared by two households, townhouse-association gates and entry panels, a minority of North Shore walk-ups and elevator buildings where MDL §50-a and HPD apply, new app-based rental buildings at St. George/Stapleton, and NYCHA developments whose repairs belong to NYCHA. Who can authorise the work decides the visit; then two island-specific physical facts — houses lifted above the flood line after Sandy (door stations and power supplies in the wrong place) and salt air on the shore — and one 2026 change: Verizon's proposed copper retirement for telephone-entry call boxes.

#### Sources status for this geo
| # | Source | Result |
|---|---|---|
| 1 | Reddit r/StatenIsland | `reddit StatenIsland intercom OR buzzer apartment building` · Firecrawl search → only r/AskNYC/r/Upperwestside/r/ShellyUSA threads; no r/StatenIsland intercom thread → EMPTY |
| 2–5 | PAA / PASF / ATP / AI Overview | EMPTY (not accessible in build env) |
| 8 | Bing / DDG | EMPTY (not accessible in build env) — DDG HTML scrape failed |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |
| — | Census ACS | not re-tried (earlier SI build: API key now required → EMPTY); CHPC figure used |

#### Building stock / housing (SI-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-H1 | carried from floodlight-camera-installation.md SI-H1 | https://chpcny.org/visualization/housing-stock-visualization/ | 83% of Staten Island units are in one- or two-family homes (CHPC, Oct 2024) | §5 para 1; §5.5 bullet 1; Sources |
| SI-H2 | carried from floodlight…md SI-H3 (Nacmias Law) ; `Staten Island townhouse condominium complex gated entrance call box homeowners association` · Firecrawl search (excerpts) | https://nacmiaslaw.com/practice-areas/closings/building-types/townhouse-condo-declaration/staten-island ; https://freelegalquote.com/hoa-in-staten-island-nyc-2026-homeowners-association-legal-faq/ | Low-rise townhouse condo communities (Annadale, Huguenot, Eltingville); one declaration per community; association often owns roads/parking/grounds; HOA membership mandatory inside a designated association | §5 para 2; §7 card; §9 board H3; §8 card |
| SI-H3 | same search (excerpt, FB realtor post) | https://www.facebook.com/northshoreholly/posts/… | "Gated Community The Accolade Condos, St. George" | Not used (FB excerpt only) |
| SI-H4 | carried from floodlight…md SI-H4 | https://www.nyc.gov/site/housingrecovery/disaster-recovery/build-it-back.page | 1,982 SI homeowners served by Build It Back; 838 homes citywide repaired and elevated above BFE | §5 para 4; §5.5 bullet 5; Sources |
| SI-H5 | carried from floodlight…md SI-H6 | https://www.nyc.gov/site/sirr/rebuilding/east-and-south-shore-staten-island.page | 11,700+ buildings in the inundated area; 1–2 family ≈ 90% | §5 para 4 |
| SI-H6 | carried from floodlight…md SI-R1 | https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction | Equipment at/above design flood elevation or built to keep water out; coastal high-hazard space below limited to parking, access, storage, crawl space | §8.5 bullet 4; §9 raised-house H3s; Sources |
| SI-H7 | carried from floodlight…md SI-H2 (Prodigy RE) | https://prodigyre.com/blog/the-two-family-wealth-engine-how-staten-islands-most-common-home-type-built-middle-class-wealth | Up-and-down high-ranch two-families (Great Kills), semi-attached (New Dorp/Dongan Hills), converted Victorians on the North Shore | §7 cards (descriptive) |

#### Public housing (SI-P)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-P1 | `NYCHA developments Staten Island list Stapleton Houses Mariners Harbor West Brighton Richmond Terrace Berry Todt Hill` · Firecrawl search (excerpts) | https://www.nyc.gov/site/nycha/about/developments/staten-island.page ; https://nychajournal.nyc/wp-content/uploads/2022/05/VEPE-4-NYCHA-Program-Partners.pdf | SI NYCHA developments: Berry, Cassidy-Lafayette, Mariners Harbor, New Lane Area, Richmond Terrace, South Beach, Stapleton, Todt Hill, West Brighton | §5 para 2; §7 card; §9 NYCHA H3 |
| SI-P2 | `Staten Island intercom broken NYCHA buzzer silive` · Firecrawl search → scrape (markdown) | https://www.silive.com/news/2022/09/many-nycha-buildings-are-unsecure-many-doors-have-broken-locks-audit-says.html | Sept 22 2022 (Giavanni Alves): Comptroller audit of 262 developments (Aug 30–Sept 8 2022): 36.8% of entrance doors open, 40.1% of entrance locks broken; open/broken share 23.5% (2018) → 57.9% (2022); SI unsecured entrances +34.9% (citywide +34.4%); Cassidy-Lafayette Houses (seniors, New Brighton): 100% of entrance door locks broken; residents said doors are propped because "intercoms, locks, keys, and door release buttons do not work"; one resident: intercoms broken for 10 years; recommendation to repair door closers, release buttons, intercoms, locks, keys | §5 para 2; §5.5 bullet 2; §9 NYCHA H3; FAQ door-closer; Sources |
| SI-P3 | same search (excerpt, SI Advance FB) | https://www.facebook.com/statenislandadvance/posts/the-todt-hill-houses-complex-is-one-of-two-nycha-developments-selected-to-underg/831294705703242/ | Todt Hill Houses one of two developments selected for a $150 million renovation | Not used (FB excerpt) |

#### North Shore rental and new buildings (SI-B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-B1 | `URL Staten Island Stapleton apartments units Lighthouse Point St. George rental building` · Firecrawl search → scrape NYCEDC (summary) | https://edc.nyc/project/lighthouse-point | Lighthouse Point next to St. George Ferry Terminal: more than 100 residential units, 20% permanently affordable; hotel, retail | §8 card; §13 card; Sources (story count NOT used — EDC says 12-story, YIMBY says 15-story: conflict) |
| SI-B2 | same search (excerpt) | https://newyorkyimby.com/2026/02/housing-units-still-available-at-lighthouse-point-in-st-george-staten-island.html | Feb 2026: affordable units still available; 35R Bay Street | Background |
| SI-B3 | `URL Staten Island Urby Stapleton Homeport apartments number of units` · Firecrawl search (excerpts) | https://www.silive.com/northshore/2016/01/website_launched_900_unit_deve.html ; https://www.architonic.com/en/pr/urby-staten-island/5103647/ | Urby Staten Island: 900 rental units planned (silive 2016); 571 completed in phase 1 (Architonic); Navy Pier Ct, Stapleton | §5 para 2; §7 card; §13 card; Sources |
| SI-B4 | `silive.com tenants intercom broken building Staten Island 2025 OR 2026` · Firecrawl search → scrape (summary) | https://www.silive.com/news/2025/05/public-spaces-in-staten-island-apartment-building-in-despair-this-is-inhumane.html | May 7 2025 (Priya Shahi): 180 Park Hill Ave (Clifton), government-subsidized complex — flooded lobby, leaks, mold, elevators; management DelShah Capital promises rehabilitation. No intercom mention in the summary | §5 para 3 (lobby conditions, not intercoms); Sources |
| SI-B5 | same search (excerpt) | https://www.silive.com/news/2026/04/live-staten-island-tenants-rally-for-enforcement-reforms-ahead-of-city-hearing-shaina-on-the-scene.html | April 2026 SI tenants rally for enforcement reforms (heat, ceilings) — excerpt only | Background |
| SI-B6 | G3 above | https://weverit.com/building/ny/new-york/1440-richmond-terrace-staten-island-10310 | Class B intercom violation open since Oct 2014 on a Richmond Terrace building | §5 para 3; §5.5 bullet 4 |

#### Landmarks / corridors (SI-L)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| SI-L1 | carried from floodlight…md SI-L4/L5 | https://en.wikipedia.org/wiki/Empire_Outlets ; https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ | Empire Outlets 350,000 sq ft by the ferry; Bay Street rezoning approved June 26 2019 | §8 card; §13 card |
| SI-L2 | carried from floodlight…md SI-H9 | https://en.wikipedia.org/wiki/Staten_Island | Hylan Blvd longest street in NYC; North Shore most urban | §8 card |
| SI-L3 | carried from floodlight…md SI-L7 | https://siuh.northwell.edu/ | SIUH at 475 Seaview Avenue | §8 card |
| SI-L4 | carried from floodlight…md SI-L3 | https://www.silive.com/news/erry-2018/03/05c8690920/10_things_to_know_about_the_st.html | SI Mall opened Aug 9 1973, Richmond Ave at Richmond Hill Rd | §13 card |
| SI-L5 | carried from floodlight…md SI-R5 | https://hdc.org/preservation-resources/expanding-historic-district-boundaries/expanding-historic-district-boundaries/ | St. George/New Brighton Historic District designated 1994 | §7 card; §13 card |
| SI-L6 | SI-P1 | NYCHA list | developments named | §13 "we also serve" not used for NYCHA (refer-out) |
| SI-L7 | Forest Avenue / Victory Boulevard storefront description | — | descriptive only (storefronts with rear/side delivery doors) — **no source; FLAG** | §8 card |

#### Licensing / permits (SI)
- NYS low-voltage license #12000287431 (protected) — intercom, strike, door station, network side.
- 120-volt feed to a transformer/power supply, new receptacle or circuit: licensed master electrician + DOB permit (silo G7).
- MDL §50-a + HMC (HPD Class B "inoperative intercom with return buzzer system") for 8+ unit class A buildings.
- NYCHA equipment: residents report via CCC (718) 707-7771 / MyNYCHA (G6); AESS does not claim NYCHA work.
- LPC for St. George/New Brighton historic district entrances (SI-L5) — panel faces visible from the street.

#### Pricing — §9 applied (1.10×), round half-up
Diagnostic $165–$330 · apartment station $275–$660 · house video monitor/door station swap $330–$825 · lobby/entry panel component $440–$1,320 · entry panel retrofit $1,650–$3,850 · transformer/power supply $330–$880 · door release strike $385–$990 · riser/bus wiring repair $1,100–$3,300 · marine-grade coastal panel $1,540–$4,180 · Mircom TX3 directory rebuild $385–$825 (not used on page) · small building full system $4,950–$13,200 · mid-size IP system $13,200–$30,800 · maintenance contract $660–$2,640/yr. Service rate $195/hr, 3-hr min ($585) unmultiplied. "Bands" for package cards use those same line items (no new figures).
FLAG: old SI page did not follow §9; "no separate toll line" wording carried from network-cable-repair-staten-island (via floodlight SI research).

#### House practices stated without an external source (FLAG for Anwar)
- Interim measures while an association decides (temporary keypad code / leave door on key / mechanical lock), documented test sheet after repair, labelled riser map, battery backup sizing, admin-credential hand-over, temporary aide codes, decommissioning and patching old panels, siding/stoop scheduling.
- Door station mounting height ~ shoulder height at the landing on lifted houses (general practice, not a code figure).
- "Same-day / 1–2 hours once on site" (blueprint §5 element 36 convention).
- Field Notes = installer-voice method note (who owns the door → power → wire → station), no specific job story.
- "Exits must still open from inside" (§8.5 bullet) — general egress principle, not fetched from the NYC Fire/Building Code this run.
- Third household on a two-family "can change how the city classifies and inspects the building" (§9 basement-button H3) — stated as a caution, defers to DOB/architect; MDL definitions not fetched.
- Dental-office release causes (timer, door pressure on strike, shared supply sag) and package-room options — general practice.
- LPC review for street-facing facade changes in St. George/New Brighton HD — carried from floodlight silo G3/SI-R5, not re-fetched.
- Cross-silo check: page also compared with floodlight-camera-installation-staten-island; only the NAP line (1.00) remains ≥0.65 after a rewrite pass.

#### Images (11) — Drive: no Intercom folder (per main run); CompanyCam not connected
`images/buzzer-repair/*.jpg` and `images/low-voltage/*video-intercom*.jpg` were inspected and **rejected as AI-generated** (garbled panel numbering, "123 MAIN STREET / ABC PROPERTY MANAGEMENT" signage) — FLAG: those folders should not be used as "real AESS photos" anywhere.
| Output (images/intercom-repair/) | Source | What it shows | Placement |
|---|---|---|---|
| intercom-repair-staten-island-akuvox-keypad-door-station-with-camera-product-photo.webp (803×1429) | images/intercom-keypad-akuvox.png | Akuvox door station: camera, card-reader symbol, 12-key keypad, speaker grille | Hero (eager) |
| …-stone-apartment-facade-with-camera-on-steel-arm.webp (228×368) | images/apartment-building-security-camera-installation/…brooklyn-stone-facade-with-camera-on-steel-wall-arm.webp (real AESS job, Brooklyn) | stone facade, windows, Greek-key cornice, camera on steel arm | §5 |
| …-akuvox-single-button-video-door-station-product-photo.webp (423×562) | images/akuvox-video-door-station.webp | single-button Akuvox station | §6 |
| …-black-akuvox-house-video-door-station-product-photo.webp (423×562) | images/akuvox-video-doorbell-black.webp | black Akuvox door station with call button | §7 |
| …-dome-camera-on-tiled-ceiling-above-glass-entrance.webp (935×720) | images/apartment-building-security-camera-installation/…manhattan-dome-camera-on-ceiling-over-glass-entrance.webp (real AESS job) | white dome camera, drop ceiling, light panels, glass storefront wall | §8 |
| …-corridor-to-grey-door-with-camera-and-wall-plates.webp (635×600) | images/apartment-building-security-camera-installation/…brooklyn-black-bullet-camera-on-ceiling-facing-grey-service-door.webp (real AESS job) | black bullet camera on ceiling, grey door with keypad lock, two metal wall plates | §9 "who owns the door" cluster |
| …-white-network-video-doorbell-rear-mounting-side-product-photo.webp (500×500) | images/apartment-building-security-camera-installation/…staten-island-poe-doorbell-camera-rear-product.webp | rear of a white network video doorbell, label "UVC-Doorbell" | §9 two-family cluster |
| …-axis-narrow-video-door-station-product-photo.webp (675×900) | images/axis-i8116-video-intercom.webp | Axis narrow video door station | §9 walk-up/package cluster |
| …-white-akuvox-indoor-touchscreen-monitor-product-photo.webp (456×456) | images/intercom-indoor-monitor.png | white Akuvox indoor touchscreen monitor | §10 equipment |
| …-blue-and-white-cable-bundles-along-ceiling-pipe.webp (710×215) | images/apartment-building-security-camera-installation/…brooklyn-blue-network-cable-bundles-along-ceiling-pipe.webp (real AESS job) | blue + white cable bundles on a ceiling rod/pipe | §12 process |
| …-akuvox-touchscreen-directory-panel-product-photo.webp (456×456) | images/intercom-touchscreen.png | Akuvox touchscreen entry panel, keypad on screen showing "1008" | §14 pricing |
DAILY-LOG note suggestion: `images: 11 = 3 real AESS job photos from other jobs + 1 real exterior job photo (Brooklyn) + 7 manufacturer intercom product shots (no real intercom photos yet)`.
