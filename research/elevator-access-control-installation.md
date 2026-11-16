# Research — Elevator Access Control Installation (silo)

Silo created Nov 14 2026 at Anwar's request. Keyword list: `keywords/elevator-access-control-installation.md` (382 keywords, his). Photos: `images/elevator-access-control-installation/` (13 real photos Anwar sent, imported Nov 14 2026 — approved for use, the people in them are not customers).

PRICING (Anwar, Nov 14 2026): sold in levels, priced PER ELEVATOR CAR, Brooklyn base x BLUEPRINT §9 multiplier for each area. Level 1 = reader inside the car (card, fob, PIN code, phone, or video intercom/keypad station such as Akuvox); once authorized the rider can pick any floor the car serves; ties into spare conductors in the elevator controller cabinet; usually programmed remotely — from $1,500 per car (Brooklyn). Level 2 = biometrics (face recognition, fingerprint, iris) — from $2,500 per car (Brooklyn). Level 3 = floor-by-floor restriction, hall-call readers, schedules, intercom floor release, destination dispatch — quoted per building after survey (no published price). Outside our price: the elevator company's visit to make the controller connection (building arranges and pays the elevator contractor directly); a network connection or new cable run to the car if remote management needs it (own line after survey). Area starting prices L1/L2: Brooklyn & Bronx $1,500/$2,500; Queens $1,575/$2,625; Staten Island $1,650/$2,750; Manhattan $1,875/$3,125; Nassau $1,725/$2,875; Suffolk $1,800/$3,000; Westchester $1,875/$3,125; Rockland $1,950/$3,250; Orange $2,100/$3,500; Putnam $2,175/$3,625; Dutchess & Ulster $2,295/$3,825. NEVER publish equipment cost, never name the school job, never mention Manhattan parking (added at billing).

SCOPE (honesty): Abstract Enterprises Security Systems does the low-voltage side — readers in the cab or at hall stations, floor-enable relays / I-O boards, wiring, credentials, programming, intercom/visitor integration. The elevator controller, car-operating-panel button wiring at the controller, fire recall and destination dispatch interfaces are coordinated with the building's licensed elevator contractor. Never claim AESS does elevator mechanical/controller work. Brands: "we install / integrate / service", never "certified dealer".

## Silo-wide findings (Nov 14 2026)

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "site:abstractenterprisessecuritysystems.com elevator" · web search | — | No existing AESS page on elevator access control (new silo). | — |
| "elevator access control" · web search | https://ipvm.com/reports/elevator-access-control-examined | Reader that only grants the car still lets the rider press any floor the car serves — floor-level restriction needs per-floor relays. | Explainer: car-call vs floor-by-floor |
| same | https://butterflymx.com/?p=3987 | Floor-by-floor lockout: each floor locked by default, fob in cab unlocks the resident's floor for a timed window; visitor access via intercom unlocking the floor. | How it works / visitor section |
| same | https://butterflymx.com/blog/elevator-access-control-by-floor-schedule/ | Landing (hall-call) restriction vs in-car restriction answer different questions; time schedules per floor. | Design choices / schedules |
| "elevator access control installation cost per floor" · web search | https://butterflymx.com/blog/access-control-cost-per-unit-multifamily/ | Access control is priced per controlled opening; elevator access control limits floors but does not replace the elevator system; vendor ranges are not a national benchmark. | Cost section framing (no AESS price invented) |
| "reddit elevator access installation" · Reddit r/accesscontrol | https://redlib.andus.dev/r/accesscontrol/comments/1hmqcnh/elevator_access_installation/m3wtb6x/?context=3 | Installer thread: relay count scales floors × cars × hall stations (20-floor 4-car example → hundreds of relays); destination dispatch avoids per-button relays. | Why scope is counted per floor × cab |
| "reddit elevator key fob floor" · Reddit r/Elevators | https://pol1.lr.ggtyler.dev/r/Elevators/comments/1juiuno/controlled_access_issue | Adding card readers to lobby and basement hall buttons cuts non-resident use. | Hall-call reader option |
| NYC DOB Buildings Bulletin 2022-010 · nyc.gov | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Devices added to cabs/hall stations must not impede normal or emergency operation and must go inoperative on Phase I / Phase II firefighters' operation (ASME A17.1 2.27.3). | Fire recall section — readers drop out on recall |
| NYC Building Code Ch. 30 / Appendix K · nyc.gov | https://www.nyc.gov/assets/buildings/building_code/update_4_combined_instructions.pdf | NYC elevator code = ASME A17.1 as modified by Appendix K; BANK/CAR FIRE RECALL switches. | Compliance section (general, not legal advice) |
| NYC Local Law 63 of 2021 (Tenant Data Privacy Act) · HPD | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Class A multiple dwellings using smart access (fobs, cards, phones) need tenant consent, a plain-language privacy policy, limits on data use. | NYC hub + borough pages — residential elevator fobs |
| LL63 text · intro.nyc | https://intro.nyc/local-laws/2021-63 | Applies to building entry, units and common areas; data of vacated tenants destroyed within 90 days. | Same |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env) unless a page section below records it. | — |

Keyword-list questions (Anwar's list) to seed FAQs, one owner page each — record in the register when used: what is elevator access control · how does it work · how to restrict elevator access to certain floors · how much does it cost · what equipment is needed · can it be controlled remotely / from my phone · can it use RFID / smartphones · can it integrate with CCTV / intercom · who installs / repairs it · can tenants use key fobs · how do I stop unauthorized people using an elevator · best system for an apartment building · can I manage access for different tenants · what is destination dispatch security.

## Question register

| Question | Page |
|---|---|



## Nyc hub (elevator-access-control-installation-nyc)

## NYC hub (elevator-access-control-installation-nyc) — research, Nov 14 2026

| Query · platform | URL | Finding | Page section used |
|---|---|---|---|
| "NYC Housing and Vacancy Survey 2023 share of rental units in elevator buildings" · web search → HPD PDF | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | 2023 NYCHVS: 3,705,000 housing units; 1,699,000 (46%) in buildings with an elevator; Manhattan 77% (712,000 units), Staten Island 10% (18,470); 829,200 units (22%) in 100+ unit buildings, 517,200 (14%) in 50–99; 861,200 occupied units in condo or co-op buildings (318,000 condo, 450,800 co-op); net rental vacancy 1.41%. | Hero stamp; "NYC by the numbers"; borough section; residential section |
| "NYC how many elevators DOB" · web search → DOB press release | https://www.nyc.gov/site/buildings/dob/pr-elevators-report.page | DOB Elevator Report (Apr 12 2018, 2017 data): 84,000+ elevator devices; stock "one of the largest and oldest in the world". | NYC by the numbers |
| "Local Law 126 of 2021 elevator agency director ..." · web search → DOB FAQ PDF | https://www.nyc.gov/assets/buildings/pdf/new_elevator_license_reqs_faqs.pdf | Since Jan 1 2022 (NYS Elevator Safety Act) anyone performing elevator work — alteration, assembly, installation, maintenance, repair, replacement, modernization — needs NYC and NYS licenses; employers need a Licensed Elevator Agency Director. (FAQ does not mention LL126 — page does not cite LL126.) | "Who does what" section; FAQ |
| "NYC DOB elevator alteration permit card reader" · web search → DOB Elevator Permit page | https://www.nyc.gov/site/buildings/property-or-business-owner/elevator-permit.page | Elevator filings go through DOB NOW: Build; Elevator Alteration filing covers minor alteration, repair or replacement; permits posted until sign-off. Page does not address devices added to cars. | "Who does what"; process step 3 |
| DOB Buildings Bulletin 2022-010 · nyc.gov (silo research) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Devices in cabs/hall stations must not impede normal or emergency operation and must go inoperative on Phase I/Phase II firefighters' operation (ASME A17.1 2.27.3.1 / 2.27.3.3). | Fire recall section; AI-gets-wrong |
| NYC Building Code Ch.30 / Appendix K · nyc.gov (silo research) | https://www.nyc.gov/assets/buildings/building_code/update_4_combined_instructions.pdf | NYC elevator code = ASME A17.1 as modified by Appendix K; BANK FIRE RECALL / CAR FIRE RECALL switches. | Fire recall section |
| Local Law 63 of 2021 · HPD / intro.nyc / Hunton / JD Supra (silo research) | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page ; https://intro.nyc/local-laws/2021-63 | Class A multiple dwellings with smart access (fobs, cards, phones, biometrics): written consent, plain-language privacy policy, data only for granting access/monitoring entrances, vacated tenants' reference data destroyed within 90 days, applies to common areas. | Tenant Data Privacy section; FAQ |
| r/accesscontrol "Elevator access installation" (silo research) | https://redlib.andus.dev/r/accesscontrol/comments/1hmqcnh/elevator_access_installation/m3wtb6x/?context=3 | Relay count = floors × cars × hall stations; destination dispatch avoids per-button relays. | Cost drivers; comparison table |
| IPVM / ButterflyMX (silo research) | https://ipvm.com/reports/elevator-access-control-examined ; https://butterflymx.com/?p=3987 | Car-only reader still lets rider press any floor; floor-by-floor lockout with timed unlock; intercom can unlock visitor's floor. | How it works; integration |
| "Manhattan office tower destination dispatch ... turnstile" · web search | (result list only; vendor case studies, not used for claims) | Destination dispatch + turnstile integration common in Manhattan towers (vendor case studies). Stated generally, no named building. | Commercial section (general) |
| "FDNY elevator key" · web search | — | Not used (security-sensitive; no key details on page). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

### FAQ questions used on the NYC hub (add to silo register)
See the FAQ list appended at the end of this file by the build.

| Question | Page |
|---|---|
| Does a New York City co-op board have to approve elevator access control before it is installed? | elevator-access-control-installation-nyc |
| Can our elevator use the same key fobs as the front door of our NYC building? | elevator-access-control-installation-nyc |
| Is installing elevator access control in NYC considered elevator work that needs an elevator license? | elevator-access-control-installation-nyc |
| Does adding card readers to an elevator need a DOB filing in New York City? | elevator-access-control-installation-nyc |
| What happens to elevator floor restriction during a fire alarm in an NYC building? | elevator-access-control-installation-nyc |
| How does Local Law 63 affect elevator key fobs in a New York City apartment building? | elevator-access-control-installation-nyc |
| Can an intercom in our Manhattan or Brooklyn building unlock only the visitor's floor? | elevator-access-control-installation-nyc |
| Can a tenant in an NYC office building add elevator floor restriction on its own floors? | elevator-access-control-installation-nyc |
| Will elevator access control slow down the morning rush in a busy NYC building? | elevator-access-control-installation-nyc |
| What do residents do if their phone dies and they use a mobile elevator credential? | elevator-access-control-installation-nyc |
| Can you add elevator access control to an older NYC building with a relay controller? | elevator-access-control-installation-nyc |
| Which NYC boroughs do you install elevator access control in? | elevator-access-control-installation-nyc |
| Can you take over an elevator card reader system another company installed in our building? | elevator-access-control-installation-nyc |
| Can the super or doorman open all elevator floors at once for a move or an emergency? | elevator-access-control-installation-nyc |


## Long Island hub (elevator-access-control-installation-long-island)

## Long Island hub (elevator-access-control-installation-long-island) — Nov 14 2026

| Query · platform | URL | Finding | Page section used |
|---|---|---|---|
| "New York State elevator mechanic licensing law" · web search / NYS DOL | https://dol.ny.gov/elevator-licensing-information | Labor Law Article 33 requires licenses for businesses and workers who design, install, inspect, maintain or repair elevators; contractor must be owned by or employ a licensed mechanic; DOL administers. | Rules Outside the City; AI Reality Check; scope table |
| "2020 Building Code of New York State elevators ASME A17.1" · web search / NYS DOS | https://dos.ny.gov/2024-03-19ebcnrd-documentdraft-version-30 | Draft Existing Building Code of NYS: altered elements of existing elevators shall comply with ASME A17.1; same elements altered in elevators responding to the same hall call control (305.8.2 in 2020 text / 306.7.7 draft). | Rules (whole bank); Q&A two-car co-op; worked example |
| NYC DOB Buildings Bulletin 2022-010 (from silo research) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Devices added to cabs/hall stations must not impede operation and go inoperative on Phase I/II (ASME A17.1 2.27.3). Cited as the stated principle, not as Long Island law. | Rules — firefighters' operation |
| "Long Beach NY oceanfront condo elevators Sandy" · web search / Habitat Magazine | https://habitatmag.com/Publication-Content/Bricks-Bucks/The-Waters-Edge-700-Shore-Road-Long-Beach-NY | The Waters Edge, 700 Shore Rd: lobby flooded, garage filled with sand, one elevator working for a time; ~$3.2M incl. electrical and boiler. | Region facts; oceanfront towers |
| same · Long Island Herald | https://liherald.com/longbeach/stories/seniors-raise-post-sandy-safety-concerns,45633 | 415 National Blvd (6-story LBHA senior building): one elevator unrepaired, front intercom not working so anyone could walk in (Jan 2013). | Region facts |
| "Great Neck co-op" · web search / CooperatorNews | https://cooperatornews.com/article/great-necks-kenwood-gardens | Kenwood Gardens, Great Neck: 7 stories, 69 units, 1925, first co-op built on Long Island. | Region facts |
| "Long Island transit-oriented development" · Bisnow | https://www.bisnow.com/news/new-york/construction-development/eight-transit-oriented-developments-making-long-island-walkable-73103 | Modera Mineola 275 units 6 stories; New Village at Patchogue 291 units. | Region facts |
| same · LongIsland.com | https://longisland.com/news/09-05-19/first-phase-of-ronkonkoma-hub-apartment-complex-opens.html | Alston Station Square, Ronkonkoma Hub: 245 units in two buildings, TRITEC, opened Sept 5 2019. | Region facts |
| same · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-completion-40-million-affordable-senior-housing-development-suffolk | 11 Park Drive Apartments, Wyandanch: 94 affordable units 62+, five stories, Oct 2022. | Region facts |
| "Long Island medical office building Lake Success" · Crexi | https://www.crexi.com/lease/properties/1108204/new-york-lake-success-quadrangle | Lake Success Quadrangle ~1.1M SF Class A office/medical, on-site owner management, indoor parking. | Region facts |
| "Garden City Hotel" · hotel site | https://gardencityhotel.com/our-hotel | 269 rooms and suites, Club Level on penthouse floor, across from Garden City LIRR station. | Region facts; hotels |
| "Stony Brook access control policy" · stonybrook.edu | https://stonybrook.edu/policy/_policies/physical-and-electronic-access-control-policy.html | Office of Access Control and Lock Shop has sole responsibility for design, installation and maintenance of electronic card access systems. | Suffolk section; campuses |
| Hofstra turnstile article · campussafetymagazine.com | (redirected to emeraldx.com) | EMPTY (not accessible in build env) — not used. | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp / Long Island Reddit | — | EMPTY (not accessible in build env). | — |

Prices: none published (Anwar has not set elevator prices). Page says quoted per building after survey and links /access-control-installation-long-island for door-side work.

### Questions used on this page (add to the silo register)
- Our Nassau co-op has two cars that answer the same lobby button. Can we put a reader in just one of them to save money?
- How do we handle the shareholder who refuses to carry a fob?
- When a unit sells, how does the new owner get access and the old owner lose it?
- Our building has a part-time doorman. Should the elevator restriction switch off while he is on duty?
- Our Lake Success medical building wants the elevators open to patients by day and card-only at night. Is that one system or two?
- Several tenants in our Melville office building use different badge brands. Can one elevator system read them all?
- Our hotel's key card vendor says the elevator interface is "their job." Where do you fit in?
- We are building near an LIRR station in Suffolk. When should elevator access be decided?
- Our senior residence wants wristbands instead of fobs. Do elevator readers accept them?
- What happens to the elevator access system when the power goes out?
- Does elevator access control on Long Island require a building permit?
- Already have an access system?
- How many floors can one elevator access system restrict?
- Can residents still use the stairs if the elevator restricts their floor?
- Do you work on Long Island weekends?
- Is the work done under a New York State license?
- Can a lost fob be shut off right away?
- Will the elevators be out of service during installation?
- Can guests be given access for just one evening?
- Who keeps the record of which floors residents visit?
- Our elevator readers were put in by a company that no longer answers. Can you support them?
- Do you install elevator access in buildings with only one elevator?
- What should the board have ready before the survey?
- Do you also install cameras in the elevator lobby and cab?


## Hudson Valley hub (elevator-access-control-installation-hudson-valley)

## Hudson Valley (hub) — elevator-access-control-installation-hudson-valley

Built Nov 14 2026 (Hudson Valley subagent). Angle: the region's buildings have grown upward (Westchester downtown towers, hospital additions, small-city lofts); elevator access is a two-trade job under NYS Labor Law Article 33; building-type playbook; six-county breakdown; fire recall and power-loss behavior; retrofit of older hydraulic/relay elevators; new-construction specification; accessibility.

| Query · platform | URL | Finding | Section used |
|---|---|---|---|
| "New Rochelle Yonkers White Plains new high-rise apartment towers downtown development 2025" · web search → fetch | https://thebcw.org/wp-content/uploads/2025/01/Westchester_Development_2024.pdf | New Rochelle >6,145 units under construction (Master Development Plan / Downtown Overlay Zone ~12M SF); Yonkers 1,050 units AvalonBay & Alexander Crossing, Hudson Piers 1,395 planned, ~2,080 pipeline; Port Chester 1,208 under construction, former United Hospital redevelopment 775 rentals + hotel + assisted living/memory care; Edge-on-Hudson Sleepy Hollow 1,457 units delivered | Why HV buildings…; facts list; building types (senior living); Westchester county block; new construction |
| same search | https://newyorkyimby.com/2026/01/renderings-reveal-two-tower-residential-complex-at-466-main-street-in-new-rochelle.html | EMPTY (fetch failed, client error) — not used | — |
| same search | https://dailyvoice.com/new-york/yonkers/work-nears-completion-on-27-story-apartment-tower-in-westchester/ | EMPTY (fetch failed) — not used | — |
| "Vassar Brothers Medical Center Poughkeepsie Patient Pavilion floors opened" · web search → fetch | https://prnewswire.com/news-releases/walshconsigli-completes-545-million-patient-pavilion-at-vassar-brothers-medical-center-301209441.html | 752,610 SF, eight stories, 264 private rooms, 30 critical care rooms, 66-room ED, 12 surgical suites; ED opened Jan 9 2021, pavilion Jan 11 2021 | Why HV buildings…; facts list |
| "Rockland County Middletown Orange County hospital medical office building…" · web search → fetch | https://realestateindepth.com/white-plains-hospital-breaks-ground-on-750-million-expansion-project | White Plains Hospital 10-story, 500,000 SF expansion, 240 more private rooms (292→436 beds), dedicated OR floor (10 ORs), new ED; opens 2028 | Why HV…; facts list; building types (hospitals) |
| same search | https://www.thebluebook.com/iProView/8248/skanska/general-contractors/construction-projects/garnet-health-medical-center-physician-office-building-cancer-center-and-associated-projects-469695/ | (title) Garnet Health Medical Center physician office building, cancer center and associated projects | Orange County block |
| same search | https://realestateindepth.com/garnet-health-signs-deal-to-join-montefiore-health-system | (title) Garnet Health joining Montefiore Health System | Orange County block |
| same search | https://www.hgar.com/montefiore-expands-healthcare-investment-in-rockland-county-with-new-urology-center | (title) Montefiore expanding outpatient care in Rockland County | Rockland County block |
| same search | https://dailyvoice.com/new-york/ramapo/lifestyle/nyack-hospital-breaks-ground-on-emergency-department-new-medical-village/693237/ | Nyack Hospital 16,300 SF two-story addition incl. 7,800 SF Medical Village (2018) | Rockland background (not quoted) |
| "Newburgh waterfront apartments Poughkeepsie Queen City Lofts…" · web search | https://hudsonvalleypress.com/?p=38101 | (title) Queen City Lofts almost ready to lease, Poughkeepsie | Dutchess County block |
| same | https://westfaironline.com/apartments/poughkeepsie-close-to-approving-another-apartment-building-on-dutchess-avenue/ | (title) Poughkeepsie close to approving another apartment building on Dutchess Avenue (Aug 2026) | Dutchess County block |
| same | https://1450wkip.iheart.com/content/2026-03-30-newburgh-waterfront-lot-set-for-mixed-use-apartment-project | (title) Newburgh waterfront lot set for mixed-use apartment project (Mar 2026); also Lofts at the Foundry listings | Orange County block; new construction |
| "New York State Labor Law Article 33 elevator mechanic license…" · web search → fetch | https://dol.ny.gov/elevator-licensing-information | Article 33: businesses/individuals who design, install, alter, maintain, service, repair conveyances must be licensed by NYS DOL; only licensed mechanics under a licensed contractor may alter conveyances; license types listed | Facts list; Our side vs elevator contractor; FAQ permit/who on site; contractor questions |
| "Building Code of New York State 2020 Chapter 30 elevators ASME A17.1 Uniform Code…" · web search → fetch | https://ecode360.com/8675937 | City of Rochester Ch. 50: ASME A17.1 as referenced by the NYS Uniform Fire Prevention and Building Code; local commissioner enforces; work requires Article 33 license (example of local enforcement outside NYC) | Fire and power section; FAQ permit |
| same | https://codes.iccsafe.org/content/get-pdf/7682/CHAPTER30.html | EMPTY (no machine-readable text) | — |
| silo file | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Add-on devices must not impede normal/emergency operation and go inoperative on Phase I/II | Fire and power section (cited as how regulators treat add-ons) |
| "reddit Westchester apartment key fob elevator floor access building" · web search → fetch | https://butterflymx.com/blog/video-intercom-with-elevator-floor-access-for-apartment-buildings/ | Intercom approval can enable "the appropriate floor instead of every floor"; elevator access does not replace the elevator system; temporary PIN/QR passes; confirm with elevator contractor | Visitors section |
| silo file | https://ipvm.com/reports/elevator-access-control-examined ; https://butterflymx.com/blog/elevator-access-control-by-floor-schedule/ ; r/accesscontrol thread | Car-call vs floor lockout; landing vs in-car; relay count arithmetic | How it works |
| Reddit Westchester/Hudson Valley threads | — | EMPTY (no relevant local thread surfaced) | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env) | — |

NYC Local Law 63 deliberately NOT applied (outside NYC); page says no equivalent outside NYC and recommends a written logging policy.

### Questions used on this page (add to register)

| Question | Page |
|---|---|
| Does a building outside New York City need a permit to add card readers to its elevators? | elevator-access-control-installation-hudson-valley |
| Who has to be on site when the elevator side is wired? | elevator-access-control-installation-hudson-valley |
| What happens to the floor restrictions when the fire alarm recalls the elevators? | elevator-access-control-installation-hudson-valley |
| If the power fails, will residents be stuck unable to reach their floor? | elevator-access-control-installation-hudson-valley |
| Can a medical office building keep staff-only floors locked while the public elevators stay open? | elevator-access-control-installation-hudson-valley |
| Can a college residence hall limit each student's card to their own floor? | elevator-access-control-installation-hudson-valley |
| Can our employees keep using the badges they already carry? | elevator-access-control-installation-hudson-valley |
| Can a delivery driver be sent to one floor from the lobby intercom without a fob? | elevator-access-control-installation-hudson-valley |
| What if a senior living resident forgets their fob? | elevator-access-control-installation-hudson-valley |
| Can floor permissions change on a schedule, like opening the gym floor only in the daytime? | elevator-access-control-installation-hudson-valley |
| Does the reader go inside the elevator car or next to the call button in the lobby? | elevator-access-control-installation-hudson-valley |
| How far into the Hudson Valley do you travel for elevator work? | elevator-access-control-installation-hudson-valley |
| The company that installed our elevator readers is gone. Can you service what they left behind? | elevator-access-control-installation-hudson-valley |
| H2: How Much Does Elevator Access Control Cost in the Hudson Valley? | elevator-access-control-installation-hudson-valley |

## Manhattan (elevator-access-control-installation-manhattan) — research, Nov 16 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Manhattan elevator operator manual elevator co-op prewar still attended" · Firecrawl web search → scrape | https://nypost.com/2025/06/17/real-estate/meet-one-of-the-last-elevator-operators-in-nyc/ | 863 Park Ave, 23-unit prewar co-op (UES): wood-paneled, brass-accented elevator manually operated by rotary lever; operator 25 years; DOB estimates only about 50 hand-operated elevators remain, mostly Manhattan (NY Post, Jun 17 2025). | Facts list; prewar co-ops; AI check (old elevators); coverage; FAQ 0 |
| same search · Reddit r/AskNYC | https://www.reddit.com/r/AskNYC/comments/wzc8s0/when_was_the_last_time_you_saw_an_elevator/ | Thread "When was the last time you saw an elevator operator?" (title/snippet only). | Background for attended-elevator angle (not quoted) |
| "Tribeca SoHo loft key-locked elevator opens directly into apartment keyed floor" · Firecrawl search + scrape | https://www.brickunderground.com/buy/buy-curious-apartments-with-private-elevators | Private/key-locked elevators common in co-op loft conversions and new condos, esp. Manhattan; truly private vs key-locked; "turn the key back to the locked position after pressing the button". | Lofts section; glossary; FAQ 1 |
| same | https://michaelbhagwandin.com/blog/your-own-private-entrance-the-complete-buyers-guide-to-keyed-elevator-apartments-in-manhattan | 104 Charlton Street, boutique condo, key-locked elevator opens directly into individual loft apartments (broker guide). | Lofts section |
| same | https://www.cityrealty.com/nyc/market-insight/features/future-nyc/private-design-full-floor-nyc-apartments-direct-elevator-access-under-25-million/44643 | A key-locked elevator may serve multiple residences, each resident's access limited to their own home. | Lofts section |
| same | https://streeteasy.com/talk/discussion/17169-private-keyed-elevators | Buyer thread: "Each floor has a key on the elevator panel". | Lofts section (owners describe key per floor) |
| "destination dispatch elevator turnstile integration Hudson Yards office tower badge" · Firecrawl search | https://smartersecurity.com/blog/going-up-does-my-facility-need-destination-dispatch/ ; https://www.kone.com/en-us/advanced-people-flow-solutions/kone-destination.html ; https://www.boonedam.com/en-us/products/accessories-and-entry-additions/destination-dispatch-systems-for-elevators | Occupants badge through the turnstile and receive elevator assignment automatically; destination systems integrate elevators, doors and turnstiles. | Destination dispatch section; Q&A H3 1; AI check |
| "One Vanderbilt OR Hudson Yards destination dispatch ..." · Firecrawl search | https://newyorkoffices.com/office-building-security/ | Broker page lists Hudson Yards towers with full-floor turnstile security (snippet). Competitor page claiming most new Midtown/Hudson Yards towers use DD not used as a fact. | Class A towers (general, no building named as DD) |
| "Manhattan office market inventory million square feet Class A 2025 report" · Firecrawl search → scrape | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-office-market/ | May 14 2024: Manhattan 594,309,799 SF office (81.6% of NYC); Class A 361,054,636 SF (60.8%), Class B 172,960,516 (29.1%), Class C 59,340,112 (10.0%); conversions 25 Water St 1,163 units, 160 Water St 592, 55 Broad St 586, 17 Battery Pl 184, 90 John St 114. | Facts list; commercial section; conversions; coverage |
| same → scrape | https://www.avisonyoung.us/web/new-york/office-market-report | Q3 2026: leasing 30.2 msf YTD, availability 13.4%, trophy availability 10.1%. | Facts list; commercial section |
| "New York City hotel rooms inventory Manhattan share 2025" · Firecrawl search | https://www.osc.ny.gov/files/reports/osdc/2026/pdf/nyc-hotel-industry-report-july-2026.pdf | 2025: ~124,000 active rooms citywide; 1,003 hotels, Manhattan 597; occupancy 84.1%. | Facts list; hotel section |
| same | https://www.nyc.gov/assets/planning/download/pdf/applicants/env-review/citywide-hotel/appendb-feis.pdf | DCP hotel market analysis: Midtown West largest Manhattan submarket, several hotels over 1,300 rooms (Marriott Marquis, Hilton Midtown, Sheraton Times Square, Row NYC); newer hotels concentrated in Garment District near Penn Station/Hudson Yards. | Hotel section |
| "Local Law 18 short-term rental ... prohibited buildings list" · Firecrawl search | https://www.nyc.gov/site/specialenforcement/registration-law/pbl.page ; https://strr-portal.ose.nyc.gov/s/introduction?language=en_US | LL18 adopted Jan 9 2022, effective Mar 6 2023; owner incl. co-op/condo board can add whole building whose leases prohibit STRs; whole buildings only. | Hotel/extended-stay section; FAQ 3 |
| "Manhattan package theft doorman building package room survey 2025" · Firecrawl search | https://www.security.org/package-theft/annual-report/ (via snippets at myurbi.co / metrocomsecurity.com) | Security.org Oct 2025 survey (3,307 US adults): apartment/condo residents report theft ~3.5x the rate of others. Page says "much higher rate" (secondhand figure not printed). | Doorman / package room section |
| "reddit AskNYC building elevator key fob only my floor Manhattan" · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/15tpbnu/can_building_require_150_for_key_fob_if_they_only/ | Rent-stabilized tenants asking whether landlord can charge per fob when phone entry offered (dollar figure deliberately not printed). | Upper Manhattan section |
| "Habitat Magazine co-op elevator key fob floor restriction shareholders" · Firecrawl search | https://www.habitatmag.com/Publication-Content/Legal-Financial/(offset)/960 | Snippet only: a co-op installed a key fob system with an elevator upgrade, dispute over health club floor access. Not used (building unidentified). | — |
| "Landmarks Preservation Commission permit interior work ..." · Firecrawl search | https://www.nyc.gov/site/lpc/applications/applications.page | LPC permit needed before work affecting the exterior and, in some cases, the interior of a designated landmark property. | Compliance (landmarks); FAQ 2; survey checklist |
| "Manhattan medical office building ..." · Firecrawl search | https://www.squarefoot.com/blog/medical-office-space-midtown-east/ | Midtown East medical buildings described with 24-hour attended lobby, rebuilt elevators, multi-specialty tenant roster. | Medical office section |
| Silo research (re-used, verified in silo file) | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | Manhattan 77% of homes (712,000 units) in elevator buildings. | Neighborhood section; facts |
| Silo research | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf ; https://www.nyc.gov/assets/buildings/pdf/new_elevator_license_reqs_faqs.pdf ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Added devices inoperative on Phase I/II; licensing since Jan 1 2022; LL63 duties for Class A multiple dwellings. | Compliance; AI check; quick answer |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ / r/Manhattan | — | EMPTY (not accessible in build env) | — |

Prices used: Manhattan rate per task/silo file — Level 1 from $1,875 per car, Level 2 from $3,125 per car, Level 3 quoted per building. No other prices.

### Questions used on this page

| Question | Page |
|---|---|
| H3: How does destination dispatch in a Hudson Yards or Midtown tower decide which floors a badge reaches? | elevator-access-control-installation-manhattan |
| H3: What should a Class B Midtown office building secure first when its elevators answer anyone who walks in? | elevator-access-control-installation-manhattan |
| H3: Can each tenant in a multi-tenant Manhattan office building manage its own people's elevator access? | elevator-access-control-installation-manhattan |
| H3: Can the cab camera in a Manhattan building tie each clip to the fob that was used? | elevator-access-control-installation-manhattan |
| H3: How should a Manhattan condo with several amenity floors set up its permission groups? | elevator-access-control-installation-manhattan |
| H3: Can a managing agent's office change a Manhattan building's elevator permissions from off site? | elevator-access-control-installation-manhattan |
| H3: What equipment actually goes into a Manhattan building for elevator access control? | elevator-access-control-installation-manhattan |
| H3: What happens to elevator access when a Financial District office building is converted to apartments? | elevator-access-control-installation-manhattan |
| FAQ: Can a hand-operated elevator with a uniformed operator, like those still found in a few prewar Manhattan co-ops, be given a card reader? | elevator-access-control-installation-manhattan |
| FAQ: Our SoHo or Tribeca loft elevator uses a separate brass key for each floor. Can fobs or phone keys replace those keys? | elevator-access-control-installation-manhattan |
| FAQ: Does a building in a Manhattan historic district need Landmarks Preservation Commission approval to add elevator readers? | elevator-access-control-installation-manhattan |
| FAQ: Can elevator credentials help a Manhattan co-op on the city's Prohibited Buildings List keep short-term guests off other residential floors? | elevator-access-control-installation-manhattan |
| FAQ: In a Manhattan tower with a hotel on the lower floors and condos above, how are guests and residents kept apart in shared elevators? | elevator-access-control-installation-manhattan |
| FAQ: Can the package room floor in a Manhattan doorman building be limited to staff and couriers? | elevator-access-control-installation-manhattan |
| FAQ: Does a Manhattan high-rise with separate low-rise, mid-rise and high-rise banks need readers in every bank? | elevator-access-control-installation-manhattan |
| FAQ: Can one system control both the passenger cars and the service elevator our porters and contractors use? | elevator-access-control-installation-manhattan |
| FAQ: Why does elevator access control cost more per car in Manhattan than in Brooklyn or the Bronx? | elevator-access-control-installation-manhattan |
| FAQ: What paperwork does a Manhattan managing agent usually ask for before elevator access work can start? | elevator-access-control-installation-manhattan |
| FAQ: What is the practical difference between Level 1 and Level 3 for a typical Upper West Side co-op? | elevator-access-control-installation-manhattan |
| FAQ: Can a Midtown office landlord keep the lobby conference center open to all tenants while each tenant's floors stay private? | elevator-access-control-installation-manhattan |

## Brooklyn (elevator-access-control-installation-brooklyn) — research, Nov 16 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Downtown Brooklyn 2004 rezoning residential towers units built since" · web search | https://www.planetizen.com/news/2019/09/106422-2004-rezoning-didnt-predict-wave-residential-development-downtown-brooklyn | 2004 rezoning aimed at offices; 2016 Borough President report: 11,000+ housing units built in the first dozen years vs 979 anticipated; 1.3M SF commercial vs 4.6M anticipated; Schermerhorn Street corridor. | Why Brooklyn now; rental towers section; stamp |
| "Gowanus rezoning 2021 approved 8,000 apartments" · web search | https://www.planetizen.com/news/2021/11/115282-gowanus-rezoning-moving-forward-could-bring-8000-new-apartments-brooklyn | Up to 8,000 new apartments, one-third reserved for lower-income tenants; CPC approval Sept 2021, Council Land Use vote Nov 10 2021; largest upzoning of the de Blasio era. | Rental towers section; facts list |
| "2005 Greenpoint Williamsburg waterfront rezoning towers" · web search | https://www.bisnow.com/news/new-york/neighborhood/why-zoning-is-and-always-will-be-everything-in-williamsburg-57216 | 2005 rezoning opened the waterfront to housing; rezoned area 9,167 units (Council Member Reynoso report); Douglaston 2,000+ waterfront units; 2 North 6th St 40 stories; 1 North 4th Place tallest. | Waterfront towers; facts list |
| "Starrett City Spring Creek Towers number of apartments" · web search | https://www.globest.com/2018/05/09/starrett-city-sold-to-brooksville-and-rockpoint-for-905-million/?amp=1 | 5,881 apartments, 46 buildings, 153 acres, north of the Belt Parkway on Pennsylvania Ave; sold to Brooksville and Rockpoint for $905M. | Large complexes section; facts list |
| "Trump Village Coney Island co-op" · web search (listings) | https://www.compass.com/building/2940-w-5th-st-brooklyn-ny-11224/293527099900282709/ | Trump Village Section 4 co-op buildings on West 5th Street, Coney Island (2930 / 2940 W 5th St); listings show units on 21st–23rd floors. | Large complexes section (named only, no unit count) |
| "Ocean Parkway co-op buildings elevator prewar" · web search | https://www.cityrealty.com/nyc/flatbush/emroy-house-763-ocean-parkway/42922 | Emroy House, 763 Ocean Parkway: co-op, built 1937, 6 floors, elevator, no doorman. Search shows many Ocean Parkway co-op buildings (81, 110, 260, 300, 415 Ocean Pkwy). | Co-op section |
| "DUMBO loft condo keyed elevator" · web search → Brick Underground | https://www.brickunderground.com/buy/buy-curious-apartments-with-private-elevators | Key-locked elevators may serve several units, each key opening one floor; older lofts use physical (often Medeco) keys that must be turned back or the floor stays open; newer use cards, keypads, codes, biometrics; The Metropolitan (North Williamsburg) has keyed elevators opening into apartments, some freight-style serving two units. | Loft / key-to-floor section; FAQ |
| "Brooklyn landlord facial recognition key fob" · web search → Security Sales | https://www.securitysales.com/emerging-tech/brooklyn-fight-facial-recognition/ | Atlantic Plaza Towers, Brownsville, ~700 apartments: landlord applied (2018) to replace key fob entry with StoneLock facial recognition; 130+ residents filed objection; DOB said facial recognition may only supplement a key-based system. | Rent-stabilized / biometrics section; FAQ |
| same · Brooklyn Daily Eagle | https://brooklyneagle.com/articles/2019/10/08/fighting-facial-recognition-tech-new-bill-would-mandate-keys/ | 718-unit rent-stabilized building owned by Nelson Management; pre-1974 rent-regulated buildings need HCR approval for a "modification in service"; tenants complained to HCR May 2019; KEYS Act proposed (outcome not verified). | Rent-stabilized section; FAQ |
| "Brooklyn apartment building package theft lobby" · web search → CBS New York | https://www.cbsnews.com/amp/newyork/news/lobby-packages-stolen-brooklyn | Man filmed taking packages from an apartment lobby on Lawton Street, Bushwick, ~7 p.m. July 19. | Package theft section |
| same · News 12 Brooklyn | https://brooklyn.news12.com/man-appears-to-use-child-in-a-stroller-to-get-inside-crown-heights-building-and-steal-package | 240 Crown St, Crown Heights (Aug 2025): man used a child in a stroller to get someone to open the lobby door, took two packages from a pile on the floor. | Package theft section |
| "Industry City Sunset Park square feet buildings tenants" · web search → Brooklyn Eagle | https://brooklyneagle.com/articles/2025/04/08/industry-city-surpasses-650-businesses/ | 650+ businesses, ~6M SF, 16 buildings, 35 acres, ~8,500–9,000 workers. | Commercial / industrial section; facts list |
| "Brooklyn Navy Yard Building 77" · web search | https://technical.ly/brooklyn/2017/11/13/building-77-opens-brooklyn-navy-yard-promising-new-future-urban-industry ; https://bkreader.com/2017/11/21/brooklyn-navy-yards-building-77-open-business-expected-bring-3000-jobs/ | Building 77 opened Nov 2017 as manufacturing/office space; expected to bring ~3,000 jobs (headline). nyc.gov press release fetch returned nav only. | Commercial section (opening year + headline jobs figure only) |
| "The Brooklyn Hospital Center DeKalb Avenue" · web search → Wikipedia | https://en.wikipedia.org/wiki/Brooklyn_Hospital_Center | Founded 1845 as Brooklyn City Hospital; 121 DeKalb Ave, Downtown Brooklyn, west side of Fort Greene Park; 464 licensed beds; Mount Sinai affiliation since 2014. | Medical section |
| NYC Local Law 63 of 2021 · HPD (silo research) | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Smart access in Class A multiple dwellings: consent, plain-language privacy policy, limits on use, departed tenants' data deleted within 90 days. | LL63 section |
| DOB Buildings Bulletin 2022-010 (silo research) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Devices added to cabs/hall stations must not impede operation, go inoperative on Phase I/II. | Fire recall notes; AI myths |
| DOB elevator license FAQ (silo research) | https://www.nyc.gov/assets/buildings/pdf/new_elevator_license_reqs_faqs.pdf | Since Jan 1 2022 elevator work needs NYC and NYS licenses. | Scope section |
| 2023 NYCHVS selected findings PDF · nyc.gov | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | EMPTY (not accessible in build env) for Brooklyn-specific figures — no Brooklyn elevator-unit share published on the page. | — |
| Reddit r/Brooklyn, r/NYCapartments elevator fob threads | — | EMPTY (no relevant thread surfaced in search; not accessible in build env). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

### Questions used on this page
FAQ:
- How does a key fob in a Brooklyn rental tower decide which elevator buttons light up?
- Can a rent-stabilized Brooklyn building switch its elevator to key fobs without asking the state first?
- Is there a Brooklyn-based company that installs elevator key fob systems, or should we call our elevator maintenance company?
- How do we keep non-residents off the elevators in a Brooklyn rental complex with dozens of buildings?
- What is the best elevator access control for a six-story prewar Brooklyn co-op with one small car and no doorman?
- Can a Brooklyn property manager release an elevator floor for a locked-out resident from a phone?
- Our Brooklyn building has two elevators side by side. Is the price per car or per building?
- Can a DUMBO or Williamsburg loft condo swap its mechanical elevator keys for fobs and keep each floor private?
- Will a reader in the elevator help with package theft in our Brooklyn lobby, or do we need something else?
- Can the freight elevator in a Brooklyn industrial building be put on cards without slowing down loading?
- Does facial recognition in the elevator make sense for a Brooklyn rental building after the Atlantic Plaza Towers dispute?
- Do older Brooklyn tenants who do not use smartphones still get full elevator access?
- How soon can a Brooklyn building get an elevator access survey booked?

Question-headings: none (all H2/H3 headings on the page are statements).

## Queens (elevator-access-control-installation-queens) — research, Nov 16 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "2023 NYCHVS Queens units in buildings with elevator" · Firecrawl search → HPD PDF | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | 2023 NYCHVS: Queens 284,200 housing units (31%) in buildings with an elevator; Queens second after Manhattan in elevator share; units built 2000 or later 71% have elevator; 20–49 unit buildings 55% | Queens by the numbers; why Queens |
| "Queens foreign-born languages census" · Firecrawl search → Census QuickFacts | https://www.census.gov/quickfacts/fact/table/queenscountynewyork/PST045225 | Queens County: foreign-born 47.6% (2020–2024); 934,750 housing units (July 1 2025); owner-occupied rate 44.9% | Multilingual / credential section; numbers |
| "Long Island City Court Square Queens Plaza towers rezoning" · Firecrawl search → NYC DCP OneLIC project description | https://www.licplan.nyc/26538/widgets/98101/documents/67133 | OneLIC (DCP): over 21,000 housing units built within a half mile of the project area since 2010; LIC last rezoned 2001; proposed actions project ~14,699 new units over 10 years | LIC section; numbers |
| same search · NY YIMBY forum | https://forum.newyorkyimby.com/t/new-york-long-island-city-general-news-photos-discussion/241 | 2001 rezoning of 34 blocks between Queens Plaza and Court Square to spur residential high-rises | LIC section |
| same search · Serene Powers blog | https://www.serenepowers.com/blog/what-is-happening-around-queens-boulevard-and-court-square-in-2026/ | 30-25 Queens Boulevard: ~525-ft tower, 561 residential units, ~21,000 SF ground-floor retail (planned) | LIC section (stated as reported/planned) |
| "Tangram Flushing" · Firecrawl scrape → Homes.com | https://www.homes.com/building/tangram-flushing-ny/b-nmz5t4es8fqfs/ | Tangram (F&T Group): two residential towers (Tangram House South 2019, Tangram House West 2022, 16 stories, ~132 units), Renaissance New York Flushing Hotel and an office building around a central courtyard | Flushing section |
| same · F&T Group press | https://www.fandtgroup.com/news-press/flushings-tangram-tower-office-condominium-nears-sell-out-real-estate-weekly | Tangram includes retail, residential, office (office condominium) and hotel | Flushing section |
| "Sky View Parc Flushing" · Firecrawl search → Homes.com / ULMA | https://www.homes.com/building/sky-view-parc-flushing-ny/b-c7gxr21kcbr8l/ ; https://www.ulmaconstruction.com/en-us/construction-projects/building-construction/residential-mixed-used/sky-view-parc-tower-new-york-usa | Sky View Parc: 448-unit condo atop a mall, three condominium towers on a 14-acre complex, fourth tower added (The Grand) | Flushing section |
| same · StreetEasy | https://streeteasy.com/complex/flushing-commons | Flushing Commons ~600 residential condominium units across two phases | Flushing section |
| "Queens co-ops garden co-op elevator co-op" · Firecrawl search → Nacmias Law | https://nacmiaslaw.com/practice-areas/closings/building-types/standard-co-op/queens | Queens holds the city's largest concentration of garden co-ops (Jackson Heights, Sunnyside, Forest Hills); large elevator co-op complexes in Forest Hills, Rego Park, Kew Gardens, Bay Terrace, many converted in the 1980s; sponsor-held unsold shares common | Co-op section |
| "Jackson Heights Historic District" · Firecrawl search → HDC | https://hdc.org/buildings/jackson-heights/ | Jackson Heights Historic District designated Oct 19 1993; low-rise garden apartments and houses | Co-op section (LPC note) |
| "Electchester" · Firecrawl scrape → Urban Omnibus | http://urbanomnibus.net/2013/05/portfolio-electchester/ | Electchester, Pomonok: built 1949–1966 with IBEW Local 3 on 103 acres of former Pomonok Country Club; ~2,500 units in 38 buildings, many six-story brick | Large complexes section |
| "Big Six Towers" · Firecrawl search → Roebling Team / bigsixtowers.com | https://www.theroeblingteam.com/neighborhoods/woodside ; https://bigsixtowers.com/ | Big Six Towers, Woodside: Mitchell-Lama co-op completed 1963 for Typographical Union No. 6; Boulevard Gardens opened 1935 | Large complexes section |
| "Jamaica Neighborhood Plan" · Firecrawl search → NYC DCP / Council | https://www.nyc.gov/content/planning/pages/our-work/plans/queens/jamaica-neighborhood-plan ; https://council.nyc.gov/press/2025/10/09/2986/ | Adopted by City Council Oct 29 2025; ~12,000 new homes (4,000 permanently affordable), ~7,000 jobs, $413M community investments; largest neighborhood rezoning in over 20 years | Jamaica section |
| "TWA Hotel rooms" · Firecrawl search → Wikipedia | https://en.wikipedia.org/wiki/TWA_Hotel | TWA Hotel at JFK: 512 rooms; JFK's only on-airport hotel | Airport hotels section |
| "LIC warehouse converted office" · Firecrawl search → factorylic.com / MCAP | https://factorylic.com/the-building-old ; https://mcapny.com/project/falchi-building/ | The Factory: built 1926 as a Macy's furniture warehouse, now workspace; Falchi Building, 31-00 47th Ave, 5-story, built 1922 as a warehouse, now mixed use | LIC conversions section |
| same · Crain's (headline/excerpt only) | https://www.crainsnewyork.com/real-estate/vacant-class-office-space-piles-queens/ | Vacant Class A office space piling up in Queens; ~$100M conversion of a former furniture warehouse into 1.1M SF | LIC conversions (general: owners chasing tenants with amenities/security) |
| "Rockaway Sandy elevators high-rise" · Firecrawl search → NYT / PMC | https://www.nytimes.com/2012/12/08/nyregion/in-queens-and-high-above-the-floods-still-feeling-hurricane-sandys-sting.html ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6181816/ | After Sandy, Queens high-rise residents feared getting stuck in elevators as power flickered; study: nearly 700 inoperable elevators citywide in public housing left elderly/disabled residents trapped on upper floors | Rockaways section (flood-safe panel placement, power) |
| "Queens package theft lobby" · Firecrawl search → QNS / CBS | https://qns.com/2025/12/burglar-stole-packages-woodside-christmas/ ; https://www.cbsnews.com/newyork/news/queens-package-theif-caught-on-video/ | Packages stolen from the lobby of a Woodside apartment building (Dec 2025); man filmed stealing packages from a Queens building lobby | Why Queens section |
| "reddit Queens key fob elevator" · Firecrawl search → Reddit | https://www.reddit.com/r/NYCapartments/comments/1pr092n/help_landlord_has_very_restrictive_key_fob_policy/ ; https://www.reddit.com/r/NYCapartments/comments/1wfs0ny/why_are_some_people_against_key_fobs_to_enter/ ; https://www.reddit.com/r/unpopularopinion/comments/1vx8j0w/elevator_key_fobs_in_residential_buildings_create/ | Tenants complain about restrictive fob policies (fob-required elevator, limited fobs), privacy worries about fob tracking, and elevator fobs as everyday hassle | Resident concerns; LL63 section; credential policy |
| Silo research (reused, not re-fetched) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page ; https://intro.nyc/local-laws/2021-63 ; https://www.nyc.gov/assets/buildings/pdf/new_elevator_license_reqs_faqs.pdf | DOB Bulletin 2022-010 (devices inoperative on Phase I/II); LL63 consent, privacy policy, 90-day deletion; NYC/NYS elevator licenses since Jan 1 2022 | Fire recall, LL63, scope sections |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ / r/Queens specific elevator thread | — | EMPTY (not accessible in build env) | — |

Not verified / left out: exact Big Six Towers building and unit counts; Sky View Parc fourth-tower unit count; any Rockaway building names; specific Jamaica medical buildings; JFK/LGA hotels other than TWA Hotel.

### Questions used on this page
- How does an elevator card reader in a Long Island City rental tower know which floors a resident may visit?
- Our Forest Hills co-op's elevator maintenance company offered to install the card readers itself. Should it, or should a security contractor?
- Will the older proximity fobs in our Rego Park building work with a new elevator reader, and are they easy to copy?
- Can a Court Square tower let residents use their phones while older residents keep fobs?
- How do we keep office visitors in a Flushing mixed-use building from reaching the residential floors?
- How does floor restriction treat the cellar laundry and roof deck in a Queens rental building?
- We manage buildings from Astoria to Far Rockaway. Where do we find one elevator access installer for all of them?
- Our hotel near JFK wants guests limited to their own floor while airline crews use the fitness floor. Can one system do both?
- Our Rockaway building lost elevator service after a coastal storm. Where should the access control panel go so flooding does not take it out?
- Can the elevator reader prompts and resident instructions be in Chinese, Spanish or Korean for our Flushing building?
- Our Long Island City warehouse conversion has a freight elevator that tenants share. Can that car be card-controlled too?
- A home health aide visits a Kew Gardens shareholder every weekday. How do we give the aide elevator access without a permanent fob?

## Bronx (elevator-access-control-installation-bronx) — research, Nov 16 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| DOB NOW Elevator Safety Compliance, SoQL count active elevators by borough · NYC Open Data | https://data.cityofnewyork.us/resource/e5aq-a4j2.json | Active devices of type Elevator (queried Nov 16 2026): Bronx 8,746; Manhattan 42,507; Brooklyn 17,430; Queens 11,410; Staten Island 1,381. Bronx distinct BINs with an active elevator: 5,346. | Bronx by the numbers |
| same, grouped by NTA, Bronx · NYC Open Data | https://data.cityofnewyork.us/resource/e5aq-a4j2.json | Top Bronx NTAs by active elevators: Concourse-Concourse Village 600; Mott Haven-Port Morris 592; Riverdale-Spuyten Duyvil 531; Bedford Park 371; Melrose 361; University Heights (South)-Morris Heights 338; Mount Hope 318; Norwood 314; Mount Eden-Claremont (West) 297; Parkchester 256; Co-op City 244; Longwood 242. | Neighborhood table |
| "2023 NYCHVS Bronx elevator" · HPD PDF | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | Bronx 562,300 housing units; 54% (302,700) had an elevator; 38% reachable from sidewalk with no steps; Bronx had second-highest share of accessible units. | Numbers table, hero stamp |
| "2025 Housing Supply Report" · Rent Guidelines Board PDF | https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2025/05/2025-HSR.pdf | New housing units completed 2023: Bronx 9,842 (highest of the five boroughs; NYC total 27,962). | New rentals section |
| "Co-op City 35 high-rise" · coopcity.com | https://www.coopcity.com/aboutus/ | Mitchell-Lama co-op, 15,372 units in 35 high-rise buildings + 7 townhouse clusters; management modernized all 160 residential elevators in the high-rises; new lobby entrances. | Co-op City section (no client claim) |
| same · coopcity.com/apartments | https://www.coopcity.com/apartments | Modern elevators in each high-rise, 24-hour private police (CCPD). | Co-op City section |
| same · Wikipedia | https://en.wikipedia.org/wiki/Co-op_City,_Bronx | Completed 1971; largest residential development in the US. | Co-op City section |
| "Grand Concourse Historic District" · LPC designation report | https://s-media.nyc.gov/agencies/lpc/lp/2403.pdf | 61 apartment houses built 1917-1959; Art Deco 888 Grand Concourse by Emery Roth with mosaic/terrazzo vestibule; 1150 Grand Concourse "fish building" mosaic. | Grand Concourse section |
| same · NYT City Room 2011 | https://archive.nytimes.com/cityroom.blogs.nytimes.com/2011/10/25/the-grand-concourse-gets-its-due/ | District designated 2011; 78 buildings; half the apartment buildings date from the 1920s. | Grand Concourse section |
| "Parkchester 171 buildings" · parkchesternyc.com / HDC Six to Celebrate / Crain's | https://www.parkchesternyc.com/about-us/history/ ; https://6tocelebrate.org/site/apartment-buildings/ ; https://www.parkchesternyc.com/wp-content/uploads/2018/10/Crains-Parkchester-1.pdf | 12,271 apartments in 171 red-brick buildings in 51 clusters, 7 to 13 stories, 129 acres; condos, some owner-occupied, some rented. | Parkchester section |
| "Riverdale Spuyten Duyvil co-op" · CityRealty / Brick Underground / NYT | https://www.cityrealty.com/nyc/spuyten-duyvil/the-burton-2550-independence-avenue/61589 ; https://www.brickunderground.com/buy/spuyten-duyvil-guide-real-estate-restaurants-things-to-do ; https://www.nytimes.com/interactive/2026/05/14/realestate/bronx-riverdale-spuyten-duyvil-apartments.html | The Burton, 2550 Independence Ave: 7-story, 142-unit postwar co-op; River Point Towers at 555 Kappock St is a mid-century co-op high-rise; Riverdale has a stock of large postwar co-ops. | Riverdale section (building types only, not clients) |
| "Amalgamated Housing" · Wikipedia | https://en.wikipedia.org/wiki/Amalgamated_Housing_Cooperative | 11 residential buildings, 1,468 units (2024), core of Van Cortlandt Village. | Co-op section |
| "Bronx Point Phase 1" · NYC Housing Connect | https://housingconnect.nyc.gov/PublicWeb/details/3663 | Newly constructed 432-unit residential project in Mott Haven. | Mott Haven section |
| "Bronx senior supportive housing" · NYC Mayor's Office / Governor / Bronx BP 2025 report | https://www.nyc.gov/mayors-office/news/2025/06/mayor-adams-governor-hochul-completion-117-unit-senior-housing-development-the-bronx ; https://www.governor.ny.gov/news/governor-hochul-announces-completion-86-million-affordable-and-supportive-housing-development ; https://bronxboropres.nyc.gov/newsroom/Reports/2025%20Annual%20Development%20Report%20Final.pdf | YP Senior Residence 117 affordable/supportive senior units; Baez Place 154 units incl. 86 supportive; Starhill Phase 2, 49 Featherbed Lane, 244 units incl. 75 supportive. | Supportive/senior section |
| "Bronx tenants elevator" · News 12 / ABC7 | https://bronx.news12.com/elevator-outage-forces-tenants-to-climb-roof-or-several-flights-of-stairs ; https://abc7ny.com/post/bronx-apartment-building-problems-have-tenants-concerned-crime-rodents-broken-elevators/15134408/ | Bronx tenant reports about broken elevators and building security/trespassing in Highbridge building. | Context only: elevator uptime matters, our system must never be the cause of an outage |
| "key fob" · Reddit r/NYCapartments | https://www.reddit.com/r/NYCapartments/comments/1wfs0ny/why_are_some_people_against_key_fobs_to_enter/ | Tenants questioning whether a landlord can force fob use not in the lease; some tenants unhappy. | LL63 / tenant communication section |
| "elevator fob delivery" · Reddit r/doordash_drivers | https://www.reddit.com/r/doordash_drivers/comments/11vysk0/all_for_an_080_tip_she_lives_in_a_building_where/ | Drivers frustrated by buildings where an elevator fob is needed; resident must come down. | Intercom floor release section |
| Silo research (DOB BB 2022-010, LL63, NYS Elevator Safety Act, IPVM, r/accesscontrol) | see silo-wide findings | Reused for fire recall, privacy and relay-count framing. | Who does what, LL63, cost drivers |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env) | — |

### Questions used on this page
- FAQ: Our apartment house is inside the Grand Concourse Historic District. Do landmark rules affect where an elevator reader can be mounted?
- FAQ: Half the block seems to know the code on our Bronx building's elevator keypad. What does it take to upgrade to individual credentials?
- FAQ: When the elevator reader in a Bronx building goes dark, should the property manager call the elevator company or a security contractor first?
- FAQ: Our Bronx building still has an old audio intercom with handsets in every apartment. Can it release a visitor's floor, or does it need replacing first?
- FAQ: If we install a video intercom in the lobby of our Mott Haven rental, can the same app run the elevator floors too?
- FAQ: We locked our Bronx building's elevator, but residents still find strangers on the stairs and at the roof door. What else does the building need?
- FAQ: The elevator company just modernized our Bronx building's cars. Does that make adding readers easier, and should we have waited?
- FAQ: Can one contractor handle the lobby door, the intercom, the cameras and the elevator readers for a rent-stabilized Bronx building?
- FAQ: How does a Bronx development with dozens of buildings keep one credential list instead of a separate one in every lobby?
- FAQ: Our Bronx complex has many separate lobbies with one elevator each, and a few already have different readers. Should every lobby end up with the same model?
- FAQ: In a Bronx supportive housing building, can case managers reach every floor while residents reach only their own floor and the lounges?
- FAQ: Our Riverdale co-op's elevator opens straight into the garage. Can we stop anyone except residents with parking from calling the car there?
- FAQ: Is there an Abstract Enterprises Security Systems office in the Bronx, and how quickly can a survey be booked?
- (No question-style headings outside the FAQ; H2s used: How to Upgrade Elevator Access Control in an Older Bronx Building; Who Repairs Elevator Access Control Systems in the Bronx...; Integrating Elevator Access Control With the Lobby Intercom...; How to Stop Unauthorized People From Using the Elevator...; How to Secure Elevator Access in a Bronx Building...)

## Staten Island (elevator-access-control-installation-staten-island) — research, Nov 16 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| silo research (NYC hub) · HPD 2023 NYCHVS | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2023-nychvs-selected-initial-findings.pdf | Staten Island 10% of homes (18,470 units) in elevator buildings vs 46% citywide, 77% Manhattan. | Numbers table; intro to market |
| "Urby Staten Island Stapleton apartments" · Firecrawl search | https://www.urby.com/location/staten-island | Studios/1BR/2BR near Stapleton station and ferry; amenities: courtyard, pool, gym, WFH mezzanine, welcome desk. No unit count, no fob/elevator detail. | North Shore rentals (general) |
| same · Architonic | https://www.architonic.com/en/pr/urby-staten-island/5103647 | 571 apartments in phase 1 (900+ planned); open mezzanine from elevators; residents-only area behind both entrances leading to elevators. | Numbers table; North Shore rentals |
| "Urby 571 apartments" · Field Condition | https://www.fieldcondition.com/blog/2016/8/23/urby-staten-island | Two buildings, 571 apartments, 115 affordable. | Numbers table |
| "Grymes Hill co-op elevator" · Firecrawl search → Homes.com / statenislandrealty | https://www.statenislandrealty.com/the-fountains-at-clove-lake-1000-1100-clove-rd-staten-island | 1000 & 1100 Clove Rd: two high-rise co-op buildings by Clove Lakes Park, modernized elevators, doorman, parking; 1100 Clove Rd 142 units (Homes.com). | Co-ops building type (named as building stock, not client) |
| same · Staten Island Advance (silive), Jan 29 2009 | https://www.silive.com/northshore/2009/01/coops_and_condos_hot_propertie.html | North Shore co-op/condo stock: prewar six-story elevator condos at 200 & 215 Hart Blvd (Silver Lake); 7-story buildings 55 Austin Pl (Tompkinsville); Grymes Hill co-ops (Howard Ave, Seth Ct, Narrows Rd N); St. George Bay Street Landing; 1000/1100 Clove Rd high-rises. | Small buildings; co-ops building type |
| same · Casa Belvedere | https://casa-belvedere.org/history-of-grymes-hill/ | Grymes Hill Manor Estates built 1953 as rentals, co-op 1983, 152 apartments on Seth Court. | Background (not quoted) |
| "Hylan Boulevard co-op" · silive Jan 2009 East Shore | https://www.silive.com/eastshore/2009/01/disparity_defines_coop_condo_s.html | Condos at the foot of Hylan Blvd in Rosebank near the waterfront. | East Shore building type |
| "Lighthouse Point St. George" · Governor's office | https://www.governor.ny.gov/news/governor-hochul-celebrates-completion-200-million-lighthouse-point-mixed-use-development | 115 residential units (30 affordable), ~60,000 SF commercial (CSI tech incubator, childcare, fitness), 274 parking spots; completed June 5 2025. | Numbers table; North Shore rentals; garage landing readers |
| same · Corcoran | https://www.corcoran.com/new-developments/for-rent/st-george/5-bay-street/32912631 | 5 Bay Street, 115-unit rentals on the harbor next to the ferry terminal. | Numbers table |
| "Staten Island senior housing" · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-completion-270-unit-affordable-and-supportive-housing-development | 12-story, 270-unit building; 138 apartments for formerly unhoused seniors with services; 10,000 SF retail. | Numbers table; senior housing |
| same · Selfhelp | https://selfhelp.net/project/the-pearl/ | The Pearl, 475 Bay Street, completed May 2024. | Senior housing (address) |
| same · HPD Dec 30 2024 | https://www.nyc.gov/site/hpd/news/048-24/new-year-new-homes-staten-island-plan-transform-sanitation-garage-232-affordable | Hillside Grove, 539 Jersey St: 232 affordable homes, three 4- and 5-story buildings incl. 90-home senior building; Bay Street rezoning site. | Numbers table; senior housing; low-rise one-car case |
| "Stapleton housing" · NYC Mayor's Office May 12 2025 | https://www.nyc.gov/mayors-office/news/2025/05/mayor-adams-nycedc-developers-over-500-new-housing-units-stapleton-advancing | 500+ mixed-income homes, 25% affordable, Front & Canal Sts (Artimus, Phoenix Realty); North Shore Action Plan: 2,400 homes. | Numbers table; new construction |
| "Bay Street Corridor rezoning" · NYC DCP | https://www.nyc.gov/content/planning/pages/our-work/plans/staten-island/bay-street-corridor-neighborhood-plan | Approved June 26 2019; manufacturing zoning since 1961 between Tompkinsville Park and Tappan Park → mixed-use. | Numbers table; mixed-use buildings |
| "Staten Island office Teleport" · PANYNJ | https://www.panynj.gov/port-authority/en/building-the-region/office-commercial-facilities.html | Teleport: 100 acres, five Class A office/specialized buildings, ~700,000 SF. | Numbers table; offices |
| same · Untapped Cities / NY Senate (2017) | https://www.untappedcities.com/330000-square-foot-office-building-on-staten-islands-teleport-campus-breaks-ground-in-nyc/ | Corporate Commons Three, 330,000 SF; ~20% for medical office. | Medical buildings |
| same · Corporate Park of Staten Island | https://officespacestatenisland.com/ | Markets office space suited to medical, education, therapy uses. | Offices |
| "Staten Island courthouse St. George" · NY Courts / DCAS | https://www.nycourts.gov/courts/13th-judicial-district ; https://www.nyc.gov/site/dcas/business/dcasmanagedbuildings/staten-island-supreme-courthouse.page | Courthouses at 26 Central Ave and Richmond Terrace in St. George. | St. George civic district (general; government buildings explicitly excluded) |
| "Staten Island Sandy co-op flooding" · silive Apr 2013 | https://www.silive.com/news/2013/04/staten_island_sandy_victims_su.html | Ten residents of a St. George co-op sued over first-floor flood damage from Sandy. | Flood section; FAQ on panel placement |
| silo research | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Added devices must not impede operation; inoperative on Phase I/II. | Fire section; myths |
| silo research | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63: consent, privacy policy, 90-day deletion. | LL63 section |
| silo research | https://ipvm.com/reports/elevator-access-control-examined ; r/accesscontrol thread | Car-enable vs floor lockout; relays = floors × cars × stations. | How it works; floor control |
| "reddit statenisland key fob elevator" · Firecrawl search | — | EMPTY (no Staten Island thread surfaced; only generic r/NYCapartments and r/unpopularopinion fob threads, not used). | — |
| "silive senior building elevator broken" · Firecrawl search | — | No Staten Island-specific result (only out-of-state stories); not used. | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $1,650 per car, Level 2 from $2,750 per car (Staten Island rate), Level 3 quoted per building. Hospitals (SIUH, RUMC) named only as neighborhood anchors, explicitly not as clients.

### Questions used on this page
- What is elevator access control, in plain terms, for a Staten Island co-op that has never had it?
- How does a fob reader in a single-car Staten Island elevator actually stop a stranger from riding up?
- What is floor access control, and does a five-story Staten Island building ever need it?
- What does installing elevator access control in a Staten Island building involve, from survey to first ride?
- Who installs elevator access control on Staten Island, and who does the elevator company's part?
- Can we keep the roof and boiler-room floors off-limits on our Staten Island building's elevator while every other floor stays open?
- What would a six-story Staten Island co-op with two cars pay to start with fob readers in both elevators?
- Where should the elevator access panel go in a Staten Island building that flooded during Sandy?
- Is a Level 1 reader in the car enough for a small Staten Island elevator building, or do we need floor-by-floor control?
- Is face recognition in the elevator worth the higher Level 2 price for a Staten Island building?
- Can a self-managed Staten Island co-op run the elevator credentials itself without a managing agent?
- How far ahead should a Staten Island building book the survey so the elevator company's connection fits its schedule?
- What happens to our Staten Island building's elevator readers when the elevator company runs its periodic inspection or tests?
(No other headings on the page end in "?".)
