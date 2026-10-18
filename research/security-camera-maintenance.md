# Research — Security Camera Maintenance (silo)

Created from the Bronx rebuild (batch run 2026-10-18).

# Security Camera Maintenance — silo research (batch file, Bronx REBUILD)

Created 2026-10-18 by the REBUILD of `security-camera-maintenance-bronx` (area page, up-link `/security-camera-maintenance-nyc`, direct line (646) 490-0629, Bronx GBP 460 E Fordham Rd, Bronx NY 10458, `#bronx`). `research/security-camera-maintenance.md` did not exist; per the run brief everything is written here for the main run to merge.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page + section used**. Shell curl is blocked; tools used: WebSearch (result lists only), WebFetch (page read through a summariser — figures below are as it reported them), Firecrawl search (excerpts) and Firecrawl scrape. "carried" = sourced by an earlier run in another research file (file + row named), not re-fetched today. Nothing below is invented. Unreachable sources are written `EMPTY (not accessible in build env)`.

Silo: `security-camera-maintenance-*` — 16 pages (NYC hub + Manhattan/Brooklyn/Queens/Bronx/Staten Island; Long Island hub + Nassau/Suffolk; Hudson Valley hub + Westchester/Rockland/Orange/Putnam/Dutchess/Ulster). Before this rebuild all 16 were one template: identical 12 FAQ intents, identical prices, file sizes within ~2.5 KB of each other.

---

## 1. Source matrix (blueprint v2.3 §3)

| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl search). reddit.com full threads: WebFetch returned `SITE_BLOCKED`. Rows R1–R3. No r/bronx thread specifically about camera maintenance surfaced → Bronx-specific maintenance Reddit **EMPTY**. |
| 2 | Google People Also Ask | **EMPTY (not accessible in build env)** — no live Google SERP surface. Proxy: the questions maintenance guides themselves pose (rows M1–M6). |
| 3 | Google PASF | **EMPTY (not accessible in build env)**. |
| 4 | Answer the Public | **EMPTY (not accessible in build env)**. |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)**. The page's §10.5 says so and instead tests seven claims repeated in maintenance guides and cost guides (M1–M6, C1–C2). It quotes no AI Overview. |
| 6 | Area landmarks | Bronx section (sourced). |
| 7 | Area use cases / building stock | Bronx section (Furman, UNHP, LPC, Co-op City carried; heat index; el lines). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** — single search backend per tool; no Bing/DDG related-search surface. |
| 9 | Local news | News 12 Bronx (2024, 2025, 2026), CBS New York (2015), Inside Climate News (Jul 2026). |
| 10 | Hyperlocal | Bronx Times (May 2026 South Bronx Unite air study; Dec 2024 dispensaries; Mar 2023 licences; Oct 2026 Third Ave BID cameras carried). Norwood News / Riverdale Press / BronxNet maintenance items: **EMPTY**. |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — Firecrawl scrape of `https://www.yelp.com/search?find_desc=security+camera+repair&find_loc=Bronx%2C+NY` returned "we do not support this site". |

---

## 2. Silo-wide findings (maintenance)

### 2.1 Maintenance guides (PAA proxy; feed §10.5 Reality Check)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M1 | `security camera maintenance checklist how often clean lens hard drive replace` · Firecrawl search (excerpt) | https://newsroom.axis.com/blog/security-camera-maintenance | Axis: break tasks into weekly, monthly, quarterly; weekly: "Clean camera lenses and housing… A blurry image is often just a dirty lens." | §10.5 H3 1; Sources |
| M2 | same (excerpt) | https://reolink.com/blog/cctv-camera-maintenance/ | Reolink: "It is recommended once a year to check for faults and issues." | §10.5 H3 1; Sources |
| M3 | same (excerpt) | https://visiondetectionsystems.com/blog/security-camera-maintenance-checklist | "Commercial systems should be checked weekly (live feeds and obstructions), maintained monthly (lens cleaning, …" | §10.5 H3 1 |
| M4 | same (excerpt) | https://xtenav.com/blog/dvr-security-system-maintenance-checklist/ | "Most integrators recommend a full inspection every six months, with quick monthly checks…" | §10.5 H3 1 |
| M5 | same (excerpt) | https://www.backstreet-surveillance.com/blog/post/how-often-do-security-cameras-really-need-maintenance | Feb 20, 2026: monthly "health check" with a smartphone and 10 minutes; quarterly deeper checks. | §10.5 H3 1 (background) |
| M6 | same (excerpt) | https://shaktivaulttechnologies.com/professional-cctv-camera-maintenance/ | "Outdoor and commercial systems do best with checks every three months." | not used (duplicate of M3/M4) |

### 2.2 Reddit / forums (excerpts)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit security camera maintenance spider webs IR night vision cleaning how often` · WebSearch (result list) | https://ipcamtalk.com/threads/spider-webs-covering-outside-camera-lens.76743/ ; https://community.home-assistant.io/t/cameras-versus-spiders/943502 ; https://eufy.com/blogs/security-camera/how-to-keep-spider-webs-off-security-cameras | Spider webs over outdoor lenses are a recurring owner complaint on camera forums (thread titles; bodies not read). | §9 H3 spider webs ("a long-running topic on camera forums"); Sources |
| R2 | `site:reddit.com r/bronx camera footage building super cameras broken` · Firecrawl search (excerpt) | https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ | r/AskNYC comment: "if the super/landlord/management are scummy and they have access to the cameras, they can simply say the cameras arent working properly and…" (opinion) | §5 para 2 (paraphrased as "residents on r/AskNYC describe…"); Sources |
| R3 | same (excerpt) | https://www.reddit.com/r/bronx/comments/1p1tow6/help_i_think_this_man_is_trying_to_hurt_me/ | r/bronx reply advises sending video plus video of a "broken front door lock" to the landlord (resident safety thread). | not used (not about maintenance) |

### 2.3 Cost guides / competitor claims
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C1 | `security camera maintenance cost Angi OR HomeAdvisor OR Fixr per year` · WebSearch (result list only) | https://cost-guide-ssr.homeadvisor.com/cost/safety-and-security/repair-an-alarm-or-security-system/ ; https://ipvm.com/forums/video-surveillance/topics/how-much-do-you-charge-for-a-service-maintenace-package | HomeAdvisor publishes a security-system *repair* cost guide (no maintenance-plan figure seen); IPVM forum thread on how integrators price service packages (body not read). No Angi/Fixr maintenance figure retrieved → **EMPTY** for a quotable national maintenance price. | §10.5 H3 4 (says national guides price repair, not upkeep); Sources |

### 2.4 Equipment / technical
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `APC UPS battery lifespan 3 to 5 years replace temperature effect` · WebSearch → WebFetch | https://www.se.com/us/en/faqs/FA158934/ | APC (Schneider): "Most APC batteries should last three to five years"; "every 8°C (15°F) increase in temperature will cut the battery's life in half" (4 yrs at 25°C → ~2 yrs at 33°C); ideal 20–25°C; internal battery runs warmer than the room. | §9 H3 battery; §10 UPS card; §5.5 bullet; Sources |
| T2 | `Backblaze hard drive failure rate by age 2025 annualized failure rate` · WebSearch → WebFetch | https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2025/ | Q2 2025 annualized failure rate 1.36%; lifetime AFR 1.30% across 393,907 drives (27 models). | §9 H3 24-hour drives; §10.5 H3 3; Sources |
| T3 | carried from research/nvr-installation.md T1 | https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-purple-hdd/data-sheet-wd-purple-hdd.pdf | WD Purple: workload rating up to 180 TB/year, ~3× desktop drives, for 24/7 surveillance. | §9 H3 24-hour drives; §10 drives card |
| T4 | `CISA Hikvision command injection vulnerability CVE-2021-36260 known exploited firmware update` · WebSearch → WebFetch | https://www.bleepingcomputer.com/news/security/over-80-000-exploitable-hikvision-cameras-exposed-online/ | Aug 22, 2022: CVE-2021-36260 command injection, patched by Hikvision firmware Sept 2021; ~80,000 vulnerable devices in a sample of 285,000 internet-facing Hikvision servers; CISA listed it among actively exploited bugs in Jan 2022. | §9 H3 firmware; §10.5 H3 6; Sources |
| T5 | carried from research/nvr-installation.md G1–G4 | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment ; https://www.hikvision.com/us-en/newsroom/latest-news/2026/Important-Notice-to-Our-Partners | FCC order effective July 16, 2026 bars importation/marketing of certain covered equipment; owners may keep using what they have; Hikvision USA: import limits "could affect access to replacement parts, warranty service, and technical support". | §9 H3 firmware; §10.5 H3 6; Sources |

### 2.5 Rules — retention, testing, footage (NY / NYC)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `New York cannabis dispensary video surveillance retention 60 days 9 NYCRR 125` · WebSearch → WebFetch | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 | 9 NYCRR §125.3: recordings retained ≥60 days (longer if under investigation); continuous recording during hours of operation, motion at other times; system must stay operational in a power outage for ≥8 hours; failure notification to licensee's representative within 5 minutes; power-loss failure expected >8 h reported to OCM within 24 h; security equipment "in full operating order"; testing/inspection at intervals not exceeding 30 calendar days; test records kept 5 years. | §8.5 bullet 1; §9 H3 cannabis; §17 FAQ log; Sources |
| G2 | `New York City law businesses required to keep surveillance camera footage days retention DCWP` · WebSearch → WebFetch | https://legislation.nysenate.gov/pdf/bills/2025/A9470B | A.9470-B (introduced Jan 6, 2026; amended, in Assembly Codes; **not passed**): businesses would have to release footage of an on-premises felony on formal written request and take "reasonable measures" so it is not recorded over; fines up to $100,000 per incident; no set retention days. | §8.5 bullet 4 (as a pending bill); §9 H3 deli retention |
| G3 | `New York smoke shop tobacco retailer surveillance camera requirement law 2025` · WebSearch → WebFetch | https://legislation.nysenate.gov/pdf/bills/2025/s1659 | S.1659 "Imette's Law" (introduced Jan 13, 2025; in committee; **not passed**): cabarets' entrances/exits on camera, ≥15 fps, no audio, continuous during hours + 2 h, 30-day retention. | §8.5 bullet 4 (pending); §9 H3 deli retention |
| G4 | same search → WebFetch | https://www.nysenate.gov/legislation/bills/2025/A4126 | A.4126 smoke-shop licensing bill: no camera requirement, in Ways and Means. | not used (no camera content) |
| G5 | `New York check cashers regulation video surveillance camera requirement 3 NYCRR retain recordings` · WebSearch → WebFetch | https://www.dfs.ny.gov/industry_guidance/industry_letters/il20000911_letter_atm_video_tape_usage | DFS industry letter (Banking Law §75-n): ATM video tape retained at least 30 days before reuse (banking institutions' ATM facilities). Check-casher camera rule: **not found** (EMPTY). | §8.5 bullet 5 (bank ATMs only, not stores); Sources |
| G6 | carried research/nvr-installation.md P1 | https://www.hornwright.com/bronx/civil-rights/false-imprisonment/how-to-preserve-body-cam-dash-cam-and-store-surv/ | Bronx law-firm guide: "Store cameras: many overwrite in 7 to 10 days." | §9 H3 detective nine days; Sources |
| G7 | carried research/nvr-installation.md T4 | https://nychajournal.nyc/nycha-completes-over-24-million-in-safety-and-security-upgrades-at-23-campuses/ | NYCHA new CCTV: same video management systems as NYPD; "21-day footage retention". | §7 NYCHA card; Sources |
| G8 | carried research/nvr-installation.md G6 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-131285 | NYC Admin Code §22-1202 biometric sign at customer entrances. | §8.5 bullet 3 |
| G9 | carried research/nvr-installation.md G8 | https://www.nysenate.gov/legislation/laws/PEN/250.00 | NY Penal Law 250: recording a conversation without one party's consent = mechanical overhearing. | §8.5 bullet 3 |
| G10 | carried research/nvr-installation.md G9 | https://dos.ny.gov/get-security-or-fire-alarm-installer-license | NYS DOS security/fire alarm installer licence covers CCTV. | §8.5 bullet 2 |
| G11 | carried research/nvr-installation.md P3 | https://www.bxtimes.com/exclusive-look-at-das-new-surveilence-camera-program/ | Bronx DA CAMS (2018–19): intranet map of BID members' camera locations; nearly 1,000 cameras enrolled. | §8 card Hub; §9 H3 detective |
| G12 | `NYC Housing Maintenance Code landlord security cameras multiple dwelling closed circuit television requirement HPD` · WebSearch (result list) | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/abcs-of-housing-owners.pdf ; https://tenant-rights.com/new-york/new-york-laws-on-security-cameras-in-building-common-areas | No HPD / Housing Maintenance Code provision requiring private landlords to install or maintain CCTV was found in the results read (bodies not opened). Brick Underground (carried, nvr T7): buildings not required to have working cameras. → **EMPTY** for a city camera-upkeep duty; page does not claim one. | §7 intro (states no city rule found); FLAG |

### 2.6 Keywords (five layers, silo)
- **Service:** security camera maintenance, CCTV maintenance, camera system maintenance plan, preventive maintenance, camera tune-up, camera cleaning, recorder health check, NVR/DVR maintenance, surveillance system service contract.
- **Problem:** blurry/foggy picture, spider webs at night, IR glare, camera offline, wrong time stamp, footage overwritten, drive failure, "No HDD", UPS battery dead, camera knocked or painted over, firmware vulnerability, lost admin password.
- **Technology:** dome/turret/bullet/PTZ, IR illuminators, lens and dome bubble, PoE switch, UPS (VRLA battery), surveillance drives (WD Purple), firmware, NTP time sync, retention, health alerts.
- **Industry:** apartment buildings (walk-up, elevator, co-op), managing agents/supers, bodegas/delis, corridor retail, auto shops, wholesale food/warehouses (Hunts Point), cannabis dispensaries, offices/clinics.
- **Geographic (Bronx):** see `## Bronx`.

### 2.7 Silo pricing base (no invented prices) — FLAG
Published identically on all 16 pre-rebuild pages including `security-camera-maintenance-brooklyn.html` (Brooklyn = §9 base 1.00×) and the hub: one-time service visit **$150–$350**; residential plan **$200–$500/yr** ("often … $50–$150 per camera per year"); commercial plan **$1,000–$5,000+/yr**; emergency/same-day **$190–$900**. Service/callback **$195/hr, 3-hr min ($585)** — blueprint v2.3 §9 (protected).
FLAGS: (1) Manhattan (1.25×) and every Long Island/Hudson Valley page show the same unmultiplied numbers — §9 not applied anywhere in the old silo. (2) Same-day low end $190 sits below the $585 three-hour minimum of the $195/hr service rate; the page publishes both with their own scopes (same-day diagnostic/fix quoted per job vs. callbacks after an AESS installation) — Anwar to confirm. (3) Old pages state "industry standard … 8–15% of system value annually" with no source — not used. (4) Silo ranges were never re-derived.

---

## Bronx

Build 2026-10-18. Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, `#bronx`) · up-link `/security-camera-maintenance-nyc`. §9 Bronx = 1.00× → silo base unchanged.

**Thesis:** Bronx cameras rarely fail on install day — they wear out. Grime from the borough's truck and highway corridors (Major Deegan/Cross Bronx/Bruckner, Hunts Point's diesel fleet) and from the elevated 4, 2/5 and 6 lines; heat in the city's most heat-vulnerable neighborhoods plus Con Ed voltage reductions and outages; cellar water; and people who deliberately damage cameras. Meanwhile footage is held to clocks — cannabis 60 days with 30-day tests, NYCHA 21 days, store recorders that overwrite in 7–10 days, pending state bills — so Bronx maintenance is a written schedule set by what each camera faces and what each owner must be able to prove.

### Environment (BX-E)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-E1 | `Cross Bronx Expressway air pollution particulate matter study residents asthma` · WebSearch → WebFetch | https://www.bxtimes.com/pollution-from-congestion-tolls-city-to-study-asthma-rates/ | Bronx Times, May 6, 2026: South Bronx Unite + Columbia Mailman, 19 monitors, Jan 2024–Dec 2025; 13 of 19 recorded PM2.5 increases after congestion pricing; average +0.22 µg/m³; largest +1.29 µg/m³ outside SBU's Mott Haven office between the Third Avenue Bridge and the Major Deegan; Major Deegan described as heavily trafficked truck corridor. | §5 para 2; §5.5 bullet; §9 H3 film; §13 card; Sources |
| BX-E2 | same search → WebFetch | https://insideclimatenews.org/news/09072026/nyc-bronx-air-quality-remains-a-problem/ | Inside Climate News, Jul 9, 2026: Hunts Point FDC distributes ~4.5 billion lb of food a year, mostly by diesel truck (NYC EDC); NYPA runs four gas-fired peaker plants in Mott Haven/Port Morris; ~90% of city freight by truck; 19% of Bronx children diagnosed with asthma vs 12% citywide. | §5.5 bullet; §8 Hunts Point card; §9 H3 film |
| BX-E3 | `NYC heat vulnerability index Bronx neighborhoods highest score` · WebSearch → WebFetch | https://bronx.news12.com/2024/07/10/new-york-city-data-shows-bronx-neighborhoods-are-more-at-risk-in-extreme-heat/52u6AcuAcHBSGdTpbPJKns | News 12, Jul 10, 2024: HVI 5 (highest) = Mott Haven, Melrose, Morrisania, Hunts Point; Throgs Neck, Pelham Bay, City Island = 2; Riverdale = 1; 14.4% of Bronx residents lack AC (Morrisania 24.2%). | §5.5 bullet; §7 cards; §9 H3 battery |
| BX-E4 | `Bronx Con Edison outage 2026 heat wave voltage reduction` · WebSearch → WebFetch | https://bronx.news12.com/bronx-outage-tracker-more-than-400-customers-still-without-power | News 12, Jul 4, 2026: ~40 Bronx customers still out (Riverdale, Wakefield, Morris Heights); Con Ed reduced voltage "to help protect the electric system during the heat wave". | §9 H3 after-outage; Sources |
| BX-E5 | carried research/nvr-installation.md BX16 | https://bronx.news12.com/2026/07/03/5000-con-edison-customers-in-the-bronx-without-power-amid-heat-wave/ONmoL7BVphOWvTtg2dafc | Jul 3, 2026: ~5,000 Bronx customers out; 8% voltage reduction incl. Riverdale, Marble Hill, Kingsbridge. | §5.5 bullet; §9 H3 after-outage |
| BX-E6 | `Bronx basement flooding storm 2025 OR 2026 flash flood Bronx News12` · WebSearch → WebFetch | https://bronx.news12.com/2025/07/15/heavy-downpours-in-bronx-and-brooklyn-prompt-flash-flood-warning/5xHIVRtvjsgNBLMxFdbms1 | News 12, Jul 14, 2025: flash-flood warning for the Bronx and Brooklyn; flooding video inside the Longwood Avenue subway station. | §9 H3 water stain; Sources |

### Elevated lines and corridors (BX-L)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-L1 | `Bronx elevated subway Jerome Avenue vibration dust residents complaints` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/IRT_Jerome_Avenue_Line | 4 train elevated over River Avenue (from just south of E 157th St) and Jerome Avenue (from ~E 169th St) to Woodlawn; first section opened June 2, 1917. | §5 para 2; §8 Jerome card; §13 card |
| BX-L2 | `IRT White Plains Road Line elevated Bronx; IRT Pelham Line elevated Westchester Avenue` · WebSearch → WebFetch | https://nycsubway.org/wiki/IRT_White_Plains_Road_Line | White Plains Road Line elevated over Westchester Ave, Southern Blvd, Boston Rd (Contract I viaduct, opened Nov 26, 1904) and White Plains Road (extension opened Mar 3, 1917). Services 2/5 not stated on that page (2 and 5 attribution from common knowledge of the line — page names the line, not services). | §5 para 2; §13 card |
| BX-L3 | same → WebFetch | https://en.wikipedia.org/wiki/IRT_Pelham_Line | 6 train elevated over Whitlock Ave then Westchester Ave; opened 1918–1920. | §5 para 2; §8 Westchester Ave card; §13 card |
| BX-L4 | same Jerome search (result) | https://bronx.news12.com/2026/06/26/mount-eden-residents-demand-action-over-late-night-noise-from-jerome-avenue-auto-shops/2AKIi6ATVfOFyQAQcoXUEf | News 12, Jun 26, 2026 headline: Mount Eden residents demand action over late-night noise from Jerome Avenue auto shops (body not read). | §8 Jerome card (headline only) |
| BX-L5 | carried research/nvr-installation.md BX7–BX9, BX12 | nyc.gov SBS BID pages; https://www.bxtimes.com/third-avenue-bid-adds-security-measures/ ; https://www.nycfoodpolicy.org/hunts-point-distribution-center-brief-overview-spotlight-produce-market/ | Fordham Road BID 35 block faces / 333 ground-floor retailers; Third Avenue BID added 18 cameras at 10 locations (Oct 2026); Hunts Point FDC ~329 acres, 155+ wholesalers. | §8 cards; §13 cards |
| BX-L6 | `Hunts Point Produce Market hours overnight operations 24 hours wholesalers` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Hunts_Point_Cooperative_Market | Hunts Point Cooperative Market: ~60 acres, 50+ wholesale food businesses, seven refrigerated/freezer buildings (~700,000 sq ft refrigerated), operates 24/7. | §8 Hunts Point card; §9 H3 24-hour drives |
| BX-L7 | `Bronx licensed cannabis dispensaries number OCM 2026` · WebSearch → WebFetch | https://www.bxtimes.com/bronx-cannabis-industry-sees-growth-in-2024-but-battles-hurdles/ | Bronx Times, Dec 23, 2024: nine licensed dispensaries opened in the Bronx in 2024 (to Dec 20) plus two in 2023; named: Hush (Williamsbridge Rd, Allerton), Two Buds (E 241st St), Freshly Baked (Arthur Ave). | §8 dispensary card; §9 H3 cannabis (businesses named only as context — not as clients) |
| BX-L8 | same → WebFetch | https://www.bxtimes.com/state-doubles-cannabis-licenses/ | Mar 15, 2023: Bronx CAURD allocation raised 10 → 20; six Bronx licensees at the time. | not used (superseded by BX-L7) |

### Building stock, tampering, tenants (BX-B)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-B1 | carried research/nvr-installation.md BX1, BX2, BX4, BX5 | furmancenter.org Bronx; unhp.org; LPC 2403.pdf; coopcity.com | 19.7% homeownership (2024); median multifamily building age 87 yrs (CB6 98); Grand Concourse HD 78 properties; Co-op City 15,372 units in 35 high-rises + 7 townhouse clusters; 63,066 units in 4+ unit buildings built 2010–2025. | §5.5; §7 cards; §13 card |
| BX-B2 | `reddit r/bronx security camera building landlord cameras not working` · WebSearch → WebFetch | https://cbsnews.com/newyork/news/police-suspects-busted-surveillance-cameras-in-multiple-bronx-buildings | CBS NY, Apr 2, 2015: men entered several West Bronx apartment buildings on Davidson Avenue (Morris Heights; numbers 1985–2024) and "damaged numerous surveillance cameras inside and outside the buildings". | §5 para 3; §9 H3 knocked cameras; Sources |
| BX-B3 | same → WebFetch | https://bronx.news12.com/2024/05/15/mott-haven-tenants-forced-to-remove-door-cameras-say-theyre-already-feeling-less-safe/3tafOiumigGWzyWZxfSRoC | News 12, May 15, 2024: Mott Haven building management gave residents a deadline to remove door-mounted cameras; Bronx Legal Services Tenant Rights Association rep: review the lease for an explicit ban. | §7 walk-up card (the building's own cameras carry more weight); Sources |
| BX-B4 | same → WebFetch | https://bronx.news12.com/recent-robberies-in-bx-building-have-tenants-on-edge-34821037 | Jan 2009, 1235 Grand Concourse co-op: tenants want better security after robberies (no camera detail in excerpt). | not used (old, no camera detail) |

### Prices used (§9 Bronx = 1.00× → silo base §2.7 unchanged)
One-time service visit $150–$350; building/home plan $200–$500/yr (~$50–$150 per camera per year); commercial plan $1,000–$5,000+/yr; same-day repair visit $190–$900; post-installation callbacks $195/hr, 3-hr minimum ($585). Worked examples on page use only these figures. Service schema AggregateOffer low 150 / high 5000.

### Keywords (Bronx geo layer)
security camera maintenance Bronx; CCTV maintenance Bronx NY; camera maintenance plan Bronx; bodega camera service Bronx; apartment building camera maintenance Bronx; Jerome Avenue, Westchester Avenue, White Plains Road, River Avenue, Major Deegan, Cross Bronx, Bruckner, Hunts Point, Fordham Road, The Hub / Third Avenue, Arthur Avenue, Mott Haven, Melrose, Morrisania, Morris Heights, Riverdale, Co-op City, Parkchester. All 11 image alts carry "security camera maintenance" + "Bronx".

### Images (11) — permanent image rule
Drive "AESS Website Photos": no maintenance folder (per brief); CompanyCam not connected. All 11 copied with Pillow (WebP q80, ≤1600 px, PNG/RGBA flattened on white), each viewed before use; no faces, house numbers, plates or readable documents. Captions say "Example photo from another AESS job (not a Bronx property)" or "Manufacturer product photo". Excluded per brief: images/parking/*, crew photos in images/network/, network-cable-repair, cat6, low-voltage, cat6-repair/aess-*, fiber-optic-installation/aess-*, root template images. Scenes chosen to differ from nvr-installation-bronx (one shared scene — storefront dome under painted fascia — used as a much tighter crop; recorder screen used as a different crop).
| images/security-camera-maintenance/ | Source | Section |
|---|---|---|
| …-bronx-dome-camera-under-water-stained-ceiling-tiles.webp (hero) | images/dvr-upgrade/dvr-upgrade-ulster-white-dome-camera-under-water-stained-ceiling.webp | Hero |
| …-bronx-dome-camera-under-painted-fascia-winter-sky.webp (crop 150,0,560,300) | images/dvr-upgrade/dvr-upgrade-brooklyn-white-turret-under-storefront-fascia.webp | §5 |
| …-bronx-mini-dome-cameras-across-shop-drop-ceiling.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-mini-domes-in-shop-drop-ceiling.webp | §6 |
| …-bronx-cameras-high-on-wall-below-mezzanine.webp | images/dvr-upgrade/dvr-upgrade-queens-two-small-cameras-high-on-white-wall-below-mezzanine.webp | §7 |
| …-bronx-ceiling-camera-near-exit-sign-and-air-vent.webp | images/dvr-upgrade/dvr-upgrade-nassau-county-small-ceiling-camera-near-exit-sign-and-vent.webp | §8 |
| …-bronx-bullet-camera-beside-return-air-grille.webp | images/dvr-upgrade/dvr-upgrade-ulster-black-bullet-camera-on-ceiling-grid-above-corridor.webp | §9 |
| …-bronx-wall-camera-above-motion-sensor.webp | images/dvr-upgrade/dvr-upgrade-nassau-county-camera-high-on-wall-above-motion-sensor.webp | §9 |
| …-bronx-turret-camera-twin-illuminators-product-photo.webp | images/dvr-upgrade/dvr-upgrade-nassau-county-white-turret-camera-with-two-illuminators-product-photo.webp (manufacturer) | §10 |
| …-bronx-stainless-steel-ptz-dome-product-photo.webp | images/dvr-upgrade/dvr-upgrade-staten-island-stainless-steel-pan-tilt-zoom-dome-product-photo.webp (manufacturer; Dahua logo visible) | §10 |
| …-bronx-recorder-screen-with-empty-channel-tiles.webp (crop 380,0,807,585) | images/dvr-upgrade/dvr-upgrade-nassau-county-recorder-screen-channel-grid-and-bitrate-table.webp | §14 |
| …-bronx-rack-recorder-vented-front-product-photo.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-large-rack-recorder-with-vented-front-product-photo.webp (manufacturer) | §15 |
DAILY-LOG note: `images: 11 reused from images/dvr-upgrade/ (8 real AESS job photos from other jobs, 2 re-cropped + 3 manufacturer product shots) (no real security-camera-maintenance photos yet)`.

### FLAGS for Anwar (Bronx page)
1. Prices: see §2.7 (silo never applied §9; $190 same-day floor vs $585 3-hr minimum; 8–15% claim dropped).
2. Unsourced AESS house practices stated as practice on the page: lens/dome cleaning method (no solvents on coated domes), IR-glare and web checks at night, mount torque/thread-locker on cameras near the el, tamper alerts/video-loss alerts, time-sync check after outages, UPS self-test and battery date labels, 90-day cadence near highways/el vs 6-month elsewhere, written visit log, drive health reading (SMART) and replacement before failure, "most faults fixed in 1–2 hours of arrival" (blueprint element 36 wording), cellar recorder off the floor, firmware only from manufacturer sources, password recovery via manufacturer reset process, cameras under el structures switching to infrared earlier/later because of shade, Jerome Avenue body-shop overspray on cameras, drive hand-back/wipe policy, lift arranged for high facade cameras, early-morning starts, 30-day retention target most store owners choose.
8. Check results (2026-10-18): `tools/check_page.py` → only 14 failures, all "live sibling … doesn't link back to /security-camera-maintenance-bronx" (main-run wiring; builder not allowed to edit siblings). Similarity (masked, difflib word-sequence): vs every silo page page ≤0.029, paragraph max 0.50 (footer line); vs nvr-installation-bronx page 0.10, paragraphs ≥0.65 only boilerplate (freshness byline, NAP, warranty sentence, footer, form fields).
9. Parallel-builder note: the session scratchpad is shared with the school-page builders (generic file names were overwritten mid-run); the page itself was not affected (verified).
3. No source found that el trains or highway traffic specifically deposit grime on cameras or loosen mounts — the page presents the el/highway exposure as the reason AESS schedules more frequent checks there (practice), and cites the air-quality studies only for what they measured.
4. No city/HPD rule requiring private landlords to keep cameras working was found (G12) — page says so.
5. Field Notes is a method note in Anwar's voice, not a specific job story — confirm or replace.
6. "Free estimates / same-day estimates" relies on site-wide copy; COI at no charge carried from the BYOE calculator ($0).
7. White Plains Road Line source does not name the 2/5 services; page says "the White Plains Road line" and only names the 4 (Jerome) and 6 (Pelham) explicitly as sourced.

---

## Question register — security-camera-maintenance silo

### Old template (asked on all 15 other pages; read 2026-10-18) — each with its area name in Q1
1. How much does security camera maintenance cost in [area]?
2. How often should I have my security cameras serviced?
3. What's included in a maintenance visit?
4. Why do I need maintenance if my cameras look like they're working?
5. Do you offer a maintenance plan or contract?
6. Can you service a system another company installed?
7. My footage looks blurry now — do I need new cameras?
8. Will a maintenance plan keep my warranty valid?
9. How does maintenance save me money?
10. Can I do any of the maintenance myself?
11. Do you provide emergency or same-day camera service?
12. Do you maintain commercial systems and buildings, not just homes?
(Pages: security-camera-maintenance-nyc, -manhattan, -brooklyn, -queens, -staten-island, -long-island, -nassau-county, -suffolk-county, -hudson-valley, -westchester-county, -rockland-county, -orange-county, -putnam-county, -dutchess-county, -ulster-county. The old -bronx page carried the same 12 and is replaced.)

### security-camera-maintenance-bronx (REBUILT 2026-10-18) — §9 Q&A (H3)
1. Our cameras look straight at the 4 train over Jerome Avenue — why does that view go soft long before the ones on the side street?
2. The store sits a few blocks from the Major Deegan — what is the grey film on the dome, and what takes it off without ruining the plastic?
3. Spider webs keep setting off motion alerts on the courtyard camera every night — is there a fix that lasts longer than a week?
4. After the July 2026 heat-wave outages, two cameras came back with the wrong date — what should be checked once Con Edison restores power?
5. Our battery backup is four years old and lives in a warm cellar — is it still protecting anything?
6. There is a brown water ring on the ceiling tile right above a camera — how worried should we be?
7. We hold a cannabis retail licence in the Bronx — what does the state expect us to test, and how often?
8. A detective asked for video from nine days earlier and the recorder had already written over it — how do we stop that happening again?
9. Is a Bronx deli or bodega legally required to keep its footage for a set number of days?
10. Someone keeps pushing the lobby camera to face the ceiling — how do you make a camera harder to knock off its view?
11. How would we find out the same morning that a camera was sprayed or covered overnight?
12. Our recorder is an older Hikvision — do firmware updates still matter, and can we still get them after the 2026 FCC order?
13. The last managing agent left without handing over the recorder password — can access be recovered without erasing the footage?
14. In a co-op, who should receive the maintenance report — the board, the managing agent or the super?
15. Our Hunts Point cold-storage unit records around the clock — does nonstop recording wear the drives out faster?

### security-camera-maintenance-bronx — §17 FAQ (accordion = FAQPage)
1. How early in the morning can your technician start in a building where tenants leave for work before seven?
2. Do you need someone with keys to the roof, the cellar and the recorder cabinet on a maintenance day?
3. Will the cameras stop recording while you are working on them?
4. Can a visit to a store on Fordham Road or Southern Boulevard be done before the shutters go up?
5. What happens to the hard drives you take out — does the old footage leave the building?
6. Do you bring a lift or tall ladder for cameras two or three storeys up a facade?
7. Can you give us a dated log of each check that we can show a regulator or an insurer?
8. Will you send a certificate of insurance to our managing agent before the first visit?
9. How is payment handled for maintenance in the Bronx?
