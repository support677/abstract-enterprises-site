# Super Live Plus App Support Repair — silo research

Created 2026-10-18 by the REBUILD batch for super-live-plus-app-support-repair-nyc, -orange-county, -putnam-county (three parallel builders; each part below is that builder's full research log, format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used; unreachable sources written EMPTY (not accessible in build env)). Question register for each page is inside its part. A concurrent run is rebuilding bronx/long-island/manhattan and will append its own parts.

---

# PART A — NYC hub builder

# Super Live Plus App Support Repair — silo research (NYC hub part file)

Created 2026-10-18 by the REBUILD subagent for `super-live-plus-app-support-repair-nyc` (queue line: `REBUILD | super-live-plus-app-support-repair-nyc | Super Live Plus App Support Repair | NYC hub | up / | (800) 486-0943 | GBP Brooklyn`). Part file for the main run to merge into `research/super-live-plus-app-support-repair.md` (not written by this agent). Concurrent rebuilds of bronx / long-island / manhattan (earlier batch) and orange-county / putnam-county (this batch) may add their own parts.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (markdown / query / PDF parser), Firecrawl Alexandria providers `apps-apple-com` (apps/app, apps/reviews) and `nvd-nist-gov` (vulnerabilities/cve). Shell curl blocked. Firecrawl does not open reddit.com, so every Reddit row is a search-result **excerpt**. "Excerpt" = read only as a snippet.

Page section labels (NYC page): §Hero, §Quick, §5 Neighborhood (+ §5.5 facts list), §Repair (same-day block, five checks, symptom table), §6 Services, §7 Architecture (+ §7.5 method), §8 Commercial (+ §8.5 rules list), §9 Q&A (cluster → H3 1–14), §10 Equipment (+ connection-method table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks + borough routing, §14 Pricing, §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ 1–10, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every Super Live Plus page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows R1–R8). Threads not openable in build env. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and works from claims published by app-store listings, reseller pages, Q&A sites and forums (rows A1–A5, R1–R8). |
| 6 | Area landmarks | NYC section rows NYC-L1–L6. |
| 7 | Area use cases / building stock | NYC section rows NYC-I1–I4, NYC-N1. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl search backend; no Bing/DDG PAA, related or autocomplete surface. |
| 9 | Local news | NYC section NYC-N1 (amNewYork, May 16 2024). |
| 10 | Hyperlocal | EMPTY for Super Live Plus specifically (no Patch / Bronx Times / Brooklyn Paper / QNS item about the app surfaced). Not used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not searched to review-text level; Apple App Store 1–2★ reviews used instead as the complaint source (A3). |

### 1.2 What the app is (S)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `Super Live Plus app TVT DVR NVR` · Firecrawl search → Firecrawl scrape (markdown) | https://play.google.com/store/apps/details?id=com.tvt.superliveplus&hl=en_US | Package `com.tvt.superliveplus`; listed developer "Peng AnTai"; "About the developer: TVT (HK) LIMITED", Hong Kong address; 3.3★ / 53.3K reviews (phone tab 3.4 / 51.6K); 5M+ downloads; Free; "professional mobile phone client software for digital video recorders and IP cameras in CCTV surveillance (compatible models only)"; Updated Oct 8, 2026; What's new "Support account switching"; data safety "No data collected / No data shared". Same developer also lists SuperLiveNVR, NVMS2, NVMS2 Plus. Visible reviews: playback "jumps" and app crashes when ending a clip recording (2020); "Doesn't connect on mobile reliably… next day it will not connect. Turn system off and on…"; app "keeps signing off" from 5/10/24, fixed by 6/2/24. | §Hero; §5 para 1; §5.5 bullets 1–2; §9 H3 12; §10.5 H3 1, 3; §17 FAQ 3; §Sources |
| S2 | Alexandria `apps-apple-com` apps/app, app_id 1058758642 | https://apps.apple.com/us/app/superlive-plus/id1058758642 | Seller "Peng Antai", bundle `com.pengantai.superliveplus`, released 2016-02-22, current 1.16.7 (2026-01-05); 3.9★ from 15,849 ratings (histogram 1★ 2,643 … 5★ 9,253); free, no in-app purchases; runs on iPhone/iPad and on Macs with Apple M1 or later (macOS 12+); support URL en.tvt.net.cn. Version history: 1.11.1 (Oct 2022) doorbell support; 1.12.0 (Mar 2023) "Support DVR cloud storage function", "Login status supports offline mode", manual door opening; 1.13.0 Push 2.0 thumbnails; 1.14.0 (May 2024) doorbell time zone/DST, LPR attributes; 1.14.4 "Fixed the issue: Playback of DVR 3.0 speeds up"; 1.15.0 (Nov 2024) "Optimized the device sharing function"; 1.16.0 (Apr 2025) "Optimized the sharing device function", "Optimized the device upgrade process", push configuration interface. | §5.5 bullet 2; §6 cards; §9 H3 5, 12; §10.5 H3 3, 6; §17 FAQ 2, 3, 6; §Sources |
| S3 | `"SuperLive Plus" google play reviews offline` · Firecrawl search (excerpt) | https://www.appbrain.com/app/superlive-plus/com.tvt.superliveplus | "SuperLive Plus scores 3.37 out of 5 stars, from 51,619 ratings on Google Play." | Background only |
| S4 | `Super Live Plus app TVT DVR NVR` · Firecrawl search → scrape (PDF parser) | https://www.mysecuresystems.com/wp-content/uploads/SuperLivePlus-User-Manual.pdf | SuperLive Plus V1.0 user manual (reseller mirror of TVT doc). LAN: add by IP + port or scan QR; phone and device "in the same network segment". Over 2G/3G/4G: PPPoE, static WAN IP, or LAN IP with port forwarding / UPnP; DDNS example `123.dvrdydns.com:89`. QR login: "My device is the MAC address (or serial number)"; "If the device and the mobile client are in the different network segment, the device shall support QRCODE and enable the NAT." Default user `admin`, default password `123456`. Server list: green = connected, gray = failed, twinkling = connecting. Local settings: record recycle, reserved disk space, audio/shake alarm, gesture password, Auto syn of device list. Help & Feedback submits issues to maker. | §5 para 2; §Repair checks 3–4 + table; §7.5; §9 H3 1, 3; §10 table; §10.5 H3 2, 5; §Sources |
| S5 | `Super Live Plus app TVT DVR NVR` · Firecrawl search → scrape (markdown) | https://www.usacompua.com/pages/super-live-plus-mobile-app-support-remote-viewing-download-pc-app | Florida reseller page: "Designed for many TVT recorders and select OEM variants"; QR pairing "no port forwarding"; "Viewer-only logins so you never share your admin password"; onboarding "Cloud P2P, QR pairing, manual add by serial/IP"; push per channel. A store review on the page calls a 16-ch hybrid DVR an "Equivalent Q-see system". | §6 sharing card; §9 H3 3; §10.5 H3 2 (quoted as reseller claim); §Sources |
| S6 | `"Super Live Plus" OR "SuperLive Plus" compatible brands DVR white label list` · Firecrawl search (excerpts) | https://www.walmart.com/ip/SuperLive-Plus-8MP-4K-16CH-Hybrid-DVR-Supports-8MP-HD-TVI-CVI-AHD-Analog-Cameras-up-8CH-IP-H-265-2x-SATA-NDAA-Compliant-Free-Remote-Surveillance-APP/18720258973 ; https://www.ebay.com/itm/366008291212 ; https://www.ultima-tech.com/8mp-4k-16ch-hybrid-dvr | Retail listings sell recorders under the name "SuperLive Plus" / "SuperLive" — "16CH HD Analog + 8CH IP", "HD-TVI/CVI/AHD", "NDAA Compliant" (seller claim). | §6 hybrid card; §9 H3 12, 14 (as seller claim); §10 cards; §Sources |
| S7 | `Shenzhen TVT Digital Technology company OEM…` · Firecrawl search → scrape (query) | https://www.tvt.net.cn/ | Shenzhen TVT Digital Technology Co., Ltd: product lines "HD IP camera, HD coaxial camera, HD NVR, HD DVR"; "made its mark in more than 30 countries and regions". Founding/listing not on page. | §5 para 1; §17 FAQ 3; §Sources |
| S8 | `Shenzhen TVT…` · Firecrawl search (excerpt) | https://www.cctvforum.com/topic/58642-tvt-supercam-plus/ ; https://www.justanswer.com/home-security-systems/s8gxp-currently-two-sites-cameras-managed.html | Excerpts: TVT DVR owner using NVMS-1000 on PC and SuperCam Plus; customer with "two sites with cameras managed under SuperLive Plus". | Background (§9 H3 6) |

### 1.3 Q-See (Q)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Q1 | `Q-See security cameras company closed 2020 customers app support ended` · Firecrawl search → scrape (query, directQuote) | https://www.q-see.com/pages/service-and-support | New Qsee (trademark owner, back in 2023): "The old Q-See has closed its server and discontinued most of the apps and PC software, which affects all customers who relied on remote viewing"; old cameras "can't be connected to the new APP"; "If the APP is not valid any more, it is suggested to access your cameras via other ways"; CMS for PC "QT View"; "you should not format the hard drive". New Qsee cannot retrieve passwords ("don't hold any servers or hardwares from the old Qsee"). | §9 H3 11; §10.5 H3 4; §Sources |
| Q2 | same search (excerpts) | https://www.reddit.com/r/homesecurity/comments/lkqpsh/qsee/ ; https://ipcamtalk.com/threads/q-see-closing-doors-jan-31st-2021-no-more-remote-viewing-options-to-fix.54091/page-14 ; https://www.q-see.com/pages/download | "Q-see went out of business Jan 31st 2021"; forum: app worked again after a NoIP DDNS account when Q-See DDNS stopped; Qsee download page: firmware "stopped update after Qsee went out of business in 2019" (dates conflict between sources — page says only "when the old company closed"). | §9 H3 11 (no date asserted beyond "closed its server"); §Sources |
| Q3 | — | — | **No source found that Q-See recorders run Super Live Plus.** Page does NOT claim Q-See = TVT or that SLP opens Q-See boxes; it says we check model-by-model. | FLAG |

### 1.4 Security (V)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| V1 | Alexandria `nvd-nist-gov` vulnerabilities/cve `CVE-2024-14007` | https://nvd.nist.gov/vuln/detail/CVE-2024-14007 | "Shenzhen TVT Digital Technology Co., Ltd. NVMS-9000 firmware (used by many white-labeled DVR/NVR/IPC products) versions prior to 1.3.4 contain an authentication bypass… single crafted TCP payload to an exposed NVMS-9000 control port… discloses… administrator usernames and passwords in cleartext". CVSS 4.0 8.7 HIGH, CWE-306; published 2025-11-24; not in KEV. | §5 para 4; §5.5 bullet 5; §6 firmware card; §9 H3 9; §10.5 H3 7; §Sources |
| V2 | `TVT NVMS-9000 DVR vulnerability botnet exploited 2025 admin credentials disclosure` · Firecrawl search → scrape (query, directQuote) | https://www.bleepingcomputer.com/news/security/new-mirai-botnet-behind-surge-in-tvt-dvr-exploitation/ | April 8, 2025: spike "peaking on April 3, 2025, with over 2,500 unique IPs scanning"; flaw disclosed by SSD Advisory May 2024; "majority of the targeted devices are based in the U.S., the U.K., and Germany"; advice: if upgrading impossible, restrict public internet access to DVR ports; if compromised "disconnect the DVR, perform a factory reset, update to the latest firmware, and then isolate it". | §5 para 4; §5.5 bullet 5; §9 H3 9; §10.5 H3 7; §Sources |
| V3 | same search (excerpts) | https://www.greynoise.io/blog/surge-exploitation-attempts-tvt-dvrs ; https://www.vulncheck.com/advisories/tvt-nvms9000-unauthenticated-admin-queries-and-information-disclosure ; https://www.scworld.com/brief/deluge-of-tvt-dvr-exploitation-attempts-likely-due-to-mirai-based-botnet | GreyNoise: surge began March 31, 2025, overlap with Mirai; SC World excerpt: targeted DVRs "had its firmware last updated seven years ago". | §Sources (GreyNoise); SC World background only |
| V4 | `TVT DVR NVR forgot admin password reset official method…` · Firecrawl search (excerpts) | https://www.reddit.com/r/hardwarehacking/comments/1ewskos/cctv_box_password_findreset/ ; https://play.google.com/store/apps/details?id=com.rat.cctvsuperpassword | r/hardwarehacking excerpt: reset method "seems to use the model number, MAC address and date + time to generate" a code. Google Play "CCTV Super Password" (third-party, 3.4★) lists SuperLive Plus, NVMS2, NVMS2 Plus and "Reset with Serial Number". No official TVT reset document found → EMPTY for official procedure. | §9 H3 10; §10.5 H3 5; §Sources |

### 1.5 Reddit and forums (R) — excerpts only
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com SuperLive Plus app` · Firecrawl search | https://www.reddit.com/r/homesecurity/comments/1brss3t/remove_access_from_superlive_plus/ | "I gave my roommate access to our cctv camera footages through superlive plus. Recently they moved out and it wasn't a peaceful goodbye." | §9 H3 5; §Sources |
| R2 | same | https://www.reddit.com/r/homesecurity/comments/1b8s9j0/trouble_with_superlive_plus_app/ | "keeps saying 'can't scan QR code'… 'Failed to connect to…'" | §10.5 H3 2 background; §Sources |
| R3 | same | https://www.reddit.com/r/SecurityCamera/comments/1h3n93v/dhcp_failure/ | "using the SuperLive plus app… for over a year… Recently the app is no longer showing a green WiFi symbol" (title "DHCP: failure"). | §Repair table row 2; §Sources |
| R4 | same | https://www.reddit.com/r/cctv/comments/1lofnhg/help_upgrading_dead_dvr_looking_for_better_mobile/ | TVT 16-ch analog + 8-ch IP DVR; "NVMS 2.0 for desktop access and SuperLive Plus for mobile. I was never a fan of SuperLive Plus — it lacks key features". | §10.5 H3 6; §Sources |
| R5 | same | https://www.reddit.com/r/tinycam/comments/glptdp/superlive_plus/ | Viewing via "SuperLive Plus app with P2P by providing a 12 characters long UUID, a username" and password. | §9 H3 3 (P2P ID); §Sources |
| R6 | same | https://www.reddit.com/r/homedefense/comments/ibiv26/dvr_question_is_someone_spying_on_me_through_my/ | "Superlive Plus and HiSharp look like apps to VIEW the cameras, but that's not the DVR system installed". | §10.5 H3 1 background |
| R7 | same | https://www.reddit.com/r/selfhosted/comments/1iazt9h/is_there_an_app_to_consolidate_all_cctv_on_a/ | Dad has "Ezviz, Hikvision, iDMSS plus, Superlive Plus, etc" apps. | §9 H3 6 background |
| R8 | same | https://www.reddit.com/r/cctv/comments/1h0lrfa/remote_access_no_data/ | SuperLive Pro remote view "no data" on Atlantic Broadband units. | Background only |
| R9 | `T-Mobile 5G Home Internet CGNAT port forwarding DVR remote viewing not possible` · Firecrawl search (excerpts) | https://www.reddit.com/r/tmobileisp/comments/17d9gas/port_forwarding/ ; https://www.purevpn.com/blog/t-mobile-cgnat-port-forwarding/ | "You cant open ports with tmobile home internet as they use CGNAT (you dont have a public ip address sitting on your router)"; "a port forwarding rule on your router only controls what happens inside your own network. It cannot open the corresponding port at T-Mobile's CGNAT layer". | §5 para 2; §Repair table; §9 H3 1; §10.5 H3 2; §Sources |

### 1.6 App-store review claims (A) — feed §10.5
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | Alexandria apps-apple-com apps/reviews 1058758642 | https://apps.apple.com/us/app/superlive-plus/id1058758642 | 2★ "Too many issues" (2026-04-03): manages condo communities; two have cameras on this app; "one property or the other will randomly disappear from the app"; law-enforcement footage request "took almost the entire day to retrieve it because the playback feature wouldn't load"; scrubbing the timeline "always lands on a time that's either much too early or too late". | §5 para 3; §9 H3 6, 7; §10.5 H3 3; §Sources |
| A2 | same | same | 1★ (2025-04-06): cameras "offline on the mobile app, but are working on the home monitor"; after latest update "unable to view past recordings". | §Repair check 1; §10.5 H3 1; §Sources |
| A3 | same | same | 1★ (2022-05-04): forgot password, no reset function, "down to one more attempt and if so unsuccessful I will be locked out". 1★ (2019-11-29) daycare: "IP address was wrong, when it wasn't". 4★ (2020): switching away from app breaks it until restart. 2★ (2024-05-09): motion alerts "constantly going off" on leaves and bugs, missing people. | §9 H3 10; §17 FAQ 10; §10.5 H3 3, 5; §Sources |
| A4 | `"SuperLive Plus" google play reviews offline` · Firecrawl search (excerpt) | https://www.justanswer.com/software/tukzx-superlive-plus-app-iphone-offline-error.html | "If SuperLive Plus shows offline on iPhone SE, first check your Wi-Fi or cellular connection. Restart the app and phone…" | §10.5 H3 1 (claim corrected) |
| A5 | — | — | Google AI Overview text for "super live plus offline" etc.: EMPTY (not accessible in build env). | §10.5 intro states this |

### 1.7 Federal (F) — carried
| # | Source | Finding | Used |
|---|---|---|---|
| F1 | carried from research/hik-connect-app-support-repair.md row F2 (https://www.fcc.gov/laboratory-division/equipment-authorization-approval-guide/equipment-authorization-system), not re-fetched | FCC rules effective Feb 6, 2023 prohibit authorization of video surveillance equipment by Hytera, Hikvision, Dahua; Covered List producers Huawei, ZTE, Hytera, Hikvision, Dahua. TVT not named. | §9 H3 14; §Sources |
| F2 | carried from same file row F1 (Federal Register 2026-13518), not re-fetched | July 16, 2026 prohibition on continued importation/marketing of covered equipment; continued use not prohibited. | §9 H3 14 |

### 1.8 Keyword plan (five layers, silo)
- Service: Super Live Plus app support, Super Live Plus repair, SuperLive Plus setup, TVT DVR app support, DVR app repair NYC.
- Problem: Super Live Plus offline, device offline, connection failed, can't scan QR code, playback won't load, push notifications not working, forgot DVR password, locked out, remove shared access.
- Technology: P2P / QR / NAT, IP + port, DDNS, port forwarding, CGNAT, NVMS-9000 firmware, NVMS2 / NVMS-1000 PC client, hybrid DVR (TVI/CVI/AHD), H.265, push 2.0.
- Industry: bodega / deli, laundromat, small landlord multifamily, condo/co-op managing agent, daycare, restaurant, multi-site retail.
- Geographic (this page): NYC, New York City, five boroughs, each borough name only as a routing link.

### 1.9 Silo pricing (no invented prices) — FLAG
Old 16 pages publish no prices (only "$0 Diagnosis by Phone" in the stats bar). The NYC page uses: $0 phone triage (old pages' framing); protected service rate $195/hr, 3-hr min ($585), not multiplied (blueprint v2.3 §9); recorder replacement borrowed from DVR Upgrade silo base (research/dvr-upgrade.md §1.8: 4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+) × NYC hub = Brooklyn base 1.00. Same borrowing as hik-connect-manhattan (×1.25) and smart-pss-bronx (×1.00). FLAG for Anwar: confirm borrowing DVR prices into the app-support silo.

---

## NYC hub

### Internet / households (NYC-I)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| NYC-I1 | `New York City households without broadband internet percent Internet Master Plan mobile-only` · Firecrawl search → scrape (markdown) | https://council.nyc.gov/data/internet-access/ | NYC Council Data Team (ACS): no internet access 8.1% of households (2021); cellular data plan only 12.8%; no broadband subscription (cable, fiber, DSL) 24.5%; 19 community districts >33% without broadband; lowest: Melrose-Mott Haven-Port Morris 44% (Bronx CD01), Borough Park-Kensington 42% (Brooklyn CD12), East Harlem 41% (Manhattan CD11), Tremont-Belmont-West Farms 41%, Longwood-Hunts Point 41%, Jamaica-St. Albans-Hollis 41% (Queens CD12). By group: seniors 45%, low-income 45%. | §Hero; §5 para 2; §5.5 bullet 3; §7 cards; §9 H3 1; §13 landmarks; §Sources |
| NYC-I2 | `Big Apple Connect NYCHA free internet developments households` · Firecrawl search → scrape (query) | https://www.nyc.gov/content/oti/pages/big-apple-connect | OTI launched Big Apple Connect September 2022; free home internet for NYCHA residents via Optimum or Spectrum depending on development; free Wi-Fi in some common spaces; agreements "guaranteeing delivery of the program until 2028". | §5.5 bullet 4; §7 NYCHA card; §9 H3 2; §Sources |
| NYC-I3 | same search (excerpts) | https://www.optimum.com/program/big-apple-connect ; https://nychajournal.nyc/big-apple-connect-extended-for-three-years/ | Optimum participating list includes Melrose, Sotomayor Houses, Coney Island I (Site 1b), Low Houses, Unity Plaza; NYCHA Journal: "330,000 NYCHA residents". | §13 Coney Island card; §5.5 bullet 4 (330,000 from excerpt) |
| NYC-I4 | R9 above | — | CGNAT on 5G home internet blocks inbound port forwards. | §5 para 2 |

### News (NYC-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| NYC-N1 | `NYPD detectives request security camera footage businesses canvass…` · Firecrawl search → scrape amNY (query, directQuote) | https://www.amny.com/politics/nyc-retail-shops-cameras-nypd-pilot-sharing/ | May 16, 2024: "Connect New York" lets businesses integrate cameras with their local NYPD precinct for real-time viewing; technology "Fusus", developed by Axon; pilot in nine precincts across five boroughs; demonstration began the previous June in Flushing and College Point, Queens; businesses "can choose how and when camera footage is accessible". | §5 para 3; §5.5 bullet 6; §8.5; §9 H3 8; §13 Flushing card; §Sources |
| NYC-N2 | same search (excerpt) | https://www.police1.com/police-products/investigation/video-surveillance/nyc-initiative-allows-retail-owners-to-share-live-surveillance-footage-with-nypd-in-effort-to-curb-theft | Businesses can give unfettered access or limit cameras and hours. | Background |
| NYC-N3 | same search (excerpt) | https://www.nyclu.org/commentary/nypd-teaming-amazon-ring-new-yorkers-should-be-worried | NYCLU commentary on NYPD and Ring Neighbors. | Not used |

### Landmarks / places (NYC-L) — all from NYC-I1, NYC-I3, NYC-N1
| # | Place | Fact | Source row |
|---|---|---|---|
| L1 | Flushing and College Point, Queens | Connect New York demonstration started there (June 2023) | NYC-N1 |
| L2 | Melrose–Mott Haven–Port Morris, Bronx | 44% without broadband | NYC-I1 |
| L3 | Borough Park–Kensington, Brooklyn | 42% without broadband | NYC-I1 |
| L4 | East Harlem, Manhattan | 41% without broadband | NYC-I1 |
| L5 | Jamaica–St. Albans–Hollis, Queens | 41% without broadband | NYC-I1 |
| L6 | Coney Island Houses (Coney Island I, Site 1b), Brooklyn | on Optimum's Big Apple Connect list | NYC-I3 |
Staten Island: no sourced Super Live Plus / broadband fact found for a landmark card → EMPTY; routed by link only.

### Local Reddit / hyperlocal (NYC)
`r/AskNYC super live plus` / `r/nyc DVR app` — not searched separately (Firecrawl site:reddit search returned no NYC-specific Super Live Plus thread in R1 query) → EMPTY.

### Local licensing / rules
- NYS low-voltage licence #12000287431 (AESS, protected).
- NY Penal Law §250.05 (audio recording without consent) — carried from research/hik-connect-app-support-repair.md (nysenate.gov), not re-fetched. §8.5, §6.

### Images (11) — permanent image rule
Drive "AESS Website Photos" has no Super Live Plus folder; CompanyCam not connected. 11 copied, converted to WebP (≤1600 px, q80), renamed `super-live-plus-app-support-repair-nyc-…`:
| New file | Source file | Kind |
|---|---|---|
| …-recorder-live-view-tiles-with-date-and-time-stamp.webp | images/nvr-installation/nvr-installation-ulster-county-recorder-live-view-tiles-with-time-stamp.webp | real AESS job photo (other job) |
| …-monitor-camera-grid-and-bitrate-table-below-cable-runs.webp | images/nvr-installation/nvr-installation-bronx-recorder-monitor-camera-grid-under-cable-runs.webp | real AESS job photo |
| …-night-view-tile-of-back-room-and-open-door.webp | images/dvr-upgrade/dvr-upgrade-queens-recorder-tile-of-back-room-and-open-door.webp | real AESS job photo |
| …-dome-camera-above-wood-panel-shop-wall.webp | images/nvr-installation/nvr-installation-staten-island-dome-camera-atop-wood-panel-store-wall.webp | real AESS job photo |
| …-ceiling-turret-camera-inside-glass-entrance.webp | images/nvr-installation/nvr-installation-putnam-county-ceiling-turret-camera-above-glass-entrance.webp | real AESS job photo |
| …-ceiling-camera-beside-lit-exit-sign.webp | images/nvr-installation/nvr-installation-long-island-ceiling-camera-near-lit-exit-sign-in-office.webp | real AESS job photo |
| …-two-small-cameras-high-on-wall-below-mezzanine.webp | images/dvr-upgrade/dvr-upgrade-staten-island-small-cameras-on-high-white-wall-below-mezzanine.webp | real AESS job photo |
| …-white-dome-camera-under-water-stained-ceiling.webp | images/dvr-upgrade/dvr-upgrade-ulster-white-dome-camera-under-water-stained-ceiling.webp | real AESS job photo |
| …-blue-and-white-network-cables-across-ceiling-pipe.webp | images/dvr-upgrade/dvr-upgrade-putnam-blue-and-white-cable-bundles-above-recorder.webp | real AESS job photo |
| …-recorder-front-and-rear-port-panels-product-photo.webp | images/dvr-upgrade/dvr-upgrade-queens-recorder-front-and-rear-panel-ports-product-photo.webp | manufacturer product photo (Swann-branded) |
| …-recorder-kit-with-four-bullet-cameras-and-monitor-product-photo.webp | images/nvr-installation/nvr-installation-westchester-county-recorder-kit-with-four-bullet-cameras-and-monitor-product-photo.webp | manufacturer/retail product photo |
Rejected: images/tvt-super-live-plus-video-doorbell.avif — the photo shows an **AXIS**-logo door station, not TVT; filename is wrong (FLAG). Several sources are re-crops of scenes already used on nvr-installation / dvr-upgrade / hik-connect / smart-pss pages (same jobs).

### House practices stated without an external source (FLAG for Anwar)
- Two-hour arrival windows, 7 days to 8 PM (copied from rebuilt hik-connect/smart-pss pages' framing); "most systems back in the app in 1–2 hours of arrival" (v2.3 §5 #36 wording).
- Hand-over sheet; viewer-only user per person; DHCP reservation; export two copies; check recorder clock before export; port-forward removal; VLAN/isolation suggestions.
- Field Notes is a method note, not a story about one job.
- ADT / Ring / SimpliSafe comparison is qualitative only.

---

## QUESTION REGISTER — super-live-plus-app-support-repair-nyc (REBUILT 2026-10-18)
Sibling files on disk at build time (15 others) all carried the same old 10 questions: "Super Live Plus offline right now?", "Is Super Live Plus a camera brand?", "Why does Super Live Plus say device offline?", "Is Super Live Plus the same as SuperCam Plus or Q-See QT View?", "Why can't I see live view or playback?", "Can you recover my Super Live Plus password?", "Why aren't my push notifications working?", "Do you fix Super Live Plus systems you didn't install?", "How much does Super Live Plus repair cost?", "What areas do you cover?". None reused.

### §9 Q&A (H3)
1. We switched the shop to 5G home internet and Super Live Plus went dark the same week — what changed?
2. Can a recorder in a NYCHA apartment on Big Apple Connect, or a building on a bulk internet deal, reach Super Live Plus at all?
3. How can I tell whether our recorder was added to Super Live Plus by QR code or by an address and port number?
4. The company that installed our Super Live Plus system is gone — can a new contractor take it over without wiping it?
5. A roommate or ex-tenant still has our cameras in their Super Live Plus app — how is that access cut off for good?
6. What should a managing agent keep on file to pull footage from Super Live Plus systems in buildings across different boroughs?
7. A detective wants video from our storefront by tomorrow — how do we export it from a Super Live Plus recorder with the time stamp intact?
8. Can a shop in a Connect New York precinct share live cameras with police and still use Super Live Plus for itself?
9. Was our recorder one of the TVT NVMS-9000 boxes the 2025 Mirai botnet went after, and how do we check?
10. Is it safe to unlock a Super Live Plus recorder with a third-party "super password" generator app?
11. Our old Q-See recorder lost its app when the company shut its servers — what are our options in the city?
12. Which recorders actually work with Super Live Plus, and how do I tell from the box in the closet?
13. When is a five-borough Super Live Plus system worth fixing instead of replacing?
14. Does the FCC Covered List treat TVT-made recorders the way it treats Hikvision and Dahua?

### §17 FAQ (= FAQPage schema)
1. Which borough page should I use if the cameras are in one borough and I live in another?
2. Does Super Live Plus charge a monthly fee, and is the cloud storage option in newer versions worth it for a city store?
3. Why does the app store list the Super Live Plus developer under a name I don't recognize?
4. Can a front-desk tablet stay logged in to Super Live Plus without anyone learning the recorder's admin password?
5. What should we photograph or copy down from the recorder before calling the NYC line?
6. Can Super Live Plus show our cameras on an office Mac or a TV as well as on phones?
7. Will you work on a recorder the landlord owns if I'm the tenant who uses the app?
8. How do you test the app on a recorder that sits in a basement with no phone signal?
9. If the recorder has to be factory reset to get back in, what happens to the footage on its drive?
10. Can alerts go to the night manager's phone without every other phone on the account buzzing all night?


---

# PART B — Orange County builder

# Super Live Plus App Support Repair — Orange County (REBUILD 2026-10-18) — research part file

Page: `super-live-plus-app-support-repair-orange-county` (REBUILD in place) · up `/super-live-plus-app-support-repair-hudson-valley` · direct line (845) 640-3835 (body, CTAs, sticky bar, form JS, schema); (800) 486-0943 only in shared mega-nav header · GBP Bronx (460 E Fordham Rd, `#bronx`) · WhatsApp wa.me/17186790359 only · §9 Orange 1.40×.

**Thesis:** Orange County's internet is being re-plumbed (Greenlight fiber in Middletown, Wallkill, Port Jervis, Goshen, Walden 2025–26 and ~2,300 Washingtonville homes by end-2026; Frontier fiber in Middletown; Spectrum/Optimum/Verizon; Starlink/satellite at the farm edges; filtered phones and networks in Kiryas Joel/Palm Tree), and each change swaps the router a TVT recorder registers through — so Super Live Plus goes grey. The page is about re-registering the recorder on the new line (NAT vs address vs VPN), re-adding phones by serial/QR, filtered-phone set-ups, and outage restarts.

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. FC = mcp__Firecrawl__firecrawl_search / firecrawl_scrape. Firecrawl will not scrape reddit.com → Reddit rows are search excerpts only.

## Source matrix (§3)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts only (R1–R5). Orange-specific ISP / camera threads: FC search `site:reddit.com orangecountyNY OR hudsonvalley Optimum OR Spectrum OR Frontier internet Orange County Monroe Warwick complaint` → only Long Island / Watertown results → EMPTY for Orange. |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page; claims taken from JustAnswer, Play reviews, CCTV Camera Pros, forum excerpts. |
| 6–7 | Landmarks / building stock | rows L1–L8 (mostly carried from security-camera-maintenance / fiber / cat6 research with their URLs). |
| 8 | Bing / DDG | EMPTY (not accessible in build env). |
| 9–10 | Local news / hyperlocal | Times Herald-Record (census), Greenlight releases, Government Market News, O&R / Central Hudson releases (carried), HGAR, OC Partnership. Times Herald-Record ISP/outage items: EMPTY (none surfaced). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). |

## Silo findings used (Super Live Plus / TVT) — S
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `Super Live Plus app TVT DVR NVR device offline` · FC search → FC scrape | https://play.google.com/store/apps/details?id=com.tvt.superliveplus&hl=en_US | "professional mobile phone client software for digital video recorders and IP cameras in CCTV surveillance (compatible models only)"; developer TVT (HK) Limited (listing name Peng AnTai); 5M+ downloads; 3.3★, 53.3K reviews; updated Oct 8 2026; what's new "Support account switching"; reviews: connects then fails next day until power-cycled; app signing off from 5/10/24 fixed ~6/2/24; playback/clip crash complaint. Free. | §5 para 1; §9 family-login H3; §10.5 H3 1, 4, 5; FAQ 6; Sources |
| S2 | same search → FC scrape | https://videos.cctvcamerapros.com/support/topic/superlive-plus-mobile-app-offline | June 6 2025: app offline in Canada while NVR fine; fix Settings > Local > Domain > Global / AUTONATGLB.COM; app used with Viewtron systems. | §5 para 1; repair table row 3; §10.5 H3 6; Sources |
| S3 | `TVT Digital Technology NVR firmware "NAT" ... port 6036` · FC search → FC scrape (PDF, query mode ×2) | https://tvtdigital.com.ua/wp-content/uploads/NVR-Compilation_User_Manual_1_4_11_Version_A0-20240703.pdf | §1.2 "Supports NAT function and QR Code scanning"; §14.1.8 "Check 'Enable' and then select the NAT server address… scan the QRCode through mobile APP"; §14.1.2 HTTP 80, server port 6036; App. D 6036 "Private communication port… audio and video stream"; §14.1.6 UPnP; §14.1.4 DDNS; password reset via security questions or email — "If you forget the answers… there is no other way to restore the admin password… contact your dealer". | §5 para 2 + facts bullet 6; §6 cards; §9 installer-gone H3, 17K corporate H3; §10 methods table; §10.5 H3 2, 7; Sources |
| S4 | same → FC scrape | https://portal.hdssfl.com/portal/en/kb/articles/superlive-plus-app-how-to-add-a-nvr-dvr | Add via Settings > Device List > Manual Add (serial, user, password) or Scan Code; status grey→green. | §6 re-adding card; §9 Middletown Frontier H3; Sources |
| S5 | `TVT OEM recorders ... "SuperLive Plus"` · FC search (excerpts) | https://videos.cctvcamerapros.com/support/topic/cameras-on-phone-and-dvr-no-vms (scraped) ; https://cctvsupply.us/en-us/collections/superlive (excerpt) ; https://www.youtube.com/watch?v=9gFKAW0G0Yc (excerpt) | Viewtron VMS adds devices by serial + user/password; does not recommend static IP with DHCP; "SuperLive" NVR listings; Shield Technology AD-H265/AI-NVR troubleshooting video. | §5 para 1; §10 desktop card; FAQ 3; Sources |
| S6 | same first search (excerpts) | https://www.justanswer.com/home-security-systems/ska6a-superlive-plus-app-offline-issue.html | "check network stability and router settings. Restart the camera and app". | §10.5 H3 1 |
| S7 | `TVT DVR NVR vulnerability CVE-2024-7339 ...` · FC search (excerpts) | https://nvd.nist.gov/vuln/detail/CVE-2024-7339 ; https://github.com/advisories/GHSA-vcqx-95xm-6xh4 | TVT DVR TD-2104TS-CL, TD-2108TS-HP, Provision-ISR SH-4050A5-5L(MM), AVISION AV108T; information disclosure via /queryDevInfo. KEV status not checked → page does not claim exploitation. | §6 firmware card; §9 CVE H3; §10.5 H3 2; Sources |
| S8 | `FCC covered list TVT Digital Technology video surveillance 2025 2026` · FC search (excerpts) | https://www.fcc.gov/supplychain/coveredlist ; https://docs.fcc.gov/public/attachments/DA-26-786A1.pdf | Covered List (updated July 28 2026) names Huawei, ZTE, Hytera, Hikvision, Dahua (+ NDAA §1709 category, drones etc.); TVT not named. | §8.5 bullet 5 (worded "not among the companies named") |
| S9 | `site:reddit.com SuperLive Plus app not connecting offline DVR` · FC search (excerpts) | https://www.reddit.com/r/SecurityCamera/comments/1h3n93v/dhcp_failure/ ; https://www.reddit.com/r/IndiaTech/comments/1cbm7im/please_help_my_cctv_cameras_are_offline_after_my/ | SuperLive Plus user, app no longer green (DHCP failure); cameras offline after router change → static IP range mismatch. | Background for §9 Walden H3 (not quoted, not linked) |

## Orange County — O
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| O1 | `Greenlight Networks fiber Walden Montgomery Orange County New York expansion` · FC search → FC scrape | https://www.greenlightnetworks.com/faster-more-reliable-fiber-internet-arrives-in-walden-as-greenlight-networks-continues-orange-county-expansion-construction-underway-in-washingtonville/ | Feb 24/26 2026: Walden serviceable, final streets by end of summer; ~2,300 Washingtonville homes under construction, connect by end 2026; >$33.75M invested in Orange; already in Middletown, Town of Wallkill, Port Jervis, Goshen, Walden; >2,200 Walden households; symmetrical speeds. | Hero; §5 para 3, facts 1; town table; §9 Walden + Washingtonville H3s; Field Notes; Sources |
| O2 | same → FC scrape (query) | https://www.greenlightnetworks.com/village-of-goshen-and-middletown-expansion/ | Jan 13 2025: >1,000 Goshen, >5,000 Middletown households; active buildout in Wallkill. | §5 para 3; town table; Sources |
| O3 | `Greenlight Networks CGNAT port forwarding public IP static IP support` · FC search → FC scrape | https://www.greenlightnetworks.com/mastering-connectivity-understanding-static-ips/ ; https://www.reddit.com/r/Rochester/comments/1jkebrq/greenlight_does_not_provide_routable_external_ip/ (excerpt) | Static IP article (Dec 2023): security cameras/remote access listed as uses; request via support. Reddit title "Greenlight Does Not Provide Routable External IP Address…"; reply says NAT + charge for public IP. Orange-specific terms not seen. | §9 Goshen static-IP H3; §10.5 H3 3; Sources |
| O4 | `Orange County NY internet providers Spectrum Optimum Frontier Verizon Fios ...` · FC search (excerpts) | https://broadbandnow.com/New-York/Middletown ; https://www.broadbandsearch.net/service/new-york/newburgh ; https://frontier.com/local/new-york/middletown | Middletown: Frontier fiber 52.1%, Spectrum 90.8%, Optimum, Verizon 5G, Viasat; Newburgh: Verizon Fios, Frontier, Optimum, Spectrum. | §5 para 3; town table; Sources |
| O5 | `ConnectALL Deployment Program award "Orange County" New York locations fiber 2026` · FC search → FC scrape (query) | https://govmarketnews.com/broadband-grants-target-underserved-new-york-communities/ | Sept 30 2025: Planet Fiber NY, 16 Orange County locations, fiber, $360,000. | facts bullet 2; Sources |
| O6 | `Orange County NY broadband study unserved ... Neuhaus` / `recordonline broadband rural Orange County ...` · FC search | (results were Orange County NC/FL/CA/TX) | EMPTY for Orange County NY broadband program. | — |
| O7 | `Town of Palm Tree New York Kiryas Joel population 2020 census formed 2019` · FC search (excerpts) + carried cat6 research | https://www.recordonline.com/story/news/local/2021/08/13/census-kiryas-joel-grew-leads-orange-population/8115187002/ ; https://en.wikipedia.org/wiki/Palm_Tree,_New_York | 32,954 (2020), +63%, largest municipality; Palm Tree created Jan 1 2019, coterminous; >3,500 condos built/planned; families moving to Blooming Grove, Woodbury, Monroe. | §5 para 4, facts 3; §7 cards; Sources |
| O8 | `Kiryas Joel filtered internet Jnet TAG filter security camera app blocked` · FC search → FC scrape (query) | https://koshersignal.com/blogs/articles/kosher-web-filter-guide | Whitelist-only "approved-apps-only setup where only specific apps… can connect to the internet"; DNS-level vs device-level filtering, strongest use both. | §5 para 4; §6 card; §9 filtered-plan H3s; Sources |
| O9 | `"Kiryas Joel" smartphones internet filter kosher phone rules` · FC search (excerpts) | https://www.reddit.com/r/Judaism/comments/1kq8esa/kasher_phones/ ; https://www.jta.org/2015/08/05/united-states/hasidic-village-makes-parents-choose-childrens-education-or-smartphone | "In Kiryas Joel they sell flip phones that are voice and text only"; 2015 KJ notice restricting parents' smartphone use. | §9 flip-phone H3; Sources (JTA linked as context only) |
| O10 | `Starlink router port forwarding not supported CGNAT support article` · FC search (excerpts) | https://www.reddit.com/r/Starlink/comments/1p8xkgy/starlink_and_port_forwarding_question/ ; https://www.purevpn.com/blog/starlink-cgnat-port-forwarding/ | Residential plan "doesn't support real port forwarding because you're behind CGNAT"; Starlink router has no port-forwarding rules. | §5 para 4; §9 Pine Island H3; §10.5 H3 2; Sources |
| O11 | carried (security-camera-maintenance research P1, P3) | https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k ; https://www.cenhud.com/en/news/2026/central-hudson-restoration-efforts-continue/ | >47,000 O&R customers affected Jul 1–6 2026; Jul 6 5pm Warwick 192 / Goshen 87 out; Sep 27 2026 ~6,000 Central Hudson still out at 9am, greatest impacts in Ulster and Orange. | §5 para 4, facts 4; §9 outage + battery H3s; Sources |
| O12 | carried (maintenance B1, B2, B3; fiber research Stewart; cat6 research) | hgar.com Walmart (Jul 2026); ocpartnership Stewart Logistics Center; en.wikipedia Stewart International Airport (1,552 acres, Port Authority 2007, 105th Airlift Wing); en.wikipedia Woodbury Common (1985, ~220 stores); en.wikipedia East End HD (>2,200 bldgs); ediblehudsonvalley (26,000 acres Black Dirt); pineislandny (ditches, farm roads); USDA 2022 (613 farms, 65,706 acres); riveralerts Port Jervis (21.47 ft 6/28/2006; 18 ft drains back up Railroad Ave–Water St) | as stated | §5 facts 5; §7; §8 cards; §13 landmarks; Sources |
| O13 | carried (maintenance R1, R2) | https://www.orangecountyny.gov/1279/Video-Camera-Community-Partnership-Progr ; Penal Law 250; 9 NYCRR 125.3; OC electrician application; Middletown ELB; Poughkeepsie Journal Apr 2025 (Newburgh dispensaries, excerpt) | DA program text (metadata/excerpt only); rules as stated. | §8.5; §9 DA H3; Sources |

## Pricing (no invented prices)
- Old Orange Super Live Plus page visible prices: only "$0 Diagnosis by Phone" (stats bar). JS chip widget ($250 service call, $175/drop, $19.99/mo…) is a shared widget on ~1,500 pages — NOT carried (same decision as dvr-upgrade research §1.8).
- Used: $0 phone/screenshot diagnosis (old-page statement); $195/hr, 3-hr minimum ($585) protected service rate, unmultiplied; recorder replacement = DVR Upgrade silo base (research/dvr-upgrade.md §1.8: 450–700 / 650–1,000 / 800–1,200 / 1,200–2,200 / 2,200+) × Orange 1.40 → **$630–$980, $910–$1,400, $1,120–$1,680, $1,680–$3,080, $3,080+** (same borrowing as hik-connect-manhattan ×1.25 and smart-pss-ulster ×1.53). **FLAG: borrowed from DVR Upgrade silo — confirm.**

## Images (11) — permanent image rule (Drive has no Super Live Plus folder; CompanyCam not connected)
Each viewed (contact sheet + full-size for two); converted with Pillow to WebP q80 (none >1600px). Excluded: store-monitor grids with tiny people (lorex brooklyn / dvr-upgrade brooklyn), Lorex-badged NVR (wrong brand implication), duplicate fascia/mural framing.
| New file (images/super-live-plus-app-support-repair/) | Source | Kind |
|---|---|---|
| …-orange-county-dome-camera-under-eave-with-bare-winter-branches.webp (hero, eager) | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-dome-camera-under-eave-against-bare-winter-trees.webp | real job photo |
| …-two-cameras-on-yellow-fascia-corner-against-sky.webp | images/lorex-camera-installation/lorex-camera-installation-long-island-two-cameras-on-yellow-fascia-corner-against-sky.webp | real (same building as hero, different framing) |
| …-dome-camera-on-long-wall-arm-beside-stone-facade.webp | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-dome-camera-on-long-wall-arm-over-stone-facade.webp | real |
| …-recorder-screen-per-channel-bitrate-table.webp | images/lorex-camera-installation/lorex-camera-installation-brooklyn-recorder-screen-per-channel-bitrate-readings.webp | real (screen) |
| …-loose-network-cables-crossing-ceiling-beam.webp | images/lorex-camera-installation/lorex-camera-installation-long-island-loose-blue-and-white-network-cables-crossing-ceiling-beam.webp | real |
| …-small-black-camera-and-wall-sensor-on-pale-wall.webp | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-small-black-camera-and-sensor-on-pale-wall.webp | real |
| …-wifi-pan-tilt-camera-with-two-antennas-product-photo.webp | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-lorex-wifi-pan-tilt-camera-with-two-antennas-product-photo.webp | manufacturer (Lorex; caption says not a Super Live Plus device) |
| …-solar-cellular-ptz-camera-with-sim-card-product-photo.webp | images/dvr-upgrade/dvr-upgrade-putnam-solar-panel-cellular-ptz-camera-with-sim-card-product-photo.webp | manufacturer |
| …-black-recorder-with-red-status-lights-product-photo.webp | images/dvr-upgrade/dvr-upgrade-nassau-county-black-recorder-with-red-status-lights-product-photo.webp | product (not identified as TVT) |
| …-white-floodlight-camera-with-twin-lamps-product-photo.webp | images/dvr-upgrade/dvr-upgrade-putnam-white-floodlight-camera-with-twin-lamps-product-photo.webp | manufacturer |
| …-large-vented-rack-recorder-product-photo.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-large-rack-recorder-with-vented-front-product-photo.webp | product (not identified as TVT) |
DAILY-LOG note: `images: 11 reused from images/lorex-camera-installation/ (7) + images/dvr-upgrade/ (4) (6 real AESS job photos from other jobs + 5 product shots) (no real Super Live Plus photos yet)`.

## Keywords (Orange geo layer)
Super Live Plus app support Orange County; SuperLive Plus offline Middletown / Newburgh / Goshen / Walden / Washingtonville / Port Jervis / Warwick / Monroe / Kiryas Joel; TVT DVR NVR remote viewing; NAT server; port 6036; re-register recorder after Greenlight / Frontier / Spectrum / Optimum switch; Starlink CGNAT; filtered phone camera app; O&R / Central Hudson outage restart; CVE-2024-7339. All 11 alts carry "Super Live Plus … Orange County".

## Question register — super-live-plus-app-support-repair-orange-county (REBUILT 2026-10-18)
### §9 Q&A (H3)
1. Greenlight connected our Walden house last week, and the recorder's network page still lists the old router as its gateway — is that why Super Live Plus went grey?
2. When Greenlight's crew connects our Washingtonville home, will their installer put the camera recorder back online too?
3. Our Middletown shop had port forwarding on the old cable router for the recorder — does that need recreating on the new Frontier router?
4. Greenlight sells a static IP as an extra — does a Goshen homeowner need to pay for one just to watch cameras?
5. Our Pine Island farm runs on Starlink — can Super Live Plus reach a TVT recorder with no way to forward a port?
6. There's a solar-powered cellular camera out on the far field — can it appear in the same Super Live Plus list as the barn recorder?
7. How much upload does a four-camera barn recorder in Warwick need before the live view stops buffering?
8. Our phones are on a filtered plan — why does the filter let us install Super Live Plus but the cameras never load?
9. Can a store in Palm Tree put the cameras on a manager's filtered phone without opening anything else on that phone?
10. The owner carries a flip phone with no apps at all — how else can the shop's cameras warn him?
11. Our Cornwall house has a standby generator, yet Super Live Plus still drops for several minutes every time the power fails — what is restarting?
12. Should the modem and the recorder in a Montgomery warehouse office share one battery backup, or have separate ones?
13. My parents in New Windsor and I in Florida, NY both need to watch their recorder — should we share one login?
14. Several managers open the Central Valley store's cameras at once on a busy outlet weekend — can that many phones overload the recorder or the line?
15. Is our TVT-made DVR one of the models in the 2024 information-disclosure record, and what should we do if it is?
16. We bought a house in Chester that came with a recorder in the basement and nobody knows its password — should we keep it or start over?
17. If we sign up for the District Attorney's Video Camera Community Partnership, does the county get a login to our app?
18. Our distribution building off Route 17K is on a corporate network — what exactly does the recorder need the IT department to allow?
### §17 FAQ (= FAQPage)
1. Is a visit to Greenwood Lake or Port Jervis priced the same as one in Newburgh?
2. Can the whole repair be done over the phone if someone is standing at the recorder?
3. Can you put in a wireless bridge so the barn's cameras reach the farmhouse recorder?
4. Will you work on a recorder that was bought online and put in by the owner?
5. Can visits in Kiryas Joel and Monroe be scheduled around Shabbat and Yom Tov?
6. Will you also look at the doorbell camera or alarm panel while you are there?
7. If we delete the app from a phone, is any recorded video lost?
8. Do you leave a written record of what you changed on the recorder and the router?
9. Does someone have to be home while you work?
10. Can a technician come in the evening, after farm chores or once a shop has closed?
De-dup: none of the 10 old-template stock intents used (brand?, why offline, SuperCam/QT View, live view/playback, password recovery, push notifications, systems you didn't install, cost, areas). Checked mechanically (check_page) against all 15 siblings on disk incl. rebuilt nyc (13:04) and putnam (13:07+). Replaced by meaning after reading the nyc/putnam rebuilds: provider-switch 'what to write down' (≈ nyc 'what to photograph'), Wi-Fi-vs-cellular (≈ putnam Kent), outage 'didn't reconnect' (≈ putnam NYSEG), commute playback data (≈ putnam train buffering), installer gone (≈ nyc), FAQ desktop/TV (≈ nyc Mac/TV), monthly fee (≈ nyc, putnam), tablet screen (≈ putnam), visit length (exact dup putnam). Overlap risk by meaning with concurrent builds: travel-abroad domain fix appears only in §10.5 (H3 heading is a quoted claim, no "?"); "installer gone" ≈ "systems you didn't install" partially — framed as password/ownership takeover.

## FLAGS
1. Borrowed prices: recorder replacement from DVR Upgrade silo base × 1.40 — confirm.
2. Unsourced house practices: re-registration method (reservation, gateway/DNS, NAT check), sub-stream for remote view, no UPnP, written filter-provider note, separate accounts, outage pull-the-plug test, off-site check, one-page hand-over, Shabbat/Yom Tov scheduling, no mileage charge (area rate covers travel — confirm), "most back within 1–2 hours of arrival" (element 36 wording), "a large share of our Orange calls start with 'since the new internet'" (house observation), "Many TVT-based recorders have an email alarm setting" (not verified in the manual scrape), playback uses main stream vs live sub-stream (general); generator transfer gap and router-boots-slower-than-recorder (general); recorders cap simultaneous remote streams by model (general); wireless-bridge practice.
3. Descriptive geography without a fetched source: Forest Road / Route 17M (KJ shops), Route 17M Middletown, Route 32 Central Valley, Route 9W Newburgh/Cornwall strip shops, "Warwick orchards", hamlet list in "we also serve", Deerpark/Greenwood Lake satellite use (general, not sourced), county courts/offices in Goshen.
4. Greenlight CGNAT/public-IP statement rests on a Rochester Reddit excerpt; Orange terms not seen (page says so).
5. Filtered-phone content is general (KosherSignal guide, Reddit excerpt); no KJ-specific filter-provider policy on camera apps found.
6. DA program page body did not render (metadata/excerpt only); page says so.
7. TVT "not named on the FCC Covered List" from list excerpt (July 28 2026 update); NDAA §1709 category not analysed.
8. CVE-2024-7339 KEV/exploitation status not checked; page claims only what the NVD excerpt says.
9. Images: hero and fascia photo are the same building (different framing); 2 recorder product shots not identified as TVT (captions say so).
10. Field Notes is a method note, not a job story.
11. The `slp/` scratch folder was shared with the Putnam builder (file clobbering); this page was rebuilt from `orange-slp-q7/` — content verified Orange-only.

## Final state
check_page --no-registration: all content checks pass; 12 remaining FAILs are 'live sibling … doesn't link back' (main-run wiring). 13,887 rendered words; 195,788 B (nyc 180,989, putnam 190,711 at 13:1x — re-check after bronx/manhattan/long-island rebuilds land). Masked-geo difflib vs siblings: page ≤0.177 (putnam), paragraphs at 1.00 only NAP/warranty boilerplate.


---

# PART C — Putnam County builder

# Super Live Plus App Support & Repair — Putnam County (part file for merge into research/super-live-plus-app-support-repair.md)

Page: `super-live-plus-app-support-repair-putnam-county` — REBUILD in place, 2026-10-18 (was crawled-not-indexed). Queue line: `REBUILD | super-live-plus-app-support-repair-putnam-county | Super Live Plus App Support Repair | Putnam | up /super-live-plus-app-support-repair-hudson-valley | (845) 640-3835 | GBP Bronx`.
Direct line (845) 640-3835 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav header. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). WhatsApp only as wa.me/17186790359 (+ footer text). Structure, CSS, nav chrome, forms and scripts copied from the rebuilt `smart-pss-support-setup-ulster-county.html`; every visible sentence written new. Nothing from the old template text, FAQ, prices or images reused.
Tools: Firecrawl search / scrape (`mcp__Firecrawl__*`, incl. Alexandria apps-apple-com and nvd-nist-gov). Shell curl not used. Reddit cannot be scraped by Firecrawl ("we do not support this site") → excerpts only. "Carried" = fetched by an earlier run in another research file (file + row named), not re-fetched.

**Thesis:** In Putnam, Super Live Plus is used mostly by people who are not at the recorder — commuters (39.3-min mean commute), owners of the 1,757 seasonal/lake houses, short-term-rental owners whose town requires a local manager within 30 miles (Putnam Valley) or a 20-minute responder (Philipstown draft) — and the path from recorder to phone crosses the county's weakest links (hills that block cell signal: "We do not have 254 square miles of coverage"; fiber still being built to 390 locations; town-wide NYSEG/Central Hudson outages). So Putnam support = rebuild the whole recorder-to-phone chain for distance: outage-proof recovery, one secure remote path (NAT/VPN, not open ports — TVT botnet/CVE), separate limited logins for nearby caretakers/managers, and testing from where the owner will actually be. (Distinct from orange-county = Greenlight fiber/Starlink/filtered phones; nyc = buildings/landlords/5G home internet.)

## 1. Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Putnam-specific Super Live Plus threads: EMPTY. Generic SLP excerpt (r/SecurityCamera DHCP failure) seen as search excerpt only (Firecrawl refuses reddit.com) → not used on page. r/hudsonvalley second-home thread carried (U3). |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on-page and tests 7 recurring claims. |
| 6 | Landmarks | carried L1–L6 (dvr-upgrade.md Putnam) + MTA Southeast station (new). |
| 7 | Use cases / building stock | carried H1–H4; property-type cards are general descriptions (FLAG). |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env). |
| 9 | Local news | Highlands Current, Westfair, News 12 HV, lohud, Mid-Hudson News, Mahopac News, Daily Voice, WAMC (new + carried). |
| 10 | Hyperlocal | Highlands Current (new x3), Mahopac News (carried), Town of Putnam Valley (carried). Optimum/Altice outage news for Putnam: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). Substitute: App Store 1–2★ reviews of the app (A2). |
| — | Drive / CompanyCam | No Super Live Plus Drive folder (per brief); CompanyCam not connected → permanent image rule. |

## 2. Silo findings used (Super Live Plus app — reusable on any SLP page)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| A1 | Alexandria `apps-apple-com` apps/app, app_id 1058758642, country us · Firecrawl scrape | https://apps.apple.com/us/app/superlive-plus/id1058758642 | Name SuperLive Plus; seller/developer "Peng AnTai" (id 444058257), bundle com.pengantai.superliveplus; support_url http://en.tvt.net.cn; released 2016-02-22; current 1.16.7 (2026-01-05, "Several identified bugs have been resolved"); price $0, no in-app purchases; rating 3.9 from 15,849 (histogram 1★ 2,643 · 2★ 1,035 · 3★ 1,292 · 4★ 1,626 · 5★ 9,253); requires iOS/iPadOS 12.1+, Mac with M1+ (macOS 12), visionOS. Version notes: 1.11.1 (2022-10-29) doorbell function; 1.12.0 (2023-03-15) DVR cloud storage, intercom + door-open under doorbell channel, login offline mode; 1.12.1 (2023-06-15) CallKit for doorbell; 1.13.0 (2023-09-24) Push 2.0 thumbnails; 1.14.0 (2024-05-10) doorbell time zone + DST, IR/LED config, SD-card download; 1.14.4 (2024-08-20) "Fixed the issue: Playback of DVR 3.0 speeds up"; 1.15.0 (2024-11-08) device sharing optimized, lighting modes, full-duplex intercom; 1.16.0 (2025-04-25) sharing, device upgrade process, push config, SD card config on IPC. | Hero sub; §5 para 2; §5.5 bullet 6; §10 cards; §9 clock Q, dock-audio Q, manager Q; §10.5 claims 4–5, 7; FAQ 1, 2, 8, 9; Sources |
| A2 | Alexandria `apps-apple-com` apps/reviews, app_id 1058758642 · Firecrawl scrape | same | Reviews used: 2026-04-03 (2★, condo manager: properties disappear from app, playback won't load, police footage request took almost all day, dragging time bar lands too early/late, app switches to other property); 2025-04-06 (1★: cameras offline on mobile app but working on home monitor; after latest update unable to view past recordings); 2024-05-09 (2★: "constantly going off" on bugs/bush/leaf, person not always detected); 2020-03-28 (4★: hard to find a time); 2019-11-29 (1★: told to erase/delete account and start again). | §5 para 2; Town (Patterson); §9 Lake Casse Q; §10.5 claims 2, 5, 7; FAQ 3, 9 |
| A3 | `"SuperLive Plus" Google Play com.tvt.superliveplus` · Firecrawl search (excerpt) | https://play.google.com/store/apps/details?id=com.tvt.superliveplus | Excerpt: "Rating 3.3 (53,299) · Free · Android"; package com.tvt.superliveplus. | §5 para 2; FAQ 2; Sources (labelled excerpt) |
| A4 | `TVT NVR default port 6036 SuperLive Plus port forwarding server address` · Firecrawl search → scrape PDF (query, directQuote) | https://www.mysecuresystems.com/wp-content/uploads/SuperLivePlus-User-Manual.pdf | SuperLive Plus V1.0 manual: LAN access by IP+port or QR; WAN by static IP / DDNS / forwarded ports or UPnP; "If the device and the mobile client are in the different network segment, the device shall support QRCODE and enable the NAT"; live-view "speed-up function … more fluent video"; custom bitrate/frame rate; audio alarm and shake alarm on video loss/sensor/motion; reserved disk space 50–500 MB. | §9 Kent Q, Brewster Q, Patterson Q; §10 table; Sources |
| A5 | same search (excerpt) | https://tvtdigital.com.ua/wp-content/uploads/NVR-NV9000-_User_Manual.pdf | TVT NVR manual: "the default server port of the NVR is 6036"; HTTP port 80. (Also TVT India quick guide excerpt, same defaults.) | §10 table; Sources (excerpt) |
| A6 | `"Super Live Plus" app DVR NVR remote viewing developer` · Firecrawl search → scrape (query) | https://techson-cctv.com/en/solutions-recorder-features | Techson (TVT-platform brand): add recorder to Super Live Plus on AutoNAT by QR code; security code to link to account; optional dynamic code; AutoNAT 2 servers from firmware 1.4.4; AutoDDNS requires router ports opened; push notification schedule set on DVR. | §6 cards; §10 table; Sources |
| A7 | `SuperLive Plus app offline … fix` · Firecrawl search → scrape (query) | https://videos.cctvcamerapros.com/support/topic/superlive-plus-mobile-app-offline | June 6, 2025: SuperLive Plus is the app for Viewtron DVRs/NVRs/IP cameras; customer in Canada saw OFFLINE; fix Settings > Local > Domain > GLOBAL/AUTONATGLB.COM. | §5 para 2 (Viewtron); Sources |
| S1 | `GreyNoise TVT NVMS9000 DVR exploitation surge 2025 CVE-2024-7339 Mirai` · Firecrawl search (full excerpt) | https://www.greynoise.io/blog/surge-exploitation-attempts-tvt-dvrs | April 7, 2025: 3× spike in exploitation attempts against TVT NVMS9000 DVRs, peak >2,500 unique IPs on April 3, >6,600 IPs in 30 days; overlap with Mirai; most targets US, UK, Germany; info-disclosure flaw can give admin control. | §9 Southeast port-forward Q; §10.5 claim 3; Sources |
| S2 | Alexandria `nvd-nist-gov` vulnerabilities/cve CVE-2024-14007 | https://nvd.nist.gov/vuln/detail/CVE-2024-14007 | Published 2025-11-24: TVT NVMS-9000 firmware "(used by many white-labeled DVR/NVR/IPC products)" before 1.3.4, auth bypass on control port, discloses admin usernames/passwords in cleartext; CVSS 4.0 8.7 High; in_kev false (page does NOT claim CISA KEV). | §9 Southeast Q; §10.5 claim 3; Sources |
| S3 | same, CVE-2024-7339 | https://nvd.nist.gov/vuln/detail/CVE-2024-7339 | Published 2024-08-01: TVT DVR TD-2104TS-CL, TD-2108TS-HP (+ Provision-ISR, AVISION) info disclosure /queryDevInfo; vendor did not respond; in_kev false. | Sources only |
| Q1 | `Q-See shut down app replacement "Super Live Plus" OR "SuperLive Plus" QT View` · Firecrawl search → scrape (query) | https://ipcamtalk.com/threads/q-see-closing-doors-jan-31st-2021-no-more-remote-viewing-options-to-fix.54091/ ; https://www.cctvcameraworld.com/replace-q-see-security-cameras-system/ | Q-See closed Jan 31, 2021; its P2P sharing/remote viewing stopped; Q-See recommended DMZ; Q-See sourced from several manufacturers. NO source found tying Q-See to SuperLive Plus/TVT → page does not claim it (the old template's "same app that replaced Q-See QT View" claim dropped). | §10.5 claim 4; Sources |

## 3. `## Putnam County` — local research
### New this run (Firecrawl, 2026-10-18)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| P1 | `Highlands Current cell tower Philipstown coverage gap Garrison Homeland Towers` · Firecrawl search → scrape (query, directQuote) | https://highlandscurrent.org/2016/05/27/new-towers-improve-ems-cell-service-putnam-county/ | May 27, 2016: Legislator Scuccimarra: "Cold Spring is notorious for having blackout spots"; Homeland Towers recently erected three structures in Kent; Walker: "We do not have 254 square miles of coverage." | Hero sub; §5 para 3; §5.5 bullet 3; Town (Kent); §9 Kent Q; §10.5 claim 1; Sources |
| P2 | same search → scrape (query) | https://westfaironline.com/construction/verizon-sues-philipstown-for-permits-to-build-new-cell-tower/ | Mar 7, 2018 (Bill Heltzel): Verizon suit, District Court White Plains; 120-ft tower at McKeels Corners "where the topography obstructs the signal"; relocate to 50 Vineyard Road, 180-ft pole; meta: "spotty wireless … 9,600 inhabitants" of Philipstown. | §5 para 3; Town (Philipstown); §9 Garrison bridge Q; §10.5 claim 1; Sources |
| P3 | `Putnam County New York residents commute mean travel time …` · Firecrawl search (excerpt) | https://fred.stlouisfed.org/series/B080ACS036079 | Mean commuting time, Putnam County 2024 (ACS 5-yr): 39.25 min (QuickFacts carried H2: 39.3). | §5 para 1; §5.5 bullet 1; Sources |
| P4 | same search (excerpt) | https://www.mta.info/stations/southeast | Metro-North Southeast station page. | Town (Southeast); Sources |
| P5 | `Optimum OR Altice internet outage Putnam County Carmel Mahopac 2026` · Firecrawl search (past year) → scrape (query) | https://hudsonvalley.news12.com/2026/04/23/police-crack-down-on-reckless-after-hours-driving-at-putnam-county-shopping-center/4DFlUzd5vGe9JVPyeF3dut | Apr 23, 2026: Mahopac Village Shopping Center, Route 6, Carmel; speeding/burnouts after stores close; Apr 17 detail (Chief Anthony Hoffmann): 3 reckless-driving arrests, 3 impounds, 22 summonses; gun menacing two nights earlier. (ISP outage news itself: EMPTY.) | §8 Route 6 card; Sources |
| P6 | `Putnam Valley OR Kent OR Carmel OR Philipstown short-term rental law permit Airbnb 2025 2026` · Firecrawl search → scrape (query) | https://highlandscurrent.org/2025/11/07/philipstown-debuts-str-law/ | Nov 7, 2025: Philipstown draft STR law introduced Oct 29; one-year permits; owner or agent able to respond within 20 minutes; guests given written statement of exits, extinguishers, emergency contacts; $500,000 liability insurance. | Town (Philipstown); §8.5 STR bullet; §9 guests Q; Sources |
| P7 | `Town of Putnam Valley short-term rental law "30 miles" operator manager code` · Firecrawl search (excerpts) | https://ecode360.com/9475947 ; https://highlandscurrent.org/2023/12/01/putnam-valley-adopts-short-term-rental-law/ | Putnam Valley Code Art. X (excerpt): "The local manager must reside within 30 miles of the Town of Putnam Valley Town Hall"; Highlands Current Dec 1, 2023 (excerpt): law adopted; single-family homes; local manager within 30 miles. (Third-party blogs' "respond within one hour" NOT used.) | Hero badge context; Town (Putnam Valley); §8.5 bullet; §9 manager Q; Sources |
| P8 | `Putnam County broadband ConnectALL unserved locations fiber 2026 Comcast Optimum Putnam` · Firecrawl search (excerpt) | https://www.governor.ny.gov/news/governor-hochul-announces-broadband-projects-totaling-more-636-million-achieve-universal | "$11,498,589 to Comcast … with a $5,033,776 match to serve 390 locations in Putnam County with fiber optic technology" (also carried B1). | §5 para 3; §5.5 bullet 4; §10.5 claim 6; Sources |
| P9 | `Putnam County NY cell phone dead zones cellular coverage 2025 OR 2026 …` · Firecrawl search | (CoverageMap, Facebook group, BroadbandNow excerpts) | No citable 2025–26 Putnam dead-zone report → EMPTY; 2015/2016/2018 sources used instead. BroadbandNow Putnam Valley figures inconsistent between excerpts (93.6% vs 46% cable) → not used. | — |

### Carried rows used (not re-fetched)
| ID | From | URL | Finding | Used |
|---|---|---|---|---|
| H1 | dvr-upgrade.md H1 | putnamcountyny.gov … Section-4-County-Profile-021815.pdf | >240 sq mi; 6 towns 3 villages; forest 66.9%; Hudson Highlands bedrock; commerce along Routes 6, 9, 22, 52, I-84. | §5 para 3 ("about two-thirds forest"); §8 intro |
| H2 | dvr-upgrade.md H2 | census.gov/quickfacts/putnamcountynewyork | 38,713 housing units; mean travel time 39.3 min; broadband subscription 94.8%. | §5 para 1; §5.5; §10.5 claim 6 |
| H3 | dvr-upgrade.md H3 | api.census.gov ACS B25004 | 1,757 seasonal/recreational/occasional units. | §5 para 1; §5.5 |
| H4 | dvr-upgrade.md H4 | historicpatterson.org ExhPutLake | Smadbeck lake colonies from 1928 (Lake Carmel, Lake Peekskill, Putnam Lake); 11,000 lots 20×100 ft at Putnam Lake. | §5 para 1; §5.5; Town (Patterson); §7 card |
| N4 | dvr-upgrade.md N4 | dailyvoice.com Isaias | Aug 5, 2020: NYSEG 34,150/38,693; Carmel 12,717, Kent 5,815; Central Hudson 3,621/5,160 (Philipstown 2,475, Cold Spring 992). | §5 para 4; §5.5; Town (Carmel, Kent); §9 generator Q |
| W3 | dvr-upgrade.md W3 | wamc.org 2021-03-11 | NYSEG circuit upgrades Horsepound/Stebbins roads, Carmel, rock drilling. | Town (Carmel) |
| W4 | dvr-upgrade.md W4 | putnamvalley.gov SoE July 29 2026 | Flash-flood emergency; Cimarron, Horton Hollow, Canopus Hollow. | §5 para 4; Town (Putnam Valley) |
| P-W4 | security-camera-maintenance.md P-W4 | lohud 2026-07-05 | July 4, 2026 storms through Westchester and Putnam; thousands without power (excerpt "3,670" NOT used as a number). | §5 para 4; Sources |
| P-W5 | security-camera-maintenance.md P-W5 | lohud 2026-08-03 | 740 Central Hudson customers, Cold Spring/Garrison. | §5 para 4; Sources |
| P-W3/P-W6 | security-camera-maintenance.md | NYSEG Patterson outage page; cenhud.com/en/outages | NYSEG town outage lists; Central Hudson text STAT/OUT to 236483. | Repair box check 3; §9 Patterson Q; Sources |
| P-I2 | security-camera-maintenance.md P-I2 | County Exec letter Aug 27, 2025 (SLF) | SLF taken root in Putnam; asks about reducing egg masses in the Great Swamp, Patterson. | Town (Patterson); Sources |
| P-C1 | security-camera-maintenance.md P-C1 | Mahopac News Jul 23, 2026 | Sheriff Hess: courthouse cameras captured portions only, system relies on motion sensors. | §9 motion-only Q; §10.5 claim 5; Sources |
| N1 | floodlight N1 | Mahopac News Aug 7, 2026 | 7 vehicles, ~3:37–5:05 a.m. Aug 5; Lake Casse, Lake Drive, Ridge Road; residents asked to check footage. | Town (Carmel); §9 Lake Casse Q |
| M1 | nvr-installation.md M1 | midhudsonnews.com 2026/09/10 | Sheriff: 22 vehicles linked to organized retail-theft rings that travel to Putnam to steal from local stores. | Town (Southeast); §8 Route 22 card |
| B2 | dvr-upgrade.md B2 | highlandscurrent.org 2023/05/05 | Optimum fiber through Philipstown; Verizon reviewing Cold Spring. | Town (Philipstown); §10.5 claim 6 |
| N1-dz | dvr-upgrade.md N1 | schumer.senate.gov Oct 5, 2015 | More dead zones in northern Westchester and Putnam than carriers' maps show. | §10.5 claim 1; Sources |
| U3 | dvr-upgrade.md U3 | reddit r/hudsonvalley 1ww3ifc (Oct 2026) | Second-home owners: caretakers weekly; neighbour with cameras, battery backup, cellular fallback. | §5 para 1; Sources |
| E1/E2 | floodlight E1/E2 | ecode360.com/6607815; putnamcountyny.gov/consumer-affairs | Ch. 145 covers low-voltage/limited data comms incl. video surveillance; no unlicensed trade; license lists. | §8.5 bullet; §9 Ch. 145 Q |
| R4 | dvr-upgrade.md R4 | coldspringny.gov Certificate of Appropriateness | HDRB approval for visible exterior changes; not visible = not reviewed. | §7 card; §8.5 |
| L1–L6, L8b | dvr-upgrade.md / floodlight | Wikipedia Mahopac, Courthouse, Cold Spring HD, Putnam County; NYC DEP West Branch; Legislature Tilly Foster; NYS Parks Fahnestock | as in source rows | §13 cards + hamlet list; schema areaServed |
| G1/G3/G4 | silo (dvr-upgrade.md §1.6) | §52-a; Penal Law 250.05; NYS Commercial Security Tax Credit | as silo | §8.5 bullets; §9 dock-audio Q |

## 4. Pricing used (no invented prices)
The 16 old Super Live Plus pages publish no SLP prices (only "$0 Diagnosis by Phone"; other $ figures are shared mega-nav JS chips). Following the rebuilt Hik-Connect/SmartPSS pages: $0 phone/screenshot triage; protected rate $195/hr, 3-hr minimum ($585), not multiplied; recorder replacement = DVR Upgrade silo base (research/dvr-upgrade.md §1.8: 4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+) × Putnam 1.45 (blueprint §9), round half-up → **$653–$1,015; $943–$1,450; $1,160–$1,740; $1,740–$3,190; $3,190+**. Schema OfferCatalog uses the same.
**FLAG (borrowed + conflict):** prices borrowed from the DVR Upgrade silo (as hik-connect/smart-pss rebuilds did). `dvr-upgrade-putnam.html` itself publishes the UN-multiplied base ($450–$700 … $2,200+) for Putnam, while this page applies §9 1.45× — Anwar to confirm which is right.

## 5. Images (11) — permanent image rule
Drive has no Super Live Plus folder; CompanyCam not connected. All candidates viewed (contact sheets + full size). Chosen to avoid scenes the concurrent NYC/Orange SLP builders used (swapped out: monitor grid under cable trays, recorder kit with four bullets, back-storeroom night tile, live-view tiles with time stamp, bitrate table crop, dome under eave/winter sky, black bullet + sensor on grey wall, stained-ceiling corner dome, corridor-scene duplicate). WebP q80, ≤1600 px. No faces (store-grid people are tiny overhead figures, one tile blurred in source), plates, house numbers or readable documents. Captions say "Real AESS job photo from another site, not a Putnam property" or "Manufacturer(-style) product photo".
| images/super-live-plus-app-support-repair/super-live-plus-app-support-repair-putnam-county-… | Source | Placement |
|---|---|---|
| store-monitor-with-aisle-and-counter-camera-tiles.webp | images/nvr-installation/nvr-installation-bronx-store-monitor-aisle-camera-grid.webp (real) | Hero |
| playback-frame-of-paved-lot-beside-brick-wall.webp | images/nvr-installation/nvr-installation-bronx-recorder-playback-brick-wall-to-lot.webp (real) | §5 |
| wide-angle-camera-tile-of-pavement-and-curb.webp | images/residential-security-camera-installation/…-nassau-county-wide-lens-recorder-tile-of-sidewalk-and-curb.webp (real) | Town by town |
| recorder-with-four-turret-cameras-product-photo.webp | images/nvr-installation/nvr-installation-westchester-county-recorder-with-four-turret-cameras-product-photo.webp (product) | §6 |
| bullet-and-dome-cameras-at-two-heights-on-blue-wall.webp | images/nvr-installation/nvr-installation-hudson-valley-bullet-and-dome-at-two-heights.webp (real) | §7 |
| small-dome-camera-between-light-panels-on-drop-ceiling.webp | images/nvr-installation/nvr-installation-staten-island-dome-camera-beside-track-lights-on-drop-ceiling.webp (real) | §8 |
| eyeball-dome-camera-in-corner-above-wall-sensor.webp | images/nvr-installation/nvr-installation-hudson-valley-eyeball-dome-in-corner-above-wall-sensor.webp (real) | §9 (outage cluster) |
| slim-black-recorder-with-front-usb-port-product-photo.webp | images/nvr-installation/nvr-installation-ulster-county-avycon-sixteen-channel-recorder-product-photo.webp (product; caption does not claim brand/TVT) | §10 |
| black-dome-camera-at-ceiling-edge-above-white-wall.webp | images/nvr-installation/nvr-installation-westchester-county-black-dome-camera-on-drop-ceiling-above-tall-white-wall.webp (real) | §13 |
| patch-cable-bundles-down-equipment-rack.webp | images/nvr-installation/nvr-installation-staten-island-patch-cable-bundles-down-equipment-rack.webp (real) | §14 |
| bullet-camera-aimed-down-corridor-at-grey-door.webp | images/nvr-installation/nvr-installation-bronx-bullet-camera-down-corridor-to-door.webp (real) | §15 |
DAILY-LOG note: `images: 11 reused from images/nvr-installation/ (10) and images/residential-security-camera-installation/ (1) (no real Super Live Plus photos yet)`.

## 6. Keywords (Putnam geo layer)
Super Live Plus Putnam County; SuperLive Plus app support / repair Putnam; Super Live Plus offline Carmel / Mahopac / Brewster / Kent / Patterson / Putnam Valley / Cold Spring / Garrison / Putnam Lake / Lake Carmel; TVT DVR/NVR remote viewing; NAT / QR code / port 6036; caretaker / rental manager login; NYSEG / Central Hudson outage recovery; Chapter 145. All 11 alts/titles carry "Putnam County Super Live Plus".

## 7. Question register — super-live-plus-app-support-repair-putnam-county (REBUILT 2026-10-18)
"?" H2s: none (repair H2 "Cameras Gone From Your Phone at a Putnam Property? Same-Day Repair" does not end in "?").
§9 Q&A H3 (clusters: Watching a Putnam Place From Somewhere Else · Sharing Access With People Who Live Near the House · After the Lights Go Out · Playback, Clips and Requests From Police · Old White-Label Recorders and Security · Putnam Rules That Touch the App):
1. We check the Putnam Lake cottage from our apartment in the city on weekends — why does Super Live Plus show it offline every few weeks and then come back by itself?
2. Our Kent house has almost no cell signal — how can the caretaker check the cameras while standing in the driveway?
3. When two of us watch the Brewster shop at the same moment the picture freezes, but one viewer alone is fine — why?
4. Putnam Valley says our short-term rental's local manager must live within 30 miles of Town Hall — how should that manager get into the cameras without our admin password?
5. Our caretaker in Mahopac checks the house after storms — can he see the cameras live but not delete anything or change settings?
6. Should guests at our Philipstown rental be able to see any of the cameras in the app?
7. Our generator picks up the Carmel house within seconds, so why does the app still lose the recorder during every outage?
8. Can the app warn us that the Patterson house has lost power, rather than just showing a camera gone dark?
9. After the outage, the recorder's clock came back an hour off — does that matter for finding footage in the app?
10. Carmel police asked neighbours near Lake Casse to check footage from about 3:30 to 5 a.m. — how do we find that window quickly on a phone?
11. Our recorder only records on motion and it missed part of what happened in the driveway — can the app show what wasn't saved?
12. How far back can the app reach on our recorder, and can that be stretched before a long stretch away from the house?
13. The camera at the bottom of our Garrison driveway rides a wireless bridge — why is it the only tile that freezes in the app?
14. Our Southeast office forwards ports so staff can reach the recorder from home — should those forwards be closed?
15. Does Putnam County's Chapter 145 cover someone who only sets up the app and recorder, with no new wiring?
16. Can we leave the two-way talk on the lakefront camera switched on to speak to people at the dock?
§17 FAQ (visible == FAQPage, 10):
1. Does the cloud-storage option added to Super Live Plus in 2023 help when the Putnam house loses its internet?
2. Which phones and tablets can still run the current Super Live Plus?
3. Can one Super Live Plus login show the recorder in our city apartment and the one at the Putnam house?
4. Do your Putnam visits reach the river side — Garrison, Nelsonville and the North Highlands — as well as the lake towns?
5. Can a Putnam visit be timed for a Friday so the cameras work before we drive up for the weekend?
6. Is the Putnam rate on this page a travel charge on top of the hourly rate?
7. Should we tape the recorder password to the recorder so the caretaker can find it?
8. Can the video doorbell at the lake house ring my phone through Super Live Plus while I am in the city?
9. Will an app update, or reinstalling Super Live Plus, wipe the recorders already saved on my phone?
10. We close the lake house for the winter — what keeps Super Live Plus working until spring?
§10.5 claim H3s (quoted claims, not questions): works anywhere you have a phone signal; offline in the app means the recorder has died; port forwarding is the reliable way; Super Live Plus is a camera brand you can buy parts for; push notifications tell you everything; everyone has fast internet now; just update the app.
De-dup notes: checked (masked, exact + by meaning) against the 13 old-template SLP pages and the rebuilt NYC (180,989 B) and Orange (194,082 B) pages as they stood at 2026-10-18 ~13:30Z. Changed during build to avoid same-intent overlap with Orange/NYC: "how long does a visit take" (Orange exact dup), monthly-fee FAQ (Orange/NYC), tablet-as-monitor FAQ (Orange/NYC), what-to-have-ready FAQ (NYC), selling-the-house access FAQ (NYC ex-tenant access), Wi-Fi-works-cellular-doesn't (Orange Middletown), power-restored-but-grey (Orange O&R), buffering/upload (Orange Warwick), clip-to-police export (NYC detective), unknown-brand recorder (NYC "which recorders work"), botnet Q reframed to the port-forward decision (NYC/Orange both ask "is ours affected").

## 8. Check results
`python3 tools/check_page.py super-live-plus-app-support-repair-putnam-county --no-registration` → only "live sibling … doesn't link back" lines (12; main-run wiring). 13,407 words; title 53; meta 154; 11 figures; 6 JSON-LD blocks; FAQ 10 = schema 10; 2 forms; tel 845/800 only.
Masked block similarity (word-level SequenceMatcher on ≥8-word p/li/td/h2/h3/figcaption/FAQ blocks, check_page.mask): ≥0.65 only on blueprint-fixed H2s ("Why … Properties Need …", "What AI Gets Wrong …", etc.) and the protected warranty sentence; every other block <0.65 vs all 15 siblings, smart-pss-support-setup-ulster-county (structure donor), smart-pss-support-setup-bronx and hik-connect-app-support-repair-manhattan. 5-word-shingle Jaccard vs any sibling ≤0.03.

## 9. FLAGS for Anwar
1. Pricing borrowed from DVR Upgrade silo × 1.45; `dvr-upgrade-putnam.html` shows the same items un-multiplied (conflict to resolve).
2. No source ties Q-See to Super Live Plus; the old template's "replaced Q-See QT View" claim was dropped.
3. Unsourced installer-practice statements: fixed addresses / UPS / restart order; generator transfer gap; simultaneous viewers dividing upload; wireless-bridge behaviour; creating limited recorder users (TVT menus not quoted); guests not given access; reinstall may lose phone-only device list; drive overwrite/retention; winter-closing advice; tablet/doorbell Wi-Fi notes; 7-day / 2-hour windows to 8 PM and "1–2 hours of arrival" (blueprint el. 36, silo convention).
4. Property-type and corridor cards are general descriptions (no per-card source), as on other Putnam rebuilds.
5. AESS's own Putnam Ch. 145 licence/registration NOT claimed; page tells owners to check any installer on county lists.
6. Sibling link-backs: 12 "doesn't link back" lines are main-run wiring (old-template siblings + NYC/Orange rebuilds); HV hub link-down also main-run.
7. File size 191,047 B: ≥2 KB from all siblings at final check (Orange 195,788; NYC 180,989); Bronx/LI/Manhattan rebuilds landing later must be re-checked.
