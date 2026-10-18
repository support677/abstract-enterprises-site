# Network Installation — silo research

Created 2026-10-18 by the REBUILD run for `network-installation-suffolk-county` (queue line: `REBUILD | network-installation-suffolk-county | Network Installation | Suffolk | up /network-installation-long-island | (631) 407-2884 | GBP Brooklyn`). No `research/network-installation.md` existed before this run.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. "Excerpt" = read only as a search-result snippet, not opened. Tools used: WebSearch (Claude), WebFetch (page read + summary). Shell curl/wget blocked and not used. Sources marked **carried** were fetched and verified by earlier 2026-10-17/18 runs and are recorded in `research/cat6-repair.md` (Suffolk section), `research/fiber-optic-installation.md` and `research/apartment-building-security-camera-installation.md` (Suffolk section); they are cited here with their URLs and not re-fetched.

Page section labels (Suffolk page): §Hero, §Quick, §5 Neighborhood (+5.5 facts), §Repair capture, §6 Services, §7 Architecture (+7.5 methods, segment plan), §8 Commercial (+8.5 rules), §9 Q&A (clusters A–F), §10 Equipment (+comparison), §10.5 AI Reality Check (H3 1–7), §11 form, §12 Process, Handover pack, §13 Landmarks, Towns table, §14 Pricing (+worked examples), §15 Packages (+BYOE), §16 Services grid, Field Notes, §17 FAQ, §19 Siblings, §Sources, NAP block.

---

## Part 1 — Silo-wide findings (usable on every Network Installation page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Silo-level: no new thread opened (reddit pages not fetchable in this env). Suffolk excerpts carried (Part 2, R1–R2). Query `site:reddit.com r/longisland Optimum outage working from home Suffolk backup internet` · WebSearch → returned only istheservicedown.com outage pages, no Reddit → EMPTY for that query. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on-page and corrects claims commonly published by cost guides/retailers/advice sites (rows T1–T4 below). |
| 6 | Area landmarks | Suffolk section L*. |
| 7 | Area use cases / building stock | Suffolk section B*/C*. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only WebSearch available. |
| 9 | Local news | Suffolk: The Record, Long Island Press, WSHU, RiverheadLOCAL, ABC7, La Voce di New York, Patch Riverhead, South Shore Press (Part 2). |
| 10 | Hyperlocal | Suffolk: RiverheadLOCAL, Riverhead News-Review, 27east, Fire Island News, Shelter Island Reporter (carried). Hyperlocal stories about business networks specifically: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). Not used on page. |

### 1.2 Technical / standards / cost sources (silo-wide)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `TIA TSB-162-A Category 6A recommended for wireless access points cabling` · WebSearch → WebFetch | https://www.cablinginstall.com/wireless-5g/article/16465896/tia-revising-specification-for-cabling-wireless-access-points | Aug 1 2013 (draft stage): TSB-162-A "recommends Category 6A for WAP cabling" and "Category 6A or better cabling for remote powering of WAPs"; 18.3 m (60 ft) square grid; multiple cables + link aggregation recognised (no fixed count). | §10.5 H3 5; Sources |
| T2 | `IEEE 802.3bt PoE type 3 type 4 watts at powered device 802.3at 25.5W` · WebSearch → WebFetch | https://ethernetalliance.org/wp-content/uploads/2018/04/WP_EA_Overview8023bt_FINAL.pdf | Type 1 af 15.4 W PSE / 13 W PD; Type 2 at 30 / 25.5 W; Type 3 bt 60 W PSE (4-pair) / 51 W PD; Type 4 90 / 71.3 W. | §9 cameras Q para 3; Sources |
| T3 | `cost to install business network small office 2025 Angi OR HomeAdvisor OR Fixr network installation cost` · WebSearch → WebFetch | https://www.fixr.com/costs/hardwired-computer-network | Updated Jan 31 2025: average $3,800, range $2,500–$4,500 for 2,000 ft Cat6 with up to eight connections, new construction; technician $50–$100/hr; electrician $40–$120/hr; no small-business figures. | §10.5 H3 1 |
| T4 | `NEMA 4X enclosure definition corrosion resistance coastal salt spray vs NEMA 4` · WebSearch → WebFetch | https://viox.com/nema-vs-ip-ratings-electrical-enclosures/ | "NEMA 4X adds corrosion resistance"; both cover outdoor/hose-directed water. | §7.5 salt-air method; Sources |
| T5 | carried (research/cat6-repair.md) | https://www.mikeholt.com/instructor2/img/product/pdf/11LE-968-sample.pdf | NEC 800.90(B): primary protector as close as practicable to the point the cable enters the building. | §9 thunderstorm Q para 2 (stated generally, "the electrical code requires one for cables exposed to lightning") |
| T6 | other HomeAdvisor / Angi pages in the same search (excerpts only: https://embedded.homeadvisor.com/cost/home-offices/install-a-computer-network-or-wiring/) | — | Not opened; not used. | — |

### 1.3 Silo pricing base (from this repo; no new prices invented)
Brooklyn base = `network-installation-brooklyn.html` pricing tables (identical lines also on -nyc, -long-island, -nassau-county): survey $450 (credited); design $350–$650; router/gateway $350; firewall $450–$900; managed switch 24-port $250 / 48-port $400; additional stacked switch $175; VLAN per segment $125; guest network $200; AP on existing drop $225 / with new run $300; AP high-bay/lift $375; rack build $650; second telecom room with fiber link from $2,400; rack cleanup from $500; demarc extension from $350; documentation $350; certification per drop $20; small office package $4,900; 25–50-user floor $12,500. Service $195/hr, 3-hr minimum ($585) — protected, not multiplied.
Suffolk = × 1.20 (v2.3 §9): $540; $420–$780; $420; $540–$1,080; $300 / $480; $210; $150; $240; $270 / $360; $450; $780; from $2,880; from $600; from $420; $420; $24; packages $5,880 and $15,000; third package "Two-Room Building" = $15,000 + $2,880 = $17,880 (sum of two published Suffolk lines, not a new base).
Worked examples (§14) are sums of these lines only: Hauppauge flex example $8,040 (+ $2,880 = $10,920); North Fork tasting-room example $5,880 + $420 + 2×$360 = $7,020.

### 1.4 Keywords (five layers)
- Service: network installation Suffolk County, business network installation, office network setup, firewall installation, managed switch installation, Wi-Fi access point installation, wireless site survey, VLAN segmentation, network documentation, network takeover.
- Problem: one-carrier address, no Fios, backup internet, cellular failover, summer cell congestion, power outage / PSEG outage, UPS runtime, generator transfer reboot, surge-damaged switch ports, ransomware spread, vendor remote access, departed employee passwords, re-divided flex bay, inherited cable, raised house flood enclosure, seasonal shutdown, untested new-construction jacks, no cell signal indoors.
- Technology: firewall dual-WAN, VPN, site-to-site tunnel, PoE 802.3at/802.3bt, Cat6/Cat6A (TSB-162-A), fiber link, point-to-point wireless bridge, UPS with network card, NEMA 4X enclosure, Wi-Fi calling, captive portal.
- Industry: flex/industrial and distribution, office parks, medical and professional suites, farms/wineries/tasting rooms, seasonal retail and restaurants, home offices, research-park firms.
- Geographic: Suffolk County, ten towns (Babylon, Huntington, Islip, Smithtown, Brookhaven, Riverhead, Southold, Southampton, East Hampton, Shelter Island), Hauppauge / Long Island Innovation Park, Route 110 (Melville, Farmingdale, Huntington Station), Ronkonkoma / Station Yards, Stony Brook, Upton, Riverhead / Route 58, Calverton, Westhampton / Gabreski, Montauk, Sag Harbor, Bridgehampton, Mattituck, Greenport, Lindenhurst, Amityville, Bay Shore, Central Islip, Fire Island.

---

## Part 2 — Suffolk County

**Thesis (distinct from the LI hub = wide buildings / telecom rooms, and Nassau = medical suites):** in Suffolk the network is designed around three county facts before headcount — (1) which carriers actually reach the address (single wired carrier common; ~51,700 Suffolk residents lacked last-mile wired broadband in 2021; ConnectALL proposed fixed-wireless/satellite awards include Suffolk; East End summer cell congestion undermines naive cellular failover); (2) long PSEG Long Island outages (Isaias: 271,352 customers out next morning, ~85% restoration estimated by end of week) → UPS bridging, shutdown order, auto-restart; (3) the county government's own 2022 ransomware attack (entry via one separately-run office, password folder, lateral movement in three hours) → segments with rules, vendor segment, individual admin accounts. Plus building stock (re-divided Hauppauge flex bays, Route 110 offices, farms/wineries, seasonal shops, Sandy-raised houses) and county/town licensing layering.

### 2.1 Carriers and broadband
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C1 | `Optimum Altice fiber rollout Long Island Suffolk towns 2024 2025 fiber-to-the-home` · WebSearch → WebFetch | https://alticeusa.com/node/3151 | Oct 1 2024: additional $40M in LI fiber; fiber available to ~2.8M passings tri-state, "nearly 900,000 on Long Island"; up to 8 Gig symmetrical; >100 LI communities; no Suffolk towns named. | §5 para 2, §5.5 bullet, Sources |
| C2 | `Verizon Fios availability Suffolk County towns not available Optimum only Long Island r/longisland` · WebSearch → WebFetch | https://www.verizon.com/home/internet/near-me/long-island-new-york/ | Lists Huntington, Huntington Station, Babylon, West Babylon, Smithtown, Commack, Islip, Bay Shore, Riverhead, Southampton under Verizon Home Internet (Fios or 5G Home); "much of Long Island"; availability checker needed per address; no statistics. | §5 para 2, §5.5, Towns table (Babylon), Sources |
| C3 | `East End Long Island broadband fiber gaps Southampton East Hampton internet access study` · WebSearch → WebFetch | https://longislandpress.com/2021/11/21/oped-broadband-access-is-a-long-island-problem | Op-ed (Rebecca L. Watts, WGU; date not stated, URL Nov 2021) citing Comptroller DiNapoli Sept 2021: 9.2% of LI households (87,730) without subscription; 61,231 Long Islanders in areas without wired high-speed; "nearly 51,700 people in Suffolk County" missing last mile. | §5 para 2, §5.5 bullet, Sources |
| C4 | `ConnectALL grant Suffolk County broadband unserved locations 2025` · WebSearch → WebFetch | https://southshorepress.locallabs.com/stories/675482976-140-million-in-state-broadband-funding-aiding-suffolk | Undated: proposed awards (need NTIA approval) — CBN Geneva fixed wireless 18,101 locations in 29 counties incl. Suffolk; SpaceX LEO satellite 13,615 locations in 37 counties incl. Suffolk; no Suffolk-only counts. | §9 A1 para 2 (stated as "proposed awards"), Sources |
| C5 | `reddit longisland North Fork OR Hamptons internet slow summer cell service crowded` · WebSearch → WebFetch | https://lavocedinewyork.com/en/lifestyles/2024/08/13/the-hamptons-solution-to-the-cell-phone-problem-an-ugly-uncool-antenna | Aug 13 2024: Hamptons residents installing vehicle cell boosters (~$500, weBoost/Wilson/Cel-Fi); towers overloaded in peak summer; Sag Harbor quote "better cell service in Bangladesh than here" (not quoted on page). | §9 A2 para 1, Sources |
| C6 | same search · WebFetch | https://patch.com/new-york/riverhead/cell-service-on-the-north-fork-dependable-or-not | July 22 2013 (Taylor K. Vecsey): "It seems like every summer the number of visitors grows and the cell reception gets worse." — reader call-out, no data. | §9 A2 para 1 ("as long ago as 2013"), Sources |
| C7 | `reddit longisland business internet Optimum Fios Hauppauge office fiber options` · WebSearch | (results: Altice press releases, ISP aggregator sites e.g. highspeedinternet.com/ny/hauppauge) | No Reddit thread; aggregator pages not used. EMPTY for Reddit. | — |

### 2.2 Power and storms
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `Tropical Storm Isaias PSEG Long Island outage customers Suffolk 2020 report days restore` · WebSearch → WebFetch | https://riverheadlocal.com/2020/08/06/isaias-update-outages-restoration-progress-and-lingering-road-closures | Published ~Aug 5–6 2020 (inferred from URL): PSEG-LI map "271,352 affected customers as of 6:32 a.m."; ~5,000 Riverhead/North Fork still out; PSEG "estimates 85% of customers will be restored by end of day Friday". | §5 para 3, §5.5, §9 B2 para 1, §10.5 H3 6, Sources |
| P2 | carried (research/cat6-repair.md, LI hub) | https://abc7ny.com/weather/widespread-damage-and-power-outages-across-long-island/6353608/ | "almost half of PSEG's 1.1 million customers in the dark at the peak" (Aug 2020). | §5.5 bullet, Sources |
| P3 | carried (F4) | https://www.weather.gov/media/okx/coastalflood/Lindenhurst%20impacts.pdf | Sandy: much of area south of Montauk Hwy inundated 2–5 ft in Lindenhurst, Amityville, Babylon; repeated moderate flooding since. | §9 D2 para 1, Sources |
| P4 | carried (F1) | https://www.fema.gov/sites/default/files/2020-07/fema_tb5_free_obstruction_requirements.pdf | TB5: enclosures under elevated buildings limited to parking, building access, storage. | §7 cards/methods, §8.5 bullet, §9 D2, Sources |

### 2.3 The 2022 Suffolk County government cyberattack
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `Suffolk County cyberattack 2022 ransomware county network systems offline months` · WebSearch → WebFetch | https://therecord.media/suffolk-county-new-york-ransomware-investigation | Apr 12 2023: entry Dec 2021 via Log4j into the county clerk's office; Aug 2022 password folder "kept on the clerk's network unprotected"; within three hours into broader county IT; exfiltration from Sept 1; ransomware Sept 8 2022; BlackCat/ALPHV; email down for >10,000 workers; dispatchers by hand for weeks; clerk IT separate from county IT; ransom not paid. | §5 para 4, §5.5, §7 segment-plan outro, §9 C1, §10.5 H3 7, Sources |
| S2 | same search · WebFetch | https://longislandpress.com/2023/11/06/cyber-attack-suffolk-new-report | Nov 2023: CIS report — public-facing Horizon environment, Log4J; CIS alerted at 3 a.m. Sept 8 2022; "By 11 a.m., the entity had completed a full network isolation." | §9 C1 para 3, Sources |
| S3 | `WSHU June 2024 Suffolk County cyberattack response cost Bellone` · WebSearch → WebFetch | https://www.wshu.org/long-island-news/2024-06-27/suffolk-county-cyberattack-response-bellone | June 27 2024: county approved "$16 million payment to outside vendors" (per Newsday); ~400,000 residents' data exposed; state of emergency into 2023; testimony that hack originated in Clerk's Office separate from county IT. | §5.5 bullet (attributed "Newsday reported"), Sources |

### 2.4 Licensing and permits
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| K1 | `"Suffolk County Department of Labor, Licensing and Consumer Affairs" home improvement electrical license` · WebSearch | https://www.harborcompliance.com/agency/suffolk-county-department-of-labor-licensing-and-consumer-affairs (title/excerpt) | Department name confirmed as "Suffolk County Department of Labor, Licensing & Consumer Affairs". | §8.5, §9 F1, Sources |
| K2 | same · WebFetch | https://www.suffolkcountyny.gov/Consumer-Affairs | "Division of Consumer Affairs"; 725 Veterans Memorial Hwy, Smithtown 11787; Riverhead office 300 Center Drive South; home improvement licences; master and restricted electrician licences (CE before renewal); online contractor licence search. | §8.5, §9 F1 para 3 |
| K3 | carried | https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License | Licence list: Home Improvement, Master Electrician, Restricted Electrical, etc.; no low-voltage/network category. | §8.5, §9 F1, §10.5 H3 3 |
| K4 | carried | https://ecode360.com/14948079 | Ch. 563 Art. XI: broad "electrical field" definition; article not applicable in towns/villages with their own licensing law or a second-class town opting out. | §8.5, §9 F2, §10.5 H3 3 |
| K5 | carried (ecode360.com/14947436 via fiber research) | https://ecode360.com/14947436 | §563-16 excludes electrical/plumbing work from home improvement article. | §9 F1 para 1 |
| K6 | carried | https://riverheadlocal.com/2019/06/25/should-jobs-being-done-by-unlicensed-contractors-be-slapped-with-stop-work-orders/ | 9,107 HI licences countywide (2018); civil penalty up to $750 / $1,500. | §9 F1 para 1 ("more than 9,000") |
| K7 | carried | https://ePermits.southamptontownny.gov/eElectrical | Southampton runs own electrical e-permit portal. | §8.5, §9 F2, Towns table |
| K8 | carried | https://newyork-811.com/homeowners/ | 811 covers Nassau/Suffolk; ≥48 hours, ≤10 working days notice. | §7.5 outbuildings, §8.5 |
| K9 | carried | https://pb.state.ny.us/public-information/faqs/ | Central Pine Barrens ~105,000 acres; Core clearing = development. | §8.5 |
| K10 | Town-by-town low-voltage permit rules | — | EMPTY (not established for any town); page says we check per address. | §9 F2 |

### 2.5 Building stock, corridors, landmarks (B/C/L)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| B1 | carried | https://www.costar.com/article/131430884/hauppauge-leads-long-island-metropolitan-area-in-available-industrial-space/ | Aug 16 2024: 26.1M sq ft around Hauppauge, Central Islip, Bay Shore; most available space on LI; small-bay preference. | §5.5, §9 D1 |
| B2 | `Hauppauge Industrial Park number of businesses employees Long Island Innovation Park` · WebSearch (excerpts) + carried | https://cmmllp.com/hauppauge-industrial-park-update-2017-long-islands-oasis-productivity-innovation/ ; https://cmmllp.com/long-island-innovation-park-at-hauppauge-showcases-hundreds-of-business-tenants-banners/ | 2017 HIA study: ~1,350 businesses, ~55,000 workers, ~11 sq mi; renamed Long Island Innovation Park at Hauppauge (2019). | §8 card, §13 card, Towns (Smithtown) |
| B3 | carried | https://iraceenterprises.com/route-110-corridor/ | Route 110: Farmingdale, Melville, Huntington Station; warehouse, flex, R&D, office; LIE access. | §8 card |
| B4 | carried (nyrej 2019) | https://nyrej.com/print/52376 (search result) | Melville Corporate Center I, 105 Maxess Rd, 149,000 sf. | §8 card, §13 card |
| B5 | carried | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Oct 22 2024: Station Yards 53 acres at Ronkonkoma LIRR; 1,450 units at completion. | §8 card, §9 D4, §13 card |
| B6 | carried | https://en.wikipedia.org/wiki/Stony_Brook_University ; https://en.wikipedia.org/wiki/Brookhaven_National_Laboratory | SBU 213 buildings / 1,454 acres + R&D park; BNL est. 1947 at Camp Upton, 5,265 acres. | §8 card, §13 cards |
| B7 | carried | https://brixmor.com/re-development/completed-projects/the-shops-at-riverhead | 115,000 sf Shops at Riverhead across from Tanger Outlets. | §8 card |
| B8 | carried | https://riverheadlocal.com/2020/01/10/pbmc-dedicates-new-critical-care-pavilion | PBMC $67.8M Corey Critical Care Pavilion (2020); roughed-out future space. | §8 card ("expanding campus"), Towns (Riverhead) |
| B9 | carried | https://riverheadnewsreview.timesreview.com/?p=94143 | Undated preliminary plat: ~2,107 acres EPCAL into eight lots; ~292 acres protected Pine Barrens. | §13 card (stated as preliminary plat) |
| B10 | carried | https://www.27east.com/southampton-press/new-business-park-continues-to-take-shape-in-westhampton-1406404 | Aug 26 2016: Hampton Business District, Gabreski, 55 acres county land. | §8 card, Towns (Southampton) |
| B11 | carried | https://27east.com/southampton-press/still-a-campus-cornerstone-new-stony-brook-southampton-hospital-aims-for-2030-opening-date-2226594 | Jan 17 2024: new hospital planned at Shinnecock Hills campus, target 2030. | Towns (Southampton) |
| B12 | carried | https://www.ny.gov/counties/suffolk ; https://en.wikipedia.org/wiki/Suffolk_County,_New_York | Ten towns; 86 miles; 912 sq mi land; Brookhaven largest and only town spanning South to North Shore. | §5 para 1, §5.5, Towns table |
| B13 | carried | https://shelterislandreporter.timesreview.com/2025/02/02/suffolk-closeup-the-farming-county/ | 578 farms (2022), 79 wineries. | Background for §7 farm card (numbers not printed on page) |
| B14 | carried | https://www.fireislandnews.com/communities/kismet/fire-island-ferries-freight-service-stalled/ ; https://www.nps.gov/fiis/planyourvisit/off-road-vehicle-permit-faqs.htm | Fire Island freight via Bay Shore (Maple Ave, disrupted 2025); NPS contractor driving permits limited. | Towns table (Islip), Towns note |

### 2.6 Local Reddit (excerpts, carried — reddit not scrapeable here)
| # | URL | Excerpt | Used |
|---|---|---|---|
| R1 | https://www.reddit.com/r/longisland/comments/vxk1bd/ | Verizon FIOS "not available where I live (NW Suffolk)". | §5 para 2 (quoted 4 words), Sources |
| R2 | https://www.reddit.com/r/longisland/comments/1g51via/best_wifi_provider_smithtown_pines_area/ | Recommends hard-wiring a home-office computer to the router via Ethernet. | Background for FAQ home offices; Sources |

### 2.7 Images (11) — permanent image rule
- Step A: Google Drive "AESS Website Photos" has no Network Installation folder (per batch brief) — none imported.
- Step B: CompanyCam not connected — none imported.
- Step C / permanent rule: candidates in images/network/, images/network-cable-repair/, images/cat6/ and images/low-voltage/ were all opened as contact sheets and **rejected as AI-generated** (rendered faces, uniforms printed with a non-AESS phone number "844-386-7238", inconsistent logos "Enterprise LLC", staged "BEFORE/AFTER" panel); every one also shows a face. Used instead: real AESS job photos already in the repo (Rockland Toyota and Manhattan deli jobs, cropped so no logo, signage, people, plates or readable documents are in frame) + manufacturer product photos.

| images/network-installation/ | Source (crop box px) | Placement |
|---|---|---|
| network-installation-suffolk-county-blue-and-white-cable-runs-under-ceiling-deck.webp | images/rockland-toyota-nvr-monitor.jpeg (170,0,900,250) | Hero (eager, og:image) |
| …-office-ceiling-grid-with-exit-sign-and-camera.webp | images/rockland-toyota-active-deterrent.jpeg (0,0,935,560) — mural/poster/people cropped out | §5 |
| …-ubiquiti-unifi-unvr-rack-appliance-product-photo.webp | images/nvr-ubiquiti-unvr.png (product photo) | §6 |
| …-corridor-drop-ceiling-and-wall-plates.webp | images/rockland-toyota-hallway-camera.jpeg (300,0,935,1050) — poster/cabinet cropped out | §7 |
| …-retail-drop-ceiling-with-ceiling-devices.webp | images/manhattan-deli-interior-cameras.jpeg (0,0,1230,430) — people, menu boards cropped out | §8 |
| …-recorder-screen-per-channel-bitrate-table.webp | images/rockland-toyota-nvr-monitor.jpeg (262,690,1075,835) | §9 cameras Q |
| …-cable-bundles-dropping-into-rack-side.webp | images/rockland-toyota-nvr-monitor.jpeg (0,0,330,690) — vendor sticker cropped out | §9 flex-bay Q |
| …-tp-link-vigi-poe-recorder-product-photo.webp | images/nvr-tplink-vigi-nvr1008h.png (product photo) | §10 |
| …-black-camera-on-drop-ceiling-tile.webp | images/rockland-toyota-ceiling-bullet.jpeg (0,0,935,700) | §14 |
| …-ceiling-dome-above-window-wall.webp | images/rockland-toyota-office-camera.jpeg (0,0,935,700) — signage cropped out | Field Notes |
| …-unifi-ceiling-fisheye-poe-camera-product-photo.webp | images/ubiquiti-unifi-ai-360-fisheye-camera-black.webp (product photo) | §17 |
All WebP q80, ≤1600 px. Captions say "Example photo from another AESS job (not a Suffolk …)" or "Manufacturer product photo"; nothing claims a Suffolk job. Note: the bitrate-table crop overlaps the scene used on lorex-camera-installation-brooklyn (different silo, different crop).

### 2.8 FLAGS for Anwar
1. **Image library:** images/network/, images/network-cable-repair/, images/cat6/, images/low-voltage/ appear AI-generated (non-AESS phone 844-386-7238 on shirts, rendered faces). Earlier pages in several silos use them (some cropped). Not used here. Real network-room/rack photos for this silo are needed in Drive.
2. **Pricing conflict:** the LI hub and network-installation-nassau-county publish Brooklyn rates un-multiplied ("Nassau and Suffolk … carry no travel loading — same rates"); the old Suffolk page used travel bands ($95/$145 per crew day). This page applies the v2.3 §9 ×1.20 per the build brief. Hub copy now contradicts this page; decide which convention the silo keeps.
3. **Third package** ($17,880) is the sum of two published lines (floor package + second room), not a separately published base.
4. **Unsourced practices** stated as AESS method (generic, no stats): outage shutdown order, vendor segment with time-limited VPN, handover pack contents, test-by-pulling-the-line, reopening checklist for seasonal sites, 50% deposit wording in FAQ (from the protected terms sentence).
5. **Related intents** near sibling questions (checked by meaning, judged distinct): Ulster "What happens to the network in a power cut?" vs this page's generator/UPS and shutdown-order Qs; county licensing Qs here are about home-improvement vs electrical and town/village layering, not "are you licensed in X".
6. **Wiring for main run:** network-installation-long-island links to Suffolk only as `/free-quote?service=network-installation&area=suffolk-county` — flip to `/network-installation-suffolk-county`. 14 siblings (all except Nassau) have no link to the Suffolk page.

---

## Question register — every FAQ / Q&A / "?" heading on every network-installation-*.html page (extracted from HTML 2026-10-18, before this rebuild; then this page's final questions)

### network-installation-bronx (23 questions)

- How much does network installation cost in the Bronx?
- Can you install a network without stopping our operation?
- Will network equipment survive in a cold room or a wash-down area?
- Why do our scanners drop as staff move through the building?
- What does a Bronx network installation include?
- Is this network installation or structured cabling?
- How many access points does a Bronx building need?
- Does guest wireless need its own segment?
- How long does a network installation take on a working premises?
- What hardware does a Bronx business need?
- Is a wireless survey worth paying for here?
- Do we need a managed switch?
- Do you work overnight and around shift changes?
- Cat6 or Cat6A on the runs feeding radios?
- Who installs business networks in the Bronx?
- Do we need a permit to run network cable?
- Can you work without stopping our operation?
- Will equipment survive in a cold room?
- Can you work alongside our IT provider?
- Our scanners drop as staff walk the aisles. Fixable?
- Do you cover yards and loading docks?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-brooklyn (23 questions)

- How much does network installation cost in Brooklyn?
- Why does a loft cost more to network than an office of the same size?
- What does a Brooklyn network installation include?
- Is this network installation or structured cabling?
- How many access points does a Brooklyn loft need?
- Our open floor has great Wi-Fi but the back rooms have none. Why?
- Does the guest network need separating from ours?
- What hardware does a Brooklyn business need?
- How long does a Brooklyn network installation take?
- Can you install without shutting the studio down?
- Is a wireless survey worth it here?
- Do we need a managed switch?
- Do you work evenings and weekends?
- Cat6 or Cat6A for the runs feeding access points?
- Who installs business networks in Brooklyn?
- Is a permit needed for network cabling?
- Can the cable be hidden in a loft?
- Will a faster circuit fix slow file transfers?
- Can you work with our IT provider?
- Do you supply hardware, or can we?
- Can you clear out the old cable?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-dutchess-county (22 questions)

- How much does network installation cost in Dutchess County?
- Can you work to our infrastructure standard?
- Why does labelling matter so much on institutional work?
- What does a Dutchess network installation include?
- Is this network installation or structured cabling?
- Why do mill conversions need so many access points?
- Should we match the switches we already run across the estate?
- How does segmentation work when the estate already has a scheme?
- How long does an installation take here?
- Can the work happen without disrupting a clinic or a school?
- Is a wireless survey required or just recommended?
- Do we need a managed switch?
- Why is our PoE budget running out across several buildings at once?
- What grade should the runs feeding radios be?
- Who installs business networks in Dutchess County?
- Do we need a permit for network cabling?
- Are you licensed to work in Dutchess?
- Will you match the switches we already run?
- Can you work alongside our in-house IT team?
- Why do mill buildings need so many access points?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-hudson-valley (23 questions)

- How much does network installation cost in the Hudson Valley?
- How do you link two buildings on the same property?
- What does a commercial network installation include up here?
- Network installation or structured cabling — what am I actually buying?
- How many Wi-Fi access points does a Hudson Valley building need?
- Why is Wi-Fi fine in one room of our building and absent in the next?
- Do we have to separate guest wireless from the staff network?
- What hardware does a small Valley business actually need?
- How long does a Hudson Valley network installation take?
- Can the upgrade happen without closing the business?
- What is a wireless site survey, and when is it worth it in the Valley?
- Do we need a managed switch in every building?
- Are the licensing rules the same across all six counties?
- Cat6 or Cat6A on the runs feeding access points?
- Who installs business networks in the Hudson Valley?
- Do I need a permit for network cabling up here?
- Do you adopt networks that another contractor installed?
- Will faster internet fix slow Wi-Fi?
- Can you consolidate our three internet bills into one?
- Can you work alongside our IT provider?
- Do you cover outdoor areas?
- Do you do emergency network repair?
- What does a site survey cost here?

### network-installation-long-island (23 questions)

- How much does network installation cost on Long Island?
- Why does a wide Long Island building need more than one telecom room?
- What does a commercial network installation on the Island actually include?
- Network installation or structured cabling — which am I actually buying?
- How many Wi-Fi access points does my Long Island office need?
- Why is my office Wi-Fi slow in some areas and fine in others?
- Does guest Wi-Fi need to be kept off the staff network?
- What network equipment does a small business need?
- How long does a Long Island network installation take?
- Can you upgrade our network without shutting the business down?
- What is a wireless site survey, and is it worth it on Long Island?
- Is a managed switch necessary in a multi-room building?
- Do you work after hours and weekends?
- Cat6 or Cat6A for the runs that feed access points?
- Who installs business networks on Long Island?
- Do I need a permit for network cabling on Long Island?
- Will you take over a network somebody else built?
- Will faster internet fix slow Wi-Fi?
- Can you work alongside our IT provider?
- Do you supply equipment, or can we?
- Can you link two buildings on the same property?
- Do you do emergency network repair?
- What does a site survey cost here?

### network-installation-manhattan (24 questions)

- How much does network installation cost in Manhattan?
- Why do Manhattan network quotes vary so much for the same drop count?
- What does a network installation on a Manhattan floor include?
- Am I buying network installation or structured cabling?
- How many access points does a Manhattan office floor need?
- Why is our wireless strong in one office and unusable in the next?
- Does guest wireless need its own segment in a client-facing office?
- What hardware does a Manhattan tenancy need?
- How long does a Manhattan network installation take?
- Can the work happen without disrupting the office?
- Is a wireless survey worth paying for in Manhattan?
- Do we need a managed switch?
- Do you work evenings and weekends?
- Cat6 or Cat6A for the drops feeding access points?
- Who installs business networks in Manhattan?
- Is it the network, the building, or the carrier?
- Do we need a DOB permit for network cabling?
- Can you handle the managing agent for us?
- Will a faster circuit fix slow wireless?
- Can you work with our IT provider?
- Do you supply hardware, or can we?
- What if the building cancels our freight window?
- Do you do emergency repair?
- What does a survey cost?

### network-installation-nassau-county (23 questions)

- How much does network installation cost in Nassau County?
- Why does a medical suite cost more to network than an office of the same size?
- Our network slows down when imaging sends a study. Is that fixable?
- What does a Nassau network installation include?
- Is this network installation or structured cabling?
- How many access points does a medical suite need?
- Nothing works inside our imaging room. Why?
- Does patient wireless need to be separate from clinical systems?
- Will our practice have to close for the work?
- How long does an installation take?
- Is it worth paying for a wireless survey in this county?
- We share a telecom room with other practices in the building. Is that a problem?
- Do we need a managed switch?
- Do the radio runs want Cat6 or Cat6A?
- Who installs business networks in Nassau County?
- Is a permit needed for network cabling?
- Are you licensed to work in Nassau?
- Will our practice have to close?
- Why does nothing work inside the imaging room?
- Can you work with our IT provider?
- Should patient wireless be separate?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-nyc (23 questions)

- How much does network installation cost in NYC?
- What is included in a commercial network installation?
- What is the difference between network installation and structured cabling?
- How many Wi-Fi access points does my office need?
- Why is my office Wi-Fi slow in some rooms and fine in others?
- Should guest Wi-Fi be separated from staff Wi-Fi?
- What network equipment does a small business actually need?
- How long does office network installation take?
- Can you upgrade our network without shutting the office down?
- What is a wireless site survey or heat map, and when is it worth paying for?
- Do I need a managed switch, or will an unmanaged one work?
- Do you work after hours in occupied offices?
- Should I use Cat6 or Cat6A for the runs feeding access points?
- What documentation do we get at closeout?
- Who installs business networks in NYC?
- Do I need a permit for network installation in NYC?
- Do you repair and take over existing networks?
- Will faster internet fix slow Wi-Fi?
- Can you work with our MSP or IT provider?
- Do you supply the equipment, or can we?
- What is a demarc extension?
- Do you do emergency network repair?
- How much does a wireless site survey cost?

### network-installation-orange-county (23 questions)

- How much does network installation cost in Orange County?
- Why does the timing of our construction schedule change the price so much?
- What should we install during rough-in that we might not need yet?
- How do you network a building of several hundred thousand square feet?
- What does an Orange County network installation include?
- Is this network installation or structured cabling?
- Why do our handhelds drop as staff move through the building?
- How many access points does a building here need?
- Does the operations segment really need to be separate?
- How long does an installation take?
- Can you work alongside our general contractor?
- Is a wireless survey worth paying for on a building that is not finished?
- Do we need a managed switch?
- Which grade should feed the radios, Cat6 or Cat6A?
- Who installs business networks in Orange County?
- Does network cable need a permit here?
- Are you licensed to work in Orange County?
- When do you need to be on our construction site?
- Should we pull spare cable during rough-in?
- Can you work with our general contractor?
- Handhelds keep dropping as staff move down the aisles — can that be fixed?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-putnam-county (23 questions)

- How much does network installation cost in Putnam County?
- Do we really need managed switches on a site this small?
- What happens if the network goes down on a Tuesday morning?
- What does a Putnam network installation include?
- Is this network installation or structured cabling?
- How many access points does a small Putnam building need?
- Our Wi-Fi is fine in the front and useless in the back. Why?
- Should guest wireless be separate?
- How long does an installation take here?
- Will we have to shut for this?
- Is a wireless survey worth it on a job this size?
- Can you support us if we already have an IT provider?
- What grade should the radio runs be?
- Are the licensing rules different from the city?
- Who installs business networks in Putnam County?
- Do we need a permit to run network cable?
- Are you licensed to work in Putnam?
- Do we really need managed switches on a small site?
- Can you fix things without coming out?
- Can you work with our IT provider?
- What is the rack card?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-queens (24 questions)

- How much does network installation cost in Queens?
- Why can two Queens quotes for the same headcount be so far apart?
- What does a Queens network installation include?
- Is this network installation or structured cabling?
- How many access points does a Queens office need?
- Our Wi-Fi is slow but the cable is fine. What is going on?
- Does guest wireless need its own segment?
- What hardware does a small Queens business need?
- How long does a Queens network installation take?
- Can the work happen without closing the business?
- Is a wireless survey worth it in Queens?
- Do we need a managed switch?
- Do you work evenings and weekends?
- Which category should the access point runs be — Cat6 or Cat6A?
- Who installs business networks in Queens?
- Network, building, or neighbour?
- Does network cabling require a permit?
- Can you fix wireless without replacing everything?
- Our neighbours' Wi-Fi seems to affect ours. Is that real?
- Can you work alongside our IT provider?
- Do you supply hardware, or can we?
- Who owns the demarc room in our building?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-rockland-county (24 questions)

- How much does network installation cost in Rockland County?
- Why does a suite in a big corporate building cost more to network than a freestanding one?
- What is a boundary trace and why does it matter?
- What does a Rockland network installation include?
- Is this network installation or structured cabling?
- How many access points does a Rockland suite need?
- Our neighbours' wireless seems to interfere with ours. Is that real?
- Can our equipment stay in the shared telecom room?
- How long does a Rockland network installation take?
- Can the work happen without interrupting the business?
- Does paying for a wireless survey make sense here?
- Do we need a managed switch?
- Are the licensing requirements the same as in the city?
- Should the radio runs be Cat6 or Cat6A?
- Who installs business networks in Rockland County?
- Your suite, your neighbours, or the carrier?
- Is a permit needed to run network cable?
- Are you licensed to work in Rockland?
- Can our rack live in the shared telecom room?
- Who pays for the demarc extension?
- Can you work with our IT provider?
- Our neighbours' wireless seems to affect ours. Real?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-staten-island (23 questions)

- How much does network installation cost on Staten Island?
- Should our network equipment be mounted off the floor?
- How do you link two buildings on the same lot?
- What does a Staten Island network installation include?
- Why does a wide single-story building need more than one room?
- Is this network installation or structured cabling?
- How many access points does an island building need?
- Our Wi-Fi is weak at the back of the building. Why?
- Does guest wireless need its own segment?
- How long does an installation take here?
- Can the work happen without disrupting the business?
- Is a wireless survey worth paying for on the island?
- Do we need a managed switch?
- Which cable grade should feed the radios — Cat6 or Cat6A?
- Who installs business networks on Staten Island?
- Is a permit required to pull network cable?
- Should the rack be off the floor?
- Can you link two buildings on our lot?
- Can you consolidate our two internet bills?
- Can you work alongside our IT provider?
- Do you cover yards and lots?
- Do you do emergency network repair?
- What does a survey cost?

### network-installation-suffolk-county — OLD template page, before this rebuild (22 questions; text replaced 2026-10-18, kept here so later builds avoid these intents too)

- How much does network installation cost in Suffolk County?
- Does it cost more to have you work on the East End?
- Why do you want a second network room in our building?
- What does a Suffolk network installation include?
- Is this network installation or structured cabling?
- Our scanners drop as staff walk the warehouse. Can that be fixed?
- How many access points does an industrial building need?
- Is a separate segment for operations actually necessary?
- How long does an installation take here?
- What are on-site spares and do we need them?
- Can you work around our season?
- Is a wireless survey worth paying for?
- Do we need a managed switch?
- What grade of cable should feed the radios?
- Who installs business networks in Suffolk County?
- Is a permit needed to run network cable?
- Are you licensed to work in Suffolk?
- Do you actually come out to the East End?
- Why do you want a second room in our building?
- Handhelds keep losing connection as staff move down the aisles. Fixable?
- What are on-site spares?
- What does a survey cost?

### network-installation-ulster-county (23 questions)

- How much does network installation cost in Ulster County?
- Our Wi-Fi works all winter and fails every summer. Why?
- Should payment terminals be on the wireless?
- Can you run cable on the outside of a building in the Stockade or Rondout?
- What does an Ulster network installation include?
- Is this network installation or structured cabling?
- How many access points does a busy restaurant or tasting room need?
- Does the guest network really need a throughput ceiling?
- How long does an installation take here?
- Can you schedule around our season?
- Is a wireless survey worth paying for?
- What happens to the network in a power cut?
- Do we need a managed switch?
- Which cable grade belongs on the radio runs?
- Who installs business networks in Ulster County?
- Is a permit needed to run network cable?
- Are you licensed to work in Ulster?
- Our Wi-Fi only fails when we are busy. Why?
- Can you run cable across the front of our building?
- Should our card terminals be on wireless?
- Can you do the work off-season?
- Do you cover terraces, barns and event fields?
- What does a survey cost?

### network-installation-westchester-county (24 questions)

- How much does network installation cost in Westchester?
- Why do Westchester quotes vary so much for the same drop count?
- Can we reuse the cable a previous tenant left behind?
- Who is responsible for removing abandoned cable?
- What does a Westchester network installation include?
- Is this network installation or structured cabling?
- How many access points does a Westchester office need?
- Our wireless is fine in the open plan and poor in the offices. Why?
- Does conference AV need its own segment?
- How long does a Westchester network installation take?
- Will installation interrupt the working day?
- Does a wireless survey pay for itself in this county?
- Do we need a managed switch?
- Cat6 or Cat6A for the runs feeding radios?
- Who installs business networks in Westchester County?
- Is it your network, your building or your carrier?
- Do we need a permit for network cabling?
- Are you licensed to work in this county?
- Can we reuse the cable the last tenant left?
- Who pays to remove abandoned cable?
- Can you work with our IT provider?
- Will a faster circuit fix slow wireless?
- Do you do emergency network repair?
- What does a survey cost?


### network-installation-suffolk-county — REBUILT 2026-10-18 (final, 19 headings + 10 FAQ)

1. Suffolk Network Down Right Now? — repair-capture heading
2. Only one wired carrier serves our Suffolk address — how should the network be designed around that? — §9 Q&A
3. Is a cellular backup line worth having on the East End, when summer crowds already overload the cell towers? — §9 Q&A
4. Should the all-in-one box from Optimum or Verizon stay in charge of the network? — §9 Q&A
5. We have a standby generator — does the network still need batteries? — §9 Q&A
6. When the battery is running down during a long outage, which equipment should stay on longest? — §9 Q&A
7. After a thunderstorm a few switch ports stopped working — what does that say about the network? — §9 Q&A
8. What did Suffolk County government's 2022 ransomware attack show that a small business network should copy? — §9 Q&A
9. Our alarm, phone and software vendors each want remote access — how should we let them in? — §9 Q&A
10. An employee who knew all the network passwords has left — what has to change? — §9 Q&A
11. Our Hauppauge flex unit used to be part of a bigger bay — how do we know which cables and closets are really ours? — §9 Q&A
12. Our house was raised after Sandy and the new ground-level space looks perfect for the network equipment — is it? — §9 Q&A
13. We close our Montauk shop from November to April — can the network be left running with nobody there? — §9 Q&A
14. A new building near the Ronkonkoma station handed us jacks that have never been used — what should be checked before move-in? — §9 Q&A
15. We have an office in Melville and a branch in Riverhead — can they work as one network? — §9 Q&A
16. How much of the network will our security cameras actually use? — §9 Q&A
17. Staff say their phones have no signal inside our steel building — is Wi-Fi calling enough? — §9 Q&A
18. Does Suffolk's home improvement licence cover network wiring in a home office? — §9 Q&A
19. Do towns and villages in Suffolk add their own rules on top of the county's? — §9 Q&A
F1. What should we have ready before the Suffolk crew arrives? — §17 FAQ
F2. How is payment handled on a Suffolk network installation? — §17 FAQ
F3. Do you install networks in Suffolk homes, or only in businesses? — §17 FAQ
F4. Can you design the network from our floor plan before anyone visits? — §17 FAQ
F5. What happens if the internet provider's installation date slips past our opening date? — §17 FAQ
F6. Will you need to get onto the roof or into the attic? — §17 FAQ
F7. Can the same network carry our desk phones? — §17 FAQ
F8. How far ahead should an East End business book work before the summer season? — §17 FAQ
F9. Can we check the network's status ourselves from a phone? — §17 FAQ
F10. If we move out of the building, can the network come with us? — §17 FAQ
