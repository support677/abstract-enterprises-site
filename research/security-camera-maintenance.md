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

---
<!-- merged from batch file security-camera-maintenance-brooklyn.md (batch run 2026-10-18) -->
# Security Camera Maintenance — Brooklyn (REBUILD, batch file)

Build 2026-10-18 by the parallel builder for `security-camera-maintenance-brooklyn` (area page, up-link `/security-camera-maintenance-nyc`, direct line (347) 934-8335, Brooklyn GBP 1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`, map link https://goo.gl/maps/3yH8sb9fXFQZgUB29 copied from nvr-installation-brooklyn.html). REBUILD: the old page was "Crawled – currently not indexed" (near-duplicate template). Nothing of the old template text was reused; only the `security-camera-maintenance-rebuilt-pages` back-link section before `<footer>` was copied unchanged.

Silo research is reused from `research/security-camera-maintenance.md` (§2 silo findings M1–M5, R1–R2, C1, T1–T5, G1–G12; §2.7 pricing base). This file adds only the Brooklyn local research and this page's question register, for the main run to merge into `research/security-camera-maintenance.md` as `## Brooklyn`.

Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: WebSearch (result lists), WebFetch (page read through a summariser — figures as it reported them), Firecrawl search (excerpts). Shell curl blocked. Nothing invented.

---

## Brooklyn

**Thesis:** In Brooklyn a camera system is worn down by water, salt and stone — recorders in cellars served by combined sewers that back up in cloudbursts (Ida 2021, September 29, 2023, July 2026 Gowanus/Coney Island flooding), brackets and connectors corroding in harbour and ocean air along the Sandy surge line (Red Hook, Sheepshead Bay/Emmons Ave, Coney Island, Sunset Park), and cameras on porous brownstone veneer and landmarked facades that cannot simply be re-drilled (LPC Ch. 11 rules; Brooklyn Heights = NYC's first historic district) — so a Brooklyn maintenance plan is built per camera around where the water goes, how close the salt is and what the wall is made of.

### Source matrix status (blueprint v2.3 §3) — Brooklyn
| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl search). r/Brooklyn camera-maintenance thread: **EMPTY**. Two excerpts used/considered (BK-R1, BK-R2). |
| 2 | Google PAA | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — §10.5 says so and tests seven common guide claims instead. |
| 6 | Landmarks | Gowanus Canal, Red Hook waterfront, Emmons Ave/Sheepshead Bay, Brooklyn Heights HD, Brooklyn Navy Yard, Industry City (all sourced below). |
| 7 | Building stock | Brownstone veneer (Brick Underground), landmarked rowhouses (LPC/HDC), FISP >6 storeys (DOB); Furman BK10 homeownership 41.0% (2024) read but not used. |
| 8 | Bing / DDG | **EMPTY (not accessible in build env)** |
| 9 | Local news | Brooklyn Eagle (2017, 2023, 2025), News 12 Brooklyn (Jul 2026), CBS New York (2019), Commercial Observer (Jan 2026), City Limits (2013). |
| 10 | Hyperlocal | BK Reader (Jul 2026). Brooklyn Paper / Bay News camera-maintenance items: **EMPTY** (only Sandy/Ida result titles seen, not read). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** (silo note: Yelp scrape unsupported). |

### Water (BK-W)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BK-W1 | `September 29 2023 Brooklyn flooding record rainfall basements Williamsburg Park Slope` · WebSearch → WebFetch | https://brooklyneagle.com/articles/2023/09/29/brooklyn-hit-hard-in-historic-new-york-city-rainfall/ | NWS: 4–6 in. in Brooklyn by ~noon, southern Brooklyn near 7 in. by mid-afternoon; FloodNet flooding reports South Williamsburg, Gowanus, Red Hook, Crown Heights, East New York; people trapped in a basement on Madison St (Thompson–Throop), Bed-Stuy, rescued ~9:30 a.m.; Boerum Hill garden apt a foot of water; Joe Coffee DUMBO basement flooded; Grand Army Plaza station steps; P.S. 312 Bergen Beach evacuated. | Hero sub; §5 para 2; §5.5 bullet; §9 H3 (garden-floor fog); §10.5 Claim 3; Sources |
| BK-W2 | `Gowanus flooding basements Hurricane Ida Brooklyn 2021 sewer backup` · WebSearch → WebFetch | https://www.bkreader.com/non-profit-community/as-brooklyn-floods-gowanus-residents-prepare-for-the-worst-12406348 | BK Reader, Jul 8, 2026: June 9, 2026 DEP flood town hall in Gowanus (~100 attendees); combined sewer overloads (DEP Dep. Commissioner Beth DeFalco); resident had two feet of water in basement in Ida, "Everything was gone"; basement residents got free kits (~$300 each); two overflow tanks on the canal, completion 2029; Coney Island submerged in several inches during a recent Monday flood. | §5 para 2; §5.5 bullet (kits, tanks 2029); §13 Gowanus card; Sources |
| BK-W3 | same search → WebFetch | https://www.nyc.gov/assets/brooklyncb9/downloads/pdf/2025/BKCB9_DEP-Flooding-101.pdf | DEP Flooding 101 (CB9, 2025): groundwater, tidal backup through sewer connections, combined-sewer backup (combined sewers serve 60% of NYC); network built for 1.5–1.75 in./hr; keep belongings on shelves above where water could enter; flood sensors near floor drain; 35 miles porous pavement planned in Brooklyn (not used). | §5 para 2; §5.5 bullet; §9 H3 (flooded recorder still running — DEP flood-sensor advice; sewage/silt in combined-sewer backups); §10.5 Claim 3; Sources |
| BK-W4 | `NYC FloodNet sensors Brooklyn Gowanus Red Hook street flooding sensor network` · WebSearch → WebFetch | https://engineering.nyu.edu/news/nyu-building-ultrasonic-flood-sensor-network-new-yorks-gowanus-neighborhood | NYU Tandon, Sep 28, 2022: FloodNet low-cost street-level flood sensors, Gowanus. | §13 Gowanus card ("FloodNet sensors began here" — FLAG: page says "began here"; article headline is about building the network in Gowanus) ; Sources |

### Salt and Sandy (BK-S)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BK-S1 | `Hurricane Sandy Red Hook Coney Island storm surge feet flooded businesses Brooklyn 2012` · WebSearch → WebFetch | https://brooklyneagle.com/articles/2017/10/27/anniversary-of-sandy-devastation-recalls-red-hook-rebound/ | Surge "more than 14 feet" pushed seawater into Red Hook ~9:30 p.m. at high tide/full moon; mandatory evacuation of nearly all of Red Hook. | §5 para 3; §5.5 bullet; §9 H3 (Red Hook screws); §13 Red Hook card; Sources |
| BK-S2 | `Sheepshead Bay Emmons Avenue Coney Island Sandy flooding businesses basements Brooklyn Paper` · WebSearch → WebFetch | https://citylimits.org/40-percent-of-sheepshead-firms-still-shut-post-sandy/ | City Limits, Mar 19, 2013: "On Emmons Avenue, roughly 85 percent of businesses suffered some form of damage"; Masal Café needed electrical overhaul, no power three weeks; estimate 40% of ~100 affected businesses might not reopen (projection, not used). | §5 para 3; §5.5 bullet; §8 Emmons card; §13 card; Sources |
| BK-S3 | `salt air corrosion outdoor electronics coastal security cameras stainless hardware Sandy Red Hook Coney Island surge` · WebSearch → WebFetch | https://www.acti.com/fr/technologies/anti-corrosion-design | ACTi (camera maker, vendor statements): salt/sea spray "aggressive to metals, accelerating oxidation, pitting, and galvanic corrosion"; failure points incl. connectors, cable glands, junction boxes, seals; suggests 316L stainless, coated fasteners. No salt-mist test standard named. | §5 para 3; §9 H3 (screws, connectors); §10 coastal replacement; §10.5 Claim 2; Sources |
| BK-S4 | same search (results only) | gazpearce.codeberg.page posts | Unattributed blog posts on CCTV salt corrosion — **not used** (unknown authorship). | — |

### Stone, landmarks, facades (BK-L)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BK-L1 | `Landmarks Preservation Commission security cameras rules historic district facade permit` · WebSearch → WebFetch | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | LPC Permit Guidebook Ch. 11: staff-level approval when criteria met; small buildings ≤2 cameras per 25 ft frontage, large ≤3; avoid primary facade unless no option; small, finished to blend; attach at mortar joints, plain masonry, wood, metalwork or concrete paving — not through cast iron or decorative surfaces; ≈10 in. visible conduit max, painted; comparative drawings not required for in-kind replacement of security cameras; no permit for "ordinary maintenance, repair, and retrofitting of health, safety, and utility equipment". | §5 para 4; §7 cards + list; §8.5 bullet; §9 H3 (landmark swap, loose bracket, cast-iron storefront, pigeon roost); §10 coastal replacement; §10.5 Claim 6; Sources |
| BK-L2 | `Brooklyn Heights first historic district 1965 Park Slope historic district number of buildings LPC Brooklyn` · WebSearch → WebFetch | https://hdc.org/borough/brooklyn-heights/ | Brooklyn Heights HD designated Nov 23, 1965 — "The first designated New York City Historic District". (Park Slope/Fort Greene/Clinton Hill HDs not sourced → not named as districts on page.) | §5 para 4; §5.5 bullet; §7 card; §13 card; Sources |
| BK-L3 | `brownstone sandstone facade delamination spalling why brownstone erodes Brooklyn rowhouse restoration` · WebSearch → WebFetch | https://www.brickunderground.com/live/facts-about-brownstones | Brownstone = sandstone; "a veneer which is attached to the front brick wall with raw metal ties"; absorptive stone delaminates when contoured; Park Slope facade restoration $700,000 (not used). | §5 para 4; §9 H3 (loose bracket); §10.5 Claim 6; Sources |
| BK-L4 | `site:reddit.com r/Brooklyn security camera building cameras not working landlord brownstone` · Firecrawl search (excerpt) | https://www.reddit.com/r/Brooklyn/comments/dd6dfz/fake_brownstones_2/ | r/Brooklyn excerpt: "That building has brick behind the brownstone… most of what you see is patching material." | Background only (consistent with BK-L3); not quoted |
| BK-L5 | `NYC DOB Facade Inspection Safety Program buildings greater than six stories every five years Local Law 11 sidewalk shed` · WebSearch → WebFetch | https://www.nyc.gov/site/buildings/safety/facade-local-law.page | Buildings "higher than six stories" inspected every five years by a QEWI; Unsafe → owner "must immediately install protection, such as a sidewalk shed". | §5.5 bullet; Sources (shed Q dropped — NYC hub covers it) |

### Power, theft, campuses (BK-P / BK-C)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BK-P1 | `Brooklyn Con Edison power outage 2026 heat wave customers Brooklyn neighborhoods` · WebSearch → WebFetch | https://brooklyn.news12.com/2026/07/04/over-1200-con-edison-customers-in-brooklyn-without-power-ahead-of-hot-holiday-weekend/6vsYOxZkj3uCDVnCJiFu2i | News 12, Jul 3, 2026: >1,200 Brooklyn customers out; 400+ in Bushwick (Willoughby Ave near Evergreen Ave), weather-related manhole fire; Con Ed "reduced voltage in parts of the city"; many with low voltage. | §5.5 bullet; §10.5 Claim 5; Sources |
| BK-P2 | `Brooklyn package theft stoop brownstone cameras 2025 OR 2026 news` · WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/park-slope-package-thieves-caught-on-camera-nypd-brooklyn | CBS NY, Aug 20, 2019: three suspects cut open packages in a Park Slope building lobby on camera; ~$500 clothing. | §9 H3 (stoop camera faces); Sources |
| BK-C1 | `Brooklyn Navy Yard 550 businesses 11,000 jobs 300 acres` · WebSearch → WebFetch | https://commercialobserver.com/2026/01/brooklyn-navy-yard-ceo-lindsay-greene/ | CO, Jan 26, 2026: "300-acre waterfront site", "50-building industrial park"; intro "over 500 businesses"/CEO "550 businesses"; jobs "more than 11,000"/"13,000"; average business "fewer than 20 employees". Page uses "hundreds of businesses" to avoid the discrepancy. | §5.5 bullet; §8 card; §9 H3 (shared internet line in campus studios); §13 card; Sources |
| BK-C2 | `Industry City Sunset Park 35 acres 6 million square feet tenants` · WebSearch → WebFetch | https://brooklyneagle.com/articles/2025/04/08/industry-city-surpasses-650-businesses/ | Apr 8, 2025: "35-acre, 6 million-square-foot mixed-use complex comprising 16 buildings"; "surpassed 650 businesses" (worker count given as 9,000 and 8,500 — not used). | §5.5 bullet; §8 card; §9 H3 (shared internet line in campus studios); §13 card; Sources |
| BK-C3 | `Furman Center Brooklyn housing stock share of units in 1-4 family buildings homeownership rate` · WebSearch → WebFetch | https://furmancenter.org/neighborhoods/view/bay-ridge-dyker-heights | BK10 homeownership 41.0% (2024); serious crime 5.2/1,000 (2025). | Not used (no building-type share; NYPD-style crime data kept off non-solar pages per Appendix B) |
| BK-R2 | same Reddit search (excerpt) | https://www.reddit.com/r/AskNYC/comments/1md93cr/are_backyard_security_cameras_legally_allowed_in/ | r/AskNYC excerpt on backyard cameras: "convince the landlord to install an outside camera at close to ground level that avoids these issues". | Background for FAQ "camera that sees into a neighbour's yard" (not quoted) |

### Silo sources reused on this page (carried, not re-fetched)
APC battery life (T1) §9 H3 hot under-stair closet + §10.5 Claim 5; Axis (M1) §10.5 Claim 1 background; HomeAdvisor/IPVM (C1) §10.5 Claim 4; 9 NYCRR §125.3 (G1), A.9470-B (G2), S.1659 (G3), NYC Admin Code §22-1202 (G8), Penal Law 250 (G9), DOS licence (G10) §8.5 list; G12 (no city camera-upkeep duty found) §7 closing para.

### Prices used (§9 Brooklyn = 1.00× → silo base unchanged)
One-time tune-up $150–$350; home/small-building plan $200–$500/yr; commercial plan $1,000–$5,000+/yr; same-day repair visit $190–$900; post-AESS-installation service $195/hr, 3-hr minimum ($585). Service schema AggregateOffer 150–5000. Worked examples (4-camera Park Slope brownstone; 24-camera waterfront restaurant) use only these ranges.

### Keywords (Brooklyn geo layer)
security camera maintenance Brooklyn; CCTV maintenance Brooklyn NY; camera maintenance plan Brooklyn; brownstone camera maintenance; waterfront/coastal camera corrosion Brooklyn; recorder flood Brooklyn basement; Gowanus, Red Hook, Sheepshead Bay, Emmons Avenue, Coney Island, Brighton Beach, Sunset Park, Industry City, Brooklyn Navy Yard, Brooklyn Heights, Park Slope, Bed-Stuy, Boerum Hill, Bushwick, Williamsburg, Greenpoint, DUMBO, Crown Heights, East New York, Gerritsen Beach, Marine Park, Mill Basin, Manhattan Beach; Fulton Street, Flatbush Avenue, Kings Highway, 86th Street, Atlantic Avenue. All 11 image alts carry "security camera maintenance" + "Brooklyn".

### Images (11) — permanent image rule
No Drive folder for this silo; CompanyCam not connected. Every image viewed before use (Read). Converted with Pillow (WebP q80, ≤1600 px; PNG flattened on white). No faces, house numbers, plates or readable documents (storeroom tile shows only a "CAM 3" overlay). Scenes chosen to avoid the 11 Bronx scenes (no stained-ceiling dome, painted-fascia/mural dome, mezzanine wall, exit-sign camera, return-grille bullet, motion-sensor short-arm camera, empty-channel recorder screen). Folders per brief: hikvision-security-camera-installation, lorex-camera-installation, products.
| images/security-camera-maintenance/ | Source | Section |
|---|---|---|
| security-camera-maintenance-brooklyn-wall-arm-dome-below-stone-cornice.webp (hero) | images/hikvision-security-camera-installation/…-westchester-county-wall-arm-camera-below-stone-cornice.webp (AESS job photo) | Hero |
| …-brooklyn-loose-network-cables-across-ceiling-beam.webp | images/lorex-camera-installation/…-long-island-loose-blue-and-white-network-cables-crossing-ceiling-beam.webp (AESS job) | §5 |
| …-brooklyn-mini-dome-beside-ceiling-speaker.webp | images/hikvision-security-camera-installation/…-westchester-county-mini-dome-and-round-speaker-in-store-ceiling.webp (AESS job) | §6 |
| …-brooklyn-wall-bullet-and-ceiling-dome-two-heights.webp | images/hikvision-security-camera-installation/…-westchester-county-high-wall-bullet-and-ceiling-dome-at-two-heights.webp (AESS job) | §7 |
| …-brooklyn-turret-camera-facing-glass-storefront.webp | images/lorex-camera-installation/…-brooklyn-ceiling-dome-camera-facing-glass-entrance-doors.webp (AESS job) | §8 |
| …-brooklyn-bullet-camera-above-hallway-door.webp | images/lorex-camera-installation/…-brooklyn-black-bullet-camera-at-ceiling-over-grey-door.webp (AESS job) | §9 |
| …-brooklyn-playback-view-along-brick-wall-to-lot.webp | images/lorex-camera-installation/…-hudson-valley-recorder-playback-view-along-brick-wall-to-paved-lot.webp (AESS job, recorder frame) | §9 |
| …-brooklyn-video-doorbell-product-photo.webp | images/lorex-camera-installation/…-brooklyn-black-lorex-video-doorbell-with-green-ring-product-photo.webp (manufacturer) | §10 |
| …-brooklyn-varifocal-bullet-with-junction-box-product-photo.webp | images/hikvision-security-camera-installation/…-long-island-white-varifocal-bullet-with-junction-box-product-photo.webp (manufacturer) | §10 |
| …-brooklyn-four-dome-camera-recorder-kit-product-photo.webp | images/products/a1.png (product photo) | §14 |
| …-brooklyn-night-recorder-view-of-cluttered-back-room.webp | images/hikvision-security-camera-installation/…-ulster-county-recorder-tile-of-dim-back-storeroom.webp (AESS job, recorder frame) | §15 |
DAILY-LOG note: `images: 11 = 8 real AESS job photos from other jobs (hikvision/lorex folders) + 3 manufacturer/product shots (lorex doorbell, hikvision bullet, products/a1 kit) (no real security-camera-maintenance photos yet)`.

### FLAGS for Anwar (Brooklyn page)
1. Prices: silo base ×1.00 (Brooklyn). Inherited silo flags stand: $190 same-day floor sits below the $585 three-hour minimum of the $195/hr rate (page keeps separate scopes); silo ranges never re-derived; "8–15% of system value" not used.
2. Unsourced AESS house practices stated as practice (not fact): rinse-before-wipe on coastal domes; stainless fixings swap; dielectric/separator on dissimilar metals; drip loops, gasket/desiccant replacement; re-anchoring into mortar joints and leaving holes for a mason; per-camera risk labels (salt/flood/stone/glare) and 6-month vs every-visit cadence; late-spring pre-storm visit; before-and-after frames on every visit; recorder height logged each visit; same-day "within an hour or two of arriving" (element 36 wording); line-interactive UPS advice; phone-camera IR check; export-format test; free pre-storm phone advice; separate recorder user accounts; channel renaming; vent cleaning; parts carried on the van (gaskets, desiccant, stainless fixings, connectors, generic brackets); COI to agents on request; drop cloths/padded ladder feet. Added after replacements: flooded-recorder triage (export first, open case, flood sensor by drain), louvred closet doors / recorder shelf for heat, pigeon hood or moving camera off a roost, cast-iron fixings sealed and cameras moved to plain surfaces, lighter secondary stream / network segment for shared internet, MP4 export and test export, cooler-door condensation repositioning.
3. Hours in LocalBusiness schema copied from the Brooklyn-GBP NVR Staten Island page ("Mo-Su 08:00-20:00"); the Bronx maintenance page uses Mon–Sat 08–19 — confirm Brooklyn GBP hours.
4. "AESS holds NYS license #12000287431" under the DOS security/fire alarm installer licensing bullet: the licence number is the site's NYS Low-Voltage licence; confirm it is the DOS installer licence the bullet refers to.
5. Navy Yard business/job counts conflict inside the source (500+/550; 11,000+/13,000) — page says "hundreds of businesses", no job count.
6. Field Notes is a method note in Anwar's voice, not a specific dated job story — confirm or replace.
7. §13 Gowanus card: "NYU's FloodNet street-flood sensors began here" — source headline is NYU "building" the network in Gowanus (2022); soften to "were installed early here" if Anwar prefers.
8. Same-day / free-estimate copy relies on site-wide claims.
9. Checker (2026-10-18, final): only failures = 10 "live sibling … doesn't link back to /security-camera-maintenance-brooklyn" (hudson-valley, long-island, manhattan, nassau-county, orange-county, putnam-county, rockland-county, suffolk-county, ulster-county, westchester-county — main-run wiring). 13,371 rendered words; 184,736 B (Bronx 180,560; Dutchess 174,766; NYC 188,169 at final check — re-check if those change).
10. Similarity (masked with check_page.mask(), difflib word sequence, text blocks ≥12 words, nav excluded): page-level 0.080 vs Bronx, 0.072 vs Dutchess, 0.067 vs NYC hub, ≤0.02 vs every other silo page and the old Brooklyn template, 0.018 vs nvr-installation-brooklyn; max paragraph 0.609 (Bronx) / 0.574 (Dutchess) — the pricing paragraph carrying the mandatory warranty sentence — and 0.560 (NYC, NAP line).
11. Parallel overlap: the NYC hub builder wrote five questions very close to five of this page's first drafts (Ida recorder, sidewalk shed, voltage sag, tenant-vs-landlord cameras, super logins); this page replaced all five. Main run: please confirm the final NYC register does not pick up any question listed below.

---

## Question register — security-camera-maintenance-brooklyn (REBUILT 2026-10-18)

Checked by meaning against the silo register (old template 12; Bronx 15 Q&A + 9 FAQ), the rebuilt Dutchess page and research/_batch/security-camera-maintenance-dutchess-county.md, and the rebuilt NYC hub page (read live 2026-10-18; its batch research file did not exist yet). Drafts dropped for overlap: seasonal close/reopen and vegetation-in-view (Dutchess); before-and-after photos and remote-owner video call (too close to Dutchess photo/remote items); booking outside trading hours and recording downtime during work (Bronx FAQ); recorder after Ida, sidewalk shed blocking view, heat-wave voltage sag, tenant-vs-landlord cameras, super/tenant recorder logins (all on the rebuilt NYC hub — written in parallel).

### §9 Q&A (H3)
1. Water reached the recorder during the last storm but it still switches on — can we keep using it?
2. Since the September 2023 downpour our garden-floor camera shows a milky blur every night — is there water inside it?
3. Our camera cable comes into the building through a cellar window well that fills in heavy rain — can water travel along the wire?
4. We are two blocks from the water in Red Hook — why are the screws on our camera brackets turning orange?
5. The connectors in the box under our Emmons Avenue awning have gone green and crusty — is that why the picture keeps dropping out?
6. Does a camera facing the beach at Coney Island need a different cleaning routine from one in Bushwick?
7. Our brownstone is in a historic district — do we need Landmarks approval to swap a dead facade camera for a new one?
8. The camera bracket on our brownstone facade is loose — can it be re-anchored without drilling into the stone?
9. Our stoop camera records the person who takes the packages but never a usable face — is that a maintenance fix or a new camera?
10. A previous installer bolted the camera on our shop's cast-iron storefront straight into the iron — should it stay there?
11. Our recorder lives in a closet under the stairs that gets very hot in summer, and it has started beeping — is the heat the reason?
12. Our Wi-Fi cameras on the back of a row house keep dropping off — is it the brick?
13. Pigeons roost on the cornice right above our facade camera and the dome is constantly fouled — what actually helps?
14. The camera covering our long back garden used to see the fence at night and now sees only the first few feet — has its night vision failed?
15. The camera in our restaurant's cellar storeroom sits beside the walk-in cooler and fogs up every time the door opens — what can be done?
16. When we hand video to the police or an insurer, the files come out in a format nobody else can play — can that be fixed on a visit?
17. A building next door is being gutted — will the dust and vibration hurt our cameras, and what should we watch for?
18. Our studio's cameras share one internet line with the business Wi-Fi — could a busy network be why remote playback stutters?
19. Our loading-door camera looks out over the water and washes out completely late every afternoon — can that be fixed?

### §17 FAQ (accordion = FAQPage, 9)
1. Do I need to hold a parking spot for your van on a brownstone block?
2. Will you leave dust or ladder marks on our stoop, hall floors or parlor-floor trim?
3. Do you need our Wi-Fi password or internet account login for a maintenance visit?
4. Do you also clean the network closet and recorder cabinet, or only the cameras?
5. Can you rename the cameras on our recorder so they say where they are, like stoop or garden gate?
6. Can a visit be timed around a renovation or a tenant move-in that is already booked?
7. If you notice a camera that can see into a neighbour's window or yard, will you tell us?
8. How far ahead should we book a pre-storm check before the hurricane season?
9. Do you carry replacement domes, gaskets and brackets on the van, or do they have to be ordered?

---
<!-- merged from batch file security-camera-maintenance-dutchess-county.md (batch run 2026-10-18) -->
# Security Camera Maintenance — Dutchess County (batch file, REBUILD)

Built 2026-10-18 by the REBUILD of `security-camera-maintenance-dutchess-county` (area page, up-link `/security-camera-maintenance-hudson-valley`, direct line (845) 640-3835, Bronx GBP 460 E Fordham Rd, Bronx NY 10458, `#bronx`; (800) 486-0943 only in the shared header chrome). For the main run to merge into `research/security-camera-maintenance.md` as `## Dutchess County` + register entries. Silo research (M1–M6, R1–R3, C1, T1–T5, G1–G12) reused, not re-fetched.

Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page + section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes). Shell curl blocked. "carried" = sourced by an earlier run in another research file (file + row named), not re-fetched today. Nothing invented.

**Thesis:** In Dutchess the cameras are far from their owners and from us (estates, farms, weekend houses, multi-building campuses) and the threats are weather events — Central Hudson/NYSEG storm outages, ice, lightning — not daily grime. So Dutchess maintenance is remote-first (health/offline alerts, remote reviews, oldest-recording checks) with hands-on visits timed to the seasons (pre-winter, post-storm) and to the links between buildings (surge, bridges, generator hand-off). Context hook: the county's removal of its 64/65 Flock plate-reader cameras (Sept 2026) makes private footage more likely to be what answers a local question.

## Dutchess County

### Source matrix (§3)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | FC search `site:reddit.com Poughkeepsie OR Dutchess security camera power outage internet down cameras offline` → r/hudsonvalley outage threads (excerpts only: https://www.reddit.com/r/hudsonvalley/comments/1uo7l4l/power_outages_to_last_through_tuesday_for_most/ "approximately 50,000 customers were without service"; https://www.reddit.com/r/hudsonvalley/comments/1uo0t98/if_central_hudson_doesnt_want_to_be_part_of_a/ comment "Extended power outages were common (1 every 1-2 years)" — opinion). No Dutchess thread about camera maintenance → **EMPTY** for camera-specific Reddit. Not quoted on page. |
| 2 | Google PAA | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — §10.5 says so on page and tests seven claims common in general advice/product/cost content instead. |
| 6 | Landmarks | DC-L1–L4 + carried |
| 7 | Use cases / building stock | carried (DC-C rows) |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** |
| 9 | Local news | Poughkeepsie Journal (Mar 17 2026; Aug 6 2020; Oct 1 2019 carried), Times Union (Sep 25 2026), Spectrum News (Jul 5–7 2026), News 12 HV (Jun 22 2026), Daily Freeman (Sep 25 2026 excerpt). |
| 10 | Hyperlocal | Mid-Hudson News (Jul 22 2026; Sep 26 2026 excerpt). Hudson Valley One: tag page excerpt only ("A camera and two license plate readers will be installed in the village") — village not identified → not used. HV Observer Red Hook "Rec Park … security cameras" headline only → not used. |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** |

### Power, storms, weather (DC-P)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| DC-P1 | `Central Hudson Dutchess County outage customers storm 2025 OR 2026 Poughkeepsie Journal` · FC search (excerpt incl. embedded Central Hudson post) | https://spectrumlocalnews.com/nys/hudson-valley/news/2026/07/05/thunderstorm-leaves-thousands-without-power-in-dutchess-county | Jul 5–7 2026: Central Hudson ~50,000 customers out at height; "Central and southern Dutchess County: 32,000+ customers"; worst impacts City/Town of Poughkeepsie, East Fishkill, LaGrange, Beekman, Union Vale, village/town of Pawling; NYSEG 1,241 Dutchess outages Tuesday; James Baird State Park and golf course closed after storm left area without power. | §5 para 2; §5.5 bullet 1; §9 generator Q; §10.5 Claim 2; §13 James Baird card; Sources |
| DC-P2 | `Dutchess County ice storm OR winter storm power outages NYSEG Central Hudson Millbrook Amenia Pawling` · FC search → FC scrape | https://www.dutchessny.gov/Departments/County-Executive/47497.htm | Published 7/6/2026: storm Saturday July 4; "most significant impacts were in the City and Town of Poughkeepsie, East Fishkill, Hyde Park, LaGrange, Beekman, Union Vale and Village and Town of Pawling"; Central Hudson "more than 19,000 customers in Dutchess County, still without power"; NYSEG "over 3,400". | §5 para 2; §5.5 bullet 1; §9 generator Q; §9 oaks Q; Sources |
| DC-P3 | same first search → FC scrape | https://www.poughkeepsiejournal.com/story/news/local/2026/03/17/thousands-without-power-across-mid-hudson-valley-on-st-patricks-day/89191636007/ | Nickie Hayes, Mar 17 2026: windstorm "interrupted electric service to approximately 14,748 customers"; "Dutchess and Ulster counties were most heavily impacted"; NWS gusts up to 55 mph; 7,181 still out of 315,428. | §5 para 2; Sources |
| DC-P4 | second search → FC scrape | https://www.poughkeepsiejournal.com/story/news/local/2020/08/06/storm-isaias-impact-continues-dutchess-thousands-without-power/3306815001/ | Aug 6 2020 (Santistevan, Wilson, Cordero): 10,499 of Central Hudson's 120,677 Dutchess customers out; 9,357 of NYSEG's 15,860 Dutchess customers out; Amenia 2,317 of 2,321; Dover 3,126 of 3,971; Pawling 1,906 of 2,984. | §5 para 2; §5.5 bullet 2; changelog; Sources |
| DC-P5 | second search (excerpt only) | https://www.facebook.com/DutchessCoGov/posts/clean-up-and-power-restoration-efforts-continue-across-dutchess-county-following/1490426973114718/ | "Central Hudson … 58,653 outages and NYSEG … 13,585 outages across Dutchess County" — date not shown in excerpt → **not used**. | not used |
| DC-P6 | `Poughkeepsie average annual snowfall coldest temperature NWS climate normals Dutchess County Airport` · FC search → FC scrape | https://nri.dutchessenvironment.com/climate-climate-change/ | Dutchess NRI: annual snowfall avg 47.1 in over 30 yrs, more in NE higher elevations; below zero 5–10 times a winter; 70 large-hail events 1971–2022 (~1–2/yr); "three major ice storms since 2008"; Poughkeepsie record low −21°F (Feb 1897), high 107°F (Jul 1966); frost-free ~162 days. | §5.5 bullet 3–4; §9 ice Q; §10.5 Claim 1; Sources |
| DC-P7 | carried research/cat6-repair.md line 259 (fiber HV run) | Earth Networks 2020 NY lightning report | Dutchess 166,641 lightning pulses (Orange 275,059 #1). | §5.5 bullet 4; §9 lightning Q; §10.5 Claim 4; Sources (named, no URL in carried row) |
| DC-P8 | carried research/cat6-repair.md D13 | https://www.poughkeepsiejournal.com/story/news/local/2019/10/01/internet-phone-outages-dutchess-county/3830205002/ | Oct 1 2019: cut fiber in Poughkeepsie area → Verizon internet/phone outages in Dutchess incl. Hyde Park, Wappingers Falls. | §9 "offline" Q; Sources |
| DC-P9 | carried research/cat6-repair.md R7 (smart-lock D1) | census.gov QuickFacts Dutchess | Households with broadband subscription 93.5%. | §5.5 bullet 6; §9 data-cap Q |
| DC-P10 | `Dutchess County broadband unserved addresses rural internet expansion 2025` · FC search; `ConnectALL BEAD Dutchess County locations awarded …` · FC search | broadband.ny.gov; ulstercountyny.gov (Ulster only) | No Dutchess-specific unserved-location count found → **EMPTY**; page uses only the 93.5% figure. | — |
| DC-P11 | `IP camera datasheet operating conditions -30 °C to 60 °C humidity 95% IP67 turret` · FC search | https://www.cortexcctv.com/spec-pdf/security-cameras/ip-ss/IP4TRFE.pdf ; https://www.homaxi.com/products/8mp-full-colour-night-vision-cctv-camera | Datasheets list operating temps −35~+60°C (Cortex) and −40°C~60°C (Homaxi). | §9 ice Q ("datasheets we have checked list … down to −35 °C or −40 °C"); Sources |

### County cameras, local news (DC-N)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| DC-N1 | `Dutchess County security cameras footage police Poughkeepsie OR Beacon OR Hyde Park 2026 camera` · FC search → FC scrape | https://www.timesunion.com/hudsonvalley/news/article/dutchess-county-decommission-flock-22448942.php | Sarah Trafton, Sep 25 2026: county to shut down and remove "all 65 of its county-operated Flock cameras" after packed forum at Pleasant Valley Town Hall; DA Anthony Parisi requested decommission; Sheriff Kirk Imperati; ARTCIC; 2026 budget $94,500; towns of New Lebanon and Milan banned Flock on town property; Newburgh terminating. | §5 para 3; §8.5 plate-reader bullet; §9 plate-reader Q; Sources |
| DC-N2 | `Mid-Hudson News Dutchess burglary surveillance camera …` · FC search (excerpts) | https://midhudsonnews.com/2026/07/22/dutchess-license-plate-cameras-called-invaluable-tools-video/ ; https://midhudsonnews.com/2026/09/26/sheriff-and-da-public-safety-efforts-handcuffed-following-forum-2/ | "There are 64 cameras throughout Dutchess County that are designed to capture license plate numbers" (Jul 22 2026); "64 Flock or Flock-style cameras … ARTCIC" (Sep 26). Count conflicts with Times Union 65 → page gives both, attributed. | §9 plate-reader Q; Sources |
| DC-N3 | same search (excerpt) | https://www.dailyfreeman.com/2026/09/25/dutchess-officials-in-reversal-drop-support-for-flock-cameras/ | Contract being cancelled; "no government contracts with Flock cameras located in Ulster County". | not used (covered by DC-N1) |
| DC-N4 | same search → FC scrape | https://hudsonvalley.news12.com/2026/06/22/man-seen-on-video-stealing-cash-from-tip-jar-at-dutchess-county-shop/2TWLwjfgQO2ca48yhkPxHK | Jun 22 2026: man on surveillance video taking cash from a tip jar at a Poughkeepsie business; shared by Alimentari Rossi and Sons on social media. | §5 para 3 (business not named on page); Sources |
| DC-N5 | earlier search (excerpt) | https://www.dutchessny.gov/Departments/Traffic-Safety/school-bus-safety.htm | Buses in 11 of 13 Dutchess districts have stop-arm cameras. | not used |

### Landmarks (DC-L)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| DC-L1 | `Walkway Over the Hudson length feet opened 2009 Poughkeepsie Highland visitors` · FC search | https://parks.ny.gov/visit/state-parks/walkway-over-hudson-state-historic-park ; https://walkway.org/visit/ | Opened October 2009 (Oct 3 per Wikipedia excerpt); deck 212 ft above river; 6,768 ft (1.28 miles); connects Poughkeepsie and Highland. | §13 card 1; Sources |
| DC-L2 | DC-P1 | Spectrum (above) | James Baird State Park + golf course closed after July 4 2026 storm. | §13 card 6 |
| DC-L3 | carried research/cat6-repair.md R2, R3, D11 | Wikipedia Vassar; marist.edu; Wikipedia Bard | Vassar ~1,000 acres; Marist 180 acres on US 9; Bard 70+ buildings, ~1,260 acres. | §13 cards 2–3 |
| DC-L4 | carried research/cat6-repair.md D8, D12 | dutchessfair.com; loftsatbeacon.com; roundhousebeacon.com | Six-day Dutchess County Fair, exhibit buildings, barns; Groveville mill 700+ employees 1880s; Roundhouse part of Matteawan Manufacturing Co., Main/East Main. | §13 cards 4–5 |

### Building stock / commercial (DC-C, all carried)
| ID | Source row | Finding | Page + section used |
|---|---|---|---|
| DC-C1 | cat6-repair.md R4 (stacker.com) | Median year built 1971; 18.0% built 1939 or earlier | §7 intro |
| DC-C2 | cat6-repair.md line 268 (USDA 2022 Census of Agriculture) | 620 farms, avg 161 acres | §5.5 bullet 5; Sources |
| DC-C3 | cat6-repair.md D2/D4 (ipark84.com; Poughkeepsie Journal Jul 14 2021) | iPark 84 ~300 acres, 2M+ sq ft; Amazon 124 acres of former plant | §7 office-park card; §8 Route 52 card; Sources |
| DC-C4 | cat6-repair.md D1 (onsemi Feb 10 2023) | EFK fab "largest onsemi manufacturing facility in the U.S." | §8 Route 52 card; Sources |
| DC-C5 | cat6-repair.md D6 (WAMC/Walsh) | Vassar Brothers 752,000 sq ft patient pavilion | §8 South Road card |
| DC-C6 | cat6-repair.md R1 (thinkdutchess IDA) | IBM South Road site | §8 South Road card (named only) |
| DC-C7 | cat6-repair.md D9 (Galleria site) | "largest … enclosed shopping center in Dutchess County … 110 … stores" | §8 Route 9 card |
| DC-C8 | cat6-repair.md R9 (diaart.org) | Dia:Beacon in 1929 Nabisco box-printing factory | §8 Beacon card |
| DC-C9 | cat6-repair.md D7 (ciachef.edu) | CIA 170-acre Hyde Park campus | §8 Route 9 North card |
| DC-C10 | cat6-repair.md D14 (Town of Poughkeepsie permit page excerpt; dutchessny.gov DBCH) | Town lists "Electric and Low Voltage Permit"; county: "Contact the local municipality"; no county contractor licence found (EMPTY) | §8.5 licensing/permit bullets; §9 permit Q |

### Prices used (§9 Dutchess 1.53 × silo base in research/security-camera-maintenance.md §2.7; round half-up)
One-time tune-up $150–$350 → **$230–$536**; plan $200–$500/yr → **$306–$765/yr** (per-camera $50–$150 → **$77–$230**); commercial $1,000–$5,000+/yr → **$1,530–$7,650+/yr**; same-day $190–$900 → **$291–$1,377**; callbacks **$195/hr, 3-hr minimum ($585)** unchanged (protected). Service schema AggregateOffer low 230 / high 7650.

### Images (11) — permanent image rule
Drive: no maintenance folder (per brief); CompanyCam not connected. Sources taken from images/dahua-camera-installation/, images/floodlight-camera-installation/, images/apartment-building-security-camera-installation/ (this builder's assigned folders). Every image viewed; scenes the Bronx page already uses (water-stained-ceiling corner dome, fascia dome in winter, mini domes across drop ceiling, mezzanine wall cameras, exit-sign/vent camera, bullet by return grille, short-arm camera over motion sensor, stainless PTZ, recorder bitrate screen, rack recorder) and their near-duplicates were skipped. No faces, house numbers, plates or readable documents. Pillow WebP q80, ≤1600 px.
| images/security-camera-maintenance/security-camera-maintenance-dutchess-county-… | Source | Section |
|---|---|---|
| turret-camera-on-ceiling-above-glass-entrance.webp (hero) | dahua-camera-installation/…-suffolk-county-turret-camera-above-glass-storefront.webp | Hero |
| dome-camera-on-long-steel-arm-on-masonry-facade.webp | dahua-camera-installation/…-long-island-dome-camera-on-long-wall-arm-on-stone-facade.webp | §5 |
| black-mini-dome-at-ceiling-corner-beside-light-panel.webp | dahua-camera-installation/…-suffolk-county-black-mini-dome-on-ceiling-grid.webp | §6 |
| turret-camera-in-ceiling-corner-beside-flag.webp | dahua-camera-installation/…-suffolk-county-turret-camera-in-ceiling-corner-beside-flag.webp | §7 |
| bullet-camera-at-corridor-ceiling-aimed-at-door.webp | dahua-camera-installation/…-long-island-bullet-camera-aimed-down-corridor-to-door.webp | §8 |
| recorder-monitor-lot-view-with-date-stamp-and-storeroom.webp | apartment-building-security-camera-installation/…-staten-island-recorder-monitor-lot-and-storeroom-views.webp | §9 |
| white-dome-camera-on-beige-ceiling-tile-near-vent.webp | floodlight-camera-installation/…-orange-county-white-dome-camera-on-ceiling-tile-near-light-panel.webp | §9 |
| network-cable-bundles-along-ceiling-pipe.webp | floodlight-camera-installation/…-staten-island-bundled-blue-and-white-network-cables-along-ceiling-pipe.webp | §9 |
| white-twin-panel-floodlight-camera-product-photo.webp | floodlight-camera-installation/…-brooklyn-white-twin-panel-floodlight-camera-product-photo.webp (manufacturer; Lorex logo) | §10 |
| black-varifocal-dome-camera-product-photo.webp | apartment-building-security-camera-installation/…-long-island-black-varifocal-dome-camera-product-photo.webp (manufacturer; Hikvision logo) | §10 |
| 16-channel-network-video-recorder-product-photo.webp | apartment-building-security-camera-installation/…-queens-16-channel-nvr-recorder-product-photo.webp (manufacturer; Hikvision logo) | §14 |
DAILY-LOG note: `images: 11 reused from images/dahua-camera-installation/, images/floodlight-camera-installation/, images/apartment-building-security-camera-installation/ (8 real AESS job photos from other jobs + 3 manufacturer product shots) (no real security-camera-maintenance photos yet)`.

### Keywords (Dutchess geo layer)
security camera maintenance Dutchess County; CCTV maintenance Poughkeepsie; camera maintenance plan Dutchess; post-storm camera check; pre-winter camera service; generator UPS camera hand-off; barn/outbuilding camera maintenance; wireless bridge camera; Route 9, Route 52, I-84, Route 22, Route 44, South Road; Poughkeepsie, Beacon, Fishkill, East Fishkill, Wappingers Falls, Hyde Park, Rhinebeck, Red Hook, Tivoli, Millbrook, LaGrange, Pleasant Valley, Beekman, Union Vale, Pawling, Dover, Amenia, Pine Plains, Millerton. All 11 alts carry "Security camera maintenance Dutchess County".

### FLAGS for Anwar (Dutchess page)
1. Prices: §9 1.53 applied to the whole silo base (incl. same-day and plan ranges). The HV hub and the old Dutchess page still show unmultiplied base prices; same-day floor $291 still sits below the $585 3-hr minimum (separate scopes, as on the Bronx page).
2. Plate-reader count conflict: Times Union says 65 county-operated Flock cameras; Mid-Hudson News 64 — page cites both.
3. Unsourced AESS house practices stated as practice: remote review via manufacturer link/temporary account and log; "roughly half of a visit's checks are inside the recorder"; pre-winter + post-storm visit timing; generator hand-off test; surge-device testing/replacement; labelling modem/router/recorder; cellular power monitor suggestion; sub-stream/cloud-upload settings and data measurement; bridge re-aim; rodent inspection; seasonal open/close checklist; camera inventory with replace-by year; grouping visits by area; "most faults fixed within 1–2 hours of arrival" (blueprint element 36 wording); caretaker access; snow/ice rescheduling; remote-access shut-off; livestock-aware barn work; photo privacy; on-site spares; no Connecticut work (outside NYS licence — confirm); Columbia County fit-in; power/heat on for visit day.
4. Field Notes is a method note in Anwar's voice, labelled as such (no sourced Dutchess job story).
5. "Same-day estimates" relies on site-wide copy.
6. Earth Networks 2020 lightning figure carried without a URL in the earlier research row.
7. County-level contractor licence: none found (EMPTY) — page says so and does not claim one; Town of Poughkeepsie permit page body was metadata-only in the earlier run.
8. Check results (2026-10-18): `tools/check_page.py` → only 8 failures, all "live sibling … doesn't link back to /security-camera-maintenance-dutchess-county" (long-island, manhattan, nassau-county, queens, rockland-county, staten-island, suffolk-county, westchester-county — main-run wiring). Size 174,766 B (Bronx 180,560; Brooklyn 184,433; old pages 156–159k).
9. Similarity (masked with check_page.mask, ≥8-word p/li/td/h3/figcaption/FAQ blocks; difflib): page-level word-sequence ratio ≤0.075 (vs Bronx), 5-gram Jaccard ≤0.010; max paragraph vs any silo page 0.647 (hero price bullet vs Bronx) excluding the required shared `security-camera-maintenance-rebuilt-pages` block (1.0, copied unchanged) — warranty-sentence paragraphs ≤0.653.

## Question register — security-camera-maintenance-dutchess-county (REBUILT 2026-10-18)

### §9 Q&A (H3)
1. We live in Millbrook and your office is in the Bronx — how much of the upkeep can be handled without a truck in our driveway?
2. When the internet at our Red Hook farmhouse drops, the app just says "offline" — how can we tell an internet outage from a dead recorder?
3. Our only internet past Amenia is a fixed-wireless link with a data cap — will remote viewing and health checks eat through it?
4. The July storm cut power in Pawling and our generator started within a minute — so why is there a gap in the recording?
5. After a lightning storm two barn cameras still work but the one at the end of the drive is dead — what usually fails, and what should be checked on the others?
6. Ice built up on the dome over our driveway every February — does that hurt the camera, and what keeps the view clear?
7. The oaks along our drive in LaGrange have grown into the camera's view since it went up — is pruning part of maintenance?
8. The barn camera reaches the house over a wireless bridge — why does it drop out every spring, and how do you keep it aligned?
9. Our house, barn and pool house each have their own electric panel — what does maintenance check on a system like that that a one-building system doesn't need?
10. Mice have moved into the pump house where a camera switch lives — what does a visit look for in outbuildings like that?
11. We close our Hyde Park house from November to April — what should be done to the camera system before we leave and when we open it again?
12. Half the cameras in our Fishkill office-park buildings are past manufacturer support — how do you decide which to keep maintaining and which to budget to replace?
13. Since Dutchess pulled its county plate-reader cameras in September 2026, will police lean more on our business cameras — and does that change how we maintain them?
14. Does a camera service visit in the Town of Poughkeepsie need a low-voltage permit?
Other "?" headings: "A Dutchess Camera Down Right Now?" (repair capture), "Not Sure Your System Will Ride Through the Next Storm?" (mid CTA).

### §17 FAQ (accordion = FAQPage)
1. We are only up on weekends — can visits happen midweek with our caretaker letting you in?
2. What happens if a maintenance visit is booked and a snowstorm or ice storm arrives that day?
3. After you finish a remote review, how is your access to our recorder shut off?
4. Can you work around horses and livestock when cameras are inside a barn?
5. Do your technicians photograph our property during a visit, and who sees those photos?
6. Can you leave a spare drive or a spare camera on site so a failure is fixed faster next time?
7. We own property on both sides of the Columbia or Connecticut line — can one plan cover both?
8. Can the gate keypad, intercom and alarm sensors be checked on the same maintenance trip?
9. Does the barn or outbuilding need power on and the house heated on the day of the visit?

De-dup notes: compared by meaning against the old 12-question template, all 15 Bronx questions/9 FAQ, and the questions currently on the rebuilt security-camera-maintenance-brooklyn.html and -nyc.html (research/_batch files for those two did not exist at build time). Avoided: post-outage clock check (Bronx), UPS age/heat (Bronx), keys/roof access (Bronx), lift/ladder (Bronx), dated log for regulator (Bronx), drive hand-back (Bronx), payment (Bronx), van parts stock and pre-storm booking lead time (Brooklyn — a "how much notice to book in Pine Plains" FAQ was replaced for this reason), voltage-sag reboot (Brooklyn/NYC), technician arrival notice and licence for cleaning (NYC), multi-site single schedule (NYC). `check_page.py` exact masked-question check: no duplicates.

---
<!-- merged from batch file security-camera-maintenance-nyc.md (batch run 2026-10-18) -->
# Security Camera Maintenance — NYC hub (batch file, REBUILD 2026-10-18)

Page: `security-camera-maintenance-nyc` (hub, up-link `/`, phone (800) 486-0943 only, Brooklyn GBP 1282 Troy Ave `#brooklyn`). Silo research reused from `research/security-camera-maintenance.md` (§1–§2.7, rows M/R/C/T/G); only NYC-hub research added here, for the main run to merge.

Format (v2.3 §12.4): exact query · platform · URL · finding · page + section used. Tools: WebSearch (result lists), WebFetch (pages read through a summariser — figures as it reported them), Firecrawl search (excerpts). Shell curl blocked. Nothing invented.

## NYC hub

**Thesis:** In New York City a camera system sits inside a chain of owners, agents, supers, tenants and city rules (Local Law 11 façade cycles and sidewalk sheds, NYCHA's camera fleet, the Tenant Data Privacy law, DHCR building-wide services, the NYPD's voluntary business-camera program, 9 NYCRR §125.3, state licensing and the 2024 city electrical code), so citywide maintenance is organised around who owns each camera, who can log in and which clock its footage must satisfy — with borough building stock (Manhattan 97% in 6+ unit buildings, Staten Island 83% one-/two-family) deciding the logistics and the §9 borough factor deciding the price.

### Source matrix (hub)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | Firecrawl search excerpts only (rows NYC-R1–R3). Thread bodies not opened. |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | **EMPTY (not accessible in build env)**. §10.5 says so and quotes no AI Overview. |
| 6 | Landmarks | Common-knowledge landmarks only (125th St/Apollo, Fulton Mall, Roosevelt Ave under the 7, Jamaica Ave under the J, St. George ferry terminal, Grand Central/Midtown East) — descriptive, no stats. FLAG: no URL fetched for these. |
| 7 | Building stock | CHPC (NYC-B1). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)**. |
| 9 | Local news | NY1 (Jun 2025), ABC7 (Sep 2021), CBS New York (May 2024). |
| 10 | Hyperlocal | Queens Post / QNS Ida article: **EMPTY** — WebFetch redirect to qns.com not permitted (PROVENANCE_REQUIRED, blocked URL https://qns.com/2021/09/queens-storm-death-toll-rises-to-11-after-three-bodies-found-in-flooded-flushing-basement-nypd/). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** (silo row: Yelp unsupported by Firecrawl). |

### Findings
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| NYC-F1 | `NYC sidewalk sheds number Get Sheds Down Local Law 11 facade inspection cycle 2025` · WebSearch → WebFetch | https://www.nyc.gov/site/buildings/safety/facade-local-law.page | FISP: buildings taller than six stories; inspection every five years; "Unsafe" → owner "must immediately install protection, such as a sidewalk shed"; repairs within 90 days of report. Page silent on cameras/appurtenance detail. | §5 para 2; §8.5 bullet "Façade inspections"; §9 Q1 |
| NYC-F2 | same search → WebFetch | https://www.nyc.gov/mayors-office/news/2025/04/mayor-adams-signs-historic-legislation-get-sheds-down-remove-unsightly-scaffolding-across | Apr 17, 2025: Intro 393-A shed permit cut from one year to three months; 394-A façade inspections every six to 12 years; 660-A under-shed lighting 45 → 90 lumens, LED, adjustable/shielded near windows; 330 long-standing sheds removed since Jul 2023; CM Keith Powers: "over 400 miles" of scaffolding. | §5 para 2; §5.5 bullet; §9 Q1, Q3; §10.5 Claim 3 |
| NYC-F3 | same search → WebFetch | https://www.nyc.gov/mayors-office/news/2026/03/mayor-mamdani-launches-new-efforts-to-take-sidewalk-sheds-down-- | Mar 6, 2026: sheds down 17% citywide; Local Law 47 sheds over unsafe façades ≤40 ft from building; LL48 proposed rule penalises sheds >180 days, 90-day updates; inspection cycle five → six years, low-risk buildings hands-on every 12; NYCHA $650M façade repairs at 40 developments, sheds removed at 200+ buildings. | §5.5 bullet; §8.5 bullet; §10.5 Claim 3 |
| NYC-N1 | `NYCHA CCTV cameras installed number developments 2025 2026 layered access security cameras` · WebSearch → WebFetch | https://www.nyc.gov/assets/nycha/downloads/pdf/2023_security_infrastructure_testimony_FINAL.pdf | Nov 30, 2023, COO Eva Trimble: >18,500 CCTV cameras; ~$600M since 2014 on cameras and security infrastructure; layered access in 400+ buildings at 80 developments; cameras blocked by sidewalk sheds or other obstructions are relocated. | §5 para 2; §5.5 bullet; §9 Q2; §10.5 Claim 3 |
| NYC-N2 | same → WebFetch | https://citymeetings.nyc/meetings/new-york-city-council/2025-04-15-1000-am-committee-on-public-housing/chapter/number-and-distribution-of-functioning-cctv-cameras-at-nycha-developments/ | Apr 15, 2025 Council Public Housing hearing (auto transcript), Lauren Gray: "over 20,000 cameras in the portfolio across 214 developments and 1,519 buildings"; 52 developments (possibly senior sites — garbled) without CCTV. | §5.5 bullet; §10.5 Claim 2 (52 figure not used) |
| NYC-N3 | carried silo G7 | https://nychajournal.nyc/nycha-completes-over-24-million-in-safety-and-security-upgrades-at-23-campuses/ | NYCHA newer CCTV 21-day retention. | §5 para 4; §5.5 bullet |
| NYC-P1 | `NYPD private security camera registration program businesses share video 2025` · WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/nypd-to-fight-rising-retail-theft-with-surveillance-video-monitoring-program-heres-how-it-works/ | May 16, 2024: city expanding a pilot (began in Queens) letting businesses connect CCTV to NYPD in real time; $1.5M to expand to nine more precincts incl. Harlem; voluntary, free, owner can customise access hours. | §5 para 4; §9 Q8; §10.5 Claim 7 |
| NYC-P2 | same → WebFetch | https://citymeetings.nyc/city-council/2024-06-10-1000-am-committee-on-technology/chapter/what-is-the-nypds-pilot-program-with-fusus-axon-that-allows-businesses-to-share-security-camera-footage | Jun 10, 2024 Council Technology hearing: chapter titled as the NYPD pilot "with Fusus Axon"; NYPD official gave no figures. | §9 Q8 ("referred to it as a pilot run with Fusus/Axon") |
| NYC-T1 | `NYC Tenant Data Privacy Act Local Law 63 2021 smart access system data retention landlord` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63 of 2021: smart access systems (fobs, RFID, apps, biometrics) in Class A multiple dwellings; privacy policy to tenants; minimal data; express consent for reference data; authentication data destroyed within 90 days unless anonymised; no sale; not for harassment. Page does not mention cameras. | §5.5 bullet; §8.5 bullet; §9 Q6; §10.5 Claim 4 |
| NYC-T2 | `DHCR fact sheet decrease in building-wide services security cameras intercom rent stabilized` · WebSearch → WebFetch | https://hcr.ny.gov/living-conditions-and-essential-services | Form RA-84.2 for building-wide decreases in "laundry, doorman, security, storage, or playground services"; "security" not defined; cameras/intercoms not mentioned. | §9 Q7; §10.5 Claim 1 |
| NYC-L1 | `NYC electrical code low voltage security camera work permit license required Department of Buildings Class 2` · WebSearch → WebFetch | https://intro.nyc/local-laws/2024-128 | LL128 of 2024 (NYC electrical code, NEC 2020 basis): "low voltage electrical work" <50 V for signalling, communication, alarm, data generally needs no electrical permit if done by licensed master/special electrician or qualified person; life-safety and certain other circuits require licensed electricians. Cameras not mentioned. | §8.5 bullet; §9 Q14; §10.5 (removed claim) |
| NYC-L2 | `NYC DCWP home improvement contractor license required security system installation` · WebSearch → WebFetch | https://www.nyc.gov/site/dca/businesses/license-checklist-home-improvement-contractor.page | HIC licence for residential home improvement; non-exhaustive list does not mention security/low-voltage. → **Not used** (unclear). FLAG. | not used |
| NYC-L3 | carried silo G10 | https://dos.ny.gov/get-security-or-fire-alarm-installer-license | NYS DOS security/fire alarm installer licence covers CCTV. | §8.5; §9 Q14 |
| NYC-C1 | `licensed adult-use cannabis dispensaries open New York City number 2026 OCM borough` · WebSearch → WebFetch | https://cannabis.ny.gov/new-york-state-celebrates-opening-600th-licensed-adult-use-cannabis-dispensary-five-year | Mar 31, 2026: 623 licensed dispensaries statewide; 600th = Pure Blossoms, Upper West Side; $3.3B sales. No NYC breakdown. | §8.5 bullet (600th on UWS) |
| NYC-C2 | carried silo G1 | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 | 60 days, 8 h outage, 5-min alert, ≤30-day tests, 5-yr records. | §8.5; §9 Q13 |
| NYC-E1 | `Con Edison 2025 heat wave outages New York City customers record peak demand July 2025` · WebSearch → WebFetch | https://ny1.com/nyc/all-boroughs/news/2025/06/25/power-outages-across-nyc-stretch-into-third-day | Jun 25, 2025 9:20 pm: 10,019 customers out (Brooklyn 6,767; Queens 3,016; Bronx 79; Manhattan 38; SI 36); >12,000 at one point from Jun 23; 8% voltage reduction in parts of SE Queens, then sections of SI and several Brooklyn neighbourhoods; one customer can be a whole building. | §5 para 3; Queens card; §9 Q11; §10.5 Claim 6 |
| NYC-E2 | `Hurricane Ida 2021 New York City basement apartment deaths number Queens` / `Ida September 2021 New York City 13 deaths 11 in basement apartments city report` · WebSearch → WebFetch | https://abc7ny.com/nyc-flooding-deadly-8-killed-basement-apartments-flood/10993722/ | Sep 3, 2021: at least 13 dead in NYC; named basement deaths in Hollis and Flushing; 3.15 in of rain in one hour in Central Park. No total basement count in article. | §5 para 3; §9 Q12 |
| NYC-B1 | `NYU Furman Center State of New York City housing share of rental units in buildings built before 1947 citywide` · WebSearch → WebFetch | https://chpcny.org/visualization/housing-stock-visualization/ | ~3.7M units; 62% in 6+ unit buildings; just over a quarter in 1–2 family; ~54% pre-1947; Manhattan 97% in 6+ unit buildings; SI 83% one-/two-family; Brooklyn most even mix; Brooklyn + Queens half of units. | §5.5 bullets; Five Boroughs cards |
| NYC-S1 | `community board liquor license stipulation security cameras retain footage 30 days Manhattan SLA method of operation` · WebSearch → WebFetch ×3 | https://www.nyc.gov/assets/manhattancb3/downloads/forms/sla-stipulations.pdf ; https://www.nyc.gov/assets/manhattancb3/downloads/sla/2024/09/stipulations/217-Bowery-Stipulations-SN.pdf ; https://www.nyc.gov/assets/manhattancb1/downloads/pdf/ll-stips/Dec_2023_stips.pdf | No camera/retention stipulation found in any of the three → **EMPTY**; not used. | not used |
| NYC-X1 | `NYC Local Law 39 2023 lithium-ion batteries UL certification sale e-bike FDNY fires 2025` · WebSearch | (result list) nyc.gov DCWP / council press | E-bike battery rules only; no camera/UPS relevance → not used. FDNY camera-related rule: **EMPTY**. | not used |
| NYC-R1 | `site:reddit.com AskNYC building security cameras not recording footage landlord super` · Firecrawl search (excerpt) | https://www.reddit.com/r/AskNYC/comments/1jvzfxb/do_most_apartment_security_cameras_only_have/ | Title "Do most apartment security cameras only have 'real-time viewing'?"; reply: "In my building it's 30days of recording and super will give you video without any issue." | §9 Q10 |
| NYC-R2 | same (excerpt) | https://www.reddit.com/r/AskNYC/comments/1bfjfdu/is_there_a_way_to_force_a_landlord_to_show_me_the/ | "Show you? Unlikely. However, file a police report the next time it happens and tell the investigating officers that the building has cameras." | §9 Q9; §10.5 Claim 4 |
| NYC-R3 | same (excerpt) | https://www.reddit.com/r/AskNYC/comments/5twdqp/can_i_petition_my_landlord_for_surveillance/ | "Landlord may agree to install a camera but doesn't have any obligation to…" | §10.5 Claim 1 |
| carried | silo T1, T5, G8, G9, C1 | APC FA158934; Federal Register 2026-13518 + Hikvision notice; NYC Admin §22-1202; Penal Law §250.00; HomeAdvisor repair guide | as in silo file | §9 Q11 (APC 3–5 yrs); §10 recorder card + Claim 5 (FCC); §8.5 biometrics/audio; Claim 5 (HomeAdvisor) |

### Keywords (NYC geo layer)
security camera maintenance NYC; CCTV maintenance New York City; camera maintenance plan NYC; building camera maintenance Manhattan/Brooklyn/Queens/Bronx/Staten Island; sidewalk shed camera relocation; Local Law 11 cameras; managing agent camera maintenance; co-op lobby camera maintenance; NYPD camera sharing readiness; NYCHA cameras; recorder retention check NYC. All 11 image alts carry "Security camera maintenance NYC" / "New York City".

### Prices (§9 on silo base §2.7)
Brooklyn/Bronx 1.00: tune-up $150–$350 · plan $200–$500/yr · commercial $1,000–$5,000+/yr · same-day $190–$900. Queens 1.05: $158–$368 · $210–$525 · $1,050–$5,250+ · $200–$945. Staten Island 1.10: $165–$385 · $220–$550 · $1,100–$5,500+ · $209–$990. Manhattan 1.25: $188–$438 · $250–$625 · $1,250–$6,250+ · $238–$1,125. Rounded half-up to whole dollars. $195/hr 3-hr min ($585) unmultiplied (protected). Service schema AggregateOffer low 150 / high 6250 + per-borough OfferCatalog.

### Images (11) — permanent image rule
Drive has no maintenance folder; CompanyCam not connected. Copied with Pillow to WebP q80 (≤1600 px; none needed resizing), each viewed first; no faces, plates, house numbers or readable documents. Scenes chosen to differ from the Bronx page's 11 (dvr-upgrade sources): water-stained-ceiling dome, fascia dome, drop-ceiling mini domes, wall-camera-above-sensor and turret-with-illuminators shots were skipped.
| images/security-camera-maintenance/ | Source | Section |
|---|---|---|
| …-nyc-turret-camera-above-glass-lobby-entrance.webp (hero) | images/nvr-installation/nvr-installation-putnam-county-ceiling-turret-camera-above-glass-entrance.webp | Hero |
| …-nyc-camera-on-steel-arm-below-stone-cornice.webp | images/nvr-installation/nvr-installation-bronx-camera-on-steel-arm-stone-facade.webp | §5 |
| …-nyc-cable-bundles-above-recorder-monitor.webp | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-cable-bundles-above-recorder-monitor.webp | §6 |
| …-nyc-bullet-camera-in-corridor-ceiling-by-door.webp | images/nvr-installation/nvr-installation-bronx-bullet-camera-down-corridor-to-door.webp | §7 |
| …-nyc-mini-camera-above-soffit-and-recessed-lights.webp | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-mini-camera-on-showroom-drop-ceiling.webp | §8 |
| …-nyc-dome-camera-near-light-fixtures-on-drop-ceiling.webp | images/nvr-installation/nvr-installation-staten-island-dome-camera-beside-track-lights-on-drop-ceiling.webp | §9 |
| …-nyc-recorder-live-view-with-date-and-time-stamp.webp | images/nvr-installation/nvr-installation-ulster-county-recorder-live-view-tiles-with-time-stamp.webp (timestamp crop of a monitor scene; Bronx used the bitrate-table crop from a different file) | §9 |
| …-nyc-dual-lens-ptz-camera-product-photo.webp | images/cam-ptz-dual.jpeg (manufacturer) | §10 |
| …-nyc-wi-fi-dome-camera-with-antennas-product-photo.webp | images/hik-connect-app-support-repair/hik-connect-app-support-repair-manhattan-hikvision-wifi-dome-camera-with-antennas-product-photo.webp (manufacturer; Hikvision logo) | §10 |
| …-nyc-bullet-camera-on-pendant-mount-office-ceiling.webp | images/nvr-installation/nvr-installation-westchester-county-bullet-camera-on-pendant-mount-in-office-ceiling.webp | §14 |
| …-nyc-patch-cables-down-equipment-rack.webp | images/nvr-installation/nvr-installation-staten-island-patch-cable-bundles-down-equipment-rack.webp | §15 |
DAILY-LOG note: `images: 11 reused (9 real AESS job photos from images/nvr-installation/ + images/commercial-security-camera-installation/, 2 manufacturer product shots from images/hik-connect-app-support-repair/ and images/cam-ptz-dual.jpeg) (no real security-camera-maintenance photos yet)`.

### FLAGS (NYC hub)
1. Pricing: §9 borough factors applied on the hub for the first time; old Manhattan/Queens/SI pages (and LI/HV) still publish unmultiplied numbers. $190 same-day floor vs $585 3-hr minimum still unresolved (silo FLAG). Commercial "+" ranges multiplied as shown.
2. Unsourced AESS house practices phrased as practice: owner-and-password sheet; shed re-aim/restore with before/after snapshots; export drill + laminated instructions; night checks; basement survey and recorder relocation advice; cable tagging; per-camera cycles; text before arrival/after leaving; super shadowing; after-hours visits; one log format across portfolios with life estimates; "most faults fixed in 1–2 hours"; BYOE at same rates; master password not kept by AESS unless asked in writing; sealed board copy of password; maintaining only client-owned cameras.
3. Landmark cards (125th St/Apollo + nearby elevated structures, Fulton Mall, 7 over Roosevelt Ave, J over Jamaica Ave in Woodhaven/Richmond Hill, St. George ferry, Grand Central/Midtown East) and borough-card details (e.g. Ocean Parkway elevator buildings) are general knowledge, not fetched this run.
4. No general NYC/NYS rule requiring private landlords to keep cameras working or to release footage to tenants was found — page says "we found none" and adds "not legal advice".
5. DCWP HIC licence applicability to camera work unclear — not stated on page. SLA/community-board camera stipulations searched, none found.
6. Fusus/Axon named only from the Council hearing chapter title (NYPD gave no detail).
7. NYCHA "over 20,000 cameras" is from an auto-generated transcript summary.
8. Field Notes is a method note in Anwar's voice, not a specific job story — confirm or replace.
9. Check (2026-10-18): `tools/check_page.py` → only failures: 7 HV/LI old-template siblings (hudson-valley, long-island, orange, putnam, rockland, ulster, westchester) don't link back to /security-camera-maintenance-nyc — main-run wiring. File size 187,995 B vs Brooklyn rebuild 184,736 B (3.2 KB gap) — re-check after the parallel builds settle.
10. Similarity (masked difflib word-sequence): page ≤0.118 vs Bronx, ≤0.081 vs Brooklyn/Dutchess rebuilds, ≤0.032 vs old template pages; paragraph max <0.65 except boilerplate (freshness byline, trust chips, the fixed §10.5 H2 pattern, warranty/NAP line).
11. Three first-draft §10.5 claims overlapped the parallel Dutchess (live picture = recording; costs same everywhere) and Brooklyn (any handyman) pages, and a portfolio question overlapped Dutchess Q12 (keep vs budget to replace) and its FAQ 7 (one plan across properties); all replaced before finishing.

---

## Question register — security-camera-maintenance-nyc (REBUILT 2026-10-18)

### §9 Q&A (H3)
1. Our building is entering its Local Law 11 façade cycle — what should happen to the cameras on the front wall before the inspectors arrive?
2. A shed went up in front of our shop last month and the entrance camera now records plywood — whose job is it to fix the view?
3. The brighter shed lights the city now requires came on and our night picture turned white — is that the camera or the lights?
4. We rent a ground-floor store and the landlord's cameras cover our entrance — can we ask for them to be serviced, or should we put up our own?
5. Should the super, the managing agent or the owner hold the recorder's admin account — and how many logins should there be?
6. Our building moved from keys to fob and app entry — does the city's tenant data law change anything about how the cameras and door logs are kept?
7. Tenants say the lobby camera has been broken for months — can a rent-stabilized tenant take that to the state?
8. The NYPD invited our store to connect its cameras for live viewing — what should be checked before we say yes?
9. How should our super hand a clip to a detective without giving away the recorder or its password?
10. Tenants keep asking how many days of video the building really keeps — how do we find the true figure?
11. Con Edison cut voltage on our block during the June heat but the lights never went out — can that still harm the recorder?
12. Our recorder sat in a basement that took water during Ida — where should it live now?
13. We hold cannabis retail licences for two stores in different boroughs — can one maintenance plan keep both stores' test records in order?
14. Should we ask a camera maintenance company for its state licence number, and what does that licence actually cover?
15. As managing agent for buildings in several boroughs, how do we get camera reports we can actually compare side by side?

### §17 FAQ (accordion = FAQPage)
1. Why does a visit cost more in Manhattan than in Brooklyn or the Bronx?
2. Can our super walk round with the technician and learn the checks?
3. Do you work evenings or weekends when an office or shop is closed?
4. We rent one floor of a building — can you maintain only our cameras and leave the landlord's alone?
5. Will you work with the IT company that manages our network?
6. How do you handle buildings with a doorman, a security desk and a freight elevator schedule?
7. Is there a minimum number of cameras for a maintenance plan?
8. Will the technician let us know before arriving and after leaving?
9. Do we pay for the whole year up front, or visit by visit?

### §10.5 claims
1. Landlords in New York are required to keep building cameras working · 2. Camera upkeep matters for shops, not for apartment buildings · 3. Sidewalk sheds are temporary, so the cameras can wait · 4. Anyone who appears on a building camera can demand a copy of the footage · 5. If footage keeps going missing, buy a new recorder · 6. Blackouts are the only power problem cameras face · 7. Once cameras are shared with the police, the police look after them.

Checked by meaning against: silo register (old template 12 + Bronx 15 + 9), and the live Brooklyn and Dutchess rebuild pages' questions/claims (their `research/_batch/` files did not exist at finish time).
