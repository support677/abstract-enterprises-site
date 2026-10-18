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


## Bronx — REBUILD batch 2026-10-18 (super-live-plus-app-support-repair-bronx): silo findings, question-register additions and local research

## Super Live Plus App Support Repair — silo research (incoming from the Bronx REBUILD)

Written 2026-10-18 by the REBUILD subagent for `super-live-plus-app-support-repair-bronx` (queue line: `REBUILD | super-live-plus-app-support-repair-bronx | Super Live Plus App Support Repair | Bronx | up /super-live-plus-app-support-repair-nyc | direct phone (646) 490-0629 | GBP Bronx`). `research/super-live-plus-app-support-repair.md` did not exist; this file is for the main run to merge into it (the Manhattan and Long Island subagents wrote their own `_incoming` files in the same batch).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Unreachable = `EMPTY (not accessible in build env)`. Tools used: Firecrawl search (`mcp__Fire_Crawl__firecrawl_search`) and Firecrawl scrape (markdown, query mode, PDF parser). Shell curl blocked. Reddit is excerpt-only (Firecrawl search snippets). "Excerpt" = read only as a search snippet.

Bronx page section labels: §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts list), §Repair (two-minute look list + "Reading the grey squares" table), §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules list), §9 Q&A (clusters A–D, H3 1–16), §10 Equipment (+ routes table, national-brand table), §10.5 AI Reality Check (Claims 1–7), §11 Form, §12 Process (7 steps = HowTo), §13 Landmarks, §14 Pricing, §15 Packages (+BYOE), §16 Complete services, §FieldNotes, §17 FAQ (1–9), §19 Siblings, §Sources.

**Bronx thesis (distinct from the Manhattan and Long Island rebuilds):** In the Bronx, Super Live Plus is a phone-only window onto a budget TVT-platform recorder that sits on the borough's most fragile internet — the city's highest no-broadband and cellular-only shares, the highest ACP enrollment when that subsidy ended, a single cable franchise (Optimum) whose gateway swaps renumber home networks, two- and three-family houses where the recorder is cabled to a tenant's router — and was usually set up by someone who has since disappeared, often on default credentials or forwarded ports that the 2025 Mirai campaign against TVT NVMS9000 hunted. The Bronx job: make the recorder findable by serial/NAT on whatever connection the property has now, close the doors, tune viewing for mobile data, and hand the keys to the owner.

---

### Part 1 — Silo-wide findings

#### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (R1–R3). Threads not openable in build env. |
| 2 | Google PAA | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and tests claims recurring in forums, store reviews, help-desk answers (JustAnswer, JustUseApp) and installer pages instead. |
| 6 | Area landmarks | Bronx section BX-L1–BX-L9. |
| 7 | Area use cases / building stock | Bronx section BX-H1–BX-H6. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl search backend available; no Bing/DDG PAA, related or autocomplete. |
| 9 | Local news | News 12 Bronx (BX-N1, BX-N2, BX-N4), ABC7 (BX-N3), Bronx Times (BX-L4). |
| 10 | Hyperlocal | Bronx Times (BX-L4), City Limits (BX-L6). Norwood News / Riverdale Press items on Super Live Plus or TVT: EMPTY (none surfaced). |
| 11 | Yelp 1–3★ | `yelp Bronx security camera installer review app stopped working remote viewing never came back` · Firecrawl search → only Yelp search-listing and Yelp "questions" pages (e.g. https://www.yelp.com/questions/loc/the-bronx-ny/travel-lot-need-remote-access-get-camera-alarm-control-home/ZVsMNBpgQ75vWC_18pjw-g — "I travel a lot and need remote access…"); no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

#### 1.2 The app and TVT (A)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `Super Live Plus app TVT Digital` · Firecrawl search → scrape (markdown) | https://play.google.com/store/apps/details?id=com.tvt.superliveplus&hl=en_US | Developer shown as "Peng AnTai"; "About the developer: TVT (HK) LIMITED"; 3.3★, 53.3K reviews; 5M+ downloads; "professional mobile phone client software for digital video recorders and IP cameras in CCTV surveillance (compatible models only)"; Updated Oct 8, 2026; what's new "Support account switching / Fixed some known issues"; data safety "No data shared with third parties / No data collected"; reviews quoted: timeline "doesn't just fast forward or rewind, it jumps" and app crashes when ending a recording (127 helpful); "Doesn't connect on mobile reliably… next day it will not connect. Turn system off and on…"; "on 5/10/24 the app keeps signing off… no setting… 'always on'… As of 6/2/24 the app is staying on". | §5 para 1; §9 C (app closing) H3; §10.5 Claims 1, 2, 7; §Sources |
| A2 | `apps.apple.com SuperLive Plus app` · Firecrawl search → scrape (query) | https://apps.apple.com/us/app/superlive-plus/id1058758642 | Seller Peng AnTai; 3.9★, 16K ratings; 129.8 MB; Business; "Requires iOS 12.1 or later". | §10.5 Claim 7; §Sources |
| A3 | `Super Live Plus app TVT Digital` (result) → Firecrawl scrape (PDF parser) | https://www.mysecuresystems.com/wp-content/uploads/SuperLivePlus-User-Manual.pdf | SuperLive Plus V1.0 user manual: access via WLAN (IP+port or QR) and "Access Device via 2G/3G/4G Network" (PPPoE/DDNS/static WAN/port forwarding/UPnP); QR scan fills "my device" = MAC or serial + user; "If the device and the mobile client are in the different network segment, the device shall support QRCODE and enable the NAT"; default user **admin**, password **123456**; live view resolution Low (CIF)/Middle (D1)/Super/Custom bitrate+frame rate; speed-up option for 720P+; channel lights (sensor/manual/motion/schedule/video loss); snap, local record, audio, two-way talk, PTZ by sliding / 3D tap; remote playback from HDD with date select, single frame, forward/rewind; remote setting mirrors device menus; local settings: reserved disk space, record recycle, audio alarm + shake alarm on video loss/sensor/motion, favourites, launch setting, gesture password, Auto syn of device list; server list icon green = connected, gray = failed, twinkling = connecting; press-and-hold QR to share device; file management + local playback. | §5 para 4; §Repair list + table; §6 cards; §9 A4, B1, B2, C2; §10 cards; §10.5 Claims 4, 5; §12; §Sources |
| A4 | `"SuperLive Plus" app store Shenzhen TVT` · Firecrawl search → scrape (query, directQuote) | https://tvtnationaldistributor.it/component/k2/itemlist/user/493-superuser.html | TVT Italian distributor notice 12/01/2022: SuperCam Plus temporarily unavailable on Play Store; use SuperLive Plus, "STESSA IDENTICA App senza marchio TVT"; accounts created on the TVT cloud with SupercamPlus also log in. | §5 para 1; §9 A6 (son's account) H3; §Sources |
| A5 | same search (excerpt) | https://apps.apple.com/in/app/supercam-plus/id1058764743 | SuperCam Plus provider: Shenzhen TVT Digital Technology Co., Ltd. | Background only |
| A6 | `Super Live Plus app TVT Digital` (excerpt) | https://www.youtube.com/watch?v=xW9rmueAF4A | "Install & Setup SuperLive Plus for Android TV App". | §10 Android TV card; §Sources |
| A7 | `Shenzhen TVT Digital Technology OEM brands…` · Firecrawl search (excerpts) | https://www.youtube.com/watch?v=3E_57atlhxM ; https://www.youtube.com/watch?v=7ygnIVjyF8g ; https://www.youtube.com/watch?v=8ZRPsys45L4 | CCTV Camera World: "The QT series DVRs… work with the smartphone app SuperLivePlus… setting and code can be found in the Network and then NAT"; Shield Technology DVRs/NVRs "and the compatible TVT models" on SuperLive Plus. | §5 para 1; §10 white-label card; §Sources |
| A8 | `reddit superlive plus app offline NVR` · Firecrawl search → scrape (markdown) | https://videos.cctvcamerapros.com/support/topic/superlive-plus-mobile-app-offline | CCTV Camera Pros, Jun 6, 2025: SuperLive Plus is the app for Viewtron DVRs/NVRs/IP cameras; customer showed OFFLINE in Canada; fix Settings > Local > Domain > GLOBAL/AUTONATGLB.COM. | §5 para 1; §9 A4; §Sources |
| A9 | `Super Live Plus app TVT Digital` → Firecrawl scrape (markdown) | https://portal.hdssfl.com/portal/en/kb/articles/superlive-plus-app-how-to-add-a-nvr-dvr | HDSS "TVT (T-Series)": Settings > Device List > ⋯ > Manual Add (serial, username, password) or Scan Code; connection goes grey to green. | §5 para 1; §10 white-label card; §Sources |
| A10 | `superlive plus "NAT" status offline DVR network settings fix` · Firecrawl search → scrape (PDF, query) | https://www.vimar.com/irj/go/km/docs/z_catalogo/DOCUMENT/49401261A0_EN_05_Videorecordergraphicaluserinterface.109666.pdf | Videorecorder GUI manual (Vimar, Oct 2015) with the NVMS-style interface: HTTP 80, RTSP 554, **Server port 6036**; NAT config "Start → Settings → Network → NAT… Check Enable and then select the NAT server" (from search excerpt); cycle record replaces earliest when disks full; per-camera expiration time deletes recordings; admin password reset via "Edit Security Question" to 123456, else "contact your dealer". **FLAG:** page describes this as "recorder manuals that use this interface"; it does not claim Vimar is TVT. | §9 A4, C1; §6 retention card; §8.5 bullet 6; §Sources |
| A11 | `TVT Digital Technology FCC covered list OR NDAA section 889 banned` · Firecrawl search → scrape (query) | https://www.fcc.gov/supplychain/coveredlist | Covered List names Huawei, ZTE, Hytera, Hikvision, Dahua (all Mar 12, 2021); TVT not named (checked Oct 2026, page cached 2026-10-17). | §8.5 bullet 2; §10.5 Claim 7 (indirect) |
| A12 | `"Super Live Plus" OR "SuperLive Plus" Bronx` · Firecrawl search (excerpts) | https://www.abstractenterprisessecuritysystems.com/super-live-plus-app-support-repair-hudson-valley ; https://www.facebook.com/Comtex.Inc/photos/… | Our own old HV page excerpt: "the name stands for Digital Mobile Surveillance…" (wrong — DMSS wording copied into SLP template); Comtex (West New York NJ) installer: "The App that we use is called Super live plus… We don't offer any monthly contracts." | §10.5 Claim 1 ("pages on our own older site got the name's meaning wrong") — **FLAG for the main run: the old silo template carries this error on every un-rebuilt page.** Comtex not used. |

#### 1.3 Security (S)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `TVT NVMS9000 DVR vulnerability exploited Mirai botnet GreyNoise 2025` · Firecrawl search (full excerpt) | https://www.greynoise.io/blog/surge-exploitation-attempts-tvt-dvrs | Apr 7, 2025: 3× surge in exploitation attempts against TVT NVMS9000 DVRs, peaking Apr 3 at over 2,500 unique IPs; info-disclosure flaw "can be used to gain administrative control"; overlap with Mirai. | §5 para 4; §5.5 bullet 6; §9 D1; §10.5 Claim 4 context; §Sources |
| S2 | same search (full excerpt) | https://www.bleepingcomputer.com/news/security/new-mirai-botnet-behind-surge-in-tvt-dvr-exploitation/ | 6,600 distinct malicious IPs in the past month; flaw first disclosed by SSD in May 2024; signs of infection: outbound traffic spikes, sluggish performance, frequent crashes or reboots, high CPU/memory when idle, altered configurations; advice: disconnect, factory reset, update firmware, isolate. | §9 D1; §Sources |
| S3 | same search → scrape (query) | https://ssd-disclosure.com/ssd-advisory-nvms9000-information-disclosure/ | May 24, 2024: unauthenticated disclosure of usernames/passwords and network config; ports "6036, 17000, 17001, 8000, etc…"; "affected versions are <1.3.4… Affected customers can contact techsupport@tvt.net.cn to inquire if there is a patch available." | §6 port card; §8.5 bullet 3; §9 C3, D1, D2 |
| S4 | same search → scrape (markdown) | https://www.vulncheck.com/advisories/tvt-nvms9000-unauthenticated-admin-queries-and-information-disclosure | CVE-2024-14007, CVSS 8.7, advisory 11/23/2025; NVMS-9000 firmware < 1.3.4 "used by many white-labeled DVR/NVR/IPC products"; commands queryBasicCfg, queryUserList, queryEmailCfg, queryPPPoECfg, queryFTPCfg; in VulnCheck KEV. | §5.5 bullet 6; §9 C3 (email config), D1; §Sources |
| S5 | `T-Mobile Home Internet port forwarding not supported CGNAT support page` · Firecrawl search (excerpts) | https://simeononsecurity.com/articles/t-mobile-home-internet-port-forwarding/ ; https://pinggy.io/blog/tmobile_port_forwarding/ | T-Mobile Home Internet uses CG-NAT; port forwarding fails by design. | §9 A2; §Sources |
| S6 | carried research/smart-pss-support-setup.md P5 | https://nysenate.gov/legislation/laws/PEN/250.05 | Penal Law §250.05 eavesdropping felony; one-party consent. | §8.5 bullet 5; §10 audio card |
| S7 | carried research/smart-pss-support-setup.md P6 | NYS DOS Article 6-D (see research/nvr-installation.md) | CCTV installation/service is licensed work in NYS. | §8.5 bullet 1; §10.5 Claim 6 |

#### 1.4 Reddit, forums, help desks (R)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit superlive plus app offline NVR` · Firecrawl search (excerpt) | https://www.reddit.com/r/SecurityCamera/comments/1h3n93v/dhcp_failure/ | "I have been using the SuperLive plus app for my camera system for over a year now. Recently the app is no longer showing a green WiFi symbol…" (title "DHCP : failure"). | §10.5 Claim 2; §Sources |
| R2 | same (excerpt) | https://www.reddit.com/r/tinycam/comments/glptdp/superlive_plus/ | "Many times the app can't make the connection and it shows my cameras as being offline. It only happens on Android 13…" | §Sources only |
| R3 | same (excerpt) | https://www.reddit.com/r/cctv/comments/1h0lrfa/remote_access_no_data/ | SuperLive Pro user, remote access "no data". | Not used |
| R4 | same (excerpts) | https://forums.justuseapp.com/en/post/CHPGMW9ZCI/app-opens-but-screen-is-black-won-t-bring-up-cameras ; https://www.justanswer.com/home-security-systems/te9n9-superlive-plus-camera-offline-android.html ; https://forums.justuseapp.com/en/post/O7MPET6XEY/no-data | Help-desk boilerplate: restart the app, restart cameras and NVR, verify NAT and DNS enabled. | §10.5 Claim 2 (the "restart" advice pattern) |
| R5 | `TVT DVR forgot password reset superlive plus…` · Firecrawl search (excerpts) | https://cctvwiki.com/en/cctv-super-password-2/ ; https://play.google.com/store/apps/details?id=com.rat.cctvsuperpassword | Third-party "super password" generators for TVT recorders. | Not used (not recommended; not cited) |
| R6 | `SuperLive Plus push notification alarm not working…` · Firecrawl search → scrape (query) | https://www.cctvcameraworld.com/push-notifications-from-security-cameras/ | Motion detection must be enabled on the recorder itself before app alerts work (article written for DMSS-app systems). | §9 B2 (general principle only; not cited as SLP-specific) |

#### 1.5 Keyword plan (five layers, silo)
- **Service:** Super Live Plus app support · Super Live Plus repair · SuperLive Plus setup · TVT DVR app repair · remote viewing repair.
- **Problem:** Super Live Plus offline / grey · cameras not showing on phone · after router change · after internet provider change · forgot recorder password · slow on mobile data · too many alerts · app closing.
- **Technology:** TVT · NVMS9000 / NVMS-9000 · NAT / P2P serial number · QR code add · sub stream · DVR / NVR / XVR · white-label (Viewtron, QT, Shield, HDSS T-Series) · SuperCam Plus · CVE-2024-14007 · CGNAT · UPnP · port 6036.
- **Industry:** two-family house · landlord · tenant · bodega / grocery · auto shop · walk-up · storefront.
- **Geographic (Bronx page only):** Bronx · Williamsbridge · Wakefield · Eastchester · Baychester · Throgs Neck · Country Club · Pelham Bay · Jerome Avenue · White Plains Road · Fordham Road · Westchester Square · Woodlawn / Katonah Avenue · the Hub.
- Placement: title, H1, H2s, §6/§9 H3s, image alts (all carry "Bronx"); no stuffing.

#### 1.6 Silo pricing — FLAG
- §9 Bronx multiplier 1.00 (no change to base figures).
- Protected service rate: **$195/hr, 3-hour minimum ($585)** — used for on-site Super Live Plus work.
- **Borrowed prices (FLAG):** recorder replacement $450–$700 (4-ch), $650–$1,000 (8-ch), $800–$1,200 (8-ch XVR), $1,200–$2,200 (16-ch), $2,200+ (32-ch) — taken from the live `dvr-upgrade-bronx.html` table (same as smart-pss-support-setup-bronx). Not invented; borrowed from another silo's approved page.
- **"Phone check — no charge" (FLAG):** house practice carried from smart-pss-support-setup-bronx ("phone triage at no charge"); not on a pricing sheet I could find.
- Worked examples (Wakefield two-family = $585; Jerome Avenue 16-ch = hourly + $1,200–$2,200 if replaced) are arithmetic on the above only.

---

### Question register — Super Live Plus App Support Repair silo

Rule (v2.3 §12.3, DAILY-RUN step 2): no FAQ/Q&A question on a new or rebuilt page may repeat an intent listed here.

#### Old template (pages not yet rebuilt — identical apart from area name; their intents to avoid where possible)
FAQ (10, on brooklyn, dutchess-county, hudson-valley, nassau-county, nyc, orange-county, putnam-county, queens, rockland-county, staten-island, suffolk-county, ulster-county, westchester-county; and on long-island/manhattan/bronx before their rebuilds): "🔧 Super Live Plus Offline Right Now?" (CTA) · Is Super Live Plus a camera brand? · Why does Super Live Plus say "device offline"? · Is Super Live Plus the same as SuperCam Plus or Q-See QT View? · Why can't I see live view or playback? · Can you recover my Super Live Plus password? · Why aren't my push notifications working? · Do you fix Super Live Plus systems you didn't install? · How much does Super Live Plus repair cost? · What areas do you cover?

#### super-live-plus-app-support-repair-bronx — REBUILT 2026-10-18 (owns these intents)
§9 Q&A (H3):
1. Our two-family house still has two routers chained together from two old plans — could that be why the recorder keeps dropping out of the app? *(double router / inner router renumbering)*
2. We moved to the cheapest internet plan after the federal discount ended — is a low-speed plan enough for the recorder? *(upload speed adequacy; ACP end; 5G/CGNAT/hotspot)*
3. The recorder is cabled to the tenant's router on the second floor — what happens when that tenant moves out? *(recorder on someone else's connection)*
4. Where on the recorder itself do we look to know whether it can reach TVT's cloud at all? *(NAT status page)*
5. The internet company's installer is coming to put in a new gateway — what should we let them change, and what should we ask them to leave alone? *(before a provider visit)*
6. My son set up the app on his account years ago — does Super Live Plus have accounts that need to move to us, separate from the recorder's password? *(app account vs recorder login)*
7. I only watch on my phone's data plan — how much data does checking the cameras use, and how do I keep it down? *(mobile data use)*
8. The phone buzzes all night for buses and headlights on our block — how do we make the app alarm only for the gate and the side door? *(too many alerts)*
9. The app keeps closing or the screen goes dark while we are watching the register — can it stay on? *(app sign-off / screen timeout)*
10. We bought a two-family house in Williamsbridge and the cameras came with it — what has to change the week we close? *(takeover at property purchase)*
11. The QR sticker on the recorder shows its serial number — can someone who photographs it watch our cameras? *(serial/QR exposure)*
12. The recorder sits on a shelf by the front door — if a burglar takes it, what do we lose and what should we change afterward? *(stolen recorder consequences)*
13. Our recorder has been slow and rebooting on its own — could it be infected, and what is the safe order to clean it up? *(Mirai symptoms + cleanup order)*
14. Is it safe to update the recorder's firmware from the phone, or should that happen on site? *(firmware method)*
15. Con Edison outages hit our block most summers — what keeps the recorder and the app working through a blackout? *(UPS / battery)*
§17 FAQ:
1. Who answers when we call the Bronx line — a dispatcher or a technician?
2. Will you show us how to back up a clip from the recorder itself before you leave?
3. Do you need to get into the tenant's apartment if the router is up there?
4. Will our Wi-Fi password or internet account need to change?
5. Can you come on a Saturday, when everyone whose phone needs setting up is home?
6. Can you tell whether the recorder's hard drive is healthy while you are there?
7. If our recorder cannot be saved, does the replacement have to be another TVT-based box?
8. What paperwork do we get when the job is finished?
9. While you are here, can you move the recorder somewhere a burglar will not find it?

Cross-check done at end of build against the Manhattan and Long Island rebuilds on disk (13:18–13:19): Bronx questions on playback-scrubbing, saving clips from the phone for police, removing a relative's access, shared logins, factory password, open ports / TVT flaws, retention days, clock after outage, "who made our recorder", photos to send before the visit, remote vs on-site, family abroad and "TV/tablet at the counter" were **dropped or replaced** because those intents are on Manhattan or Long Island.

---

### Bronx

Build 2026-10-18. Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`) · up-link `/super-live-plus-app-support-repair-nyc` · §9 Bronx = 1.00.

#### Internet, cable franchise, subsidy (BX-I)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-I1 | re-checked: `osc.ny.gov dinapoli broadband` · Firecrawl scrape (query, directQuote) | https://www.osc.ny.gov/press/releases/2024/12/dinapoli-report-examines-broadband-availability-access-and-affordability-nyc | Dec 11, 2024: as of 2023 the Bronx had the highest poverty share (28.9%), highest no-broadband share (36.7%) and highest cellular-only share (20.3%); Bronx and Brooklyn highest average monthly broadband price (2024). | §5 para 2; §5.5 bullet 1; §9 B1; §10.5 Claim 5; §Sources |
| BX-I2 | re-checked · Firecrawl scrape (query, directQuote) | https://thebronx.org/understanding-and-overcoming-the-bronx-digital-divide/ | Jul 8, 2025: 22.4% lack home broadband; "Fully 44 percent of Bronx households were enrolled in ACP when it ended in 2024—by far the highest share in the city"; one in three households (184,000+) lack a computer. | §5 paras 2–3; §5.5 bullet 2; §9 A2; §10 routes table; §Sources |
| BX-I3 | `Optimum Altice cable franchise Bronx Brooklyn Spectrum…` · Firecrawl search → scrape (query) | https://www.nyc.gov/content/oti/pages/franchises/cable-tv-franchises | "View the Altice USA Franchise Agreement – Bronx" (Altice also holds Brooklyn; Spectrum and Verizon other franchises). | §5.5 bullet 3; §13 card 1; §Sources |
| BX-I4 | `Big Apple Connect NYCHA free internet Bronx developments Optimum` · Firecrawl search (full excerpts) | https://www.nyc.gov/content/oti/pages/big-apple-connect ; https://www.optimum.com/program/big-apple-connect | OTI launched Big Apple Connect Sept 2022; "All Bronx developments below are serviced by Altice/Optimum"; Optimum page lists Bronx River, Bronx River Addition, Gun Hill, Highbridge Gardens, Patterson, Pelham Parkway, Webster; 500 Mbps; Bronx store 2912 3rd Ave., Bronx, NY 10455. | §5.5 bullet 3; §13 card 1; §Sources |
| BX-I5 | same search (excerpt) | https://nychajournal.nyc/big-apple-connect-extended-for-three-years/ | Extended through June 2028. | Not used |

#### Housing stock (BX-H)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-H1 | `Bronx housing units in structure 1-unit 2-unit 3-4 units percent ACS Bronx County` · Firecrawl search (excerpt) + scrape (PDF, query) | https://www.osc.ny.gov/files/reports/osdc/pdf/report-13-2024.pdf | "The South Bronx: An Economic Snapshot" (OSC report 13-2024), Figure 6: Bronx 26.4% of units in 1–4-unit buildings, 71.6% in 5+ (excerpt); scrape returned South Bronx 11.6% / 86.4%, five-year data ending 2021. **Note:** the Bronx-wide 26.4% comes from the search excerpt of the same table; the scrape only confirmed the South Bronx row. | §5.5 bullet 4 ("about a quarter… 26.4%… far more common outside the South Bronx, where only 11.6%…") |
| BX-H2 | `furmancenter Bronx` · Firecrawl scrape (query) | https://www.furmancenter.org/neighborhoods/the-bronx/ | Homeownership 19.7% (2024); population 1,384,724 (2024); median household income $47,600 (2024); (excerpt) 7.9% of rental units public housing (2025); 63,066 units in 4+ buildings 2010–2025. | §5.5 bullet 5; §Sources |
| BX-H3 | `Bronx Community District 12 Wakefield Williamsbridge one- and two-family homes…` · Firecrawl search (excerpt) | https://www.homes.com/local-guide/bronx-ny/williamsbridge-neighborhood/ | Williamsbridge: "You'll see two- and three-family homes, often with private driveways, garages…" | §7 card 1 (Williamsbridge only); §9 C1; §Sources |
| BX-H4 | `Country Club Throggs Neck Bronx detached single-family homes…` · Firecrawl search (full excerpt) | https://cityneighborhoods.nyc/country-club | Country Club: peninsula between Pelham Bay and Throgs Neck; "blocks of detached homes"; "single-family homes, bungalows, and split-level houses"; "predominantly homeowner-occupied". | §7 card 2; §7.5 para 2; §Sources |
| BX-H5 | carried research/smart-pss-support-setup.md BX-H4 | https://s-media.nyc.gov/agencies/lpc/lp/2403.pdf | Five-/six-storey apartment houses dominant along the Grand Concourse. | §7 card 3 (building type only) |
| BX-H6 | Homes.com Throgs Neck / Zillow waterfront results (excerpts only) | https://www.homes.com/bronx-ny/throgs-neck-edgewater-park-neighborhood/ | Listing pages only. | Not used |

#### Corridors / landmarks (BX-L)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-L1 | `Bronx Community District 12 …` → Firecrawl scrape (markdown) | https://www.nyc.gov/site/bronxcb12/about/about.page | CB12: Wakefield — "White Plains Road is the main shopping district, popular for its many fresh produce markets and Spanish, West Indian, and East Indian specialty food shops"; 2 and 5 lines; Williamsbridge — White Plains Road primary thoroughfare; Eastchester — "Dyre Avenue is the main commercial strip"; Baychester — "Eastchester Road is the main commercial thoroughfare"; Woodlawn — Katonah Avenue main commercial thoroughfare, "many fine restaurants and specialty shops", McLean Avenue = NY/Westchester County line; Edenwald hosts the 47th Precinct. | §8 cards 1, 2, 6; §13 cards 2, 6; §Sources |
| BX-L2 | `Jerome Avenue rezoning auto repair shops Bronx corridor` · Firecrawl search (full excerpt) | https://citylimits.org/3-years-after-bronx-rezoning-jerome-avenue-auto-shops-under-pressure/ | UAMA: 35–40 auto businesses displaced since rezoning, "around 150 still operate"; "one of the largest concentrations of automotive businesses in the city"; virtually all rent. | §7 card 6; §13 card 4; §14 example 2 (location only); §Sources |
| BX-L3 | carried research/smart-pss-support-setup.md BX-L1 | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=49 | Fordham Road BID: 35 block faces, 333 ground-floor businesses. | §8 card 3; §Sources |
| BX-L4 | carried BX-L3 | https://www.bxtimes.com/third-avenue-bid-adds-security-measures/ | Bronx Times, Oct 2, 2026: Third Avenue BID 18 cameras at 10 locations. | §8 card 4; §Sources |
| BX-L5 | carried BX-N1 / BX-L6 | https://abc7ny.com/post/surveillance-video-reward-offered-arrest-alleged-shoplifter-wanted-stabbing-bronx-bodega-employee/15429424/ ; https://en.wikipedia.org/wiki/IRT_Pelham_Line | Oct 15, 2024: police released surveillance footage after a Westchester Square bodega worker was stabbed stopping a theft; 6 train elevated over Westchester Ave. | §8 card 5; §Sources |
| BX-L6 | carried BX-F1 | https://www.bronxda.nyc.gov/html/outreach/enroll-in-bronxcams.shtml | BronxCAMS (2018): voluntary, confidential map; DA staff "contact the camera owner or designee to view footage and request a copy"; "Our Office does not have access to cameras or camera footage"; 198 E. 161st Street. | §8.5 bullet 4; §13 card 5; §Sources |
| BX-L7 | carried BX-F2 | https://www.riverdalepress.com/stories/bronx-da-wants-borough-directory-of-security-cameras,68834 | May 2019: systems "loop, or tape over, existing footage after… as short as 24 hours". | Not used (retention Q removed after the overlap check; source removed from the page) |
| BX-L8 | `Bronx homeowners security cameras package theft Throggs Neck…` · Firecrawl search (excerpt) | https://www.bxtimes.com/security-cameras-coming-to-pelham-parkway-houses/ | 2014: 375 cameras at Pelham Parkway Houses (Vacca funding). | Not used (2014) |

#### Local news (BX-N)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-N1 | `Bronx homeowners security cameras package theft Throggs Neck OR Pelham Bay OR Wakefield 2026 news` · Firecrawl search → scrape (query) | https://bronx.news12.com/2025/10/23/man-caught-on-camera-stealing-from-mailboxes-in-throgs-neck/74zBl2o9JN1pYwqv8nfkXI | Oct 15 (2025) ~9:30 p.m., Ring doorbell camera at a residential home near Clarence and Randall avenues, Throgs Neck, caught mailbox theft; postal inspector + NYPD investigating. | §13 card 3; §Sources (no names used) |
| BX-N2 | same → scrape (query) | https://bronx.news12.com/2025/12/10/caught-on-camera-porch-pirates-strike-again-this-holiday-season/7ssxJZkkO6ppcqn9vpkPgs | Pelham Gardens resident's home video of packages stolen Dec 2 (2025); four packages that season. | Not used (removed from the page sources) |
| BX-N3 | same (excerpts) | https://bronx.news12.com/2025/06/03/throgs-neck-neighbors-on-edge-after-cars-broken-into-stolen/1cXa3XYC1POZGuFAcU9fsG ; Pelham Bay airbag thefts (News 12 Facebook) | Car break-ins Throgs Neck / Pelham Bay. | Not used |
| BX-N4 | carried BX-N4 (smart-pss) | https://bronx.news12.com/2026/07/03/5000-con-edison-customers-in-the-bronx-without-power-amid-heat-wave/ONmoL7BVphOWvTtg2dafc | Jul 3, 2026: ~5,000 Bronx Con Ed customers out; 8% voltage reduction in parts of the northwest Bronx. | §9 D3 (Con Ed); §Sources |

#### Local Reddit / hyperlocal
- `reddit r/bronx security cameras house DVR app landlord` · Firecrawl search → only non-Bronx r/Landlord, r/legaladvice, r/Tenant, r/HomeNetworking threads (e.g. https://www.reddit.com/r/HomeNetworking/comments/14g9bri/landlords_wants_to_use_my_network_for_security/ — tenant asked to let landlord's cameras use their internet). r/bronx threads on Super Live Plus/TVT: EMPTY. The HomeNetworking excerpt (non-Bronx) informed the "recorder on the tenant's router" idea only as a pattern; not quoted.
- Norwood News / BronxNet / Riverdale Press items on Super Live Plus or TVT: EMPTY.

#### Local licensing / rules
- NYS licensing (S7) → §8.5 bullet 1, §10.5 Claim 6.
- FCC Covered List, TVT not named (A11) → §8.5 bullet 2.
- SSD advisory / patch contact (S3) → §8.5 bullet 3.
- BronxCAMS voluntary/confidential (BX-L6) → §8.5 bullet 4.
- Penal Law §250.05 (S6) → §8.5 bullet 5, §10 audio card.
- Recorder cycle record / expiration (A10) → §8.5 bullet 6.
- NYC rule requiring private footage retention: EMPTY (as recorded in research/nvr-installation.md).

#### Prices used (Bronx 1.00×) — see §1.6 (FLAGS)

#### Images (11) — permanent image rule
Drive "AESS Website Photos" has no Super Live Plus folder; CompanyCam not connected (per coordinator). Sourced ONLY from images/residential-security-camera-installation/, images/floodlight-camera-installation/, images/door-buzzer-installation/, images/intercom-repair/. All viewed first via contact sheets and full-size reads; product shots in those folders rejected (clean marketing renders of Reolink/Ubiquiti/Alarm.com/Akuvox gear — look rendered, wrong brands). No faces, house numbers, plates or readable documents (sidewalk tile shows a partial parked car with no readable plate; mural is artwork). No image claims to show the Bronx, a customer, TVT hardware or the Super Live Plus app; captions say "Example photo from another AESS job (not a Bronx property)". Converted with Pillow, WebP q80, all ≤1600 px.
| images/super-live-plus-app-support-repair/ | Source | Section |
|---|---|---|
| super-live-plus-app-support-repair-bronx-dome-camera-under-storefront-fascia-beside-mural.webp (hero, eager, 917×647) | images/floodlight-camera-installation/floodlight-camera-installation-brooklyn-dome-camera-under-fascia-beside-led-strip-lights.webp | Hero |
| …-bronx-camera-on-steel-arm-below-stone-facade-windows.webp (228×368) | images/intercom-repair/intercom-repair-staten-island-stone-apartment-facade-with-camera-on-steel-arm.webp | §5 |
| …-bronx-network-cable-bundles-above-equipment-rack.webp (600×300) | images/floodlight-camera-installation/floodlight-camera-installation-hudson-valley-network-cable-bundles-above-equipment-rack.webp | §6 |
| …-bronx-turret-camera-under-water-stained-ceiling-tiles.webp (685×620) | images/floodlight-camera-installation/floodlight-camera-installation-hudson-valley-turret-camera-high-in-corner-of-storage-room.webp | §7 |
| …-bronx-dome-camera-on-tiled-ceiling-above-glass-entrance.webp (935×720) | images/intercom-repair/intercom-repair-staten-island-dome-camera-on-tiled-ceiling-above-glass-entrance.webp | §8 |
| …-bronx-wide-angle-channel-view-of-sidewalk-and-curb.webp (310×310) | images/residential-security-camera-installation/residential-security-camera-installation-nassau-county-wide-lens-recorder-tile-of-sidewalk-and-curb.webp | §9 cluster A |
| …-bronx-camera-watching-corridor-to-grey-service-door.webp (640×905) | images/door-buzzer-installation/door-buzzer-installation-ulster-county-camera-covering-corridor-to-service-door.webp | §9 cluster B |
| …-bronx-small-black-camera-high-on-white-wall.webp (1247×935) | images/door-buzzer-installation/door-buzzer-installation-ulster-county-small-camera-on-plain-wall.webp | §9 cluster C |
| …-bronx-black-bullet-camera-on-bracket-under-drop-ceiling.webp (735×580) | images/floodlight-camera-installation/floodlight-camera-installation-hudson-valley-black-bullet-camera-on-bracket-under-drop-ceiling.webp | §9 cluster D |
| …-bronx-dome-camera-and-motion-sensor-in-ceiling-corner.webp (400×500) | images/intercom-repair/intercom-repair-putnam-county-dome-camera-and-motion-sensor-in-ceiling-corner.webp | §10 |
| …-bronx-ceiling-camera-near-red-exit-sign.webp (845×620) | images/floodlight-camera-installation/floodlight-camera-installation-orange-county-ceiling-camera-and-device-beside-red-lit-exit-sign.webp | §14 |
DAILY-LOG note: `images: 11 reused from images/floodlight-camera-installation/, images/intercom-repair/, images/door-buzzer-installation/, images/residential-security-camera-installation/ (no real super-live-plus photos yet)`. Several of these source photos are themselves crops of the same original AESS shots used across other silos (e.g. the water-stained turret and cable bundles).

#### House practices stated without an external source (FLAG for Anwar)
- "Follow the cable before touching the phone"; one router per house with any second box as an access point; recorder on a connection the owner controls; prefer the NAT/serial method over port forwarding; router reservation or automatic addressing instead of a hand-typed fixed IP.
- Battery backup (UPS) sizing advice for recorder + gateway; surge protector ≠ UPS.
- One recorder user per person; viewing users for counter screens; gesture lock on shared tablets.
- Evidence copy = recorder USB backup (not phone recording); note camera/date/times/who copied.
- Before a provider visit: photograph old gateway, ask installer not to touch recorder or open ports.
- "Most faults back to a live picture within one to two hours" (blueprint element 36 wording).
- "The person who answers is the technician who plans the visit" (carried claim from model pages).
- Office hours Mon–Sat 8:00–19:00 (from the LocalBusiness schema used on the model page).
- Phone check at no charge (see §1.6).
- National-brand comparison table (ADT/Ring/SimpliSafe) — general description (blueprint element 25).
- Field Notes is a method note in Anwar's voice, not a specific Bronx job story — confirm or replace.

#### Build notes
- Checked against rebuilt siblings on disk at the end of the build: super-live-plus-app-support-repair-manhattan.html (186,682 B, 13:19) and -long-island.html (178,970 B, 13:18). Masked paragraph similarity (difflib on geo-masked p/li/h3/td ≥10 words): max 0.64 vs Manhattan, 0.64 vs Long Island, 0.63 vs smart-pss-support-setup-bronx (content; the shared `:root` CSS line is the only higher hit), ≤0.52 vs old-template siblings.
- Bronx page bytes 183,046 — 4,076 B from Long Island and 3,636 B from Manhattan; re-check size cluster if either sibling changes again before shipping.


## Long Island hub — REBUILD batch 2026-10-18 (super-live-plus-app-support-repair-long-island): silo findings, question-register additions and local research

## Super Live Plus App Support Repair — silo research (incoming, from the Long Island hub REBUILD)

Built 2026-10-18 by the subagent for `super-live-plus-app-support-repair-long-island` (queue line: `REBUILD | super-live-plus-app-support-repair-long-island | Super Live Plus App Support Repair | Long Island hub | up / | (800) 486-0943 | GBP Brooklyn`). `research/super-live-plus-app-support-repair.md` did not exist; this file is for the main run to merge (Bronx and Manhattan siblings were built in parallel and will add their own files).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (markdown, query/directQuote mode, PDF parser), WebSearch (one query). Shell curl blocked. Reddit threads cannot be opened (excerpts only). "Re-checked" = fetched again today from a URL first found by an earlier build (file named).

Page section labels (LI hub): §Hero, §Quick, §5 Island (+ §5.5 facts list), §Repair (same-day block + checks + "what the app shows" table), §Counties (Nassau vs Suffolk), §6 Services, §7 Architecture (+ §7.5 method), §8 Commercial (+ §8.5 rules), §9 Q&A (clusters A–F), §10 Equipment (+ remote-access table, national-brand table), §10.5 AI Reality Check (Claims 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ BYOE), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources, §Close.

**Long Island hub thesis (distinct from Bronx/Manhattan siblings, which deal with dense buildings):** on Long Island a Super Live Plus failure is almost always a problem of *distance between an empty house and an owner who is somewhere else*. The recorder sits in a slab ranch closet, a raised South Shore house or a closed East End house; the owner is on the LIRR, in the city at work, or wintering away. So the jobs are: recorders that were added to the app by their home-network address and go grey on cellular; Optimum/Fios gateway swaps that wipe port-forwarding; PSEG restorations that reboot the recorder in the wrong order; seasonal houses where nobody can press a button for months; and access that was shared with family, tenants or a roommate and must be taken back. The hub separates Nassau (453 sq mi, 2 cities/3 towns/64 villages, dense, year-round) from Suffolk (2,373 sq mi, 10 towns, long distances, seasonal East End) and sends readers down to each county page.

---

### Part 1 — Silo-wide findings (usable on every Super Live Plus page)

#### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (R1–R8). Threads not openable in build env. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so on the page and tests seven claims repeated in forum answers, how-to pages and generic troubleshooting lists (A1–A5, M1, R1–R8) |
| 6 | Landmarks | Long Island section LI-L |
| 7 | Building stock / use cases | Long Island section LI-H |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl's search backend and one WebSearch query available |
| 9 | Local news | PSEG LI release Sept 28 2026; NCPD news flash Jan 16 2026 |
| 10 | Hyperlocal | Garden City PD village page; LI Herald/Patch Super Live Plus items: EMPTY (none surfaced) |
| 11 | Yelp 1–3★ | `yelp Long Island security camera repair DVR app not working review 1 star Nassau Suffolk` · Firecrawl search → only Yelp search-listing pages (West Islip, Amagansett, Nassau, Bethpage listings), no review text → EMPTY (not accessible in build env). Substitute: Google Play 1–3★ review excerpts on the app listing (A1). |

#### 1.2 The app (A)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `SuperLive Plus app device offline TVT` · Firecrawl search → scrape (markdown) | https://play.google.com/store/apps/details?id=com.tvt.superliveplus&hl=en_US | Package `com.tvt.superliveplus`. Listed developer name "Peng AnTai"; "About the developer: TVT (HK) LIMITED", Hong Kong address. Description: "professional mobile phone client software for digital video recorders and IP cameras in CCTV surveillance (compatible models only)". 3.3★, 53.3K reviews, 5M+ downloads, "Updated on Oct 8, 2026", What's new: "Support account switching / Fixed some known issues". Data safety: "No data shared with third parties", "No data collected". Reviews shown: playback timeline "jumps" and app crashes when ending a clip recording (127 helpful); "can scan and connect, but next day it will not connect. Turn system off and on and connection works" (25 helpful); app kept signing off from 5/10/24, fixed by 6/2/24, developer did not answer emails (52 helpful). Same developer lists SuperLiveNVR, NVMS2 Plus, NVMS2. | §5 para 1; §5.5 bullets 1–2; §9 C, D H3s; §10.5 Claims 1, 3, 6; §17 FAQ 1, 2; §Sources |
| A2 | `apps.apple.com "SuperLive Plus" app` · Firecrawl search (excerpt) | https://apps.apple.com/us/app/superlive-plus/id1058758642 | Free, Business, "Designed for iPad", 3.9 from 16K ratings, age 4+, EN + 32 more languages, 129.8 MB, iPhone and iPad. | §5.5 bullet 2; §17 FAQ 3, 9; §Sources |
| A3 | same search (excerpt) | https://apps.apple.com/in/app/supercam-plus/id1058764743 | SuperCam Plus — provider "Shenzhen TVT Digital Technology Co., Ltd.", requires iOS 15.0 or later. (Separate TVT app.) | §10 card "Other TVT apps"; §9 E H3; §Sources |
| A4 | `TVT Digital Technology Shenzhen OEM DVR NVR brands SuperLive Plus Viewtron` · Firecrawl search → scrape | https://www.tvt.net.cn/ | Shenzhen TVT Digital Technology Co., Ltd: product lines "HD IP camera, HD coaxial camera, HD NVR, HD DVR"; news items Sept 2025 Network Optix partnership, Jan 2025 "NDAA Compliance Statement" (news/1106 — image only, text not extractable → content NOT used). Search excerpt (YouTube channel): "established in 2004 and headquartered in Shenzhen". | §5 para 1; §10 intro; §10.5 Claim 4 (statement exists, contents not relied on); §Sources |
| A5 | `Super Live Plus app TVT DVR NVR "SuperLivePlus"` · WebSearch | https://www.mysecuresystems.com/wp-content/uploads/SuperLivePlus-User-Manual.pdf (scraped, PDF parser, 16 pp.) | SuperLive Plus V1.0 User Manual: functions Live View, Remote Playback, Local Setting, Remote Setting, Local Record & Playback; "Optimizing the P2P connection"; H.265 added; gesture lock; sharing (screenshot, device, download address). WLAN: "Make sure your phone network and device network are in the same network segment on LAN." Cellular: PPPoE / static WAN / LAN IP + port forwarding in router "virtual server" ("If you has enabled the UPnP function in both the device and router, you can skip this step"). QR login: "My device is the MAC address (or serial number) of the device"; "If the device and the mobile client are in the different network segment, the device shall support QRCODE and enable the NAT." Domain/IP login example "123.dvrdydns.com:89". Old default "admin" / "123456". Live view indicators (sensor, manual, motion, schedule, video loss). Resolution choices CIF/D1/Super/Custom bitrate & frame rate; speed-up function for 720P+. Remote playback "record saved in the HDD(s) of the device"; single-frame, forward, rewind. Local Setting: Reserved disk space 50/100/200/500 MB, Record recycle (auto-deletes old local records), audio/shake alarm on video loss/sensor/motion, Launch setting, gesture password, Auto syn (device list synchronised and carried into new app versions; manual "Syn"). Server List: green = connected, grey = not connected, twinkling = connecting; press and hold QR to share device. File management, local playback, Help/Feedback (Type: DVR), About "Detect new version". | §5 para 2; §Repair table; §6 cards; §7.5; §9 A, C, D H3s; §10.5 Claims 1, 2, 5; §12 steps; §17 FAQ 6; §Sources |
| A6 | `SuperLive Plus app device offline TVT` · Firecrawl search → scrape | https://videos.cctvcamerapros.com/support/topic/superlive-plus-mobile-app-offline | CCTV Camera Pros (June 6, 2025): SuperLive Plus is "used with Viewtron security camera systems (DVRs, NVRs, and IP cameras)". Customer visiting Canada saw OFFLINE although NVR fine; fix: "change the DOMAIN (within the SUPERLIVE PLUS app) to match the region"; path "SETTINGS > LOCAL > select DOMAIN … set the DOMAIN to GLOBAL/AUTONATGLB.COM". | §9 E H3 (travel abroad); §10.5 Claim 1; §Sources |
| A7 | `TVT Digital Technology …` (same search) → scrape | https://videos.cctvcamerapros.com/support/topic/nat-setup-viewtron-dvr-nvr-web-interface | (Sept 30, 2026) NAT path on Viewtron recorder web UI: Settings (Function Panel) > Network > NAT; scan QR in SuperLive Plus (Live screen > QR Scan), type password manually; "green Wi-Fi signal" then Play. Viewtron web default admin / a1111111. IPTOOL finds recorder IP from a PC on the same network. | §6 NAT card; §9 A H3 3; §12 step 3; §10.5 Claim 5; §Sources |
| A8 | `apps.apple.com …` (excerpt) | https://superliveplus.net/ | Unofficial site repeating the Play description. NOT used (not the maker). | — |

#### 1.3 Reddit / forums (R) — excerpts only
| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com "superlive plus" cameras` · Firecrawl search | https://www.reddit.com/r/tinycam/comments/glptdp/superlive_plus/ | "Cameras supported by SuperLive Plus app will not work in tinyCam app." | §9 E H3 (third-party apps); §Sources |
| R2 | same | https://www.reddit.com/r/homesecurity/comments/1brss3t/remove_access_from_superlive_plus/ | "I gave my roommate access to our cctv camera footages through superlive plus. Recently they moved out…" | §9 C H3 (revoke access); §Sources |
| R3 | same | https://www.reddit.com/r/homesecurity/comments/aqcv2h/security_camera_software_question/ | Recommended remote viewing "NVMS-1000 and SuperLive Plus. I never, ever, ever have a remote connection" | §5 para 2; §Sources |
| R4 | same | https://www.reddit.com/r/SecurityCamera/comments/1h3n93v/dhcp_failure/ | "using the SuperLive plus app … for over a year … no longer showing a green WiFi symbol" (title "DHCP : failure") | §Repair table (DHCP row); §9 B H3; §Sources |
| R5 | same | https://www.reddit.com/r/cctv/comments/1lofnhg/help_upgrading_dead_dvr_looking_for_better_mobile/ | Horizontal scroll timeline "like SuperLive Plus, Reolink" vs vertical. | §9 D H3 (playback scrubbing) background; §Sources |
| R6 | same | https://www.reddit.com/r/UnifiProtect/comments/1wxncgd/multi_cam_playback/ | "I currently use SuperLive Plus where i can playback all cams at the same time if i scrub." | §10.5 Claim 3 (balance); §Sources |
| R7 | same | https://www.reddit.com/r/selfhosted/comments/1iazt9h/is_there_an_app_to_consolidate_all_cctv_on_a/ | Owner with Ezviz, Hikvision, iDMSS plus, Superlive Plus apps for different DVRs. | §9 E H3; §Sources |
| R8 | same | https://www.reddit.com/r/homedefense/comments/ibiv26/dvr_question_is_someone_spying_on_me_through_my/ | "Superlive Plus and HiSharp look like apps to VIEW the cameras, but that's not the DVR system". | §10.5 Claim 6 background; not quoted |
| R9 | `SuperLive Plus app device offline TVT` (excerpt) | https://www.cctvforum.com/topic/58642-tvt-supercam-plus/ | "device off line"; "SuperLive is far worse in my experience, and would never connect even on NAT." | §10.5 Claim 1 background; §Sources |

#### 1.4 Rules, ISPs, registry (G) — silo-usable
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `FCC covered list` · Firecrawl scrape (directQuote) | https://www.fcc.gov/supplychain/coveredlist | Video-surveillance entries name Hytera, Hangzhou Hikvision and Dahua (all March 12, 2021), plus Huawei/ZTE telecom; newest entry Digitalsystem Technology (July 7, 2026). TVT not among the entries returned. | §10.5 Claim 4; §8.5 bullet; §Sources |
| G2 | carried (research/hik-connect-app-support-repair.md F1; not re-fetched) | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment | July 2026 FCC order on covered equipment; continued use of owned equipment unaffected. | §10.5 Claim 4 (one clause) |
| G3 | `Optimum Altice gateway port forwarding security camera DVR remote viewing stopped working new router` · Firecrawl search (excerpts) | https://www.optimum.net/pages/internet/features.html ; https://www.reddit.com/r/OPTIMUM/comments/1lr3v63/how_do_i_actually_actually_access_my_router_for/ | Optimum: "lets you manage your router settings online, from any location … Port Configuration Settings". r/OPTIMUM: "Call and have them push the config to your new modem, they'll need the mac address". | §9 A H3 1, 3; §10.5 Claim 5; §Sources |
| G4 | `site:reddit.com r/longisland security cameras app offline Optimum OR Fios DVR` · Firecrawl search (excerpt) | https://www.reddit.com/r/OPTIMUM/comments/14qqz2u/how_to_assign_24_to_devices_on_an_automatic_24_5/ | Optimum router "automatically assigns 2.4 or 5"; "2.4 devices are constantly switching back and…". r/longisland Super Live Plus threads: EMPTY. | §7 card (Wi-Fi cameras); §Sources |
| G5 | `dos.ny.gov` · Firecrawl scrape (directQuote) | https://dos.ny.gov/get-security-or-fire-alarm-installer-license | NYS DOS security/fire alarm installer licence: age 18, fingerprints, at least 81 hours qualifying education, examination; master electrician waiver. | §8.5 bullet 1; §Sources |
| G6 | `site:reddit.com "superlive plus"` | — | Google Play reviews used as the 1–3★ substitute (A1). | — |

#### 1.5 Keyword plan (five layers)
- **Service:** Super Live Plus support, SuperLive Plus repair, Super Live Plus setup, SuperLive Plus remote viewing, Super Live Plus app help, TVT DVR app support, SuperLive Plus NAT setup, Super Live Plus access sharing.
- **Problem:** SuperLive Plus offline / grey icon, works on Wi-Fi not on cellular, router swap, port forwarding lost, DHCP failure, domain setting abroad, playback jumps, app crash on clip, signs out, default password, roommate/tenant still has access, phone storage full.
- **Technology:** TVT DVR/NVR, NAT/P2P, QR code, serial/MAC, IP + port, DDNS, UPnP, H.265, sub/main stream, Auto syn, Reserved disk space, Record recycle, gesture lock, Server List, Viewtron, SuperCam Plus, SuperLiveNVR, NVMS2, IPTOOL, LTE router.
- **Industry:** homeowners, seasonal/second-home owners, landlords with accessory apartments, strip-centre shops, offices, marinas/farms.
- **Geographic (LI hub):** Long Island, Nassau, Suffolk, Levittown, Garden City, East Garden City/Old Country Road, Uniondale, Hempstead Turnpike, Jericho Turnpike, Sunrise Highway, Route 110, Hauppauge, Ronkonkoma, Riverhead/Route 58, East Hampton, North Fork, South Fork, Montauk + §13 list. All image alt/title carry "Super Live Plus" + "Long Island".

#### 1.6 Pricing (no invented prices) — FLAG
Old Super Live Plus pages publish **no dollar prices** (checked old LI page; no `$` figures in body). Following the Hik-Connect / Smart PSS precedent: $0 phone/screenshot triage; protected service rate **$195/hr, 3-hour minimum ($585)** (v2.3 §9) — not multiplied; recorder replacement **borrowed from DVR Upgrade silo base** (research/dvr-upgrade.md §1.8: 4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+) × Nassau 1.15 / Suffolk 1.20, Decimal round half-up:
| | 4-ch | 8-ch | 8-ch hybrid | 16-ch | 32-ch |
|---|---|---|---|---|---|
| Nassau 1.15 | $518–$805 | $748–$1,150 | $920–$1,380 | $1,380–$2,530 | $2,530+ |
| Suffolk 1.20 | $540–$840 | $780–$1,200 | $960–$1,440 | $1,440–$2,640 | $2,640+ |
FLAG for Anwar: (1) recorder figures are BORROWED from the DVR Upgrade silo; (2) whether $195/hr should carry county multipliers; (3) "$0 triage" is a framing, not a published price.

---

### Question register (Super Live Plus silo)

#### Old template — every old sibling page (16 identical, read 2026-10-18 with check_page parser)
1. 🔧 Super Live Plus Offline Right Now? 2. Is Super Live Plus a camera brand? 3. Why does Super Live Plus say "device offline"? 4. Is Super Live Plus the same as SuperCam Plus or Q-See QT View? 5. Why can't I see live view or playback? 6. Can you recover my Super Live Plus password? 7. Why aren't my push notifications working? 8. Do you fix Super Live Plus systems you didn't install? 9. How much does Super Live Plus repair cost? 10. What areas do you cover?
Intents to avoid as generic questions: what SL+ is / brand; generic offline; SL+ vs SuperCam Plus/QT View; generic live/playback failure; password recovery; push notifications; systems not installed by us; cost; coverage area.

#### super-live-plus-app-support-repair-long-island (rebuilt 2026-10-18) — see the page; listed in full below after the build.
(Listed in full in "LI page questions" at the end of this file.)

---

### Long Island

#### Mandatory sources for this geo
Reddit r/longisland: EMPTY for Super Live Plus (G4). PAA/PASF/ATP/AI Overview/Bing/DDG: EMPTY (not accessible in build env). Yelp: EMPTY (listings only). News: PSEG LI (LI-P1), NCPD (LI-N3). Hyperlocal: Garden City PD (LI-N2).

#### Building stock / geography (LI-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-H1 | re-checked (first found research/nvr-installation.md LI-H1) · Firecrawl scrape directQuote | https://kerimurrayarchitecture.com/levittown-ny/ | "Built between 1947-1951"; "built on concrete slabs"; "In all, 17,447 homes were constructed in Levittown between 1947 and 1951." | §5 para 2; §5.5; §7 slab card; §13 Levittown; §Sources |
| LI-H2 | re-checked (nvr LI-H3) · Firecrawl scrape | https://www.ny.gov/counties/nassau | "453 sq miles"; "Two cities, three towns, 64 incorporated villages, and more than 60 unincorporated hamlets". | §Counties; §5.5; §Sources |
| LI-H3 | re-checked · Firecrawl scrape | https://www.ny.gov/counties/suffolk | "2373 sq miles"; "easternmost county … divided into 10 towns: Babylon, Brookhaven, East Hampton, Huntington, Islip, Riverhead (county seat), Shelter Island, Smithtown, Southampton and Southold." | §Counties; §5.5; §13 Riverhead; §Sources |
| LI-H4 | re-checked (nvr LI-H4) · Firecrawl scrape PDF parser 72 pp., directQuote | https://www.ehamptonny.gov/DocumentCenter/View/28279/Route-114-Affordable-Housing-Market-Study-and-Update | PDF title "East Hampton - Market Assessment - 3.16.26": "With a total of 44,227 housing units, 17,993 (41%) are owner-occupied (primary residence) while 20,952 (47%) are used for seasonal, recreational, or occasional." Also "57%" of workforce commutes into the study area (not used). | §5 para 3; §5.5; §7 seasonal card; §13 East Hampton; §Sources |

#### Power (LI-P)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-P1 | re-checked (nvr LI-P1) · Firecrawl scrape directQuote ×2 | https://www.psegliny.com/en/Newsroom/2025/092826-StormUpdate0800 | "(UNIONDALE, N.Y. – Sept. 28, 2026)"; >95% restored; "6,108 of 1.2 million electric customers across Long Island and the Rockaways"; "Over the course of 72 hours, the storm caused more than 124,000 outages."; "More than 1,150 trees and nearly 700 large branches fell."; "More than 1,350 local and off-Island field workers"; "16-hour shifts". (URL path /2025/, body dated 2026.) | §5 para 3; §5.5; §9 B H3; §13 Uniondale; §10.5 Claim 2; §Sources |

#### Internet (LI-I)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-I1 | re-checked (nvr LI-I1) · Firecrawl scrape directQuote | https://alticeusa.com/node/3151 (resolves to optimum.com/about-us/news/…long-island-additional-40m-investment) | "(OCTOBER 1, 2024)" $40M additional investment; fibre "available to over 2.8 million passings across the New York tri-state area – including nearly 900,000 fiber passings on Long Island". | §5 para 4; §5.5; §9 A H3 1; §Sources |
| LI-I2 | G3 / G4 | — | Optimum router settings online / port configuration; band steering complaint. | §9 A; §7 |
| — | Verizon Fios LI availability, Comptroller broadband gap | carried in research/nvr-installation.md LI-I2/I3 — NOT re-checked → not used as figures; Fios named only as a provider. | — |

#### Police / news (LI-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-N1 | re-checked (nvr LI-N1) · Firecrawl scrape directQuote | https://scpdshield.org/Initiatives | Camera Registry Program "allows citizens and business owners to register the locations of their video surveillance systems"; SCPD may "request program participants to check their video surveillance system for a specific date and time"; retrieval "at the convenience of the camera owner". Integrated Emergency Response System: remote access to "previously authorized I.P. based video monitoring systems" only "in the event of a true emergency, such as an active shooter attack, hostage situation or other immediate threat to life and property"; "opt into or out of the program at any time". | §5 para 4; §5.5; §8.5; §9 C H3 (registry); §10.5 Claim 7; §Sources |
| LI-N2 | re-checked · Firecrawl scrape directQuote | https://gardencitypolice.net/private-camera-reg | "strictly voluntary and does NOT provide us access to security camera systems that are privately owned by participants"; detectives "may ask to inspect your surveillance video recorded during a finite period". Page metadata: 349 Stewart Ave, Garden City, NY 11530. | §9 C H3; §10.5 Claim 7; §13 Garden City; §Sources |
| LI-N3 | re-checked · Firecrawl scrape directQuote | https://www.pdcn.org/CivicAlerts.aspx?AID=14776 | Posted Jan 16, 2026: burglary Wed Jan 14, 2026, 10:30 p.m.; subject entered "the delivery station in the rear of the Nordstrom Rack located at 1040 Old Country Road through an unlocked door and removed merchandise"; video released. (Store not named on page.) | §8 Old Country Road card; §13 card; §Sources |

#### Licensing (LI-K)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| LI-K1 | G5 | dos.ny.gov | State licence requirements. | §8.5 |
| LI-K2 | carried research/nvr-installation.md LI-K1/K2 (not re-checked) | nassaucountyny.gov/1547 ; suffolkcountyny.gov Consumer Affairs | County consumer-affairs offices license home improvement contractors. Used only as "each county has its own consumer-affairs office" (generic) — FLAG. | §8.5 bullet 2 |

#### Places (LI-L)
Levittown (LI-H1); Garden City / 349 Stewart Ave (LI-N2); Old Country Road, East Garden City (LI-N3); Uniondale (LI-P1 dateline); Riverhead county seat (LI-H3); East Hampton (LI-H4). Corridor names (Hempstead Turnpike, Jericho Turnpike, Sunrise Highway, Route 110, Route 58, Hauppauge, Ronkonkoma, Montauk Highway, LIE, LIRR) used as place names only — FLAG: no per-corridor source; Hauppauge park numbers carried in nvr research were NOT confirmed today (cmmllp page returned no text) → not used.

#### Images (11) — Drive: no Super Live Plus folder; CompanyCam not connected → permanent image rule
Viewed each (contact sheets + full Read). Rejected: ulster live-view tile with a parked car (possible plate), duplicate crops of the same scenes (fascia-corner family, storeroom family, bitrate-table family), Nassau monitor tiles with people. Captions say what is visible and that the photo is from an AESS job/example or a manufacturer product photo; none claims Long Island, a customer, or the Super Live Plus app.
| Output (images/super-live-plus-app-support-repair/super-live-plus-app-support-repair-long-island-…) | Source |
|---|---|
| wall-monitor-camera-grid-below-ceiling-cables.webp | images/nvr-installation/nvr-installation-bronx-recorder-monitor-camera-grid-under-cable-runs.webp |
| night-playback-tile-brick-wall-and-paved-lot.webp | images/nvr-installation/nvr-installation-bronx-recorder-playback-brick-wall-to-lot.webp |
| infrared-channel-view-of-storeroom-doorway.webp | images/nvr-installation/nvr-installation-bronx-recorder-tile-dim-back-storeroom.webp |
| store-monitor-tiles-of-shop-aisles.webp | images/lorex-camera-installation/lorex-camera-installation-manhattan-monitor-tiles-of-shop-aisles-and-shelving.webp |
| patch-cable-bundles-down-equipment-rack.webp | images/nvr-installation/nvr-installation-staten-island-patch-cable-bundles-down-equipment-rack.webp |
| network-cables-crossing-ceiling-beam.webp | images/lorex-camera-installation/lorex-camera-installation-long-island-loose-blue-and-white-network-cables-crossing-ceiling-beam.webp |
| ceiling-camera-near-lit-exit-sign.webp | images/nvr-installation/nvr-installation-long-island-ceiling-camera-near-lit-exit-sign-in-office.webp |
| white-dome-camera-at-fascia-corner-against-sky.webp | images/nvr-installation/nvr-installation-long-island-dome-camera-at-fascia-corner-against-sky.webp |
| turret-camera-in-storeroom-ceiling-corner.webp | images/nvr-installation/nvr-installation-bronx-turret-camera-storage-room-corner.webp |
| dome-camera-on-wall-arm-over-stone-facade.webp | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-dome-camera-on-long-wall-arm-over-stone-facade.webp |
| recorder-front-and-rear-ports-product-photo.webp | images/nvr-installation/nvr-installation-long-island-swann-recorder-front-and-rear-poe-ports-product-photo.webp (Swann product photo — not a TVT recorder; caption says so) |
DAILY-LOG note: `images: 11 reused from images/nvr-installation/, images/lorex-camera-installation/ (no real Super Live Plus photos yet)`.

#### FLAGS (LI hub)
1. Prices: recorder replacement borrowed from DVR Upgrade base × 1.15/1.20 (see 1.6).
2. House practices stated without external source (installer knowledge): NAT preferred over port forwarding; reserved DHCP address; recorder/router boot order after outages; battery units; cellular router backup; changing shared logins to revoke access; per-person recorder users; exporting from recorder rather than phone for police; seasonal-house checklist; one- to two-hour on-site fix time; two-hour arrival windows 8 AM–8 PM; "dispatched from Brooklyn".
3. TVT NDAA statement (Jan 14, 2025) is an image; its contents were not read or relied on.
4. FCC Covered List check returned the video-surveillance entries only; TVT absence stated as "not among the entries we read on October 18, 2026".
5. Field Notes are Anwar-voice general method, not a specific job story — confirm or replace with a real island anecdote.

---

### LI page questions (super-live-plus-app-support-repair-long-island, rebuilt 2026-10-18)

**§9 Q&A question H3s (8):**
1. Optimum swapped our gateway during a fibre upgrade and the recorder dropped out of Super Live Plus — what did the new box change?
2. Our cameras play on the kitchen Wi-Fi but go grey as soon as the phone is on cellular — why only at home?
3. Fios installed a new router and our old port-forwarding rules are gone — should we rebuild them or switch the recorder to NAT?
4. Out east our address has only one wired provider — can a cellular router keep Super Live Plus reachable?
5. After PSEG restored power the recorder came back, but its clock is wrong — does that matter for the app?
6. How can we tell from Florida or the city whether the recorder at our East End house is still recording?
7. When we close the house for the winter, what should stay powered for Super Live Plus to keep working?
8. Our shop’s recorder shares the internet with the card terminal — can watching the app from home slow down payments?

**§9 statement H3s (non-questions, converted after reading the parallel Manhattan and Bronx pages at 13:15–13:17Z):** Taking the cameras back from a tenant who has moved out of the accessory apartment (Manhattan: roommate moved out); Sharing the driveway view with family in the city, without sharing your login (Manhattan: family abroad); Installation-day passwords that were never changed (Manhattan: factory password); What the Suffolk and Garden City camera registries do, and do not, give police (Manhattan: Connect New York log-in); Find the moment on the phone, export it from the recorder (Manhattan: detective asked for video; Bronx: back up a clip); When the app starts filling the phone (Manhattan: where do clips end up); Rebadged recorders: checking that Super Live Plus is the right app (Manhattan: dealer sticker); All-in-one camera apps and TVT-made recorders (Manhattan: VLC / home-automation hub); Offline only while you are abroad: the Domain setting (Manhattan: Domain before travelling); A Nassau store and a Suffolk store on one phone (Manhattan: walk-up and store on one phone); Three photos and two screenshots save most of a visit (Manhattan: what to have on hand).

**§17 FAQ (9, = FAQPage):**
1. Can you set up the app for a caretaker who looks after several East End houses?
2. Will updating the app on our phones break the link to an older recorder?
3. Our house is already monitored by an alarm company — will your work on the cameras interfere with it?
4. Does somebody need to be at the house, or can you fix it remotely?
5. Our recorder is several years old — how do we know whether it still works with the current app?
6. Is it safe to give your technician the recorder’s admin password?
7. What happens to our recorded footage if the recorder has to be replaced?
8. Can a relative who prefers another language use Super Live Plus?
9. Can we move the recorder to our other house and keep the same app setup?
(Dropped after reading Manhattan: "subscription / cloud" (Manhattan: subscription fee; data to developer) and "iPad or computer" (Manhattan: Mac at the front desk). Dropped "how long does an on-site repair take" — masked 0.69 vs an old-template line.)

**§10.5 claim H3s:** "Device offline means your internet is down"; "Just reboot the recorder and it will reconnect"; "Delete the app and reinstall it"; "Super Live Plus recorders are banned like Hikvision"; "Forward the recorder’s ports on your router and the app will work"; "The app stores your video in the cloud"; "Registering with the police lets them watch your cameras".

**Borderline intents kept (FLAG):** Q1 (after a gateway swap) vs Bronx "installer is coming to put in a new gateway — what should we let them change" (before vs after); Q2 (works on Wi-Fi, not cellular) vs Manhattan "phone lists the recorder by an IP address — move it to the serial?" (symptom vs remedy; this is the LI thesis); Q3 (rules wiped by a new router) vs Manhattan "installer forwarded ports years ago — still open?" (lost vs lingering).

**Intents this page owns:** ISP gateway swap after the fact; local-address-only device on cellular; rebuilding vs replacing port forwarding after a router change; cellular router for single-provider addresses; recorder clock after outage; remote proof-of-recording for a seasonal house; what stays powered in a closed house; app viewing vs card-terminal bandwidth; caretaker for several houses; alarm-company coexistence; app updates vs older recorders; remote vs on-site fix; old recorder vs current app; giving the admin password; footage on replacement; app languages; moving the recorder between houses.

**Masked similarity (difflib on masked word lists, blocks ≥8 words) vs all 15 siblings incl. the new Bronx/Manhattan pages:** no body block ≥0.65; remaining matches are blueprint-fixed H2 patterns only ("Why … Properties Need …", "… for …'s Architecture", "Types of … We Install", "What AI Gets Wrong …", "… Near …'s Landmarks", "Every … Service on …", "… Across … and the …", "… Questions Answered").


## Manhattan — REBUILD batch 2026-10-18 (super-live-plus-app-support-repair-manhattan): silo findings, question-register additions and local research

## Super Live Plus App Support Repair — silo research (incoming, Manhattan rebuild)

Written 2026-10-18 by the subagent rebuilding `super-live-plus-app-support-repair-manhattan` (queue line: `REBUILD | super-live-plus-app-support-repair-manhattan | Super Live Plus App Support Repair | Manhattan | up /super-live-plus-app-support-repair-nyc | direct phone (929) 560-0737 | GBP Bronx`). `research/super-live-plus-app-support-repair.md` does not exist; this file sits in `research/_incoming/` for the main run to merge with the Bronx and Long Island part files built in the same batch (merge, don't duplicate silo rows).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search/scrape (`mcp__Fire_Crawl__*`, markdown / query mode / PDF parser), WebSearch, WebFetch. Shell curl blocked. "Excerpt" = read only as a search-result snippet. Firecrawl does not open reddit.com pages → Reddit rows are excerpts.

Page section labels (Manhattan page): §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts), §Repair (same-day block + checks + symptom table), §6 Services (+ before/after table), §7 Architecture (+§7.5 method), §8 Commercial (+ single-location set-up, §8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ brand table, connection table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process (+ leave-behind list), §13 Landmarks, §14 Pricing (+ time table), §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

**Manhattan thesis:** *Super Live Plus has no cloud account — the recorder's own user name and password are the key, and in Manhattan the recorders behind it are anonymous white-label TVT-family boxes in walk-ups, tenement storefronts, small-landlord buildings and shared apartments.* The job is (1) identify the real hardware family behind the dealer sticker, (2) take the recorder off the open internet (remove port forwards/UPnP, move phones to the NAT serial-number path, check firmware against the TVT-family CVE record), (3) rebuild access as one named user per person so departures (roommates, staff, agents) are one deletion, changing access *last*, and (4) handle footage leaving the building (detectives, insurers, Connect New York, the Lower Manhattan camera network). Distinct from the Hik-Connect Manhattan thesis (cloud-account ownership transfer + FCC order) and the SmartPSS Manhattan thesis (desk PC on someone else's network).

---

### Part 1 — Silo-wide findings

#### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows R1–R6). |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and works from claims repeated on app-help sites/forums (rows A1–A4, I1–I4). |
| 6 | Area landmarks | Manhattan section M-L1–M-L6. |
| 7 | Area use cases / building stock | M-H1, M-H2, M-L3, M-L4. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only WebSearch/Firecrawl backends; no Bing/DDG PAA, related or autocomplete surface. |
| 9 | Local news | M-N1 (Gothamist). |
| 10 | Hyperlocal | EMPTY for Super Live Plus specifically (no Manhattan hyperlocal item about the app surfaced). |
| 11 | Yelp 1–3★ | `yelp security camera repair Manhattan NY review DVR app stopped working 1 star` · Firecrawl search → only Yelp search-listing pages (e.g. https://www.yelp.com/search?find_desc=Security+Camera+Repair&find_loc=Central+Park%2C+Manhattan%2C+NY "Rating 4.4(1,597)"); no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

#### 1.2 The app (A)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | direct scrape · Firecrawl | https://play.google.com/store/apps/details?id=com.tvt.superliveplus | Title "SuperLive Plus"; developer link "Peng AnTai"; 3.3★, 53.3K reviews; 5M+ downloads; price 0; description "a professional mobile phone client software for digital video recorders and IP cameras in CCTV surveillance (compatible models only)"; updated Oct 8, 2026; what's new "Support account switching / Fixed some known issues"; data safety "No data shared with third parties", "No data collected"; privacy policy at autonatglb.com; "About the developer: TVT (HK) LIMITED", Rm 2102 Wang Cheong Enterprises Ctr, 65-69 Chai Wan Kok St, Tsuen Wan, Hong Kong; other Peng AnTai apps SuperLiveNVR, NVMS2 Plus, NVMS2. Reviews quoted on listing: 2020 crash during clip recording; "Doesn't connect on mobile reliably…"; 5/10/24 app signing off, fixed 6/2/24. | §5 para 1; §5.5; §10.5 H3 1, 5; §17 FAQ 1, 2, 10; §Sources |
| A2 | `Super Live Plus app TVT Shenzhen developer NVR DVR` · WebSearch → WebFetch | https://apps.apple.com/bb/app/superlive-plus/id1058758642 | Seller Peng AnTai; "SuperLive Plus is a specially developed monitoring software for the iPhone"; versions 1.16.x 2025–2026 (device sharing, full-duplex intercom); 4.0★ from 2 ratings (Barbados store); iOS 12.1+, Mac macOS 12.0+ with Apple M1 or later, "Designed for iPad. Not verified for macOS"; privacy: diagnostics not linked to user, "not been verified by Apple". | §6 desk card; §17 FAQ 2, 8; §Sources |
| A3 | `SuperLive Plus app server address region setting autonat` · Firecrawl search → scrape (PDF, query) | https://www.mysecuresystems.com/wp-content/uploads/SuperLivePlus-User-Manual.pdf | Add device by QR code, by IP+port on LAN, by WAN IP/domain; "Input my device (IP address/domain name), nick name, user and password"; default "admin" / "123456"; local settings: reserved disk space, record recycle, audio/shake alarm "when video loss/sensor/motion alarm occurs", snap, gesture password, auto sync; device sharing by pressing and holding the QR code; server list. | §5 para 2; §9 multi-property H3; §10.5 H3 6; §17 FAQ 3, 7; §Sources |
| A4 | `Super Live Plus app TVT Shenzhen developer NVR DVR` · WebFetch | https://www.cctv42.co.uk/uploads/media/1dce4cac596dbb91e357e29dc831ecb922f395e5.pdf | Older SuperLive Plus manual: live view, playback from DVR HDD, PTZ only if device supports it, local alarms (not push), remote setting menu varies by DVR, H.264/H.265. Manufacturer not named. | Background §10.5 H3 6 |
| A5 | `SuperLive Plus app server address region setting autonat` · Firecrawl scrape | https://videos.cctvcamerapros.com/support/topic/superlive-plus-mobile-app-offline | June 6, 2025: "SuperLive Plus is the iPhone and Android mobile app that is used with Viewtron security camera systems (DVRs, NVRs, and IP cameras)"; customer offline in Canada; fix "SETTINGS > LOCAL > select DOMAIN … set the DOMAIN to GLOBAL/AUTONATGLB.COM". | §Repair table; §10 brand table; §10.5 H3 7; §17 FAQ 5; §Sources |
| A6 | same search · Firecrawl scrape | https://keironcheesbrough.com/help/remote_viewing | UK installer: "Download one app — SuperCam Plus or SuperLive Plus"; package names com.tvt.superliveplus / com.tvt.supercamplus; add via Server list + IP/DDNS/SN; username admin; "Older systems were left on 123456 — change it"; Macs with Apple silicon can use SuperCam Plus from the Mac App Store; some older recorders use AutoNAT in a browser (IE mode). | §5 para 1; §10 brand table; §10.5 H3 1; §17 FAQ 7, 8; §Sources |
| A7 | `Super Live Plus device offline fix autonat server address` · WebSearch → WebFetch | https://forums.justuseapp.com/en/post/B4VZ25CGWS/device-offline | Eight generic steps: restart device, check network, force close, update app, reinstall app, permissions, restart router, contact support. No server names. | §10.5 H3 4; §Sources |
| A8 | `SuperLive Plus app TVT …` · WebFetch | https://www.2mtechnology.net/knowledge-base/which-phone-app-do-i-use-to-view-my-cameras-2mt-7232/ | 2MT-7232 → Super Live Plus (2MN-7116 → Guarding Vision). | §10 brand table; §Sources |
| A9 | `SuperLive Plus app server address region setting autonat` · Firecrawl scrape | https://community.home-assistant.io/t/superlive-plus-app-integration/553878 | Mar 2023: resident of "a block of flats" with Avision AV104T DVR uses SuperLive Plus Android app remotely; app shows HTTP, HTTPS, Server, RTSP ports; Sep 2023 reply: after finding "the manufacturer behind the Avision brand" a working RTSP format `rtsp://USERNAME:PASSWORD@IP:PORT/?chID=…&streamType=main&linkType=tcp`. | §5 para 1; §9 dealer-sticker H3; §10 brand table; §17 FAQ 6; §Sources |
| A10 | `TVT Digital Technology Shenzhen 002835 …` · WebSearch → WebFetch | https://securitycamcenter.com/?p=5312 | SuperLivePro/SuperLive Plus "generally used by generic H.264 DVRs and H.265 NVRs", often sold with no brand or dealer label; enable NAT on recorder; scan QR; default password usually 123456. | §10 brand table; §Sources |
| A11 | `Viewtron SuperLive Plus app NVR …` · WebFetch | https://videos.cctvcamerapros.com/?p=42576 | Viewtron VMS connects by serial number (recommended) or static IP ("we do not recommend"). | Background §10 connection table |

#### 1.3 The hardware maker (T)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `TVT Digital Technology Shenzhen 002835 surveillance company OEM` · WebSearch → WebFetch | https://www.morningstar.com.au/investments/security/SZSE/002835 | Shenzhen TVT Digital Technology Co Ltd (SZSE:002835): R&D, manufacture and distribution of video surveillance products — HD analog, IP and speed-dome cameras, NVR and hybrid DVR, software; 1,476 employees; HQ Nanshan, Shenzhen. | §5 para 1; §10 hybrid card; §Sources |
| T2 | same · WebFetch | https://www.security-essen.de/impetus_provider/exhibitor-list/detail/shenzhen-tvt-digital-technology-co-ltd-20fbf | "established in 2004"; DVRs, IP cameras, hybrid DVR/NVR, mobile DVR, CMS/phone apps; customers in "more than 120 countries". | §5 para 1; §Sources |
| T3 | `TVT NVR default server port 6036 http port 80 SuperLive Plus port forwarding` · Firecrawl search → scrape (PDF, query, 190 pp.) | https://tvtdigital.com.ua/wp-content/uploads/NVR-NV9000-_User_Manual.pdf | © Shenzhen TVT 2019. HTTP 80, HTTPS 443, server port 6036, RTSP 554; NAT / NAT2.0 enable → scan QR in mobile client; UPnP "convenient, but increases data leakage risk… disabling UPnP is recommended when not in use"; admin with no default password (set at first wizard); reset via security questions / recover to 123456 / users with "Account and Authority" permission; permission groups Administrator, Advanced, Ordinary, max 8 groups; allow/block lists; DDNS (e.g. www.dvrdydns.com). | §5 para 2–3; §5.5; §Repair; §6; §7.5; §9 clusters 1–3; §10 cards + connection table; §10.5 H3 2–3; §17 FAQ 7; §Sources |
| T4 | Firecrawl scrape (Keiron A6) | https://keironcheesbrough.com/help/remote_viewing | SuperCam Plus = com.tvt.supercamplus (sister app). | §10.5 H3 1 |

#### 1.4 Security record (S)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `SuperLive Plus vulnerability CVE TVT NVR` · WebSearch → WebFetch (NVD page returned only shell → cvefeed) | https://cvefeed.io/vuln/detail/CVE-2018-25126 | NVMS-9000 firmware "contains hardcoded API credentials and an OS command injection flaw in its configuration services"; fixed credential → /editBlackAndWhiteList → root; "firmware from mid-February 2018 onward addresses the issue"; vendor Shenzhen TVT; used in "many white-labeled DVR/NVR/IPC products"; CVSS 4.0 9.3 Critical; published Nov 24, 2025. | §5 para 3; §5.5; §9 TVT-flaws H3; §10.5 H3 3; §Sources |
| S2 | same · WebFetch | https://www.cvelogic.com/vendor/tvt | CVE-2025-34036 (2025-06-24) unauthenticated OS command injection in white-labeled TVT DVRs, "Cross Web Server" TCP 81/82; CVE-2024-7339 (2024-08-01) info disclosure `/queryDevInfo` in TD-2104TS-CL, TD-2108TS-HP, Provision-ISR SH-4050A5-5L(MM), AVISION AV108T, public exploit; CVE-2019-20085 NVMS-1000 directory traversal, listed in CISA KEV; CVE-2013-6023 TD-2308SS-B traversal. | §5 para 3; §9 TVT-flaws H3; §10 brand table; §10.5 H3 3; §Sources |
| S3 | `Manhattan lobby surveillance DVR hacked cameras exposed online…` · Firecrawl search → scrape (query) | https://www.securityweek.com/40000-unprotected-security-cameras-found-on-internet/ | June 11, 2025: Bitsight found >40,000 cameras worldwide exposing live feeds over HTTP or RTSP; advice: secure connection, replace default credentials, disable unneeded remote access, update, monitor logins. | §10.5 H3 3; §Sources |

#### 1.5 Forums / Reddit (R) — excerpts
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com "superlive plus" OR "super live plus" camera` · Firecrawl search | https://www.reddit.com/r/homesecurity/comments/1brss3t/remove_access_from_superlive_plus/ | "I gave my roommate access to our cctv camera footages through superlive plus. Recently they moved out and it wasn't a peaceful goodbye." | §5 para 2; §9 roommate H3; §Sources |
| R2 | same | https://www.reddit.com/r/tinycam/comments/glptdp/superlive_plus/ | "I am not the owner of the cameras, but I can view them using the SuperLive Plus app with P2P by providing a 12 characters long UUID, a username…" | §9 serial-vs-address H3; §Sources |
| R3 | same | https://www.reddit.com/r/SecurityCamera/comments/1h3n93v/dhcp_failure/ | Using SuperLive Plus over a year; app no longer shows green Wi-Fi symbol (DHCP failure). | Background §Repair table (address conflict row) |
| R4 | same | https://www.reddit.com/r/homesecurity/comments/aqcv2h/security_camera_software_question/ | Recommended remote software NVMS-1000 and SuperLive Plus — "I never, ever, ever have a remote connection". | Background §10.5 |
| R5 | same | https://www.reddit.com/r/homedefense/comments/ibiv26/dvr_question_is_someone_spying_on_me_through_my/ | "Superlive Plus and HiSharp look like apps to VIEW the cameras, but that's not the DVR system…" | Background §5 (app ≠ recorder) |
| R6 | carried from research/hik-connect-app-support-repair.md M-B4 (Firecrawl 2026-10-15) | https://www.reddit.com/r/NYCapartments/comments/1qjxeao/anyone_else_struggle_with_wifi_in_prewar_railroad/ | Poster in "a pre-war NYC railroad-style two bedroom apartment" with "ongoing WiFi issues". | §9 Wi-Fi-camera-by-the-door H3; §Sources |

#### 1.6 Other silo knowledge reused (sourced in other research files)
| # | Source file / row | URL | Finding | Used |
|---|---|---|---|---|
| X1 | research/dvr-upgrade.md G3; research/apartment-building-security-camera-installation.md | https://nysenate.gov/legislation/laws/PEN/250.05 | Eavesdropping, one-party consent; class E felony. | §8.5 |
| X2 | research/dvr-upgrade.md G1 | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a backyard video imaging device, private right of action. | §8.5 |
| X3 | research/smart-pss-support-setup.md M-K1 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-131285 | Admin Code §22-1202 biometric signage for retail / food and drink establishments; face geometry. | §8.5 |
| X4 | research/smart-pss-support-setup.md D/R rows (Dahua wiki, r/Dahua) | https://dahuawiki.com/SmartPSS_Lite | DMSS is Dahua's phone viewer (a different product). | §10.5 H3 1 |
| X5 | research/smart-pss-support-setup.md M-L5 | https://en.wikipedia.org/wiki/Canal_Street_(Manhattan) | Canal St East Broadway → West St; southern edge of SoHo/Little Italy, northern edge of Tribeca; open storefronts, banks, jewelry shops to the east. | §8 card; §13 card |

#### 1.7 Keywords — five layers (silo)
- **Service:** Super Live Plus support, SuperLive Plus repair, Super Live Plus setup, remote viewing setup, access audit, remove user access, port-forward clean-up, firmware update, footage export, recorder replacement.
- **Problem:** Super Live Plus not connecting, offline abroad / Domain setting, login refused, former roommate/employee still has access, shared admin password, default 123456 password, exposed ports, UPnP, factory reset lost users, Wi-Fi camera dropping, alerts all night.
- **Technology:** TVT / TVT (HK), Peng AnTai, com.tvt.superliveplus, SuperCam Plus, NVMS-9000 / NVMS-1000, NAT / NAT2.0, serial number / QR, autonatglb.com, ports 80 / 6036 / 554 / 81–82, RTSP, DDNS, hybrid DVR, NVR, PoE, CVE-2018-25126, CVE-2024-7339, CVE-2025-34036, CVE-2019-20085.
- **Industry:** small landlords, walk-ups, rent-stabilized buildings, tenement storefronts, delis/bodegas, restaurants, salons, small offices/studios, shared apartments, managing agents.
- **Geographic (Manhattan page):** Manhattan; Canal Street; Chinatown (Mott, Grand, East Broadway); Lower East Side (Orchard Street, Delancey, Essex Crossing, Essex Market, 97 Orchard St); Washington Heights (St. Nicholas Ave, 181st St, GWB, Dyckman St); Lower Manhattan / Community District 1; East Village; Harlem; plus the "also serve" list.

#### 1.8 Silo pricing (no invented prices) — FLAG
The 16 old Super Live Plus pages publish no recorder-replacement figures. The Manhattan page uses only: $0 photo/screenshot review; protected service rate $195/hr, 3-hr minimum ($585) (v2.3 §9, verbatim, not multiplied); recorder replacement = **borrowed** DVR Upgrade silo base (research/dvr-upgrade.md §1.8) × Manhattan 1.25: 4-ch $563–$875, 8-ch $813–$1,250, 8-ch hybrid $1,000–$1,500, 16-ch $1,500–$2,750, 32-ch $2,750+ (same figures as the rebuilt Hik-Connect and SmartPSS Manhattan pages). **FLAG for Anwar: confirm the Super Live Plus silo may borrow the DVR Upgrade replacement prices.** The "where the three hours go" time table (§14) contains planning durations only, no prices. DHCR MCI figures ($2,556/camera etc.) are quoted as DHCR's reasonable-cost ceilings, explicitly "not our prices".

---

### Question register — Super Live Plus App Support Repair silo

#### Old shared template (identical on all 16 pages before rebuild, incl. old Manhattan)
Is Super Live Plus a camera brand? · Why does Super Live Plus say "device offline"? · Is Super Live Plus the same as SuperCam Plus or Q-See QT View? · Why can't I see live view or playback? · Can you recover my Super Live Plus password? · Why aren't my push notifications working? · Do you fix Super Live Plus systems you didn't install? · How much does Super Live Plus repair cost? · What areas do you cover? · (heading) Super Live Plus Offline Right Now?
**Intents reserved by the register (not used as questions on Manhattan):** what-it-is/brand; generic device offline; SuperCam/QT View sameness; live view/playback failure; password recovery; push notifications; non-AESS systems; cost; coverage area.

#### Manhattan page (new) — §9 Q&A (H3)
1. A roommate moved out of our East Village apartment — how do we stop the cameras showing on their phone?
2. The landlord, the handyman and two shopkeepers all use the same admin login — what does splitting that up involve?
3. Can a tenant be shown one hallway camera without seeing the rest of the building?
4. The building changed managing agents — does the old agent's phone keep working until someone acts?
5. Our installer forwarded ports on the router years ago — are they still open, and do we still need them?
6. How do we tell whether our white-label recorder carries one of the TVT flaws published since 2018?
7. Is switching UPnP on a reasonable shortcut for getting the app working?
8. The recorder carries a sticker from a dealer we've never heard of — how do you work out who made it?
9. For a Manhattan shop, is it better to add the recorder to phones by serial number or by its address?
10. A detective asked for last night's video from our storefront — can we send it from the phone app?
11. Can a recorder our staff view in Super Live Plus be linked into Connect New York, and what do we keep control of?
12. If we only register our cameras with Connect New York, can police log in to them?
13. If the landlord replaces the camera system in a rent-stabilized building, can that turn into a rent increase?
14. Our four-family walk-up has no super on site — who should hold the recorder's administrator password?
15. Can a deli owner watch the register camera while the counter staff can't change any settings?
16. The small-business security tax credit — can we still claim it for a camera repair?
17. A counter worker used a personal phone to watch the shop — what should happen on their last day?
18. We own a walk-up in Harlem and a store on Orchard Street — how do we keep the store manager out of the building's cameras?
19. Family members abroad want to see the store — is that safe?
20. How many people can sensibly share one recorder?
21. Our apartment uses Wi-Fi cameras added straight to the app, with no recorder — does any of this apply?
22. A Wi-Fi camera that worked on the kitchen counter keeps dropping once it's mounted by the door of our pre-war apartment — why?
23. Should the cameras share the Wi-Fi network our laptops use?
24. What should the owner have on hand when the technician arrives?
25. Can the work be done while the store stays open?

#### Manhattan page (new) — §17 FAQ (= FAQPage schema, 10)
1. Why does the app store show a person's name, not a company, as the Super Live Plus developer?
2. Does Super Live Plus send our camera data to the app developer?
3. Where do clips recorded inside the app end up?
4. How many days of video can our recorder keep?
5. Should a New Yorker change the app's Domain setting before travelling abroad?
6. Can the same recorder also feed VLC or a home-automation hub?
7. How can we tell whether our recorder still has its factory password?
8. Can Super Live Plus run on a Mac at the front desk?
9. What happens to the cameras if the building's internet goes down?
10. Is there a subscription fee for Super Live Plus?

#### Semantic de-dup vs the parallel Bronx and Long Island rebuilds (read from disk 2026-10-18)
- LI "caretaker for several East End houses" ↔ Manhattan multi-property question → Manhattan reframed to *keeping the store manager out of the building's cameras* (permission isolation, Q18).
- LI "kitchen Wi-Fi works, grey on cellular" ↔ Manhattan IP-vs-serial question → Manhattan reframed as a *choice of method for a shop* (Q9).
- Manhattan Q&A "family abroad" no longer answers the Domain intent (points to FAQ 5) so that intent is answered once.
- Kept distinct after review: Bronx "son set up the app on his account" (cloud accounts) vs Manhattan (none); Bronx "QR sticker photographed" vs Manhattan (statement only, no question); Bronx "buses and headlights alerts" vs Manhattan §10.5 H3 6 (claim heading, not a question); LI "Fios new router, rebuild forwards or NAT" vs Manhattan Q5 (exposure audit of forwards still open).
- Masked paragraph similarity (SequenceMatcher on geo-masked p/li/td/h3 blocks ≥12 words): first draft had 7 blocks ≥0.65 vs LI (instant-action bullet, Domain table cell, two pricing cells, calculator line, mid-CTA, package card, complete-services intro) — all rewritten; final re-run (after the Bronx and LI pages' latest saves) shows no block ≥ 0.62 vs any of the 15 siblings (highest 0.62, warranty sentence vs an LI hand-over paragraph).

---

### Manhattan

#### M-H Housing / building stock
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-H1 | `Rent Guidelines Board housing supply report Manhattan rent stabilized units number by borough 2025` · Firecrawl search → scrape (PDF, query) | https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/housing-and-buildings/2026/2026-may-segments-of-the-rent-stabilized-housing-stock.pdf | ~928,000 rent-stabilized apartments across ~43,000 buildings (2025); "only one of the City's 59 Community Districts has a median rent over $2,500—Manhattan Community District 1 in lower Manhattan" (pre-1974 stabilized). Manhattan totals given only as Core/Upper split (numbers not extracted) → not used. | §5.5; §13 CD1 card; §Sources |
| M-H2 | same search (excerpt) | https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2026/05/2026-HSR.pdf | RGB 2026 Housing Supply Report violation tables (Manhattan Class B/C). Ambiguous in excerpt → not used. | Not used |
| M-H3 | Census ACS 2023 re-check · Firecrawl scrape | https://api.census.gov/data/2023/acs/acs5?get=… | "Missing Key" — EMPTY (not accessible in build env). Census figures therefore NOT used on this page. | Not used |

#### M-K Local rules / programs
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-K1 | `DHCR major capital improvement closed circuit television security system eligible MCI operational bulletin` · Firecrawl search (excerpt) | https://govt.westlaw.com/nycrr/Document/I4f8a049ecd1711dda432a117e6e0f345 | 9 NYCRR 2502.4 schedule of MCIs: "TELEVISION SYSTEM: – new security monitoring system including additional components needed for the system." | §8.5; §9 MCI H3; §Sources |
| M-K2 | same → Firecrawl scrape (PDF, query) | https://sidranelaw.com/wp-content/uploads/2023/11/operational-bulletin-2021-1-update-2.pdf | DHCR Update No. 2 to Operational Bulletin 2021-1 (issued January 4, 2023): New TV Security System — cameras $2,556 per camera, monitors $1,178 per monitor, receivers $1,193 per receiver. | §8.5 (as DHCR ceilings, not AESS prices); §9 MCI H3; §Sources |
| M-K3 | `New York State commercial security tax credit retail theft cameras $3,000 small business 2024 budget` · Firecrawl search (excerpts) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit ; https://www.nysenate.gov/legislation/laws/EXC/845-E ; https://www.governor.ny.gov/news/governor-hochul-announces-new-initiatives-crack-down-organized-retail-theft-and-protect | Refundable credit up to $3,000 per retail location; FY25 budget; Executive Law §845-e. | §8.5; §9 tax-credit H3; §Sources |
| M-K4 | same → Firecrawl scrape (query, direct quote) | https://www.avigilon.com/blog/ny-retail-security-tax-credit | "This program expired at the end of 2025 and as of early 2026, it has not been renewed." Eligibility: ≤50 employees; expenses > $4,000 (≤25 employees) or > $6,000 (>25). | §8.5; §9 tax-credit H3; §Sources |
| M-K5 | `Manhattan lobby surveillance … 2024 OR 2025` · Firecrawl search → scrape | https://newyorkcityconnect.org/ | Connect New York home page on 2026-10-18: 3,595 registered cameras, 1,453 integrated cameras. | §5 para 4; §5.5; §Sources |
| M-K6 | Firecrawl scrape | https://newyorkcityconnect.org/camera-integration/ | Integration needs "a small fususCORE device that plugs into your router"; "Camera integration is free of charge"; voluntary; owner selects cameras and permissions; public-area-facing only; "Registering a camera does not provide the New York Police Department with any remote access…"; no facial recognition; AES-256, TLS 1.3 to AWS GovCloud; explicit written permission required. | §5.5; §6 Connect card; §8.5; §9 Connect H3s; §Sources |

#### M-N News
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-N1 | `Manhattan lobby surveillance DVR hacked cameras exposed online New York building 2024 OR 2025` · Firecrawl search → scrape (query, direct quote) | https://gothamist.com/news/assume-theres-a-camera-now-how-911-spurred-nycs-vast-private-surveillance-network | David Brand, Sep 10, 2026: Lower Manhattan Security Initiative (2008) gave police access to thousands of cameras on public and private property south of Canal Street; Domain Awareness System now relies on what former Mayor Eric Adams described as more than 80,000 cameras; >5,500 cameras registered through Connect New York (Axon Fusus); plan to link 20,000 NYCHA cameras; 1998 NYCLU tally of 2,400 cameras across Manhattan. | §5 para 4; §5.5; §8 Canal card; §13 Canal card; §Sources |
| M-N2 | same search (excerpts) | https://nysfocus.com/2025/08/11/eric-adams-nycha-nypd-cameras-surveillance ; https://prospect.org/2026/08/07/nyc-tenants-sue-over-spying-operation-in-public-housing/ | NYCHA camera feeds via Big Apple Connect; tenant lawsuit Aug 2026. | Not used (NYCHA not the page's audience) |

#### M-L Landmarks / corridors
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-L1 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Chinatown,_Manhattan | Approx. borders Canal/Hester, Worth, East Broadway, Essex, Lafayette; main streets Canal, Mott, Grand, East Broadway; tenements; greengrocers, fishmongers, jewelers, banks, restaurants, mini malls; Community District 3; ZIPs 10013 and 10002; 5th Precinct. | §7 tenement card; §8 Mott/Grand card; §13 Chinatown card; §Sources |
| M-L2 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Lower_East_Side | Between the Bowery and East River, Canal to Houston; first tenements at Corlear's Hook 1833; "new law" tenements with air shafts; Tenement Museum 97 Orchard Street; Orchard Street "Bargain District" now boutiques, restaurants, bars, galleries below Delancey especially around Broome and Orchard; Essex Crossing announced Sept 2013 at Essex and Delancey; Essex Market; 7th Precinct. | §7 tenement card; §8 Orchard + Essex cards; §13 Tenement Museum + Essex Crossing cards; §Sources |
| M-L3 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Washington_Heights,_Manhattan | Bounded by Dyckman St (Inwood), 155th St (Harlem), Harlem River, Hudson River; commercial streets St. Nicholas Ave, 181st St, Broadway; pre-war apartment buildings incl. five- and six-story New Law tenements; GWB, Fort Tryon, Morris-Jumel; 33rd and 34th Precincts. | §7 Upper Manhattan card; §8 St. Nicholas card; §13 GWB card; §Sources |
| M-L4 | research/smart-pss-support-setup.md M-L5 (X5) | https://en.wikipedia.org/wiki/Canal_Street_(Manhattan) | see X5. | §8; §13 |
| M-L5 | M-N1 | Gothamist | LMSI south of Canal. | §13 Canal card |
| M-L6 | M-H1 | IBO | Community District 1 median-rent fact. | §8 Lower Manhattan card; §13 CD1 card |

#### Manhattan sources EMPTY
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG — EMPTY (not accessible in build env).
- Yelp 1–3★ (Manhattan) — EMPTY (only listing pages).
- Manhattan hyperlocal (Patch, West Side Rag, The Lo-Down, Manhattan Times) items about Super Live Plus — EMPTY (none surfaced).
- Census ACS API — EMPTY (API key required in build env); no Census numbers on the page.
- Field Notes: no real AESS Manhattan anecdote supplied → written as a method note ("change access last"), no story.

#### Images
images: 11 reused from images/security-camera-maintenance/, images/school-security-camera-installation/, images/apartment-building-security-camera-installation/ (no real Super Live Plus photos yet; Drive folder absent, CompanyCam not connected). `images/parking-lot-camera-installation/` does not exist in the tree. All 11 viewed before use; none show faces, plates, house numbers or readable documents; product photos are unbranded. Alt/title/caption describe only what is visible and say product photos are not from a Manhattan job and do not show Super Live Plus.

| # | File (images/super-live-plus-app-support-repair/) | Source |
|---|---|---|
| 1 | super-live-plus-app-support-repair-manhattan-unbranded-rack-recorder-vented-front-product-photo.webp | images/security-camera-maintenance/security-camera-maintenance-bronx-rack-recorder-vented-front-product-photo.webp |
| 2 | super-live-plus-app-support-repair-manhattan-bullet-camera-on-pendant-mount-at-office-ceiling.webp | images/security-camera-maintenance/security-camera-maintenance-nyc-bullet-camera-on-pendant-mount-office-ceiling.webp |
| 3 | super-live-plus-app-support-repair-manhattan-black-camera-on-blue-wall-above-motion-sensor.webp | images/security-camera-maintenance/security-camera-maintenance-bronx-wall-camera-above-motion-sensor.webp |
| 4 | super-live-plus-app-support-repair-manhattan-mini-dome-over-wood-slat-wall-by-light-panel.webp | images/security-camera-maintenance/security-camera-maintenance-queens-mini-dome-over-wood-slat-wall-near-light-panel.webp |
| 5 | super-live-plus-app-support-repair-manhattan-small-cameras-high-on-double-height-wall.webp | images/school-security-camera-installation/school-security-camera-installation-manhattan-small-cameras-on-high-wall-of-double-height-room.webp |
| 6 | super-live-plus-app-support-repair-manhattan-ceiling-dome-camera-over-glass-entrance-wall.webp | images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-manhattan-dome-camera-on-ceiling-over-glass-entrance.webp |
| 7 | super-live-plus-app-support-repair-manhattan-bullet-camera-in-back-corridor-toward-door.webp | images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-manhattan-bullet-camera-on-ceiling-grid-in-back-corridor.webp |
| 8 | super-live-plus-app-support-repair-manhattan-dome-camera-under-water-stained-ceiling-tiles.webp | images/security-camera-maintenance/security-camera-maintenance-bronx-dome-camera-under-water-stained-ceiling-tiles.webp |
| 9 | super-live-plus-app-support-repair-manhattan-mini-camera-at-ceiling-edge-above-lit-soffit.webp | images/security-camera-maintenance/security-camera-maintenance-orange-county-mini-camera-at-ceiling-edge-above-lit-soffit.webp |
| 10 | super-live-plus-app-support-repair-manhattan-four-dome-cameras-and-recorder-kit-product-photo.webp | images/security-camera-maintenance/security-camera-maintenance-brooklyn-four-dome-camera-recorder-kit-product-photo.webp |
| 11 | super-live-plus-app-support-repair-manhattan-recorder-live-view-tiles-with-date-stamp.webp | images/security-camera-maintenance/security-camera-maintenance-nyc-recorder-live-view-with-date-and-time-stamp.webp |
