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
