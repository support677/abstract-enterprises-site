# Research — Door Buzzer Repair silo

Created 2026-10-22 by the scheduled batch run (first REBUILD pages in this silo). Every entry: exact query · platform · URL · finding · page+section used. Unreachable sources are marked EMPTY (not accessible in build env). Each page section carries its own Question register.

## Silo-wide (door buzzer repair)

Written 2026-10-22 by the Bed-Stuy agent of the Door Buzzer Repair REBUILD batch (Bed-Stuy / Belmont / Beverley Square). There is no `research/door-buzzer-repair.md` yet; this section is the silo-level layer to seed it. Where a finding was carried from an earlier research file it is marked "carried" with its original ID.

### Five-layer source status
| Layer / source | Status | Notes |
|---|---|---|
| Google PAA | EMPTY (not accessible in build env) | — |
| Google PASF | EMPTY (not accessible in build env) | — |
| Answer the Public | EMPTY (not accessible in build env) | — |
| Google AI Overview | EMPTY (not accessible in build env) | Page §10.5 says so explicitly and tests claims from cost guides / vendor pages instead (below) |
| Bing / DuckDuckGo | EMPTY (not accessible in build env) | — |
| Yelp 1–3★ | EMPTY (not accessible in build env) | carried: intercom-repair.md row 11 (Yelp list pages only, no review text) |
| Keyword volumes | EMPTY — Ahrefs `keywords-explorer-matching-terms` (keywords "buzzer repair,intercom repair,door buzzer", US) returned `Insufficient plan` | Keyword layers below are built from research, not volumes |
| Reddit | Partial (search excerpts only; threads not opened) | see S-R rows |

### Silo sources
| # | Exact query · platform | URL | Finding | Page + section used (Bed-Stuy) |
|---|---|---|---|---|
| S-R1 | `site:reddit.com Bed Stuy buzzer OR intercom apartment building door` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/1t74q1e/is_no_buzzer_and_one_mailbox_for_3_apartments/ | Thread "Is no buzzer and one mailbox for 3 apartments, normal for Brooklyn"; reply excerpt: "I also do not have a buzzer in my building. I'm in BedStuy and have heard of quite a bit of this in Ridgewood too." | §5 para 3; §9 H3 "three-apartment house with no buzzer"; Sources |
| S-R2 | same | https://www.reddit.com/r/AskNYC/comments/1ocj4l7/need_freelowcost_housing_lawyer_brooklyn/ | Brooklyn rent-stabilized building, 120 open HPD violations: "Broken intercom/buzzer (non-functional since 2023) · … Broken front door" (excerpt; neighborhood not stated) | Background only (not on page) |
| S-R3 | same | https://www.reddit.com/r/AskNYC/comments/190ywaa/ | Ground-floor tenants become "the door buzzer" for packages (excerpt) | Background only |
| S-R4 | carried intercom-repair.md R1/R3 | https://www.reddit.com/r/AskNYC/comments/10uzqs0/ ; https://www.reddit.com/r/AskNYC/comments/17knzko/ | Residents' advice: call 311 / file a complaint | §9 tenant framing (not quoted) |
| S-G1 | `nyc.gov HPD owner responsibilities intercom self-closing doors entrance door lock requirements multiple dwelling` · WebSearch → Firecrawl gov search excerpt | https://ag.ny.gov/sites/default/files/tenants_rights.pdf (also nyc.gov/assets/buildings/pdf/tenants_rights.pdf) | AG Tenants' Rights Guide: post-1/1/1968 multiple dwellings "must have automatic self-closing and self-locking doors at all entrances"; 8+ apartments also two-way voice intercom with buzz-open; pre-1968 "also must have self-locking doors and a two-way intercom system if requested by a majority of all the apartments"; landlords may recover cost (MDL § 50-a) | §8.5 bullet 1; "1968 line" section; §9 H3 1899 walk-up; SVG MDL table; §10.5 H3 2 |
| S-G2 | WebFetch | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | Defective self-closing door = "a class C immediately hazardous violation"; correct within 14 days of NOV receipt; HPD reinspects within 20 days of correction date; Local Law 71 of 2022 = 300 class A MDs/year proactive inspections; HMC § 27-2041.1 | "Door has to close" section; §8.5 bullet 2; SVG HPD clock |
| S-G3 | WebFetch | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/abcs-of-housing-owners.pdf | ABCs of Housing does NOT address intercoms/entrance doors (only "Provide and maintain security measures… good lighting") | Not used (negative finding) |
| S-G4 | Firecrawl gov search `NYC Housing Maintenance Code 27-2005 owner duty maintain intercom "27-2043" locks entrance door` | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-60477 | HMC § 27-2043: key lock + heavy-duty latch/deadbolt + chain on dwelling-unit doors (class A) | Background (not on page) |
| S-G5 | WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Staff can permit intercom panels "within or adjacent to a door opening", or on a fence/wall in front of the entranceway; max one intercom panel per door opening; compatible design; not through cast iron or decorative surfaces; ordinary maintenance/repair needs no permit; new gate under stoop staff-level, replacing an existing historic gate not staff-level | §7.5 areaway; §8.5 bullet 3; §9 H3 areaway gate; §10.5 H3 4; SVG LPC |
| S-G6 | carried intercom-repair.md G5 | https://portal.311.nyc.gov/article/?kanumber=KA-01074 | 311 Apartment Maintenance complaint covers "Doorbells, buzzers, or intercoms that are broken or missing" | SVG process (311 step) |
| S-G7 | carried door-buzzer-installation.md S4 | https://up.codes/s/sensor-release-of-electrically-locked-egress-doors | IBC sensor-release / maglock egress conditions | §8.5 bullet 5 |
| S-G8 | carried door-buzzer-installation.md S11 | https://www.access-board.gov/ada/chapter/ch03/ | 2010 ADA high forward reach 48 in max | §8.5 bullet 6 |
| S-G9 | carried intercom-repair.md G7 | https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-electrical.page | Line-voltage work needs licensed electrician + permit | §8.5 bullet 4 |
| S-A1 | carried door-buzzer-installation.md S6 | https://us.allegion.com/en/resources/education/leading-the-industry/decoded/fail-safe-vs-fail-secure.html | Fail-safe unlocks on power loss, fail-secure stays locked; with a strike you can always exit by the lever | §10 strikes card |
| S-A2 | carried intercom-repair.md A1 | https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ | "minor repairs typically run $150 to $400" | §10.5 H3 1 |
| S-A3 | carried door-buzzer-installation.md S9 | https://swiftlane.com/blog/apartment-intercom-installation-cost/ | Software "$5 to $15 per unit per month" | §10.5 H3 6 |
| S-A4 | carried intercom-repair.md G2 | https://butterflymx.com/blog/nyc-intercom-law/ | Rule "generally applies to Class A multiple dwellings with eight or more units built or converted after January 1, 1968"; older "require closer review" | §10.5 H3 2 |
| S-A5 | carried door-buzzer-installation.md S10 | https://butterflymx.com/blog/apartment-call-box/ | Intercom "requires no building wiring" | §10.5 H3 6 |
| S-A6 | carried door-buzzer-installation.md S8 | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/ | Installation national average $2,500 | §10.5 H3 3 |
| S-B1 | `Bedford-Stuyvesant brownstone buzzer intercom broken landlord` · WebSearch → WebFetch | https://www.brownstoner.com/forum-archive/2007/10/electric-door-s | 10/29/2007: brownstone 3′×10′ glazed double doors, told "no system to accomodate a buzzer"; BKRed routed wiring behind the astragal, drilled door nearest wall | §5 para 3; Sources |
| S-B2 | same → WebFetch | https://www.brownstoner.com/forum-archive/2009/09/intercome-probl/?cpage=2 | 9/14/2009 Park Slope brownstone: 11 of 12 intercoms replaced, 12th tenant refused access → whole line down; door propped | "Bell wire" section para 3 (labelled Park Slope) |
| S-B3 | same → WebFetch | https://www.brownstoner.com/forum/about-brooklyn/intercom-for-a-three-family | User "bedstuyreno" (~2012, date inferred from "11 years 11 months ago"): wants "a basic buzzer and intercom" in each unit of a 3-family brownstone; reply suggests Aiphone | §5 para 3 ("around 2012") |

### HPD / 311 categories (silo level, verified for Brooklyn)
- HPD violations dataset wvxf-dwi5 writes buzzer faults under **§ 27-2005 HMC** with wording like "PROPERLY REPAIR OR REPLACE THE BROKEN OR DEFECTIVE BELL BUZZER INTERCOM SYSTEM FROM THE BUILDING ENTRANCE DOOR TO PANEL…"; classes found A, B and C (not only B — see FLAG on the Brooklyn hub).
- 311 dataset erm2-nwe9: complaint_type `GENERAL`, descriptor `BELL/BUZZER/INTERCOM` (records from 2020); `DOOR/WINDOW` › `DOOR`, `DOOR FRAME` also common.
- Self-closing door violations cite § 27-2005, 27-2007, 27-2041.1 HMC, MDL §§ 238/309/107(2)(c), 28 RCNY § 25-171.

### Keyword plan (five layers, silo — from research, no volumes)
- **Service:** door buzzer repair, buzzer repair, apartment buzzer repair, intercom and buzzer repair, electric strike repair, door release repair, buzzer transformer replacement, apartment station/handset replacement, lobby panel repair, bell wire repair, door closer adjustment.
- **Problem:** buzzer works but door won't open, strike hums, door won't latch, vestibule door won't close, one apartment dead, bells crossed, all buttons weak, door unlocked all day (welded relay), renovation cut the wire, HPD intercom violation, self-closing door violation, kick-stand/propped door, no buzzer in a three-family.
- **Technology:** fail-secure/fail-safe electric strike, keeper, flush bolts, astragal, door closer sweep/latch speed, bell transformer (16–24 V), push buttons, handsets, relay/door-release module, maglock + REX, app/IP intercom panel, admin account.
- **Industry:** owner-occupied two-family, three-/four-family rentals, walk-ups/French flats, co-ops/condos, mixed-use store buildings, churches/schools, managing agents, out-of-state owners, NYCHA (refer to NYCHA).
- **Geographic:** per page.

## Bedford-Stuyvesant, Brooklyn — /door-buzzer-repair-bedford-stuyvesant-brooklyn-ny (REBUILD, 2026-10-22)

Neighborhood page; up-link `/door-buzzer-repair-brooklyn-new-york`; GBP Brooklyn (1282 Troy Ave, `@id` #brooklyn); direct (347) 934-8335 in body/CTAs/schema; (800) 486-0943 only in shared mega-nav; WhatsApp only wa.me/17186790359 (+ footer text). Prices: Brooklyn ×1.00 from `door-buzzer-repair-brooklyn-new-york` table, consistent with `door-buzzer-repair-pricing` ($250 service call that applies toward bigger jobs).

**Thesis:** "The buzzer and the door it opens": a Bed-Stuy entrance is a chain never designed as one system — button/handset → bell wire through an 1870s–1910s rowhouse later split into 2–4 apartments → cellar transformer → strike in an old double-leaf or vestibule door → closer/latch. Built on the two-door brownstone entrance (LPC report), PLUTO conversions, HPD's CB3 record (2,040 intercom violations, 2nd in Brooklyn; 12,965 self-closing-door violations, 9,087 Class C), 311 (1,956 bell/buzzer/intercom complaints since 2020, 1st in Brooklyn) and the MDL 1968 line (≈82% of residential lots pre-1968). Distinct from the alarm Bed-Stuy page (alarms) and door-buzzer-installation pages (new systems) and from the separate `door-buzzer-repair-stuyvesant-heights-brooklyn-ny` page (linked, district covered only as part of Bed-Stuy).

**Boundaries:** Wikipedia — Flushing Ave (N), Classon Ave (W), Broadway (E), Atlantic Ave (S); 79th Pct (263 Tompkins Ave) west of Marcus Garvey Blvd, 81st Pct (30 Ralph Ave) east. Data queries use Brooklyn CB 3 / CD 303, which is close to but not exactly the neighborhood (includes slivers of Ocean Hill and Clinton Hill NTAs — stated on page).

### Local sources
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| L1 | SoQL `$select=class,violationstatus,count(*)&$where=novdescription like '%INTERCOM%' AND boro='BROOKLYN' AND communityboard='3'` · Firecrawl scrape (NYC Open Data wvxf-dwi5) | https://data.cityofnewyork.us/resource/wvxf-dwi5.json | A closed 332 / open 113; B closed 1,141 / open 446; C closed 7 / open 1 → 2,040 total, 560 open | §5 para 4; §5.5 bullet 1; §9 H3 Class A/B; SVGs |
| L2 | same dataset, group by communityboard (Brooklyn) | same | CB17 2,224; CB3 2,040; CB8 1,878; CB14 1,865; CB9 1,773; CB5 1,260; CB4 1,121; CB16 957 … | §5 para 4; SVG CB |
| L3 | same, group by year of inspectiondate | same | 1989–2004 total 64; 2005 28 … 2013 110, 2017 130, 2019 135, 2025 139 (max), 2026 94 (to Oct 22) | §5.5 bullet 1; SVG years |
| L4 | same, group by nta | same | Bed-Stuy (East) 1,083; (West) 930; Ocean Hill 19; Clinton Hill 8 | §5 para 6; SVG NTA |
| L5 | same, group by streetname (top 15) | same | Fulton St 114, Gates Ave 92, Madison St 92, Quincy 89, Jefferson Ave 85, Putnam Ave 81, Tompkins Ave 76, Herkimer 75, Monroe 74, MacDonough 74, Lafayette 69, Greene 62, Chauncey 59, Halsey 57, Throop 54 | §5 para 6; §8 Fulton/Tompkins cards; SVG streets |
| L6 | same, 3 most recent records | same | e.g. Kosciuszko St Oct 13 2026 Class B "BELL BUZZER INTERCOM SYSTEM FROM THE BUILDING ENTRANCE DOOR TO PANEL…"; Vernon Ave Oct 16 Class A at one apartment (addresses not named on page) | "1968 line" para 2 (wording); §9 Class A/B H3 |
| L7 | `novdescription like '%SELF-CLOSING%'` CB3 by class/status | same | A 162/32; B 2,693/991; C 7,191/1,896 → 12,965 total, 9,087 Class C, 2,919 open | §5 para 4; "Door has to close" section; SVGs |
| L8 | same, 4 most recent Class C | same | Oct 20 2026 Bed-Stuy (West): "REMOVE DEVICE PREVENTING DOOR FROM BEING SELF-CLOSING KICK STAND AT VESTIBULE DOOR"; Oct 19: latch sets at cellar/boiler-room doors, hinges at an apartment entrance | emergency block; "Door has to close" para 1; §9 vestibule H3 |
| L9 | 311 erm2-nwe9 `community_board='03 BROOKLYN'` descriptor search INTERCOM/BUZZER/DOOR | https://data.cityofnewyork.us/resource/erm2-nwe9.json | DOOR/WINDOW›DOOR 4,950; GENERAL›BELL/BUZZER/INTERCOM 1,956; DOOR FRAME 705 … | §5 para 4 (buzzer count only; DOOR count not used because its period is unclear) |
| L10 | 311 BELL/BUZZER/INTERCOM CB3 by year | same | 2020 196; 2021 297; 2022 271; 2023 299; 2024 317; 2025 312; 2026 264 | §5.5 bullet 2; SVG 311 |
| L11 | 311 BELL/BUZZER/INTERCOM Brooklyn by board | same | CB3 1,956 (1st); CB17 1,858; CB14 1,686; CB9 1,569; CB8 1,408; CB5 1,142; CB4 1,022; CB1 1,007 | §5 para 4; SVG rank |
| L12 | PLUTO 64uk-42ks `cd='303'` group by bldgclass with sum(unitsres) | https://data.cityofnewyork.us/resource/64uk-42ks.json | B3 3,692 (7,384 units); C0 3,429 (10,287); B1 1,468; C1 1,017 (11,203); C3 976; B9 656; C2 630; S2 471; B2 365; A4 321; R1 278 (1,675); C7 163; D1 131 (7,415); D3 38 (8,420); D7 51 (2,758); S1 72, S3 194, S4 79, S5 100, S9 207 | §5 para 3; §5.5 bullet 4; §7 cards; SVG classes/units |
| L13 | PLUTO cd 303, unitsres>0, yearbuilt>0, by era | same | pre-1900 6,605; 1900–30 4,275; 1931–67 1,624; 1968+ 2,710 (15,214) → 82% pre-1968 | §5 para 1; §5.5 bullet 5; SVG 1968 |
| L14 | PLUTO cd 303, unitsres≥8, pre/post 1968 | same | pre 1,003 lots / 21,194 units; post 573 / 18,259 | "1968 line" para 2; §7 newer buildings card; SVG units |
| L15 | `Stuyvesant Heights Historic District designation brownstones limestone rowhouses LPC` · WebSearch → WebFetch | https://www.citylandnyc.org/bed-stuyexpanded-stuyvesant-heights-historic-district-designated-capping-decades-long-process/ | Designated Apr 16 2013 (published Apr 22), unanimous, 20-year process; ~825 buildings; Halsey/Macon N, Fulton S, Malcolm X E, Tompkins W; developed 1880–1920; mid-19th-c. wood-frame houses; 1890s French flats; Bethany Baptist Church | §5.5 bullet 6; §7 wood-frame card; landmarks card; SVG districts |
| L16 | same → WebFetch | https://s-media.nyc.gov/agencies/lpc/lp/2496.pdf | LP-2496: shared first-floor entrance "through a vestibule before entering a hallway…" (p.13); round-headed double-leaf doors (p.17); areaways/raised basements; limestone/brownstone/brick Renaissance Revival (p.19); rough-faced brownstone Queen Anne (p.18); French flats 4–5 stories; 7 Decatur St (1888), 291–293 Stuyvesant Ave (1898); MacDonough St Italianate rows 1872 by Curtis L. North | §5 para 2; §7 cards; two-door section; SVG doors |
| L17 | same search → WebFetch | https://hdc.org/buildings/stuyvesant-heights-historic-district/ | Designated Sept 14 1971; over 430 structures; brick and brownstone | landmarks card (conflict stated) |
| L18 | `Brooklyn Community District 3 … precinct` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Bedford%E2%80%93Stuyvesant,_Brooklyn | Boundaries; 79th/81st Pct; Fulton main shopping street; Nostrand/Bedford/Stuyvesant; Tompkins & Malcolm X edges of Stuyvesant Heights HD; Lewis Ave Macon Library; A/C 1936, G 1937, J/M/Z Broadway, LIRR Nostrand Ave; ~8,800 pre-1900 buildings; Stuyvesant Heights HD 577 contributing buildings/17 blocks; Bedford HD Dec 8 2015; Willoughby–Hart Jun 25 2024 (~50); Alice & Agate Courts Feb 10 2009 (36 Queen Anne row houses); Herbert Von King Park (1857/1871/1985); Boys and Girls HS on Fulton St | §5 para 1; §8 cards; landmarks; SVG districts |
| L19 | WebFetch | https://www.nyc.gov/site/brooklyncb3/resources/nypd-precincts-firehouses.page | 79th & 81st Pcts cover the district; PSA 3 covers NYCHA developments | Sources |
| L20 | `NYCHA developments Bedford-Stuyvesant list …` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Marcy_Houses | Completed 1949; 27 six-story buildings; 1,705 apts; ~4,286 residents; bounded Flushing, Marcy, Nostrand, Myrtle | §7 public housing card; landmarks card |
| L21 | same → WebFetch | https://www.nyc.gov/assets/nycha/downloads/pdf/sumner-factsheet-en.pdf | Built 1958; 13 buildings; 1,088 families; ~2,400 residents; 22 acres | §7 public housing card |
| L22 | `Marcy Houses intercom broken doors NYCHA tenants` · WebSearch → WebFetch | https://comptroller.nyc.gov/reports/observations-of-building-doors-in-nycha-developments | Sept 21 2022: 262 developments; 40.1% entrance locks broken; 36.8% entrance doors open; 28.5%/37.5% rear-side; 23.5% (2018) → 57.9% (2022); no development-level Bed-Stuy results; intercoms only anecdotal | SVG NYCHA; Sources |
| L23 | `Tompkins Houses OR Sumner Houses …` · WebSearch → WebFetch | https://pix11.com/news/local-news/brooklyn/broken-elevator-and-outages-plague-tompkins-houses-in-brooklyn/amp/ | Jan 31 2026 (metadata): Tompkins Houses, 760 Park Ave: elevator out, gas/heat/electric outages (no intercom content) | Sources only |
| L24 | `79th precinct Bed-Stuy burglary apartment building buzzed in followed tenant lobby` · WebSearch → WebFetch | https://www.dnainfo.com/new-york/20160422/bed-stuy/burglar-breaks-into-four-bed-stuy-apartments-police-say | Apr 14 2016 near Willoughby Ave & Broadway: burglar followed a resident into the building, entered four apartments via balcony sliding doors | "Door has to close" para 4 |
| L25 | same → WebFetch | https://patch.com/new-york/bed-stuy/bed-stuy-thief-robs-same-apt-building-twice-3-hours-cops | Published Nov 11 2019 (event Oct 13): near Kosciuszko St & Marcus Garvey Blvd, cellar door entry twice in ~3 hours, >$4,000 | "Door has to close" para 4 |
| L26 | same → WebFetch | https://brooklyn.news12.com/police-2-thieves-wanted-for-string-of-burglaries-in-bed-stuy-building | Oct 25 2023: Bedford Ave building, thieves entered vacant apartment, cut into ground-floor smoke shop (entry route not stated) | Sources only |
| L27 | `Bed-Stuy package theft vestibule front door reddit` · WebSearch → WebFetch | https://brooklyn.news12.com/police-doordasher-steals-package-from-a-bed-stuy-resident | Feb 25 2025 (event Feb 14): Bainbridge St building, package taken from "in front of his door" | Sources only |
| L28 | WebFetch | https://www.cbsnews.com/newyork/news/gilmer-holding-corporation-macdonough-street-apartment-building-violations | 25 MacDonough St, 267 HPD violations since 2018, $2M fine (no intercom content) | Not used |
| L29 | WebFetch | https://caplantech.journalism.cuny.edu/?p=657 | No intercom/door content | Not used |
| L30 | `Bedford-Stuyvesant Restoration Corporation …` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Bedford_Stuyvesant_Restoration_Corporation | Founded Apr 1 1967 (RFK, Lindsay, Javits, Thomas R. Jones); former Sheffield Farms milk-bottling plant bought 1968, restored 1972; Billie Holiday Theatre, Skylight Gallery | landmarks card |
| L31 | HPD violations API via WebFetch | https://data.cityofnewyork.us/resource/wvxf-dwi5.json?… | EMPTY (not accessible in build env — WebFetch permission timeout); same query succeeded via Firecrawl (L1) | — |
| L32 | Bed-Stuy Reddit (r/BedStuy) | — | EMPTY — no r/BedStuy buzzer thread surfaced in search | — |
| L33 | Yelp Bed-Stuy intercom/locksmith 1–3★ | — | EMPTY (not accessible in build env) | — |

### Question register (all questions on the page)
§9 Questions Answered (H3):
1. The outer doors lock but the inner vestibule door does not. Which one should the buzzer release?
2. Can a wooden double-leaf door bind hard enough to stop the release?
3. Our vestibule door swings back open after every visitor. Is that the buzzer or the door?
4. Can the areaway gate under our stoop be buzzed open, or only the garden-floor door?
5. The garden-floor bell rings upstairs instead. How do pairs get crossed in a split brownstone?
6. After one floor was renovated, the other apartments' handsets went dead. What did the contractor cut?
7. Why does every button in our walk-up ring weakly, and the strike barely click?
8. Our walk-up was built in 1899. Can tenants require the owner to put in an intercom?
9. Is a three-apartment house with no buzzer at all unusual in Bed-Stuy?
10. Why did HPD write our dead buzzer as Class A when a neighbor's was Class B?
11. A sign installer drilled through our building's buzzer cable on Fulton Street. How long until the apartments are back?
12. Our new condo's app intercom stopped calling phones after the developer left. Who holds the admin account?

§17 FAQ (= FAQPage schema, 8):
13. Do you need to see our certificate of occupancy before repairing a converted house?
14. The owner of our house lives out of state. Can the repair still go ahead?
15. Will the street door be left unlocked while you work on it?
16. Can you keep our original brass bell buttons when you repair the buzzer?
17. Is cloth-covered bell wire still safe to keep in service?
18. Should we take down the old handsets that no longer work?
19. Do tenants need to be home during a buzzer repair?
20. We are selling our Bed-Stuy house. What should buyers be told about the buzzer?

Near-intent review (kept, different in meaning): #7 vs silo "The whole panel is dead or weak — does that mean the system is finished?" (cause/transformer vs replace decision); #6 vs silo "A whole line of apartments lost the buzzer — what causes that?" and Belmont "The shop below us is renovating its ceiling…" (diagnosis after a renovation cut vs general cause / prevention); #8 vs Belmont "Our building went up after 1968…" (pre-1968 majority request vs post-1968 requirements); #10 vs Belmont "HPD wrote our intercom violation at one apartment…" (class vs location). Replaced during build because they matched batch siblings in meaning: tenant-books-visit, prep-before-visit (Belmont), basement bell at side door, painting over button, porch rebuild (Beverley Square), and heading "Already bought the part?" (exact dup with Belmont).

### Images (11) — source → dest (all under images/door-buzzer-repair/)
| # | Source | Dest (door-buzzer-repair-bedford-stuyvesant-…) | Type |
|---|---|---|---|
| 0 | access-control-installation/…-brighton-beach-brooklyn-axis-white-door-station-with-speaker-grille.webp | white-video-door-station-with-speaker-grille-product-photo.webp | product |
| 1 | intercom-repair/…-staten-island-dome-camera-on-tiled-ceiling-above-glass-entrance.webp | dome-camera-on-tiled-ceiling-above-glass-entrance.webp | real |
| 2 | intercom-repair/…-staten-island-black-akuvox-house-video-door-station-product-photo.webp | black-video-door-station-with-card-and-bell-icons-product-photo.webp | product |
| 3 | intercom-repair/…-putnam-county-slim-black-video-doorbell-with-ring-button.webp | slim-black-video-doorbell-with-lit-ring-button-product-photo.webp | product |
| 4 | intercom-repair/…-putnam-county-dome-camera-and-motion-sensor-in-ceiling-corner.webp | dome-camera-above-motion-sensor-in-white-wall-corner.webp | real |
| 5 | apartment-building-security-camera-installation/…-long-island-recorder-screen-with-camera-tiles-under-cable-runs.webp | recorder-screen-under-exposed-cable-runs.webp | real |
| 6 | apartment-building-security-camera-installation/…-westchester-county-black-bullet-camera-on-ceiling-grid-beside-air-vent.webp | black-bullet-camera-on-drop-ceiling-beside-vent.webp | real |
| 7 | access-control-installation/…-boerum-hill-brooklyn-face-recognition-door-station-screen.webp | touchscreen-face-recognition-door-station-product-photo.webp | product |
| 8 | products/d2.png | four-dome-camera-kit-with-recorder-and-monitor-product-photo.webp | product |
| 9 | products/a4.png | four-dome-camera-kit-with-recorder-product-photo.webp | product |
| 10 | products/f3.png | four-bullet-camera-kit-with-recorder-and-monitor-product-photo.webp | product |
Avg-hash: no pair with another batch page is the same scene (all <45-bit pairs looked at: different products on white backgrounds). Rejected: smart-lock-installation/ and low-voltage/ door-hardware photos (AI renders: branded uniforms, faces); the intercom-repair pool's remaining door stations, stone facade, grey-door corridor and cable-bundle scenes (already used by the Belmont page, which drew on the same pool); turret-above-vestibule (same scene as #1).

### Flags for Anwar
- **Image pool conflict:** the Belmont page took 9–10 scenes from `images/intercom-repair/` (assigned to Bed-Stuy). Bed-Stuy therefore uses only 4 intercom-repair scenes, 2 access-control product photos, 2 apartment-building camera photos and 3 `images/products/` camera-kit product photos. Only 4 of 11 are real job photos and 4 show cameras rather than entry hardware. **Real door-buzzer photos (strikes, closers, vestibule doors, transformers, panels) are urgently needed.**
- **check_page quirk:** silo detection returns `door` (no `door-buzzer-repair-brooklyn.html` exists; the hub is `-brooklyn-new-york`), so the tool demands an up-link to `/door-brooklyn` and compares against all 151 `door-*` pages. The page links up to `/door-buzzer-repair-brooklyn-new-york`. Needs a tool fix or an alias, not a page change.
- **Hub conflict:** the Brooklyn hub says "HPD treats a dead intercom as a Class B hazardous violation, with civil penalties in the range of $250 to $500 per day"; HPD's CB3 data shows Class A (445) and Class C (8) as well as B (1,587). The page states the data; the penalty range was not verified and is not used.
- **Pricing:** Brooklyn ×1.00 from the hub table; pricing page agrees on the $250 service call (applies toward bigger jobs) but has no component table. No BYOE labor figure exists in this silo → "quoted at the diagnosis". The blueprint's $195/hr callback rate is not used (silo uses the $250 service call). Packages are three patterns built from existing list lines, no new numbers.
- **Source conflicts stated on page:** Stuyvesant Heights HD size (HDC "over 430 structures" vs Wikipedia "577 contributing residential buildings, 17 blocks"); Wikipedia ~8,800 pre-1900 buildings vs PLUTO 6,605 pre-1900 residential lots (different units/areas); CB3 vs neighborhood boundaries.
- **AESS practice claims to confirm:** same-day arrival when called before noon; most single faults fixed in one visit of an hour or two; unlockable doors first on the day's list and secured before leaving if a part is missing; photo review free; COI before the visit; tenant calls need owner approval; door test before wiring; label every pair at both ends and leave a written pair map / hand-over note; disconnect retired stations; fit customer-supplied parts with labor quoted at diagnosis; never bypass maglock egress releases; send photos/findings to out-of-state owners; owner can approve remotely and pay the $250 online; low-voltage only (line voltage by licensed electrician).

## Belmont, Bronx — /door-buzzer-repair-belmont-bronx-ny (REBUILD, 2026-10-22)

Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, #bronx) · up /door-buzzer-repair-bronx-new-york · prices Bronx x1.00 from hub + /door-buzzer-repair-pricing.

### Sources (exact query · platform · URL · finding · page+section used)
| # | Query | Platform | URL | Finding | Used |
|---|---|---|---|---|---|
| L1 | `Belmont Bronx Arthur Avenue Little Italy history tenements` | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Belmont,_Bronx | Bounds Fordham Rd / Bronx Park / E 181st / Third Ave; 5–6-story walk-up & elevator bldgs, most pre-1939, Art Deco/Tudor; CB6; 48th Pct 450 Cross Bronx Expwy; Engine 88/Ladder 38 2223 Belmont Ave; ZIPs 10457/10458/10460; Mount Carmel 1906; Belmont Library/Fermi 610 E 186th 1981; Fordham 1841; St. Barnabas; restoration boom mid-1990s | Neighborhood §5; Coverage; Q&A 1968; Sources |
| L2 | `NYC multiple dwelling … intercommunication system …` | WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/MDW/50-A (+ research/intercom-repair.md G1 for pre-1968 clause) | Post-1/1/1968 class A: self-closing/self-locking doors; 8+ apts intercom w/ voice + release; older: on majority tenant request/consent | §8.5 rules; Q&A 1968 + three-family; AI H3 4; SVG 'law' |
| L3 | `NYC Housing Maintenance Code intercom self-closing …` | WebSearch → WebFetch | https://nycadmincode.readthedocs.io/t27/c02/sch02/art11/index.html | 27-2041 peephole, 27-2043 locks/chain, 27-2044 self-closing in old-law tenements; no intercom text in that article | Background only (not cited on page) |
| L4 | same | WebFetch | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | Apartment entrance & public hall doors must self-close/latch; defect = Class C, 14 days; Local Law 71/2022 | §8.5; Q&A wedging; SVG 'classbc' |
| L5 | SoQL on HPD violations (wvxf-dwi5), NTA='Belmont', novdescription like %INTERCOM% | Firecrawl scrape of data.cityofnewyork.us API (WebFetch blocked: PROVENANCE_REQUIRED) | https://data.cityofnewyork.us/resource/wvxf-dwi5.json | All-time 897 (235 open/662 closed); 2021-01-01→2026-10-22: 475 at 170 bldgs; 447 'LOCATED AT APT'; 269 also BELL/BUZZER; by year 55/68/67/98/100/87; class B 395, A 67, C 13; status dismissed 158, closed 134, NOV sent 108, not complied 38, first no access 23, other 14; months 33–50 (flat); streets (Washington 47/8, E 187 44/17, Webster 41/13, Hoffman 37/8, Park 31/11, Beaumont 29/11, E 189 27/9, Cambreleng 20/7, Crotona 19/12, Prospect 19/6, Belmont Ave 18/4, Southern Blvd 11/5, Hughes 10/7); rooms: foyer 197, hall 58, kitchen 47, 'entire apartment' 24; Bronx rank 3rd (Concourse-Concourse Village 587, Univ Hts S–Morris Hts 499) | Hero; §5.5; thesis; Q&A; Field Notes; AI; 15+ SVGs |
| L6 | same dataset, LOCK + (BUILDING ENTRANCE DOOR / VESTIBULE); POWER OUTAGE; SELF-CLOSING | Firecrawl API | same | 868 entrance/vestibule lock violations at 209 bldgs; 84 mention power outage, 57 of them 'mechanical' lock; 5,049 self-closing at 456 bldgs, 3,265 with no 'APT' in text | §5.5; §8.5; Q&A doors; SVG 'doors','outage' |
| L7 | SoQL 311 (erm2-nwe9) descriptor BELL/BUZZER/INTERCOM by ZIP/year/dow/hour | Firecrawl API | https://data.cityofnewyork.us/resource/erm2-nwe9.json | 10458: 319/251/367/358/259 (2022–2026 YTD); 10457: 154/223/282/251/254; 10460: 142/141/180/163/143; 10458 since 2023 by DOW Sun105 Mon220 Tue224 Wed211 Thu204 Fri177 Sat94; by hour peak 9a–4p + 108 in 10 p.m. hour (n=1,235) | §5.5; SVGs z311, zips, zipyears, dow, hours |
| L8 | SoQL PLUTO (64uk-42ks) cd=206 & zipcode=10458 | Firecrawl API | https://data.cityofnewyork.us/resource/64uk-42ks.json | 1,042 res lots / 9,813 units; 3+ unit lots 662: pre-1901 4, 1901–29 386, 1930–39 114, 1940–67 5, 1968+ 153 (units 31/5,492/1,167/196/2,229); size 1–2:380, 3–7:314, 8–19:186, 20–49:137, 50+:25 (8+ = 348 lots, 7,963 units, 284 pre-1940); C1 228/4,001 u/4.3 fl; C7 96/1,641/4.6; C0 210; B 263 lots; D1 18/1,104/8.1 fl; D7 10/508 | §5, §7 cards/methods; Q&A 1968/three-family; SVGs eras, classes, floors, sizes, agesize, eraunits |
| L9 | `Belmont Bronx buzzer intercom broken lobby door tenants HPD` | WebSearch → WebFetch | https://www.openigloo.com/building/nyc/2012562-2030910003/bronx-belmont-655-east-189-street-10458 ; …2381-belmont-avenue… | Tenant reviews: "front door is always broken…" (1912, 27 units); "lobby door is broken…" | Background only (not on page) |
| L10 | same | WebFetch | https://bronx.news12.com/belmont-landlord-fined-10-million-after-years-of-tenant-neglect ; https://bronx.news12.com/tenants-of-belmont-building-complain-of-horrible-apartment-conditions | 480 E 188th St $10M fine (Jul 2025) – elevator/heat, no doors/intercom; 2024 conditions story – no doors/intercom | Not used (off-topic) |
| L11 | `reddit Belmont Bronx apartment buzzer front door package stolen Arthur Avenue` + `48th precinct Belmont…` | WebSearch → WebFetch | https://hoodline.com/2026/07/four-armed-men-storm-belmont-home-hold-bronx-family-at-gunpoint/ ; https://bronx.news12.com/police-suspect-wanted-for-belmont-apartment-burglary-38284378 | Jul 2026 home invasion near Washington Ave/E 185th, door kicked (Ring video via News 12); 2018 burglary, no detail | Not used (no buzzer link; avoided sensational) |
| L12 | `Arthur Avenue Retail Market opened 1940 La Guardia pushcart Belmont` | WebSearch → WebFetch | https://citylore.org/?p=21335 ; https://w1.planning.org/greatplaces/streets/2016/arthuravenue/ | Market opened Oct 29, 1940, 117 stalls, La Guardia; merchants' co-op 1980s; APA 2016 Great Street 184th–187th, "all buildings are mixed use" | §5; §8 cards; Coverage |
| L13 | `Belmont Business Improvement District Arthur Avenue East 187th Street businesses count` | WebSearch → WebFetch | https://bronxlittleitaly.com/wp-content/uploads/2025/12/Belmont-BID-Fact-Sheet-2025.pdf | BID boundaries (E Fordham Rd Southern Blvd–Lorillard Pl; Arthur Ave Fordham–E 183rd; E 187th Southern–Lorillard; Crescent Ave E 187th–Arthur); Zoo/NYBG construction 1898; Snuff Mill; Lorillard mansion → St. Barnabas | §8; Coverage; SVG map |
| L14 | `Fordham students off-campus apartments Belmont …` | WebSearch → WebFetch | https://thefordhamram.com/news/fordham-off-campus-housing-guide | Apr 9, 2025: student triangle Third/Crescent/Cambreleng; 6 realty cos; "students graduate… leave at the same time"; $900–$1,200/mo | §5; Q&A Fordham calendar; SVG reset |
| L15 | `intercom repair cost apartment buzzer repair average price Angi OR Fixr OR HomeGuide` | Firecrawl search (excerpts) | https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ ; https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/ | Swiftlane: minor repairs $150–$400, small-bldg replacement ~$2,200–$5,000; ButterflyMX: ~$1,500–$2,500 | AI reality check H3 2; SVG vs |
| L16 | (reused) research/intercom-repair.md A1 / door-buzzer-installation.md S8 | — | https://www.homeadvisor.com/cost/safety-and-security/install-intercom-system/ | Intercom install avg $2,500, $1,500–$15,000 | AI H3 1; SVG vs |
| L17 | (reused) research/intercom-repair.md G5 | — | https://portal.311.nyc.gov/article/?kanumber=KA-01074 | 311 apartment maintenance covers broken/missing doorbells, buzzers, intercoms | SVG flow caption |
| L18 | site:reddit.com Belmont Bronx buzzer/intercom/front door | Firecrawl search | — | Nothing local | EMPTY |
| — | Google PAA / PASF / AnswerThePublic / AI Overview / Bing / DDG / Yelp 1–3★ | — | — | EMPTY (not accessible in build env); AI section quotes HomeAdvisor/Swiftlane/ButterflyMX instead and says so on the page |

### Thesis
"The broken buzzer is usually upstairs": 447 of 475 HPD intercom violations in Belmont (2021–Oct 22, 2026) are located at an apartment (foyer 197, kitchen 47), in a neighborhood where ~75% of 3+ unit buildings are 1901–1939 walk-ups (many with stores below, C7) → diagnose from the quiet apartment outward (handset → wall run → floor splice/riser → cellar supply/panel/strike), price only the failed part; plus door/lock/power-outage orders (868 / 57), storefront ceiling cable routes, Fordham-calendar turnover reset. Distinct from Bed-Stuy/Beverley Square (Brooklyn) and from the old Fordham/East Tremont templates.

### Boundaries / flags
- HPD NTA "Belmont" extends west of Third Ave (Webster/Washington/Park Ave) — larger than Wikipedia's Belmont; stated on page (Sources + Commercial card).
- ZIP 10458 also covers Fordham/Bedford Park; stated on page. PLUTO year-built partly estimated; stated.
- Hub claim "HPD … penalties $250 to $500 per day" NOT used (unverified) — flag for Anwar.
- Pricing page vs hub: no conflict (pricing page only lists the $250 service call; hub has the Bronx ranges + 8.875% tax → $272.19).
- check_page.py identify(): silo resolves to "door" (no door-buzzer-repair-bronx.html; hub is -bronx-new-york) → false "no link up to parent hub /door-bronx". Page links /door-buzzer-repair-bronx-new-york. Same on Bed-Stuy ("/door-brooklyn").
- _redirects: only the 301! rule exists (line ~2265); 200 rule missing (main run wiring). sitemap entry exists (lastmod 2026-05-03, priority 0.5).

### AESS practice claims to confirm (Anwar)
Hours 7 days 8am–8pm (from model schema); "most single faults fixed in one visit of one to two hours"; same-business-day text reply with likely fault + range; door-open calls moved to front of day; labeling of riser/terminal strips + written apartment-by-apartment note; relocating kitchen stations via surface raceway; fitting customer-supplied parts on the $250 call when a simple swap (warranty only AESS-supplied); how a second trip for an ordered part is billed (FAQ says "we tell you before we leave"); building-wide station audit offering; extra chime/second station; scheduling around store hours / early starts.

### Question register
Q&A (section 9, H3):
- Need a Buzzer Fixed in Belmont Today?
- HPD wrote our intercom violation at one apartment, not at the lobby. What does that tell the technician?
- My handset rings, but the door button on it does nothing, while my neighbor’s opens the door fine. What failed?
- Our handset hangs on the kitchen wall beside the stove. Should a replacement go in the same spot?
- Past repairs left our building with handsets from three different makers. Will a new one work on the old wiring?
- The vestibule lock was changed last month and now buzzing does nothing. How can a new lock stop the buzzer?
- An HPD order says to provide a mechanical lock “in the event of a power outage.” What has to change at our door?
- People keep wedging the lobby door because the buzzer is dead. What does that cost the building beyond the repair?
- Our building went up after 1968. Does that change what must be at the front door?
- We own a three-family house on a Belmont side street. Do the apartment-building intercom rules reach us?
- HPD marked our reinspection “no access.” Can a dead buzzer be the reason, and how is the next visit handled?
- The shop below us is renovating its ceiling. Could that cut our building’s buzzer, and how do we protect it?
- Our lease cycle follows the Fordham calendar. What should be reset at the door system when one group moves out and the next moves in?
- Can the repair happen during store hours on Arthur Avenue without blocking the shop entrance?
- Most of our handsets still work but are original. Is replacing just the dead ones a false economy?
- How is a repair priced when the fault turns out to be in the wall between two floors?
FAQ (accordion = FAQPage schema):
- What does replacing one apartment’s handset in a Belmont walk-up cost?
- Can a tenant book the visit for their own apartment, or does the owner have to?
- Is the $250 charged again if a part has to be ordered for a second trip?
- Can you test every apartment’s station in one visit and give the owner a written list?
- Will you mark the riser and terminal strips so the next repair is quicker?
- Do you repair the lobby door closer and lock too, or only the electronics?
- What should the super have ready before we arrive at a Belmont building?
- Is a cellular or app-based panel worth considering for a five-story walk-up with old wiring?
- Can a second ringer be added in a back bedroom where the handset can’t be heard?
- Can the street panel show a code instead of a tenant’s name?
- How long does a typical one-apartment repair take?
- Can you work in the evening when tenants are home to let us in?
### Images (11, permanent image rule; none taken in Belmont, captions say so)
- door-buzzer-installation/door-buzzer-installation-ulster-county-indoor-answering-monitor.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-white-apartment-answering-screen.webp (456, 456)
- door-buzzer-installation/door-buzzer-installation-ulster-county-keypad-entry-panel-with-camera.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-keypad-door-station-with-camera.webp (803, 1429)
- door-buzzer-installation/door-buzzer-installation-ulster-county-touchscreen-directory-entry-panel.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-touchscreen-tenant-directory-panel.webp (456, 456)
- door-buzzer-installation/door-buzzer-installation-ulster-county-single-button-video-door-station.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-single-button-video-door-station.webp (423, 562)
- door-buzzer-installation/door-buzzer-installation-ulster-county-narrow-video-intercom-for-door-frame.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-narrow-black-door-frame-intercom.webp (675, 900)
- door-buzzer-installation/door-buzzer-installation-ulster-county-camera-covering-corridor-to-service-door.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-back-hall-toward-grey-steel-door.webp (640, 905)
- access-control-installation/access-control-installation-clason-point-bronx-job-photo-stone-facade-camera-on-steel-arm.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-stone-facade-with-steel-wall-arm.webp (228, 368)
- access-control-installation/access-control-installation-edenwald-blue-and-white-cables-above-equipment-rack.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-cable-bundles-above-equipment-rack.webp (560, 285)
- access-control-installation/access-control-installation-pelham-parkway-directory-panel-for-a-courtyard-arch.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-dark-keypad-station-with-screen.webp (456, 456)
- access-control-installation/access-control-installation-edenwald-white-doorbell-mounting-backplate.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-white-door-station-mounting-plate.webp (500, 500)
- access-control-installation/access-control-installation-pelham-parkway-single-button-lobby-door-station.webp -> images/door-buzzer-repair/door-buzzer-repair-belmont-audio-door-station-with-call-button.webp (456, 456)- Avg-hash (16x16) vs the 22 Bed-Stuy/Beverley Square files: low-distance pairs were all white-background product photos of different products (checked visually) — no shared scene. Mine: audio station vs single-button video station = different products (12 bits, visually distinct).
- Page also carries 43 inline SVG charts/diagrams built only from the data above (not counted as words).

## Beverley Square, Brooklyn — /door-buzzer-repair-beverley-square-brooklyn-ny (REBUILD, 2026-10-22)

Up: /door-buzzer-repair-brooklyn-new-york · phone (347) 934-8335 · GBP Brooklyn (#brooklyn, 1282 Troy Ave) · prices Brooklyn x1.00 (hub ranges + pricing-page $250 service call).

### Thesis
Two trades in one neighborhood: (1) ~210 interior lots of freestanding 1894–1910 wood houses with porches, side doors and cellars, many now two or three units (bells, chimes, transformers, crossed circuits, porch-door strikes, LPC rules in the new Beverley Square West Historic District, ADU/basement units needing their own bell); (2) six-story pre-war elevator buildings and store-and-apartment buildings on the Beverley Road / Cortelyou Road edges, where almost all HPD intercom (67) and self-closing door (290) violations on these lots are written. Multiple Dwelling Law thresholds (3+ families; §50-a pre-1968 majority request) separate the two.

### Boundaries
Beverley Road (N) to Cortelyou Road (S); West = Argyle Rd (some say Stratford Rd) to the Q cut; East = Q cut (Marlborough Rd / E 16th St) to E 19th St. Study area for data: interior lots on Argyle, Rugby, Marlborough Rds and E 16th–19th Sts between the two roads, plus lots fronting Beverley/Cortelyou between the Westminster/Argyle midline and E 19th St (+0.0005° lon). 283 lots, 1,146 homes.

### Sources
| Exact query | Platform | URL | Finding | Page + section |
|---|---|---|---|---|
| Beverley Square East West Brooklyn neighborhood history boundaries | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Beverley_Squares | boundaries, Q cut between Marlborough & E16, Ackerson, 1898 E 19th St, 1901 Lott farm, styles, Q stations, PS 139, CB14, LPC designation 11/25/2025, 118 houses | Hero, Neighborhood, Landmarks, Sources |
| Beverley Square West historic district LPC Flatbush Victorian | WebSearch → WebFetch | https://www.6sqft.com/victorian-flatbush-gains-two-new-historic-districts/ | vote 11/25/2025, 118 houses 1894–1910, Argyle/Rugby/Marlborough, architects Petit/Slee/Driesler, ADU guidelines (basements, cellars, attics; no new backyard homes) | LPC section, Units, FAQ |
| (same) | WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/proposed_landmarks/Beverley_Square_West_Historic_District_proposed.pdf | calendared 6/17/2025, hearing 10/21/2025; 118 and 119 houses; architects A. White Pierce, Petit, Driesler; former Voorhies farm 1901 | Neighborhood, Sources (conflicts) |
| (same) | WebFetch | https://www.cbsnews.com/amp/newyork/news/victorian-flatbush-landmark | 12/4/2025; Westminster & Stratford excluded; residents' fears of development; Cortelyou Rd single-family converted | Neighborhood, LPC |
| (same) | WebFetch | https://www.brownstoner.com/architecture/flatbush-historic-districts-hearing-landmarks-lpc/ | hearing 10/21/2025, 119 houses, 35 for/3 against, open porches, double porches on Westminster | Neighborhood, LPC |
| ditmasparkcorner Beverley Square West association house tour | WebSearch → WebFetch | https://www.brooklynpaper.com/brooklyn-landmarking-slowdown-2025-flatbush-historic-districts | only new Brooklyn districts 2025; LPC staff on boundaries | Sources |
| (BK Reader) | WebFetch | https://www.bkreader.com/neighborhood/beverley-squares-beverley-square-east-beverley-square-west/neighborhood-profile-beverley-squares-8050376 | Cortelyou Rd main shopping corridor; Church/Flatbush/Newkirk nearby | Business |
| LPC rules intercom doorbell historic district permit | WebSearch → WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | intercoms/doorbells staff-level; within/adjacent to door opening; fence/wall in front; one panel per opening; cut sheets; attach to wood/plain masonry/mortar; no permit for maintenance/repair; LPC 212-669-7817 | LPC section, QA, FAQ, diagram |
| Multiple Dwelling Law 50-a intercom … | WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/MDW/50-A | post-1968 8+ apts intercom; pre-1968 on majority written request; 90 days/6 months; misdemeanor | Rules section |
| MDL section 4 definition | WebSearch → WebFetch | https://newyork.public.law/laws/n.y._multiple_dwelling_law_section_4 | multiple dwelling = 3+ families; Class A = permanent residence | Rules section, AI check |
| HPD intercom violation class B … self-closing | WebSearch → WebFetch | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/june-2022-maintenance-bulletin.pdf | LL62/63 of 2022: self-closing doors Class C, 14 days, $250–$500 + $250/day | Rules, HPD, QA |
| nyc.gov HPD intercom … class B | WebSearch → WebFetch | https://LawHelpNY.org/sites/default/files/attachments/HPD%20Violations%20Checklist.pdf | door/lock classes; no intercom entry | Sources |
| HPD violations API (intercom, ZIP 11226) | WebFetch | https://data.cityofnewyork.us/resource/wvxf-dwi5.json?... | EMPTY (not accessible in build env — permission timeout) | — |
| (same via Firecrawl) block list + INTERCOM/BUZZER/SELF-CLOS | Firecrawl scrape | https://data.cityofnewyork.us/resource/wvxf-dwi5.json?$where=boroid='3' AND block in(5116…5162)… | matched to PLUTO lots: 67 intercom/buzzer (53 B, 13 A, 1 C) on 13 bldgs 1991–2025, 59 on edge roads; 290 self-closing (236 C) on 24 bldgs; HPD spells "BEVERLY ROAD"; cites §27-2005 HMC | HPD section, maps, tables, AI, Sources |
| PLUTO box query | Firecrawl scrape | https://data.cityofnewyork.us/resource/64uk-42ks.json?... | 283 lots/1,146 homes: 120 A, 74 B, 41 S, 22 C, 11 D, 15 other; 118 lots tagged BSW HD; PP 70; CD 314; Argyle Rd ZIP 11218, rest 11226; big bldgs 1710 Cortelyou (131, 1960), 1601 Beverley (96, 1940); 2007/2014 newer bldgs | Neighborhood, Architecture, maps |
| Cortelyou Road station … Beverley Road station | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Beverley_Road_station ; https://en.wikipedia.org/wiki/Cortelyou_Road_station | Q only; 1907 station houses between Marlborough & E16; Cortelyou rebuilt 1994–96 | Landmarks, facts |
| NYPD 70th Precinct … | WebSearch → WebFetch | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/70th-precinct.page ; https://www.brownstoner.com/architecture/building-of-the-day-154-lawrence-avenue/ (title only) | covers Midwood, Fiske Terrace, Ditmas Park, PPS; 154 Lawrence Ave | Landmarks, schema |
| Cortelyou Library … Flatbush Food Coop | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Cortelyou_Library ; https://www.grocery.coop/coops/flatbush-food-cooperative-0/ | library opened 1983, remodeled 2021; co-op 1415 Cortelyou Rd, founded 1976 | Business, Landmarks |
| City of Yes ADU basement legalization CD14 | WebSearch → WebFetch | https://www.nyc.gov/site/buildings/dob/pr-legalizing-basement.page ; https://www.nyc.gov/assets/planning/download/pdf/plans-studies/city-of-yes/housing-opportunity/housing-opportunity-guide-adus.pdf | LL126/2024 proposed rules 11/10/2025, certain CDs (CD14 NOT confirmed); ADU one per 1–2 family, 800 sf | Units section |
| City Council approves City of Yes Dec 5 2024 | WebSearch (result title/URL only) | https://www.governor.ny.gov/news/governor-hochul-mayor-adams-and-council-speaker-adams-celebrate-passage-most-pro-housing | dated December 5, 2024 passage | Units section |
| Beverley Square burglary/package theft | WebSearch | — | nothing Beverley-Square-specific; not used | — |
| reddit Ditmas Park Victorian buzzer basement side entrance | WebSearch | — | only listings; Reddit EMPTY (not accessible in build env) | — |
| Google PAA / PASF / AnswerThePublic / AI Overview / Bing / DDG / Yelp | — | — | EMPTY (not accessible in build env) | AI section framed as generic cost-guide claims |

### Question register (this page)
QA (H3): Can an electric strike go into a hundred-year-old wooden porch door frame without splitting it? · Where is the doorbell transformer in a freestanding Flatbush house, and why is it so hard to find? · Our two units share one doorbell transformer in the cellar. Can it run a video doorbell for each unit? · How do we give a new attic or basement unit its own bell without opening the walls? · Our porch is being rebuilt this summer. What should the carpenter leave for the doorbell wiring? · Which side of the Q tracks puts our house inside the historic district? · What will Landmarks staff look for if we replace the porch intercom with a video unit? · Why do the big buildings on these two roads keep getting self-closing-door violations, and what does that have to do with the buzzer? · Only the apartments on one side of our six-story building stopped hearing the lobby. Where does a technician start? · (H3 label) Already bought a doorbell or door station?
FAQ (8, = FAQPage): Our house on Rugby Road is in the new historic district. Do we need a Landmarks permit just to fix the porch doorbell? · We rent the second floor of a two-family on East 17th Street. The owner's bell works and ours does not. Whose wiring is that? · Can the bell for a basement apartment be at a side door instead of on the front porch? · Our porch has a storm door in front of the main door. Where should the button go so visitors can reach it? · Painters keep covering our porch button. How do we protect it the next time the porch is painted? · Our six-story building on Cortelyou Road has an open HPD intercom violation. What paperwork do you give us after the repair? · We are converting the attic into an apartment. When should the new buzzer wire be run? · We want a new porch light and a video doorbell at the same time on a landmarked house. Can they be planned together?
Checked against all door-buzzer-repair FAQ/H2/H3 questions (1,906 unique strings) and the concurrent Bed-Stuy and Belmont pages; five of my drafts were rewritten to avoid their intents (outer-vs-inner vestibule release, crossed split-house bells, pre-1968 three-family intercom duty, keeping original buttons, post-renovation dead lines).

### Images (11, all from images/access-control-installation/ Brooklyn-named files; no images/products/ used — those are camera kits)
- Mapping (source → dest, images/door-buzzer-repair/door-buzzer-repair-beverley-square-*):
  - dumbo-white-unv-video-doorbell-with-camera-and-bell-button → slim-white-video-doorbell-with-camera-and-bell-button (hero)
  - windsor-terrace-dome-camera-on-yellow-fascia-against-bare-branches → dome-camera-under-yellow-eave-against-bare-branches
  - marine-park-video-doorbell-with-bell-button → black-two-button-video-doorbell-with-bell-icon
  - windsor-terrace-recorder-views-of-brick-side-path-and-back-room-door → recorder-view-of-brick-side-walkway-and-storeroom-door
  - prospect-park-south-white-wired-video-doorbell → white-wired-video-doorbell
  - prospect-park-south-recorder-screen-view-of-sidewalk-and-curb → recorder-screen-view-of-sidewalk-slabs-and-curb
  - park-slope-turret-camera-in-cellar-storage-room-corner → small-camera-in-corner-of-cellar-storage-room
  - prospect-park-south-silver-single-button-door-station-with-card-reader → silver-one-button-door-station-with-card-reader
  - south-williamsburg-rounded-silver-and-black-video-intercom → rounded-silver-and-black-video-intercom
  - starrett-city-black-video-doorbell-beside-white-plug-in-chime → battery-video-doorbell-with-plug-in-chime
  - starrett-city-small-camera-on-soffit-below-red-exit-sign → lit-exit-sign-and-small-camera-on-drop-ceiling (replaced a Windsor Terrace cable photo that looked like the same room as a Bed-Stuy recorder-screen image)
- Swapped out after hash/visual dedupe vs Belmont: Axis black door station, Akuvox brushed single-button, Akuvox touchscreen directory, Akuvox white monitor, grey steel corridor door, blue cable bundles (same scenes as Belmont files).

### Flags
- Conflicts (stated on page): 118 vs 119 district houses; Lott farm (Wikipedia) vs Voorhies farm (LPC); architects Petit/Slee/Driesler (6sqft) vs Pierce/Petit/Driesler (LPC); west edge Argyle vs Stratford; PLUTO year-built (1920s) vs LPC 1894–1910.
- Brief said "Q/B": Wikipedia shows only the Q stops at Beverley Rd and Cortelyou Rd; page says Q only. Brief's "Ocean Ave/Ocean Pkwy edges" not used (outside study area).
- Hub's "HPD Class B intercom, $250–$500/day" claim not used; HPD data shows intercom violations mostly Class B under §27-2005 HMC; the $250–$500 figure is the self-closing-door (Class C) penalty from LL62/63.
- Basement legalization CD14 eligibility not confirmed (stated on page).
- Pricing: $250 service call (pricing page + hub agree) and hub item ranges; blueprint $195/hr not used — silo uses $250 call. No price conflict between hub and pricing page (pricing page lists only the $250 call).
- AESS practice claims to confirm: same-day, 1–2 h single-fault repairs; button-by-button survey and labelling at transformer; dated repair notes for HPD; cut sheets/photos for LPC applications (owner files); BYOE labor-only quoted after testing; check closer/latch on every lobby call; won't run wire across porch face; legacy Lee Dan/TekTone/Alpha stations (from hub).
- check_page.py quirk: identifies this silo as "door" (no door-buzzer-repair-brooklyn.html), so it demands an up-link to nonexistent /door-brooklyn; page links /door-buzzer-repair-brooklyn-new-york (and /door-buzzer-repair-nyc).
