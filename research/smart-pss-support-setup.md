# Smart PSS Support Setup — silo research

Created 2026-10-18 by the REBUILD run for `smart-pss-support-setup-bronx` (queue line: `REBUILD | smart-pss-support-setup-bronx | Smart PSS Support Setup | Bronx | up /smart-pss-support-setup-nyc | (646) 490-0629 | GBP Bronx`). First page of this silo to be rebuilt; the other 15 silo pages (NYC hub, 4 boroughs, LI hub + Nassau/Suffolk, HV hub + 6 counties) are still the old shared template (~124 KB each, identical text with the area name swapped).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Tools used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (markdown, query mode, PDF parser). Shell curl is blocked. Reddit could not be scraped (Firecrawl does not support reddit.com in earlier runs), so every Reddit row is a search-result **excerpt** only. Rows marked "carried" were fetched by earlier runs in another research file (file + row named) and were not re-fetched today.

Page section labels (Bronx page): §Hero, §Quick (instant action block), §5 Neighborhood (+ §5.5 facts list), §Repair (same-day block + five checks), §6 Services, §7 Architecture (+ §7.5 "How the setup changes"), §8 Commercial (+ §8.5 rules list), §9 Q&A (clusters A–E → H3 1–20), §10 Equipment (+ comparison tables), §10.5 AI Reality Check (Claims 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ BYOE), §16 Complete services, §FieldNotes, §17 FAQ (1–9), §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every Smart PSS page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit (r/Dahua, r/cctv, r/homesecurity) | Excerpts only (rows R1–R9). Threads not openable in build env. r/homesecurity SmartPSS-specific threads: EMPTY (none surfaced). |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and instead checks seven claims repeated by download sites, how-to videos and forum answers against Dahua docs (rows D1–D9, P1–P2, R1–R9). |
| 6 | Area landmarks | Bronx section, rows BX-L1–BX-L7. |
| 7 | Area use cases / building stock | Bronx section, rows BX-H1–BX-H4. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl search backend available; no Bing/DDG PAA, related or autocomplete. |
| 9 | Local news | Bronx section rows BX-N1–BX-N4 (ABC7, amNY, Riverdale Press, News 12). |
| 10 | Hyperlocal | Riverdale Press (BX-F2), Bronx Times (carried BX-L3). Norwood News / BronxNet SmartPSS or footage-export items: EMPTY (none surfaced). |
| 11 | Yelp 1–3★ | `yelp Bronx security camera repair review "Smart PSS" OR "DVR" software remote viewing technician` · Firecrawl search → only Yelp search-listing pages (Bronx installation listing "Rating 4.7(1,347)"; Queens/Brooklyn/NJ listings), no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

### 1.2 Dahua official documents (D)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D1 | `SmartPSS Lite Dahua download release notes version Windows` · Firecrawl search → scrape (markdown) | https://dahuawiki.com/SmartPSS_Lite | Banner: "NOTE: SmartPSS has been discontinued and is no longer supported for Windows and M Series Macintosh Computers. Please download and install SmartPSS Lite instead." Links: Notice of Discontinuation; Windows Download and macOS M Series Download; User/Access Control/Attendance manuals. Intro: lightweight platform for SMB, "video surveillance, access control and various attendance functions… P2P linking, real-time monitoring, video playback, event center". Guides listed: P2P setup, ASC3202B, First Card Unlock, Anti-Passback, Multi-card, Holiday Schedule. Datasheet V1.003.0000000.0 (2022-06-06). Page last modified 27 June 2025. | §5 para 1; §6 install card; §10 access-control card; §10.5 Claim 1; §9 H3 7 (Mac); §Sources |
| D2 | `"SmartPSS" discontinuation notice Dahua 2024…` · Firecrawl search → scrape | https://dahuawiki.com/Discontinuation_of_SmartPSS | Notice is an image only (text not extractable); page last modified 2 Oct 2024. Search excerpts: SmartPSS AC also discontinued → "install SmartPSS Lite instead". | Background (date of notice page) |
| D3 | same as D1 → scrape | https://dahuawiki.com/SmartPSS_Lite/SmartPSS_Lite_P2P_Setup | Prereqs: device initialized; SmartPSS Lite installed. Steps: on device Network > P2P "Verify P2P is enabled and the status is 'Online'"; Home > Device Manager > + Add > Method "SN(For Device Support P2P)", device name, SN, user/password > Add; verify Online Status green dot "Online"; Home > Monitor > Live View; double-click device. Last modified 13 Feb 2024. | §6 connection card; §7.5 "Different networks"; §Repair checks 2–3; §9 H3 17; §10.5 Claim 2; §Sources |
| D4 | `SmartPSS Lite export video playback download .dav MP4 Smart Player dahuawiki` · Firecrawl search → scrape (query) | https://dahuawiki.com/SmartPSS/How_To_Export_Device_Record | Export: Playback → device tree → Record Type, Stream Type (Main/Sub), Time → Search → play → Time Clip icon (start) → drag window → Time Clip again (end) → Export Setup: Path, Export Format "ASF, AVI, MP4, or Original Format", "Export SmartPlayer Player: Check the box to include the playback software with the export" → Export Progress window (Pause/Start/Delete) → "Exported" tab. No encryption option mentioned. Last modified 2 Oct 2024. (Guide is filed under SmartPSS; the Lite Monitor manual D7 describes the same clip/export flow.) | §6 export card; §9 H3 1, 4, 5; §10.5 Claim 3; §12 step 3; §Sources |
| D5 | same search → scrape (query) | https://dahuawiki.com/Software/Dahua_Toolbox/SmartPlayer | SmartPlayer (Dahua Toolbox) plays "DAV, AVI, MOV, MP4, ASF or FLV"; forward/reverse playback, speed, audio, full screen, layouts, frame stepping. No watermark-verification claim on page. Last modified 11 Apr 2019. | §9 H3 5; §10.5 Claim 3; §Sources |
| D6 | `SmartPSS Lite user manual PDF system requirements…` · Firecrawl search → scrape (PDF parser, markdown) | https://dahuawiki.com/images/a/a4/SmartPSSLite_User%27s_Manual_Eng.pdf | SmartPSS Lite User's Manual V1.0.0 (Apr 2022), 39 pp. Install screen "Need Space:243M"; initialization password "8 to 32 non-blank characters… at least two types"; security questions; "Auto Login after Registration"; login Remember Password / Auto Login / Forgot password? (reset by security questions); user menu: User Manager (roles/users/permissions), Lock Screen, Switch User, Open Debugging Log; System Status icon "If the CPU usage is high, the icon turns red"; Basic Setting: Auto check time (devices check time daily), Auto Start ("automatically started after the computer is turned on"), Network Ability ("when network condition is fluent… High"); Monitor Setting: Default Stream Type (Self adaptive/Sub/Main), Instantly replay time, Local Record Time (example 30 min, default path \Data\User\Record), Decode Type, Resume Last Preview, Show IVS Rule; Event setting: alarm sound loop, SMTP (server, port, user, password, sender, up to 5 receivers, None/SSL/TLS, Test); Local Path (Pic/Record); Data Management (overwrite ratio when disk full; data clear by days); Backup and Restore (manual/auto); Device add: Auto Search, Manual by IP (port "37777 by default. The actual port number shall prevail"), by SN (P2P), Import xml batch; device config: time (Time Zone, System Time with Sync PC, DST, NTP), firmware upgrade, restart; Log Query; Event Config (intrusion event: alarm sound, email, Link Video, alarm I/O, arming periods); Event Center (stats, 7-day trend, 1/4/9 split live view); live view icons Local Record, snapshot path .../Data/User/Picture/Capture, audio, audio talk, instant replay, zoom. Privacy notice: comply with local law, "clear and visible identification". | §5 para 4; §6 cards (install, clock, users, restart, alarms, handover); §7.5; §8.5 privacy bullet; §9 H3 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18; §10.5 Claims 4–6; §17 FAQ 5; §Sources |
| D7 | same search (excerpt) → scrape (PDF parser) | https://dahua-store.ru/wp-content/uploads/2025/01/smartpsslite_monitor-manual_eng.pdf | SmartPSS Lite Monitor Solution User's Manual V1.0.3 (revisions: V1.0.0 Apr 2022, V1.0.1 Jan 2024, V1.0.2 Sep 2024, V1.0.3 Dec 2024 "Updated the live view"). Live view: organization/area tree, saved views and view groups, tour plans with day/week schedules, PTZ (presets, tour, pan, scan, pattern, wiper); right-click: Start Record (default ".../Data/User/Record"), Snapshot, Continuous Snapshot, Instant Playback, Split Track, Stream Type, Image Adjustment, Smart OSD (AI rule/IVS overlay); Main Stream "higher quality and larger traffic consumption", Sub Stream "lower quality and smaller traffic consumption"; Playback: device and local (PC) videos, Time Clip, Smart Search ("dynamic detection analysis of a certain area"; results purple on timeline; device must support it "Otherwise, the result will be empty"), Sync multi-window playback, export path/format. Appendix: strong passwords, "minimum set of permissions", account lock, keep password-reset info current, IP/MAC binding, HTTPS, firewall allowlist, VLAN isolation of video vs office network, check online users, physical protection. (Hosted by a Russian reseller; Dahua document.) | §6 views/tours card; §7.5 shared PCs; §9 H3 4, 6, 9, 12, 13; §10 PTZ and deterrence cards; §10.5 Claim 5; §Sources |
| D8 | `SmartPSS Lite user manual…` (excerpts) | https://www.dahua.market/software/SmartPSSLite_VideoIntercom_Manual_Eng.pdf ; https://securityeyes.com.au/wordpress/wp-content/uploads/2024/10/SmartPSSLite_Access-Manual_Eng.pdf | Separate SmartPSS Lite manuals exist for Video Intercom and Access Control solutions. Not opened beyond excerpts. | §10 intercom + access cards (existence only) |
| D9 | `SmartPSS Lite download release notes…` (excerpt) → scrape (query) | https://www.scribd.com/document/982439294/Release-Note-Smartpss-ite | Release notes V1.003.0000000.0 → V1.003.0000008.4, every version "Windows 7/Windows 8/Windows 10/Windows 11 (64 bit)"; V1.003.0000006.0 "Supports software version detection and online update"; V1.003.0000002.4 "Update and optimize network security"; V1.003.0000008.4 "Spport device cloud upgrade". No dates on page. Third-party upload (Scribd) of a Dahua document. | §5.5 bullet 5; §9 H3 7, 8; §10.5 Claim 4; §17 FAQ 2; §Sources |
| D10 | same search (excerpt) → scrape (query) | https://ametawiki.ametagroup.com/docs/smartpss | Reseller wiki: SmartPSS Lite Windows V1.003.0000006.0.R.240517, release date 2024-05-17; macOS version available; old SmartPSS V2.002.0000009.0.R.190426 (Win32) for old access control: "NO P2P connection, install it in local database computer only." | §10.5 Claim 1; §Sources |
| D11 | same search (excerpt) | https://dh-vision.com/pages/smart-pss | Reseller: "OS: Windows 7 / 8 / 10 / 11 (64-bit)". | Corroborates D9 (not cited on page) |

### 1.3 Forums, P2P change and security (P)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `"SmartPSS" discontinuation notice…` · Firecrawl search → scrape | https://ipcamtalk.com/threads/old-smartpss-v2-003-cannot-connect-to-dahua-nvr-starting-today-but-smartpss-lite-can.78475/ | Thread started Oct 8, 2024 (US user): old SmartPSS on many PCs/Androids suddenly showed NVRs offline while "SmartPSS lite… and the DMSS app can connect"; complaints Lite removed conveniences (doesn't remember export file type, default view size) and takes longer to save clips. Quoted linked thread (steve1225, Jul 4, 2024): from Dahua Poland, "starting August 1 Dahua cloud will stop supporting P2P connections from all old apps" — gDMSS/iDMSS and old SmartPSS 2.0 (2019/2020); official recommendation DMSS + SmartPSS Lite; "This limitation does not apply direct IP connections"; reason: old P2P protocol "contained poor password/key encoding". Same poster: open port 37777 + DDNS works but "opens Your NVR to external attacks"; suggests VPN. Other US users (Florida) still connected via old 2.003 on Oct 9, 2024 — rollout uneven. | §5.5 bullet 4; §7.5; §9 H3 18, 19; §10.5 Claims 1, 5; §Sources |
| P2 | carried research/dahua-camera-installation.md (Security advisories) | https://cvefeed.io/vuln/detail/CVE-2021-33044 | Dahua identity-authentication bypass; CVSS 3.1 9.8; added to CISA KEV Aug 21, 2024; action "Apply mitigations per vendor instructions or discontinue use". | §9 H3 18; §10.5 Claim 5; §Sources |
| P3 | carried research/hik-connect-app-support-repair.md F1, F2 | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment ; https://www.fcc.gov/laboratory-division/equipment-authorization-approval-guide/equipment-authorization-system | FCC order DA 26-635 (released Jun 26, published Jul 6, effective Jul 16, 2026) prohibits continued importation and marketing of covered equipment added to the Covered List in 2024 or earlier; "does not affect the continued use or operation of previously authorized covered equipment; consumers may continue to use any device or equipment that they currently possess…"; rejected exemption for spare parts/replacements. Covered List producers include Dahua. | §8.5 bullet 5; §9 H3 20; §Sources |
| P4 | `Windows 10 end of support October 14 2025…` · Firecrawl search (excerpts, microsoft.com) | https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025 ; https://learn.microsoft.com/en-us/windows/whats-new/extended-security-updates | Windows 10 reached end of support Oct 14, 2025; PCs "will still function" but no technical support, software updates or security fixes; paid ESU option (consumer page says enrolment until program end Oct 12, 2027 — date not used on page). | §5.5 bullet 5; §8.5 bullet 6; §9 H3 8; §10.5 Claim 4; §Sources |
| P5 | carried research/dvr-upgrade.md G3 | https://nysenate.gov/legislation/laws/PEN/250.05 | Penal Law §250.05 eavesdropping class E felony; one-party consent. | §8.5 bullet 3 |
| P6 | carried research/nvr-installation.md (G9 licensing) | NYS DOS Article 6-D (see that file) | CCTV installation/service is licensed work in NYS. | §8.5 bullet 1; §10.5 Claim 6 |

### 1.4 Reddit (R) — excerpts only
| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com SmartPSS Lite problem export playback slow` · Firecrawl search | https://www.reddit.com/r/cctv/comments/1l26s73/please_help_dahua_system_with_smart_pss_download/ | "Sometimes I download from certain cameras and it works fine exported mp4. But with other cameras it is flipped 90 degrees and aspect ratio is…" | §9 H3 5 (quoted); §10.5 Claim 3; §Sources |
| R2 | same | https://www.reddit.com/r/Dahua/comments/yicb7j/download_24h_footage/ | "The only solution I can find at this moment is to export using the SMART PSS application, however it really takes ages." | §9 H3 4 (quoted); §Sources |
| R3 | same | https://www.reddit.com/r/Dahua/comments/1wb9uf6/unable_to_download_video_from_dahua_nvr/ | "Saving to a different storage drive (e.g. internal computer drive, not a usb stick)." | §9 H3 4 (quoted); §Sources |
| R4 | same | https://www.reddit.com/r/Dahua/comments/1cdgymm/dahua_dhinvr44324ks21_the_cameras_keep_getting/ | Internet at the camera end "head an upload speed that is too low to support the video bitrate you have selected." | §9 H3 16 (quoted); §Sources |
| R5 | same | https://www.reddit.com/r/Dahua/comments/1ifsh6q/dmss_app_slow/ | Troubleshoot by loading a camera through Smart PSS on a wired PC; load one camera. | Background §9 H3 16 |
| R6 | `site:reddit.com r/Dahua SmartPSS Lite device offline OR "login failed" OR "Windows 11"` · Firecrawl search | https://www.reddit.com/r/Dahua/comments/1rrcoj3/i_can_access_my_cameras_using_the_dmss_app_but/ ; https://www.reddit.com/r/Dahua/comments/1vj9tqi/dahua_dmss_app_service_degradation/ ; https://www.reddit.com/r/Dahua/comments/1sqfrbz/cant_remote_access_via_smartpsslite_but_can_with/ | Online in DMSS but not SmartPSS Lite (on V1.003.0000006.0.R.240517); the reverse during a DMSS "service degradation". | §9 H3 17; §10.5 Claim 7; §Sources |
| R7 | same | https://www.reddit.com/r/cctv/comments/1g7g37e/smart_pss_offline_status_invalid_username_or/ | Adding by SN fails with "Offline (invalid username or password)". | §9 H3 17 (quoted); §Sources |
| R8 | same | https://www.reddit.com/r/Dahua/comments/15njnaz/smartpss_crashing_on_windows_11/ | "my Windows 11 SmartPSS program crashes whenever I try to stream more than 1 camera simultaneously". | §9 H3 10; §Sources |
| R9 | `"SmartPSS" discontinuation…` · Firecrawl search | https://www.reddit.com/r/Dahua/comments/1liq1nz/smart_pss_alternative/ ; https://www.reddit.com/r/Dahua/comments/1f88393/new_smartpss_lite_wrongly_registers_my_nvrs_as/ ; https://www.reddit.com/r/Dahua/comments/1fzsb6w/p2p_service_down_for_several_systems_suddenly/ | Lite direct to NVR "limited to 64 channels"; Lite mis-registering NVR channel counts; US: systems offline in old SmartPSS while Lite and DMSS work. | Background only (64-channel figure NOT used on page — single forum excerpt) |

### 1.5 Keyword plan (five layers, silo)
- **Service:** Smart PSS support, SmartPSS setup, SmartPSS Lite installation, Smart PSS Lite support, Dahua PC software setup, SmartPSS export video, SmartPSS playback, SmartPSS add device, SmartPSS remote viewing, SmartPSS user permissions, SmartPSS time sync.
- **Problem:** SmartPSS device offline, SmartPSS offline invalid username or password, old SmartPSS not connecting (2024 P2P change), SmartPSS crashing / stuttering, export slow / failed, MP4 flipped, wrong time stamp, PC filling up, Windows 10 end of support, 32-bit PC, open port 37777, CVE-2021-33044, super/manager changeover, shared PC.
- **Technology:** SmartPSS Lite V1.003.x, SmartPSS 2.0 (discontinued), SmartPlayer, DAV/original format, MP4/AVI/ASF, P2P serial number, IP + port 37777, sub stream / main stream, Smart Search, Local Record, Auto Start / Auto Login / Resume Last Preview, NTP / DST, User Manager, Lock Screen, Event Config / Event Center, SMTP, Backup and Restore, DMSS, Dahua NVR / DVR / XVR, PTZ, deterrence (TiOC-type) cameras, VLAN, VPN.
- **Industry:** bodegas/delis, storefront strips, supers, managing agents, co-ops/condos, large complexes, warehouses/market units, multi-store owners, offices.
- **Geographic (Bronx page):** Bronx; Fordham Road, The Hub / Third Avenue / 149th Street, Westchester Square, White Plains Road, Jerome Avenue, Hunts Point, Bronx Terminal Market, Arthur Avenue / Belmont, East Tremont, Southern Boulevard, Grand Concourse, East 161st Street (Bronx DA), Co-op City / Bay Plaza, Riverdale, Parkchester, Mott Haven, Melrose, Morrisania, Highbridge, Port Morris + §13 "we also serve" list. Every image alt/title carries "Smart PSS" + "Bronx".

### 1.6 Silo pricing (no invented prices) — FLAG
The 16 existing Smart PSS pages publish **no dollar prices** for Smart PSS work: the pricing block says "Single service call", "By system size", "Custom quote", and "We give a likely range by phone before any visit" (checked on the old Bronx, Brooklyn and NYC hub pages; the only $ figures in those files are the shared mega-nav JS price chips, not silo prices). The Bronx page therefore uses only:
- phone triage at no charge (the old pages' "likely range by phone before any visit" — no fee ever stated);
- the protected service rate **$195/hr, 3-hour minimum ($585)** (blueprint v2.3 §9 / App. A), not multiplied (Bronx 1.00 anyway);
- recorder replacement = **DVR Upgrade silo prices** (research/dvr-upgrade.md §1.8; dvr-upgrade-bronx.html shows the same at Bronx 1.00): 4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid/XVR $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+.
- Service schema AggregateOffer low 0 / high 2200.
FLAG for Anwar: (1) confirm the $195/hr rate is the right charge for SmartPSS visits (blueprint describes it as the service/callback rate "not on the initial install"); (2) confirm Smart PSS pages may borrow DVR-upgrade recorder prices; (3) "$0 phone triage" is a framing of the old pages' free phone range, not a published price.

---

## Bronx

Build 2026-10-18. Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`) · up-link `/smart-pss-support-setup-nyc`. §9 Bronx = 1.00 × Brooklyn base.

**Thesis:** In the Bronx, the SmartPSS computer is the borough's footage-export station. Residents mostly watch cameras on phones (Bronx has the city's highest shares of households with no broadband and cellular-only access, and one in three households has no computer), so SmartPSS lives on business PCs — a bodega back office, a super's desk, a managing agent's office, a warehouse dispatch window — and its real job is getting a clean, correctly time-stamped clip to a detective, the Bronx DA's office (BronxCAMS) or an insurer before the recorder loops, on a supported 64-bit Windows PC that restarts itself after outages and with accounts that survive super and owner changeovers.

### Internet and computer access (BX-I)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-I1 | `Bronx households without broadband internet percent NYC Internet Master Plan Bronx highest` · Firecrawl search → scrape (query) | https://www.osc.ny.gov/press/releases/2024/12/dinapoli-report-examines-broadband-availability-access-and-affordability-nyc | NYS Comptroller, Dec 11, 2024: as of 2023 the Bronx had the highest share of households with no broadband access (36.7%) and with access via cellular data plans only (20.3%); highest poverty share (28.9%); Bronx and Brooklyn highest average broadband price; price near 100 Mbps highest in the Bronx; Bronx/Brooklyn just over 7% no internet of any type vs 4% Manhattan. | §5 para 2; §5.5 bullet 1; §9 H3 16; §Sources |
| BX-I2 | same search → scrape (query) | https://thebronx.org/understanding-and-overcoming-the-bronx-digital-divide/ | Bronx Community Foundation, Jul 8, 2025: 22.4% of households lack broadband at home (vs 18% Queens, 12.5% Manhattan); 44% of Bronx households were in ACP when it ended in 2024; one in three households — over 184,000 homes — lack a computer; Riverdale/Kingsbridge 19%, Soundview/Parkchester 30%+, Melrose/Mott Haven/Hunts Point 35% without a computer. | §5 para 2; §5.5 bullet 1; §Sources |
| BX-I3 | same search (excerpt) | https://council.nyc.gov/data/internet-access/ | Council data team: Melrose–Mott Haven–Port Morris 44% without broadband; Tremont–Belmont–West Farms 41%; Longwood–Hunts Point 41%. | Not used (older ACS vintage; BX-I1 newer) |
| BX-I4 | `Optimum outage Bronx internet down customers 2026` · Firecrawl search (news) | — | EMPTY (no results). Page makes no ISP-outage claim. | — |

### Footage requests, courts and police (BX-F)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX-F1 | `Bronx District Attorney CAMS camera registry businesses register surveillance cameras` · Firecrawl search → scrape | https://www.bronxda.nyc.gov/html/outreach/enroll-in-bronxcams.shtml | BronxCAMS launched 2018 by the DA's Crime Strategies Bureau; community members/businesses "voluntarily list their cameras to the database, which already includes NYPD and NYCHA cameras"; confidential map "that will never be released to the public" with "information on how to retrieve footage"; "Our Office does not have access to cameras or camera footage"; staff "contact the camera owner or designee to view footage and request a copy". Online form or mail to 198 E. 161st Street, Bronx, NY 10451; bronxcams@bronxda.nyc.gov. | §Hero sub; §5 para 3; §5.5 bullet 2; §8.5 bullet 2; §9 H3 2; §13 card 1; §17 FAQ 7; §Sources |
| BX-F2 | same search → scrape (query) | https://www.riverdalepress.com/stories/bronx-da-wants-borough-directory-of-security-cameras,68834 | Riverdale Press, May 5, 2019: registry of private cameras so prosecutors know where to go, who to talk to "and how much time they have"; Carmen Facciolo (DA's office) on the old routine: "you would have to go out, you would have locate the camera… find out the owner… Get their attorney's name. Figuring out how to start the subpoena"; "More and more cases we're handling each day has some type of video footage"; systems "often loop, or tape over, existing footage after a period of time that can be as short as 24 hours"; registry entries include how videos can be shared and where footage is stored. | §5 para 3; §5.5 bullet 3; §9 H3 2; §Sources |
| BX-F3 | same search → scrape (query) | https://www.hornwright.com/bronx/civil-rights/malicious-prosecution/how-to-preserve-body-cam-dash-cam-and-surveillan/ | Horn Wright (Bronx case guide, undated): private systems "may overwrite footage in 7–30 days"; preservation letter; chain of custody — "Keep original files whenever possible", "Avoid editing or clipping the footage", "Document who handled it", label storage; back up in two locations. (Note: research/security-camera-maintenance.md quoted "seven to ten days" from this firm; today's scrape reads 7–30 — page uses 7–30.) | §5.5 bullet 3; §9 H3 1; §10.5 Claim 3; §Sources |
| BX-N1 | `Bronx store owner police asked surveillance video footage USB detectives bodega cameras 2026` · Firecrawl search → scrape (query) | https://abc7ny.com/post/surveillance-video-reward-offered-arrest-alleged-shoplifter-wanted-stabbing-bronx-bodega-employee/15429424/ | ABC7, Oct 15, 2024: police released surveillance footage of a man who stabbed a bodega employee at 91 Westchester Square who tried to stop a theft; United Bodegas of America offered a $2,000 reward. | §5 para 3; §8 Westchester Square card; §13 card 4; §Sources (no names used) |
| BX-N2 | carried research/nvr-installation.md BX15 | https://www.amny.com/news/bronx-bodega-shot-robbery-brooklyn-shooting/ | Aug 25, 2026: customer shot and killed during robbery at a deli on East 149th Street, West Concourse; "caught on video"; amNY surveillance footage matched a discarded sweatshirt. | §5 para 3 (stated factually, no names); §Sources |
| BX-N3 | same search as BX-N1 (excerpts) | https://www.fox5ny.com/news/jesus-acosta-arrested-after-deadly-bronx-bodega-shooting-caught-camera ; https://www.nbcnewyork.com/bronx/bodega-shooting-video-grand-concourse/6539946/ | Same Aug 2026 case; suspect named in coverage. | Not used (names avoided) |
| BX-N4 | carried research/nvr-installation.md BX16 | https://bronx.news12.com/2026/07/03/5000-con-edison-customers-in-the-bronx-without-power-amid-heat-wave/ONmoL7BVphOWvTtg2dafc | Jul 3, 2026: ~5,000 Bronx Con Ed customers out; 8% voltage reduction in parts of northwest Bronx. | §9 H3 9; §Sources |

### Building stock (BX-H) — carried
| ID | Source | URL | Finding | Used |
|---|---|---|---|---|
| BX-H1 | carried research/nvr-installation.md BX2 | https://unhp.org/blog/how-will-bronx-buildings-survive-as-they-age/ | Median Bronx multifamily building 87 years old. | §5.5 bullet 6 |
| BX-H2 | carried BX1 | https://www.furmancenter.org/neighborhoods/the-bronx/ | 2024 homeownership 19.7% (city 32.7%). | §5.5 bullet 6 |
| BX-H3 | carried BX5 | https://www.coopcity.com/aboutus/ | Co-op City 15,372 units, 35 high-rises, 7 townhouse clusters. | §7 card 3; §13 card 6 |
| BX-H4 | carried BX4 | https://s-media.nyc.gov/agencies/lpc/lp/2403.pdf | Five-/six-storey apartment house dominant along the Grand Concourse. | §7 card 1 (building type only) |

### Corridors / landmarks (BX-L) — carried
| ID | Source | URL | Finding | Used |
|---|---|---|---|---|
| BX-L1 | carried BX7 | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=49 | Fordham Road BID: 35 block faces, 333 ground-floor retail businesses. | §8 card 1; §13 card 2 |
| BX-L2 | carried BX8 | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | 12 Bronx BIDs incl. Belmont, Jerome-Gun Hill, White Plains Road, Westchester Square, HUB Third Avenue. | §8 cards 4, 6 |
| BX-L3 | carried BX9 | https://www.bxtimes.com/third-avenue-bid-adds-security-measures/ | Bronx Times, Oct 2, 2026: Third Avenue BID 18 cameras at 10 locations. | §8 card 2; §13 card 3 |
| BX-L4 | carried BX12 + research/security-camera-maintenance.md BX-L6 | https://www.nycfoodpolicy.org/hunts-point-distribution-center-brief-overview-spotlight-produce-market/ ; https://en.wikipedia.org/wiki/Hunts_Point_Cooperative_Market | Hunts Point FDC ~329 acres, 155+ wholesalers; cooperative market operates 24/7. | §8 card 5; §13 card 5 |
| BX-L5 | carried BX11 | https://en.wikipedia.org/wiki/Bronx_Terminal_Market | Bronx Terminal Market south of Yankee Stadium. | §8 card 6 |
| BX-L6 | carried research/security-camera-maintenance.md BX-L3 | https://en.wikipedia.org/wiki/IRT_Pelham_Line | 6 train elevated over Westchester Avenue. | §8 card 3; §13 card 4 |
| BX-L7 | carried BX14 | https://en.wikipedia.org/wiki/Bay_Plaza_Shopping_Center | Bay Plaza beside Co-op City. | §13 card 6 (name only) |

### Local Reddit / hyperlocal
- r/bronx threads about SmartPSS, camera PCs or footage exports: EMPTY (none surfaced in the searches above).
- Norwood News, BronxNet, Bronx Times items on SmartPSS / camera software: EMPTY.

### Local licensing / rules
- NYS low-voltage / Article 6-D licensing (P6) → §8.5 bullet 1.
- BronxCAMS voluntary + confidential (BX-F1) → §8.5 bullet 2.
- Penal Law §250.05 audio (P5) → §8.5 bullet 3.
- Dahua privacy notice in manual (D6) → §8.5 bullet 4.
- FCC June 2026 order (P3) → §8.5 bullet 5; §9 H3 20.
- Windows 10 end of support (P4) → §8.5 bullet 6.
- NYC rule requiring private footage retention: EMPTY (as recorded in research/nvr-installation.md).

### Prices used (Bronx 1.00×) — see §1.6
Phone triage no charge; on-site $195/hr, 3-hr minimum ($585); extra time $195/hr; recorder replacement $450–$700 / $650–$1,000 / $800–$1,200 / $1,200–$2,200 / $2,200+. Worked examples: East Tremont deli = $585; four Concourse walk-ups = hourly beyond minimum + 8-ch replacement $650–$1,000 if needed.

### Images (11) — permanent image rule
Drive "AESS Website Photos" has no Smart PSS subfolder; CompanyCam not connected. No real SmartPSS screenshots or SmartPSS-PC photos exist in the library — **no image claims to show SmartPSS**; the hero caption says the screen is the recorder's own output, not SmartPSS. All 11 viewed before use (contact sheets), converted with Pillow (WebP q80, ≤1600 px; PNG flattened on black to keep the product background). No faces identifiable (store-monitor tiles show tiny distant figures only), no house numbers, plates or readable documents. Recorder product shots in images/dvr-upgrade/ were rejected because none is Dahua (Honeywell, Swann, Hikvision, Lorex, Uniview, DW, etc.). Root `images/dahua-*.png` filenames don't match content (known library flag) — files chosen by what they show.
| images/smart-pss-support-setup/ | Source | Section |
|---|---|---|
| smart-pss-support-setup-bronx-monitor-16-camera-grid-and-bitrate-table.webp (hero, eager, 1127×935) | images/dahua-camera-installation/dahua-camera-installation-orange-county-recorder-monitor-camera-grid-and-cable-bundles.webp (real AESS job) | Hero |
| …-bronx-turret-camera-in-stockroom-corner.webp | images/dahua-camera-installation/…-orange-county-turret-camera-in-storage-room-corner.webp (real) | §5 |
| …-bronx-mini-dome-cameras-in-shop-drop-ceiling.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-mini-domes-in-shop-drop-ceiling.webp (real) | §6 |
| …-bronx-turret-camera-above-glass-entrance.webp | images/dahua-camera-installation/…-suffolk-county-turret-camera-above-glass-storefront.webp (real) | §7 |
| …-bronx-ceiling-monitor-store-aisle-camera-tiles.webp | images/dvr-upgrade/dvr-upgrade-brooklyn-store-monitor-showing-camera-grid.webp (real) | §8 |
| …-bronx-camera-tile-with-date-stamp-brick-wall-lot.webp | images/dvr-upgrade/dvr-upgrade-nassau-county-split-screen-tile-brick-wall-and-paved-lot.webp (real) | §9 cluster A (clock) |
| …-bronx-night-camera-tile-back-room-open-door.webp | images/dvr-upgrade/dvr-upgrade-queens-recorder-tile-of-back-room-and-open-door.webp (real) | §9 cluster A (Smart Search) |
| …-bronx-bullet-camera-aimed-down-corridor.webp | images/dahua-camera-installation/…-long-island-bullet-camera-aimed-down-corridor-to-door.webp (real) | §9 cluster C |
| …-bronx-network-cable-bundles-above-recorder-shelf.webp | images/dvr-upgrade/dvr-upgrade-queens-blue-and-white-cable-bundles-above-recorder-rack.webp (real) | §9 cluster D |
| …-bronx-dahua-turret-red-blue-deterrence-lights-product-photo.webp | images/dahua-8.png (Dahua manufacturer photo) | §10 |
| …-bronx-dahua-mini-pan-tilt-dome-product-photo.webp | images/dahua-1.png (Dahua manufacturer photo) | §14 |
DAILY-LOG note: `images: 11 = 9 real AESS job photos from other jobs + 2 manufacturer product shots (no real smart-pss photos yet)` — sources images/dahua-camera-installation/, images/dvr-upgrade/, root images/dahua-*.png. Several real scenes are the same source photos (different crops) already used on nvr-installation-bronx and security-camera-maintenance-bronx (monitor grid, brick-wall tile, corridor bullet, storeroom tile).

### House practices stated without an external source (FLAG for Anwar)
- Two-copy export routine (original + SmartPlayer as evidence copy, MP4 as convenience) — built on D4/D5 + BX-F3, but the routine is AESS practice.
- "Use main stream for exports"; "new USB stick better than a used one"; write down camera/date/times/who exported.
- Export first, then fix the recorder clock; changing a recorder clock "can leave overlapping or missing stretches in the timeline" (general recorder behaviour, unsourced).
- Copying a full day from the recorder's own USB backup menu (recorder feature, not sourced from a Dahua doc in this run).
- BIOS "power on after outage" + Windows auto-login trade-off; small battery backup under the PC.
- Order of preference P2P → VPN → forwarded non-default port.
- Separate Windows account for rent records; Remember Password off on shared PCs.
- "Most SmartPSS faults back to a working picture within one to two hours" (blueprint element 36 wording).
- One-page handover sheet; training ends when the clerk has exported twice; sealed password copy only by written agreement.
- "Recorders sold under other labels run Dahua firmware" (general industry knowledge; no brand named).
- National-brand comparison table (ADT/Ring/SimpliSafe) is general description, unsourced (blueprint element 25).
- Field Notes is a method note in Anwar's voice, not a specific Bronx job story — confirm or replace.

---

## QUESTION REGISTER — Smart PSS Support Setup silo

Rule (v2.3 §12.3, DAILY-RUN step 2): no FAQ/Q&A question on a new or rebuilt page may repeat an intent listed here.

### Old template (all 15 un-rebuilt pages; identical apart from the area name — to be rebuilt, avoid these intents where possible)
Forum-style cards: Is Smart PSS free or is there a catch? · Do I have to pay a subscription to view my own cameras now? · Lite vs the old Smart PSS — which is better? · Why is the download so hard to find on Dahua's site? · Should I just DIY the install? · Works on my home WiFi but offline when I'm out — why? · Installs fine on Windows 11 but the window is blank. · Old Smart PSS suddenly can't connect, but Lite and the phone app can. · Can one PC watch all my store locations? · How do I give my manager view-only access? · Live view works but I can't open recordings. · Smart PSS keeps freezing and crashing. · I lost the admin password to the recorder. · Do I still need the phone app if I have Smart PSS?
"Asked every way" H3s: What is Smart PSS used for? · How do I install Smart PSS? · How do I add cameras to Smart PSS? · Why is Smart PSS not connecting? · Which Smart PSS for Windows 11? · Where do I download Smart PSS safely? · Can Smart PSS do remote viewing? · Is there a Smart PSS for Mac? (+ CTA "Smart PSS still not cooperating?")
FAQ: Is Smart PSS a camera brand? · What's the difference between Smart PSS and Smart PSS Lite? · Why does Smart PSS show my devices offline? · Why won't Smart PSS launch on Windows 11? · How do I add my NVR or DVR to Smart PSS? · Why can't I export clips in Smart PSS Lite? · Why is Smart PSS slow, freezing, or crashing? · Can Smart PSS manage multiple locations? · Do you support Smart PSS systems you didn't install? · Is Smart PSS the same as the DMSS phone app? · Can you set up Smart PSS remotely? · How much does Smart PSS setup or support cost in NYC?

### smart-pss-support-setup-bronx — REBUILT 2026-10-18 (owns these intents)
§9 Q&A (H3):
1. A detective is at the counter asking for last night's video — what should we export from SmartPSS Lite, and in which format?
2. Should we list our cameras with BronxCAMS, and what will the DA's office actually ask us for later?
3. The time on our clip is an hour off from when it really happened — will that cause problems, and how does it get fixed?
4. We need four hours from three cameras and the export bar barely moves — what is the faster way to pull a long stretch?
5. Our exported MP4 plays sideways or squashed on the adjuster's laptop — what went wrong?
6. A package went missing from the lobby table sometime over three days — is there a faster way to find it than scrubbing the timeline?
7. The only computer in the store is an old 32-bit laptop — can SmartPSS Lite run on it at all?
8. Our camera PC is still on Windows 10 — is it all right to keep it as the SmartPSS machine?
9. After a blackout the PC comes back to the Windows login and the camera wall stays dark until the owner arrives — can it restart on its own?
10. With sixteen cameras open, the little CPU icon turns red and the picture stutters — which settings actually help?
11. Where does SmartPSS put the snapshots and recordings it saves on the PC, and how do we stop the drive from filling up?
12. If thieves take the recorder, is there any way the PC could have kept its own copy of the cameras?
13. Our super is leaving next week and a new one starts Monday — what should change in SmartPSS and on the recorder that day?
14. The camera PC in the super's office is the same computer that holds rent records — can the camera program be locked when he steps out?
15. Can the front-door camera pop up on the super's screen when someone forces the courtyard gate at night?
16. The managing agent watches from an office in another neighborhood and the picture keeps freezing — is it their internet or ours?
17. The recorder shows online in the DMSS app but offline in SmartPSS Lite on the same desk — where do we look first?
18. Someone told the owner to open port 37777 on the router so the PC can see the recorder from home — is that a good idea?
19. Our night manager still keeps the old SmartPSS 2.0 next to Lite because saving clips felt quicker — can the store keep both?
20. With all the FCC news about Dahua, will SmartPSS stop working on the cameras we already own?
CTA H2 (not a Q&A): Not Sure Which SmartPSS Is on Your PC?
§17 FAQ:
1. What should we have ready before the technician comes to set up SmartPSS?
2. Can you set SmartPSS up on the computer we already have instead of selling us a new one?
3. Will the cameras keep recording while you work on the SmartPSS computer?
4. Can you come before the gates go up or after the store closes?
5. Who ends up holding the passwords after the visit?
6. Can you teach our night clerk to export a clip without calling anyone?
7. Will you fill out the BronxCAMS registration for us?
8. What happens if the problem turns out to be the recorder and not SmartPSS?
9. How is payment handled for a SmartPSS visit in the Bronx?
De-dup notes: overlaps with old-template intents deliberately reframed — Q17 (phone works/PC offline, credential-vs-network) vs old "devices offline"; Q19 (keeping the old client beside Lite) vs old "old Smart PSS can't connect"; Q13/Q14 (super changeover, shared PC lock) vs old "manager view-only access"; Q10 (CPU icon/stream settings) vs old "freezing and crashing". Mechanical check (tools/check_page.py) found no masked-exact question matches with any sibling. Later rebuilds should leave the Bronx-owned intents above (BronxCAMS, detective export format, clock offset, 32-bit/Windows 10 PC, super changeover, port 37777, FCC continued use) to this page and take different angles (e.g. multi-site organization trees, DSS step-up, Mac clients, access-control/attendance modules, intercom, LTE/hotspot sites, seasonal homes).

### Build notes (Bronx)
- tools/check_page.py: only failures are 14 × "live sibling … doesn't link back to /smart-pss-support-setup-bronx" (main-run wiring). Words 13,834; 185,728 bytes (siblings ~124 KB, outside the 2 KB cluster).
- Masked-geo similarity (difflib word sequence on body paragraphs): vs smart-pss nyc/brooklyn/manhattan page 0.030, paragraph max 0.30; vs dmss-app-support-repair-bronx 0.022 / 0.38; hik-connect-app-support-repair-bronx 0.022 / 0.38; guarding-vision-app-support-repair-bronx 0.020 / 0.38; dahua-camera-installation-bronx 0.019 / 0.30; dvr-upgrade-bronx 0.017 / 0.31; hik-connect-app-support-repair-manhattan 0.070 (para max 0.88 = shared warranty/NAP sentence); security-camera-maintenance-bronx 0.103 and nvr-installation-bronx 0.068 (para max 1.00 = identical freshness byline / NAP boilerplate only). 8-word-shingle Jaccard vs all 15 silo pages ≤0.013 (residue = shared nav chrome).
