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

## Silo-wide addendum (Bronx River / Bronxdale / Bronxwood batch, 2026-10-22)


Compiled 2026-10-22 during the Bronx River / Bronxdale / Bronxwood rebuild batch (builder: Bronx River). Build environment: Firecrawl MCP (search/scrape), WebSearch, WebFetch (WebFetch timed out on permission for comptroller.nyc.gov; shell curl blocked). Every row: exact query · platform · URL · finding · page+section used. `EMPTY (not accessible in build env)` = the surface could not be opened, not that it has no data.

### 1. SERP surfaces
| # | Layer | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|---|
| S1 | Google PAA | "door buzzer repair" / "door buzzer repair Bronx" · Google | — | EMPTY (not accessible in build env — no Google SERP access; Firecrawl/WebSearch return organic results only) | — |
| S2 | Google PASF / related | same · Google | — | EMPTY (not accessible in build env) | — |
| S3 | Answer the Public | "door buzzer repair" · answerthepublic.com | — | EMPTY (not accessible in build env — tool requires login/JS) | — |
| S4 | Google AI Overview | "door buzzer repair cost NYC" · Google | — | EMPTY (not accessible in build env). Bronx River §10.5 therefore checks claims from articles that AI answers tend to repeat (S8–S10), stated as such on page | Bronx River §10.5 intro |
| S5 | Bing PAA/related | "door buzzer repair NYC" · Bing | — | EMPTY (not accessible in build env) | — |
| S6 | DuckDuckGo | "door buzzer repair NYC" · DDG | — | EMPTY (not accessible in build env) | — |
| S7 | Organic (WebSearch) | `door buzzer repair cost NYC apartment building` · WebSearch (standard) | https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix ; https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ ; https://www.homeadvisor.com/tloc/Howard-Beach-NY/Door-Install-Repair/ ; https://contractorplus.app/resources/construction-costs/repair-door/new-york-ny | Organic SERP for cost intent dominated by Brick Underground, vendor blogs (Swiftlane), and national cost aggregators (HomeAdvisor, ContractorPlus). Aggregator figures not read/used | Bronx River §10.5 H3 3 (names Angi/HomeAdvisor/Fixr as national-average sources, figures not used) |
| S8 | Article claims | scrape (query) · Firecrawl | https://www.brickunderground.com/improve/nyc-intercom-repair-guide-how-to-fix | Nov 7 2019 (Mimi O'Connor): "A lot of times it's user error" (Lock and Tech); service-call estimates $195/hr and $250/hr + parts; "It's all in the wire connections" (Paragon) — lobby base, apartment station, strike, power supply; Lee Dan prevalent; 5-apt building replaced in a day, 100-unit in ~2 days | Bronx River §10.5 H3 2, 3, 4, 6; sources |
| S9 | Organic (problem) | `apartment buzzer sounds but door won't unlock electric strike cause` · WebSearch | https://www.seco-larm.com/?p=194 ; https://butterflymx.com/blog/how-cold-weather-affects-apartment-intercoms/ ; https://www.brownstoner.com/forum-archive/2006/01/broken-buzzerin ; (dormakaba KB link 404) | SECO-LARM: strike not activating → check connector, 12/24 VDC source, meter voltage/amperage, heavier gauge or bigger supply, activation device. Cold-weather article exists (not read) | Bronx River §6/§9 strike answers; sources |
| S10 | Organic (problem) | `apartment door buzzer won't stop buzzing OR "buzzer stuck" fix intercom NYC` · Firecrawl search | https://butterflymx.com/blog/apartment-building-buzzer-bombing/ ; https://www.doityourself.com/stry/how-to-fix-an-apartment-intercom-buzzer ; https://security-systems.nyc/blog/apartment-intercom-not-working/ ; https://www.reddit.com/r/askanelectrician/comments/11bcgtd/old_intercom_will_not_stop_buzzinghelp/ ; https://www.imperasecurity.com/intercom-repair | Problem layer: "buzzer bombing" (ButterflyMX), DIY "touch wires together" test, "persistent buzzing, door release failure" (security-systems.nyc), Reddit advice to cut a speaker wire (unsafe/not repeated), competitor FAQ "buzzer works but door won't open" (Impera) | Keyword plan §3; no quotes on page |

### 2. Community / reviews
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit bronx buzzer not working landlord door "buzzer" apartment Bronx` · Firecrawl search (excerpts only) | https://www.reddit.com/r/AskNYC/comments/10uzqs0/landlord_wont_fix_my_intercom_is_there_any_legal/ ; https://www.reddit.com/r/nyc/comments/cr3om/my_apartment_building_doesnt_have_any/ ; https://www.reddit.com/r/AskNYC/comments/pt1uft/old_apartment_whats_normal_and_whats_not/ ; https://www.reddit.com/r/NYCapartments/comments/pq2gez/advice_intercom_lawrequirements_for_a_24_hour/ | Recurring resident intents: landlord won't fix intercom/legal options; 24-unit building with no buzzer — is it required; "HPD regulations say you should have a working buzzer/intercom" (commenter, unverified); "intercom and door buzzer broken for months". Thread bodies not opened | Intent only (Bronx River §whose-door, MDL thresholds); not quoted |
| R2 | r/bronx, r/Soundview local threads on buzzers | — | EMPTY (no local thread surfaced; Reddit not openable beyond excerpts) | — |
| Y1 | `yelp intercom buzzer repair Bronx review technician never showed overcharged` · Firecrawl search | https://www.yelp.com/search?find_desc=Intercom+Repair&find_loc=The+Bronx%2C+NY+10465 ; https://www.yelp.com/search?find_desc=Intercom+Repair&find_loc=Van+Nest%2C+Bronx%2C+NY | Only Yelp search-page excerpts (aggregate ratings, a positive snippet). 1–3★ review text: EMPTY (not accessible in build env) | — |
| Y2 | competitor snippet (same search) | https://www.uasecurity.com/Intercom-Systems-Bronx-New-York.htm | Bronx competitor advertises "Qualifying common repairs $150–$250" — market price signal; not named on page | Pricing context only |

### 3. Keyword plan — five layers (silo)
Not search-volume data (no keyword tool reachable — Ahrefs MCP not used this run); assembled from S7–S10, R1, the Bronx hub, the pricing page and competitor snippets.
- **Service:** door buzzer repair, buzzer repair, apartment buzzer repair, intercom buzzer repair, door release repair, electric strike repair/replacement, buzzer system repair, buzzer transformer replacement, lobby panel repair, buzzer service call.
- **Problem:** buzzer not working, buzzer rings but door won't open/unlock, door release clicks but stays locked, buzzer won't stop buzzing / stuck, one apartment buzzer dead, no sound / weak buzzer, buzzer works when dry fails when wet, gate release not working, buzzer bombing, door doesn't close/latch, hum from transformer.
- **Technology:** electric strike (fail-secure / fail-safe), magnetic lock, push-to-exit / REX sensor, doorbell/buzzer transformer (16–24 VAC), 12/24 VDC power supply, battery backup, two-wire audio, riser pair, amplifier, button plate, audio handset, cellular door station.
- **Industry / property:** two-family house, three/four-family house (class A multiple dwelling), small walk-up, co-op/condo lobby, NYCHA (refer out), auto shop / garage, warehouse/storage unit, storefront with apartments above, offices/clinics.
- **Geographic:** NYC, Bronx, each borough/county hub, neighborhood pages (Bronx River: East 174th St, Bronx River Ave, Harrod/Manor/Noble/Croes Aves, Starlight Park, Soundview, ZIP 10472).
- **Legal/intent modifiers (cross-layer):** landlord responsibility, HPD complaint / 311, Multiple Dwelling Law 50-a, self-closing door violation (HMC 27-2041.1), warranty of habitability, NYCHA repair ticket.

### 4. Notes for later pages in the silo
- Most of the existing 160+ door-buzzer-repair pages repeat the same ~25 generic questions (cost, same day, landlord won't fix, brands, upgrade to video, stuck open, no sound, weekend, parts on truck). New pages should avoid those intents entirely and ask building-type-specific questions.
- Pricing on the Bronx hub ($250 service call + component ranges) vs blueprint service rate $195/hr, 3-hr minimum ($585): Bronx River page uses $250 for the visit and $195/hr for extended tracing / return visits / customer-supplied parts — needs Anwar's confirmation silo-wide.

## Bronx River, Bronx

Page: `door-buzzer-repair-bronx-river-bronx-ny` (REBUILD, was crawled-not-indexed) · built 2026-10-22 · phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd) · up-link /door-buzzer-repair-bronx-new-york · prices Bronx ×1.00 (hub list) · 13,859 rendered words.

**Thesis — "Whose door is it?"** Bronx River packs three rulebooks into a few blocks around East 174th Street: NYCHA towers (Bronx River Houses, Addition, Sotomayor — NYCHA's door, residents log tickets, AESS does not repair), one- and two-family houses (HMC "private dwelling"; owner downstairs is the landlord), three-plus-unit houses (class A multiple dwelling — self-closing door duty, apartment locks; MDL §50-a intercom rule only at 8+ units), and garages/storage along Bronx River Avenue (fail-safe vs fail-secure, release from bays). Every repair starts by sorting the door. Section order: hero → intake → neighborhood → **whose-door decision block** → repair capture + NYCHA ticket log → services → architecture (house circuit + door anatomy SVGs) → commercial + rules → Q&A (grouped by who is asking) → equipment → AI check → form → process → landmarks → pricing → packages → services grid → field notes → FAQ → areas → sources → close.

### Local research matrix
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | scrape · Firecrawl | https://en.wikipedia.org/wiki/Bronx_River,_Bronx | Redirects to the river article (no neighborhood article). River facts only (mouth between Hunts Point and Soundview, Greenway, Concrete Plant/Starlight Parks). | Confirmed no standalone article; not cited for neighborhood |
| L2 | `"Bronx River Houses" NYCHA East 174th Street buildings` · Firecrawl search → scrape | https://en.wikipedia.org/wiki/Bronx_River_Houses | 9 bldgs × 14 stories, completed Feb 28 1951, 13.94 acres bounded by E 174th St, Harrod Ave, Bronx River Ave; 3,025 residents; 1,260 apts (older listings 1,245); Hohauser / Novick; Addition 2 senior bldgs 6+14 stories, 225 apts, Feb 28 1966, E 172nd–174th / Manor–Harrod; PSA 8 2794 Randall Ave; Bambaataa / community center; 1979 tenant patrol; 1999 135 CCTV cameras | Hero, §5, §5.5, Q&A NYCHA, landmarks, schema mentions, sources |
| L3 | `"Bronx River" neighborhood Bronx boundaries Soundview ...` · Firecrawl search; then scrape (query) | https://en.wikipedia.org/wiki/Soundview,_Bronx | Bronx River = historic community name, recognized by CB9; 1967 Sound View naming; western edge along river = storage/warehousing/auto repair; Sotomayor (ex-Bronxdale) 28 × 7-story; Casa Celina 2024, 16 stories, 204 senior apts; 43rd Pct 900 Fteley Ave; IRT Pelham (6) on Westchester Ave, Elder Ave station; ZIPs 10472/10473 | §5, §5.5, §8, landmarks, sources |
| L4 | same search (result) → scrape (directQuote) | https://www.nyc.gov/assets/bronxcb9/pdf/2025/FY2026StatementBX09.pdf | CB9: south of E Tremont, Bronx River to Westchester Creek, 4.1 sq mi, ~200,000 people, Bronx River listed first; NYCHA capital requests "New intercoms/front door (hard to see address & easy to pull open)", "Intercom system renovation needed", "Entrance/Exit Door renovations needed" (28-building dev't — matches Sotomayor count, development names not in text); Argus camera Bronx River Ave E174–E177 (illegal dumping); Bronx River Ave & Rosedale street sinking | §5, §5.5, §8.5 (street numbers), Q&A (house number), landmarks, sources |
| L5 | `Bronx River Houses intercom OR "front door" OR "lobby door" broken tenants NYCHA` · Firecrawl search → scrape | https://citylimits.org/initial-tally-shows-nycha-bronx-river-tenants-favoring-trust/ | Apr 15 2024 (Tatyana Turner): Bronx River Addition 122 ballots, 84 Trust / 22 PACT / 16 Section 9; $66M outstanding repair needs | §5.5, Q&A (Addition), sources |
| L6 | same search → scrape (directQuote) | https://comptroller.nyc.gov/newsroom/stringer-releases-investigative-survey-of-nycha-doors/ | Oct 12 2018: 299 developments, 1,023 doors broken/tampered/unlockable; Bronx 24% of 767 front doors open, 20% of 276 rear/side unlocked; doors held open by rope, tape (description). Not Bronx-River-specific in passages read. WebFetch of same URL refused (permission timeout) | Sources (context only) |
| L7 | `Starlight Park Bronx River reopened East 174th Street bridge Greenway Bronx Times` · Firecrawl search | https://www.nycgovparks.org/parks/starlight-park (excerpt) | 13-acre park at E 174 St / Bronx River | §5.5, landmarks |
| L8 | same search → scrape (query) | https://forgotten-ny.com/2026/10/bronx-river-starlight/ | Oct 18 2026 (Kevin Walsh): Starlight amusement park 1919–1942 (1918 exposition), Sheridan Fields renamed Starlight Park 1998, 174th St bridge, Sheridan Expwy → boulevard, Greenway section 2023 | §5.5, landmarks, timeline SVG, sources |
| L9 | `"Bronx River" section Bronx 10472 two-family OR three-family house "Manor Avenue" ...` · Firecrawl search (excerpts) | https://streeteasy.com/building/1359-bronx-river-avenue-bronx ; https://www.propertyshark.com/mason/Property/71099/1209-Manor-Ave-Bronx-NY-10472/ ; https://www.compass.com/homes-for-sale/bronx-ny-10472/multi-family/ ; https://www.homes.com/bronx-ny/soundview-neighborhood/multi-family-homes-for-sale/ | 1915 2-story 3-family on Bronx River Ave; 1930 2–4 family on Manor Ave (PropertyShark labels locality West Farms); Compass labels Manor & Noble Ave listings "Bronx River"; 4-family Bronx River Ave, 4-unit Croes Ave | §5, §7, timeline; addresses NOT printed on page |
| L10 | `NYC Housing Maintenance Code 27-2043 intercom self-closing ...` · Firecrawl search → scrape HMC PDF (directQuote) | https://www.nyc.gov/assets/buildings/pdf/HousingMaintenanceCode.pdf | §27-2041.1 self-closing doors: class C, 14 days, $250–$500 + $250/day; §27-2043 key lock, heavy-duty latch/deadbolt + chain guard (class A); §27-2045 "private dwelling" = unit in 1–2 family home occupied by non-owner; §27-2049 street numbers visible from sidewalk | §whose-door, §8.5, Q&A, thresholds SVG |
| L11 | carried from research/intercom-repair.md G1/G3/G5/G6 (silo-adjacent, verified there) | nysenate.gov MDL §50-a/§3; RPL §235-b; portal.311.nyc.gov KA-01074; nyc.gov NYCHA repairs / CCC | MDL 50-a 8+ units post-1/1/1968, majority request older; warranty of habitability; 311 covers buzzers; NYCHA CCC (718) 707-7771 / MyNYCHA | §whose-door, §8.5, Q&A, AI check, close |
| L12 | Reddit r/bronx / r/Soundview for Bronx River buzzer/door threads | — | EMPTY (no Bronx River–specific thread surfaced; Reddit only as excerpts in build env) | — |
| L13 | Bronx Times / News 12 Bronx / Norwood News — Bronx River buzzer or entry-door news | (search excerpts only: bronx.news12.com Adam Houses item is Morrisania, not used) | EMPTY for Bronx River entry doors/buzzers | — |
| L14 | 311 / HPD complaint counts for Bronx River addresses | — | EMPTY (not queried — would need per-address Open Data pulls; out of time budget) | — |

### Flags for Anwar (Bronx River page)
- AESS practice claims stated conservatively, please confirm: we decline NYCHA entry-system repairs at a resident's request; written diagnosis after every visit (copy to tenant with owner's OK); common strike sizes carried on the truck; door left locking on key/latch if a part is ordered; pre-purchase buzzer check sold as a normal service call; $195/hr, 3-hr minimum ($585) used for extended tracing, owner-requested return visits and fitting customer-supplied parts (the Brooklyn hub $250-vs-$195 conflict is still open); "most single-fault repairs finished in one visit, often within an hour or two of arrival"; certificate of insurance on request; warranty FAQ lists exclusions (existing wiring, customer parts, weather/impact/surge) adapted from blueprint Appendix A.
- Field Notes are written as Anwar's standard method, explicitly "not a particular job" — no real Bronx River anecdote was available.
- CB9 request quotes: development names are not attached in the text read; page attributes them to "NYCHA developments in the district" only.
- Apartment count conflict for Bronx River Houses (1,260 Wikipedia vs 1,245 older NYCHA listing) stated on page.
- Neighborhood extent ("east bank around E 172nd–174th, Bronx River Ave to Croes Ave") is inferred from CB9 naming, Compass labels and the NYCHA boundaries — no official boundary exists.
- Images: first pick from images/smart-lock-installation/ was AI-generated and has been replaced (main-run instruction). The 11 now on the page are real AESS job/product photos from images/access-control-installation/ (10) and images/network-installation/ (1); none shares an md5 with the Bronxdale/Bronxwood sources and none repeats their scenes (corridor, stone facade, cable bundles, storefront fascia, night storeroom, door-station products). They show ceilings, lobbies, a shop, a storage room, a recorder and a walk-up facade rather than buzzer hardware, because the real photos containing door stations were already taken by the sibling pages. Real buzzer/strike photos are still needed. Old AI files are listed as DROP in images-door-buzzer-repair-bronx-river-bronx-ny.txt.

### Question register — door-buzzer-repair-bronx-river-bronx-ny
- [FAQ + schema] What does the $250 service call cover when the building is a two- or three-family house?
- [FAQ + schema] When does the $195 an hour rate with a three-hour minimum apply instead of the $250 visit?
- [FAQ + schema] If a part has to be ordered, will you leave the front door locking and closing before you go?
- [FAQ + schema] Whose permission do you need before working on the buzzer in a rented house?
- [FAQ + schema] Can you replace only the outdoor button plate and keep the bells inside the apartments?
- [FAQ + schema] Which buzzer jobs in a house also need a licensed electrician?
- [FAQ + schema] What should I say on the phone so the technician arrives with the right part?
- [FAQ + schema] Two houses share one driveway gate. Can both houses' buzzers release it?
- [FAQ + schema] The ground-floor family uses the side door, but their bell button is on the front stoop. Can the button be moved?
- [FAQ + schema] Does the warranty cover a buzzer you repaired, or only parts you supplied?
- [§9 H3] I live in one of the nine towers at Bronx River Houses and the lobby door release is dead. Can I hire AESS to fix it myself?
- [§9 H3] A relative in the Bronx River Addition senior building cannot get down to the lobby while its intercom is out. What can the family do while NYCHA schedules the repair?
- [§9 H3] Our house on Bronx River Avenue has three apartments, one bell button for each floor. Does the city treat it differently from a two-family house?
- [§9 H3] We live on the first floor of our own two-family house and rent the top floor. Is the tenant's buzzer legally ours to keep working?
- [§9 H3] A tenant called you with the owner's agreement. Will the tenant get a copy of what you found, or only the owner?
- [§9 H3] The button upstairs releases our inner vestibule door but not the iron gate at the sidewalk. Why would one work and not the other?
- [§9 H3] After heavy rain the bell button on our stoop works for a day and then quits. Is water getting into the outdoor button?
- [§9 H3] In our four-family house a visitor's ring never reaches the top floor, though the other apartments ring fine. Where does a single floor's wire usually fail in a house that size?
- [§9 H3] Every bell in our three-apartment house went faint at about the same time. Is that one failing part or several?
- [§9 H3] Our repair shop on Bronx River Avenue keeps the office door on a buzzer. Can staff out in the bays release it without walking to the desk?
- [§9 H3] We rent warehouse space near East 174th Street. If a buzzer and a magnetic lock share one power supply, what happens to the door in a power cut?
- [§9 H3] Delivery drivers cannot find our house number to ring the right bell. Is fixing that part of a buzzer job?
- [§9 H3] We are about to buy a two-family house in the Bronx River section. Can you check the front door and buzzer before we close?
- [§9 H3] If the strike on our front door has to be replaced, how long is the door out of service in a three-family house?

## Bronxdale, Bronx

Page: `door-buzzer-repair-bronxdale-bronx-ny` (REBUILD, 2026-10-22). Phone (646) 490-0629, GBP Bronx (460 E Fordham Rd, #bronx). Up: /door-buzzer-repair-bronx-new-york. Prices: Bronx ×1.00 = existing Bronx hub lines ($250 service call + ranges) and $195/hr, 3-hr minimum ($585).

**Thesis — "the front door has to do the finding."** Bronxdale is a City Planning map label that residents and websites disagree about (CB11 in 2014: "No one calls that area Bronxdale"; borough historian: label above Pelham Pkwy "probably a mistake"; listings say Bronxwood / Pelham Parkway / Allerton / even Morris Heights; the NYCHA "Bronxdale Houses" are in Soundview, renamed Sotomayor 2010). In dense 6–7-story elevator buildings and courtyard developments (Pelham Parkway Houses), visitors cannot find you by neighborhood name, so the building number, entrance, directory, numbering and call codes are as much a part of the repair as the talk/release circuit. Built on Husock's account of the Pelham Parkway Houses (buzzers "long been broken", codes "burned by a cigarette and couldn't be read", buildings on a diagonal so addresses found only "by wandering around the courtyard"). Section order is distinct: intake → neighborhood → same-day → "finding layer" (directories/numbering/codes/entrances) → talk/release/door → services → architecture → courtyard entrances → commercial + code callouts → owner/tenant duties (MDL §50-a, HPD) → Q&A → equipment → AI check → CTA → form → process → landmarks → pricing → packages → complete services → field notes → FAQ → areas → sources.

### Research matrix (exact query · platform · URL · finding · used on page)

| # | Query | Platform | URL | Finding | Page section |
|---|---|---|---|---|---|
| 1 | scrape "Bronxdale, Bronx" | Firecrawl scrape (Wikipedia) | https://en.wikipedia.org/wiki/Bronxdale,_Bronx (redirects to Allerton, Bronx) | DCP classified southern part of Allerton as "Laconia" and northern as "Bronxdale"; names "highly disputed"; NYCHA: Boston Road Plaza (1×20 st), Eastchester Gardens, Parkside Houses (14 bldgs, 6/7/14/15 st), Pelham Parkway Houses (23×6 st); tenements within five blocks of the El on White Plains Rd; 49th Pct 2121 Eastchester Rd; ZIPs 10467/10469 | Neighborhood ¶2; facts list; FAQ coverage |
| 2 | Bronxdale Bronx neighborhood boundaries White Plains Road Bronx Park East Pelham Parkway | WebSearch | (results list) | Pointed to Pelham Parkway nbhd article, Forgotten NY, Lehman (redirected, not read) | — |
| 3 | fetch | WebFetch | https://forgotten-ny.com/?p=18422 | Bronxdale was a village on the Boston Post Road amid Lorillard land; snuff mill stands in NYBG; "When the Botanical Garden was developed the village disappeared"; Boston Road north of Bronx Park lined with fast food, used-car dealers, gas stations | Neighborhood ¶1; landmarks (Snuff Mill); commercial (Boston Road) |
| 4 | fetch | WebFetch | https://www.lehman.cuny.edu/vpadvance/artgallery/arch/neighborhoods/bronxdale.html | 302 to lehman.edu/public-art-bronx — EMPTY (not followed) | — |
| 5 | fetch | WebFetch | https://en.wikipedia.org/wiki/Pelham_Parkway_(neighborhood),_Bronx | Boundaries Pelham Pkwy S / Dyre Ave line / Bronxdale Ave / Bronx Park East; "dominated by 6 and 7-story elevator apartment and coop buildings"; Art Deco and Tudor; White Plains Rd primary commercial thoroughfare; White Plains Rd + Lydig Ave "a beehive of activity"; Bronx Park 718 acres; 49th Pct; ZIPs 10461/10462 (10467/10469 north); Pelham Parkway 2.3 mi × 400 ft | Neighborhood ¶2–3; facts; commercial; landmarks |
| 6 | Bronxdale Bronx neighborhood boundaries NTA "Bronxdale" Pelham Parkway South Bronx River Parkway | Firecrawl search | (results) | Surfaced Wikimapia, Prison Policy NTA table, Bronx Times, AESS's own access-control Bronxdale page | — |
| 7 | scrape | Firecrawl scrape | http://wikimapia.org/22467305/Bronxdale | Bronxdale = area around northern Bronxdale Ave; approx. Pelham Pkwy (N), Muliner Ave (E), Rhinelander Ave (S), Bronx River Pkwy (W); some sources add Bronxwood north of the parkway | Neighborhood ¶2 (stated as community-written) |
| 8 | scrape | Firecrawl scrape | https://www.prisonpolicy.org/origin/ny/nta.html | BX07 Bronxdale 2010 census pop 35,538 | Facts list (cross-check) |
| 9 | "BX07" Bronxdale neighborhood tabulation area | Firecrawl search | https://www.nyc.gov/assets/planning/download/pdf/data-maps/nyc-population/census2010/t_pl_p5_nta.pdf (excerpt) | BX07 Bronxdale: 34,309 (2000), 35,538 (2010), +1,229 (+3.6%), 349.04 acres, 101.8 persons/acre | Facts list; population SVG |
| 10 | NTA polygon via NYC Open Data / ArcGIS | Firecrawl scrape | data.cityofnewyork.us resource cpf4-rkhq; services5.arcgis.com NTA query | 404 / invalid URL — EMPTY (exact BX07 polygon not obtained) | — (boundary stated as disputed instead) |
| 11 | Bronxdale Bronx "north of Pelham Parkway" OR "south of Pelham Parkway" | Firecrawl search | (results) | Found Bronx Times 2014 naming article | — |
| 12 | scrape | Firecrawl scrape | https://www.bxtimes.com/nabe-change-push-for-bronxdale/ | Ben Kochman, Jan 16 2014: CB11 + DCP to drop "Bronxdale"/"Laconia" for "Allerton"; DCP map labels "a small slice of the area above Pelham Parkway and west of Pelham Gardens" Bronxdale; Jeremy Warneke (CB11 DM): "No one calls that area Bronxdale…"; Joe Thompson (49th Pct Community Council pres., ~50 yrs): "You tell people you're from Bronxdale and they have no idea where you are from"; "Allerton Avenue area"; Lloyd Ultan: village on W bank of Bronx River at Boston Rd, now Bronx Zoo parking lot; Bronxdale Ave was "Bear Swamp Road"; label above Pelham Pkwy no historical basis, probably a mistake; Allerton Ave named after Mayflower passenger Isaac Allerton, main commercial strip | Hero; Neighborhood ¶1; facts; AI check #1; landmarks; commercial; sources |
| 13 | gov search: NYC HMC intercom multiple dwelling eight or more apartments buzzer door lock 27-2043 | Firecrawl gov search | https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a ; https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173560 | MDL §50-a: post-1/1/1968 class A MDs — self-closing/self-locking entrance doors; 8+ apts intercom at lobby door with voice + release; pre-1968 on majority tenant request; owner cost recovery; wilful damage/jamming = misdemeanor. BC 1010.4.4: 8+ dwelling units intercom; attendant alternative. HMC §27-2043 apartment door locks. BC 1010.1.9.8/1010.1.9.9 electrically locked egress doors (headings only) | Commercial code callouts; owners & tenants; AI check #5–6; Q&A side door |
| 14 | HPD violation class intercom "class B" self-closing door repair within 30 days NYC | Firecrawl search | https://www.nyc.gov/site/hpd/services-and-information/penalties-and-fees.page | A 90 days; B 30 days; C lead/window guards/mold/pests 21 days; C self-closing doors 14 days; C heat/hot water no time; other C 24 h; B penalties $25–$100 + $10/day (5 or fewer units) / $75–$500 + $25–$125/day | Owners & tenants ¶2; HPD SVG |
| 15 | scrape | Firecrawl scrape (PDF) | https://www.lawhelpny.org/sites/default/files/attachments/HPD%20Violations%20Checklist.pdf | Examples of C: "No lock on entrance door to building"; B: entrance door lock/knob defective (apartment) | Owners & tenants ¶2; HPD SVG |
| 16 | scrape | Firecrawl scrape | https://ag.ny.gov/publications/residential-tenants-rights-guide | Plain-language MDL §50-a summary ("two-way voice intercom system from each apartment to the front door… 'buzz' open") | Owners & tenants ¶1 |
| 17 | Pelham Parkway Houses NYCHA completed 1950 six-story … | Firecrawl search | https://en.wikipedia.org/wiki/Pelham_Parkway_Houses ; https://www.mapquest.com/us/new-york/nycha-pelham-parkway-houses-441096223 | 23 six-story bldgs, completed June 1950; blocks Mace/Waring, Bronxwood–Williamsbridge; Waring–Astor, Paulding–Williamsbridge; Astor–Pelham Pkwy, Wallace–Bronxwood; MapQuest 1,263 apts, completed June 30 1950, 23.74 acres | Neighborhood ¶3; facts; courtyard section; landmarks |
| 18 | scrape | Firecrawl scrape | https://manhattan.institute/article/in-nycha-the-little-things-are-a-big-deal | Howard Husock (orig. NY Daily News, article-1.3890711): 1,266 apts in 23 six-story brick bldgs (1950); "call the household rather than to buzz; the buzzers have long been broken"; tenant: "99%" broken; visitors let in as tenants go out; codes "burned by a cigarette and couldn't be read"; scaffolding sheds over lobbies; bldgs on a diagonal, "only by wandering around the courtyard can one find individual addresses" | Hero; Neighborhood ¶4; facts; finding layer; courtyard section; Q&A |
| 19 | "Bronxdale Houses" NYCHA Soundview | Firecrawl search + scrape | https://en.wikipedia.org/wiki/Sotomayor_Houses | Former Bronxdale Houses in Soundview, opened Jan 1955, 28 bldgs ~1,500 apts, renamed for Justice Sotomayor June 2010 (board vote May 20 2010, ceremony June 4) | Neighborhood ¶2; names SVG |
| 20 | Pelham Parkway Bronx intercom OR buzzer OR "front door" broken tenants building news | Firecrawl search (web+news) | https://unhp.org/publications/press/role-of-private-equity-worries-tenant-advocates/ | Chloe Tribich (undated reprint): 750-760 Pelham Pkwy South tenant assoc. pres. Ray Ruiz lists broken front door locks — NOT USED (no date) | — |
| 21 | scrape | Firecrawl scrape | https://www.bxtimes.com/no-luxury-for-pelham-parkway-tenants/ | Sept 13 2014: 1540 & 1130 Pelham Pkwy S, 1135 Pelham Pkwy N, 2160 Matthews Ave; Goldfarb; elevators out, hot water cut; lobby ceiling "pocked with holes" from botched camera install | Architecture (rentals) |
| 22 | scrape | Firecrawl scrape | https://www.cityrealty.com/nyc/morris-heights/2144-bronx-park-east/111396 | 2144 Bronx Park East built 1927, 78 rental apts; CityRealty files it under "Morris Heights" | Neighborhood ¶2–3; architecture; area SVG |
| 23 | "Pelham Parkway North" art deco apartment buildings 1930s | Firecrawl search | https://streeteasy.com/building/601-pelham-parkway-north-bronx/106 (excerpt) | 601 Pelham Pkwy N: co-op "in Bronxwood", 116 units, 7 stories, 1937 | Neighborhood ¶2–3; facts |
| 24 | scrape | Firecrawl scrape | https://juan.americasgrouprealty.com/real-estate/601-n-pelham-parkway-315-bronx-ny-10467/1049801/204041354 | MLS 1049801 (listed 2026-09-29): Art Deco, architect H.I. Feldman, builder Dr. J. Billig; terracotta foyer, original mosaics, two elevator banks; intercom; directions "BRONXWOOD neighborhood"; neighborhood field "Pelham Parkway"; cross st Bronx Park East & Barker Ave; "Stories Total: 6" | Neighborhood ¶2–3; facts |
| 25 | Pelham Parkway station IRT White Plains Road Line opened 1917 | Firecrawl search | https://en.wikipedia.org/wiki/Pelham_Parkway_station_(IRT_White_Plains_Road_Line) | Opened March 3, 1917 (2/5) | Facts; landmarks |
| 26 | reddit bronx buzzer "Pelham Parkway" OR "Bronx Park East" OR Allerton intercom doesn't work delivery | Firecrawl search | https://www.reddit.com/r/AskNYC/comments/17knzko/front_door_buzzer_broken_at_walkup_apartment/ (excerpt) | Generic NYC walk-up buzzer broken ~1 year; no Bronxdale-specific thread — local Reddit EMPTY | not used |
| 27 | intercom buzzer rings wrong apartment crossed wires directory apartment building fix (silo angle: Problem layer) | Firecrawl search | https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/ ; https://www.doityourself.com/stry/how-to-fix-an-apartment-intercom-buzzer | Repair when isolated & parts available; DIY guides test button/transformer (simple circuits) | AI check #2, #4; equipment repair-vs-replace |
| 28 | Hub cross-check | repo | door-buzzer-repair-bronx-new-york.html | $250 service call + ranges; NYCHA/Mitchell-Lama serviced via management with COI; same-day usually on calls before 10 AM | Pricing; FAQ; same-day |
| — | Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG / Yelp 1–3★ for "door buzzer repair Bronxdale" | — | — | EMPTY (not accessible in build env) | AI check states this |

### Keyword layers used (natural placement)
Service: door buzzer repair, buzzer repair, intercom repair, door release repair, strike replacement, amplifier replacement, riser repair, apartment station replacement, lobby panel repair. Problem: rings wrong apartment, buzzer sounds but door won't open, door unlocks by itself, one line of apartments dead, voice fades on top floors, directory unreadable, code list out of date. Technology: button panel, amplifier, riser, junction box, electric strike, magnetic lock, keypad/code-dial, telephone entry, video entry. Industry: co-op, rental, NYCHA/courtyard housing, walk-up, two-/three-family, apartments over stores, clinics/offices. Geographic: Bronxdale, Pelham Parkway North/South, Bronx Park East, White Plains Road, Allerton Avenue, Lydig Avenue, Boston Road, Wallace Ave, Williamsbridge Rd, 10467/10469/10462/10461, the Bronx.

### Question register — door-buzzer-repair-bronxdale-bronx-ny
FAQ (visible + FAQPage):
1. If the repair needs a part we don't carry and a second trip, is the $250 service call charged again?
2. Does someone from the building need to be there, or can the technician work with just the super's keys?
3. Which streets and ZIP codes does this Bronxdale page actually cover, since nobody agrees on the borders?
4. How long does a release-only repair take compared with replacing an amplifier?
5. Is it safe for a co-op shareholder to swap the handset inside their own apartment themselves?
6. Can we get a written report that the board or management can keep in the building's files?
7. Our entry panel dials residents over a phone line. What happens if the building cancels its landline?
8. If we call in the afternoon with the lobby door stuck open, will anyone come the same day?
Questions Answered (H3):
9. Our co-op's lobby directory still lists shareholders who sold years ago. Who is allowed to change the names, and do the numbers on the panel have to match the apartment doors?
10. Visitors to our courtyard building keep walking up to the identical entrance next door and buzzing strangers. Is there anything at the panel that helps them find the right door?
11. Since our renovation, pressing 3F downstairs rings the apartment across the hall. Is that the wiring or just the labels?
12. Our keypad entry still shows tenants who moved out, and nobody has the programming code. Can the list be fixed without wiping everyone's codes?
13. Every apartment ending in B went silent on the same day while the rest of the building still works. Where does a technician start looking?
14. Residents on our top floor say the lobby voice is a whisper, while the second floor hears it clearly. Why would the sound fade the higher you go?
15. The lobby door hums when someone buzzes from upstairs but still won't open unless you shove it. Is the strike broken?
16. Packages keep getting left in our vestibule because drivers cannot reach anyone upstairs. Can the panel ring a cell phone instead of the apartment handset?
17. My mother's home attendant arrives early and often can't get buzzed in, because Mom can't reach the handset in time. What are the options?
18. Our front door works fine, but the side courtyard door stays unlocked all the time. Is that part of the intercom repair or a separate job?
19. The buzzer in our Pelham Parkway rental has been dead for months. What should we document before calling 311?
20. We are a small co-op board with no live-in super. What should we insist the repair company leaves behind after an intercom job?
21. The 2 and 5 trains on White Plains Road drown out our lobby speaker. Can that be improved without replacing the panel?
22. Repair the old panel, or replace it? (equipment H3)

## Bronxwood, Bronx

Page: door-buzzer-repair-bronxwood-bronx-ny · built 2026-10-22 · direct line (646) 490-0629 · GBP Bronx (460 E Fordham Rd) · Bronx x1.00

**Thesis:** Bronxwood Avenue as a dividing line. Wikipedia puts Allerton in ZIP 10467 west of the avenue and 10469 east of it; ACS 2024 5-yr shows 10467 = 8% single-unit / 14% owner-occupied vs 10469 = 46% single-unit / 51% owner-occupied (10466: 33% / 40%). East of the avenue and north of Gun Hill the stock is two-story two-family houses, so a Bronxwood buzzer is usually a two-button doorbell-type circuit (porch buttons, basement transformer, stapled pair along joists, electric release in a wooden frame behind a storm door) shared by an owner and a tenant, and legally a private dwelling (MDL §4) outside §50-a. Page order: hero → instant block → same-day repair → neighbourhood (name conflict + ZIP line) → how a two-family buzzer is wired → services → architecture → owner/tenant responsibility (MDL/HPD) → commercial → Q&A → equipment → AI check → CTA → form → process → landmarks → pricing → packages → complete services → field notes → FAQ → areas → sources → final CTA/company.

### Research matrix (query · platform · URL · finding · page section)
| # | Query | Platform | URL | Finding | Used in |
|---|---|---|---|---|---|
| 1 | scrape "Bronxwood, Bronx" | Firecrawl scrape (Wikipedia) | https://en.wikipedia.org/wiki/Bronxwood,_Bronx (redirects to Allerton, Bronx) | Bronxwood = southern Allerton (Allerton Ave N, Esplanade Ave E, Pelham Pkwy S, Bronx River Pkwy W), incl. Pelham Parkway Houses + Boston Road Plaza; Google Maps formerly called whole area Bronxwood; DCP used Bronxdale/Laconia; "dominated by multi-unit homes", tenements within ~5 blocks of the el; ZIP 10467 W / 10469 E of Bronxwood Ave; 4 NYCHA devs (Pelham Pkwy Houses 23 six-story bldgs; Boston Road Plaza 20-story); 49th Pct 2121 Eastchester Rd; E62/L32 3431 White Plains Rd; PS 76 Adee & Bronxwood Aves; Allerton library 2740 Barnes Ave (1959, renovated 2015); stations Pelham Pkwy, Allerton Ave, Burke Ave, Gun Hill Rd; buses Bx8/12/25/26/28/30/38/39; Allerton Ave primarily commercial W of Laconia Ave | Neighborhood, facts list, Architecture, Commercial, Landmarks, schema mentions |
| 2 | Bronxwood Bronx neighborhood houses Bronxwood Avenue history | WebSearch | (results list) | led to Forgotten NY, WFUV, cityneighborhoods, openigloo, StreetEasy | — |
| 3 | fetch | WebFetch | https://forgotten-ny.com/?p=7299 | Kevin Walsh, Jan 8 2008: Bronxwood Park = North & South Oak Drives between Wallace & Cruger Aves just N of Burke Ave; John T. Adee sponsored, late 1880s–early 1890s; two-family houses (aluminum siding), porches, old-fashioned gate, steep hill on Wallace Ave with no road/step street | Neighborhood, Architecture, Landmarks, FAQ (gate) |
| 4 | fetch | WebFetch | https://wfuv.org/content/bronxwood-park-modern-relic | Katie Meyer, Mar 10 2014: reached via Gun Hill Rd → Holland Ave; gated driveways, large porches, houses re-sided; dates to 1880s | Architecture, Landmarks |
| 5 | fetch | WebFetch | https://www.cityneighborhoods.nyc/bronxwood | boundaries Pelham Pkwy / Bronx Park East / Waring Ave / Williamsbridge Rd; "low-rise brick homes, two-family houses, and small apartment buildings" | Neighborhood, name table |
| 6 | "Bronxwood" Google Maps Allerton ... NYT 2014 | WebSearch | — | Bronx Times articles found; NYT not opened | — |
| 7 | fetch | WebFetch | https://www.bxtimes.com/pols-join-push-for-allerton/ | Ben Kochman, Feb 1 2014: Crowley, Vacca, Gjonaj letter Jan 28 backing CB11 "Allerton"; DCP says no official map | Neighborhood, AI check |
| 8 | fetch | WebFetch | https://www.bxtimes.com/allerton-nabe-sorta-official-now/ | Kochman, Feb 16 2014: DCP relabels "Bronxdale" area "Allerton"; "no official neighborhood boundaries in New York City"; Gene DeFrancis, Allerton International Merchants Association | Neighborhood, Commercial, FAQ (name) |
| 9 | fetch ×7 | WebFetch | streeteasy.com/building/{3540,3716,4038,4109,4135}-bronxwood-avenue-bronx, 2926-holland-avenue-bronx (+3720 listed in search, not opened) | all two-family, 2 stories; built 1965, 1950, 1950, 1925, 1910; Holland Ave 1935 labelled "Bronxwood"; others labelled Williamsbridge/Wakefield. six records opened in total (five Bronxwood Ave, one Holland Ave) | Hero, Neighborhood, AI check |
| 10 | fetch | WebFetch | https://www.openigloo.com/buildings/bronx/bronxwood/pre-war?page=15 | ~498 pre-war buildings listed under "Bronxwood" (Hering, Paulding, Wallace, Cruger, Holland, Barnes, Esplanade...) | Neighborhood, Architecture |
| 11 | fetch | WebFetch | https://www.nyc.gov/assets/nycha/downloads/pdf/Pelham%20Parkway.pdf | 23 buildings; map streets incl. Wallace, Barnes, Matthews, Bronxwood, Paulding Aves, Mace, Waring; ZIPs 10467/10469 | Neighborhood, Landmarks |
| 12 | scrape (query) | Firecrawl | https://censusreporter.org/profiles/86000US10469-10469/ (WebFetch refused; Firecrawl used) | ACS 2024 5-yr: 68,521 pop; 25,373 units; 51% owner; 46% single-unit | Hero, Neighborhood, SVG |
| 13 | scrape (query) | Firecrawl | https://censusreporter.org/profiles/86000US10467-10467/ | 96,421 pop; 40,791 units; 14% owner/86% renter; 8% single-unit | Hero, Neighborhood, SVG |
| 14 | scrape (query) | Firecrawl | https://censusreporter.org/profiles/86000US10466-10466/ | 71,116 pop; 26,146 units; 40% owner; 33% single-unit | Neighborhood, SVG |
| 15 | Multiple Dwelling Law 50-a ... | Firecrawl gov search | https://nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf ; https://law.justia.com/codes/new-york/mdw/article-3/title-2/50-a ; https://ag.ny.gov/sites/default/files/tenants_rights.pdf | §50-a: class A MD erected/converted after 1/1/1968 → self-closing self-locking entrance doors; intercom if 8+ apts; pre-1968 on majority tenant request; AG guide summary | Responsibility section, AI check, FAQ |
| 16 | MDL §4 definition ... | Firecrawl gov search | https://nysenate.gov/legislation/laws/MDW/4 | private dwelling ≤2 families; multiple dwelling = 3+ families living independently | Responsibility section, AI check, FAQ |
| 17 | HPD property registration ... | Firecrawl gov search | https://nyc.gov/site/hpd/services-and-information/register-your-property.page ; ABCs of Housing owners guide | register if 3+ units, or 1–2 family where neither owner nor immediate family resides | Responsibility section, Q&A (absentee owner), SVG |
| 18 | "Bronxwood Avenue" Bronx news 2025 OR 2026 | WebSearch | — | nothing relevant (property pages: two lots = religious facility, lodge; not used) | — |
| 19 | Allerton ... break-ins front door Bronx Times 49th | WebSearch + WebFetch | bronx.news12.com/bronx-native-warns-allerton-residents-of-serial-porch-pirate-in-the-area (Oct 25 2022, summary only); bxtimes.com/men-attempt-to-break-into-allerton-apt-multiple-times/ (Jason Cohen, Mar 1 2022, Mace Ave apartment door); bronx.news12.com/allerton-residents-jittery-after-string-of-robberies-34821460 (Oct 2008, 2910 Wallace Ave tenants) | context only | Sources list only |
| 20 | reddit Bronx two-family house doorbell buzzer ... | Firecrawl search | https://www.reddit.com/r/AskNYC/comments/1t74q1e/ (excerpt only) | reply claims "3 units are in the same category as single family homes" (wrong under MDL §4) | AI check |
| 21 | door buzzer stopped working two family house door release transformer doorbell wiring (silo) | Firecrawl search | https://diy.stackexchange.com/questions/326630/ ; https://www.homedepot.com/c/ah/how-to-fix-a-doorbell/9ba683603be9fa5395fab9055b186d7 | staples shorting doorbell pair; button/chime/transformer/wiring checklist | Wiring section, AI check |
| 22 | door buzzer repair cost intercom repair cost Angi OR Fixr OR HomeAdvisor (silo) | Firecrawl search | https://swiftlane.com/blog/apartment-intercom-replacement-cost-in-2026-typical-ranges-what-impacts-price/ ; https://butterflymx.com/blog/replace-broken-buzzer-intercom-system-for-small-apartment-building/ (excerpts) | minor repairs $150–$400; replacement $2,200–$5,000 small building | AI check, pricing compare |
| 23 | Bronxwood Avenue runs from Pelham Parkway north ... | WebSearch | Redfin street sitemaps (10466/10467) | Bronxwood Ave spans 10467, 10469, 10466 | Neighborhood (no endpoints stated) |
| — | Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG / Yelp 1–3★ | — | — | EMPTY (not accessible in build env) | — |
| — | Local Reddit r/bronx for Bronxwood/Allerton buzzers | Firecrawl search | — | EMPTY (no relevant thread surfaced) | — |
| — | Hyperlocal buzzer/intercom news in Bronxwood | WebSearch | — | EMPTY (none found; none invented) | — |

Pricing used (from door-buzzer-repair-bronx-new-york.html, Bronx x1.00): $250 service call incl. diagnostic ($272.19 with 8.875% tax); station $250–$525; relay/button $250–$475; transformer $325–$650; strike + alignment $450–$950; lobby/door panel $650–$1,800; riser/run repair $850–$2,400; service rate $195/hr, 3-hr minimum ($585).

### Question register — door-buzzer-repair-bronxwood-bronx-ny
- Why does the buzzer ring in both apartments when only one button is pressed?
- When the release clicks and the latch stays put
- Why did the buzzer die right after work on the boiler or the electrical panel?
- Can a buzzer that a previous owner disconnected be brought back into service?
- Is a metal button plate or a plastic one better on a porch that faces the street?
- Should the buzzer button be on the gate post or at the front door?
- The owner lives out of state. How does a buzzer repair get done when nobody nearby has the basement key?
- Could each household have its own code at the front door instead of a key?
- Three checks a tenant can make first
- Will a wireless doorbell kit fix a dead buzzer in a brick two-family house?
- How is a buzzer in a pre-war building on Wallace or Holland Avenue different?
- A shop door on White Plains Road wears out its electric release every year or so. Is there a sturdier option?
- In our two-family house the release button opens the front door from the downstairs apartment but does nothing from upstairs. Where is the fault likely to be?
- We put an aluminum storm door in front of the main door, and since then the buzzer sounds but the inner door has to be pulled before it opens. Did the storm door cause that?
- A house in Bronxwood Park has a locked gate at the sidewalk and a long walk up to the porch. What decides the price of adding a buzzer release at the gate?
- The city planning map calls our block Allerton, but the listing we bought from said Bronxwood. Does the name change anything about the repair or the rules that apply?
- Our basement was finished years ago and the buzzer wire disappeared into the new ceiling. Can it be repaired without opening the whole ceiling?
- Will a one-button video doorbell work for a house where two apartments share the front door?
- Our buzzer makes a constant low hum even when nobody presses it. Is that dangerous, and can we unplug it ourselves?
- The buzzer works, but it is so faint at the back of the house that we keep missing deliveries. Can it be made louder or moved?
- The upstairs tenant has a baby who naps in the afternoon. Can the bell be kept quiet at certain hours without stopping the door release from working?
- (non-question H3 statements in Q&A: "When an old two-button buzzer is worth keeping"; "When the release clicks and the latch stays put"; "Three checks a tenant can make first")
