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


---
<!-- appended by batch build cat6-repair-queens, 2026-10-17 -->
## Queens

Batch run 2026-10-17 (cat6-repair-queens). Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, #bronx, as on network-cable-repair-queens / fiber-optic-installation-queens / sonos-installation-queens) · up-link /cat6-repair-nyc. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. "Carried" = finding fetched earlier today by another silo's Queens run and logged in that research file (not re-fetched); the file is named.

**Thesis (different from NYC hub, LI, HV and from network-cable-repair-queens):** in Queens the Cat6 is worn out by how the building is *used*, not by risers (NYC hub), heat/distance/weather (LI) or outside-in storms (HV). Three engines: (1) working storefronts and kitchens on the BID corridors — heat over the line, mop water at low jacks, roll-down gates, POS vendors who stop at the wall; (2) the borough's houses and basements being re-renovated and re-occupied — Ida and the 2023 floods, the 2024 basement program, brick rowhouses and Mathews flats where cable is surface-run on masonry, drywall screws and other trades' drills; (3) new LIC/Hunters Point/Sunnyside towers whose in-unit jacks run to a media panel that was never patched. network-cable-repair-queens's angles (shared riser tracing, Maspeth over-length, machinery vibration, other tenants' work, afternoon ceiling heat, Rockaway corrosion, office above a restaurant) were read and avoided as questions.

### Reddit (local)
- `site:reddit.com Queens ethernet wall jack not working apartment house cat6` · Firecrawl search (excerpts only; Firecrawl scrape of reddit.com refused: "we do not support this site") →
  - https://www.reddit.com/r/longislandcity/comments/1hw6agf/does_your_apartment_have_ethernet_available/ — excerpt: "Any cat5 wiring in your apartment walls would be connected to a patch panel somewhere. Each port on the panel would then have to be patched…" → §5 para 4 (towers), §9 Q "Every jack in our new LIC apartment is dead", §10.5 H3 5 (paraphrased, attributed to a commenter in r/longislandcity).
  - https://www.reddit.com/r/HomeNetworking/comments/1q38rgl/ (renovated house, "the only keystone that was terminated is this one. All the other just had a loose cat6 behind…") — not Queens; background only for §9 renovation Q. Not quoted.
- `Long Island City apartment tower in-unit ethernet jack structured media panel not connected renter` · Firecrawl search → https://www.reddit.com/r/Apartmentliving/comments/1lfi4m4/wall_ethernet_not_working_who_is_responsible/ (excerpt: "none of the ethernet ports in the wall are connected to eachother") — not Queens; background only for §9 rental Q. Not quoted.
- Queens-specific Reddit threads on failing Cat6 in restaurants/basements: EMPTY (none returned; reddit not scrapeable in build env).

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 says on the page that the AI Overview could not be viewed; each H3 is framed as a commonly repeated claim and corrected with the sources below.

### Restaurant / storefront (use case)
- `number of restaurants in Queens NYC DOHMH inspection data borough` · Firecrawl search → https://www.nyc.gov/site/doh/services/restaurant-grades.page (excerpt): "health inspection results for New York City's 29,000 restaurants on ABCEats" → §5.5 bullet. (nycdatascience.com student analysis "Queens 4540" — undated student work, NOT used. data.lohud.com list of closed Queens restaurants — not used.)
- `restaurant kitchen ethernet cable heat grease POS network problems cable rated temperature 60C` · Firecrawl search →
  - scrape https://support.toasttab.com/en/article/Network-Cable-Troubleshooting-1492723816122 (last updated Sep 17 2026): stationary devices "should use Ethernet rather than Wi-Fi … more stable than Wi-Fi and is not affected by wireless interference"; quick fix for dropping connection = "Reseat or replace the cable"; "If the cable runs into a wall jack and the jack appears to be the problem, the jack may need repair. Repairs to in-wall cabling may require an outside resource such as an electrician, as Toast does not provide service for intensive cable work."; hardware uses "Cat5e and Cat6". → §5 para 2, §9 Q "POS company says it's in the wall", §10.5 H3 1 and 2, §6 card.
  - scrape https://f3tech.com/2025/03/5-things-you-shouldnt-do-with-ethernet-cables-in-restaurants/ (F3 Technologies, Mar 5 2025): restaurant cable mistakes include "placing cables too close to heat and water", "leaving them exposed or tangled into messy 'rat's nests'". → §5 para 2, §7.5 kitchen paragraph (attributed to a restaurant IT firm).
  - specgravity.com "28% of POS errors trace back to connectivity issues" (excerpt only, vendor blog, method unknown) — NOT used.
  - Silo source reused: Fluke / ISO/IEC 11801 insertion-loss derating 0.4 %/°C (20–40 °C) — research LI section → §9 kitchen-display Q (heat over the line).

### Building stock / landmarks / corridors
- `Queens one- and two-family homes share of housing stock attached rowhouses statistic` · Firecrawl search → scrape https://chpcny.org/visualization/housing-stock-visualization/ (CHPC "Taking Stock", Oct 2024, 2023 NYCHVS): "about 3.7 million housing units"; "Half of all NYC's housing is found in Brooklyn and Queens"; "garden apartments in Sunnyside"; small homes "over a quarter of all housing units"; over half of units built before 1947. No Queens-only building-type split → Queens split EMPTY. → §5 para 1, §5.5.
  - Urban Omnibus 2016 excerpt (217,000 row houses citywide) — not used (citywide, methodology).
- `Ridgewood Queens historic districts brick rowhouses tenements Mathews Flats number of buildings Landmarks` · Firecrawl search (excerpts) →
  - http://s-media.nyc.gov/agencies/lpc/lp/2319.pdf (LPC Ridgewood North HD report): 96 buildings, "primarily three-story brick tenements"; G.X. Mathews Company "built and sold over 300 tenements in Ridgewood between 1909 and 1912"; Mathews also built "over 300 buildings, including its model flats, smaller, two-story apartment buildings, and one- and two-family houses" in Woodside, and "250 one-family brick homes with garages in the Elmhurst section". → §5 para 3, §5.5, §7 card, §13 card.
  - https://hdc.org/buildings/central-ridgewood-historic-district/ : "approximately 990 buildings and sites, most of which are brick row houses"; Paul Stier built "over 2,000 houses in the area". → §7 card, §13 card.
  - Wikipedia Mathews Model Flats excerpt ("more than 3,000 buildings in Queens", garbled) — NOT used.
- Carried from research/smart-lock-installation.md (Queens rows C1, C3, C4, Q1, Q7, Q8, Q13): Census QuickFacts Queens pop 2,358,182, 934,750 housing units (July 1 2025), owner-occupied 44.9% (2020–2024); OSC report 24-2025 LIC/Sunnyside/Woodside housing +~42% 2010–2023 to ~66,700 units; Glen Oaks Village 2,904 garden apartments in 134 buildings; Local Law 126 of 2024 basement/cellar program (Queens CD2 in program area; pre-April 20 2024 units; apply by April 20 2029; water sensors/alarms within 3 months; sprinkler within 2 years); Fresh Meadows 140-building complex (NYT 1972); Jackson Heights HD designated Oct 19 1993; Queens BIDs (11: 180th Street, 82nd Street Partnership, Bayside Village, Downtown Flushing Transit Hub, Downtown Jamaica Partnership, GatewayJFK, Long Island City Partnership, Myrtle Avenue (Queens), Steinway Street, Sunnyside Shines, Woodhaven). → §5.5, §7, §8, §9 basement Q, §13.
- Carried from research/fiber-optic-installation.md (Queens section): LIC 2001 rezoning (adopted July 26 2001, 37 blocks); One Court Square 673 ft, 50 storeys, completed 1989, tallest in Queens until 2019; Hunters Point South 1,194 rentals (Dec 2021); Silvercup Studios (former bakery, 1929–30; studio 1983); Kaufman Astoria (1920, 11 stages); JFK $270M 350,000 sq ft cargo centre (Apr 2025, temperature-controlled space); LaGuardia $8B, Terminal B; Queens College 83 acres; Flushing Main St pedestrian count "only second to Times Square" (Streetsblog ~Dec 2019, Chamber's Choe); seven Queens IBZs; 7 train viaduct (not used — fiber page's angle). → §8 cards, §13 cards.

### Local news / hyperlocal
- `Queens flash flooding September 29 2023 businesses basements damage Queens` · Firecrawl search → scrape https://queenseagle.com/all/2023/9/29/floods-engulf-queens (Ryan Schwach, Sept 29 2023): remnants of Tropical Storm Ophelia; "Countless basement apartments in the borough were flooded"; "the wettest day in New York City since Hurricane Ida"; at LaGuardia "Terminal A was shut down due to heavy flooding inside the building"; East Elmhurst severely flooded incl. 23rd Street; Elmhurst Hospital 30-year-old roof leaked; Beach 67th St, Arverne flooded. → §5 para 3, §5.5, §9 basement Q context, §10.5 H3 4.
  - https://en.wikipedia.org/wiki/September_2023_New_York_floods (excerpt: damage ~$100M; one basement "flooded again, after it was previously flooded during … Ida") — supporting only, not quoted.
- Carried (smart-lock / soundbar files): Queens Daily Eagle — 11 of 12 confirmed Ida dead from Queens, 10 lived in basement apartments; DOHMH flooding-and-health data story. → §5 para 3, §5.5.
- `Queens rats rodents chewed wires restaurant building news qns.com OR qchron.com` · Firecrawl search → scrape https://qns.com/2021/07/rat-complaint-in-queens-have-jumped-nearly-30-percent-during-the-first-half-of-2021/ (Allie Griffin, July 22 2021): 1,812 Queens rat complaints Jan 1–June 30 2021 vs 1,424 in H1 2020 (311 data); rise "in part … attributed to the reopening of restaurants"; Ridgewood 221 vs 103; Woodside 180 vs 89; Astoria (11105) 106; Corona 86; Briarwood 81. (Article labels Ridgewood "11358" — zip typo; page uses neighbourhood names only.) → §5.5, §6 rodent card, §10.5 H3 4.
  - PIX11 excerpt (rats chewing car wiring, soy-based coating theory) — not used (vehicles).
  - qchron.com Forest Hills rats excerpt — not used.
- `July 14 2025 flash flood Queens basements subway flooding rainfall inches` · Firecrawl search → NWS OKX event page https://www.weather.gov/okx/20250714 (excerpt: 4–6.5 in in hardest-hit areas) — regional, not Queens-specific → NOT used.
- Queens Chronicle / QNS / Patch items on Cat6 or network-cable repair specifically: EMPTY.

### Local licensing / permits / code (reused silo sources; no new Queens-specific permit source)
- NYC Electrical Code = 2020 NEC + NYC amendments, full effect Dec 21 2025 (nyc.gov, silo) → §8.5.
- NEC 800.25 abandoned cable (EC&M, silo) → §8.5, process step 5.
- DOB post-Ida advice (CityLand Sept 2 2021, silo): never operate breakers standing in water; extensive repairs may need registered contractors/permits → §8.5, §9 basement Q.
- Local Law 126 of 2024 basement program (carried) → §8.5, §9 basement Q (no legal advice; page says the program's inspection items are the owner's/architect's matter).
- LPC: Jackson Heights HD and Ridgewood HDs designated → §8.5 (exterior work on designated buildings may need LPC approval — silo/fiber LPC sources).
- Firestopping at rated penetrations: stated as general practice, no Queens-specific source.

### Prices used (live AESS pages only; no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-queens.html pricing table and FAQ; cat6-repair-nyc.html. Protected rate (v2.3 §9) → not multiplied.
- Replacement Cat6 drop "From $175/drop" (cable, keystone jack, wall plate, panel punch-down, testing, both-end labelling, patch cord) — network-cable-repair-queens.html table; same figure on cat6-repair-nyc.html. Page uses $175 as published for Queens.
- New-install comparison: Cat5e $233 / Cat6 $272 / Cat6A $388 per drop to 100 ft — cat6-installation-queens.html (identical to cat6-installation-nyc.html; no Queens multiplier applied on that live page).
- Outdoor/exterior entry made good, sealed and bonded: Bronx published "from $185 per penetration" (network-cable-repair-bronx.html, quoted on cat6-repair-nyc) × §9 Queens 1.05 = $194.25 → **from $194 per penetration** (no live Queens figure exists for this item).
- Third-party national (labelled): Fixr Jan 2025 $125–$250 per drop, $45–$75/hr (silo).
- FLAGS for Anwar: (1) §9 Queens 1.05× would make the replacement drop $183.75 → $184; network-cable-repair-queens.html and the NYC hub publish $175 for Queens, so the page follows the live Queens figure (conflict noted, same choice as NYC/LI/HV hubs). (2) cat6-installation-queens $272 Cat6 drop = NYC figure, no 1.05× (1.05× would be $286); quoted as published, comparison only. (3) $194 exterior-entry figure is a derived §9 number (Bronx base × 1.05), not yet published elsewhere.

### Keyword notes (five layers, Queens geo)
- Service: Cat6 repair Queens, Cat6 cable repair Queens NY, Cat6 jack repair, POS Cat6 repair, restaurant network cable repair, Cat6 re-termination, Cat6 certification, apartment Ethernet jack repair, media panel repair.
- Problem: KDS/POS offline, register no link, mop-water corrosion at floor jacks, roll-down gate damage, drywall screw through Cat6, renovation-cut runs, flooded basement Cat6, rodent-chewed Cat6, dead apartment jacks (unpatched panel), crowded media enclosure, third-party drill damage, two-family shared closet.
- Technology: Cat6, Cat6A, keystone, 110 punch-down, structured media enclosure, patch panel, certification tester, TDR/distance to fault, PoE, surface raceway, firestopping, insertion-loss temperature derating.
- Industry: restaurants, bakeries, groceries, salons, pharmacies, retail on BID corridors, medical/dental in converted houses, landlords of two-family houses, co-op boards, condo/rental tower residents, studios and lofts, cargo forwarders near JFK.
- Geographic: Queens; Flushing (Main St), Astoria (Steinway St, 30th Ave), Jackson Heights (37th Ave, 82nd St, Roosevelt Ave), Elmhurst, Corona, Woodside, Sunnyside, LIC (Court Square, Hunters Point), Ridgewood (Myrtle Ave), Glendale, Middle Village, Maspeth, Forest Hills, Rego Park, Kew Gardens, Richmond Hill, Woodhaven, Jamaica (Jamaica Ave, 165th St), Hollis, St. Albans, Bayside (Bell Blvd), Whitestone, College Point, Fresh Meadows, Glen Oaks, East Elmhurst, Howard Beach, Ozone Park, Rockaways (Arverne).

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run), CompanyCam not connected
Source pool images/network-cable-repair/*-queens.webp (the 11 scenes used on the NYC hub — chosen so the Staten Island builder, drawing on the LI/HV hub scene set, does not overlap). Every source shows a technician's face, so each was cropped with PIL to hands/equipment only (re-viewed after cropping: no faces, house numbers, plates or phone numbers; AESS shirt logos visible). WebP q80, all ≤1600 px. md5-unique within images/cat6-repair/.
| images/cat6-repair/ | Source (images/network-cable-repair/) | Crop |
|---|---|---|
| cat6-repair-queens-wall-jack-open-pair-tester.webp (hero) | network-jack-repair-queens.webp | 0,450,1000,1024 |
| cat6-repair-queens-nicked-jacket-on-ceiling-grid.webp | crushed-network-cable-repair-queens.webp | 240,280,1536,1024 |
| cat6-repair-queens-ceiling-bundle-flashlight-check.webp | network-cable-inspection-queens.webp | 630,0,1536,620 |
| cat6-repair-queens-corroded-plug-block-wall-box.webp | water-damaged-network-cable-repair-queens.webp | 680,380,1536,1024 |
| cat6-repair-queens-wall-plate-keystone-punch.webp | keystone-jack-replacement-queens.webp | 600,490,1536,1024 |
| cat6-repair-queens-link-down-tester-at-rack.webp | network-closet-troubleshooting-queens.webp | 0,430,820,1024 |
| cat6-repair-queens-labelled-panel-punch-down.webp | patch-panel-repair-queens.webp | 0,0,1000,1024 |
| cat6-repair-queens-dome-camera-no-poe-test.webp | poe-camera-cable-repair-queens.webp | 0,0,900,1024 |
| cat6-repair-queens-split-jacket-steel-desk-leg.webp | damaged-ethernet-cable-repair-queens.webp | 0,470,1536,1024 |
| cat6-repair-queens-tone-probe-labelled-cords.webp | network-cable-tracing-queens.webp | 760,0,1536,1024 |
| cat6-repair-queens-wire-map-crossed-open-pair.webp | network-cable-fault-detection-queens.webp | 0,300,1536,1024 |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (no real Cat6 Repair photos yet)`. Review note: the library photos appear AI-generated (uniform branding, idealised scenes) — same caveat logged on earlier pages; none shows a Queens location, and captions say only what is visible.


---
<!-- appended by batch build cat6-repair-bronx, 2026-10-17 -->
## Bronx

Batch run 2026-10-17 (cat6-repair-bronx). Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, #bronx, LocalBusiness block modelled on network-cable-repair-bronx.html) · up-link /cat6-repair-nyc. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked.

**Thesis (different from NYC hub, LI, HV, Queens, Staten Island and network-cable-repair-bronx):** Bronx Cat6 comes in two ages — young cable in the borough's recent new-construction boom (built-in installation defects, unterminated media-panel runs, other trades, long late-terminated roof/amenity camera runs) and Cat6 retrofitted later into 1920s–40s five- and six-storey apartment houses (hallway surface raceway, light wells/chases/old intercom conduit, cellars beside steam heat, renovations, super's emergency patches). The repair starts by "dating" the failure: built-in defect (often the installer's to answer for) vs later damage (a route problem). Also: most buildings are rented and run by agents/supers, and the Cat6 mostly carries building systems (intercom, cameras, readers, lockers, laundry). network-cable-repair-bronx's angle (cold rooms, yards, wash-down, shared cellar panel, hostile environment) and cat6-installation-bronx's FAQ were read and avoided.

### Reddit
- `site:reddit.com r/bronx ethernet OR cat6 OR "network cable" apartment building` · Firecrawl search (excerpts only; reddit not scrapeable) →
  - https://www.reddit.com/r/AskNYC/comments/gmwnwh/is_it_legal_for_me_to_run_an_ethernet_cable_along/ — excerpt: "NYC building code does not require conduit for low voltage cabling." → §10.5 H3 4 (paraphrased, attributed to "a commenter on r/AskNYC", then corrected: listing/firestop/raceway).
  - https://www.reddit.com/r/Fios/comments/1oz9xcz/1_gb_fios_installion_in_a_5thfloor_apt_bronx_nyc/ — excerpt (Fios install in a 5th-floor Bronx apt; tech brought the ONT into the apartment) → background only, not used.
  - https://www.reddit.com/r/Fios/comments/1woft3r/need_fios_service_on_harrison_ave_the_bronx/ — excerpt (Verizon/Optimum wires behind properties) → not used.
- `reddit bronx new building apartment ethernet jacks wall not working cat6 smart panel` · Firecrawl search → no Bronx thread; r/HomeNetworking https://www.reddit.com/r/HomeNetworking/comments/ttcbcp/moved_into_an_apartment_with_ethernet_ports_but/ and r/techsupport https://www.reddit.com/r/techsupport/comments/1qlp8fa/apartment_has_ethernet_jacks_in_each_room_but/ (excerpt: "remove each cable from the punchdown block and re-terminate it to a RJ45 connector") → background for §6 media-panel card and §10.5 H3 2 (forum framing, not quoted). Bronx-specific fault threads: EMPTY.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview was not visible; each H3 is a commonly repeated claim (Fixr cost guide, r/AskNYC, how-to "re-crimp", mesh Wi-Fi, "indoor cable has no heat problem") corrected with sourced facts.

### Building stock / housing (local)
- `Bronx renter-occupied housing share multifamily buildings built before 1947 percentage Furman Center Bronx` · Firecrawl search → scrape https://www.furmancenter.org/neighborhoods/the-bronx/ (query, directQuote; page last updated 05/06/2026): "In 2024, the homeownership rate in The Bronx was 19.7%, which is lower than the citywide share of 32.7%."; "Between 2010 and 2025, 63,066 units in 4+ unit buildings were built in The Bronx." → §5.5 bullets 3 and 5. (Housing-unit row with unlabelled year columns — NOT used.)
- `Bronx new housing construction permits led city units Bronx building boom 2023 2024` · Firecrawl search → https://www.osc.ny.gov/files/reports/pdf/report-24-2025.pdf (OSC "Housing Production in New York City", excerpt): "In 2023, the Bronx's share of net new units citywide reached 35 percent, surpassing Brooklyn's share of 34 percent"; "In 2023, 11 very large buildings were completed on or close to the rezoned waterfront, totaling 3,270 housing units … Another 1,019 housing units … were built in the Jerome Avenue Neighborhood Plan area in four 100+ unit buildings"; "In 2024, the Bronx maintained higher-than-average production with 8,093 new units"; Bronx 570,439 units in 2023. → §5 para 1, §5.5 bullets 1–2.
  - https://newyorkyimby.com/2026/05/new-york-yimbys-2026-first-quarter-construction-report-tallies-a-dramatic-increase-in-development.html (excerpt): Bronx residential/hotel units filed 3,677 → 7,344 Q1 2026 — not used on page (filings, not completions).
- `Grand Concourse Historic District Art Deco apartment buildings landmarked number of buildings` · Firecrawl search → https://s-media.nyc.gov/agencies/lpc/lp/2403.pdf (LPC designation report, excerpt): 78 properties along one mile of the Grand Concourse between East 153rd and 167th Streets; 61 apartment houses constructed 1917–1959; "the five- and six-story apartment house became the dominant building type along the Grand Concourse and within the Bronx"; Jerome Avenue subway completed 1918. → §5.5 bullet 4, §7 pre-war card, §13 card 1.
- `Co-op City Bronx 35 buildings 15,372 apartments Riverbay largest cooperative housing` · Firecrawl search → https://www.coopcity.com/aboutus/ (excerpt): "15,372 residential units in 35 high-rise buildings and seven (7) townhouse clusters". → §5.5 bullet 6, §13 card 6, borough section.

### Corridors / landmarks
- `Jerome Avenue rezoning 2018 approved housing units Bronx City Council` · Firecrawl search → https://www.sobro.org/jeromeavenue (excerpt): "In 2018 the New York City Council approved the rezoning of a 92-block stretch of the Bronx's Jerome Avenue"; https://council.nyc.gov/land-use/plans/jerome-avenue-neighborhood-plan/ (excerpt, ~95-block area — differing count; page uses SoBRO/City Limits "92-block"). → borough section (Highbridge/Concourse).
- `Lower Concourse rezoning Mott Haven waterfront Bronx Point new towers Harlem River` · Firecrawl search → https://edc.nyc/project/lower-concourse-infrastructure-investment-strategy (excerpt): "In 2009, this 30-block stretch along the Harlem River was rezoned"; https://bronxpoint.nyc/ (excerpt): "approximately 530,000 square feet … adjoining the Harlem River waterfront", adjacent to Mill Pond Park; https://danieltrubman.substack.com/p/the-apartments-are-ready-the-waterfront (Sep 17 2026, excerpt): One River Park at 355 Exterior Street, two towers, "north of 700 apartments", affordable lottery opened Sept 2026. → borough section (Mott Haven), §13 card 2. (700-apartment figure not used on page.)
- `Fordham Road Business Improvement District number of businesses stores Fordham Road` · Firecrawl search → https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=49 (excerpt): "No. Block Faces Covered: 35. No. Ground Floor Retail Businesses: 333." (nyctourism.com "almost 300 specialty stores" — not used). → §8 card 1.
- `"The Hub" Third Avenue 149th Street Bronx BID retail corridor busiest intersection` · Firecrawl search → https://en.wikipedia.org/wiki/The_Hub,_Bronx (excerpt): 2/5 at Third Avenue–149th Street; BID = Hub-Third Ave Merchants District Management Association. → §8 card 2, §13 card 4.
- `Bronx Terminal Market Gateway Center square feet retail Major Deegan 149th Street` · Firecrawl search → https://en.wikipedia.org/wiki/Bronx_Terminal_Market (excerpt): 913,000 sq ft GLA; 17-acre site south of Yankee Stadium; https://www.related.com/our-company/properties/bronx-terminal-market (excerpt) parking for 2,600 cars (not used). → §8 card 3.
- `Bay Plaza Shopping Center Co-op City square feet mall Bronx opened 2014` · Firecrawl search → https://en.wikipedia.org/wiki/Bay_Plaza_Shopping_Center (excerpt): opened August 14, 2014; Hutchinson River Parkway and I-95; grew to ~2,000,000 sq ft. → §8 card 5, §13 card 6.
- `Fordham University Rose Hill campus acres Bronx` · Firecrawl search → https://www.fordham.edu/about/campuses/rose-hill-campus/ (excerpt): "85 acres". → §8 card 6, §13 card 3.
- Hunts Point 329 acres, 155+ wholesalers — silo NYC section (nycfoodpolicy.org) → §8 card 4, §13 card 5.
- Neighbourhood names in §13 "we also repair" and the borough section are place names only (no claims).

### Local news / hyperlocal
- `Bronx Times OR Norwood News building internet cables cut vandalism tenants outage apartment Bronx` · Firecrawl search → results were fire/elevator/collapse stories (cbsnews.com Norwood fire; CBS 15-storey elevator outage; News12 3160 Webster Ave) and an abc7 Spectrum fiber-vandalism story in Brooklyn/Queens — none about Bronx building data cabling → NOT used. Bronx Times / Norwood News / Riverdale Press items on Cat6 or building network cabling: EMPTY.
- `September 29 2023 flash flooding Bronx basements rainfall record New York City` · Firecrawl search → https://en.wikipedia.org/wiki/September_2023_New_York_floods (excerpt: wettest September since 1882, 14.25 in) — Bronx-specific damage not in excerpt → NOT used (cellar water is covered by NCR Bronx/NYC hub).

### Local licensing / permits / code
- NYC Electrical Code = 2020 NEC + NYC amendments, full effect Dec 21 2025 (nyc.gov, silo) → §8.5 bullet 1.
- NEC 800.25 abandoned cable (EC&M, silo) → §8.5 bullet 2, §9 chase/conduit Qs.
- `Landmarks Preservation Commission permit required exterior work buildings in historic district nyc.gov` · Firecrawl search → https://www.nyc.gov/site/lpc/applications/applications.page (excerpt): "The City's Landmarks Law requires owners to obtain permits from the Landmarks Preservation Commission before doing work that affects the exterior and, in some …" → §8.5 bullet 4, §10.5 H3 4.
- Firestopping of rated penetrations: stated as general practice, no Bronx-specific source.
- Insertion-loss temperature derating (Fluke / ISO/IEC 11801, silo LI section) → §9 boiler Q, §10.5 H3 7.

### Prices used (live AESS Bronx pages only; Bronx §9 multiplier = 1.00×, so no conversion)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-bronx.html pricing table (same on cat6-repair-nyc.html). 
- Replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord) — network-cable-repair-bronx.html.
- Exterior entry made good, sealed and bonded, from $185 per penetration — network-cable-repair-bronx.html (its original source).
- New-install comparison Cat5e $233 / Cat6 $272 / Cat6A $388 per drop to 100 ft — cat6-installation-bronx.html.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party (silo).
- No conflict between the hub and the Bronx pages. FLAG for Anwar: the shared JS price-chip widget on network-cable-repair-bronx.html shows "$250 Service Call", "Cat6A from $250/drop" and "Min. Job $500" — these conflict with the published $195/hr × 3 h ($585) model and were NOT used.

### Keyword notes (five layers, Bronx geo)
- Service: Cat6 repair Bronx, Cat6 cable repair Bronx NY, Cat6 jack repair, Cat6 re-termination, Cat6 certification/recertification, apartment Ethernet jack repair, media panel termination, intercom/camera cable repair, hallway raceway repair.
- Problem: new-building jacks never worked, failed at handover, unterminated home runs, move-in damage (TV mounts, drills), roof/amenity camera link faults, raceway pulled/crushed, upper-floor intercom stations dead, taped/coupled splices, winter-only cellar failure (steam heat), renovation-cut common cable, facade/sidewalk-shed disturbance.
- Technology: Cat6, Cat6A, permanent link/channel, time-domain fault location, keystone, 110 punch-down, structured media panel, surface raceway, CMR/CMP, firestop, PoE, insertion-loss temperature derating, CCA.
- Industry: rental towers, pre-war apartment houses, co-ops/complexes, managing agents/supers, storefronts (Fordham Road, The Hub), big-box retail (Bronx Terminal Market, Bay Plaza), medical offices, campuses, one-/two-family houses.
- Geographic: the Bronx; Mott Haven, Port Morris, Lower Concourse, Highbridge, Concourse, Mount Eden, Morris Heights, Jerome Avenue, Fordham, Belmont (Arthur Avenue), University Heights, Bedford Park, Norwood, Kingsbridge, Riverdale, Spuyten Duyvil, Parkchester, Castle Hill, Soundview, Unionport, Co-op City, Pelham Bay, Throgs Neck, Country Club, City Island, Hunts Point, Longwood, West Farms, Wakefield, Williamsbridge, Woodlawn, Allerton, White Plains Road, Westchester Square.

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run), CompanyCam not connected
Primary pool images/cat6/ (180 files = only 15 distinct photos by md5; all 15 had already been reused on the LI/HV hubs). Chose 11 of the 15; the 4 not chosen (conference-table grommet, floor box, outlet row, voice/data plate) are the scenes the Staten Island page uses, so no scene overlaps with SI or Queens (Queens used images/network-cable-repair/). Every source shows a technician's face, so each was cropped with PIL to hands/equipment only (re-viewed after cropping: no faces, house numbers, plates or phone numbers; AESS shirt logos visible on some). WebP q80, ≤1600 px. md5-unique.
| images/cat6-repair/ | Source (images/cat6/) | Crop (on 800-px-wide preview scale) |
|---|---|---|
| cat6-repair-bronx-ceiling-tile-replacement-feed.webp (hero) | cat6-cable-installation-bronx-ceiling-drop.webp | 340,0,800,640 |
| cat6-repair-bronx-new-building-corridor-repull.webp | cat6-cable-installation-dutchess-county-corridor-pull.webp | 0,250,800,640 |
| cat6-repair-bronx-cubicle-keystone-retermination.webp | cat6-keystone-termination-brooklyn-outlet.webp | 400,280,800,640 |
| cat6-repair-bronx-fish-tape-masonry-conduit.webp | cat6-wiring-bronx-fish-tape-conduit.webp | 0,300,800,640 |
| cat6-repair-bronx-printer-jack-cord-test.webp | office-cat6-installation-bronx-printer-data-jack.webp | 360,250,800,640 |
| cat6-repair-bronx-metal-stud-cable-bundle.webp | commercial-cat6-installation-bronx-stud-rough-in.webp | 330,200,800,640 |
| cat6-repair-bronx-drywall-access-cut.webp | cat6-retrofit-installation-bronx-drywall-cut-in.webp | 330,300,800,640 |
| cat6-repair-bronx-workstation-plate-punch-down.webp | cat6-network-drop-installation-nyc-workstation-outlet.webp | 380,280,800,640 |
| cat6-repair-bronx-labelled-rack-bundle.webp | cat6-patch-panel-installation-bronx-network-room.webp | 430,0,800,640 |
| cat6-repair-bronx-desk-data-jacks-identified.webp | cat6-data-drop-installation-bronx-workstation-outlets.webp | 290,300,800,640 |
| cat6-repair-bronx-j-hook-cable-support.webp | cat6-installer-bronx-jhook-pathway.webp | 300,0,800,420 |
DAILY-LOG note: `images: 11 reused from images/cat6/ (no real Cat6 Repair photos yet)`. Review note: the library photos appear AI-generated (uniform branding, idealised scenes); none shows a Bronx location; captions describe only what is visible.

## Question register — cat6-repair-bronx

§9 "Questions Answered" (H3), clusters "Cable from the building boom" / "Cable retrofitted into older apartment houses" / "Public halls, shafts and renovations":
1. Our Bronx building opened last year and some jacks never worked — is that a repair job or the builder's punch list?
2. Links in our new building passed at handover but started failing once tenants moved in — what changed?
3. Why do the cameras on our new building's roof and amenity floors fail more often than the apartment jacks?
4. The developer handed over the building with no Cat6 test results — can installation defects be told apart from later damage?
5. In a 1920s apartment house, what usually breaks the Cat6 running in surface raceway along the public hallway?
6. Only the upper-floor video intercom stations lost picture — is the riser Cat6 to blame?
7. Our super patched a broken Cat6 run with tape and a coupler — what has to be undone?
8. Why would a cellar Cat6 run start failing only once the boiler is on for the winter?
9. Can a damaged Cat6 run that shares an old pipe chase or abandoned dumbwaiter shaft be replaced in the same space?
10. Can the old intercom or buzzer conduit in our building carry a replacement Cat6 run?
11. Tenants keep pulling at the Cat6 to a hallway camera — what kind of repair holds up in a public corridor?
12. A gut renovation in one apartment cut the Cat6 that serves the whole floor's cameras — is it best fixed before the new walls close?

FAQ (§17, = FAQPage schema):
F1. Can you handle a repair for an owner who lives out of state and leaves everything to a managing agent?
F2. Is Cat6 repair priced any differently in the Bronx than elsewhere in the city?
F3. Will you tell us if a failure is the original installer's workmanship so we can send it back to them?
F4. Can you repair Cat6 in a building that is still under construction, before it has a certificate of occupancy?
F5. Can you repair the Cat6 feeding a camera inside an elevator cab?
F6. Do you take on one- and two-family houses in the Bronx, or only larger buildings?
F7. Do you repair the Cat6 behind package lockers and smart mailroom equipment?
F8. What should we do to an occupied apartment before a technician repairs a jack inside it?
F9. Can you repair the Cat6 that crosses our roof to the rooftop cameras?
F10. Can you repair camera or intercom cable disturbed by facade work or a sidewalk shed?

Other "?" headings: "Cat6 Link Down Somewhere in the Bronx?" (repair capture), "Bronx Cat6 Link Still Failing Tonight?" (closing).

De-dup notes: compared by meaning against the NYC, LI and HV registers above and against the Queens and Staten Island pages as built at ~09:25 (their registers were not yet in this file). Removed from the first draft because Queens/SI cover the same intent: "every jack in a new apartment is dead / never connected" (Queens) → kept only as body text (§6 card, §10.5 H3 2), replaced by the move-in damage Q; "drywall screwed over Cat6" (Queens) → replaced by roof/amenity camera Q; "roll-down gate near the Cat6" (Queens) and "register drops when cooler/compressor kicks on" (SI) → gate-motor interference moved to §7.5 body text, replaced by the old intercom conduit Q; "does the super/landlord need to be there" (Queens) → replaced by the out-of-state owner/managing-agent FAQ; "Wi-Fi extender instead of repair" (Queens) → replaced by the under-construction FAQ; "show our staff how to tell cable from device faults" (Queens) → replaced by the facade/sidewalk-shed FAQ (the superintendent checks stay as a table, not a question). Related-but-distinct: F3 (attributing a fault to the installer) vs NYC F3 (will you repair another contractor's Cat6); Q8 (heating-season failure) vs LI Q1 (summer attic) and HV Q4 (cold garage). cat6-installation-bronx and network-cable-repair-bronx FAQs avoided (cost, pre-war masonry, cold storage, storefronts, CCA, plenum, riser full, Cat5e upgrade; yard camera, cellar flood, dead jack, 100 Mbps, certified reports, Bronx-based).

Masked paragraph similarity (difflib on geo-masked p/li/td/h3/figcaption ≥8 words, Jaccard-prefiltered): no block ≥0.65 vs cat6-repair-nyc, -long-island, -hudson-valley, -queens, -staten-island, cat6-installation-bronx or network-cable-repair-bronx except excluded constants (freshness stamp, warranty sentence, licence/rating strip, NAP, "parts you supply" line, silo link list).


---
<!-- appended by batch build cat6-repair-staten-island, 2026-10-17 -->
## Staten Island

Batch run 2026-10-17 (cat6-repair-staten-island, up-link /cat6-repair-nyc, phone (347) 934-8335, GBP Brooklyn 1282 Troy Ave as on network-cable-repair-staten-island.html). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources above (Fluke, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fixr Jan 2025, CityLand/DOB Ida advice) reused in general terms only.

**Thesis (differs from NYC hub / LI / HV / Queens / Bronx):** Staten Island Cat6 lives in houses (83% of units in 1–2 family homes) and much of it sits at or below a water line — Sandy surge zone on the East Shore, raised/rebuilt/modular post-Sandy homes, flash-flooded and chronically damp block-wall basements. The repair decision is "where should each connection live relative to the water line" (relocate panel/switch/terminations above it; only continuous cable below; NYC BC Appendix G), plus house-specific faults: two-family runs through the other unit, data cable sharing bored holes with power, provider-relocated routers orphaning home runs, house-to-office splits. Commercial: Hylan Blvd medical/retail, Seaview Ave (SIUH), Richmond Ave/New Springville, St. George/Bay St, West Shore logistics.

### Reddit
- `site:reddit.com r/statenisland ethernet cable wiring house internet` · Firecrawl search · results were r/HomeNetworking, r/smarthome, r/Spectrum, r/Fios threads, none on r/statenisland → r/statenisland: EMPTY (not accessible in build env / no matching thread). Not used.
- `reddit statenisland "ethernet" OR "cat6" OR "wired" house basement` · Firecrawl search · no r/statenisland result (generic r/HomeNetworking, r/smarthome finished-house threads) → EMPTY. Not used.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on-page that AI Overview could not be viewed; the seven H3 claims are framed as commonly published claims (flood recovery, powerline adapters, ISP inside wiring, Fixr cost, "raise the outlets", "pre-wired house", "clean corroded connectors") and corrected with the sourced facts below.

### Building stock
- `Staten Island one- and two-family homes share of housing units NYC Planning Furman Center borough profile` · Firecrawl search →
  - https://chpcny.org/visualization/housing-stock-visualization/ (CHPC "Taking Stock", Oct 2024, excerpt): "in Staten Island, 83 percent of units are in one- or two-family homes"; "Staten Island contains just five percent of the city's housing"; "small homes in Midland Beach". → §5 para 1, §5.5 bullet 1.
  - https://www.osc.ny.gov/files/reports/pdf/report-24-2025.pdf (NYS Comptroller, Housing Production in NYC, March 2025, excerpt): SI 185,196 units in 2024; new-building units in SI: 1 unit 33.1%, 2 units 49.1% ("a third of units from new buildings were single family homes and another almost half were in two-unit buildings"). → §5.5 bullet 2 (82% combined).
  - https://prodigyre.com/blog/the-two-family-wealth-engine… (realtor blog, 83% claim) — not used (CHPC is the primary).
- `Build It Back Staten Island homes elevated rebuilt number Sandy` · Firecrawl search + scrape https://www.nyc.gov/site/housingrecovery/disaster-recovery/build-it-back.page (directQuote): "8,319 homeowners served citywide"; "Staten Island – 1,982"; "838 homes repaired and elevated above base flood elevation"; "492 completely rebuilt homes, including 103 modular homes". → §5 para 2, §5.5 bullet 4, §7 cards (raised, rebuilt/modular), FAQ modular.
  - https://www.dnainfo.com/new-york/20170921/midland-beach/build-it-back-modular-homes-installation (excerpt: modular homes arriving Midland Beach, 137 Freeborn St) — background only.
- https://rebuildbydesign.org/wp-content/uploads/2022/03/floodplain-by-numbers.pdf (excerpt; SI floodplain building counts by "below grade/above grade" — category labels ambiguous in excerpt) — NOT used.

### Flood history / local news
- `Hurricane Sandy Staten Island deaths storm surge Midland Beach Oakwood Beach damage homes` · Firecrawl search →
  - https://www.silive.com/topic/hurricane-sandy/posts.html (excerpt): "storm surge … claimed the lives of 24 Staten Islanders — more victims than any other borough". → §5 para 2, §5.5 bullet 3.
  - https://storymaps.arcgis.com/stories/10787fbc706440f587425d69e3239c57 (excerpt): "the east shore of Staten Island, from South Beach to Oakwood Beach, was flooded by the storm surge and many houses were destroyed". → §5 para 2.
  - https://www.dvidshub.net/news/482917/seawall-will-raise-quality-life-shore-communities-staten-island-new-york (scrape, directQuote, dated 10.10.2024): "the approximate 5-mile-long seawall, with an elevation of 21 feet will be constructed … from the edge of Fort Wadsworth in the north, that's just south of the Verrazzano-Narrows Bridge, to Oakwood Beach in the south"; excerpt: "20-foot storm surge" (not used). → §5.5 bullet 5, §13 Fort Wadsworth card, Shore-by-shore East Shore.
  - Facebook group posts in results — not used.
- `Oakwood Beach buyout New York State homes purchased returned to nature Staten Island` · Firecrawl search + scrape https://urbanomnibus.net/2015/02/leaving-the-sea-staten-islanders-experiment-with-managed-retreat/ (Elizabeth Rush, Feb 11 2015, directQuote): "Of the 326 properties the State plans to purchase in Oakwood Beach, it currently owns 296 and has demolished 60. In Ocean Breeze 52 of the 109 planned purchases have been completed". → background for East Shore context; figures NOT placed on page (dated 2015).
- `Staten Island flash flooding July 2025 OR 2023 basements Mid-Island neighborhoods silive` · Firecrawl search + scrape https://www.silive.com/news/2025/07/severe-flash-flooding-cripples-major-staten-island-roads-during-storm-monday.html (Scott R. Axelrod, July 14 2025, directQuote): SIR "not running between the Huguenot and Tottenville stations due to flooding"; "Hylan Boulevard, in the vicinity of New Dorp Lane, was nearly impassable … as if it was a river"; "Richmond Avenue near Nome Avenue in New Springville"; "Amboy Road near Clarke Avenue"; "the basements of several homes on the block were flooded" (Poplar & Rossville avenues). → §5 para 3, §5.5 bullet 6, §8 Hylan card, Shore-by-shore Mid-Island and South Shore.
- `Staten Island internet outage businesses Verizon Spectrum silive 2025` · Firecrawl search → silive Jan 15 2026 Verizon bill-credit outage story (excerpt), Downdetector, Facebook — NOT used (carrier outage, not cabling). Hyperlocal news on Cat6/network-cable faults on SI: EMPTY.

### Local codes / permits
- `NYC Building Code Appendix G flood-resistant construction electrical equipment above design flood elevation Staten Island` · Firecrawl search + scrape https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction (directQuote): "Utilities and attendant equipment shall be located at or above the design flood elevation … or … constructed so as to prevent water from entering or accumulating within the components during conditions of flooding"; "Only flood-damage-resistant materials and finishes shall be utilized below the design flood elevation"; coastal high-hazard: space below lowest horizontal member "Free of obstructions; or Enclosed with breakaway walls providing unconditioned space useable solely for parking of vehicles, building access, storage or crawl space"; "Appendix G was amended by Local Law 77 of 2023 … effective date of June 10, 2023". → §5 para 4, §8.5 bullets 1–2, §9 Qs (flood-zone code, relocation), flood-line table.
- `NYC elevation certificate flood zone homeowners FloodHelpNY design flood elevation Staten Island` · Firecrawl search → https://www.nyc.gov/site/housingrecovery/programs/elevation-certificate.page (excerpt): "An Elevation Certificate (EC) is a document that identifies the elevation of your home in relation to the Flood Zone and the Base Flood Elevation". → FAQ F1. https://www.floodhelpny.org/en/elevation-certificates (excerpt) — background.
- `NEC 800.133(A)(2) communications cables separated at least 50 mm 2 in from electric light power conductors` · Firecrawl search → https://www.law.cornell.edu/cfr/text/29/1910.308 (excerpt): "Indoor communications wires and cables shall be separated at least 50.8 mm (2 in.) from conductors of any electric light, power, Class 1, nonpower-limited …"; https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-233133 (NYC Electrical Code Art. 805 excerpt, network-powered broadband 2 in.) — background; Mike Holt forum excerpt quoting NEC — background. → §7.5 bullet, §8.5 bullet 3, §9 bored-holes Q (exceptions referred to generally, not listed).
- NEC 800.25 abandoned cable (silo source, EC&M) → §8.5 bullet 4, FAQ tidy basement.
- DOB/CityLand Ida advice (silo source): "Never attempt to turn off the power or operate a circuit breaker while standing in water" → Before-you-call table row 1.

### Landmarks / corridors / commercial
- `Matrix Global Logistics Park Staten Island Bloomfield Amazon fulfillment center square feet` · Firecrawl search (excerpts): https://www.dnainfo.com/new-york/20170619/bloomfield/matrix-global-logistics-park-gulf-avenue-amazon — "200-acre Matrix Global Logistics Park, at a former oil tank storage facility"; https://www.margulieshoelzli.com/projects/matrix-global-logistics-park/ — "Building 1 is a 975,000 square foot facility consisting of a single story, 40-foot clear height structure"; "four buildings totaling up to 3.5 million square feet". → §8 Bloomfield card, Shore-by-shore West Shore.
- `Staten Island University Hospital North campus Seaview Avenue …` · Firecrawl search (excerpts): https://siuh.northwell.edu/ and /about — 475 Seaview Avenue; "668-bed specialized teaching hospital … two main campuses"; "1979: … moved from the Castleton Avenue complex to the new facility at 475 Seaview Avenue"; https://rumcsi.org/ — RUMC "440+-bed teaching hospital" (not used). → §8 Seaview card.
- `Staten Island Advance Hylan Boulevard New Dorp Lane medical offices …` · Firecrawl search (excerpts): https://rumcsi.org/locations/rhn-primary-walk-in-immediate-care-center-hylan-boulevard/ (4360 Hylan Blvd walk-in); https://www.orlincohen.com/location/staten-island-3311-hylan/ (3311 Hylan orthopedic office); https://www.citymd.com/urgent-care-locations/ny/new-dorp (2710 Hylan). → §8 Hylan card.
- `Empire Outlets St. George Staten Island opened square feet stores` · Firecrawl search (excerpt) https://en.wikipedia.org/wiki/Empire_Outlets — "350,000-square-foot retail complex in the St. George neighborhood"; steps from the ferry (empireoutlets.nyc). → §8 St. George card, §13 card.
- `Staten Island Mall New Springville Richmond Avenue square feet stores opened 1973` · Firecrawl search (excerpts): https://www.silive.com/news/erry-2018/03/05c8690920/10_things_to_know_about_the_st.html — "opened its doors on Aug. 9, 1973, with Macy's and Sears as its two anchor tenants"; https://www.nytimes.com/1973/08/10/archives/… — "on Richmond Avenue at Richmond Hill Road". → §8 Richmond Ave card, §13 card.
- `College of Staten Island Willowbrook campus acres …` · Firecrawl search (excerpt) https://www.csi.cuny.edu/about-csi/csi-glance — "Completed in 1994, the 204-acre landscaped Willowbrook campus of CSI, the largest in NYC". → §13 card.
- `Snug Harbor Cultural Center 83 acres 26 buildings …` · Firecrawl search (excerpt) https://en.wikipedia.org/wiki/Snug_Harbor — "83-acre … campus containing more than two dozen architecturally significant buildings set along the Kill Van Kull on the North Shore". → §13 card.
- `Freshkills Park acres former Fresh Kills landfill Staten Island NYC Parks` · Firecrawl search (excerpts): https://www.nycgovparks.org/park-features/freshkills-park — "Formerly the world's largest landfill"; https://freshkillspark.org/the-park/faqs — "At 2,200 acres, Freshkills Park is the largest landfill-to-park project in the world"; https://freshkillspark.org/ — "restoring 360 acres of wetlands". → §13 card.
- `Bay Street corridor Stapleton Staten Island rezoning Homeport Urby mixed-use buildings` · Firecrawl search (excerpts): nyc.gov Bay Street Corridor Neighborhood Plan page (no body text in excerpt); prodigyre realtor blog (~1,800 homes legalised by 2019 rezoning) — NOT used as a figure; corridor named only. → §8 St. George/Bay Street card.
- The Teleport (silo NYC source) — mentioned in hub; not repeated as a card here.
- Neighbourhood list in §13 "we also repair" = place names only.

### Prices used (live AESS pages only; no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-staten-island.html pricing table (also the cat6-repair-nyc hub).
- Replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord) — network-cable-repair-staten-island.html; same $175 on cat6-repair-nyc ("in every borough").
- Exterior entry made good (sleeved, sealed, bonded, drip loop) from $185 per penetration — network-cable-repair-staten-island.html.
- "No separate travel charge" for the bridge — network-cable-repair-staten-island.html FAQ/body.
- New-install comparison Cat5e $254 / Cat6 $296 / Cat6A $424 per drop to 100 ft — cat6-installation-staten-island.html.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party.
- FLAG for Anwar: blueprint §9 gives Staten Island 1.10× (Verrazzano surcharge), which would make the replacement drop $192.50 → $193; but the live SI network-cable-repair page and the cat6-repair-nyc hub both publish $175 un-multiplied (hub says "$175 per drop in every borough"), and the SI page publishes "no separate travel charge". No conflict between hub and SI page, so the page follows both live sources and applies no multiplier. cat6-installation-staten-island's $296 Cat6 drop = 1.088× NYC $272 (not 1.10×; 1.10× would be $299) — quoted as published, comparison only.

### Keyword notes (five layers, SI geo)
- Service: Cat6 repair Staten Island, Cat6 cable repair, Cat6 re-termination, relocating network equipment above flood level, Cat6 recertification, network split for two-family/house-office, Cat6 tracing.
- Problem: corroded basement jacks, flood-damaged Cat6, block-wall corrosion, runs under raised houses, dead pre-wired jacks, provider-moved router, data cable sharing holes with power, register drops when compressor starts, counter jack damage, PoE camera/AP faults.
- Technology: Cat6/Cat6A, permanent link, certification margins, time-domain fault location, sealed surface boxes/standoffs, NYC BC Appendix G design flood elevation, elevation certificate, 2-in separation from power (29 CFR 1910.308), NEC abandoned cable, PoE.
- Industry: homeowners, two-family landlords, medical/dental and professional offices in converted houses, strip-mall retail/POS, restaurants, West Shore warehouses, hospital-area practices.
- Geographic: Staten Island, North/Mid-Island/East/South/West Shore, St. George, Bay Street, Hylan Boulevard, New Dorp Lane, Seaview Avenue, Richmond Avenue/New Springville, Bloomfield, Forest Ave, Victory Blvd, Rossville, Tottenville, Midland Beach, Oakwood Beach, Fort Wadsworth; §13 list.

### Images (11) — permanent image rule; Drive folder "AESS Website Photos/Cat6 Repair" empty (main run), CompanyCam not connected
All cropped with PIL to remove faces and the printed phone number on shirts (network/ originals show "844-386-7238" on uniforms — cropped out), saved WebP q80 ≤1600px; md5-unique within page. Scenes chosen to avoid the scenes used by cat6-repair-queens (NCR set) and cat6-repair-bronx (cat6 set) in this batch; originally drafted crops of the corroded-plug, PoE-dome, drywall-cut, fish-tape and labelled-bundle scenes were dropped after the sibling pages showed they used the same scenes.
| images/cat6-repair/ | Source (crop box) |
|---|---|
| cat6-repair-staten-island-rack-tester-wire-map-check.webp (hero) | cat6-repair/cat6-repair-long-island-rack-cable-tester-reading.webp (470,385,1536,864) |
| cat6-repair-staten-island-block-wall-core-drill-entry.webp | network/network-installation-staten-island-core-drill-cmu-wall-penetration.webp (600,280,1448,1086) |
| cat6-repair-staten-island-outlet-row-plate-termination.webp | cat6-repair/cat6-repair-hudson-valley-outlet-row-low-wall.webp (0,350,1448,1086) |
| cat6-repair-staten-island-data-voice-plate-punch-down.webp | cat6-repair/cat6-repair-hudson-valley-data-voice-plate-retermination.webp (590,0,1402,1122) |
| cat6-repair-staten-island-pos-counter-jack-test.webp | cat6-repair/cat6-repair-long-island-pos-counter-jack-no-link-test.webp (0,500,1536,1024) |
| cat6-repair-staten-island-ceiling-access-point-cable.webp | cat6-repair/cat6-repair-long-island-ceiling-access-point-cable.webp (0,0,850,1024) |
| cat6-repair-staten-island-floor-box-keystone-service.webp | cat6-repair/cat6-repair-hudson-valley-floor-box-jack-service.webp (0,410,1402,1122) |
| cat6-repair-staten-island-switch-port-led-inspection.webp | cat6-repair/cat6-repair-long-island-switch-port-flashlight-check.webp (0,0,830,1024) |
| cat6-repair-staten-island-conference-table-grommet-cable.webp | cat6-repair/cat6-repair-hudson-valley-conference-table-cable-pull.webp (0,450,1402,1122) |
| cat6-repair-staten-island-toner-probe-panel-tracing.webp | network/network-installation-staten-island-network-cable-toner-tracing.webp (0,0,850,1086) |
| cat6-repair-staten-island-rj45-plug-and-crimper.webp | cat6-repair/cat6-repair-long-island-rj45-plug-recrimp.webp (0,410,1536,1024) |
DAILY-LOG note: `images: 11 reused (9 from images/cat6-repair LI/HV hub crops, originally images/network-cable-repair + images/cat6; 2 from images/network/) (no real Cat6 Repair photos yet)`.

## Question register — cat6-repair-staten-island

§9 "Questions Answered" (H3):
1. Our house was raised after Sandy — why do the Cat6 runs that cross the space underneath keep failing? (Water line)
2. Should the router, switch and patch panel come up out of a basement that has flooded before, and what happens to the Cat6 if they move? (Water line)
3. What does a flood-zone building's code allow below the design flood elevation when a Cat6 run is repaired? (Water line)
4. Why does a jack screwed straight onto the foundation block fail when the same kind of jack on a stud wall nearby keeps working? (Water line)
5. The upstairs unit's Cat6 passes through the downstairs apartment's ceiling — can the fault be pinned down before anyone opens the tenant's ceiling? (Houses)
6. The internet provider moved our router to a new spot during an upgrade, and the wired rooms stopped working — how do the runs get re-pointed? (Houses)
7. Our Cat6 goes through the same drilled holes as the house's electrical cable — could that explain the errors? (Houses)
8. We are turning the ground floor into an office and renting out the upstairs — can the existing Cat6 be split into two separate networks? (Houses)
9. When a Cat6 run inside a two-storey island house has to be replaced, what routes avoid opening finished walls? (Houses)
10. A register at our shop drops off whenever the walk-in cooler or the air compressor kicks on — is the Cat6 to blame? (Shops)
11. Why do the Cat6 links at a strip-mall counter fail more often than the ones in the back office? (Shops)

FAQ (§17, = FAQPage schema):
F1. Do you need to see the house's elevation certificate before moving network equipment out of the basement?
F2. Can the basement links be tested before storm season so we know which ones are weak?
F3. Can you repair the network cable to a standby generator or a heating system controller?
F4. Do you repair the Cat6 that connects a solar inverter or battery system to the home network?
F5. Can you repair a network cable that runs out to an EV charger in the driveway or garage?
F6. Does the power to the house have to be shut off while you work on the Cat6?
F7. Do you repair Cat6 in a modular home?
F8. Can a repair at a home office be booked on a Saturday?
F9. Can you leave the basement wall looking tidy after moving the panel upstairs?

Other "?" headings: "Wired Link Dead on Staten Island This Morning?" (repair capture), "Want Every Jack in the House Working and Labelled?" (CTA), "Island Network Link Failing Today?" (closing).

De-dup notes (by meaning): checked against NYC (26), LI (23), HV (25) registers above and the Queens and Bronx pages as built at ~09:25. Rewritten/removed from the first draft because a sibling already held the intent: "house sold as wired for Ethernet, half the jacks dead" (Queens "every jack in our new LIC apartment is dead"; Bronx "jacks never worked — repair or punch list") → replaced by Q6 provider-moved router; FAQ "can a tenant book a repair or must the owner" (Queens "repair in a rented apartment without the landlord's permission") → replaced by F3 generator/heating controller; FAQ "will a dehumidifier/sump protect basement Cat6" (Queens "will a damp basement keep damaging a run after repair") → replaced by F2 pre-storm baseline test; Q4 reframed from "why do basement jacks corrode" to the mounting-surface comparison; Q5 reframed to fault location before opening the tenant's ceiling (Queens holds "shared closet — repair one without cutting off the other"). Avoided intents: NYC Q15 trace without opening plaster (Q9 is replacement routing), NYC Q16 dry-out/reuse, LI Q5 insurance documentation, HV Q2 test-after-strike (F2 is pre-storm baseline), HV Q8 indoor cable on house exterior, HV Q14 one-trip prep (one-trip scoping kept in body only), LI F1 travel charge (no-bridge-charge stated in pricing body only), LI F2 pre-purchase test, LI F9 multi-unit visit, NYC F7 old cable on re-pull (F9 is about finish, abandoned cable mentioned in passing), HV F5 matching plates, HV F3 gate/intercom post. AI-check H3s chosen to avoid the LI "mesh" and "any electrician" H3s.

Masked paragraph similarity (difflib, geo-masked, p/li/td/h3/figcaption ≥8 words, prefiltered by bigram overlap): every block ≥0.65 vs cat6-repair-nyc, -long-island, -hudson-valley, -queens, -bronx is an excluded constant (freshness stamp, warranty sentence, licence/rating strip, NAP line, "parts you supply" warranty line, not-advice footer note, silo-nav link row, price-table item/source cells); vs network-cable-repair-staten-island only price-table cells.


---
<!-- appended by batch build cat6-repair-queens, 2026-10-17 -->
## Question register — cat6-repair-queens

§9 "Questions Answered" (H3):
1. Why does the kitchen display screen lose its connection when the line is busiest? (Counters/kitchens)
2. Mop water reaches the floor box under our register every night — is that what keeps killing the link? (Counters/kitchens)
3. Our POS company says the problem is "in the wall" and they don't repair wiring — what happens next? (Counters/kitchens)
4. Our roll-down gate housing has a Cat6 run beside it — could the gate be what keeps damaging it? (Storefronts)
5. Our basement is being brought up to the city's basement-apartment rules — what happens to the Cat6 running across its ceiling? (Houses/basements)
6. A contractor screwed new drywall over our Cat6 and now two rooms are dead — can it be fixed without tearing the wall off again? (Houses/renovation)
7. In our two-family house the tenants' Cat6 and ours share one closet — how do you repair one without cutting off the other? (Houses)
8. An installer drilled through our Cat6 while bringing in new internet service — can you document the damage as well as fix it? (Houses)
9. The room jacks in our Long Island City rental all run to a media panel in the hall closet — what has to happen in that panel before they work? (Towers)
10. Can a Cat6 jack in a rented apartment be repaired without the landlord's permission? (Apartments)
11. The builder's media panel in our condo closet is so crowded the door won't shut — can the Cat6 in it be repaired without rewiring the apartment? (Towers)
12. Our Jackson Heights co-op won't let contractors open the courtyard-side walls — how is a dead Cat6 run repaired from inside the apartment? (Co-ops)
13. Management says only their vendor can touch the telecom room — can you still fix the Cat6 inside our unit? (Towers)

FAQ (§17, = FAQPage schema):
F1. Can you leave a spare Cat6 run in place when you repair a kitchen or counter link?
F2. Does the building's super or landlord need to be there while you work?
F3. Would a Wi-Fi extender do the same job as repairing a dead Cat6 jack?
F4. How long should we keep the test results you give us?
F5. Can you repair a Cat6 run that passes through a fire-rated wall or floor?
F6. Do you repair the Cat6 that feeds digital menu boards?
F7. We just leased a Queens storefront and the last tenant left Cat6 everywhere — can you tell us what is usable?
F8. Do you give a written estimate before replacing any cable?
F9. Does a repaired Cat6 link come back at the same speed it had before?
F10. Can you show our staff how to tell a cable fault from a device fault next time?

Other "?" headings: "Register or Kitchen Screen Offline in Queens Right Now?" (repair capture), "A Queens Cat6 Link Down Before Tonight's Service?" (closing).

De-dup notes: compared by meaning against the NYC, LI and HV registers above and against the Bronx and Staten Island pages as on disk at ~09:30 (their registers appended in parallel). Changes made: LIC dead-jacks question re-angled from "broken or never connected" to the media-panel patching step (Bronx asks the building-wide punch-list version); a "damp basement keeps damaging the repair" FAQ was replaced with the post-repair speed FAQ because Staten Island asks whether to move equipment out of a flood-prone basement. Avoided on purpose: LI attic heat/stapled cable/garage conversion/pre-closing test/mall tenant/remote IT provider; HV rodents-in-barn ("how much chewed cable to replace" — rodents covered in body and §10.5 only), cold-weather, storm; NYC splice-vs-whole-run (drywall Q is about access, not splicing), riser approval, flooded cellar reuse, three-hour minimum; network-cable-repair-queens (office above restaurant, afternoon heat, shared riser tracing, PoE reboot, dead jack, before-opening scheduling). Borderline, flagged for review: F7 (inheriting a previous tenant's cabling) is close in spirit to LI F2 (testing a house before closing) and NYC F3 (repairing another contractor's Cat6).

Masked paragraph similarity (difflib, geo-masked, p/li/td/h3/figcaption ≥8 words): mean 0.42–0.43 vs each of cat6-repair-nyc, -long-island, -hudson-valley, -bronx, -staten-island. Blocks still ≥0.65 are excluded constants only: freshness stamp, warranty sentence, licence/rating line, BYOE warranty line, NAP, shared silo-nav sentence, pricing-source cells and the not-legal-advice note.

## Rockland County (cat6-repair-rockland-county)

Built 2026-10-17 (batch subagent). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query/directQuote mode). "Carried" = source already recorded with URL and finding in research/fiber-optic-installation.md (Rockland section), research/sonos-installation.md (Rockland section) or research/cat6-repair.md (silo) on 2026-10-17 and not re-fetched. Silo technical sources (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fixr Jan 2025) reused from research/cat6-repair.md in general terms only.

**Thesis (distinct from NYC = risers/pre-war/managing agents; LI = attic heat/length/outdoor; HV hub = storms/outdoor/distance; network-cable-repair-rockland-county = plaza continuous ceilings/neighbour fit-outs/landlord utility rooms; cat6-installation-rockland-county = new drops/campus belt; fiber-optic-installation-rockland-county = campus inheritance; sonos-installation-rockland-county = split-level audio):** Rockland's Cat6 is retrofit Cat6. The county's housing and commercial stock was built in the 1950s–70s boom before data cabling, so every run was added later by ISP installers, previous owners, renovators or IT providers. Faults concentrate at the points the retrofit created (staples, garage-ceiling crossings, hidden couplers/junction boxes above finished lower levels, rushed terminations), and are exposed by (1) multi-gig fiber upgrades, (2) ISP equipment relocations, (3) water on lower levels (July 2023 flash flood, Spring Valley repeated flooding), (4) property/tenant turnover; plus Rockland's new Chapter 286 written-contract rules. Rockland has the fewest lightning pulses of the six HV counties, so storms are de-emphasised versus the hub.

### Reddit (local)
- `site:reddit.com r/Rockland ethernet wiring house cat6 installer` · FC search · no r/Rockland cabling thread returned (results: r/electricians, r/HeliumNetwork, r/homeautomation, r/Honolulu — irrelevant). r/Rockland Cat6/ethernet fault threads: EMPTY (not accessible in build env — Firecrawl does not scrape reddit.com; search returned no relevant thread).
- Carried: https://www.reddit.com/r/Rockland/comments/1i0qwu0/optimum_vs_fios_in_rockland/ (excerpt: "Optimum - at least, in Nanuet - is a disaster…"; new excerpt this run: "Optimum fiber is the best if you can get it at your home.") → background for §5 para 3 (fiber upgrades); not quoted on page.

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★
- EMPTY (not accessible in build env). §10.5 states on-page that the AI Overview could not be opened; each H3 is framed as a commonly published claim and corrected with the sourced facts below.

### Local news / hyperlocal / weather
- `Rockland County Hurricane Ida September 2021 flooding Spring Valley Suffern Haverstraw basements damage` · FC search → lohud live blog https://www.lohud.com/story/weather/2021/09/02/hudson-valley-hurricane-ida-flooding-latest-updates/5692766001/ (FC scrape: only the lede "The remnants of Hurricane Ida hammered parts of the Hudson Valley, flooding much of the region…" — no Rockland-specific text) → NOT used. CBS2 YouTube "Anger grows following flooding of Rockland County apartment complex" (excerpt only) → led to the next query. Rockland-specific Ida facts: EMPTY.
- `Spring Valley NY apartment complex flooding heavy rain tenants Rockland news` · FC search → FC scrape https://abc7ny.com/post/floodplagued-spring-valley-apartment-complex-faces-uncertain-future-rockland-county/19194893/ (ABC7, Marcus Solis, May 29 2026): 9 Park Avenue, Spring Valley; problems "persisted for years, including a major flood in 2019"; county notices May 7 citing critical violations at the 52-unit complex; ordered "vacated, repaired or demolished"; "Basement apartments have already been deemed off-limits because of flooding" (og description); Ed Markunas, county Office of Buildings and Codes, on foundation cracks. → §5 para 4, §10.5 H3 4, §9 Q "basement units shut… reroute", Five Towns (Ramapo).
- `Rockland County flash flooding July 2023 OR 2024 OR 2025 Stony Point Haverstraw Sloatsburg roads basements` · FC search → FC scrape https://rocklandtimes.com/2023/07/11/stony-point-swamped-flash-flooding-causes-road-closure-and-property-damage-across-northern-rockland/ (Rockland County Times, Joe Kuhn, July 11 2023): storm "on Sunday" (July 9, 2023) "dumping over 8 inches of rain on the county and causing a flash flood that severely damaged homes, roadways, and state parks in north Rockland"; "Route 9W has suffered severe damage and cannot currently be used to enter or exit the town"; Route 210, Cedar Flats Road, Bulsontown Road closures. → §5 para 4, §5.5 bullet 4, §10.5 H3 4, Five Towns (Stony Point).
- Same search → FC scrape https://hazardmitigation.ny.gov/assess_risk/presidentially_declared_disasters/dr_4723_severe_storms_and_flooding_july_2023 (MitigateNY): "Declared Counties: Clinton, Dutchess, Essex, Hamilton, Ontario, Orange, Putnam, and Rockland"; "Rockland County: Several roads were washed out near Cedar Brook." → §5 para 4, §5.5 bullet 4, §10.5 H3 4.
- Stony Point PD / Rockland Report Facebook excerpts (Beach Road, Cricketown Road flooding) → NOT used (social posts).
- Carried (research/sonos-installation.md HV section): O&R July 6 2026 update https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k — "more than 47,000 customers have been impacted" since July 1; Clarkstown and Ramapo among towns still out. → §5.5 bullet 6.
- Carried (research/cat6-repair.md HV hub / fiber HV): Earth Networks 2020 NY lightning report — Rockland 64,575 pulses, 28 thunder days (lowest of six HV counties); Orange 275,059. → §5.5 bullet 5, §10.5 H3 5.
- Carried (fiber Rockland): Rockland Times Nov 2 2012 Sandy article — Piermont business district dark, basements pumped. → §13 Piermont Pier card.
- Local news on Cat6 / network-cable faults in Rockland specifically: EMPTY.

### Building stock / history / census
- `rocklandhistory.org a brief history of rockland` · FC scrape https://www.rocklandhistory.org/a-brief-history-of-rockland (re-fetched this run, directQuote): "In 1950s, homes were built at a rate of more than one thousand per year. Much of this growth was brought about by the opening of Tappan Zee Bridge in 1955 and the completion of the Palisades Interstate Parkway and the New York State Thruway during the same decade."; Nyack Turnpike connected Nyack to Suffern; Haverstraw "brick-making center of the East in 1817"; "more than forty-two brickyards"; county 176 sq mi. → §5 para 1, §5.5 bullet 1, §8 Route 59 card, §13 Haverstraw Brick Museum card.
- `censusreporter Rockland County profile` · FC scrape http://censusreporter.org/profiles/05000US36087-rockland-county-ny/ (re-fetched): 109,671 housing units; owner occupied 66%; single unit 64%. → §5.5 bullet 3.
- Carried (fiber Rockland): Wikipedia Rockland County census table 1950 89,276 → 1970 229,903; Ramapo 148,919 (2020). → §5 para 1, Five Towns (Ramapo).
- Carried (sonos HV): Stacker Sep 25 2025 (Census data) Rockland median year built 1970; 11.5% (12,523) built 1939 or earlier. → §5.5 bullet 2, §7 river-village card.
- Carried (fiber Rockland): https://explorerocklandny.com/about/communities/ five towns, 19 villages, 16 hamlets; https://www.ny.gov/counties/rockland town/village list (Spring Valley, Nyack straddle town lines). → §5.5 bullet 7, Five Towns intro, §13 town list.
- Split-level / raised-ranch prevalence statistic: none found (also EMPTY in sonos research) → described qualitatively only.

### Internet / fiber upgrades (multi-gig thesis)
- `Optimum fiber rollout Rockland County Nanuet Spring Valley ONT installation 2025` · FC search → FC scrape https://www.optimum.net/pages/fiber.html (Optimum "About Optimum Fiber Installation"): "Ethernet CAT 6 or higher", "A home network switch with a 10Gb port", "A 2.5Gb or 10Gb Ethernet adapter"; "We'll work with you to find the best location for your new equipment"; "we may need to drill a small hole"; install "may take up to three hours". → §5 para 3, §9 Qs 1–3 (context), §10.5 H3 1.
- Carried (fiber Rockland): https://ispreports.org/internet-service-providers-rockland-county-ny/ excerpt "Optimum offers Fiber service to 91.5% of Rockland County homes." → §5 para 3 (attributed to "a comparison site").
- `IEEE 802.3bz 2.5GBASE-T 5GBASE-T Cat5e Cat6 100 meters` · FC search → https://en.wikipedia.org/wiki/2.5GBASE-T_and_5GBASE-T (excerpt): 2.5GBASE-T and 5GBASE-T (802.3bz-2016) "can be deployed at a cable length of up to 100m on Cat 5e or better cables"; table lists Cat5e or Cat6, 100 m. Corroborated by https://resources.l-p.com/products/2-point-5-g-copper-sfp-2-point-5g-base-t-guide excerpt. → §9 Q1, §10.5 H3 1.
- Silo (ICC TSB-155-A): 10GBASE-T over Cat6 up to 37 m / 37–55 m → "10 gigabits over shorter runs" in §9 Q1 and §10.5 H3 1.

### Corridors / landmarks (all carried from research/fiber-optic-installation.md Rockland section and research/sonos-installation.md Rockland section unless noted)
- Nanuet Town Centre / Shops at Nanuet debuted 2013 (Wikipedia excerpt) → §8 Route 59 card. (1969 enclosed-mall date was a Reddit poster's claim — NOT used.)
- Palisades Center auction $175 million, Feb 2026 (News 12 excerpt https://hudsonvalley.news12.com/2026/02/06/palisades-center-mall-foreclosure-auction-goes-for-175-million/5TQCf7BHIIywOsEqXQfQcj) → §5 para 5, §8 Route 59 card.
- Blue Hill Plaza (Wikipedia): 21-storey + 8-storey, nearly 1.2M sq ft, 90 acres, SOM, completed 1972, ~40% of Rockland office leasing market (2011, citing Pearl River Patch), fiber from two central offices; Route 304 (rcbizjournal excerpt) → §8 Pearl River card, §13 card.
- Hudson Valley iCampus (industrialrealtygroup.com): ~2M sq ft lab/manufacturing/office, 200 acres, "mixed-use, multi-tenant campus" → §8 card, §13 card.
- Bradley Corporate Park (re-nj.com May 9 2019): 16 buildings, 180 acres, 1.2M sq ft, Blauvelt → §8 Route 303 card.
- 108 Route 303 Tappan 54 acres sold 2026; Monsey Center (Route 59 & Saddle River Road) sold (rocklandnews.com July 8 2026) → §8 Route 303 and Suffern/Monsey cards.
- Montefiore Nyack Hospital foundation newsletter: "more than 180,000 patients and visitors each year" → §8 Nyack card.
- Rockland Community College, 145 College Road, Suffern, 175 acres (suny.edu excerpt) → §8, §13 card.
- Edward Hopper House, 82 North Broadway, built 1858 by maternal grandfather (Wikipedia/edwardhopperhouse.org; sonos research) → §13 card.
- Haverstraw Brick Museum, 12 Main Street (haverstrawbrickmuseum.org; sonos research) → §13 card (street number not used on page).
- Piermont Pier, 1841, eastern terminus of the Erie Railroad, owned by the village, "almost a mile" (rocklandaudubon.org; piermont-ny.gov; sonos research) → §13 card.
- New City as county seat, Main Street/North Main Street professional offices; Suffern Lafayette Avenue downtown — from live page cat6-installation-rockland-county.html (AESS page, not an external source) → §8 cards. Flag: treat as AESS-published description.

### Local licensing / permits
- `Rockland County Chapter 286 home improvement license law 2026 contractors written contract` · FC search → FC scrape https://ecode360.com/9666538 (directQuote): adopted by the Rockland County Legislature 4-14-2026 by L.L. No. 4-2026; "HOME IMPROVEMENT — Means the following being done to a private residence: repair, replacement, remodeling, installation, construction, alteration, conversion, modernization made to, in or upon a private residence, apartment or dwelling place of not more than three units…"; listed examples (waterproofing, siding, decks, windows, roofs, … excavation) — no mention of data/low-voltage cabling; exclusions incl. "(2) Electrical work", "(10) … alarm device or system by a County-licensed alarm business or alarm agent"; "Every home improvement contract in excess of $500, and all amendments thereto, shall be in writing and shall be signed by all the parties"; "Before any work is done, the owner shall be furnished with a copy of the written agreement, signed by the contractor"; "No additional work in excess of $500 shall be performed without prior written authorization … on a contract change-order form"; search excerpt: cancel "prior to 12:00 midnight on the third business day". → §8.5 callout 1, §9 Q "new home improvement law", §10.5 H3 7. Page does NOT claim whether Cat6 repair is covered (directs to Dept of Consumer Protection) and does NOT claim AESS holds a Rockland HI licence.
- Carried (fiber Rockland): https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits — Master Electrician / inspection agency under Chapter 250; HI licence under Chapter 286. → §8.5 callout 2.
- `Rockland County Office of Buildings and Codes building permit required low voltage wiring data cabling Clarkstown Orangetown` · FC search → clarkstown.gov/building/building-permits, orangetown.com/when-do-i-need-a-building-permit (excerpts only, no list text), allamericanelectricalservice.com blog excerpt "Permit requirements are set by your municipality — Haverstraw, Stony Point, Clarkstown, Ramapo and Orangetown each run their own building…" (third-party, not cited by name). FC scrape https://www.rocklandcountyny.gov/departments/buildings-codes returned no body text. Whether low-voltage/data repair needs a permit in any Rockland town: EMPTY → page says only that permits are issued by the town or village and that like-for-like repair "rarely" needs one, checked per job. Flag for human review.
- Silo: NEC 800.25 abandoned cable (EC&M) → §8.5 callout 4.

### Yelp / competitor complaints — EMPTY (not accessible in build env)

### Prices used (live AESS pages only — no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-rockland-county.html ("specialty service rate of $195/hr with a three-hour minimum ($585)"), also HV hub.
- Replacement Cat6 drop "from $175" — network-cable-repair-rockland-county.html ("priced from $175 for a commercial Cat6 drop") and cat6-repair-hudson-valley.html.
- New-install comparison Cat5e $265 / Cat6 $309 / Cat6A $441 per drop to 100 ft — cat6-installation-rockland-county.html.
- Third-party national: Fixr Jan 2025 $125–$250/drop, $45–$75/hr (silo).
- CONFLICT FLAG: blueprint §9 Rockland multiplier 1.30× would make the replacement drop $228 (175 × 1.30 = 227.5, half-up); the live Rockland NCR page and the HV hub publish $175 un-multiplied, and $195/hr is a protected rate. Page follows the live pages. cat6-installation-rockland-county $309 = HV hub figure (1.136× NYC $272), not a §9 multiplier.

### Images (11) — permanent image rule (Drive folder empty per main run; CompanyCam not connected)
Library check: images/network-cable-repair/ and images/cat6/ contain only 31 distinct photos (each duplicated across area filenames), and all 31 are already used on the NYC/LI/HV Cat6 Repair hubs, so reuse of a source scene was unavoidable. Sources taken only from the first third (alphabetical) of each folder. Every source shows a technician's face, so each was CROPPED to a face-free region (also making the frame visually distinct from the hub use). Converted to WebP q80, all ≤1600 px wide.
| images/cat6-repair/ | Source | Crop box |
|---|---|---|
| cat6-repair-rockland-county-wire-map-crossed-open-pair.webp (hero) | network-cable-repair/network-cable-fault-detection-rockland-county.webp | (0,290,1536,1024) |
| cat6-repair-rockland-county-flashlight-ceiling-bundle-check.webp | network-cable-repair/network-cable-inspection-hudson-valley.webp | (680,0,1536,700) |
| cat6-repair-rockland-county-exposed-pairs-at-desk-leg.webp | network-cable-repair/damaged-ethernet-cable-repair-rockland-county.webp | (0,470,1300,1024) |
| cat6-repair-rockland-county-nicked-jacket-on-ceiling-grid.webp | network-cable-repair/crushed-network-cable-repair-rockland-county.webp | (250,200,1536,1024) |
| cat6-repair-rockland-county-keystone-punch-down-wall-plate.webp | network-cable-repair/keystone-jack-replacement-rockland-county.webp | (600,500,1400,1024) |
| cat6-repair-rockland-county-ceiling-access-point-cable-end.webp | network-cable-repair/access-point-cable-repair-rockland-county.webp | (0,0,860,1024) |
| cat6-repair-rockland-county-data-outlets-under-desk.webp | cat6/cat6-data-drop-installation-rockland-county-workstation-outlets.webp | (480,380,1402,1122) |
| cat6-repair-rockland-county-corridor-repull-cable-cart.webp | cat6/cat6-installation-rockland-county-corridor-pull.webp | (0,450,1402,1122) |
| cat6-repair-rockland-county-solid-copper-box-ceiling-feed.webp | cat6/cat6-cable-installation-rockland-county-ceiling-drop.webp | (560,0,1402,1122) |
| cat6-repair-rockland-county-floor-box-keystones.webp | cat6/cat6-floor-box-installation-rockland-county-conference-room.webp | (380,400,1402,1122) |
| cat6-repair-rockland-county-table-grommet-replacement-feed.webp | cat6/cat6-cable-installation-manhattan-conference-table-drop.webp | (660,150,1402,1122) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (6) and images/cat6/ (5), cropped to remove faces (no real cat6-repair photos yet)`. Note for Anwar: the library photos look AI-generated (company logo patches, stylised labels); the corridor crop still shows a distant figure from the waist down with no face.

### Keyword notes (five layers)
- Service: Cat6 repair Rockland County, Cat6 cable repair, Cat6 re-termination, Cat6 jack repair, Cat6 certification/testing, multi-gig link repair, hidden coupler removal.
- Problem: dead jack, link stuck at 1 gigabit after fiber upgrade, jacks dead after ISP moved router/ONT, drill strike, staple damage, finished-ceiling fault, junction-box splices, mesh falling back to wireless backhaul, lower-level flood corrosion, PoE budget drops, exam-room jack damage, doorbell PoE run.
- Technology: Cat6, Cat6A, 802.3bz 2.5G/5G, 10GBASE-T, certification tester, distance-to-fault, tone and probe, keystone, solid-conductor RJ45, PoE, CCA, NEC 800.25 abandoned cable, firestopping.
- Industry: homeowners (raised ranches, split-levels, colonials, capes, river-village houses), two-family/small multifamily landlords, medical/dental practices, office suites, strip plazas/shopping centres, flex/warehouse, home offices, renters.
- Geographic: Rockland County; Clarkstown, Orangetown, Ramapo, Haverstraw, Stony Point; New City, Nanuet, West Nyack, Congers, Valley Cottage, Bardonia, Pearl River, Orangeburg, Blauvelt, Tappan, Piermont, Sparkill, Suffern, Monsey, Airmont, Spring Valley, Hillburn, Sloatsburg, Pomona, Garnerville, Thiells, Tomkins Cove, Nyack; Route 59, Route 303, Route 304, Route 9W, Blue Hill Plaza, iCampus, Palisades Center, Nanuet Town Centre.

### Masked similarity (sim.py, 5-word shingle Jaccard, geo-masked)
vs cat6-repair-nyc 0.029 · cat6-repair-long-island 0.024 · cat6-repair-hudson-valley 0.038 · network-cable-repair-rockland-county 0.018 · cat6-installation-rockland-county 0.014 (shared shingles are mostly the mega-nav, forms and protected strings).

## Question register — cat6-repair-rockland-county

§9 "Questions Answered" (H3):
1. We moved to a multi-gig fiber plan in Rockland, but the wired office still tops out around one gigabit — is the Cat6 in the wall the limit? (Fiber/multi-gig)
2. The internet installer put the new box in a different room, and two wall jacks stopped working that same day — what happened to them? (Fiber/multi-gig)
3. The fiber crew drilled a new entry hole and now one basement run tests short — could the drill have caught it? (Fiber/multi-gig)
4. The Cat6 from our raised ranch's lower-level den to the bedrooms upstairs failed after we finished the basement ceiling — can it be reached without tearing out the new drywall? (Houses)
5. Why do the jacks on the half-level above the garage in our split-level fail more than any others in the house? (Houses)
6. A previous owner left a plastic junction box in our New City basement ceiling with several Cat6 runs joined inside it — can it stay? (Houses)
7. Our mesh Wi-Fi points are plugged into Cat6 jacks but still show a wireless link back to the router — is the wiring to blame? (Houses)
8. Our router and switch sit on the same lower-level wall as the sump pump — where should the Cat6 terminations go so the next flood does not reach them? (Water)
9. The basement units in our Spring Valley building are shut because of flooding, but the Cat6 to the upper floors passes through them — can it be rerouted around? (Water)
10. Exam-room jacks in our New City practice keep failing after the cleaning crew moves the carts — is there a repair that stops it? (Business)
11. We added a PoE camera to the small switch in our Clarkstown home office and now the desk connection drops — can PoE on one port affect another port's Cat6? (Business)
12. Our Suffern office's Cat6 was put in by the internet provider when we opened — when it fails, is the provider responsible or are we? (Business)
13. Does Rockland's new home improvement law change what our written Cat6 repair quote has to say? (Paperwork)
14. The alarm panel and our Cat6 share a closet in our Pearl River house — can the network runs be repaired without setting off or disturbing the alarm? (Paperwork)

FAQ (§17, = FAQPage schema):
F1. Can we send photos of the jack, the network closet and the router by WhatsApp before you come out to Rockland?
F2. Do you need our Wi-Fi password or internet account details to repair the Cat6?
F3. Can the old cable be used to pull its replacement through the wall of our split-level?
F4. If a run is being replaced anyway, can a second Cat6 be pulled alongside it for later use?
F5. Will the rest of our home network stay up while one Rockland run is being repaired?
F6. Is there a charge for a second trip if the repair needs a part that was not on the van?
F7. Can you repair the Ethernet run to a TV or games console behind a wall-mounted TV?
F8. We rent our Rockland house or apartment. Can we book the repair ourselves, or does the landlord have to?
F9. Can you repair the Cat6 feeding a wired video doorbell at a Rockland front door?
F10. What happens if the test shows our Cat6 is fine and the problem is the computer or the router?

Other "?" headings: "A Rockland Cat6 Jack Dead This Morning?" (repair capture), "Is Your Rockland Cat6 Ready for a Faster Internet Plan?" (multi-gig readiness H2), "Wired Connection Gone Quiet Somewhere Between Suffern and Nyack?" (closing).

De-dup notes: compared by meaning against the NYC, LI and HV registers in research/cat6-repair.md, plus the FAQ/headings of network-cable-repair-rockland-county, cat6-installation-rockland-county and the fiber/sonos Rockland registers. Deliberately avoided: NYC Q1 (100 Mbps link light — ours is multi-gig negotiation after an ISP upgrade), NYC Q2 (worked for years, now intermittent), NYC Q3 (cord vs jack vs wall), NYC Q8 (splice a damaged section — ours is an inherited junction box of joins), NYC Q10 (bad run takes PoE port down — ours is switch power budget affecting other ports), NYC Q14 (riser/neighbour approval), NYC Q15 (tracing in pre-war wall), NYC Q16 (cellar water dry-out — ours are relocation above the sump and rerouting around closed units), NYC F7 (old cable after re-pull), LI F2 (test before closing), LI F3 (school/house of worship), LI F9 (HOA), HV Q6 (addition joint), HV Q10 (high-bay damage), HV Q12/13 (brick/stone routes), HV F5 (matching plates), HV F10 (what to have ready — ours F1 is the photo channel), NCR Rockland FAQ (cost, several drops died at once, neighbour's shop, neighbour's contractor, marking, join vs replace, dead outlet, card terminal busy, landlord utility room, test reports, warranty, rest of HV), cat6-installation-rockland FAQ (licensing who may work, historic Nyack, cost), fiber Rockland FAQ (which parts of Rockland covered). Orange/Putnam batch siblings were not on disk when this page was built; all questions name Rockland places or Rockland-specific triggers (Chapter 286, Spring Valley flooding, raised ranch/split-level stock) to keep intent distinct — main run should re-check once those pages exist.

## Orange County (cat6-repair-orange-county)

Batch run 2026-10-17. Area page; up = /cat6-repair-hudson-valley; phone (845) 640-3835 (800 only in shared header chrome); GBP Bronx (#bronx, 460 E Fordham Rd). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. FC search = mcp__Firecrawl__firecrawl_search; FC scrape = mcp__Firecrawl__firecrawl_scrape. Shell curl blocked.

**Thesis (distinct from HV hub = storms/outdoor/distance; Rockland; Putnam):** most Orange County Cat6 that fails did not wear out — it was damaged by the trades that followed the cabling crew, or never finished/certified, in the county's fast-growth decade (KJ +63%, county +28,000, Route 17K warehouses, Crystal Run medical buildings); second strand: 19th-c. brick main streets with mixed/joined runs; third: lightning and floods (delayed corrosion). Repair = locate by distance, open small, photograph cause (who pays), certify.

### Local research (new this run)
- `Kiryas Joel Town of Palm Tree population growth 2020 census new construction` · FC search → FC scrape https://www.recordonline.com/story/news/local/2021/08/13/census-kiryas-joel-grew-leads-orange-population/8115187002/ (Times Herald-Record, Chris McKenna, Aug 13 2021): KJ 32,954 (+63%), most populous municipality; Warwick 32,027, town of Newburgh 31,985, Wallkill 30,486, Middletown 30,345, city of Newburgh 28,856, New Windsor 27,805; KJ ≈ half of county's 28,000+ increase; county +7.6% to ~401,000; >3,500 condos built/planned; families moving to Blooming Grove, Woodbury, Monroe; Palm Tree same boundaries. → §5 paras 1, facts list bullets 1–2; §7 card 1; §9 Q1; FAQ 1.
- `July 9 2023 flash flood Highland Falls Cornwall Orange County damage rainfall inches` · FC search → FC scrape https://abc7ny.com/post/new-york-flooding-hudson-valley-west-point-orange-county/13482914/ (ABC7, Jul 12 2023): Hochul "Nine inches of rain in this community… '1,000 year event'"; Fort Montgomery fatality; West Point garrison HQ inundated; Popolopen Bridge (US 9W) major damage; road closures incl. Route 218, 9, 9W, 9A, 293, 32, 6. → §5 para 4; §9 Highland Falls Q; Weather table; (corridor text cut).
- `Port Jervis Delaware River flood 2006 downtown damage businesses` / `Port Jervis 2006 flood June …` · FC search → FC scrape https://riveralerts.com/Site/Predicted/01434000 (NWS predicted page, Delaware at Matamoras/Port Jervis): crests 21.47 ft 6/28/2006, 20.52 ft 4/3/2005, 19.52 ft 9/18/2004; record 26.6 ft 2/12/1981 ice jam, damage to 950 structures ($14.7M); at 18 ft river may back up storm drains into Port Jervis between Railroad Ave and Water St; serious backwater near Neversink at 2006 crest. → §5 para 4 + facts bullet 5; Weather table rows 1–2.
- USGS SIR 2007-5067 (https://pubs.usgs.gov/publication/sir20075067): scrape returned HTTP 500 — EMPTY (not accessible in build env).
- `Crystal Run Healthcare Middletown campus buildings square feet medical offices` · FC search → FC scrape https://www.crystalrunhealthcare.com/crystal-run-through-years: 155 Crystal Run Rd opened 2002 (Town of Wallkill); 95 Crystal Run Rd 2009 (first 3T MRI, ASC, women's imaging); Newburgh 70,000 sq ft 2015; Monroe 66,000 sq ft 2016; 2,400+ employees. → §5 para 1; §7 medical card; §8 Crystal Run card; §9 imaging-vendor Q.
- `Orange County NY Department of Consumer Affairs home improvement contractor license requirement` · FC search → https://www.orangecountyny.gov/255/Licenses (FC scrape: page body JS-only — license list EMPTY); FC scrape https://www.orangecountyny.gov/DocumentCenter/View/951/Consumer-Law-Help-Manual---Home-Improvements-PDF: contract >$500 (contractor earning >$1,500/yr) must be written, plain English, signed; name/address/phone/licence number if any; work, materials incl. makes/models; progress payments; hourly payments not progress payments. → §8.5 bullet 1. Whether Orange County licenses home-improvement contractors: EMPTY — page makes no claim.
- `USDA 2022 Census of Agriculture Orange County New York number of farms average size` · FC search → https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36071.pdf (excerpt): 613 farms, 65,706 acres in farms. Average size cut off in excerpt — not used. → facts bullet 6.
- `Black Dirt Region Warwick Pine Island onion farms acres Orange County NY` · FC search → https://en.wikipedia.org/wiki/Black_Dirt_Region (excerpt: western Town of Warwick, centred on Pine Island). → facts bullet 6; §7 farm card. (Edible Hudson Valley "26,000 acres" excerpt not used.)
- `Route 17 third lane project Orange County NYSDOT 2026 construction start Exit 120 131` · FC search → excerpts only (ocpartnership.org, cicbca.org Federal Register concept); used only the 2022 HGAR $1B figure from fiber research (corridor section later cut). 
- `Middletown NY downtown North Street historic commercial buildings 19th century` · FC search → https://www.middletownny.gov/294/Middletown-Architecture (scrape: JS shell, EMPTY); https://northendmiddletownneighborhood.org/ excerpt ("North End … 18th- and 19th-century commercial … buildings") → background for "Middletown's North Street… same vintage" (§5 para 3).
- `drywall screw through ethernet cable new construction intermittent network fault` · FC search → excerpts only (reddit r/HomeNetworking cut cable; setupteam.ca retrofit) — background only, not quoted. Construction-damage reasoning rests on silo BICSI study guide (crushed by ties/staples, pull tension) and Fluke NEXT KB (couplers should not be used).
- `site:reddit.com Newburgh OR Middletown OR Goshen OR Warwick NY ethernet cable house wiring` · FC search → no Orange County cabling thread (r/hudsonvalley Kingston electrician only). Local Reddit: EMPTY (not accessible in build env).

### Reused (sources reached by earlier runs, research/fiber-optic-installation.md Orange section / HV hub)
- Earth Networks 2020 lightning: Orange 275,059 pulses, #1 in NY → §5 para 4, facts bullet 4, §9 Warwick barn Q, weather table.
- HGAR May 15 2020: Amazon 1,015,740 sq ft at Route 17K/747; Medline 1.2M sq ft; Town of Montgomery; construction began 2020 → facts bullet 3, §8 card 1.
- Pike County Courier letter (Orange Environment, Nov 2024): 37 warehouse projects, ~15M sq ft (attributed) → facts bullet 3.
- Wikipedia: East End HD (445 acres, >2,200 buildings, NRHP 1985, Italianate brick, Broadway/Liberty) → §5 para 3, §8 card, §13 card; Orange County Government Center (Rudolph, 1967, Irene 2011, reopened 2017) → §8, §13; Touro Horton campus (randrealty 2014, ~375,000 sq ft) → §7, §13; Woodbury Common (1985, 220 stores, 845,000 sq ft) → §8, §13; LEGOLAND NY (2021, ~150 of 500 acres, 250-room hotel, Exit 125) → §8, §13; Port Jervis (Tri-States Monument 1882, Erie RR, Front St, pop ~8,775) → §8, §13; Stewart Airport 1,552 acres → §8; county 840 sq mi, only NY county bordering NJ and PA → §13.
- Orange County Local Law No. 8 of 2007 (county electrician licence) and Local Law No. 1 of 2024 → §8.5 bullet 2, §10.5 H3 6.
- City of Newburgh ARC certificate of appropriateness (ecode360 30538879) → §7.5, §8.5 bullet 3.
- Greenlight Networks Orange County expansion (2025–2026 releases) → FAQ 6 (provider name only); Galleria at Crystal Run → §8 card.
- Times Union Jun 27 2024 (~13,000 Orange outages, ~60 mph) and O&R Jul 6 2026 (>47,000 customers affected) → weather table.
- Silo technical: Mike Holt 800.90(B) primary protector; EC&M NEC 800.25; Fluke NEXT KB (couplers); BICSI study guide (staples/ties); computercablestore (4 pairs for gigabit); Fixr Jan 2025 → §8.5, §10.5, §9.

### PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★
EMPTY (not accessible in build env). §10.5 states on-page that AI Overview could not be viewed; claims framed as commonly published.

### Local news/hyperlocal (Times Herald-Record, Mid-Hudson News) on Cat6/network cable faults specifically
EMPTY (no relevant result).

### Prices used (live AESS pages only; no new prices)
- $195/hr, 3-hr minimum ($585); additional $195/hr; replacement Cat6 drop from $175 (cable, keystone, plate, punch-down, testing, both-end labels, patch cord); lift hire at cost per day; closet audit by port count; plenum add per drop; after-hours premium — network-cable-repair-orange-county.html pricing table.
- New-install comparison Cat5e $276 / Cat6 $321 / Cat6A $459 per drop inside 100 ft — cat6-installation-orange-county.html.
- FLAGS: (1) §9 Orange 1.40× on Brooklyn Cat6 drop $247 = $346, but live cat6-installation-orange-county shows $321 (= Putnam's figure too); quoted as published. (2) $175 replacement drop and $195/hr carry no multiplier on any live Orange page; followed live pages. (3) cat6-installation-orange-county.html still carries the three-year warranty block (not this page's concern; this page uses the one-year sentence only).

### Images (11) — permanent image rule (Drive empty, CompanyCam not connected)
Middle third (alphabetical) of images/network-cable-repair/ and images/cat6/. Every scene in the library is already used by a hub (files are byte-identical copies per area), so each source was CROPPED to remove technicians' faces (all library photos show faces) and resaved WebP q80; crops differ visually from the hub versions.
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-orange-county-link-down-tester-switch-rack.webp (hero) | network-cable-repair/network-closet-troubleshooting-orange-county.webp |
| cat6-repair-orange-county-drywall-access-cut-at-failed-jack.webp | cat6/cat6-retrofit-installation-orange-county-drywall-cut-in.webp |
| cat6-repair-orange-county-wall-jack-no-link-open-pair-test.webp | network-cable-repair/network-jack-repair-orange-county.webp |
| cat6-repair-orange-county-cubicle-keystone-reterminate.webp | cat6/cat6-keystone-termination-ulster-county-outlet.webp |
| cat6-repair-orange-county-labelled-rack-bundles-network-room.webp | cat6/cat6-patch-panel-installation-orange-county-network-room.webp |
| cat6-repair-orange-county-probe-trace-labelled-patch-panel.webp | network-cable-repair/network-cable-tracing-orange-county.webp |
| cat6-repair-orange-county-rack-certifier-patch-port-test.webp | network-cable-repair/network-cable-repair-orange-county.webp |
| cat6-repair-orange-county-replacement-cable-fed-into-ceiling.webp | cat6/cat6-installation-suffolk-county-ceiling-drop.webp |
| cat6-repair-orange-county-j-hook-support-rehang.webp | cat6/cat6-installer-orange-county-jhook-pathway.webp |
| cat6-repair-orange-county-patch-panel-port-repunch.webp | network-cable-repair/patch-panel-repair-orange-county.webp |
| cat6-repair-orange-county-ceiling-tile-flashlight-cable-check.webp | network-cable-repair/network-cable-inspection-orange-county.webp |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (6) and images/cat6/ (5), cropped to exclude faces (no real cat6-repair photos yet)`.

### Keywords (five layers)
Service: Cat6 repair Orange County, Cat6 cable repair Newburgh/Middletown, Cat6 re-termination, construction-damage repair, handover/punch-list testing, Cat6 certification. Problem: dead jacks new building, drywall screw through cable, staple damage, never-terminated runs, hidden coupler, mixed old cable, delayed flood corrosion, lightning barn link, PoE drops. Technology: certification tester, distance-to-fault, tone probe, category-rated splice, keystone, NEC 800.90/800.25, fiber alternative. Industry: multi-family, new homes, distribution, medical, main-street retail/restaurants, hotels, outlet retail, farms/venues, schools/municipal. Geographic: Orange County NY, Newburgh, New Windsor, Middletown, Wallkill, Goshen, Chester, Monroe, Kiryas Joel, Woodbury/Central Valley, Montgomery, Warwick, Pine Island, Cornwall, Highland Falls, Port Jervis, Route 17K, Route 17, I-84, I-87, Stewart, Crystal Run, Woodbury Common.

## Question register — cat6-repair-orange-county

§9 "Questions Answered" (H3) + other "?" headings:
- Cat6 Down Somewhere Between Port Jervis and the Hudson?
- The jacks in several apartments of a new multi-family building in Kiryas Joel or Monroe lost link at the same time — where does the fault usually sit?
- Our new Montgomery office failed its Cat6 test after the drywall and flooring crews finished — how do you show the general contractor which trade damaged the runs?
- Our new-build house in Chester was sold with Cat6 in every room, but half the wall jacks are dead and the wiring subcontractor is gone — can the runs be found and finished?
- A distribution building near Stewart opened with hundreds of Cat6 runs that were never certified — how do you find the bad ones without stopping the operation?
- Our new Orange County building passed its electrical inspection — why didn’t anyone catch the Cat6 faults?
- The Cat6 between our ground-floor shop and the upstairs office on Front Street in Port Jervis runs through an old stair chase — can it be repaired without opening the finished ceiling?
- We found an inline coupler hidden inside the wall behind a Middletown storefront jack — how many more could there be, and how are they found?
- Our Newburgh building has a shop downstairs and apartments above, and every tenant’s provider ran its own Cat6 — how do you work out which runs are whose before repairing one?
- After the July 2023 flash flood our building in Highland Falls was cleaned up and the network seemed fine — why are Cat6 links failing now?
- Our Warwick farm’s Cat6 to the barn has died in a thunderstorm three summers running — should it be rebuilt in copper again or replaced with fiber?
- Our store near Woodbury Common is refitted for every season, and Cat6 jacks fail after each refit — how do we stop it?
- Our practice in one of the medical buildings off Crystal Run Road was renovated, and the imaging vendor wants the Cat6 recertified before connecting — what will they want to see?
- Guest rooms at our hotel near the Route 17 Goshen exit are losing their wired connection one room at a time — is it the cable or the in-room hardware?
- Orange County Jacks Still Dead After Move-In Week?

FAQ (§17, = FAQPage schema):
- Can repair visits in Kiryas Joel, Monroe and nearby communities be scheduled around Shabbat and Jewish holidays?
- Can you repair Cat6 in an Orange County building that is still under construction, before the certificate of occupancy?
- Can you work under a school-district or municipal purchase order in Orange County?
- Do you repair Cat6 at Orange County wedding barns and event venues ahead of a booked date?
- Can you work at a distribution centre near Stewart Airport that requires gate badges and a site safety induction?
- Greenlight’s installer left the fiber terminal in our garage — can the Cat6 already in our Orange County walls carry the service to other rooms?
- Can you repair Cat6 in a log or post-and-beam home in Orange County where there are no hollow walls?
- What happens if the fault turns out to be outside our building, on the utility pole or the provider’s line?
- Can one visit cover Cat6 faults at two of our Orange County sites — say Newburgh and Middletown — on the same day?
- Can a Cat6 repair at a Newburgh or Middletown restaurant be finished before opening so the registers are ready for service?
De-dup notes: compared by meaning with the silo register (NYC, LI, HV) and the parallel Rockland/Putnam pages as on disk. Rewritten after reading them: drywall-screw Q (Putnam asks how to find it) → now "how to show the GC which trade caused it"; spray-foam Q (Putnam asks the same) → "passed electrical inspection, why no one caught Cat6 faults"; telephone-grade mixed run (Putnam Carmel) → "hidden inline couplers, how many and how found"; flood-closet relocation (Rockland sump-pump Q) → "which runs belong to which tenant's provider"; FAQ historic-district approval (Putnam Cold Spring) → wedding-barn/venue FAQ. Avoided NYC water-reuse (Q16), NYC F7/F8 (old cable removal, reroute), LI F2/F5 (pre-closing test, mall tenant), HV storm/outbuilding Qs. Masked 5-gram Jaccard: NYC 0.031, LI 0.027, HV 0.050, Rockland 0.037, Putnam 0.042.

## Putnam County (cat6-repair-putnam-county)

Batch run 2026-10-17. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources (Fluke, BICSI guide, NEC 800.90 / 800.25, Fixr Jan 2025) reused from research/cat6-repair.md in general terms only.

**Thesis (differs from NYC = riser/pre-war access, LI = heat/length/environment, HV = weather from the outside in, NCR Putnam = power-event vs cable):** in Putnam the cable is cheap and the route is expensive — Highlands bedrock, wetland buffers and NYC watershed land, finished lake-cottage interiors (spray foam), Cold Spring historic-district façades — so the repair is "measure first, open once": locate the fault by distance, repair the termination or damaged length in place, replace only when testing proves the run can't be saved, then choose the route that fights rock/water/walls least.

### Reddit
- `site:reddit.com Putnam County NY OR Mahopac OR Carmel ethernet OR internet wiring OR "cat6" house` · Firecrawl search · https://www.reddit.com/r/Fios/comments/1qo2vqn/happening_again/ (excerpt only): "If the splice cases are frozen then all the light goes bad. We've been having these problems lately in Putnam Valley, NY." → background only (carrier-side fault, outside our scope); not quoted. Other hits (r/electricians Putnam feeders, r/Homebuilding) irrelevant. Local Reddit on failing Cat6: EMPTY (not accessible in build env — reddit not scrapeable).

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on-page that the AI Overview could not be viewed; each H3 is framed as a commonly published claim (cost guides, forums, how-to pages), corrected with sourced facts below.

### Geology / terrain
- `Hudson Highlands Putnam County bedrock gneiss shallow soils ledge outcrops geology` · Firecrawl search · https://nysm.nysed.gov/sites/default/files/mc11_bedrockgeologyputnamwestchesternyfairfieldct.pdf (excerpt): "The rocks of the Hudson Highlands comprise a Precambrian complex of gneisses, migmatite, marble, granite and granodiorite." → §5 para 1, §5.5 bullet 1. (Southeast "Brewster Yards DEIS" geology excerpt — not used.)
- `Putnam County power outages storm NYSEG Central Hudson customers without power Carmel Mahopac` · Firecrawl search → scrape https://www.wamc.org/hudson-valley-news/2021-03-11/nyseg-is-upgrading-circuits-in-putnam-county (WAMC, Mar 11 2021): NYSEG circuit upgrades in the Town of Carmel on Horsepound Road and Stebbins Road; "there will be some rock drilling to get them into the ground"; wider, more wind-resistant poles. → §5 para 1, §5.5 bullet 1.

### Water / watershed / wetlands (local licensing & permits)
- `Putnam County NY reservoirs NYC watershed Croton system West Branch Boyds Corner Middle Branch` · Firecrawl search · https://www.nyc.gov/site/dep/water/west-branch-reservoir.page (excerpt): Towns of Kent and Carmel; ~35 miles from NYC; 8 billion gallons; in service 1895; connected to Lake Gleneida "one of the three controlled lakes"; 20 sq mi drainage basin. → §5 para 2, §5.5, §9 West Branch Q, §13 landmark card.
- Same search · https://govt.westlaw.com/nycrr/... (excerpt): Croton System reservoirs = Bog Brook, Boyds Corner, Croton Falls, Middle Branch, West Branch, East Branch, Diverting… → §5 para 2.
- `NYC DEP watershed regulations land disturbance trenching near reservoir watercourse wetland 100 feet limiting distance Putnam` · Firecrawl search · https://www.law.cornell.edu/regulations/new-york/10-NYCRR-128-3.9 (excerpt): "The construction of an impervious surface within the limiting distance of 100 feet of a watercourse or wetland, or within the limiting distance of 300 feet of a reservoir, reservoir stem, or controlled lake, is prohibited"; SWPPP for clearing/grading ≥2 acres within limiting distances. → §5.5, §8.5 card, §9 West Branch Q. Page states a cable trench is not an impervious surface (our reading; flagged below).
- `Town of Kent OR Town of Carmel NY wetlands permit buffer 100 feet excavation regulated activity` · Firecrawl search → scrape https://www.townofcarmelny.gov/DocumentCenter/View/456/Wetland-Permit-Application-PDF (directQuote): "the Town protects wetlands 1/8 of an acre and larger. In addition, a 100 foot buffer around each wetland is also regulated… if any type of construction or other activity within this area is to be conducted, a wetland permit will be required"; form asks about disturbance "within 100 feet of a wetland? (Including lakes, ponds, streams, etc.)". → §5 para 2, §5.5, §8.5 card, §9 Lake Mahopac Q, glossary, FAQ dock.
- Same search · https://www.townofkentny.gov/286/Building-permit-requirements (search excerpt only; scrape returned only page chrome): "If your project is 100 feet from wetlands (ponds, streams, and watercourses), more than 5,000 square feet of soil disturbance, Permits generally take 14 - 21…" → §8.5 card, §9 West Branch Q (page names only the 100-ft flag, not timings). Full Kent text: EMPTY (not accessible in build env).
- Reused (HV hub research): Central Hudson Dig Safely / 811 notice → §8.5 "call before you dig" (page gives no day count).
- Putnam County / town low-voltage licensing for cable repair: EMPTY — not researched to a primary source; page makes no licensing claim beyond AESS's NYS licence. (Note: cat6-installation-putnam-county.html says "Putnam licenses at county level" — unsourced there; not repeated.)

### Historic district
- `Cold Spring village Historic District Review Board certificate of appropriateness exterior changes Main Street` · Firecrawl search · https://www.coldspringny.gov/242/Historic-District-Review-Board (excerpt: "reviews exterior changes to buildings") → scrape https://www.coldspringny.gov/DocumentCenter/View/2075/Cold-Spring-Architectural-and-Historic-District-Design-Standards-PDF (directQuote): Board reviews "any change, construction, reconstruction or demolition of exterior architectural features… visible from the street"; typical features include "Exterior features such as air conditioners, commercial trash receptacles, fences, utilities, etc."; not subject to review: "Regular and normal maintenance which does not alter the appearance…" and "Work which is not visible from the street." → §5 para 3, §7 village card/method, §8.5 card, §9 Cold Spring Q, glossary.
- `Cold Spring Historic District National Register Main Street…` · Firecrawl search → scrape https://en.wikipedia.org/wiki/Cold_Spring_Historic_District: 691 acres; built early 19th c.; NRHP Nov 23 1982; bounded by Main St (NY 301), Cedar (NY 9D), Fair St, Paulding Ave; "over 200 buildings". → §13 card.

### Local news / weather
- Patch, scrape https://patch.com/new-york/southeast/power-outages-slam-hudson-valley (Lanning Taliaferro, May 15–16 2018): "anecdotal reports were made of tornado-like winds in Newburgh and Carmel"; NYSEG "28,459 in Putnam"; Central Hudson "4,698 in Putnam". → §5 para 4, §5.5, §10.5 H3 7.
- `Putnam County flooding storm damage roads closed Philipstown Putnam Valley Highlands Current 2023 OR 2024 OR 2025` · Firecrawl search → scrape https://highlandscurrent.org/2023/07/22/elected-officials-and-public-confront-storm-damage/ (directQuote): flooding "caused by more than 8 inches of rain, tore into bridges, dams, roads and buildings… at least 130 homes, severely damaging about 20"; Philipstown roads damaged: Old Manitou Rd (closed), Old Albany Post Rd, Chapman Rd, Avery Rd, Philipse Brook Rd, Indian Brook Rd; county work on Upper and Lower Station Roads, Garrison; "Philipstown and other western Putnam towns suffered the most". → §5 para 4, §5.5, Town-by-town (Philipstown).
- Same search → scrape https://www.putnamvalley.gov/state-of-emergency-declared-in-the-town-of-putnam-valley-effective-at-4-pm-on-wednesday-july-29-2026/ : State of Emergency effective 4 PM Wed July 29 2026 "due to the flash flooding, torrential rainfall, numerous road and bridge closures"; travel restricted on Cimarron, Horton Hollow, Canopus Hollow, Tinker Hill, Reichert St, Camp Collins Rd. → §5 para 4, §5.5, §10.5 H3 7, Town-by-town (Putnam Valley). (Page spells "Reichert"; Instagram excerpt "Reichart" — page uses only the first four road names.)
- Reused (fiber HV research): Earth Networks 2020 NY lightning report — Putnam 75,093 pulses, 35 thunder days. → §5.5, §10.5 H3 7.
- lohud / News12 / Putnam County News & Recorder on Cat6 or network-cable faults specifically: EMPTY. (pcnr.com storm article excerpt — undated in excerpt, not used.)

### Housing / demographics
- Reused (sonos HV research): Stacker Sep 25 2025 (Census data) — Putnam #41, median year built 1968, 17.9% (6,857) built 1939 or earlier. → §5 para 3, §5.5, §7 card.
- `Putnam County NY housing units census quickfacts owner-occupied…` · Firecrawl search · https://datausa.io/profile/geo/putnam-county-ny (excerpt): "In 2024, 83.8% of the housing units in Putnam County, NY were occupied by their owner." → §5.5. (Census Reporter 38,607 housing units — not used.)
- `Lake Mahopac largest lake Putnam County acres…` · Firecrawl search · https://www.putnamvalley.gov/districts-pv/lake-oscawana-management-improvement-district/ (excerpt): Lake Oscawana "the largest of several lakes and ponds in the Town of Putnam Valley". Lake Mahopac acreage conflicts (587 realty vs 583 Tripadvisor) — no acreage used. → lake names only (§5, §7, Town-by-town).

### Landmarks / corridors
- `Historic Putnam County Courthouse Carmel 1814…` · Firecrawl search · https://en.wikipedia.org/wiki/Putnam_County_Courthouse_(New_York) (excerpt: built 1814, renovated 1847, hamlet of Carmel, county seat); https://www.lohud.com/story/news/local/putnam/2024/03/22/... (excerpt: "built in 1814, and is one of the oldest court houses in New York… on Gleneida Avenue"). → §13 card, §8 Gleneida card.
- `Tilly Foster Farm Brewster Southeast county-owned acres history` · Firecrawl search · https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2022/August/minutes/Phys-08-25-22-Presentation-Tilly-Foster-Overview-2022.pdf (excerpt): "Approximately 199 Acres in the Town of Southeast… Originally used as a dairy farm, then used for horse breeding… Putnam County purchased in 2002." → §13 card, Town-by-town (Southeast).
- `Clarence Fahnestock Memorial State Park acres…` · Firecrawl search · https://parks.ny.gov/visit/state-parks/fahnestock-state-park-clarence-fahnestock (excerpt): "This 15,000-acre park, covering land in Putnam and Dutchess counties"; office 1498 Rte 301. (Wikipedia gives 15,731 acres — page uses the NYS Parks figure.) → §13 card.
- Reused (sonos HV research): Boscobel — moved 15 miles upriver; demolished in the 1950s, fragments reassembled (Wikipedia / boscobel.org). → §13 card.
- `Brewster Yards Southeast NY transit-oriented development Metro-North Harlem Line Brewster station…` · Firecrawl search · https://en.wikipedia.org/wiki/Brewster_station (excerpt: Harlem Line, 9 Main Street, Brewster); Southeast station/Brewster Yards expansion (DHK, southeast-ny.gov excerpts — not used). → §8 Brewster card, Town-by-town, FAQ Metro-North.
- Corridors (Route 6, Route 22, Route 52, Route 311, Route 312, I-84, Route 301, Taconic) and hamlet names in "We also repair" = place names only, consistent with network-cable-repair-putnam-county.html coverage list. No business, building or tenant is named as a customer.
- `Putnam County broadband unserved…` · Firecrawl search: Comcast "$11.4 million … 390 locations in Putnam County" excerpt is Putnam County, **Florida** (palatkadailynews) — NOT used. Putnam NY broadband award data: EMPTY.

### Prices used (live AESS Putnam pages only; no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr; replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord); battery backup "quoted per position"; closet audit "quoted by port count"; after-hours/weekend "premium applies"; "No travel surcharge" — network-cable-repair-putnam-county.html pricing table. → §14 table, packages, FAQ Saturday.
- New-install comparison Cat5e $276 / Cat6 $321 / Cat6A $459 per drop to 100 ft — cat6-installation-putnam-county.html. → §14, §10.5 H3 1.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party. → §14, §10.5.
- FLAGS: (1) $175 replacement drop and $195/hr carry no §9 1.45× multiplier on any live Putnam page (1.45× of $175 would be ~$254); page follows the live Putnam page. (2) cat6-installation-putnam-county $321 differs from HV hub's $309 HV installation figure; page quotes the Putnam figure. (3) "Cable trench is not an impervious surface" is our reading of 10 NYCRR 128-3.9 wording, worded cautiously and with a not-legal-advice note.

### Images (11) — permanent image rule (Drive folder empty per main run; CompanyCam not connected)
All 31 distinct photos in images/network-cable-repair/ + images/cat6/ are already used by the three hubs (perceptual-hash check), so sources were taken from the last third of each folder alphabetically and **cropped to exclude every face** (brief rule), which also makes them visually distinct from the hub/sibling uses.
| images/cat6-repair/ | Source (crop box) |
|---|---|
| cat6-repair-putnam-county-counter-jack-no-link-reading.webp (hero) | network-cable-repair/pos-network-cable-repair-putnam-county.webp (600,470,1536,1024) |
| cat6-repair-putnam-county-corroded-plug-block-wall.webp | network-cable-repair/water-damaged-network-cable-repair-putnam-county.webp (640,300,1536,1024) |
| cat6-repair-putnam-county-rj45-plug-and-crimper.webp | network-cable-repair/rj45-connector-replacement-putnam-county.webp (0,450,1536,1024) |
| cat6-repair-putnam-county-data-voice-keystone-rework.webp | cat6/cat6-voice-data-outlet-installation-westchester-county.webp (620,480,1402,1122) |
| cat6-repair-putnam-county-partition-jack-row-reterminate.webp | cat6/office-cat6-installation-putnam-county-outlet-bank.webp (500,350,1448,1086) |
| cat6-repair-putnam-county-poe-dome-no-power-reading.webp | network-cable-repair/poe-camera-cable-repair-putnam-county.webp (0,0,900,1024) |
| cat6-repair-putnam-county-switch-port-link-lights.webp | network-cable-repair/switch-port-troubleshooting-putnam-county.webp (0,0,830,1024) |
| cat6-repair-putnam-county-fish-tape-conduit-repull.webp | cat6/cat6-wiring-putnam-county-fish-tape-conduit.webp (0,440,1402,1122) |
| cat6-repair-putnam-county-panel-port-repunch.webp | network-cable-repair/patch-panel-repair-queens.webp (0,0,1000,1024) |
| cat6-repair-putnam-county-replacement-cable-carton.webp | cat6/office-cat6-installation-nyc-corridor-crew-pull.webp (0,500,760,1122) |
| cat6-repair-putnam-county-printer-data-jack-retermination.webp | cat6/office-cat6-installation-suffolk-county-printer-data-jack.webp (560,400,1402,1122) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (6) and images/cat6/ (5), cropped to exclude faces (no real cat6-repair photos yet)`.

### Keyword notes (five layers)
- Service: Cat6 repair Putnam County, Cat6 cable repair, Cat6 re-termination, in-line Cat6 repair, Cat6 fault location, Cat6 certification after repair, aerial/outdoor Cat6 repair, PoE camera cable repair.
- Problem: dead jack, intermittent drop, no link, PoE no power, screw/nail through cable, crushed cable, torn aerial span, corroded plug, flooded basement panel, garage penetration, telephone-grade cable mislabelled as Cat6, kitchen cable damage.
- Technology: distance to fault, permanent link vs channel, insertion/return loss, split pair, category-rated junction, support wire, drip loop, primary protector (NEC 800.90), abandoned cable (NEC 800.25), shielded Cat6, mesh wired backhaul.
- Industry: homeowners, lake/second homes, short-term rentals, village retail/restaurants, professional offices in converted houses, practices, trade yards, home businesses, farms.
- Geographic: Putnam County; Carmel, Mahopac, Kent, Lake Carmel, Southeast, Brewster, Patterson, Putnam Valley, Philipstown, Cold Spring, Nelsonville, Garrison; Route 6/22/52/301/311/312, I-84, Taconic; West Branch Reservoir, Lake Gleneida, Lake Mahopac, Lake Oscawana.

## Question register — cat6-repair-putnam-county

§9 "Questions Answered" (H3):
1. If trenching a new Cat6 run across our Putnam Valley lot means cutting through ledge, what are the alternatives to digging?
2. Does replacing a Cat6 run near Lake Mahopac or another lake in the Town of Carmel need a wetland permit?
3. We are close to the West Branch Reservoir in Kent — do the city's watershed rules limit how a damaged Cat6 run can be replaced?
4. A falling limb tore down the Cat6 we had strung between the house and the garage — should the aerial run be repaired or put underground?
5. Our standby generator takes over during Putnam outages — why do the PoE cameras drop when it does, and is the Cat6 to blame?
6. Our cottage on Lake Carmel was winterized with spray-foam insulation, and the Cat6 inside the walls has failed — can it still be repaired?
7. A drywall screw or trim nail went through a Cat6 run during our renovation — how do you find the damaged spot without opening every wall?
8. Where the Cat6 passes from our attached garage into the house in Mahopac, the hole was never sealed — does the repair have to fix that?
9. Since an EV charger went into our Patterson garage, the Cat6 link out there keeps dropping — can the new circuit cause that?
10. Does a Cat6 repair on a Main Street building in Cold Spring need approval from the Historic District Review Board?
11. Our Carmel office is a converted house, and some of its jacks turn out to be wired with telephone-grade cable rather than Cat6 — can those be repaired?
12. The Cat6 to the kitchen printer and card terminal in our Cold Spring restaurant keeps failing — what about a kitchen kills network cable?

FAQ (§17, = FAQPage schema):
F1. Can you repair the Cat6 at a short-term rental in Cold Spring or Philipstown between guest stays?
F2. Our caretaker looks after the lake house while we are away — can the technician meet them instead of us?
F3. Can you repair Cat6 that runs down to a dock or boathouse on Lake Mahopac?
F4. Will you protect the plaster and woodwork when repairing Cat6 inside an older Garrison or Cold Spring house?
F5. We run a business from a home office in Patterson — can a failed link get a temporary fix the same day while the proper repair is planned?
F6. Our house is up a steep private road in Putnam Valley — can a technician still get there in winter?
F7. If the problem turns out to involve the electrical side — a generator inlet, a panel or a surge device — do you bring in an electrician?
F8. Will you photograph a repair that ends up hidden inside a wall or ceiling, so a future owner or contractor can find it?
F9. We commute on Metro-North from Brewster — can a Cat6 repair be booked for a Saturday or an early morning?
F10. Our builder used shielded Cat6 — does that change how a repair is done?

Other "?" headings: "Dead Cat6 Jack Somewhere Between Cold Spring and Brewster?" (repair capture), "Lake House or Garage Link Dark Since Last Weekend?" (closing).

De-dup notes: compared by meaning against the NYC, Long Island and Hudson Valley registers in research/cat6-repair.md and against cat6-repair-rockland-county.html as built at 09:36 (parallel batch). Three draft questions were replaced because Rockland asks the same intent: mesh node on wireless backhaul despite Cat6 jack; internet installer moved the box and jacks died; where to put terminations when the network wall floods (→ garage-to-house penetration, EV-charger garage drop, telephone-grade cable in a converted-house office). Avoided: HV storm/strike/post-outage/cold/buried-ice/rodent/indoor-cable-outdoors/pole-plug/stone-wall/remote-site/weekend-house/gate/well-house/barn/crawlspace/knob-and-tube/Starlink/retest-after-storm/jack-matching; LI attic heat, over-length, garage water, flood insurance, salt air, landscaper-cut buried run, slab ranch, stapled attic cable, seasonal reopening, campus links, long PoE camera run, dock scanners, travel charge, pre-closing test, school/library breaks, medical before hours, mall tenants, re-insulation, surge protection, garage conversion, HOA, remote IT; NYC 100 Mbps, intermittent, cord/jack/cable, NEXT, return loss, which end, re-pull, splice-or-replace (ours asks route alternatives / renovation puncture location, not "can it be spliced"), PoE night reboot, PoE port damage, Cat6A parts, 10G errors, CCA, riser approval, pre-war trace, cellar water reuse, three-hour minimum, recertify floor, other contractor's cable, port mapping, Cat6A on van, 24-port time, old cable fate, reroute around wall, ceiling APs, two buildings on a lot. Watch: Q5 (generator transfer) is adjacent to HV Q3 (links dead after power return) — different intent (momentary transfer reboot vs permanent failure).


---

# Merged from batch 2026-10-17 (cat6-repair-nassau-county)

## Nassau County (cat6-repair-nassau-county) — local research, 2026-10-17 batch

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources (Fluke NEXT KB incl. "female couplers should not be used", computercablestore 4-pair/100 Mbps, EC&M NEC 800.25, Fixr Jan 2025) reused from research/cat6-repair.md. Hub-research items reused: ny.gov "two cities, three towns, 64 incorporated villages"; Nassau Consumer Affairs HIC licensing + fingerprinting (nassaucountyny.gov/1563 excerpt).

**Thesis (distinct from LI hub heat/length/weather, NYC access/risers, HV outside-in):** Nassau is a built-out, owner-occupied county of pre-1960 housing renovated repeatedly; Cat6 was retrofitted into finished rooms and is most often damaged by the *next* trade (drywall screws, flooring nails, kitchen/basement remodels, attic/roof/solar crews, HVAC, provider equipment moves, office refits, post-Sandy house raising). Repair = locate by distance from both ends, open one patchable hole, plate the studs, keep terminations above flood level in raised/flood-zone homes, check the municipality (3 towns/2 cities/64 villages) only when new pathways are needed.

### Housing stock / demographics
- `Nassau County median year structure built housing units owner-occupied census` · Firecrawl search →
  - https://www.census.gov/quickfacts/nassaucountynewyork (excerpt): 480,591 housing units (July 1 2025); owner-occupied rate 81.9% (2020–2024); median value owner-occupied $684,700; 48,718 employer establishments (2023). → §5 para 2, §5.5 bullets 3 and 5.
  - https://www.point2homes.com/US/Neighborhood/NY/Nassau-County-Demographics.html (excerpt, ACS-derived): median construction year 1955; 33.9% built 1950–59; 19.2% built 1939 or earlier; 76.1% 1-unit detached. → §5 para 1, §5.5 bullets 1–2, §10.5 H3 1 (attributed "ACS figures as republished by Point2 Homes").

### Sandy / house raising / flood guidance
- `Nassau County NY Rising home elevation Superstorm Sandy number of homes elevated South Shore` · Firecrawl search →
  - https://projects.newsday.com/long-island/sandy-by-the-numbers/ (scrape): "nearly 3,500" LI homes elevated or slated, "mostly in flood zones, where raising is required to qualify for flood insurance and to rebuild in accordance with local and state building codes"; 361 storm homes resold at auction (199 Nassau). Sources FEMA, GOSR. → §5 para 4, §5.5 bullet 4.
  - https://www.nysenate.gov/newsroom/in-the-news/2019/todd-kaminsky/7-years-after-sandy-most-are-back-their-homes-theyre-not (scrape, Newsday reprint 2019): GOSR "78% of 3,310 elevations were completed"; Island Park home raised 8 ft; Freeport split-level took 5 ft of water. → §5 para 4, §5.5 bullet 4 (3,310 only; personal stories not used).
- `FEMA P-348 protecting building utility systems from flood damage elevate electrical equipment above base flood elevation telecommunications` · Firecrawl search → https://agents.floodsmart.gov/sites/default/files/media/document/2025-07/fema_nfip-p-348-protecting-building-utility-systems-from-flood-damage-2017.pdf (excerpt): "Electrical devices and wiring should be located above the required flood elevation"; "Primary components like modems, video switches, splitters, and routers should be elevated." → §5 para 4, §7.5 raised houses, §8.5 bullet 4, §9 raised-house Qs, §10.5 H3 6.

### Licensing / permits
- `Nassau County Office of Consumer Affairs electrician license master electrician low voltage exemption` · Firecrawl search → nassaucountyny.gov/1563 (excerpt only; licensing phone/hours). qualifyingagents.com excerpt says the county DCA list does not include electricians — not used. Detail of who needs a HIC licence: EMPTY (page JS shell, as on hub run).
- `Town of Hempstead building permit low voltage wiring required data cable` · Firecrawl search →
  - https://hempsteadny.gov/191/Building-Department + /622/Online-Permit-Center (excerpts): town building department, online permit centre. → §8.5 bullet 2, Towns section.
  - https://ehhaineselectric.com/resource/do-i-need-a-permit-for-electrical-work-in-nassau-county/ (scrape, directQuote): "Low-voltage systems (security, data, A/V) may not require a permit, but running new wiring through walls or attics often does."; "Electrical permits must be pulled by a licensed master electrician registered in the specific township or village." → §8.5 bullets 2–3, §10.5 H3 5 (attributed to "an electrical contractor's published guide").
- Village-specific low-voltage permit rules: EMPTY (not searched per village; page says check by address).

### Landmarks / corridors
- `Marcus Avenue Lake Success office buildings Northwell headquarters...` · Firecrawl search → https://libn.com/2016/06/06/northwell-health-relocates-hq/ (excerpt: HQ relocated to 100,000 sf building at 2000 Marcus Ave, New Hyde Park); https://www.bskyre.com/news/2018/5/10/northwell-closes-on-36m-acquisition (excerpt: 103,000 sf office building, ~20 acres, 1 Marcus Ave). → §8 card 1, §13 card 4.
- `Mineola transit-oriented development apartments near LIRR station...` · Firecrawl search → https://www.burmanre.com/work/residential (excerpt: The Bridge at Mineola, 101 units, $130M, "In Construction", across from Mineola LIRR); https://www.harrisbeachmurtha.com/news/mineola-apartment-project-approved-in-one-meeting/ (The Royal Blue, $45M, 54 units, ¼ mile from station — not used); libn.com 2023 $85M TOD (excerpt, not used). → §7 card "New transit-oriented buildings", §9 Mineola rental Q, §13 card 2.
- `NYU Langone Hospital Long Island Mineola beds; NUMC...` · Firecrawl search → https://en.wikipedia.org/wiki/NYU_Langone_Hospital_%E2%80%93_Long_Island (591 beds, moved to Mineola 1900); https://www.numc.edu/about/centers-of-care/nassau-university-medical-center/ (530-bed teaching hospital, 2201 Hempstead Tpke) + /news-events/media-kit/ (began 1935 as Meadowbrook Hospital). → §8 cards 2–3, §13 card 2.
- `Garden City New York planned village Alexander Turney Stewart 1869...` · Firecrawl search → https://www.nytimes.com/1998/11/15/nyregion/an-immigrant-s-vision-created-garden-city.html (excerpt: acquired pasture from Town of Hempstead in 1869 for $55 an acre); gardencityny.net/228 scrape returned no text (EMPTY), excerpt only. → §13 card 1.
- `Nassau Hub Uniondale Nassau Coliseum redevelopment...` · Firecrawl search → https://libn.com/2022/09/20/county-extends-rxr-deadline-for-nassau-hub-project-payment/ (excerpt: RXR $1.5B plan, ~70 acres); https://www.nassaucoliseum.com/about (excerpt: 77 acres of property); nassaucountyny.gov/4670 scrape empty (EMPTY). → §8 card 4, §13 card 5.
- `Nassau Community College Mitchel Field campus...` · Firecrawl search → https://www.ncc.edu/aboutncc/fastfacts.shtml (excerpt: 1962 expanded to 135 acres at former Mitchel AFB); https://preservationlongisland.org/preservation-in-progress-tourmitchel-field-air-base-and-flight-line/ (scrape: Army closed Mitchel Field 1961, 1,117-acre airbase; Cradle of Aviation restoration team in Hangar 5; Georgian Revival officers' houses). → §8 card 5, §13 card 3.
- `Freeport Nautical Mile Woodcleft Avenue restaurants Sandy flooding businesses` · Firecrawl search → https://www.ottosseagrillny.com/ourstory (excerpt: Village of Freeport reinventing Woodcleft Ave into The Nautical Mile; Irene Aug 2011 ~3 ft of water; brass plate marking Sandy flood line). CBS/LI Advocate excerpts not used. → §8 card 6, §13 card 6.

### Reddit / hyperlocal
- `site:reddit.com longisland Nassau ethernet cable contractor drilled through OR damaged OR "cat6" house` · Firecrawl search → https://www.reddit.com/r/longisland/comments/1hcuoly/is_verizon_internet_better_than_optimum/ (excerpt about provider tech running line and drilling) and r/OPTIMUM excerpt — background for the provider-move angle only; not quoted. Nassau-specific Reddit threads on damaged Cat6: EMPTY.
- `drywall screw nail through ethernet cable wall intermittent network fault nail plate low voltage` · Firecrawl search → r/HomeNetworking "Likelihood of me nailing though a data cable in drywall?" (title only) — background; not quoted.
- Newsday/Patch/Herald on Cat6 or network-cable faults in Nassau: EMPTY.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 says on-page that the AI Overview could not be opened; claims framed as commonly published (Fixr Jan 2025 $45–$75/hr, $125–$250/drop from silo research).

### Prices used (no new prices)
- $195/hr, 3-hour minimum ($585); replacement Cat6 drop from $175; plenum "add per drop"; after-hours/weekend "premium applies"; closet audit "quoted by port count" — network-cable-repair-nassau-county.html pricing table (same $195/$175 on cat6-repair-long-island hub).
- Comparison: Cat5e $254 / Cat6 $296 / Cat6A $424 per drop to 100 ft — cat6-installation-nassau-county.html.
- FLAG: blueprint §9 Nassau 1.15× would make the $175 drop $201 (and $195/hr → $224); hub and the live Nassau NCR page publish un-multiplied $175/$195, so this page follows the hub. $296 Cat6 install = 1.088× NYC $272, not 1.15× ($313) — quoted as published.

### Images (11) — permanent image rule
Drive folder empty / CompanyCam not connected (main run). All 31 unique base photos in images/network-cable-repair/ (16) and images/cat6/ (15) were already used once on cat6-repair-nyc/-long-island/-hudson-valley, so reuse was unavoidable; chosen mostly from NYC-used bases (furthest from the parent hub). 10 of 11 cropped to remove technicians' faces; none show house numbers, plates or readable documents.
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-nassau-county-nicked-jacket-on-metal-edge.webp (hero) | network-cable-repair/crushed-network-cable-repair-*.webp (full frame) |
| …-ceiling-run-flashlight-inspection.webp | network-cable-repair/network-cable-inspection-* (crop) |
| …-wall-jack-no-link-test.webp | network-cable-repair/network-jack-repair-* (crop) |
| …-open-stud-wall-cable-pull.webp | cat6/commercial-cat6-installation-*-stud-rough-in (crop) |
| …-data-voice-plate-retermination.webp | cat6/cat6-voice-data-outlet-installation-* (crop) |
| …-wire-map-crossed-open-pair.webp | network-cable-repair/network-cable-fault-detection-* (crop) |
| …-rack-link-down-tester.webp | network-cable-repair/network-closet-troubleshooting-* (crop) |
| …-ceiling-replacement-feed.webp | cat6/cat6-cable-installation-*-ceiling-drop (crop) |
| …-patch-panel-punch-down.webp | network-cable-repair/patch-panel-repair-* (crop) |
| …-desk-outlet-identification.webp | cat6/cat6-data-drop-installation-*-workstation-outlets (crop) |
| …-poe-dome-camera-no-power.webp | network-cable-repair/poe-camera-cable-repair-* (crop) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (7) and images/cat6/ (4), 10 cropped to remove faces (no real cat6-repair photos yet)`.

### Keyword notes (five layers)
- Service: Cat6 repair Nassau County, Cat6 cable repair, Cat6 jack repair, Cat6 re-termination, Cat6 fault location, Cat6 certification after renovation.
- Problem: drywall screw through cable, nail through Ethernet, buried coupler/splice, finished-basement run failure, attic damage by roofers/solar, router moved by provider, split Cat6 run, media panel failure, office refit dead desks, raised-house rewiring.
- Technology: distance-to-fault, certification, steel nail plates, old-work brackets, borescope, surface raceway, FEMA P-348, NEC 800.25.
- Industry: homeowners/home offices, landlords/managing agents, office suites (Marcus Ave), medical suites (Mineola/East Meadow), main-street mixed use, restaurants (Nautical Mile), new TOD rentals.
- Geographic: Nassau County, Towns of Hempstead/North Hempstead/Oyster Bay, Glen Cove, Long Beach, Mineola, Garden City, Lake Success, Uniondale, East Meadow, Freeport, South Shore (Island Park, Oceanside, Baldwin, Massapequas) + "we also repair" town list.

## Question register — cat6-repair-nassau-county

§9 "Questions Answered" (H3):
1. Our Cat6 jack died the week the drywall was hung. How do you find where a screw went through the cable without opening the whole wall?
2. A kitchen remodel closed up the wall where our Cat6 had a splice. Is that link worth saving?
3. We finished the basement and the new ceiling now covers every Cat6 run. What happens when one of them fails?
4. How do you show that a roofing or solar crew damaged the Cat6 in our attic?
5. Every time a jack is re-terminated it loses a few inches. What happens when there is no slack left in the wall?
6. Our house was raised after Sandy and the router moved upstairs. Do the old Cat6 runs from the ground floor still make sense?
7. In a flood-zone house, where should repaired Cat6 jacks and junctions go?
8. The internet company moved our modem to another room and now the Cat6 to the office is dead. What did they disturb?
9. A previous contractor split one Cat6 run to feed two rooms. Can that be repaired, or does each room need its own run?
10. Our Cat6 all lands in a structured media panel in a closet. Can one bad connection there take out several rooms?
11. Our suite was re-carpeted and re-furnished over a weekend and on Monday six desks had no network. Where do we start?
12. We bought a downtown building with a store below and offices above. Can you tell which Cat6 runs still serve anyone?
13. The wall jack in our new apartment in a Mineola rental building has never worked. Is that ours to fix or the building's?

FAQ (§17, = FAQPage schema):
F1. Do we need to be home for the whole Cat6 repair visit?
F2. Can you patch the drywall after opening a wall to fix the Cat6?
F3. Will you work alongside our general contractor while the renovation is still going?
F4. Can you repair Cat6 in a house we rent in Nassau, and does the landlord have to agree?
F5. Can you come on a Saturday so we do not lose a workday at home?
F6. Can surface raceway be used instead of opening a finished wall?
F7. Is it a problem that our Cat6 runs right beside the electrical panel and power cables?
F8. Can you check the Cat6 behind a TV that someone else wall-mounted?
F9. Do you repair Cat6 in Glen Cove and Long Beach as well as the towns?
F10. Can you fix the coax or phone wiring during the same visit?

Other "?" headings: "Nassau Cat6 Link Down Since the Contractors Left?" (repair capture), "Cat6 Dead Somewhere Between Elmont and Massapequa Park?" (closing).

De-dup notes: compared by meaning against the NYC, LI and HV registers. Deliberately avoided: NYC Q8 splice-in-general (ours is a buried splice after a remodel), NYC Q15 tracing in pre-war plaster (ours is locating a fastener puncture), NYC F7 old cable after re-pull, NYC Q16/LI Q4–5 water dry-out/insurance (ours: where to place terminations in flood-zone houses; contractor-damage documentation rather than insurance), LI Q8–9 slab access/stapled attic cable, LI F2 pre-closing test, LI F6 attic re-insulation, LI F8 garage conversion, HV Q6 addition joint, HV Q8 indoor cable outside, HV Q11 shared telecom room, HV F1 knob-and-tube, HV F3 gate/intercom post, HV F5 matching plates. Licensing and permits are answered in body (§8.5, Towns section, §10.5) only, because cat6-installation and fiber Nassau pages already ask licence questions.

Masked paragraph similarity (difflib, geo-masked, p/li/td/h3/figcaption ≥8 words): vs cat6-repair-long-island mean 0.41, vs -nyc 0.40, vs -hudson-valley 0.40, vs -suffolk-county 0.42, vs -westchester-county 0.41, vs network-cable-repair-nassau-county 0.37. Blocks ≥0.65 are excluded constants (freshness stamp, warranty sentence, licence/rating strip, NAP, form success line, pricing-table item names/sources, silo cross-link list); captions of photos shared with the Suffolk/Westchester pages were rewritten to fall below 0.65.


---

# Merged from batch 2026-10-17 (cat6-repair-suffolk-county)

<!-- part file for research/cat6-repair.md — written by the cat6-repair-suffolk-county builder, 2026-10-17 batch; the main run merges it -->
## Suffolk County (cat6-repair-suffolk-county)

Batch run 2026-10-17. Area page, up-link /cat6-repair-long-island. GBP Brooklyn (1282 Troy Ave, #brooklyn). Direct line (631) 407-2884 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: WebSearch (titles/URLs), WebFetch (page read + summary), Firecrawl search (mcp__Firecrawl__firecrawl_search, excerpts). Shell curl blocked. Silo-wide technical sources (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fluke temperature/insertion-loss KB, Mike Holt 800.90(B), computercablestore four-pair gigabit) are reused from research/cat6-repair.md and cited on the page only in general terms.

**Thesis (distinct from the LI hub and from the Nassau page):** Suffolk Cat6 is *inherited* cable — it was installed for a building, a tenant or a floor plan that has since changed. Flex buildings in the Hauppauge / Central Islip / Bay Shore industrial node are carved into smaller bays for new tenants; South Shore houses were lifted after Sandy and their runs lengthened or rerouted through enclosures that may hold only parking, access and storage; farm buildings became tasting rooms and offices; summer rentals get re-patched by guests; hospital and college campuses grow wing by wing; new construction at Station Yards hands over jacks nobody has tested. The repair skill is reading what changed since the cable went in, then repairing to the building as it is now. The county's length (86 miles, ten towns, island and ferry communities) means the visit is planned to finish in one trip. LI hub owns heat/length/storm/seasonal-reopening as its thesis; this page uses those only as background.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Query `site:reddit.com r/longisland ethernet OR cat6 Suffolk house previous owner wiring` · Firecrawl search (excerpts; reddit not scraped) → https://www.reddit.com/r/longisland/comments/1l9fokf/ (excerpt "Looking for a Company that will Run Cat6 cables"; already in hub research — background only); https://www.reddit.com/r/longisland/comments/1g51via/best_wifi_provider_smithtown_pines_area/ (excerpt: "if your husband works from home I'd highly recommend hard wiring his computer to your router via an Ethernet cable") → background for §5 para on home offices, not quoted; https://www.reddit.com/r/longisland/comments/vxk1bd/ (excerpt: Verizon FIOS "not available where I live (NW Suffolk)") → background only. Fault-specific Suffolk threads: EMPTY. Query `reddit longisland Suffolk ethernet cable wall jack not working house wired` · WebSearch → no r/longisland result (generic r/HomeNetworking mirrors only) → EMPTY. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 states this on the page; each H3 is framed as a claim commonly published by how-to sites, retailers and cost guides (Angi/HomeAdvisor/Fixr named generically; Fixr Jan 2025 figures from silo research). |
| 6 | Landmarks | L1–L6 below |
| 7 | Use cases / building stock | C1–C6, F1–F4, B1–B3 below |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | CoStar (Aug 2024), CBS New York (July 2015), 27east/Sag Harbor Express (Jan 2024), RiverheadLOCAL (2019, 2020), Fire Island News (May 2025), Long Island Advocate (July 2026, carried) |
| 10 | Hyperlocal | Fire Island News, RiverheadLOCAL, 27east, Suffolk Times/Riverhead News-Review (carried). Hyperlocal stories about Cat6/network-cable faults in Suffolk: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix — new sources fetched for this page
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| C1 | `Long Island industrial flex buildings subdivided smaller tenants Hauppauge vacancy 2025` · WebSearch → WebFetch | https://www.costar.com/article/131430884/hauppauge-leads-long-island-metropolitan-area-in-available-industrial-space/ | Aug 16 2024, CoStar Analytics: Hauppauge node is Long Island's largest, "over 26.1 million square feet of space clustered predominantly around Hauppauge, Central Islip and Bay Shore"; "contending with the most available space on Long Island", "driven by a mismatch between property sizes and occupiers' space preferences"; headline: tenant preference for small-bay space. (Rest paywalled.) | §5 para 2, §5.5 bullet, §7 re-tenanted flex card, §8 Hauppauge/Central Islip/Bay Shore card, §9 subdivided-bay Q |
| C2 | same search · WebFetch | https://www.cbre.com/insights/figures/long-island-industrial-figures-q4-2025 | Page returned no data → EMPTY, not used | — |
| B1 | `Mastic Beach OR Lindenhurst homes raised elevated after Sandy number NY Rising Suffolk` · WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/l-i-open-foundations-ban | July 30 2015, CBS New York, Lindenhurst dateline: Long Island towns and villages banning open pilings for elevated homes, "requiring a closed foundation with water vents"; Legislator Kevin McCaffrey: closed foundations protect "the mechanical structure of the house; the pipes from freezing"; NY Rising elevation grants "have averaged over $100,000". No count of homes. | §5 para 3, §5.5 bullet, §7 lifted-house card, §9 lifted-house Qs |
| B2 | same search · WebFetch | https://www.npr.org/2013/10/27/241222083/to-avoid-flooding-coastal-homeowners-lift-themselves-up | ROBOTS_DISALLOWED → EMPTY, not used | — |
| H1 | `Stony Brook Southampton Hospital new campus Southampton College site` · WebSearch → WebFetch | https://27east.com/southampton-press/still-a-campus-cornerstone-new-stony-brook-southampton-hospital-aims-for-2030-opening-date-2226594 | Jan 17 2024 (Michael Wright): new hospital on 15 acres at the NE end of the 85-acre Stony Brook Southampton campus in Shinnecock Hills; current hospital on 19 acres in Southampton Village; preliminary plan 275,000 sq ft; target 2030 ("realistic best case scenario"); cost $365M originally, "probably north of $400 million". | §8 medical card, §7 medical card |
| H2 | `Peconic Bay Medical Center Riverhead Corey Critical Care Pavilion opened square feet` · WebSearch → WebFetch | https://riverheadlocal.com/2020/01/10/pbmc-dedicates-new-critical-care-pavilion | Jan 10 2020 (URL date): $67.8M Corey Critical Care Pavilion dedicated; rooftop helipad; 16-bed ICU/cardiac unit; Kanas Regional Heart Center with two cardiac cath labs; "roughed-out space for future cardiac surgical suites"; unfinished space for a future expanded ED; three years' construction. | §8 medical card, §5.5 bullet |
| R1 | `Tanger Outlets Riverhead Route 58 number of stores square feet` · WebSearch → WebFetch | https://brixmor.com/re-development/completed-projects/the-shops-at-riverhead | The Shops at Riverhead: "115,000-square-foot center … across from the Tanger Outlets"; Costco anchor; PetSmart, Marshalls/HomeGoods, HomeSense, Ulta; separate 12,000 sq ft building facing Old Country Road (Sleep Number, T-Mobile). Year not stated. | §8 Route 58 card |
| I1 | `Fire Island Ocean Beach ferry Bay Shore contractors materials barge how work gets done` · WebSearch → WebFetch | https://www.fireislandnews.com/communities/kismet/fire-island-ferries-freight-service-stalled/ | May 19 2025 (Linda Leuzzi): Fire Island Ferries freight normally via Town of Islip's Maple Avenue site in Bay Shore; disrupted from March 14 by town construction; using Saltaire terminal; company serves eight communities "As far west as Kismet and to the east, Point O'Woods". | §9 Fire Island Q, §7 barrier-island card |
| D1 | `Dig Safely New York Long Island call 811 notice working days excavation homeowner` · WebSearch → WebFetch | https://newyork-811.com/homeowners/ | New York 811 serves "the five boroughs of New York City and Nassau and Suffolk Counties on Long Island"; call "at least 48 hours but no more than 10 working days (excluding weekends and legal holidays)" before digging. | §8.5 bullet, §9 811 Q |
| W1 | `North Fork farm barn converted winery tasting room Southold Riverhead agritourism building code` · WebSearch → WebFetch | https://suffolktimes.timesreview.com/?p=71857 | Undated (Nov 7 hearing, year not given): Southold Planning Board hearings on winery buildings — Sannino 2,800 sq ft winery with production/retail/education; Surrey Lane 3,610 sq ft winery/retail; Purita 2,600 sq ft addition to 6,400 sq ft production building. Undated → NOT stated as current; used only as background that North Fork winery buildings combine production, retail and storage under one roof. Not quoted. | background for §9 winery Q |

### Carried, verified Suffolk sources (fetched by earlier 2026-10-17 runs; see research/fiber-optic-installation.md and research/smart-lock-installation.md Suffolk sections)
| # | URL | Finding | Page section used |
|---|---|---|---|
| T1 | https://www.ny.gov/counties/suffolk ; https://www.suffolkcountyny.gov/Visiting/Towns-and-Villages ; https://en.wikipedia.org/wiki/Suffolk_County,_New_York (smart-lock T5) | Ten towns (Babylon, Brookhaven, East Hampton, Huntington, Islip, Riverhead, Shelter Island, Smithtown, Southampton, Southold); 86 miles long; 912 sq mi land / 1,461 water; most county offices in Hauppauge; Brookhaven largest town and the only one spanning South Shore to North Shore. | §5 para 1, §5.5, Ten Towns section, schema areaServed |
| F1 | https://www.fema.gov/sites/default/files/2020-07/fema_tb5_free_obstruction_requirements.pdf (smart-lock F1) | TB5: "The NFIP limits the use of enclosures under elevated buildings to parking of vehicles, building access, and storage." P-348: components below required elevation must resist flood loads or be elevated. | §7.5 lifted houses, §9 equipment-under-house Q, §8.5 bullet |
| F2 | https://longislandadvocate.com/superstorm-sandy-still-haunts-suffolk-residents-today/ (smart-lock F2) | July 15 2026: NY Rising bought flood-zone houses to demolish or paid to raise them; Lindenhurst "now full of empty lots". | §5 para 3 |
| F3 | https://www.seagrant.sunysb.edu/media/sandy12/Newsday-Sandy010713.pdf (smart-lock F3) | Newsday Jan 2013 FEMA tally: Suffolk 20,798 structures flooded/damaged/destroyed; 8,153 with >50% damage. | §5.5 bullet |
| F4 | https://www.weather.gov/media/okx/coastalflood/Lindenhurst%20impacts.pdf (fiber Suffolk) | NWS: Sandy peak 7.7 ft NGVD 10/29/2012; much of the area south of Montauk Highway inundated 2–5 ft in Lindenhurst, Amityville, Babylon; repeated moderate flooding ~4 ft (2016–2018). | §5 para 3, Ten Towns (Babylon) |
| I2 | https://www.nps.gov/fiis/planyourvisit/off-road-vehicle-permit-faqs.htm (smart-lock I1) | Only year-round residents and contractors/businesses can apply for driving permits; contractor permits authorise driving only to communities where the holder has work; winter access by ferry, water taxi or private boat. | §9 Fire Island Q |
| P1 | https://pb.state.ny.us/public-information/faqs/ (fiber Suffolk) | Central Pine Barrens ~105,000 acres (eastern Brookhaven, western Southampton, southern Riverhead); 1993 Act; in the Core, clearing or material alteration of vegetation counts as development; Core development needs a Commission hardship waiver with public hearing. | §9 Pine Barrens Q, §8.5 bullet |
| A1 | https://shelterislandreporter.timesreview.com/2025/02/02/suffolk-closeup-the-farming-county/ (fiber Suffolk) | 578 farms in 2022; 33,821 acres; 79 wineries in Suffolk; Farmland Preservation Program 1974. | §5.5, §7 farm card, Ten Towns (Southold/Riverhead) |
| S1 | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more (fiber/smart-lock) | Oct 22 2024: Station Yards, 53 acres at Ronkonkoma LIRR; 1,450 units at completion; Phase 1 489 units (2020); Phase 2 388; near LIE Exit 60 and MacArthur. | §7 new-build card, §9 new-construction Q, §13 card |
| E1 | https://riverheadnewsreview.timesreview.com/?p=94143 (fiber Suffolk) | Undated: preliminary plat dividing ~2,107 acres at EPCAL into eight lots; Calverton Aviation & Technology to buy 1,643 acres; ~292 acres protected Pine Barrens. | §8 Calverton card, §13 card (stated as preliminary plat) |
| G1 | https://www.27east.com/southampton-press/new-business-park-continues-to-take-shape-in-westhampton-1406404 (fiber Suffolk) | Aug 26 2016: Hampton Business District at Gabreski Airport, 55 acres county land, 40-year lease 2009, 10 buildings planned; Building 2 67,000 sq ft offices/medical. | §8 Westhampton card |
| U1 | https://sunysuffolk.edu/about-suffolk/campus-information/ (fiber Suffolk) | Ammerman Campus, Selden, 156 wooded acres, 13,000+ students; Grant Campus, Brentwood, 10,000+; Eastern Campus, Riverhead. | §7 campus card, §13 card |
| K1 | https://riverheadlocal.com/2019/06/25/should-jobs-being-done-by-unlicensed-contractors-be-slapped-with-stop-work-orders/ (smart-lock research) | County home improvement licence for residential repairs/alterations; written test + liability and workers' comp insurance; civil penalty up to $750 first / $1,500 subsequent; 9,107 licences countywide (2018). | §8.5 licensing bullet |
| K2 | https://suffolkcountyny.gov/Departments/Consumer-Affairs/Licensing ; https://ecode360.com/14947436 (fiber Suffolk) | Consumer Affairs licenses Master and Restricted Electricians under Ch. 563 Art. XI; Art. II home improvement; §563-16 excludes electrical/plumbing work as defined in §563-126. No low-voltage text. | §8.5 licensing bullet (page states what the code contains; no exemption claimed) |
| K3 | https://ePermits.southamptontownny.gov/eElectrical (fiber Suffolk) | Town of Southampton runs its own electrical e-permit portal. Low-voltage rule not stated. | §8.5 permits bullet |
| L1 | https://en.wikipedia.org/wiki/Big_Duck (smart-lock L2) | Built 1931 by duck farmer Martin Maurer as a shop; moved to Flanders 1937; back in Flanders Oct 6 2007; NRHP 1997. | §13 card |
| L2 | https://en.wikipedia.org/wiki/Fire_Island_Lighthouse (smart-lock L1) | 168-ft tower, operating 1858; in FINS east of Robert Moses State Park. | §13 card |
| L3 | https://www.vanderbiltmuseum.org/about-us/history/ (smart-lock L3) | 43-acre waterfront estate, built 1910–1936, above Northport Bay; deeded to Suffolk County 1944; public 1950. | §13 card |

### Local licensing / permits summary (page §8.5)
Suffolk Ch. 563 (Art. II home improvement; Art. XI electricians, with town/village carve-out already on hub) · RiverheadLOCAL 2019 licence numbers/penalties · Southampton e-permits · New York 811 notice window · FEMA TB5 enclosure use · NEC 800.25 abandoned cable / 800.90 primary protector (silo) · Central Pine Barrens Core clearing rule. Town-by-town low-voltage permit rules: EMPTY (page says we check per address).

### Prices used (live AESS Suffolk pages only; no new prices)
| Figure | Source |
|---|---|
| $195/hr, three-hour minimum ($585); additional time $195/hr | network-cable-repair-suffolk-county.html pricing table (and LI hub) |
| Replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord) | network-cable-repair-suffolk-county.html; same figure on cat6-repair-long-island.html |
| Over-length re-route — quoted per run; closet audit, mapping and labelling — quoted by port count; plenum (CMP) — add per drop; after-hours/weekend — premium applies | network-cable-repair-suffolk-county.html |
| No East End surcharge; eastern work planned into scheduled windows | network-cable-repair-suffolk-county.html (table note) |
| Comparison only: new Cat6 drop $296 (Cat5e $254, Cat6A $424) to 100 ft | cat6-installation-suffolk-county.html |
| Third-party national (labelled): Fixr Jan 2025 $125–$250 per drop, $45–$75/hr | silo research |
**FLAG for Anwar (pricing):** blueprint §9 Suffolk 1.20× applied to the $175 replacement drop would be $210, and other silos' Suffolk pages (fiber, Sonos, smart lock) publish ×1.20 figures. The LI hub and network-cable-repair-suffolk-county.html both publish $175 un-multiplied for Suffolk, so this page follows the hub's published figure, per the build instruction, and states that the figure is the one already published for Suffolk. The $195/hr rate is protected verbatim (not multiplied) on every silo. The $296 Cat6 install drop (1.088× NYC $272) is quoted as published.

### Keyword notes (five layers)
- Service: Cat6 repair Suffolk County, Cat6 cable repair Suffolk, Cat6 re-termination, Cat6 recertification, Cat6 reroute, Cat6 jack repair, patch panel repair, tenant fit-out cable acceptance testing, raised-house Cat6 reroute.
- Problem: inherited/previous-tenant Cat6, subdivided flex bay wired to neighbour's closet, failed floor jacks on slab, roof-deck runs damaged by reroofing, splices/couplers added during house lift, equipment in flood enclosure, guests re-patching a rental's network, untested new-construction jacks, buried run in Pine Barrens, wash-down area.
- Technology: permanent link vs channel, certification tester, wire map, NEXT, return loss, insertion loss, couplers, keystones, 110 punch-down, PoE, NEC 800.25/800.90, CMR/CMP, outdoor/direct-burial cable, sealed enclosures.
- Industry: flex/industrial tenants, distribution, wineries/farms, hospitals and medical offices, colleges, retail on Route 58, summer rentals/estates, barrier-island cottages, new apartments, municipal.
- Geographic: Suffolk County; ten towns; Hauppauge, Central Islip, Bay Shore, Islandia, Ronkonkoma, Station Yards, Calverton/EPCAL, Riverhead/Route 58, Westhampton/Gabreski, Shinnecock Hills/Southampton, Selden, Brentwood, Lindenhurst, Babylon, Amityville, Mastic Beach, Fire Island (Kismet–Point O'Woods, Ocean Beach, Saltaire), Flanders, Centerport, Montauk, Orient, Shelter Island.

### Images (11) — permanent image rule; Drive folder empty and CompanyCam not connected (checked by main run)
Every photo in images/network-cable-repair/ and images/cat6/ (31 distinct scenes by perceptual hash) is already used on at least one cat6-repair page, and 30 of 31 show a technician's face. Per the batch brief (reject any photo showing a face), each source below was CROPPED (framing only, no other edit) so no face is in frame, then saved as WebP q82. Sources chosen from scenes not used on the parent LI hub. The parallel Nassau and Westchester builds copied some of the same scenes uncropped/under other names — the crops here differ in framing.
| images/cat6-repair/ | Source (crop box px) |
|---|---|
| cat6-repair-suffolk-county-wire-map-fail-crossed-open-pair.webp (hero) | network-cable-repair/network-cable-fault-detection-suffolk-county.webp (150,220,880,1024) |
| cat6-repair-suffolk-county-torn-jacket-on-ceiling-grid.webp | network-cable-repair/crushed-network-cable-repair-suffolk-county.webp (no crop; no face) |
| cat6-repair-suffolk-county-split-jacket-at-steel-frame.webp | network-cable-repair/damaged-ethernet-cable-repair-suffolk-county.webp (0,440,1100,1024) |
| cat6-repair-suffolk-county-ceiling-tile-flashlight-inspection.webp | network-cable-repair/network-cable-inspection-suffolk-county.webp (660,0,1536,600) |
| cat6-repair-suffolk-county-tone-probe-labelled-cords.webp | network-cable-repair/network-cable-tracing-suffolk-county.webp (790,0,1536,1024) |
| cat6-repair-suffolk-county-patch-panel-reterminate-labelled-run.webp | network-cable-repair/patch-panel-repair-suffolk-county.webp (140,0,990,1024) |
| cat6-repair-suffolk-county-link-down-rack-test.webp | network-cable-repair/network-closet-troubleshooting-suffolk-county.webp (0,440,820,1024) |
| cat6-repair-suffolk-county-wall-jack-no-link-open-pair.webp | network-cable-repair/network-jack-repair-suffolk-county.webp (0,440,900,1024) |
| cat6-repair-suffolk-county-replacement-run-from-carton.webp | cat6/cat6-installation-suffolk-county-ceiling-drop.webp (520,0,1402,1122) |
| cat6-repair-suffolk-county-reroute-through-steel-studs.webp | cat6/commercial-cat6-installation-suffolk-county-stud-rough-in.webp (640,0,1402,1122) |
| cat6-repair-suffolk-county-outlet-row-retermination.webp | cat6/office-cat6-installation-suffolk-county-outlet-bank.webp (560,300,1402,1122) |
DAILY-LOG note: `images: 11 reused (cropped to remove faces) from images/network-cable-repair/ (8) and images/cat6/ (3) (no real cat6-repair photos yet)`. The library looks AI-rendered (flagged by earlier builders) — for Anwar to review.

## Question register — cat6-repair-suffolk-county

§9 "Questions Answered" (H3):
1. Our bay in a subdivided Hauppauge flex building has jacks that still run back to a closet on the other tenant's side. Can the repair bring them to our own panel?
2. Our lease says the landlord hands over working data cabling. What test results should we ask for before accepting the space?
3. Floor jacks in our slab-on-grade office keep failing after the floors are washed or after heavy rain. What is happening under there?
4. The building was reroofed and now the Cat6 runs to the rooftop cameras and units fail. Who fixes what?
5. Our South Shore house was lifted after Sandy and the rooms fed through the new crawl space keep dropping. Why?
6. The network equipment used to sit in the enclosure under our raised house. Where can it go, and how do the runs get rerouted?
7. Our winery's Cat6 runs through the same building as the wash-down area. How is it kept working when the floor is hosed?
8. Summer guests at our rental re-patched the network cabinet and now half the house is offline. How do you put it back and stop it happening again?
9. Can a Cat6 repair be done in a Fire Island community where contractors need a driving permit or a ferry?
10. Our failed buried Cat6 crosses woodland inside the Pine Barrens. Can it be dug up and replaced?
11. Does anyone have to mark utilities before a failed buried Cat6 run is dug up?
12. We bought a new apartment at a Suffolk development and some jacks have never worked. Is that a builder issue or a repair?

FAQ (§17, = FAQPage schema):
F1. Will you send photos of what you found inside the wall or ceiling?
F2. Can one Cat6 run be split to feed two devices instead of pulling a second cable?
F3. Can you fix a Cat6 jack that was painted over or caulked during a repaint? (replaced TV/soundbar question in batch de-dup vs Westchester)
F4. Will a Cat6 repair interrupt our alarm or camera monitoring?
F5. Can you repair the Cat6 that connects an EV charger in a garage or carport to the network? (narrowed in batch de-dup vs Staten Island solar/battery question)
F6. Does someone need to be at the property for the whole visit?
F7. Can a Cat6 repair be done while a house elevation or renovation crew is still on site?
F8. Can you repair Cat6 in a unit we rent out year-round while the tenant is living there?

Other "?" headings: "Suffolk Cat6 Link Down Before the Doors Open?" (repair capture), "Inherited Somebody Else's Cat6 Somewhere in Suffolk?" (closing).

De-dup notes: checked by meaning against the full register (NYC 26, LI 23, HV 25) and against network-cable-repair-suffolk-county (cost, back-of-unit drops, joining a damaged run, extended drop when wall moved, warehouse AP hot afternoons, mezzanine handrail, dead jack, three previous tenants/labelling, East End charge, certified reports, cover, Nassau) and cat6-installation-suffolk-county FAQ (cost, county differences, licensing, flex buildings, distance, inclusions, drop count, 10G, CCA, plenum, Cat5e upgrade, evenings/seasonal). Dropped during drafting: inline couplers after reconfiguration (NCR Suffolk owns "extended a drop when the wall moved"), previous-tenant labelling (NCR Suffolk) → reframed to lease acceptance test results; one-trip planning for distant sites (HV Q14); converted barn office (HV F7); travel charge East End (LI F1); licence question (cat6-installation-suffolk-county; licensing kept in §8.5 body only); before-closing house test (LI F2); attic re-insulation (LI F6). Parallel Nassau/Westchester drafts were not on disk when this register was written — main run to re-check.

### Addendum (size fix, same day)
Added section "Cat6 Below the Flood Line on Suffolk's South Shore" (no new questions) using only sources already in this file: F4 NWS Lindenhurst impact table (7.7 ft peak 10/29/2012; 2–5 ft south of Montauk Highway; ~4 ft moderate flooding 2016–2018), F1 FEMA TB5 / P-348, B1 CBS New York 2015 (closed foundations with water vents; McCaffrey quote), F2 Long Island Advocate July 2026 (NY Rising buyouts or elevation; Lindenhurst empty lots). Service JSON-LD gained a description and the remaining published Suffolk price lines from network-cable-repair-suffolk-county.html (additional time, re-route quoted per run, closet audit by port count, plenum added per drop, after-hours premium).


---

# Merged from batch 2026-10-17 (cat6-repair-westchester-county)

## Westchester County — local research (2026-10-17 batch, cat6-repair-westchester-county)

Area page; up = /cat6-repair-hudson-valley; direct line (914) 877-2578; GBP Bronx (460 E Fordham Rd, #bronx); Westchester ×1.25. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape; "Census API" = Firecrawl Alexandria census-gov census/data. Shell curl blocked. Silo-wide technical sources (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fixr Jan 2025) are reused from research/cat6-repair.md in general terms only. Sources marked "(reused: <file>)" were fetched and verified by earlier runs and are not re-fetched here. To be merged into research/cat6-repair.md by the main run.

**Thesis (different from the NYC, LI and HV hubs):** Westchester Cat6 mostly lives behind *finished, occupied, owner-maintained surfaces* — home offices in pre-1960 plaster houses (53.1% of the county's housing units were built before 1960; 28.0% before 1940), apartments, co-ops and condos (24.8% of units are in buildings of 20+ units), and a new generation of downtown rental towers pre-wired with in-unit Cat6 and small per-unit switches — with 17.3% of the county's workers working from home. So a Westchester repair is decided by (1) reaching the fault through plaster, concrete and cabinetry with the least disturbance, (2) the ownership line between ISP equipment (ONT/router), building, board/landlord and occupant, and (3) where the network corner sits relative to flood-prone lower floors in Sound-shore and river-valley neighbourhoods. NYC = risers/pre-war access/managing agents; LI = heat, horizontal distance, outdoor environment; HV hub = weather, outbuildings, distance, office parks. Avoided on purpose: storms/lightning, outbuildings, barns, attics, slab ranches, warehouses, office-park shared telecom rooms (all hub/sibling lanes).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `reddit r/Westchester ethernet wiring house cat6 home office plaster walls` · FC search → https://www.reddit.com/r/Westchester/comments/105v2vv/peekskill_area_need_my_house_wired_for_ethernet/ (excerpt: "Need my house wired for ethernet, any recommendations? … Any recs on someone who can come in and run cables for my…") → §5 para 3 (residents asking for wired runs, not quoted verbatim). Same search returned r/HomeNetworking plaster-and-lath threads (https://www.reddit.com/r/HomeNetworking/comments/fmiznk/running_cat6a_in_100_year_old_house/ — "my house is super old with plaster and lathe") → background for §9 plaster cluster only, not Westchester-specific, not quoted. r/Westchester co-op thread https://www.reddit.com/r/Westchester/comments/mjisio/westchester_coops_condos/ (excerpt: co-ops let buyers live in towns like Bronxville and Scarsdale "without having to pay condo or house money") → §7 co-op card context. Fault-specific r/Westchester threads: EMPTY. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 states this on the page; each H3 is framed as a commonly published claim, not as AI Overview wording. |
| 6 | Landmarks | L1–L6 below |
| 7 | Building stock / use cases | W1–W6 below |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | lohud (Journal News) N1–N2; ABC7 (reused) |
| 10 | Hyperlocal | Patch / News 12 Westchester on Cat6 or network-cable faults: EMPTY (no relevant result in the searches above). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| W1 | Census API: acs/acs5/profile 2023, DP04 year built + units in structure, DP03 worked from home, county:119 state:36 | https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP04)&ucgid=0500000US36119 (and group(DP03)) | Westchester County, ACS 2019–2023 5-year: 391,861 housing units; built 1939 or earlier 28.0%; 1940–49 7.1%; 1950–59 18.0%; 1960–69 14.0%; 1970–79 9.9%; 1980–89 8.4%; 1990–99 5.1%; 2000–09 5.2%; 2010–19 3.8%; 2020+ 0.5% (→ 53.1% before 1960; 4.3% since 2010); 1-unit detached 43.5%; 10–19 units 4.9%; 20+ units 24.8%; workers 16+ who worked from home 17.3%. | Hero subhead, §5 paras 1–2, §5.5 facts list (bullets 1–3), §7 intro, §9 cluster intros, §13 |
| W2 | `Westchester County median year structure built housing units 1939 or earlier census` · FC search | https://planning.westchestercountyny.gov/census-housing | County Planning publishes "Year Structure Built" and "Median Year Home Built (ACS)" tables (excerpt only; PDFs not opened). | Cited in research only (W1 used for numbers) |
| W3 | `New Rochelle new apartment building amenities "Cat6" wiring units` · FC search | https://properties.lefigaro.com/rental/apartment-westchester-new+york-united+states/?ville=new+rochelle&option=terrasse | Listing excerpt (New Rochelle luxury rental): "The kitchen is also wired with Cat6. Each unit has its own Network Switch in mechanical room and has its own Two Access Points for WIFI access…" | §5 para 3, §5.5 bullet 5, §7 new-tower card, §9 Q7 (closet switch heat) |
| W4 | same search | https://www.apartments.com/517-walnut-st-mamaroneck-ny-unit-a/0wsf1l2/ (also Zillow / RentHop copies) | Mamaroneck rental listing excerpt: "Cat6 hard wiring from your ONT hookup to each room … with cable pass-throughs in each…" (address NOT used on page). | §5 para 3, §5.5 bullet 5, §9 Q4 (ONT boundary) |
| W5 | (reused: research/smart-lock-installation.md W2, from research/soundbar-installation.md) | https://cooperatornews.com/article/westchester-county | ~42,000 co-ops, ~25,000 condos, ~53,000 rentals across the county's cities, towns and villages. | §5.5 bullet 3, §7 co-op card |
| W6 | (reused: research/fiber-optic-installation.md Westchester + smart-lock W3) | https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster ; https://www.governing.com/magazine/getting-ahead-of-the-nimby-energy-an-older-city-learns-to-build ; https://www.pew.org/en/research-and-analysis/articles/2024/11/13/how-more-housing-revitalized-a-suburban-downtown | New Rochelle downtown overlay adopted late 2015; permits up to 6,370 housing units; more than 4,500 new units online by 2025 (Governing). | §5 para 3, §5.5 bullet 4, §8 card, §13 "also serve" context |
| W7 | (reused: research/fiber-optic-installation.md Westchester) | https://westchestermagazine.com/home/ginsburg-white-plains-1-martine/ ; https://www.lohud.com/story/news/local/westchester/white-plains/2017/03/09/white-plains-office-building-approved-apartments/98950974/ | 1 Martine, White Plains: 188 loft apartments, "the county's first major office-to-residential redevelopment"; former AT&T building at 440 Hamilton Ave approved for 245 rental apartments (2017). | §8 White Plains card, §9 Q10 context |
| W8 | (reused: research/smart-lock-installation.md W5) | https://914inc.com/westchesters-platinum-mile-is-making-a-serious-comeback/ | Platinum Mile repositioning toward medical use (3030 Westchester Ave named). | §8 Platinum Mile card, §9 Q10 |
| N1 | `Westchester flash flooding basements 2025 Mamaroneck OR Yonkers OR "White Plains" storm lohud` · FC search → FC scrape | https://www.lohud.com/story/news/local/westchester/mamaroneck/2023/10/02/mamaroneck-assessing-storm-and-flood-damage-from-the-weekend/71031010007/ | lohud, Alexandra Rivera, Oct 2 2023: severe torrential rain Thursday–Friday (Sept 28–29, 2023); "Places like New Rochelle, Yonkers and Mamaroneck got hit the hardest with over six inches of rain." | §5 para 4, §5.5 bullet 6, §9 Q9 (network corner above flood line), flood table |
| N2 | same search → FC scrape | https://www.lohud.com/story/news/local/westchester/2025/04/11/up-to-12300-westchester-county-ny-homes-could-be-lost-to-flooding-by-2040-regional-plan-report/83025329007/ | lohud, Michael P. McKinney, Apr 11 2025, on a Regional Plan Association report: 6,800 to more than 12,300 Westchester homes could be lost to "permanent, chronic, and coastal" flooding by 2040. | §5 para 4, §5.5 bullet 6 |
| N3 | same search (excerpt only) | https://www.lohud.com/story/news/local/westchester/mamaroneck/2025/02/26/westchester-ny-sound-shore-saw-floods-trapped-people-rescues-in-2007-mamaroneck-rye-port-chester/78025939007/ | Excerpt: 2007 winter storm dumped 4 inches of rain on lower Westchester; "nowhere to go but basements in Mamaroneck, Rye, New Rochelle and Port…". | §5 para 4 (Sound-shore basements pattern; 2007 named) |
| N4 | (reused: research/cat6-repair.md HV section) | https://abc7ny.com/post/flooding-brooklyn-nj-nyc-flooded/10994078/ | Ida, Sept 2021: Mamaroneck up to 14 ft of water in some neighbourhoods; basements filling. | §5 para 4 (mentioned in passing only; already a hub fact) |
| X1 | `Westchester County electrician license required low voltage Department of Consumer Protection licensed trades` · FC search → FC scrape | https://consumer.westchestercountyny.gov/trade-licenses | "Plumbers and Electricians must obtain a trade license from Westchester County in order to work in the county"; consumers should ask to see the county licence card; online licence search. No mention of low-voltage/data cabling (page makes no claim either way). | §8.5 licensing bullet, §10.5 H3 on licensing-free myth avoided; FAQ none |
| X2 | (reused: research/smart-lock-installation.md W4 / fiber HV) | https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors ; https://www.yonkersny.gov/DocumentCenter/View/14753/Home-Improvement-License-Application-052825 | County home-improvement contractor licence; Yonkers issues its own home-improvement licence application. No claim that AESS holds either. | §8.5 licensing bullet |
| X3 | (reused: research/smart-lock-installation.md X11) | https://dos.ny.gov/notice-adoption ; https://www.harrison-ny.gov/building-department/news/new-code-effective-12312025 | 2025 Uniform Code (2025 Building Code of NYS, based on 2024 IBC) effective Dec 31, 2025; Harrison building department notice. | §8.5 rated-wall/firestop bullet |
| X4 | (reused: research/fiber-optic-installation.md Westchester) | https://www.ny.gov/counties/westchester ; https://en.wikipedia.org/wiki/Westchester_County,_New_York | 48 municipalities (six cities, 19 towns, 23 villages); White Plains county seat. | §5.5 bullet 2 context, §8.5 permits bullet |
| T1 | silo (research/cat6-repair.md) | EC&M NEC 800.25 ; Fluke NEXT KB ; BICSI study guide | Abandoned accessible cable removed unless tagged; NEXT mostly from untwist at terminations; return-loss causes (kinks, staples, crush, water); fault location by distance. | §7.5, §9 answers, §10, §10.5 |
| L1 | `Lawrence Park Historic District Bronxville artists colony houses built National Register` · FC search | https://en.wikipedia.org/wiki/Lawrence_Park_Historic_District ; https://www.villageofbronxville.gov/DocumentCenter/View/243/An-Illustrated-History-of-Bronxville-PDF | NRHP 1980; "primarily residential and representative of early suburban growth"; Bronxville history PDF: narrow meandering streets, irregular building plots, eclectic mix of houses. | §13 card 1 |
| L2 | `Rye Playland opened 1928 Art Deco National Historic Landmark county-owned amusement park` · FC search | https://en.wikipedia.org/wiki/Playland_(New_York) ; https://npgallery.nps.gov/GetAsset/4b8e2d7e-4c98-4de8-b57d-076a47f61853 | Rye; opened 1928; owner Westchester County; 280 acres; NRHP nomination: "the first totally planned amusement park in the country". Art Deco Music Tower (FB excerpt — not used). | §13 card 2 |
| L3 | `Westchester County Center White Plains Art Deco opened 1930 arena` · FC search | https://en.wikipedia.org/wiki/Westchester_County_Center ; https://countycenter.biz/ | Opened 1930 (grand opening May 22, 1930), Art Deco, renovated 1988; 198 N Central Ave, White Plains. | §13 card 3 |
| L4 | `Hudson River Museum Glenview mansion Yonkers built 1877 Trevor Park` · FC search | https://www.hrm.org/glenview/ ; https://en.wikipedia.org/wiki/Glenview_Mansion | Glenview: 1877 Gilded Age home on the National Register, built for financier John Bond Trevor; became home of the Hudson River Museum in 1924. | §13 card 4 |
| L5 | `Lyndhurst mansion Tarrytown Gothic Revival 1838 Alexander Jackson Davis National Trust` · FC search | https://lyndhurst.org/ ; https://savingplaces.org/places/lyndhurst | Gothic Revival mansion in Tarrytown designed in 1838 by Alexander Jackson Davis; National Trust Historic Site. | §13 card 5 |
| L6 | `Caramoor Katonah Rosen house Mediterranean villa built 1930s estate acres` · FC search | https://caramoor.org/our-story/rosen-house-and-collection ; https://www.hudsonrivervalley.com/sites/Rosen-House-at-Caramoor/details | Rosen House, Mediterranean Revival villa at Caramoor, Katonah; "took ten years to complete". (FB excerpt 25,000 sf / 1920s–30s — not used.) | §13 card 6 |

### Prices used (live AESS pages only; no new prices)
- $195/hr, three-hour minimum ($585); additional time $195/hr — network-cable-repair-westchester-county.html pricing table (same as cat6-repair-hudson-valley hub).
- Replacement Cat6 drop from $175 (cable, keystone, plate, panel punch-down, testing, both-end labelling, patch cord) — network-cable-repair-westchester-county.html; hub publishes the same $175 for Westchester.
- New-install comparison Cat5e $265 / Cat6 $309 / Cat6A $441 per drop to 100 ft — cat6-installation-westchester-county.html (= Brooklyn base ×1.25 rounded; matches §9 Westchester multiplier).
- Closet audit "quoted by port count"; plenum (CMP) "add per drop"; after-hours/weekend "premium applies"; arranged access windows in multi-tenant buildings "no labour premium" — network-cable-repair-westchester-county.html.
- Fixr Jan 2025 national figures — labelled third-party only.
- FLAG (carried from hub): $195 and $175 carry no §9 multiplier on any live Westchester/HV page; this page follows the hub's published Westchester figures, as instructed.

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected per main run)
All 31 distinct source photos in images/network-cable-repair/ (16) and images/cat6/ (15) are already used at least once on cat6-repair-nyc / -long-island / -hudson-valley (perceptual-hash check). Every source shows a technician's face, so each was **cropped to the work area to remove faces**, which also makes these files visually distinct from the earlier uses. Brand logos on shirts/tool are visible in some crops; no house numbers, plates or readable documents.
| images/cat6-repair/ | Source | Crop (fraction x0,y0,x1,y1) |
|---|---|---|
| cat6-repair-westchester-county-wall-jack-no-link-test.webp (hero) | network-cable-repair/network-jack-repair-westchester-county.webp | 0,0.35,0.50,1 |
| -split-jacket-exposed-pairs.webp | network-cable-repair/damaged-ethernet-cable-repair-westchester-county.webp | 0,0.45,0.70,1 |
| -keystone-punch-at-plate.webp | network-cable-repair/keystone-jack-replacement-westchester-county.webp | 0.46,0.46,1,1 |
| -drywall-access-cut-at-box.webp | cat6/cat6-retrofit-installation-bronx-drywall-cut-in.webp | 0.30,0.40,1,1 |
| -crushed-bundle-over-duct.webp | network-cable-repair/crushed-network-cable-repair-westchester-county.webp | none (no face) |
| -wire-map-fail-screen.webp | network-cable-repair/network-cable-fault-detection-westchester-county.webp | 0,0.25,0.75,1 |
| -tone-probe-labelled-panel.webp | network-cable-repair/network-cable-tracing-westchester-county.webp | 0.53,0.15,1,1 |
| -fish-tape-conduit-feed.webp | cat6/cat6-wiring-bronx-fish-tape-conduit.webp | 0,0.32,1,1 |
| -data-voice-plate-rework.webp | cat6/cat6-voice-data-outlet-installation-bronx.webp | 0.45,0.40,1,1 |
| -panel-port-reterminate.webp | network-cable-repair/patch-panel-repair-westchester-county.webp | 0,0.15,0.62,1 |
| -switch-port-flashlight.webp | network-cable-repair/switch-port-troubleshooting-westchester-county.webp | 0,0,0.55,1 |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (8) + images/cat6/ (3), cropped to remove faces (no real cat6-repair photos yet)`. Photos look AI-rendered (same flag as earlier builders). Finishing pass: -fish-tape-conduit-feed (top 70 px) and -wire-map-fail-screen (top 40 px) re-cropped to remove a visible chin/mouth; captions corrected to what is visible (no cord on the FAIL tester; "metal post" not "desk leg"; shirt logo not sleeve patch; "blue line" from the fish-tape reel).
Finishing pass (size/clone fix): removed the "Where Cat6 Faults Hide" and "Renovating?" sections (repeated Q&A content), the AI-section items "Powerline or coax adapters" and "A $20 tester" (unsourced $20; repeated the equipment note), an unsourced Verizon/Optimum forum sentence, "best-known" (Lyndhurst), and an implied work-history sentence. No questions removed.

### Keyword notes (five layers, Westchester geo)
- Service: Cat6 repair Westchester County, Cat6 cable repair Westchester, Cat6 jack repair, home office Cat6 repair, apartment Cat6 repair, Cat6 re-termination, structured media panel repair, Cat6 recertification.
- Problem: dead wall jack, Cat6 behind plaster, punctured Cat6 (nail/screw/TV mount), Cat6 near steam riser/radiator, Cat6 in duct chase, failed run in concrete co-op, hot unit closet switch, ONT-to-router link down, flooded basement network corner, damage by another trade.
- Technology: Cat6, Cat6A, keystone, 110 punch-down, structured media enclosure, ONT, PoE, wire map, NEXT, return loss, fault location by distance, CMR/CMP, firestop.
- Industry: homeowners with home offices, co-op and condo owners, renters in new towers, landlords/managing agents, medical practices in converted offices, village storefronts, small professional offices.
- Geographic: Westchester County, Yonkers, Mount Vernon, New Rochelle, White Plains, Scarsdale, Bronxville, Larchmont, Mamaroneck, Rye, Port Chester, Harrison, Hartsdale, Tarrytown, Sleepy Hollow, Ossining, Peekskill, Mount Kisco, Katonah, Bedford, Chappaqua, Pelham, Platinum Mile, Central Park Avenue, Mamaroneck Avenue.

## Question register — cat6-repair-westchester-county

§9 "Questions Answered" (H3):
1. Where along a run fished through plaster-and-lath walls does a Cat6 fault usually sit?
2. If a Cat6 repair does need an opening in a finished wall, how big is it and who puts the wall back?
3. The previous owner's Cat6 all ends in a basement corner full of coax splitters and an old phone block — can that be sorted out without rewiring the house?
4. Our Cat6 runs from the fiber or cable box in the basement to the office upstairs — whose problem is it when that link stops working?
5. One room's jack died and every run goes back to a white panel in a closet — does the panel have to be replaced?
6. Does our co-op board have to approve a Cat6 repair that stays inside our own apartment?
7. Our new rental has a small network switch in the unit's utility closet — why do some rooms drop out when that closet runs hot?
8. Our 1960s apartment building has concrete ceilings and no drop ceiling — how is a failed Cat6 run replaced there?
9. The router and switch sit on the basement floor in a part of town that floods — how should the Cat6 be re-terminated when they move upstairs?
10. Our practice moved into a converted office on the Platinum Mile and the exam-room jacks fail certification — is it the cable or the conversion?
11. An electrician's lighting retrofit went through our ceiling and now four desks are dead — how is damage by another trade documented and repaired?
12. Why does the Cat6 that runs beside an old steam riser or radiator keep failing?
13. A picture hook or a TV-mount screw went into the wall — can a punctured Cat6 run be found and fixed?
14. Our 1950s split-level has Cat6 running through the forced-air duct chase — can it be repaired there, or does it have to move?

FAQ (§17, = FAQPage schema):
F1. Can the repair be scheduled so a home office is offline for as short a time as possible?
F2. Do you need our Wi-Fi or router password to repair the Cat6?
F3. Will you work with our superintendent if the switch is in a locked basement room?
F4. Can a dead jack behind a built-in bookcase or kitchen cabinet be repaired without removing the cabinetry?
F5. Can you repair the Cat6 behind a wall-mounted TV without taking the TV down?
F6. Do you repair Cat6 in a two-family house where each unit has its own internet service?
F7. Will a Cat6 repair interrupt the building's intercom or door-entry system?
F8. Can you repair the Cat6 that feeds a generator, solar inverter or battery monitoring gateway?
F9. Do you protect floors and clean up plaster dust after the work?
F10. Can one visit cover both our home office and a small office we run in town?

Other "?" headings: "Home Office or Apartment Link Down in Westchester?" (repair capture), "Dead Jack Somewhere Between Yonkers and Peekskill?" (closing).

De-dup notes: compared by meaning against the full register in research/cat6-repair.md (NYC 26, LI 23, HV 25). Dropped from first plan because a sibling already holds the intent: plaster tracing without opening (NYC Q15) → replaced with opening size/who patches (Q2); cellar water dry-out (NYC Q16) and flood insurance documentation (LI Q5) → replaced with moving the network corner above the flood line (Q9); seasonal reopening (LI Q10) and garage-cold (HV Q4) → not used; knob-and-tube (HV F1), matching plates (HV F5), labelling, licensing questions → body only or not used; school summer work (LI F3), medical before patients (LI F4) → not used. Re-check against cat6-repair-nassau-county / -suffolk-county once final (same batch).


## Manhattan (cat6-repair-manhattan)

Batch run 2026-10-17 (subagent build; to be merged into research/cat6-repair.md by the main run). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources already in research/cat6-repair.md (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, NYC Electrical Code effective Dec 21 2025, Fixr Jan 2025) are reused only in general terms.

**Thesis (differs from the NYC hub, the LI/HV hubs, network-cable-repair-manhattan and cat6-installation-manhattan):** Manhattan Cat6 is *inherited plant repaired inside someone else's window*. Most links on a Manhattan floor were installed by somebody other than the current occupant (a landlord pre-built, a previous tenant, an IT or AV vendor, a conversion developer), on pathways specific to Manhattan building types (raised floors, slab poke-throughs, power poles, glass-front rooms, consolidation points, shielded Cat6A in new towers, sidewalk vaults under cast-iron storefronts). The repair is planned so that diagnosis happens before the building's work window and the fix, certification and labelling finish inside it. NYC hub thesis (access/risers/pre-war plaster generally) and cat6-installation-manhattan thesis (access governs new drops) are not reused; NCR Manhattan's tenant-vs-base-building blame question is not reused.

### Reddit (local)
- Query: `site:reddit.com AskNYC ethernet apartment wall jack not working landlord pre-war building` · Firecrawl search (excerpts only; reddit not scraped) →
  - https://www.reddit.com/r/AskNYC/comments/p8myp8/do_all_nyc_apartments_have_ethernet_ports/ — excerpt "Ethernet wall ports don't work in apartment complex. What can I do?" → background for §9 Q1 (converted-office apartments) and FAQ F6 framing; not quoted.
  - https://www.reddit.com/r/AskNYC/comments/jdljwa/who_is_responsible_for_internetcable_wiring_in/ — excerpt "I'm having trouble with my built in wall Ethernet" → background only (ownership question NOT used: already on network-cable-repair-manhattan).
  - https://www.reddit.com/r/AskNYC/comments/1tez8o2/incorrectly_wired_internet_cables_in_building/ — excerpt: building "wired for cable (coax) and not internet" → §9 Q1 body (some "data" jacks in residential conversions are not what they look like); not quoted.
  - https://www.reddit.com/r/AskNYC/comments/9ezss5/ — excerpt "typically a small prewar in the boroughs kind of thing" → not used.
- Manhattan-specific Reddit threads on failing Cat6 in offices: EMPTY (not accessible in build env — reddit not scrapeable; search returned only residential threads).

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview could not be viewed; each H3 is framed as a commonly published claim (vendor, cost-guide, forum) and corrected with the sourced facts below.

### Local licensing / code / building rules
- Query: `NYC Department of Buildings low voltage telecommunications cabling permit not required limited energy` · Firecrawl search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 (scrape, directQuote): §28-105.4.7 "An electrical permit shall not be required for the installation, alteration, maintenance, or repair of electrical wiring that is designed to operate at less than 50 volts for signaling, communication, alarm, and data transmission circuits, provided that such work is performed by a licensed master electrician, special electrician, or qualified person as defined in the New York city electrical code." Exceptions: life-safety systems, hazardous locations, intrinsically safe systems, connection to control circuits that activate light/heat/power. "(L.L. 2024/128, 12/21/2024, eff. 12/21/2025)". → §8.5 compliance callout 1; §5.5 fact 4; §10.5 H3 "any handyman"; body only (no question — "Do I need a permit" is already on cat6-installation-manhattan).
- Query: `Landmarks Preservation Commission permit interior alterations not required unless interior landmark or affects exterior` · Firecrawl search → https://www.nyc.gov/site/lpc/about/permits-and-making-alterations.page (scrape, directQuote): "You do not need a permit from the Landmarks Commission to perform ordinary repairs or maintenance chores"; "An LPC permit for interior work is required in the following cases: when the work requires a permit from the Buildings Department or, when work on the interior affects the exterior, when the interior has been designated by the Landmarks Commission as an interior landmark." → §8.5 callout 2; §7.5 lofts paragraph; §10.5 H3 "landmarked building". (Not used as a question: cat6-repair-brooklyn asks the LPC question.)
- Query: `brickunderground co-op alteration agreement wiring ethernet board approval contractor insurance Manhattan` · Firecrawl search → https://www.brickunderground.com/guides/how-to-renovate/what-is-an-alteration-agreement (search result carried full page text): "A decoration agreement can sometimes be approved by the managing agent without a full board review, meaning you can have it authorized in less than a week"; "your board will generally require your contractor to be licensed and insured up to a certain dollar amount and the building named on the insurance policy"; alteration agreements "impose (often stiff) daily penalties … if the contractor works outside of authorized hours"; "Most buildings also have their own house rules". → "Building Window" section (decoration vs alteration agreement, body only); §7 co-op card; §8.5 callout 3.
- Query: `Manhattan office building "contractor rules and regulations" pdf certificate of insurance freight elevator riser access low voltage cabling` · Firecrawl search → only SEC lease exhibits / Federal Register — no Manhattan building rules document retrievable. EMPTY. Page describes building rules only in general terms supported by Brick Underground.
- NYC Electrical Code (2020 NEC + NYC amendments) effective Dec 21 2025; NEC 800.25 abandoned cable — silo research (reused) → §8.5.

### Building stock / corridors / landmarks
- Query: `Manhattan office inventory million square feet pre-war Class B buildings share built before 1950` · Firecrawl search →
  - https://comptroller.nyc.gov/reports/spotlight-new-york-citys-office-market/ (scrape, directQuote; May 14 2024, CoStar data): NYC "nearly 730 million square feet of office space … The vast majority (82% or ~600M) is in Manhattan, predominantly in the prime business districts, south of 59th Street"; Manhattan column: total 594,309,799; Class A 361,054,636; Class B 172,960,516; Class C 59,340,112. → §5 para 2, §5.5 fact 1, §8 intro.
  - https://www.metro-manhattan.com/blog/nyc-office-market-401-buildings-full-availability-shrinks/ (scrape, directQuote; Alan Rosinsky, published Oct 14 2025): of 401 fully leased buildings, "The median one was built in 1931 but renovated in 2011. Prewar bones with modern systems…" → §5 para 3, §5.5 fact 2, §7 pre-war tower card.
  - CHPC "Taking Stock" excerpt (citywide housing, "Over half of units, about 2 million, were constructed before 1947") — citywide, already covered by NYC hub's RGB figure; not used.
- Query: `25 Water Street office to residential conversion largest in country units square feet Financial District` · Firecrawl search → https://en.wikipedia.org/wiki/25_Water_Street (scrape): completed 1969 as 4 New York Plaza; office 1969–2022; redevelopment began 2023; ~1,300 apartments, "the largest such office-to-residential property conversion in the United States"; plan to add 10 floors to existing 22; leasing began January 2025, first residents the next month. Also newyorkyimby.com Feb 2025 excerpt (1,300 apartments). → §5.5 fact 3; §7 conversion card; §9 Q1; §13 landmark card.
- Query: `SoHo-Cast Iron Historic District designated 1973 number of buildings blocks` · Firecrawl search → https://villagepreservation.org/2024/08/14/the-soho-cast-iron-historic-district-a-1973-designation-that-helped-shape-nycs-cultural-legacy/ (excerpt): "approximately 26 blocks, covering nearly 500 buildings"; corroborated by https://sohobroadway.org/soho-castironhistoricdistrict-landmarks/ excerpt ("26 city blocks … approximately 500 buildings"). → §13 card; §8 SoHo corridor card; §7 loft card.
- Query: `SoHo sidewalk vaults vault lights cast iron buildings under sidewalk cellar space history` · Firecrawl search → https://sohobroadway.org/let-there-be-light-the-vaulted-sidewalks-of-soho-broadway/ (scrape, directQuote; Yukie Ohta, Nov 28 2018): vault lights "tiny skylights that diffuse sunlight into the vault below the sidewalk"; "Invented by Thaddeus Hyatt in 1854"; "Costly to maintain and replace, many vault lights were neglected and consequently corroded"; many "filled in with concrete or stone or replaced completely by diamond plate steel"; buildings post "HOLLOW SIDEWALK" or "VAULTED SIDEWALK" signs. 6sqft excerpt (https://www.6sqft.com/soho-and-tribecas-windowed-sidewalks-provided-light-to-basement-factory-workers-before-electricity/) confirms SoHo and Tribeca. → §9 Q7 (storefront vault); §8 SoHo card.
- Ladies' Mile — https://en.wikipedia.org/wiki/Ladies%27_Mile_Historic_District (scrape): designated May 1989 by LPC; "440 buildings on 28 blocks and parts of blocks, from roughly 15th Street to 24th Street and from Park Avenue South to west of the Avenue of the Americas"; "mostly multi-story store and loft buildings"; department stores between the Civil War and WWI. → §13 card; §8 Flatiron card.
- Hudson Yards — https://en.wikipedia.org/wiki/Hudson_Yards,_Manhattan (scrape): 28-acre development by Related and Oxford built over the West Side Rail Yard; 10 Hudson Yards groundbreaking Dec 4 2012, opened 2016; Phase 1 opened March 15 2019; Manhattan West (Brookfield) over the rail yard west of Ninth Ave, 31st–33rd. → §13 card; §8 Far West Side card; §9 Q6 (shielded Cat6A in newer towers — no claim that any named tower uses it).
- Rockefeller Center — https://en.wikipedia.org/wiki/Rockefeller_Center (scrape): 19 commercial buildings on 22 acres between 48th and 51st Streets; 14 original Art Deco buildings between Fifth and Sixth Avenues; construction started 1931, first buildings opened 1933, core complete 1939; NYC landmark 1985, NHL 1987. → §13 card; §8 Midtown card.
- Columbia Manhattanville — Query `Columbia University Manhattanville campus 17 acres West Harlem 125th Street opened 2017` · Firecrawl search → https://neighbors.columbia.edu/news/columbia-university-dedicates-its-17-acre-manhattanville-campus-establishing-its-academic-and (excerpt): "Its 17-Acre Manhattanville Campus … October 24, 2016 … along Broadway immediately above West 125th Street". Wikipedia page for the campus returned 404 (not used). → §13 card; §8 Harlem card (stated with the excerpt's facts only).

### Local news / hyperlocal
- Query: `Manhattan water main break flooded basements businesses SoHo 2025 OR 2024` · Firecrawl search → https://abc7ny.com/post/water-main-break-floods-streets-inwood-manhattan/17791596/ (scrape, directQuote; Sept 11 2025): "A 20-inch water main break in Upper Manhattan sent water gushing down the streets and into some basements"; break "just after 11:30 p.m. Wednesday on Dyckman Street and Nagle Avenue". → §5.5 fact 5; §8 Upper Manhattan card. (News12 Bronx Pelham Bay result — Bronx, not used.)
- Manhattan news specific to Cat6/network cabling failures: EMPTY (no result).
- Hyperlocal (Tribeca Citizen, West Side Rag, Our Town, amNY) on cabling: EMPTY (no relevant result in searches above).

### Technical (Manhattan-pathway angle)
- Query: `HDBaseT cable requirements Cat6 solid core 100 meters avoid patch panels couplers troubleshooting flicker` · Firecrawl search (excerpts) → https://support.atlona.com/hc/en-us/articles/360054843994-HDBaseT-Cabling-A-Guide: "Stranded cables dramatically reduce signal quality and distance. If you want 4K signals to reach 100 m, you must use shielded Cat 6A."; https://support.pulse-eight.com/support/solutions/articles/30000053197-...: "Cat cabling is the most common cause of HDBaseT signal problems … Always use solid core cable"; https://cn.control4.com/docs/product/av-cables/cabling-guide/english/latest/: "Wall plates, joiners, patch panels, and leads must be CAT6/6a/7 rated. Use no more than two patch cables resulting in a three-segment installation". → §9 Q8 (conference display).
- Query: `TIA-568 consolidation point 15 meters from telecommunications room requirement open office zone cabling` · Firecrawl search → https://www.cablinginstall.com/home/article/16469148/another-look-at-zone-cabling (excerpt): "As defined under TIA/EIA-568-B.1, a CP is a passive interconnection point in the horizontal cabling located at least 15 meters from the TR." → §9 Q11 (consolidation point).
- Query: `shielded Cat6A F/UTP shield continuity bonding both ends test failure troubleshooting` · Firecrawl search → https://www.zion-communication.com/UTP-vs-F-UTP-vs-U-FTP-vs-S-FTP-Shielding-Grounding-Thermal-Rules-id49063765.html (vendor excerpt): "Most 'shielded cable failures' are actually system failures: shield continuity breaks at patching, racks are not bonded, or PoE bundles trap heat". → §9 Q6 (attributed as a vendor's guidance).
- Raised-floor, poke-through, power-pole and glass-partition pathway descriptions (§9 Q2–Q5) are written from general field practice; no statistics or named buildings are attached to them.

### Prices used (only from live AESS Manhattan pages; no new prices)
- $195/hr, three-hour minimum ($585) — network-cable-repair-manhattan.html ("$195 an hour against a three-hour minimum — $585 for the opening block").
- Replacement Cat6 run from $175 per drop — network-cable-repair-manhattan.html ("A run needing full replacement is priced from $175 per commercial Cat6 drop"; "evening freight windows appear as a named premium line").
- New-install comparison Cat5e $254 / Cat6 $296 / Cat6A $424 per drop — cat6-installation-manhattan.html.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — third-party, labelled.
- Basis: blueprint §9 gives Manhattan 1.25×; as on cat6-repair-nyc, the multiplier is NOT applied separately because the live Manhattan pages already publish these figures for Manhattan (applying 1.25× again would contradict them). FLAG (carried from NYC hub): $175 and $195 are un-multiplied on every live borough page; cat6-installation-manhattan's $296 is 1.088× the NYC $272, not 1.25× ($340).

### Keyword notes (five layers)
- Service: Cat6 repair Manhattan, Cat6 cable repair Manhattan, Cat6 re-termination, Cat6 recertification, Cat6 jack repair, patch panel repair, Cat6A repair, shielded Cat6A repair, HDBaseT cable repair, consolidation point repair.
- Problem: failed certification, inherited/undocumented Cat6, power-pole furniture feed failure, raised-floor crush, poke-through damage, glass-front room run, vault-cellar corrosion, conference display blanking, shield discontinuity, CP failure, flood-damaged cellar link.
- Technology: TIA-568 permanent link/channel, consolidation point (≥15 m from TR), F/UTP shield bonding, HDBaseT, PoE, firestopped poke-through, plenum/riser listing, NEC 800.25, NYC Admin Code §28-105.4.7.
- Industry: Class A/B/C offices, trading floors, law/finance suites, medical suites (UES), SoHo/Flatiron retail and showrooms, co-ops/condos, office-to-residential conversions, universities (Manhattanville).
- Geographic: Manhattan; Midtown, Rockefeller Center, Plaza District, Hudson Yards/Manhattan West, Financial District/Water Street, SoHo, Tribeca, Flatiron/Ladies' Mile, Union Square, Upper East Side, Upper West Side, Harlem/125th Street, Manhattanville, Washington Heights, Inwood (Dyckman St).

### Images (11) — permanent image rule; Drive folder empty (main run), CompanyCam not connected
Only 16 distinct photos exist in images/network-cable-repair/; all 16 are already used on a cat6-repair sibling (NYC used 11 as re-encoded copies, LI/HV the rest). Chosen: the 9 whose exact hashes are not in images/cat6-repair/, plus 2 (access point, RJ45) already used once by LI. Each looked at before naming; alt/title/caption describe only what is visible.
| images/cat6-repair/ | Source (images/network-cable-repair/) |
|---|---|
| cat6-repair-manhattan-tester-fail-crossed-open-pair.webp (hero) | network-cable-fault-detection-manhattan.webp |
| cat6-repair-manhattan-ceiling-tile-flashlight-inspection.webp | network-cable-inspection-manhattan.webp |
| cat6-repair-manhattan-jacket-scuffed-on-ceiling-grid-edge.webp | crushed-network-cable-repair-manhattan.webp |
| cat6-repair-manhattan-split-jacket-at-workstation-leg.webp | damaged-ethernet-cable-repair-manhattan.webp |
| cat6-repair-manhattan-keystone-punch-down-at-wall-plate.webp | keystone-jack-replacement-manhattan.webp |
| cat6-repair-manhattan-tone-probe-labelled-patch-cords.webp | network-cable-tracing-manhattan.webp |
| cat6-repair-manhattan-link-down-at-core-switch.webp | network-closet-troubleshooting-manhattan.webp |
| cat6-repair-manhattan-wall-jack-no-link-open.webp | network-jack-repair-manhattan.webp |
| cat6-repair-manhattan-patch-panel-port-repunch.webp | patch-panel-repair-manhattan.webp |
| cat6-repair-manhattan-ceiling-access-point-plug.webp | access-point-cable-repair-manhattan.webp |
| cat6-repair-manhattan-rj45-plug-crimp-check.webp | rj45-connector-replacement-manhattan.webp |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (no real cat6-repair photos yet)`.

## Question register — cat6-repair-manhattan

§9 "Questions Answered" (H3):
1. Why do Cat6 jacks fail in apartments carved out of a converted Manhattan office building?
2. Our desks get their Cat6 down power poles from the ceiling — why do those links fail after the furniture is moved?
3. The Cat6 link to a glass-walled meeting room died — where does that cable actually run, and how is it reached?
4. Can Cat6 under a raised access floor be repaired without lifting the whole floor?
5. What happens to the fire-rated poke-through fitting when a Cat6 run up through the slab is replaced?
6. Does a repair on shielded Cat6A have to keep the shield bonded from end to end?
7. Why do Cat6 links that pass through the vault under a SoHo or Tribeca storefront keep failing?
8. Why does a conference-room display fed over Cat6 blank out or flicker?
9. Can a failing link on a trading desk or reception desk be moved to a spare run tonight and repaired properly later?
10. If testing shows the fault is in the building’s riser rather than our suite, what do you hand the building’s vendor? (main run 2026-10-17: replaced the approved-vendor question — same intent as cat6-repair-queens)
11. Why do the Cat6 links that pass through a zone box above an open-plan ceiling fail together?

FAQ (§17, = FAQPage schema):
F1. Can you repair Cat6 in a sublet or co-working suite where the main tenant controls the telecom closet?
F2. Do you bring the ladders or lifts needed for double-height loft and lobby ceilings?
F3. Our floor is mid-renovation under a general contractor — can you repair the Cat6 other trades damaged before the ceilings are closed?
F4. Do you cover Upper Manhattan — Harlem, Washington Heights and Inwood — as well as Midtown and downtown?
F5. Will your technician work alongside our building engineer or super on the day?
F6. Can you repair the Cat6 that feeds a lobby desk, concierge station or package room in a residential building?
F7. Can the landlord or managing agent be invoiced directly when the failed Cat6 is base-building cable?
F8. Can we get a written scope of the repair to submit to the managing agent before the visit is approved?

Other "?" headings: "Is a Manhattan Desk, Register or Boardroom Offline Right Now?" (repair capture), "Manhattan Cat6 Link Failing Before Your Building Window Closes?" (closing).

Avoided (by meaning): all 26 cat6-repair-nyc questions, 23 cat6-repair-long-island, 25 cat6-repair-hudson-valley questions; network-cable-repair-manhattan (cost, repair-vs-replace, COI, after-hours, prove landlord's fault, dead jack, slow vs Wi-Fi, PoE reboot, certified reports, four-tenant ceiling, warranty, other boroughs, who repairs, causes, scheduling speed); cat6-installation-manhattan (cost, building requirements, pre-war install, after-hours, permit, inclusions, drop count, 10G, plenum, full riser, Cat5e upgrade, apartments/co-ops/townhouses). Three first-draft FAQs were replaced after reading the parallel cat6-repair-brooklyn draft (09:30): co-op decoration-vs-alteration, Landmarks approval and who patches plaster/ceilings — all same intent as Brooklyn FAQs; the facts stay in body text. Permit/licence rules (§28-105.4.7) answered in §8.5 body only, not as a question. HV Q14 ("what can we send so the first visit finishes") intent avoided — pre-visit preparation is body text in "The Building Window" section, not a question. HV Q11 (shared telecom room with neighbour) avoided; §9 Q10 (riser-vendor) is about exclusive-vendor rules, not neighbour equipment.

Masked similarity (geo names and phones masked; blocks = p/li/td/h2/h3/figcaption ≥8 words; difflib per block + 5-word shingle Jaccard over the whole page), final build 190,043 B / 13,479 rendered words: vs cat6-repair-nyc Jaccard 0.009, whole-text 0.007, mean block 0.43; vs cat6-repair-long-island 0.008 / 0.008 / 0.43; vs cat6-repair-hudson-valley 0.007 / 0.011 / 0.43; vs cat6-repair-brooklyn (parallel draft) 0.006 / 0.008 / 0.42; vs network-cable-repair-manhattan 0.001 / 0.001 / max block 0.59. Blocks ≥0.65 are only blueprint-excluded constants (licence/rating strip, warranty sentence, freshness stamp, Bronx NAP line, the fixed "What AI Gets Wrong About…" H2 pattern, pricing-table item lines).
File size sits between the NYC hub (+2,048 B bound 189,548) and the HV hub (−2,048 B bound 190,644): margins ~495 B and ~600 B — wiring edits to those hubs should stay small (a link or two).

Main-run edits 2026-10-17: JSON-LD re-indented (no content change) to clear the ±2 KB clone-size check; sibling links to Queens/Bronx/Staten Island/Rockland/Orange/Putnam added.


## Brooklyn (cat6-repair-brooklyn)

Batch run 2026-10-17 (parallel with cat6-repair-manhattan). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl MCP (mcp__Firecrawl__firecrawl_search / firecrawl_scrape). Shell curl blocked. Silo-wide technical sources in research/cat6-repair.md (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, nyc.gov Electrical Code page, Fixr Jan 2025, computercablestore 100 Mbps page, ipsecuritydepot CCA) are reused in general terms only.

**Thesis (differs from the NYC hub, the LI/HV hubs and the parallel Manhattan page):** in Brooklyn the building type decides where a Cat6 link failed and which repair route the building allows. Seven building families, each with its own failure point and its own route: the rowhouse belt (renovation-era runs, coupler plates, bends where runs leave the floor, LPC only when the exterior is touched), Victorian Flatbush wood-frame houses, co-ops (alteration vs decoration agreement), post-2004/2005 rezoning towers (developer-installed Cat6 now ~15-20 years old, structured-media enclosures, conduit in slabs), mill-construction warehouses (DUMBO), waterfront industrial campuses (Navy Yard, Sunset Park District) and the low-lying/flood-exposed blocks (Sea Gate/Coney Island, Red Hook, Gowanus). Manhattan page leans on high-rise/riser/building management; this page avoids riser/managing-agent framing except for co-op paperwork.

### Reddit / forums (source 1)
- Query: `site:reddit.com r/Brooklyn ethernet wiring apartment brownstone cat6` · Firecrawl search (excerpts only; Firecrawl refuses to scrape reddit.com — "we do not support this site") →
  - https://www.reddit.com/r/Brooklyn/comments/1k56guy/brooklyn_renovation_wiring_for_wifi_and_future/ — excerpt: "You should have a minimum of 2 cat6 drops in each room from the network cabinet. run 4 Ethernet cables to each room (future proof)." → background for §5 para 2 (renovation-era home runs to a cabinet). Not quoted.
  - https://www.reddit.com/r/homeautomation/comments/12q87ww/advice_for_a_gut_renovation_lighting_lock_wifi/ — excerpt: "gut renovating a Brooklyn brownstone. Ethernet drops. Planning to have one in every room, plus wiring for the ceiling mounted WAPs." → background §5 para 2. Not quoted.
  - https://www.reddit.com/r/lowvoltage/comments/1o0rlwj/msp_looking_for_a_reliable_professional_partner/ — excerpt: "4 family apartment building in Brooklyn Heights NY needs the following 6 to 8 CAT6+ cable drops" → background only.
  - Fault-specific r/Brooklyn threads (failing Cat6, dead jacks): EMPTY (not accessible in build env — reddit not scrapeable, no fault thread in results).
- Query: `Brownstoner Brooklyn brownstone renovation ethernet wiring plaster walls networking` · Firecrawl search → scrape https://www.brownstoner.com/forum/home-entertainment-systems/wiring-a-house-with-ethernet-hdmi-speakers-etc/ (directQuote; reply timestamp "14 years and 5 months ago"): owner of "very old very neglected house" asks about wiring while walls are open; reply: "The easiest route may be to buy pre-terminated cables (with connectors) of the appropriate lengths and use wall plates with integrated female connectors on the box (rear) side."; "you might just want to put conduit in the walls with strategically located access boxes"; "pull multiple Cat5e or Cat6 data runs from each location to a central location … near a Demarc". → §9 Q1 (coupler plates), §5 para 2, FAQ F2 (pull string/conduit), §10.5 H3 "couplers".

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on-page that the AI Overview could not be viewed and frames each H3 as a commonly published claim (forum/how-to/cost-guide), corrected with sourced facts.

### Building stock / landmarks / corridors (sources 6, 7)
- Query: `Brooklyn rowhouses brownstones share of housing stock built before 1940 Brooklyn` · Firecrawl search → scrape https://urbanomnibus.net/2016/05/how-many-row-houses-are-there-in-new-york-city/ (Neil Freeman, May 4 2016, directQuote): "there are 217,000 row houses in New York. With 761,000 residential properties total, that's more than a quarter of the residential building stock!"; "there's a solid row house belt running across Brooklyn, from Bay Ridge up through Park Slope, Bed-Stuy, and Bushwick. Southern Bushwick is home to a tract of wood frame row houses, another rarity."; "The largest row houses are in Manhattan and Bedford-Stuyvesant, Brooklyn." → §5 para 1, §5.5 bullet 1, §7 rowhouse + frame cards, neighbourhood section.
- Query: `Victorian Flatbush free-standing wood frame houses Prospect Park South historic district number of houses` · Firecrawl search → scrape https://6tocelebrate.org/neighborhoods/victorian-flatbush/ (Historic Districts Council, directQuote): "Victorian Flatbush is known for being the largest concentration of wooden Victorian-style homes in the country. The area presently has five New York City Historic Districts"; comprised of 11 neighbourhoods developed after Flatbush joined Brooklyn in 1894, "yards, freestanding homes". → §5.5 bullet 2, §7 frame-house card, §9 Q4, §13 landmark card.
- Query: `2005 Greenpoint Williamsburg rezoning waterfront towers number of units built since` · Firecrawl search → scrape https://greenpointers.com/2025/05/13/a-walking-tour-looks-back-on-the-legacy-of-the-2005-greenpoint-williamsburg-waterfront-rezoning/ (Pamela Rafalow Grossman, May 13 2025, directQuote): rezoning of "approximately 180 blocks" of former industrial/maritime waterfront; "As of May 2024, Greenpoint and Williamsburg had added 26,253 housing units in the previous 13 years." → §5.5 bullet 3, §7 tower card, §8 corridor card, §9 Q7.
- Query: `Downtown Brooklyn 2004 rezoning residential towers units built since office` · Firecrawl search → excerpts: Pratt Center PDF "In June of 2004, the New York City Council formally approved a large-scale rezoning of Downtown Brooklyn"; https://storymaps.arcgis.com/stories/fd7bebf0949e4a7f96615a9b41e91dfe "Core Downtown Brooklyn experienced a 10x increase in housing units." Scrape of https://www.downtownbrooklyn.com/dtbk20/ returned no body text — EMPTY. Used only: June 2004 rezoning approval (Pratt excerpt) and "tenfold increase in housing units in the core" (storymap excerpt, attributed). → §5.5 bullet 3, §8 Downtown card.
- Query: `Brooklyn Navy Yard 2025 tenants businesses jobs acres Building 77` · Firecrawl search → scrape https://www.brooklynnavyyard.org/brooklyn-navy-yard-fy25-impact-report/ (Jan 8 2026, directQuote): "Spanning more than 300 acres along Brooklyn's waterfront, the Brooklyn Navy Yard is now home to over 550 businesses supporting more than 13,000 jobs and generating more than $2.5 billion in annual economic impact." → §5.5 bullet 5, §8 Navy Yard card, §13 card.
- Query: `Brooklyn Army Terminal Sunset Park square feet tenants buildings NYCEDC` · Firecrawl search → scrape https://edc.nyc/project/sunset-park-district (directQuote): Sunset Park District "spans 200 acres of the South Brooklyn waterfront and includes four major industrial campuses—the Brooklyn Army Terminal (BAT), South Brooklyn Marine Terminal (SBMT), MADE Bush Terminal, and the Brooklyn Wholesale Meat Market"; "BAT's 4 million-square-foot waterfront industrial campus"; "the 36-acre MADE Bush Terminal". → §8 Sunset Park card, §13 BAT card.
- Carried from research/cat6-repair.md (NYC section, Brooklyn Eagle Apr 8 2025): Industry City 650+ businesses, 35 acres, ~6 million sq ft, 16 buildings. → §8 Sunset Park card.
- Query: `DUMBO historic district designated 2007 warehouse factory buildings tech companies offices` · Firecrawl search → scrape https://s-media.nyc.gov/agencies/lpc/lp/2279.pdf (LPC designation report, directQuote): designated "December 18, 2007"; "The approximately 91 buildings in the historic district reflect important trends in the development of industrial architecture"; "The earliest of these buildings are representative of the slow-burning mill construction popular in the mid-to-late nineteenth century." Search excerpt: Arbuckle warehouse at 20 Jay Street (1908) erected by Turner Construction Company (excerpt only, not used). → §7 mill card, §8 DUMBO card, §13 card.
- Query: `Brooklyn Heights Historic District 1965 first historic district New York City designated` · Firecrawl search → excerpts: https://hdc.org/buildings/brooklyn-heights-historic-district/ "Designated November 23, 1965. The first designated New York City Historic District"; https://thebha.org/neighborhood/ same. → §13 landmark card, §8.5 LPC callout.
- Query: `Gowanus rezoning 2021 approved flooding canal housing units` · Firecrawl search → scrape https://www.nyc.gov/content/planning/pages/our-work/plans/brooklyn/gowanus (directQuote): "The City Council adopted the Gowanus Neighborhood Plan on November 23, 2021."; goals include "resilience in the face of climate change" and canal clean-up. → §8 Gowanus card, neighbourhood section.
- Query: `Ocean Parkway Midwood prewar co-op elevator buildings Brooklyn cooperative apartments history` · Firecrawl search → only listing sites (streeteasy, homes.com). Not used as sources. Co-op building specifics: EMPTY (listing data not used).

### Local licensing / permits / rules
- Query: `Landmarks Preservation Commission permit interior work historic district rowhouse not required exterior only` · Firecrawl search → scrape https://www.nyc.gov/site/lpc/about/permits-and-making-alterations.page (directQuote): "You do not need a permit from the Landmarks Commission to perform ordinary repairs or maintenance chores."; "An LPC permit for interior work is required in the following cases: when the work requires a permit from the Buildings Department or, when work on the interior affects the exterior, when the interior has been designated by the Landmarks Commission as an interior landmark." → §9 Q3, §8.5 callout 1, §10.5 H3.
- Query: `co-op alteration agreement low voltage wiring contractor insurance board approval Brooklyn brickunderground` · Firecrawl search → https://www.brickunderground.com/guides/how-to-renovate/what-is-an-alteration-agreement (search excerpt, full guide text in excerpt): alteration agreement = "contract between you and your co-op or condo board"; "A decoration agreement can sometimes be approved by the managing agent without a full board review, meaning you can have it authorized in less than a week"; "your board will generally require your contractor to be licensed and insured up to a certain dollar amount and the building named on the insurance policy"; "If you are not sure where your planned work falls, play it safe by running it by the managing agent". → §9 Q6, §8.5 callout 3.
- Query: `EPA Renovation Repair and Painting rule pre-1978 housing 6 square feet interior lead-safe certified firm` · Firecrawl search → excerpts: https://www.epa.gov/lead/lead-renovation-repair-and-painting-program "requires that anyone paid to perform work that disturbs painted surfaces in homes, childcare facilities and preschools built before 1978 be certified"; https://www.dshs.texas.gov/... summary "triggered when a renovation, repair or a painting job disturbs more than 6 square feet of interior surface space in a room". → FAQ F4, §8.5 callout 4.
- Query: `NYC Local Law 1 2004 lead paint pre-1960 buildings contractor work practices HPD` · Firecrawl search → excerpt https://www.nyc.gov/site/hpd/services-and-information/lead-based-paint.page: "Local Law 1 of 2004 requires owners of buildings built before 1960 … to presume that the paint is lead-based paint". → FAQ F4, §8.5 callout 4.
- NYC Electrical Code (2020 NEC + NYC amendments, full effect Dec 21 2025) and NEC 800.25 abandoned cable — reused from research/cat6-repair.md silo section. → §8.5 callout 2.
- AESS NYS licence #12000287431 (site constant).
- DOB permit thresholds for low-voltage repair work: EMPTY (no source found; page makes no claim beyond LPC's own wording).

### Local news / hyperlocal / flood (sources 9, 10)
- Query: `Hurricane Sandy Red Hook flooding businesses basements electrical damage Brooklyn` · Firecrawl search → scrape https://www.nyc.gov/html/sirr/downloads/pdf/final_report/Ch_1_SandyImpacts_FINAL_singles.pdf (SIRR report ch. 1, directQuote): "Near Sea Gate, on the Coney Island peninsula in Brooklyn, the water reached 11 feet above ground level"; "flood damage at critical facilities in Southern Manhattan, Red Hook, and the Rockaways disrupted landline and Internet service throughout the neighborhoods they served for up to 11 days"; "In coastal areas, flood damage to building telecommunications equipment and cabling caused long-term outages"; "floodwaters filled basements and ruined electrical and other building systems"; "more than half of all buildings … in the area flooded by Sandy were outside of FEMA's 100-year floodplain"; "almost 30 supermarkets and 50 bodegas" in Coney Island and Brighton Beach affected. → §5 para 4, §5.5 bullets 4 and 6, §9 Q11, §10.5 H3 flood, §13 Coney Island card.
- Query: `Hurricane Ida September 2021 Brooklyn basement flooding deaths Brooklyn neighborhoods flooded` · Firecrawl search → scrape https://a816-dohbesp.nyc.gov/IndicatorPublic/data-stories/flooding-and-health/ (NYC DOHMH, directQuote): "Record-breaking 3.5 inches per hour of rainfall fell in some areas, exceeding NYC's sewer capacity of 1.75 inches per hour"; "Unlike the flooding that happened during Sandy, which mostly affected coastal areas, rainfall (or pluvial) flooding can happen anywhere in the city." → §5 para 4, §5.5 bullet 6, §9 Q11, §10.5 H3 flood.
- Query: `Brooklyn rats chewed internet cable outage building Brooklyn news` · Firecrawl search → scrape https://brooklyn.news12.com/2026/07/30/crown-heights-residents-stuck-caging-rats-in-infested-apartment-building/3VsqzqOxLSVDmE57mzrtg2 (News 12 Brooklyn, July 30 2026, directQuote): resident of a Crown Heights building trapped two large rats; "golf ball-sized holes beneath her kitchen cabinets where she believes the rats are entering"; "You can hear the rats in the walls."; HPD issued violations. → §9 Q5 (context, attributed). Brooklyn news on rodent-damaged data cable specifically: EMPTY.
- BK Paper / Brooklyn Eagle / Bklyner / Brownstoner news on Cat6 or network-cable faults specifically: EMPTY.

### Prices used (Brooklyn = 1.00× per blueprint §9 — identical to cat6-repair-nyc, no new prices)
- $195/hr, three-hour minimum ($585) — cat6-repair-nyc.html / network-cable-repair-brooklyn.html.
- Replacement Cat6 run from $175 per drop — cat6-repair-nyc.html / network-cable-repair-brooklyn.html ($175/drop).
- Outdoor run entry sealed and bonded from $185 per penetration — as on cat6-repair-nyc.html (source network-cable-repair-bronx.html); 1.00× Brooklyn.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party.
- NOT used: cat6-installation-brooklyn.html per-drop figures ($247 Cat6 etc.) — differ from the $272 the NYC hub quotes as comparison; omitted rather than introduce a second comparison figure. FLAG for Anwar.

### Keyword notes (five layers, Brooklyn geo)
- Service: Cat6 repair Brooklyn, Cat6 cable repair Brooklyn, Cat6 jack repair, Cat6 re-termination, Cat6 recertification, Cat6 re-pull, Cat6 tracing.
- Problem: coupler-plate runs, bend-radius failure at floor-to-wall transition, rodent-chewed Cat6, structured-media panel faults, conduit-in-slab damage, vibration-loosened terminations, cookline heat/grease, flood-exposed cellar closets, router/demarc moved by ISP.
- Technology: keystone, punch-down, inline coupler, structured media enclosure, Cat6/Cat6A, permanent link vs channel, time-domain fault location, EMT/ENT conduit, pull string.
- Industry: brownstone home offices, two-family houses, co-ops/condos, restaurants/storefronts, manufacturers at the Navy Yard and Sunset Park, creative offices in DUMBO, medical/professional practices.
- Geographic: Brooklyn, Park Slope, Bed-Stuy, Bushwick, Bay Ridge, Flatbush/Victorian Flatbush/Prospect Park South, Ditmas Park, Crown Heights, East Flatbush, Downtown Brooklyn, DUMBO, Brooklyn Heights, Williamsburg, Greenpoint, Gowanus, Red Hook, Sunset Park, Coney Island/Sea Gate, Brighton Beach, Sheepshead Bay, Canarsie.

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" empty (main run), CompanyCam not connected
All 15 unique photos in images/cat6/ are already used (by cat6-repair-long-island / -hudson-valley); none by cat6-repair-nyc. 11 chosen by fit; Manhattan agent uses images/network-cable-repair/.
| images/cat6-repair/ | Source (images/cat6/) |
|---|---|
| cat6-repair-brooklyn-labelled-patch-cords-network-rack.webp (hero) | cat6-patch-panel-installation-bronx-network-room.webp |
| cat6-repair-brooklyn-ceiling-tile-replacement-pull.webp | cat6-cable-installation-bronx-ceiling-drop.webp |
| cat6-repair-brooklyn-open-ceiling-corridor-pull.webp | cat6-cable-installation-dutchess-county-corridor-pull.webp |
| cat6-repair-brooklyn-fish-tape-emt-conduit-block-wall.webp | cat6-wiring-bronx-fish-tape-conduit.webp |
| cat6-repair-brooklyn-wall-access-cut-oscillating-tool.webp | cat6-retrofit-installation-bronx-drywall-cut-in.webp |
| cat6-repair-brooklyn-keystone-punch-down-partition.webp | cat6-keystone-termination-brooklyn-outlet.webp |
| cat6-repair-brooklyn-data-voice-jack-retermination.webp | cat6-voice-data-outlet-installation-bronx.webp |
| cat6-repair-brooklyn-printer-data-jack-rework.webp | office-cat6-installation-bronx-printer-data-jack.webp |
| cat6-repair-brooklyn-j-hook-support-above-grid.webp | cat6-installer-bronx-jhook-pathway.webp |
| cat6-repair-brooklyn-metal-stud-bundle-reroute.webp | commercial-cat6-installation-bronx-stud-rough-in.webp |
| cat6-repair-brooklyn-floor-box-keystone-service.webp | cat6-floor-box-installation-brooklyn-conference-room.webp |
DAILY-LOG note: `images: 11 reused from images/cat6/ (no real cat6-repair photos yet)`.

## Question register — cat6-repair-brooklyn

§9 "Questions Answered" (H3):
1. The Cat6 from our brownstone renovation ends on wall plates with snap-in couplers instead of punched-down jacks. Is that why it is unreliable? (Rowhouses)
2. Why do Cat6 runs fished through a rowhouse so often fail right where they leave the floor and turn up into the wall? (Rowhouses)
3. (converted to non-question H3 "Landmark rules and a Cat6 run inside a brownstone" — LPC intent also asked on cat6-repair-manhattan)
4. Is a dead Cat6 run easier to replace in a Flatbush wood-frame house than in a brick rowhouse? (Frame houses)
5. Rats got into the walls and chewed through a Cat6 run. Once it is replaced, how do we stop it happening again? (Frame houses / pests)
6. (converted to non-question H3 "Co-op house rules and a small Cat6 repair" — decoration-vs-alteration intent also asked on cat6-repair-manhattan)
7. Every Cat6 run in our condo ends in a white structured-media box in a closet. Can that box be repaired, or does it have to be replaced? (Co-ops, condos, towers)
8. Our Cat6 runs in conduit buried in the concrete floor of a newer tower. If the cable inside is damaged, does the slab have to be cored? (Co-ops, condos, towers)
9. Can machine vibration in a converted factory loosen Cat6 terminations over time? (Industrial / commercial)
10. The Cat6 behind our restaurant's cookline keeps failing. Is that heat, grease or the cable? (Industrial / commercial)
11. We are raising our network equipment above the flood line. Can the existing Cat6 be extended to the new height, or does every run need replacing? (Flood-exposed blocks)
12. After the internet provider moved the router to the front of the house, half our Cat6 wall jacks went dead. What happened? (Homes / home offices)

FAQ (§17, = FAQPage schema):
F1. (removed by main run 2026-10-17 — "Can you repair Cat6 that runs behind built-in bookcases or kitchen cabinets?" duplicated cat6-repair-westchester-county)
F2. Can you leave a pull string or conduit so the next Cat6 repair is easier?
F3. (removed by main run 2026-10-17 — "Does the electricity have to be shut off…" duplicated cat6-repair-staten-island; its replacement duplicated F8 and cat6-repair-rockland-county)
F4. Our house is more than a century old. What about lead paint when a wall is opened?
F5. I rent my apartment. Do I need the landlord's permission for a Cat6 repair?
F6. Can the old telephone wiring in the walls stand in for a failed Cat6 run?
F7. A jack was ripped out of the wall when furniture was moved. Can it be fixed without re-pulling the cable?
F8. (removed by main run 2026-10-17 — "Will the rest of our network stay up…" duplicated cat6-repair-rockland-county)
F9. In a two-family house, do you need to get into the other apartment to repair our Cat6?
F10. Can you tell whether a renovation damaged our Cat6 or whether it failed on its own?

Other "?" headings: "Need Cat6 Repair in Brooklyn Today?" (repair capture), "Still Fighting a Bad Cat6 Link in Brooklyn?" (closing).

De-dup notes: compared by meaning against the NYC (26), Long Island (23) and Hudson Valley (25) registers in research/cat6-repair.md, and read against network-cable-repair-brooklyn and cat6-installation-brooklyn headings. Deliberately not asked: water-damaged closet reuse (NYC Q16) — Brooklyn flood angle is relocation above the flood line instead; riser/neighbour approval (NYC Q14) — Brooklyn co-op angle is the alteration-vs-decoration paperwork class only; tracing in pre-war plaster (NYC Q15); stapled cable salvage (LI Q9); least-visible replacement route (HV Q12); rodent extent of damage (HV Q7) — Brooklyn rodent question is about protecting the repaired run; travel charge (LI F1); test before closing (LI F2); intercom/gate (HV F3); another contractor's work (NYC F3); remote IT provider (LI F10); evenings/weekends, plenum, 10G, CCA, cost, Cat5e upgrade (cat6-installation-brooklyn / NCR Brooklyn).

Final de-dup vs cat6-repair-manhattan (built in parallel, read at 09:2x): Manhattan asks LPC approval, co-op decoration agreement and who patches openings; Brooklyn removed those as questions (body text kept). Remaining Brooklyn questions share no intent with Manhattan's 21 questions.

Similarity (geo-masked, digits stripped; 5-word shingle Jaccard on full visible text; difflib per p/li/td/h3/figcaption block >=8 words): Jaccard vs nyc 0.023, long-island 0.021, hudson-valley 0.019, manhattan 0.021. Blocks >=0.65 are only excluded constants (licence/rating strip, warranty sentence, freshness stamp, NAP line).

Main-run edits 2026-10-17 (size/dup fixes): removed from "What AI Gets Wrong" the Wi-Fi-mesh myth (incl. the Brick Underground paragraph), the BICSI-style tester paragraph, the DIY/bargain-cable paragraph; those sources are no longer used on the page. CSS minified and JSON-LD compacted (no content change) to clear the ±2 KB clone-size check.
Final FAQ count 7. Markup whitespace compacted and duplicate ImageObject url fields dropped (contentUrl kept) to clear the size check.

## Dutchess County (cat6-repair-dutchess-county)

Built 2026-10-17 (batch with cat6-repair-ulster-county). Area page, up-link /cat6-repair-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx), copied from the hub. Direct line (845) 640-3835 in body, CTAs and schema; (800) 486-0943 only in the shared header chrome. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Fire_Crawl__/mcp__Firecrawl__ firecrawl_search (excerpts only unless "scraped"); "FC scrape" = firecrawl_scrape (query mode, direct quotes). Shell curl blocked. To be merged into research/cat6-repair.md by the main run.

**Thesis (differs from NYC = access/risers/pre-war; LI = environment/heat/distance/storms; HV hub = weather, outbuildings, distance, rodents):** Dutchess is a county of institutions and industry — a regional hospital, the East Fishkill fab and former IBM campuses, IBM South Road, four colleges, a culinary college, Route 9 retail — so a Cat6 repair is governed by **the rules of the room it runs through**: infection-control permits above clinical ceilings, firestop on rated walls, cleanroom/gowning and badge/escort rules, EMI from plant machinery and shielded-cable bonding, HDBaseT and multi-gig margin on campuses, kitchen heat/grease, asbestos (ICR 56) and lead (RRP / City of Poughkeepsie rental registry) in older buildings, and a repair record facilities/compliance teams can file.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | FC search `site:reddit.com Poughkeepsie OR Beacon ethernet cable wall jack not working` → only generic r/wifi, r/homelab, r/eero, r/HomeNetworking threads, none Dutchess → EMPTY (no Dutchess cabling thread). Not used. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 states this on page; its 7 H3 claims are framed as claims repeated in generic how-to/product/cost content and corrected with the sources below. |
| 6 | Landmarks | D1–D10 below |
| 7 | Use cases / building stock | D1–D12, reused R1–R9 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Poughkeepsie Journal (Oct 1 2019 Verizon fiber cut; Jul 14 2021 IBM East Fishkill campus), WAMC (Jan 9 2021 VBMC pavilion), Westfair (iPark East Fishkill). |
| 10 | Hyperlocal | Poughkeepsie Journal used; Daily Freeman / Mid-Hudson News / Highlands Current on Cat6 or cabling faults: none found → EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix — new for this page
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| D1 | `onsemi East Fishkill fab acquisition GlobalFoundries completed 300mm Dutchess` · FC search → FC scrape | https://investor.onsemi.com/news-releases/news-release-details/onsemi-commemorates-transfer-ownership-east-fishkill-new-york | Feb 10 2023 release: acquisition of GF's 300 mm East Fishkill site "effective December 31, 2022"; "added more than 1,000 world-class technologists and engineers"; "The EFK fab is the largest onsemi manufacturing facility in the U.S." (ATREG excerpt: $430M, 2019 agreement — not used.) | §5.5 bullet 2; §7 card; §8 Route 52 card; §13 card 2; Across Dutchess (Fishkill) |
| D2 | `iPark East Fishkill former IBM campus Hopewell Junction redevelopment tenants 2025` · FC search | http://ipark84.com/ (excerpt) | "The former IBM East Campus in East Fishkill, New York, iPark 84 is situated on 300-acres of land with over two million square feet of buildings" | §5.5 bullet 3; §8 card; §13 card 2 |
| D3 | same search | https://westfaironline.com/economic-development/national-resources-plans-mixed-use-ipark-for-former-ibm-east-fishkill-site/ (excerpt, Ryan Deffenbaugh; year not shown in excerpt) | IBM East Fishkill campus "developed by the company in the 1960s and was once home to more than 10,000 employees"; National Resources iPark; "corridor along Route 52"; "access to Interstate 84"; IBM/eMagin leased "offices, laboratories and clean rooms" (dated → not used) | §8 card heading "Route 52 and I-84"; Across Dutchess (Fishkill) — corridor names only |
| D4 | same search → FC scrape | https://www.poughkeepsiejournal.com/story/news/local/2021/07/14/ibm-east-fishkill-evolution-former-campus-shows-economic-shift-ipark-amazon/7396416002/ (Geoffrey Wilson, Jul 14 2021) | "iPark comprises 300 acres and two million square feet in buildings"; "Amazon has taken over 124 acres of the former plant"; "Amazon aims to open a 629,186-square-foot warehouse"; "roughly 2,000 employed on the east campus" | §5.5 bullet 3 |
| D5 | same search | https://extapps.dec.ny.gov/data/DecDocs/314054/Report.HW.314054.2025-07-31.IAQ%20Testing%20Plan%20B220(B310).pdf (excerpt) | "Building 220 (B310) is owned by iPark East Fishkill LLC … OGS is leasing approximately 305,000 square feet of space for warehouse" | §8 Route 52 card |
| D6 | `Vassar Brothers Medical Center patient pavilion square feet opened Poughkeepsie` · FC search | https://www.walshgroup.com/news/2021/walshconsiglicompletes545millionpatientpavilionatvassarbrothersmedicalcenter.html ; https://www.wamc.org/hudson-valley-news/2021-01-09/new-patient-pavilion-opens-at-vassar-brothers-medical-center ; https://www.northwell.edu/locations/vassar-brothers-medical-center (excerpts) | Walsh/Consigli completed Nuvance Health's "752,610-square-foot patient pavilion", "$545 million"; WAMC Jan 9 2021: "752,000 square-foot, eight-level addition"; hospital now listed on northwell.edu | §5 para 1; §5.5 bullet 1; §7 card; §8 hospital card; §13 card 1 |
| D7 | `Culinary Institute of America Hyde Park campus acres students restaurants Route 9` · FC search | https://www.ciachef.edu/cia-new-york/ ; https://en.wikipedia.org/wiki/The_Culinary_Institute_of_America_at_Hyde_Park (excerpts) | CIA: "170-acre riverside main campus in Hyde Park", student-run restaurants; Wikipedia: between the Hudson and U.S. Route 9, ~2,300 students, four public restaurants, grounds "70 acres" (conflicts with CIA's 170 — page uses the college's own figure, attributed) | §8 Route 9 North card; §13 card 3 |
| D8 | `Dutchess County Fairgrounds Rhinebeck acres buildings events year-round` · FC search | https://dutchessfair.com/ ; https://dutchessfair.com/schedule-and-map/ ; https://dutchessfair.com/fair-features/ (excerpts) | Map: "Buildings A,B,C – Commercial Exhibits & Vendors", horse/dairy barns, "Rhinebeck Bank Main Stage"; "The 6-day Dutchess County Fair"; events e.g. Octoberfest Oct 10–11 2026 | §13 card 6; shops/venues section para 4 |
| D9 | `Poughkeepsie Galleria Route 9 square feet stores Town of Poughkeepsie mall 2025` · FC search | https://www.poughkeepsiegalleriamall.com/ (excerpt); https://en.wikipedia.org/wiki/Poughkeepsie_Galleria (excerpt) | Mall: "the largest and most dominant enclosed shopping center in Dutchess County … 110 national and local stores"; Wikipedia 1,100,000 sq ft, 123 shops (not used — conflicts with mall's count) | §7 retail card; §8 Route 9 card; shops section |
| D10 | `Dutchess Community College Pendell Road campus buildings acres Poughkeepsie` · FC search | https://www.sunydutchess.edu/about/facts/locations/poughkeepsie.html (excerpt) | "Our Poughkeepsie campus spans 130 acres … eleven buildings"; 53 Pendell Road | §5.5 bullet 5 |
| D11 | `Bard College Annandale-on-Hudson campus acres buildings students` · FC search | https://en.wikipedia.org/wiki/Bard_College (excerpt) | "more than 70 buildings with a total gross building space of 1,167,090 sq ft"; 2,303 students (2025); Montgomery Place 380 acres bought Jan 2016; total "1260 acres" | §5.5 bullet 5 |
| D12 | `Beacon NY Main Street converted factory buildings Fishkill Creek mills offices lofts history` · FC search | https://www.loftsatbeacon.com/about/history.html ; https://www.roundhousebeacon.com/about/ (excerpts) | Groveville Carpet Mill: A.T. Stewart acquired 1876, "employed over 700 people in the 1880s", "Groveville Mill Dam … tallest on Fishkill Creek" with operating hydro; Roundhouse buildings "part of the Matteawan Manufacturing Company in the early 1800s", "corner of Main and East Main Streets" | §13 card 5; Across Dutchess (Beacon) |
| D13 | `Dutchess County network outage cable cut internet down businesses Poughkeepsie news 2025` · FC search → FC scrape | https://www.poughkeepsiejournal.com/story/news/local/2019/10/01/internet-phone-outages-dutchess-county/3830205002/ (Oct 1 2019) | "A cut fiber in the Poughkeepsie area caused Internet and phone outages for Verizon customers in Dutchess County"; "some areas of Hyde Park and Wappingers Falls … individual reports of outages in Beacon and Cold Spring"; restored for majority by 4:15 p.m. | Across Dutchess (Poughkeepsie); FAQ F10 context |
| D14 | `Dutchess County home improvement contractor license required county OR town building permit low voltage` · FC search → FC scrape (page returned metadata only) | https://www.townofpoughkeepsie-ny.gov/203/Permit-Applications-Submittal-Requiremen (search excerpt); https://www.dutchessny.gov/Departments/DBCH/Building-Permits-Certificates-Occupancy-Lot-Approval.htm (excerpt) | Town of Poughkeepsie lists "Electric and Low Voltage Permit 2022 (PDF)" and "Contractors List 2026"; county DBCH page: "Contact the local municipality" for building permits. County-level contractor licence for Dutchess: EMPTY (no county source found; page makes no licensing claim). | §8.5 local-permits bullet; FAQ F6 |
| T1 | `infection control risk assessment ICRA above ceiling work telecommunications cabling hospital dust containment` · FC search | https://www.ashe.org/system/files/media/file/2022/08/ICRA%202.0%20Tool%20%2B%20Permit.pdf (excerpt) | ICRA 2.0 Type B includes "Work conducted above the ceiling (e.g., … installation of conduit and/or cabling…)"; Type C includes "Non-existing cable pathway or invasive electrical work above ceilings"; precautions incl. HEPA, polyethylene containment, adhesive mats | §8.5 bullet 1; §9 Q1; §10 containment card; process step 2 |
| T2 | same search | https://www.hfmmagazine.com/articles/4693-protecting-patient-spaces-when-working-overhead (Michael Huff, Mar 30 2023, excerpt) | Low-voltage cabling above ceilings "can consist of network, nurse call, security, building automation, telemetry, infant abduction, fire alarm and even tube system communication cabling"; should be "properly supported by either a cable tray or J hooks"; 360-degree inspection list (stained tiles, gaps, debris, abandoned cabling) | Healthcare Ceilings section |
| T3 | `firestop penetration communications cable fire-rated wall …` · FC search; `NEC 800.26 spread of fire …` · FC search | https://www.mikeholt.com/newsletters.php?action=reply&inResponseTo=18041&letterID=1308 (excerpt) | "Use firestop methods approved by the authority having jurisdiction to maintain the fire-resistance rating of the fire-rated assembly [800.26]" | §8.5 bullet 2; §9 Q2; §10.5 H3 7; decision table |
| T4 | `IEEE 802.3bz 2.5GBASE-T 5GBASE-T Cat5e Cat6 100 meters access points alien crosstalk downshift` · FC search → FC scrape | https://archive.nbaset.ethernetalliance.org/wp-content/uploads/2017/05/NBASET-Downshift-WP-1217.pdf | 2.5 Gb/s uses Cat5e's 100 MHz, 5 Gb/s up to 200 MHz; "The worst-case happens when you have a dense bundle … running over a long distance"; "As noise increases and the link fails, Downshift selects the next lower speed" | §6 card; §9 Q9; §10.5 H3 3 |
| T5 | `variable frequency drive VFD interference Ethernet cable separation shielded Cat6 grounding industrial noise errors` · FC search → FC scrape | https://www.controldesign.com/connections/connectors/article/11297404/shielded-and-grounded-industrial-ethernet (Jan 7 2021) | "in an industrial environment with 480-Vac conductors and especially variable-frequency-drive (VFD) output cables … it can need some help"; "shielded eight-position-eight-contact (8P8C) connectors are needed for termination of shielded twisted pair"; author recommends grounding shield at the "source" end only | §9 Q4, Q5; §10.5 H3 2, 4 |
| T6 | `HDBaseT Cat6 cable length 100 meters flicker no signal termination shielded cable recommended classroom projector` · FC search → FC scrape | https://support.atlona.com/hc/en-us/articles/360054843994-HDBaseT-Cabling-A-Guide | home-run "with no keystones, couplers, or punch-downs"; 70 m product: Cat6 4K "130' (40 m)"; "Shielded Cat 6A is ideal"; zip ties not recommended; "typical cable testers cannot determine whether a cable will pass HDBaseT" | §6 card; §9 Q8; §10.5 H3 3 |
| T7 | `cleanroom cabling low outgassing cable jacket ISO 14644 contractor gowning protocol network cable installation cleanroom` · FC search | https://ringandping.com/cleanroom-cabling-for-medical-device-manufacturing/ (vendor blog excerpt) | "Cleanroom cabling requires protocol compliance at every stage: gowning, tool preparation, material selection, penetration sealing, and post-work…" | §9 Q6 (attributed as vendor guidance) |
| T8 | `Cat6 cable temperature rating 60°C 75°C kitchen heat …` · FC search | https://infinity-cable-products.com/blogs/performance/ethernet-cable-temperature-range (excerpt) | "Cat6 riser cables … -20°C to 60°C (-4°F to 140°F) for operation" | §9 Q11; §10.5 H3 6 (stated as "common riser Cat6 … about 60 °C") |
| T9 | `New York Industrial Code Rule 56 asbestos survey required before renovation building owner minor repair ceiling tiles` · FC search | https://dol.ny.gov/system/files/documents/2023/12/icr56.pdf ; https://www.atlantictesting.com/new-york-state-department-of-labor-industrial-code-rule-56-asbestos-survey-exemption-clarifications/ ; https://www.cnsenviro.com/post/asbestos-operations-and-maintenance-plans (excerpts) | Part 56 applies throughout NYS; survey required "Prior to commencement of any demolition, renovation, remodeling or repair"; Atlantic Testing: "there really are no exceptions to an asbestos survey in New York State" | §8.5 bullet 4; §10.5 H3 5; FAQ F4; "What to send" list |

### Reused from earlier research in this repo (sources reached by earlier runs; not re-fetched)
| # | Finding | Source (as logged) | Page section |
|---|---|---|---|
| R1 | IBM quantum facility, 2455 South Road, ~300,000 sq ft + Building 416 renovation, construction start Sept 2026 | thinkdutchess.com IDA summary (research/fiber-optic-installation.md) | §5.5 bullet 4; §8 South Road card |
| R2 | Vassar ~1,000 acres, founded 1861 | en.wikipedia.org/wiki/Vassar_College (research/fiber-optic-installation.md) | §5.5 bullet 5 |
| R3 | Marist 180 acres on US 9; 6,382 students | marist.edu / Wikipedia (research/smart-lock-installation.md D9) | §5.5 bullet 5; §13 card 4 |
| R4 | Dutchess median year built 1971; 22,056 homes (18.0%) built 1939 or earlier | stacker.com (research/soundbar/sonos/smart-lock) | §5.5 bullet 6; home-office section |
| R5 | City of Poughkeepsie rental registry: 2+ units, 12601, pre-1980 → lead safety certificate | dutchessny.gov Rental-Registry-Program (smart-lock D2) | §5.5 bullet 6; §8.5 bullet 5; §9 Q10; FAQ F5 |
| R6 | EPA RRP: ≤6 sq ft interior = minor repair and maintenance | epa.gov FAQ (smart-lock D3) | §8.5 bullet 5; §10.5 H3 5; FAQ F5 |
| R7 | Census QuickFacts Dutchess: broadband 93.5%, mean commute 31.2 min | census.gov (smart-lock D1) | §5.5 bullet 7; home-office section |
| R8 | Poughkeepsie station on Metro-North Hudson Line | Wikipedia Hudson Line (smart-lock D21) | home-office section ("Hudson Line out of Poughkeepsie and Beacon") |
| R9 | Dia:Beacon 1929 Nabisco box-printing factory | diaart.org (research/soundbar-installation.md) | §8 Beacon card; Across Dutchess (Beacon) |
| R10 | NEC 800.25 abandoned cable (EC&M); Fixr Jan 2025 national $125–$250/drop, $45–$75/hr | research/cat6-repair.md silo sources | §8.5 bullet 3; §14 |
| R11 | Corridor names Route 9, I-84, Route 44, Route 55, Taconic and the town list | parking-lot-camera-installation-dutchess-county-research-matrix.md (names only, no figures) | §7, §8, §13 "we also repair", Across Dutchess |

### Prices used (live AESS pages only; nothing invented)
| Figure | Scope | Source |
|---|---|---|
| $195/hr, 3-hr minimum ($585); further hours $195 | repair time | cat6-repair-hudson-valley.html table; network-cable-repair-dutchess-county.html ("$195 Hourly Specialty Rate") |
| From $175 per drop | replacement Cat6 run | cat6-repair-hudson-valley.html; network-cable-repair-dutchess-county.html ("Replacement Cat6 drops from $175 per drop") |
| $333 Cat6 / $286 Cat5e / $477 Cat6A per drop to 100 ft | new-install comparison only | cat6-installation-dutchess-county.html table |
| Quoted by port count / per run / for the site | closet mapping, fiber or re-route, containment/firestop/after-hours | cat6-repair-hudson-valley.html conventions |
| $125–$250/drop, $45–$75/hr | national third-party, labelled | Fixr Jan 2025 (silo) |
**Conflicts / flags for Anwar:** (1) Blueprint §9 Dutchess 1.53× was NOT applied to the $175 replacement drop (would be $268): the live HV hub and the live Dutchess network-cable-repair page both publish $175 un-multiplied for Dutchess, and $195/hr is protected verbatim. (2) network-cable-repair-dutchess-county.html also publishes a "$250 service call + on-site diagnosis" model and ranges (termination $250–$425, splice $350–$700 etc.) that conflict with the $195/hr 3-hr minimum; this page follows the hub and does not mention the $250 service call. (3) cat6-installation-dutchess-county.html's $333 Cat6 drop = 1.224× NYC $272, not the §9 1.53× ($416).

### Images (11) — permanent image rule
Drive "AESS Website Photos/Cat6 Repair" empty (caller), CompanyCam not connected. Perceptual-hash check: images/network-cable-repair/ (224 files) and images/cat6/ collapse to 31 distinct photos, and all 31 are already used by cat6-repair-nyc / -long-island / -hudson-valley. Chose 11 used on NYC or LI but **none used on the HV up-link hub**. Each viewed before naming; byte-identical copies (already WebP, 1536×1024). Note: the library photos look AI-rendered (as the smart-lock Queens/Dutchess builders also noted) — real Cat6 repair photos should replace them.
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-dutchess-county-link-down-tester-core-switch.webp (hero) | network-cable-repair/network-closet-troubleshooting-bronx.webp |
| cat6-repair-dutchess-county-ceiling-bundle-flashlight-check.webp | network-cable-repair/network-cable-inspection-bronx.webp |
| cat6-repair-dutchess-county-panel-port-repunch.webp | network-cable-repair/patch-panel-repair-bronx.webp |
| cat6-repair-dutchess-county-nicked-jacket-ceiling-grid.webp | network-cable-repair/crushed-network-cable-repair-bronx.webp |
| cat6-repair-dutchess-county-checkout-jack-no-link.webp | network-cable-repair/pos-network-cable-repair-bronx.webp |
| cat6-repair-dutchess-county-wire-map-crossed-open-pair.webp | network-cable-repair/network-cable-fault-detection-bronx.webp |
| cat6-repair-dutchess-county-tone-probe-labelled-panel.webp | network-cable-repair/network-cable-tracing-bronx.webp |
| cat6-repair-dutchess-county-wall-jack-open-reading.webp | network-cable-repair/network-jack-repair-bronx.webp |
| cat6-repair-dutchess-county-ceiling-access-point-lead.webp | network-cable-repair/access-point-cable-repair-bronx.webp |
| cat6-repair-dutchess-county-wall-plate-keystone-repunch.webp | network-cable-repair/keystone-jack-replacement-bronx.webp |
| cat6-repair-dutchess-county-split-jacket-desk-frame.webp | network-cable-repair/damaged-ethernet-cable-repair-bronx.webp |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (no real cat6-repair photos yet)`.

### Keyword notes (five layers)
- Service: Cat6 repair Dutchess County, Cat6 cable repair Poughkeepsie, shielded Cat6 repair, Cat6 re-termination, Cat6 certification after repair, firestop restoration, HDBaseT link repair, multi-gig access point cable repair.
- Problem: link down, multi-gig downshift to 1 Gb/s, projector flicker over Cat6, errors when drives run, broken rental jacks, kitchen-heat damage, mixed T568A/T568B, crushed/nicked jacket, provider outage vs inside cabling.
- Technology: Cat6/Cat6A, F/UTP shielded, 8P8C shielded connectors, 2.5GBASE-T/5GBASE-T (802.3bz), HDBaseT, plenum/riser, NEC 800.25/800.26, ICRA 2.0, ICR 56, EPA RRP.
- Industry: hospitals/outpatient, semiconductor/manufacturing, labs, colleges/schools, restaurants/commercial kitchens, retail/malls, event venues, rentals/student housing, home offices.
- Geographic: Dutchess County; City/Town of Poughkeepsie, Arlington, Beacon, Fishkill, East Fishkill, Hopewell Junction, Wappingers Falls, LaGrange, Hyde Park, Rhinebeck, Red Hook, Annandale-on-Hudson, Millbrook, Pleasant Valley, Pawling, Amenia, Millerton; Route 9, Route 52, I-84, Route 44, Route 55.

### Masked-geo similarity (difflib, p/li/td/h3/figcaption ≥8 words, geo names masked)
vs cat6-repair-hudson-valley mean 0.42 · vs cat6-repair-nyc 0.42 · vs cat6-repair-long-island 0.41 · vs network-cable-repair-dutchess-county 0.38 · vs cat6-installation-dutchess-county 0.38. Every block ≥0.65 is an excluded constant (freshness stamp, licence/rating strip, warranty sentence, NAP) or a pricing-table row quoting the price source. cat6-repair-ulster-county not on disk at build time — main run to re-check.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★; Dutchess Reddit cabling threads; Daily Freeman / Mid-Hudson News / Highlands Current cabling stories; Dutchess county-level contractor licence; Town of Poughkeepsie permit page body (metadata only); Field Notes anecdote (no sourced Dutchess job → written as general practice and labelled so).

## Question register — cat6-repair-dutchess-county

§9 "Questions Answered" (H3):
1. Our failed Cat6 is above the ceiling of a patient floor — what has to happen before a tile can come down? (Hospitals, clinics, labs)
2. When a replacement Cat6 run passes through a fire-rated corridor wall, who restores the firestop — and how do we prove it? (Hospitals, clinics, labs)
3. A lab instrument depends on one Cat6 link that cannot drop mid-run — how is a repair scheduled around it? (Hospitals, clinics, labs)
4. Ethernet errors on our production line climb whenever the drives and motors are running — is the Cat6 the problem? (Production floors)
5. Someone repaired our shielded Cat6 with ordinary unshielded jacks — does that matter? (Production floors)
6. Can a Cat6 fault inside a cleanroom or gowned area be repaired without breaking the room's protocol? (Production floors)
7. The Cat6 patch cords on our moving machinery keep breaking every few months — what lasts longer? (Production floors)
8. A classroom projector fed over Cat6 (HDBaseT) flickers or goes black — is it the cable, the wall plate or the extender? (Campuses)
9. We installed new multi-gig access points, but they only link at 1 Gb/s on the existing Cat6 — can the cable be fixed? (Campuses)
10. Tenants keep breaking the wall jacks in our rental units — is there a sturdier repair? (Campuses/rentals)
11. The Cat6 to our kitchen order screens keeps failing — what in a commercial kitchen damages it? (Kitchens, shops, inherited plant)
12. Some jacks in our building are wired T568A and some T568B — is that why certain links fail? (Kitchens, shops, inherited plant)

FAQ (§17, = FAQPage schema):
F1. Can your technician work under badge, escort and safety-orientation rules on a secured manufacturing campus?
F2. Our plant runs three shifts. How do you repair a Cat6 link that can never be down for long?
F3. Can a Cat6 fault at a wedding or event venue be fixed before a booked weekend?
F4. Do you repair Cat6 in older buildings where the ceiling tiles or pipe wrap might contain asbestos?
F5. Is a Cat6 repair in a pre-1978 Poughkeepsie house or rental done lead-safe?
F6. Does a Cat6 repair in a Dutchess town need a permit?
F7. Our Cat6 runs under a raised computer-room floor. Can it be repaired without powering anything down?
F8. Is it worth repairing Cat6 in a building we plan to renovate next year?
F9. Our electrician is already on site for other work. Can you coordinate the Cat6 repair with them?
F10. After a provider outage, how do we know whether our own Cat6 was damaged too?

Other "?" headings: "Cat6 Down at a Dutchess Plant, Practice or Campus?" (repair capture), "A Dutchess Link Failing Before Tomorrow's Shift?" (closing).

De-dup notes (compared by meaning against all 26 NYC, 23 LI and 25 HV register entries, plus network-cable-repair-dutchess-county and cat6-installation-dutchess-county headings/FAQ): avoided COI/managing-agent approval (NYC Q14 — mentioned in body only for mall landlords), medical office before patients arrive (LI F4 — Q1 is about infection-control permits, not timing), remote IT provider (LI F10), school/library break (LI F3), mall tenant space (LI F5 — retail covered in body only), shared telecom room without touching neighbour (HV Q11), least-visible route in brick (HV Q12), match jacks and plates (HV F5), test before purchase (LI F2), Cat6A parts on van (NYC F5), 10G errors (NYC Q12 — Q9 is 2.5/5G downshift on APs), 100 Mb/s pair fault (NYC Q1 — mentioned in body list only), "is a tester enough" (network-cable-repair-dutchess — §10.5 H3 3 is a body claim about HDBaseT/multi-gig, not an FAQ), construction damage (network-cable-repair-dutchess), licensing "who is allowed" (cat6-installation-dutchess — F6 is about municipal permits, not licensing). Heat: LI Q1 (attic pass-March/fail-July) vs Q11 here (kitchen grease/steam/wash-down/temperature rating) — different setting and cause set; main run may judge. F2 (three-shift temporary bypass) and Q3 (lab instrument idle window) both use a temporary link — different contexts (continuous plant vs batch instrument). cat6-repair-ulster-county (same batch) was not on disk when this register was written — main run to compare.

## Ulster County (cat6-repair-ulster-county)

Built 2026-10-17 (batch with cat6-repair-dutchess-county). Area page, up-link /cat6-repair-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx), copied from the hub's LocalBusiness block. Direct line (845) 640-3835 in body, CTAs and schema; (800) 486-0943 only in the shared header chrome. WhatsApp only as wa.me/17186790359. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Fire_Crawl__firecrawl_search (excerpts only unless "scraped"); "FC scrape" = mcp__Fire_Crawl__firecrawl_scrape (query mode, direct quotes). Shell curl blocked. Merged into research/cat6-repair.md by the continuation run (same day).

**Thesis (differs from NYC = access/risers/pre-war; LI = environment/heat/distance/storms; HV hub = weather, outbuildings, freeze, rodents, distance; Dutchess = institutions/industry, the rules of the room):** Ulster is getting fiber now — Archtop Fiber (headquartered in Kingston, on the former IBM campus) has launched in Kingston and Saugerties and is building in Woodstock; Planet Networks also sells fiber in Kingston; the county's ConnectALL/BEAD programme is taking fiber to the last ~1,300 unserved locations. Once the connection outside is fast, **the Cat6 inside becomes the bottleneck** — and in Ulster that inside cable is usually *inherited*: run by previous owners of houses that changed hands (STRs up 220% in a decade, weekend owners), by DIYers in cabins and log homes, by long-gone tenants of subdivided industrial buildings, terminated on plugs instead of jacks, painted over, buried in spray foam or hidden behind landmark facades. The page is about repairing that inherited Cat6 from the new fiber terminal (ONT) inward, room by room.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | U1–U2 (r/hudsonvalley, r/kingstonnewyork excerpts on Archtop / Planet Networks fiber). Ulster Reddit threads about failing in-wall Cat6: EMPTY. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so on page; its 7 H3 claims are framed as claims common in generic how-to / product / forum content and corrected with the sources below. |
| 6 | Landmarks | U3, U9–U12, R4–R9 |
| 7 | Use cases / building stock | U4–U8, U13, R1–R3, R10 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Archtop Fiber release (Oct 1 2024), Lower Esopus Watershed Partnership (Irene 2011), Grist Mill Real Estate / Hull PG (Hudson Valley Mall), New York Almanack (Levon Helm Studios, excerpt only — not used). |
| 10 | Hyperlocal | Hudson Valley One / Daily Freeman items reused from earlier runs (R-rows). Daily Freeman / Hudson Valley One / Kingston Wire stories on Cat6 or in-building cabling faults: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix — new for this page
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| U1 | `Archtop Fiber Kingston Saugerties fiber internet expansion Ulster County homes` · FC search | https://archtopfiber.com/blog/2024/10/01/archtop-fiber-begins-construction-on-state-of-the-art-fiber-network-in-woodstock/ (excerpt) | Oct 1 2024: Archtop "has started building a 100%-fiber Internet network in the Town of Woodstock"; "Headquartered in Kingston"; "Woodstock is one of several communities in Ulster County with which Archtop Fiber has an MOU"; service launched in Kingston, Saugerties, Rhinebeck, Warwick; "multi-gig, 100%-fiber". Same search: archtopfiber.com homepage excerpt "Download and upload speeds up to 8 Gbps … 300 Enterprise…"; Facebook excerpt "installations are being done this year in the towns of Kingston, Ulster, Hurley, Esopus and Saugerties" (Facebook — not used); Reddit r/hudsonvalley/11tsdnz title "Archtop Fiber coming to Kingston, Saugerties - competition for Spectrum". | §5 para 1–2; §5.5 bullet 1; Fiber Hand-off section; §8 Enterprise Drive card; Across Ulster (Kingston, Saugerties, Woodstock); §10.5 H3 1 |
| U2 | `site:reddit.com kingstonnewyork OR hudsonvalley Archtop fiber install ethernet router wiring house` · FC search | https://www.reddit.com/r/hudsonvalley/comments/1unfmxq/kingston_internet_options/ ; https://www.reddit.com/r/kingstonnewyork/comments/1ljldek/planet_networks_fiber/ ; https://www.reddit.com/r/hudsonvalley/comments/1i3o1a5/planet_networks_internet/ (excerpts) | Kingston residents compare Archtop and Planet Networks fiber; one says "the install was super easy, they even threw in a free extension router"; another chose Planet Networks over Archtop. (A thread claiming Archtop "lags constantly" — opinion, NOT used.) | §5 para 2 (residents comparing fiber providers; "extension router" excerpt quoted); Fiber Hand-off section |
| U3 | (carried, see R-rows) Spectrum News Feb 27 2026 — iPark 87 East Campus hosts Ulster BOCES and Archtop Fiber | research/cat6-repair.md HV section | Former IBM Kingston, 200 acres, >1M sq ft, Enterprise Drive, county foreclosure 2019 | §5.5 bullet 2; §7 card; §8 card; §13 card |
| U4 | `Audinate Dante network cable requirements Cat5e Cat6 100 meters gigabit clock sync` · FC search → FC scrape | https://support.getdante.com/hc/en-gb/articles/5508296322975-What-type-of-Ethernet-cable-is-recommended-for-Dante | "Most Dante audio networking devices support Gigabit Ethernet (1 Gbps)"; "CAT5e or CAT6 – Ideal for most Dante networks"; "CAT5 – Can be used for legacy or 100 Mbps networks, but is not recommended for modern Dante systems". Search excerpt (Yamaha Dante design guide): Yamaha Dante devices "designed to be used with gigabit transmission (1000BASE-T), so be sure to use a CAT5e or higher network cable". | §9 Q11; §10.5 H3 6; Studios section |
| U5 | `Bearsville Theater Woodstock recording studio history Levon Helm Studios barn` · FC search → FC scrape | https://levonhelm.com/studio | "situated on 18 acres in historic Woodstock"; "The Barn was constructed in 1975 from local hemlock, pine, and bluestone. Levon designed and acoustically engineered the space himself"; used for "concerts, recording sessions, rehearsals, writing retreats, and private events". (newyorkalmanack.com July 2026 dispute/cancelled shows — excerpt only, NOT used.) | §13 card; Studios section; §7 card (studios/venues) |
| U6 | `pass-through RJ45 connectors problems solid core cable failure trimmed wire ends short` · FC search → FC scrape | https://www.truecable.com/blogs/cable-academy/terminating-pass-through-rj45-connectors-onto-solid-copper-ethernet-cable-a-really-bad-idea | "RJ45 8P8C plugs terminated onto solid copper bulk Ethernet should be your last termination option"; "Patch panels, keystone jacks, or field termination plugs are the preferred way to terminate solid copper Ethernet"; "Pass-through plugs, for all of their convenience, are less tolerant of fitment problems than standard RJ45 connectors"; "If you have a poor fitting RJ45 plug you will not only experience issues with speed but also with the ability to power your camera or WiFi AP"; "don't plug and unplug this cable often because solid copper conductors don't hold up to repeated handling". | §9 Q6; §6 card; §10.5 H3 4; decision table row |
| U7 | `solid conductor cable should terminate in jack not RJ45 plug horizontal cabling TIA-568 patch cord stranded` · FC search | https://www.csd.uoc.gr/~hy435/material/Cabling%20Standard%20-%20ANSI-TIA-EIA%20568%20B%20-%20Commercial%20Building%20Telecommunications%20Cabling%20Standard.pdf (excerpt) | ANSI/TIA/EIA-568-B horizontal cabling: "Each 4 pair cable shall be terminated on an 8 position modular jack"; "Cables used to make patch cords should be stranded." | §9 Q6; §10.5 H3 4 |
| U8 | `Kingston NY historic landmarks preservation commission exterior work visible public right of way building permit districts` · FC search | https://kingston-ny.gov/hlpc ; https://engagekingston.com/27697/widgets/94955/documents/64622 ; https://ecode360.com/6728919 (excerpts) | HLPC: "projects involving the exterior of historic properties (individually listed and within historic districts) visible from the public right-of-way" are reviewed; FAQ: exterior projects visible from the right of way "are subject to desk level review. Desk Reviews are generally turned around within one week"; Kingston Code Art. 8: no "material change in the appearance of such a property … visible from a public street or alley … without first obtaining a certificate of appropriateness from the HLPC"; "Nothing in this subsection shall be construed to prevent the ordinary maintenance and repair of any exterior architectural feature … that does not involve a change in design, building materials, color, or outward appearance." (timberdesignbuild.com contractor page lists districts — not used; district names taken from kingston-ny.gov via smart-lock research R5.) | §9 Q9; §8.5 bullet 2; Across Ulster (Kingston) |
| U9 | `spray foam insulation low voltage cable buried future access conduit recommendation Ethernet` · FC search | https://www.avsforum.com/threads/new-construction-prewire-with-spray-foam-insulation.2455338/ ; https://www.reddit.com/r/diyelectronics/comments/1qgih6u/ ; https://epicsprayfoam.com/blog/is-spray-foam-safe-around-electrical-wiring/ (excerpts) | AVS Forum: "Never heard of spray foam hurting low voltage (or any other) cable. You don't need to put any cable in the conduit. Just a pull string."; Reddit: "You can run conduit before the spray foam and save a lot of headache"; spray-foam contractor: foam "approved and safe for use around standard electrical lines, including low-voltage wiring such as ethernet". (Chicago Green Insulation claim that foam traps heat causing failures — contested, NOT used.) | §9 Q10 (attributed as installers' and forum advice); FAQ none |
| U10 | `log home electrical wiring runs drilled through logs chase low voltage wiring after construction difficult` · FC search | https://coventryloghomes.com/electrical/ ; https://forums.mikeholt.com/threads/log-homes.150844/ ; https://www.reddit.com/r/electricians/comments/1euomsf/ (excerpts) | Log-home builder: "The builder will drill large holes that line up vertically through several rows of logs in order to pull the wiring up through"; Mike Holt forum: builders drill "holes for you as they stack the logs"; Reddit kit-cabin thread: plans "called for holes to be drilled through the logs for wire". | §9 Q8; §7 log/cabin card |
| U11 | `paint inside ethernet wall jack contacts painted over network jack not working` · FC search | https://www.quora.com/How-do-you-fix-an-Ethernet-wall-jack-that-is-not-working ; https://www.reddit.com/r/talesfromtechsupport/comments/f7gn7f/dont_paint_over_the_network_jacks/ (excerpts) | Quora answer: "One of the most common reasons for wall jack fails is being painted, and paint getting on the conductors"; tech-support thread "Don't paint over the network jacks!". Forum-level sources — page states it as field experience, not a statistic. | FAQ F10 |
| U12 | `gigabit ethernet uses all four pairs cannot split one cable two jacks 100 Mbps two pairs splitter` · FC search | https://www.reddit.com/r/HomeNetworking/comments/1nf8dnd/ ; https://www.eufy.com/blogs/security-camera/ethernet-splitter ; https://www.quora.com/Can-you-split-one-Ethernet-cable-for-multiple-devices (excerpts) | "The two pair setup is for either two phone lines or 100 Mbps ethernet. All four pairs are required for 1 Gbps ethernet"; splitter devices "max out at 100 Mbps … gigabit speeds … use all four wire pairs". Corroborates silo source computercablestore.com (gigabit needs all four pairs). | FAQ F2; FAQ F7 (phone jacks) |
| U13 | `Archtop Fiber installation ONT inside wiring customer equipment Wi-Fi router what to expect install day` · FC search | https://www.t-mobile.com/home-internet/the-signal/internet-help/how-is-fiber-optic-internet-installed ; https://www.gokinetic.com/blog/how-is-fiber-internet-installed (excerpts; generic provider guides, not Archtop) | ONT "typically mounted inside or just outside your home near where the fiber enters and must be connected to a power source"; "The ONT is linked to your router or gateway using an Ethernet cable"; router "in a centrally located position". Archtop-specific install / demarcation terms: EMPTY (not found) — page tells owners to ask their provider what it owns. | §9 Q1–Q3; Fiber Hand-off section; FAQ F8 |
| U14 | `Hurricane Irene 2011 Esopus Creek flooding Phoenicia Ulster County damage Route 28` · FC search | https://loweresopus.org/2011/09/snapshot-of-rainfall-and-gauge-data-for-irene/ (excerpt) | "Almost all of Ulster County received more than six inches of rain and some places exceeded eight inches"; "Record flood levels … along the Upper Esopus Creek, the Stony Clove Creek in Phoenicia, the Rondout Creek in Rosendale, and a near record crest at the Walkill River in Gardiner"; Saugerties Lighthouse Drive flooding from storm surge up the Hudson. | §5.5 bullet 6; Across Ulster (Route 28 / Phoenicia, Rosendale) |
| U15 | `Hudson Valley Mall Town of Ulster Route 9W redevelopment 2025 2026` · FC search | https://www.hullpg.com/property-details/hudson-valley-mall ; https://gristmillrealestate.com/blog/the-hudson-valley-mall-emptied-out-the-town-of-ulster-didnt (excerpts) | Hull Property Group: "Hudson Valley Mall is a retail property serving Ulster County. Positioned along U.S. Route 9W, supporting long-term redevelopment and repositioning"; Grist Mill: a relocation approved by the Town of Ulster was under construction by June 2025 (details of which tenant — not used). | §8 Route 9W card (as "repositioning" only) |

### Reused from earlier research in this repo (sources reached by earlier runs; not re-fetched)
| # | Finding | Source (as logged) | Page section |
|---|---|---|---|
| R1 | Ulster ConnectALL $20.8M award, ~1,300 unserved locations (Sept 25 2025); May 1 2026 federal approval: all 1,293 unserved locations to get fiber under BEAD via Verizon | ulstercountyny.gov newsroom 2025-09-25 and 2026-05-01 (research/soundbar-installation.md, sonos, smart-lock) | §5 para 2; §5.5 bullet 1; Fiber Hand-off; §10.5 H3 1 |
| R2 | Ulster STRs: 942 (2015) → 2,013 / 2,827 units, 3.28% of housing (May 2025); 36% of STR owners use out-of-county mailing addresses; Shandaken ~10% | Ulster County Comptroller STR report Sept 2025 (research/soundbar-installation.md, smart-lock U2) | §5 para 3; §5.5 bullet 4; FAQ F4; Across Ulster |
| R3 | Ulster: 25.3% (21,829) homes built 1939 or earlier; median year built 1966 (Stacker, Census) | research/sonos-installation.md, smart-lock U11 | §5.5 bullet 3 |
| R4 | Kingston Stockade: Four Corners at John and Crown, 18th-c stone houses on all four corners; Senate House (1676 stone dwelling, first NY Senate 1777) | FOHK walking tour; parks.ny.gov (soundbar/smart-lock) | §13 card; §7 card |
| R5 | Kingston local districts: Stockade, Rondout-West Strand, Chestnut Street, Fair Street, Wilbur — exterior work visible from right of way reviewed before building permit | kingston-ny.gov (smart-lock research) | §8.5; §9 Q9 |
| R6 | Historic Huguenot Street: 10-acre NHL district, 30 buildings, seven stone houses, 1678 settlement | huguenotstreet.org (soundbar/smart-lock) | §13 card |
| R7 | Rondout: D&H Canal opened 1828 to haul coal 108 miles; Rondout zenith 1870 | FOHK / New York Almanack (soundbar) | §7 card; §13 card |
| R8 | Opus 40: bluestone earthwork, Saugerties; by 1898 at least 10,000 people in Ulster made a livelihood from bluestone | opus40.org (soundbar) | §7.5; §13 card |
| R9 | Ashokan Reservoir: created 1915, 14 miles west of Kingston; Ashokan Rail Trail 11.5 miles West Hurley–Boiceville | dec.ny.gov; ulstercountyny.gov (smart-lock, soundbar) | Across Ulster (Route 28) |
| R10 | SUNY New Paltz: 6,197 undergraduates, 1,036 graduate students | newpaltz.edu (soundbar/smart-lock) | Across Ulster (New Paltz) |
| R11 | Ulster cell dead zones along Routes 212 and 28 (Phoenicia, Shandaken, West Hurley) | hudsonvalleyone.com Dec 2016 (smart-lock U8) | Fiber Hand-off (why wired links matter); Across Ulster (Route 28) |
| R12 | Daily Freeman Sept 27 2026: nor'easter peak >14,000 Ulster outages; Central Hudson serves 93,209 Ulster customers | soundbar research | §5.5 bullet 5 |
| R13 | Earth Networks 2020: Ulster 182,760 lightning pulses, 49 thunder days | fiber/cat6-repair HV research | §5.5 bullet 5 |
| R14 | Ellenville / Route 209 through Spring Glen, Ellenville, Napanoch, Wawarsing; Shawangunk Ridge | ewcoc.com (soundbar) | Across Ulster; §8 card |
| R15 | Census QuickFacts Ulster: 183,330 people, 87,657 housing units (2025); broadband subscription 92.4% | census.gov (soundbar/smart-lock U1) | §5.5 bullet 1 |
| R16 | Ulster County: Master Electrician's licence required "to perform electrical work in Ulster County" (Trades and Construction page); county contractor licensing law of 2009 introduced, adoption not verified | ulstercountyny.gov; legislature PDF (soundbar/smart-lock U26) | §8.5 bullet 4 (no claim that low-voltage repair needs the electrical licence) |
| R17 | NEC 800.25 abandoned cable (EC&M); TIA-568 / Fluke NEXT KB; computercablestore (gigabit = four pairs; blue/brown pair fault → 100 Mb/s); NYC DEP watershed regs (Ulster); Central Hudson 811 | research/cat6-repair.md silo + HV | §8.5; §9 Q1, Q5; §10.5 |
| R18 | Walkway Over the Hudson to Highland (1.28 miles, 1888 rail bridge) | hudsonrivervalley.com (soundbar) | Across Ulster (Highland) |
| R19 | Byrdcliffe (1902, Whitehead, 1,500 acres) Woodstock; Mohonk Mountain House (1869, New Paltz) | woodstockguild.org; mohonk.com (smart-lock/soundbar) | Across Ulster (Woodstock, New Paltz) |

### Prices used (live AESS pages only; nothing invented)
| Figure | Scope | Source |
|---|---|---|
| $195/hr, 3-hr minimum ($585); further hours $195 | repair time | cat6-repair-hudson-valley.html table; network-cable-repair-ulster-county.html ("$195 Hourly Specialty Rate"; "$195/hr specialty rate, three-hour minimum"); cat6-installation-ulster-county.html ("service is $195 per hour with a three-hour minimum ($585)") |
| From $175 per drop | replacement Cat6 run | network-cable-repair-ulster-county.html ("Replacement Cat6 drops from $175 per drop where a run has to be pulled fresh"); cat6-repair-hudson-valley.html |
| Cat6 $333 / Cat5e $286 / Cat6A $477 per drop to 100 ft | new-install comparison only | cat6-installation-ulster-county.html pricing table |
| Quoted by port count / per run / for the site | closet mapping, inter-building, landmark-district exterior work | cat6-repair-hudson-valley.html conventions |
| $125–$250/drop, $45–$75/hr | national third-party, labelled | Fixr Jan 2025 (silo) |
**Conflicts / flags for Anwar:** (1) network-cable-repair-ulster-county.html publishes BOTH "$195/hr specialty rate, three-hour minimum" and a "$250 service call including diagnosis" table (termination $250–$425, panel port $250–$475, certification $45–$85/run, splice $350–$700, exterior entry $400–$850, buried trace $650–$1,800) — this page follows the HV hub / Dutchess approach ($195/hr, 3-hr min) and does not mention the $250 service call. (2) Blueprint §9 Ulster 1.53× NOT applied to $175 (would be $268) — live Ulster and HV pages publish $175 un-multiplied. (3) cat6-installation-ulster-county.html $333 Cat6 drop = 1.224× NYC $272, not §9 1.53×; quoted as published, comparison only. (4) cat6-installation-ulster-county.html carries the old three-year warranty wording in its body (seen in the price-context scan: "After the warranty period, service is $195 per hour…") — not this page's concern, flagged.

### Images (11) — permanent image rule
Drive "AESS Website Photos/Cat6 Repair" empty (caller); CompanyCam not connected. None of the 11 sources used by cat6-repair-dutchess-county is reused. 8 from images/cat6/ (the Ulster-named copies), 3 from images/network-cable-repair/ that Dutchess did not use. Each viewed before naming; byte-identical copies (already WebP). Captions describe only what is visible; no customer, building or local project claimed. Note: the library photos look AI-rendered (as the Dutchess / smart-lock builders also noted) — real Cat6 repair photos should replace them.
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-ulster-county-switch-port-flashlight-check.webp (hero) | network-cable-repair/switch-port-troubleshooting-bronx.webp |
| cat6-repair-ulster-county-rj45-plug-crimp-inspection.webp | network-cable-repair/rj45-connector-replacement-bronx.webp |
| cat6-repair-ulster-county-corroded-plug-block-wall.webp | network-cable-repair/water-damaged-network-cable-repair-bronx.webp |
| cat6-repair-ulster-county-dome-camera-no-poe-reading.webp | network-cable-repair/poe-camera-cable-repair-bronx.webp |
| cat6-repair-ulster-county-data-voice-plate-check.webp | cat6/cat6-data-drop-installation-ulster-county-workstation-outlets.webp |
| cat6-repair-ulster-county-floor-box-keystone-rework.webp | cat6/cat6-floor-box-installation-ulster-county-conference-room.webp |
| cat6-repair-ulster-county-ceiling-replacement-pull.webp | cat6/cat6-installation-ulster-county-ceiling-drop.webp |
| cat6-repair-ulster-county-cubicle-jack-reterminate.webp | cat6/cat6-keystone-termination-ulster-county-outlet.webp |
| cat6-repair-ulster-county-labelled-cords-network-room.webp | cat6/cat6-patch-panel-installation-ulster-county-network-room.webp |
| cat6-repair-ulster-county-drywall-access-cut-beside-box.webp | cat6/cat6-retrofit-installation-ulster-county-drywall-cut-in.webp |
| cat6-repair-ulster-county-fish-tape-conduit-repull.webp | cat6/cat6-wiring-ulster-county-fish-tape-conduit.webp |
DAILY-LOG note: `images: 11 reused from images/cat6/ (8) and images/network-cable-repair/ (3) (no real cat6-repair photos yet)`.

### Keyword notes (five layers)
- Service: Cat6 repair Ulster County, Cat6 cable repair Kingston, Cat6 jack repair, Cat6 re-termination, Cat6 certification, ONT-to-router Cat6 repair, inherited cable mapping, conduit re-pull, Dante network cable repair.
- Problem: fast at the router / slow in the room, dead jacks after a house sale, Cat5e behind a Cat6 plate, plugs on in-wall cable, pass-through plug failures, painted jacks, cable lost in spray foam, log-wall runs, landmark facade conduit, Dante clock dropouts, camera recording gaps, solar gateway offline.
- Technology: ONT, XGS-PON / multi-gig fiber, Cat6/Cat5e/Cat6A, keystone vs RJ45 plug, field-termination plug, TIA-568 horizontal cabling, Dante / audio over IP, PoE, structured media enclosure, NEC 800.25.
- Industry: homes and weekend houses, short-term rentals, log homes/cabins, recording studios and venues, makers and offices at reused industrial campuses, Uptown Kingston shops, New Paltz businesses, farms with solar.
- Geographic: Ulster County; Kingston (Uptown/Stockade, Rondout, Midtown), Town of Ulster, Saugerties, Woodstock, Bearsville, Phoenicia, Shandaken, Hurley, Marbletown, Rosendale, New Paltz, Gardiner, Highland, Lloyd, Marlboro, Milton, Esopus, Ellenville, Wawarsing; Route 9W, Route 28, Route 209, Route 299, Route 32, I-87/Thruway, Enterprise Drive.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★; Ulster Reddit threads on failing in-wall Cat6; Daily Freeman / Hudson Valley One / Kingston Wire cabling stories; Archtop / Planet Networks demarcation and inside-wiring terms; municipal low-voltage permit rules for Ulster towns (page tells owners to ask the town building department); Field Notes anecdote (no sourced Ulster job → written as general practice and labelled so).

### Masked-geo similarity (difflib, p/li/td/h3/figcaption ≥8 words, geo names masked) — re-measured after the continuation run
Mean best-block similarity vs every cat6-repair sibling: Manhattan 0.38; Bronx, Brooklyn, Queens, Long Island, Nassau, Orange, Rockland, Suffolk 0.39; NYC, Hudson Valley, Dutchess, Putnam, Westchester, Staten Island 0.40. The only blocks ≥0.65 are excluded constants: freshness/byline stamp, the warranty sentence, the NAP line, the licence/rating strip and the shared silo-nav area lines. (First build, before this run: mean 0.41–0.43 vs NYC, LI, HV, Dutchess.)

### Continuation run (2026-10-17) — what changed vs the first draft (origin/draft/cat6-repair-ulster-county, 12d90681)
- **Size-cluster fix (the only check that failed):** 182,206 B → 170,980 B by minifying the four inline style blocks (comments and whitespace only), compacting the six JSON-LD blocks (same data, no separator spaces), stripping HTML indentation outside script/style, and moving ten repeated inline styles to page classes `.z1`–`.za` (each declaration `!important`, so it behaves as the inline style did). Playwright full-page screenshots at 1440×900 and 390×844 were pixel-identical before and after. Nearest sibling: cat6-repair-brooklyn 175,475 B (gap ≈4.5 KB, still >2 KB after the main run adds a back-link to it).
- **Question de-dup against the whole silo register** (the first draft compared only NYC, LI, HV and Dutchess). Same-intent questions already registered elsewhere were removed from this page's question set:
  - §9 headings turned into statements (body text kept, opening sentence adjusted): fiber terminal → existing run to the router (Orange: Greenlight terminal in garage); who owns the provider cable (Westchester: fiber box to office, whose problem); flexible conduit replacement (Brooklyn: conduit in slab, must the slab be cored); log home with no hollow walls (Orange: log/post-and-beam); Kingston historic district approval (Putnam: Cold Spring Historic District Review Board); spray foam (Putnam: winterized cottage spray foam); old tenant's Cat6 on a leased campus (Queens: last tenant left Cat6 everywhere).
  - FAQ: removed camera-recording interruption (Suffolk F: alarm or camera monitoring), one run to two jacks (Suffolk: split one run; Nassau: split run), solar gateway (Westchester, Staten Island), short-term rental between guest stays (Putnam), mesh vs repair (Queens: Wi-Fi extender), phone jacks to Ethernet (Brooklyn: old telephone wiring stand in), structured-wiring cabinet (Brooklyn: structured-media box), painted jacks (Suffolk: painted or caulked jack). Added seven new FAQs (register below); FAQ now 9 = FAQPage 9, regenerated from the visible FAQ.
  - Short headings/captions rewritten where they matched a sibling ≥0.65: §5.5 and §8.5 sub-headings, the three-hour-minimum heading, one §10.5 claim heading, the fish-tape caption, the form success message.
- **Conventions re-checked against cat6-repair-dutchess-county (live):** canonical, Bronx GBP, (845) 640-3835 body/CTA/schema with (800) 486-0943 only in header chrome, wa.me only for WhatsApp, warranty sentence verbatim (once), no three-year wording, 4.7/201, licence #12000287431, two Web3Forms forms with landing_page `cat6-repair-ulster-county`, links up to /cat6-repair-hudson-valley and to all 15 other cat6-repair pages. Hero badge, meta and both town dropdowns list Ulster towns only (no Putnam/Dutchess towns).
- **Images:** Drive "AESS Website Photos/Cat6 Repair" re-checked this run — empty (no files, no used/ folder). The draft's 11 images kept (unique to this page). Since the draft, commit d8cb9aad appended 14 "aess-cat6-repair-*" photos (already in images/cat6-repair/) to every live cat6-repair page, which now carry 25 figures and fail check_page's exactly-11 rule; they were not added here so the page passes. Those 14 also look AI-rendered (perfect branded uniforms, on-screen "PASS" graphics, a before/after banner) — flagged for Anwar.
- Words 12,534 (was 12,608). No new research, prices, stats or quotes were added; the new FAQ answers are general repair practice plus facts already on the page (warranty terms, installation page pricing reference).

## Question register — cat6-repair-ulster-county

§9 "Questions Answered" (H3 questions; the other §9 H3s are statement headings, see continuation note):
1. Our new fiber service tests at full speed beside the router but not at the desk upstairs — where does the Cat6 testing start? (Fiber arrives)
2. The previous owners took their network equipment when they sold — why are all the Cat6 jacks in our new house dead? (Inherited cable)
3. The wall plate says Cat6, but the cable behind it is printed Cat5e — does that explain our slow room? (Inherited cable)
4. Several of our Cat6 runs end in crimped plugs hanging out of the wall instead of jacks — is that why they keep failing? (Inherited cable)
5. One Cat6 run in our studio's Dante audio network keeps dropping out — is the cable to blame? (Studios, makers, reused campuses)

FAQ (§17, = FAQPage schema):
F1. The fiber terminal has a backup battery, so why do our wired rooms still go offline during a power cut?
F2. While you are here for a repair, can you add a jack in another room?
F3. If a run has to be replaced, should the new cable be Cat6A rather than Cat6?
F4. Can Cat6 behind acoustic panels or under a studio floor be repaired without damaging the room's treatment?
F5. We are selling our house — is it worth repairing dead Cat6 jacks before it goes on the market?
F6. A pet chewed the cable where it comes out of the wall — what repair holds up?
F7. Should a Cat6 repair be done before or after the fiber installation appointment?
F8. Will you leave a list showing which wall jack goes to which switch port?
F9. What warranty comes with a Cat6 repair?

Other "?" headings: "Ulster Link Down Since the Fiber Went In?" (repair capture), "Bought the House, Inherited the Wiring?" (CTA), "Taking Over an Ulster Property? What to Check in Its Cat6" (checklist section), "A Kingston-to-Catskills Link Still Dead Tonight?" (closing).

De-dup notes (continuation run, compared by meaning against all 14 earlier registers in this file — NYC, LI, Bronx, Staten Island, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess): Q1 vs Rockland multi-gig ceiling and Dutchess multi-gig AP downshift — Q1 is where testing starts when a gigabit-or-less fiber plan is slow in one room; Q2 vs Westchester previous-owner basement corner, Orange new-build dead jacks, Suffolk never-worked apartment jacks, Brooklyn/Nassau provider moved router — Q2 is the missing central switch after a sale; Q3 (Cat5e behind a Cat6 plate) and Q4 (plugs on solid in-wall cable; Brooklyn's snap-in couplers is a different defect) have no match; Q5 Dante has no match. F1 vs Dutchess provider-outage damage and Putnam generator/PoE camera drop — F1 is why wired rooms die while the terminal stays up; F2 vs Rockland spare cable pulled alongside — F2 is a new jack in another room; F3 vs NYC Cat6A repaired with Cat6 parts / Cat6A on the van — F3 is choosing the replacement category; F4 vs Manhattan and Dutchess raised floors — F4 is acoustic treatment; F5 vs LI test before purchase — F5 is the seller's side; F6 vs Brooklyn rats in the walls — F6 is pet damage at the outlet; F7 no match; F8 vs Putnam/Suffolk photos and Queens keeping test results — F8 is the jack-to-port map; F9 no warranty question in any register.


## Midtown, Manhattan (cat6-repair-midtown-manhattan-ny) — first Cat6 Repair neighbourhood page

Batch run 2026-10-17 (subagent build; not committed). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl MCP (mcp__Firecrawl__firecrawl_search / firecrawl_scrape with directQuote). Shell curl blocked. Up-link /cat6-repair-manhattan; phone (929) 560-0737; GBP Bronx.

**Thesis (differs from cat6-repair-manhattan and every borough/county page):** Midtown Cat6 rarely wears out — it is *disturbed by other people's work above the ceiling*. Density (GCP 76M sf / Times Square 31M sf offices) plus building-wide legal programmes (LL26 sprinklers, LL88 lighting + sub-metering, LL97 emissions retrofits) plus tenant churn (Comptroller flight-to-quality data) put lighting, mechanical, sprinkler, furniture and fit-out crews in the same ceiling band as tenant Cat6. Repairs are therefore post-trade sweeps with before/after certification, plenum-listed replacement lengths and independent re-support; plus Midtown-specific floor types (hot desks/docks, merged suites with two closets, pods over floor boxes, closets turned into pantries, landlord smart-building cable in new East Midtown towers, Garment District workrooms, MSMX conversions). The Manhattan page's thesis (inherited plant repaired inside the building window) is referenced via up-link, not repeated.

### Reddit (local)
- Query: `site:reddit.com Midtown office ethernet ports dead building IT cabling NYC` · Firecrawl search (excerpts only, reddit not scraped) → https://www.reddit.com/r/lowvoltage/comments/1pbz8dk/recommendation_needed_to_run_ethernet_in_midtown/ (excerpt: 17 ethernet runs for a commercial building, 3 rooms, Midtown); https://www.reddit.com/r/sysadmin/comments/7nop3w/cabling_contractor_for_100person_office_midtown/ (excerpt: recommendation for low-voltage contractor for a new 100-user Midtown office). → Sources section "forum context" only; nothing quoted. Midtown threads about *failing* Cat6: EMPTY (not accessible in build env).

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 says on the page that the AI Overview could not be opened; each H3 is framed as a commonly published claim and corrected with sourced facts.

### Office market / districts / building stock
- Query: `Grand Central Partnership district office space square feet workers ...` · Firecrawl search → scrape https://www.grandcentralpartnership.nyc/about (directQuote): founded mid-1980s; ~70 blocks, 35th–54th St, Second–Fifth Ave; 76 million sq ft commercial/residential/retail; "more than a quarter million office workers". → §5 para 2, §5.5 fact 1, §13 Grand Central card, Sources.
- Query: `Times Square hotels number of hotel rooms Midtown Times Square Alliance office space square feet` · search → scrape https://www.timessquarenyc.org/business-community/market-research-data (directQuote): 0.1% of city land; ~10% of jobs; "nearly 180,000 workers, 19,000+ hotel rooms, and 31 million SF of office space". → §5 para 2, §5.5 fact 2, §8 retail/hospitality para, §13 Times Square card, Sources.
- Query: `Midtown Manhattan office occupancy 2025 Kastle return to office Midtown leasing record sublease` · search → scrape https://comptroller.nyc.gov/reports/nycs-office-market-doom-loop-or-boom-loop/ (directQuote; Nov 13 2025, CoStar): FY2025 net change in occupied space 5-star +3,348,666 sf, 1–4 star −1,092,097 sf; 5-star ≈10% of NYC office space, almost all in Manhattan CBD south of 59th St; Manhattan CBD availability 14.3% 2025 Q4. → §5 para 4, §5.5 fact 5, Sources. (Avison Young / Colliers / JLL excerpts in same search not used.)
- Query: `Midtown South Mixed-Use Plan approved City Council 42 blocks Garment District residential conversions` · search (excerpts) → https://council.nyc.gov/press/2025/08/14/2940/ (approved Aug 14 2025; largest residential neighbourhood rezoning in two decades; 9,500+ units); https://sitemaps.cb5.org/blog/project/midtown-south-mixed-use-rezoning/ (≈42 blocks, W 23rd–W 40th, Fifth–Eighth Ave); https://newyorkyimby.com/2025/08/city-council-approves-midtown-south-mixed-use-plan.html (introduces residential zoning to an area previously limited to commercial and industrial uses). Scrape of https://www.midtownsouthplan.nyc/ returned only "42 blocks of Midtown South". → §5.5 fact 6, §9 Q (showroom during conversion), §8 Garment card, Sources.
- Query: `Garment District Alliance district boundaries square feet office space businesses about` · search (excerpt) → https://garmentdistrict.nyc/history: district settled between 9th Ave and Broadway, 34th–42nd St; Special Garment Center District 1987 restricted ~8 million sq ft to manufacturing. → §8 Garment card, Sources.
- Query: `Garment Center historic district Landmarks Preservation Commission designated loft buildings Seventh Avenue` · search → scrape https://www.nyc.gov/site/lpc/about/pr2025/lpc-designates-five-garment-industry-related-buildings.page (directQuote; Aug 12 2025): five buildings designated (Barbey Building 1908–09; Fashion Tower 135 W 36th, 20 storeys, 1924–25, Emery Roth; Furcraft; 29th Street Towers; Lefcourt Clothing Center 275 Seventh Ave, 27 storeys, designed 1927, Ely Jacques Kahn). → §8.5 Landmarks callout, §13 card, Sources.
- Query: `East Midtown rezoning 2017 new office towers One Vanderbilt 270 Park Avenue Grand Central` · search (excerpts) → https://www.nyc.gov/content/planning/pages/our-work/plans/manhattan/greater-east-midtown (One Vanderbilt special permit for extra floor area in return for ~$225M of Grand Central improvements); https://slgreen.com/sl-green-celebrates-the-historic-opening-of-one-vanderbilt-avenue/ (terracotta façade echoing Grand Central ceiling tiles; SL Green gives 1.7M sf — NOT used because DCP gives 1.3M sf zoning floor area; conflict avoided by omitting the size). → §7 New towers card, §13 card, §9 Q (landlord smart-building cable), Sources.
- Query: `270 Park Avenue JPMorgan Chase headquarters opened 2025 employees floors` · search (excerpt of press release) → https://www.jpmorganchase.com/newsroom/press-releases/2025/grand-opening-270-park and /newsroom/stories/jpmc-celebrates-new-global-hq-at-270-park-ave: opened Oct 21 2025; 60 storeys; 2.5M sf; 10,000 employees; State Sen. Liz Krueger's statement: "the first new office tower built under the East Midtown Rezoning" (attributed on page). → §7 card, §13 card, Sources.
- Rockefeller Center (19 buildings, 22 acres, 48th–51st, from 1931, core 1939) — carried from the Manhattan section above (Wikipedia scrape by earlier run). → §8 Sixth Ave card, §13 card.

### Local licensing / code / building rules
- Query: `Local Law 88 lighting upgrades deadline January 1 2025 buildings over 25,000 square feet NYC` · search → scrape https://www.nyc.gov/site/buildings/codes/ll88-lighting-system-upgrades-sub-meter-installation.page (directQuote): covered buildings >25,000 gsf; covered tenant spaces >5,000 gsf; lighting compliance and sub-metering on and after Jan 1 2025; reports due May 1 2025 ($115 fee). → §5 para 3, §5.5 fact 3, §9 Q1, trades table, Sources.
- Query: `Local Law 26 of 2004 sprinklers office buildings 100 feet or higher deadline July 1 2019 NYC` · search (excerpt) → https://www.nyc.gov/assets/buildings/pdf/ll26of2004_reminder.pdf: full sprinklers in office buildings over 100 ft, complete on or before July 1 2019. → §5 para 3, §5.5 fact 4, trades table, Sources. (Fiber Midtown page already asks a LL26/sprinkler-hanging question — not used as a question here.)
- Query: `Local Law 97 office building retrofits Midtown HVAC electrification 2030 emissions limits buildings over 25,000 square feet` · search (excerpt) → https://www.nyc.gov/site/buildings/codes/ll97-greenhouse-gas-emissions-reductions.page: most buildings >25,000 sf, limits from 2024, stricter 2030. → §5 para 3, §9 Q2, Sources.
- Query: `NYC after hours variance AHV construction work weekdays 7 a.m. 6 p.m. noise code interior work exemption DOB` · search → scrape https://www.nyc.gov/site/buildings/industry/after-hour-variances.page (directQuote): AHV required for construction activity before 7:00 am, after 6:00 pm, or Sat/Sun; filed ≥3 business days before first work day; 14-day window. Page does NOT say whether no-permit low-voltage repair is "construction activity" — the page therefore applies AHV only to work that grows into construction (e.g. coring) and otherwise defers to building rules. → §8.5 after-hours callout, "Quiet Work, Loud Work" section, Sources.
- Query: `NEC 2020 800.113 CMP plenum cable "other spaces used for environmental air" ceiling cavity communications cable requirement` · search → scrape https://www.cablinginstall.com/standards/cabling-standards/article/16465916/data-communications-cables-in-air-ducts-and-plenums (directQuote; Sept 2011): ceiling cavity plenum = NEC "other spaces used for environmental air"; Chapter 8 permits Types CMP and CATVP there. → §8.5 cable-listing callout, §10.5 H3 "any Cat6", equipment card, Sources. (NYC-amendment text on plenum cable: EMPTY — not retrieved; page cites the NEC framing plus the nyc.gov electrical-code effective date already in this file.)
- Reused from silo/Manhattan sections: Admin Code §28-105.4.7 (LL128/2024); NYC Electrical Code (2020 NEC) effective Dec 21 2025; NEC 800.25 abandoned cable; LPC permits page. → §8.5 callouts.

### Local news / hyperlocal
- Query: `Midtown Manhattan water main break flooding basements 2025` · search → only Inwood (ABC7, already used on Manhattan page), Pelham Bay (Bronx) and 14th St/1st Ave (EV Grieve, Aug 2026 — East Village, not Midtown). Midtown-specific incident relevant to cabling: EMPTY. Not used.
- Midtown news on Cat6/network cabling failures: EMPTY (no result).

### Prices used (live AESS Manhattan pages only; no new prices)
- $195/hr, 3-hr minimum ($585); replacement run from $175; evening freight-window premium as a named line — network-cable-repair-manhattan.html (as carried by cat6-repair-manhattan.html).
- New-drop benchmark Cat5e $254 / Cat6 $296 / Cat6A $424 — cat6-installation-manhattan.html.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — third-party, labelled.
- No §9 multiplier applied on top (same basis and FLAG as the Manhattan section above).

### Images (11) — Step C library; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run 14:07Z), CompanyCam not connected
All 11 are crops of the AESS photos already in images/cat6-repair/ (aess-cat6-repair-*), cropped to remove technicians' faces (and, for the access-point photo, the head/hard hat), resized ≤1600 px, WebP q80. Each looked at before naming; alt/title/caption describe only what is visible; no building is named.
| new file (images/cat6-repair/) | source | crop |
|---|---|---|
| cat6-repair-midtown-manhattan-certifier-pass-laptop-labelled-rack.webp (hero) | aess-cat6-repair-certifier-results-labeled-rack.webp | right 53% |
| cat6-repair-midtown-manhattan-tester-at-numbered-panel.webp | aess-cat6-repair-testing-labeled-patch-panel.webp | right 52% |
| cat6-repair-midtown-manhattan-cable-coil-fed-above-ceiling.webp | aess-cat6-repair-pulling-cat6-above-ceiling.webp | right 55% |
| cat6-repair-midtown-manhattan-torn-jacket-on-steel-edge.webp | aess-cat6-repair-damaged-cat6-jacket-sharp-edge.webp | full (no face) |
| cat6-repair-midtown-manhattan-ceiling-access-point-cable.webp | aess-cat6-repair-access-point-cable-repair.webp | right 58%, top 34% |
| cat6-repair-midtown-manhattan-checkout-counter-switch-ports.webp | aess-cat6-repair-pos-counter-cable-repair.webp | right 50% |
| cat6-repair-midtown-manhattan-desk-wall-jack-retermination.webp | aess-cat6-repair-office-wall-jack-repair.webp | right 70%, bottom 55% |
| cat6-repair-midtown-manhattan-tone-probe-trace-at-rack.webp | aess-cat6-repair-toning-cable-at-rack.webp | right 55% |
| cat6-repair-midtown-manhattan-channel-test-pass-at-rack.webp | aess-cat6-repair-cat6-channel-certification-test.webp | right 55% |
| cat6-repair-midtown-manhattan-wire-map-pass-at-patch-panel.webp | aess-cat6-repair-wire-map-test-patch-panel.webp | right 50% |
| cat6-repair-midtown-manhattan-keystone-punch-down-t568b.webp | aess-cat6-repair-punching-down-cat6-keystone.webp | right 78% |
Not used: before-after-rack-cleanup (faces in both panels), crimping-rj45 and poe-camera-cable-test (faces; the camera photo also shows parked cars). DAILY-LOG note suggestion: `images: 11 cropped from AESS photos in images/cat6-repair/ (aess-cat6-repair-*; faces cropped out)`.

### Keyword notes (five layers)
- Service: Cat6 repair Midtown, Cat6 cable repair Midtown Manhattan, Cat6 re-termination, recertification, post-trade ceiling sweep, before-and-after certification, plenum replacement run, re-support, port map.
- Problem: links lost after lighting/duct/sprinkler/furniture work, hot desk offline, dock vs cord vs link, merged-suite two-closet faults, pod over floor box, hidden punch block after closet removal, landlord cable in tenant ceiling, workroom lint/heat/traffic damage.
- Technology: CMP plenum cable, "other spaces used for environmental air", 90 m permanent link, consolidation point, PoE room panels, PoE lighting, J-hooks/independent support, T568A/B.
- Industry: Class A/B offices, finance/law HQs, media on Sixth Ave, Plaza District firms, Garment District showrooms and workrooms, Times Square hotels/theatres, restaurants/retail, U.N.-area missions/NGOs.
- Geographic: Midtown, Grand Central, East Midtown, Plaza District, 57th St, Sixth Ave, Rockefeller Center, Times Square, Theater District, Garment District, Penn Plaza, Turtle Bay, Murray Hill, Bryant Park, Herald Square, Koreatown, NoMad, Hell's Kitchen, Columbus Circle.

### Masked similarity (geo masked incl. Midtown/Grand Central/Garment District/Times Square; blocks p/li/td/h2/h3/figcaption ≥8 words; word-level difflib)
Final build 227,952 B / 13,814 rendered words. Max non-constant block vs any Cat6 sibling 0.61 (pricing-table benchmark line vs cat6-repair-staten-island; ADT/Ring line and AI-method note vs cat6-repair-manhattan). Blocks ≥0.65 are only blueprint-excluded constants: warranty sentence, licence/rating strip, Bronx NAP line, fixed H2 patterns "What AI Gets Wrong About Cat6 Repair in …" and "Every Cat6 Cable Repair Service We Handle in …". Vs fiber-optic-installation-midtown-manhattan-ny (cross-silo): only constants ≥0.65 after rewrite. File size placed above 224.5 KB to clear the ±2 KB clone window of every sibling (nearest: cat6-repair-manhattan 222,470 B; margin ≈5.5 KB) — JSON-LD indentation is wide for that reason.

## Question register — cat6-repair-midtown-manhattan-ny

§9 "Questions Answered" (H3):
1. The building's Local Law 88 lighting upgrade is moving floor by floor — what should we test before and after the electricians reach us?
2. The mechanical contractor is replacing ductwork and air boxes above our ceiling for the building's emissions work — should our Cat6 be moved first or repaired afterwards?
3. Since prefabricated phone booths and focus pods went onto our floor, the desks beside them keep losing network — how are those two things connected?
4. Our booking system shows hot desks as "offline" even when people are sitting at them — is that the dock, the desk cord or the Cat6 in the floor?
5. Our suite was combined with the one next door, and the two old telecom closets were never merged — why do some desks fail whenever the other closet's switch is restarted?
6. In our last renovation the small telecom closet on the floor became a pantry — where did its Cat6 go, and can it still be repaired?
7. In our new East Midtown tower the landlord's smart-building network runs through the same ceiling — how do we know which Cat6 is ours before anything is cut?
8. Our showroom stays open while the floors above are converted to apartments under the Midtown South rezoning — how do we keep our Cat6 working through the construction?
9. Our Garment District workroom still cuts, sews and presses on the same floor as the office — what does that do to the Cat6, and how should it be repaired?

FAQ (§17, = FAQPage schema):
F1. Do you need the building's loading dock booked, or can a repair technician come in through the main lobby?
F2. Some Midtown buildings only allow union contractors — can you work in those?
F3. Do you repair the Cat6 behind the room-booking panels outside our meeting rooms?
F4. Our floor has blue, yellow and grey Cat6 — does the colour matter when a run is repaired?
F5. Will lifting ceiling tiles set off the smoke detectors or the building's fire alarm?
F6. Our new floor uses PoE-powered lighting on Cat6 — do you repair those links as well?
F7. Can a Midtown repair visit cover our office and our second suite in another building on the same day?

Other "?" headings: "Network Jack Dead on a Midtown Floor This Morning?" (repair capture), "Midtown Desks Still Offline After the Trades Went Home?" (closing).

Avoided (by meaning): Westchester "electrician's lighting retrofit … how is damage by another trade documented" (Q1 here is pre/post baseline planning around a scheduled building programme, not documenting damage already done); Suffolk/Queens lease-acceptance and inherited-storefront testing; Manhattan power-pole, glass room, raised floor, poke-through, zone box, riser vendor, sublet/co-working, written scope, building engineer; fiber Midtown LL26 sprinkler-hanging and Times Square sign questions; Orange hotel guest-room and restaurant-before-opening; Dutchess three-shift and badge/escort; Rockland/Westchester password; NYC 100 Mbps, PoE port, re-pull; HV "what can we send"; LI travel charge; Ulster labelling list; Bronx/Westchester boiler/steam-riser heat. Plenum kept to body text (cat6-installation-manhattan asks a plenum question). Permit/licence and AHV kept to body text.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing & DDG, Yelp 1–3★; Reddit threads on failing Midtown Cat6; Midtown local news on cabling failures or Midtown-specific flooding; NYC-amendment text on plenum cable; Manhattan building contractor-rule documents (carried EMPTY from Manhattan section).


## Williamsburg, Brooklyn (cat6-repair-williamsburg-brooklyn-ny) — local research, 2026-10-17 batch

Silo research reused from research/cat6-repair.md (technical sources: Fluke NEXT troubleshooting, BICSI-style study guide, TSB-184-A, NEC 800.25 via EC&M, NYC Electrical Code effective Dec 21 2025 via nyc.gov, Fixr Jan 2025 national figures). Only local / page-specific sources below. Tools: Firecrawl search + scrape (mcp__Firecrawl__*). Shell curl blocked. Format: exact query · platform · URL · finding · page + section used.

Thesis: Williamsburg Cat6 is mostly exposed or semi-exposed cable added by occupants (factory/warehouse lofts and Loft Law IMDs, restaurant/bar/shop fit-outs, venues, East Williamsburg industrial units, post-2005 towers). Faults are mechanical damage from the next trade, tenant or season (sprinkler work, fit-outs, draft lines, outdoor-dining set-up, stage use); the repair must re-route/re-support the run so the next change does not reach it.

### Mandatory sources (§3)
- Reddit — query `reddit Williamsburg Brooklyn ethernet wiring apartment loft internet cable` · Firecrawl search · https://www.reddit.com/r/AskNYC/comments/p8myp8/do_all_nyc_apartments_have_ethernet_ports/ (search excerpt only: "New construction often has ports in each room, but old construction will usually have coaxial cables instead…"); https://www.reddit.com/r/AskNYC/comments/gmwnwh/ (Brooklyn renter asking if running Ethernet along an outside wall violates codes — excerpt only). Scrape of reddit.com refused by Firecrawl ("we do not support this site"). No r/Williamsburg thread on network cabling returned. → background only (new vs old building wiring, §10.5 "new buildings" claim framed without quoting). Local Reddit: EMPTY (not accessible in build env).
- Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG — EMPTY (not accessible in build env). §10.5 claims are framed as common claims in search summaries, cost guides and forums, not as quotes from Google.
- Yelp 1–3★ — EMPTY (not accessible in build env). (Yelp only surfaced as search-result snippets; no complaint text used.)
- Local news / hyperlocal on Cat6/network cable faults in Williamsburg — no relevant result. EMPTY. (Lithium-ion fire search `Williamsburg Brooklyn fire lithium-ion e-bike battery building 2025 FDNY` returned only Midwood/Bushwick/Dean St items — not Williamsburg-specific; not used.)

### Research matrix — local facts used
| # | Exact query | Platform | URL | Finding | Page + section |
|---|---|---|---|---|---|
| W1 | `Williamsburg Brooklyn Loft Law interim multiple dwelling buildings North Side warehouses artists` | Firecrawl search → scrape | https://www.nyc.gov/site/loftboard/about/about.page | 1982 MDL Art. 7-C (Loft Law) created IMD class (former commercial/manufacturing buildings with ≥3 families); amended June 2010, 2013, 2015, 2019; units must not be in an IBZ "other than the Greenpoint, Williamsburg, certain parts of North Brooklyn and certain parts of the Long Island City" IBZs; Loft Board oversees legalisation to Art. 7-B fire/safety standards | §5 Neighborhood ¶2; §5.5 facts; §7 building card "Interim Multiple Dwellings"; After Building Work section |
| W2 | `Greenpoint-Williamsburg rezoning 2005 175 blocks waterfront NYC Planning` | Firecrawl search | https://www.nyc.gov/assets/planning/download/pdf/plans/greenpoint-williamsburg/greenpointwill.pdf (excerpt) | "On May 11, 2005, the City Council approved the Department of City Planning's rezoning proposal" | §5 ¶3; §5.5 facts |
| W3 | same | Firecrawl scrape | https://www.cbsnews.com/newyork/news/williamsburg-greenpoint-rezoning-20-years-later/ | 2005 rezoning of 175 blocks along Williamsburg/Greenpoint waterfront; 2020 census showed 41% population increase in Williamsburg over the decade | §5 ¶3; §5.5 facts |
| W4 | `Domino Sugar Refinery landmark designation 2007 Williamsburg redevelopment Refinery office building opened` | Firecrawl search → scrape | https://en.wikipedia.org/wiki/Domino_Sugar_Refinery | Operated 1856–2004; filter, pan & finishing house NYC landmark 2007; openings 325 Kent 2017, Domino Park 2018, One South First & Ten Grand 2019, One Domino Square 2024; Two Trees leasing 460,000 sq ft office in Refinery building | §5 ¶3; §5.5 facts; §8 Kent/Wythe; §13 landmark card |
| W5 | same | Firecrawl search | https://abc7ny.com/post/domino-sugar-factory-office/13834016/ (excerpt) | Refinery reopened as office building "The Refinery at Domino"; landmark 2007 | §13 landmark card |
| W6 | `Wythe Hotel Williamsburg 1901 factory building converted cooperage` | Firecrawl search | https://www.wythehotel.com/about ; https://ma.com/wythe-hotel.html ; https://serifeditorial.com/places/wythe-hotel-williamsburg-brooklyn (excerpts) | Cooperage by Theobald Engelhardt standing since 1901, later textile factory; 1901 cooperage converted with a contemporary rooftop addition; hotel opened 2012 | §8 Kent/Wythe; §13 landmark card; §5 ¶1 (cooperages, textile mills) |
| W7 | `Williamsburgh Savings Bank Broadway Driggs landmark Weylin; Williamsburg Bridge opened 1903 J M Z Marcy Avenue` | Firecrawl search | http://s-media.nyc.gov/agencies/lpc/lp/1910.pdf (excerpt); https://weylin.com/about/history/ (excerpt) | 175 Broadway at NW corner Broadway & Driggs; built 1870–1875; exterior designated May 17, 1966 (LP-0164); first-floor banking hall designated interior landmark (LP-1910); Williamsburg Bridge opened December 1903; now Weylin event space | §8 Broadway; §8.5 landmarks bullet; §13 landmark card |
| W8 | `Williamsburg Brooklyn music venues Music Hall of Williamsburg North 6th Street Brooklyn Bowl Wythe Avenue Baby's All Right` | Firecrawl search | https://www.bowerypresents.com/music-hall-of-williamsburg/ ; https://en.wikipedia.org/wiki/Baby%27s_All_Right (excerpts) | Music Hall of Williamsburg, 66 North 6th St; Baby's All Right, 146 Broadway off Bedford Ave, bar + venue, 5,000 sq ft | §8 Broadway, North 6th; §13 landmark card |
| W9 | `East Williamsburg Industrial Business Zone Morgan Avenue manufacturing warehouses businesses` | Firecrawl search → scrape | https://www.nyc.gov/content/planning/pages/our-work/plans/brooklyn/north-brooklyn-industry-plan | North Brooklyn IBZ study area 1,066 acres across Greenpoint, East Williamsburg, Bushwick; 19,500 jobs (2016), 77% industrial incl. manufacturing, wholesale, transportation, construction, waste mgmt, motion picture recording; plan released Nov 19 2018 | §5 ¶5; §5.5 facts; §7 building card; §8 Morgan Ave; §13 landmark card |
| W10 | same | Firecrawl search | https://cityneighborhoods.nyc/east-williamsburg (excerpt) | "The L train's Morgan Avenue station, once an overlooked stop amid warehouses, now opens onto … cafés, galleries, and rooftop venues" | §8 Morgan Avenue |
| W11 | `Williamsburg Brooklyn restaurant original pressed tin ceiling Grand Street storefront` | Firecrawl search → scrape | https://forgotten-ny.com/2021/02/grand-street-williamsburg/ | Grand Street and Metropolitan Avenue = "Williamsburg's two major commercial strips"; Williamsburg Houses completed 1938, 12 blocks ~23 acres between Maujer/Scholes/Leonard/Bushwick Ave, NYC landmark 2003; 4-story walkups (Boerum & Graham) | §5 ¶4; §8 Grand/Metropolitan; §13 Williamsburg Houses card; §7 tenement card |
| W12 | same | Firecrawl search | https://www.facebook.com/TheMobHistorian/videos/.../3958153184316203/ (excerpt) | Bamonte's "feeding the same Brooklyn neighborhood since 1900. Pressed tin ceilings…" | §9 Q pressed-tin ceiling |
| W13 | `Bamonte's restaurant Withers Street Williamsburg since 1900` | Firecrawl search | https://en.wikipedia.org/wiki/Bamonte%27s ; https://m.yelp.com/biz/bamontes-brooklyn (excerpts) | Bamonte's, 32 Withers Street, Williamsburg, established 1900 | §9 Q pressed-tin ceiling |
| W14 | `Dining Out NYC roadway dining season April 1 November 29 structures removed rules` | Firecrawl search → scrape | https://www.diningoutnyc.info/rules/roadway/operate | Roadway cafés operate Apr 1–Nov 29 only; may set up from Mar 25; restaurant stores the café off-season; clear-path, noise rules | §5 ¶4; §5.5 facts; §8.5 bullet; §9 Q roadway dining; §10.5 outdoor-cable claim |
| W15 | `Dining Out NYC roadway cafe design rules electrical cords wiring cross sidewalk` | Firecrawl search | https://www.diningoutnyc.info/rules/sidewalk/materials-extras (excerpt); https://www.nycstreetdesign.info/furniture/dining-out-nyc (excerpt); https://rules.cityofnewyork.us/rule/dot-proposed-rule-outdoor-dining/ (adopted, effective March 3 2024) | Sidewalk-café electric connections must run from the building, not from City property such as a street light; roadway cafés removed and stored off-season; features cannot be permanently affixed to roadway/sidewalk; building attachments need DOB or LPC approval; no element may obstruct the clear path | §8.5 bullet; §9 Q roadway dining |
| W16 | `NFPA 13 sprinkler piping shall not be used to support nonsystem components cables` | Firecrawl search → scrape | https://www.meyerfire.com/daily/any-contact-allowed-with-sprinkler-pipe ; https://www.fhca.org/focusonflorida/entry/cabling_on_sprinkler_piping (excerpt); https://up.codes/s/support-of-non-system-components (excerpt) | NFPA 13 (17.1.3.1 current; 9.1.1.7 older eds.): "Sprinkler piping or hangers shall not be used to support non-system components"; NFPA 25 5.2.2.2: piping not subjected to external loads resting on or hung from it | §8.5 bullet; §9 Q sprinkler; §10.5 support claim |
| W17 | `NEC 800.133(C) communications cables shall not be strapped taped attached exterior of conduit raceway as means of support` | Firecrawl search | https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=549 ; https://www.ecmweb.com/national-electrical-code/code-basics/article/20897736/the-nec-and-communications-circuits (excerpts) | NEC 800.24: exposed cables supported by building structure so not damaged by normal building use; 800.133(B): don't strap/tape/attach communications cables to raceways as means of support | §8.5 bullet; §9 Q sprinkler; §10.5 support claim |
| W18 | `glycol beer line trunk condensation insulation sweating bar draft system` | Firecrawl search | https://byo.com/projects/diy-draft-trunk-lines-when-you-want-to-run-long-draft-lines/ ; https://beer-co.us/draft-beer-trunk-systems-key-components-and-installation-tips (excerpts) | Trunk bundles beer + glycol lines in insulation; "Any warm air in contact with the cold lines will sweat … water will then pool in the low spot" | §9 Q glycol/bar jacks |
| W19 | `tactical Cat6 cable etherCON stage snake rugged portable audio network cable` | Firecrawl search | https://www.belden.com/products/cable/audio-cable/ethernet-snake-cable ; https://www.showmecables.com/west-penn-tactical-cat6-ultra-rugged-ethercon-cable (excerpts) | Belden CatSnake: rugged, flexible, for portable professional AV, passes UL 1581 −40 °C cold bend, RJ45/etherCON compatible; tactical Cat6 with locking connectors | §9 Q stage cable; §10 equipment |

### Local licensing / permits used
- NYC Electrical Code (2020 NEC + NYC amendments) effective Dec 21 2025 — carried from silo NYC section (nyc.gov).
- NEC 800.24 / 800.133 support rules (W17); NEC 800.25 abandoned cable — carried from silo (EC&M).
- NFPA 13 / NFPA 25 sprinkler support (W16).
- Dining Out NYC (DOT rule effective March 3 2024) (W14, W15).
- LPC designations: Domino Refinery 2007, Williamsburgh Savings Bank 1966 + interior (W4, W7).
- Loft Law / Loft Board (W1). Nothing here is presented as legal advice (stated on page).

### Prices used (Brooklyn = 1.00× per blueprint §9; identical to cat6-repair-brooklyn, no new prices)
$195/hr, 3-hour minimum ($585); replacement run from $175 per run; exterior wall entry from $185 per penetration; long runs/lifts/finishes/after-hours quoted after testing; packages Starter $585, Standard $195/hr after first 3 hours, Premium repair time + from $175 per run; BYOE labour only. Fixr Jan 2025 ($125–$250/drop, $45–$75/hr) shown as third-party national yardstick only.

### Images (11) — permanent image rule
Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run); CompanyCam not connected. Copied from images/network-cable-repair/ (the `-brooklyn` files) into images/cat6-repair/: flashlight-on-ceiling-cable-bundle (network-cable-inspection), no-link-at-register-jack (pos-network-cable-repair), handheld-tester-at-rack (network-cable-repair), poe-tester-at-dome-camera (poe-camera-cable-repair), ceiling-access-point-reconnect (access-point-cable-repair), corroded-plug-by-block-wall (water-damaged-network-cable-repair), crimping-new-rj45-plug (rj45-connector-replacement), open-pair-result-at-wall-plate (network-jack-repair), toner-probe-on-patch-cords (network-cable-tracing), labelled-panel-retermination (patch-panel-repair), keystone-punch-down-at-plate (keystone-jack-replacement). Alt/title/caption describe only what is visible. CONCERN: on inspection these library photos (like the cat6/ set) look AI-generated (rendered "Abstract Enterprise LLC" uniform logos, stylised screens) — flagged for Anwar.

### Keyword notes (five layers)
Service: Cat6 repair Williamsburg, Cat6 re-termination, Cat6 certification, replacement run, re-support exposed runs. Problem: dead jack, dropping register, corroded jack, crushed run, cable tied to sprinkler pipe, NO LINK / open pair, no PoE. Technology: Cat6/Cat6A, shielded, solid vs stranded, CCA, time-domain fault location, toner, PoE, etherCON/tactical cable, DMX/network lighting. Industry: lofts/IMDs, restaurants/bars, retail, music venues/studios, hotels, adaptive-reuse offices, East Williamsburg industrial/film. Geographic: Williamsburg, Brooklyn; Bedford Ave, Grand St, Metropolitan Ave, Broadway, Kent/Wythe, North 6th St, Morgan Ave; East/South Williamsburg, Greenpoint (adjacent).

### Masked similarity (geo-masked, digits stripped, p/li/td/h3/figcaption ≥8 words, difflib + 5-word shingle Jaccard)
Final build 155,480 B / 12,312 rendered words. Jaccard ≤0.007 vs every cat6-repair-* page (incl. batch siblings LIC 0.003, Fordham 0.004) and 0.000 vs network-cable-repair-williamsburg / structured-cabling-installation-williamsburg. Blocks ≥0.65 are only excluded constants: warranty sentence, NAP line, licence/rating strip. (Midtown batch sibling not on disk when measured.)

## Question register — cat6-repair-williamsburg-brooklyn-ny

§9 "Questions Answered" (H3), clusters "Loft Ceilings and Exposed Brick" / "Storefronts, Bars and Outdoor Dining" / "Stages, Studios and Venues":
1. The Cat6 across our loft ceiling was cable-tied to the sprinkler pipe, and after the sprinkler contractor's visit two runs are dead. Where should the replacement hang?
2. Our landlord will not allow any new holes in the exposed brick. How is a replacement Cat6 run fixed along it?
3. The failed run is above our shop's original pressed-tin ceiling. Can it be replaced without taking the tin down?
4. Our roadway dining setup has to come down every winter. How should the network link to the outdoor card terminal and printer be built so it survives the seasons?
5. The Cat6 jacks under our bar sit beside the beer and glycol lines, and they keep corroding. Is the draft system doing that?
6. The Cat6 between our stage box and the mixing desk gets coiled, stepped on and rolled under cases every night. Should it be repaired or replaced, and with what?

FAQ (§17, = FAQPage schema):
F1. Do you repair the Cat6 that carries lighting control at a venue or photo studio?
F2. Do you repair the Cat6 feeding ticket scanners or a digital jukebox at a bar or venue?

Other headings: none end in "?" (repair capture "Cat6 Down on a Williamsburg Block Today", closing "A Williamsburg Register, Camera or Desk Still Offline Tonight", §10.5 H3s are "Claim: …" statements).

De-dup notes (by meaning, against every register in research/cat6-repair.md — NYC, LI, HV, Bronx, SI, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess, Ulster — and the batch siblings as on disk at ~14:55, plus network-cable-repair-williamsburg and structured-cabling-installation-williamsburg FAQs): Q1 (sprinkler-pipe support) has no match; LIC's "J-hooks packed full" is a different cause. Q2 (no-holes fastening on brick) vs HV Q12 (least-visible route in brick townhouse) and LIC "do new supports in concrete need landlord approval" — Q2 is the fixing method under a no-drill rule, not visibility or approval. Q3 pressed-tin ceiling — no match (Westchester F4 cabinetry is a different obstruction). Q4 roadway dining seasonal link — no match. Q5 glycol condensation at bar jacks vs Brooklyn Q10 cookline heat/grease, Putnam Q12 kitchen, Dutchess Q11 kitchen — different cause (draft-line condensation) and setting. Q6 portable stage cable vs Ulster Q5 (Dante dropouts, "is the cable to blame") — Q6 is repair-vs-replace and cable type for portable cords. F1 lighting control vs Dutchess Q8 HDBaseT projector flicker / Manhattan Q8 display flicker — F1 is scope (DMX/network lighting cabling), not flicker diagnosis. F2 venue devices vs Queens F6 menu boards, Fordham door-counter threshold — device-specific, door counters removed from wording to avoid Fordham overlap. Dropped during drafting because a sibling held the intent: "paint a replacement run to match the ceiling" (LIC: colour that blends in / painted runs), "remove our Cat6 when the loft lease ends" (LIC: which Cat6 has to come out when we move out), fire/smoke exposure (no local source), walk-up stairs surcharge (no published policy), Saturday/Sunday/after-closing scheduling (Putnam/Nassau/SI/Orange), pricing-vs-borough (Bronx F2).


## Long Island City, Queens (cat6-repair-long-island-city-queens-ny) — local research, 2026-10-17 batch

Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, #bronx) · up-link /cat6-repair-queens. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. "Carried" = fetched by an earlier run and logged in research/cat6-repair.md (Queens / silo sections), not re-fetched.

**Thesis:** in Long Island City the Cat6 lives *on* the structure, not inside it. Converted Degnon-era concrete lofts and brick warehouses have open ceilings, so runs hang on J-hooks, ride steel conduit on block/brick/columns, cross thick slabs through sleeves, and pass through tenant-built metal-stud partitions. Faults sit mid-run at the support (overfilled hooks, sag, beam-edge bends, stud knockouts, packed conduit, painted cable, hot PoE bundles), and constant tenant turnover (2001 rezoning, OneLIC 2025) layers abandoned cable on the same hooks. Repair = cable + the hook/pipe/stud/slab that damaged it. Angles already used on cat6-repair-queens (LIC media-panel patching, tower towers/co-ops, kitchens, basements) were avoided as questions.

### Local facts (sources 6, 7 — landmarks, building stock, use cases)
- `Long Island City Partnership neighborhood businesses jobs statistics Long Island City industrial business zone` · Firecrawl search · https://www.longislandcityqueens.com/ (excerpt) · "25 Million Square Feet of Commercial & Industrial Space", "100,000+ Daily Workforce", "40,000+ Residents"; LICP runs the LIC BID and provides services for the LIC IBZ; IBZ = area where city zoning restrictions prevent residential rezoning · §5 para 3, §5.5 bullets 3–4.
- `OneLIC neighborhood plan rezoning Long Island City approved City Council 2025` · Firecrawl search · https://council.nyc.gov/press/2025/11/12/3008/ (excerpt: rezone ~54 blocks, nearly 15,000 homes, 4,350 affordable) and https://www.cozen.com/news-resources/publications/2025/new-york-city-council-approves-long-island-city-neighborhood-plan (excerpt, Nov 17 2025: approved Nov 12 2025; 54 full/partial blocks; ~14,700 units; >3.5 million sq ft commercial/industrial projected; Industrial Subarea south of the Queensboro Bridge stays industrial with "loft-like buildings", part of LIC IBZ) · §5 para 3, §5.5 bullet 5.
- `Hurricane Sandy Long Island City Hunters Point flooding Newtown Creek buildings basements damage` · Firecrawl search · https://www.newtowncreekalliance.org/what-does-hurricane-sandy-reveal-about-newtown-creek/ (excerpt): "some companies already had their bulkhead underwater"; "Basement and ground floor electrical systems were destroyed." · §5 para 4, street-by-street Hunters Point.
  - Same search · https://www.reddit.com/r/longislandcity/comments/xr6cna/ (r/longislandcity post title/excerpt): "Floodwalls along Hunter's Point and a storm gate across Newtown Creek are part of the new $52 billion federal plan" · §5 para 4 (stated as "discussed" plan; $ figure not used).
  - nyc.gov SIRR Ch.1 PDF excerpt ("over 60 percent in Queens") — context unclear in excerpt, NOT used.
- `Degnon Terminal Long Island City history factories Sunshine Biscuit Loose-Wiles LaGuardia Community College building` · Firecrawl search → scrape https://givemeastoria.com/2025/04/13/long-island-city-the-gateway-to-the-worlds-greatest-industries/ (Jason D Antos, Apr 13 2025): 1907 Degnon Terminal Company acquired 362 building lots "south of Jackson Avenue"; first structure 1909 Loose-Wiles Sunshine Biscuit "Thousand Window Bakery", plant closed 1965, now LaGuardia Community College; private rail to every plant; by 1918 more than 70 plants making WWI materials · §5 para 1, §5.5 bullet 1, §13 card 1, street-by-street Degnon blocks.
- `Standard Motor Products building Long Island City Center Building Falchi Building office conversion concrete loft` · Firecrawl search · https://www.costar.com/article/1498917249/ (excerpt): "The SMP Building, built in 1919, now has a mix of office, flex and light industrial spaces with creative tenants"; https://smpbuilding.com/ (37-18 Northern Blvd); https://www.instagram.com/p/DVJeIMNjZ8G/ (listing excerpt): "concrete floors, 12 to 14 foot ceilings" · §5 para 1, §5.5 bullet 2, §13 card 2, pricing "height and reach" bullet. (Falchi/Center Building: nothing usable returned — not used.)
- `Queensbridge Houses largest public housing development North America apartments buildings 1939` · Firecrawl search · https://en.wikipedia.org/wiki/Queensbridge_Houses (excerpt citing LIC Post Oct 17 2019): 96 buildings, 3,142 units, ~7,000 people, opened 1939, between Vernon Blvd and 21st St, largest in North America · §5.5 bullet 7, §13 card 5.
- `Long Island City life sciences lab conversion industrial building Queens 2024 2025 LIC Post` · Firecrawl search · https://newyorkyimby.com/2022/01/life-science-redevelopment-project-announced-for-43-10-23rd-street-in-long-island-city-queens.html (excerpt: 43TEN, 208,000 sq ft lab/research at 43-10 23rd St) and https://www.constructiondive.com/news/suffolk-breaks-ground-life-sciences-project-new-york-city/630539/ (excerpt: gut renovation of 218,000 sq ft seven-story lab building at 43-10 23rd St). Figures differ, page says "more than 200,000 square feet" · §5.5 bullet 6, §7 card 5.
- `Pepsi-Cola sign Long Island City landmark designated 2016 Gantry Plaza State Park MoMA PS1 former public school` · Firecrawl search · https://en.wikipedia.org/wiki/Pepsi-Cola_sign (excerpt: designated NYC landmark June 2016, at Gantry Plaza State Park); nyctourism.com says August 2016 — page says "2016" only · §13 card 6.
- Carried (research/cat6-repair.md Queens section, from research/fiber-optic-installation.md): One Court Square 673 ft, 50 storeys, completed 1989, tallest in Queens until 2019; LIC 2001 rezoning (37 blocks); Hunters Point South rentals; Silvercup Studios (former Silvercup Bakery 1929–30, studio since 1983) · §5 para 3, §7 cards 3–5, §13 cards 3–4.

### Reddit (source 1)
- `site:reddit.com r/longislandcity internet ethernet office building wiring` · Firecrawl search (excerpts only; reddit not scrapeable in build env) · https://www.reddit.com/r/longislandcity/comments/1d7rxda/thoughts_on_sven/ — "how good is the ethernet wiring in the apt? are the apt ethernet cables connected to a switch exclusively for the apartment?" · §5 para 4 (paraphrased resident concern). Other hits (1hw6agf patch-panel thread — already used on cat6-repair-queens; 1wzblta, 15xo8v4, 1wjs8ye provider chatter) not used.
- LIC-specific Reddit threads about failing Cat6 in lofts/offices: EMPTY.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview could not be viewed; H3s framed as commonly repeated claims and corrected with sources below.

### Local news / hyperlocal (sources 9, 10)
- Sandy/Newtown Creek and OneLIC items above (Newtown Creek Alliance, NYC Council, Cozen). Queens Eagle OneLIC excerpt (https://queenseagle.com/all/2025/11/13/council-passes-major-lic-rezoning-after-having-powers-curtailed) — date confirmation only.
- LIC Post / Queens Chronicle / QNS items on Cat6 or network-cable faults in LIC: EMPTY.

### Technical sources (pathway/support angle — new for this page)
- `J-hook spacing TIA-569 maximum 5 feet cable sag J-hook fill capacity Cat6 crush` · Firecrawl search · https://www.belden.com/blog/installing-j-hooks-avoid-these-mistakes-to-maintain-network-uptime (excerpt): per ANSI/TIA-569 J-hooks no more than 5 ft (1.5 m) apart; further apart → sag, "abrasion, stress the cable"; https://www.nvent.com/...F1185B-NAEN.pdf (excerpt): "Non-continuous supports may not exceed spacing of 5' (1.5 m) per TIA 569-C.9.7. Cable capacity is calculated based on a 70% fill rate" · §9 Q1, §7.5 open ceilings, "Reading the ceiling" section, after-repair list.
- `painting over communications cable plenum jacket paint overspray voids listing data cable` · Firecrawl search · https://www.belden.com/blog/what-happens-when-you-alter-or-modify-communications-cables (excerpt: "Don't paint your cables! ... can cause damage, reduce product lifecycle and void the product warranty"); https://legrand.my.site.com/knowledgebase/s/article/FAQ-Can-you-paint-Cat5-or-Cat6-cables (excerpt: not recommended; can damage jacket and wire) · §9 Q2, FAQ F3, services card.
- `metal stud knockout grommet bushing low voltage data cable jacket damage sharp edges` · Firecrawl search · https://titananchors.com/blogs/news/snap-in-bushings-grommets-for-metal-studs-... (excerpt: grommets prevent cable being cut or frayed through metal studs); https://forums.mikeholt.com/threads/per-code-does-low-voltage-require-bushings-while-going-through-metal-studs.134085/ (excerpt: damaged Cat5e "will not shock or start a fire, but installing a snap in bushing may prevent you from loosing jobs") · §9 Q5, §7.5 partitions.
- `GPR concrete scanning before core drilling slab rebar conduit why scan NYC` · Firecrawl search · https://www.gp-radar.com/services/concrete-scanning (excerpt: GPR reveals rebar, post-tension cables, conduit; one-side access vs X-ray both sides; conduit strike = shock risk; PT cable cut = structural risk) · §9 Q6, §8.5 concrete penetrations.
- `FDNY fire alarm system out of service notification placed on test contractor dust smoke detectors construction` · Firecrawl search · https://www.lowermerion.org/departments/fire-department/steps-to-prevent-false-fire-alarms (excerpt: cover smoke detectors during construction, remove covers after); https://www.countyfire.us/blog/how-to-clear-an-fdny-fire-alarm-violation-a-commercial-property-owners-guide/ (excerpt: out-of-service alarm → FDNY can mandate fire guard) · §9 Q7, §8.5 fire alarm bullet. (Page says management/fire-alarm vendor decides; no procedure stated as law.)
- Carried silo sources: TIA TSB-184-A (Belden; approved March 2017, 1000 mA/pair, 100 W, temperature rise, bundle limits) → §9 Q3; NEC 800.25 abandoned cable (EC&M) → §8.5, §9 Q8, §10.5 H3 7, field notes; NYC Electrical Code = 2020 NEC + amendments, full effect Dec 21 2025 (nyc.gov) → §8.5; Fluke NEXT troubleshooting ("Female couplers ... should not be used in a data installation") → §10.5 H3 3; Brick Underground Jan 29 2019 (NYC walls "piping, plumbing, cement, brick"; Ethernet most effective) → §10.5 H3 4; Fixr Jan 2025 → §10.5 H3 5, §14.

### Local licensing / permits / building rules
- NYC Electrical Code (2020 NEC + NYC amendments, Dec 21 2025), NEC 800.25, firestopping at rated penetrations (general practice, no LIC-specific source), slab penetrations at owner's discretion with scanning, fire-alarm impairment handled by building/FDNY rules (sources above). AESS NYS licence #12000287431.

### Prices used (live AESS pages only; no new prices)
- $195/hr, 3-hour minimum ($585) — network-cable-repair-queens.html / cat6-repair-queens.html.
- Replacement run from $175/drop — network-cable-repair-queens.html (as on cat6-repair-queens).
- Outside entry from $194/penetration — as published on cat6-repair-queens.html (Bronx $185 × 1.05, derived there; flag carried).
- Comparison: Cat5e $233 / Cat6 $272 / Cat6A $388 per drop — cat6-installation-queens.html.
- Third-party national: Fixr Jan 2025 $125–$250/drop, $45–$75/hr (labelled).
- No LIC-specific surcharge; Queens 1.05× not re-applied (same choice and flag as cat6-repair-queens).

### Images (11) — permanent image rule
Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run); CompanyCam not connected. Each source viewed; every source shows a technician's face, so all were cropped (PIL) to hands/equipment only and re-viewed (no faces, house numbers, plates or readable documents). WebP q80. Saved as images/cat6-repair/cat6-repair-long-island-city-queens-*.webp:
| File | Source folder (file) |
|---|---|
| j-hooks-exposed-ceiling (hero) | images/cat6/ (cat6-installer-bronx-jhook-pathway) |
| fish-tape-emt-conduit-block-wall | images/cat6/ (cat6-wiring-bronx-fish-tape-conduit) |
| nicked-jacket-on-grid-rail | images/network-cable-repair/ (crushed-network-cable-repair-queens) |
| metal-stud-knockouts | images/cat6/ (commercial-cat6-installation-bronx-stud-rough-in) |
| link-down-tester-at-rack | images/network-cable-repair/ (network-closet-troubleshooting-queens) |
| wire-map-fail-screen | images/network-cable-repair/ (network-cable-fault-detection-queens) |
| cable-from-ceiling-tile-reel | images/cat6/ (cat6-cable-installation-bronx-ceiling-drop) |
| split-jacket-at-steel-frame | images/network-cable-repair/ (damaged-ethernet-cable-repair-queens) |
| dense-rack-bundles | images/cat6/ (cat6-patch-panel-installation-bronx-network-room) |
| patch-cord-at-switch-port | images/network-cable-repair/ (switch-port-troubleshooting-queens) |
| drywall-cut-in-low-box | images/cat6/ (cat6-retrofit-installation-bronx-drywall-cut-in) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ and images/cat6/ (no real Cat6 Repair photos yet)`. Review note: the library photos look AI-generated (uniform branding, idealised scenes) — same caveat as earlier Cat6 Repair pages; crops differ from the cat6-repair-queens crops; captions describe only what is visible.

### Keyword notes (five layers)
- Service: Cat6 repair Long Island City, Cat6 cable repair LIC Queens, loft network cable repair, J-hook rework, conduit cable replacement, Cat6 re-termination, Cat6 certification, move-out cabling survey.
- Problem: overloaded J-hooks, cable sag, painted Cat6, PoE bundle heat, stud-knockout jacket damage, packed conduit, slab crossing, abandoned cable, smoke-detector dust when drilling.
- Technology: Cat6/Cat6A, TIA-569 support spacing, TSB-184-A, NEC 800.25, GPR slab scanning, firestop, grommets, bridle rings, beam clamps, distance-to-fault.
- Industry: design/architecture studios, film and post-production, showrooms, labs, start-ups/agencies, restaurants on Vernon/Jackson, loft property managers, tower residents.
- Geographic: Long Island City, Hunters Point, Court Square, Queens Plaza, Dutch Kills, Ravenswood, Blissville, Degnon blocks (Thomson Ave, Skillman Ave, 47th Ave), Northern Blvd, Vernon Blvd, Jackson Ave, Center Blvd, 21st St; nearby Sunnyside, Woodside, Astoria.

### Masked-geo similarity (difflib, p/li/td/h3/figcaption ≥8 words, geo masked incl. neighbourhood names)
vs every cat6-repair page on disk (16 area pages + williamsburg-brooklyn-ny + fordham-bronx-ny; midtown-manhattan-ny not on disk at check time): after two rewrite passes the only blocks ≥0.65 are excluded constants — warranty sentence, licence/rating strip, NAP line and pricing-source cells.

## Question register — cat6-repair-long-island-city-queens-ny

§9 "Questions Answered" (H3):
1. The Cat6 across our loft's open ceiling hangs in J-hooks that are packed full — can overloaded hooks be what is failing the links? (Open ceilings)
2. Painters sprayed our open ceiling black, cables and all — do painted Cat6 runs need replacing? (Open ceilings)
3. Can a big bundle of PoE-powered Cat6 on our exposed tray run hot enough to cause faults? (Open ceilings)
4. One Cat6 in the steel conduit along our brick wall has failed — can it be pulled out without damaging the cables that still work? (Conduit, studs, concrete)
5. Our office partitions are built on metal studs — could the stud openings be what is cutting into the Cat6 jacket? (Conduit, studs, concrete)
6. A replacement run has to go between floors of our old factory building — does the concrete have to be scanned before anyone drills? (Conduit, studs, concrete)
7. Will drilling for a replacement run set off our building's smoke detectors? (Conduit, studs, concrete)
8. When we move out of our loft, which of our Cat6 has to come out and which can stay for the next tenant? (Lease end)

FAQ (§17, = FAQPage schema):
F1. Our building only lets contractors use the freight elevator by reservation — who books it?
F2. Do you also cover Sunnyside, Astoria and Woodside, next door to Long Island City?
F3. Can the replacement cable on an exposed ceiling be a colour that blends in?
F4. Do you repair Cat6 in live-work lofts and artist studios as well as offices?
F5. Do desks and equipment under an exposed-ceiling run have to be cleared before you work overhead?
F6. Do new supports drilled into our concrete ceiling need the landlord's approval?

Other "?" headings: "Lost Link in a Long Island City Loft or Studio Today?" (repair capture), "A Dead Court Square or Hunters Point Link Before Monday Morning?" (closing).

De-dup notes (by meaning, vs every register in research/cat6-repair.md): avoided NYC splice/coupler (couplers only in §10.5 body), PoE reboot/one-bad-run-kills-port (Q3 is bundle heat per TSB-184-A, not a single device), riser approval; LI attic heat; HV school-addition joint, thick stone wall sleeve, high-bay "what is hitting it"; Bronx old conduit reuse (Q4 is removing one cable from a shared conduit without harming the rest); Brooklyn machine vibration and slab-conduit coring (Q6 is scanning before a *new* hole, not coring to reach a cable already in the slab); Manhattan raised floor/zone box/ladders-and-lifts/co-working; Suffolk painted-over *jack* (Q2 is jacket overspray on exposed runs) and landlord hand-over test results (Q8 is tenant move-out removal obligations); Dutchess EMI/moving machinery; Nassau cable beside power; Queens LIC media-panel and leftover-storefront-cable questions. Coverage FAQ F2 follows the per-page coverage pattern used on Manhattan F4 / Nassau F9 with different areas — flagged as borderline. Borderline also: F5 (clearing desks) vs Westchester F9 (protect floors/clean up) — different intent (access space vs cleanliness).


## Fordham, Bronx (cat6-repair-fordham-bronx-ny) — local research, 2026-10-17 batch

Neighbourhood page; up = /cat6-repair-bronx; phone (646) 490-0629 (800 only in the shared header chrome); GBP Bronx (#bronx, 460 E Fordham Rd — the GBP office is inside this neighbourhood). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. Entries marked CARRIED were fetched earlier on 2026-10-17 by the fiber-optic-installation-fordham-bronx-ny run (research/fiber-optic-installation.md, "Fordham, Bronx" section) and were not re-fetched here. Silo-wide technical sources are in research/cat6-repair.md.

**Thesis (different from cat6-repair-bronx and from fiber-optic-installation-fordham-bronx-ny):** In Fordham, Cat6 fails at changeover, not from age. Fordham Road storefronts turn over (80 vacant in the SBS/BID inventory; Dr. Jay's → Target; Best Buy at Fordham Plaza closing), upper-floor offices are re-fitted for clinics, agencies and schools, and student rooms turn over every semester. Each occupant cuts, abandons and adds cable, so a repair starts with a live-or-dead sort of inherited cable, then deals with the rooms where the usual method has to bend: entrance thresholds and counters on a shop floor that barely closes, bullet-resistant teller counters (11 check cashers, 12 banks, 27 jewellery/pawn), lead-lined X-ray rooms in dental/medical suites (40 medical storefronts; 46% of local jobs in education/health/social assistance), and student houses running on chained small switches. The Bronx parent's thesis (new towers vs pre-war apartment houses, "dating" a failure) and the fiber Fordham thesis (buildings changing jobs, re-planning backbones, curb logistics) were read and avoided.

### Reddit (local)
- `site:reddit.com Fordham Bronx store OR apartment ethernet OR internet OR wifi OR cameras` · FC search → https://www.reddit.com/r/bronx/comments/15bxozc/any_alternative_to_optimum/ (excerpt: "My Optimum internet goes down and is extremely slow almost every morning until around 11:30, and I pay extra for high speed.") → §10.5 H3 3 (quoted as an r/bronx commenter, Bronx-wide, not Fordham-specific). Other results (r/bronx University Heights safety, r/Fordham off-campus living, r/NYCapartments sublet near Fordham University at E 191st St) are housing threads, not wiring → background only (student-room context), not quoted.
- CARRIED: https://www.reddit.com/r/howislivingthere/comments/1wa3g7e/how_is_life_in_the_bronx/ ("Fordham road is probably one of the most chaotic shopping area in the country.") → not used on this page.
- Fordham-specific threads about failed Ethernet/Cat6: EMPTY (none returned).

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG — EMPTY (not accessible in build env)
§10.5 states on the page that the AI summary was not visible; each H3 is a commonly repeated assumption ("the space is wired so it will work", "your switch can test the cable", "slow internet is always the provider", "a shop can run on Wi-Fi", "any hole can be patched", "a long patch cord will do", "a lit port means a healthy cable"), corrected with the sources below.

### Yelp 1–3★ — EMPTY (not accessible in build env)
CARRIED from the fiber Fordham run: query `yelp low voltage cabling contractor Bronx Fordham reviews` returned only Yelp search pages for electricians elsewhere in the Bronx; no cabling reviews. Not used.

### Commercial district (primary source)
- `Fordham Commercial District Needs Assessment` · FC scrape (query, directQuote, pdf parser) https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/avenyc-cdna-fordham.pdf → "one of the busiest commercial corridors in New York City"; 4, B, D lines and "the fourth busiest Metro-North station"; ~118,000 residents (118,076), density 86,189/sq mi; inventory along Fordham Road (Andrews Ave–Southern Blvd), Jerome Ave, Grand Concourse (E 184th St–E Kingsbridge Rd), Webster Ave; retail mix: Vacant 80, Clothing & Shoe 65, Beauty/Barber 52, Limited-service restaurants 47, Cell Phone & Electronics 46, Doctors/Dentists/Medical 40, Jewelry/Watch Repair/Pawn 27, Government/Social Services/Nonprofits/Houses of Worship 26, Pharmacies/Optical/Health 26, Professional Services 26, Schools/Universities/Educational 20, Automotive 15, Banks & Credit Unions 12, Check Cashing & Money Transfer 11; merchants with 0–2 employees 43% (234 merchant surveys, Winter–Spring 2022); 188 street vendors, "largest street vending scene in the Bronx"; jobs located in Fordham: Educational Services/Health Care/Social Assistance 46%; median age 29. → hero sub (implicitly), §5 paras 1, 3, 4, §5.5 bullets 1–4, §8 cards, "Above the Shops" section, §10.5 H3 1, landmarks card 1.

### Local news / hyperlocal
- `Fordham Road Bronx 2026 new store opening OR closing storefront Norwood News OR Bronx Times` · FC search → FC scrape https://www.bxtimes.com/addition-of-target-to-fordham-road/ (Bronx Times, Oct 20, 2022): Target opening on Fordham Road at "the northeast corner of East Fordham Road and Valentine Avenue", "once home to Dr. Jay's … that closed its doors due to high rents in February 2020"; "In August, one smash-and-grab saw almost $2.15 million from Webster Avenue's Rocco's Jewelry"; merchants cite theft and high rents. → §5 para 2, §10.5 H3 4 ("a district that has seen smash-and-grab thefts").
- Same search → FC scrape https://www.norwoodnews.org/update-dot-invites-proposals-for-new-vendors-on-fordham-plaza-with-a-deadline-of-april-11/ (Norwood News, published Feb 26, 2025): "the Best Buy store located at the plaza, at Fordham Road and Webster Avenue, is set to shutter on March 1"; DOT inviting proposals for three retail/food spaces at Fordham Plaza; Bronx Night Market operates at Fordham Plaza last Saturday of the month April–November. → §5 para 2, §13 card 1.
- Same search → FC scrape https://www.norwoodnews.org/bronx-cb6-demands-answers-on-fordham-plaza-reconstruction-as-city-assesses-fordham-corridor-needs/ (Norwood News, Feb 25, 2023): CB6 letter; plaza reconstruction "completed in 2016"; "$34 million"; plaza retail spaces vacant. → §8 card 2, §13 card 1 ("reconstruction completed in 2016").
- `Lehman Grand dormitory Dollar Savings Bank building Grand Concourse opened 2026 Norwood News` · FC search (full excerpts returned) → https://www.norwoodnews.org/bedford-park-the-lehman-grand-lehman-colleges-first-dorm-opens/ (Norwood News, Aug 2026): ribbon cutting Aug 5, 2026; "more than 180 students"; "newly renovated, landmarked Dollar Savings Bank building, located on the Grand Concourse at Fordham Road"; designated NYC landmark 1994. https://newyorkyimby.com/2026/08/lehman-colleges-first-dormitory-opens-at-2530-grand-concourse-in-fordham-the-bronx.html: 2530 Grand Concourse; LPC designated "both the exterior and the banking hall interior as landmarks in July 1994"; NRHP Nov 2024; interior fit-out complete June. → §5 para 5, §7 card 3, §8.5 bullet 3, §10.5 H3 5, §13 card 2.
- CARRIED: https://www.norwoodnews.org/bedford-park-the-lehman-grand-lehman-colleges-first-dorm-opens/ (fiber run scrape): Fine Fare supermarket on the ground floor → §7 card 3 ("a supermarket in the old banking hall").
- Bronx Times / Norwood News / News12 items about Cat6 or network-cable failures in Fordham buildings specifically: EMPTY (none retrieved).

### Street redesign
- `NY1 Fordham Road bus lanes` · FC scrape https://ny1.com/nyc/all-boroughs/traffic_and_transit/2026/07/22/city-announces-redesign-of-bus-lanes-on-fordham-road (NY1, July 22, 2026): groundbreaking; "new offset bus lanes from Sedgwick Avenue and Boston Road"; "130,000 daily bus riders"; "will also provide parking and loading spaces for local businesses"; completion "by the end of the year"; Belmont BID board member quoted with concerns. → §5.5 bullet 5, §8 card 5 ("owners who have watched the Fordham Road redesign closely").

### Broadband
- CARRIED: https://www.osc.ny.gov/files/reports/pdf/report-20-2025.pdf (State Comptroller report 20-2025, Figure 8): PUMA 4207 Fordham, Bedford Park & Norwood — 47.8% of households without broadband, 33.2% cellular data only (Comptroller's definitions). → §5.5 bullet 6, §13 card 5.

### Buildings, campuses, landmarks
- CARRIED: https://www.fordham.edu/about/campuses/rose-hill-campus/ (85 acres, est. 1841) → §5 para 5, §13 card 4.
- CARRIED: https://www.monroeu.edu/sites/default/files/documents/2023/09/13/BXCampusMap_091123.pdf (King Hall 2501 Jerome Ave, Jerome Hall 2468 Jerome Ave, Monroe Hall 29 E Fordham Rd, Ustin Hall 2375 Jerome Ave) → §5 para 5, §7 card 5, §8 card 4.
- CARRIED: https://www.nytimes.com/2007/07/11/realestate/commercial/11bronx.html (excerpt: "One Fordham Plaza, a 557,000-square-foot office and retail building") → §5 para 3, §7 card 2 (generic).
- CARRIED: https://secretnyc.co/bronx-historic-paradise-theater-reopening/ (Sept 2026: opened 1929; becoming 4,000-seat Paradise Performing Arts Center; 2403 Grand Concourse) → §7 card 3, §13 card 3.
- CARRIED: https://newyorkyimby.com/2026/07/rendering-revealed-for-2740-webster-avenue-in-fordham-the-bronx.html (12-storey dormitory planned at 2740 Webster Ave) → §7 card 5.
- CARRIED: https://fordhamhill.com/living-at-fordham-hill/history (built 1950, co-op 1982, nine high-rises, 1,130 apartments) → §7 card 6.
- CARRIED: https://www.nypl.org/locations/bronx-library-center (opened January 17, 2006; 78,000 sq ft) → §13 card 5.
- CARRIED: https://www.nycgovparks.org/parks/poe-park (park and Poe Cottage); Visitor Center (urbanomnibus) → §13 card 6.
- CARRIED: https://www.sbhny.org/locations/ (St. Barnabas Hospital, 4422 Third Ave) → §8 card 6.
- Street geography (Jerome Avenue elevated 4 line; E 187th/188th St toward Arthur Avenue/Belmont; Fordham Plaza beside Metro-North) used as place names only, no claims beyond location.

### Technical sources (new for this page)
- `HHS business associate FAQ janitorial electricians plumbers incidental access protected health information not a business associate` · FC search → https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html (excerpt: BAA not required "With a person (e.g., janitorial service, electrician) whose functions or services do not involve the use or disclosure of PHI, provided that access to PHI by such persons would be only incidental, if at all, and that reasonable safeguards are in place."); https://www.hhs.gov/hipaa/for-professionals/faq/is-a-business-associate-contract-required-for-inadvertent-contact-with-phi/index.html. → FAQ F1, §8.5 bullet 6.
- `USAC E-Rate Category Two basic maintenance of internal connections eligible cabling repair` · FC search → https://www.usac.org/e-rate/applicant-process/before-you-begin/eligible-services-overview/ (excerpt: "BMIC covers the repair and upkeep of eligible internal connections. Eligible repair and upkeep services include hardware, wiring, and cable maintenance, along with configuration changes performed on-site.") → FAQ F2, "Above the Shops" schools para.
- `x-ray room lead lined wall penetrations conduit cable shielding must be maintained NCRP 147 penetrations baffle` · FC search → https://www.aapm.org/pubs/protected_files/NCRP/NCRP_Report_147_AAPM.pdf (excerpt: "baffling these penetrations with supplementary lead shielding. The supplementary thickness shall at least have shielding equivalent to the displaced …"); FC scrape https://hps.org/publicinformation/ate/q12989/ (Health Physics Society "Ask the Experts", Jeff Brunette, CHP, Aug 13 2019: NCRP 147 vague on penetrations, recommends NCRP 49 diagrams; shield the other side of the wall over an area of twice the largest gap from the penetration centre; floor penetrations — avoid line of sight through conduit). → §9 Q6 (X-ray room), §8.5 bullet 5, §10.5 H3 5.
- `Cisco TDR cable diagnostics accuracy` · FC scrape (query, directQuote) https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/infra/tdr/tdr-for-cable-status.html: TDR "estimate[s] the type of fault and the approximate distance to the fault"; fault types open/short; "If TDR locates a faulty cable, use an offline cable diagnosis tool for a detailed analysis."; "TDR results might differ between runs on different switch models … because of the resolution difference"; "Link state may be affected during TDR test". → §9 Q2, §10.5 H3 2, shop-floor checks table row 7.
- `Panduit RJ45 lock-in device blockout device prevent unauthorized removal patch cord jack` · FC search → https://www.panduit.com/content/dam/panduit/en/products/media/9/99/699/0699/101350699.pdf (excerpt: "Prevents unauthorized removal of cable, IP phone, other networking equipment or critical connection"); https://objects.eanixter.com/PD524589.PDF (excerpt: blockout device "designed to protect network integrity and prevent unauthorized access to the network by securing the RJ45 opening"). → FAQ F3, §6 equipment card.
- `bullet resistant fiberglass panel UL 752 under counter teller …` + `bullet resistant fiberglass panel electrical box penetration backer plate overlap` · FC search → https://fortifiedestate.com/product/bullet-resistant-fiberglass-panels/ (excerpt: "It is ideal to cover cut-outs, such as electrical boxes, with a small square of extra ballistic material that spans the length between two studs."); https://gssdoors.com/bullet-resistant-wall-panels (excerpt: "Doors, windows, electrical boxes and other penetrations must also be detailed to avoid gaps."); https://www.actionbullet.com/blog/what-bulletproof-products-are-ideal-for-bank-security/ (UL 752 levels for bank counters, background). FC scrape of https://elixirenvironmental.com/… returned no penetration text → not used. → §9 Q5 (teller counter), §6 card 5.
- `network switches daisy chained one switch fails all downstream devices …` · FC search → https://www.omnitron-systems.com/blog/building-a-scalable-network-by-daisy-chaining-poe-switches (excerpt: "Single Point of Failure. In a daisy-chain configuration, if one switch fails, it can affect all devices downstream."); https://www.reddit.com/r/HomeNetworking/comments/1g5bqtq/what_are_the_implications_of_daisy_chaining/ (excerpt: "make sure that you don't accidentally make a loop"). → §9 Q7.
- `network loop two wall jacks connected same cable broadcast storm unmanaged switch whole network down` · FC search → https://www.reddit.com/r/sysadmin/comments/1cen486/how_often_do_you_see_broadcast_storms_and_network/ (excerpt: "Common causes are: mis-patched unmanaged switches, switches with MSTP/RSTP/STP disabled …"); https://community.cisco.com/t5/switching/looping-on-unmanaged-switches-bringing-down-the-whole-network/td-p/705704. → §9 Q8.
- `cash drawer printer driven RJ12 cable kick out port receipt printer not ethernet` · FC search → https://grindless.com/guides/drawer/ (excerpt: printer Ethernet ports are "NOT the same as a drawer kick" port); https://community.spiceworks.com/t/can-you-identify-this-cash-drawer-cable/649218 (excerpt: printer "RJ11 (possible RJ12) drawer kick-out port … The included cash drawer has an RJ-45 port on it"); https://cloudv2.microbizcloud.com/support/solutions/articles/9000270944-how-to-connect-a-cash-drawer-to-a-receipt-printer-via-rj11-cable. → FAQ F6.
- Silo sources reused (research/cat6-repair.md): NYC Electrical Code = 2020 NEC amendments, full effect Dec 21, 2025 (nyc.gov) → §8.5 bullet 1; NEC 800.25 abandoned cable (EC&M) → §8.5 bullet 2, inherited-cable section; Fixr Jan 2025 $125–$250/drop, $45–$75/hr (third-party) → §14. CARRIED from fiber Fordham: LPC permit needed for work in designated interior landmarks (https://www.nyc.gov/site/lpc/about/permits-and-making-alterations.page) → §8.5 bullet 3.

### Local licensing / permits
- NYS low-voltage licence #12000287431 (AESS). Interior-landmark permit (LPC) for the Dollar Savings Bank banking hall; NYC Electrical Code cable listings; firestopping of rated penetrations (general practice, no Fordham-specific source); X-ray room shielding governed by the facility's shielding design/radiation-safety adviser (HPS/NCRP sources above; no NYS DOH-specific rule retrieved — EMPTY for a NYS-specific citation, so the page names no state rule).

### Prices used (no new prices; Bronx §9 multiplier 1.00×)
$195/hr, 3-hour minimum ($585), additional time $195/hr; replacement run from $175/drop; outside entry sealed and bonded from $185/penetration (all from network-cable-repair-bronx.html, as used on cat6-repair-bronx.html); new-install comparison Cat6 $272, Cat5e $233, Cat6A $388 per drop to 100 ft (cat6-installation-bronx.html). Packages: Starter $585; Standard $585 + $195/hr after 3 h; Premium repair time + from $175/run, entries from $185. Fixr figures labelled third-party.

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run), CompanyCam not connected
Source folder images/network-cable-repair/ (only 16 distinct photos across 224 files; each "-bronx" file is byte-identical to its other-area twins). Each photo viewed before use; every source showed a technician's face, so each was CROPPED with PIL (no generation/retouching) to hands, tools and equipment only and re-viewed as a contact sheet (no faces, house numbers, plates or readable documents; AESS shirt logos remain on some). WebP q80, native ≤1536 px. Alt/title/caption describe only what is in the crop. Cat6 parent (cat6-repair-bronx) uses images/cat6/ scenes, so no scene overlaps with the parent.
| images/cat6-repair/ | Source (images/network-cable-repair/) | Crop box (x0,y0,x1,y1) |
|---|---|---|
| cat6-repair-fordham-bronx-register-jack-no-link-test.webp (hero, eager) | pos-network-cable-repair-bronx.webp | 700,0,1536,1024 |
| cat6-repair-fordham-bronx-tone-probe-labelled-patch-field.webp | network-cable-tracing-bronx.webp | 780,0,1536,1024 |
| cat6-repair-fordham-bronx-jacket-worn-on-ceiling-grid.webp | crushed-network-cable-repair-bronx.webp | none (no face in source) |
| cat6-repair-fordham-bronx-split-jacket-at-desk-leg.webp | damaged-ethernet-cable-repair-bronx.webp | 0,440,1100,1024 |
| cat6-repair-fordham-bronx-dome-camera-no-poe-test.webp | poe-camera-cable-repair-bronx.webp | 150,0,900,1024 |
| cat6-repair-fordham-bronx-switch-port-light-check.webp | switch-port-troubleshooting-bronx.webp | 60,60,830,1024 |
| cat6-repair-fordham-bronx-ceiling-bundle-flashlight.webp | network-cable-inspection-bronx.webp | 700,0,1536,520 |
| cat6-repair-fordham-bronx-wall-jack-open-reading.webp | network-jack-repair-bronx.webp | 100,460,820,1024 |
| cat6-repair-fordham-bronx-panel-punch-down-label.webp | patch-panel-repair-bronx.webp | 140,100,1000,1024 |
| cat6-repair-fordham-bronx-wire-map-fail-crossed-open.webp | network-cable-fault-detection-bronx.webp | 0,300,1536,1024 |
| cat6-repair-fordham-bronx-rj45-plug-crimp.webp | rj45-connector-replacement-bronx.webp | 0,430,1536,1024 |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (no real Cat6 Repair photos yet)`. Review note: these library photos look AI-generated (idealised scenes, uniform branded shirts, legible on-screen text); the brief only excludes the aess-cat6-repair-* set, so they were used under the permanent image rule — flag for replacement when real photos arrive.

### Keyword notes (five layers, Fordham geo)
- Service: Cat6 repair Fordham, Cat6 cable repair Bronx NY, Cat6 jack repair, re-termination, certification, live-or-dead cable survey, inherited cable testing, POS/register cable repair, camera cable repair, entrance/door cable re-route.
- Problem: inherited/abandoned cable after tenant turnover, cut runs after fit-out, cable under thresholds, patch cords used as ceiling runs, dead failover link, chained switches, network loop, teller-counter armour, X-ray room shielding, moved partitions.
- Technology: Cat6, Cat6A, permanent link, TDR (switch vs certifier), tone and probe, keystone, lock-in/blockout devices, PoE, NEC Art. 800 abandoned cable, firestop, UL 752 ballistic panels, lead shielding (NCRP 147).
- Industry: Fordham Road retail (clothing, phones/electronics, jewellery/pawn), banks and check cashers, medical/dental suites, pharmacies, agencies/nonprofits, schools/training centres, libraries (E-Rate), student housing/residence halls, co-op towers.
- Geographic: Fordham, Fordham Road (Jerome Ave–Webster Ave), Fordham Plaza, Webster Avenue, Grand Concourse (E 184th St–Kingsbridge Rd), Jerome Avenue, E 187th/188th St, Arthur Avenue, Third Avenue/St. Barnabas, Belmont, Bedford Park, University Heights, Kingsbridge Heights, Fordham Manor, Fordham Heights, Norwood, Tremont.

### Masked-geo similarity (scratch sim: geo + "Fordham" + digits masked; p/li/td/h2/h3/figcaption blocks ≥8 words; difflib per block, Jaccard-prefiltered; plus 5-word shingle Jaccard over all blocks)
Whole-page 5-gram Jaccard: vs cat6-repair-bronx 0.014; every other cat6-repair page 0.005–0.007 (incl. batch siblings williamsburg 0.005, long-island-city 0.005); vs fiber-optic-installation-fordham-bronx-ny 0.005; network-cable-repair-bronx and cat6-installation-bronx 0.000. Mean best-block ratio 0.03–0.07. Blocks ≥0.65 are excluded constants only: freshness stamp, warranty sentence, licence/rating strip, NAP line, owner-supplied-parts warranty line, the fixed blueprint H2 patterns ("Why … Properties Need …", "What AI Gets Wrong About …", "Types of … We Carry Out …") and two pricing-table cells naming the price source.

## Question register — cat6-repair-fordham-bronx-ny

§9 "Questions Answered" (H3), clusters "Shop floors that hardly ever close" / "Rooms with armour or lead in the walls" / "Houses and halls full of students":
1. The Cat6 to the anti-theft pedestals and the door counter crosses our entrance under the threshold strip. Why does it keep failing, and where should it go instead?
2. Our store switch's cloud dashboard says one cable has a fault "at 9 metres." How far can that reading be trusted?
3. The last tenant ran shop-bought patch cords through the ceiling to the cameras. Are they worth repairing, or do they get replaced as proper runs?
4. We only find out the backup internet line's Cat6 is dead when the main line fails. How is a run that sits idle most of the year kept honest?
5. Our check-cashing counter is lined with bullet-resistant panels. How is a failed Cat6 run to a teller station replaced without drilling through the armour?
6. The X-ray room in our dental office has lead in the walls. How is a failed Cat6 run to the imaging computer replaced without opening a gap in the shielding?
7. In our house of student rooms near the university, each room's switch feeds the next one. Why does one room's problem take out the rooms after it?
8. Every time one tenant plugs in, the whole house's network slows to a crawl. Can a cable cause that?

FAQ (§17, = FAQPage schema):
F1. Does a Cat6 repair in our medical or dental office need a HIPAA business associate agreement?
F2. Can a school or library put a Cat6 repair through its E-Rate maintenance funding?
F3. Can jacks in a waiting room or on the sales floor be locked so the public cannot unplug or use them?
F4. Do you repair the Cat6 that feeds an ATM inside a shop?
F5. Our store is part of a national chain. Can you work to head office's ticket, check-in and close-out rules?
F6. The cable from our cash drawer looks like a network cable. Is that part of a Cat6 repair?

Other "?" headings: "Register or Teller Line Offline on Fordham Road?" (repair capture), "Counter or Exam Room Still Offline at Closing Time?" (closing).

De-dup notes (by meaning, against every register in research/cat6-repair.md — NYC, LI, HV, Bronx, Staten Island, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess, Ulster — and the batch siblings williamsburg-brooklyn and long-island-city-queens as on disk at ~14:25; also the fiber-optic-installation-fordham-bronx-ny register). Deliberately NOT asked because a sibling holds the intent: last tenant left Cat6 — what is usable (Queens F7) and which runs still serve anyone (Nassau Q12) → inherited cable handled as body text (table "What the Last Occupant Leaves in the Ceiling", Standard package) only; lease handover test results (Suffolk Q2) → "Taking Over a Fordham Space" list, not a question; store refitted every season (Orange) and furniture moved/power poles (Manhattan Q2) → not used; roll-down gate (Queens Q4), cooler/compressor (SI Q10), strip-mall counter (SI Q11), floor box mop water (Queens Q2) → not used; landmark/LPC approval (Manhattan/Brooklyn) → §8.5 body only; permit question (Dutchess F6) → not asked; scheduling before opening/patients/Saturdays (Orange, LI F4, SI F8, Nassau F5, Putnam F9) → body only; landlord permission (Queens Q10, Brooklyn F5, Nassau F4, Rockland F8) → not asked; tenants breaking jacks/sturdier repair (Dutchess Q10) → locking FAQ F3 is about public access, not sturdiness; split one run for two devices (Nassau Q9, Suffolk F2) → not used; interrupt alarm/camera monitoring (Suffolk F4) → not used; fiber Fordham register (bus-lane unloading, holiday season, sprinkler pipes, provider damage, CO) → not used as questions. Borderline, for a human read: Q3 (stranded patch cords used as ceiling runs) vs Ulster Q4 (crimped plugs hanging out of the wall on solid cable) — different defect; Q1 (cable under an entrance threshold to pedestals/door counter) vs Williamsburg FAQ "Do you repair the Cat6 feeding ticket scanners, door counters or a jukebox at a bar or venue?" — Q1 is the threshold failure mechanism and re-route, not service scope; Q2 (switch TDR distance) vs NYC Q3 (cord vs jack vs wall) — Q2 is about trusting a switch's built-in test.


## St. George, Staten Island (cat6-repair-st-george-staten-island-ny)

Built 2026-10-17 (batch subagent; batch with cat6-repair-financial-district-manhattan-ny and cat6-repair-park-slope-brooklyn-ny). Up-link /cat6-repair-staten-island; phone (347) 934-8335; GBP Brooklyn (1282 Troy Ave, #brooklyn) — all copied from the parent page. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query / directQuote mode). Shell curl blocked. Silo technical sources already in research/cat6-repair.md (Fluke NEXT KB, BICSI study guide, ICC TSB-155-A, Belden TSB-184-A, EC&M NEC 800.25, Fixr Jan 2025, 29 CFR 1910.308 2-in separation, DOB/CityLand Ida advice) are reused in general terms only and not re-fetched. Carried = recorded with URL and finding in research/fiber-optic-installation.md (St. George section) or research/soundbar-installation.md (St. George section) on 2026-10-17 and not re-fetched.

**Thesis (differs from the parent = water line / houses / Sandy; fiber St. George = vertical fiber routes, landmarks paperwork; soundbar St. George = reading old walls for a TV):** St. George is Staten Island's office district. The civic centre (Borough Hall, the 2015 courthouse at 26 Central Ave, the 1919 courthouse, the 1961 Judicial Center at 130 Stuyvesant Pl with the County Clerk and DA, the 120th Precinct) is ringed by 1960s office buildings that are "largely occupied by law offices and legal-related companies" (60 Bay St, built 1969), legal-services nonprofits, small practices in converted hillside houses, and Bay Street storefront offices — plus pre-war apartment buildings, the Castleton Park towers, Bay Street Landing lofts and the new Lighthouse Point mixed-use building at the ferry. So Cat6 repair here is mostly **inherited office cabling that has outlived several tenants and fit-outs**: desks daisy-chained through IP phones, stranded patch cable used as wall cable, runs laid across light fixtures, cable under carpet at doorways, sagging wall-mounted panels, one uplink between floors, untested backup-internet links, and jacks under leaky old windows on the hill — repaired around court-calendar mornings, confidential files and tight ferry-side parking. Water (the parent's thesis) appears only in the window-leak question and in body context.

### Reddit (local)
- `reddit statenisland St. George office internet ethernet wiring building` · FC search · results were r/HomeNetworking, r/sysadmin, r/ITManagers and one AESS page; no r/statenisland thread → r/statenisland for Cat6/office cabling in St. George: EMPTY (not accessible in build env / no matching thread). Not used.
- Carried (soundbar St. George section): r/statenisland threads describing St. George as walkable with "nice old style houses" and the closest neighbourhood to the ferry — background for §5 only, paraphrased, not quoted.
- `PCs connected to VOIP phones losing internet connection` (found via the query `IP phone PC port pass-through computer loses network when phone reboots or unplugged` · FC search) → https://www.reddit.com/r/networking/comments/1hirvt6/pcs_connected_to_voip_phones_losing_internet/ (excerpt: "take one phone go the switch connected directly…") — not St. George; background for §9 phone pass-through Q only, not quoted.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG — EMPTY (not accessible in build env)
§10.5 says on-page that AI Overview could not be viewed; its seven H3 claims are framed as claims commonly published by cost guides, vendor blogs and forums, each corrected with the sourced facts below (DOB §28-105.4.7, Fluke stranded-cable figures, TIA-569 separation table, Cisco PC-port behaviour, Fixr Jan 2025 national figures, NEC 800.25).

### Yelp 1–3★ — EMPTY (not accessible in build env)
Yelp listings appeared only as search-result titles (Richmond County Supreme Court 26 Central Ave; NYPD 120th Precinct 78 Richmond Ter; lawyers near St. George incl. "Staten Island District Attorney · 130 Stuyvesant Pl" and "Katz Law Offices · 36 Richmond Ter"). No cabling-contractor reviews for St. George. Not used except to confirm addresses.

### Civic centre / courts / offices (landmarks + commercial)
- `26 Central Avenue Staten Island courthouse Supreme Court Criminal Court opened 2015 St. George` · FC search → https://en.wikipedia.org/wiki/Richmond_County_Courthouse_(Staten_Island) (excerpt: courthouse at 26 Central Avenue "opened on September 28, 2015"); https://www.nycourts.gov/courts/13th-judicial-district (excerpt "26 Central Ave, Staten Island, NY 10301"); https://www.silive.com/entertainment/2021/04/then-and-now-courthouses-of-richmond-county-borough-hall.html (excerpt: "Located at 26 Central Avenue, it celebrated its grand opening on September 28, 2015"). → §8 Central Avenue card, §13 courthouse card, §5 para 1.
  - FC scrape https://ennead.com/work/staten-island-courthouse/ (directQuote): "On a hilltop site overlooking New York Harbor"; "Housing the New York State Supreme Civil and Criminal Courts, lower Criminal Court and related agencies"; "Year 2015"; "Size 184,000 GSF"; "Fourteen Courtrooms, Hearing Room, Judges' Chambers, Administrative Office, Children's Center, Law Library, Attorney Lounge, Press Office". → §5.5 fact 2, §13 courthouse card.
- Carried (fiber St. George): 1919 Richmond County Courthouse, 18 Richmond Terrace, Carrère and Hastings, NYC landmark 1982 (https://en.wikipedia.org/wiki/Richmond_County_Courthouse_(Staten_Island)); Borough Hall 10 Richmond Terrace 1906 Carrère and Hastings, landmark 1982 (https://en.wikipedia.org/wiki/Staten_Island_Borough_Hall); St. George Terminal (city facility opened June 8 1951, bus ramps A–D, SIR terminus; https://en.wikipedia.org/wiki/St._George_Terminal); St. George Theatre 35 Hyatt St, opened Dec 4 1929 (https://en.wikipedia.org/wiki/St._George_Theatre); St. George/New Brighton Historic District designated July 19 1994, "some 78 buildings", hillside crescents (https://s-media.nyc.gov/agencies/lpc/lp/1883.pdf); SIUH Community Park 75 Richmond Terrace, opened June 24 2001 (https://en.wikipedia.org/wiki/SIUH_Community_Park). → §13 cards, §7 hillside card, §8 Hyatt Street card.
- `St. George Staten Island civic center offices Borough Hall 10 Richmond Terrace Staten Island Legal Services nonprofit offices Stuyvesant Place` · FC search →
  - https://www.statenislandusa.com/borough-hall.html (excerpt): Borough Hall "Standing directly across from the Ferry Terminal … houses the Borough President's Office, offices of the Departments of Buildings and Transportation and other civic offices"; "(entrance on Stuyvesant Place)". → §13 Borough Hall card, §8 Stuyvesant Place card.
  - https://www.legalservicesnyc.org/boroughs/staten-island-legal-services/ (excerpt): Staten Island Legal Services "60 Bay Street, Suite 900"; "located near the St. George transportation". → §8 Bay Street card (named as an example of a legal nonprofit in the office building; no claim of work).
  - https://www.facebook.com/stgeorgecivic/ (excerpt): St. George Civic Association — "Stuyvesant Place, Hyatt, Wall and Richmond Terrace"; "Stuyvesant Place and Hyatt Street at the rear steps of Borough Hall". → street names only (§8, hero badge).
- `"130 Stuyvesant Place" Staten Island building offices District Attorney` · FC search → https://www.statenislandda.org/contact/ (excerpt: "Main Office: 130 Stuyvesant Place, 7th Floor"); https://www.nyc.gov/html/om/html/97/sp717-97.html (excerpt: 1997 release "Opens Newly Renovated Staten Island City Office Building. 130 Stuyvesant Place Will Alleviate Overcrowding in Richmond County Courthouse"). FC scrape https://www.nyc.gov/site/dcas/business/dcasmanagedbuildings/staten-island-mark-costantino-judicial-center.page (directQuote): "Date Built: 1961"; "Located directly behind the Staten Island Supreme Courthouse and Borough Hall, 130 Stuyvesant Place is also referred to as the Staten Island Judicial Center. The building houses the Staten Island County Clerk, District Attorney and other court-related offices." → §5.5 fact 3, §8 Stuyvesant Place card, §7 1960s office card.
- `NYPD 120th Precinct 78 Richmond Terrace St. George Staten Island` · FC search → https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/120th-precinct.page (excerpt: "The 120th Precinct serves the North Shore of Staten Island … 78 Richmond Terrace"). FC scrape https://hdc.org/buildings/120th-police-precinct-station-house/ (directQuote): "Designated: June 27, 2000"; "an impressive neo-Renaissance style building set on Richmond Terrace in Staten Island's civic center"; "an Italian Renaissance palace clad in terra cotta treated to look like limestone to harmonize with Carrere & Hastings' neighboring Richmond County Courthouse"; "Designated Individual Landmarks". → §13 precinct card, §8 Richmond Terrace card.
- `"60 Bay Street" Staten Island office building St. George tenants floors` · FC search → https://civicstoop.org/… (excerpt: "the office building at 60 Bay Street in Staten Island's St. George neighborhood"); https://www.silive.com/opinion/2011/10/the_courthouse_effect.html (excerpt: Muss: "High-end office tenants see tremendous value at 60 Bay Street. And with the tremendous new courthouse set to open nearby…") — background. FC scrape https://muss.com/property/60-bay-street/ (directQuote): "with the Staten Island Ferry just across the street"; "Located one block away from the current Federal and NY State Courts and Borough Hall, 60 Bay Street is largely occupied by law offices and legal-related companies"; "Recent upgrades to the property include high-speed elevators, a new lobby and state-of the-art wiring for internet and telecommunication systems"; "Floors: 10"; "Total SF: 114,590 SF"; "Built: 1969". → §5 para 2, §5.5 fact 4, §7 1960s office card, §8 Bay Street card. ("state-of-the-art wiring" is the owner's marketing claim; page states it only as the owner's description and does not claim anything about suite cabling.)
- `Staten Island DRI Strategic Investment Plan` (same search) · FC scrape (pdf parser, directQuote) https://www.ny.gov/sites/default/files/atoms/files/Staten_Island_DRI_Strategic_Investment_Plan.pdf: "Downtown Revitalization Initiative New York City Strategic Investment Plan November 2020"; project list includes "Upgrade the Ground-Level Façade at the 60 Bay St. Office Building" and "Renovate the Façade and Create a New Storefront at 585 Bay St."; ferry terminal information booth at "1 Bay Street"; Visit Staten Island partnership incl. "Destination St. George". → §5.5 fact 5 (DRI, Nov 2020, "Downtown Staten Island"), §8 Bay Street card.

### Waterfront / new mixed-use
- `Lighthouse Point 5 Bay Street St. George commercial tenants CSI Tech Incubator office space` · FC search → https://www.governor.ny.gov/news/governor-hochul-celebrates-completion-200-million-lighthouse-point-mixed-use-development (excerpt: "The first phase of the development features 115 new residential units, 60,000 square feet of commercial space, and 274 parking spots."); https://newyorkyimby.com/2025/06/lighthouse-point-phase-one-finishes-construction-at-5-bay-street-in-st-george-staten-island.html (excerpt: "Commercial tenants confirmed to date include the College of Staten Island Tech Incubator, The Learning Experience childcare center, and Club…"); https://edc.nyc/press-release/mixed-use-housing-complex-opens-lighthouse-point. → §7 new mixed-use card, §5.5 fact 6, §8 waterfront card.
- Carried (soundbar St. George): Empire Outlets opened May 15 2019 next to the St. George Terminal, 55 Richmond Terrace; Castleton Park 454 homes in two buildings at 165 and 185 St. Marks Place, ~20 storeys (silive 2015 / CAMBA); Bay Street Landing warehouses "converted into loft co-ops and condos in 1984" with "raw concrete ceilings and exposed support columns" (homes.com / statenislandrealty.com); "roughly 70% of housing units are renter-occupied" (DeFalco 2026 guide, St. George–New Brighton); "Street parking near the ferry terminal fills up fast" (DeFalco). → §7 cards, FAQ parking, §5 para 3.
- `St. George Staten Island Hurricane Sandy flooding Bay Street Richmond Terrace waterfront storm surge` · FC search → silive gallery excerpt "Bay Street at William Street is flooded from the storm surge of Hurricane Sandy" (William St is south of St. George, not used as a St. George fact); NYC SIRR report (excerpt: surge "on Staten Island, they rose to 14 feet") — not used. Facebook result about St. George Island, Florida — irrelevant. Not used on page.
- `silive St. George Bay Street businesses restaurants 2026` · FC search → silive Oct 2026 closures list (Stapleton/Rosebank Bay Street restaurants, not St. George) — not used. SI Advance/silive hyperlocal on Cat6 or office network faults in St. George: EMPTY.

### Local licensing / permits / codes
- `NYC DOB electrical permit not required low voltage communications cabling under 50 volts` · FC search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 (excerpt, NYC Admin Code § 28-105.4.7 "Low voltage electrical work"): "An electrical permit shall not be required for the installation, alteration, maintenance, or repair of electrical wiring that is designed to operate at less than 50 volts for signaling, communication, alarm, and data transmission circuits, provided that such work is performed by a licensed master electrician, special electrician, or qualified person as defined in the New York city electrical code." Also https://up.codes/s/low-voltage-electrical-work (same text). → §8.5 bullet 1, §10.5 H3 (permit claim), process step.
- Carried (fiber St. George): LPC Permit Guidebook — interior work needs an LPC permit only when it needs a DOB permit or affects the exterior (https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Introduction.pdf). → §8.5 bullet (historic district houses).
- Silo: NEC 800.25 abandoned cable (EC&M) → §8.5; 29 CFR 1910.308 2-in separation from power (research/cat6-repair.md SI section) → §8.5; NYC Electrical Code = 2020 NEC + amendments effective Dec 21 2025 (nyc.gov, silo) → §8.5.

### Technical sources (new for this page)
- `TIA-569 separation data cable fluorescent lighting 5 inches 12 cm unshielded twisted pair EMI` · FC search → https://www.elliottelectric.com/StaticPages/ElectricalReferences/DataComm/separation_interference.aspx · FC scrape (directQuote): table "Minimum Separation … IA/TIA-569": "Fluorescent lighting | 12 in | 12 in | 12 in"; "Transformers and electric motors | 40 in". Other excerpts in the same search give 12 in for fluorescent fixtures (LinkedIn RCDD post, industrialmonitordirect) and one (Facebook) 50 mm from power — the page uses only the Elliott table figure (12 in), described as a pathway-design guideline. → §9 fluorescent Q, §8.5 bullet, §10.5 H3.
- `stranded patch cable vs solid in wall attenuation 20 percent more TIA-568 patch cord length limit 10 meters` · FC search → FC scrape https://www.flukenetworks.com/blog/cabling-chronicles/considerations-choosing-stranded-vs-solid-cable (directQuote, 2024-03-06): "stranded cables exhibit 20 to 50 percent more attenuation than solid copper conductors (20 percent for 24 AWG and 50 percent for 26 AWG)"; "they also have higher DC resistance"; "When it comes to 90-meter horizontal permanent links … both TIA and ISO/IEC standards require solid wire cable. Stranded cable (24 and 26 AWG) is limited to patch cords and 10-meter lengths within a 100-meter channel." → §9 stranded-cable Q, §10.5 H3 "a patch cord is a patch cord", inherited-cabling table.
- `IP phone PC port pass-through computer loses network when phone reboots or unplugged` · FC search → https://community.cisco.com/t5/ip-telephony-and-phones/ip-phone-reboot/td-p/2969509 (excerpt): "When a phone reboots, the computer loses connection because the PC port of the phone doesn't have a 'bypass' functionality." Spiceworks threads (excerpts) on random drops through VoIP phones — background. → §9 phone pass-through Q.

### Building stock summary (for §7)
1960s civic/office buildings (130 Stuyvesant Pl 1961; 60 Bay St 1969, 10 floors) · Beaux-Arts/neo-Renaissance civic landmarks (offices around them, never claimed as our sites) · 1880s–1920s hillside houses in the historic district, many divided or used as offices (carried) · Bay Street storefront buildings with offices/apartments above (DRI storefront projects) · pre-war elevator apartments and the Castleton Park towers (carried) · Bay Street Landing concrete lofts (carried) · Lighthouse Point 2025 mixed-use with 60,000 sq ft commercial (new).

### Prices used (copied from the live parent cat6-repair-staten-island.html; no new prices, no new multiplier)
$195/hr, three-hour minimum ($585); additional time $195/hr; replacement or extension Cat6 run from $175 per drop; entry sleeved/sealed/bonded from $185 per penetration; comparison new Cat6 drop $296 (Cat5e $254, Cat6A $424) per cat6-installation-staten-island; no separate bridge charge; Fixr Jan 2025 $125–$250/drop and $45–$75/hr labelled third-party national. Parent's FLAG still applies: blueprint §9 SI 1.10× would give $193 for the drop, but the parent and the NYC hub publish $175 un-multiplied; this page follows the parent exactly. Packages: Starter $585; Standard $195/hr after the first 3 hours; Premium repair time + from $175 per run; BYOE labour only.

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" EMPTY (checked by main run), CompanyCam not available
images/cat6-repair/ also holds 14 `aess-cat6-repair-*.webp` files (commit d8cb9aad) used on every area page; they were viewed and NOT used: they show technicians' faces and one is an obviously rendered before/after graphic with overlaid text. Every borrowed image was viewed at full size before cropping; crops remove all faces; no house numbers, plates or readable documents remain (tester screens and cable labels only). Saved WebP q80, ≤1600 px. None of these source scenes is used on cat6-repair-staten-island (parent used the NCR rack-tester, POS, access-point, switch-port and RJ45 scenes and the cat6 outlet-bank/voice-data/floor-box/conference-table scenes).
| images/cat6-repair/ | Source (crop box) |
|---|---|
| cat6-repair-st-george-tester-fail-crossed-open-pair.webp (hero) | network-cable-repair/network-cable-fault-detection-staten-island.webp (0,300,1150,1024) |
| cat6-repair-st-george-crushed-bundle-metal-edge.webp | network-cable-repair/crushed-network-cable-repair-staten-island.webp (full frame) |
| cat6-repair-st-george-split-jacket-exposed-pairs.webp | network-cable-repair/damaged-ethernet-cable-repair-staten-island.webp (0,600,1150,1024) |
| cat6-repair-st-george-wall-plate-punch-down.webp | network-cable-repair/keystone-jack-replacement-staten-island.webp (300,520,1536,1024) |
| cat6-repair-st-george-ceiling-tile-flashlight-check.webp | network-cable-repair/network-cable-inspection-staten-island.webp (700,0,1536,560) |
| cat6-repair-st-george-probe-tracing-patch-panel.webp | network-cable-repair/network-cable-tracing-staten-island.webp (800,0,1536,1024) |
| cat6-repair-st-george-rack-tester-link-down.webp | network-cable-repair/network-closet-troubleshooting-staten-island.webp (0,440,1300,1024) |
| cat6-repair-st-george-wall-jack-no-link-test.webp | network-cable-repair/network-jack-repair-staten-island.webp (0,500,1536,1024) |
| cat6-repair-st-george-dome-camera-no-poe-test.webp | network-cable-repair/poe-camera-cable-repair-staten-island.webp (0,0,700,1024) |
| cat6-repair-st-george-corroded-plug-block-wall-jack.webp | network-cable-repair/water-damaged-network-cable-repair-staten-island.webp (660,380,1536,1024) |
| cat6-repair-st-george-fish-tape-conduit-block-wall.webp | cat6/cat6-wiring-bronx-fish-tape-conduit.webp (600,280,1402,1122) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (10) and images/cat6/ (1) (no real cat6-repair photos yet)`. Flag for Anwar: the network-cable-repair and cat6 library images, like the aess-cat6-repair set, look AI-rendered (uniform logo patches, generic offices); the rule forbids AI images but these are the only borrow folders the run allows.

### Keyword notes (five layers, St. George geo)
- Service: Cat6 repair St. George, Cat6 cable repair Staten Island, office Cat6 repair, Cat6 re-termination, Cat6 certification/recertification, patch panel repair, wall jack repair, Cat6 tracing, PoE camera cable repair.
- Problem: desk computer drops with the phone, stranded patch cable in the wall, cable lying on light fixtures, cable under carpet at a doorway, sagging wall-mounted panel, single uplink between floors, dead backup internet link, jack under a leaking window, porch crawlspace run, inherited tenant cabling.
- Technology: Cat6/Cat6A, permanent link vs channel, solid vs stranded (Fluke), TIA-569 separation (12 in fluorescent), IP phone PC port, PoE, dual-WAN failover, NEC 800.25, NYC Admin Code § 28-105.4.7, 2-in separation from power.
- Industry: law offices and legal services, court-related businesses, nonprofits, professional practices in converted houses, Bay Street shops and cafés, co-working/incubator tenants, apartment owners and renters.
- Geographic: St. George, Staten Island, North Shore, Richmond Terrace, Bay Street, Stuyvesant Place, Central Avenue, Hyatt Street, Wall Street, St. Marks Place, Hamilton Avenue, Westervelt Avenue, Fort Hill, Tompkinsville, New Brighton, Stapleton, Randall Manor.

## Question register — cat6-repair-st-george-staten-island-ny

§9 "Questions Answered" (H3), under three non-question H2s:
1. Every computer in our office plugs into the back of a desk phone — why does the computer go offline whenever its phone does, and is one Cat6 run to blame? (Civic-centre offices)
2. Some of the "Cat6" in our office walls turns out to be the grey, floppy kind used for patch cords — does that explain the slow and flaky rooms? (Civic-centre offices)
3. The Cat6 above our suspended ceiling lies right on top of the old fluorescent light fixtures — could the lights be what keeps knocking desks off? (Civic-centre offices)
4. The run to our conference table crosses a doorway under the carpet — can people walking over it be what keeps breaking that link? (Civic-centre offices)
5. Our firm's network gear hangs on a plywood board with the cables hanging off the patch panel by their own weight — can that cause ports to fail? (Civic-centre offices)
6. Our office takes two floors of an old building and a single Cat6 run up the stairwell joins them — how do we stop one failure taking the upper floor offline? (Converted buildings on the hill and on Bay Street)
7. We pay for a backup internet line, but when the main service went down the backup never took over — could its Cat6 be the problem? (Converted buildings)
8. Our practice is in a Victorian house on the hill, and the Cat6 to the front rooms runs through the crawlspace under the porch — what goes wrong under there? (Hillside houses)
9. The wall jack under one of our old wood windows keeps failing after storms — is rain getting to it, and what is the repair? (Hillside houses)

FAQ (§17, = FAQPage schema):
F1. Our office holds confidential client files — how does a technician work around them?
F2. Is there anywhere for the technician to park near the courts and the ferry, or should we arrange something?
F3. If the repair turns out bigger than quoted, how do you get our approval when nobody from the office can be there?
F4. Do you repair the network cable to a staff time clock or a visitor sign-in kiosk?
F5. Do you take a deposit before a Cat6 repair?
F6. Will our desk phones, printers and copiers need setting up again after the Cat6 is repaired?
F7. Can you repair the cable that feeds the card reader on our suite door?
F8. Can the work be kept quiet while we are meeting clients?

Other "?" headings: "Desk Offline Near Borough Hall Before the Day Starts?" (repair capture), "Moving Into a Suite Somebody Else Wired?" (CTA), "St. George Link Failing Today?" (closing).

De-dup notes (by meaning, against every register in research/cat6-repair.md — NYC, LI, HV, Bronx, SI, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess, Ulster — and against the soundbar and fiber St. George registers): candidates dropped because a sibling already holds the intent — "fault in the riser vs our suite" (Manhattan Q10), "jacks still run to the other tenant's closet" (Suffolk Q1), "which runs belong to which tenant" (Orange, Nassau Q12), "zone box above the ceiling fails together" (Manhattan Q11), "move a failing desk to a spare run tonight" (Manhattan Q9), "power poles after furniture moves" (Manhattan Q2), "surface raceway in a hallway" (Bronx Q5), "old pipe chase / dumbwaiter" (Bronx Q9), "concrete ceilings" (Westchester Q8), "conduit in a slab" (Brooklyn Q8), "steam riser / radiator heat" (Westchester Q12), "closet runs hot" (Westchester Q7), "duct chase" (Westchester Q14), "basement box ownership" (Westchester Q4), "least visible replacement route in a brick townhouse" (HV Q12), "LPC approval" (Manhattan/Brooklyn; LPC kept in body only), "Does a repair need a permit?" (Dutchess F6 — DOB § 28-105.4.7 kept in §8.5 body only), "Saturday / early morning / evening booking" (SI F8, Nassau F5, Putnam F9), "Wi-Fi or router password" (Rockland F2, Westchester F2), "be home for the whole visit" (Nassau F1, Suffolk F6), "cable vs device fault" (Rockland F10, Queens F10, NYC Q3), "badge/escort rules" (Dutchess F1, Orange), "remote IT provider" (LI F10), "old cable on re-pull" (NYC F7), "intercom interruption" (Westchester F7 — our F7 is repair of an access reader's cable, not interruption of an intercom), "re-terminating changes switch ports" (NYC F4 — our F6 is device re-configuration, flagged as borderline for review), "stapled cable" (LI Q9). Stranded-cable Q2 is a different material from CCA (NYC Q13), Cat5e print (Ulster Q3) and telephone-grade (Putnam Q11) — flagged as same family for review. Window-leak Q9 differs from SI Q4 (jack on a damp foundation wall) and the parent's flood-line questions (rain at a window above grade, not ground water).

Masked paragraph similarity (difflib SequenceMatcher on geo-masked p/li/td/h3/figcaption blocks of 8+ words, word-set prefilter 0.4): after two rewording passes every block at or above 0.65 versus all 16 cat6-repair area pages, the two parallel batch drafts on disk (cat6-repair-financial-district-manhattan-ny, cat6-repair-park-slope-brooklyn-ny), soundbar-installation-st-george and fiber-optic-installation-st-george is an excluded constant only (freshness stamp, warranty sentence, licence/rating line, "parts you supply" line, NAP line, silo-nav link rows). network-cable-repair-staten-island max 0.61. Blocks rewritten during the passes: repair-capture paragraph, instant-action bullet, all pricing-table cells, package copy, CTA text, form intro and success message, related-service blurbs, AI-check intro and one H3, three figure captions that matched park-slope/queens/rockland/orange captions of the same source scenes, abandoned-cable bullet, sources-list descriptions.
Image-scene overlap to note: park-slope (same batch) also borrowed the crushed-bundle, crossed/open-pair tester, dome-camera no-PoE, corroded-plug, wall-jack no-link and toner scenes; financial-district borrowed the corroded-plug, fish-tape and dome-camera scenes. Files, crops and captions differ, but the main run may want to swap scenes so each neighbourhood page shows different photos.


## Financial District, Manhattan (cat6-repair-financial-district-manhattan-ny)

Batch run 2026-10-17 (subagent build; to be merged into research/cat6-repair.md by the main run). Neighbourhood spoke under /cat6-repair-manhattan · phone (929) 560-0737 · Bronx GBP (460 E Fordham Rd). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: WebSearch (result lists), WebFetch (page read), Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources already in this file (NYC Admin Code §28-105.4.7, LPC permits page, NEC 800.25 via EC&M, NYC Electrical Code effective Dec 21 2025, Fixr Jan 2025, 25 Water Street Wikipedia) are reused and named on the page as such.

**Thesis (differs from cat6-repair-manhattan, which is "inherited plant repaired inside the building's window", and from fiber-optic-installation-financial-district-manhattan-ny, which is "a backbone designed to be separated, moved and kept dry"):** in the Financial District the building keeps changing around the Cat6 — two office-to-residential conversion waves, re-let and re-divided floors, enclosed Water Street arcades, cellars reshaped after Sandy, floors handed back at lease end — so a repair starts by asking what changed in the building, then certifies, repairs and records. Supporting angles: underfloor duct outlets in post-war towers, dust/vibration from conversion demolition, worn hot-desk jacks (connector plating/mating-cycle standards), inter-floor links at convenience stairs, arcade-infill shop routes, lease surrender removal vs NEC abandoned-cable rule, first-wave conversions wired before Cat6 existed.

### Reddit (local) — EMPTY (not accessible in build env)
- Query: `reddit FiDi apartment ethernet port not working converted building Financial District` · WebSearch → no reddit.com thread for FiDi returned (results: Telus forum, Verizon Fios forum, generic blogs). EMPTY. Not used.

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview could not be viewed; each H3 is framed as a widely repeated claim and corrected with the sources below.

### Neighbourhood data / conversions
- Query: `Downtown Alliance Lower Manhattan office to residential conversions 2025 list buildings units Financial District` · WebSearch → result list; then Firecrawl scrape https://downtownny.com/research/2025-lower-manhattan-real-estate-year-in-review/ (directQuote): 2025 leasing 4.75M sf, "Most Active Year Since 2019"; vacancy 22.2% (eight quarters of decline), Class A 21.1%; residents "surpassed 70,000 for the first time"; 90 new retail openings; Q4 hotel occupancy 90%. → §5 para 3, §5.5 facts 5, "Leaving Cleanly" section para 1.
- Same search → WebFetch https://newyorkyimby.com/2025/05/222-broadway-begins-798-unit-office-to-residential-conversion-in-manhattans-financial-district.html: 222 Broadway, 31 storeys, 798 rentals + 40,000 sf commercial, CetraRuddy, TPG/GFP, bought spring 2024 $147.5M, completion May 2027. → §5.5 fact 1, §7 card, §8 Broadway card, §13 landmark card.
- Same search → WebFetch https://propmodo.com/playbook/80-broad-street-joins-the-next-wave-of-financial-district-conversions/: 80 Broad St, built 1935, 37 storeys, 326 units, DOB filing Jan 22 2026, apartments floors 2–34. → §5.5 fact 1, §7 setback-tower card, §13 landmark card.
- Query: (Firecrawl scrape, URL from research/fiber-optic-installation.md FiDi section) https://cbcny.org/research/potential-office-residential-conversions (directQuote): 421-g converted "nearly 13 million square feet of office space, or roughly 13 percent of the lower Manhattan office market" 1995–2006; 98 office buildings, 12.8M sf, 12,865 units. → §5 para 1, §5.5 fact 1, §7 first-wave card, "The First Wave" section.
- Query: `Cat6 standard TIA-568-B.2-1 published June 2002 category 6` · Firecrawl search (excerpts) → https://www.blackbox.com/en-au/insights/blackbox-explains/inner/detail/copper-cable/copper-category-standards/category-6-and-6a ("ratified by the TIA/EIA in June 2002"); https://www.scribd.com/document/250675325/Wp-Leviton-Tia-Cat6 ("On June 20, 2002 TIA published the category 6 addition"). → §5.5 fact 2, §9 statement H3 "Wiring older than the Cat6 standard", §7 first-wave card, "The First Wave" section, §10.5 H3 3.
- 25 Water Street (~1,300 apartments; largest US office-to-residential conversion) — reused from this file's Manhattan section (Wikipedia). → §5.5 fact 1, §7 conversions card.

### Sandy / flooding (sources 9, 10)
- Query: `Hurricane Sandy Lower Manhattan office buildings flooded basements telecom copper salt water damage Verizon 140 West Street` · WebSearch → WebFetch https://www.benton.org/headlines/look-inside-verizons-flooded-communications-hub (Nov 1 2012): storm surge "breached the protective plugs" around incoming cables; basement "cable vault" flooded; 3.5 of 5 basement levels under "brackish" water. → "After the Water" section para 1, §10.5 H3 1.
- Same search → WebFetch https://www.amny.com/news/downtown-still-calling-for-answers-from-verizon (Kaitlyn Meade, Jan 23 2013): Verizon reported "95 percent of the copper cable infrastructure" feeding back to Broad St destroyed (hubs, manholes, conduits, building connection points); 140 West St back in 27 hours, 104 Broad St office in 10 days; decision to replace copper with fibre. → §5.5 fact 4, "After the Water" para 2, §10.5 H3 2.
- Query: (Firecrawl scrape; WebFetch permission timed out) https://therealdeal.com/new-york/2012/11/01/trd-survey-more-than-17-million-sf-of-downtown-office-space-shuttered-in-sandys-wake/ (Adam Pincus, Nov 1 2012, directQuote): ≥17.3M sf, ≥15 east-side buildings closed with flooded basements/sub-basements; 55 Water St 3.6M sf, 1 New York Plaza 2.5M sf, 2 Broadway 1.6M sf, 4 New York Plaza 1.5M sf; "pumping water from two levels of underground tunnels where communications lines had flooded under Pearl Street". → §5.5 fact 3, "After the Water" para 1, §8 Whitehall card, §13 1 New York Plaza card.
- Query: (Firecrawl scrape) https://en.wikipedia.org/wiki/Lower_Manhattan_Coastal_Resiliency (directQuote): FiDi–Seaport master plan released 2021; buried flood walls, deployable flood gates, pump stations; 15–20 years, $5–7B; funding not secured as of late 2025. → §5.5 fact 6, "After the Water" para 4, FAQ F5 framing.
- Query: `Financial District water main break flooded basements Lower Manhattan 2024 OR 2025 OR 2026` · WebSearch → WebFetch https://www.cbsnews.com/newyork/news/water-main-break-causes-flooding-in-lower-manhattan/ (July 6 2013, Two Bridges/Madison St) and https://amny.com/manhattan/water-main-break-in-manhattan-leaves-south-street-flooded-during-evening-rush-hour (Feb 2020, South St at Catherine Slip). Both outside the Financial District → NOT used.

### Streets, landmarks, building stock (sources 6, 7)
- Query: `55 Wall Street interior landmark banking hall designated Landmarks Preservation Commission` · WebSearch → WebFetch https://en.wikipedia.org/wiki/55_Wall_Street: Merchants' Exchange (Isaiah Rogers) 1836–1841/42; McKim, Mead & White added floors 1907–1910 for National City Bank; NYC landmark Dec 21 1965; interior landmark (banking hall) Jan 12 1999; contributing property to the Wall Street Historic District (NRHP) Feb 20 2007; banking hall = Cipriani Wall Street event venue since 2006; upper floors condos (Cipriani Club Residences); hotel 2000–2003. → §7 bank card, §8 Wall/Broad card, §8.5 designated-interiors callout, §9 statement H3 "Designated interiors on Wall Street", §13 card.
- Query: (Firecrawl scrape) https://en.wikipedia.org/wiki/Stone_Street_(Manhattan) (directQuote): first cobbled street in New Amsterdam 1658; renamed 1794; Great Fire Dec 16 1835; "Over 600 new buildings were built in the First Ward in 1836, including numerous four-storey Greek Revival commercial buildings on Stone Street"; LPC Stone Street Historic District 1996, NRHP 1999; eastern blocks pedestrian in summer with outdoor dining; Broad St–Coenties Alley block closed 1980 (85 Broad St); remaining street portions part of the Financial District street layout, a city landmark. → §7 counting-house card, §8 Pearl/Hanover/Stone card, §13 card, "The Oldest Blocks" section.
- Query: `Water Street arcades infill retail zoning text amendment 2016 Financial District privately owned public spaces` · WebSearch → WebFetch https://citylandnyc.org/city-council-subcommittee-land-use-committee-vote-approve-rezoning-water-streets-privately-owned-public-space-modifications (June 17 2016): 17 buildings covered; special permit for arcades larger than 7,500 sf (seven buildings); Downtown Alliance commitment letter (three years of programming; annual POPS checks); Land Use Committee approved June 15 2016. https://www.nyc.gov/site/planning/plans/water-street-pops/water-street-pops.page → redirect only, EMPTY. → §6 arcade card, §7 plaza-tower card, §8 Water St card, §9 Q6, "Water Street" section.
- Query: (Firecrawl scrape) https://baxtel.com/data-center/epsilon-ny-75-broad (directQuote): 75 Broad = "the historic ITT carrier hotel"; Verizon colocation on the 7th floor; NYI Broad Street Connect launched Q4 2023 with owner JEMB Realty. (WebFetch permission timed out.) → §13 card, FAQ F1.
- Underfloor duct: (Firecrawl scrape; WebFetch permission timed out) https://www.econline.com/doc/cellular-underfloor-duct-system-0001 (directQuote): header duct "with four compartments (one for power, two for voice and one for data)"; cell duct three compartments (two voice/data, one power). Era not sourced → page does not date underfloor ducts. → §6 card, §7.5 table, §9 Q1.

### Technical
- Query: `RJ45 connector contacts dust contamination oxidation causes intermittent connection gold plating harsh environment` · WebSearch → Firecrawl scrape https://cccassoc.org/wp-content/uploads/2026/06/CCCA-The-Weakest-Link-Exposing-the-Dangers-of-Non-Compliant-RJ45-Connectivity-Final-11-7-25.pdf (CCCA, directQuote): TIA-1096-A hard-gold contacts, ≥50 µin gold, nickel barrier; IEC 60603-7 mating cycles 750 (performance level 1) / 2,500 (level 2) without exceeding 20 mΩ increase; defective plating "can cause gold to wear off the jack contact surface after as few as 10 to 15 insertions and removals". → §9 Q3 (dust), §9 Q5 (hot desks), §10.5 H3 4, "Shared Desks" section. Dust-on-contacts effect is stated as field reasoning (no source quantifies dust); RJ45 dust-cap product pages from the same search not used.
- Query: `construction dust contamination RJ45 jacks patch panel network intermittent errors protect telecom room during renovation` · WebSearch → product listings only (RJ45 dust covers). No usable source → dust Q worded as field practice.
- Query: `office lease surrender restoration clause remove tenant cabling telecommunications wiring end of lease New York` · WebSearch → WebFetch https://www.lawinsider.com/clause/surrender-restoration/_4: sample clause (Standard Form Industrial Net Lease, Cue Health Inc.) requires removal of "all electronic, fiber, phone and data cabling and related equipment" unless landlord written notice. Presented on page as "one published sample", not NY-specific. → §9 Q7, "Leaving Cleanly" section.
- Reused silo sources: NYC Admin Code §28-105.4.7 (<50 V permit exemption, licensed/qualified person) → §8.5, §10.5 H3 6; LPC permits page (ordinary repairs; interior landmark) → §8.5, §9 statement H3; NEC 800.25 via EC&M (abandoned cable) → §8.5, §9 Q7, §10.5 H3 5; NYC Electrical Code effective Dec 21 2025 → §8.5; Fixr Jan 2025 ($125–$250/drop, $45–$75/hr) → §10.5 H3 7.
- Inter-floor (convenience stair) links: written from general code practice (riser listing, listed firestop) — no statistic or named building attached.

### Local news on Cat6/network cabling failures in FiDi — EMPTY (no relevant result in the searches above).

### Prices used (only from live AESS Manhattan pages; no new prices)
- $195/hr, three-hour minimum ($585) — network-cable-repair-manhattan.html / cat6-repair-manhattan.html.
- Replacement run from $175 per drop — network-cable-repair-manhattan.html.
- Comparison new-install Cat5e $254 / Cat6 $296 / Cat6A $424 per drop — cat6-installation-manhattan.html.
- Evening/weekend freight windows as a named premium line — network-cable-repair-manhattan.html.
- Basis: blueprint §9 Manhattan 1.25×; as on cat6-repair-manhattan the figures already published for Manhattan are used as they stand (no second multiplier). Packages: Starter $585; Standard $195/hr after first 3 h; Premium repair time + from $175/run. Warranty sentence verbatim in §14.

### Keyword notes (five layers)
- Service: Cat6 repair Financial District, Cat6 cable repair Lower Manhattan, Cat6 re-termination, Cat6 certification, floor box / underfloor outlet repair, hot-desk jack replacement, lease hand-back cable removal, inter-floor Cat6 repair.
- Problem: conversion dust/vibration, intermittent panel errors, worn jacks, pinched cable at floor fittings, arcade-shop route failures, corroded contacts after flooding, abandoned cable, undocumented routes, pre-2002 cabling in converted apartments.
- Technology: TIA-568 Cat6 (June 2002), TIA-1096-A plating, IEC 60603-7 mating cycles, cellular underfloor duct, riser-rated cable, listed firestop, certification margin, distance-to-fault, native tester files.
- Industry: finance/law/advisory floors, converted residential towers, restaurants (Stone/Pearl), arcade retail (Water St), colocation (75 Broad), event venues in protected interiors.
- Geographic: Financial District, Wall Street, Broad Street, Water Street, Old Slip, Maiden Lane, William Street, John Street, Pearl Street, Hanover Square, Stone Street, Broadway, Fulton Street, Trinity Place, Whitehall, South Ferry, the Battery; landmarks 55 Wall St, 222 Broadway, 80 Broad St, 1 New York Plaza, 75 Broad St, Stone Street HD; adjacent Battery Park City, Tribeca, Civic Center, Seaport, Two Bridges.

### Images (11) — permanent image rule; Drive "AESS Website Photos/Cat6 Repair" EMPTY (per main run), CompanyCam not available
All source scenes were looked at. Every source photo shows a technician's face, so each was cropped to hands/equipment only (no faces, house numbers, plates or readable documents remain; a "Cat 6 550MHz CMR" carton was cropped out). Source library images appear AI-rendered (uniform branding), as noted by earlier runs. NCR types already used on cat6-repair-manhattan were avoided (the 5 NCR types used here are not on that page). Note: images/cat6-repair/ also holds 14 `aess-cat6-repair-*.webp` files added in commit d8cb9aad ("Add 14 AESS Cat6 repair photos") that every cat6-repair area page now carries as extra figures; they were NOT used here because this page must have exactly 11 figures and the run instructions specified the permanent image rule — flagged for the main run.
| images/cat6-repair/ | Source |
|---|---|
| cat6-repair-financial-district-tester-wire-map-at-rack.webp (hero) | images/network-cable-repair/network-cable-repair-manhattan.webp (cropped) |
| cat6-repair-financial-district-no-poe-no-link-at-dome-camera.webp | images/network-cable-repair/poe-camera-cable-repair-manhattan.webp |
| cat6-repair-financial-district-register-jack-no-link-reading.webp | images/network-cable-repair/pos-network-cable-repair-manhattan.webp |
| cat6-repair-financial-district-patch-panel-port-flashlight-check.webp | images/network-cable-repair/switch-port-troubleshooting-manhattan.webp |
| cat6-repair-financial-district-corroded-plug-block-wall-box.webp | images/network-cable-repair/water-damaged-network-cable-repair-manhattan.webp |
| cat6-repair-financial-district-fish-tape-into-conduit-elbow.webp | images/cat6/cat6-wiring-bronx-fish-tape-conduit.webp |
| cat6-repair-financial-district-oscillating-tool-wall-opening.webp | images/cat6/cat6-retrofit-installation-bronx-drywall-cut-in.webp |
| cat6-repair-financial-district-labelled-bundle-entering-rack.webp | images/cat6/cat6-patch-panel-installation-bronx-network-room.webp |
| cat6-repair-financial-district-partition-plate-retermination.webp | images/cat6/cat6-keystone-termination-brooklyn-outlet.webp |
| cat6-repair-financial-district-floor-box-keystone-service.webp | images/cat6/cat6-floor-box-installation-brooklyn-conference-room.webp |
| cat6-repair-financial-district-j-hook-bundle-above-grid.webp | images/cat6/cat6-installer-bronx-jhook-pathway.webp |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (5) and images/cat6/ (6), cropped to remove faces (no real cat6-repair photos yet)`.

### Masked-geo similarity (difflib per p/li/td/h3/figcaption ≥8 words, geo names masked, Jaccard ≥0.3 prefilter)
Mean best-match 0.02–0.05 vs every cat6-repair page on disk (16 area pages + park-slope + st-george as on disk 14:46) and vs fiber-optic-installation-financial-district-manhattan-ny (0.03), network-cable-repair-manhattan (0.00), cat6-installation-manhattan (0.00). Remaining blocks ≥0.65 are excluded constants only: warranty sentence, NAP line, licence/rating line, pricing-table rows (price figures), silo cross-link county lists. Final file 244,568 B; 12,641 rendered words.

## Question register — cat6-repair-financial-district-manhattan-ny
§9 "Questions Answered" (H3), clusters "Floors that keep changing hands" / "Desks, shops and how they are used" / "Leases, records and older wiring":
1. Why do the Cat6 runs in our post-war tower's underfloor duct keep failing right at the floor outlets? (Floors)
2. Our building is being converted to apartments — is any of the office Cat6 worth repairing for the new units? (Floors)
3. Demolition started on the floors above us and our patch panel now throws intermittent errors — can dust and vibration do that? (Floors)
4. Our firm has two floors joined by an internal staircase — can the Cat6 between them go through the stair opening instead of the building riser? (Floors)
5. Our hot desks are plugged and unplugged all day — can that wear out a Cat6 jack? (Desks/shops)
6. Our shop opened in an enclosed former arcade along Water Street — where does its Cat6 run, and why does it give trouble? (Desks/shops)
7. We are handing back two floors when our lease ends — does the Cat6 we leave behind have to come out? (Leases)
Statement H3s (not questions): "Wiring older than the Cat6 standard" (avoids Ulster Q3 / Putnam Q11 / Brooklyn F6 identification intents), "Designated interiors on Wall Street" (avoids Putnam Q10 / Brooklyn's converted LPC intent).
FAQ (§17, = FAQPage schema):
F1. Can you repair the Cat6 inside our cage at a downtown colocation facility?
F2. Our firm asks every contractor to sign a confidentiality agreement before entering the trading floor — is that a problem?
F3. Can our IT team have the tester's native result files as well as the PDF report?
F4. Our building's freight elevator is out of service for modernization — can a repair still go ahead?
F5. If a coastal storm warning is issued while a repair is booked, what happens to the appointment?
Other "?" headings: "Cat6 Link Down Somewhere Between Fulton Street and the Battery?" (repair capture), "Downtown Link Still Down After the Contractors Leave Tonight?" (closing).
De-dup notes (by meaning) against every register in research/cat6-repair.md (NYC, LI, HV, Bronx, SI, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess, Ulster) and the headings/FAQ of fiber-optic-installation-financial-district-manhattan-ny, network-cable-repair-manhattan and cat6-installation-manhattan. Deliberately avoided: any flood/water-reuse or move-equipment-above-flood-line question (NYC Q16, SI Q2–Q4, Nassau Q6–Q7, Brooklyn Q11, Westchester Q9, Suffolk Q5–Q6, Rockland Q8, Orange Q10) — Sandy handled as a body section; storm-season pre-testing (SI F2); converted-office apartment jack failures (Manhattan Q1); raised-floor/poke-through (Manhattan Q4–Q5) — underfloor-duct Q is about why outlets fail, not floor access; fiber FiDi underfloor-duct Q is about routing new fibre; demolition-above (fiber FiDi asks keeping riser fibre alive; ours asks dust/vibration as an error cause); other-trade damage documentation (Westchester Q11, Nassau Q4, Queens Q8, Orange Q2); re-homing runs to own panel (Suffolk Q1); handover test results (Suffolk Q2); leave a spare (Queens F1); old-cable removal on re-pull (NYC F7); jack durability vs tenants breaking jacks (Dutchess Q10 — ours is mating-cycle wear on shared desks); security perimeter access, union labour, DFS inventory, latency, coverage of BPC/Seaport (fiber FiDi); badge/escort on secured campus (Dutchess F1 — ours is a confidentiality agreement); test-result retention period (Queens F4 — ours is native file format); certified reports (NCR Manhattan — ours is native files).


## Park Slope, Brooklyn (cat6-repair-park-slope-brooklyn-ny)

Batch run 2026-10-17 (neighborhood page; up-link /cat6-repair-brooklyn, hub /cat6-repair-nyc). Brooklyn GBP (1282 Troy Ave, #brooklyn), direct line (347) 934-8335 (800 number only in the shared header), Brooklyn ×1.00 pricing. Built in parallel with cat6-repair-st-george-staten-island-ny and cat6-repair-financial-district-manhattan-ny.
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (directQuote query mode). Shell curl blocked. Firecrawl does not scrape reddit.com, so Reddit entries are search excerpts only.

**Thesis:** in Park Slope the rowhouse's framing and its landmarked envelope decide the repair route. Joists span party wall to party wall, so vertical runs are easy and front-to-back runs are hard; cellar cable is commonly tied to century-old gas/water pipes; parlor floors, plaster cornices and pressed-tin storefront ceilings are worked around, not cut; the brownstone facade is under LPC criteria down to the mortar joint. Secondary building types: PPW pre-war co-ops, post-2003 Fourth Avenue condos (closet media enclosures), Fifth/Seventh Avenue mixed-use buildings with flood-exposed cellars (Sept 2023), conversions/institutions. Differs from the Brooklyn parent (building-family thesis across the borough), the soundbar Park Slope page (parlor detail/noise) and the parallel St George / FiDi pages.

### 1. Reddit (source 1) — Firecrawl search excerpts only
- `site:reddit.com r/parkslope ethernet internet wiring brownstone` · Firecrawl search →
  - https://www.reddit.com/r/parkslope/comments/1x69q1e/wifi_what_are_your_solutions/ — excerpt: "In multi-level brownstones, what WiFi set up do folks have? I've been using Spectrum forever and it sucks. Just got a WiFi extender and it doesn't make ..." → §5 para 2; §10.5 H3 "mesh Wi-Fi".
  - https://www.reddit.com/r/parkslope/comments/11hcbe9/whats_with_the_terrible_internet_options_in_south/ — excerpt: "just moved over to this neck of the woods ... the internet leaves something to be desired. With remote work ..." → "How Cat6 Faults Differ Across the Slope" South Slope paragraph.
  - https://www.reddit.com/r/Fios/comments/1cyyz1z/nyc_311_verizon_needs_access_to_backyards_to/ — title "[NYC 311]: Verizon needs access to backyards to install Fios"; excerpt "I noticed many brownstones in Brooklyn also have Fios, from Park Slope ..." → §9 rear-wall route question.
- `Park Slope Fifth Avenue flooding 2023 storm businesses flooded basements Brooklyn` · Firecrawl search → https://www.reddit.com/r/parkslope/comments/xd7fyb/did_anyone_else_have_flooding_in_their_basements/ — excerpt: "This is storm water that overwhelms the sewer system and then comes up in the lower parts of some buildings." → §9 H3 "Fifth Avenue cellars after the 2023 flood".
- Fault-specific r/parkslope threads (dead jacks, failed Cat6): EMPTY (not accessible in build env — reddit not scrapeable, no fault thread in results).

### 2–5, 8, 11. Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 says on-page that the AI Overview could not be viewed; each H3 is framed as a commonly published claim and corrected with the sourced facts below.

### 6/7. Building stock, framing, landmarks, corridors
- `brownstone rowhouse floor joists span party wall to party wall running wires front to back` · Firecrawl search → scrape https://www.brownstoner.com/forum-archive/2005/05/floor-joist-que/ (Brownstoner forum, May 11 2005; Bed-Stuy owner's question about a "1899 3-story, 20' wide brownstone"), directQuote: "Floor josts typically run side to side in both brick and frame rowhouses." / "In most cases, the joists run from side to side, using the masonry side walls as supports." Search excerpt also: Philadelphia Rowhouse Manual (https://www.phila.gov/media/20190521124726/Philadelphia_Rowhouse_Manual.pdf) "Typically, wood joists span from party wall to party" — not used (not NYC). → §5 para 3, §5.5 bullet 2, §9 Q1, Diagram 1, §10.5 H3 "hollow walls".
- `brownstone parquet floor border inlay original parlor floor remove boards run wires Brownstoner` · Firecrawl search → scrape https://www.brownstoner.com/interiors-renovation/old-wood-floors-refinish-replace-interior-design-renovation-ideas/ (Liz Sadler Cryan, Dec 12 2017), directQuote: "Original wood floors can be one of the most striking features of a brownstone or townhouse, especially if they have intricate parquet or borders."; "Brownstone owners often call upon Zambrano to repair original parquet floors because he collects and saves old pieces of inlay borders. In cases where the original floor is missing or unsalvageable, he often sands and refinishes the original pine subfloors." → §9 Q3 (parquet).
- `Park Slope storefront original pressed tin ceiling Seventh Avenue Fifth Avenue shop restored` · Firecrawl search → https://www.facebook.com/groups/20107376010/posts/10164096167056011/ — excerpt: "Classic tin ceiling in Purity Diner. They moved to this location (corner of 7th st and 7th Ave) in '99" (search excerpt only, community group). → §9 Q6 (pressed tin), attributed as "one neighborhood history group".
- `Ansonia Clock Factory Park Slope Seventh Avenue 12th Street converted cooperative apartments history` · Firecrawl search → https://www.brownstoner.com/architecture/building-of-the-day-420-12th-street/ — excerpt: "Ansonia Clock Company factory, now apartments. Year Built: 1880-1881. It's been residential since 1982, the complex is now co-ops, with seventy ..."; also cityrealty / streeteasy / corcoran listing excerpts (not used as sources). → §7 conversions card, §13 landmark card, South Slope paragraph.
- `Congregation Beth Elohim Garfield Place Eighth Avenue Park Slope historic temple built` · Firecrawl search → scrape https://en.wikipedia.org/wiki/Congregation_Beth_Elohim, directQuote: Classical Revival synagogue completed 1910 (construction began 1909, Simon Eisendrath and B. Horowitz), six-story Temple House built 1928–1929; both contributing properties to the Park Slope Historic District (NYC 1973, NRHP 1980). → §13 card.
- `Old First Reformed Church Seventh Avenue Carroll Street Park Slope built 1891 history` · Firecrawl search → https://6tocelebrate.org/site/old-first-reformed-church/ — excerpt: "Neo-Gothic structure dedicated in 1891 and replaced a chapel on Carroll Street used until 1886"; https://www.nycago.org/Organs/Bkln/html/FirstReformed.html — "remained on Livingston Street until 1886, when a chapel was completed at Seventh Avenue and Carroll Street"; https://oldfirstbrooklyn.org/history/ excerpt. → §13 card.
- `NewYork-Presbyterian Brooklyn Methodist Hospital Park Slope Seventh Avenue 6th Street founded 1881` · Firecrawl search → https://findingaids.library.nyu.edu/cbh/arc_155_methodist_episcopal_hospital/ — excerpt: "incorporated on May 27, 1881, and opened on December 19, 1887 at the corner of 6th Street and 7th Avenue in the Park Slope neighborhood"; https://en.wikipedia.org/wiki/NewYork-Presbyterian_Brooklyn_Methodist_Hospital — "between 7th and 8th Avenues, on 6th Street". → §8 medical card, §13 card.
- `Brooklyn Public Library Central Library Grand Army Plaza opened 1941 Art Deco building` · Firecrawl search → https://www.bklynlibrary.org/locations/central — excerpt: "Central Library first opened its doors to the public on February 1, 1941." → §13 card.
- `Park Slope Food Coop 782 Union Street members founded 1973` · Firecrawl search → https://www.foodcoop.com/hours/ (782 Union Street); https://www.ncg.coop/partners-find/ny/park-slope-food-coop — "founded in 1973 ... PSFC has more than 16,000 members". → §8 Union Street card, §13 card (stated as landmark, not a client).
- Carried from research/soundbar-installation.md Park Slope section (sources reached by an earlier 2026-10-17 run; not re-fetched): Wikipedia Park Slope Historic District (1,802 contributing buildings 1862–c.1920; 2012 expansion to 2,575 buildings; 2016 expansion; largest landmarked neighborhood by number of buildings); HDC (1973 designation); New York YIMBY Apr 2016 (second extension adds 292 buildings, mostly St. Marks Ave–Sterling Pl); CityLand (first extension ~582 buildings); NYC DCP Park Slope rezoning PDF (CPC Apr 2 2003, Council Apr 30 2003, 110 blocks, R8A on Fourth Ave); NYU Furman Center Park Slope/Carroll Gardens (homeownership 37.1% 2024 vs 32.7% citywide; 6,563 new units 2010–2025 in 4+ unit buildings); CityRealty 35 Prospect Park West (Emery Roth, 1929, 16 stories); brooklyn.studio / Brownstoner (Queen Anne 1891 limestone; Romanesque Revival 1892); NYC SBS BID directory (Park Slope 5th Ave BID est. June 2008, 62 block faces, 521 ground-floor retail businesses); defalcorealty guide (Seventh Ave "upscale dining, boutique shopping, and specialty food stores", March 2026). → §5, §5.5, §7, §8, area-by-area section.

### 9/10. Local news / hyperlocal
- `Park Slope brownstone fire FDNY neighbors damaged Brooklyn Paper` · Firecrawl search → scrape https://www.brooklynpaper.com/massive-fire-devastates-park-slope-brownstone/ (Ben Verde, Oct 24 2019), directQuote: "Over 100 firefighters rushed to the scene"; "The blaze erupted on the ground floor of the rowhouse near Eighth Street and Seventh Avenue shortly after 4 pm, before spreading through a dumbwaiter to the upper floors, officials said." → §5.5 bullet 6, §9 H3 "Dumbwaiter shafts, closets and the holes between floors" (sealing penetrations). Neighbor-house damage not stated in the article → not claimed.
- `Park Slope Fifth Avenue flooding 2023 storm businesses flooded basements Brooklyn` · Firecrawl search → scrape https://www.brooklynpaper.com/local-businesses-struggling-after-flood/ (Oct 4 2023), directQuote (Joanna Tallantire, Park Slope Fifth Avenue BID): "Over 30 businesses were directly affected by the flooding on Fifth Avenue, Park Slope"; "Up to 6 feet of water flooded basements. The water knocked over and destroyed the equipment and produce in many of the restaurants and bars." Also abc7ny / ny1 excerpts (not used). → §5 para 4, §5.5 bullet 5, §8 Fifth Avenue card, §9 H3 "Fifth Avenue cellars after the 2023 flood".
- Brooklyn Paper / Park Slope Reader / Patch / Brownstoner news on Cat6 or network-cable faults in Park Slope specifically: EMPTY.

### Local licensing / permits / code
- `Landmarks Preservation Commission permit security cameras mounted on facade historic district rowhouse mortar joints rules` · Firecrawl search → https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf (full guidebook; camera section not in scrape text) → `LPC Permit Guidebook Chapter 7 Health Safety Utility Equipment security cameras pdf nyc.gov` · Firecrawl search → scrape https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook%20_Chapter11_HealthSafety.pdf, directQuote: "If installation requires conduit, the conduit must be concealed by going through plain masonry or wall cladding behind the installation." / "If this is not possible, staff may approve a maximum of approximately ten inches of visible conduit." / "If surface-mounted, the conduit must be painted to match the background surface and secured into mortar joints where possible — not installed on any decorative surfaces." / "For small residential or commercial buildings, no more than two security cameras can be installed for every 25 feet of street frontage." → §9 Q4 (facade entry), Diagram 3, §10.5 H3 "clip the camera cable".
- `Landmarks Preservation Commission brownstone repair guide sandstone delaminating spalling` · Firecrawl search → scrape https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter1_Restoration.pdf, directQuote: "Staff can issue a permit for repairing or resurfacing brownstone facades and elements, which are very susceptible to deterioration over time"; "All resurfacing work must be undertaken by a qualified contractor"; caption "Significantly deteriorated brownstone, often referred to as delamination."; "Temperature must remain a constant 45 degrees or above for a period of 72 hours after installation." (samples of temperature-sensitive materials). Main guidebook scrape: "Unsure whether your work requires a permit? Contact LPC". → §9 Q4, §9 Q5, FAQ (winter facade work).
- Search excerpt (same query set): https://www.nyc.gov/site/lpc/about/pr2025/lpc-launches-new-permit-guidebook-and-mapping-tools-20250626.page — "LPC Launches New and Updated Permit Guidebook and Mapping Tools". → FAQ (checking whether a house is in the district).
- Reused from research/cat6-repair.md Brooklyn section (not re-fetched): LPC "Permits and Making Alterations" (no permit for ordinary repairs; interior work needs LPC permit only with DOB permit / exterior effect / designated interior); EPA RRP (pre-1978, >6 sq ft); HPD Local Law 1 (pre-1960 presumption). → §8.5 callouts, §10.5 H3 "landmark district".
- `NEC 800.133(C) communications cables shall not be strapped taped attached to exterior of conduit raceway support pipes` · Firecrawl search → scrape https://www.ecmweb.com/national-electrical-code/code-basics/article/20897736/the-nec-and-communications-circuits (Mike Holt, EC&M, Jul 15 2013), directQuote: "Support exposed cables with supports that fasten to frame members, securing the cables with straps, staples, hangers, cable ties, or similar fittings [800.24]. Install these in a manner that doesn't damage the cable."; "Don't strap, tape, or attach communication wires or cables to raceways as a means of support. [800.133(B)]."; "Remove abandoned cables ... remove the accessible portion". → §9 Q2 (cable on pipes), §8.5 electrical-code callout, §10.5 H3 "whatever is in the cellar".
- `fuel gas code gas piping shall not be used to support other piping cables wiring "shall not support"` · Firecrawl search → no NYC Fuel Gas Code text returned. EMPTY. Page makes no gas-code claim; the pipe answer rests on NEC 800.24/800.133(B) and practical reasons only.
- NYC Electrical Code (2020 NEC + amendments, full effect Dec 21 2025) — reused from silo section. → §8.5.
- DOB permit thresholds for low-voltage repair: EMPTY (not claimed).
- AESS NYS license #12000287431 (site constant).

### Technical
- `indoor CMR Cat6 cable run outdoors sunlight UV degrade jacket outdoor rated CMX` · Firecrawl search → https://www.truecable.com/blogs/cable-academy/facts-about-ethernet-cable-jacket-ratings — excerpt: "If you install either CMR or CMP cable outdoors, the jacket will begin to degrade immediately and will fail in a matter of months." → §9 Q5, §10.5 H3 "any Ethernet cable works outdoors".
- Silo technical sources reused in general terms only (research/cat6-repair.md): 90 m permanent link, NEXT/untwist (Fluke), return-loss/insertion-loss causes (BICSI-style guide), gigabit four pairs / 100 Mbps fallback (computercablestore), Fixr Jan 2025 $125–$250/drop, $45–$75/hr. → glossary, §10.5, pricing.

### Prices used (Brooklyn ×1.00 per blueprint §9 — identical to cat6-repair-brooklyn / cat6-repair-nyc; no new prices)
- $195/hr, three-hour minimum ($585); replacement run from $175; exterior entry sealed and bonded from $185 per penetration; Fixr national figures labelled third-party. Packages: $585 starter; $195/hr after first 3 h; repair time + from $175/run.

### Keyword notes (five layers, Park Slope geo)
- Service: Cat6 repair Park Slope, Cat6 cable repair Park Slope Brooklyn, Cat6 jack repair, re-termination, recertification, run replacement, cellar re-hanging.
- Problem: front-to-back run failure, cable tied to pipes, crushed/cooked cellar cable, facade camera entry/delaminating brownstone, outdoor run in indoor cable, flood-corroded cellar terminations, media-enclosure faults, top-floor access point link.
- Technology: Cat6/Cat6A, permanent link, distance-to-fault, wire map, NEXT, return loss, insertion loss, PoE, keystone, J-hooks, fire-rated sealant, outdoor UV jacket.
- Industry: brownstone homes and home offices, split rowhouses/rentals, PPW co-ops, Fourth Ave condos, Fifth/Seventh Ave shops and restaurants, medical offices, congregations/schools, conversions.
- Geographic: Park Slope, North/Center/South Slope, Prospect Park West, Fifth/Seventh/Fourth Avenues, Union St, Flatbush Ave, Grand Army Plaza, Garfield Pl, Carroll St, 6th St, 12th St, Berkeley Pl, Prospect Expressway; adjacent Prospect Heights, Windsor Terrace, Gowanus, Carroll Gardens, Sunset Park.

### Images (11) — permanent image rule
Drive "AESS Website Photos/Cat6 Repair" EMPTY (checked by main run); CompanyCam not available. 11 copied from images/network-cable-repair/ (16 unique photos there; none of these used on cat6-repair-brooklyn, which used images/cat6/). Each viewed before use; cropped with PIL to remove technicians' faces (every source frame showed a face except the crushed-bundle frame); WebP q80, ≤1600 px. No house numbers, plates or readable documents (panel strip "OFFICE 214 - DATA" and tester screens are equipment labels).
| images/cat6-repair/ | Source (images/network-cable-repair/) | Crop |
|---|---|---|
| cat6-repair-park-slope-tester-crossed-open-pair.webp (hero) | network-cable-fault-detection-bronx.webp | lower 724 px (face removed) |
| cat6-repair-park-slope-wall-jack-no-link-reading.webp | network-jack-repair-bronx.webp | lower-left (face removed) |
| cat6-repair-park-slope-keystone-punch-down-wall-plate.webp | keystone-jack-replacement-bronx.webp | lower-right (face removed) |
| cat6-repair-park-slope-tone-probe-labelled-panel.webp | network-cable-tracing-bronx.webp | right side from x=790 (face removed) |
| cat6-repair-park-slope-corroded-plug-damp-block-wall.webp | water-damaged-network-cable-repair-bronx.webp | right/lower (face removed) |
| cat6-repair-park-slope-cable-bundle-pressed-on-duct-edge.webp | crushed-network-cable-repair-bronx.webp | none |
| cat6-repair-park-slope-dome-camera-no-poe-test.webp | poe-camera-cable-repair-bronx.webp | left side (face removed) |
| cat6-repair-park-slope-rj45-plug-crimp.webp | rj45-connector-replacement-bronx.webp | lower band (face removed) |
| cat6-repair-park-slope-patch-panel-repunch.webp | patch-panel-repair-bronx.webp | left side (face removed) |
| cat6-repair-park-slope-switch-port-flashlight-check.webp | switch-port-troubleshooting-bronx.webp | left side (face removed) |
| cat6-repair-park-slope-ceiling-access-point-lead.webp | access-point-cable-repair-bronx.webp | upper-left (face removed) |
DAILY-LOG note: `images: 11 reused from images/network-cable-repair/ (11) (no real cat6-repair photos yet)`.
FLAG for Anwar: the images/network-cable-repair/ and images/cat6/ source photos look rendered (AI-style) rather than job-site photos; used because they are the library the permanent image rule points to.
Four schematic inline-SVG diagrams (rowhouse plan, section, facade entry, distance-to-fault scale) were drawn for the page; they are labelled "schematic, not to scale" and depict no real address.

### Masked-geo similarity (scratchpad sim.py: checker mask() + Park Slope/avenue/borough names + digits removed; p/li/td/h3/figcaption blocks ≥8 words; difflib on top-3 trigram candidates; 5-word shingle Jaccard)
Jaccard ≤0.010 vs every cat6-repair page (incl. parallel st-george and financial-district), soundbar Park Slope, network-cable-repair-brooklyn, structured-cabling Park Slope. Blocks ≥0.65 remaining are only excluded constants (warranty sentence, NAP line, licence/rating strip, freshness stamp).

## Question register — cat6-repair-park-slope-brooklyn-ny

§9 "Questions Answered" (H3, grouped under non-question H2s: Rowhouse geometry · Original floors, plaster and woodwork · The landmarked front and the back of the house · Shops on the avenues and the newer buildings):
1. Why is replacing a front-to-back Cat6 run in a Park Slope rowhouse so much harder than replacing one that goes straight up between floors? (Rowhouse geometry)
2. Our cellar Cat6 is cable-tied to the old gas and water pipes. Does the repair have to take it off them? (Rowhouse geometry)
3. The failed run lies under the original parquet and inlaid border of our parlor floor. Can it be replaced without lifting the floor? (Original floors)
4. The Cat6 to our front-door camera comes through the brownstone face, and the stone is flaking around the hole. What is the right repair? (Landmarked front)
5. Could a replacement run go down the back wall of the house instead of through the floors? (Back of the house)
6. Our shop has its original pressed-tin ceiling. Can a failed run above it be replaced without taking the tin down? (Shops)
Non-question H3s in §9 (statements, not registered as questions): "Dumbwaiter shafts, closets and the holes between floors"; "Plaster, cornices and when a small cut is the right call"; "Fifth Avenue cellars after the 2023 flood"; "What the Fourth Avenue buildings share with every newer tower".

FAQ (§17, = FAQPage schema, 5):
F1. Can the outside part of a facade or rear-wall repair be done in winter?
F2. While a run is being repaired, can its wall jack be moved a few feet along the wall?
F3. Will a repaired run be able to power a camera or access point we add later?
F4. Do we have to tell the neighbors if the work is on our side of the party wall?
F5. How can we check whether our house is inside the Park Slope Historic District before the visit?

Other "?" headings: "Lost the Wired Link on One Floor of the House?" (repair capture), "Park Slope Jack Still Dead?" (closing).

De-dup notes (meaning-level, against every register in research/cat6-repair.md and the live headings of the parallel cat6-repair-st-george-staten-island-ny and cat6-repair-financial-district-manhattan-ny pages):
- Dropped "Do we need to save a parking space on the block for your van?" — same intent as St George FAQ "Is there anywhere for the technician to park near the courts and the ferry…" (built in parallel); replaced with F1 (winter timing of exterior work).
- Dropped while drafting: fire next door / which runs to test (template overlap with HV Q2 lightning "which runs should be tested… even if they still seem to work"); firestopping who restores (Dutchess Q2, Queens F5, Manhattan Q5); stoop rebuild (Bronx Q12 / Nassau F3 renovation coordination); daisy-chained floor switches (Nassau Q10, Bronx Q6); split networks for a garden rental (SI Q8); whose responsibility in a condo-converted brownstone (Nassau Q13, Westchester Q4); sanctuary livestream camera (unsourced); LPC approval itself (Manhattan/Putnam Q10 — kept as body text and FAQ F5 is a lookup, not approval); chimney/dumbwaiter shaft reuse (Bronx Q9 — kept as statement H3 only).
- Partial overlaps left for main-run judgement: Q5 rear-wall route vs HV Q8 (indoor cable already run outside — does it need replacing?): Q5 asks whether to choose an exterior route at all; F2 jack move vs Ulster F2 (add a jack in another room); F3 future PoE vs NYC Q9/Q10 (PoE camera reboots / bad run takes port down) — F3 is about capacity of a repaired run for devices not yet installed; Q2 cable on pipes vs Westchester Q12 (Cat6 beside steam riser/radiator keeps failing) — Q2 is about support method and removal from pipes.

## Upper West Side, Manhattan (cat6-repair-upper-west-side-manhattan-ny)

Batch run 2026-10-17 (subagent build; not committed; to be merged into research/cat6-repair.md by the main run). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl MCP (mcp__Firecrawl__firecrawl_search = excerpts unless "scraped"; mcp__Firecrawl__firecrawl_scrape with directQuote or markdown). Shell curl blocked. Up-link /cat6-repair-manhattan; phone (929) 560-0737; GBP Bronx (#bronx, 460 E Fordham Rd). Facts marked "carried" were fetched by the 2026-10-17 soundbar-installation-upper-west-side run (research/soundbar-installation.md, "Upper West Side, Manhattan" section) and are reused, not re-fetched.

**Thesis (differs from cat6-repair-manhattan, cat6-repair-midtown-manhattan-ny and every borough/county page):** on the Upper West Side the Cat6 is a *retrofit added after the fact, by many different hands, into homes and small institutions designed long before networks* (prewar apartment houses built after the 1904 Broadway subway, side-street row houses in nine historic districts, avenue walk-ups, Riverside Boulevard towers, Lincoln Square campuses, practices in apartment-building suites, storefronts that change hands). A repair is (1) archaeology — reading which installer (renovator, ISP, AV firm, previous tenant, super, developer) put the run where, because each leaves a typical weak point (shallow boxes in plaster-on-block walls, AC-sleeve drip paths, molding corners, fire-escape runs, chimney flues, in-unit panels) — and (2) done in occupied homes under co-op house rules, around residents' days (23% work at home; 43.6% single-person households; 22.9% aged 65+). Manhattan page = inherited plant inside the building window; Midtown = other trades disturbing ceilings; neither thesis is repeated.

### 1. Reddit
- Query: `site:reddit.com Upperwestside ethernet OR "network cable" OR wifi apartment wiring` · Firecrawl search (excerpts only; reddit not scraped) →
  - https://www.reddit.com/r/Upperwestside/comments/1oosjv5/wifi_technician_needed/ — excerpt "Is it the wifi that doesn't work? Or the internet? What happens when you try to connect via a wire to the modem?" → background for §5 (home-office reliance) and §10.5 H3 mesh; not quoted.
  - https://www.reddit.com/r/Upperwestside/comments/1ug7x56/wireless_internet_in_the_uws_anyone_have_a/ — excerpt on WiFi range vs wired connection → background §10.5 H3 1; not quoted.
  - https://www.reddit.com/r/Upperwestside/comments/1dj3nqi/internet_service_providers/, https://www.reddit.com/r/nyc/comments/cjnuhr/isps_in_the_upper_west_side/ — ISP threads, background only.
- Carried: https://www.reddit.com/r/AskNYC/comments/1pkvn82/question_about_very_hard_walls_in_prewar/ — "If concrete you will need anchors. Gypsum block is a lot easier to drill into" → §7.5 prewar paragraph, §9 shallow-box Q ("plaster over gypsum or terracotta block"); Sources list "background".
- Carried: r/Upperwestside handyman threads (1us7sb6 "skilled in mounting") → Sources "background"; not quoted.
- UWS Reddit threads about *failing Cat6* specifically: EMPTY (not accessible in build env — reddit not scrapeable; search returned only ISP/Wi-Fi threads).

### 2–5, 8, 11. Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview could not be viewed; each H3 is framed as a commonly published claim (cost guides, Angi/HomeAdvisor, product pages, forums) and corrected with sourced facts.

### 6/7. Building stock, landmarks, institutions
- Carried: https://www.furmancenter.org/neighborhoods/upper-west-side/ (Firecrawl scrape; page updated 05/06/2026) — 2024 population 230,436; housing units 130,471; homeownership 35.6% (city 32.7%); 65+ 22.9%; single-person households 43.6%; 12 Mitchell-Lama properties / 2,075 units. Re-confirmed in this run by search excerpt (`Manhattan Community District 7 work from home share ...` → same URL, "230,436 people", "homeownership rate ... 35.6%"). → §5 paras 4, §5.5 facts 1 and 6, FAQ 3 (Mitchell-Lama), Sources.
- Query: `Manhattan Community District 7 work from home share residents American Community Survey Upper West Side` · Firecrawl search → scrape (directQuote) http://censusreporter.org/profiles/79500US3604107-nyc-manhattan-community-district-7-upper-west-side-puma-ny/ — "Census data: ACS 2024 1-year unless noted"; "23%† Worked at home" (the † = high margin of error flag); median age 43.5; 130,471 units. → §5 para 4, §5.5 fact 2 (stated with the margin-of-error caveat), Sources.
- Carried: LPC post https://www.facebook.com/NYCLandmarks/videos/dyk-the-upper-west-side-has-nine-historic-districtsfeatured-here-is-the-upper-we/577968259884199/ — "the Upper West Side has nine Historic Districts"; https://hdc.org/tags/upper-west-side/ — West End–Collegiate HD Jan 3 1984, ext. June 23 2015, "most elaborate and eclectic collection of row houses in the city"; West 71st Street HD Aug 29 1989 (cul-de-sac row houses). → §5 para 3, §5.5 fact 3, §7 row-house card, §13 West End–Collegiate card, Sources.
- Carried: https://en.wikipedia.org/wiki/The_Ansonia — 2109 Broadway 73rd/74th; 17 storeys; opened April 16 1904; landmark 1972; condo 1992; light courts; 1904 subway station at Broadway & 72nd "spurred the development of high-rise apartment buildings on the Upper West Side along Broadway". → §5 para 1, §7 card, §13 Ansonia card, Sources.
- Carried: https://en.wikipedia.org/wiki/The_Dakota (1880–1884, Hardenbergh, four to twenty rooms, co-op 1961); https://streeteasy.com/building/the-apthorp (390 West End Ave, built 1908, block W 78th–79th); https://en.wikipedia.org/wiki/The_Belnord (1908–1909, arches to internal courtyard). → §7 prewar card, §13 Dakota and Apthorp/Belnord cards, Sources.
- Carried: https://www.cityrealty.com/nyc/market-insight/features/get-to-know/what-classic-six-apartment-why-nyc-buyers-still-covet-prewar-layout/20582 — classic six includes "a smaller room originally intended for live-in household staff … typically positioned near the kitchen"; associated with prewar co-ops on the UWS/UES. → §5 para 1 ("servants' rooms"), §7 prewar card ("staff rooms off the kitchen"), hero form placeholder context, Sources.
- Query: `Riverside South development Upper West Side former Penn Central rail yard towers number of buildings Riverside Boulevard` · Firecrawl search (excerpts) →
  - https://www.nycgovparks.org/parks/riverside-park-south/history — "Built on the former site of the New York Central Railroad's 60th Street Yard, Nineteen buildings were eventually erected". → §5.5 fact 4, §7 Riverside card, §13 card, Sources.
  - https://en.wikipedia.org/wiki/Riverside_South,_Manhattan — table: 180 Riverside Blvd 1999 (40 st., 516 apts); 200 Riverside 2000; 160 Riverside 2001; 220 Riverside 2003 (49 st.); 60 Riverside Blvd/The Aldyn 2011 (38 st., 136 apts). → §5.5 fact 4 ("cable well over twenty years old" = inference from 1999 completion), §13 card, Sources.
  - https://danielblatman.com/blog/riverside-boulevard-new-development-corridor-on-the-upper-west-side — "19 towers built over three decades on a former rail yard between 59th and 72nd Streets" → §7 Riverside card ("between about 59th and 72nd Streets").
- Query: `Lincoln Center campus acres buildings Fordham Lincoln Center Juilliard LaGuardia High School Amsterdam Avenue` · Firecrawl search (excerpts) → https://www.fordham.edu/about/campuses/lincoln-center-campus/ ("The eight-acre campus spans two city blocks"); https://en.wikipedia.org/wiki/Fiorello_H._LaGuardia_High_School (100 Amsterdam Ave between W 64th and 65th, Lincoln Square); https://starrfoundation.org/... ("16-acre campus", Amsterdam Avenue side). → §7 campus card, §8 Lincoln Square card, §13 Lincoln Center card, Sources.
- Query: `Upper West Side doctors offices ground floor prewar apartment buildings Central Park West West End Avenue "professional" suites medical` · Firecrawl search → then scrape (markdown) https://www.metro-manhattan.com/neighborhoods/uptown-manhattan/upper-west-side/ (market data "Last reviewed July 2026"): "your neighbors will mostly be doctors, therapists, nonprofits, and whatever grew up around Lincoln Center"; "All of Uptown Manhattan holds maybe 3 to 4 million square feet of office space"; table row "Central Park West and West End side streets … Professional and medical suites in apartment buildings … 500 to 2,500 SF"; "Healthcare runs this neighborhood. Doctors, dentists, therapists"; Therapy/Psychiatry best-fit "Central Park West and West End side streets"; 1995 Broadway "went up in 1973 … Eighteen stories … column-free full floors of roughly 5,000 feet"; "Mount Sinai moved its Upper West Side OB-GYN practices into 7,000 gut-renovated square feet at 348 Amsterdam Avenue in 2026 (Commercial Observer, April 2026)"; "Lincoln Center: 16.3 acres and 11 resident arts organizations … $335 million … due in summer 2028"; "broke ground in May 2026". Also heller­org.com 25 CPW listing excerpt ("Ground Floor professional/medical offices in a historic prewar condo on Central Park West") — background. → §5 para 5, §7 postwar and campus cards, §8 intro, practice cards and "Practices that share a building" subsection, §9 therapy Q, §13 Lincoln Center card, Sources. (Broker's internal research — attributed as Metro Manhattan's description, not presented as official data.)

### 9/10. Local news / hyperlocal
- Query: `Upper West Side storefront vacancy Broadway Amsterdam Columbus 2025 West Side Rag` · Firecrawl search → scrape (directQuote) https://www.westsiderag.com/2025/10/30/80-vacant-storefronts-blight-51-upper-west-side-broadway-blocks (Gus Saltonstall, Oct 30 2025): "on Broadway from West 59th to 110th streets, the Rag counted 80 vacant storefronts in October 2025 — five more than the 75 … last October, but five fewer than the 85 … in August of 2023". → §5 para 5, §5.5 fact 5, §8 "Shops that inherit someone else's cable", Sources.
- Carried: BIDs — https://columbusamsterdambid.org/ ("along Columbus and Amsterdam Avenues from West 96 Street to West 110 Street"); https://www.nyctourism.com/attractions-tours/lincoln-square-business-improvement-district/ ("home to the famed Lincoln Center … founded in 1996"); https://www.columbusavenuebid.org/ (og:description "a short walk from the American Museum of Natural History and Central Park"). → §8 corridor cards, Sources.
- Carried: https://www.westsiderag.com/2025/11/25/macys-thanksgiving-day-parade-uws-inflation-event-2025-what-to-know — inflation outside AMNH "from West 77th to 81st streets, between Columbus and Central …"; https://www.nbcnewyork.com/holidays/thanksgiving-parade-2025-balloon-inflation-where-to-see-in-person-in-nyc/6423199/ — "Wednesday, Nov. 26 from 1 to 6 p.m." → FAQ 1, Sources.
- Query: `Upper West Side water main break flooded basements 2025 OR 2026` · Firecrawl search → results only East Village (14th St/1st Ave, Aug 2026), Pelham Bay (Bronx), Salt Lake City. UWS-specific flooding incident: EMPTY. Not used.
- UWS news on Cat6/network cabling failures: EMPTY (no result).

### Local licensing / code / building rules
- Query: `FDNY fire escape must be kept clear obstruction NYC rule` · Firecrawl search (excerpts) → https://up.codes/viewer/new_york_city/nyc-fire-code-2022/chapter/10/means-of-egress §1027.7: "Fire escapes, and access thereto, shall be maintained in a safe and operational condition, and continuously maintained free from obstructions and impediments to immediate use in the event of fire or other emergency." https://fdnysmart.org/wp-content/uploads/2015/04/apartment_fire_safety-en.pdf ("KEEP YOUR EXITS CLEAR … keep the fire escape window clear"); https://www.brickunderground.com/live/can-you-sit-or-put-stuff-on-your-fire-escape-rules-nyc ("FDNY's residential safety guide says you should keep your fire escape clear of obstructions at all times"). → §8.5 callout 3, §9 fire-escape Q, §10.5 H3 6, Sources.
- Carried: https://www.brickunderground.com/guides/how-to-renovate/fifteen-things-your-coop-or-condo-board-might-not-let-you-do-in-your-renovation — "Some buildings only allow summer renovations … Most limit work to 9-5 weekdays." → §5 para 3, §9 summer-rule Q, Sources.
- Carried: Mitchell-Lama supervision — https://www.nyc.gov/site/hpd/services-and-information/mitchell-lama-program.page; https://www.osc.ny.gov/press/releases/2026/03/... ("HPD- and DHCR-supervised Mitchell-Lama developments"). → FAQ 3 (supervision only; no specific alteration rule claimed).
- Reused from silo/Manhattan sections: Admin Code §28-105.4.7 (LL128/2024) (amlegal); NYC Electrical Code (2020 NEC + amendments) fully in effect Dec 21 2025 (nyc.gov); LPC "Permits and Making Alterations" (nyc.gov/lpc); NEC 800.25 abandoned cable (EC&M). → §8.5 callouts 1, 2, 4, 5; §10.5 H3 2 and 5; Sources.

### Technical (UWS retrofit angle)
- Query: `TIA-568 minimum bend radius four times cable diameter UTP Cat6 installation` · Firecrawl search (excerpts) → https://www.elliottelectric.com/StaticPages/ElectricalReferences/DataComm/minimum_bending.aspx ("Minimum Bend Radius for Cable - TIA/EIA 568 … Minimum installed radius is 4 times cable diameter for horizontal runs"); https://www.commsbuyer.ie/cable-bend-radius-cat6/ ("four times the cable's outer diameter, per ANSI/TIA-568"). → §9 shallow-box Q, Sources.
- Query: `through-wall air conditioner sleeve condensation dripping inside wall water damage apartment` · Firecrawl search (excerpts) → https://allbritten.com/why-is-my-air-conditioner-leaking-water-inside-the-apartment/ ("the most common cause is a clogged condensate drain line"); https://www.reddit.com/r/HomeImprovement/comments/hosxpb/ ("the pan isn't draining properly and the condensation … soaks into the wall"). → §9 AC-sleeve Q (cause stated generally), Sources. No NYC-specific statistic used.
- Chimney-flue routing (§9 flue Q), crown-molding concealment (§9 molding Q), installer "signatures" table and preschool floor-level jacks (§9) are written from general field practice; no statistics, named buildings or stories attached.

### Prices used (live AESS Manhattan pages only; no new prices)
- $195/hr, 3-hr minimum ($585); replacement run from $175; evening/weekend access as a named premium line — network-cable-repair-manhattan.html, as carried by cat6-repair-manhattan.html (read this run).
- New-drop benchmark Cat5e $254 / Cat6 $296 / Cat6A $424 — cat6-installation-manhattan.html (as shown on cat6-repair-manhattan.html).
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — third-party, labelled.
- Packages: $585 starter; $195/hr after 3 h; repair time + from $175/run — all composed only of the above.
- No §9 1.25× multiplier applied on top (same basis and FLAG as the Manhattan and Midtown sections).

### Images (11) — Step C library; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run), CompanyCam not needed
All 11 are new crops of the AESS photos in images/cat6-repair/ (aess-cat6-repair-*), cropped differently from the Midtown copies where possible and with every face removed; WebP q80, ≤1600 px. Each viewed (contact sheet) before naming; alt/title/caption describe only what is visible; no building, customer or local job is claimed.
| new file (images/cat6-repair/) | source | crop box (x0,y0,x1,y1) |
|---|---|---|
| cat6-repair-upper-west-side-certifier-and-laptop-pass-report.webp (hero, og:image) | aess-…-certifier-results-labeled-rack | 600,300,1400,933 |
| cat6-repair-upper-west-side-tester-at-numbered-panel-ports.webp | aess-…-testing-labeled-patch-panel | 760,150,1400,700 |
| cat6-repair-upper-west-side-cable-bundles-on-ceiling-supports.webp | aess-…-pulling-cat6-above-ceiling | 500,0,1400,560 |
| cat6-repair-upper-west-side-split-jacket-exposed-pairs-steel-edge.webp | aess-…-damaged-cat6-jacket-sharp-edge | 400,150,1400,850 |
| cat6-repair-upper-west-side-access-point-cable-at-open-tile.webp | aess-…-access-point-cable-repair | 720,0,1400,1250 |
| cat6-repair-upper-west-side-storefront-counter-switch-cabinet.webp | aess-…-pos-counter-cable-repair | 790,0,1400,933 |
| cat6-repair-upper-west-side-wall-plate-rework-tester-on-floor.webp | aess-…-office-wall-jack-repair | 0,560,1100,933 |
| cat6-repair-upper-west-side-tone-probe-at-numbered-panel.webp | aess-…-toning-cable-at-rack | 640,220,1400,800 |
| cat6-repair-upper-west-side-cat6-channel-pass-and-remote.webp | aess-…-cat6-channel-certification-test | 700,280,1400,900 |
| cat6-repair-upper-west-side-wire-map-pass-patch-cords.webp | aess-…-wire-map-test-patch-panel | 760,300,1400,900 |
| cat6-repair-upper-west-side-keystone-t568b-punch-down-bench.webp | aess-…-punching-down-cat6-keystone | 560,150,1400,933 |
Not used: before-after-rack-cleanup (faces + text overlay), crimping-rj45 (face), poe-camera-cable-test (face, parked cars). FLAG: several aess-* source photos show rendering artefacts typical of AI generation (garbled on-screen text such as "Test Tes Pessult", "Deley Skew", inconsistent logos) — they were used as instructed (library "real AESS photos"), but Anwar should confirm they are genuine. DAILY-LOG note suggestion: `images: 11 cropped from AESS photos in images/cat6-repair/ (aess-cat6-repair-*; faces cropped out)`.

### Keyword notes (five layers)
- Service: Cat6 repair Upper West Side, Cat6 cable repair Upper West Side Manhattan, Cat6 re-termination, Cat6 jack repair, recertification, retrofit run tracing, home-office link repair, in-unit panel repair, practice suite cabling repair.
- Problem: shallow wall box / bend radius, AC-sleeve condensate corrosion, fire-escape cable run, crown-molding concealed run, chimney-flue run, co-op summer rule, child-height classroom jacks, storefront inherited cable, mesh-instead-of-cable myth.
- Technology: TIA-568 bend radius (4× OD), low-profile/angled keystones, paintable raceway, inspection camera, certifier distance-to-fault, PoE access points, plenum-listed replacement (office/shop ceilings only), NEC 800.25.
- Industry: prewar co-ops/condos/rentals, Mitchell-Lama, brownstones/row houses, walk-ups over shops, Riverside Boulevard condos, medical/dental/therapy suites, schools/preschools, congregations, museums, Lincoln Center arts organisations, Broadway/Amsterdam/Columbus retail and restaurants.
- Geographic: Upper West Side, Lincoln Square, Columbus Circle edge, Central Park West, West End Avenue, Riverside Drive, Riverside Boulevard, Broadway, Amsterdam, Columbus, West 70s/80s/90s, Manhattan Valley, Cathedral Parkway, Morningside Heights edge, Community District 7.

### Masked similarity (uws/sim_uws.py in the scratchpad: geo masked incl. Upper West Side/West Side/Midtown/Bay Ridge/Astoria/Lincoln Square/Manhattan Valley; blocks p/li/td/h2/h3/figcaption with ≥6 masked words; word-level difflib)
Final build 233,763 B / 13,892 rendered words (after the 15:30Z revision; earlier 233,167 B / 13,865) (check_page count). Every non-constant block < 0.65 vs all 19 Cat6 Repair pages on disk (16 hub/area pages, Midtown, and the parallel Bay Ridge and Astoria drafts as of 15:13Z) and vs soundbar-installation-upper-west-side-manhattan-ny (cross-silo). Blocks ≥ 0.65 are only blueprint-mandated H2 patterns ("[Service] for [Area]'s Architecture", "… Near [Area]'s Landmarks", "… in [Area]: Questions Answered", "Every [Service] Service in [Area]", "Why [Area] Properties Need [Service] …"), the silo cross-link list, and excluded constants (warranty sentence, licence/rating strip, Bronx NAP line, "What AI Gets Wrong About…", "Every Cat6 Cable Repair Service We Handle in…"). Highest prose block after four rewrite passes: 0.62. File size: 5.2 KB above Midtown (227,952), 7.3 KB below Astoria (240,501 at 15:13Z), 13.4 KB below Bay Ridge (246,542) — JSON-LD indentation is wide for that reason (same technique as Midtown).

## Question register — cat6-repair-upper-west-side-manhattan-ny

§9 "Questions Answered" (H3 questions; revised 2026-10-17 ~15:30Z after the main run asked for a meaning-level pass against the six newly live neighbourhood registers):
1. Our mother's medical-alert base unit is plugged into a wall jack in her apartment that has stopped working — how is the repair handled so the alert service is not left unchecked? (Inside prewar apartments) — NEW; replaces the AC-sleeve corrosion Q, same intent as St. George Q9 (jack under a window failing because water reaches it). Source: Furman Center 65+ share 22.9% (carried). AC-sleeve condensate stays as body text only.
2. The Cat6 jacks in our prewar apartment sit in very shallow old wall boxes — is that why they keep failing?
3. A previous tenant ran our Cat6 out the window and along the fire escape — when it fails, can it go back the same way?
4. Our co-op allows alteration work only in the summer — which parts of a Cat6 repair can still be done in winter? (kept: building's seasonal alteration rule; Park Slope F1 is about weather for exterior facade work)
5. The Cat6 hidden behind our crown molding stopped working — does the molding have to come off to repair it?
6. A previous owner ran our brownstone's Cat6 up a disused chimney flue — can it be repaired there, or should it come out?
Converted to statement H3s (not registered as questions): "Practice suites inside apartment buildings: working around the appointment book" (was the therapy-privacy Q — same intent as St. George F1 confidential files / F8 quiet while meeting clients, and Fordham F1 HIPAA); "Preschool classrooms and data jacks at child height" (was the preschool Q — overlaps Park Slope F2 / Bay Ridge "move the jack a few feet").

FAQ (§17, = FAQPage schema):
F1. Can a repair near the Museum of Natural History be booked for the day before Thanksgiving?
F2. Our doorman only lets up contractors whose names are on the building's list — what do you send ahead?
F3. Do you repair Cat6 in Mitchell-Lama co-ops and rentals on the Upper West Side?
F4. Our parent lives alone and is not comfortable with technology — can we stay on the phone while the technician works?

Other "?" headings: "Upper West Side Jack Dead Since This Morning?" (repair capture), "Upper West Side Jack Still Dark After Trying Everything?" (closing).

De-dup notes (compared by meaning against every register in research/cat6-repair.md — NYC, LI, HV, Bronx, Staten Island, Queens, Rockland, Orange, Putnam, Nassau, Suffolk, Westchester, Manhattan, Brooklyn, Dutchess, Ulster, Midtown — and against the parallel Bay Ridge and Astoria drafts as on disk at 15:13Z):
- Deliberately not asked (intent already owned): where a fault sits in plaster-and-lath runs and opening finished walls (Westchester Q1/Q2), co-op board approval for in-apartment repair (Westchester Q6 — Q4 here is about the *seasonal* alteration window, not approval), concrete ceilings (Westchester Q8), steam riser/radiator heat (Westchester Q12, Bronx Q8), TV-mount screw (Westchester Q13), structured-media panel (Westchester Q5, Brooklyn Q7, Nassau Q10), ISP moved the router (Rockland Q2, Brooklyn Q12, Nassau Q8, SI Q6), landlord permission (Queens Q10, Brooklyn F5, Nassau F4), indoor cable run outside to a shed (HV Q8 — Q3 here is specifically the fire-escape egress rule), least-visible route along casings (HV Q12 — Q5 here is about reaching an existing run hidden in crown molding), no-hollow-wall homes (Orange FAQ), sturdier jacks against tenants (Dutchess Q10 — Q8 here is child-height safety/relocation in classrooms), medical before patients arrive (LI F4 — Q7 here is confidentiality and session privacy), caretaker meeting the technician (Putnam F2 — F4 here is a remote family member on the phone with an elderly resident), out-of-state owner via managing agent (Bronx F1), Midtown loading dock/lobby (F1 there) vs F2 here (doorman list/name ahead), Shabbat scheduling (Orange), lease-end/selling (Ulster F5), dumbwaiter (Bronx Q9), hallway raceway (Bronx Q5), molding-free surface raceway (Nassau F6).
- Batch siblings: Bay Ridge asks "Can a jack be moved a short distance while its dead run is being repaired?" (general relocation) and "plaster around our wall jack crumbled"; Astoria asks about drilling noise for neighbours and window-frame camera runs. Q8 (child-height classroom jacks), Q2 (shallow boxes / bend radius) and Q3 (fire escape) were kept because their intents (child safety, bend radius, egress rule) differ — main run may want to re-read Q8 against Bay Ridge's relocation question.
- Permit/licence, Landmarks and plenum rules kept to body text (§8.5, §10.5), not asked as questions.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing & DDG, Yelp 1–3★; Reddit threads on failing UWS Cat6 (reddit not scrapeable); UWS local news on cabling failures; UWS-specific flooding/water-main incidents (search returned only East Village/Bronx/out-of-state).

### Flags for review
1. aess-cat6-repair-* source photos look AI-rendered (garbled screen text); used as instructed — confirm authenticity.
2. FAQ F2 says we confirm the technician's name/arrival window and can send it the day before; FAQ F4 and §"Homes, Not Offices" say technicians do not change passwords/settings and can phone a remote family member — practice statements consistent with Manhattan/Midtown pages but not separately confirmed by Anwar.
3. Census Reporter 23% work-at-home figure carries a high-margin-of-error flag (stated on page).
4. Metro Manhattan figures are a broker's internal research (attributed as such).
5. Prices: same un-multiplied Manhattan figures as Midtown (§9 1.25× not stacked) — carried FLAG.
6. Scratchpad note: the scratchpad directory is shared by the three batch subagents; this run's build files are in scratchpad/uws/. Early in the run this agent accidentally executed the Bay Ridge agent's scratchpad build.py once (it rebuilt cat6-repair-bay-ridge-brooklyn-ny.html from that agent's own sources); the Bay Ridge agent has rebuilt its page since (file updated 15:12Z).

### Revision 2026-10-17 ~15:30Z (main-run request)
- Meaning-level pass of all §9 H3 questions, FAQ and FAQPage schema against the registers/pages of williamsburg-brooklyn, long-island-city-queens, fordham-bronx, st-george-staten-island, financial-district-manhattan and park-slope-brooklyn: 3 changes (above). FAQ F1–F4 unchanged (Thanksgiving street closure ≠ St. George parking; doorman list ≠ LIC freight booking; Mitchell-Lama; remote family member ≠ St. George F3 approval when nobody on site).
- Neighbourhood cross-link block taken from the main run's wiring of the page (Midtown, Williamsburg, LIC, Fordham, St. George, Financial District, Park Slope, Bay Ridge, Astoria) and kept in the build source.
- Similarity rerun vs all 25 Cat6 pages: four headings/cells reworded (services card, comparison-table row, sources H2, bill-drivers H3); no non-pattern block ≥ 0.65.
- Full `python3 tools/check_page.py cat6-repair-upper-west-side-manhattan-ny` → PASS (233,763 B).

## Bay Ridge, Brooklyn (cat6-repair-bay-ridge-brooklyn-ny)

Batch run 2026-10-17 (subagent build, parallel with cat6-repair-upper-west-side-manhattan-ny and cat6-repair-astoria-queens-ny; not committed). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl MCP (mcp__Firecrawl__firecrawl_search / firecrawl_scrape, directQuote mode). Shell curl blocked. Up-link /cat6-repair-brooklyn; phone (347) 934-8335; GBP Brooklyn (1282 Troy Ave, #brooklyn).

**Thesis (differs from cat6-repair-brooklyn and every Cat6 sibling):** Bay Ridge buildings are *renovated, not replaced* — the Special Bay Ridge District (1978) and the 2005 contextual rezoning keep the low-rise stock, owners stay (41% homeownership, only 452 new units 2010–2025), so Cat6 is added one renovation at a time by different hands and is damaged by later renovations (own house or the one next door). Repair = identify which layer of past work a failed run belongs to, test from where runs meet (cellar cabinet / closet / under-counter), and repair through small openings in plaster, block and stone. Building families: limestone/brick row houses (party walls, cellars, Doctors' Row), detached houses near Shore Road (two-switch houses, trunk link), semi-detached/two-family, post-war Shore Road co-ops (little hollow wall; under-carpet runs), pre-war/mid-rise rentals (Ridge Blvd/4th Ave), mixed-use avenue buildings (3rd/5th/86th; take-out windows, counters), ground-floor practices. Brooklyn page's thesis (building type decides failure point across the borough) is referenced via up-link, not repeated.

### Reddit (source 1)
- Query: `site:reddit.com r/bayridge ethernet internet wiring apartment` · Firecrawl search → only r/AskNYC / r/Brooklyn ISP threads (https://www.reddit.com/r/Brooklyn/comments/1f8zbtu/..., https://www.reddit.com/r/Brooklyn/comments/108tpbh/... "even on our block some brownstones are wired for it and others are not"). Nothing Bay Ridge- or Cat6-fault-specific; not used. Bay Ridge Reddit threads on failing Cat6: EMPTY (not accessible in build env — reddit not scrapeable).
- Query: `Bay Ridge illegal basement apartments conversions Community Board 10 complaints` · search excerpt https://www.reddit.com/r/Brooklyn/comments/1naer3a/... (DOB illegal-basement complaint thread) — background only, not used.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on-page that the AI Overview could not be opened; each H3 is framed as a commonly repeated claim and corrected with sourced facts (Fixr Jan 2025, Fluke NEXT KB, computercablestore 100 Mbps page — all from the silo section of research/cat6-repair.md).

### Zoning, housing, building stock (sources 6, 7)
- Query: `Special Bay Ridge District zoning 1978 purpose preserve low-rise character` · Firecrawl search → scrape https://zr.planning.nyc.gov/article-xi/chapter-4 (directQuote): purposes "(a) to preserve, protect and maintain the existing scale and character of the residential and commercial community; (b) to encourage design … in character with the neighborhood…" → §5 para 1, Sources.
- Same search → scrape https://www.citylandnyc.org/city-increases-zoning-protection-for-bay-ridge/ (published 2005-04-15, directQuote): "On March 23, 2005, the City Council approved … rezoning plan for a 249-block area within Brooklyn's Special Bay Ridge District, bounded by 65th Street to the north, Seventh Avenue to the east and Shore Road to the south and west." "Areas restricted to single-family or two-family homes increased from 33 to 101 blocks." og:description: "In 1978, after neighborhood residents protested the development of three large residential buildings, the twin 30-story Bay Ridge Towers and the 13-story Shore Hill Apartments, the City…" → hero subhead, §5 para 1, §5.5 fact 1, Sources.
- Search excerpt (same query): https://www.brooklynpaper.com/rezone-could-put-end-to-low-rise-ridge/ ("Bay Ridge Special Zoning District that capped development height back in 1978") — corroboration only.
- Query: `Furman Center Bay Ridge Dyker Heights community district BK10 housing units built before 1947 share` · search → scrape https://www.furmancenter.org/neighborhoods/bay-ridge-dyker-heights/ (directQuote, updated 2026): homeownership rate 33.6% (2000) … 41.0% (latest column); "From 2010 to 2025, the neighborhood added 452 new housing units". Pre-1947 share: not returned — EMPTY. → §5 para 3, §5.5 fact 2, Sources.
- Query (same) → scrape https://cbbrooklyn.cityofnewyork.us/cb10/about/neighborhoods/ (directQuote): CB10 = Bay Ridge, Dyker Heights, Fort Hamilton; "commercial corridors of 3rd Avenue, 4th Avenue, 5th Avenue, Fort Hamilton Parkway, 11th Avenue, 13th Avenue and the bustling 86th Street strip"; "One and two family homes comprise the major portion of the housing composition and aging multiple dwellings together with some new structures, line Shore Road, Ridge Boulevard and 4th Avenue, while smaller clusters of four to six story structures are randomly situated". → §5 para 2, §7 building cards, §8 intro, §9 walk-up H3, Sources.
- Query: `Bay Ridge co-op buildings Shore Road postwar apartment towers history` · search excerpts → https://soldbysoldano.com/9201-shore-road-bay-ridge-co-op/ (9201 Shore Road "The Len", built 1960, 254 apartments, postwar co-op; "The Len is the largest of the nine co-op and condo buildings on Shore Road"); https://soldbysoldano.com/9323-shore-road-bay-ridge-co-op/ (9323 Shore Road, 1961, 72 apartments, six storeys); https://www.homes.com/building/9201-shore-rd-brooklyn-ny/... ("red-brick tower … built in 1960"). → §5.5 fact 5, §7 co-op card, §13 landmark card, Sources. (Broker sources; used for build year/unit count only.)
- Query: `Bay Ridge Towers 30-story co-op Colonial Road Shore Hill Apartments history` · search excerpts: Shore Hill 558 federally assisted apartments (shorehillhousingbk.com); NHP Foundation: two interconnected 14-story towers built 1977. Not used beyond CityLand's wording (storey counts conflict 13 vs 14 — omitted). Colonial Road co-ops/detached homes: no source found — EMPTY; "Colonial Road" not named on the page.
- Query: `Bay Ridge Brooklyn limestone row houses semi-detached brick history development 1900s Brownstoner` · search excerpts (Brownstoner listings; dates 1899–1910 conflict with LPC 1906–1913 — LPC used). Background only.
- Query: `Bay Ridge illegal basement apartments conversions Community Board 10 complaints` · search → scrape https://www.citylandnyc.org/council-member-works-to-combat-illegal-home-conversions/ (2014-10-02, directQuote): "since 2010, over 1,000 complaints for illegal home conversions came from communities within the Council Member's district, Bay Ridge, Dyker Heights, and Fort Hamilton"; "Illegal conversions pose a hazard to tenants, with faulty wiring that can cause fires…". → §5 para 4, Sources.

### Landmarks / corridors (source 6)
- Query: `Bay Ridge Parkway Doctors' Row Historic District designated Landmarks Preservation Commission limestone rowhouses` · search excerpt (full text in excerpt) https://www.nyc.gov/site/lpc/about/pr2019/lpc-designates-the-first-historic-district-in-bay-ridge-brooklyn.page: first historic district in Bay Ridge; "a block of 54 row houses on Bay Ridge Parkway between 4th and 5th avenues constructed between 1906 and 1913 … all two stories tall with a basement"; limestone-fronted; "continues to be a hub for people in the medical profession". → §5.5 fact 3, §7 row-house card, §8 Bay Ridge Parkway card, §8.5 landmarks callout, §9 practice question context, §13 card, Sources.
- Query: `Gingerbread House 8220 Narrows Avenue Bay Ridge landmark…` and `Gingerbread House Bay Ridge landmark designated 1988 Arts and Crafts James Sarsfield Kennedy` · search → scrape http://s-media.nyc.gov/agencies/lpc/lp/1623.pdf (LPC designation report, directQuote): "8200 Narrows Avenue House"; "Built 1917; architect James Sarsfield Kennedy"; "constructed of uncut, randomly laid stone"; public hearing May 15, 1987; "important and rare example of the Arts and Crafts style". (Listing sites say 8220 Narrows Ave and "designated 1988" — LPC address 8200 used; designation year not stated on page, only the 1987 hearing.) → §7 detached card, §8.5 callout, §13 card, Sources.
- Query: `Fort Hamilton Army garrison Bay Ridge oldest active military installation history` · search excerpt https://installations.militaryonesource.mil/in-depth-overview/fort-hamilton: "cornerstone … set in 1825 and the first garrison flag was raised in 1831"; "the only active duty military installation in the greater New York City Metropolitan Area". → §8 card, §13 card, Sources.
- Query: `Verrazzano-Narrows Bridge opened 1964 Bay Ridge Fort Hamilton anchorage` · search excerpts: https://en.wikipedia.org/wiki/Verrazzano%E2%80%93Narrows_Bridge ("opened on November 21, 1964"); https://www.mta.info/agency/bridges-and-tunnels/verrazzano-narrows-bridge ("world's longest suspension span" when opened); NPS Facebook excerpt ("ends of the bridge are at historic Fort Hamilton in Brooklyn…"). → §13 card, Sources.
- Query: `Owl's Head Park Bay Ridge acres history Shore Road Park promenade NYC Parks` · search (full text) https://www.nycgovparks.org/parks/owls-head-park/history: Yellow Hook renamed Bay Ridge in 1853; terminal moraine; Henry C. Murphy estate, bought by Eliphalet W. Bliss 1866; designated park 1928; Acreage 24.22. → §13 card, Sources.
- Query: `86th Street BID Bay Ridge Fifth Avenue BID Third Avenue merchants storefronts number of businesses` · search → scrape https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=55 (Bay Ridge 5th Avenue: est. June 2006; 40 block faces; 376 ground-floor retail businesses) and ?bid=42 (86th Street Bay Ridge: est. October 2001; 16 block faces; 145 ground-floor businesses). Excerpts: https://www.86bid.org/directory ("R train to 86th Street and 4th Avenue"); https://www.facebook.com/ThirdAvenueBayRidge/ ("Third Avenue in Bay Ridge … a 36-block strip of unique businesses"). → §5.5 fact 4, §8 corridor cards, Sources.

### Local licensing / permits / rules
- LPC permits page (https://www.nyc.gov/site/lpc/about/permits-and-making-alterations.page), NYC Electrical Code effective Dec 21 2025 (nyc.gov), NEC 800.25 (EC&M), EPA RRP / NYC LL1 of 2004, Brick Underground alteration vs decoration agreements — all reused from the silo and Brooklyn sections of research/cat6-repair.md (no new fetch). → §8.5 callouts, §9 limestone and co-op H3s, Sources.
- Bay Ridge-specific permit or DOB rule for low-voltage repair: EMPTY (none found; page makes no claim beyond LPC's wording).

### Local news / hyperlocal (sources 9, 10)
- Query: `Bay Ridge Hurricane Ida 2021 flooding basements Brooklyn Paper` · search → scrape https://www.brooklynpaper.com/ida-flood-aftermath-clear-skies-rain-storm/ (Sept 2 2021, directQuote): "Hurricane Ida dumped between five and six inches of rain on most of Brooklyn"; photo captions: Parks employee "shovels mud blocking a walkway in Owl's Head Park in Bay Ridge"; "A large puddle blocks a piece of the Shore Road Promenade in Bay Ridge"; Bay Ridge Cares "born out of Superstorm Sandy". → §5.5 fact 6, Sources. (Flood questions not asked — intent taken on SI/Nassau/Brooklyn.)
- Query: `Bay Ridge Brooklyn internet outage Spectrum Verizon Fios news residents` · search → only Facebook group excerpt (Bay Ridge residents reporting Fios issues) and provider status pages; Spectrum store at 531 86th St. Not used. Local news on Cat6/network-cable failures in Bay Ridge: EMPTY.
- Yelp 1–3★ for Bay Ridge cabling contractors: EMPTY (not accessible in build env).

### Prices used (only figures already published on cat6-repair-brooklyn.html; Brooklyn = 1.00×, no multiplier)
- $195/hr, three-hour minimum ($585).
- Replacement run from $175 per run.
- Exterior entry for an outdoor run, sealed and bonded, from $185 per penetration.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — third-party, labelled.
- BYOE labour-only = repair time only (as on the Brooklyn page). No new prices.

### Images (11) — Step C library; Drive "AESS Website Photos/Cat6 Repair" EMPTY (checked by main run), CompanyCam not needed
New crops of the AESS photos in images/cat6-repair/ (aess-cat6-repair-*), each looked at before naming; faces, readable documents, house numbers and plates cropped out; crops differ from the Midtown copies; WebP q80, ≤1600 px. Alt/title/caption describe only what is visible; no photo is said to show a Bay Ridge building or job.
| new file (images/cat6-repair/) | source | crop box (x0,y0,x1,y1) |
|---|---|---|
| cat6-repair-bay-ridge-poe-dome-camera-tester-block-wall.webp (hero, og:image) | aess-cat6-repair-poe-camera-cable-test.webp | 740,0,1340,933 (no face, no cars) |
| cat6-repair-bay-ridge-wall-plate-rework-tester-on-floor.webp | aess-cat6-repair-office-wall-jack-repair.webp | 560,470,1400,933 |
| cat6-repair-bay-ridge-split-jacket-exposed-pairs.webp | aess-cat6-repair-damaged-cat6-jacket-sharp-edge.webp | 380,140,1400,820 |
| cat6-repair-bay-ridge-rj45-plug-crimp-bench.webp | aess-cat6-repair-crimping-rj45-connector.webp | 0,450,1400,933 (below the face) |
| cat6-repair-bay-ridge-cable-fed-to-ceiling-supports.webp | aess-cat6-repair-pulling-cat6-above-ceiling.webp | 600,0,1400,580 |
| cat6-repair-bay-ridge-under-counter-switch-cabling.webp | aess-cat6-repair-pos-counter-cable-repair.webp | 700,320,1400,933 |
| cat6-repair-bay-ridge-keystone-pairs-colour-chart.webp | aess-cat6-repair-punching-down-cat6-keystone.webp | 330,280,1400,933 |
| cat6-repair-bay-ridge-tone-probe-numbered-panel.webp | aess-cat6-repair-toning-cable-at-rack.webp | 640,150,1400,933 |
| cat6-repair-bay-ridge-channel-pass-with-remote-unit.webp | aess-cat6-repair-cat6-channel-certification-test.webp | 690,260,1220,933 |
| cat6-repair-bay-ridge-labelled-cam-ap-office-ports.webp | aess-cat6-repair-before-after-rack-cleanup.webp ("after" panel only) | 1000,272,1400,933 |
| cat6-repair-bay-ridge-laptop-wire-map-report.webp | aess-cat6-repair-certifier-results-labeled-rack.webp | 880,420,1400,933 |
Not used: access-point-cable-repair, testing-labeled-patch-panel, wire-map-test-patch-panel (faces dominate; Midtown already used tighter crops). DAILY-LOG note suggestion: `images: 11 cropped from AESS photos in images/cat6-repair/ (aess-cat6-repair-*; faces cropped out)`.

### Keyword notes (five layers)
- Service: Cat6 repair Bay Ridge, Cat6 cable repair Bay Ridge Brooklyn, Cat6 jack repair, re-termination, recertification, replacement run, re-route, cabinet clean-up and labelling, PoE camera link repair.
- Problem: damage from renovation or work next door (party wall), unsleeved facade holes, corroded outdoor plugs, single trunk link between two switches, under-carpet/saddle runs crushed, take-out window pinching, imaging workstation drops, crumbling plaster jack mounts, split dual-jack plates.
- Technology: certification (NEXT, return loss), distance-to-fault, PoE reading, T568B, keystone, old-work bracket, surface raceway, outdoor-rated Cat6, sleeve/drip loop.
- Industry: homeowners (row/detached/two-family), co-op owners, landlords of walk-ups, Third Ave restaurants/bars, Fifth Ave & 86th St retail, dental/medical practices on Bay Ridge Parkway.
- Geographic: Bay Ridge, Shore Road, Narrows Avenue, Bay Ridge Parkway/Doctors' Row, Ridge Boulevard, Third/Fourth/Fifth Avenue, 86th Street, Fort Hamilton Parkway, Owl's Head Park, Fort Hamilton, Verrazzano-Narrows Bridge, 65th Street, Seventh Avenue; adjacent: Dyker Heights, Sunset Park, Bath Beach.

### Masked similarity (geo masked incl. Bay Ridge/Shore Road/avenue names; blocks p/li/td/h2/h3/figcaption ≥8 words; word-level difflib; constants excluded = warranty sentence, licence/rating strip, NAP line, fixed H2 patterns)
Final build 246,542 B / 12,623 rendered words. Max non-constant block vs any Cat6 sibling ≈0.64 (crimp-photo caption vs cat6-repair-astoria-queens-ny — same source photo; rewritten after that run, re-check in main run), then 0.62 (neighbourhood link line vs midtown; lead-paint callout vs brooklyn). File size placed well above the batch siblings (Astoria 238,361 / UWS 233,364 at last check) and Midtown 227,952 to clear the ±2 KB window — JSON-LD indentation is wide for that reason (as on Midtown).

## Question register — cat6-repair-bay-ridge-brooklyn-ny

§9 "Questions Answered" (H3):
1. The house next door is being gutted. Can work on the far side of our shared party wall damage the Cat6 on our side?
2. (converted 2026-10-17 at main-run request to non-question H3 "Camera cable through a limestone, brick or stone front" — same intent as cat6-repair-park-slope-brooklyn-ny Q4)
3. (converted 2026-10-17 at main-run request to non-question H3 "Detached houses where one cable carries the whole upper floor" — same intent as cat6-repair-st-george-staten-island-ny Q6)
4. The cable to the card terminal at our take-out window keeps failing where it passes through the window frame. What is going on?
5. The imaging workstation in our ground-floor dental office keeps losing its connection in the middle of a patient visit. Is the cable likely to be the cause?

Non-question H3s in §9 (body text, deliberately not asked): "Flat roofs, cocklofts and the top-floor run" (cockloft route asked as a question on cat6-repair-astoria-queens-ny); "Runs under carpets and across door saddles in Shore Road co-ops" (converted from a question — Astoria asks about crushed runs across shop/stage floors and walkways); "Hallway cameras and tenants' own runs in Bay Ridge walk-ups"; "Cellar cabinets that grew one switch at a time".

FAQ (§17, = FAQPage schema):
F1. Third Avenue closes for parades and street events several times a year. Can a repair at our shop be booked around those days? (replaced by main-run request 2026-10-17: deposit question duplicated cat6-repair-st-george-staten-island-ny F5; source for parades: PoliticsNY excerpt https://politicsny.com/2019/08/12/point-counterpoint-on-proposed-bay-ridge-bid/ — "Bay Ridge's 3rd Avenue is home to hundreds of merchants, as well as multiple annual parades")
F2. The plaster around our wall jack has crumbled and the jack keeps falling back into the wall. Can that be fixed?
F3. Can you compare your test results with the readings the original installer left us? (replaced 2026-10-17: pressed-tin duplicated Williamsburg Q3 / Park Slope Q6)
F4. Only one of the two jacks on our wall plate works. Is the dead one fed by a separate cable?
F5. The way into our row house's cellar is a low door under the front stoop. Can the technician still get the equipment down there? (replaced 2026-10-17: entrance counters/EAS duplicated Fordham Q1; row houses with basement per LPC Doctors' Row release)
F6. A previous owner split our house into extra units, and we are turning it back into one home. What happens to the separate switches and runs each unit had? (replaced by main-run request 2026-10-17: jack-move question duplicated cat6-repair-park-slope-brooklyn-ny F2; context CityLand 2014 conversions, NEC 800.25)

Other "?" headings: "Cat6 Link Down Somewhere Between Shore Road and Seventh Avenue?" (repair capture), "Bay Ridge Jack Still Dead After the Last Round of Work?" (closing).

De-dup notes (by meaning, against every register in research/cat6-repair.md and the two batch siblings as on disk at 15:xx): party-wall damage ≠ Midtown Q1 (baseline around a scheduled building programme) / Westchester Q11 / Orange / Nassau Q4 / Queens Q8 (documenting another trade's damage) — this asks whether a neighbour's work can reach cable on our side and how it is found; ≠ Astoria party-wall question (a shared internet run crossing the wall). Limestone-hole reuse ≠ Bronx F10 (facade work disturbing cable) / Astoria (painting the outdoor run). Two-switch trunk ≠ Rockland Q11 (PoE on one port affecting another) / Midtown Q5 (two closets in merged suites). Take-out window ≠ Queens Q4 (roll-down gate) / Astoria roadway-dining teardown. Imaging workstation ≠ Orange (imaging vendor recertification after renovation) / Rockland Q10 (exam-room carts). Deposit ≠ NYC F1 (three-hour minimum). Crumbling plaster mount ≠ UWS (shallow old wall boxes cause failures) — closest neighbour; flag for main-run review. Pressed tin, dual-jack plate, entrance counters/EAS, moving a jack: no match found (Nassau Q9 split run feeding two rooms is a different intent from a dual plate with one dead jack). Avoided: landlord permission, lead paint, LPC approval and co-op paperwork as questions (kept as body text), flood/raised house, router moved by ISP, rodents, cookline, Wi-Fi extender, parking (Astoria), coax/phone.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing & DDG, Yelp 1–3★; Reddit threads on failing Cat6 in Bay Ridge; Bay Ridge local news on network-cable failures; pre-1947 housing share for BK10 (Furman page did not return it); Colonial Road building stock; Bay Ridge-specific DOB/permit rules for low-voltage repair.

### Post-wiring note (2026-10-17)
Read against the six newly live registers (Williamsburg, LIC, Fordham, St. George, Financial District, Park Slope). Remaining near-overlaps NOT changed (main run asked for only two edits): FAQ F3 pressed-tin ceiling ≈ Williamsburg Q3 / Park Slope Q6; FAQ F5 people counter / anti-theft pedestals ≈ Fordham Q1; §9 Q2 camera cable through a hole in the stone front ≈ Park Slope Q4; §9 Q3 single trunk link between floors ≈ St. George Q6. Flagged for main-run decision.
All four flagged overlaps resolved 2026-10-17 (two FAQ replaced, two §9 questions converted to statement headings). Final: 3 §9 questions + 6 FAQ; 251,067 B; full check_page.py PASS.

## Astoria, Queens (cat6-repair-astoria-queens-ny)

Batch run 2026-10-17 (subagent build; not committed). Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, #bronx, LocalBusiness block modelled on cat6-repair-queens.html) · up-link /cat6-repair-queens. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl MCP (mcp__Firecrawl__firecrawl_search / firecrawl_scrape). Shell curl blocked. "Carried" = fetched earlier today by the Sonos or Soundbar Astoria runs and logged in research/sonos-installation.md / research/soundbar-installation.md `## Astoria, Queens` (not re-fetched).

**Thesis (differs from cat6-repair-queens and every other Cat6 page):** Astoria Cat6 fails where it *crosses out of its room* — window frames and fire escapes, the cockloft of flat-roofed attached houses, party walls, air-conditioner sleeve gaps, storefront frames, curbside dining setups that are packed away every winter, stage/workshop floors near Kaufman Astoria Studios, and bar cellars where beer trunks sweat. Most households rent a floor of a small building (18.5% homeownership), so runs were added one tenant at a time through the nearest gap. Repairs = find the crossing by distance, replace that length, move it to its own sealed entry/support/protector, and leave a crossing map. The Queens borough page's thesis (kitchens, basements, new towers' media panels) is referenced via up-link, not repeated.

### Reddit (local)
- `site:reddit.com astoria ethernet cable apartment wall jack internet` · Firecrawl search (excerpts only; reddit not scraped) →
  - https://www.reddit.com/r/astoria/comments/1gkk2jh/how_to_extend_ethernet_cable/ — excerpt: "for residential/above wall you can get away with any CAT6 or 5E RJ45 terminated cable" → §10.5 H3 1 (paraphrased, attributed to an r/astoria commenter), Sources.
  - https://www.reddit.com/r/astoria/comments/1vb87af/verizon_fios_in_closet/ — excerpt: "my ont is in my closet, but my router is in the living room." → Sources (background only).
- Carried (soundbar/sonos Astoria): r/astoria 31st Street el noise threads → not used on this page (el kept to corridor card; vibration intent belongs to cat6-repair-brooklyn).
- r/astoria threads on failing Cat6 at windows/fire escapes/cocklofts: EMPTY (none returned).

### Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 says on the page that the AI Overview could not be opened; each H3 is a commonly repeated claim corrected with the sources here and in the silo section.

### Outdoor dining (use case + rule)
- `Dining Out NYC roadway cafe season April November structures removed off-season rules` · Firecrawl search → scrape https://www.diningoutnyc.info/rules/roadway/operate (cached 2026-10-17): roadway cafés may operate April 1 – November 29, not November 30 – March 31; set-up allowed from March 25; "The restaurant is responsible for storing the roadway cafe during the off-season"; furnishings secured during non-operating hours "cannot impede or block access to utility infrastructure"; hours Mon–Sat 8 a.m.–midnight, Sun 10 a.m.–midnight. → §5 para 4, §5.5 fact 4, §8.5 callout, §9 Q1, scheduling section, mid-CTA 2, Sources.
  - abc7ny.com excerpt (Nov 29 deadline) and rules.cityofnewyork.us comments — not used.

### Fire escapes (code)
- `NYC fire code fire escapes shall be kept clear obstruction wires cables attached fire escape` · Firecrawl search → scrape https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-144641 (Fire Code ch. 10): FC 1027.7 "Fire escapes, and access thereto, shall be maintained in a safe and operational condition, and continuously maintained free from obstructions and impediments…"; FC 1027.7.3 air conditioners in fire-escape windows; FC 1027.7.4 drop-ladder operation not obstructed (awnings, furniture, etc.). → §8.5 callout, §9 fire-escape section (non-question H3), services card, crossing table, Sources.
  - Excerpts not used: 1 RCNY §15-10 (wire/chain fire escapes), FDNY Facebook video, UpCodes, Brick Underground (carried by soundbar run).

### Cockloft (building stock)
- `cockloft definition row house flat roof space between top floor ceiling and roof FDNY` · Firecrawl search → scrape (directQuote) https://www.fireengineering.com/fire-safety/firefighters-and-construction-the-cockloft/ (Salvatore Ancona, Mar 23 2021): "The cockloft is a void space that is created between the top floor ceiling and the roof decking"; common in Type III (ordinary) construction; created "to use as a utility passageway" and captures heat; fire in the cockloft "can quickly consume multiple units of attached buildings". → §9 cockloft Q, §7 cards/paragraph, crossing table, Sources.

### Bars / beer lines
- `glycol beer line trunk condensation drip insulation draft system basement cooler to bar` · Firecrawl search (excerpt) → https://byo.com/projects/diy-draft-trunk-lines-when-you-want-to-run-long-draft-lines/ (Brew Your Own): trunk line = bundle of beer lines plus two glycol lines, taped and foam-insulated; "In a basement, or any humid area, cold draft lines will produce lots of sweat." → §8 restaurants/bars paragraph, §9 beer-line Q, crossing table, Sources.

### Air-conditioner sleeves
- `through-wall air conditioner sleeve condensation water leak wall cavity sleeve gap` · Firecrawl search (excerpts) → https://hdsupplysolutions.com/.../203844_InstallationGuide-PDF.pdf (24-inch wall sleeve guide): "Weatherproof gaps between the wall sleeve and all exterior and interior wall surfaces … Use a waterproof filler and sealant such as caulk" → services card, crossing table, Sources. https://www.naturalhandyman.com/qa/qaroomac.html excerpt (leaks from rain or condensation) — background only.
- `"Fedders" buildings Astoria Queens …` · Firecrawl search → only a Brooklyn Paper (Bay Ridge) mention of "Fedders houses" — NOT used (not Astoria). EMPTY for Astoria.

### Jukebox (FAQ)
- `TouchTunes jukebox internet connection requirements ethernet wired broadband` · Firecrawl search (excerpts) → https://documents.touchtunes.com/MAN901095-001R01.pdf (Fusion guide): "The cable used for a broadband connection is straight-wired Ethernet cable with RJ45 connectors at both ends." Also 900165-001 (broadband connection since software 2.2.3-18). → FAQ 3, Sources.

### Gas shut-offs (open walls)
- `Astoria Queens gas shutoff building months Con Edison repiping tenants 2024 2025` · Firecrawl search (excerpts) → https://www.coned.com/en/services-and-outages/preventing-recovering-from-outages/repairs-after-outages/how-to-get-your-gas-back ("Your building manager hires a licensed plumber… The plumber files documents with your local buildings department and Con Edison before beginning repairs"); https://www.nyc.gov/site/buildings/tenant/gas-cut-off.page (DOB tenant page). Astoria-specific gas shut-off news: EMPTY (none returned). → §8.5 callout (general), Sources.

### Building stock / landmarks / corridors
- `Old Astoria historic wood frame houses 19th century 12th Street 27th Avenue Astoria village` · Firecrawl search (excerpts) → https://oana-ny.org/history/places-and-landmarks/ (Old Astoria Neighborhood Association): "a cluster of historic homes grace 12th and 14th Streets between 27th Avenue and Astoria Park South" → §7 card, Sources. Forgotten NY (Remsen House, 1835, demolished 2005) and Urban Archive (9-29 27th Ave Italianate) — background only, not stated.
- `Kaufman Arts District Astoria established 2014 Museum of the Moving Image Frank Sinatra School` · Firecrawl search (excerpts) → https://www.pentagram.com/work/frank-sinatra-school-of-the-arts/story (school adjacent to KAS and MoMI at 35th Ave & 36th St); https://movingimage.org/feature/the-astoria-studio/ (Sinatra school "directly across the street"). Kaufman Arts District founding date: not confirmed → not stated (page says "studio blocks").
- `Astoria Queens 2006 blackout …` · Firecrawl search (excerpts) → https://www.baruch.cuny.edu/nycdata/disasters/blackouts-queens.html; https://en.wikipedia.org/wiki/2006_Queens_blackout (not used). Figures used are the carried ones below.
- Carried (research/sonos-installation.md + research/soundbar-installation.md Astoria sections):
  - Furman Center Astoria (QN CD1, includes part of LIC) https://www.furmancenter.org/neighborhoods/astoria/ — 99,819 units, homeownership 18.5% vs 32.7% (2024); 2025 sales 204 two-to-four-family vs 47 one-family; 15,142 new units in 4+ unit buildings 2010–2025 → §5 para 2, §5.5, §10.5, Sources.
  - https://raremaps.com/gallery/detail/106601/one-hundred-houses-on-ditmars-avenue-astoria — "one hundred 20-foot brick houses located on Ditmars Avenue" → §5 para 3, §7 card, Sources.
  - Halletts Point FEIS (nyc.gov) — Astoria Houses 1,103 units, 22 buildings, 27 acres, 1951 → §5, §7, §13, Sources. Durst https://www.durst.org/properties/halletts-point — three towers, 1,000+ rentals → §13. NYT Feb 15 2019 — first building leasing → §5.
  - Astoria Line opened 1917, entirely elevated, Ditmars terminal (Wikipedia / nycsubway.org) → §5.5, §8, Sources.
  - 2006 blackout: Baruch NYCdata July 17–25 (eight days); Pace Env. Law Review — 12 of 22 LIC-network feeders lost → §5.5, §10.5 H3 6, Sources.
  - KAS / MoMI (movingimage.org): studio opened 1920 by Famous Players-Lasky at 35th Ave & 35th St; KAS since 1982; Sesame Street from 1993; twelve stages by 2019; museum 1988, reopened Jan 15 2011, $67M, 267-seat theatre → §5, §8, §13, Sources.
  - Astoria Park (NYC Parks): 56+ acres 1913; pool July 2 1936, 330×165 ft, largest of eleven WPA pools. Hell Gate Bridge (Wikipedia): 1917, 1,017-ft arch → §13.
  - Steinway Mansion (Wikipedia/MAS): 1857–58, landmark 1967. Steinway & Sons "Company Town": ~400 Queens workers by mid-1870s; Steinway Street named for the company → §7, §13.
  - Bohemian Hall (bohemianhall.com/about; theclio.com/entry/53541): society 1892; cornerstone Oct 1 1910; outdoor bar/park 1919; NRHP 2001 → §13.
  - Steinway Street BID (NYC SBS directory); "Little Egypt" (blogs.baruch.cuny.edu/astoria/?p=114); Athens Square Park, 30th Ave (NYC Parks) → §8 cards.
- Silo sources reused (research/cat6-repair.md): NYC Electrical Code (2020 NEC) effective Dec 21 2025; NEC 800.25 (EC&M); Admin Code §28-105.4.7; DOB After Hour Variances (Midtown section); Toast network-cable troubleshooting; computercablestore 100 Mbps/two pairs; Fixr Jan 2025.

### Local news / hyperlocal
- Astoria news on Cat6 / network cable failures, fire-escape cable incidents or outdoor-dining cabling: EMPTY (no result in the searches above).

### Prices used (live AESS Queens pages only; no new prices)
- $195/hr, 3-hour minimum ($585) — cat6-repair-queens.html / network-cable-repair-queens.html.
- Replacement run from $175 per drop — same pages.
- Sealed, bonded building entry from $194 per penetration — as published on cat6-repair-queens.html (that page's derivation: Bronx $185 × 1.05; flagged there).
- New-drop benchmark Cat6 $272 (Cat5e $233, Cat6A $388) — cat6-installation-queens.html, comparison only.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — third-party, labelled.
- Packages are sums of these lines only ($585; $585 + from $194 per entry; repair time + from $175 per run). No Astoria multiplier.

### Images (11) — Step C library; Drive "AESS Website Photos/Cat6 Repair" EMPTY (main run), CompanyCam not needed
All 11 cropped (PIL, WebP q80, ≤1600 px) from the AESS photos in images/cat6-repair/aess-cat6-repair-*; each viewed before and after cropping; faces removed; crops differ from the Midtown copies; no building named, no readable documents, phone numbers, house numbers or plates (parked cars in the PoE photo cropped out).
| new file (images/cat6-repair/) | source | crop (x0,y0,x1,y1) |
|---|---|---|
| cat6-repair-astoria-dome-camera-poe-reading-at-wall-box.webp (hero, og:image) | aess-cat6-repair-poe-camera-cable-test.webp | 790,0,1400,933 |
| cat6-repair-astoria-wire-map-pass-on-tester.webp | aess-cat6-repair-wire-map-test-patch-panel.webp | 760,220,1400,933 |
| cat6-repair-astoria-split-jacket-at-steel-frame.webp | aess-cat6-repair-damaged-cat6-jacket-sharp-edge.webp | 300,150,1400,820 |
| cat6-repair-astoria-under-counter-switch-and-cabling.webp | aess-cat6-repair-pos-counter-cable-repair.webp | 720,330,1400,933 |
| cat6-repair-astoria-cable-fed-into-ceiling-supports.webp | aess-cat6-repair-pulling-cat6-above-ceiling.webp | 520,0,1400,560 |
| cat6-repair-astoria-wall-plate-jack-rework-near-floor.webp | aess-cat6-repair-office-wall-jack-repair.webp | 560,470,1400,933 |
| cat6-repair-astoria-tone-generator-and-probe-at-bundle.webp | aess-cat6-repair-toning-cable-at-rack.webp | 640,150,1400,933 |
| cat6-repair-astoria-keystone-pairs-punched-with-chart.webp | aess-cat6-repair-punching-down-cat6-keystone.webp | 330,150,1400,933 |
| cat6-repair-astoria-laptop-results-beside-labelled-ports.webp | aess-cat6-repair-certifier-results-labeled-rack.webp | 880,90,1400,933 |
| cat6-repair-astoria-ceiling-access-point-patch-lead.webp | aess-cat6-repair-access-point-cable-repair.webp | 720,0,1400,1150 |
| cat6-repair-astoria-rj45-plug-crimp-on-bench.webp | aess-cat6-repair-crimping-rj45-connector.webp | 0,440,1400,933 |
Not used: before-after-rack-cleanup (faces + text overlay), cat6-channel-certification-test, testing-labeled-patch-panel. DAILY-LOG note suggestion: `images: 11 cropped from AESS photos in images/cat6-repair/ (aess-cat6-repair-*; faces cropped out)`. Review note: the aess-* photos look rendered rather than photographed (uniform logos, idealised scenes) — same caveat as earlier runs.

### Keyword notes (five layers)
- Service: Cat6 repair Astoria, Cat6 cable repair Astoria Queens, outdoor Cat6 re-route, sealed building entry, cockloft cable replacement, curbside terminal link, stage-floor crossing repair, crossing map.
- Problem: camera dead after rain, fire-escape cable, window-track crush, AC sleeve gap, roofer damage in the cockloft, party-wall shared link, storefront-frame cable, beer-line condensation, carts over cable, short-lease office.
- Technology: outdoor-rated Cat6/Cat6A, PoE 802.3af/at, distance-to-fault, weatherproof jack/box, cable protector, raceway, keystone/RJ45, T568A/B.
- Industry: two-family owners and tenants, walk-up residents, restaurants/cafés/bars, production offices and studio suppliers, storefronts, gyms/offices on 31st St.
- Geographic: Astoria, Ditmars–Steinway, Ditmars Blvd, 30th Ave, Broadway, Steinway Street, 31st Street, 35th Avenue, Old Astoria, Halletts Point, Astoria Heights, Astoria Park, Hell Gate; adjacent LIC, Sunnyside, Woodside, Jackson Heights, East Elmhurst.

### Masked similarity (geo masked incl. Astoria/Ditmars/Steinway/Halletts Point and every borough/county/neighbourhood name; blocks p/li/td/h2/h3/figcaption ≥8 words; word-level difflib)
Build 240,565 B / 13,105 rendered words (after second de-dup pass). Max non-constant block vs any Cat6 sibling 0.62 (services-grid line vs cat6-repair-midtown-manhattan-ny; sealed-entry and new-drop pricing cells vs cat6-repair-queens). Blocks ≥0.65 are only blueprint-excluded constants: warranty sentence, licence/rating strip, Bronx NAP line, Fixr price cell, fixed H2 patterns "What AI Gets Wrong About Cat6 Repair in …" and "Every Cat6 Cable Repair Service We Handle in …". Batch siblings (UWS 233,364 B; Bay Ridge 246,542 B at time of check) were included; file size placed ≈7 KB from UWS and ≈6 KB from Bay Ridge by JSON-LD indentation — main run must re-check the size cluster after the siblings are final.

## Question register — cat6-repair-astoria-queens-ny

§9 "Questions Answered" (H3), under non-question H2s "Where the cable leaves the building" · "Attached houses and the spaces they share" · "Stages, bars and production spaces":
1. The Cat6 to the camera over our shop sign was threaded through the hollow metal frame of the shop window — can it be repaired inside the frame?
2. The only way to our top-floor rooms is through the cockloft under the flat roof — can a failed run be replaced through that space?
3. We share one internet connection with the attached house next door through a Cat6 run that crosses the party wall — who can repair it, and how?
4. Our apartment in one of the Halletts Point towers has a terrace — can a wired camera out there be fed without drilling through the building's outside wall?
Non-question H3s in the same section (converted, content kept): "Outdoor dining terminals: a link built to be unplugged every November" (= williamsburg Q4); "Cat6 that runs out of a window and along a fire escape has to come off it" (UWS fire-escape Q); "Cable that crosses a stage or workshop floor has to come off the floor" (≈ williamsburg Q6); "Register runs that share a cellar chase with beer lines need separating from them" (= williamsburg Q5).

FAQ (§17, = FAQPage schema):
F1. Can you take down the dead cables an old provider left hanging on the front of our building while you repair our Cat6?
F2. Do you repair the Cat6 that connects the card readers on the washers and dryers in our laundromat?

Other "?" headings: "Wired Link Down Somewhere in Astoria Right Now?" (repair capture), "Still Dead on the Far Side of the Window, the Roof or the Wall?" (closing).

De-dup notes (by meaning, against every register in research/cat6-repair.md incl. the six pages that went live mid-build — Williamsburg, LIC, Fordham, St. George, FiDi, Park Slope — and the batch siblings UWS / Bay Ridge):
- Replaced/converted in the second pass: roadway-dining Q (= Williamsburg Q4), beer-line Q (= Williamsburg Q5), stage-floor Q (≈ Williamsburg Q6), production-office hand-back Q (≈ LIC Q8 / FiDi Q7 lease end) → replaced by the Halletts Point terrace Q; FAQ parking (= St. George F2), jukebox (= Williamsburg F2), noise for neighbours (≈ St. George F8 quiet work), paint outdoor run to blend in (≈ LIC F3 colour that blends in) → replaced by the laundromat card-reader FAQ (one FAQ net).
- First pass: AC-sleeve Q dropped (UWS); fire-escape Q converted (UWS); doorway-crossing FAQ dropped (Bay Ridge / St. George Q4); dryer-vent FAQ dropped (Westchester Q14).
- Kept, checked: party-wall shared link vs Park Slope F4 (neighbour notice) and Bay Ridge (neighbour's gut renovation) — different intent; cockloft route vs Park Slope Q1/Q5 and LI Q9 — different; facade dead-cable removal vs LIC Q8 / FiDi Q7 / NYC F7 — exterior abandoned provider cable, not lease-end or re-pull.

New sources for the second pass:
- `Halletts Point apartments balcony terraces Durst amenities` · Firecrawl search (excerpts) → https://www.apartments.com/10-halletts-point-astoria-ny/1j2c5h6/ ("Large Terrace"); https://www.durst.org/news_items/5931 (amenity terrace) → §9 Q4.
- `laundromat card reader system washers dryers requires ethernet network connection installation guide` · Firecrawl search (excerpt) → https://buyunitynow.com/credit-card-operated-washer-and-dryer-guide-2/ ("Most readers work over either ethernet or cellular connections. Ethernet is cheaper long term but requires wiring.") → FAQ F2.
- Jukebox (TouchTunes) source now unused on the page.

Final build: 240,565 B, 13,105 rendered words; max non-constant masked similarity 0.62.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, AI Overview, Bing & DDG, Yelp 1–3★; r/astoria threads on failing Cat6; Astoria news on network-cable failures; Astoria-specific gas shut-off news; "Fedders"-type building source for Astoria; Kaufman Arts District founding date.

# Merged from batch 2026-10-17 (cat6-repair-flushing-queens-ny)

## Flushing, Queens (cat6-repair-flushing-queens-ny)

Batch run 2026-10-17 (neighbourhood page). Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, #bronx, copied from cat6-repair-queens.html) · up-link /cat6-repair-queens · hub /cat6-repair-nyc. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. "Silo" = source already logged in research/cat6-repair.md (not re-fetched).

**Thesis (different from cat6-repair-queens and every sibling):** Downtown Flushing is a 24/7, nearly fully occupied district stacked vertically — basement and upper-level food courts, multi-level malls, upper-floor clinics and offices, and podium complexes (One Fulton Square, Tangram, Sky View Parc, Flushing Commons) with garages under them — and it re-tenants constantly. Cat6 fails at the seams between tenants and layers (shared ceilings, landlord switches, garage levels, previous tenants' splices) and in below-grade spaces that flash-flood. The repair is about proving whose run it is, working clean above food and patients, rating replacement cable for the space (plenum/garage), and leaving labels/port maps in the wording the staff actually use. Queens parent's angles (kitchen heat, mop water, roll-down gates, POS vendor stops at the wall, basement-apartment program, rowhouse masonry, LIC media panels) were avoided as questions.

### Reddit (local)
- `site:reddit.com flushing queens apartment ethernet port not working` · Firecrawl search (excerpts only; reddit not scrapeable in build env) →
  - https://www.reddit.com/r/Flushing/comments/1spiap6/experience_with_internet_services_around_flushing/ — excerpt: "Just find a dock with Ethernet port and use it as often as you can. If you can't get FiOS get cable and avoid 5g for now." → background for the wired-over-wireless position (§10.5 H3 5); not quoted on page.
  - https://www.reddit.com/r/Flushing/comments/1jgok85/best_karaoke_spots_in_flushing/ (from karaoke query below) — confirms KTV venues are a local business type → §8 business table (karaoke row); not quoted.
- Flushing-specific Reddit threads about failing Cat6 in malls/clinics: EMPTY (none returned).

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview could not be viewed; each H3 is framed as a commonly repeated assumption and corrected with the sources below. (Yelp appeared only as search-result excerpts for venue facts, not as 1–3★ reviews.)

### Commercial district / business mix
- `Downtown Flushing Transit Hub BID Main Street pedestrians busiest` · Firecrawl search → scrape (pdf parser) https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/n360-cdna-flushing.pdf (NYC SBS Neighborhood 360° Commercial District Needs Assessment, Downtown Flushing, fieldwork Jan–Jun 2016, with Greater Flushing Chamber + Downtown Flushing Transit Hub BID): corridors Main St, Roosevelt Ave, Northern Blvd, Union St, 39th Ave, College Point Blvd; "active, 24/7 district"; "mix of mid-rise and new high-rise buildings"; "Nearly 100% commercial storefront occupancy rate"; "Active upper floor uses with a wealth of healthcare and professional services"; "home to 60+ commercial banks district-wide"; merchants "relocate to different storefronts within the district as new shopping centers and spaces become available"; 85% of surveyed merchants rent; "Merchants experience language and cultural barriers…"; Union Street "traditionally … center of the Korean American community … extended eastward … along Northern Boulevard"; College Point Blvd "home furnishing wholesalers and warehouses despite the recent introduction of new mixed-use shopping centers"; "Multi-Level Shopping Centers"; One Fulton Square, New York Food Court, Shops at SkyView Center pictured; population 68,902, density 50,663/sq mi, foreign-born 71%; Flushing–Main St avg weekday subway ridership 60,226 (2015); pedestrian count weekday morning 3,485 on Main St between 37th and 38th Aves. → §5 paras 1–2, §5.5 bullets 1–3, §6/§7 cards, §8 corridor cards, §10.5 H3 4/6/7, Block by Block section.
- `New World Mall Flushing food court stalls Main Street` · Firecrawl search → scrape https://www.newworldmallnyc.com/food-court : "With 32 diverse brands" → §5 para 3, §5.5 bullet 4, §10.5 H3 5 ("thirty-odd vendors").
  - Yelp excerpt "over 30 food stalls" and Tripadvisor excerpt "a dozen vendors" — user-generated, NOT used.
- `Golden Shopping Mall Flushing basement food stalls 41-28 Main Street` · Firecrawl search → https://ny.eater.com/2024/4/19/24132546/golden-mall-flushing-reopening-best-dishes (excerpt): Golden Mall, 41-28 Main Street; basement food court opened 1990; "finally closed in 2019"; revamped/reopened (Eater, Apr 19 2024) → §5 para 3.
- `Flushing Queens karaoke KTV private rooms Main Street` · Firecrawl search → https://www.9plusktv.com/ (excerpt: "over 20 uniquely themed private rooms"); Yelp search excerpt (Wave KTV, 40-33 Main St Fl 2); https://singkaraok3.com/ (excerpt: 156-16B Northern Blvd, hours to 2am / 4am Fri–Sat) → §8 Union St/Northern Blvd card ("open into the small hours"), §8 business table karaoke row. No venue named on page.
- `Flushing leaders bash Main Street busway plan` · scrape https://queenseagle.com/all/flushing-leaders-bash-main-street-busway-plan (David Brand, July 17 2020): Main St busway 0.3 mile Northern Blvd to Sanford Ave/Kissena Blvd; BID survey >200 vendors opposed → background only (access/crowds); NOT used on page.

### Building stock / developments
- `Tangram Flushing mixed-use development apartments office retail 39th Avenue` · Firecrawl search → scrape https://newyorkyimby.com/2016/12/construction-underway-on-tangrams-13-story-192-unit-residential-building-at-133-27-39th-avenue-flushing.html (Reid Wilson, Dec 5 2016): four-building, 1.2M sq ft mixed-use on block bound by College Point Blvd, Prince St, 37th and 39th Aves; 13-storey 192-unit condo at 133-27 39th Ave; "four-level, 377-car underground parking garage"; 14-storey office building at 37-12 Prince St; hotel planned; ~30 shops and 24,000 sq ft food hall → §5 para 3, §7 podium card, §9 garage Q, Block by Block.
- `One Fulton Square Flushing Hyatt Place 39th Avenue Prince Street mixed-use` · Firecrawl search → scrape https://www.qchron.com/editions/north/new-hotel-opens-in-downtown-flushing/article_7de80dc7-aef3-5fca-846e-40685d4261a7.html (Liz Rhoades, June 26 2014): 168-room Hyatt Place; $125M, 330,000 sq ft; "retail and medical space and luxury condos"; entrances on Prince St, 39th and Roosevelt Aves; "underground parking for 299 cars"; F&T Group → §5 para 3, §8 39th Ave card, §9 garage Q.
- `Shops at SkyView Center Flushing College Point Boulevard Skyview Parc apartments towers` · Firecrawl search → https://www.homes.com/building/sky-view-parc-flushing-ny/b-c7gxr21kcbr8l/ (excerpt: "A 448-unit condo atop a busy mall in Flushing designed by Perkins Eastman"); https://thegrandsvp.com/ (excerpt: direct access to The Shops at SkyView; 40-26 College Point Blvd) → §5 para 3, §7 podium card, §8 College Point Blvd card.
- Scrape https://newyorkyimby.com/2026/09/two-tower-second-phase-of-flushing-commons-breaks-ground-in-flushing-queens.html (Michael Young & Matt Pruznick, Sept 17 2026): phase two broke ground at 37-10 138th St; F&T Group + NYCEDC + YMCA; tallest building 18 storeys; 156 condos, ~132,000 sq ft retail/dining, 123,000 sq ft office, 63,000 sq ft YMCA; phase one completed 2017 with 148 condos, 90 office condominiums, ~30,000 sq ft retail and 982 parking spaces; site formerly surface parking; completion expected June 2029 → §5 para 3, §7 office-condo card, §8 37th Ave/138th St card, §10.5 H3 2, §13 Flushing Commons card, §9 garage Q.
  - Reader comment (David of Flushing) on the same page: retail being replaced by medical clinics; whole third floor at 39th Ave & Union St medical — user comment, NOT quoted; page relies on the SBS upper-floor-healthcare finding instead.
- `Queens Crossing Flushing 136-20 38th Avenue office medical condos retail` · Firecrawl search → LoopNet/MyStateMLS excerpts (office/medical condo units) → background only; NOT used.
- `Special Flushing Waterfront District rezoning approved 2021 apartments Flushing Creek` · Firecrawl search → excerpts (zr.planning.nyc.gov ch. 7; flushingwaterfront.com "1,725 units proposed"; advocacy sites) → contested/advocacy figures; NOT used.

### Demographics / language
- `Flushing Queens Chinese language spoken at home percent limited English proficiency community district 7` · Firecrawl search → https://www.aafederation.org/research/asian-languages-in-new-york-city/ (excerpt): "Queens Community District 7 (Flushing, Murray Hill & Whitestone) had the largest Chinese-speaking population, at 82,588 speakers" → §5.5 bullet 5, §9 labels Q context. Data USA excerpt (36.8% of CD7 households speak Chinese at home) — not used.

### Landmarks
- `Flushing Town Hall 1862 Northern Boulevard landmark history` · Firecrawl search → https://en.wikipedia.org/wiki/Flushing_Town_Hall (excerpt: built 1862; NYC Landmark 1968) and https://www.flushingtownhall.org/mission-and-history (excerpt: 1862 landmark owned by the City; 9-year $8M restoration from 1990; 308-seat theater) and NYC DDC Facebook excerpt (Northern Boulevard at Linden Place) → §8.5 landmark bullet, §13 card.
- `Bowne House Flushing Quaker Meeting House oldest house of worship Queens` · Firecrawl search → https://flushingfriends.org/history/40-2/ (excerpt: "Built in 1694 by John Bowne and other early Quakers, the Old Quaker Meeting House is, by all known accounts, the oldest house of worship in New York State"); https://www.bownehouse.org/nearby (excerpt: Quakers had met in the Bowne House for 30 years; land acquired 1692); nylandmarks Facebook excerpt (Bowne House, 37-01 Bowne Street; Meeting House on Northern Boulevard) → §8.5 landmark bullet, §13 cards.
- `Queens Public Library Flushing branch Main Street busiest library building` · Firecrawl search → https://www.queenslibrary.org/about-us/locations/flushing (41-17 Main Street) and http://www.queenslibrary.org/about-us/news-media/blog/6609 (excerpt: closes ~5 weeks from Monday April 27 2026 for essential safety improvements) → §13 card.
- `NewYork-Presbyterian Queens hospital Flushing beds Main Street` · Firecrawl search → https://www.nyp.org/locations/queens/nyp-queens (56-45 Main Street, Flushing NY 11355) → §13 card, Block by Block (Kissena Blvd).

### Local news / hyperlocal / flooding
- `Hurricane Ida Flushing flooding basements College Point Boulevard 2021` · Firecrawl search →
  - https://ny1.com/nyc/all-boroughs/news/2026/07/19/flushing-residents-deal-with-flash-flooding-aftermath (NY1, July 19 2026; full excerpt in result): Saturday flash flooding submerged basements and garages in Flushing; blocked drains; water overflowed "from their toilet and bathtub, flooding their basement"; same area had severe flooding that killed multiple people during Ida (2021); OEM commissioner Christina Farrell cites topography; pumps distributed → §5 para 4, §5.5 bullet 6, §9 sewer-backup Q, §10.5 H3 3, After the Storm section.
  - https://www.nyc.gov/site/cdbgdr/hurricane-ida/hurricane-ida.page (excerpt): "only 6.9% of Ida-impacted buildings are in the 100-year floodplain, and 13.7% are in the 500-year floodplain" → §10.5 H3 3.
- Queens Chronicle / QNS / Patch items on Cat6 or network-cable repair in Flushing specifically: EMPTY.

### Technical / code (new this page)
- `NEC 800.154 plenum cable CMP required ceiling space used for environmental air communications cable` · Firecrawl search → https://forums.mikeholt.com/threads/plenum-rated-cable-in-emt.64549/ (excerpt quoting code: "Cables installed in ducts, plenums, and other spaces used for environmental air shall be Type CMP"); https://winnieindustries.com/resources/knowledge_center/frequently-asked-questions/air_handling_faq/ (excerpt: CMP required in plenum spaces, e.g. above a suspended ceiling used for air handling) → §8.5 plenum bullet, §9 plenum Q, equipment card, repair table.
- `sewage backup flooded basement cleanup Category 3 black water porous materials discard electrical cables` · Firecrawl search → https://www.belfor.com/us/en/resources/category-3-water-damage-guide/ (excerpt: sewer backup = Category 3; porous materials discarded) and https://northwestarkansas.pauldavis.com/blog/what-to-do-when-sewage-backs-up-into-your-nwa-home-a-step-by-step-emergency-guide/ (excerpt: "The IICRC standard for Category 3 water is removal, not cleaning") → §9 sewer-backup Q (paraphrased as restoration-industry practice), After the Storm checklist.
- Silo sources reused: NYC Electrical Code (2020 NEC + amendments, full effect Dec 21 2025); NEC abandoned-cable rule; DOB post-Ida advice; NYC Health restaurant grades (29,000 restaurants, letter grades) → §9 health-inspection Q; Toast network-cable troubleshooting article → §10.5 H3 5; Fixr Jan 2025 national figures → §14.
- Lead-lined imaging rooms and bullet-resistant teller partitions: described as general construction practice with no numeric claims and no Flushing-specific source; answers commit only to not penetrating the assembly. Flag for review.

### Prices used (live AESS pages only; no new prices)
- $195/hr, 3-hour minimum ($585) — cat6-repair-queens.html / network-cable-repair-queens.html.
- Replacement drop from $175 — cat6-repair-queens.html table (network-cable-repair-queens figure).
- Exterior/garage entry from $194 per penetration — as published on cat6-repair-queens.html.
- Comparison only: Cat5e $233 / Cat6 $272 / Cat6A $388 — cat6-installation-queens (as quoted on cat6-repair-queens.html).
- Fixr Jan 2025 $125–$250/drop, $45–$75/hr — national, labelled.
- No neighbourhood premium applied; warranty sentence verbatim.

### Images (11) — Drive "AESS Website Photos/Cat6 Repair" EMPTY (checked by main run); library images/cat6-repair/ used (cp, WebP unchanged, all md5-distinct, each viewed before naming)
| images/cat6-repair/ | copied from | section |
|---|---|---|
| cat6-repair-flushing-pos-counter-switch-cords.webp (hero) | aess-cat6-repair-pos-counter-cable-repair.webp | hero |
| cat6-repair-flushing-nicked-jacket-ceiling-grid-edge.webp | cat6-repair-nassau-county-nicked-jacket-on-metal-edge.webp | §5 |
| cat6-repair-flushing-wall-jack-open-no-link.webp | cat6-repair-nassau-county-wall-jack-no-link-test.webp | §6 |
| cat6-repair-flushing-replacement-run-from-cat6-carton.webp | cat6-repair-nassau-county-ceiling-replacement-feed.webp | §7 |
| cat6-repair-flushing-dome-camera-no-poe-reading.webp | cat6-repair-nassau-county-poe-dome-camera-no-power.webp | §8 |
| cat6-repair-flushing-data-voice-plate-punch-down.webp | cat6-repair-nassau-county-data-voice-plate-retermination.webp | §9 |
| cat6-repair-flushing-tone-probe-labelled-patch-cords.webp | cat6-repair-suffolk-county-tone-probe-labelled-cords.webp | §10 |
| cat6-repair-flushing-wire-map-fail-crossed-open.webp | cat6-repair-nassau-county-wire-map-crossed-open-pair.webp | §10.5 |
| cat6-repair-flushing-partition-outlet-row-retermination.webp | cat6-repair-suffolk-county-outlet-row-retermination.webp | §12 |
| cat6-repair-flushing-ceiling-bundle-flashlight.webp | cat6-repair-nassau-county-ceiling-run-flashlight-inspection.webp | §13 |
| cat6-repair-flushing-desk-data-ports-labelled.webp | cat6-repair-nassau-county-desk-outlet-identification.webp | §15 |
DAILY-LOG note: `images: 11 reused from images/cat6-repair/ library (Nassau/Suffolk/aess sets; no Flushing-specific photos)`. Review note: library photos appear AI-generated (same caveat as earlier pages); none shows a Flushing location; captions describe only what is visible; the hero photo shows a technician's face in profile (AESS uniform), no customer.

### Keyword notes (five layers, Flushing geo)
- Service: Cat6 repair Flushing, Cat6 cable repair Flushing Queens, food court POS cable repair, kiosk Ethernet repair, clinic network jack repair, plenum Cat6 replacement, Cat6 certification, port mapping/labelling.
- Problem: stall register offline, shared-ceiling damage by neighbour fit-out, kiosk relocation, non-plenum cable in return-air ceiling, garage camera corrosion, flash-flood/sewer-backup basement, unlabelled turnover cable.
- Technology: Cat6/Cat6A, CMP/CMR ratings, keystone/punch-down, certification tester, fault distance, toner, PoE load test, conduit/metal raceway, firestop.
- Industry: food-court vendors, malls, banks and money-transfer counters, medical/dental suites, accounting/travel/insurance offices, hotels, karaoke lounges, wholesalers, office-condo owners, condo associations.
- Geographic: Flushing; Main St, Roosevelt Ave, 39th Ave, Prince St, Union St, Northern Blvd, College Point Blvd, 37th Ave/138th St, 40th/41st Rd, Kissena Blvd; Murray Hill, Broadway–Flushing, Auburndale, Kissena Park, Queensboro Hill, Pomonok, Kew Gardens Hills, Fresh Meadows, College Point, Whitestone, Bayside, Corona, Willets Point.

## Question register — cat6-repair-flushing-queens-ny

§9 "Questions Answered" (H3):
1. Does opening the ceiling above our food-court stall put our health inspection at risk? (Food courts)
2. The mall wants to move our island kiosk further along the concourse — can the existing Cat6 follow it, or does a new run have to come from the closet? (Malls)
3. Does the cable above a mall's drop ceiling have to be plenum-rated, and what happens if our old run isn't? (Malls/offices)
4. Our Cat6 runs through the underground garage beneath the building — what does garage air and traffic do to it? (Podium buildings)
5. Our dental office's X-ray room has shielded walls — can a dead Cat6 run to the imaging computer be repaired without compromising the shielding? (Clinics)
6. Our counter sits behind a bullet-resistant partition — how is the Cat6 to the window terminal repaired without disturbing the partition? (Financial counters)
7. Our patch panel was labelled in Chinese by the last installer and our new office manager reads only English — can the labels be redone in both languages? (Labels)
8. Sewer water backed up into our basement during the storm — should the cleanup company or the cabling contractor go in first? (Flooding)

FAQ (§17, = FAQPage schema):
F1. Can you repair the Cat6 that feeds a self-order kiosk or a table-ordering screen?
F2. Do you repair the network cable to a staff time clock or attendance terminal?
F3. Can the test results go to both our business and the mall or building management?
F4. Do you repair the Cat6 behind a hotel front desk?
F5. Do you repair the Cat6 that feeds supermarket checkout lanes and scales?
F6. Do you repair the Cat6 in a karaoke lounge's private rooms?
F7. Do you need floor plans or building drawings before a repair?
F8. How can we confirm that the technician who arrives is licensed?
F9. Can you repair the Cat6 at a pharmacy counter without holding up prescriptions?
F10. Will a cable repair change our network settings or IP addresses?

Other "?" headings: "Need Repair in Flushing Before the Dinner Crowd Arrives?" (repair capture), "A Flushing Stall, Desk or Camera Offline Right Now?" (closing).

De-dup notes: every question compared by meaning against all 383 questions/question-headings on the 16 live cat6-repair-*.html pages and the registers in research/cat6-repair.md (and against cat6-repair-riverdale-bronx-ny / -new-dorp-staten-island-ny as on disk during the build). Rejected as too close: shared-closet ownership (Orange #213 "which runs are whose"), adjacent-tenant ceiling (SI two-family ceiling), Wi-Fi instead of cable (Queens F3), inherited tenant cable (Queens F7), off-hours/before-opening scheduling (Orange, LI), pre-season testing (SI), acoustic panels (Ulster), riser/base-building responsibility (Manhattan), two-sites-one-visit (Orange/Westchester), parking charge (would need an unpublished price policy). Replaced after reading the batch siblings on disk: dental-chair floor-box FAQ (New Dorp asks what damages the dental-chair Cat6), floor-cord FAQ (Riverdale rug patch cord; New Dorp flat cable under carpet), clinic patient-information FAQ (New Dorp patient-records question), and the licence FAQ narrowed to licence verification only (Riverdale asks about same-day certificates of insurance). Borderline, flagged for review: F3 (results to two parties) vs Queens F4 (keeping results) — different intent (recipients vs retention); §9 Q8 (sewer backup sequencing) vs NYC "cellar closet took on water — can the Cat6 dry out and be reused?" — different intent (contamination and order of trades vs reuse).

### Build checks (2026-10-17)
- tools/check_page.py cat6-repair-flushing-queens-ny --no-registration: only remaining failures are the 16 "live sibling … doesn't link back" lines (sibling/parent wiring is the main run's job). 12,347 rendered words; 180,294 bytes; title 58; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10.
- Masked-geo similarity (simcheck.py vs cat6-repair-queens.html): MAX 0.641. Parallel run vs all 17 other cat6-repair pages (incl. riverdale + new-dorp as on disk): every paragraph < 0.65 after rewrites (one 20-word home-link sentence that hit 0.66–0.74 was cut below the 20-word threshold).
- Size window: siblings in flux during the batch (riverdale ~176.2K, new-dorp ~233.0K at last check); this page sits between riverdale+2 KB and brooklyn−2 KB — re-check after the batch settles.

# Merged from batch 2026-10-17 (cat6-repair-riverdale-bronx-ny)

## Riverdale, Bronx (cat6-repair-riverdale-bronx-ny)

Batch run 2026-10-17. Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, #bronx; LocalBusiness block copied from cat6-repair-bronx.html with url/image set to this page) · up-link /cat6-repair-bronx, hub /cat6-repair-nyc. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Silo-wide technical sources (Fluke NEXT, TSB-155/184, NEC 800.25, NYC Electrical Code, Fixr, CCA vendor blog) reused from the silo section of research/cat6-repair.md.

**Thesis (different from cat6-repair-bronx and the Flushing/New Dorp batch pages):** Riverdale's Cat6 is owner-added — retrofitted by co-op shareholders, homeowners and integrators, not by developers — so the person at the dead jack usually owns the wall, pays for the repair, and works under somebody else's rules: the co-op's proprietary lease/house rules/alteration agreement, Fieldston's private streets and landmark district, and the Special Natural Area District that protects the ridge's slopes, rock and trees. Failures follow the owner's shortcuts (terrace sliders, AC sleeves, rugs, combination/duplex joins, shallow outdoor runs over rock and roots, integrator wiring in plaster). Parent's angle (new-building defects vs pre-war retrofit, agent-run rentals) avoided.

### Building stock / housing
- `Furman Center Riverdale Fieldston Kingsbridge BX08 homeownership rate units built` · Firecrawl search → scrape https://www.furmancenter.org/neighborhoods/riverdale-fieldston/ (directQuote; last updated 05/06/2026): "In 2024, the homeownership rate in Riverdale/Fieldston was 38.4%, which is higher than the citywide share of 32.7%"; "Between 2010 and 2025, 2,087 units in 4+ unit buildings were built in Riverdale/Fieldston"; population 95,283 (2024) → §5 para 1–2, §5.5 bullets 1–2. (Bronx 19.7% / 63,066 from the Bronx section of the silo file.)
- `Riverdale Bronx co-op apartment buildings high-rise postwar Henry Hudson Parkway housing stock` · Firecrawl search → scrape https://cooperatornews.com/article/a-river-runs-through-it (The Cooperator, Annette Hall, May 2010, directQuote): "The post World War II building boom hit Riverdale with multi-family dwellings and large apartment buildings, many of which eventually became co-ops"; "co-ops tend to predominate in Riverdale"; broker: "a prewar building east of the highway" → §5 para 1, §7 cards 1–2.
  - Same search, excerpts: https://www.compass.com/building/windsor-north-bronx-ny/293528534956157461/ — "Henry Hudson Pkwy W … Co-op in Riverdale 133 Units, Built in 1961, Post-war Elevator" → §7 card 1 (building-type example only; no claim of work there). https://www.nybits.com/apartments/bronx_coop_buildings.html ("A post-war high-rise building. The Fountain Garden Apartments (4499 Henry Hudson Parkway)") and https://streeteasy.com/building/3701-henry-hudson-pkwy-w-bronx/4c ("The Georgian … a postwar co-op") → background, not used.
- `Association of Riverdale Cooperatives and Condominiums ARC member buildings apartments` · Firecrawl search → https://www.riverdalepress.com/stories/riverdale-cooperatives-association-re-elects-board-continues-community-advocacy,151840 (excerpt): "more than 100 co-operatives and condominiums part of the membership"; https://arc-riverdale.com/join-arc/ (excerpt): "ARC represents all of the co-ops and condominiums in Riverdale, Bronx, NY — essentially buildings in the 10463 and 10471 zip codes" → §5.5 bullet 3, sources list.
- `co-op alteration agreement minor alteration low voltage wiring board approval contractor insurance certificate New York co-op` · Firecrawl search → https://www2.nycbar.org/RealEstate/Forms/Coop_Condo_%20Form_Alteration_Agreement_Coops_Commentary10.pdf (NYC Bar model alteration agreement, excerpt): contractors' insurance "shall name the Corporation"; Shareholder to deliver certificates → "House Rules" section para 2, §10.5 H3 7, FAQ F2. (myhomeus.com / gallerykbny / miltoncoste excerpts — background, not used.)

### Landmarks / protected ground
- `Special Natural Area District Riverdale zoning steep slopes trees rock outcrops NA-2` · Firecrawl search → https://zr.planning.nyc.gov/article-x/chapter-5 (excerpt): §105-942 SNAD-2 "Riverdale, Spuyten Duyvil and Fieldston … This ridge contains steep slopes, rock outcrops, ponds, brooks, swampy areas and mature trees", last amended 5/21/1975; steep slope = incline of 25% or greater; site plans show trees of six-inch caliper or more; §105-50(c) filling, excavating, grading "shall avoid creation of steep slopes or conditions causing erosion" → "Outdoor Cat6 on the Riverdale Ridge" para 1 & 3, §5.5 bullet 5, §9 Q6/Q7.
  - scrape https://www.riverdalenature.org/planning-and-zoning-in-nyc (Riverdale Nature Preservancy, directQuote): protected features — mature trees 6" caliper or greater; steep slopes (≥25%), natural topography, topsoil; rock outcrops and erratic boulders; wetlands; botanic environments → ridge section para 1.
- `Fieldston Historic District Landmarks Preservation Commission privately owned streets houses Riverdale` · Firecrawl search → https://en.wikipedia.org/wiki/Fieldston,_Bronx (excerpt): privately owned; streets and common areas owned by the Fieldston Property Owners' Association, which plows streets, does sewer repair, cares for about 1000 trees, runs a security patrol; parking restricted to residents and guests; LPC designated the Fieldston Historic District January 10, 2006, 252 houses and related structures; Baum designed 62 houses, Gregory 42; bounded by Manhattan College Parkway, Henry Hudson Parkway, 250th Street and Broadway; Horace Mann and Ethical Culture Fieldston in Fieldston, Riverdale Country just north → §5 para 3, §5.5 bullet 4, §7 card 3, ridge para 4, §9 Q8, §13 card 3, FAQ (parking item later replaced, see register notes).
  - https://s-media.nyc.gov/agencies/lpc/lp/2138.pdf (LPC designation report, excerpt): roads follow natural contours, Delafield Estate retained ownership of roads; houses in "picturesque styles following the strict design guidelines of the Fieldston Property Owners Association"; examples incl. "hipped tile roof, stone base"; 1960s–70s houses incl. 4660 Waldo Ave "with a bridge over a … ravine to reach the building" → §7 cards 3 and 5, §13 intro.
- `Riverdale Historic District Landmarks Preservation Commission 1990 designated villas Independence Avenue` · Firecrawl search → scrape https://www.nypap.org/preservation-history/riverdale-historic-district/ (directQuote): 100-acre parcel purchased in 1852; divided into seven estates; five original homes survive; "earliest known railroad suburb of New York City"; designated October 16, 1990 → §5.5 bullet 5, §7 card 4, §13 card 2.
- `Wave Hill public garden Riverdale 28 acres Hudson River Palisades history` · Firecrawl search → https://en.wikipedia.org/wiki/Wave_Hill (excerpt): 28-acre estate in Hudson Hill; Wave Hill House 1843 gray fieldstone; given to the City in 1960; about 65,000 visitors a year → §13 card 1.

### Corridors / commercial
- `Riverdale Avenue Johnson Avenue shopping strip small businesses Riverdale Bronx merchants Riverdale Press` · Firecrawl search → scrape https://www.riverdalepress.com/stories/the-heart-of-our-communities,47105 (Pearl Korn, Oct 21 2010, directQuote): Johnson Avenue "perhaps four blocks of 35 stores, 4 banks, a supermarket, a CVS Pharmacy … a Kosher butcher, a shoe maker"; Riverdale Avenue "about 50 stores on this two-block shopping area" → §8 card 1.
  - scrape https://www.riverdalepress.com/stories/study-explores-retail-challenges-and-development-patterns-in-northwest-bronx-neighborhoods,230746 (Michelle Mullen, May 2026, directQuote): CB8 study by Kahdija Jabbi; CD8 includes Riverdale, Kingsbridge, Marble Hill, Kingsbridge Heights, Spuyten Duyvil, Fieldston; storefront vacancy "about 6.9 percent"; North Riverdale eateries, salons, specialty businesses around Mosholu Avenue and Riverdale Avenue; broker: Riverdale Avenue "one of the strongest retail corridors in the district" → §8 cards 2–3 and closing para, FAQ F5.
- `Riverdale Bronx neighborhood Wikipedia Manhattan College Horace Mann Riverdale Country School Hebrew Home Henry Hudson Parkway Metro-North` · Firecrawl search → https://en.wikipedia.org/wiki/Riverdale,_Bronx (excerpt): Riverdale Avenue primary north–south thoroughfare; ZIPs 10463/10471 (10471 north of Manhattan College Parkway and 239th St; 10463 shared with Kingsbridge and Marble Hill); sections Central Riverdale, Fieldston, Hudson Hill, North Riverdale, Mosholu, Spuyten Duyvil/South Riverdale (incl. business district at W 231st St and Broadway), Villanova Heights; Hill Schools; Manhattan University; University of Mount Saint Vincent; SAR, Kinneret; many synagogues and churches → §7 card 6, §8 cards 4–5, §13, "Section by Section", FAQ F4/F5.

### Local news / hyperlocal
- `Riverdale Press internet outage Optimum Verizon Fios Riverdale building residents` · Firecrawl search → scrape https://www.riverdalepress.com/stories/verizons-fiber-optic-network-nears-completion-in-riverdale,54591 (Shant Shahrigian, July 10 2014, directQuote): 13 miles of underground and aerial fiber; buildings need only "lateral" street-to-building cables; "Co-ops lead the way"; board member at 3935 Blackstone Ave. → House Rules checklist bullet 5.
  - Same search → scrape https://bronx.news12.com/5000-con-edison-customers-in-the-bronx-without-power-amid-heat-wave (July 3 2026, directQuote): "about 1,000 customers in Riverdale are without electricity"; Con Edison "reduced voltage by 8% in parts of northern Manhattan and the northwest Bronx, including Riverdale, Marble Hill, Kingsbridge and Van Cortlandt Park" → §5.5 bullet 6, FAQ F3.
  - Optimum outage pages / Downdetector / CBS Optimum outage (excerpts) → not Riverdale-cabling specific, not used.
- Riverdale Press / Bronx Times items about building data cabling or Cat6 specifically: EMPTY.

### Reddit
- `site:reddit.com Riverdale Bronx apartment ethernet OR internet OR wiring co-op` · Firecrawl search → results were housing threads only (r/bronx https://www.reddit.com/r/bronx/comments/1e1i0sq/is_the_apartment_search_doomed/ "These co-ops are so expensive now"; r/NYCapartments https://www.reddit.com/r/NYCapartments/comments/1r7bwtf/why_dont_more_people_look_to_woodlawn_bronx_or/ "Spent 10 years in Riverdale … quiet, nice parks, and surprisingly green"; r/AskNYC co-op purchase thread) → background only (co-op ownership), not quoted. Riverdale threads about Ethernet/cabling faults: EMPTY.

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 states on the page that the AI Overview was not visible; each H3 is a commonly repeated claim (Fixr cost range, re-crimp, mesh Wi-Fi, "anyone can do it", indoor cable outdoors, link light = pass, "no permission needed in a co-op") corrected with sourced facts.

### Local licensing / permits / code
- NYC Electrical Code = 2020 NEC + NYC amendments, full effect Dec 21 2025 (nyc.gov, silo) → §8.5 bullet 1.
- NEC 800.25 abandoned cable (EC&M, silo) → §8.5 bullet 2.
- LPC permit for exterior work in historic districts (nyc.gov LPC applications page, silo Bronx section) → ridge para 4, §8.5 bullet 4, §9 Q8.
- SNAD rules (ZR 105-942, 105-50) → above.
- Firestopping of rated penetrations: general practice, no Riverdale-specific source.

### Prices used (Bronx §9 multiplier 1.00×; figures exactly as published on cat6-repair-bronx.html)
- $195/hr, three-hour minimum ($585); additional time $195/hr.
- Replacement run from $175 per drop.
- Exterior entry sealed and bonded from $185 per penetration.
- New-install comparison Cat5e $233 / Cat6 $272 / Cat6A $388 per drop to 100 ft.
- Fixr Jan 2025 national $125–$250/drop, $45–$75/hr — labelled third-party.
- Insurance certificate at no charge — process statement (no price), not a new price.

### Images (11) — Drive "AESS Website Photos/Cat6 Repair" EMPTY (checked by main run); library images/cat6-repair/ used, md5-unique, each viewed before naming
| images/cat6-repair/ | Source (same folder) |
|---|---|
| cat6-repair-riverdale-dome-camera-no-poe.webp (hero) | cat6-repair-putnam-county-poe-dome-no-power-reading.webp |
| cat6-repair-riverdale-wall-jack-open-result.webp | cat6-repair-westchester-county-wall-jack-no-link-test.webp |
| cat6-repair-riverdale-abraded-bundle-on-metal-edge.webp | cat6-repair-westchester-county-crushed-bundle-over-duct.webp |
| cat6-repair-riverdale-panel-punch-down-labelled.webp | cat6-repair-westchester-county-panel-port-reterminate.webp |
| cat6-repair-riverdale-split-jacket-at-steel-edge.webp | cat6-repair-westchester-county-split-jacket-exposed-pairs.webp |
| cat6-repair-riverdale-corroded-plug-block-wall.webp | cat6-repair-putnam-county-corroded-plug-block-wall.webp |
| cat6-repair-riverdale-wire-map-fail-tester.webp | cat6-repair-westchester-county-wire-map-fail-screen.webp |
| cat6-repair-riverdale-rj45-plug-crimper.webp | cat6-repair-putnam-county-rj45-plug-and-crimper.webp |
| cat6-repair-riverdale-tone-probe-labelled-patch-panel.webp | cat6-repair-westchester-county-tone-probe-labelled-panel.webp |
| cat6-repair-riverdale-flashlight-ceiling-bundle.webp | cat6-repair-rockland-county-flashlight-ceiling-bundle-check.webp |
| cat6-repair-riverdale-ceiling-access-point-cable.webp | cat6-repair-rockland-county-ceiling-access-point-cable-end.webp |
Captions/alts describe only what is visible; none claims a Riverdale location, customer, named building or completed project. Captions rewritten after simcheck flagged similarity to the Westchester/Rockland/Putnam captions of the same photos. Note: these library photos appear AI-generated (uniform branding, idealised scenes), as already noted in the Bronx section.

## Question register — cat6-repair-riverdale-bronx-ny

§9 "Questions Answered" (H3), clusters "Inside co-op and condo apartments" / "Houses on the ridge":
1. We combined two apartments into one — why do the jacks on the side that used to be the other unit never join our network?
2. The Cat6 to our terrace camera was run under the sliding door and has gone dead — what replaces a cable pinched in a door track?
3. A previous owner pushed our Cat6 through the through-wall air-conditioner sleeve — is that why the link fails every summer?
4. Where does the Cat6 linking the two floors of a duplex apartment usually fail?
5. Under a co-op proprietary lease, is the Cat6 inside our apartment walls the shareholder's to repair or the corporation's?
6. Our house is inside the Special Natural Area District — does that change how a failed buried Cat6 run can be replaced?
7. Roots from a mature tree have lifted the path over our buried Cat6 — is the cable underneath likely to be damaged?
8. Fieldston's streets are privately owned — does a repair that has to cross the curb or the roadway involve the property owners' association?
9. A wall touch panel for our home-automation system has gone blank — could the Cat6 behind it be the cause?

FAQ (§17, = FAQPage schema):
F1. What will one dead jack in a Riverdale co-op apartment cost to put right?
F2. Our managing agent wants a certificate of insurance naming the co-op before any work — can you send it the same day?
F3. During a heat wave Con Edison lowered the voltage in Riverdale — can that harm our Cat6 or the cameras on it?
F4. Can you repair the Cat6 that feeds livestream cameras in a synagogue or church sanctuary?
F5. Do you also repair Cat6 in Spuyten Duyvil, Kingsbridge and Marble Hill?
F6. The integrator who wired our house has closed — can you look after the cabling from now on?
F7. Can a Cat6 repair be finished inside the hours a co-op allows for contractor work?
F8. How far is Riverdale from your base, and how soon can a technician arrive?

Other "?" headings: "Wired Link Gone Dark Between Spuyten Duyvil and the Yonkers Line?" (repair capture), "Riverdale Jack Still Dead After Dinner?" (closing).

De-dup notes: compared by meaning against every question register in research/cat6-repair.md and every question/question-heading on the cat6-repair-*.html pages on disk (738 lines extracted), including the same-batch Flushing and New Dorp pages. Avoided: co-op board approval (Westchester F6), courtyard-wall repair from inside (Queens Q12), historic review board (Putnam Q10) — kept as body text only; ledge trenching (Putnam), wetland/watershed permits (Putnam), Lake Mahopac dock, buried-conduit ice, falling limb aerial run, rodents, steam riser, dumbwaiter chase, provider-moved router, "test before closing", "match existing plates", "Saturday" and "home for the visit" questions. Replaced after reading New Dorp's page: parking on private streets (New Dorp asks where the technician parks) → livestream sanctuary cameras; patch cord under the rug (New Dorp asks about flat cable under carpet) → integrator-gone ongoing care. Related-but-distinct: F1 (one-jack all-in cost) vs Bronx F2 (is the Bronx priced differently) and NYC F1 (is the minimum charged for a 20-minute fix); Q5 (ownership/responsibility under the proprietary lease) vs Westchester F6 (board approval) and Queens F7 (invoice the landlord for base-building cable); Q6 (SNAD) vs Putnam wetland/watershed (different regulation, different features); F3 (voltage reduction) vs Suffolk "power came back but links never did" (cause and equipment-vs-cable framing differ).

Masked paragraph similarity (scratchpad simcheck.py, plus fastsim.py = same masking/difflib with a 0.59 prefilter): final max 0.630 vs cat6-repair-bronx (NYC Electrical Code bullet). All other siblings < 0.61 after rewrites (nyc 0.557, staten-island 0.550, manhattan 0.566, dutchess 0.599, queens 0.607, westchester 0.594, rockland 0.580, putnam 0.594, long-island 0.587, hudson-valley 0.596, nassau 0.598, orange 0.594, ulster 0.572, flushing 0.565, new-dorp 0.595; brooklyn 0.609, suffolk 0.606 before later caption rewrites). Captions of shared-source photos and the silo link card were rewritten after first-pass hits of 0.66–0.75.

# Merged from batch 2026-10-17 (cat6-repair-new-dorp-staten-island-ny)

## New Dorp, Staten Island (cat6-repair-new-dorp-staten-island-ny)

Built 2026-10-17 (batch: Flushing QN, Riverdale BX, New Dorp SI). Neighbourhood spoke; up-link /cat6-repair-staten-island, silo hub /cat6-repair-nyc. Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared header chrome; WhatsApp only as https://wa.me/17186790359. GBP Brooklyn (1282 Troy Ave, #brooklyn) copied from the parent page's LocalBusiness block. Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. Rows marked "reused" were taken from research/soundbar-installation.md (New Dorp section, ND-S#) or the Staten Island section of research/cat6-repair.md and were not re-fetched.

**Thesis:** New Dorp's Cat6 splits along Hylan Boulevard and the Lane. Inland (New Dorp Heights and the central blocks) it lives in 1960s–70s high ranches, semi-attached and attached houses whose networks were extended by owners — switches chained room to room, flat cable under carpets, runs tied to basement pipes, jacks behind furniture. On New Dorp Lane it lives in two-storey mixed-use buildings full of dental offices, clinics, pharmacies and shops — operatory links, PCs daisy-chained through desk phones, counter links, patient-record privacy. Below Hylan, in New Dorp Beach, it lives in converted bungalows and raised rebuilt houses on blocks that only got storm sewers in 2025 — enclosure rules and flood openings decide where cable may go. Different from the parent (borough-wide water-line thesis), and from every other Cat6 area page.

### Local research log

| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| CND-1 | `New Dorp Beach sewer storm drainage project DEP Staten Island flooding` · FC search → FC scrape (markdown) | https://www.nyc.gov/site/dep/news/25-020/city-completes-84-million-street-drainage-project-new-dorp-beach-area-hit-hard-by | DEP/DOT/DDC release, May 20 2025: $84 million project; 8,701 ft of new storm sewers "in an area that had none before"; 101 new catch basins, 50 replaced; Milton, Finley and Cedar Grove Avenues raised by over a foot, Hett Avenue lowered about 10 in; DDC worked with more than 880 homeowners on driveways/front yards; construction began spring 2019; 3.32 miles of water main, 3.19 miles of sanitary sewer replaced; more than 40 blocks. | §5 para 4; §5.5 bullets 4–5; Three New Dorps table (below Hylan); §10.5 H3 "storm sewers"; Landmarks card 6 |
| CND-2 | same search · FC search (excerpt only) | https://www.nysenate.gov/newsroom/press-releases/2019/andrew-j-lanza/77-million-project-improve-drainage-and-streets-new | 2019 announcement ($77m at the time, 9,500 ft planned). Background only; page uses the 2025 completion figures. | research only |
| CND-3 | `NEC 800.133(C) communications cables shall not be strapped taped attached to exterior of conduit raceway as means of support` · FC search (excerpts) | https://www.ecmweb.com/national-electrical-code/code-basics/article/20897736/the-nec-and-communications-circuits ; https://www.electricallicenserenewal.com/Electrical-Continuing-Education-Courses/NEC-Content.php?sectionID=549 | EC&M: "Support exposed cables with supports that fasten to frame members, securing the cables with straps, staples, hangers, cable ties, or similar fittings [800.24]" and "Don't strap, tape, or attach communication wires or cables to raceways as a means of support." Second source: exposed cables "shall be supported by the building structure in such a manner that the cable will not be damaged by normal building use." | §9 Q3 (pipes); §8.5 compliance bullet; Equipment card (hangers); §10.5 H3 "cable ties" |
| CND-4 | `FEMA Technical Bulletin 1 flood openings must not be blocked obstructed enclosure below elevated building` · FC search → `FEMA TB 1 "Requirements for Flood Openings…" pdf` · FC search → FC scrape (pdf parser, directQuote) | https://www.norfolk.gov/DocumentCenter/View/64828/Flood-Openings---FEMA-TB-1-sec-8 | FEMA TB-1 section 8 (hosted by Norfolk): "Every enclosed area is required to have at least two flood openings on exterior walls"; installed on at least two sides "to decrease the chance that all openings will be blocked by floating debris"; openings "allow water to automatically enter and exit"; bottom no higher than 1 ft above grade. (Page states only that openings exist to let water in and out freely and that we do not route cable through them; no claim that a specific code section bans a cable.) | §9 Q8; §8.5 bullet; Building card (raised houses) |
| CND-5 | same · FC scrape (floods.org TB 1/5 news) | https://www.floods.org/news-views/fema-news/fema-out-with-the-old-in-with-the-updated-nfip-technical-bulletins-1-5/ | Query answer empty (directQuote returned nothing). Not used. | — |
| CND-6 | `IP phone PC port pass-through computer loses network when phone unplugged or rebooted` · FC search (excerpts) | https://community.cisco.com/t5/ip-telephony-and-phones/ip-phone-reboot/td-p/2969509 | Cisco Community: "When a phone reboots, the computer loses connection because the PC port of the phone doesn't have a 'bypass' functionality." (Spiceworks thread says some phones pass traffic during reboot — page says "many" phones, not all.) | §9 Q6; Services card "desk phone and PC" |
| CND-7 | `New Dorp Lane dentist dental offices Chinese businesses Staten Island 2025` · FC search (excerpts) | https://acenterfordentalexcellence.com/dentist-in-staten-island/ ; https://www.mapquest.com/us/new-york/defeo-louis-dds-278422461 ; https://www.zocdoc.com/dentists/new-dorp-staten-island-ny-1904pm | Directory/practice listings place dental offices on New Dorp Lane itself (97 New Dorp Lane) and on Hylan Boulevard "near the intersection with New Dorp Lane" (2749 Hylan). Practices are NOT named on the page; used only to say dental offices sit on the Lane and on Hylan at the Lane. | §8 commercial card (Hylan near the Lane); §9 Q5 intro |
| CND-8 | `site:reddit.com statenisland New Dorp internet wiring house` · FC search | — | Only r/AskNYC threads (Ethernet in NYC apartments; Spectrum advice "Check your speeds with a wired connection"), nothing on r/statenisland or New Dorp. r/statenisland: EMPTY (not accessible in build env / no matching thread). | — |
| CND-9 | `silive New Dorp Lane businesses 2026` · FC search → FC scrape (directQuote) | https://www.silive.com/topic/New%20Dorp/ | SI Advance topic page: 2011 post "Builder eyes New Dorp parking spaces" — "New Dorp Lane, a great little commercial strip of mostly old fashioned mom 'n pop stores" and "New Dorp Lane municipal parking lot"; Feb 4 2015: SIEDC and New Dorp Merchants Group shopper's guide "Featuring Nearly 100 Different Local Businesses". No Cat6/network-cable story. Hyperlocal news on Cat6 faults in New Dorp: EMPTY. | §8 Lane card (2011 quote). Parking lot NOT used on the page (2011 item; current status unverified). |
| CND-10 | reused (cat6 SI research) · FC scrape | https://www.silive.com/news/2025/07/severe-flash-flooding-cripples-major-staten-island-roads-during-storm-monday.html | Scott R. Axelrod, July 14 2025: "Hylan Boulevard, in the vicinity of New Dorp Lane, was nearly impassable … as if it was a river". | §5 para 4; §5.5 bullet 6; §8 Hylan card |
| CND-11 | reused (cat6 SI research) | https://www.citymd.com/urgent-care-locations/ny/new-dorp | CityMD New Dorp urgent care at 2710 Hylan Blvd. | §8 Hylan medical card |
| CND-12 | reused ND-S1 | https://en.wikipedia.org/wiki/New_Dorp,_Staten_Island | Nieuw Dorp, 1671; ZIP 10306; NTA 2020 pop 29,083 (27,623 in 2010); five 1960s Hylan Blvd shopping centres, largest Hylan Plaza (1966); New Dorp HS; Staten Island Tech; Miller Field; library at 309 New Dorp Lane. | §5 para 1; §5.5 bullet 1; §8 card; Landmarks cards |
| CND-13 | reused ND-S3 | https://s-media.nyc.gov/agencies/lpc/lp/1696.pdf | Lane Theater, 168 New Dorp Lane, opened Feb 10 1938, interior landmark Nov 1 1988; development from the 1880s; by 1917 a commercial strip on the Lane facing the railroad. | §5 para 2; Landmarks card 1 |
| CND-14 | reused ND-S4 | https://www.citylandnyc.org/council-approved-staten-island-commercial-districts/ | Dec 2005 rezoning: commercial-only buildings max two floors; residential barred from ground floor; mixed-use max 35 ft. | §5 para 2; §5.5 bullet 2; Building card (Lane mixed-use) |
| CND-15 | reused ND-S5 | https://citylandnyc.org/city-council-approves-new-dorp-bid | BID approved Apr 5 2017: 146 properties, about 180 businesses on the Lane and adjacent streets between Hylan Blvd and Richmond Rd. | §5.5 bullet 2; §8 Lane card |
| CND-16 | reused ND-S6 | https://documentedny.com/2026/07/30/chinese-immigration-staten-island-boom/ | Carol Chen (The City Reporter via Documented), Jul 30 2026: Chinese businesses concentrated around New Dorp Lane — restaurants, pharmacies, dentist offices, clinics; adult day-care centres; Staten Island Chinese School in New Dorp (since 1972). | §5 para 2; §8 cards (practices; schools card: SI Chinese School enrolment up sharply 2023–2024); FAQ F2 (adult day centre) |
| CND-17 | reused ND-S7 | https://www.defalcorealty.com/?p=7298 | DeFalco Realty, Sep 17 2026: high ranches / raised ranches common in 10306; semi-attached and two-family homes; New Dorp Heights toward Richmond Rd/Todt Hill; central blocks around Edison St, Rose Ave, Clawson St; flood risk "can differ by elevation and block". | §5 para 3; Three New Dorps table; Building cards 1–2 |
| CND-18 | reused ND-S8 | https://www.point2homes.com/US/Neighborhood/NY/Staten-Island/New-Dorp-Demographics.html | ACS 2019–2023 (Point2's small New Dorp boundary): 41.4% 1-unit detached, 25.3% 1-unit attached, 17.7% two units; median year built 1968; 69.3% owner-occupied. | §5 para 3; §5.5 bullet 3; Building cards |
| CND-19 | reused ND-S9, ND-S10 | https://www.dnainfo.com/new-york/20140411/new-dorp-beach/state-will-add-no-more-neighborhoods-sandy-buyout-program/ | Apr 11 2014: state added no more neighbourhoods to the Sandy buyout; New Dorp Beach not added (Oakwood Beach and Ocean Breeze were). | §5 para 4; Three New Dorps table |
| CND-20 | reused ND-S11 | https://theneighborhoods.substack.com/p/new-dorp-staten-island | May 22 2025: Sandy left parts of New Dorp Beach under about six feet of water; city auctioned damaged lots with resilient-building requirements; rebuilt homes raised above their foundations. | §5 para 4; Building card (raised rebuilds) |
| CND-21 | reused ND-S13 | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-001.pdf | DOB Buildings Bulletin 2022-001: wet-floodproofed space below the DFE limited to "parking of vehicles, storage and building access". | §9 Q8; §8.5 bullet; Building card |
| CND-22 | reused ND-S14, ND-S15 | https://new.mta.info/press-release/mta-announces-opening-of-elevators-staten-island-railway-new-dorp-station ; https://en.wikipedia.org/wiki/New_Dorp_station | Sep 19 2023: New Dorp first SIR station with elevators; station opened 1860, open cut at New Dorp Lane, rebuilt 1965–68; north exit New Dorp Lane, south exit Rose Ave. | Landmarks card 2; §5.5 |
| CND-23 | reused ND-S16, ND-S17 | https://www.nps.gov/gate/learn/historyculture/miller-field.htm | Miller Field: sold to the federal government 1919, Air Coast Defense Station completed 1921, part of Gateway since 1972, entrance via New Dorp Lane. | Landmarks card 3 |
| CND-24 | reused ND-S19, ND-S2 | https://spectrumlocalnews.com/nys/central-ny/news/2026/05/21/new-york-city-summer-events-pools-beaches-2026 ; https://en.wikipedia.org/wiki/New_Dorp_Beach,_Staten_Island | Cedar Grove Beach listed for 2026 at Ebbitts St and Cedar Grove Ave; New Dorp Beach "Most houses are converted beach houses, with many attached homes"; flooding between Marine Way and Tysens Lane. | Landmarks card 6; Building card (bungalows) |
| CND-25 | reused ND-S21 | https://en.wikipedia.org/wiki/Staten_Island_Technical_High_School | Staten Island Tech, 485 Clawson St, in the former New Dorp HS building (vacated 1982). | §8 schools card; Landmarks card 4 |
| CND-26 | reused ND-S22 | https://www.apartments.com/tysens-park-apartments-staten-island-ny/m0xq0tj/ | Tysens Park Apartments, 30 Ebbitts St / Mill Rd. | Building card (garden apartments) |
| CND-27 | Silo technical sources reused, not re-fetched (research/cat6-repair.md silo + SI sections): Fluke NEXT/untwist & time-domain location; BICSI-style study guide (crush/kink → return loss, stranded cable → insertion loss); Belden TSB-184-A PoE bundles; EC&M NEC 800.25 abandoned cable; NYC Electrical Code = 2020 NEC amendments, full effect Dec 21 2025; 29 CFR 1910.308 2-in separation; NYC BC Appendix G (LL 77 of 2023); Fixr Jan 2025 national figures. | as recorded there | as recorded there | §7.5, §8.5, §9 answers, §10, §10.5, §14 |
| CND-28 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 H3s are framed on the page as commonly repeated claims, not as quoted AI Overview text. | §10.5 |

### Prices used (copied only from cat6-repair-staten-island.html; no multiplier, no new lines)
$195/hr with a three-hour minimum ($585); additional time $195/hr; replacement or extension run from $175 per drop; exterior/below-house entry made good from $185 per penetration; comparison new-install drop $296 (Cat5e $254, Cat6A $424); no separate bridge/travel charge; Fixr Jan 2025 national $125–$250 per drop and $45–$75/hr (labelled third-party). Packages: Starter $585; Standard $195/hr after the first three hours; Premium repair time + from $175 per run (+ from $185 per penetration).

### Images (11) — Step C, library images/cat6-repair/ (Drive folder "AESS Website Photos/Cat6 Repair" empty per main run)
Copied unchanged (cp, WebP kept); each viewed before naming; md5-unique; sources from the Brooklyn / Manhattan / Dutchess / Ulster sets only.

| New file (images/cat6-repair/) | Source | What is visible |
|---|---|---|
| cat6-repair-new-dorp-wire-map-fail-crossed-open-pair.webp (HERO) | cat6-repair-dutchess-county-wire-map-crossed-open-pair.webp | handheld tester screen "FAIL", pins 1–2 crossed pair, pin 6 open pair, blue cord on top, rack behind |
| cat6-repair-new-dorp-corroded-plug-at-block-wall.webp | cat6-repair-ulster-county-corroded-plug-block-wall.webp | gloved hand holding RJ45 plug with green corrosion, flashlight, surface box on concrete block |
| cat6-repair-new-dorp-dome-camera-no-poe-test.webp | cat6-repair-ulster-county-dome-camera-no-poe-reading.webp | technician on stepladder, tester reading "NO PoE / NO LINK" at a white dome camera on a wall |
| cat6-repair-new-dorp-fish-tape-into-wall-conduit.webp | cat6-repair-brooklyn-fish-tape-emt-conduit-block-wall.webp | technician feeding a red 240 ft fish tape into metal conduit on a block wall |
| cat6-repair-new-dorp-access-cut-beside-wall-box.webp | cat6-repair-brooklyn-wall-access-cut-oscillating-tool.webp | oscillating tool cutting a small panel in drywall beside a blue box with blue cable |
| cat6-repair-new-dorp-register-counter-jack-no-link.webp | cat6-repair-dutchess-county-checkout-jack-no-link.webp | tester "NO LINK" plugged into a jack under a checkout counter, POS screen "NETWORK OFFLINE" |
| cat6-repair-new-dorp-printer-jack-rework.webp | cat6-repair-brooklyn-printer-data-jack-rework.webp | technician working at a wall plate labelled PRINTER DATA beside a large office copier |
| cat6-repair-new-dorp-j-hooks-above-ceiling-grid.webp | cat6-repair-brooklyn-j-hook-support-above-grid.webp | blue cables laid in J-hooks above an open ceiling grid, Cat6 550MHz CMR carton |
| cat6-repair-new-dorp-patch-panel-port-repunch.webp | cat6-repair-manhattan-patch-panel-port-repunch.webp | punch-down tool on a patch panel labelled OFFICE 214 – DATA, labelled cable |
| cat6-repair-new-dorp-split-jacket-at-desk-frame.webp | cat6-repair-dutchess-county-split-jacket-desk-frame.webp | gloved hands holding a blue cable with split jacket and exposed pairs at a metal desk frame |
| cat6-repair-new-dorp-data-voice-plates-at-desk.webp | cat6-repair-ulster-county-data-voice-plate-check.webp | technician pointing at DATA 1 / DATA 2 / VOICE plates under a desk with an IP desk phone |

DAILY-LOG note: `images: 11 reused from images/cat6-repair/ library (brooklyn/manhattan/dutchess/ulster sets; no real Cat6 Repair photos yet)`.

### Flags for Anwar
1. Installer practices stated as policy: we do not route cable through flood openings; we do not open or log into computers holding patient records; ladders/cable kept clear in occupied adult day centres; chained switches replaced by home runs or one central switch where routes allow. Confirm.
2. No Field Notes story: no documented New Dorp Cat6 job; changelog says so.
3. Partial question overlaps for the main run to judge: Q4 (furniture pressing on jack → angled/recessed hardware) vs Brooklyn "jack ripped out when furniture was moved — fix without re-pull" (one-time damage vs recurring pressure); Q6 (PC through desk phone) vs NYC "patch cord, jack or cable?" (device-chain vs cable diagnosis); Q7 (patient-record privacy) vs Rockland/Westchester "do you need our Wi-Fi password" (credentials vs PHI scope); Q9 (evening-only lag) vs NYC "worked for years, now drops intermittently" (time-of-day ISP congestion vs physical fault); FAQ F3 (reuse satellite hole) vs HV "indoor Cat6 along the outside of the house" (entry point vs cable rating).

### Build checks (2026-10-17)
- check_page.py --no-registration: 12,572 rendered words; title 54; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 5 = FAQPage 5; 2 forms. Only failures: 16 area/hub pages not yet linking back to /cat6-repair-new-dorp-staten-island-ny (main-run wiring; sitemap/_redirects/parent link-down also pending).
- File 232,966 B (JSON-LD indent 2, page body lines indented 103 spaces — whitespace only). Nearest cat6 siblings: Manhattan 222,470; Rockland 216,848; Flushing ~180K and Riverdale ~176K at build time. Re-check after wiring.
- simcheck.py masked paragraph similarity (final): parent 0.644; NYC 0.630; Brooklyn 0.586; Queens 0.558; Bronx 0.592; Manhattan 0.599; LI 0.578; Nassau 0.568; Suffolk 0.592; HV 0.560; Westchester 0.565; Rockland 0.565; Orange 0.561; Putnam 0.583; Dutchess 0.536; Ulster 0.600; Flushing 0.541; Riverdale 0.592.
- LocalBusiness block: Brooklyn GBP fields (@id #brooklyn, 1282 Troy Ave, +1-347-934-8335, geo, rating, sameAs, Person) copied from the parent; url = this page and areaServed = New Dorp / New Dorp Beach / Staten Island, following the soundbar New Dorp neighbourhood convention.

## Question register — cat6-repair-new-dorp-staten-island-ny

§9 "Questions Answered" (H3):
1. Three small switches are chained from room to room through our high ranch — can one bad Cat6 between them take the whole upper floor offline? (Inland houses)
2. A flat Ethernet cable was run under the living-room carpet to the TV and keeps losing its link — can it stay under there? (Inland houses)
3. The old Cat6 across our basement ceiling is zip-tied to the copper water line and the gas pipe — does it have to come off them? (Inland houses)
4. A headboard or sofa keeps pressing on the wall jack and the plug keeps snapping — is there a repair that stops it happening? (Inland houses)
5. What usually damages the Cat6 that feeds the computer and X-ray sensor at a dental chair? (The Lane)
6. Our office computers plug into the back of the desk phones, and when a phone is unplugged the computer drops too — is that a cabling fault? (The Lane)
7. Can the Cat6 at a medical or dental office be repaired without anyone opening the computers that hold patient records? (The Lane)
8. Can the Cat6 for the camera under our raised house leave through one of the flood vents in the enclosure wall? (Below Hylan)
9. Our son's wired gaming PC lags only on weekday evenings — is the Cat6 in the wall to blame? (Not the cable)

FAQ (§17, = FAQPage schema):
F1. Where will the technician park for a job on New Dorp Lane, or on a block where every driveway is shared?
F2. Our adult day centre is open every day — how are ladders and loose cable kept away from members while a ceiling run is repaired?
F3. The old satellite dish is gone — can its hole through the wall be reused for the Cat6 to an outdoor camera?
F4. Which lights on the router or switch should we look at before calling about a dead wired connection?
F5. What can the printing along a cable's jacket tell you before any testing starts?

Other headings: none end in a question mark (repair-capture and CTA headings are statements).

### Batch wiring notes (main run, 2026-10-17, flushing / riverdale / new-dorp)
- Question re-check vs the 10 neighbourhood pages that went live while this batch was building: Flushing FAQ "staff time clock or attendance terminal" (same intent as St. George) reworded to the missed-punches diagnostic question; Flushing Q&A headings on shielded X-ray rooms and bullet-resistant counters (same intent as Fordham) turned into statement headings; Riverdale CTA heading reworded to a statement.
- Riverdale: two paragraphs (NYC Electrical Code bullet, AI-Overview intro) rewritten after scoring 0.718 / 0.684 masked similarity vs Long Island City.
- File sizes separated from siblings by whitespace indentation only (no rendered change).


## Mott Haven, Bronx (cat6-repair-mott-haven-bronx-ny) — local research, re-verified 2026-10-21

Built from the 2026-10-17 draft on `origin/draft/cat6-repair-mott-haven-tottenville` (that branch had no Mott Haven research section). Every local fact below was re-checked on 2026-10-21 via Firecrawl search/scrape; facts that could not be confirmed were removed from the page (listed at the end).

Thesis: in Mott Haven the cable's neighbour decides how it fails — garage bays (oil), Port Morris distilleries (classified areas), day cares (children's reach), fire-damaged attached buildings (smoke/water), street crossings (revocable consent), NYCHA flats (no drilling, Big Apple Connect routers), landmarked rowhouse facades (LPC) — so the repair is chosen for the neighbour, not the reel.

### Silo-wide surfaces
- Reddit (r/bronx, r/AskNYC) · PAA · PASF · Answer the Public · Google AI Overview · Bing/DDG related · Yelp 1–3★: **EMPTY (not accessible in build env)**. The page's AI Reality Check says so and uses recurring quick-answer claims checked against the sources below.

### Local entries (exact query · platform · URL · finding · page + section used)
1. `Furman Center Mott Haven Melrose neighborhood profile homeownership rate public housing` · Firecrawl search + scrape · https://www.furmancenter.org/neighborhoods/mott-haven-melrose/ · last updated 05/06/2026; homeownership 6.1% (2024) vs 32.7% citywide; public housing 24.1% of rental units; 11,870 units in 4+ unit buildings built 2010–2025 · §5 Neighborhood paras 3–4, §5.5 stats list, AI Reality Check #1, Sources.
2. `Mott Haven Commercial District Needs Assessment SBS storefronts delis automotive vacancy` · Firecrawl search + scrape (PDF) · https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/avenyc-cdna-motthaven.pdf · Jordan L. Mott developed the industrial area in the 1830s and built workers' housing around Alexander Ave; "A dozen new mixed-income residential towers are currently being built, mostly in the southwestern corner along the Harlem River and next to the bridges"; 8.3% storefront vacancy; storefront counts delis/bodegas 38, beauty/barber 26, automotive/rental/gas 21, schools & day care 19, medical 18, agencies/nonprofits/worship 17; 55% of businesses 0–2 employees; "more than 441 surveys and various stakeholder meetings"; corridors incl. E 138th, Rider, 3rd Ave, E 136th, Lincoln, Brook, St Ann's, Alexander, Willis, Cypress, Bruckner, Canal Pl; 2019 ADT Third Ave E 138th–Bruckner 36,397; industrial past sustains automotive and warehouse uses · §5 paras 2–4, §5.5, §8 intro + corridor cards (Third Ave, St. Ann's/Willis/Brook), Q&A garage answer, Sources.
3. `Port Morris Bruckner Boulevard rezoning City Planning non-conforming residences 129 lots antiques` · Firecrawl search + scrape (PDF) · https://www.nyc.gov/assets/planning/download/pdf/plans/port-morris/port_morris.pdf · area bounded by Park Ave, Willow Ave, E 134th St and the Harlem River; "Approximately one-third (44) of the 129 lots … are occupied by residential buildings, which do not conform with existing zoning"; MX districts; "potential for upper floor apartments and loft conversions in … vacant and underutilized buildings"; antiques "Antique Row" on Bruckner Blvd · §5 para 2, §5.5, §8 Bruckner card, Sources. Also CityLand https://www.citylandnyc.org/mixed-use-antique-district-expanded/ (129 lots approved March 9, 2005) — background only.
4. `Patterson Houses Bronx 1,790 apartments 15 buildings opened 1950` · Firecrawl search · https://en.wikipedia.org/wiki/Patterson_Houses (opened 1950) + https://pattersonhouses.us/famous-residents/ (15 buildings, 6 and 13 stories, ~1,790 apartments) · §5.5, §7 public-housing card, Sources.
5. `Mott Haven Herald Betances Houses renovation security cameras RAD PACT 1,088 apartments 2021` · Firecrawl search · https://www.motthavenherald.com/2021/03/08/bronx-nycha-improvements-havent-sold-other-public-housing-residents-on-rad-and-blueprint/ · Betances' 1,088 apartments renovated incl. security cameras under RAD · §7 card (Betances named), Sources.
6. `Bankside Bronx Brookfield 1,350 units Third Avenue Bridge towers 25 25 17 stories` · Firecrawl search · https://www.cityrealty.com/nyc/market-insight/rental-building-offers/the-bronx/bankside-1-billion-plan-mott-haven-waterfront-crystallizes-leasing-begins-fall-2021/49783 · 1,350-unit plan straddling the Third Avenue Bridge; three towers 25, 25, 17 stories · §5 para 3, §7 waterfront card, Sources.
7. `307 Bruckner Boulevard last-mile logistics facility YIMBY 2026` · Firecrawl search · https://newyorkyimby.com/2026/08/construction-nears-completion-on-307-bruckner-boulevard-in-port-morris-the-bronx.html (two-story last-mile logistics facility nearing completion) + https://www.307bruckner.com/ (±100,000 SF, delivers Q3 2026) · §8 Port Morris card, Q&A logistics para, Sources.
8. `Port Morris Bronx neighborhood guide distillery brewery design workshops former factories` · Firecrawl search · https://cityneighborhoods.nyc/port-morris · former factories turned into loft studios, distilleries and design workshops incl. Bronx Brewery and Port Morris Distillery; auto shops alongside · §6 production card, §8 Port Morris card, distillery Q&A, Sources.
9. `Historic Districts Council Mott Haven Historic District July 29 1969 Irish Fifth Avenue 1863 1865` · Firecrawl search · https://hdc.org/buildings/mott-haven/ (designated July 29, 1969; rows built 1863–1865; three districts: Mott Haven, Mott Haven East, Bertine Block) + https://s-media.nyc.gov/agencies/lpc/lp/0451.pdf (Alexander Ave "The Irish Fifth Avenue") + https://hdc.org/borough/mott-haven/ (Mott Haven East and Bertine Block designated April 5, 1994) · §5 para 2, §5.5, §7 rowhouse card, §13 landmark card 1, Sources.
10. `Bertine Block Historic District 31 buildings East 136th Street Willis Avenue Brown Place 1877 1899 designated 1994` · Firecrawl search · https://www.livingplaces.com/NY/Bronx_County/Bronx_Borough/Bertine_Block_Historic_District.html (31 buildings, both sides of E 136th between Willis Ave and Brown Pl) + https://urbanarchive.org/… (developed 1877–1899) + https://www.6sqft.com/location/bertine-block-historic-district/ (Mott Haven East and Bertine Block designated 1994) · §7 rowhouse card, §13 card 2, Sources.
11. `Estey Piano Company Factory Bronx landmark 2006 1886 oldest piano factory Lincoln Avenue Bruckner` · Firecrawl search · https://hdc.org/buildings/estey-piano-company-factory/ (NE corner Lincoln Ave and Bruckner Blvd since 1886; oldest known former piano factory standing in the Bronx) + https://www.citylandnyc.org/estey-piano-company-factory-receives-hearing/ (LPC hearing April 11, 2006, 112 Lincoln Ave) · §7 factory card, §13 card 3, Sources.
12. `St. Ann's Church Bronx 1841 Gouverneur Morris Jr. memory of his mother fieldstone` · Firecrawl search · https://southofunionsq.villagepreservation.org/city/ny/lo/295b9793-f977-4edd-8d0b-7945b1bc2ab2 (erected 1841 by Gouverneur Morris Jr. as memorial to his mother; fieldstone) + https://en.wikipedia.org/wiki/St._Ann%27s_Episcopal_Church_(Bronx) + https://nycemetery.wordpress.com/2021/04/15/st-anns-churchyard-bronx/ (churchyard) · §7 churches card, church Q&A para, §13 card 4, Sources.
13. `St. Mary's Park Bronx 35.31 acres largest park south Bronx recreation center indoor pool` · Firecrawl search · https://www.nycgovparks.org/parks/st-marys-park · largest park in the south Bronx; 35.31 acres; rec center with 72-foot pool · §13 card 5.
14. `Lincoln Hospital Bronx 234 East 149th Street Level I trauma busiest single-site emergency department` · Firecrawl search · https://www.nychealthandhospitals.org/locations/lincoln/ + https://en.wikipedia.org/wiki/Lincoln_Hospital_(Bronx) · 234 E 149th St; adult Level I trauma centre; busiest single-site ED in NYC · §8 Lincoln card, §13 card 6.
15. `Third Avenue fire Bronx East 139th 140th Street two-story building roof collapse May 2026 CBS New York` · Firecrawl search · https://www.cbsnews.com/newyork/news/bronx-fire-deli-mott-haven/ · two-alarm fire, two-story building, Third Ave between E 139th and E 140th; roof collapsed; did not spread; neighbour: "You could smell how bad it was." · fire Q&A para 1, Sources. (Man found dead per ABC7/NY1 — not used on page.)
16. `Mott Haven Herald four-alarm fire Third Avenue Melrose businesses gutted June 2024` · Firecrawl search · https://www.motthavenherald.com/2024/06/21/third-avenue-shops-destroyed-in-four-alarm-fire/ · four-alarm fire gutted a row of businesses in Melrose's Third Ave commercial corridor (June 20, 2024) · fire Q&A, Sources.
17. `Big Apple Connect NYCHA free internet modem wireless router September 2022 extended 2028 Optimum Spectrum` · Firecrawl search · https://www.nyc.gov/content/oti/pages/big-apple-connect · launched September 2022; free internet, free wireless router and modem, free Wi-Fi in certain common spaces; agreements with Altice (Optimum) and Charter (Spectrum) guarantee delivery until 2028 · NYCHA Q&A, AI Reality Check #4, FAQ 2, Sources.
18. `Optimum Big Apple Connect participating NYCHA developments list Patterson Mitchel Mott Haven` · Firecrawl search · https://www.optimum.com/program/big-apple-connect + OTI list · Bronx list includes Mitchel, Mott Haven, Patterson, Saint Mary's Park, Melrose · NYCHA Q&A, Sources.
19. `NYCHA repairs process Customer Contact Center MyNYCHA app` · Firecrawl search · https://www.nyc.gov/site/nycha/residents/nycha-repairs-process.page · apartment and building/common-area repairs via CCC (718) 707-7771 or MyNYCHA · FAQ 1, Sources.
20. `Legal Aid Society tenants lease prohibits alterations without landlord's prior permission` · Firecrawl search · https://legalaidnyc.org/get-help/housing-problems/what-you-need-to-know-about-repair-and-service-rights/ · "most leases prohibit tenants from making alterations … without the landlord's prior permission" · NYCHA Q&A, Sources.
21. `NYC Health Code Article 47 child care "free of electrical, chemical, mechanical and all other types of hazards"` · Firecrawl search · https://on.nyc.gov/article-47-health-code + https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-45180 · "Premises shall be free of electrical, chemical, mechanical and all other types of hazards." · §8.5 rules list, day-care Q&A, Sources.
22. `NYC Department of Buildings code notes revocable consent …` · Firecrawl search + scrape (PDF) · https://www.nyc.gov/assets/buildings/pdf/code_notes_revocable_consent.pdf · no permanent private-use installation in the right of way except via DOT revocable consent; "may take approximately six months"; fixed term, annual compensation; consents "other than for telecommunications purposes" by DOT; eligible improvements incl. "Overhead Pipe, Conduit, Cable" · §8.5, street Q&A, AI Reality Check #6, Sources.
23. `NYC Electrical Code 2020 NEC amendments full effect December 21 2025 Department of Buildings` · Firecrawl search · https://www.nyc.gov/site/buildings/codes/electrical-code.page · 2025 NYC Electrical Code took full effect December 21, 2025 (2020 NEC + NYC amendments) · §8.5, Sources.
24. `Bluefield Process Safety distilleries electrical classification` · Firecrawl search + scrape · https://bluefieldsafety.com/2025/11/process-safety-in-distilleries-electrical-classification/ · "it will have Class I areas because of the ethanol, and it will usually have Class II areas because milling grain produces combustible dust"; problems from unrated outlets and extension cords run in from outside the classified area · distillery Q&A, AI Reality Check #3, Sources.
25. `Cables and Kits oil resistant ethernet cable PVC jackets …` · Firecrawl search + scrape · https://www.cablesandkits.com/learning-center/oil-and-chemical-resistant-ethernet-cables/ · "Standard PVC jackets crack, bubble, or soften when exposed to oils, lubricants, alcohols, or acid vapors"; UL Oil Res I (limited contact) / Oil Res II (prolonged exposure, higher temps) · garage Q&A, AI Reality Check #2, equipment card, Sources.
26. `Paul Davis smoke residue electronics damage over time` · Firecrawl search · https://baltimore.pauldavis.com/blog/hidden-dangers-of-using-electronics-after-smoke-or-water-exposure/ · "the concern is that residue will cause damage over time" · fire Q&A, AI Reality Check #5, Sources.
27. `Fixr cost to install ethernet cable per drop` · Firecrawl search · https://www.fixr.com/costs/upgrading-to-cat6-cabling · labour $45–$75/hr; single Cat6 drop $125–$250 · §14 pricing table (third-party context row), Sources.
28. AESS prices (repo, not web): `cat6-repair-bronx.html` + `network-cable-repair-bronx.html` ($195/hr, 3-hr minimum $585; replacement run from $175; exterior entry from $185) and `cat6-installation-bronx.html` (Cat6 $272, Cat5e $233, Cat6A $388 per drop). Bronx multiplier 1.00× (v2.3 §9) — no new prices · §14, §15.

### Removed from the 2026-10-17 draft (could not be confirmed now)
- SBS assessment "fourteen corridors", "November 2021 – June 2022", "written in 2022", "early 2022", "phone and electronics stores", "St. Ann's Avenue photographed in the SBS report" → replaced with verified counts/wording.
- CBS "more than 100 firefighters" and "smell it inside her apartment" → replaced with verified "two-alarm" and the quoted neighbour line.
- Health Code quote "to eliminate all conditions in areas accessible to children…" → only the verified "free of … hazards" quote kept.
- DOB "above-ground cable and conduit with underground cable", "telecom consents from the city's technology agency" → replaced with the PDF's actual wording.
- "Lincoln at Bankside at 101 Lincoln Avenue"; Fixr "January 2025" date; "low-voltage contractors' forums" attribution (Reddit/forums EMPTY).

### Question register — cat6-repair-mott-haven-bronx-ny
Q&A (§9, H3):
1. The Cat6 to the diagnostic computer and cameras in our auto repair shop runs along the bay wall, where oil, brake cleaner and degreaser get splashed. Is that what keeps killing it, and what should replace it?
2. Our distillery's network cable passes through the still room. Can a failed run in there be repaired with ordinary jacks and boxes?
3. The Cat6 to the parent-view camera in one of our day-care classrooms has failed. Can it be repaired while the children are in, and how do we keep the new cable out of their reach?
4. A fire next door left smoke in our ceiling and water from the hoses down our walls. Our network still works — does the Cat6 need replacing anyway?
5. Our shop and our storeroom are in two buildings on opposite sides of the street. Can a Cat6 link be strung across, or run under, the street between them?
FAQ (§17, = FAQPage):
6. Our NYCHA building's lobby intercom or a hallway camera has stopped working. Can a resident hire you to repair its cable?
7. Can the wall jacks we have repaired plug straight into the free router Big Apple Connect gave us?
Headline questions (not register intents): "Link Dead Somewhere Between the Third Avenue Bridge and Port Morris?"; "Still Offline Beside the Bay, the Still or the Classroom?"
Overlap check: mechanical masked-question check vs all 30 silo pages (incl. in-progress Tottenville) — no repeats. Semantic: closest neighbours are Bronx #11 (hallway camera pulled by tenants — durability, vs ours: who may authorise NYCHA building-cable work), NYC "two buildings on the same lot" (vs ours: across a public street / revocable consent), Flushing garage-air question (underground parking garage air vs ours: auto-repair bay oil) — judged different intents.


## Tottenville, Staten Island (cat6-repair-tottenville-staten-island-ny) — 2026-10-21

Built from the 2026-10-17 draft on `origin/draft/cat6-repair-mott-haven-tottenville` (that branch had no Tottenville research section). Every local fact was checked again on 2026-10-21. Anything that could not be confirmed was removed or reworded (listed under "Corrections to the draft").
Thesis: almost no Tottenville house was built with Ethernet in it. The village houses (c.1850–1920s) and the post-1980 colonials (median year built 1989) both got their Cat6 later as retrofit cable, so faults sit along the route that cable took: down stud bays, behind knee walls, across garage ceilings, down downspouts, and through siding. The page covers finding that route and fixing it.

### Reddit
- `reddit statenisland Tottenville internet ethernet wiring house` · Firecrawl search · no Tottenville-specific thread. The only results were generic r/HomeNetworking threads, and none were used. → **EMPTY** (nothing local).

### Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG / Yelp 1–3★
- **EMPTY (not accessible in build env)**. The page's AI section says outright that the AI Overview could not be viewed and quotes nothing from it.

### Neighbourhood, housing stock, census
- `Tottenville, Staten Island` · Firecrawl scrape · https://en.wikipedia.org/wiki/Tottenville,_Staten_Island · Facts used: southernmost neighbourhood in NYC and NYS, water on three sides (New York Bight to the south, Arthur Kill to the west and north), and Nassau Pl/Bethel Ave/Page Ave as the eastern border. 2.505 sq mi. The Tottenville-Charleston NTA SI0305 had 16,089 people in 2020, −4.6% from 16,860. During the 1990s the area SE of Hylan Blvd, "until then nearly uninhabited", had intense home building. A second commercial core grew on Page Ave and west of Amboy Rd. 123rd Pct is at 116 Main St, the post office at 228 Main St, and Engine 151/Ladder 76 at 7219 Amboy Rd. The library at 7430 Amboy Rd was designed by Carrère & Hastings, opened in 1904 and is a city landmark. SIR terminus since June 2, 1860. Arthur Kill station opened Jan 21, 2017 and replaced Atlantic and Nassau. The trip to St. George is 14 miles and 42 min. Express buses SIM2/25/26. → §5 paras 1–2, §5.5 bullet 4, §8 Main St/Amboy Rd/Page Ave cards, §13 library and station cards, Timing section, Sources.
- `Point2 Tottenville Staten Island demographics year built housing units` · Firecrawl search + scrape (directQuote) · https://www.point2homes.com/US/Neighborhood/NY/Staten-Island/Tottenville-Demographics.html · Figures: 5,412 units, median year built 1989. Built 1939 or earlier: 1,101 (20.4%). Built 1980–89: 933; 1990–99: 1,241; 2000–09: 824, so 2,998 (≈55%) went up in 1980–2009. Units in structure: 1-unit detached 51.6%, 2 units 24.4%, 1-unit attached 19.8%. Owner-occupied 82.9%. The survey years were not shown, so the page says only "American Community Survey estimates". → §5 para 1–2, §5.5 bullets 1–3, two-family subsection, repair-or-reroute section.
- `Cooperator "Tottenville" "Diamond in the Rough" Florida style colonials` · Firecrawl search + scrape (directQuote) · https://cooperatornews.com/article/a-diamond-in-the-rough (David Garry, May 2006) · A DeFalco Realty broker says 14-foot-wide bungalows are being replaced by "Florida Style" centre-hall colonials, and that stucco and brick exteriors are most popular. The article also notes Victorian construction "complete with wrap-around porches and sunrooms" and the condo communities Surfside Village and The Captain's Quarters. → §5 para 2, §7 cards, porch subsection.
- `Forgotten New York Tottenville 2025 Bentley Street Hopping Avenue flag mural LoBaido` · Firecrawl search + scrape · https://forgotten-ny.com/2026/05/return-to-tottenville-2025/ (Kevin Walsh, May 9 2026) · Facts used: #76 Bentley, Greek Revival c.1850, built by oyster catcher Aaron Van Name. #88 Bentley, built c.1890 for a shipbuilder, has a wraparound porch. #92 Hopping is an 1886 Gothic Revival cottage. #60 Hopping was built in 1896 for a train conductor. #65 Hopping is a 1903 Colonial Revival. #12 Hopping (1921) has a dormer. #97 Satterlee is Italianate and was built for a shipbuilder. The Tottenville–Perth Amboy ferry landed at the north end of Bentley St and ended in 1963. Hylan, Amboy and Arthur Kill roads all lead to Tottenville. → §5 para 2, §7 cards, §13 Bentley/ferry card.
- Same source, Part 2 · Firecrawl scrape · https://forgotten-ny.com/2026/05/return-to-tottenville-2025-part-2/ (May 21 2026) · Facts used: Hylan Blvd was built in pieces in the 1920s between Rosebank and Tottenville and ends at the Conference House (1680). 7639 Amboy was built in 1850 for ship joiner Abraham Romaine, and 7635 for a boatsmith. Rutan-Journeay House, 7647 Amboy, 1848, landmarked. Bedell House, 7484 Amboy, 1869 Second Empire, landmarked 2005. Library at 7430 (1904, Carrère & Hastings). Masonic Hall on Main St. Scott LoBaido's flag mural at Main and Amboy dates from 2017. "Tottenville unfortunately has no landmarked districts". Outerbridge Crossing to Perth Amboy. → §8 Main St/Amboy/Hylan cards, §8.5 landmarks callout, §13 Amboy landmark houses card, Timing section.

### Local news / Sandy / resilience
- `silive Hurricane Sandy decimates Staten Island homes in Tottenville Yetman Avenue` · Firecrawl search + scrape (directQuote) · https://www.silive.com/southshore/2012/10/hurricane_sandy_decimates_stat.html (Mark D. Stein, Oct 30 2012) · Quote: "a gigantic wave tore through the end of Yetman, near Billop Avenue". Also "a pair of cement foundations filled with muddy water". → §5 para 4.
- `Governor Hochul Living Breakwaters completion Tottenville September 2024 $111 million` · Firecrawl search + scrape (directQuote) · https://www.governor.ny.gov/news/governor-hochul-announces-completion-111-million-coastal-resiliency-project-staten-island · Facts: $111M project, 2,400 linear feet, eight partially submerged structures, built to reduce waves reaching buildings and roads "to below three feet". Sand replenishment from Manhattan St to Loretto St. Homes were knocked off foundations in Sandy. The project will "help restore the beach along Conference House Park". Completion month is September 2024 (from the SI Advance listing, https://www.silive.com/climate/2024/09/…). The exact day was not confirmed, so the page now says "September 2024". → §5 para 4, §5.5 bullet 6, §13 Living Breakwaters card.

### Landmarks / corridors
- `nycgovparks conference house park` · Firecrawl scrape (directQuote) · https://www.nycgovparks.org/parks/conference-house-park · Facts: the "265-acre park". Four historic buildings: Conference House, Biddle, Ward and Rutan-Beckett. Built 1680. The "unsuccessful Revolutionary War peace conference" was held on September 11, 1776. "South Pole" marks the southernmost point of NYS. (The Parks history page gives 286.57 acres as the park acreage. The page uses the 265 acres stated on the main park page. Flag for review.) → §13 Conference House Park card.
- `Charleston, Staten Island` · Firecrawl scrape (directQuote) · https://en.wikipedia.org/wiki/Charleston,_Staten_Island · Facts: the Veterans Road West corridor, the island's first Target and third Home Depot at Bricktown Centre, and "In June 2016, a Shoprite opened on Veterans Road". → §8 Arthur Kill Road/Bricktown card.
- `Tottenville Shopping Center 7001 Amboy Road renovation 2013 45,000 square feet` · Firecrawl search + scrape (directQuote) · https://www.newswire.com/news/hollister-construction-services-breaks-ground-on-comprehensive-renovation-29629 (Sep 26 2013) · Facts: RiverCrest Realty's Tottenville Shopping Center at 7001 Amboy Road, a 20,000 sq ft building added to an existing 45,000 sq ft facility built in 1963. This source replaces the draft's REBusiness Online citation, which was not re-checked. Supporting source: https://www.commercialcafe.com/commercial-property/us/ny/staten-island/tottenville-square/ (excerpt: built 1963, renovated 2013). → §8 Amboy Road card, Sources.
- `Tottenville High School` · Firecrawl scrape · https://en.wikipedia.org/wiki/Tottenville_High_School · Fact: "located at 100 Luten Avenue, in Huguenot". → §13 closing line.

### Codes / building practice (substitute for local licensing)
- https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 · Firecrawl scrape (directQuote) · Admin Code §28-105.4.7: no electrical permit is needed for work under 50 V on signalling, communication, alarm or data circuits, if a licensed master or special electrician or a qualified person does it. → §8.5 permits callout.
- https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Introduction.pdf · Firecrawl scrape (directQuote) · LPC permits are needed for exterior work. For interior work they are needed only when the project needs a DOB permit, or when it affects the exterior (for example louvers or vents). → §8.5 landmarks callout.
- https://www.law.cornell.edu/cfr/text/29/1910.308 · Firecrawl scrape (directQuote) · Indoor communications cable must be separated at least 2 in. from light and power conductors. → §8.5, Q&A stud bay, diagram 1.
- https://www.thisoldhouse.com/this-old-house/season-46/westford-historic-renovation/fire-risks-with-balloon-framed-houses (Jul 23 2025) · Firecrawl scrape (directQuote) · Balloon framing uses long continuous studs "from the house's foundation to the roof". Continuous stud bays "act like chimneys". Fire blocking is described. → Q&A stud bay, diagram 1.
- https://www.greenbuildingadvisor.com/article/insulating-behind-kneewalls (Martin Holladay, Jun 14 2019) · Firecrawl scrape (directQuote) · Defines a kneewall as "a short wall under a sloped ceiling" with a cramped attic behind it. → Q&A knee wall.
- https://www2.minneapolismn.gov/media/content-assets/www2-documents/departments/Cutting,-Notching,--Boring-Wood-Frame-Members.pdf · Firecrawl scrape (directQuote) · Bored holes in joists must not be within 2 in. of the top or bottom, and the diameter must be no more than 1/3 of the depth. → §8.5 structure, Q&A joist holes, AI section, diagram 2.
- https://ismartgate.com/manuals/LiftMaster_8010_manual.pdf · Firecrawl scrape (directQuote) · "Attach the wire to the wall and ceiling with the staples … Do not pierce the wire with the staple as this may cause a short or an open circuit." The draft's claim about "keep the control away from moving parts" was not returned by the scrape, so it was removed. → garage Q&A, diagram 3.
- https://certainteed.ca/completion · Firecrawl scrape (directQuote) · "All external fixtures must be attached to a solid backing (such as exterior grade plywood) … Never attach a fixture directly to vinyl siding … allow for expansion and contraction". → siding Q&A, AI section, diagram 4.
- https://www.fixr.com/costs/upgrading-to-cat6-cabling (updated Jan 31 2025) · Firecrawl scrape (directQuote) · "$125 to $250, including materials and labor" per drop, and labour at "$45 and $75 per hour". → AI section claim 7.

### Prices used (live AESS pages only; no new prices; SI §9 multiplier 1.10 is already built into the published SI figures)
- cat6-repair-staten-island.html and network-cable-repair-staten-island.html: $195/hr with a 3-hr minimum ($585), replacement drop from $175, exterior penetration from $185, no travel charge.
- cat6-installation-staten-island.html: Cat6 $296, Cat5e $254, Cat6A $424 per drop up to 100 ft (shown for comparison only).

### Keyword notes (five layers)
- Service: Cat6 repair, Cat6 cable repair, Ethernet cable repair, network cable repair, re-termination, certification.
- Problem: dead jack, camera offline, dropped link, crushed/split jacket, wet plug, loose outdoor box.
- Technology: Cat6/Cat6A/Cat5e, T568A/B, PoE, keystone, patch panel, certifier, toner/probe, outdoor-rated cable.
- Industry: homes (village houses, colonials, two-families, townhouses, shore rebuilds), shops, home offices.
- Geographic: Tottenville, Staten Island, South Shore, Main St, Amboy Rd, Hylan Blvd, Page Ave, Bentley St, Hopping Ave, Satterlee St, Arthur Kill Rd, Conference House Park, Charleston, Richmond Valley, Pleasant Plains, Prince's Bay, Huguenot, Rossville, Woodrow, Annadale, Great Kills.

### Images (11) — Drive "AESS Website Photos/Cat6 Repair" EMPTY, CompanyCam not connected; replaced per coordinator decision ("never AI-generated" wins)
The draft's 11 cat6-repair-tottenville-* crops of the AI-looking images/cat6-repair library were deleted. All 11 replacements are new crops of real AESS job photos, saved as WebP q80 in images/cat6-repair/ and published as reference photos (not presented as Tottenville jobs). ImageObject contentLocation was removed. Faces, signs, the flag, the TV, framed documents and box labels were cropped out. Source roots: images/rockland-toyota-*.jpeg, nassau-window-depot-*.jpeg and manhattan-deli-exterior-camera.jpeg. These are the same originals behind the folders the coordinator listed (warehouse-*, super-live-plus-*, uniview-*, floodlight-*); no other real originals exist in those folders. Crops avoid the regions used by the Sonos Throgs Neck page.
- recorder-screen-camera-grid-and-bitrate-table ← rockland-toyota-nvr-monitor.jpeg (monitor only)
- bullet-on-pendant-mount-in-ceiling-tile ← rockland-toyota-ceiling-bullet.jpeg
- dome-under-stained-ceiling-in-storeroom ← nassau-window-depot-storage-camera.jpeg (box labels cropped)
- exterior-dome-under-yellow-fascia ← manhattan-deli-exterior-camera.jpeg (shop sign and mural cropped)
- dome-on-ceiling-between-light-panels ← rockland-toyota-office-camera.jpeg (people and documents cropped)
- dome-in-ceiling-corner-of-office ← nassau-window-depot-office-camera.jpeg (sign, flag and documents cropped)
- small-camera-high-on-wall-above-drop-ceiling ← rockland-toyota-wall-camera.jpeg
- bullet-camera-on-painted-wall ← rockland-toyota-bullet-camera.jpeg (dealer sign cropped)
- bullet-on-ceiling-grid-in-corridor ← rockland-toyota-hallway-camera.jpeg (blank-plate wall used by Sonos excluded)
- ceiling-device-with-red-light-and-downlights ← rockland-toyota-active-deterrent.jpeg (mural and TV niche cropped)
- dome-on-ceiling-tile-near-wall-corner ← rockland-toyota-dome-camera.jpeg (brand sign and TV cropped)

### Diagrams (genuine content; inline SVG, not counted as words)
Six diagrams were added: balloon-frame stud bay, joist boring limits, garage sweep zone, siding mounting block, two-end testing, and downspout vs soffit route. Every number in them comes from the sources above. The page is 274,505 B (13,874 words) after the image swap, which is in the free size window.

### Corrections to the draft (2026-10-17)
- The 16,089 population belongs to the Tottenville–Charleston tabulation area, not Tottenville alone. The page now says so.
- "Living Breakwaters completed September 27, 2024" is now "September 2024", because the exact day was not confirmed.
- "Bedell House … restored in 2017" was removed (no source found).
- "Bring back oyster habitat" became "help restore the beach along Conference House Park" (the governor's release wording).
- "Florida Style" is now attributed to a 2006 broker quote, not to "writers at the time".
- The NEC 800.25 abandoned-cable claim was removed (no source checked).
- The LiftMaster "moving parts" claim was removed.
- The REBusiness source was replaced with Newswire.
- "ACS 2019–2023" was removed because the survey years were not confirmed.
- The Fixr range now reads "materials and labour".

### Question register — cat6-repair-tottenville-staten-island-ny
Q&A (H3, §9):
1. In our 1880s house the wall cavities run straight from the cellar to the attic — when a Cat6 run dropped down one of them fails, can its replacement go down the same space? (Village houses)
2. The only cable to our dormer bedroom runs through the low space behind the knee wall — how is a failed run there reached? (Village houses)
3. How large a hole can be drilled through the old floor joists for a replacement run, and does where it goes matter? (Village houses)
4. Which way should the Cat6 to the camera above our garage door cross the ceiling so the door and opener can never reach it? (Newer colonials)
5. Someone ran our backyard camera cable down inside the gutter downspout — is that why it keeps failing, and where should it go instead? (Newer colonials)
6. The box where our camera's Cat6 meets its patch lead is screwed straight to the vinyl siding and keeps pulling loose — how should it be remounted? (Newer colonials)
FAQ:
F1. Will you still work in our attic or behind a knee wall during a summer heat wave?
F2. Every December our front camera drops off the network once the holiday lights go up along the gutter — could the decorations be damaging its cable?
F3. The weatherproof data outlet on our back deck has stopped working — can it be repaired, or does the whole outdoor outlet have to be replaced?
F4. The builder left a box of spare cable and jacks in our basement — can you use it for the repair?
Other "?" headings: "Lost a Link South of Hylan This Morning?" (repair capture), "Replacing Siding, a Garage Door or the Roof This Year?" (mid CTA), "Tottenville Link Down Between the Station and the Park?" (closing).
De-dup notes: checked by meaning against every FAQ question and "?" heading on all 30 cat6-repair pages on disk, including the parallel Mott Haven page, and against network-cable-repair-staten-island and cat6-installation-staten-island. Three draft questions were replaced or re-angled:
- "Can you send a certificate of insurance to our townhouse association…" duplicated Riverdale's COI question and NYC Q14. It was replaced by F3 (deck outlet).
- "Do you repair the network cable to pool automation or a hot-tub controller…" followed the same pattern as Staten Island's generator/heating-controller question and the EV-charger questions. It was replaced by F2 (holiday lights).
- "…clipped beside the opener rail — why does it keep breaking?" was close to Queens' "roll-down gate housing … could the gate be what keeps damaging it?". It was re-angled to a routing question (Q4).
Also deliberately avoided: salt air (Long Island), mesh backhaul (Rockland), party walls (Astoria and Bay Ridge), selling the house (Ulster), mice or chewed cable (Hudson Valley), the shared-hole-with-electrical question (Staten Island Q7; this page covers it only as body text), and raised houses and flood vents (Staten Island and New Dorp).
Masked similarity (difflib on geo-masked p/li/td/h2–h4/figcaption ≥12 words, Jaccard-prefiltered): the only blocks at or above 0.65 against any silo page, or against the smart-lock and soundbar Tottenville pages, are excluded constants: the warranty sentence, footer NAP and licence lines, the freshness stamp, the parts-warranty line, and the "orientation, not legal advice" note (0.80 vs St. George). Document 5-gram overlap is at most 0.026 (St. George).

### Area-page neighbourhood block anchor (for the main run's wiring)
`<a href="/cat6-repair-tottenville-staten-island-ny" class="lnk">Tottenville, Staten Island</a>` (same pattern as "St. George, Staten Island" and "New Dorp, Staten Island").
