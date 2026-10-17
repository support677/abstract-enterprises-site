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
