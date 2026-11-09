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


## Manhattan — REBUILD batch 2026-10-18 (smart-pss-support-setup-manhattan): silo findings, question-register additions and local research

## Smart PSS Support Setup — silo research (incoming, Manhattan rebuild)

Written 2026-10-18 by the subagent rebuilding `smart-pss-support-setup-manhattan` (queue line: `REBUILD | smart-pss-support-setup-manhattan | Smart PSS Support Setup | Manhattan | up /smart-pss-support-setup-nyc | direct phone (929) 560-0737 | GBP Bronx`). `research/smart-pss-support-setup.md` did not exist on main; this file sits in `research/_incoming/` for the main run to merge (sibling builds for Bronx and Ulster County may write their own silo findings — merge, don't duplicate).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search (`mcp__Fire_Crawl__firecrawl_search`), Firecrawl scrape (markdown / query mode / PDF parser), Firecrawl Alexandria `census-gov` provider, WebSearch. Shell curl blocked. WebFetch to ipcamtalk.com failed (client error) — those rows come from Firecrawl scrape. Reddit cannot be scraped (Firecrawl refuses reddit.com) → Reddit rows are **search-result excerpts only**. "Excerpt" = read only as a snippet.

Page section labels (Manhattan page): §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts), §Repair (same-day block + checks + symptom table), §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ connection-method table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

**Manhattan thesis:** *Smart PSS in Manhattan lives on somebody else's PC on somebody else's network.* The client runs on a front-desk, security-office, office-manager or back-office Windows workstation that a building IT contractor, tenant IT department or managing agent controls. The work is (1) moving desks off the discontinued SmartPSS onto SmartPSS Lite on locked-down PCs, (2) reaching the recorder across VLANs/firewalls without exposing it, (3) sizing large buildings past Lite's 64-device / 64-channel ceiling, and (4) operator accounts, export procedure and NYC privacy rules (biometric signage, Tenant Data Privacy Act, Labor Law 203-c, Penal Law 250.05).

---

### Part 1 — Silo-wide findings

#### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows R1–R8). |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and works from claims repeated in forums/blogs (rows D1–D6, R1–R8, I1–I4). |
| 6 | Area landmarks | Manhattan section M-L1–M-L6. |
| 7 | Area use cases / building stock | Manhattan section M-H1, M-O1. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only WebSearch/Firecrawl backends; no Bing/DDG PAA, related or autocomplete surface. |
| 9 | Local news | M-N1 (amNY), M-N2 (NYT headline excerpt). |
| 10 | Hyperlocal | Brick Underground package-theft piece (excerpt, M-N3). West Side Rag / Patch Manhattan camera-software items: EMPTY (none surfaced). |
| 11 | Yelp 1–3★ | `yelp security camera installation Manhattan NY reviews "Smart PSS" OR "Dahua" software setup complaint` · Firecrawl search → only Yelp search-listing pages (e.g. https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Manhattan%2C+NY — "Rating 4.7(1,481)"); no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

#### 1.2 Dahua primary sources (D)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D1 | `Dahua DSS Agile SmartPSS Plus new PC client replaces SmartPSS Lite 2025` · Firecrawl search → scrape | https://dahuawiki.com/SmartPSS_Lite | Banner: "NOTE: SmartPSS has been discontinued and is no longer supported for Windows and M Series Macintosh Computers. Please download and install SmartPSS Lite instead." Download table lists Windows and "macOS M Series" downloads; user, access-control and attendance manuals. Page last modified 27 June 2025. | §Hero; §5 para 2; §5.5; §6 migration card; §9 "old SmartPSS from 2020" H3; §10.5 H3 1; §Sources |
| D2 | same → scrape | https://dahuawiki.com/Discontinuation_of_SmartPSS | Notice is an image only (text not readable in build env); page last modified 2 October 2024. | §5.5 ("notice page dated October 2024"); §Sources |
| D3 | `SmartPSS Lite system requirements Windows download Dahua user manual` · WebSearch → Firecrawl scrape (PDF) | https://cdn.document360.io/0b8a1602-1fb0-4465-a168-a93a81974a0b/Images/Documentation/SmartPSS%20Lite_datasheet%20V1.003.0000000.0_20220606.pdf | SmartPSS Lite datasheet V1.003 (2022-06-06): "lightweight platform … for small and medium-sized businesses"; P2P linking, live view, playback, event center, access control, attendance. Config requirement CPU i5-6500 @3.20GHz, 8 GB, 256 GB HDD; Windows 7/8/10 64-bit; resolution 1280×800+. **Devices 64; Video channels 64; Access channels 64.** Image/video and database storage time 62 days default, up to 365. Device types IPC, fisheye, XVR, DVR, NVR, ASC, ASI, ASA, TPC. Decoding 64-ch D1 on the reference PC. Arbitrary split up to 64-ch preview. Storage method local HDD. Access control: 1,000 people; remote open/close doors. Attendance: 1,000 people, 19 report types, 32 shifts. Alarm: tripwire, intrusion, SMD, face detection. | §5.5; §6; §7.5; §9 64-camera, four-screen, retention H3s; §10 cards; §10.5 H3 4, 5; §17 FAQ; §Sources |
| D4 | `site:… SmartPSS Lite P2P` · Firecrawl scrape | https://dahuawiki.com/SmartPSS_Lite/SmartPSS_Lite_P2P_Setup | Steps: on recorder Network > P2P verify enabled and "Online"; SmartPSS Lite Home > Device Manager > + Add > Method "SN(For Device Support P2P)"; name, SN, username, password; verify Online Status green; Home > Monitor > Live View. Modified 13 Feb 2024. | §Repair table; §9 serial-vs-IP H3; §Sources |
| D5 | `Dahua default ports 37777 TCP 37778 UDP 80 554 P2P remote access SmartPSS` · Firecrawl search (excerpts) | https://dahuawiki.com/NVRiSettingNetwork ; https://dahuawiki.com/IPCRemoteAccess | Default ports TCP 37777, UDP 37778, HTTP 80, HTTPS 443, RTSP 554. | §7.5 IT paragraph; §9 VLAN H3; §10 table; §10.5 H3 2; §Sources |
| D6 | `SmartPSS Lite forgot login password reset security question admin account client` · Firecrawl search (excerpt of manual) | https://dahuawiki.com/images/a/a4/SmartPSSLite_User%27s_Manual_Eng.pdf | SmartPSS Lite User's Manual V1.0.0 (April 2022): first login initialises the client with its own password and security questions; "Remember Password" option; "Forgot password?" resets via security questions; device added by IP shows Port 37777 default. | §9 auto-login H3; §17 FAQ (Windows account); §Sources |
| D7 | `SmartPSS Lite video wall multiple monitors extend screen tour live view security desk` · Firecrawl search → scrape (PDF, query) | https://dahua-store.ru/wp-content/uploads/2025/01/smartpsslite_monitor-manual_eng.pdf | SmartPSS Lite Monitor Solution manual: clip/download formats "dav, avi, mp4, asf" (§3.3.1); tours (§2.2.2), view groups (§2.2.3); local record saved to ".../Data/User/Record"; Security Recommendation appendix: add users and "allocate a minimum set of permissions"; strong passwords, account lock, "Enable Account Binding IP/MAC". | §6; §9 guard permissions + detective H3s; §10.5 H3 6; §17 FAQ local recording; §Sources |
| D8 | same search (excerpts) | https://dahuawiki.com/SmartPSS/How_To_Use_SmartPSS_With_Two_Monitors ; https://www.youtube.com/watch?v=b5nXTepC6MI | Dahua wiki multi-monitor how-to (tabs dragged to second monitor); video title/description: client "with up to 4 monitors, each of which runs up to 64" (excerpt, applies to old SmartPSS video). | §9 four-screen H3 (described cautiously: tabs to separate monitors) |
| D9 | `SmartPSS Lite export AVI DAV format convert player evidence police` · Firecrawl search (excerpts) | https://dahuawiki.com/SmartPSS/How_To_Export_Device_Record ; https://support.amcrest.com/hc/en-us/articles/360002005131-How-To-Convert-DAV-to-AVI-Files ; https://ipcamtalk.com/threads/recommend-dav-to-mp4-converter-please.30193/ | Export via Playback; DAV is Dahua's native format, Smart Player converts DAV→AVI; IPCamTalk: SmartPSS exports to AVI, MP4 etc. | §9 detective H3; §10.5 H3 6 |

#### 1.3 Federal / security (F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F1 | `FCC July 2026 order prohibits importation marketing Hikvision Dahua covered equipment existing devices continue use` · Firecrawl search (full excerpt) | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment | Prohibits continued importation and marketing of covered equipment added to the Covered List in 2024 or earlier; effective 10 days after publication; for use-based entries the prohibition applies only to importation/marketing for the covered uses; "does not affect the continued use or operation of previously authorized covered equipment; consumers may continue to use any device or equipment that they currently possess…"; replacements: "would defeat the entire purpose of this prohibition". | §5 para 4; §8.5; §9 not used as Q (intent kept to body); §10.5 H3 7; §Sources |
| F2 | `https://www.fcc.gov/supplychain/coveredlist` · Firecrawl scrape (query, direct quote) | https://www.fcc.gov/supplychain/coveredlist | Dahua entry: "Video surveillance and telecommunications equipment produced by Dahua Technology Company, to the extent it is used for the purpose of public safety, security of government facilities, physical security surveillance of critical infrastructure, and other national security purposes…" — date of inclusion March 12, 2021. | §5.5; §8.5; §10.5 H3 7; §Sources |
| F3 | `CVE-2021-33044 Dahua authentication bypass CISA known exploited vulnerabilities` · Firecrawl search (excerpts) | https://nvd.nist.gov/vuln/detail/cve-2021-33044 ; https://www.cisa.gov/news-events/alerts/2024/08/21/cisa-adds-four-known-exploited-vulnerabilities-catalog | "Attackers can bypass device identity authentication by constructing malicious data packets." In CISA KEV as "Dahua IP Camera Authentication Bypass Vulnerability", added August 21, 2024, due September 11, 2024. | §6 firmware card; §10.5 H3 2; §8.5; §Sources |

#### 1.4 Forums, Reddit, blogs (R / I) — feed §10.5 and the symptom table
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com SmartPSS Lite problem Dahua` · Firecrawl search | https://www.reddit.com/r/Dahua/comments/1rrcoj3/i_can_access_my_cameras_using_the_dmss_app_but/ | Excerpt: "Update 3/12/26 Dahua says that is a global issue. No ET to fix the issue. I can access my cameras using the DMSS app but not with SmartPSS Lite". | §9 serial-vs-IP H3; §10.5 H3 3; §Sources |
| R2 | same | https://www.reddit.com/r/Dahua/comments/1sqfrbz/cant_remote_access_via_smartpsslite_but_can_with/ | Excerpt: locally shows device on Port 37777 … can't remote access via SmartPSS Lite but can with DMSS. | §10.5 H3 3 |
| R3 | same | https://www.reddit.com/r/Dahua/comments/1w7fqvl/cant_connect_through_p2p_on_smartpss_lite_dmss/ | Excerpt reply: "Go to Menu > Maintain > Network > Advanced network detection. Change your DNS if needed, and or check your router for filter blocking." | §Repair checks |
| R4 | same | https://www.reddit.com/r/Dahua/comments/1f88393/new_smartpss_lite_wrongly_registers_my_nvrs_as/ | Excerpt: "SmartPSS light has a hard limit of 64 channels total. You'll get this error as soon as more than 64 channels have connected to the software." | §9 64-camera H3; §10.5 H3 4 |
| R5 | same | https://www.reddit.com/r/Dahua/comments/1law4a8/smartpss_lite_sound_is_not_enabled_on_the_local_pc/ | Excerpt: three PCs suddenly output "Sound is not enabled on the local PC". | §17 FAQ alarm sound |
| R6 | same | https://www.reddit.com/r/Dahua/comments/1ptwgl7/smartpss_lite_download_failed_to_export/ | Excerpt: "Failed to export" after ~30 s. (Export-failure intent is in the register → not used as a question; background for §9 detective H3.) | Background |
| R7 | same | https://www.reddit.com/r/Dahua/comments/1u2bsz9/smartpss_lite_not_getting_ivs_tripwire/ | Excerpt: check audio plays; check volume mixer for SmartPSS Lite. | §17 FAQ alarm sound |
| R8 | `Dahua DSS Agile …` · Firecrawl search | https://www.reddit.com/r/Dahua/comments/1liq1nz/smart_pss_alternative/ | Excerpt: direct to NVR, Lite limited to 64 channels. | §9 64-camera H3 |
| I1 | `Dahua SmartPSS Lite vs SmartPSS end of life DSS Agile replacement` · WebSearch → Firecrawl scrape (direct quote) | https://ipcamtalk.com/threads/what-happened-to-smartpss.75955/ | "Can't find it on Dahua's website anymore for PC…" — "Its gone. They're pushing a new subscription model with DSS Pro." — "You can still download the Lite version which works pretty well…" | §10.5 H3 1; §Sources |
| I2 | `SmartPSS Lite Windows 11 not opening crash fix "SmartPSS Lite" ipcamtalk` · Firecrawl search → scrape | https://ipcamtalk.com/threads/old-apps-gdmss-idmss-and-smartpss-2-0-will-stop-support-p2p-from-august-1.77062/ | 2024 thread: information from Dahua Poland that from August 1 Dahua cloud stops P2P connections from old gDMSS/iDMSS and "old SmartPSS 2.0 apps from 2019/2020". | §9 old-SmartPSS H3; §Repair table; §Sources |
| I3 | same search (excerpt) | https://ipcamtalk.com/threads/old-smartpss-v2-003-cannot-connect-to-dahua-nvr-starting-today-but-smartpss-lite-can.78475/ | Title: "old SmartPSS (v2.003) cannot connect to Dahua NVR starting today, but SmartPSS lite can." | §9 old-SmartPSS H3 |
| I4 | `… DSS Agile …` (excerpt) | https://janexint.com.pl/…/DSS%20Express%20VS%20SmartPSS-EN.pdf | "DSS Express will gradually open the gap with Smart PSS, replacing Smart PSS as the infrastructure…" (excerpt). | §10 DSS card (background) |

#### 1.5 Keywords — five layers (silo)
- **Service:** Smart PSS support, SmartPSS setup, SmartPSS Lite installation, Smart PSS configuration, SmartPSS migration, desk client setup, video wall setup, footage export, operator accounts.
- **Problem:** SmartPSS discontinued, old SmartPSS won't connect, device offline in SmartPSS Lite, P2P offline, 64-channel limit / max channel error, sound not enabled, failed to export, locked-down PC, firewall blocking 37777.
- **Technology:** Dahua NVR/XVR/DVR, SmartPSS Lite, DSS Express / DSS Pro, DMSS, P2P (SN), TCP 37777 / UDP 37778 / RTSP 554, VLAN, .dav/.avi/.mp4/.asf, Smart Player, IVS tripwire, SMD, face detection, ASI/ASC/ASA access and attendance terminals.
- **Industry:** co-ops and condos with front desks, doorman rentals, managing agents, office tenants (Class A/B), showrooms, retail, restaurants, medical suites, security guard firms.
- **Geographic (Manhattan page):** Manhattan; Midtown; Garment District; Hudson Yards / Manhattan West; Flatiron District / Silicon Alley; Chelsea (W 21st St & Seventh Ave); Stuyvesant Town–Peter Cooper Village; Canal Street / Chinatown / SoHo / Tribeca; Lower Manhattan / Water Street; Midtown East / Third Avenue; Upper West/East Side; Harlem; Washington Heights; Inwood.

#### 1.6 Silo pricing (no invented prices) — FLAG
The 16 old Smart PSS pages publish **no dollar figures**. The Manhattan page uses only: $0 phone/screenshot triage; protected service rate $195/hr, 3-hr minimum ($585) (v2.3 §9, verbatim, not multiplied — same as the rebuilt Hik-Connect Manhattan page); recorder replacement = DVR Upgrade silo base (research/dvr-upgrade.md §1.8) × Manhattan 1.25: 4-ch $563–$875, 8-ch $813–$1,250, 8-ch hybrid $1,000–$1,500, 16-ch $1,500–$2,750, 32-ch $2,750+. DSS server installs above Lite's 64-channel ceiling: "quoted after a walk-through" (no number). FLAG for Anwar: confirm Smart PSS silo may borrow DVR replacement prices.

---

### Question register — Smart PSS Support Setup silo

#### Existing 15 sibling pages (old shared template — identical on all 15; also the old Manhattan page)
Visible H3s (9): What is Smart PSS used for? · How do I install Smart PSS? · How do I add cameras to Smart PSS? · Why is Smart PSS not connecting? · Which Smart PSS for Windows 11? · Where do I download Smart PSS safely? · Can Smart PSS do remote viewing? · Is there a Smart PSS for Mac? · Smart PSS still not cooperating?
FAQ schema (13): Is Smart PSS a camera brand? · Difference between Smart PSS and Smart PSS Lite? · Why does Smart PSS show my devices offline? · Why won't Smart PSS connect on Windows 11? · How do I add my NVR or DVR to Smart PSS? · Why can't I export video clips in Smart PSS Lite? · Why is Smart PSS slow, freezing, or crashing? · Can Smart PSS manage cameras across multiple locations? · Do you support Smart PSS systems you didn't install? · Is Smart PSS the same as the DMSS phone app? · Does Smart PSS work with third-party cameras? · Can you set up Smart PSS remotely? · How much does Smart PSS setup or support cost in NYC?
**Intents reserved by the register (not reused on Manhattan):** what-it-is / brand; install; add device; not connecting / offline (generic); Windows 11; safe download; remote viewing (generic); Mac; Lite-vs-full difference; export failure; slow/crash; multi-location; non-AESS systems; DMSS vs PSS; third-party cameras; remote setup; cost.

#### Manhattan page (new) — §9 Q&A (H3)
1. The building's IT contractor locked down the lobby PC — what does SmartPSS Lite need permission to do?
2. Should the desk's SmartPSS Lite sign itself back in after a power cut, or wait for a person?
3. Our lobby workstation still runs the SmartPSS release installed around 2020 — what changes if we leave it alone?
4. How do we stop an overnight guard from changing recorder settings through the desk client?
5. The recorder sits on the camera VLAN and the desk PC on the office VLAN — which traffic has to cross between them?
6. When the PC and the recorder are in the same building, should the client reach the recorder by serial number or by local address?
7. Our tenant firewall blocks unknown outbound traffic — can the desk client work with no cloud path at all?
8. How should a security office with a few hundred cameras divide them between desk workstations and operators?
9. What does a security office need to run a four-screen camera wall from one workstation?
10. How long does the client keep its own snapshots, alarm records and logs on the PC?
11. A detective asked for the lobby recording from one night — who at the building should handle it, and what goes in the hand-over?
12. Do face-detection alarms in SmartPSS Lite put our store under the city's biometric signage rule?
13. If the co-op adds face-reader entry managed from SmartPSS Lite, what does the Tenant Data Privacy Act ask of the board?
14. What should the desk write down each time someone views or exports footage?
15. Our office floor and the landlord's lobby both run Dahua recorders — can one PC show both without blurring who controls what?
16. Will the attendance module work as a restaurant's time clock?
17. What should be ready before the technician sits down at the desk PC?
18. Does the building's IT person have to be there for the visit?

#### Manhattan page (new) — §17 FAQ (= FAQPage schema)
1. Does SmartPSS Lite record anything on the PC itself, or only display the recorder?
2. Can the desk PC sound an alarm when a door is held or forced open?
3. Which Windows account should run SmartPSS Lite on a shared front-desk computer?
4. If the desk computer dies, do the cameras stop recording?
5. Can the doorman release the lobby door from SmartPSS Lite?
6. When the guard contract moves to a new company, what has to change at the desk before their first night?
7. Should the desk PC connect over the building's Wi-Fi?
8. What if company policy blocks USB drives on the desk PC?
9. How much disk does the desk computer need for saved clips?
10. How do we keep busy-avenue alarms from flooding the desk all night?

---

### Manhattan

#### M-H Building stock (census)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-H1 | Alexandria `census-gov` `census/data` · dataset acs/acs5, vintage 2023, variables B25024_001E, B25024_008E, B25024_009E, B25035_001E, B25003_001E, B25003_003E, geography county:061 in state:36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36061 | New York County: 918,806 housing units; 201,967 in 20–49-unit buildings; 522,823 in 50+-unit buildings; median year built 1951; 775,376 occupied, 583,733 renter-occupied. | §5 para 1; §5.5; §Sources |

#### M-O Office stock
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-O1 | `Manhattan office inventory square feet 2025 Class B buildings vacancy report` · Firecrawl search → scrape (query) | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-office-market/ | NYC Comptroller Spotlight, May 14, 2024: Manhattan office space 5-star 75,619,534 sq ft; 4-star 271,349,692; Class B 172,960,516; 3-star or less 14,085,410. Conversion-incentive eligibility: below 59th Street, ≥250,000 gsf, built before 2000; examples 175 Water St (now 161 Water, 1982, 580,000 sq ft, 97% vacant) and 850 Third Avenue (1959, 575,000 sq ft). | §5 para 2; §5.5; §7 cards; §8 cards; §Sources |

#### M-L Landmarks / corridors
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-L1 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Garment_District,_Manhattan | Fifth–Ninth Ave, 34th–42nd St; showrooms; manufacturing lofts converted to offices (accountants, lawyers, PR, tech) and apartments. | §8 card; §13 card |
| M-L2 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Hudson_Yards,_Manhattan | 30th–41st St, West Side Hwy–Eighth Ave; 60-block rezoning approved January 2005; Phase 1 opened March 15, 2019; Manhattan West between 31st–33rd west of Ninth; 10th Precinct. | §8 card; §13 card |
| M-L3 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Flatiron_District | 14th–23rd St, Sixth Ave–Park Ave South; birthplace of "Silicon Alley". | §8 card; §13 card |
| M-L4 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Stuyvesant_Town%E2%80%93Peter_Cooper_Village | 110 red-brick buildings, 11,250 apartments, First Ave–Avenue C, 14th–23rd St; first building opened August 1, 1947; 13th Precinct. | §7 card; §9 64-camera H3 (as example of scale only, no claim about its cameras); §13 card |
| M-L5 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Canal_Street_(Manhattan) | East Broadway to West Street; through Chinatown; southern edge of SoHo/Little Italy, northern edge of Tribeca; low-rent open storefronts, banks and jewelry shops to the east. | §8 card; §13 card |
| M-L6 | amNY scrape (below, M-N1) | — | Chelsea, West 21st Street & Seventh Avenue lobby. | §13 card |

#### M-N News / hyperlocal / Reddit (local)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-N1 | `West Side Rag OR "Upper East Site" OR Patch Manhattan building surveillance footage package theft lobby 2025` · Firecrawl search → scrape (query) | https://www.amny.com/news/thief-snatches-package-from-lobby-of-manhattan-building-nypd/ | Dec 15, 2020: man stole a $400 clothing package from a Manhattan apartment-building lobby near West 21st Street and Seventh Avenue; NYPD released photos and video of the suspect. | §5 para 3; §13; §Sources |
| M-N2 | same search (excerpt/headline) | https://www.nytimes.com/2021/02/19/nyregion/package-theft-east-village.html | NYT Feb 19, 2021 headline: "90,000 Packages Are Stolen in N.Y.C. Every Day. How One Building…" (East Village); excerpt: footage showed a masked man unlocking the door with a plastic card. | §5 para 3; §Sources (excerpt) |
| M-N3 | same search (excerpt) | https://www.brickunderground.com/live/realty-bites-dealing-with-package-delivery-theft-landlords-nyc | Landlord "should be willing to look at security camera footage". | Background §9 log H3 |
| M-R1 | `site:reddit.com NYCapartments building security camera footage management won't share doorman` · Firecrawl search | https://www.reddit.com/r/NYCapartments/comments/1bjwldr/package_stolen_from_lobby_of_building_i_just/ | Excerpt: "Landlord is saying that the security camera systems are down and that there is nothing they can do about a stolen package." | §5 para 3; §FieldNotes; §Sources |
| M-R2 | same | https://www.reddit.com/r/AskNYC/comments/1bfjfdu/is_there_a_way_to_force_a_landlord_to_show_me_the/ | Excerpt: building with lobby cameras, no doorman, packages stolen, tenant asks how to force landlord to show the feed. | §9 log H3 (context) |
| M-R3 | same | https://www.reddit.com/r/AskNYC/comments/ot6tw4/i_think_people_might_be_casing_our_apartment_or/ | Excerpt: "Good management never gives security camera video to anyone except police." | §9 log H3 (quoted as a resident view) |

#### M-K Local law / licensing
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-K1 | `NYC biometric identifier information law commercial establishments signage Administrative Code 22-1202 DCWP` · Firecrawl search (full excerpts) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-131285 ; https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=3704369&GUID=070402C0-43F0-47AE-AA6E-DEF06CDF702A | §22-1202(a): commercial establishments (places of entertainment, retail stores, food and drink establishments) that collect/retain/convert/store/share customers' biometric identifier info must post a clear sign near all customer entrances; (b) no selling/sharing for value. L.L. 2021/003, eff. 7/9/2021. Definition incl. "a scan of hand or face geometry". Damages $500 / $5,000; 30-day notice before suit on (a). | §8.5; §9 face-detection H3; §Sources |
| M-K2 | `NYC Tenant Data Privacy Act Local Law 63 2021 smart access systems multiple dwellings requirements` · Firecrawl search (excerpts) | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page ; https://www.hinshawlaw.com/en/insights/privacy-cyber-and-ai-decoded-alert/privacy-law-essentials-new-york-citys-tenant-data-privacy-act | HPD: owners of multiple dwellings using smart access (key fobs, RFID cards, phone apps, biometric identifiers…) to grant entry to class A multiple dwellings, common areas or units must provide tenants a data retention and privacy policy; may not use location tracking outside the building. Effective July 29, 2021; existing buildings to comply by January 1, 2023 (law-firm excerpt). | §7.5; §8.5; §9 TDPA H3; §Sources |
| M-K3 | (silo knowledge reused from research/hik-connect-app-support-repair.md, sourced there) | https://nysenate.gov/legislation/laws/PEN/250.05 ; FirstService Residential guide | Penal Law §250.05 eavesdropping; Labor Law §203-c no video in restrooms/locker/changing rooms. | §8.5 |
| M-K4 | `Manhattan office building tenant IT network firewall blocks security camera software VLAN landlord base building network` · Firecrawl search (excerpt) | https://nyflnerds.com/firewall-management-smbs-nyc-rules/ | NYC IT firm (Mar 17, 2026): typical NYC office VLAN layout separates corporate users, servers, VoIP, "Cameras/IoT: security cameras, NVRs", guest Wi-Fi, management; rule mindset "default deny between VLANs". | §5 para 2; §7.5; §9 VLAN H3; §Sources |

#### Manhattan sources EMPTY
- Google PAA / PASF / AI Overview / ATP / Bing / DDG — EMPTY (not accessible in build env).
- Yelp 1–3★ (Manhattan) — EMPTY (only listing pages).
- West Side Rag / Patch / Upper East Site camera-software items — EMPTY (none surfaced).
- Field Notes: no real AESS Manhattan anecdote supplied → written as a method note, no story.

#### Semantic de-dup note (vs Ulster rebuild in the same batch)
Ulster (built in parallel) asks about the "max channel" error after migration, DSS for multi-store, adjuster can't open exports and removing one farmhand's access. Manhattan's matching questions were re-framed to distinct intents: dividing a control room's cameras by duty across workstations (Q8), who owns a police request and the hand-over (Q11), and a whole guard-company changeover (FAQ 6). Masked paragraph similarity vs Ulster, Bronx, NYC hub and every other sibling < 0.65 except the mandatory warranty sentence.

#### Images
images: 11 reused from images/dahua-camera-installation/ (suffolk-county, long-island), images/network-installation/, images/nvr-installation/ (no real Smart PSS photos yet). Mapping in the page build report.

| # | File (images/smart-pss-support-setup/) | Source |
|---|---|---|
| 1 | smart-pss-support-setup-manhattan-thirty-two-tile-recorder-monitor-under-ceiling-cables.webp | images/nvr-installation/nvr-installation-bronx-recorder-monitor-camera-grid-under-cable-runs.webp |
| 2 | smart-pss-support-setup-manhattan-per-channel-kbps-table-on-monitor.webp | images/network-installation/network-installation-suffolk-county-recorder-screen-per-channel-bitrate-table.webp |
| 3 | smart-pss-support-setup-manhattan-purple-patch-cable-bundle-beside-rack.webp | images/network-installation/network-installation-suffolk-county-cable-bundles-dropping-into-rack-side.webp |
| 4 | smart-pss-support-setup-manhattan-twelve-camera-store-split-screen-on-ceiling-monitor.webp | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-camera-grid-on-ceiling-mounted-monitor.webp |
| 5 | smart-pss-support-setup-manhattan-recorder-tile-brick-wall-and-lot-with-date-stamp.webp | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-recorder-view-along-brick-wall-to-lot.webp |
| 6 | smart-pss-support-setup-manhattan-black-bullet-camera-on-corridor-ceiling-facing-grey-door.webp | images/dahua-camera-installation/dahua-camera-installation-long-island-bullet-camera-aimed-down-corridor-to-door.webp |
| 7 | smart-pss-support-setup-manhattan-dome-camera-on-steel-arm-under-patterned-cornice.webp | images/dahua-camera-installation/dahua-camera-installation-long-island-dome-camera-on-long-wall-arm-on-stone-facade.webp |
| 8 | smart-pss-support-setup-manhattan-white-turret-camera-in-ceiling-above-glass-entrance-wall.webp | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-turret-camera-above-glass-storefront.webp |
| 9 | smart-pss-support-setup-manhattan-dahua-mini-pan-tilt-dome-product-photo.webp | images/dahua-camera-installation/dahua-camera-installation-long-island-white-mini-pan-tilt-dome-product-photo.webp |
| 10 | smart-pss-support-setup-manhattan-dim-recorder-tile-of-crowded-back-storeroom.webp | images/nvr-installation/nvr-installation-bronx-recorder-tile-dim-back-storeroom.webp |
| 11 | smart-pss-support-setup-manhattan-small-cameras-high-on-white-wall-of-open-hall.webp | images/dahua-camera-installation/dahua-camera-installation-long-island-small-cameras-on-high-wall-of-open-hall.webp |


## Ulster County — REBUILD batch 2026-10-18 (smart-pss-support-setup-ulster-county): silo findings, question-register additions and local research

## Smart PSS Support Setup — silo research + Ulster County (incoming part file)

Page: `smart-pss-support-setup-ulster-county` (REBUILD in place 2026-10-18; Google "Crawled – currently not indexed" as a near-duplicate area-swapped template). Queue line: `REBUILD | smart-pss-support-setup-ulster-county | Smart PSS Support Setup | Ulster | up /smart-pss-support-setup-hudson-valley | direct phone (845) 640-3835 | GBP Bronx`.
Routing used: direct line (845) 640-3835 in body/CTAs/schema; (800) 486-0943 only in the shared header chrome; GBP Bronx (460 E Fordham Rd, Bronx NY 10458, schema `@id` #bronx); WhatsApp only as wa.me/17186790359.

Written by the Ulster subagent for the coordinator to merge into `research/smart-pss-support-setup.md` (which did not exist on main at build time; the Bronx and Manhattan builders may write their own parts). Format v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`), WebSearch, WebFetch. Shell curl blocked. WebFetch could not open ipcamtalk.com (CLIENT_ERROR) — those threads were read through Firecrawl scrape instead. Firecrawl does not scrape reddit.com, so Reddit rows are search excerpts only. Nothing invented; excerpts marked.

---

### Part 1 — Silo-wide findings (SmartPSS / SmartPSS Lite / DSS)

#### 1.1 Mandatory sources (v2.3 §3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (S-R1–S-R6 below). Full threads not readable in this environment. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — the page's §10.5 says so and tests seven claims commonly repeated in forum answers/tutorials, corrected with the sources below |
| 6 | Landmarks | Ulster section U-rows + carried rows |
| 7 | Use cases / building stock | Ulster section (carried Census rows) |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Hudson Valley One (Archtop Fiber 2026; Kingston police cameras 2026, carried); Central Hudson release (carried) |
| 10 | Hyperlocal | HV1; Ulster County Comptroller; Radio Catskill (carried) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

#### 1.2 Product status — SmartPSS discontinued, SmartPSS Lite, DSS
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| S1 | `Dahua SmartPSS end of life replaced SmartPSS Lite DSS Agile` · WebSearch → Firecrawl scrape | https://ipcamtalk.com/threads/what-happened-to-smartpss.75955/ | Thread started Apr 23 2024: "Can't find it on Dahua's website anymore for PC". Reply (bigredfish): "Its gone. They're pushing a new subscription model with DSS Pro. You can still download the Lite version…". Reply (ludshed): Lite "won't work with more than 16 channel units" / "max channel error on 24, 32 and above units" (forum report). | §5 para 2; §9 cluster 1; §10.5 H3 1; Sources |
| S2 | same · Firecrawl scrape | https://dahuawiki.com/SmartPSS_Lite | DahuaWiki banner: "SmartPSS has been discontinued and is no longer supported for Windows and M Series Macintosh Computers. Please download and install SmartPSS Lite instead." Lite = "lightweight platform … for small and medium-sized businesses (SMB). It offers video surveillance, access control and various attendance functions … P2P linking, real-time monitoring, video playback, event center". Downloads listed: Windows and macOS M Series. Datasheet V1.003 (2022-06-06). Page modified 27 June 2025. | Hero; §5 para 2; §5.5; §6 cards; §10; FAQ access control; Sources |
| S3 | same · Firecrawl scrape | https://dahuawiki.com/Discontinuation_of_SmartPSS | Notice page (image only), last modified 2 Oct 2024. Text of the image not readable → page cites only the existence/date of the notice. | §5.5; Sources |
| S4 | `SmartPSS Lite "max channel" error` · WebSearch → Firecrawl scrape | https://ipcamtalk.com/threads/smartpss-lite-max-channel-error.76061/ | Started Apr 30 2024. Installer: new NVR (SN with "RAZ", model ending 4KS3) would not connect to old SmartPSS; DahuaWiki note quoted: "New devices on the latest firmware will not work on older versions of SmartPSS via P2P. Please update to the latest version of SmartPSS". Poster (oh6hfx): "in new 30. september 2024 update SmartPSS max channel limit is reduced to 32. However, it means online channels"; workaround: leave "auto log in to device" unchecked and log in only to devices needed. Same poster: "10 minutes continuous live view and then stream is closed" — later "it is P2P which has now this limit". Reply (steve1225): if an ISP/firewall blocks P2P the connection goes "over Dahua cloud for a full stream (then there is 10 minutes limit…)" (forum explanation, not Dahua's). Also: "empty new installation without any device added and it takes 100% cpu" (one user's report). | §5 para 2; §5.5; §9 Q1, Q2, Q5; §10.5 H3 2–3; FAQ dedicated PC; Sources |

#### 1.3 How SmartPSS / Lite adds and reaches devices
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| S5 | `SmartPSS add device port 37777 IP domain SN P2P` · WebSearch → Firecrawl scrape | https://dahuawiki.com/SmartPSS_Lite/SmartPSS_Lite_P2P_Setup | Prereq "Dahua device already initialized"; on device Network > P2P verify enabled and status "Online"; in Lite Home > Device Manager > + Add > Method to add "SN(For Device Support P2P)"; enter name, SN, user, password; verify green "Online". Modified 13 Feb 2024. | §Repair checks; §6; §9 Q4; §12 step 3; Sources |
| S6 | same · WebFetch | https://securitycamcenter.com/smart-pss-add-nvr-dvr-p2p/ | SN found on label, web UI Info > Version, or Main Menu > Settings > Network > P2P; guide "also applies to Dahua OEM brands, including Amcrest, Lorex, Honeywell, Speco". | §10 equipment; FAQ OEM brands; image caption (Honeywell recorder); Sources |
| S7 | `SmartPSS Lite user manual auto login auto start…` · Firecrawl search → scrape (PDF, query) | https://dahuawiki.com/images/a/a4/SmartPSSLite_User%27s_Manual_Eng.pdf | Manual V1.0.0, April 2022. Default install path C:\Program Files\SmartPSSLite. Add devices by "Automatically search", "Manually adding", "Import in batches"; "the port number is 37777 by default". Settings: "Auto Start — The platform is automatically started after the computer is turned on"; "Auto Login … will log in automatically the next time"; "Resume Last Preview … automatically open the last preview after restarting". Default record path \Data\User\Record; snapshots …/Data/User/Picture/Capture. Alarm linkage: alarm sound, "Send alarm email", "Configure linkage video", alarm I/O. Password rule: "8 to 32 non-blank characters and contain at least two types of characters". | §9 Q8–Q10; §12; FAQ paths/password; §Repair; Sources |
| S8 | `Using SmartPSS over internet` · Firecrawl scrape | https://ipcamtalk.com/threads/using-smartpss-over-internet.67886/ | Jan 2023: user's SmartPSS shows camera "offline" over the internet; replies: VPN to tunnel in; port-forwarding "though not advised"; "Check that SPSS is allowed outbound through the Windows Firewall"; port "defaults to 37777"; per-camera ports or "enable p2p and manually enter each cams serial number". | §9 Q4; §10 table; §10.5 H3 4; Sources |
| S9 | `SmartPSS export` · Firecrawl search → scrape | https://dahuawiki.com/SmartPSS/How_To_Export_Device_Record | Playback > choose device, Record Type, Stream Type (Main/Sub), Time > Search; Time Clip start/end; Export Setup: path; "Export Format … (ASF, AVI, MP4, or Original Format)"; "Export SmartPlayer Player: Check the box to include the playback software with the export". Modified 2 Oct 2024 (SmartPSS 2.0 article). | §9 Q11–Q12; §8.5; FAQ; §12 step 6; Sources |

#### 1.4 Connections, lockouts, Starlink
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| S10 | `Starlink CGNAT port forwarding not supported public IPv4 static IP option` · Firecrawl search | https://starlink.com/support/article/1192f3ef-2a17-31d9-261a-a59d215629f4 (excerpt) | "Starlink WiFi routers do not support port forwarding or firewall rules for IPv4 or IPv6." | §5 para 3; §9 Q4; §10 table; §10.5 H3 4; Sources |
| S11 | same | https://www.purevpn.com/blog/starlink-cgnat-port-forwarding/ (excerpt) | Public IPv4 option needs a third-party router; "Starlink does not currently offer static IP addresses". | §9 Q4 (background); Sources |
| S12 | `Dahua recorder account locked after failed login attempts…` · Firecrawl search | https://www.cctvforum.com/topic/40555-account-locked-5-failed-attempts/ (excerpt); https://ipcamtalk.com/threads/account-locked.996/ (excerpt); https://ipvm.com/discussions/dahua-password-change-problem (excerpt) | CCTV Forum: Dahua "locks an account after 3 failed login attempts in a short period of time, you just need to wait I think 30 minutes" (forum, hedged). IPCamTalk: "update your SmartPSS clients or they will hammer the account with wrong password and lock you out". IPVM: "SmartPSS reports the DVR to be offline because the account is locked". | §9 Q13; §Repair table; Sources |

#### 1.5 Reddit (excerpts only)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S-R1 | `reddit SmartPSS Dahua problem export playback slow` · Firecrawl search | https://www.reddit.com/r/Dahua/comments/1cdgymm/dahua_dhinvr44324ks21_the_cameras_keep_getting/ | Excerpt: "Your internet connection where the camera is head an upload speed that is too low to support the video bitrate you have selected. In SmartPSS, …" | §9 Q7; §10.5 H3 5 |
| S-R2 | same | https://www.reddit.com/r/Dahua/comments/1ptwgl7/smartpss_lite_download_failed_to_export/ | "SmartPSS lite download: Failed to export"; update: older SmartPSS "the download still fails". | §9 Q11 (export failures happen; export at the recorder as fallback) |
| S-R3 | same | https://www.reddit.com/r/cctv/comments/1l26s73/please_help_dahua_system_with_smart_pss_download/ | "I help my parents monitor their CCTV via Smart PSS. Sometimes I download from certain cameras and it works fine exported mp4. But with other …" | §5 para 4 (family member managing remotely — generic, not located) |
| S-R4 | same | https://www.reddit.com/r/Dahua/comments/1rconlx/dahua_nvr_dahua_cameras_playback_not_working/ | "DST issues cause synchronisation problems in DMSS & Smart PSS lite. Sometimes it just shows 'Loading'…" | FAQ DST |
| S-R5 | same | https://www.reddit.com/r/Dahua/comments/15njnaz/smartpss_crashing_on_windows_11/ | "my Windows 11 SmartPSS program crashes whenever I try to stream more than 1 camera simultaneously" | FAQ dedicated PC (as one user's report) |
| S-R6 | same | https://www.reddit.com/r/Dahua/comments/1ifsh6q/dmss_app_slow/ | "Try to load a camera through Smart PSS on a computer, connected via Ethernet" | §Repair checks (wired PC first) |

#### 1.6 Regulation and security (silo)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S13 | `FCC 2026 order prohibiting importation marketing previously authorized covered equipment Dahua Hikvision continued use` · Firecrawl search | https://docs.fcc.gov/public/attachments/DA-26-635A1.pdf (excerpt) | DA 26-635, released June 26 2026: prohibits continued importation and marketing of covered equipment added to the Covered List in 2024 or earlier; "will not affect the continued use or operation of already-purchased communications equipment"; for use-based Covered List entries "the prohibitions … will not apply to importation and marketing for non-'covered' uses". Effective 10 days after Federal Register publication (FR July 6 2026 → July 16 2026, per hik-connect research). | §5 para 5; §8.5; §9 Q3; §10.5 H3 7; Sources |
| S14 | carried: research/dahua-camera-installation.md | https://www.globalsecurity.org/intell/library/news/2022/intell-221125-fcc01.htm ; https://docs.fcc.gov/public/attachments/DA-26-48A1.pdf | Nov 25 2022: Hikvision and Dahua equipment barred from new authorization; Covered List includes Dahua; use-based coverage (public safety, government facilities, critical infrastructure, national security). | §8.5; §10.5 H3 7 |
| S15 | carried: research/dahua-camera-installation.md | https://cvefeed.io/vuln/detail/CVE-2021-33044 | Dahua identity authentication bypass during login; CVSS 9.8; added to CISA KEV Aug 21 2024. | §9 Q15; Sources |
| S16 | carried: research/dahua-camera-installation.md | https://www.dahuasecurity.com/aboutUs/trustedCenter/details/775 | DHCC-SA-202507-001 (July 23 2025): CVE-2025-31700/31701 in some IPC series; builds after April 16 2025 not affected. | §6 firmware card |

#### 1.7 Silo pricing (no invented prices) — FLAG
The 16 old SmartPSS template pages carried inconsistent chips ($250 service call, $175/drop, $200–$400, $400–$900, $700–$1,800, $2,500+, $0/mo) that match neither blueprint §9 nor the protected $195/hr rate; none carried. This page uses only: $0 phone/screenshot triage (silo convention from the rebuilt Hik-Connect page); protected service rate $195/hr, 3-hr minimum ($585), not multiplied; recorder replacement = DVR Upgrade silo base (4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+) × Ulster 1.53 → $689–$1,071; $995–$1,530; $1,224–$1,836; $1,836–$3,366; $3,366+ (identical to dvr-upgrade-ulster). FLAG for Anwar: confirm app-support silos borrow DVR replacement prices.

#### 1.8 Keyword plan (five layers)
- **Service:** Smart PSS support, SmartPSS setup, SmartPSS Lite setup, Dahua PC client setup, SmartPSS migration, DSS upgrade advice, SmartPSS export help.
- **Problem:** SmartPSS discontinued, max channel error, P2P live view stops after 10 minutes, device offline over Starlink, account locked, export fails, DST playback mismatch, PC restarts after outage, high CPU.
- **Technology:** SmartPSS Lite, DSS Pro/Express, P2P (SN), IP/domain port 37777, VPN, CGNAT, main/sub stream, bitrate, ASF/AVI/MP4/original + SmartPlayer, auto start/auto login/resume last preview, alarm email linkage, access control/attendance.
- **Industry:** second-home owners, farms/orchards/wineries, dispensaries, small shops and studios, campus office tenants, landlords of student rentals, contractors, municipal-adjacent small offices.
- **Geographic (this page):** Ulster County; Kingston (Uptown/Stockade, Midtown/Broadway, Rondout), Town of Ulster/Route 9W/iPark 87, New Paltz/Route 299/Main Street, Saugerties/Route 32/Exit 20, Woodstock/Route 212, Phoenicia/Shandaken/Route 28, Stone Ridge/Route 213, Ellenville/Route 209, Rosendale, Highland, Esopus.

---

### Part 2 — Question register (silo)

#### 2.1 Existing 15 sibling pages (old template, generated 2026-10-18 with the check_page.py parser)
Every one of bronx, brooklyn, dutchess-county, hudson-valley, long-island, manhattan, nassau-county, nyc, orange-county, putnam-county, queens, rockland-county, staten-island, suffolk-county, westchester-county (and the old ulster-county) carries the same nine intents:
1. What is Smart PSS used for?
2. How do I install Smart PSS?
3. How do I add cameras to Smart PSS?
4. Why is Smart PSS not connecting?
5. Which Smart PSS for Windows 11?
6. Where do I download Smart PSS safely?
7. Can Smart PSS do remote viewing?
8. Is there a Smart PSS for Mac?
9. Smart PSS still not cooperating? (banner heading)
The rebuilt Ulster page avoids all nine intents (it does describe P2P/IP adding and macOS availability in prose, never as a question).
Bronx (scheduled run) and Manhattan (sibling subagent) were being rebuilt concurrently; their new questions were not on disk when this page was written — coordinator to re-run the cross-page check.

#### 2.2 smart-pss-support-setup-ulster-county — REBUILT 2026-10-18 (final, after dedupe vs the concurrent Manhattan rebuild read at ~12:20)
**§9 Q&A (H3):**
1. We replaced a storm-damaged recorder and the old SmartPSS on the office PC won’t connect to the new one — why?
2. After moving to SmartPSS Lite, two recorders dropped off with a “max channel” message — why?
3. We have stores in Kingston, New Paltz and Saugerties — is Dahua’s paid DSS worth it over SmartPSS Lite?
4. Our barn recorder sits behind Starlink — why will SmartPSS reach it by serial number but not by address?
5. Live view over P2P cuts out after about ten minutes — is that the software or our connection?
6. Fiber is finally coming down our road — what should change in SmartPSS the day it’s connected?
7. How far can the stream settings drop before the picture is useless over a rural DSL line?
8. How long should a battery backup keep the modem, recorder and SmartPSS PC running through a Central Hudson outage?
9. Can SmartPSS Lite email us when something trips at an unattended camp or barn?
10. Can we watch the farm in SmartPSS from the Kingston office and the farmhouse PC at the same time?
11. The clip we need is on a camp recorder that sits on satellite internet — export it over the link, or drive up and pull it off the box?
12. The insurance adjuster can’t open the files we exported — what went wrong?
13. SmartPSS lists the recorder as offline and the recorder’s own screen says the account is locked — how did that happen?
14. A seasonal farmhand has left — how do we cut off their SmartPSS access without redoing everyone else’s?
15. Our recorder’s firmware dates from 2021 — does the Dahua login flaw CISA lists change how we should use SmartPSS?
16. Does changing only the software on a Stockade District storefront’s camera system involve Kingston’s preservation commission?
17. Our Route 28 dispensary already gives the state remote access — can the owner also watch through SmartPSS without getting in the way?
**§17 FAQ (= FAQPage, 9):**
1. Is a PC that already runs our point-of-sale or farm bookkeeping software powerful enough for SmartPSS Lite?
2. Do the Kingston police or the sheriff have a way to log in to our SmartPSS or recorder?
3. What password rules does SmartPSS Lite apply to its own login?
4. Can the cameras in SmartPSS be named by barn, field or building instead of by channel number?
5. Do Honeywell, Lorex, Amcrest or Speco recorders work in SmartPSS?
6. Why does a SmartPSS visit in Ulster County cost more than the same visit in the Bronx?
7. Can the clocks changing for daylight saving time throw off a playback search?
8. Is SmartPSS Lite still free, or has Dahua moved everything to a subscription?
9. How long does an Ulster SmartPSS visit usually take?
**De-dup notes:** replaced six first-draft items whose intent matched the rebuilt smart-pss-support-setup-manhattan page: "office PC still runs original SmartPSS — what breaks if we leave it" (= Manhattan "lobby workstation still runs the 2020 release — what changes if we leave it alone") → storm-replaced recorder won't pair with old SmartPSS; "when to outgrow Lite for DSS" (≈ Manhattan >64 cameras) → multi-town stores DSS value; "make the PC reopen after an outage" (= Manhattan "sign itself back in after a power cut") → battery runtime sizing; "should the PC store the footage" (= Manhattan "does Lite record on the PC" / "if the desk computer dies") → simultaneous remote viewers and upload; "which export setting for a trooper" (= Manhattan "detective asked … which format") → export over satellite vs drive-up USB export; "caretaker playback-only login" (= Manhattan "stop an overnight guard changing settings") → revoking one departed worker. FAQ: "where are snapshots saved" (≈ Manhattan disk/retention of client files) → police/sheriff login access; "door reader and time clock" (= Manhattan attendance module) → naming cameras by building. Bronx rebuild not on disk at build time.
**§10.5 claim H3s (not questions):** “SmartPSS and SmartPSS Lite are the same program”; “P2P is unlimited and free”; “Port forwarding 37777 is the standard fix”; “Starlink users just need a static IP”; “Lower the bitrate and the problem goes away”; “Export as original format to keep it forensic”; “Dahua is banned, so SmartPSS will stop working”.

---

### Part 3 — `## Ulster`

**Thesis (distinct from nvr-installation-ulster-county = water + regulated retention; dvr-upgrade-ulster = recorder guarding an empty house through outages; hikvision Ulster = covered-use buildings/absence; HV hub siblings = generic):** In Ulster County the SmartPSS screen and the recorders it watches are usually miles apart — an office in Kingston or a house in the city watching a barn in Shandaken, a camp in Denning, a shop on Route 28 — over an internet link that differs road by road (Archtop fiber and cable in the Kingston/Saugerties corridor, DSL and satellite in the hollows, Starlink behind CGNAT, cell dead zones on Routes 212/28) and is changing as the county's fiber build reaches the last ~1,293 unserved locations. So SmartPSS support here is choosing the connection method per link (P2P vs IP vs VPN), fitting streams to thin uplinks, keeping the viewing PC alive through Central Hudson outages, moving people off discontinued SmartPSS onto Lite (or DSS where Lite's limits bite), and getting clean exports to troopers, deputies, insurers and — for dispensaries — the state.

#### Ulster rows (new this run)
| ID | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| U1 | `Ulster County NY 20 towns 3 villages one city square miles county seat Kingston` · Firecrawl search → scrape (directQuote) | https://comptroller.ulstercountyny.gov/sizing-up-ulster/ | Aug 15 2016: "Ulster County has only 3 of the 81 villages and 20 of the 105 towns that comprise the Region, yet it is the geographically largest county (1,124 square miles) of the seven that define the area." | §5 para 1; §5.5; Sources |
| U2 | same · search | https://en.wikipedia.org/wiki/Ulster_County,_New_York (excerpt) | County seat and largest city Kingston. | §5.5 |
| U3 | `Archtop Fiber 2026 Ulster County expansion…` · Firecrawl search → scrape (query) | https://hudsonvalleyone.com/2026/04/30/archtop-fiber-gets-green-light-for-125-million-expansion/ | Apr 30 2026: NY PSC approved a $125 million investment plan for "Town of Ulster-based Archtop Fiber"; conditionally authorized restructuring to secure a $115 million five-year term loan through 2030. No homes-passed or town list on the page. | §5 para 3; §5.5; §9 Q6; Sources |
| U4 | same · search | https://archtopfiber.com/blog/2024/10/01/archtop-fiber-begins-construction-on-state-of-the-art-fiber-network-in-woodstock/ (excerpt) | Oct 2024: construction begun in Woodstock; "Woodstock is one of several communities in Ulster County with which Archtop Fiber has an MOU." | §9 Q6; §13 Woodstock card |

#### Carried Ulster rows (sources fetched by earlier runs; file named; not re-fetched unless noted)
| ID | From | URL | Finding | Used |
|---|---|---|---|---|
| C-U1 | research/dvr-upgrade.md U1 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36111 | 86,178 housing units; 6,545 seasonal/recreational/occasional (7.6%); 21,829 built 1939 or earlier (25.3%); median year built 1966. | §5 para 1; §5.5 |
| C-U2 | research/dvr-upgrade.md U2 | Census B25004 county subdivisions | Seasonal share: Hardenburgh 70%, Denning 55%, Shandaken 33%, Woodstock 19%; Kingston city 1%. | §5 para 1; §7 camp card |
| C-U3 | research/dvr-upgrade.md U5 / C14 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ ; dailyfreeman.com 2026-09-27 | Sept 26 2026 nor'easter: >19,000 Central Hudson homes/businesses being restored; "hardest-hit areas include Woodstock, Shawangunk, Plattekill and Hurley in Ulster County"; Ulster peak >14,000 outages; ~93,000 Ulster customers. | §5 para 4; §5.5; §9 Q8 |
| C-U4 | research/dvr-upgrade.md U9 | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion ; https://radiocatskill.org/ulster-county-secures-59m-for-fiber-broadband-expansion/ (excerpts) | Sept 25 2025: $20.8M ConnectALL award for "nearly 1,300 unserved households, businesses, and community facilities"; Radio Catskill May 4 2026: "all 1,293 unserved locations in the county will receive fiber broadband service"; MTC fiber in Phoenicia; USDA grant for fiber in Denning. | §5 para 3; §5.5; §9 Q6 |
| C-U5 | research/dvr-upgrade.md C15 | https://hudsonvalleyone.com/2016/12/29/dead-zones-more-than-a-decade-into-the-cell-phone-era-much-of-ulster-county-still-has-no-service/ | Cell dead zones along Routes 212 and 28; worst ZIPs incl. 12464 Phoenicia, 12477 Saugerties, 12458 West Hurley. | §5 para 3; §10 table (cellular backup) |
| C-U6 | research/dvr-upgrade.md U10 | https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf (excerpt) | 2,827 short-term rentals (3.28% of housing, May 2025); 36% of owners out-of-county mailing addresses. | §5 para 2 |
| C-U7 | research/dvr-upgrade.md U7 / nvr UH1 | https://hudsonvalleyone.com/2026/09/02/police-defend-kingstons-surveillance-cameras-as-residents-raise-privacy-concerns/ | Kingston: 7 LPRs + 71 other cameras since 2020, concentrated in Midtown and Uptown; KPD camera video overwritten every 14–21 days (nvr UH1). | §8 Uptown card; §9 Q11 context |
| C-U8 | research/nvr-installation.md UN1 | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 | Adult-use dispensary: recordings retained ≥60 days; remote access/login for immediate viewing by the Office; unaltered copy on request; failure notice within 5 minutes; 8 hours during outage. | §8 Route 28 card; §8.5 |
| C-U9 | research/nvr-installation.md UN3 | https://hudsonvalleyone.com/2024/11/24/ulster-county-marijuana-dispensary-holiday-gift-guide | 5 Ulster dispensaries: Route 28 Town of Ulster; North Chestnut St New Paltz; Plaza Rd Kingston; Route 32 Kingston; Route 213 Stone Ridge (town names only). | §8 cards |
| C-U10 | research/nvr-installation.md UN8 / dvr C9 | https://hudsonvalleyone.com/2024/05/13/ipark-87-progress-report ; ulstercountyny.gov 2026-02-27 | iPark 87: 200-plus-acre, million-square-foot former IBM campus; East Campus hosts Ulster BOCES and Archtop Fiber. | §7 campus card; §8; §13 |
| C-U11 | research/nvr-installation.md UN9 | https://en.wikipedia.org/wiki/Ellenville,_New_York | Ellenville village, Town of Wawarsing, pop. 4,167 (2020), NY 52/US 209; D&H Canal; Ulster Knife Co.; Nevele closed 2009. | §7 mill card; §8; §13 |
| C-U12 | research/dvr-upgrade.md C1 | https://kingston-ny.gov/hlpc | Districts Stockade, Rondout–West Strand, Chestnut St, Fair St; certificate of appropriateness for material change visible from street/alley; ordinary maintenance exempt. | §9 Q16; §8.5 |
| C-U13 | research/dvr-upgrade.md C20 | https://ecode360.com/35131702 | Ulster Ch. 185: electrical work includes wiring for signaling, communication, alarm or data transmission; master electrician licence for permits. | §8.5 (new outlet/UPS circuit by licensed electrician; no claim software work needs a licence) |
| C-U14 | research/dvr-upgrade.md C2/C3/C21/C23/C24 | FOHK/parks.ny.gov; huguenotstreet.org; opus40.org; walkway.org; dec.ny.gov | Senate House 1676 stone dwelling; Historic Huguenot Street 10-acre NHL district; Opus 40 bluestone; Walkway west end in Highland; Ashokan Reservoir 1915. | §7 stone card; §13 cards |
| C-U15 | research/dvr-upgrade.md U12 | https://www.thruway.ny.gov/travelers/interchange-exit-listing | Exit 18 New Paltz (NY 299); Exit 19 Kingston (NY 28); Exit 20 Saugerties–Woodstock (NY 32). | §8; §13 intro |
| C-U16 | research/dvr-upgrade.md C26 | USDA 2022 Census of Agriculture | Ulster 486 farms, average 150 acres. | §5.5; §7 farm card |
| C-U17 | research/nvr-installation.md UN10 | https://www.chronogram.com/food-drink/shawangunk-wine-trail-tells-the-regions-story-by-the-glass-23340721/ | Shawangunk Wine Trail, west side of the Hudson, Ulster and Orange. | §8 wineries card |
| C-U18 | research/dvr-upgrade.md C12 | newpaltz.edu | SUNY New Paltz 6,197 undergraduates, 1,036 graduate students. | §7 rental card; §13 |
| C-U19 | research/dvr-upgrade.md S7 / silo | homeadvisor.com; angi.com NY | HomeAdvisor $1,289 avg ($589–$2,040); Angi NY $797–$2,222 (install averages, not software support). | §10.5 (not used — kept for reference) |
| C-U21 | research/dvr-upgrade.md C27 / C10 / C11 / C16 | hullpg.com; goloveny.com; iloveny.com; archtopfiber.com 2024-10-01 | Hudson Valley Mall, Town of Ulster on Route 9W, in redevelopment; Uptown Kingston Wall St/North Front shops; New Paltz Main St (Route 299); Archtop launched Kingston and Saugerties, building Woodstock. | §8 cards; town-by-town table |
| C-U20 | silo G8–G10 (nvr research) | nysenate PEN 250.05; NYS Commercial Security Tax Credit | One-party consent eavesdropping; credit ≤50 employees up to $3,000/location. | §8.5 |

#### EMPTY (not accessible in build env / not found)
Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★. Reddit threads about SmartPSS from Ulster/Kingston subreddits: EMPTY (r/kingstonnewyork camera search returns Flock/Jenoptik threads only — carried dvr U4). Ulster-specific Starlink subscriber data: EMPTY. A dated Ulster SmartPSS job for Field Notes: EMPTY (Field Notes written as a method note). Text of Dahua's SmartPSS discontinuation notice image: EMPTY (image only). Ulster police guidance on preferred video export format: EMPTY (page says to ask the requesting officer). Google Drive "AESS Website Photos" has no Smart PSS subfolder; CompanyCam not connected.

#### House practices on the page without an external source (FLAG for Anwar)
Dedicated small PC for SmartPSS; UPS on PC + modem + recorder; BIOS "restore on AC power loss" setting; Windows auto sign-in for the viewing account; sub-stream for live view and main stream for export; recommending VPN over port-forwarding; one Windows user per role; "export MP4 plus original with SmartPlayer" as our default for police/insurer; offline-alarm email via a role mailbox; written hand-over sheet; "most visits fit inside the three-hour minimum"; two-hour windows seven days to 8 PM (silo convention); travel included in the 1.53 factor.

#### Images (11) — permanent image rule
Drive has no Smart PSS folder; CompanyCam not connected. All 11 copied/converted to `images/smart-pss-support-setup/` (WebP q80), viewed before naming; alt/title/caption describe only what is visible; none claimed as Ulster, a customer site or SmartPSS software.
| Output file | Source |
|---|---|
| smart-pss-support-setup-ulster-county-recorder-monitor-thirty-two-tile-grid-with-bitrate-table.webp | images/dahua-camera-installation/dahua-camera-installation-orange-county-recorder-monitor-camera-grid-and-cable-bundles.webp |
| …-black-bullet-camera-high-on-pale-blue-wall.webp | images/dahua-camera-installation/…-orange-county-black-bullet-camera-high-on-painted-wall.webp |
| …-small-ceiling-camera-near-exit-sign-in-drop-ceiling.webp | images/dahua-camera-installation/…-orange-county-ceiling-cameras-beside-exit-sign-and-on-grid.webp |
| …-white-turret-camera-in-corner-of-unfinished-room.webp | images/dahua-camera-installation/…-orange-county-turret-camera-in-storage-room-corner.webp |
| …-dahua-bullet-camera-with-warm-light-led-product-photo.webp | images/dahua-camera-installation/…-orange-county-bullet-camera-with-warm-light-leds-product-photo.webp |
| …-dahua-pan-tilt-camera-with-red-and-blue-lights-product-photo.webp | images/dahua-camera-installation/…-orange-county-pt-camera-with-red-and-blue-lights-product-photo.webp |
| …-dahua-white-ptz-dome-camera-product-photo.webp | images/dahua-camera-installation/…-orange-county-white-ptz-dome-camera-product-photo.webp |
| …-dahua-stainless-steel-camera-housing-product-photo.webp | images/dahua-camera-installation/…-orange-county-stainless-steel-housing-bullet-camera-product-photo.webp |
| …-recorder-playback-frame-of-brick-wall-and-paved-lot.webp | images/lorex-camera-installation/lorex-camera-installation-hudson-valley-recorder-playback-view-along-brick-wall-to-paved-lot.webp |
| …-camera-frame-of-storeroom-and-open-doorway.webp | images/dvr-upgrade/dvr-upgrade-putnam-grey-camera-tile-of-storeroom-and-open-doorway.webp |
| …-honeywell-35-series-recorder-with-front-usb-ports-product-photo.webp | images/dvr-upgrade/dvr-upgrade-ulster-dark-grey-recorder-with-two-front-usb-ports-product-photo.webp |
DAILY-LOG note: `images: 11 reused from images/dahua-camera-installation/ (8, orange-county), images/lorex-camera-installation/ (1), images/dvr-upgrade/ (2) (no real Smart PSS photos yet)`.
