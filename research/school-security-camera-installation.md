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



---
<!-- merged from batch 8 (school brooklyn + long-island builds) -->
# School Security Camera Installation — silo research (v2.3 §3)

Created 2026-10-18 by the Brooklyn rebuild run (first rebuild in this silo). Research tools available in the build env: WebSearch (US web search, results as title+URL), WebFetch (page fetch + summary), Firecrawl search (titles + snippets) and Firecrawl scrape (Reddit is blocked for scrape: "we do not support this site"). Shell curl to the web is blocked. Google PAA / PASF / AI Overview / Answer the Public / Yelp review bodies cannot be opened from this environment.

Format of every entry: **query** · platform · URL · finding · used on (page + section). "excerpt" = only the search snippet was read.

## Silo base prices (from existing pages, Brooklyn = 1.00×)

Source: existing `school-security-camera-installation-brooklyn.html` (pre-rebuild, pricing table + FAQ), read 2026-10-18.

| Line | Brooklyn base |
|---|---|
| Commercial IP camera, installed | $450 – $950 each |
| NVR + storage | $750 – $6,000+ by scale |
| Daycare / preschool (6–12 cameras) | $4,500 – $8,000 |
| Single-building school / parochial (16–32) | $12,000 – $30,000 |
| Multi-wing / yeshiva campus (32–64) | $25,000 – $48,000 |
| Multi-building campus (64–128) | $40,000 – $95,000+ |
| College / institutional | quoted per phase; $200,000+ full campus |
| Service after install (v2.3 §9 protected) | $195/hr, 3-hr minimum ($585) |

Inconsistencies found in the existing silo (FLAG for Anwar): Bronx shows $495–$1,045/camera and $5,000–$8,800 daycare (≈1.10×, but §9 says Bronx = 1.00×); Queens shows the same numbers as Bronx (≈1.10×, §9 says 1.05×); Manhattan, Staten Island and Nassau all show $540–$1,140 (≈1.20×; §9 says 1.25 / 1.10 / 1.15). The NYC hub uses a different tier table ($4,500–$9,500 daycare, $9,000–$16,000 small parochial, …). No BYOE / labor-only price exists anywhere in the silo. Old pages carry the three-year warranty paragraph (must be replaced by the one-year terms sentence on rebuild).

## 1. Reddit
- **"site:reddit.com school security cameras private school installer"** · Firecrawl search · https://www.reddit.com/r/SecurityCamera/comments/1g0nb3u/researching_options_for_cameras_for_a_small/ (excerpt) · Small private school researching cameras; advice thread mentions using equipment quoted by the alarm company and doing labor themselves. · Brooklyn page: AI Reality Check (DIY vs installed).
- same query · https://www.reddit.com/r/msp/comments/1de3j08/new_security_cameras_for_school/ (excerpt) · "Many states in the US require that you be a licensed security company with the state in order to sell/install cameras. Look at Verkada or ..." · Brooklyn page: Q&A (licensing), Equipment (cloud-licensed platforms).
- same query · https://www.reddit.com/r/NYCTeachers/comments/1ba0t6d/is_your_doe_school_getting_cameras/ (excerpt) · NYC teachers discussing DOE installing cameras in their schools; commenter: "It is completely legal for the school to install cameras anywhere they want it is public property". · Brooklyn page: The Neighborhood (DOE schools run their own system).
- same query · https://www.reddit.com/r/k12sysadmin/comments/q62cqh/what_security_cameras_are_your_schools_using/ (excerpt) · K-12 sysadmins compare on-premise VMS vs cloud. · Equipment section.
- **"site:reddit.com Brooklyn daycare cameras parents watch live feed"** · Firecrawl search · https://www.reddit.com/r/nycparents/comments/1uxbj39/looking_for_a_daycare_with_cameras_in_nyc_any/ (excerpt) · NYC parents looking for daycares with cameras; one says their daycare has cameras "but they aren't live-streamed for the parents to watch all day". · Brooklyn page: Q&A (parent live view), Building Specialists (daycare).
- same · https://www.reddit.com/r/nycparents/comments/1w0eguj/daycares_with_cameras/ (excerpt) · "some daycares do use cameras that parents can access, but it's less common than in other places." · Brooklyn page: Q&A (parent live view).
- same · https://www.reddit.com/r/Greenpoint/comments/1pjevc7/need_help_getting_video_security_footage/ (excerpt) · Greenpoint family seeking footage after a daycare incident: "The daycare hasn't given clear answers, and the Department of Health follow-up has been poor." · Brooklyn page: The Neighborhood (footage-retrieval pain), Q&A (export).
- Thread bodies: EMPTY (not accessible in build env — Reddit blocked for scrape).

## 2. Google PAA
EMPTY (not accessible in build env). Substitute: question intents taken from the Reddit/news items above and from the register below.

## 3. Google PASF
EMPTY (not accessible in build env).

## 4. Answer the Public
EMPTY (not accessible in build env).

## 5. Google AI Overview
EMPTY (not accessible in build env). The Reality Check section on each page must therefore not quote an AI Overview verbatim; it addresses the generic claims found in the vendor/marketplace results returned for the same queries (e.g. eufy blog https://www.eufy.com/eu-de/blogs/security-camera/school-security-cameras and charterts.com "3 Questions to Consider When Installing Security Cameras in Schools" https://charterts.com/?p=16637, both excerpt only), and states that it is paraphrasing common summary claims.

## 6/7. Landmarks & use cases — see area sections.

## 8. Bing & DuckDuckGo
EMPTY (not accessible in build env as separate surfaces; WebSearch backend not identified).

## 9. Local news / 10. Hyperlocal (silo-wide items)
- **"NYC DOE school safety agents NYPD School Safety Division cameras public schools"** · WebSearch → WebFetch · https://en.wikipedia.org/wiki/New_York_City_Police_Department_School_Safety_Division · NYPD School Safety Division is the law-enforcement agency for DOE schools; ~5,000 School Safety Agents (infobox 5,147); division transferred from the Board of Education to NYPD in 1998. · Brooklyn page: The Neighborhood, facts list.
- same query · https://citylimits.org/what-do-cameras-cure-system-gets-own-scrutiny/ (City Limits, Jan 21 2008) · DOE + School Construction Authority designed the IPDVS camera system in 2003, first implemented July 2004; authorized by Local Law 52 of 2004; run by DOE Office of School and Youth Development; NYPD school safety agents watch live feeds; ~6,000 cameras in 130 buildings projected by end of 2008; ~$120M. · Brooklyn page: The Neighborhood, facts list, AI Reality Check.
- **"NYS Nonpublic School Safety Equipment (NPSE) grant cameras 2025 2026"** · WebSearch → WebFetch · https://www.nysed.gov/nonpublic-schools/nonpublic-school-safety-equipment-npse-grant-0 · NPSE = reimbursement program for religious and independent schools; non-competitive, formula-driven, allocated per pupil on prior-year nonpublic enrollment; inaugural year 2013-14; Year 10 = $45 million; Years 11-13 (FY 2023-24 to 2025-26) combined; "Beginning in 2025 there will be a competitive component (RFP application)"; administered by NYSED Office of Religious and Independent School Support (ORISS). Equipment list is in separate guidance (not read). · Brooklyn page: Q&A (funding), Pricing.
- **"NYC Local Law nonpublic school security guard reimbursement…"** · WebSearch → WebFetch · https://www.nyc.gov/assets/dcas/downloads/pdf/business/local_law_2.pdf · Local Law 2 of 2016 (Admin Code §10-172): city reimburses eligible nonprofit nonpublic schools for security guards — one guard at 300–499 students, two at 500+, one more per additional 500; annual cap $19.8M; guards must be from a qualified provider list. Covers guards, not cameras. · Brooklyn page: Q&A (guard program vs cameras), facts list.
- **"New York State Education Department facial recognition ban schools 2023"** · WebSearch → WebFetch · https://www.nysed.gov/news/2023/state-education-department-issues-determination-biometric-identifying-technology-schools · Sept 27 2023 Commissioner's determination under State Technology Law §106-b: schools in NYS may not purchase or use facial recognition technology; other biometrics decided locally. Page does not say whether nonpublic schools are covered. · Brooklyn page: Equipment, AI Reality Check (no facial recognition).
- **"Landmarks Preservation Commission security cameras rules…"** · WebSearch → WebFetch · https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf · LPC staff can approve cameras when: no more than 2 cameras per 25 ft of frontage (small buildings) or 3 per 25 ft (large/institutional); not on primary facade unless no other option; attach at mortar joints/plain masonry/wood/metal, not through cast iron or decorative surfaces; small and painted to blend; ~10 inches max visible conduit; manufacturer cut sheets filed via Portico. · Brooklyn page: Building Specialists, Commercial compliance, Q&A.
- **"NYC DOB permit required low voltage security camera installation…"** · WebSearch → WebFetch · https://www.nyc.gov/assets/buildings/local_laws/ll128of2024.pdf · Local Law 128 of 2024: low-voltage work (<50 V signaling/communication/alarm/data) exempt from electrical permits when done by a licensed master/special electrician or a "qualified person"; life-safety-connected wiring and control circuits switching light/heat/power need a master or special electrician; fire alarm separately under FDNY. Effective date not confirmed from excerpt. · Brooklyn page: Commercial compliance, Q&A.
- **"NYC Health Code Article 47 child care … OCFS regulations cameras"** · WebSearch → WebFetch · https://regulations.justia.com/states/new-york/title-18/chapter-ii/subchapter-c/article-2/part-418/subpart-418-1/section-418-1-15 · 18 NYCRR 418-1.15(b)(9): cameras may not substitute for direct supervision; may transmit images of children "in common rooms, hallways and play areas only"; bathrooms and changing areas must be free of video surveillance; parents/staff must be told cameras are in use and where. (Part 418-1 is OCFS's day care center rule; NYC group child care centers are permitted under Article 47 of the NYC Health Code — see CCC testimony title https://archive.cccnewyork.org/data-and-reports/publications/ccc-testimony-regarding-the-proposed-amendments-to-article-47-of-the-new-york-city-health-code-related-to-child-care-services-at-family-shelters, excerpt.) · Brooklyn page: Building Specialists (daycare), Q&A.
- same · https://nysenate.gov/legislation/bills/2025/A4530 · A4530 (Morinello) would require video recording in day care areas for children ≤3, 90-day retention; in Assembly Children & Families committee, referred Jan 7 2026 — not law. · Brooklyn page: AI Reality Check (no daycare camera mandate yet).
- **"Securing Communities Against Hate Crimes grant DCJS nonpublic schools…"** · WebSearch → WebFetch · https://www.governor.ny.gov/apply-securing-communities-against-hate-crimes-grant-program · SCAHC: DCJS funding for nonprofits at risk of hate crimes because of ideology/beliefs/mission; lists alarms, panic buttons, fences, shatter-resistant glass, PA systems "among other items"; RFP posted by DCJS. Page itself does not name cameras or schools. · Brooklyn page: Q&A (funding).
- **"Brooklyn yeshiva security cameras grant news"** · WebSearch → WebFetch · https://www.brooklyneagle.com/articles/2017/2/28/cuomo-beef-security-yeshivas · Brooklyn Eagle (Feb 28 2017): $25M state grant program let yeshivas and day care centers improve security, eligible uses incl. camera and monitoring systems and lighting. · Brooklyn page: The Neighborhood.
- **"Education Law 2801-b"** · WebSearch → WebFetch · https://www.nysenate.gov/legislation/laws/EDN/2801-B · Education Law §2801-b: State School Safety Improvement Teams (DHSES, State Police, DCJS, SED) review safety plans submitted voluntarily by districts under 125,000 inhabitants, BOCES, nonpublic schools and county vocational boards. · Brooklyn page: Q&A (plan review), Commercial compliance.
- **"FAR 52.204-25 … section 889"** · WebSearch · https://www.acquisition.gov/far/52.204-25 (title only) · FAR clause implementing NDAA FY2019 §889 (covered telecom/video surveillance equipment incl. Hikvision, Dahua, Hytera). · Equipment.

## 11. Yelp 1–3★
- **"security camera installation Brooklyn yelp reviews school"** · Firecrawl search · https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Brooklyn%2C+NY (excerpt: listing page only) · Review bodies: EMPTY (not accessible in build env).

## Keyword layers (silo)
- Service: school security camera installation, school CCTV installation, school surveillance system, classroom camera, school camera upgrade, school camera repair.
- Problem: break-ins over weekends/holidays, vandalism/graffiti, door propping, unknown visitors at dismissal, missing footage when parents/police ask, analog system failing.
- Technology: IP cameras, NVR, PoE, fiber link between buildings, video door station/intercom, access control, mass notification (adjacent), NDAA-compliant hardware.
- Industry: Catholic/parochial academies, yeshivas and Jewish day schools, independent schools, charter schools, 3-K/Pre-K CBOs, daycare centers, after-school programs, colleges.
- Geographic: per area page.

## Question register

Extracted programmatically on 2026-10-18 from all 16 existing `school-security-camera-installation-*.html` pages with the `tools/check_page.py` parser (every `.faq-question` plus every h2/h3/summary ending in "?"). Pages being rebuilt must not repeat any of these in meaning, and must append their own questions below.

### school-security-camera-installation-bronx (23 questions)

- Need School Camera Repair in the Bronx Today?
- How many cameras does a Bronx school building need?
- What does the elevated train actually do to cameras?
- Does Throggs Neck really need marine-grade cameras?
- Can a driveway camera record the street beyond our gate?
- Our charter shares a building with another program. Whose cameras are they?
- Who watches the building over summer recess?
- Will new cameras work with our existing buzzer and burglar alarm?
- Is there dedicated security funding for Bronx religious schools?
- Who ends up owning the recordings?
- What does a school camera system cost in the Bronx?
- How do you decide the camera count for our building?
- Is facial recognition allowed in any Bronx school?
- Can cameras go inside classrooms?
- Which spaces can never be recorded?
- How long should we keep footage?
- Can you install while school is in session?
- Which brands do you install, and why does NDAA §889 matter?
- What funding can Bronx schools use for cameras?
- Will you integrate cameras with our buzzer, alarm, and door hardware?
- Do you repair or take over systems someone else installed?
- Are your technicians licensed and suited to school settings?
- Need Repair on a Bronx School System Right Now?

### school-security-camera-installation-brooklyn (23 questions)

- Need School Camera Repair in Brooklyn Today?
- How many cameras does a Brooklyn school building need?
- Does the NPSE grant apply to Brooklyn yeshivas and religious schools?
- Is it legal for our entrance camera to see the sidewalk?
- Should the rear schoolyard be covered after hours?
- Can one recorder serve a main building plus an annex across the street?
- Who watches the building in August?
- Will new cameras work with the intercom and alarm we already own?
- Are there special security funds for Jewish schools?
- Who ends up owning the footage?
- What does a school camera system cost in Brooklyn?
- How do you decide how many cameras our building needs?
- Is facial recognition allowed in any Brooklyn school?
- Can we put cameras inside classrooms?
- Which locations are off-limits for cameras?
- How much footage history should we keep?
- Can installation happen while classes run?
- Which brands do you use, and why does NDAA matter?
- Is grant money available for Brooklyn school cameras?
- Will you tie cameras into our buzzer, alarm, and door hardware?
- Do you fix or adopt systems another company installed?
- Are your technicians licensed and appropriate for school settings?
- Need Repair on a Brooklyn School System Right Now?

### school-security-camera-installation-dutchess-county (23 questions)

- Dutchess School Camera System Down Right Now?
- How many cameras does a Dutchess school or campus need?
- How do you install cameras on a historic or Register-listed building?
- What actually protects historic copper gutters and downspouts?
- What do underwriters and placement consultants expect from a boarding campus?
- What changes on an estate-scale property with a long drive?
- Can a residential campus lawfully camera its grounds?
- What does ridge-country winter do to the hardware spec?
- Is there funding help for Dutchess nonpublic schools?
- When the project closes, who owns the footage?
- What does a school camera system cost in Dutchess County?
- How do you count cameras for a campus with acreage and multiple eras of buildings?
- Is facial recognition permitted at any Dutchess school?
- Can cameras go inside classrooms or seminar rooms?
- Which spaces can never be recorded?
- How much recorded history should we keep?
- Can installation work around the academic calendar and historic-building approvals?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Dutchess schools use for camera work?
- Will the cameras tie into our existing buzzer and alarm?
- Do you repair or take over systems from other installers?
- Are your technicians licensed and appropriate for school and residential settings?
- Need a Dutchess School System Repaired Today?

### school-security-camera-installation-hudson-valley (34 questions)

- Need School Camera Repair in the Hudson Valley Today?
- How much do school security cameras cost in the Hudson Valley?
- Who installs school cameras in Westchester?
- Who installs school cameras in Rockland?
- Are cameras allowed in private schools in NY?
- Can daycare parents demand live camera access?
- What cameras do schools actually use?
- How long do schools keep camera footage?
- Do school cameras work in rural darkness?
- Can school cameras survive Hudson Valley winters?
- Who repairs school camera systems near me?
- Do grants pay for school cameras in NY?
- Is DIY school camera installation legal?
- How many cameras does a Hudson Valley school campus need?
- What does the NPSE grant cover for Valley yeshivas and religious schools?
- Can boarding schools put cameras near dormitories?
- Should the driveway and carline be covered?
- What happens to school camera systems during ice storms and outages?
- Do rural internet connections limit remote school camera viewing?
- Can cameras integrate with our existing alarm, intercom, or panic system?
- What about summer camps using our school building?
- Who owns the footage — the school or the camera company?
- How much does school security camera installation cost in the Hudson Valley?
- Is facial recognition legal in Hudson Valley schools?
- Can cameras be installed in classrooms or near dormitories?
- Where can school cameras never be installed?
- How long should a Hudson Valley school keep camera footage?
- Can you install while school is in session?
- What camera brands do you install for Hudson Valley schools, and what is NDAA compliance?
- Can grants pay for school security cameras in the Hudson Valley?
- Do you integrate cameras with buzzers, intercoms, panic alarms, and access control?
- Do you repair or take over existing school camera systems in the Hudson Valley?
- Are your installers licensed and vetted to work in schools?
- Need Repair on a Hudson Valley School System Right Now?

### school-security-camera-installation-long-island (35 questions)

- Need School Camera Repair on Long Island Today?
- How much do school security cameras cost on Long Island?
- Who installs school cameras in Nassau County?
- Who installs school cameras in Suffolk County?
- Are cameras allowed in private schools in NY?
- Can daycare parents demand camera access?
- What cameras do schools actually use?
- How long do schools keep camera footage?
- Do school cameras record audio?
- Can school cameras be monitored remotely?
- Who repairs school camera systems near me?
- Do grants pay for school cameras in NY?
- Is DIY school camera installation legal?
- Do Long Island public schools share camera feeds with police?
- How many cameras does a typical Long Island school need?
- What does Alyssa’s Law mean for Long Island schools?
- Can a Long Island school put cameras on athletic fields?
- Should the bus loop and parent pickup line be covered?
- Do salt air and coastal weather really affect school cameras?
- Can cameras integrate with our existing school alarm or intercom?
- What happens to school camera systems over summer break?
- Who owns the footage — the school or the camera company?
- How much does school security camera installation cost on Long Island?
- How many cameras does a Long Island school campus need?
- Is facial recognition legal in Long Island schools?
- Can cameras be installed in classrooms?
- Where can school cameras never be installed?
- How long should a Long Island school keep camera footage?
- Can you install while school is in session?
- What camera brands do you install for Long Island schools, and what is NDAA compliance?
- Can grants pay for school security cameras on Long Island?
- Do you integrate cameras with buzzers, intercoms, panic alarms, and access control?
- Do you repair or take over existing school camera systems on Long Island?
- Are your installers licensed and vetted to work in schools?
- Need Repair on a Long Island School System Right Now?

### school-security-camera-installation-manhattan (34 questions)

- Need School Camera Repair in Manhattan Today?
- How much do school security cameras cost in Manhattan?
- Who installs school cameras in Manhattan?
- Are cameras allowed in private schools in NY?
- Can NYC daycare parents demand live camera access?
- What cameras do NYC schools actually use?
- How long do schools keep camera footage?
- Do school cameras record audio?
- Can school cameras be monitored remotely?
- Who repairs school camera systems near me?
- Do grants pay for school cameras in NY?
- Do cameras work on landmarked buildings?
- Is DIY school camera installation legal?
- How many cameras does a Manhattan school building need?
- How do installs work around freight elevators and building rules?
- Can cameras cover the dismissal scene on a public sidewalk?
- What about the rooftop play deck?
- Do co-op or condo neighbors get a say in our camera install?
- What happens to school camera systems in August?
- Can cameras integrate with our existing intercom or alarm?
- Do Jewish day schools have extra funding options for cameras?
- Who owns the footage — the school or the camera company?
- How much does school security camera installation cost in Manhattan?
- Is facial recognition legal in Manhattan schools?
- Can cameras be installed in classrooms?
- Where can school cameras never be installed?
- How long should a Manhattan school keep camera footage?
- Can you install while school is in session?
- What camera brands do you install for Manhattan schools, and what is NDAA compliance?
- Can grants pay for school security cameras in Manhattan?
- Do you integrate cameras with buzzers, intercoms, panic alarms, and access control?
- Do you repair or take over existing school camera systems in Manhattan?
- Are your installers licensed and vetted to work in schools?
- Need Repair on a Manhattan School System Right Now?

### school-security-camera-installation-nassau-county (23 questions)

- Nassau School Camera System Down Right Now?
- How many cameras does a Nassau school property need?
- What makes postwar single-story schools harder to secure?
- Do Nassau schools really need wildlife-filtered detection?
- What changes for schools near the water on the South Shore?
- Can gate cameras at an estate campus record the road beyond?
- Who watches the building across ten weeks of summer?
- Will new cameras work with our existing buzzer and alarm?
- Is there dedicated security funding for Nassau’s religious schools?
- Who ends up owning the recordings?
- What does a school camera system cost in Nassau County?
- How do you set the camera count for our property?
- Is facial recognition allowed in any Nassau school?
- Can cameras go inside classrooms?
- Which spaces can never be recorded?
- How much recorded history should we keep?
- Can you install during the school year?
- Which brands do you install, and why does NDAA §889 matter?
- What funding can Nassau schools use for camera work?
- Will you integrate cameras with our buzzer, alarm, and door hardware?
- Do you repair or take over systems another company installed?
- Are your technicians licensed and suited to school settings?
- Need a Nassau School System Repaired Today?

### school-security-camera-installation-nyc (33 questions)

- How much do school security cameras cost?
- How many cameras does a school need?
- Can schools put cameras in classrooms?
- Are cameras allowed in school bathrooms?
- Who can view school camera footage?
- How long do schools keep camera footage?
- Can parents request school video?
- Do daycares need cameras in New York?
- What camera brands are banned for schools?
- Will cameras lower a school’s insurance costs?
- Can school cameras record audio?
- Who pays for school security cameras?
- What is the best security camera system for schools?
- How much does it cost to install security cameras in a school?
- Are security cameras effective in schools?
- Can teachers be recorded in the classroom?
- Is facial recognition legal in New York schools?
- How many security cameras does a high school need?
- Do private schools need security cameras?
- What is NDAA compliance for school cameras?
- How long is school camera footage kept?
- How much does school security camera installation cost in NYC?
- How many security cameras does a school need?
- Can cameras be installed in classrooms?
- Where can school cameras never be installed?
- How long should a school keep camera footage?
- Can you install while school is in session?
- What camera brands do you install for schools, and what is NDAA compliance?
- Can grants pay for school security cameras?
- Do you integrate cameras with buzzers, intercoms, and access control?
- Do you repair or take over existing school camera systems?
- Are your installers licensed and vetted to work in schools?
- Questions answered. Building surveyed next?

### school-security-camera-installation-orange-county (23 questions)

- Orange County School Camera System Down Right Now?
- How many cameras does an Orange County school property need?
- What does “growth-ready” actually mean in a camera system?
- How do you protect rooftop HVAC from copper theft?
- What changes on a farm-adjacent or open-land campus?
- Who responds to a 2 a.m. alert when the Sheriff is twenty minutes out?
- Can a boarding school lawfully camera its residential areas?
- What does mountain weather do to the hardware spec?
- Is there funding help for Orange County’s nonpublic schools?
- At the end of the job, who owns the footage?
- What does a school camera system cost in Orange County?
- How do you set the camera count for a property with acreage?
- Is facial recognition allowed in any Orange County school?
- Can cameras go inside classrooms?
- Which areas can never be recorded?
- How much recorded history should we keep?
- Can installation work around our calendar — school year, break windows, yom tov?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Orange County schools use for camera work?
- Will the cameras tie into our existing buzzer and alarm?
- Do you repair or take over systems other companies installed?
- Are your technicians licensed and appropriate for school settings?
- Need an Orange County School System Repaired Today?

### school-security-camera-installation-putnam-county (23 questions)

- Putnam School Camera System Down Right Now?
- How many cameras does a Putnam school actually need?
- What makes a small-school system different from a scaled-down big one?
- How do you design around barns, paddocks, and animal areas?
- What does a wooded quarter-mile driveway change?
- Who responds at 1 a.m. when the nearest deputy is miles of back road away?
- Can a residential program lawfully camera its campus?
- What does watershed-adjacent property change about installation?
- Is there funding help for Putnam’s nonpublic and residential schools?
- When the job’s done, who owns the footage?
- What does a school camera system cost in Putnam County?
- How do you set the camera count on a wooded property?
- Is facial recognition allowed in any Putnam school?
- Can cameras go inside classrooms?
- Which spaces can never be recorded?
- How much recorded history should a school keep?
- Can installation work around the school calendar?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Putnam schools use for camera work?
- Will the cameras tie into our buzzer and alarm?
- Do you repair or take over systems from other installers?
- Are your technicians licensed and suited to school settings?
- Need a Putnam School System Repaired Today?

### school-security-camera-installation-queens (23 questions)

- Need School Camera Repair in Queens Today?
- How many cameras does a freestanding Queens campus need?
- Does salt air really change the camera spec on the Rockaways?
- Can the parking lot camera legally record the street beyond it?
- What about modular classrooms and trailer annexes?
- Can evening sports and rentals be covered without new wiring?
- Who monitors the building during summer recess?
- Will new cameras cooperate with our existing buzzer and alarm?
- Is there dedicated security money for Jewish schools in Queens?
- Who ends up owning the recordings?
- What does a school camera system cost in Queens?
- How is the camera count determined for a freestanding campus?
- Is facial recognition permitted in any Queens school?
- Can classrooms be covered?
- Which spaces can never have cameras?
- How much video history should we hold?
- Can work proceed while school is in session?
- Which brands do you install, and why does NDAA matter here?
- What funding exists for Queens school cameras?
- Will you integrate with our buzzer, alarm, and door hardware?
- Do you repair or adopt systems installed by others?
- Are your technicians licensed and suitable for school environments?
- Need Repair on a Queens School System Right Now?

### school-security-camera-installation-rockland-county (22 questions)

- Rockland School Camera System Down Right Now?
- How many cameras does a Rockland school or campus need?
- How do you connect cameras across separate buildings?
- Can installation be scheduled around the yeshiva calendar?
- What protects a bus yard overnight?
- Do you handle security for buildings still under construction?
- What does winter do to exterior cameras here?
- Will the cameras integrate with our existing buzzer and alarm?
- Is there dedicated funding for Rockland’s nonpublic schools?
- At the end of the project, who owns the footage?
- What does a school camera system cost in Rockland County?
- How do you count cameras for a multi-building institution?
- Is facial recognition permitted in any Rockland school?
- Can cameras go inside classrooms or shiur rooms?
- Which spaces can never be recorded?
- How much recorded history should we keep?
- Can you work around our calendar — Shabbos, yom tov, bein hazmanim?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Rockland schools use for camera work?
- Do you repair or take over systems from other installers?
- Are your technicians licensed and suited to our institutions?
- Need a Rockland School System Repaired Today?

### school-security-camera-installation-staten-island (23 questions)

- School Camera System Down on Staten Island?
- How many cameras does a typical Staten Island school need?
- What does “marine-tiered” exterior spec actually mean?
- Do deer and turkeys really break camera systems here?
- Our school flooded in 2012. What changes in the camera design?
- Can driveway cameras at a hilltop school record the street below?
- Who monitors the building over summer recess?
- Will new cameras integrate with our existing buzzer and alarm?
- Is there security funding for Staten Island’s religious schools?
- Who ends up owning the footage?
- What does a school camera system cost on Staten Island?
- How do you determine the camera count for our property?
- Is facial recognition permitted in any island school?
- Can cameras be placed inside classrooms?
- Which areas can never be recorded?
- How much footage history should we keep?
- Can installation happen while school is in session?
- Which brands do you install, and why does NDAA §889 matter here?
- What funding can island schools use for camera projects?
- Will you tie cameras into our buzzer, alarm, and door hardware?
- Do you repair or adopt systems another company installed?
- Are your technicians licensed and appropriate for school environments?
- Need a Staten Island School System Repaired Right Now?

### school-security-camera-installation-suffolk-county (23 questions)

- Suffolk School Camera System Down Right Now?
- How many cameras does a Suffolk school property take?
- What does Suffolk’s size change about a camera project?
- Do you handle the deer problem or do we live with false alerts?
- What’s different about Sound-side versus ocean-side installs?
- Who responds to an alert on the East End, where police are spread thin?
- Can a boarding school lawfully camera its residential areas?
- Will new cameras tie into our existing buzzer and burglar alarm?
- Is there funding help for Suffolk’s nonpublic schools?
- At the end of the job, who owns the footage?
- What does a school camera system cost in Suffolk County?
- How do you decide camera count on a big property?
- Is facial recognition allowed at any Suffolk school?
- Can cameras go inside classrooms?
- Which areas can never be recorded?
- How long should our school keep footage?
- Can you install while school is in session?
- Which camera brands do you install, and what does NDAA §889 change?
- What funding can Suffolk schools tap for cameras?
- Do the cameras integrate with our buzzer, alarm, and door hardware?
- Do you repair systems or take over ones another installer abandoned?
- Are your technicians licensed and appropriate for school environments?
- Need a Suffolk School System Fixed Today?

### school-security-camera-installation-ulster-county (23 questions)

- Ulster School or Camp Camera System Down Right Now?
- How many cameras does an Ulster school or camp need?
- What does “winterizing” a camp camera system actually involve?
- Where can cameras lawfully point at a sleepaway camp?
- What protects a shuttered camp’s kitchen and equipment buildings all winter?
- Who responds to a 1 a.m. alert when the deputy is mountain miles away?
- What changes when a public rail trail borders school ground?
- What does a Catskills winter do to the hardware spec?
- Is there funding help for Ulster’s nonpublic schools and camps?
- When the job’s done, who owns the footage?
- What does a school or camp camera system cost in Ulster County?
- How do you count cameras for a property with acreage, buildings, and a gate?
- Is facial recognition allowed at any Ulster school?
- Can cameras go inside classrooms?
- Which spaces can never be recorded — school or camp?
- How much recorded history should we keep?
- Can installation work around the school calendar and the camp season?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Ulster schools and camps use?
- Will the cameras tie into our existing buzzer and alarm?
- Do you repair or take over systems from other installers?
- Are your technicians licensed and appropriate for schools and camps?
- Need an Ulster School or Camp System Repaired Today?

### school-security-camera-installation-westchester-county (23 questions)

- Westchester School Camera System Down Right Now?
- How many cameras does a Westchester school property need?
- What does Westchester’s terrain change about camera design?
- Do you really tune out deer, coyotes — even bears?
- What does winterization actually involve?
- How do you handle cameras near property lines and neighbors?
- Who watches a campus over breaks and summer?
- Will new cameras integrate with our existing buzzer and alarm?
- Is there security funding for Westchester’s nonpublic schools?
- At the end of the project, who owns the footage?
- What does a school camera system cost in Westchester County?
- How do you set the camera count on a terraced or wooded property?
- Is facial recognition permitted in any Westchester school?
- Can cameras go inside classrooms?
- Which spaces can never be recorded?
- How much recorded history should we keep?
- Can you install during the school year?
- Which brands do you install, and what does NDAA §889 change?
- What funding can Westchester schools use for camera work?
- Will the cameras integrate with our buzzer, alarm, and door hardware?
- Do you repair or take over systems from other installers?
- Are your technicians licensed and suited to school environments?
- Need a Westchester School System Repaired Today?


### school-security-camera-installation-brooklyn — REBUILT 2026-10-18 (replaces the pre-rebuild list above for this page)

- School Cameras Dark or Recorder Beeping in Brooklyn? — Q&A / heading
- Our academy shares a building with the parish. Who has to approve the camera plan — the principal, the pastor or the diocese? — Q&A / heading
- We rent our classrooms from a church. Can we put cameras in, and what happens when the lease ends? — Q&A / heading
- Does our 3-K or Pre-K contract with the city require cameras? — Q&A / heading
- Our school is a 1920s brick building. How does cable reach the fourth floor without opening walls? — Q&A / heading
- Do we need a Department of Buildings permit for the camera wiring? — Q&A / heading
- Should the recorder sit in the principal's office? — Q&A / heading
- Can our old analog cameras and coax be reused, or does everything go? — Q&A / heading
- We have a city-reimbursed security guard at the door. How should the cameras work with the guard? — Q&A / heading
- What should the screen at our front desk actually show? — Q&A / heading
- Who in our school should hold the administrator password? — Q&A / heading
- What's the right way to give NYPD a clip from our system? — Q&A / heading
- How do we document the cost for a grant reimbursement? — Q&A / heading
- Our yeshiva runs Sunday classes and evening programs. Can alerts follow a different schedule on those days? — Q&A / heading
- Can the cameras become a way for someone to get onto our school network? — Q&A / heading
- How many exterior cameras will Landmarks allow on a school's street front? — Q&A / heading
- Our school is in a historic district but the inside isn't landmarked. Do interior cameras need approval? — Q&A / heading
- Can a state school safety team look at our plan before we spend money? — Q&A / heading
- Our after-school program uses a public school's gym in the evening. Can we install cameras there? — Q&A / heading
- What happens to our footage and equipment if the school closes or merges? — Q&A / heading
- Can one camera system serve the school by day and a weekend congregation or community group? — Q&A / heading
- Can you name our diocese, network or landlord as additional insured on your certificate? — FAQ
- Can we spread the project over two school years? — FAQ
- What training do our staff get when the system is finished? — FAQ
- How often should school cameras be cleaned and checked? — FAQ
- Should we post signs that cameras are in use? — FAQ
- If a yard camera gets smashed, is the replacement covered? — FAQ
- We're opening a new charter school next September. When should the camera plan start? — FAQ
- Do you take out the old cameras and cable when you replace a system? — FAQ
- What happens on the free walkthrough, and how long does it take? — FAQ
- Do your technicians see student footage, and will they keep it confidential? — FAQ


## Brooklyn

Page: `school-security-camera-installation-brooklyn` (REBUILD 2026-10-18). Phone (347) 934-8335, Brooklyn GBP (1282 Troy Ave). Pricing: Brooklyn base 1.00× (silo base table above, used as-is).

**Thesis:** in Brooklyn the DOE's public schools already have a city-built camera network watched by NYPD school safety agents, so the real buyers are the schools and programs outside it — Catholic academies, yeshivas/Jewish day schools, independent schools, charter schools in their own space, CBO 3-K/Pre-K and daycare centres, after-school programs — and the page is organised around who owns/approves the system, the building types they occupy (parish buildings, multi-building yeshivas, landmarked independents, leased charters, storefront/basement centres) and the rules that apply to them (LPC camera criteria, LL128 low-voltage, day care placement rules, NYSED facial-recognition ban, NPSE, LL2 guard program).

### Local research matrix
| Source | Query | Platform | URL | Finding | Used on |
|---|---|---|---|---|---|
| Reddit | "site:reddit.com Brooklyn daycare cameras parents watch live feed" | Firecrawl search | https://www.reddit.com/r/Greenpoint/comments/1pjevc7/need_help_getting_video_security_footage/ (excerpt) | Greenpoint family: daycare "hasn't given clear answers, and the Department of Health follow-up has been poor", seeking neighbours' footage | The Neighborhood ¶4; Sources |
| Reddit | same | Firecrawl search | https://www.reddit.com/r/nycparents/comments/1uxbj39/looking_for_a_daycare_with_cameras_in_nyc_any/ (excerpt) | NYC daycares that record but do not stream to parents | The Neighborhood ¶4; Building Specialists (3-K/daycare notes) |
| Reddit | "site:reddit.com school security cameras private school installer" | Firecrawl search | https://www.reddit.com/r/NYCTeachers/comments/1ba0t6d/is_your_doe_school_getting_cameras/ (excerpt) | DOE installs cameras in its own schools | Sources (supports Neighborhood ¶1) |
| PAA / PASF / ATP / AI Overview / Bing-DDG | — | — | — | EMPTY (not accessible in build env) | Reality Check states it paraphrases common summary claims, not a quoted Overview |
| Landmarks | "Packer Collegiate Institute Joralemon Street landmark…" | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Packer_Collegiate_Institute | 170 Joralemon St; founded 1845; Minard Lafever building opened Nov 1854; Brooklyn Heights Historic District; PK-12 | Coverage card 1; Neighborhood ¶2 |
| Landmarks | "Saint Ann's School Brooklyn Heights Bosworth Building…" | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Crescent_Athletic_Club_House | 129 Pierrepont St at Clinton St; completed 1906 (Frank Freeman); Bosworth Building of Saint Ann's School since 1966 purchase | Coverage card 1; Neighborhood ¶2 |
| Landmarks | "Poly Prep Country Day School Dyker Heights campus acres address" | WebSearch → WebFetch | https://en.wikipedia.org/wiki/Poly_Prep | 9216 Seventh Ave (26 acres); lower school 50 Prospect Park West; founded 1854 | Coverage cards 2–3; Neighborhood ¶2 |
| Landmarks / news | "Brooklyn private school security news 2025 2026…" | WebSearch → WebFetch | https://patch.com/new-york/parkslope/berkeley-carroll-threatened-school-shooting-documents-show | Berkeley Carroll, 181 Lincoln Place; Feb 7–8 2022 online threat to a ninth-grader; security increased; FBI + NYPD Intelligence investigating, advised against closing | Neighborhood ¶5; Coverage card 2 |
| Use cases | "Diocese of Brooklyn Catholic academies number of schools…" | WebSearch → WebFetch | https://en.wikipedia.org/wiki/List_of_schools_in_the_Roman_Catholic_Diocese_of_Brooklyn | 7 Brooklyn Catholic high schools (Bishop Loughlin–Fort Greene; Cristo Rey Brooklyn & Nazareth Regional–East Flatbush; Fontbonne Hall–Fort Hamilton; St. Edmund Prep–Homecrest; Saint Saviour–Park Slope; Xaverian–Bay Ridge) + 30 elementary academies | Neighborhood ¶2; facts list; Coverage cards 5–6 |
| Use cases | "NYC 3-K Pre-K community-based organizations…" | WebSearch → WebFetch | https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/education/2025/2025-may-utilization-up-capacity-down-a-look-at-3k-and-prek-trends-in-nyc.pdf | 2023-24: 3-K 34,900 of 52,373 seats in CBOs vs 8,307 district; Pre-K 40,376 of 74,323 CBO vs 27,134 district (citywide; no Brooklyn split) | Facts list |
| Use cases | "Borough Park Williamsburg yeshiva enrollment…" | WebSearch | (titles only: Hebrew Institute of Boro Park, Nesivos Hatalmud, JTA 2025 yeshiva standards) | No enrolment figure retrieved → none used | — |
| Local news | "Brooklyn school break-in burglary caught on camera 2025…" | WebSearch → WebFetch | https://brooklyn.news12.com/burglar-sought-in-series-of-jewish-school-break-ins | News 12 Brooklyn, May 28 2025: Kensington Jewish school — Feb 2025 side window broken with rock; May 15 side door forced, $360 + cards; following weekend fence climbed, wall damaged, $300 — only last incident on camera | Neighborhood ¶3; Commercial (13th Ave bullet) |
| Local news | same | WebSearch → WebFetch | https://brooklyn.news12.com/man-wanted-in-borough-park-yeshiva-break-in-34776659 | News 12, July 23 2012: man broke into Borough Park yeshiva during Shabbat; seen trying to cover a surveillance camera | Neighborhood ¶3; Commercial (13th Ave) |
| Local news | "Brooklyn private school security news…" | WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/pilot-program-named-after-leiby-kletzky-to-put-security-cameras-in-borough-park-flatbush | CBS NY May 20 2012: $1M pilot, ~150 community-owned cameras in Borough Park and Flatbush | Not used on page (street cameras, not schools) |
| Hyperlocal | "Brooklyn yeshiva security cameras grant news 2025" | WebSearch → WebFetch | https://www.brooklyneagle.com/articles/2017/2/28/cuomo-beef-security-yeshivas | Brooklyn Eagle Feb 2017: $25M state grants for yeshivas and day care centres, incl. cameras/monitoring and lighting | Sources (funding) |
| Hyperlocal | same | WebSearch | https://www.brooklynpaper.com/homeland-grants-shield-jewish-centers (title only) | Federal homeland-security grants to Brooklyn Jewish institutions (not read) | Not used |
| Licensing/permits | LPC, LL128, Article 47/OCFS (see silo §9) | WebFetch | see silo section | Staff-level LPC camera criteria; LL128 low-voltage permit exemption; day care camera placement rules | Building Specialists; Commercial compliance; Q&A (Landmarks, DOB); FAQ (signs) |
| Yelp 1–3★ | "security camera installation Brooklyn yelp reviews school" | Firecrawl search | https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Brooklyn%2C+NY | Listing only; review bodies EMPTY (not accessible in build env) | — |

### Streets / corridors named on the page (descriptive only, no unsourced stats)
13th Avenue (Borough Park), Lee Ave & Bedford Ave (Williamsburg), Kingston Ave & Eastern Parkway (Crown Heights), Flatbush/Nostrand/Church Aves, Fifth & Third Aves (Bay Ridge), Coney Island Ave & Avenue J (Midwood), Joralemon St, Pierrepont St, Lincoln Place, Prospect Park West, Seventh Ave (Dyker Heights), Troy Ave (AESS office).

### House practices on the page that are NOT externally sourced (flag)
Brand mix (Uniview / Hanwha Wisenet / Axis, Lorex for small centres); "most systems recording again within 1–2 hours of arrival"; two-hour arrival windows; twice-yearly maintenance rhythm; walkthrough ≈1 hour + plan in a few business days; installer service account disabled after handover; COI/additional-insured handling; signing school confidentiality agreements; labour-only (BYOE) install priced per camera after walkthrough (no BYOE price exists in silo); illustrative 18-camera parish-school plan (explicitly labelled as an illustration, not a project).

## Long Island (hub) — school-security-camera-installation-long-island

Built 2026-10-18 by b8-school-li (REBUILD of the crawled-not-indexed LI hub). Thesis: on Long Island a school camera system is a public-procurement project before it is a wiring job — ~125 separately governed districts, budget/bond votes, GML §103 sealed bids or BOCES cooperative contracts, NYSED Office of Facilities Planning oversight (NYC schools fall outside it), the District 4 Nassau–Suffolk tele-data prevailing wage, Project SAVE plans and Ed Law 2-d — on campuses spread over fields, lots and bus loops rather than stacked on a city block. Brooklyn page owns NYC private/parochial/yeshiva/charter/daycare angles; this page only touches nonpublic schools via LI-specific permit/grant facts.

### Research matrix (exact query · platform · URL · finding · page+section used)

| # | Source type | Exact query | Platform | URL | Finding | Used in |
|---|---|---|---|---|---|---|
| 1 | Reddit | "Suffolk County school bus stop-arm camera program BusPatrol tickets Nassau County school bus cameras" | Firecrawl search | https://www.reddit.com/r/longisland/comments/18rfmc1/bye_bye_school_bus_camera_program/ | Thread title "Bye bye school bus camera program" (r/longisland) referencing a Newsday piece on Nassau & Suffolk bus-camera developments. Page itself: EMPTY (not accessible in build env — scraper refuses reddit.com); excerpt only, not quoted on page. | Not used as a fact (context only) |
| 2 | Google PAA | — | — | — | EMPTY (not accessible in build env) | — |
| 3 | Google PASF | — | — | — | EMPTY (not accessible in build env) | — |
| 4 | Answer the Public | — | — | — | EMPTY (not accessible in build env) | — |
| 5 | Google AI Overview | — | — | — | EMPTY (not accessible in build env). "AI Reality Check" H3s are framed as common generic claims, not quotes of a captured Overview. | §10.5 framing only |
| 6a | Landmarks / institutions | "Western Suffolk BOCES headquarters address Dix Hills; Eastern Suffolk BOCES Patchogue 201 Sunrise Highway; Nassau BOCES Garden City 71 Clinton Road" | Firecrawl search | https://www.nassauboces.org/ ; https://www.wsboces.org/contact-us-2/ ; https://www.boces.org/regional-boces-directory/ ; https://www.esboces.org/about-us/locations | Nassau BOCES George Farber Administrative Center, 71 Clinton Rd, Garden City; WSBOCES central admin 507 Deer Park Rd, Dix Hills; ESBOCES 201 Sunrise Hwy, Patchogue | District/BOCES section cards; Landmarks section |
| 6b | Landmarks / districts | "Long Island 124 school districts Nassau 56 Suffolk 69" | WebSearch + WebFetch | https://en.wikipedia.org/wiki/List_of_Long_Island_public_school_districts_and_schools | "125 public school districts, containing a total of 656 public schools" (no per-county split on page) | Why section para 1; numbers list |
| 7a | Use cases — Smart Schools (Suffolk) | "Smart Schools Bond Act Long Island district investment plan security cameras Nassau Suffolk" | Firecrawl search + scrape (pdf parser) | https://www.islipufsd.org/smart-schools-bond-act-information ; https://files.smartsites.parentsquare.com/7734/26-10-13_smart-schools-investment-plan-2.pdf | Islip UFSD SSIP #2 presented Oct 13, 2026: cameras Wing Elem 29 ($54,763.02), Commack Road Elem 25 ($45,035.18), Sherwood Elem 23 ($39,903.56), Middle School 35 ($58,243.67), High School 22 ($44,031.57) = 134 cameras (plan text elsewhere says "additional 132 cameras"); Genetec Streamvault archiver $46,459.06; 180 APs $266,340.95; access control 5 doors Wing $15,805.19, 1 door Commack Rd $1,269.19; total ≈$571,851.39; process: 30-day website posting → second hearing → board resolution → NYSED portal → NYSED review → Smart Schools Review Board; reimbursement model; quotes valid 30–90 days; Plan #1 636 Chromebooks July 2026, $324,360 reimbursement awaited; comments to 215 Main St, Islip | Why para 3; Q&A Smart Schools cluster; AI check (cost, timeline); Equipment (archiver); Landmarks; FAQ (VMS) |
| 7b | Use cases — Smart Schools (Suffolk) | same query | Firecrawl scrape | https://www.pmschools.org/departments/technology/smart-schools-bond-act | Patchogue-Medford: preliminary plan approved Apr 24, 2017 meeting that served as public hearing; 30 days community feedback; final board approval June 1, 2017; submit to NYSED | Q&A "What has to happen between…" |
| 7c | Use cases — state | same | Firecrawl scrape | https://www.nysed.gov/edtech/smart-schools-bond-act | $2B bond approved by voters 2014; Office of Educational Design & Technology reviews SSIPs | Why para 3 |
| 7d | Use cases — state review threshold | "NYSED Office of Facilities Planning building permit security cameras low voltage project school district submission required" | Firecrawl gov search | https://p12.nysed.gov/mgtserv/smart_schools/docs/Special%20Education%20Guidance%20-%20FINAL%2020241104.pdf | High-tech security not requiring construction or ≤$100,000 capitalized cost → no formal capital-project review by Rate Setting/OSE/OFP, but must be code compliant | Why para 2; Q&A capital-project question |
| 8 | Bing & DuckDuckGo | — | — | — | EMPTY (not accessible in build env) | — |
| 9a | Local news — Newsday 2018 | (Firecrawl search) "Long Island school district bond vote security cameras vestibules 2025 OR 2026 Newsday" | Firecrawl scrape | https://www.newsday.com/long-island/education/school-safety-security-w24072 | July 26, 2018: 23 LI districts approved for $10,812,920 SSBA security (Brentwood $4,537,383; Valley Stream Central $1,954,631…); 37 of 124 districts had security items in 2018-19 budgets; capital projects ~9 months at SED (Borges, ASBO); NCPD trained 400+ principals + superintendents of all 56 Nassau districts + private/parochial/yeshivas; 177 on-duty patrol cars visit a school daily; Rave Panic Button Nassau 2016 (44 of 56), Suffolk $2M bond signed that week; Massapequa armed guards; Montauk interior cameras | Why para 2, numbers list, Two Counties, police paragraph, AI check |
| 9b | Local news — Newsday 2022 | same search | Firecrawl scrape | https://www.newsday.com/long-island/education/school-security-upgrades-dbb7te94 | Dec 17, 2022: Middle Country upgraded 564 cameras in $2M SSBA project incl. card access, booths; SCPD emergency access; Merrick analog→digital ~$200,000 three buildings; Jericho $1.6M cameras+badges+locks; Manhasset ~$44M bond Dec 8 with >$10M safety; Glen Cove $2.2M security in $30.5M bond Dec 6; ≥30 LI school cyber incidents in 3 years | Numbers list; Q&A vote question; FAQ (analog, network); Landmarks; AI check (police) |
| 9c | Local news — Newsday 2026 | same search | Firecrawl scrape | https://www.newsday.com/long-island/education/east-meadow-school-bond-vote-t1ftuzt4 | East Meadow $71.5M bond approved (Newsday updated Mar 5, 2026) 1,132–462; entrance vestibules, classroom door handles/locks, fire alarms districtwide; turf fields, lighting, bleachers; 20-year bond | Why para 5; Q&A vestibule; Landmarks |
| 9d | Local news — CBS NY 2013 | "Nassau BOCES cooperative bidding program security cameras districts" | WebSearch + WebFetch | https://www.cbsnews.com/newyork/news/long-island-goes-cutting-edge-on-school-security-live-feeds-to-police-cars | Apr 18, 2013: Nassau BOCES fibre network + command centre; police view feeds in emergencies; 3 districts incl. Roslyn (~80 cameras at Roslyn HS) | District section; AI check (police) |
| 9e | Local news — ABC7 2024 | bus-camera search above | Firecrawl scrape | https://abc7ny.com/post/suffolk-county-school-bus-camera-tickets-almost-dismissed/14981798/ | June 20–21, 2024: Suffolk dismissed ~90% of 9,000 backlogged bus-camera tickets after appellate ruling; ~3,000 of 8,000 at one Jericho Tpke stop, Smithtown; ~$2M lost | Q&A stop-arm question |
| 10 | Hyperlocal / county gov | same bus search | Firecrawl scrape | https://www.suffolkcountyny.gov/schoolbus | 2019 law S4524B/A4950B; Suffolk program via BusPatrol (stop-arm + internal cameras, DVR, GPS, LTE) at no cost to schools; long list of participating districts incl. ESBOCES & WSBOCES; 2019 East Meadow 10-bus study 615 illegal passes in a month | Q&A stop-arm question |
| 11 | Yelp 1–3★ | — | — | — | EMPTY (not accessible in build env) | — |

Additional primary sources (law, wages, guidance):

| Query | Platform | URL | Finding | Used in |
|---|---|---|---|---|
| "New York Education Law 2801-a district-wide school safety plan building-level emergency response plan 30 day public comment" | Firecrawl gov search | https://nysenate.gov/legislation/laws/EDN/2801-A ; https://regents.nysed.gov/sites/regents/files/424p12d1.pdf | District-wide plan: 30 days public comment + ≥1 public hearing, filed with commissioner within 30 days; building-level plans confidential (not subject to FOIL), filed with local police + State Police within 30 days; annual review; Reg 155.17 adopt by Sept 1 | Rules list; Q&A building-level plan; FAQ drawing |
| same gov search (result 8/9) | Firecrawl gov search | https://nysed.gov/sites/default/files/programs/facilities-planning/mps-2026.pdf ; https://nysed.gov/sites/default/files/programs/facilities-planning/safeschoolsbydesign-aguidebynysed-april2025.pdf | MPS 2026 S818: cameras only where no reasonable expectation of privacy; never facing toilets/locker/changing rooms; State Technology Law §106-b bans school facial recognition. Safe Schools by Design (Apr 2025): 4 functions; fully networked IP; video surveillance & use policy; interior cameras face exterior doors; cameras at all exterior doors; perimeter; higher resolution for plates; standardize by use, not manufacturer | Rules list; services; Q&A vestibule & phasing; equipment; FAQ policy & standardise; AI check facial recognition |
| OFP gov search above | Firecrawl gov search | http://nysed.gov/facilities-planning/about-us ; https://nysed.gov/facilities-planning/authorizing-school-construction | OFP = code enforcement authority for public schools, BOCES, charters chartered after 7/31/10; plans outside NYC reviewed → building permit. Capital projects need voter approval of object & purpose (Ed Law §1718), meetings 45-day notice; BOCES may authorize by board resolution (voter approval only for acquisitions) | Why para 2; Q&A vote, capital project, private school, BOCES |
| "General Municipal Law section 103 purchase contracts exceeding $20,000 public works contracts exceeding $35,000 cooperative purchasing BOCES 119-o" | Firecrawl gov search | https://p12.nysed.gov/mgtserv/purchasing/handbook.html ; https://ecode360.com/6404113 | School district bids: purchases >$20,000, public works >$35,000; ≥5 days between ad and opening; true leases, state/county contracts excepted from §103 (local §104-b policy) | Numbers; rules; Q&A bid; FAQ lease |
| "Nassau BOCES "cooperative bidding" OR "cooperative purchasing" program member districts" | Firecrawl search | https://www.nassauboces.org/services-for-districts/business-services/cooperative-bidding ; https://www.esboces.org/programs-services/admin-business/cooperative-bidding/cb | Nassau BOCES Cooperative Bidding & Purchasing: electronic bidding system for participating districts, other BOCES, municipalities; ESBOCES program initiated Aug 1981 | Numbers; District section; Q&A coop |
| "NYS Department of Labor prevailing wage Nassau Suffolk electrician teledata technician security camera installation public work school district" | Firecrawl gov search | https://apps.labor.ny.gov/wpp/viewOriginalWageSchedule.do?projectId=326149 ; https://dol.ny.gov/wage-theft-bureau-public-work-prevailing-wage-enforcement-laws-and-guidance | District 4 (Nassau, Suffolk) "Telephone and Integrated Tele-Data System Electrician" $42.93 (7/1/2026) / $44.43 (8/1/2026), "applies to ALL Voice, Data & Video work", excludes fire alarm & energy mgmt (regular electrician $66.75 7/1/2026); supplements extra; debarment for willful violations | Why para 4; Q&A prevailing wage x2; pricing note; AI check |
| "Education Law 2-d third-party contractor data privacy agreement student personally identifiable information video surveillance footage" | Firecrawl gov search | https://nysed.gov/sites/default/files/programs/data-privacy-security/2026-data-privacy-and-security-quick-reference.pdf ; https://nysed.gov/data-privacy-security/frequently-asked-questions-about-data-privacy-and-security ; https://studentprivacy.ed.gov/faq/faqs-photos-and-videos-under-ferpa | 2-d third-party contractor incl. data management/storage; DPA, supplemental info, Parents' Bill of Rights, DPO, breach reporting | Rules; Q&A 2-d; AI check cloud; FAQ lease |
| "Diocese of Rockville Centre Catholic schools number of elementary and high schools Nassau Suffolk" | Firecrawl search (excerpt) | https://www.drvc.org/about/ | 10,776 students in 35 Catholic elementary schools; 9,857 in nine high schools | Numbers list |
| "Non-Public School Safety Equipment NPSE grant NYSED…" | Firecrawl gov search | https://nysed.gov/nonpublic-schools/nonpublic-school-safety-equipment-npse-grant-0 | NPSE reimburses religious/independent schools, per-student allocation (Y10 $45M) | Q&A private school; AI check grants |
| "Securing Communities Against Hate Crimes grant 2026 nonpublic schools…" | Firecrawl search + scrape | https://www.governor.ny.gov/apply-securing-communities-against-hate-crimes-grant-program | DCJS grants to nonprofits at risk of hate crimes; interior/exterior security improvements | Q&A private school; AI check grants |

House practices on the page that are NOT sourced (flag for Anwar): two-hour arrival windows / 1–2 hr restore; drive-health alerts and drive replacement cycles; separate camera VLAN; delivering camera drawings to the building-level team; three-layer quote with named alternates; evening/weekend/break scheduling; checking every camera after dark; face-matching left off and unlicensed (consistent with §106-b); subcontracting to prime contractors; IT checklist; 100 m PoE copper limit (TIA standard, not cited).

### Question register — additions from school-security-camera-installation-long-island (rebuilt 2026-10-18; replaces the 35 old LI questions)

FAQ (visible + FAQPage):
- Can we see a camera-by-camera drawing before the board votes on the project?
- Will the new cameras work with the video management software our district already runs?
- Can a district standardise on one camera brand across all its buildings?
- Who should manage the camera switches, district IT or the camera contractor?
- Does a voter-approved camera project count against the district's property tax cap?
- Can the camera names match the door numbers in our emergency plans?
- Can a district lease a camera system instead of buying it?
- What should a district put in its video surveillance and use policy before cameras go live?
- What do you need from the district's IT department before installation day?

Q&A (H3):
- How much notice do bidders get when a Long Island district advertises a camera bid?
- What does a BOCES cooperative award actually cover on a camera job?
- Does a camera upgrade need a public vote, or can the board of education approve it alone?
- Does the Wicks Law apply when cameras ride inside a large Long Island bond project?
- Who sits on the Smart Schools Review Board, and why does its schedule matter?
- Why does Smart Schools money reach the district only after the installer has been paid?
- How should an installer’s quote be written so it survives months of state review?
- Does school camera installation for a public district on Long Island carry prevailing wage?
- Why can the same camera cost a public district more to install than a private school down the road?
- Can residents obtain a school’s camera locations through a Freedom of Information request?
- Does switching to cloud video change what a district must post under Education Law 2-d?
- Where should cameras sit in a newly built entrance vestibule?
- Which parts of a big Island campus should get cameras first when the money covers only one phase?
- How far from the building can a field camera be before copper cable stops working?
- Who reviews the footage when a Suffolk school bus camera records a car passing?
- Does a private or parish school on Long Island need the State Education Department’s approval for camera work?
- Do BOCES buildings follow the same camera rules as the districts they serve?

Near-overlaps to watch (checked against rebuilt Brooklyn, Manhattan and Orange County pages; LI questions on bid threshold, coop purchase, SED trigger, SS sequence, hard drives, architect/CM, stop-arm garage, ERP/camera access, 2-d installer and handover were reworded or replaced to avoid duplicating them): phasing priority (LI) vs "Can we spread the project over two school years?" (BK) — different intent (which first vs whether); LI capital-project threshold vs BK "Do we need a DOB permit" — different authority/intent. Parish-ownership, analog-reuse, walkthrough and network-intrusion questions were removed from LI to avoid duplicating BK.

### Images (11) — source files
Real AESS job photos (re-cropped, none of a school, captions say so): images/rockland-toyota-ceiling-bullet.jpeg, rockland-toyota-wall-camera.jpeg, rockland-toyota-dome-camera.jpeg, nassau-window-depot-office-camera.jpeg, manhattan-deli-interior-cameras.jpeg, manhattan-deli-exterior-camera.jpeg. Manufacturer product shots (Ubiquiti UniFi): ubiquiti-unifi-g5-dome-ultra-camera-white.jpg, ubiquiti-unifi-g6-entry-doorbell.jpg, ubiquiti-unifi-ai-ptz-precision-4k-camera-white.jpg, ubiquiti-unifi-ai-lpr-bullet-4k-camera-black.jpg, ubiquiti-unifi-g6-turret-4k-camera-white.jpg. Rejected: all images/school-*-long-island-ny.webp and legacy-school-cctv-*.webp (AI-generated "Lincoln High School" crews with phone numbers on shirts).

### Added 2026-10-18 (size/uniqueness pass)
| Query | Platform | URL | Finding | Used in |
|---|---|---|---|---|
| "Wicks Law separate prime contracts threshold Nassau Suffolk Westchester $3 million public work Labor Law General Municipal Law 101" | Firecrawl gov search | https://nysenate.gov/legislation/laws/gmu/101 | Separate prime specs for plumbing, HVAC, electrical above $1.5M in Nassau/Suffolk/Westchester ($3M NYC, $500K elsewhere); sealed subcontractor list below threshold | Q&A Wicks question |
| "school district property tax levy limit exclusion capital local expenditures voter approved bond debt service tax cap" | Firecrawl gov search | https://p12.nysed.gov/mgtserv/documents/PropTaxCap_SED_Final_1-13-20.pdf ; https://dos.ny.gov/november-18-2020vol-xlii-issue-46 | Capital local expenditures (incl. capital equipment, debt service, voter-approved where required; PPU under Local Finance Law; excludes maintenance/operations) are outside the school tax levy limit (Ed Law 2023-a) | FAQ tax cap |
| (from Newsday 2018 scrape, row 9a) | — | https://www.newsday.com/long-island/education/school-safety-security-w24072 | Smart Schools Review Board = SED, SUNY, Division of Budget reps; meets when critical mass of projects; full 23-district 2018 security approvals table | Q&A Review Board; numbers table |
