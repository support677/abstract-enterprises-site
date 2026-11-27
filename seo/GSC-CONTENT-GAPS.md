# GSC Content Gaps — master queue

Search terms Google already shows abstractenterprisessecuritysystems.com for, with no page of their own. Built and maintained by the "Daily GSC content-gap page builder" scheduled task (Anwar's permanent rule, Nov 27 2026: "constantly scan [Search Console] and make those pages that we don't have").

- Source: Search Console, property sc-domain:abstractenterprisessecuritysystems.com, data_state all. 6-mo = May 27 – Nov 26 2026; 28-day = Oct 30 – Nov 26 2026.
- Branded queries (abstract / aess / enterprise) and queries under 5 impressions dropped. Tokens normalized (plurals, install/installer/installation, cams/cameras, near me / ny / nyc / best / company / service / cost words stripped).
- GAP = no single page slug carries the query's service words. Then checked for intent: if an existing silo already answers it under different words, the cluster is **COVERED** and goes to the daily zero-click optimizer, not a new page.
- New pages are built by the page factory from PAGE-QUEUE.md (DAILY-RUN.md, full BLUEPRINT), hubs first, then boroughs/counties; neighborhoods only when a Google Ads / Facebook campaign targets one.
- Hard rules: a NEW service needs Anwar's keyword list in keywords/ first (he declined Claude-drafted lists); never compete with an existing page; never delete/rename/merge pages or change H1s/URLs; never write "AESS" on the site; no byline; only prices Anwar set; out of scope: electrical, hood/fire suppression, mortise/door lock hardware, wall patching; fire alarm pages only Suffolk + Hudson Valley.
- Merge note: seo/GSC-REGEX-GAPS.md (daily optimizer's no-page list) did not exist in the repo on Nov 27 2026; merge it here when it appears.

## Run log

| Date | Queries (6-mo) | Gap queries | Gap impressions (6-mo) | New clusters | Pages queued | Notes |
|---|---|---|---|---|---|---|
| 2026-11-27 | 22,633 | 6,857 | 435,335 | 15 NEEDS KEYWORD LIST | 32 (smart home 16, video surveillance 16) | First run. This session could not push to GitHub directly; queue committed through the GitHub connection. Pages are built by the page factory, not this run. |

## 1. Building / Queued (keyword list in keywords/)

| Cluster | 6-mo impr | 28-day impr | Top queries | Top areas | Pages | Keyword list | Status |
|---|---|---|---|---|---|---|---|
| Smart home installation | 60,429 | 1,597 | smart home installation near me; smart home installation long island; smart home installer brooklyn | NYC 12,433; Manhattan 11,589; Brooklyn 8,695; Long Island 3,300 | smart-home-installation-{nyc, long-island, hudson-valley, 5 boroughs, 8 counties} | keywords/smart-home-installation.md | Queued (16 TODO in PAGE-QUEUE.md, Nov 27). Price source not mapped in tools/check_page.py yet |
| Home security system installation | 37,188 | 4,291 | home security systems; security system installation near me; security system installer | NYC 6,844; Westchester 1,824; Brooklyn 1,612; Manhattan 1,384 | home-security-system-installation-* | keywords/home-security-systems.md | Building — NYC hub file in repo, 15 TODO |
| Video surveillance system installation | 26,130 | 3,255 | video surveillance system installation long island city; security surveillance system installation manhattan; surveillance camera installation nyc | NYC 3,280; Westchester 1,906; Queens 1,471; Manhattan 1,126 | video-surveillance-installation-{16 areas} | keywords/video-surveillance-installation.md | Queued (16 TODO in PAGE-QUEUE.md, Nov 27). Price source not mapped in tools/check_page.py yet |
| Burglar alarm installation | 9,308 | 1,217 | burglar alarm installation; burglar alarm companies; burglar alarm systems service long island | Westchester 2,025; Long Island 1,422; Manhattan 596 | burglar-alarm-installation-* | keywords/burglar-alarm-installation.md | Building — NYC hub file in repo, 15 TODO |

## 2. NEEDS KEYWORD LIST (Anwar asked by text Nov 27 2026 — do not re-ask before Dec 4)

| Cluster | 6-mo impr | 28-day impr | Top queries | Top areas | Suggested page type + slug | Status |
|---|---|---|---|---|---|---|
| Home intercom systems | 17,002 | 2,791 | home intercom systems long island; intercom systems nyc; intercom system installation nyc | NYC 4,141; Long Island 3,406; Queens 1,254 | intercom-installation-{missing 13 areas}: the silo exists in only 3 areas and has no keyword file | NEEDS KEYWORD LIST |
| Lutron / smart lighting | 9,925 | 477 | lutron smart lighting long island; smart lighting installation brooklyn; lutron installer brooklyn | NYC 2,639; Manhattan 1,986; Brooklyn 1,444 | lutron-lighting-installation-{16} (brand; don't claim certified — Anwar isn't Lutron-certified yet) | NEEDS KEYWORD LIST |
| Fire alarm inspection | 9,056 | 978 | fire alarm inspection suffolk county; fire alarm inspection miller place; fire alarm inspection locust valley | Suffolk 919; Nassau 824 | fire-alarm-inspection-{suffolk-county, hudson-valley + HV counties} only; Nassau/NYC blocked (FM number / NICET) | NEEDS KEYWORD LIST |
| Alarm / camera monitoring | 7,014 | 547 | smart home monitoring long island; home security monitoring westchester; alarm monitoring nyc | NYC 1,117; Long Island 682; Westchester 352 | alarm-monitoring-{16} ($45 app / $30 keypad tiers; COPS + CHeKT) | NEEDS KEYWORD LIST |
| Control4 | 4,476 | 445 | control4 smart home long island; control4 home automation system long island | Long Island 1,782; Westchester 1,086; NYC 544 | control4-installation-{16} (not certified yet — no dealer claim) | NEEDS KEYWORD LIST |
| Whole-home / multi-room audio | 3,645 | 547 | multi-room audio systems long island; whole home audio brooklyn | Long Island 1,519; Westchester 688; Rockland 558 | whole-home-audio-installation-{16}; Sonos wording stays on sonos-installation-* | NEEDS KEYWORD LIST |
| Home theater (missing areas) | 2,986 | 423 | home theater installation queens; home theater systems long island; home cinema installation nyc | Long Island 964; Queens 413; Westchester 398 | home-theater-installation-{nyc, hudson-valley, 5 boroughs, nassau, suffolk, putnam, dutchess, ulster}: 4 pages exist, no keyword file | NEEDS KEYWORD LIST |
| Outdoor TV installation | 2,692 | 316 | outdoor tv installation long island; outdoor tv installation nyc | Long Island 906; NYC 727; Manhattan 358 | outdoor-tv-installation-{16}; link tv-installation-* | NEEDS KEYWORD LIST |
| Home network / WiFi | 2,392 | 141 | home network installation scarsdale; wifi installation westchester county | Westchester 854; NYC 674; Brooklyn 310 | wifi-installation-{16}; network-installation-* keeps "network installation" | NEEDS KEYWORD LIST |
| Surround sound | 2,001 | 207 | surround sound installation long island; surround sound design long island | Long Island 747; NYC 425 | surround-sound-installation-{16} | NEEDS KEYWORD LIST |
| Hidden camera installation | 1,483 | 74 | hidden camera; hidden cameras; hidden camera for home | (no area) | hidden-camera-installation-nyc first; legal/consent facts sourced | NEEDS KEYWORD LIST |
| Savant | 1,173 | 126 | savant smart home long island; savant dealer bronxville | Long Island 813; Westchester 140 | savant-installation-{16} (no dealer claim) | NEEDS KEYWORD LIST |
| Crestron | 1,121 | 112 | westchester residential crestron installer; brooklyn crestron installer; crestron alternative nyc | Westchester 450; Brooklyn 276 | crestron-installation-{16} (no dealer claim) | NEEDS KEYWORD LIST |
| Video management system (VMS) | 1,091 | 10 | video management systems companies; commercial video management systems | (no area) | video-management-system-installation-nyc | NEEDS KEYWORD LIST |
| Outdoor speakers | 885 | 145 | outdoor speaker installation long island; outdoor speakers westchester county | Long Island 384; Westchester 378 | outdoor-speaker-installation-{16} | NEEDS KEYWORD LIST |

## 3. COVERED by an existing silo (same intent, different words) → daily zero-click optimizer notes, no new page

| Cluster | 6-mo impr | 28-day impr | Top queries | Existing page silo that should rank |
|---|---|---|---|---|
| Fire alarm installation / system (LI, HV, Suffolk) | 83,478 | 8,859 | fire alarm system installation long island; fire alarm installation poughkeepsie; fire alarm system installation in westchester | fire-alarm-installation-*-ny hubs + counties (LIVE). Optimizer: work "fire alarm system" wording into them. Residential smoke-detector searches stay out (NFPA 72 commercial-only rule) |
| Security cameras (general) | 29,242 | 3,782 | apartment security camera systems nyc; security camera system; construction site cctv camera nyc | security-camera-installation-*, cctv-installation-*, apartment-building / construction-site camera silos |
| Alarm systems (general) | 17,330 | 2,196 | alarm systems near me; alarm providers; alarm systems installation brooklyn | alarm-installation-* (16) |
| Business / commercial security cameras | 11,454 | 1,245 | business security camera systems; restaurant security cameras nyc; business security camera installation | commercial-security-camera-installation-* (16) |
| Access control / key fob / card | 9,200 | 1,325 | access control systems long island; keypad access control westchester; key fob entry system nyc | access-control-installation-* (16) |
| TV wall mount installation | 9,004 | 1,086 | tv wall mount installation near me; loewe tv installers long island | tv-installation-* (16) |
| Audio/video (AV) installation | 8,002 | 1,495 | home technology installation long island; audio video installation nyc; commercial av installation long island | av-sound-installation-* (16) |
| Commercial alarm / alarm companies | 6,969 | 454 | alarm system companies near me; commercial alarm companies near me | alarm-installation-*, commercial-security-systems-* |
| Wiring / cabling (general) | 6,266 | 798 | nyc approved cabling; residential cabling solutions new york | structured-cabling-installation-*, network-installation-*, low-voltage-installation-* |
| Network cabling / ethernet | 5,217 | 677 | ethernet wiring manhattan; ethernet cable installation long island | network-installation-*, cat6-installation-* |
| Structured / low-voltage wiring | 4,881 | 527 | low voltage wiring westchester county; structured wiring nyc | low-voltage-installation-*, structured-cabling-installation-* |
| Building / apartment / co-op intercom | 3,306 | 409 | building intercom nyc; apartment intercom nyc; coop intercom system nyc | /apartment-intercom-system-nyc, /co-op-board-intercom-upgrade, intercom-repair-* |
| Home security camera installation | 3,008 | 146 | home camera security systems; home security camera system | residential-security-camera-installation-* (16) |
| Commercial fire alarm | 3,000 | 903 | commercial fire alarm installation; commercial fire alarm systems westchester | fire-alarm-installation-*-ny (commercial NFPA 72 pages) |
| Doorbell camera (Ring/Nest) | 2,949 | 395 | nest doorbells in queens; video doorbell installation long island | doorbell-camera-installation-* (16) |
| Keyless entry / keypad | 1,901 | 375 | keyless entry installation nyc; keyless entry installation manhattan | smart-lock-installation-* (16) |
| Samsung Frame TV | 628 | 120 | samsung frame tv mounting long island; frame tv installation near me | tv-installation-* (Frame TV mounting is on those pages) |
| Buzzer | 539 | 90 | buzzer systems nyc; replace apartment buzzer | door-buzzer-repair-*, door-buzzer-installation-nyc |
| Unmatched long tail (906 queries) | 24,824 | — | security home systems; home cinema installation; card key access; solar security trailer rental | Mostly existing silos (home security, home theater, access control, solar-surveillance-trailer); re-checked next run |

## 4. Skipped — out of scope

| Cluster | 6-mo impr | Reason |
|---|---|---|
| Kitchen hood / fire suppression | 1,707 | Not our scope (Anwar, Oct 2026) |
| Electrical work | 1,149 | Not our scope |
| Mortise / deadbolt / locksmith | 223 | Not our scope (Nov 19 2026) |
| Test tools ("fluke") | 1,061 | Not a service search |
| NYC / Nassau fire alarm pages | — | Blocked until NICET (NYC) / Nassau FM number |
