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


## Nassau County (elevator-access-control-installation-nassau-county) — research, Nov 17 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Nassau County co-op apartment buildings elevator Great Neck Garden City Long Beach" · Firecrawl search → DeVito Team (Keller Williams Greater Nassau), OneKey MLS compilation Aug 18 2026 | https://thedevitoteam.com/coops-and-condos/nassau-county-coops/high-rise/ | Only 9 Nassau co-op developments of 7+ storeys: The Wychwood, Great Neck Plaza (built 1929, 7 storeys); Long Beach 8 — Lafayette Terrace (1966, 7), Long Beach Terrace (1965, 9), Neptune Towers (1968, 9), Oakwood House (1965, 7), Sea Pointe Towers (1987, 10), Sherwood House (1965, 7), Surfside (1968, 7), Watersedge (1967, 7). 4–6 storey mid-rises excluded from that list. | Numbers table; "where the buildings are"; Long Beach building type |
| same · Homes.com Nassau co-op listings | https://www.homes.com/nassau-county-ny/co-ops-for-sale/ | Elevator co-op listings on Shore Rd and E Broadway (Long Beach), Beach Rd and Grace Ave (Great Neck); "elevator building, laundry room, storage and bike". | Background (street names) |
| same · Leatherman Homes buyer guide | https://leathermanhomes.com/blog/co-ops-for-sale-in-nassau-county | Co-op buildings concentrate near LIRR stations in walkable downtowns. | Background |
| "Long Beach NY oceanfront condo Hurricane Sandy elevator flooding" · Habitat Magazine, Nov 7 2012 | https://www.habitatmag.com/Publication-Content/Building-Operations/2012/2012-November/Hurricane-Sandy-Long-Beach-Co-op-Condo-Cleanup | Alexander Wolf & Co.: four managed Long Beach buildings lost ground floors; 840 Shore Road ground and first floors flooded; Ocean Club condo lost first floor, pool, heating systems, gym, lobbies; 25 Neptune Blvd lobby and super's apartment flooded, boiler room under 15 feet of water; Oceanside buildings without power, largely senior residents. | Flood section; FAQ on panel height |
| "Mineola transit-oriented development apartment building" · Firecrawl search → LIBN Aug 1 2023 | https://libn.com/2023/08/01/85m-transit-oriented-development-advances-in-mineola/ | $85M TOD: 119 apartments in an eight-story building on a 0.64-acre site across from the Mineola LIRR station. | Numbers table; station rentals |
| same · Burman RE | https://www.burmanre.com/work/residential | The Bridge at Mineola: 101 units, $130M, directly across from the Mineola LIRR station. | Station rentals |
| same · Vision Long Island (Facebook post) | https://www.facebook.com/visionlongisland/posts/mineola-transit-oriented-development-project-advances-planned-locallythe-bridge-/1421490393341488/ | 106 condo units planned at 530 West Broadway; two-story structure above a mezzanine connecting two buildings. | Station condos (two buildings joined — multiple cars) |
| same · Patch | https://patch.com/new-york/mineola/downtown-mineola-77m-housing-project-boost-western-nassaus-economy-0 | 266-unit apartment building at 199 2nd St, about 27 affordable units, underground parking. | Numbers table; garage stop |
| same · Aurora Contractors | https://auroracontractors.com/projects/mineola-residences/ | Mineola Residences: 112 units, 67 one-bedrooms. | Background |
| "Westbury transit-oriented development 187 apartments" · LIBN Sept 4 2026 / Aug 6 2026 / Apr 7 2025 | https://libn.com/2026/09/04/westbury-approves-100m-transit-oriented-development/ | Westbury Village Board unanimously approved Gotham's $100M TOD on a former MTA lot at Westbury LIRR station — MTA's first TOD on Long Island. Westbury created a downtown zoning district in Dec 2019 covering ~50 acres near the station; Alpine Residential's $97M 187-unit TOD across from the station. Instagram (Westbury) says construction expected to begin 2027. | Numbers table; new construction section; "decide access early" |
| same · r/longisland | https://www.reddit.com/r/longisland/comments/1koazwc/industrial_site_to_become_187unit_apt_complex_in/ | Thread on the industrial site becoming the 187-unit complex in Westbury's TOD district. | Corroboration only |
| "Garvies Point Glen Cove condo rental buildings" · LIBN Apr 26 2019 | https://libn.com/2019/04/26/long-awaited-1-3b-garvies-point-project-finally-takes-shape/ | $1.3B Garvies Point; a 350-unit condo building of nine stories of residences over two stories of parking planned on the western end. | Glen Cove waterfront type; garage levels |
| same · garviespoint.com | https://garviespoint.com/ | Garvies Point Glen Cove: The Beacon condominium residences, Village Square luxury rentals, Harbor Landing. | Glen Cove type (names) |
| "Nassau County affordable senior apartments elevator" · Governor's office / NYHC | https://thenyhc.org/projects/the-allan-and-geraldine-rosenberg-residence/ | Allan and Geraldine Rosenberg Residence, Freeport (Selfhelp Realty Group): five stories, 44 one-bedroom apartments plus one two-bedroom for an on-site manager, all affordable. | Senior housing type |
| same · Governor's office / HCR | https://hcr.ny.gov/news/governor-hochul-announces-completion-72-million-affordable-and-supportive-housing-development | Estella Housing, Village of Hempstead: $72M, new five-story building, 95 affordable units, supportive housing. | Supportive housing type; numbers table |
| same · North Hempstead Housing Authority | https://northhempsteadhousingauthority.com/senior_disabled_housing.html | Homestead Senior Apartments: building with elevator access to all levels, completed 1979, 98 studio/1-bedroom units. | Senior housing type (older elevator) |
| "Garden City Franklin Avenue medical office building" · NYU Langone location directory | https://nyulangone.org/locations/directory/nassau-county | Multi-suite medical buildings on Franklin Ave, Garden City (1000, 1111, 1300 with suites LL2/ML2/ML6/UL3A, 1401) and 120 Mineola Blvd Suite 550, 200 Old Country Rd Mineola. | Medical corridor type (named as corridor only, not as clients) |
| same · NYU Langone | https://nyulangone.org/locations/nyu-langone-hospital-long-island | NYU Langone Hospital—Long Island: 591-bed medical center in Mineola. | Medical corridor anchor (not a client) |
| "Nassau County Fire Marshal plan review fire alarm permit" · Nassau County | https://www.nassaucountyny.gov/DocumentCenter/View/1590 | NCFM Contractors Guide to Plan Submission (2013): requires a completed Fire Alarm Plan Approval Application and Fire Alarm Permit Application. No mention of elevator recall or access control interfaces. | Permits section (fire alarm side handled by the alarm contractor) |
| same · Nassau County Fire Marshal | https://www.nassaucountyny.gov/DocumentCenter/View/47105/Clean-Agent-Fire-extinguishing-System-Contractors | Office of the Fire Marshal, 1194 Prospect Avenue, Westbury, NY 11590. | Permits section |
| same · NCFM Annual Report 2021 | https://www.nassaucountyny.gov/DocumentCenter/View/37051 | Office enforces the Nassau County Fire Prevention Ordinance and the Uniform Fire Prevention and Building Code of NYS; performs plan review and oversees new commercial construction. | Permits section |
| "Nassau County villages building department" · Nassau County | https://www.nassaucountyny.gov/3406/Cities-Towns-Villages | 2 cities (Long Beach, Glen Cove), 3 towns (Hempstead, North Hempstead, Oyster Bay), 64 incorporated villages, 100+ unincorporated areas. | Permits section; coverage section |
| same · Nassau County building permits page | https://www.nassaucountyny.gov/3482/Building-and-Zoning-Permits | Building permits are issued by the city, town or village — call them directly. | Permits section |
| same · ozgc.com | https://ozgc.com/nassau-county-building-permits/ | Nearly every one of the 64 villages runs its own building department, inspectors and code. | Permits section |
| same · ecode360 Village of Floral Park | https://ecode360.com/print/FL0046?guid=9459857 | Village Superintendent of Buildings must hold NYS Uniform Code code-enforcement qualifications; reviews permits and COs. | Permits section (example) |
| "New York State biometric privacy law" · NY Senate | https://www.nysenate.gov/legislation/bills/2025/S1422 | S1422A "Biometric Identifier Privacy Act" — a bill (passed Senate 06/06/24 in prior session), not enacted law; would require written retention/destruction policy. | Privacy section (described as pending, not law) |
| same · Baker Donelson biometrics chart (May 2025) | https://www.bakerdonelson.com/webfiles/Publications/Global-Biometrics-Laws-Chart.pdf | NY Labor Law § 201-a: employers may not require employees to be fingerprinted as a condition of employment; voluntary fingerprinting permitted. | Privacy section (staff fingerprints) |
| same · Holland & Knight | https://www.hklaw.com/en/insights/publications/2021/08/nyc-passes-biometric-data-protection-laws-aimed-at-businesses | NYC's Tenant Data Privacy Act / biometric law are city laws (NYC residents/buildings). | Privacy section: LL63 is NYC-only |
| silo research (LI hub) · NYS DOL | https://dol.ny.gov/elevator-licensing-information | Labor Law Article 33: licensed businesses/workers for elevator installation, maintenance, repair. | Who does what |
| silo research · ASME A17.1 2.27.3 via NYC DOB BB 2022-010 | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Added devices must not impede operation and must go inoperative on Phase I/II firefighters' service — cited as the ASME A17.1 rule (NYS code also adopts A17.1), not as a Nassau rule. | Fire section |
| silo research · IPVM / r/accesscontrol | https://ipvm.com/reports/elevator-access-control-examined | Car-enable vs floor lockout; relays scale floors × cars × stations. | How it works |
| "reddit longisland apartment key fob elevator" · Firecrawl search | — | EMPTY (no Long Island thread; only r/NYCapartments, r/unpopularopinion, r/AskNYC fob threads — not Nassau, not used). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $1,725 per car, Level 2 from $2,875 per car (Nassau rate from the Long Island hub), Level 3 quoted per building. NYU Langone and Franklin Avenue buildings named only as landmarks, explicitly not as clients. No Nassau building named as a customer.

### Questions used on this page
- What does elevator access control actually change for residents of a Nassau County co-op?
- Can a Long Beach oceanfront building keep its elevator access panel safe from another storm surge?
- Do we need a permit from our village to add elevator readers in Nassau?
- Who is allowed to wire our readers into the elevator controller in Nassau County?
- How many relays does a two-car station rental in Mineola or Westbury typically need for floor restriction?
- Does New York City's Local Law 63 apply to a Garden City or Great Neck building that adds elevator fobs?
- Can staff in a Nassau medical or office building be required to use fingerprint readers in the elevator?
- How do home health aides get up in a Nassau senior building once the elevator needs a credential?
- What would a seven-story Nassau co-op with two cars pay to start with fob readers in both?
- Should a Nassau building under construction decide on elevator access before the elevators are ordered?
- Can a reader at our garage call button stop people walking down the ramp and calling the elevator?
- Will our Nassau building's elevator readers still let the fire department take the cars?
- Our fobs work at the front door but not in the elevator since our old installer stopped answering. Can you help in Nassau?
- How soon can someone come out to survey an elevator in Nassau County?
(No other headings on the page end in "?".)


## Suffolk County (elevator-access-control-installation-suffolk-county) — research, Nov 17 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Suffolk County population towns" · Firecrawl search → US Census QuickFacts | https://www.census.gov/quickfacts/suffolkcountynewyork | 2020 Census population 1,525,920; 1,674.7 people per square mile. | Numbers table; intro |
| same · Suffolk County open data | https://opendata.suffolkcountyny.gov/datasets/census-designated-place/about | Ten towns and two Native American reservations in Suffolk County. | Numbers table; code-by-town section |
| same · Wikipedia (village list only) | https://en.wikipedia.org/wiki/Suffolk_County,_New_York | Incorporated villages incl. Lake Grove, Islandia, Westhampton Beach, Sag Harbor; fourth-most populous NY county, most populous outside NYC. | Background (village examples) |
| "Patchogue downtown apartments" · Firecrawl search → TRITEC | https://tritecre.com/project/new-village/ | New Village at Patchogue: 291 apartment homes, 45,000 SF retail, 17,000 SF office. | Numbers table; downtown rentals |
| same · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-groundbreaking-160-million-carriage-house-development-downtown | The Carriage House, W. Main St, Patchogue: $160M, 262 homes (53 affordable), two five-story buildings, 455,000 SF, split by the Patchogue River with a riverwalk; Nord Development Group and ACRE. | Numbers table; two-building TOD example; FAQ two buildings one system |
| same · Conifer | https://coniferllc.com/properties/conifer-village-at-patchogue-senior-apartments/ | Conifer Village at Patchogue senior apartments, 1BR/2BR leasing. | Senior housing (named only as building type example) |
| "Ronkonkoma Hub phase apartments" · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-groundbreaking-phase-two-state-art-new-ronkonkoma-hub | Phase two: $256M, 388 housing units, 73,000 SF commercial, 15,500 SF office. | Numbers table; TOD rentals |
| same · TRITEC Station Yards | https://tritecre.com/project/station-yards/ | Station Yards master plan: 1,450 apartment units. | Numbers table |
| LI hub research (Nov 14) · LongIsland.com | https://longisland.com/news/09-05-19/first-phase-of-ronkonkoma-hub-apartment-complex-opens.html | Alston Station Square: 245 units in two buildings, opened Sept 5 2019. | Numbers table |
| "Wyandanch Rising apartments" · NY Housing Conference | https://thenyhc.org/projects/wyandanch-village-wyandanch-rising/ | Two mixed-income buildings with 177 units built; third, 124-unit building in progress (at time of writing). | Numbers table; affordable rentals |
| same · Long Island Business News, Sep 11 2025 | https://libn.com/2025/09/11/affordable-apartments-wyandanch-village/ | Applications open for 202 affordable apartments in a soon-to-be-completed 218-unit building in Wyandanch Village. | Numbers table; lease-up FAQ |
| LI hub research · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-completion-40-million-affordable-senior-housing-development-suffolk | 11 Park Drive Apartments, Wyandanch: 94 affordable units for 62+, five stories, Oct 2022. | Senior housing section |
| "Huntington Station apartments new development" · Governor's office | https://www.governor.ny.gov/news/governor-hochul-announces-completion-24-million-53-unit-affordable-housing-development-seneca | Huntington Apartments (Home Leasing): 53 affordable apartments incl. 27 with supportive services for veterans; historic 19th-century building transformed. | Supportive housing; historic-building retrofit |
| same · Preservation League of NYS | https://www.preservenys.org/blog/excellence-award-spotlight-huntington-apartments | 201 Fall Street; 53 apartments incl. 27 permanent supportive. | Same (address) |
| same · Avalon | https://www.avaloncommunities.com/new-york/huntington-station-apartments/avalon-huntington-station/ | Avalon Huntington Station rentals (2BR/3BR, lofts). | Named as building-type example only |
| "Riverhead downtown apartments" · RiverheadLOCAL, May 30 2025 | https://riverheadlocal.com/2025/05/30/heatherwood-celebrates-groundbreaking-of-downtown-riverhead-apartment-building/ | Heritage on Main (Heatherwood), East Main St: five stories, 165 market-rate units (52 studios, 80 1BR, 33 2BR), 7,910 SF ground-floor commercial/amenity/leasing, 155 parking stalls, between East End Arts and Riverview Lofts; ~2 years construction. | Numbers table; East End section; Q&A |
| same · Riverhead News-Review, Mar 2026 | https://riverheadnewsreview.timesreview.com/2026/03/132676/town-approves-zenith-groups-bid-to-expand-downtown-apartment-project/ | Town Board on March 17 approved Zenith Group expansion to five stories, 15 apartments. | Small mixed-use buildings section |
| "Lindenhurst downtown apartments" · BLD | https://bldnow.com/bld-projects/lindenhurst-multi-family-residential-project/ | Proposed Lindenhurst buildings: 5 stories, 172 apartments over ground-level retail and parking. | Numbers table; garage stop |
| same · NY Forward Strategic Investment Plan | https://www.ny.gov/sites/default/files/2024-05/NYF_1_Lindenhurst_Strategic_Investment_Plan.pdf | Downtown Lindenhurst is mixed-use around Wellwood Ave. | Mixed-use section |
| "Stony Brook Medicine medical office" · Stony Brook Medicine | https://www.stonybrookmedicine.edu/advancedspecialtycare/grandopening | Advanced Specialty Care, 500 Commack Road: 30+ specialties, nearly 120,000 SF. | Medical buildings section (named as type anchor, not a client) |
| same | https://www.stonybrookmedicine.edu/advancedspecialtycare/lakegrove | Advanced Specialty Care at Lake Grove, ~170,000 SF at full build-out. | Medical section |
| LI hub research · Stony Brook University policy | https://stonybrook.edu/policy/_policies/physical-and-electronic-access-control-policy.html | Office of Access Control and Lock Shop has sole responsibility for design, installation and maintenance of electronic card access on campus. | Campus section: we don't work on SUNY campus systems; off-campus private buildings only |
| "Melville office building" · Realmo listing | https://realmo.com/listing/3-huntington-quadrangle-melville-ny-11747/13001205 | 3 Huntington Quadrangle, Melville: ~400,000 SF, renovated lobby, corridors, elevators. | Office section |
| same · LIBN Feb 2 2023 | https://libn.com/2023/02/02/town-revives-plan-to-rezone-lis-corporate-center-for-live-work-redevelopment/ | Town of Huntington revived plan to rezone Melville corporate center for live/work redevelopment; 560 Broadhollow Rd 52,000 SF office bought Nov 2021. | Office-to-residential conversion section |
| "Hauppauge Industrial Park" · RPA | https://rpa.org/reports/hauppauge-industrial-park-economic-opportunity-analysis | ~1,300 companies, 55,000+ employees; largest park in the Northeast. | Office/flex section |
| same · HIA-LI | https://www.hia-li.org/li-iph/ | "Long Island Innovation Park at Hauppauge", ~1,350 companies, 55,000 employees. | Same |
| "Suffolk fire marshal plan review" · Town of Brookhaven | https://www.brookhavenny.gov/304/Fire-Prevention | Division of Fire Prevention inspectors are NYS-certified; commercial buildings not requiring annual inspection are inspected at least every three years. | Code-by-town section |
| same · Brookhaven permit requirements PDF | https://www.brookhavenny.gov/DocumentCenter/View/1021/Permits-Submission-Requirement-PDF | All Division of Fire Prevention permits applied for on online portal (rev. 3/11/2025). | Code-by-town section |
| same · Town of Islip Fire Marshal's Office | https://islipny.gov/community-and-services/documents/departments/fire-prevention-bureau/211-permit-submission-requirements/file | Islip Fire Marshal's Office, 24 Nassau Ave, Islip; permit submission requirements (updated 5/30/25). | Code-by-town section |
| same · Town of Huntington Fire Prevention FAQ | https://www.huntingtonny.gov/content/13749/114570/114580/117979/default.aspx | "The licensed concern contracted to install such equipment must apply for a construction permit from the Bureau of Fire Prevention"; inspection witnessed by a Fire Marshal. | Code-by-town section; fire alarm interface FAQ |
| "Suffolk senior apartments elevator broken" · NBC New York, Apr 23 2025 | https://www.nbcnewyork.com/video/on-air/as-seen-on/residents-at-long-island-senior-facility-stranded-due-to-broken-elevator/6236454/ | Residents of an East Patchogue senior facility stuck because a broken elevator had not been repaired. | Senior section: why access hardware must never add downtime |
| silo research · NYS DOL | https://dol.ny.gov/elevator-licensing-information | Labor Law Art. 33: elevator contractors and mechanics licensed by NYS DOL. | Who does what |
| silo research · NYS DOS Existing Building Code draft | https://dos.ny.gov/2024-03-19ebcnrd-documentdraft-version-30 | Altered elevator elements comply with ASME A17.1; elevators on the same hall call treated alike. | Two-car banks |
| silo research · NYC DOB BB 2022-010 (principle only, ASME A17.1 2.27.3) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Added cab/hall devices must not impede operation and go inoperative on Phase I/II. Cited as the ASME principle, not as Suffolk law. | Fire section |
| silo research · IPVM / r/accesscontrol | https://ipvm.com/reports/elevator-access-control-examined | Car-enable vs per-floor relays; relays scale floors × cars × stations. | How it works |
| "reddit longisland key fob elevator" · Firecrawl search | — | EMPTY (no Suffolk thread surfaced; only NYC/r/unpopularopinion threads, not used). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $1,800 per car, Level 2 from $3,000 per car (Suffolk rate, from the Long Island hub), Level 3 quoted per building. LL63 noted as NYC-only, not applied. Stony Brook Medicine and SUNY named only as building-type anchors, explicitly not clients.

### Questions used on this page
- Our Patchogue rental has a garage under the building. Should the reader go at the garage call button, in the car, or both?
- What does a Level 1 elevator reader cost per car in Suffolk County?
- Why is the Suffolk price higher than the price for buildings in the city?
- Which office do we talk to about permits: the town, the village, or the county?
- Does New York City's Local Law 63 apply to fobs in a Suffolk apartment building?
- Can the Town of Huntington fire marshal stop our elevator project?
- Our Suffolk rental is two separate five-story buildings with their own elevators. Can one resident credential work in both?
- How do we give a home health aide elevator access to one resident's floor without giving out a resident fob?
- Will an elevator reader slow down paramedics at a Suffolk senior building at night?
- Our Melville office building has tenants on three different badge systems. Can the elevators read them all?
- What happens to the elevator readers after a hurricane knocks out power for days?
- We are converting an older Hauppauge or Melville office building to apartments. When should the elevator access be planned?
- Can you program floor changes remotely so you do not have to drive out to Riverhead for every update?
- Is a face-recognition reader worth it for a two-story Suffolk medical office?
- How long does a Suffolk elevator access project take from the first call to the first ride?
(No other headings on the page end in "?".)


## Westchester County (elevator-access-control-installation-westchester-county) — research, Nov 17 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Yonkers downtown new apartment tower elevator rental units 2025" · Firecrawl search → New York YIMBY | https://newyorkyimby.com/2024/12/miroza-tower-tops-out-at-44-hudson-street-in-yonkers.html | Miroza Tower, 44 Hudson St, Yonkers: 25 stories, 250 rentals, on-site garage for 222 vehicles + 25-space off-site lot; fitness center, rooftop garden, library, playroom, party room; completion expected fall 2025. | Numbers table; Yonkers H3 (garage problem) |
| same · Yonkers IDA | https://yonkersida.com/completed-projects/page/11/ | Park Vista @ Croton Heights: six-story, 60-unit rental (excerpt). | Yonkers H3 (older smaller rentals) |
| same · Elevator World / Facebook (Hudson Piers, Hudson 44) | https://elevatorworld.com/news/daily-news/developers-promote-design-for-mixed-use-tower-in-yonkers/ | Miroza: 250 rental units, small commercial ground floor. Hudson Piers excerpt only (not used). | Background |
| "New Rochelle downtown development apartments" · Office of the Governor | https://www.governor.ny.gov/news/governor-hochul-announces-completion-more-200-affordable-apartments-new-rochelle | Highgarden Tower, New Rochelle: 19 stories, 219 affordable units, 77 supportive; parking, two community lounges, laundry, gym, storage, playroom; July 25 2024; Georgica Green Ventures with RXR. | Numbers table; New Rochelle H3; supportive buildings; day-in-the-building section |
| same · Pew Charitable Trusts | https://www.pew.org/en/research-and-analysis/articles/2024/11/13/how-more-housing-revitalized-a-suburban-downtown | Downtown rezoning late 2015; ~80,000 residents; housing added at >2x US rate 2017–2021; rents +7% 2017–2023 vs 31% US. | Numbers table; New Rochelle H3 |
| same · City of New Rochelle affordable housing report 2018 | https://www.newrochelleny.gov/DocumentCenter/View/9834/Affordable-Housing-Report-New-Rochelle-62618-FINAL | ~1,200 new market-rate apartments built/approved/proposed (excerpt). | Background (not quoted) |
| "White Plains downtown residential towers" · The New York Times (Dec 23 2015) | https://www.nytimes.com/2015/12/23/realestate/reviving-downtown-white-plains-with-new-places-to-live-and-linger.html | 55 Bank Street: two 16-story residential towers, 561 apartments (search excerpt). | Numbers table; White Plains H3 (twin towers) |
| same · Homes.com | https://www.homes.com/building/trump-tower-at-city-center-white-plains-ny/b-9szm296z09xxt/ | Condominium tower at City Center, White Plains. | White Plains H3 |
| same · Nancy Kennedy Team blog | https://thenancykennedyteam.com/blog/downtown-white-plains-is-adding-thousands-of-homes-almost-none-of-them-for-sale | EMPTY (404 on scrape; search excerpt "more than 5000 downtown apartments built/under construction/planned" not verified, not used). | — |
| "Mount Vernon new apartment building downtown" · NYS HCR (Aug 11 2026) | https://hcr.ny.gov/news/governor-hochul-announces-construction-underway-229-unit-affordable-housing-development | QWest Towers, Mount Vernon West TOD zone: two buildings, 229 apartments, 12 mobility-disability units, 7 sensory-disability units, ~3,300 SF commercial; construction underway; Stagg Group, Simone Development, Rev. Dr. L'Judie Matt-Simmons. | Numbers table; Mount Vernon H3; new-construction section; FAQ |
| same · New York Housing Conference | https://thenyhc.org/projects/115-s-macquesten/ | 115 S MacQuesten Pkwy: 315 residential units in two connected buildings (8-story and ...; excerpt). | Numbers table; Mount Vernon H3 |
| "Journal News Mount Vernon elevator outage" · lohud (May 27 2021) | https://www.lohud.com/story/news/local/westchester/mount-vernon/2021/05/27/mount-vernon-residents-angry-after-five-weeks-no-elevator-horizon-realty/7471506002/ | Six-story Mount Vernon apartment building without its only elevator for 5+ weeks. | Mount Vernon H3 (one-car fragility) |
| same · City of Mount Vernon Facebook (Aug 21 2026) | https://www.facebook.com/mountvernonny/posts/for-immediate-releaseaugust-21-2026mount-vernon-ny-the-city-of-mount-vernon-is-r/1386092890340381/ | City statement on an apartment elevator outage (excerpt only). | Not used |
| "Westchester co-op apartments Hartsdale Scarsdale Bronxville elevator" · Homes.com | https://www.homes.com/hartsdale-ny/co-ops-for-sale/ | Hartsdale co-op listings advertise "elevator building". | Numbers section (co-op layer) |
| same · Reddit r/Westchester | https://www.reddit.com/r/Westchester/comments/1k56tsp/thoughts_on_coops/ | Resident: outside single-family homes, most lower-Westchester for-sale properties are co-ops. | Numbers section (co-op layer) |
| same · Facebook group Westchester914 | https://www.facebook.com/groups/Westchester914/posts/4273392386248914/ | Request for a lower-Westchester co-op/condo without steps for aging parents. | Senior/aging shareholders section |
| "NYS Uniform Code elevator ASME A17.1 Westchester building department" · Town of Greenburgh eCode360 | https://ecode360.com/6816202 | Ch. 170: elevator permit required before material alteration, issued only to installer-permit holder; semiannual inspections; certificate of operation displayed in each car; references ASME A17.1 (1993 ed.) and NYS Uniform Code. | Who-does-what section; FAQ on local approval; after-installation |
| same · Greenburgh Building Dept | https://www.greenburghny.com/441/Elevators-and-Conveyances | Elevator installer-inspector permit and inspection checklists page. | Background |
| same · NYS DOS 2025 PMCNYS notice | https://dos.ny.gov/system/files/documents/2025/07/2025pmcnys_noa_2025-07-24.pdf | 2025 NYS codes reference ASME A17.1-2022/CSA B44-2022. | Who-does-what section; fire section |
| "Valhalla Westchester Medical Center medical office Hawthorne" · WMCHealth | https://www.wmchealth.org/locations/westchester-medical-center-outpatient-clinics-adult ; https://www.wmchealth.org/wp-content/uploads/2025/09/WMC-Patient-Guide.pdf | WMC headquartered in Valhalla; outpatient clinics at 19 Bradhurst Ave Suite 700, Hawthorne; development office 7 Skyline Drive, Hawthorne. Named only as area anchors, not clients. | Medical buildings H3; FAQ |
| "reddit r/Westchester elevator key fob apartment building security" · Firecrawl search | https://www.reddit.com/r/Westchester/comments/1bd4tai/anyone_have_experiences_with_these_apartments_in/ | White Plains apartment thread mentions typical elevator issues (excerpt only). | Not quoted |
| silo research (reused) | research/elevator-access-control-installation.md | Car-enable vs floor lockout; relays = floors × cars × stations; fire service override. | How it works; floor restriction |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $1,875 per car, Level 2 from $3,125 per car (Westchester row of the Hudson Valley hub table), Level 3 quoted per building. Worked examples only multiply those per-car figures. NYC Local Law 63 / DOB stated as NOT applying in Westchester. Brands: install/integrate/service only, no dealer/partner claim.

### Questions used on this page
- Our Yonkers waterfront tower's garage shares elevators with the apartments. What stops someone who walks in behind a car from riding upstairs?
- Does adding a card reader to a Westchester elevator need approval from the town or village building department?
- Do New York City's Local Law 63 tenant data rules apply to a fob or face reader in a New Rochelle or White Plains apartment building?
- Can a single-car Hartsdale co-op start with one fob reader and add floor restriction for the roof and storage floors later?
- How does a visitor reach one apartment in a New Rochelle rental tower when every floor button is locked?
- What does elevator access control cost for a two-car condominium in Bronxville?
- Can a White Plains office building give each tenant company its own floors and let the office manager add new employees?
- Which floors in a Valhalla or Hawthorne medical office building should stay open to patients, and which should be locked?
- We are building a new elevator project in Mount Vernon. What should go on the drawings now so access control is easy later?
- Our Tarrytown co-op still uses a brass key switch in the car for the basement. Is replacing it with a fob output a big job?
- What should happen to a Westchester building's elevator floor restriction when a storm knocks out power?
- Who maintains the elevator readers after installation if our building switches elevator maintenance companies?
- Can our Peekskill senior residence give residents a large-button keypad or a fob instead of a phone app?
- If a resident of our Scarsdale co-op loses a fob late at night, can they still get home in the elevator?
- How soon can Abstract Enterprises Security Systems survey a Westchester building, and which phone line should we call?
(No other headings on the page end in "?".)


## Rockland County (elevator-access-control-installation-rockland-county) — research, Nov 17 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Rockland County NY towns villages population 2020 census housing units" · Firecrawl search → Census QuickFacts | https://www.census.gov/quickfacts/rocklandcountynewyork | 109,999 housing units (July 1 2025, V2025); owner-occupied rate 67.9% (2020–2024); 2020 Census population 338,329; +5.6% 2020–2025. | Numbers table; intro (mostly owner-occupied houses, elevators concentrated in a minority of buildings) |
| same · Census profile | https://data.census.gov/cedsci/profile?g=050XX00US36087 | 173.7 sq mi land area; five towns: Clarkstown, Haverstraw, Orangetown, Ramapo, Stony Point. | Five-towns section; code section |
| "Blue Hill Plaza Pearl River office tower 21 stories" · Firecrawl search → bluehillplaza.com | https://bluehillplaza.com/about/ | 93-acre campus; One Blue Hill Plaza 21-story 550,000 SF; second building six-story (Wikipedia says eight-story — conflict, page says "a second, much lower building"). | Numbers table; offices building type (named only as the county's tallest office landmark, not a client) |
| same · Wikipedia | https://en.wikipedia.org/wiki/Blue_Hill_Plaza | 21-story tower + eight-story building on 90 acres, ~20 miles north of NYC. | Cross-check (conflict on second building height noted) |
| same · CBRE listing | https://www.cbre.com/properties/properties-for-lease/office/details/US-SMPL-158127/blue-hill-plaza-1-blue-hill-plaza-pearl-river-ny-10965 | Advertises 24-hour building access and security. | Offices (multi-tenant towers expect after-hours access control) |
| "Nyack apartment building elevator…" · Firecrawl search → Village of Nyack | https://www.nyack.gov/departments/Housing | Nyack Plaza: 173 units; senior housing in the elevatored tower at Depew Ave & S Franklin Ave; family housing on Depew and Hudson Aves. | Numbers table; senior housing section |
| same · Rockland County Business Journal, Feb 9 2022 | https://rcbizjournal.com/2022/02/09/nyack-developer-hopes-to-build-affordable-disability-accessible-apartment-complex-on-main-street/ | Proposed Main St building with an elevator sized for two wheelchairs, wider halls. | Accessibility discussion (reader height/reach) |
| same · Village planner zoning analysis | https://www.nyack.gov/media/Planning%20Department/Final_Nyack_Phase_1_Zoning_Analysis_of_Potential_Impacts.pdf | ZBA approved 11 new units from six projects in the DMU (downtown mixed-use) zone over two years — small infill. | Village downtown mixed-use section |
| "Nyack Point Apartments Main Street" · Firecrawl search → RentCafe / RHAC | https://nyack-point-apartments.rentcafewebsite.com/ | Nyack Point Apartments, 263 Main St: modern three-story building with community room. | Village downtown section (three-story elevator scale) |
| same · Zillow | https://www.zillow.com/apartments/nyack-ny/diana-place/CkGGX6/ | Diana Place, 259 Main St Nyack, lists an elevator. | Village downtown section |
| "Haverstraw waterfront apartments elevator…" · Firecrawl search → GDC Rentals | https://gdcrentals.com/waterfront/ | The Waterfront at Harbors (Haverstraw): elevator buildings with only two units per floor, indoor garage parking, at the Hudson's widest point. | Waterfront building type; garage hall-call reader; flood/river weather |
| same · Harbors at Haverstraw | https://harborsathaverstraw.com/ | Bills itself as the only waterfront destination community in Rockland County (condos). | Waterfront building type |
| "Rockland County senior housing…" · Firecrawl search → Governor's office, Jun 9 2026 | https://www.governor.ny.gov/news/governor-hochul-announces-start-construction-53-million-affordable-housing-development | 30 West, Village of Haverstraw: $53M, 81 apartments, up to 60% AMI, 20 supportive apartments; parking garage for tenant and public use; rooftop balcony. Construction started Jun 2026. | Numbers table; new-construction section (spec the readers before the elevator is ordered); garage shared with public |
| same · HCR referral list (2024) | https://hcr.ny.gov/system/files/documents/2024/03/referral-list-for-renters-hfa.pdf | Senior buildings incl. West Haverstraw Senior Citizens Apartments (Route 9W) and Maplewood Gardens (Nanuet). | Senior section (named as building stock only) |
| same · HUD USER case study | https://www.huduser.gov/portal/casestudies/study-050624.html | Vincent's Village, Nanuet (Clarkstown): 93 senior units, opened May 2021, on former St. Agatha's Home site; residential buildings two-story. | Senior section (low-rise senior buildings: a single car, often one stop above the lobby) |
| same · Apartments.com | https://www.apartments.com/airmont-gardens-55-senior-apartments-suffern-ny/dy18rgj/ | Airmont Gardens 55+ (Suffern) advertises a two-way entry access system. | Senior section (door intercom exists, elevator often open) |
| "Suffern village apartments new building elevator…" · Firecrawl search → 176 Lafayette | https://176lafayette.com/ | Suffern boutique rental: "secure elevator building with keyless entry and intercom accessibility", surface and garage parking, within half a mile of Suffern station. | Transit/village rentals section |
| same · Esther Gitlow Towers (Facebook / site) | https://www.facebook.com/p/Esther-Gitlow-Towers-61574265449245/ ; https://esthergitlowtowers.org/ | 196 Lafayette Ave, Suffern: senior one-bedrooms; lists controlled access, security system, elevators. | Senior section (Suffern) |
| "Pearl River NY new apartment building downtown units" · Firecrawl → Rockland County Times, May 21 2026 | https://rocklandtimes.com/2026/05/21/new-apartments-proposed-for-pearl-river/ | Sidetrack Properties proposed 109 units on West Jefferson Ave, walking distance to Pearl River Metro-North station (proposal stage). | Numbers table (labelled proposed); new construction |
| same · Town of Orangetown Local Law 13 of 2025 | https://www.orangetown.com/local-law-13-2025-zone-change-77-e-central-ave-80-84-e-washington-ave-pearl-river-adopted-12-2-2025/ | Zone change, 77 E Central Ave & 80–84 E Washington Ave: 20 rental units for 55+ in downtown Pearl River; "Dionne's Way" 16 rental units on Main/William Sts. | Downtown Pearl River 55+ (small elevator buildings) |
| same · Club West at Pearl River | https://www.theclubwestatpearlriver.com/ | 55+ apartment community in Pearl River. | Senior section |
| "Spring Valley NY … apartments" · Firecrawl → Hudson Valley Property Group | https://hudsonvalleypropertygroup.com/spring-valley-renovation-220-units-to-be-modernized-kept-affordable-by-ex-residents-firm/ | Main St Spring Valley lined with apartments over stores; 178-unit Hickory House on Main St is a shareholder co-op. | Co-op section; mixed-use |
| same · lohud gallery, Aug 6 2021 | https://www.lohud.com/picture-gallery/news/local/rockland/2021/08/06/mold-and-water-issues-hickory-house-co-op-spring-valley/5499290001/ | Shareholders raised mold and water issues at Hickory House co-op, North Main St. | Co-op section (water near equipment; panel placement) |
| same · Village of Spring Valley | https://www.villagespringvalley.org/special-permit-land-use-projects | Valley Heights Apartments, 200 N Main St (special permit project). | Spring Valley stock |
| "Rockland County Fire and Emergency Services … Uniform Code" · Firecrawl → Rockland County Buildings & Codes | https://www.rocklandcountyny.gov/departments/buildings-codes | County Office of Buildings and Codes administers and enforces the NYS Uniform Code and Energy Code within the Village of Spring Valley (permits, COs, inspections). | Code section (who is the AHJ differs by village/town) |
| same · eCode360 Rockland County Ch. 23 | https://ecode360.com/38757897 | County Director enforces the Uniform Code for the Village of Spring Valley during the article's effective dates. | Code section |
| same · eCode360 Village of West Haverstraw Ch. 107 | https://ecode360.com/5090758 | Uniform Fire Prevention and Building Code enforced by the Village Fire Safety Inspector. | Code section (village fire inspectors) |
| same · Town of Clarkstown | https://www.clarkstown.gov/weekly-column/clarkstown-code-enforcement-recognized-by-rockland-county-illegal-housing-task-force-2/ | Town code enforcement active; Rockland County illegal housing task force. | Background (not quoted) |
| "New York State elevator mechanic license law Article 33" · Firecrawl → NYS DOL | https://dol.ny.gov/elevator-licensing-information | Since Jan 1 2022, businesses doing design, installation, maintenance, alteration, service and repair of elevators must be licensed by NYS DOL (Elevator Contractor, Elevator Mechanic, inspector licenses, etc.); temporary mechanic licenses from Jun 10 2026. | Who-does-what section; FAQ (ask for the elevator contractor's NYS DOL license) |
| same · NYS Senate, Labor Law Art. 33 | https://www.nysenate.gov/legislation/laws/LAB/A33 | Article 33 "Elevators and other conveyances; licensing", §§950–956. | Who-does-what citation |
| silo research | https://ipvm.com/reports/elevator-access-control-examined | Car-enable vs floor lockout; relays = floors × cars × stations. | How it works; floor control |
| silo research (NYC hub) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Added devices must not impede elevator operation and go inoperative on firefighters' service. Used as the general principle only; NYC bulletins are NOT applied to Rockland as law. | Fire section (principle; local AHJ governs) |
| "reddit Rockland County apartment key fob elevator security" · Firecrawl search | — | EMPTY for Rockland: only r/NYCapartments, r/unpopularopinion, r/accesscontrol generic fob threads. r/accesscontrol note: confirm readers read existing 125 kHz 26-bit fobs if reusing. | Upgrade section (general, attributed to installer forum) |
| "Rockland senior apartment elevator out of service … lohud/dailyvoice" · Firecrawl search | — | EMPTY for Rockland: results were Atlanta, St. Louis, Bronx, Albany. Not used. | — |
| Montefiore Nyack / Good Samaritan Suffern | (HV hub research: https://www.hgar.com/montefiore-expands-healthcare-investment-in-rockland-county-with-new-urology-center) | Montefiore expanding outpatient care in Rockland. Hospitals named only as neighborhood anchors for medical offices, never as clients. | Medical section |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ / Mid-Hudson News | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $1,950 per car, Level 2 from $3,250 per car (Rockland rate, HV hub table), Level 3 quoted per building. NYC Local Law 63 stated as NYC-only (does not apply in Rockland). Hospitals named only as anchors.

### Questions used on this page
- Our Nyack building has three floors and one elevator. Is elevator access control worth it at that size?
- Which Rockland office approves elevator access control work: the town, the village, or the county?
- Does the elevator company that services our Rockland building need a state license to connect our readers?
- Can an elevator reader in our Haverstraw waterfront building keep the garage level for residents only?
- Our Spring Valley co-op still uses a brass key switch in the elevator. What replaces it?
- Will older residents in a Rockland senior building manage a fob, or is a keypad kinder?
- Can home health aides in our Pearl River 55+ building get an elevator credential that expires when the job ends?
- What happens to a Rockland elevator reader during an ice-storm power outage?
- Can we restrict the elevator only at night in our Suffern mixed-use building and leave it open during store hours?
- Our medical office near Nyack has practices on different floors. Can each practice control its own floor?
- We are building a new elevator building in Rockland. When should elevator access control be designed in?
- How long does it take to add elevator access control to a typical Rockland apartment building?
- Is there a monthly fee for a Rockland elevator access system, and can the board run it without one?
(No other headings on the page end in "?".)


## Orange County (elevator-access-control-installation-orange-county) — research, Nov 17 2026

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Orange County NY population 2020 census" · Firecrawl search | https://data.census.gov/profile/Orange_County,_New_York?g=050XX00US36071 | 2020 Census total population 401,310. | Numbers table |
| same · Pattern for Progress | https://www.pattern-for-progress.org/orange-county-population-density-by-census-tract/ | Newburgh, Middletown and Port Jervis are pockets of high population density in the county. | Numbers table; intro |
| "Middletown NY senior housing elevator" · Firecrawl search → scrape (PDF) | https://www.orangecountyny.gov/DocumentCenter/View/117/Affordable-Housing-for-Adults-PDF?bidId | County list of affordable adult housing: elevators named at Middlecrest Crossing II (100, Middletown), Senior Horizons at Silver Lake (84), Southeast Towers (106, 62+/disabled, elevators + keycard access), Monroe Commons (35, elevator + intercom security), Cerone Place (60, Newburgh), High Point (82), Hudson Pointe (65), New Windsor Senior Housing (92), Park Plaza (23, Port Jervis, coded entry), Waters Edge buildings (Port Jervis), Promenade at Tuxedo Place (40), The Cedars (Walden), Rocky Point (44, Washingtonville). 17 complexes list an elevator. | Numbers table; senior building type; area table; FAQ (Southeast Towers keycards → Middletown keycard FAQ) |
| "Garnet Health Medical Center Middletown floors" · Firecrawl search | https://www.garnethealth.org/news/garnet-health-medical-center-celebrates-milestone-anniversary | Seven-story, 383-bed medical center at 707 East Main Street, opened August 5, 2011. | Numbers table; medical buildings (landmark only, not a client) |
| "SUNY Orange Newburgh Kaplan Hall" · Firecrawl search | https://sunyorange.edu/newburgh/ ; https://www.selux.us/usa/en/cases/suny-orange-kaplan-hall | Kaplan Hall 87,000 sq ft, multi-level underground parking garage (1st Street), corner of Grand and First, opened for classes Jan 19, 2014. | Numbers table; campus/garage building type |
| "Newburgh waterfront new apartment building elevator" · Firecrawl search → scrape | https://www.cityofnewburgh-ny.gov/CivicAlerts.aspx?AID=1520 | $6.89M Pro-Housing Supply Fund for infrastructure supporting 200+ mixed-income homes on Liberty Street; $2M for mixed-use next to Washington's Headquarters: 145 units + 10,000 sq ft commercial on a parcel vacant 50+ years; $2M Newburgh Landing. | Numbers table; Newburgh mixed-use type |
| same · Pennrose | https://www.pennrose.com/apartments/new-york/bourne-kenney/ | Bourne & Kenney redevelopment, 205 affordable homes, Contour Housing Partners + Newburgh Housing Authority; Bourne tower upgrades incl. new building systems and enhanced safety and security; scheduled 2026. | Numbers table; renovation section; modernization FAQ |
| "Middletown NY downtown apartment building" · Firecrawl search | https://www.governor.ny.gov/news/governor-hochul-announces-completion-middletown-downtown-revitalization-initiative | Middletown DRI completed; facade assistance to 17 downtown buildings, 74 residential units benefited (13 new). | Area table (Middletown downtown buildings) |
| "Orange County Government Center Goshen" · Firecrawl search → scrape | https://en.wikipedia.org/wiki/Orange_County_Government_Center ; https://www.paulrudolph.institute/196301-orange-county-government-center ; https://savingplaces.org/stories/architectural-rescue-gone-wrong-orange-county-new-york | Paul Rudolph design, completed 1967 (legislature first met Jan 1970); closed since 2011 after Hurricane Irene damage; partly demolished 2015; reopened 2017 after renovation. | County building type; fire/power/storm section |
| "NYS elevator mechanic licensing law" · Firecrawl search | https://dol.ny.gov/elevator-licensing-information ; https://www.nysenate.gov/legislation/laws/LAB/A33 ; https://www.nysenate.gov/legislation/laws/LAB/954 | Labor Law Art. 33 (§950–957): businesses/individuals doing elevator design, installation, alteration, service, repair must be DOL-licensed; individuals working on an elevator need an elevator mechanic license (exceptions: accessibility lift technician / elevator accessibility technician); elevator contractor license requires employing licensed mechanics; temporary mechanic license changes from June 10, 2026. | Licensing section; myths; FAQ (who connects controller) |
| "Palm Tree Kiryas Joel multifamily elevator" · Firecrawl search | https://ecode360.com/11009523 ; https://www.jta.org/quick-reads/town-of-palm-tree-becomes-first-official-u-s-haredi-orthodox-town | Village of Kiryas Joel Ch. 47 Affordable Housing: planning board may require an elevator or reserved space for one, depending on state building code. Kiryas Joel split from Town of Monroe to become Town of Palm Tree. | Monroe/Palm Tree building type; area table |
| "Times Herald-Record elevator broken apartment Newburgh OR Middletown" · Firecrawl search | — | Results were Middletown CT and other states' stories; no verifiable Orange County NY item. Not used. | — |
| Stewart Airport-area office/industrial · Firecrawl search | — | EMPTY (no specific source retrieved; mentioned only generically as office/flex area, no figures). | Office/flex building type (qualitative) |
| Reddit r/Newburgh, r/HudsonValley elevator/fob threads | — | EMPTY (not accessible in build env). | — |
| Mid-Hudson News / Times Herald-Record elevator stories | — | EMPTY (no Orange County NY result surfaced). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |
| silo research | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63 is NYC-only; cited only to say it does NOT apply in Orange County. | Licensing section; FAQ |
| HV hub pricing table | /elevator-access-control-installation-hudson-valley | Orange County Level 1 from $2,100/car, Level 2 from $3,500/car, Level 3 per building. | Quick answer; cost section; FAQ |

Prices used: Level 1 from $2,100 per car, Level 2 from $3,500 per car (Orange County rate from HV hub), Level 3 quoted per building. Garnet Health and Montefiore St. Luke's Cornwall named only as landmarks, explicitly not as clients. Senior complexes named from the county's public list as examples of the building type, not as clients.

### Questions used on this page
- Our Middletown senior building already uses keycards at the front door. Can the same cards run the elevator?
- How far ahead should an Orange County building schedule an elevator access control survey?
- Does New York City's Local Law 63 apply to biometric elevator readers in an Orange County apartment building?
- Can a property manager who runs buildings in Port Jervis and Walden control elevator access for both from one office?
- What should happen to the controlled elevator in an Orange County senior building when a storm knocks out the power?
- Who makes the connection to the elevator controller in Orange County, and why can't the security installer do it?
- Can a medical office building near Garnet Health open its floors to patients during office hours and lock them at night?
- Is it worth adding elevator access control during an elevator modernization in Newburgh rather than afterward?
- How do home health aides get up to a client's floor in an Orange County elevator building without a resident's fob?
- What does a Level 1 elevator reader cost for a single-car building in Orange County?
- Can a county or court building in Goshen add the elevator to the badge system staff already use?
- Our Orange County building's elevator card reader stopped working and the original installer is gone. Where do we start?
- Will residents who use wheelchairs or walkers be able to use the elevator reader easily?
(No other headings on the page end in "?".)


## Putnam County (elevator-access-control-installation-putnam-county) — research, Nov 18 2026 (max-burn)

Angle: "a county of two- and three-story elevators" — Putnam's elevator stock is small senior complexes (PCHC Gleneida Court / Route 6 Mahopac, Stonecrest, Hillcrest/Hughson Commons), a 55+ condo in two elevator buildings in Cold Spring, the hospital campus, county/town buildings, LULAs and platform lifts in churches/libraries/town buildings, a few Main Street mixed-use buildings in Brewster, and new construction on Route 6 / Route 22. Design brief: simple for older riders, works offline (internet/cell gaps), survives outages (generators), run remotely by managers covering several towns.

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Putnam County New York 2020 census population 97,668 towns villages" · Firecrawl search | https://en.wikipedia.org/wiki/Putnam_County,_New_York | 2020 Census population 97,668; county seat Carmel. | Stock table row 1 |
| same | https://www.census.gov/quickfacts/fact/table/carmeltownputnamcountynewyork/PST045225 | Carmel town 34,442 (V2025 estimate). | Background only (not on page) |
| repo research (research/fire-alarm-installation.md, Putnam section) | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | Six towns (Carmel, Kent, Patterson, Philipstown, Putnam Valley, Southeast), three villages (Brewster, Cold Spring, Nelsonville); approximately three-quarters of the county in the NYC watershed. | Stock table rows 1 and last; rural section |
| repo research (research/cctv-installation.md, Putnam section) — ACS 2023 5-yr DP04 via census API | https://api.census.gov/data/2023/acs/acs5/profile?get=group(DP04)&ucgid=0500000US36079 | 38,369 housing units; 77.7% detached; broadband subscription 94.6% of households. | Stock table row 2; rural section (internet) |
| "Putnam County NY senior apartments elevator Carmel Brewster Mahopac" · Firecrawl search | https://www.putnamcountyny.gov/osr | Office for Senior Resources lists PCHC Gleneida Court (62+/disabled), Lakeview Apts 8 Gleneida Court, Sr. Housing @ Mahopac Hills 170 Rt 6; Wilder Balter: Stonecrest (3101 Stonecrest Dr, Brewster), Hughson Commons (4100 Gables Way, Carmel); Putnam Community Foundation 50 Main Street Brewster (62+). | Building types (senior); area table |
| "Gateway Summit Overlook Carmel…" · Firecrawl search → scrape | https://www.putnamhousing.com/senior-housing/ | 10/12/14 Gleneida Court: two-story, 24 units, NO elevator (stair glides), surveillance + generator. 20 Gleneida Court: two-story, 24 units, elevator, generator. Lakeview, 8 Gleneida Court: two-story, 24 units, elevator, generator. 170 Route 6 Mahopac: three-story, 48 units, elevator. | Stock table row 3; building types; rural section (generators) |
| Stonecrest · Firecrawl scrape | https://wbhomes.com/communities/stonecrest/ | Affordable senior community, 136 apartments; "Elevators in Each Residential Building"; emergency call system; on-site management office. | Stock table; building types (multi-building) |
| "Hillcrest Commons Senior Apts" · Firecrawl scrape | https://affordablehousinghub.org/housing/new-york/putnam-county/carmel/hillcrest-commons-senior-apts-25129-lihtc | 2000 Heights Ln, Carmel; 76 low-income senior units (60 1BR, 16 2BR); placed in service 2012. | Stock table |
| Hillcrest Commons II · Firecrawl scrape | https://wbhomes.com/communities/hillcrest-commons-phase-2/ | 74 apartments; head of household 55+; on-site management office; community room suite. (No elevator stated on the page.) | Stock table (no elevator claim made for it specifically) |
| Hughson Commons · Firecrawl scrape | https://wbhomes.com/communities/hughson-commons/ | 4100 Gables Way, Carmel; affordable senior; emergency call system; on-site management. (No elevator stated.) | Building types (named as example of the multi-building senior type only) |
| "Butterfield redevelopment Cold Spring…" · Firecrawl search → scrape | https://www.thehirerealty.com/condos/butterfield-condominiums/ | 49 condo residences, active adult 55+, two elevator buildings, one parking space per unit in a parking deck, train station less than a mile, next to Philipstown Friendship Center for Seniors and NewYork-Presbyterian medical care. | Stock table; building types (condo); area table; FAQ seasonal owners (generic) |
| same search | https://www.lohud.com/story/news/local/putnam/philipstown/2015/07/08/groundbreaking-ailes-senior-center/29879073/ | 2015 groundbreaking; 10-building complex incl. 55 condominiums (planning-stage figure; listing says 49 built). | Not used (superseded by listing) |
| "Putnam Hospital Carmel NY beds…" · Firecrawl search | https://www.northwell.edu/locations/putnam-hospital | Putnam Hospital, 670 Stoneleigh Avenue, Carmel (now listed by Northwell). Bed counts conflict across sources (106 staffed vs 164) — no bed count used. | Stock table; building types (landmark only, NOT a client) |
| "Donald B. Smith Government Campus… 40 Gleneida Avenue" · Firecrawl search | https://www.putnamcountyny.gov/component/jbusinessdirectory/companies/donald-b-smith-conservation-area?Itemid=101 | Putnam County Office Building, 40 Gleneida Avenue, Carmel. | Stock table; building types (county) |
| "Brewster village apartments … Brewster Crossing" · Firecrawl search → scrape | https://putnamedc.org/potential-large-projects/ | Brewster Crossing TOD: DORMANT. Garden Street School: residential rentals concept. Overlook (Gateway Summit) Route 6 Carmel: actively under construction (150-unit multifamily per list). EE Brewster, 1534 Route 22 Southeast: 60-unit senior housing + grocery, APPROVED. 25 & 31 Front St Patterson: two 3-story buildings, apartments over retail, conceptual. Hotel Route 311 & Fair St Patterson: ~120 rooms, 4 stories, pending. YMCA 684 Peekskill Hollow Rd: renovation. Fields Lane / Independent Way (Southeast) office/warehouse projects. | Stock table; building types (new construction, Brewster, office/flex); area table |
| same · Putnam County Press, Jun 23 2026 | https://www.putnampresstimes.com/post/is-affordable-housing-right-for-garden-street | Garden Street School affordable housing: concept only, no formal application (Covington Development + WBP Development); Mayor Schoenig: village "already has the highest population density out of all the communities in Putnam County". | Building types (Brewster) |
| same | https://putnamcountyny.gov/images/Departments/Planning_Dev_Transport/PDF_Documents/nichemarketingplanbrewster.pdf | 25-unit senior apartment complex by Putnam Community Foundation opened Aug 2008 (Brewster). | Background (50 Main St named from OSR list instead) |
| "New York State elevator licensing Article 33" · Firecrawl scrape | https://dol.ny.gov/elevator-licensing-information | DOL licensing required for design, construction, installation, inspection, testing, maintenance, alteration, service, repair of elevators and conveyances. License types: Elevator Contractor, Elevator Inspection Contractor, Elevator Mechanic, Accessibility Lift Technician, Elevator Inspector, Elevator Accessibility Technician (substitutable for platform lifts under ASME A18.1). Unlicensed individuals may not alter/maintain conveyances or install power lines from the mainline to the conveyance; only licensed mechanics under a licensed contractor. | Who-touches-what section; LULA section; FAQ (LULA, power circuit) |
| "ASME A17.1 two-way emergency communication 2.27.1" · Firecrawl search | https://up.codes/s/emergency-operation-and-signaling-devices | A17.1 2.27.1.1: two-way emergency communications between car and authorized personnel. | How-it-works; FAQ emergency phone |
| same | https://nationalelevatorindustry.org/elevator-emergency-communications/ | NEII: car emergency communication required in A17.1 since the 1930s; 2019 edition adds video/text for deaf/hard-of-hearing. | How-it-works; FAQ emergency phone |
| "LULA limited use limited application…" · Firecrawl search | https://nwliftsma.com/2026/10/lula-elevators-churches-town-buildings-offices/ ; https://www.elevators.com/commercial-elevators/lula-limited-use-limited-application/ | LULA = class of elevator for low-rise buildings between a wheelchair lift and full commercial elevator; churches, small offices, public buildings up to three levels. | LULA section; glossary; FAQ |
| "hydraulic elevator typically used low-rise…" · Firecrawl search | https://www.stanleyelevator.com/blog/traction-elevator-vs-hydraulic-elevator/ ; https://moseleyelevator.com/hydraulic-elevator-vs-other-types-which-is-right-for-your-building/ | Hydraulic elevators most often in buildings up to five stories; slower (≤150 ft/min). | How-it-works (hedged: "likely to be hydraulic"); FAQ hydraulic |
| silo research | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Add-on devices must not impede operation; inoperative on firefighters' service. Stated as NYC guidance, not Putnam law. | Failure-mode section |
| silo research | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63 is NYC-only. | Code section: does NOT apply in Putnam |
| repo research (fire-alarm-installation.md Putnam) | https://ecode360.com/5066448 ; https://www.ecode360.com/9532000 ; https://www.coldspringny.gov/node/6320 ; https://ecode360.com/6316884 ; https://mail.pattersonny.org/PDFs/Codes/Chapter43-Alarms.pdf | Carmel code Ch. 59 Building Construction & Fire Prevention (fire inspectors); Village of Brewster Code Enforcement Officer administers Uniform Code, issues COs; Cold Spring: State code + Village Code + Architectural and Historic District Design Standards; Philipstown: Code Enforcement Official + Fire Marshal; Patterson Ch. 43 names Town Fire Inspector and Code Enforcement Officer. | Code enforcement section |
| repo research (cctv-installation.md Putnam) | https://www.schumer.senate.gov/newsroom/press-releases/schumer-cell-phone-wireless-carriers-are-wrongly-claiming-quality-reception-on-coverage-maps-for-northern-westchester-and-putnam-counties-in-reality-areas-are-often-dead-zones-schumer-calls-for-feds-to-immediately-investigate-deceptive-coverage-maps | Oct 5 2015: RootMetrics testing; coverage maps overstated reception; Schumer called for federal investigation. | Rural section (dated 2015 on page); FAQ phone credential |
| repo research (cctv-installation.md Putnam) | https://patch.com/new-york/southeast/13k-without-power-putnam-after-sunday-storm ; https://dailyvoice.com/article/thousands-still-without-power-in-westchester/ | ~13,000 Putnam customers out Oct 2017; NYSEG 28,043 Putnam customers out after May 15 2018 storms. | Rural section (outages, dated) |
| repo research (cctv-installation.md Putnam) — NYS Open Data | https://data.ny.gov/resource/ca8h-8gjq.json | 2024 Putnam County total index crimes 519. | Myths section #1 |
| HV hub / silo pricing note | research/elevator-access-control-installation.md (PRICING) | Putnam L1 $2,175/car, L2 $3,625/car, L3 per building. | Quick answer, pricing, FAQ, schema |
| "reddit Putnam County NY … elevator fob" · Firecrawl search | — | EMPTY for Putnam: only generic r/unpopularopinion, r/Renters, r/NYCapartments fob threads. Not used. | — |
| Hudson Valley/Putnam local news on elevator outages or fob complaints (Mid-Hudson News, Highlands Current, Patch) | — | EMPTY (no Putnam elevator-specific item surfaced in build env). | — |
| PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). | — |

Prices used: Level 1 from $2,175 per elevator car, Level 2 (biometrics) from $3,625 per car, Level 3 quoted per building after survey; worked examples are multiples only (2 × $2,175 = $4,350; 2 × $3,625 = $7,250). Elevator contractor's connection visit, any network line/cable run, and the panel's electrical circuit stated as outside the price. No equipment cost, no school job, no parking. Putnam Hospital and all named buildings are stated as examples of building types from public listings, not clients. LL63 stated as NYC-only.

### Questions used on this page
- Our building has a LULA elevator rather than a full-size passenger car. Can it take a card reader?
- Our small Putnam building has a hydraulic elevator. Does a hydraulic car change how the reader is connected?
- The machine room in our Putnam building has no internet. Can the elevator credentials still be managed from the office?
- Will a reader installed in the car interfere with the elevator's emergency phone?
- Who supplies the electrical circuit that powers the elevator access panel?
- Can one floor in our Putnam County building require a PIN code on top of a fob?
- Does a phone credential work inside a steel elevator car where there is no cell signal?
- Our condominium has owners who leave for the winter. Can their elevator access be paused and switched back on in spring?
- Which costs sit outside the Putnam County per-car price, and who pays them?
- Our lower elevator landing opens to an unheated garage. Will a reader there hold up through a Putnam winter?
- What routine upkeep does an elevator access system need after it is installed?
- Can the access system warn our manager when a reader or controller goes offline?
(Headings ending in "?": none — the five myth H3s are quoted statements; all H2/H3s are statements.)


## Dutchess County (elevator-access-control-installation-dutchess-county) — research, Nov 18 2026 (max-burn)

Angle: one real small city (Poughkeepsie) with a new wave of six- and eight-story Main Street mid-rises, Beacon's three-story infill and a multi-building riverside complex, a long list of elevator-served senior buildings spread from Wappingers Falls to Red Hook, two hospital campuses and a growing IBM campus in the Town of Poughkeepsie, colleges with residence halls, and real local lessons about elevator reliability (a lightning strike that took out a senior building's elevator; a two-car senior tower with outage complaints). Pages talk only about Dutchess County.

| Query · platform | URL | Finding | Use |
|---|---|---|---|
| "Dutchess County New York 2020 census population City of Poughkeepsie Beacon" · Firecrawl search (Census QuickFacts) | https://www.census.gov/quickfacts/fact/table/dutchesscountynewyork/BZA010222 | Dutchess County: 2020 Census 295,911; July 1 2025 estimate 300,708 (V2025). | Numbers table; intro |
| same · Census QuickFacts | https://www.census.gov/quickfacts/fact/table/poughkeepsiecitynewyork/INC110224 | City of Poughkeepsie: 2020 Census 31,577; 2025 estimate 32,499. | Numbers table; town guide |
| same · Census QuickFacts | https://www.census.gov/quickfacts/fact/table/beaconcitynewyork/COM100224 | City of Beacon: 2020 Census 13,769; 2025 estimate 14,931. | Numbers table; Beacon section |
| same · Census profile | https://data.census.gov/profile/Poughkeepsie_town,_Dutchess_County,_New_York?g=060XX00US3602759652 | Town of Poughkeepsie 2020 population 45,471. | Numbers table; Town of Poughkeepsie commercial section |
| "Poughkeepsie new apartment building elevator waterfront Main Street 2025 units" · Firecrawl search → scrape City of Poughkeepsie news flash (Sept 29 2025) | https://www.cityofpoughkeepsie.gov/m/newsflash/Home/Detail/375 | 309–316 Main St: six-story, 120 mixed-income units, 14,800+ SF ground-floor commercial (adaptive reuse + new construction). 47–51 Cannon St: former Dutchess County Board of Elections building becoming an eight-story mixed-use building with 140 units, geothermal. PK4Keeps comprehensive plan and first major zoning revision since 1979 adopted 2022. $10M DRI (round 8). Downtown BID covers 219 properties. | Numbers table; downtown mid-rise section; FAQ (two entrances / mixed-use) |
| same · Governor's office (May 27 2026) → scrape | https://www.governor.ny.gov/news/governor-hochul-announces-construction-starting-147-million-affordable-housing-development | Wallace Campus, Main & Catharine Sts: $147M, 187 units — 69 in the 1870s former Wallace Department Store, 118 in two new buildings; 30 supportive units; 22,000+ SF retail across three buildings; preserves limestone façade, existing stairways and fourth-floor dome ceiling; 11 mobility-impairment units and 5 sensory-disability units; game room, fitness space, movie room, co-working, study hall and bike storage in each building; all-electric. | Numbers table; downtown section (multi-building credential list, amenity rooms, historic interior, supportive units) |
| "Beacon NY new apartment building units elevator Main Street Highlands Current" · Firecrawl search → scrape The Current (Nov 24 2023) | https://highlandscurrent.org/2023/11/24/booming-beacon-6/ | Beacon Commons (16 W Main St) 62 apartments; 2 Cross St three-story, retail + 18 apartments, nine for seniors, county housing trust award $1,575,000; 364 Main St three-story, retail + 20 apartments; 248 Tioronda Ave 64 apartments + 25,400 SF commercial; 393-397 Fishkill Ave three-story mixed-use, 12 apartments. | Beacon section; town guide |
| "Edgewater Beacon apartments" · Firecrawl search → scrape The Current (Aug 14 2026) | https://highlandscurrent.org/2026/08/14/beacon-city-updates/ | Edgewater: amended permit would bring the project to 248 units / 359 bedrooms; three residential buildings constructed, four remain; parking moved after bedrock found. | Beacon section (multi-building complex, phased buildings) |
| same · Edgewater Beacon site | https://edgewater-beacon.com/ | "Seven building apartment complex" with Hudson River views. | Beacon section |
| "Dutchess County senior apartments elevator …" · Firecrawl search → scrape PDF | https://www.dutchessny.gov/Departments/Aging/Docs/senior-citizen-housing-in-dutchess-county.pdf | OFA "Housing for Older Adults in Dutchess County 2026-27" (revised June 2026). Elevator named at: Cannon Street Housing (134 Cannon St, Poughkeepsie, 40 units, on-site super); DiMarco Place II (Wappingers Falls, 32 units, laundry/garbage room each floor); Horizons at Fishkill (89 units, elevators, covered parking, package receiving); Meadow Ridge II (Beacon, 52 units, elevators, secured entry with intercom); Pendell Commons (Poughkeepsie, 71 units, controlled building access, intercom); Red Hook Commons (96 units in two phases, intercoms, on-site super); Spring Manor (Poughkeepsie, elevators in select buildings); Stone Ledge (Hyde Park, 84 units, controlled building access, intercom); Maplewood (457 Maple St, 64 units, "historical building"); Castle Court at Concord Village (60 units); St. Anna HDFC (70 units). Admiral Halsey Senior Village, 135 Main St (118 units, security doors, intercom systems). Hamlet at Pawling (80 units, controlled access). Bartel Place, Millbrook (24 units). | Senior section table; town guide; FAQ |
| "Poughkeepsie Journal apartment elevator out of service residents" · Firecrawl search → scrape (summary) | https://www.poughkeepsiejournal.com/story/news/local/central-dutchess/2016/07/27/lakeview-arms-elevator-poughkeepsie/87618734/ | Lakeview Arms (Town of Poughkeepsie): elevator out for more than a week after a lightning strike on July 20 2016; Town Building Inspector issued summonses for code violations. | Lightning/surge section; myth section |
| same · Hudson Valley Press (Aug 5 2020) → scrape (summary) | https://hudsonvalleypress.com/2020/08/05/senior-tenants-concerned-with-living-conditions/ | Admiral Halsey tower, 135 Main St, City of Poughkeepsie: an 85-year-old tenant trapped about 30 minutes in one of the building's two elevators; council member and mayor responded to complaints about outages. | Senior section (reliability first, two-car buildings) |
| "MidHudson Regional Hospital Poughkeepsie … beds" · Firecrawl search | https://www.wmchealth.org/locations/midhudson-regional-hospital | MidHudson Regional Hospital, member of WMCHealth, 243-bed facility in Poughkeepsie. Landmark only, not a client. | Medical section; numbers table |
| HV hub research (reused) | https://prnewswire.com/news-releases/walshconsigli-completes-545-million-patient-pavilion-at-vassar-brothers-medical-center-301209441.html | Vassar Brothers Medical Center Patient Pavilion: eight stories, 752,610 SF, 264 private rooms; opened Jan 2021. Landmark only, not a client. | Medical section; numbers table |
| "IBM Poughkeepsie site campus buildings redevelopment 2025" · Firecrawl search | https://dec.ny.gov/news/environmental-notice-bulletin/2026-09-30/seqr/town-of-poughkeepsie-ibm-quantum-facility-building | IBM quantum facility at 2455 South Road, Town of Poughkeepsie: four new buildings incl. ±233,700 SF quantum facility building with ±45,000 SF mezzanine; ±372,958 SF total new construction (DEC ENB Sept 30 2026). Landmark only. | Commercial / industrial section |
| "Marist … Vassar … Dutchess Community College" · Firecrawl search | https://www.sunydutchess.edu/around-campus/campus-places/index.html | DCC Conklin Hall: 132,000 SF residence hall, 24/7 security. | Campus section |
| same | https://maristconnect.marist.edu/s/1516/GID2/index.aspx?sid=1516&gid=2&pgid=1331 | Marist North Campus Housing: first of four new residence halls opened Aug 2016 with 292 beds for juniors and seniors. | Campus section |
| same | https://www.marist.edu/student-life/campus/housing/residence-areas | Marist residence areas include Marian Hall and Midrise Hall. | Campus section (named only) |
| "Culinary Institute of America Hyde Park … Bard …" · Firecrawl search | https://www.ciachef.edu/new-york-residence-halls/ ; https://www.bard.edu/reslife/residencehalls/ | CIA Hyde Park campus offers coed housing for more than 1,700 students; Bard lists dozens of residence halls and houses. | Campus section (named only, not clients) |
| "Dutchess County government 22 Market Street … county office building" · Firecrawl search | https://www.setty.com/portfolio-of-experience/dutchess-county-courthouse-building ; https://www.facebook.com/DutchessCoGov/posts/beginning-jan-15th-the-county-clerks-record-room-and-requisition-desk-will-move-/1336495431841207/ | 22 Market St County Office Building is 89,250 GSF and houses administrative departments; County Clerk's Record Room on its third floor. Landmark only. | Public buildings section |
| "City of Poughkeepsie building department Uniform Code enforcement permits elevator" · Firecrawl search | https://ecode360.com/27006425 ; https://www.cityofpoughkeepsie.gov/DocumentCenter/View/1817/Building-Permit-Requirements-PDF | City Code Ch. 6: Building Inspector expected to know proper installation of elevators; permit applications at the Building Inspector's office; permit requirements call for two sets of plans and specifications. | Licensing/approvals section |
| same | https://www.townofpoughkeepsie-ny.gov/202/Building | Town of Poughkeepsie Building Department enforces through permits, notices, orders, inspections and certificates. (Full page scrape: EMPTY — proxy tunnel error; search excerpt only.) | Licensing/approvals section |
| "19 NYCRR Part 1203 …" · Firecrawl search | https://dos.ny.gov/system/files/documents/2021/12/2021-12-10-full-text-of-rule-part-1203.pdf | Every city, village, town and county responsible for Uniform Code enforcement must run a code enforcement program (19 NYCRR 1203.2). | Licensing/approvals section; FAQ-free (no permit question used) |
| silo research (reused) | https://dol.ny.gov/elevator-licensing-information ; https://www.nysenate.gov/legislation/laws/LAB/A33 | Labor Law Art. 33: elevator design, installation, alteration, maintenance and repair require NYS DOL licensing; individuals need an elevator mechanic license. | Two-licenses section; scope |
| silo research (reused) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-010.pdf | Add-on devices must not impede elevator operation and drop out on Phase I/II firefighters' service (stated as the general principle; NYC bulletins are not Dutchess law). | Fire/power section |
| silo research (reused) | https://ipvm.com/reports/elevator-access-control-examined ; https://butterflymx.com/blog/elevator-access-control-by-floor-schedule/ ; r/accesscontrol thread | Car enable vs floor lockout vs landing control; relays = floors × cars × stations. | How it works; pricing |
| silo research (reused) | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Local Law 63 is NYC-only — cited only to say it does not apply in Dutchess County. | Two-licenses section; myths |
| HV hub / silo pricing note | research/elevator-access-control-installation.md (PRICING) | Dutchess Level 1 from $2,295/car, Level 2 from $3,825/car, Level 3 per building after survey; elevator contractor's controller visit and any new network/cable run to the car are outside the price. | Quick answer; pricing; FAQ |
| Mid-Hudson News / Reddit r/Poughkeepsie, r/HudsonValley / PAA / PASF / Answer the Public / AI Overview / Bing / DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env / not searched beyond the queries above). | — |
| "2010 ADA Standards 308 reach ranges" · Firecrawl search | https://www.ada.gov/assets/pdfs/2010-design-standards.pdf | 308.2/308.3: unobstructed forward and side reach 48 in maximum, 15 in minimum above the floor. | Reader placement section |
| Vassar College residence hall / Vassar Inn details | https://www.facebook.com/Serino4NY/posts/i-was-thrilled-to-visit-vassar-college-for-a-tour-of-the-future-vassar-inn-and-i/824355712831062/ | Excerpt only (50-room inn); not used. | — |

Prices used: Level 1 from $2,295 per elevator car, Level 2 (biometrics) from $3,825 per car, Level 3 (floor-by-floor, hall-call readers, schedules, destination dispatch) quoted per building after survey. Worked examples only multiply those per-car figures. Elevator contractor's controller visit and any new network/cable run to the car stated as outside the price. No equipment cost. Hospitals, colleges, IBM and county buildings named only as landmarks/building types, never as clients. Senior properties named from the county's public OFA guide as examples of the building type, not as clients. NYC Local Law 63 stated as not applying in Dutchess County.

### Questions used on this page
- Our Poughkeepsie building has street entrances on two different floors. Which levels should be treated as the lobby?
- Our Beacon building's elevator has doors on both the front and the back. Can a floor be locked on one side only?
- Does adding access control affect our maintenance contract or warranty with the elevator company?
- Can the readers run in a log-only mode for a week or two before we start restricting floors?
- How do you keep a reader inside the elevator cab from being pried off, kicked or sprayed?
- How do you hand out credentials to every resident on changeover day without a long line in the lobby?
- We plan to renovate our elevator cab interiors next year. Should we wait, or can the readers be moved later?
- When the super puts the car on independent service for a move-in, does the reader still restrict floors?
- Does the per-car price change if one of our cars only serves two floors?
- If we choose a cloud-managed platform now, can we switch platforms later without rewiring the elevator?
- What should a Dutchess County board or owner expect to see in a written elevator access control proposal?
- Can a shared conference or event floor in our Poughkeepsie office building open for a booked event and lock again afterward?
(No headings on the page end in "?". Four FAQ drafts — hydraulic vs traction, internet requirement, unheated garage landing reader, routine upkeep — were replaced because the parallel Putnam County page asks the same things.)
