# Research — School Security Camera Installation (silo)

Merged from per-page batch research files (batch run 2026-10-18). Silo-wide findings and question registers are kept per contributing page below; later pages append a `## <area>` section and add their questions to the register.


---
<!-- from school-security-camera-installation-manhattan.md -->
# School Security Camera Installation — Manhattan (REBUILD research, batch file)

Written 2026-10-18 by the REBUILD of `school-security-camera-installation-manhattan` (area page, up-link `/school-security-camera-installation-nyc`, direct line (929) 560-0737, Bronx GBP 460 E Fordham Rd / `#bronx`). `research/school-security-camera-installation.md` did not exist and other builders were working other pages of this silo in parallel, so this file holds (1) the silo-wide matrix as seen from this build, (2) a `## Manhattan` local section, (3) the question register for this page plus every question found on the existing silo pages. The main run should merge it into `research/school-security-camera-installation.md`.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: WebSearch, WebFetch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`). Shell curl is blocked.

---

## 1. Source matrix (blueprint v2.3 §3)

| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl search), rows R1–R4. No Manhattan-specific school-camera thread surfaced. |
| 2 | Google People Also Ask | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — §10.5 on the page says so and tests claims commonly repeated in cost guides/forums/older pages against primary sources; it does not quote an AI Overview. |
| 6 | Area landmarks | Manhattan section (Wikipedia, LPC, Landmark West). |
| 7 | Area use cases / building stock | NYU Steinhardt co-location study; City Limits 2014 building-age figures; Wikipedia (campuses, Léman). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** |
| 9 | Local news | amNY (Feb 17 2023), NBC NY (Feb 17 2023), ABC7 (June 23 2022), CBS NY (Jan 8 2019), Catholic World Report (June 5 2025). |
| 10 | Hyperlocal | I Love the Upper West Side (DOE door system item — title only, not read: **EMPTY** for content); Landmark West (PS 166 listing). West Side Rag / Patch Manhattan school-camera items: **EMPTY** (none surfaced). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** |

## 2. Silo-wide findings (school security cameras)

### 2.1 Law, rules and programs
| ID | Exact query · platform | URL | Finding | Used on Manhattan page |
|---|---|---|---|---|
| L1 | `New York State ban facial recognition schools Commissioner determination 2023 biometric` · WebSearch → WebFetch | https://www.nysed.gov/news/2023/state-education-department-issues-determination-biometric-identifying-technology-schools | Sept 27 2023 determination: "prohibits schools in New York State from purchasing or utilizing facial recognition technology"; other biometrics left to local decision weighing privacy, civil rights, effectiveness, parental input; basis State Technology Law §106-b; Rosa quote. | §5.5 facts; §8.5 callout; §9 analytics H3; §10.5 H3 4; Sources |
| L2 | same · WebFetch | https://www.bsk.com/news-events-videos/update-on-the-commissioner-of-education-rsquo-s-determination-of-the-use-of-biometric-technology-in-schools | Bond Schoeneck & King: ban covers "public, private and charter schools"; fingerprinting not banned; SSBA-funded FR bought before Dec 20 2020 must be discontinued. | §9 analytics H3; §10.5 H3 4; Sources |
| L3 | `NYS Education Law 2-d security cameras video personally identifiable information student` · WebSearch → WebFetch | https://nysed.gov/sites/default/files/programs/data-privacy-security/privacy-terms-for-parents_0.pdf | NYSED glossary: educational agency = school district, BOCES, school (incl. charter schools, approved private schools for students with disabilities), NYSED; third-party contractors receiving student data need a DPA + Parents Bill of Rights; PII = info in a student's education record. Nonpublic schools generally not addressed. | §8.5; §9 2-d H3; Sources |
| L4 | `FERPA FAQs on photos and videos under FERPA ...` · WebSearch → WebFetch | https://studentprivacy.ed.gov/faq/faqs-photos-and-videos-under-ferpa | Video is an education record when directly related to a student and maintained by the school; law-enforcement-unit records excluded; parents may inspect, copies generally not required; redaction cannot be charged; disclosure to police generally needs consent or exception. | §9 security-office H3; §10.5 H3 5; FAQ; Sources |
| L5 | `Education Law 2801-a school safety plan ...` · WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/EDN/2801-A | District-wide + building-level plans; building-level plan confidential incl. floor plans/blueprints, disclosed only to authorized staff and law enforcement; filed with local law enforcement and state police within 30 days; charter MOU clause (subd. 10). Nonpublic not named. | §9 drawings H3; FAQ floor plans; Sources |
| L6 | `New York Labor Law 203-c video recording restrooms ...` · WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/LAB/203-C | No employer video recording in restrooms or rooms designated for employees to change; court-order exception; footage unusable. | §6 card; §7.5; Sources |
| L7 | (verification) · WebFetch | https://www.nysenate.gov/legislation/laws/PEN/250.05 | Eavesdropping, class E felony — basis for audio-off default. | §10 equipment audio note; Sources |
| L8 | `Alyssa's Law New York silent panic alarm schools bill status 2025` · WebSearch → WebFetch | https://abc7ny.com/school-safety-alyssas-law-panic-alarms-new-york-schools/11989474/ | June 23 2022: Hochul signed law requiring districts to *consider* silent panic alarms; Adams spokesman said city schools don't need them (SSAs have direct NYPD line). | §9 panic H3; Sources |
| L9 | same · WebFetch | https://www.nysenate.gov/legislation/bills/2025/S6410 | S6410 (Sen. Robert Jackson): would *require* ≥1 silent panic alarm per public school building linked to police; in Senate Education Committee, re-referred Jan 7 2026; not passed. | §9 panic H3; §10.5 H3 6; Sources |
| L10 | `Nonpublic School Safety Equipment NPSE grant ...` · WebSearch → WebFetch | https://www.nysed.gov/sites/default/files/programs/nonpublic-schools/npse-eligible-item-list.pdf | Eligible since 4/1/2013: "cameras and affiliated recording devices", "visitor intercom", "remote electronic door unlatching system", "System maintenance/service call". Installation not listed as its own item. | §9 NPSE H3; §14; Sources |
| L11 | `NYC nonpublic school security guard program Local Law 2 of 2016` · WebSearch → WebFetch | https://www.nyc.gov/assets/dcas/downloads/pdf/business/nps_rules.pdf | LL 2/2016; DCAS; schools ≥300 students; 1 guard 300–499, 2 for 500–999, +1 per 500; reimburses guard wages; equipment only inside a 25% "reasonable costs" cap for the guard company. | §9 guard H3; Sources |
| L12 | `Smart Schools Bond Act ...` · WebSearch → WebFetch | https://www.nysed.gov/smart-schools/about-smart-schools-bond-act | $2B, approved Nov 4 2014; High-Tech Security plans must assure no facial recognition or similar self-learning analytics. | §10.5 H3 4; Sources |
| L13 | `NYC DOE ... Local Law 36 of 2014` · WebSearch → WebFetch | https://intro.nyc/local-laws/2014-36 | Charter §528: Chancellor with NYPD decides camera placement at DOE buildings — entrances/exits and areas without reasonable expectation of privacy; door alarms. | §5; §9 co-location H3; Sources |
| L14 | `Chancellor's Regulation A-412 ...` · WebSearch → WebFetch | https://pwsauth.nycenet.edu/docs/default-source/default-document-library/a-412-final-version70b2d643e2644c21b728183efbd323c7.pdf | A-412 (Dec 21 2023): SSAs do visitor control and patrol; no camera provisions. | §9 co-location H3 (background) |
| L15 | `Landmarks Preservation Commission security cameras permit rules` · WebSearch → WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Staff-level permits; ≤3 cameras per 25 ft frontage on large institutional buildings; not on primary façade unless no option; attach at mortar joints/plain masonry/wood/metal, never through cast iron or decorative surfaces; conduit concealed, ≤~10 in visible painted; cut sheets required. | §7; §7.5; §9 LPC H3; §13; Sources |
| L16 | `NYC noise code construction permitted hours ...` · WebSearch → WebFetch | https://www.nyc.gov/assets/dep/downloads/pdf/environment/education/nyc-noise-code-fact-sheet.pdf | Construction weekdays 7 a.m.–6 p.m.; after-hours with permit for listed reasons. | §9 hours H3; §12; Sources |
| L17 | `NYC Local Law 128 of 2024 low voltage` · WebSearch → WebFetch | https://intro.nyc/local-laws/2024-128 | Defines low-voltage electrical work (<50 V signaling/communication/alarm/data); no electrical permit for low-voltage work by qualified persons; life-safety systems reserved to licensed electricians. | §8.5; FAQ; Sources |
| L18 | carried from research/hikvision-security-camera-installation.md F1/F2/N1 | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment ; https://www.law.cornell.edu/cfr/text/2/200.216 | FCC DA 26-635, effective July 16 2026, bars continued importation/marketing of previously authorized covered equipment (use-based for Hikvision/Dahua); 2 CFR 200.216 bars grant/loan funds for covered video surveillance used for public safety/security. | §9 grant-brand H3; §10; Sources |
| L19 | `FCC covered list Hikvision Dahua ... NDAA section 889` · WebSearch → WebFetch | https://ipvm.com/reports/hikua-bans | NDAA 889 federal procurement/contractor/federal-funds bans; FCC Nov 2022 no new authorizations; 2024 court upheld. (Third-party summary.) | §10 background; Sources |
| L20 | `New York child day care video cameras ... A4530` · WebSearch → WebFetch | https://nysenate.gov/legislation/bills/2025/A4530 | A4530 (Morinello) would require cameras in day-care rooms for children ≤3, 90-day retention; in committee, not passed. | FAQ day-care; §10.5 H3 7; Sources |
| L21 | `Nonprofit Security Grant Program New York 2025 ...` · WebSearch → WebFetch | https://www.dhses.ny.gov/nonprofit-programs | DHSES: FY2026 NSGP application period closed; prequalification in SFS, UEI, Charities Bureau registration, vendor questionnaire >$50k. | §9 grant-brand H3; Sources |

### 2.2 Reddit / forums (excerpts only)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com NYC school cameras privacy parents footage request` · Firecrawl search | https://www.reddit.com/r/NYCTeachers/comments/1vdidtg/coworkers_with_meta_glasses/ | r/NYCTeachers excerpt: NYC public schools use a boilerplate release form for filming. | §5 (paraphrased: teachers already think about who films them); Sources |
| R2 | same | https://www.reddit.com/r/nycparents/ | r/nycparents excerpt: a public-school parent campaigning to change the citywide media-consent process. | §5; Sources |
| R3 | same | https://www.reddit.com/r/Teachers/comments/qm1u6g/we_just_got_told_that_cameras_will_be_installed/ | r/Teachers (not NYC): staff told cameras would record video and sound 24/7 in rooms — staff alarm. | §10.5 H3 3 (framed as forum reaction); Sources |
| R4 | same | https://www.reddit.com/r/ECEProfessionals/comments/17e7u4r/cameras_viewable_by_parents/ | early-childhood staff: parent-viewable cameras vs admin-only security cameras. | FAQ day-care (background) |

### 2.3 Keyword layers (planned; no volume data — Ahrefs not used)
- Service: school security camera installation; school CCTV; school surveillance system; school camera repair/upgrade.
- Problem: shared-building camera ownership; landmark façade camera; FERPA video request; facial recognition ban; footage retention; panic alarm pre-wire.
- Technology: IP camera, PoE, NVR, VMS, fiber riser, analog-to-IP (EoC), privacy masking, NDAA-compliant.
- Industry: independent school, charter school, parochial/Catholic school, yeshiva/day school, preschool/daycare, DOE co-located campus.
- Geographic: Manhattan, Upper West Side, Upper East Side, Harlem, Washington Heights, Lower Manhattan/Financial District, Lincoln Square.

## Manhattan

**Thesis:** A Manhattan school almost never controls its whole building — it shares it (DOE campuses and charters in DOE space), rents it (independent schools in former bank and office buildings, parish schools in church property, preschools in leased floors) or occupies a landmarked pre-war shell — so a camera system there is designed around who owns each wall, door and recording: layout drawings kept confidential with the safety plan, an analytics menu that respects the 2023 facial-recognition ban, video handled the way FERPA/Ed Law 2-d expect, LPC-compliant façade fixings, and cable work inside the noise-code day and the school calendar.

| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M1 | `NYC DOE schools co-located buildings number shared campus` · WebSearch → WebFetch | https://steinhardt.nyu.edu/research-alliance/research/spotlight-nyc-schools/trends-school-co-locations-nyc | 2012-13: 832 of 1,748 NYC schools (47.6%) co-located, 1,232 buildings; Manhattan and Bronx already >40% in 2005; charters co-located rose 26%→~60%. | §5; §5.5; §9; Sources |
| M2 | `NYC public schools door camera buzzer locking system ...` · WebSearch → WebFetch | https://www.amny.com/education/all-nyc-public-schools-will-soon-have-front-door-locking-systems/ | Feb 17 2023: ~$43M contract (Symbrant Technologies), $78M budgeted, ~1,300 schools in the first year of ~1,850; pilot six schools per borough; lead photo PS 11 Chelsea. | §5; §5.5; §9 co-location H3; Sources |
| M3 | same · WebFetch | https://www.nbcnewyork.com/news/local/nyc-schools-to-get-camera-based-door-looking-security-system-what-to-know/4110353/?amp=1 | Front doors first; staff see who is at the door before admitting. | §9; Sources |
| M4 | `C.B.J. Snyder school buildings Manhattan landmark` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Public_School_9_(historic_building) | 466 West End Ave at W 82nd; Snyder; 1894–96; NRHP 1987, NYC landmark 2009; within Riverside-West End HD Ext. I; houses Mickey Mantle School (P.S. 811M) since 2002. | §7; §13 landmark card; Sources |
| M5 | `Public School 166 132 West 89th Street landmark` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/PS_166_(Manhattan) | 132 W 89th St; Snyder; built 1897–98, opened Sept 1899; NYC landmark 2000; Richard Rodgers School of Arts & Technology. | §7; §13; Sources |
| M6 | `Julia Richman Education Complex 317 East 67th Street` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Julia_Richman_Education_Complex | UES; building begun 1922, dedicated 1924; 1993–95 $30M renovation into separate spaces; six schools (Urban Academy, Vanguard, Talent Unlimited, P226M, Ella Baker, Manhattan International) + toddler center + Mount Sinai clinic. | §5; §7; §13; Sources |
| M7 | `Martin Luther King Jr. Educational Campus 122 Amsterdam Avenue` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Martin_Luther_King_Jr._Educational_Campus | 122 Amsterdam Ave (W 65th–66th); opened 1975; weathering-steel curtain wall; perimeter corridors with floor-to-ceiling glass, many windowless inner classrooms; replaced by multiple high schools; opposite LaGuardia HS. | §7; §13; Sources |
| M8 | `Manhattan school intruder entered building 2025 NYPD` · WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/manhattan-school-intruder/ | Jan 8 2019: George Washington HS (192nd St & Audubon Ave) lockdown; 29-year-old seen on the rooftops; in custody; lockdown before students entered. | §5; §13 card; §9 roof H3; Sources |
| M9 | `Léman Manhattan Preparatory School 41 Broad Street` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/L%C3%A9man_Manhattan_Preparatory_School | Lower School at 41 Broad St, former HQ of Bank of America International; founded 2005 as Claremont Prep; PreK–12; upper campus in the Cunard Building. | §7 (office/bank building type); §13; Sources |
| M10 | `Archdiocese of New York Catholic schools Manhattan number 2025` · WebSearch → WebFetch | https://www.catholicworldreport.com/2025/06/05/archdiocese-of-new-york-launches-school-renewal-plan-releases-results-of-viability-study/ | June 2025: viability study of 77 parish/regional elementary schools; "Parish-based schools are a particular strength in Manhattan"; St. Mark the Evangelist and Mt. Carmel-Holy Rosary (Manhattan) closed end of 2024–25. | §5; §9 merger H3; Sources |
| M11 | `NYC school buildings average age ...` · WebSearch → WebFetch | https://citylimits.org/nycs-silent-infrastructure-challenge-aging-public-buildings/ | City Limits, Mar 18 2014: average public school building 66 years old; 209 of 1,179 buildings built before 1920 (~18%). (Unsourced within article; dated.) | §5.5 (dated); Sources |
| M12 | `Manhattan private schools number independent schools NYSAIS` · WebSearch | (results only: nysais.org, privateschoolreview.com) | No authoritative Manhattan count retrieved → **EMPTY** for a number; page gives no count. | not used |
| M13 | Manhattan school-camera Reddit (r/manhattan, r/UpperWestSide) | — | **EMPTY** (no thread surfaced in searches above). | — |

### AESS house practices on the page (unsourced — phrased as practice) → FLAGS
- Layout drawing marked confidential and shared only with the school's named safety contact (our reading of 2801-a; nonpublic schools adopt voluntarily).
- Camera network on its own switch/VLAN; school IT keeps admin; vendor gets a separate limited account.
- Audio off and facial recognition not offered on school jobs.
- Survey timing (one walk-through per floor, roof and cellar), drill windows booked outside instructional hours, holiday/summer scheduling.
- Two-hour response / 1–2 h restore claims NOT made; repair section only says same-day where possible.
- COI naming the building owner/managing agent supplied on request; staging via service entrance.
- Retention default 30 days suggested as a starting point (no Manhattan law sets it for nonpublic schools).

### Pricing used (§9 Manhattan 1.25× on the silo's Brooklyn base page as it stood on 2026-10-18)
Brooklyn base: $450–$950 per installed camera; tiers 6–12 cams $4,500–$8,000; 16–32 $12,000–$30,000; 32–64 $25,000–$48,000; 64–128 $40,000–$95,000+; NVR+storage $750–$6,000+. Hub-only line items (NYC hub, treated as base): PTZ/LPR $1,200–$2,200; vestibule camera + intercom + buzzer $2,800–$6,500; analog-to-IP per coax run $180–$320. ×1.25, round half-up → $563–$1,188; $5,625–$10,000; $15,000–$37,500; $31,250–$60,000; $50,000–$118,750+; $938–$7,500+; $1,500–$2,750; $3,500–$8,125; $225–$400. Service $195/hr, 3-h min ($585), unmultiplied.
**Inconsistencies flagged:** old Manhattan page used ~1.2× ($540–$1,140) not 1.25; NYC hub tier ranges differ from Brooklyn's (6–12 cams $4,500–$9,500 vs $4,500–$8,000; 32–64 $24,000–$55,000 vs $25,000–$48,000); Brooklyn page is being rebuilt in parallel — if its base changes, Manhattan figures need re-deriving.

---

## Question register

### This page (school-security-camera-installation-manhattan, rebuilt 2026-10-18)
§9 Q&A (H3):
1. Our charter school has two floors of a DOE building — can we put our own cameras in the shared stairwells?
2. Two schools share one lobby on our campus — whose recorder should hold the entrance video?
3. Does the DOE's camera-and-buzzer front door make a co-located school's own cameras redundant?
4. What will the Landmarks Preservation Commission let us mount on a designated school façade?
5. Can new camera cable reach the upper floors of a pre-war school without opening plaster walls?
6. Our school leases floors in a former bank or office tower — who signs off on the riser and the lobby camera?
7. After the 2023 biometric determination, which camera analytics can a New York school still switch on?
8. Should the cameras be run by the school's security office rather than the dean's office?
9. Does Education Law 2-d reach the company that installs and services a charter school's cameras?
10. Is our camera layout drawing part of the confidential building-level safety plan?
11. Does the noise code limit when a crew can pull cable in a school on a residential block?
12. Does the NPSE item list cover service calls on cameras a nonpublic school already owns?
13. Our school receives a city-reimbursed security guard — can that program pay for cameras?
14. If we apply for a federal Nonprofit Security Grant, can the budget include any recorder brand?
15. Our parish school is merging into another building — can the cameras move with us?
16. Should we pre-wire for a silent panic alarm while the camera cable is being run?
17. What should a roof camera on a Manhattan school actually be watching?
FAQ (§17, = FAQPage):
1. How long does a camera survey of a multi-floor Manhattan school take?
2. Which drawings should we send before the survey, and how do you keep them?
3. Can the cameras run on the school's existing network, or do they need their own?
4. What happens to the recordings and the recorder when our lease ends and we move?
5. Can a preschool in a church basement or leased storefront use classroom cameras?
6. Can you give us a camera inventory for the annual safety-plan review?
7. On a shared campus, who should hold the administrator password?
8. Will you work alongside the guard company and the building's own security staff?
9. Is there a smallest job you will quote at a Manhattan school?
10. Do you remove the old coax and dead cameras left by the previous system?

De-dup notes: compared by meaning against every question below and the NYC hub. Deliberately NOT asked here: cost, camera count, classroom cameras, never-record spaces, retention length, install during session, brand/NDAA in general, grants in general, buzzer/alarm integration, repair/takeover, licensing/vetting, footage ownership, summer/August, sidewalk/street view, facial recognition legality as such (covered in body + analytics angle instead), Alyssa's Law meaning (asked as pre-wire timing instead), daycare live access for parents (asked as A4530/preschool setting instead).

### Existing silo pages (as found 2026-10-18; Brooklyn, Long Island, Orange were being rebuilt in parallel — their new questions not seen)
(Each list extracted by tools/check_page.py parser: `.faq-question` + every h2/h3/summary ending in "?")

- nyc (hub): How much do school security cameras cost? · How many cameras does a school need? · Can schools put cameras in classrooms? · Are cameras allowed in school bathrooms? · Who can view school camera footage? · How long do schools keep camera footage? · Can parents request school video? · Do daycares need cameras in New York? · What camera brands are banned for schools? · Will cameras lower a school's insurance costs? · Can school cameras record audio? · Who pays for school security cameras? · What is the best security camera system for schools? · How much does it cost to install security cameras in a school? · Are security cameras effective in schools? · Can teachers be recorded in the classroom? · Is facial recognition legal in New York schools? · How many security cameras does a high school need? · Do private schools need security cameras? · What is NDAA compliance for school cameras? · How long is school camera footage kept? · How much does school security camera installation cost in NYC? · How many security cameras does a school need? · Can cameras be installed in classrooms? · Where can school cameras never be installed? · How long should a school keep camera footage? · Can you install while school is in session? · What camera brands do you install for schools, and what is NDAA compliance? · Can grants pay for school security cameras? · Do you integrate cameras with buzzers, intercoms, and access control? · Do you repair or take over existing school camera systems? · Are your installers licensed and vetted to work in schools? · Questions answered. Building surveyed next?
- manhattan (OLD template, overwritten by this rebuild — kept here so no later page reuses them either): Need School Camera Repair in Manhattan Today? · How much do school security cameras cost in Manhattan? · Who installs school cameras in Manhattan? · Are cameras allowed in private schools in NY? · Can NYC daycare parents demand live camera access? · What cameras do NYC schools actually use? · How long do schools keep camera footage? · Do school cameras record audio? · Can school cameras be monitored remotely? · Who repairs school camera systems near me? · Do grants pay for school cameras in NY? · Do cameras work on landmarked buildings? · Is DIY school camera installation legal? · How many cameras does a Manhattan school building need? · How do installs work around freight elevators and building rules? · Can cameras cover the dismissal scene on a public sidewalk? · What about the rooftop play deck? · Do co-op or condo neighbors get a say in our camera install? · What happens to school camera systems in August? · Can cameras integrate with our existing intercom or alarm? · Do Jewish day schools have extra funding options for cameras? · Who owns the footage — the school or the camera company? · How much does school security camera installation cost in Manhattan? · Is facial recognition legal in Manhattan schools? · Can cameras be installed in classrooms? · Where can school cameras never be installed? · How long should a Manhattan school keep camera footage? · Can you install while school is in session? · What camera brands do you install for Manhattan schools, and what is NDAA compliance? · Can grants pay for school security cameras in Manhattan? · Do you integrate cameras with buzzers, intercoms, panic alarms, and access control? · Do you repair or take over existing school camera systems in Manhattan? · Are your installers licensed and vetted to work in schools? · Need Repair on a Manhattan School System Right Now?
  - Note: old Q "Do cameras work on landmarked buildings?" vs new Q4 (what LPC permits on a designated façade) — new one asks for the specific permit rules, answered from the LPC guidebook; old one asked feasibility. Old Q "What about the rooftop play deck?" vs new Q17 (what a roof camera should watch, GW HS rooftop intruder) — related; new answer is about roof-access doors/bulkheads, not play-deck supervision.
- bronx: Need School Camera Repair in the Bronx Today? · How many cameras does a Bronx school building need? · What does the elevated train actually do to cameras? · Does Throggs Neck really need marine-grade cameras? · Can a driveway camera record the street beyond our gate? · Our charter shares a building with another program. Whose cameras are they? · Who watches the building over summer recess? · Will new cameras work with our existing buzzer and burglar alarm? · Is there dedicated security funding for Bronx religious schools? · Who ends up owning the recordings? · What does a school camera system cost in the Bronx? · How do you decide the camera count for our building? · Is facial recognition allowed in any Bronx school? · Can cameras go inside classrooms? · Which spaces can never be recorded? · How long should we keep footage? · Can you install while school is in session? · Which brands do you install, and why does NDAA §889 matter? · What funding can Bronx schools use for cameras? · Will you integrate cameras with our buzzer, alarm, and door hardware? · Do you repair or take over systems someone else installed? · Are your technicians licensed and suited to school settings? · Need Repair on a Bronx School System Right Now?
  - Note: Bronx "Our charter shares a building with another program. Whose cameras are they?" overlaps new Q1/Q2. New Q1 is specifically about installing in shared stairwells (Charter §528 / Chancellor placement authority); Q2 about which recorder holds a shared lobby. Flag for reviewer: closest semantic neighbour in the silo.
- brooklyn / dutchess-county / hudson-valley / long-island / nassau-county / orange-county / putnam-county / queens / rockland-county / staten-island / suffolk-county / ulster-county / westchester-county: full lists in the main-run merge (extracted to scratch `sibq.json`); all use the same 12-question template FAQ (cost, count, facial recognition, classrooms, never-record spaces, retention, install in session, brands/NDAA, grants, integration, repair/takeover, licensing) plus 8–12 area Q&A (salt air, deer, winter, boarding campuses, Alyssa's Law (LI), NPSE for yeshivas, summer, footage ownership, street view). None asks about LPC permit criteria, FERPA law-enforcement unit, Ed Law 2-d vendors, 2801-a drawing confidentiality, noise-code hours, DCAS guard program, NSGP brand limits, parish mergers, panic-alarm pre-wire, or the FAQ topics above.

## Images (11) — source log
No Drive "School" folder; CompanyCam not connected. Permanent image rule applied:
- 6 real AESS job photos from other jobs, re-cropped: dahua-camera-installation/…long-island-bullet-camera-aimed-down-corridor-to-door; …orange-county-ceiling-cameras-beside-exit-sign-and-on-grid; …orange-county-recorder-monitor-camera-grid-and-cable-bundles; …long-island-small-cameras-on-high-wall-of-open-hall; …long-island-dome-camera-on-long-wall-arm-on-stone-facade; nvr-installation/…staten-island-patch-cable-bundles-down-equipment-rack.
- 5 manufacturer product shots (unbranded): products/f4.png, products/a3.png, cam-eyeball-ir.png, cam-eyeball-white.png, cam-turret-side.png.
Excluded per instructions: images/parking/*, network crew photos, network-cable-repair, cat6, low-voltage, cat6-repair/aess-*, fiber-optic-installation/aess-*, root school-*-ny.webp. Hikvision/Dahua-branded product shots avoided on purpose (page steers schools to non-covered brands).

---
<!-- from school-security-camera-installation-orange-county.md -->
# School Security Camera Installation — Orange County (batch research)

Created 2026-10-18 by the REBUILD of `school-security-camera-installation-orange-county` (area page, up-link `/school-security-camera-installation-hudson-valley`, direct line (845) 640-3835, Bronx GBP 460 E Fordham Rd / `#bronx`). `research/school-security-camera-installation.md` did not exist; a parallel builder is writing the Manhattan file (`research/_batch/school-security-camera-installation-manhattan.md`), so this file holds silo-wide findings gathered in this build plus the Orange County section and the question register for this page. The main run can merge it into `research/school-security-camera-installation.md`.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: WebSearch, WebFetch (summaries of the fetched page), Firecrawl search (excerpts). Shell curl blocked. Nothing below is invented; where only a search listing or excerpt was seen it says so. Unreachable sources: `EMPTY (not accessible in build env)`.

**Thesis of the Orange County page (one sentence):** in Orange County a school camera system is a public-money project with a paper trail — Smart Schools allocations, SED building aid and Facilities Planning permits when wiring is involved, GML bidding and Labor Law Article 8 for districts, NPSE reimbursement for the county's large nonpublic sector, BOCES capital work, and later FERPA/2801-a/police use of the footage — so the camera job is designed, documented and handed over so it survives the claim, the audit and the records request across the 17 Orange-Ulster BOCES component districts plus Newburgh, from 2007-era district IP systems (Middletown) to bus garages now sharing the road with the county's stop-arm program.

---

## 1. Source matrix (blueprint v2.3 §3)

| # | Source | Status |
|---|---|---|
| 1 | Reddit | **EMPTY (not accessible in build env)** for Orange County school cameras — `reddit hudsonvalley school security cameras Orange County district` (WebSearch) returned no reddit.com result. Substituted: IPVM discussion forum thread (row F1). |
| 2 | Google PAA | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)**. Page §10.5 says so on the page and tests seven claims commonly repeated about school cameras against primary sources; it does not quote an AI Overview. |
| 6 | Area landmarks | Sourced (section 3). |
| 7 | Area use cases | Sourced: BOCES district list, SED Smart Schools plan pages, BusPatrol/county page, KJ district. |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** — substitute: Firecrawl search SERP for `school security camera installation Orange County NY` (row S1). |
| 9 | Local news | News 12 Hudson Valley (Dec 2021, Dec 2023), Hudson Valley Press (Mar 2020, Sep 2024), AS&U citing Mid Hudson News (Aug 2026). |
| 10 | Hyperlocal | Hudson Valley Press (Newburgh), Goshen CSD news post. Times Herald-Record school-camera item: **EMPTY** (no result surfaced for `recordonline school district cameras Orange County board approves security cameras 2025`; results were Orange County, Florida). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — Firecrawl SERP only surfaced a Yelp listing for Orange County, *California* (wrong county), no review text. |

---

## 2. Silo-wide findings (school security cameras, New York)

### 2.1 Law and regulation
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | `New York State Education Department facial recognition ban schools determination September 2023 Education Law 106-b` · WebSearch → WebFetch | https://www.nysed.gov/news/2023/state-education-department-issues-determination-biometric-identifying-technology-schools | Sept 27, 2023, Commissioner Betty A. Rosa: schools may not purchase or use facial recognition technology; other biometric technology is a local decision weighing privacy, civil rights, effectiveness and parent input; issued under **State Technology Law §106-b** (not Education Law), after an ITS biometrics report released Aug 7, 2023. | §5 facts list; §8.5; §9 "biometric ruling" H3; §10.5 H3; Sources |
| L2 | same search → WebFetch | https://www.securityinfowatch.com/access-identity/biometrics/news/53074206/new-york-lifts-ban-on-biometric-technologies-in-k-12-schools | (SIA-written) the Sept 2023 determination ended the blanket biometric moratorium in effect since Dec 2020 (bill A6787 of 2019); facial recognition remains the exception, applies to public and private K-12. | §9 biometric H3 (fingerprint readers a local decision); Sources |
| L3 | (search listing) | https://www.nysed.gov/sites/default/files/programs/data-privacy-security/biometric-determination-9-27-23.pdf | Determination PDF (listing only, not opened). | Sources |
| L4 | `Monroe-Woodbury school district security cameras vestibule capital project` · WebSearch → WebFetch | https://www.nysed.gov/sites/default/files/programs/facilities-planning/security-camera-mca-051711.pdf | SED Facilities Planning memo (expenses on/after July 1, 2011): camera allowance $2,000 per camera up to a **$35,000** total claim on Form FB Schedule N; above $35,000 must be a regular capital project with building-permit review and Facilities Planning pre-approval to generate building aid; a system installed before a permit is rejected → no aid. SED project manager line (518) 474-3906. | §5; §8.5; §9 SED wiring H3; §10.5 H3; §14; Sources |
| L5 | `reddit school security camera installer cost district quote questions` · WebSearch → WebFetch | https://nysed.gov/facilities-planning/installation-security-cameras | SED page: cameras aidable as building aid in student-occupied buildings (Ed Law §3602 subd. 6-c); "special cost-per-unit allowance" sets a per-building maximum; a full system with "electrical wiring installed through the building" is capital construction needing a permit; equipment-only installs use a special claim form, no permit. | §9 SED wiring H3; §14; Sources |
| L6 | same search (listing) | https://www.nysed.gov/sites/default/files/programs/facilities-planning/special_cost_allowance_form_for_purchase_of_security_cameras.pdf | SED special cost allowance claim form (listing only). | Sources |
| L7 | `Smart Schools Bond Act high-tech security nonpublic school loan program cameras NYSED guidance` · WebSearch → WebFetch | https://p1232.nysed.gov/mgtserv/smart_schools/docs/Guidance_Smart%20Schools_revised_030723.pdf | SSBA = $2 billion; High-Tech Security category covers "video surveillance, emergency notification systems, and physical access controls"; capital-intensive security (new wiring/construction) needs Facilities Planning approval; streamlined review for limited door/entrance work still needs Letter of Intent, project code, licensed architect/engineer review; where a permit is required it must be issued before any payment; **nonpublic loan requirement covers classroom tech and connectivity, not security**; installation of new devices/servers claimed under School Connectivity. (Fetched summary said no facial-recognition text in this guidance — page does not attribute the FR rule to SSBA guidance.) | §5; §9 nonpublic-loan H3; §9 Smart Schools H3; §10.5; Sources |
| L8 | `Nonpublic School Safety Equipment grant NPSE New York security cameras eligible reimbursement` · WebSearch → WebFetch | https://www.nysed.gov/sites/default/files/programs/nonpublic-schools/revised.npse-guidance-7.10.23.pdf | NPSE (Year 9 guidance): reimbursement, not a grant up front; external cameras eligible **only as part of an access control system** (intercom/remote unlatch); external lighting for primary entries, door hardening, radios eligible; Years 4–9 add security assessments, personnel; visitor-ID-to-police-database scanners ineligible (operating expense); one claim per BEDS code per year; invoices + proof of payment required; questions ORISS@nysed.gov. | §5; §9 NPSE H3; §15; FAQ; Sources |
| L9 | (search listing) | https://www.assembly.ny.gov/mem/Andrew-Hevesi/story/110451 → WebFetch | May 16, 2024: 2024-25 budget $70M for NPSE (up 55% from $45M); program began 2013-14 with $5M. | §5 facts; Sources |
| L10 | `Education Law 2801-a district-wide school safety plan building-level emergency response plan confidential video` · WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/EDN/2801-A | District-wide plan (public comment ≥30 days, hearing) + building-level emergency response plans kept confidential, exempt from FOIL, filed with local police and State Police within 30 days of adoption; reviewed at least annually. | §8.5; §9 building-level plan H3; Sources |
| L11 | `Education Law 2-d security camera video footage …` · WebSearch → WebFetch | https://studentprivacy.ed.gov/faq/faqs-photos-and-videos-under-ferpa | FERPA: video is an education record when directly related to a student and maintained by the school (e.g., fight footage used for discipline); background/incidental appearance usually not; law-enforcement-unit video is not an education record; parents may inspect; schools must redact others if reasonably possible, else parents may inspect the whole clip; FERPA generally doesn't require copies. | §9 fight-footage H3; FAQ; Sources |
| L12 | (listing, same search) | https://www.nysed.gov/sites/default/files/programs/data-privacy-security/ex-officio-guidance-may-2025.pdf | NYSED data-privacy guidance (listing only, not opened). Ed Law 2-d camera-specific guidance: **EMPTY** (no NYSED page found saying how 2-d applies to video). Page treats 2-d only as "vendor contracts that touch student data", hedged. | §8.5 (hedged) |
| L13 | `General Municipal Law 103 competitive bidding threshold …` · WebSearch → WebFetch | https://www.osc.ny.gov/files/local-government/academy/pdf/seeking-competition-procurement-062624.pdf | OSC: GML §103 purchase contracts > $20,000, public works > $35,000; aggregate over 12 months, no artificial splitting; piggybacking under GML §103(16) (government-let contract with extension clause, lowest bid/best value) — **sunsets June 30, 2026** per that deck; below-threshold buys follow the board's §104-b procurement policy. | §9 bidding H3s; §10.5; Sources. FLAG: piggyback sunset date — status after June 30, 2026 not verified; page says "check whether it has been extended". |
| L14 | `NY school district security camera installation prevailing wage Labor Law 220 public work low voltage` · WebSearch → WebFetch | https://statistics.labor.ny.gov/legal/adjudication/pdf/public-work/mcsi-advanced-report-recommendation.pdf | NYS DOL hearing officer report (Nov 2, 2010): AV installer underpaid prevailing wage on public work projects incl. Spencerport CSD; willful findings, 16% interest + 25% penalty recommended. (Audio-visual, not cameras.) | §8.5; §10.5 H3 (framed as "AV installation at a school district treated as public work") ; Sources |
| L15 | `Security camera surveillance systems best practices` (listing in L14 search) → WebFetch | https://www.nyssba.org/news/2018/06/07/on-board-online-june-11-2018/security-camera-surveillance-systems-best-practices-and-policy-concerns/ | NYSSBA On Board (June 11, 2018, NYS Assn of School Attorneys): video only in public spaces; no restrooms/locker rooms; audio permanently disabled; post notice; PERB has found regular surveillance usable for discipline/evaluation is a mandatory subject of bargaining; check CBA and board policy. | §9 union H3; §9 signage H3; Sources |
| L16 | `FCC covered list Hikvision Dahua …` · WebSearch → WebFetch | https://ipvm.com/reports/hikua-bans | NDAA §889: no federal dollars (incl. grant recipients) on Hikvision/Dahua video; FCC barred new equipment authorizations Nov 2022; upheld by appeals court Apr 2024. | §10; §10.5; Sources |

### 2.2 Forums / buyer pain points
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F1 | `reddit school security camera installer cost district quote questions` · WebSearch → WebFetch | https://ipvm.com/discussions/school-100-camera-system-1-bid-3x-budget-needs-help | School wanted ~100 cameras across buildings + lot on $100k; only bid ~$400k, not itemized. Advice: itemize, get more bidders, ask why others didn't bid (insurance, bonding, prevailing wage), clarify scope (network, racks, storage, trenching), rebid with camera locations and pre-bid walkthrough; some said $100k for 100 cameras is aggressive. | §10.5 H3; §14; Sources |
| S1 | `school security camera installation Orange County NY` · Firecrawl search (SERP excerpts) | (SERP) — results incl. https://www.orangecountyny.gov/2478/School-Bus-Safety-Program-in-Orange-Coun , https://www.thumbtack.com/ny/middletown/security-camera-install , https://rockland-orange-security.com/ , Long Island K-12 integrators | Bing/DDG substitute. No Orange-County-specific school camera competitor page in top 10; county bus-safety page ranks. Yelp result was Orange County CA. | context only |

### 2.3 Five keyword layers (from sources above; no volumes available)
- **Service:** school security camera installation, school camera system upgrade, school video surveillance, campus camera installation, bus garage cameras, school camera repair.
- **Problem:** cameras from an old capital project, recorder full/overwrites, footage request from parent, SED aid rejected, single bid over budget, bus loop congestion, after-hours break-ins at shops.
- **Technology:** IP/PoE cameras, NVR/VMS, fisheye/multisensor, PTZ, door-station cameras with remote unlatch, NDAA-compliant brands, no facial recognition.
- **Industry:** public school districts, BOCES, nonpublic/yeshiva schools, Catholic schools, daycares/pre-K, colleges, bus contractors.
- **Geographic:** Orange County NY, Newburgh, Middletown, Goshen, Monroe-Woodbury/Central Valley, Kiryas Joel, Warwick, Port Jervis, Pine Bush, Washingtonville, Cornwall, Chester, Florida, Greenwood Lake, Highland Falls, Tuxedo, Minisink, Valley Central (Montgomery/Walden), Marlboro (Ulster, BOCES component).

---

## 3. `## Orange County`

| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| O1 | `Orange-Ulster BOCES component school districts list` · WebSearch → WebFetch | https://www.ouboces.org/about-us/component-districts | 17 components: Chester UFSD, Cornwall CSD, Florida UFSD, Goshen CSD, Greenwood Lake UFSD, Highland Falls/Fort Montgomery CSD, Kiryas Joel UFSD, Marlboro CSD, Middletown ECSD, Minisink Valley CSD, Monroe-Woodbury CSD, Pine Bush CSD, Port Jervis City SD, Tuxedo UFSD, Valley Central SD, Warwick Valley CSD, Washingtonville CSD; Newburgh ECSD listed as non-component. | §5; §8; §19 text; FAQ; Sources |
| O2 | `Orange-Ulster BOCES security cameras schools safety` · WebSearch → WebFetch | https://www.asumag.com/safety-security/news/55395381/orange-ulster-boces-advances-safety-upgrades-as-part-of-1588-million-capital-project | AS&U Aug 3 2026 (citing Mid Hudson News Aug 1): voter-approved **$158.8M** O-U BOCES capital project, two Goshen campuses; CTE Center on **Gibson Road** in major construction; "enhanced security systems" and better control of employee access badges after a State Comptroller audit; asst. supt. Mark Coleman (paraphrased); CTE programs incl. welding, HVAC, carpentry, electrical, cosmetology, networking, heavy equipment, digital media. No camera detail. | §5; §7 CTE card; §9 CTE H3s; §13 landmark; Sources |
| O3 | `Newburgh Enlarged City School District security cameras capital project` · WebSearch → WebFetch | https://hudsonvalleypress.com/2020/03/18/3-5m-for-necsd-updates-to-technology-and-security/ | Hudson Valley Press Mar 18 2020: NECSD $3.5M Smart Bond approval for 2018 proposal: visitor management, "upgraded and additional camera infrastructure", access control all buildings, 911-dial alerts, mass notification, optional panic button; can't fund personnel; district has 16 buildings; Supt. Roberto Padilla: "We are committed to the safety of our scholars and staff." | §5; §9; Sources |
| O4 | `Middletown Enlarged City School District security cameras` · WebSearch → WebFetch | https://www.securityworldmarket.com/na/Newsarchive/new-york-state-school-district-uses-axis-and-cdw-g (also thejournal.com 2007-03-13) | 2007: Middletown City schools installed ~**265 Axis network cameras** across 7 school + 2 admin buildings (hallways, cafeterias, lots), PoE on existing VoIP switches, Mirasys VMS, CDW-G; video kept **30 days** unless incident; planned police/first-responder feed sharing; state grant via Assemblywoman Aileen Gunther. | §5; §7; §9 old-cabling H3; §10.5; Sources |
| O5 | `nysed.gov smart-schools Middletown City School District approved plans` · WebSearch → WebFetch | https://www.nysed.gov/smart-schools/middletown-city-school-district-approved-plans ; https://nysed.gov/sites/default/files/programs/smart-schools/middletown-city-sd-ssip-11-28-17.pdf | Middletown SSIP Nov 28 2017 $6,377,663 (connectivity, classroom tech; High-Tech Security $0 in that plan); SSIP May 17 2022 High Tech Security **$499,475**. | §5 facts; §9; Sources |
| O6 | `Pine Bush Central School District security cameras capital project` · WebSearch → WebFetch | https://nysed.gov/smart-schools/pine-bush-central-school-district-approved-plans | Pine Bush SSIPs incl. High Tech Security: Jul 14 2017 $939,532; Feb 6 2018 $973,868 (HTS only); Feb 26 2020 $1,040,114; Mar 7 2023 $2,096,502 (incl. Nonpublic Loan). | §5; §9; Sources |
| O7 | same → WebFetch | https://pinebushschools.org/about-us/pine-bush-capital-project-february-2025 | Pine Bush capital vote Mar 4 2025: $79,295,000 total (Prop 1 $52.26M, Prop 2 $27.035M); HVAC, roofs, fire alarm upgrades in all 7 buildings, new IT equipment, elevators; no cameras mentioned; seven buildings named (Circleville ES/MS, EJ Russell ES, Pakanasink ES, Pine Bush ES, Crispell MS, Pine Bush HS). | §7; §9 construction H3; Sources |
| O8 | `Port Jervis City School District security cameras` · WebSearch → WebFetch | https://nysed.gov/smart-schools/port-jervis-city-school-district-approved-plans | Port Jervis SSIP Nov 28 2017, $2,958,135 (connectivity, classroom tech, High Tech Security). | §5; Sources |
| O9 | `nysed smart schools Warwick Valley OR Monroe-Woodbury OR Goshen Central approved plans high tech security` · WebSearch → WebFetch | https://www.nysed.gov/smart-schools/warwick-valley-central-school-district-approved-plans | Warwick Valley SSIPs: May 11 2016 $1,474,275; Jan 20 2017 $270,814; Feb 26 2020 $467,544 (incl. High Tech Security). | §5; Sources |
| O10 | same → WebFetch | https://www.nysed.gov/smart-schools/minisink-valley-central-school-district-approved-plans | Minisink Valley SSIP Mar 6 2019 High Tech Security **$3,571,363**; Feb 24 2021 amendment −$155. | §5; Sources |
| O11 | `Monroe-Woodbury school district security cameras vestibule capital project` · WebSearch → WebFetch | https://hudsonvalley.news12.com/monroe-woodbury-school-district-approves-98-million-capital-improvement-project | News 12 Dec 6 2023: Monroe-Woodbury $98M capital project approved 878–290; boilers at five schools, roofs at four, infrastructure at all seven; no security items named. | §7; §9 construction H3; Sources |
| O12 | `Orange County NY school bus stop-arm camera program` · WebSearch → WebFetch | https://www.orangecountyny.gov/2478/School-Bus-Safety-Program-in-Orange-Coun | County program launched 2024 with BusPatrol (AlertBus); state authority S.4524B/A.4950B (Aug 6 2019), VTL §1174-a; 30-day warning period; $250 first violation, +$25 repeats within 18 months, cap $300; footage on onboard DVR sent over encrypted LTE; 15 participating districts listed (Chester, Cornwall, Middletown, Florida, Goshen, Greenwood Lake, Highland Falls-Fort Montgomery, Kiryas Joel, Minisink Valley, Monroe-Woodbury, Newburgh, Port Jervis, Valley Central, Warwick Valley, Washingtonville); funded by fines. | §5; §7 bus garage; §9 bus H3s; §10.5; Sources |
| O13 | same search → WebFetch | https://hudsonvalleypress.com/2024/09/18/dangerous-and-illegal-behavior-caught-on-camera/ | Sept 18 2024: program began May (summer trial), 500+ buses; 1,895 citations so far, 722 in June; most violations 3–4 pm drop-off; County Executive Steve Neuhaus quote "When you see the red lights flashing and the stop arm come out, you must stop." | §5 facts; §9 bus loop H3; Sources |
| O14 | same search → WebFetch | https://www.gcsny.org/goshen-joins-bus-orange-county-safety-program/ | Goshen CSD joined; camera tech installed at the **Goshen bus garage**; $250 minimum penalty; no license points. | §7 bus garage card; Sources |
| O15 | `Kiryas Joel Village Union Free School District special education public school created 1989` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Kiryas_Joel_School_District | KJ Village UFSD created 1989 by Legislature to provide public special education; *Board of Ed. of Kiryas Joel v. Grumet* (1994); re-authorized 1995; also runs buses and buys supplies for private-school (mostly yeshiva) students; 2021–22 roughly 120–158 students in its public program. | §5; §7 nonpublic card; §9 NPSE/loan H3s; Sources |
| O16 | `Orange County NY` tighter security (in reddit search results) · WebSearch → WebFetch | https://hudsonvalley.news12.com/tighter-security-among-plans-to-help-combat-excessive-violence-in-orange-county-school-district | News 12 Dec 14 2021: unnamed Orange County district — student shooting outside a school, fights, "boxing matches" recorded in hallways; tighter security planned. Body not available; district not named. | §5 (hedged: "an Orange County district, unnamed in the report"); Sources |
| O17 | `SUNY Orange campuses Middletown Newburgh Kaplan Hall` · WebSearch (listing) | https://sunyorange.edu/newburgh/ ; https://www.wikipedia.org/wiki/SUNY_Orange | SUNY Orange has a Newburgh campus besides Middletown (listing). | §13 landmark card |
| O18 | `Mount Saint Mary College Newburgh NY campus Hudson River` · WebSearch (listing) | https://en.wikipedia.org/wiki/Mount_Saint_Mary_College_(New_York) | Mount Saint Mary College, Newburgh (listing). | §13 |
| O19 | carried from repo `lorex-camera-installation-orange-county.html` Sources | https://censusreporter.org/profiles/05000US36071-orange-county-ny/ | ACS 2024: 411,767 residents. | §5 facts (one figure) |
| O20 | landmarks (well-known, linked to Wikipedia; not separately fetched) | https://en.wikipedia.org/wiki/United_States_Military_Academy ; https://en.wikipedia.org/wiki/Stewart_International_Airport ; https://en.wikipedia.org/wiki/Tri-States_Monument (carried from Lorex Orange page) | USMA West Point (Highland Falls district borders it); Stewart Airport in New Windsor; Tri-States Monument at Port Jervis. | §13 |

### Orange County EMPTY items
- Reddit r/hudsonvalley / r/orangecountyny school-camera threads: EMPTY.
- Times Herald-Record (recordonline) school camera stories: EMPTY (search surfaced Florida results).
- Washingtonville, Goshen, Cornwall, Chester, Tuxedo, Greenwood Lake, Florida, Highland Falls camera-specific district news: EMPTY (not searched individually beyond Washingtonville, which returned nothing local).
- Orange County Sheriff SRO program: EMPTY (search returned Orange County, Florida only).
- Newburgh/Middletown NCES enrollment counts: EMPTY (only third-party aggregators surfaced) — not used.

---

## 4. Existing silo question register (from every school-security-camera-installation-*.html except Orange, read 2026-10-18)

Old template pages (Bronx, Brooklyn, Queens, Staten Island, Nassau, Suffolk, Westchester, Rockland, Putnam, Dutchess, Ulster) each carry ~23 questions on the same intents: repair-today banner; camera count; local hazard (el, salt air, deer, winter, historic gutters); street/sidewalk/driveway recording; summer recess monitoring; buzzer/alarm integration; religious/nonpublic funding; footage ownership; cost; camera-count method; facial recognition; classrooms; never-recorded spaces; retention; install during school year; brands + NDAA §889; funding; door hardware integration; take over other installers' systems; licensed technicians. Hubs (NYC, LI, HV, Manhattan) add: who installs in [county]; private schools allowed; daycare parents live access; what cameras schools use; footage retention; audio; remote monitoring; who repairs near me; grants; landmarked buildings; DIY legal; police feeds (LI); Alyssa's Law (LI); athletic fields; bus loop/pickup line (LI); dorms; carline (HV); ice storms; rural internet (HV); summer camps (HV); freight elevators, sidewalk dismissal, rooftop play deck, co-op neighbours (Manhattan). Full verbatim list: run `tools/check_page.py`-style extraction (408 lines captured in build scratch). The Orange page avoids every one of these intents or takes a materially different angle (noted per question in §5).

## 5. Orange County page question register (every FAQ/Q&A question on the page)

(filled after build — see below)

Section §9 (visible H3 Q&A, grouped under H2 clusters) and §17 FAQ (=FAQPage schema). Checked against §4 by meaning; `tools/check_page.py` exact/masked duplicate check: none.

### §9 Questions Answered (H3)
- Orange County School Cameras Dark Before the First Bus?
- Our district still has part of its Smart Schools allocation left — can that money buy cameras, and what has to happen first?
- Why does the State Education Department care whether new wiring is part of the camera job?
- Will our camera project have to go out to public bid, and how do we avoid splitting it the wrong way?
- Can a district buy cameras off another government's contract instead of running its own bid?
- We received one bid and it is triple our budget — what should we look at before we reject it?
- Our cameras went in during the 2000s — can the network cable they use be kept?
- What happens to the recordings on the old recorder when the new system goes in?
- Three projects left us with three brands of cameras — can they end up on one screen?
- Do the county's stop-arm bus cameras also cover our bus garage?
- What should a bus garage camera be able to show after a night with no one there?
- Can our own parking-lot cameras help when a stop-arm ticket is disputed?
- Which shop-floor hazards change where cameras go in a career and technical building?
- Our campus is in the middle of a capital project — should the cameras wait until construction ends?
- When two families both ask to see the same hallway fight clip, what does the school have to blur first?
- Does our building-level emergency response plan have anything to do with camera access?
- What should a written agreement settle before village police or the sheriff get a live link to our cameras?
- Does the 2023 biometric ruling stop fingerprint door readers as well as face matching?
- Do we have to bargain with the teachers' union over where cameras go?
- Should staff and visitors be told where every camera is?
- A small district has one IT person for every building — how do we keep the system from depending on one login?
- Can our nonpublic school borrow cameras through the public district's Smart Schools plan?
- Our yeshiva has NPSE funds — will they reimburse outdoor cameras that are not tied to a door system?
- What does a daycare in a converted house actually need from cameras?
- Already bought the equipment?

### §17 FAQ
- How many working days does a 30-camera school building take, and will it fit inside winter recess?
- What should be in the handover file when a school camera project closes?
- Can the cameras run on the district's existing network, or does IT need a separate one?
- How do we show an auditor or a court that the recorder's time stamp was right on the day of an incident?
- Do you provide certified payroll on prevailing-wage school jobs?
- Can we add cameras next year without replacing the recorder?
- What insurance paperwork do you give a district before work starts?
- What maintenance should a school schedule on its cameras each summer?
- How long do the hard drives in a school recorder last before they need replacing?
- Do you work through our architect or construction manager, or directly with the district?

Notes on near-intents: 'hallway fight clip' is framed on FERPA redaction between two families (NYC hub asks generally whether parents can request video); 'police live link' is framed on the written agreement (LI hub asks whether LI schools share feeds); 'daycare in a converted house' asks which views (NYC hub asks whether daycares need cameras; HV/LI ask about parent live access); 'biometric ruling / fingerprint readers' is about non-face biometrics (every sibling asks whether facial recognition is legal).

## 6. FLAGS (for Anwar)
- Unsourced AESS house practices phrased as practice: 1–2 h restore after arrival; same-day callouts; 5–8 working days for a 30-camera building; certified payroll/prevailing-wage capability; COI with additional insured; two admin accounts + sealed credentials; VLAN segmentation; summer maintenance routine; drive-replacement policy; not pulling cable before approval route confirmed; red/blue deterrent lights off at schools; plenum cable on J-hooks; asbestos-plan compliance; Field Notes is a method note, not a specific job.
- Prices: silo Brooklyn base (school-security-camera-installation-brooklyn: $450–$950/camera; daycare $4,500–$8,000; single building $12,000–$30,000; multi-wing $25,000–$48,000; multi-building $40,000–$95,000+; NVR $750–$6,000+; college $200,000+) × §9 Orange 1.40 → $630–$1,330; $6,300–$11,200; $16,800–$42,000; $35,000–$67,200; $56,000–$133,000+; $1,050–$8,400+; $280,000+. $195/hr 3-h min ($585) unmultiplied. INCONSISTENCIES: old Orange page used $585–$1,235 (1.30×); HV hub uses a "county band" $565–$1,285 and HV lanes ($5,600–$9,500 etc.) that match neither §9 county factors; Bronx page uses 1.10× ("ten-point band") vs §9 1.00×; old pages still print the three-year warranty. Multiplier applied to whole installed range incl. equipment (silo ranges bundle equipment) — same open question as NVR silo.
- BYOE/labour-only: no silo BYOE base price exists → page gives no BYOE number ("quoted per position at walkthrough").
- GML §103(16) piggyback sunset June 30, 2026 (OSC 2024 deck) — extension status not verified; page tells reader to check.
- NPSE per-pupil amount not stated; Year-9 guidance is 2023 — later-year rules not re-read.
- Ed Law §2-d application to video: no NYSED source found; mentioned only as vendor-contract rule (hedged).
- News 12 Dec 2021 item: body not available; district unnamed — page says so.
- §10.5 tests "claims commonly repeated" without an AI Overview capture (AI Overview EMPTY); ADT/Ring/SimpliSafe comparison is qualitative.
- Landmarks linked to Wikipedia/college pages from search listings (not fetched in full).
- Images: 11 = 8 real AESS job photos from other jobs (from images/dvr-upgrade/ and images/apartment-building-security-camera-installation/, several re-cropped) + 3 manufacturer product shots (images/products/a4, d4 crop, f4 crop). No real school photos exist. The underlying job scenes also appear on many other silo pages under other names.
- check_page.py does NOT compute masked-geo paragraph similarity (only exact/masked duplicate questions/answers and file-size clusters); similarity was measured with a separate script: page 5-gram Jaccard ≤0.010, paragraph max 0.633 (vs new Manhattan page, closing NAP) — all < 0.65.

