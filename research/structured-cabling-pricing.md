# Structured Cabling Pricing — silo research

Created 2026-10-18 by the REBUILD run for `structured-cabling-pricing-suffolk-county` (queue line: `REBUILD | structured-cabling-pricing-suffolk-county | Structured Cabling Pricing | Suffolk | up / | (631) 407-2884 | GBP Brooklyn`). No `research/structured-cabling-pricing.md` existed before this run.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. "Excerpt" = read only as a search-result snippet. Tools: WebSearch + WebFetch (Claude), Firecrawl search (mcp__Fire_Crawl__firecrawl_search). Shell curl blocked, not used. Sources marked **carried** were fetched and verified by the 2026-10-18 network-installation Suffolk run and are recorded in `research/network-installation.md` Part 2 (IDs in brackets); cited here, not re-fetched.

Page section labels (Suffolk page): §Hero, §Quick, §5 Neighborhood (+5.5 facts), §Repair capture, §6 Services, §7 Architecture (+7.5 methods), §8 Commercial (+8.5 rules), §9 Q&A (clusters A–E), §10 Equipment (+comparison table), §10.5 AI Reality Check (H3 1–7), mid CTA, §11 form, §12 Process, Checklist, §13 Landmarks, Towns table, §14 Pricing (+site lines, calculation, volume, worked examples), mid CTA, §15 Packages (+BYOE), §16 Services grid, Field Notes, §17 FAQ, §19 Siblings, §Sources, repair line, NAP block.

---

## Part 1 — Silo-wide findings

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `reddit cost per drop cat6 running cable office quote too high` · WebSearch → result `lr.in.psf.lt/r/homelab/comments/1lduoif/builder_wants_600_per_drop` (a read-only mirror of reddit.com/r/homelab/comments/1lduoif/) · WebFetch. Finding: "Builder wants $600 per drop!" — new-build house, no walls up; commenters: low-voltage installers "often charge about $50 per drop", others $75–$150, one builder $125 regardless of length; "'I don't want to' pricing"; open walls make it cheap; termination/scope changes price. Location eastern Wisconsin (not local). Used: §10.5 H3 3 and H3 4; Sources (linked as reddit.com canonical URL). Local Reddit (r/longisland) for cabling prices: EMPTY (no thread found). |
| 2 | Google People Also Ask | EMPTY (not accessible in build env). |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on-page and checks the claims published by cost guides/forums instead (T1, R1). |
| 6 | Area landmarks | Part 2 L*. |
| 7 | Area use cases / building stock | Part 2 B*. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env). Firecrawl search used as a second engine (F1, F2). |
| 9 | Local news | East Hampton Star, CRE Daily (GlobeSt/C&W), NY Senate press release, Shelter Island Reporter (carried), RiverheadLOCAL (carried). |
| 10 | Hyperlocal | East Hampton Star (A1); 27east (carried). Hyperlocal stories specifically about cabling prices: EMPTY. |
| 11 | Yelp 1–3★ | `yelp network cabling installation Suffolk County NY reviews` · Firecrawl search → only Yelp search-listing excerpts (e.g. https://www.yelp.com/search?find_desc=Network+Cabling&find_loc=Cutchogue%2C+NY ; aggregate star counts, no review text). 1–3★ review content: EMPTY (not accessible in build env). Not used. |

### 1.2 Cost guides and competitors (silo-wide)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `structured cabling cost per drop 2025 Cat6 installation average price` · WebSearch → WebFetch | https://www.fixr.com/costs/upgrading-to-cat6-cabling | Updated Jan 31 2025: average $3,800 (≈2,000 ft, eight drops); range $2,000–$5,000; contractor drop $125–$250 incl. materials and labour; ISP drop $90–$120; labour $45–$75/hr, 40–48 hrs for 2,000 ft; Cat6 material $0.15–$0.25/ft; drivers "cable length, number of drops, and installation complexity"; outdoor conduit/trenching and attic runs add cost. | §10.5 H3 1, 2, 5; §10 comparison table (ISP column, described without numbers); Sources |
| T2 | same search (excerpts only) | https://www.monoprice.com/p/resources/cat6-cable-installation-costs-what-you-really-pay-for ; https://unio.digital/blog/structured-cabling-cost-per-drop ; https://datawiresolutions.com/blog/network-cabling-cost | Not opened. | — |
| F1 | `"structured cabling" Long Island cost per drop Hauppauge OR Ronkonkoma OR Melville` · Firecrawl search | https://www.abstractenterprisessecuritysystems.com/structured-cabling-installation-long-island (excerpt) | AESS's own LI page publishes the Brooklyn base list unmultiplied ($175 Cat6, $250+ Cat6A, +$40 plenum, $20 cert, $8/ft tray) and $150–$300 per drop. Conflict with §9 — see FLAG 2. Competitor results (netwolfcyber.com, networkcablinglongisland.com, lowvoltagenewyork.com, mason247.com) excerpts only, no prices; not used. | FLAG only |
| P1 | `NYS Department of Labor prevailing wage schedule Suffolk County telecommunication worker data cabling` · WebSearch → WebFetch | https://broadband.ny.gov/prevailing-wage-webinar-deck | ConnectALL projects covered by Labor Law §224-e from Apr 9 2022, no funding threshold; §224-f / §224-a other cases; three-prong public work test ("A public agency must be a party to a contract involving the employment of laborers, workmen, or mechanics"); rates set every July 1 by the Bureau of Public Work; schedules July 1–June 30. No Suffolk telecom rate given. | §8.5 bullet, §9 Q "school district or village", Sources |

### 1.3 Approved price base (from this repo — no prices invented)
Base = `structured-cabling-pricing.html` (silo main page, Brooklyn/NYC base): Cat6 drop $175; Cat6A $250+; plenum +$40; shielded +$50; CMR included; minimum $500; Fluke cert $20/drop; 24-port panel $75; 48-port $125; wall cabinet $250; floor rack $450; horizontal manager $50; vertical $75; tray/J-hooks $8/ft; Wi-Fi AP drop $300; rack cleanup $500+; demarc $350+; fiber termination $35; OTDR $40/strand; multimode 12-strand floor-to-floor $4,500–$7,000; single-mode 24-strand building-to-building $8,000–$15,000+; volume tiers 5% / 8–12% / 15–20%. Service rate $195/hr, 3-hr minimum ($585) — protected, not multiplied.
Suffolk = × 1.20 (v2.3 §9), round half-up only where non-integer: $210; $300+; +$48; +$60; included; $600; $24; $90; $150; $300; $540; $60; $90; $9.60 → $10/ft; $360; $600+; $420+; $42; $48; $5,400–$8,400; $9,600–$18,000+. Percent tiers unchanged.
Worked examples / packages (§14, §15) are sums of these lines only: home office 4×$210 = $840 (+$390 panel+cabinet → Starter $1,230); 12 Cat6A + panel + cabinet + cert = $4,278 − 5% on drops $180 = $4,098 (Standard); warehouse side 4 AP + 120 ft J-hooks = $2,640; Melville 20 Cat6A + plenum + cert + 48-port = $7,590 − $300 = $7,290; Premium 24 Cat6A $7,200 − 5% = $6,840 + 2 AP $720 + 48-port $150 + rack $540 + vertical $90 + cert $576 + 150 ft $1,500 = $10,416.
Not priced (no approved number exists; described as drivers only): lift days, trenching, abandoned-cable removal, ceiling tiles/patching, landlord after-hours fees, island freight, outdoor conduit/materials, removal at lease end.

### 1.4 Keywords (five layers)
- Service: structured cabling pricing Suffolk County, structured cabling cost, cost per drop, Cat6 drop price, Cat6A drop price, network cabling cost, data drop installation, access point drop, patch panel installation, network rack installation, fiber between buildings, cable certification, demarc extension, rack cleanup.
- Problem: inherited cable from previous tenant, re-divided bay, closet on wrong side of demising wall, high ceiling / lift, open deck no support, return-air plenum ceiling, 100 m channel limit, long single-storey store, raised house flood level, barn/outbuilding link, brittle ceiling tiles, lease removal clause, landlord cabling standards, comparing quotes, sales tax on invoice, prevailing wage public work.
- Technology: Cat6, Cat6A, CMR riser, CMP plenum, shielded F/UTP, multimode OM3/OM4, single-mode OS2, OTDR, Fluke certification, J-hooks, cable tray, keystone jack, 24/48-port panel, wall cabinet, floor rack, point-to-point wireless bridge, outdoor-rated cable, fire-stop.
- Industry: flex/industrial and distribution, office park tenants, professional offices in converted houses, medical suites, retail (Route 58), farms and wineries, new construction / developers, school districts, villages and towns, homeowners and home offices.
- Geographic: Suffolk County; ten towns (Babylon, Huntington, Islip, Smithtown, Brookhaven, Riverhead, Southold, Southampton, East Hampton, Shelter Island); Hauppauge / Long Island Innovation Park (Oser Ave, Motor Pkwy), Route 110 (Melville, Farmingdale, Huntington Station), Melville Corporate Center (Maxess Rd), Islandia, Bohemia, Ronkonkoma / Station Yards / MacArthur Airport, Holbrook, Stony Brook / Route 25A, Upton / BNL, Riverhead / Route 58 / Tanger, Calverton, Westhampton / Gabreski, North Fork (Mattituck, Cutchogue, Greenport, Orient), Montauk Highway / Amagansett, Lindenhurst, Amityville, Bay Shore, Fire Island, Shelter Island.

---

## Suffolk

**Thesis (distinct from LI cat6 page = horizontal geometry/90 m; network-installation-suffolk = carriers/outages/breach):** in Suffolk the drop count sets only the floor of a cabling price — the **building's previous life** sets the rest: re-divided 1970s Hauppauge flex bays (17 ft clear, inherited cable, closet on the wrong side of the new wall → lift days, J-hooks, clean-up), second-generation Route 110/Melville suites (landlord standards, plenum per building, removal clauses), ~1970 houses and houses used as offices (route-finding through attic/basement), farms/wineries (links between buildings), Sandy-raised South Shore houses (layout above the flood line) and new construction at Station Yards (open walls, two visits, certification). Around that sit three published money rules: the ×1.20 Suffolk factor (distance, East End travel), Suffolk's 8¾% sales tax since 2025-03-01 with the capital-improvement test, and prevailing wage on public work.

### Building stock, markets (B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| B1 | `Suffolk County housing stock year built median age homes Long Island census built 1950s 1960s ranch` · WebSearch → WebFetch | https://stacker.com/stories/new-york/counties-oldest-homes-new-york | Suffolk County #47 of 50; median year built 1970; Census 2023 5-year estimates. | §5 para 1, §5.5 bullet 1, §9 Q house, Sources |
| B2 | `Hauppauge Industrial Park buildings built 1960s 1970s aging flex buildings renovation` · WebSearch → WebFetch | https://www.loopnet.ca/Listing/320-Oser-Ave-Hauppauge-NY/35572244 | Built 1975; 20,114 SF RBA; 17' clear; office ±3,700 SF; type Industrial/Warehouse. | §5.5 bullet 2, §9 Q height (17 ft), Sources |
| B3 | `Melville Route 110 office building conversion 2024 2025 vacancy Long Island office market` · WebSearch → WebFetch | https://www.credaily.com/briefs/long-island-office-vacancy-dips-below-12-first-since-2020/?.tsrc=rss | Sep 28 2026: C&W — LI office vacancy 11.8% Q2, first below 12% since mid-2020; Suffolk 50.2% of H1 leasing; largest lease Microchip 73,500 SF in Hauppauge; NYU Langone paid $135.5M for Melville property to demolish offices for a hospital (not used). | §5.5 bullet 3, Sources |
| B4 | carried [B1] | https://www.costar.com/article/131430884/hauppauge-leads-long-island-metropolitan-area-in-available-industrial-space/ | Aug 2024: Hauppauge area largest available industrial space on LI; small-bay preference. | §5 para 1, Sources |
| B5 | carried [B2] | https://cmmllp.com/hauppauge-industrial-park-update-2017-long-islands-oasis-productivity-innovation/ | ~1,350 businesses, ~11 sq mi (2017); renamed Long Island Innovation Park at Hauppauge (2019). | §8 card, §13 card, Sources |
| B6 | carried [B3] | https://iraceenterprises.com/route-110-corridor/ | Route 110: Farmingdale, Melville, Huntington Station; office, R&D, flex; LIE access. | §8 card, Sources |
| B7 | carried [B4] | https://nyrej.com/print/52376 (search result) | Melville Corporate Center, 105 Maxess Rd. | §13 card |
| B8 | carried [B5] | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Station Yards 53 acres at Ronkonkoma LIRR; ~1,450 units at completion. | §5.5 bullet 6, §8 card, §9 Q open walls, §13 card, Sources |
| B9 | carried [B6] | https://en.wikipedia.org/wiki/Stony_Brook_University ; https://en.wikipedia.org/wiki/Brookhaven_National_Laboratory | SBU 213 buildings; BNL on former Camp Upton. | §13 cards, Sources |
| B10 | carried [B7] | https://brixmor.com/re-development/completed-projects/the-shops-at-riverhead | Shops at Riverhead across from Tanger Outlets (Route 58). | §8 card, §13 card, §9 Q long store, Sources |
| B11 | carried [B10] | https://www.27east.com/southampton-press/new-business-park-continues-to-take-shape-in-westhampton-1406404 | Hampton Business District at Gabreski, county land. | §8 card, Towns table, Sources |
| B12 | carried [B13] | https://shelterislandreporter.timesreview.com/2025/02/02/suffolk-closeup-the-farming-county/ | 578 farms (2022), 79 wineries. | §5.5 bullet 5, Sources |
| B13 | carried [B12] | https://www.ny.gov/counties/suffolk | Ten towns; ~86 miles. | §5 para 1, Towns table, Sources |

### Tax, licensing, public work, land rules (K)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| K1 | `Suffolk County NY sales tax rate 8.625%` · WebSearch → WebFetch | https://trykintsugi.com/sales-tax-guides/usa/new-york/suffolk-county | Combined 8.75% (4% state, 4.375% county, 0.375% special district). Cross-checked against K2. | background |
| K2 | `tax.ny.gov Publication 718 Suffolk County sales tax rate` · WebSearch → WebFetch | https://www.tax.ny.gov/forms/locality-notices/st-25-1.htm | "Effective March 1, 2025, Suffolk County is increasing its local sales and use tax rate from 4¼% to 4⅜%"; combined 8⅝% → 8¾%. | §5 para 4, §5.5 bullet 4, §9 Q tax, §10.5 H3 7, §14, Sources |
| K3 | same · WebFetch | https://www.grassiadvisors.com/blog/suffolk-county-sales-tax-rate-increase-effective-march-1-2025-what-construction-businesses-need-to-know/ | Same change; materials taxed at 8¾% from 3/1/2025; contracts before Dec 17 2024 transition. No reason given for increase. | Sources |
| K4 | `tax.ny.gov capital improvement tax bulletin TB-ST-104 installation wiring building sales tax contractor` · WebSearch → WebFetch | https://tax.ny.gov/pubs_and_bulls/tg_bulletins/st/capital_improvements.htm | Three tests (adds value/prolongs life; becomes part of real property; intended permanent); "no sales tax due on the charge to the customer" with Form ST-124; contractor pays tax on materials. Wiring not named as an example. | §9 Q tax, §10.5 H3 7, Sources |
| K5 | `Suffolk County Code chapter 563 electrician license low voltage "electrical field" exemption town village` · WebSearch → WebFetch | https://www.nysenate.gov/newsroom/press-releases/2014/lee-zeldin/senator-zeldin-announces-huge-win-suffolk-county | Aug 15 2014: S.5132 signed — lets Suffolk adopt "one single permit at the county level"; electricians work in any municipality "without additional town or village licensing permits required". | Sources (§8.5 licensing bullet states only the Ch. 563 carve-out) |
| K6 | carried [K4] | https://ecode360.com/14948079 | Ch. 563 Art. XI not applicable in towns/villages with own licensing law. | §8.5, Sources |
| K7 | carried [K2] | https://www.suffolkcountyny.gov/Consumer-Affairs | County Consumer Affairs; electrician licences. | Sources |
| K8 | carried [K7] | https://ePermits.southamptontownny.gov/eElectrical | Southampton electrical e-permits. | Towns table, Sources |
| K9 | carried [K8] | https://newyork-811.com/homeowners/ | 811 covers Nassau/Suffolk; ≥48 hours notice. | §8.5, site-lines para, Process step 4, Sources |
| K10 | carried [K9] | https://pb.state.ny.us/public-information/faqs/ | Central Pine Barrens; Core clearing restricted. | §8.5, site-lines para, Sources |
| K11 | Town-by-town low-voltage permit rules | — | EMPTY (not established for any town). Page says we tell you if your town asks for more. | §8.5 |
| K12 | Suffolk telecom/communications prevailing wage rate | — | EMPTY (schedule not retrieved; page states the rule, no rate). | — |

### Flooding, access (F/A)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| F1 | carried [P3] | https://www.weather.gov/media/okx/coastalflood/Lindenhurst%20impacts.pdf | Sandy inundation south of Montauk Hwy in Lindenhurst, Amityville, Babylon; repeated flooding since. | §7 card, §9 Q raised house, Sources |
| F2 | carried [P4] | https://www.fema.gov/sites/default/files/2020-07/fema_tb5_free_obstruction_requirements.pdf | Enclosures below elevated buildings limited to parking, access, storage. | §7.5, §9 Q raised house, Sources |
| A1 | `"trade parade" East End Hamptons Route 27 traffic contractors morning` · WebSearch → WebFetch | https://www.easthamptonstar.com/opinion-columnists/202178/mast-head-new-trade-parade | July 8 2021: "new trade parade" pours out of Springs in the morning; stop-and-go on Montauk Highway through Amagansett. | §5 para 3, Sources |
| A2 | carried [B14] | https://www.fireislandnews.com/communities/kismet/fire-island-ferries-freight-service-stalled/ ; https://www.nps.gov/fiis/planyourvisit/off-road-vehicle-permit-faqs.htm | Fire Island freight via Bay Shore; NPS limits contractor vehicles. | §9 Q ferry, Towns table, Sources |

### Landmarks (L) used in §13
Long Island Innovation Park at Hauppauge (B5, B2), Melville Corporate Center / Maxess Rd (B7), Station Yards Ronkonkoma (B8), Stony Brook University (B9), Brookhaven National Laboratory Upton (B9), Tanger Outlets / Route 58 Riverhead (B10).

### Images (11) — permanent image rule
- Step A: Drive "AESS Website Photos" has no Structured Cabling subfolder (per batch brief). Step B: CompanyCam not connected.
- Library check: every file in images/network/, network-cable-repair/, cat6/, cat6-repair/ (aess-*), low-voltage/, fiber-optic-installation/ (aess-*) was opened as contact sheets. All show the hallmarks of AI-generated imagery (rendered technicians with uniform "Abstract Enterprise LLC" logos, a non-AESS phone number 844-386-7238 printed on shirts, staged BEFORE/AFTER panels with text) — the same finding as research/network-installation.md FLAG 1. Not used (the rule forbids AI-generated images).
- Used instead: 11 new crops of the real AESS job photos in images/ root (Rockland Toyota, Manhattan deli, Nassau Window Depot jobs), cropped to ceilings/cable only — no people, logos, signage, plates or readable documents; crops differ from those used on network-installation-suffolk-county and dahua-camera-installation-suffolk-county. WebP q80, ≤1600 px. Captions say "Example photo from another AESS job (not a Suffolk …)".

| images/structured-cabling-pricing/structured-cabling-pricing-suffolk-county-… | Source (crop box px) | Placement |
|---|---|---|
| blue-and-white-cable-runs-along-overhead-pipe.webp | rockland-toyota-nvr-monitor.jpeg (200,0,860,215) | Hero (eager, og:image) |
| stained-ceiling-tiles-over-storage-room-corner.webp | nassau-window-depot-storage-camera.jpeg (0,0,935,520) | §5 |
| mixed-cable-bundle-beside-rack-rails.webp | rockland-toyota-nvr-monitor.jpeg (0,180,280,700) | §6 |
| high-suspended-ceiling-grid-over-two-storey-hall.webp | rockland-toyota-showroom.jpeg (330,0,1247,300) | §7 |
| ceiling-grid-with-light-troffers-and-detector.webp | rockland-toyota-bullet-camera.jpeg (150,600,935,900) | §8 |
| corridor-ceiling-with-return-air-grille.webp | rockland-toyota-hallway-camera.jpeg (0,70,935,640) | §9 flex-bay Q |
| drop-ceiling-tiles-and-fluorescent-troffer.webp | manhattan-deli-monitor.jpeg (0,0,440,300) | §9 end |
| unused-recorder-channels-beside-rack-equipment.webp | rockland-toyota-nvr-monitor.jpeg (850,600,1247,935) | §10 |
| drop-ceiling-edge-below-tall-painted-wall.webp | rockland-toyota-wall-camera.jpeg (0,620,1050,935) | §13 |
| textured-ceiling-tiles-at-office-wall-corner.webp | nassau-window-depot-office-camera.jpeg (380,0,800,470) | §14 |
| dropped-soffit-with-recessed-downlights.webp | rockland-toyota-active-deterrent.jpeg (380,560,935,800) | §15 |

Log note: `images: 11 reused (re-cropped) from images/ root real AESS job photos (no real structured cabling photos yet; images/network/, network-cable-repair/, cat6/, cat6-repair/, low-voltage/, fiber-optic-installation/ rejected as AI-generated)`.

### FLAGS for Anwar / main run
1. **Image library** — the silo folders named in the brief appear AI-generated (see above). Real cabling/rack photos for this silo are needed in Drive.
2. **Price conflict** — `structured-cabling-pricing.html` says "Same per-drop pricing across all 5 NYC boroughs, Long Island, and the Hudson Valley"; `structured-cabling-installation-long-island` publishes the base list unmultiplied; the old Suffolk configurator used a different scheme (min $750, Cat6 $226, panel $194, rack $388, cert $32, concealing $259/drop); `cat6-installation-suffolk-county` uses yet other figures ($211/$254…). This page applies v2.3 §9 ×1.20 to the silo main page list. Decide which convention the silo keeps.
3. **Up-link** — queue says `up /`, but check_page.py expects child pages to link to `/structured-cabling-pricing-long-island`, which does not exist. The page links Home (breadcrumb) and `/structured-cabling-pricing` (main list). The check line "no link up to parent hub" cannot pass without a rule decision or a new LI hub page.
4. **Sibling link-backs** — all 12 sibling pages lack links to this page (not a registration-flag check, so it also fails with --no-registration). Wiring for the main run.
5. **Registration** — `_redirects` has the 301! rule but not `/structured-cabling-pricing-suffolk-county /structured-cabling-pricing-suffolk-county.html 200`. Sitemap entry exists (lastmod 2026-05-03 → update).
6. **Unsourced AESS method statements** (generic, no stats): lift ~12 ft threshold, separate rough-in/trim-out visits, landlord fee passthrough, island jobs quoted individually, reuse of jack boxes, Wisetack financing (link carried over from the old page).
7. **Packages** are sums of published lines, not separately approved package prices.

---

## Question register — every FAQ / Q&A / "?" heading on every structured-cabling-pricing page (extracted from HTML 2026-10-18)

### structured-cabling-pricing (silo main page, 14)
- Cat6 vs Cat6A: Which Should You Pick?
- When Is Plenum Cable Required? (callout)
- How much does a Cat6 drop cost in NYC?
- How much does a Cat6A drop cost in NYC?
- What's the minimum cabling job size?
- Do you give volume discounts?
- What does a 20-drop office cost?
- When is plenum-rated cable required?
- What's included in Fluke certification?
- Cat6 vs Cat6A — which should I pick?
- How much does fiber optic cabling cost?
- Do you do after-hours and weekend work?
- How fast can you start?
- Do I need a permit for cabling?

### structured-cabling-pricing-manhattan (9)
- Why is Manhattan cabling pricing higher than Brooklyn?
- Do you handle co-op alteration agreements?
- How long does a Manhattan cabling job take?
- Do you do off-hours and weekend work?
- When is plenum cable required in a Manhattan building?
- What about LPC landmarked buildings?
- How do you fish cable through pre-war plaster walls?
- Do you certify every drop?
- Are you licensed for Manhattan?

### structured-cabling-pricing-bronx, -brooklyn, -dutchess-county, -nassau-county, -orange-county, -putnam-county, -queens, -rockland-county, -staten-island, -ulster-county, -westchester-county (0 each)
Configurator template pages — no FAQ / Q&A / "?" headings.

### structured-cabling-pricing-suffolk-county — OLD template page, before this rebuild (0)
Configurator template, no questions.

### structured-cabling-pricing-suffolk-county — REBUILT 2026-10-18 (20 Q&A headings + 9 FAQ)
1. Why does our Suffolk quote show the same drop at one price but a higher total for the warehouse side? — §9 A
2. What exactly is the 1.20 Suffolk factor paying for? — §9 A
3. A contractor from Nassau quoted less. How do we compare the two quotes fairly? — §9 A
4. Are ferry and barrier-island jobs priced the same as the mainland? — §9 A
5. Our Hauppauge bay was split off a bigger building. How is the old cable above the ceiling priced? — §9 B
6. Our warehouse ceiling is over 17 feet. How does height change what we pay? — §9 B
7. The Melville landlord sent a cabling rulebook. Will following it cost us more? — §9 B
8. Our house was built around 1970, with a finished basement and a low attic. Which route costs less? — §9 B
9. Can one quote cover the office, tasting room and barn on a North Fork property? — §9 B
10. Our South Shore house was raised after Sandy. Where can the panel and cable go? — §9 B
11. A building near the Ronkonkoma station still has open walls. What are we paying for at this stage? — §9 B
12. Does Suffolk's 8¾% sales tax get added to a cabling invoice? — §9 C
13. We are a school district or a village. Why is our cabling priced on a different basis? — §9 C
14. What do we receive at the end that the next contractor can use? — §9 C
15. We expect to grow in two years. What should we pay for now so we do not pay twice? — §9 D
16. Can we split the work — cable this year, cameras and Wi-Fi later? — §9 D
17. Is it cheaper to repair our existing cable or replace it? — §9 D
18. Our Route 58 store is one long room. At what point does the length start to cost money? — §9 E
19. Our office is near the water on one of the forks. Does salt air change the cable or the price? — §9 E
20. The lease says we must remove our cabling when we leave. What will that cost? — §9 E
F1. What deposit books a Suffolk cabling crew? — §17
F2. Can we get a budget figure from a floor plan and photos before anyone visits? — §17
F3. Is the Suffolk price list the same for homes as for businesses? — §17
F4. Can you price cable for a camera system we already bought? — §17
F5. What happens to the price if we add drops halfway through the job? — §17
F6. Is financing available for a larger Suffolk cabling project? — §17
F7. Can you price cabling for a building we have not leased or bought yet? — §17
F8. Will you work out the drop locations with our IT company and phone vendor? — §17
F9. Can you reuse the jacks and wall plates already in our walls? — §17

Intents deliberately not asked on this page (answered on the main page or as body text only): per-drop cost, Cat6 vs Cat6A, minimum job, volume discounts, plenum requirement, certification contents, fiber cost, after-hours, start time, permits, licensing, job duration.
