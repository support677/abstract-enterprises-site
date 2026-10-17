# Research — Cat6 Repair silo

Built 2026-10-17 (batch run, first page of the silo: cat6-repair-nyc). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Sources the build environment could not open are written `EMPTY (not accessible in build env)`; nothing is inferred to fill a gap. Tools used: WebSearch (result titles/URLs only) and WebFetch (page read + summarised). Shell curl/wget is blocked.

Differentiation note: this silo sits between two live silos. `network-cable-repair-*` covers any copper/Ethernet fault generally (callout speed, the switch-vs-cable question, COI, documentation, Cat5e upgrade). `cat6-installation-*` covers new drops (per-drop pricing, drop counts, plenum, 10G distance, CCA avoidance). Cat6 Repair pages take the narrower thesis: **an installed Cat6 link that no longer performs to its category** — certification failures (NEXT, return loss, insertion loss, wire map), the re-terminate / replace-the-cord / re-pull decision, PoE faults on Cat6, Cat6 vs Cat6A repair differences, and tracing undocumented Cat6 in NYC buildings. Questions on those two silos' NYC hubs were read and avoided (see register).

## Silo-wide findings

### 1. Reddit
- Query: `reddit cat6 run failing certification NEXT re-terminate or replace cable` · WebSearch → no reddit.com URL returned. Results were Fluke knowledge-base and trade pages (used under §9 below). Reddit: EMPTY.
- Query: `reddit NYC apartment ethernet cable in wall damaged landlord fix` · WebSearch → no reddit.com URL returned. Nearest NYC-specific result used: https://www.brickunderground.com/improve/how-to-make-wifi-signal-better-in-nyc-apartment (WebFetch) — Brick Underground, Mimi OConnor, Jan 29 2019; quotes Peter Lopez: "New York City walls are full of all sorts of stuff: piping, plumbing, cement, brick"; plumbing "a big wifi killer"; running Ethernet is the most effective fix, can involve "drilling holes in floors/ceilings", ~$200 simple to ~$1,200 complex (third-party figure). → NYC hub §5 THE NEIGHBORHOOD (why wired links matter in NYC walls), §10.5 reality check.
- Query: `site:reddit.com ethernet wall jack stopped working only 100mbps cat6 split pair` · WebSearch → no reddit.com URL returned. EMPTY. Substitute: https://www.computercablestore.com/ethernet-stuck-at-100-mbps-how-to-fix-gigabit-speed (WebFetch): "Gigabit Ethernet requires all four twisted wire pairs"; 100 Mbps "can operate using only two pairs"; "A fault on the blue or brown pair is a common reason a connection may fall back to 100 Mbps" (pins 4,5,7,8); split pairs pass continuity but "can prevent a reliable Gigabit link". → NYC hub §9 Q "jack links at 100 Mbps", §6 services, field notes.

### 2. Google People Also Ask — EMPTY (not accessible in build env)
### 3. Google PASF — EMPTY (not accessible in build env)
### 4. Answer the Public — EMPTY (not accessible in build env)
### 5. Google AI Overview — EMPTY (not accessible in build env)
Substituted with claims published by cost guides and vendor blogs (quoted as those pages state them; not presented as AI Overview text):
- Query: `cat6 cable repair cost per hour national average network cable repair cost guide 2025` · WebSearch → https://www.fixr.com/costs/upgrading-to-cat6-cabling (WebFetch): updated Jan 31 2025; Cat6 project $2,000–$5,000, national average $3,800 (≈2,000 ft, 8 drops); $125–$250 per drop; $0.90–$1.55/ft installed; labour $45–$75/hr. → NYC hub §10.5 H3 on national cost figures; §14 pricing (labelled third-party national).
- Query: `copper clad aluminum CCA Cat6 PoE problems overheating NEC` · WebSearch → https://www.ipsecuritydepot.com/blog/why-cca-ethernet-cable-fails-poe-installs/ (WebFetch, vendor blog Aug 2026): CCA "roughly 58 percent higher resistance than copper"; 802.3at PD needs ≥42.5 V at input; aluminium work-hardens and fractures at punch-downs; "TIA-568 specifies solid copper conductors" so CCA "cannot form part of a certified channel". → NYC hub §9 Q on identifying CCA, §6 services, §10.5. Belden blog (https://www.belden.com/blog/smart-building/cca-cable-5-reasons-to-stay-away): WebFetch blocked (permission not answered) — EMPTY.

### 6/7. Landmarks / use cases — see NYC section.

### 8. Bing & DuckDuckGo — EMPTY (not accessible in build env)

### 9. Technical / trade sources (substitute for news on the technical side)
- Query: `Fluke Networks NEXT failure causes untwist termination Cat6 troubleshooting` · WebSearch → https://www.flukenetworks.com/knowledge-base/dsx-cableanalyzer-series/next-near-end-crosstalk-troubleshooting-dsx-cableanalyzer (WebFetch): "In many cases, excessive crosstalk is due to poorly twisted terminations"; 13 mm of untwist "does not guarantee a PASS"; voice-grade patch cords, split pairs and "Female couplers ... should not be used in a data installation"; wrong test limit; locate failing end, re-terminate; time-domain (HDTDX) shows "the fault by distance". → NYC hub §9 certification cluster, §10 equipment, §12 process, §10.5.
- Same search → https://open-exam-prep.com/study-guides/bicsi-inst2-copper/troubleshooting/transmission-failure-analysis (WebFetch; BICSI-style study guide): NEXT causes (untwist >13 mm, split pairs, Cat5e cord in Cat6 channel, crushed by ties/staples) → re-terminate; return loss causes (kinks, bend radius, over-tight ties, pull tension >25 lbf/110 N, water, bad connectors) — near-end → cord/jack, far-end → remote termination, mid-span → replace run; insertion loss → length >90 m permanent link / 100 m channel, temperature above 20 °C, stranded cable; wire map pass ≠ speed capability. → NYC hub re-terminate vs re-pull decision table, §9.
- Query: `Cat6 10GBASE-T 55 meters TSB-155 alien crosstalk Cat6A 100 meters` · WebSearch → https://icc.com/help/can-icc-cat6-solution-support-10gbase-t/ (WebFetch): per TSB-155-A, 10GBASE-T over Cat6 "up to 37 meters", and "between 37 and 55 meters" depending on alien crosstalk; Cat6 "not recommended for NEW installations targeted to support 10GBase-T". → NYC hub Cat6 vs Cat6A repair section, §9 Q on 10G errors.
- Query: `TIA TSB-184-A PoE bundle size temperature rise 802.3bt 90W Cat6` · WebSearch → https://www.belden.com/blog/how-the-new-tsb-184-a-standard-supports-poe (WebFetch): TSB-184-A approved March 2017; up to 1000 mA per pair, max 100 W; temperature rise "can push cables beyond their rated temperatures"; unbundled or small bundles, limits bundles to 24 cables; recommends Cat6A or better for new PoE. → NYC hub PoE section, §9 PoE cluster.
- Query: `NEC 800.25 abandoned cable removal accessible portion NYC electrical code low voltage` · WebSearch → https://www.ecmag.com/magazine/articles/article-detail/codes-standards-removing-old-cable-bonding-hot-tubs-and-more (WebFetch): "All accessible portions of abandoned cable must be removed" — 800.25 (communications), 820.25 (CATV); cable tagged for future use may stay (answer based on 2014 NEC). → NYC hub §8.5 compliance, re-pull section.
- Query: `New York City Electrical Code based on 2017 NEC effective date DOB` · WebSearch → https://www.nyc.gov/site/buildings/codes/electrical-code.page (WebFetch): current NYC Electrical Code = NYC amendments to the 2020 NEC (NFPA 70); "took full effect on December 21, 2025". → NYC hub §8.5 compliance, §5.5 facts.

### 10. Local news / hyperlocal
- Query: `Hurricane Ida 2021 NYC basement flooding damaged electrical building systems news` · WebSearch → https://www.citylandnyc.org/dob-issues-advice-after-historic-flooding-from-ida/ (WebFetch): DOB advice Sept 2 2021 after Ida flash flooding; flooding can damage electrical wiring; "Never attempt to turn off the power or operate a circuit breaker while standing in water"; extensive repairs may need registered contractors/permits. → NYC hub §9 water-damage question, building section (cellar closets).
- Query: `rats chewing cables NYC building internet outage news` · WebSearch → no NYC-specific article returned (results were Mallorca, Scotland, Singapore, generic). EMPTY for NYC. Not used.
- Hyperlocal (BK Paper/Eagle, Bronx Times, Queens Chronicle, SI Advance) on Cat6 repair specifically: no relevant result in the searches above. EMPTY.

### 11. Yelp 1–3★
- Query: `yelp network cabling New York review technician ethernet not working` · WebSearch → no yelp.com URL returned. EMPTY (not accessible in build env). Thumbtack NY ethernet-wiring page (https://www.thumbtack.com/ny/new-york/ethernet-wiring, WebFetch): no prices, only two positive reviews — no complaints to use. Not used.

### Keywords (five layers)
- Service: Cat6 repair, Cat6 cable repair, Cat6 re-termination, Cat6 jack repair, Cat6 patch panel repair, Cat6 certification / recertification, Cat6 cable testing, Cat6 tracing / toning, Cat6 re-pull.
- Problem: failing Cat6 run, NEXT failure, return loss failure, wire map fail, split pair, open pair, crossed pair, link stuck at 100 Mbps, intermittent drop, crushed/kinked Cat6, PoE camera no power, PoE reboot, water-damaged Cat6, undocumented cable.
- Technology: Cat6, Cat6A, Cat5e, TIA-568, permanent link, channel, keystone, 110 punch-down, RJ45 plug, PoE 802.3af/at/bt, TSB-184-A, TSB-155-A, 10GBASE-T, CCA vs solid copper, CMR / CMP.
- Industry: offices, medical suites, restaurants/POS, retail, warehouses/food distribution, co-ops/condos (building management), lofts.
- Geographic: NYC, New York City, five boroughs, Manhattan, Brooklyn, Queens, the Bronx, Staten Island (borough pages pending — /free-quote anchors).

## NYC section (cat6-repair-nyc)

### Landmarks / corridors (all verified)
- Query: `60 Hudson Street carrier hotel Western Union building telecommunications hub history` · WebSearch → https://datacenterdynamics.com/en/analysis/new-york-new-york-the-nyc-carrier-hotel-microcosm (WebFetch): 60 Hudson St 1928–1930 Western Union HQ, 24 floors, became AT&T telecom hub after WU left in the 1980s; 32 Avenue of the Americas = AT&T Long Lines Building, 27 floors, built in phases from 1911, final work 1929–1932; 111 8th Avenue completed 1932 as Port Authority Building, acquired by Google 2010. → §8 corridors, §13 landmarks.
- Query: `Brooklyn Navy Yard number of businesses employees 300 acres` · WebSearch → https://www.bisnow.com/news/new-york/commercial-real-estate/whats-really-happening-at-the-brooklyn-navy-yard-21478 (WebFetch, Jan 29 2014): ~300 acres; 330 manufacturing businesses; ~7,000 workers; Building 77 960,000 SF 16 storeys (then under renovation). Stated with its 2014 date. → §8 corridors.
- Query: `Industry City Sunset Park 35 acres buildings tenants` · WebSearch → https://brooklyneagle.com/articles/2025/04/08/industry-city-surpasses-650-businesses/ (WebFetch, Apr 8 2025): 650+ businesses, 35 acres, ~6 million sq ft, 16 buildings. → §8 corridors, §13.
- Query: `Teleport Staten Island Bloomfield office park history fiber` · WebSearch → https://en.wikipedia.org/wiki/Teleport_(Staten_Island) (WebFetch): 100-acre business park, five buildings ~700,000 sq ft, developed mid-1980s by the city and the Port Authority, satellite and fiber connectivity; AT&T moved ~4,000 employees out in 2001; two buildings sold 2009 to Nicotra Group (Corporate Commons). → §8, §13.
- Query: `Hunts Point Food Distribution Center 329 acres businesses NYCEDC` · WebSearch → https://www.nycfoodpolicy.org/hunts-point-distribution-center-brief-overview-spotlight-produce-market/ (WebFetch, 2018 article): 329 acres, 155+ wholesalers; Produce Market ~60% of produce sales in NYC; Cooperative Meat Market six refrigerated/freezer buildings ~1,000,000 sq ft refrigerated space. → §8 corridors (cold-room cabling).
- Query: `Long Island City Court Square office buildings converted industrial loft Queens tech businesses` · WebSearch → https://newyorkyimby.com/2016/12/reveal-for-warehouse-to-office-conversion-and-expansion-at-11-20-46th-road-in-long-island-city.html (WebFetch, Dec 20 2016): 11-20 46th Road two-storey warehouse converted to four-storey, 32,000 sq ft offices (C3D Architecture). → §8 corridors (warehouse-to-office conversions).
- Carried from research/smart-lock-installation.md row N14 (sources reached by earlier runs): Rent Guidelines Board 2025 Housing Supply Report — 54% of units in pre-1947 buildings; Co-op City 15,372 apartments in 35 high-rises + 7 townhouse clusters; Park Slope Historic District 1973/2016. Row N13: 2023 NYCHVS 3.7 million housing units (HPD testimony). → §5.5 facts, §13 landmarks.

### Building stock / use cases (from the sources above)
- Pre-war masonry and plaster (54% of units pre-1947) → cable in old chases, through masonry, fished in plaster; repair access, not cable cost, drives time.
- Carrier hotels and converted industrial lofts (60 Hudson, 32 AoA, 111 8th, Industry City, Navy Yard, LIC conversions) → dense trays, decades of abandoned cable (NEC 800.25), unlabeled runs.
- Cold storage at Hunts Point → condensation at transitions, corrosion (matches return-loss/water causes above).
- Co-ops/condos/managed towers → managing-agent approval, COI, contractor hours (mentioned in body only; COI question already on network-cable-repair-nyc FAQ).

### Local licensing / permits
- NYC Electrical Code (2020 NEC + NYC amendments) effective Dec 21 2025 — nyc.gov (above).
- NEC 800.25 abandoned communications cable — EC&M (above).
- DOB Ida advisory Sept 2 2021 — CityLand (above).
- AESS NYS licence #12000287431 (site constant).

### Prices used on cat6-repair-nyc (only from live AESS pages)
- $195/hr, three-hour minimum ($585) — network-cable-repair-nyc.html (and every network-cable-repair area page).
- Replacement Cat6 drop where a run must be re-pulled: from $175 per drop — network-cable-repair-nyc.html ("new commercial Cat6 drops start at $175 per drop"); network-cable-repair-manhattan/bronx include cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord. Published at $175 on borough pages including Manhattan, so no §9 multiplier applied (applying one would contradict live borough pages) — flagged for review.
- New-install drop prices for comparison: Cat5e $233, Cat6 $272, Cat6A $388 per drop to 100 ft — cat6-installation-nyc.html pricing table.
- Exterior entry sealed and bonded: from $185 per penetration — network-cable-repair-bronx.html.
- Third-party national (labelled as such): Fixr Jan 2025 $125–$250 per drop, $45–$75/hr.

## Question register — cat6-repair-nyc

Section §9 "Questions Answered" (H3):
1. Why does a Cat6 jack show a link light but only connect at 100 Mbps?
2. Why would a Cat6 run that worked for years start dropping out intermittently?
3. How do I know whether the problem is the patch cord, the jack or the cable in the wall?
4. What does it mean when a Cat6 link fails NEXT on a certification test?
5. Our run fails return loss but passes wire map — what does that point to?
6. If a link passes at the panel but fails at the desk, which end gets re-terminated?
7. When is re-terminating a failed Cat6 run pointless and a re-pull the only fix?
8. Can a single damaged section of Cat6 be spliced, or does the whole run come out?
9. Why does a PoE camera on Cat6 keep rebooting at night?
10. Can one bad Cat6 run take a PoE switch port down with it?
11. Should a damaged Cat6A run be repaired with Cat6 parts?
12. Our Cat6 links at 10G but throws errors — is the cable the problem?
13. How can I tell if the "Cat6" in my walls is actually copper-clad aluminum?
14. Who has to approve a Cat6 repair that goes through a riser or a neighbour's ceiling?
15. Can you trace a Cat6 run that disappears into a pre-war wall without opening plaster?
16. A cellar network closet took on water — can the Cat6 dry out and be reused?

FAQ (§17, = FAQPage schema):
F1. Is the three-hour minimum charged even if the Cat6 fix takes twenty minutes?
F2. Can you recertify a whole floor of Cat6 rather than just the failed links?
F3. Can you repair Cat6 that another contractor installed?
F4. Will re-terminating change which switch port each desk lands on?
F5. Do you carry Cat6A parts on the van as well as Cat6?
F6. How long does it take to re-terminate a full 24-port Cat6 patch panel?
F7. What happens to the old cable when a Cat6 run is re-pulled?
F8. Can a Cat6 run be rerouted around a new wall instead of re-pulled end to end?
F9. Do you fix Cat6 runs that feed Wi-Fi access points in the ceiling?
F10. Can you repair a Cat6 run between two buildings on the same lot?

Other "?" headings: "Cat6 Link Down in New York City Right Now?" (repair capture), "Failing Cat6 Run in NYC Today?" (closing).

Avoided (already on network-cable-repair-nyc / cat6-installation-nyc FAQ/headings): repair-vs-replace in general, callout speed, cost of network cable repair, COI for building (COI mentioned in body only), documentation proving a repair passed, cameras/access-control cabling, Cat5e→Cat6 upgrade, work in occupied hours, switch vs cable, labelling undocumented cables, service outside the five boroughs, warranty question (warranty sentence placed in pricing body instead), 10G support, CCA avoidance (ours is identification), plenum, drop count, drop cost, testing after install, max distance.

Angles reserved for the other Cat6 Repair hubs (do not reuse on Long Island / Hudson Valley): the 16 §9 questions and 10 FAQ questions above.


---
<!-- merged from batch build cat6-repair-long-island, 2026-10-17 -->
## Long Island hub (cat6-repair-long-island)

Batch run 2026-10-17. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources in research/cat6-repair.md (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25) are reused only in general terms. To be merged into research/cat6-repair.md by the main run.

**Thesis (different from the NYC hub):** NYC = access, risers, pre-war plaster, managed buildings. Long Island = the environment around the cable: attic/roof-deck heat (insertion-loss derating), horizontal distance on wide one-storey floorplates (90 m limit), outdoor and between-building runs (storm, lightning, water, salt air, landscaping), seasonal/idle East End buildings, slab-house attic access. Repair decision on LI is "will the new run fail for the same environmental reason", not "can we get a pull through the riser".

### Reddit (local)
- Query: `site:reddit.com r/longisland ethernet cable office network wiring problem` · Firecrawl search (excerpts only; Firecrawl does not scrape reddit.com) →
  - https://www.reddit.com/r/longisland/comments/1l9fokf/looking_for_a_company_that_will_run_cat6_cables/ — excerpt: "Anyone know a company that will come run Cat6 cables for my cameras and access points at minimum?" → background for §5 para 5 (Cat6 installed by camera vendors / owners) and §10.5 H3 "mesh" (cameras/APs need the wire). Not quoted on page.
  - https://www.reddit.com/r/longisland/comments/1kvzp6g/low_voltage_tech_for_wiring_home_with_ethernet/ — excerpt: "I think any electrician should be able to help you." → §10.5 H3 "Any electrician can repair network cable" (claim framing; not quoted).
  - https://www.reddit.com/r/longisland/comments/t9o47b/recommendations_for_home_ethernet_wiring_in_new/ — excerpt (MoCA over coax suggestion) → not used.
- Fault-specific LI Reddit threads (failing runs, attic heat, storm damage): EMPTY (not accessible in build env — reddit not scrapeable, search returned no fault threads).

### PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states that the AI Overview could not be viewed and frames each H3 as a commonly published claim, corrected with sourced facts below.

### Local licensing / code
- Query: `Suffolk County Code Chapter 563 Article XI electrician license low voltage installer` · Firecrawl search → https://ecode360.com/14948079 (Firecrawl scrape, directQuote): "It shall be unlawful … for any person to engage in and carry on in the County any business, trade or calling for hire regulated by this article without having first obtained a license … from the Office"; RESTRICTED LICENSE = "A license to engage in a limited area or areas within a specific business regulated by this article"; fee $100 (not used); "This article shall not be applicable within any town or village which has hereinbefore enacted legislation regulating the licensing of business, trade or enterprise … nor in any town of the second class which elects by local law not to have this article apply". → §8.5 Suffolk bullet; §10.5 H3 electrician; Nassau/Suffolk section.
- Query: `Nassau County Office of Consumer Affairs home improvement license contractor requirement` · Firecrawl search → https://www.nassaucountyny.gov/1547/Consumer-Affairs and https://www.nassaucountyny.gov/1563/Licensing-Registrations (search excerpts): "All Licensed Home Improvement Contractors must be fingerprinted. Fingerprinting is done at IDENTOGO". Scrape of https://www.nassaucountyny.gov/1566/Obtaining-a-Home-Improvement-License returned only the JS shell (no body text) — "who must be licensed" detail EMPTY. → §8.5 Nassau bullet (residential home-improvement licensing + fingerprinting only).
- Query: `NEC 800.90 primary protector communications cable outdoor run between buildings lightning exposure Ethernet surge` · Firecrawl search → https://www.mikeholt.com/instructor2/img/product/pdf/11LE-968-sample.pdf (excerpt): "The primary protector must be located as close as practicable to the point at which the cable enters the building [800.90(B)]". → §7.5 outdoor paragraph, §8.5 entry-protection bullet, §9 garage Q, §10.5 surge H3, FAQ F7.
- NEC 800.25 abandoned cable (EC&M, silo research) → §8.5, process step 5.
- Municipal structure (carried from research/fiber-optic-installation.md LI hub, ny.gov county pages): Nassau "Two cities, three towns, 64 incorporated villages", 453 sq mi; Suffolk "10 towns", 2,373 sq mi. → §5.5, §8.5 permits bullet, Nassau/Suffolk section.
- Town/village low-voltage permit specifics: EMPTY (carried finding from fiber research; page says only that permits are issued by town/village/city and checked per address).

### Building stock / landmarks / corridors
- Query: `Long Island ranch houses built 1950s Levittown number of homes slab construction` · Firecrawl search → https://kerimurrayarchitecture.com/levittown-ny/ (scrape, directQuote): "Built between 1947-1951"; "built on concrete slabs"; "ranch homes built on concrete slabs, included an expandable attic but no garage, and were heated with hot-water radiant heating pipes"; "17,447 homes were constructed in Levittown between 1947 and 1951". → §5 para 1, §5.5, §7 slab-ranch card, §9 slab Q, §13 Levittown card.
- Query: `Long Island Expressway Route 110 Melville office park built 1970s 1980s history corridor` · Firecrawl search → https://iraceenterprises.com/route-110-corridor/ (excerpt): "The corridor spans Farmingdale, Melville, and Huntington Station, supporting a dense concentration of warehouse, flex, R&D, and office uses. LIE access…". NYT 1997 article (https://www.nytimes.com/library/realestate/commercial/ir970420.html): scrape refused — EMPTY. → §8 Route 110 card.
- Carried from research/fiber-optic-installation.md (LI hub, sources fetched by that run): Hauppauge park 1,350 businesses, $13.4B revenue, ~55,000 workers, ~11 sq mi, two-thirds under Town of Smithtown overlay (cmmllp.com 2017); renamed Long Island Innovation Park at Hauppauge (cmmllp.com Apr 2019); Melville Corporate Center I, 105 Maxess Rd, 149,000 s/f (nyrej.com 2019); RXR Plaza Uniondale beside Meadowbrook Pkwy with LIE/Northern/Southern State access, "West Tower" (CBRE listing); Stony Brook University 213 buildings / 1,454 acres + R&D park (Wikipedia); Hofstra ~117 buildings / 244 acres, Uniondale section of Hempstead, part south of Hempstead Tpke (Wikipedia); Brookhaven National Laboratory est. 1947 at Camp Upton, 5,265 acres (Wikipedia); Isaias "almost half of PSEG's 1.1 million customers in the dark at the peak" (abc7ny.com Aug 2020); Sandy — Long Beach $150M damage, Nassau voluntary evacuations of South Shore surge area south of Sunrise Highway (Wikipedia). → §5, §5.5, §8 cards, §13 cards, Nassau/Suffolk section.
- Query: `Roosevelt Field mall square feet stores Garden City largest mall Long Island` · Firecrawl search → https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) (scrape): East Garden City section of Uniondale; largest mall on Long Island; 243 stores; 2,372,053 ft² GLA; built on Roosevelt (Hazelhurst) Field where Lindbergh began his transatlantic flight; airfield closed 1951. → §8 Old Country Road card, §13 card.
- Query: `Long Island MacArthur Airport Ronkonkoma Hub redevelopment acres Islip` · Firecrawl search → https://govmarketnews.com/suffolk-county-master-developer-rfp-ronkonkoma-hub/ (excerpt): Suffolk "restarting its search for a master developer to transform 48 acres within the broader 179-acre redevelopment area between Long Island MacArthur Airport and the Ronkonkoma Long Island Rail Road station"; https://libn.com/2026/07/02/suffolk-issues-rfp-ronkonkoma-development/ (excerpt, July 2 2026). → §8 Ronkonkoma card.

### Local news / weather (hyperlocal substitute)
- Query: `August 2024 Suffolk County flash flood Stony Brook rainfall inches businesses basements` · Firecrawl search → https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20240823 (scrape, directQuote): record rainfall Aug 18–19 2024; "first-ever flash flood emergency for Suffolk County"; "1-in-1,000-year rain event for the impacted area"; Mill Pond Dam failed; Route 25A closed; "Over 2,000 residents and business owners experienced flood damage"; Stony Brook University cancelled move-in day; >70 structures major damage/destroyed. Stony Brook FD Facebook excerpt "almost 10 inches of rain between midnight and 6:00 a.m." (not used — Facebook). → §5 para 4, §5.5, §9 insurance Q, §10.5 flood H3, §13 Stony Brook card.
- Query: `Long Island lightning strike fried network equipment ethernet business Newsday OR Patch` · Firecrawl search → https://longisland.news12.com/2026/07/19/lightning-strike-in-woodmere-takes-out-power/3t8gdoyPmSdQBmspgI2TZf (excerpt: strike hit a power line on Rica Lane, Woodmere) → NOT used (power line, not data cabling). LI news on lightning-damaged network cabling: EMPTY.
- Newsday / Patch / TBR / News12 on Cat6 or network-cable faults specifically: EMPTY.

### Technical (LI-specific angle)
- Query: `TIA-568 insertion loss temperature derating 0.4% per degree C above 20C UTP cable length reduction attic` · Firecrawl search → https://www.flukenetworks.com/knowledge-base/dsx-cableanalyzer-series/temperature-impacts-your-insertion-loss-measurement-dsx (scrape, directQuote): "As temperature increases, you can expect the Insertion Loss of your link to increase too."; quoting ISO/IEC 11801:2011 Table 32: "H should be reduced by 0,2 % per ºC for screened cables; 0,4 % per ºC (20 ºC to 40 ºC) and 0,6 % per ºC (>40 ºC to 60 ºC) for unscreened cables." → §5 para 2, §5.5, §6 heat card, §9 March/July Q, §10.5 attic H3, decision table row 1.

### Prices used (only from live AESS Long Island pages)
- $195/hr, three-hour minimum ($585); additional time hourly — network-cable-repair-long-island.html, -nassau-county.html, -suffolk-county.html.
- Replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord) — network-cable-repair-long-island.html pricing table.
- Over-length re-route "Quoted per run"; plenum (CMP) "Add per drop"; evening/weekend "Premium applies" (occupied medical, retail, food-service) — same table.
- New-install comparison: Cat5e $254 / Cat6 $296 / Cat6A $424 per drop to 100 ft — cat6-installation-long-island.html.
- East End: "handled by planned windows rather than a surcharge" — network-cable-repair-suffolk-county.html changelog. → FAQ F1.
- FLAG for Anwar: (1) $175 replacement drop is published un-multiplied on LI pages (blueprint §9 would give Nassau 1.15× = $201, Suffolk 1.20× = $210); page follows the live LI pages. (2) cat6-installation-long-island's $296 Cat6 drop = 1.088× the NYC $272, which matches neither Nassau 1.15× ($313) nor Suffolk 1.20× ($326); quoted as published, labelled comparison only. (3) MANIFEST-187 already noted Cat6 per-drop pricing identical across pages — the LI installation page has since diverged from NYC.

### Keyword notes (five layers, LI geo)
- Service: Cat6 repair Long Island, Cat6 cable repair Nassau/Suffolk, Cat6 re-termination, Cat6 recertification, outdoor Cat6 repair, Cat6 reroute.
- Problem: Cat6 fails in heat / summer, attic Cat6 damage, over-length Cat6 run, storm-damaged Ethernet, lightning-damaged switch port, flood-damaged Cat6, corroded outdoor RJ45, chewed cable, landscaping-cut buried cable, PoE camera drops at night/far end.
- Technology: insertion loss, temperature derating, 90 m permanent link, primary protector (NEC 800.90), outdoor/direct-burial Cat6, CCA vs solid copper, PoE extender, fiber between buildings.
- Industry: flex/industrial buildings, office parks, strip retail/POS, mall tenants, medical/dental, marinas/waterfront, seasonal East End businesses, schools/libraries/houses of worship, HOAs/condos, homeowners.
- Geographic: Long Island, Nassau County, Suffolk County, Levittown, Hicksville, Massapequa, Bethpage, Hauppauge, Route 110 (Farmingdale, Melville, Huntington Station), Old Country Road, East Garden City/Uniondale, Hempstead, Ronkonkoma/MacArthur, Stony Brook, Upton, North Fork, South Fork, East End; town list in §13.

### Images (11) — permanent image rule; Drive folder empty (main run), CompanyCam not connected
Source photos chosen by perceptual match to avoid the 11 sources used by cat6-repair-nyc (NYC used NCR crushed, inspection, water-damaged, keystone-jack, network-closet, patch-panel, poe-camera, damaged-ethernet, network-cable-tracing, network-jack, network-cable-fault-detection).
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-long-island-rack-cable-tester-reading.webp (hero) | network-cable-repair/network-cable-repair-long-island.webp |
| cat6-repair-long-island-j-hook-ceiling-pathway.webp | cat6/cat6-installer-long-island-jhook-ceiling-pathway.webp |
| cat6-repair-long-island-ceiling-access-point-cable.webp | network-cable-repair/access-point-cable-repair-long-island.webp |
| cat6-repair-long-island-drywall-access-cut-at-jack.webp | cat6/cat6-retrofit-installation-bronx-drywall-cut-in.webp |
| cat6-repair-long-island-pos-counter-jack-no-link-test.webp | network-cable-repair/pos-network-cable-repair-long-island.webp |
| cat6-repair-long-island-printer-data-jack-patch-cord.webp | cat6/office-cat6-installation-long-island-printer-data-jack.webp |
| cat6-repair-long-island-fish-tape-conduit-repull.webp | cat6/cat6-wiring-bronx-fish-tape-conduit.webp |
| cat6-repair-long-island-switch-port-flashlight-check.webp | network-cable-repair/switch-port-troubleshooting-long-island.webp |
| cat6-repair-long-island-labelled-bundle-network-room.webp | cat6/cat6-patch-panel-installation-long-island-network-room.webp |
| cat6-repair-long-island-rj45-plug-recrimp.webp | network-cable-repair/rj45-connector-replacement-long-island.webp |
| cat6-repair-long-island-cubicle-keystone-punch-down.webp | cat6/cat6-keystone-termination-brooklyn-outlet.webp |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (5) and images/cat6/ (6) (no real cat6-repair photos yet)`.

## Question register — cat6-repair-long-island

§9 "Questions Answered" (H3):
1. Why would a Cat6 run in a Long Island attic pass certification in March and fail it in July? (Heat, length)
2. The tester says a warehouse run is 104 metres. What are the options short of moving the switch? (Heat, length)
3. Why do the links at the far end of a long Long Island office wing fail first? (Heat, length)
4. After a nor'easter there is water in the box where our Cat6 enters the detached garage. What needs fixing? (Storms/water)
5. Can you document flood-damaged Cat6 for an insurance claim after a storm like August 2024's? (Storms/water)
6. How does salt air near the South Shore and the harbours affect Cat6 terminations? (Storms/water)
7. Landscapers trenched for a sprinkler system and now the pool-house link is dead. Can a buried Cat6 run be repaired? (Storms/water)
8. Our ranch is on a slab with no basement. How is a failed Cat6 run reached for repair? (Building)
9. Can Cat6 that a previous owner stapled to the attic joists be saved? (Building)
10. A seasonal East End shop sat closed all winter. Why do some Cat6 links fail when it reopens? (Building)
11. Why do links between two buildings on a Long Island office or school campus keep failing? (Building)
12. A parking-lot camera at the end of a long run powers up but drops video. Is the run too long for PoE? (Devices)
13. Our dock scanners lose their connection only when the bay doors are open. Is that cabling? (Devices)

FAQ (§17, = FAQPage schema):
F1. Is there a travel charge to repair Cat6 on the North Fork or the South Fork?
F2. Can you test the Cat6 in a Long Island house before we close on it?
F3. Can you work in a Long Island school, library or house of worship during a summer or holiday break?
F4. Can a Cat6 repair at a medical or dental office in Nassau or Suffolk be done before patients arrive?
F5. Can you repair Cat6 inside a mall or shopping-centre tenant space on Long Island?
F6. We are having the attic re-insulated. Should the Cat6 up there be checked first?
F7. Can surge protection be added to an outdoor Cat6 run that has not failed yet?
F8. We are turning a Long Island garage into an office. Can the Cat6 already out there be reused?
F9. Can a homeowners' association or condo complex on Long Island book one visit for several units?
F10. Can you work with our remote IT provider during a Long Island repair visit?

Other "?" headings: "Cat6 Link Dead in Nassau or Suffolk This Morning?" (repair capture), "Cat6 Failing Somewhere Between the Queens Line and Montauk?" (closing).

Avoided: all 26 cat6-repair-nyc questions; network-cable-repair-long-island FAQ/headings (cost, speed, PoE reboot generic, dead jack, Cat5e upgrade, certified reports, warranty, who repairs, wide-floorplate fault location); cat6-installation-long-island FAQ (attic install, licensed contractor in Nassau/Suffolk, 90 m limit, CCA, plenum, 10G, evenings/weekends); cat6-repair-hudson-valley (same batch) storm-port, post-strike testing, cold-weather garage, buried-conduit ice, weekend-house remote diagnosis, retest after storm — two LI questions (lightning damage, nor'easter port/cable) were rewritten after reading the HV draft to avoid intent overlap. Licensing is answered in §8.5 body only (no question) because cat6-installation-long-island already asks it.

Masked paragraph similarity (difflib, geo-masked, p/li/td/h3/figcaption ≥8 words): vs cat6-repair-nyc mean 0.41, every block ≥0.65 is an excluded constant (freshness stamp, warranty sentence, licence/rating strip, NAP, form success line, price-table item names/figures); vs cat6-repair-hudson-valley mean 0.40, same constants only; vs network-cable-repair-long-island mean 0.37, blocks ≥0.65 are its pricing-table row descriptions quoted as the price source.


---
<!-- merged from batch build cat6-repair-hudson-valley, 2026-10-17 -->
## Hudson Valley hub — local research (2026-10-17 batch, cat6-repair-hudson-valley)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources (Fluke, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fixr) are reused from research/cat6-repair.md. Verified Hudson Valley sources reached earlier today by the fiber-optic-installation-hudson-valley run (research/fiber-optic-installation.md, HV section) are reused where noted "(fiber HV run)". Shell curl is blocked; Firecrawl search/scrape used for new sources.

**Page thesis (differs from NYC hub):** valley Cat6 fails from the outside in — storms/surges on runs that leave the building, freeze/thaw and wet conduit, heat in attics/high-bay roofs, rodents in outbuildings, long runs near the 100 m channel, and decades of re-tenanted office-park and campus plant; plus distance, so the repair is planned to finish in one trip. NYC hub thesis (riser/pre-war/managing-agent access) not reused.

### Reddit
- `site:reddit.com hudsonvalley ethernet OR "cat6" OR "network cable" house barn` · Firecrawl search · no r/hudsonvalley thread on cabling (only a cabin-delivery thread https://www.reddit.com/r/hudsonvalley/comments/17pbo08/ — irrelevant). r/hudsonvalley: EMPTY. Topical r/Homebuilding excerpt (house/garage/barn Cat6) — background only, not quoted.
- `mice rodents chewing ethernet cable barn garage outbuilding damage network` · Firecrawl search · https://www.reddit.com/r/homelab/comments/fpejmn/rats_have_chewed_through_my_cat6_in_new_house/ excerpt ("Its normal for rats to chew on pipes and wires. PVC will hardly slow them down") — background for §9 rodent Q and FAQ barn answers; not quoted on page.
- Reused (fiber HV run): r/HomeNetworking barn threads — background only.

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
§10.5 Reality Check states on-page that AI Overview could not be viewed; claims are attributed to forums/how-to/cost guides:
- MikroTik forum (fiber HV run) https://forum.mikrotik.com/t/is-fiber-always-the-better-choice-between-buildings/272583 — isolation "functional not safety", separate grounding electrodes, counter-view "myth" → §10.5 H3 1.
- Mike Holt forum (new, below) and TrueCable excerpt (new, below) → §10.5 H3 2.
- Fixr Jan 2025 (silo) → §10.5 H3 5, §14 national comparison.

### Local news / hyperlocal
- `lightning strike damaged network equipment business Hudson Valley news Daily Freeman OR lohud OR Times Herald-Record` · Firecrawl search · results: News12 HV "Possible lightning strike damages Monsey home" (https://hudsonvalley.news12.com/possible-lightning-strike-damages-monsey-home, excerpt only — not used, residential fire, no cabling); Times Union thunderstorm article (scraped below). Daily Freeman / Times Herald-Record / Poughkeepsie Journal: no relevant result — EMPTY.
- Scrape https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php (Lana Bellamy, June 27 2024): outages "affected a combined 60,000 Orange and Rockland and Central Hudson customers"; Central Hudson "more than 35,000 customers who reported outages in northeastern Orange, Dutchess and Ulster counties"; ~13,000 Orange, ~10,000 Dutchess; winds "about 60 mph". → §5.5 facts list (bullet 2); §9 power-restoration Q context.
- `Hurricane Ida 2021 flooding Mamaroneck Westchester businesses basements damage` · Firecrawl search → scrape https://abc7ny.com/post/flooding-brooklyn-nj-nyc-flooded/10994078/ (published 2021-09-02): Mamaroneck "some neighborhoods reporting as much as 14 feet of water"; three confirmed fatalities in Westchester (George Latimer); "many reported water filling their basements and rising to the first floor". → §5.5 facts (bullet 3); Six Counties (Westchester).
  - Town of Mamaroneck Sept 2021 e-newsletter (https://www.townofmamaroneckny.gov/CivicSend/ViewMessage/message/153573) — excerpt only, not used.
- `iPark 87 Kingston former IBM campus redevelopment tenants square feet` · Firecrawl search → scrape https://spectrumlocalnews.com/nys/hudson-valley/news/2026/02/27/ulster-county-moves-to-foreclose-on-2-ipark-87-west-parcels (Feb 27 2026): "long-vacant former IBM Kingston manufacturing facility situated on 200 acres with over 1 million square feet of buildings located along Enterprise Drive in Ulster"; county acquired through foreclosure in 2019; East Campus "hosts the new Ulster BOCES Career and Technical Center and Archtop Fiber"; foreclosure on two West Campus parcels. → §5.5 facts (bullet 5); §8 card "Enterprise Drive"; Six Counties (Ulster).
- `Westchester office park conversion I-287 corridor older office buildings vacancy 2025` · Firecrawl search → scrape https://howprop.com/big-changes-in-westchesters-office-market/ (Howard Properties, May 11 2026): 1.1M sq ft vacant former IBM facility removed from stats; 660,000 sq ft "700 series" of 1970s office buildings on Route 287, White Plains, bought for mixed-use; vacancy "now 19.9%, down from a recent peak of 27%"; "our newest office building today is 37 years old!". → §5.5 facts (bullet 4); §7 office-park card context. (Lincoln Property Q3 2025 PDF excerpt 26.2% vacancy — different methodology, not used.)
- `Newburgh East End Historic District number of buildings largest historic district New York` · Firecrawl search → scrape https://en.wikipedia.org/wiki/East_End_Historic_District_(Newburgh,_New_York): 445 acres, 2,217 buildings, incl. Washington's Headquarters SHS (NHL); city recognised 1973, NRHP 1985; mostly 2–3 storey Italianate brick townhouses. → §5.5 facts (bullet 6); §13 landmark card; §9 townhouse Q; Six Counties (Orange). (newburghny.org excerpt says "250 buildings within its 1,010 acres" for a sub-district — conflicting/unclear, not used.)

### Technical (outdoor / frost)
- `water in underground conduit freezes crushes ethernet cable outdoor run winter` · Firecrawl search →
  - scrape https://forums.mikeholt.com/threads/water-in-buried-conduit-question.101610/ : "The biggest danger to the condutors in water in conduits, around here, is when the water freezes and crushes the conductors. This often damages the insulation and or jacket and conductor failure will follow." → §9 buried-conduit Q (paraphrased, attributed to electricians on the forum); §10.5 H3 2.
  - https://www.truecable.com/blogs/cable-academy/into-the-great-outdoors-running-ethernet-cable-outside (excerpt): "Use direct burial grade Ethernet cable for underground conduit runs… Leave a few lazy 'S' shapes in the trench to allow for freeze/thaw" → §10.5 H3 2 ("cable makers' outdoor guidance").
- Reused (fiber HV run): EC&M Article 800 summary (800.90 primary protector, 800.93, 800.100) → §8.5 callout 1; Earth Networks 2020 NY lightning report (Orange 275,059 pulses #1; Ulster 182,760; Westchester 168,634; Dutchess 166,641) → §5.5 bullet 1, §10.5 H3 1, Six Counties (Orange).

### Landmarks / corridors / building stock (reused, fiber HV run — all verified there)
- Westfair: 1111 & 1129 Westchester Ave ~335,000 sq ft, Platinum Mile, Onyx Equities → §8 card 1.
- REBusiness: Westchester Medical Center Critical Care Tower $220M, groundbreaking July 2024; Regeneron Tarrytown ~900,000 sq ft → §8 card 2.
- HGAR May 15 2020: Amazon 1,015,740 sq ft at Route 17K/747 and Medline 1.2M sq ft, Town of Montgomery → §8 card 3; §5 para 4 ("construction starting in 2020").
- Hoodline Feb 14 2026: Palisades Center ~2,359,541 sq ft, Feb 2026 foreclosure auction → §8 card 4; §13 card 6; Six Counties (Rockland).
- Dutchess IDA IBM Quantum summary: 2455 South Road, ~300,000 sq ft + Building 416 renovation → §8 card 5.
- Wikipedia: Kingston Stockade (NRHP 1975, 8 blocks, 32 acres, stone houses at Crown & John, Senate House 1676) → §13 card 1; Stewart International Airport (1,552 acres, runways 11,817/6,004 ft, 105th Airlift Wing) → §13 card 3; Vassar (≈1,000 acres, 100+ buildings, 1861, Main Building 1865 Renwick) → §13 card 4; Vanderbilt Mansion NHS (211 of ~600 acres, 1896–1899, carriage house, hydro plant) → §13 card 5.
- USDA 2022 Census county profiles: Dutchess 620 farms avg 161 acres; Ulster 486 farms avg 150 acres → §5.5 bullet 7; Six Counties (Dutchess).
- Ulster County Sept 25 2025: $20.8M ConnectALL award, ~1,300 unserved locations, pending NTIA approval → Six Counties (Ulster).
- Town lists in §13 "we also repair" are place names only (consistent with MANIFEST-site-rebuild-187 HV list).

### Local licensing / permits (reused, fiber HV run)
- Westchester DCP: "Westchester law requires that home improvement contractors have a county license" → §8.5 callout 3; Six Counties (Westchester).
- Rockland Consumer Protection licences page (HIC, Master Electrician; Chapter 250) → §8.5 callout 3; Six Counties (Rockland).
- Central Hudson Dig Safely / 811: 2–10 working days' notice → §8.5 callout 4.
- NYC DEP watershed regulations (Dec 2019; Ulster, Orange, Putnam, Westchester) → §8.5 callout 5; Six Counties (Putnam).
- Orange/Putnam/Dutchess/Ulster county trade licensing: EMPTY (page makes no claim).

### Prices used (live AESS pages only; no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-hudson-valley.html pricing table (also Westchester, Rockland, Orange, Putnam pages).
- Replacement Cat6 drop from $175 — network-cable-repair-hudson-valley.html (and all six county pages).
- New-install comparison Cat5e $265 / Cat6 $309 / Cat6A $441 per drop to 100 ft — cat6-installation-hudson-valley.html.
- "Inter-building link correction — quoted per run"; "Closet audit — quoted by port count" — network-cable-repair-hudson-valley.html.
- "Lift hire where the site has none — at cost, quoted per day" — network-cable-repair-orange-county.html.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party.
- FLAGS for Anwar: (1) network-cable-repair-dutchess-county.html and -ulster-county.html publish a different model — "$250 service call + on-site diagnosis", termination $250–$425, panel port $250–$475, splice $350–$700, exterior entry seal/drip loop/bonding $400–$850, buried trace $650–$1,800, certification $45–$85/run — which conflicts with the $195/hr 3-hr minimum on the HV hub and the other four county pages. This page uses the hub figures and says the written quote confirms the county figure. (2) The $175 replacement drop and $195 rate carry no §9 multiplier on any live HV page; cat6-installation-hudson-valley $309 per Cat6 drop is 1.136× the NYC $272, not a §9 multiplier. (3) NYC hub's $185 exterior-entry figure (Bronx) was NOT used here because the Dutchess/Ulster pages show $400–$850 for the same scope.

### Keyword notes (five layers)
- Service: Cat6 repair Hudson Valley, Cat6 cable repair, outdoor Cat6 repair, Cat6 re-termination, Cat6 surge/storm damage repair, Cat6 certification after repair, building-to-building Cat6 repair, PoE camera cable repair.
- Problem: switch ports dead after thunderstorm, surge-weakened link, frozen/wet conduit, freeze–thaw fault, chewed/rodent-damaged Cat6, indoor cable used outdoors, corroded RJ45 at pole camera, expansion-joint failure, link down after power outage, high-bay damage.
- Technology: Cat6, Cat6A, TIA permanent link/channel, 100 m channel, fault location by distance, data-line surge protector, NEC Article 800 primary protection, CMR/CMP, outdoor/direct-burial cable, drip loop, media converter, PoE budget.
- Industry: office parks, corporate/manufacturing campuses, distribution warehouses, schools/libraries/municipal, medical suites, retail centres/farm stores, farms/estates, second homes.
- Geographic: Hudson Valley; Westchester, Rockland, Orange, Putnam, Dutchess, Ulster; Platinum Mile/I-287, Valhalla, Tarrytown, Route 17K/Montgomery/Stewart, Route 59/West Nyack, South Road Poughkeepsie, Enterprise Drive/iPark 87, Kingston Stockade, Newburgh East End.

### Question register — cat6-repair-hudson-valley
§9 "Questions Answered" (H3):
1. Why did a storm kill the switch ports for the barn and the yard cameras but leave the office desk ports working?
2. Which Cat6 runs should be tested after a strike near the property, even if they still seem to work?
3. The power came back after an outage, but some Cat6 links never did — what failed?
4. Why does a Cat6 link to an unheated garage or barn only fail in the coldest weeks of winter?
5. Our outdoor Cat6 runs through buried conduit — can ice in the pipe damage it?
6. A Cat6 run crosses from the original school building into its addition and keeps failing at the joint — why there?
7. Mice got into the barn ceiling — how much of the chewed Cat6 has to be replaced?
8. Someone ran indoor Cat6 along the outside of the house to the shed — it still works, so does it need replacing?
9. Water got into the plug at a pole-mounted camera — can the run be saved, or does it have to come back to the building?
10. Our Cat6 to cameras and access points in a high-bay warehouse keeps getting damaged — what is hitting it?
11. Our office-park suite shares a telecom room with the tenant next door — can a Cat6 repair be done without touching their equipment?
12. The failed Cat6 in our brick townhouse office runs along the baseboards and door casings — what is the least visible way to replace it?
13. How is a Cat6 run repaired where it passes through a thick stone wall and the old sleeve is packed full?
14. We are an hour from most contractors — what can we send so the first Cat6 repair visit finishes the job?
15. Can a Cat6 fault at a weekend house be narrowed down before anyone is there?

FAQ (§17, = FAQPage schema):
F1. Can you repair Cat6 in an older house that still has knob-and-tube or other old electrical wiring?
F2. Can you repair the Cat6 between a Starlink dish or rural internet antenna and the router?
F3. Do you repair Cat6 that feeds a driveway gate, keypad or intercom post?
F4. Can you repair a Cat6 run that feeds a well house or pump house?
F5. Will you match the existing jacks and plates in a finished house or office?
F6. Can you repair Cat6 in the crawlspace under an older house?
F7. Can you repair Cat6 in a converted barn or carriage house now used as an office or studio?
F8. Can you work in a barn with horses or livestock in it?
F9. Can you come back and retest a repaired link after the next big storm?
F10. What should we have ready for a technician arriving at a remote site?

Other "?" headings: "A Hudson Valley Cat6 Link Down Since the Storm?" (repair capture), "Outbuilding or Yard Camera Offline This Week?" (closing).

De-dup notes: compared by meaning against the NYC register (research/cat6-repair.md) and the parallel cat6-repair-long-island page as built at 05:11. Removed/rewritten from first draft because LI covered the same intent: hot-attic pass-in-spring/fail-in-summer (→ expansion-joint Q), surge protector on outdoor run (→ well-house FAQ), stapled cable salvage (→ least-visible replacement route in masonry), seasonal building reopening (→ converted barn FAQ), travel/area charge (→ knob-and-tube FAQ). Storm Qs reworded to pattern (outdoor vs desk ports) and hidden-damage triage, distinct from LI's single-camera cable-or-port and "what gets damaged" questions. NYC F10 (run between two buildings) intent avoided: outdoor runs are handled as weather/plug/cable-rating questions, not "can you repair between buildings".
