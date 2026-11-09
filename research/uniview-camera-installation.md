# Research — Uniview Camera Installation silo

Created 2026-10-18 by the subagent rebuilding `uniview-camera-installation-manhattan` (queue line: `REBUILD | uniview-camera-installation-manhattan | Uniview Camera Installation | Manhattan | up /uniview-camera-installation-nyc | (929) 560-0737 | GBP Bronx`). `research/uniview-camera-installation.md` did not exist, so this file holds the full silo research (v2.3 §3, all 11 sources), the question register and the `## Manhattan` section. A parallel agent building `uniview-camera-installation-dutchess-county` writes its notes to a separate file that the main run merges — merge, don't duplicate.

Format (v2.3 §12.4): **exact query · platform · URL · finding · page+section used**. Tools actually used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, web and news sources), Firecrawl scrape (markdown / query mode / PDF parser), Firecrawl gov search (`firecrawl_gov_search`), Firecrawl Alexandria `census-gov` provider. Shell curl blocked. Reddit and Yelp pages are not scrapeable in this environment → Reddit rows are **search-result excerpts only**; Yelp = EMPTY. "Excerpt" means the finding was read only as a search snippet.

Manhattan page section labels used below: §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts), §Repair (same-day block + symptom table), §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ NVR table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every Uniview page)

### 1.1 Mandatory sources (v2.3 §3) — status

| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only — rows R1–R12 (r/uniview, r/homesecurity, r/videosurveillance, r/homelab, r/SecurityCamera, r/AskNYC, r/nyc). |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 states this on the page and works from claims that appear in ranking pages (rows C1–C6) and forum excerpts (R rows). |
| 6 | Area landmarks | Manhattan section M-L rows. |
| 7 | Area use cases / building stock | Manhattan section M-H, M-O rows. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only Firecrawl search backends; no Bing/DDG related-search or autocomplete surface. |
| 9 | Local news | M-N1–M-N5 (NBC New York, CBS New York, amNY via search; West Side Rag). |
| 10 | Hyperlocal | West Side Rag (M-N3, M-N4). Patch Manhattan / Bronx Times-style Manhattan camera items: none surfaced beyond these. |
| 11 | Yelp 1–3★ | `yelp security camera installation Manhattan review "never showed" OR "stopped working" OR "no response" camera installer` · Firecrawl search → only Yelp search-listing pages (e.g. https://www.yelp.com/search?find_desc=Cctv+Security+Camera+Installation&find_loc=Upper+West+Side%2C+Manhattan%2C+NY); no 1–3★ review text → **EMPTY (not accessible in build env)**. Not used. |

### 1.2 Federal / regulatory status of Uniview (primary sources only)

| # | Exact query · platform | URL | Finding | Used (Manhattan page) |
|---|---|---|---|---|
| F1 | `Uniview Zhejiang Uniview Technologies FCC Covered List` · Firecrawl search → Firecrawl scrape (query, direct quote) | https://www.federalregister.gov/documents/2024/12/11/2024-29136/additions-to-the-entity-list | BIS final rule published Dec 11, 2024 adds "Zhejiang Uniview Technologies Co., Ltd., a.k.a. … Uniview" (Hangzhou) to the Entity List because it "enables human rights violations, including high-technology surveillance targeted at the general population, Uyghurs, and members of other ethnic and religious minority groups." Licenses are required "to export, reexport or transfer (in-country) items subject to the EAR" to the entity; review policy "presumption of denial". The rule governs exports **to** Uniview; it says nothing about US purchase or use of Uniview products. | §5 para 4; §5.5; §8.5; §9 H3 "questionnaire" and "Entity List … firmware/warranty"; §10.5 H3 2; §Sources |
| F2 | `https://www.fcc.gov/supplychain/coveredlist` · Firecrawl scrape (markdown, full page read programmatically; scraped 2026-10-18; page notes "Updated October 16, 2026") | https://www.fcc.gov/supplychain/coveredlist | Text search of the full list: **0 mentions of "Uniview" or "UNV"**. Hikvision and Dahua entries (date of inclusion March 12, 2021) read "Video surveillance and telecommunications equipment produced by … to the extent it is used for the purpose of public safety, security of government facilities, physical security surveillance of critical infrastructure, and other national security purposes…". The page also carries 2025–2026 additions unrelated to Uniview (foreign UAS, routers, robotic devices, inverters) and an "Importation/Marketing Prohibitions on Previously-Authorized Covered Equipment" section. | §5.5; §8.5; §9 questionnaire H3; §10.5 H3 2; §Sources |
| F3 | `Uniview NDAA section 889 Hikvision Dahua Hytera Uniview not named` · Firecrawl search (excerpts) | https://arcdyn.com/ndaa-compliant-security-cameras-dealer-guide ; https://tec-tel.com/resources/ndaa-section-889-camera-compliance | Section 889 names Huawei, ZTE, Hytera, Hikvision and Dahua (plus subsidiaries/affiliates); dealer guides state Uniview is not named. (Secondary sources — the page words this as "Section 889 names five companies; Uniview is not one of them" and cites the statute list, not a compliance claim.) | §9 questionnaire H3; §10.5 H3 2 |
| F4 | same search (excerpt) → Firecrawl scrape (query) | https://systems-integrations.com/is-uniview-the-next-hikvision-and-dahua-why-betting-on-ndaa-loophole-hardware-is-like-playing-russian-roulette/ | Integrator blog (Oct 11, 2026) argues Uniview could be added to future restrictions; **links no primary sources**. Not used as fact; used only as evidence that the question is being asked. | §10.5 H3 2 (context, unattributed) |
| F5 | `Uniview FCC 2026 covered list proposal video surveillance` · Firecrawl search (past year) | (results: law-firm drone items, dealer pages) | No FCC document naming Uniview surfaced. Recorded as: no primary-source action against Uniview found beyond the Entity List. | §10.5 H3 2 |

### 1.3 Uniview (UNV) product and documentation facts

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| U1 | `Uniview NVR301-04LS3-P4 datasheet specifications PoE HDD` · Firecrawl search (full excerpt of PDF) | https://global.uniview.com/it/res/202307/07/20230707_1883693_UNV%E3%80%90Datasheet%E3%80%91NVR301-04LS3-P4%20V1.06-EN_973275_168459_0.pdf | NVR301-04LS3-P4: 4-ch IP input; Ultra 265/H.265/H.264; incoming 64 Mbps / outgoing 48 Mbps; **128 remote users**; protocols incl. P2P, RTSP, DDNS; HDMI to 4K; 1 SATA, **up to 6 TB per disk**; 4 PoE ports, **max 30 W single port, 54 W total**, IEEE 802.3at/af; 1 RJ45 10/100; 2× USB 2.0; VCA by camera (intrusion, cross line, enter/leave area, audio detection, UMD); face search, behavior search; alarms incl. Illegal Access, Disk Full; certification CE, FCC, UL. | §10 NVR table; §9 roof-run H3; §14; §15 starter card |
| U2 | `Uniview NVR301-08LS3-P8 datasheet 8 PoE max power` · Firecrawl search (excerpts) | https://unvuae.com/product/nvr301-08ls3-p8-nvr301-16ls3-p8/ ; https://customvideosecurity.com/uniview-unv-nvr301-08ls3-p8-… | NVR301-08LS3-P8: 8 PoE ports, max 30 W per port, **75 W total**, 802.3at/af (distributor copies of the datasheet). | §10 NVR table |
| U3 | `Uniview NVR302-16B-P16-IQ datasheet 2 SATA 16 PoE incoming bandwidth` · Firecrawl search (excerpts) | https://global.uniview.com/Products/Network_Video_Recorders/Easy_Series/2HDD/NVR302-16B-P16-IQ/ | NVR302-16B-P16-IQ: 2 HDDs, 16-ch, 16 PoE, 1U; incoming bandwidth 160 Mbps, outgoing 128 Mbps. | §10 NVR table; §15 premium context |
| U4 | `Uniview IPC3618LB-ADF28K-DL datasheet ColorHunter dual light 8MP` · Firecrawl search (excerpts) | https://global.uniview.com/us/Products/Network_Cameras/Eco_Camera/Dual_Light/IPC3618LB-ADF28K-DL/ | 8 MP, 1/2.7" CMOS, 3840×2160 @20 fps; **9:16 corridor mode**; built-in mic; dual light (IR + white light). | §10 cards; §17 FAQ corridor mode; §14 |
| U5 | `Uniview EC-T4F28DL turret 4MP dual light datasheet` · Firecrawl search (excerpts) | https://ellipsesecurity.com/wp-content/uploads/2026/04/EC-T4F28DL.pdf ; https://www.streakwave.com/uniview-ec-t4f28dl-4mp-dual-light-fixed-turret-28mm-built-in-mic | EC-T4F28DL: 4 MP, 1/3" CMOS, 2560×1440 @25 fps; smart dual light; built-in mic; up to 30 m (98.4 ft) IR and warm light. | §10 cards; §15 standard card |
| U6 | `Uniview EZStation EZView app EZCloud uniview.com` · Firecrawl search → scrape (markdown) | https://global.uniview.com/Products/Software/PC/EZStation/ | EZStation 3.0: unified management of IPCs, NVRs, decoders, access control; add devices by IP/domain/EZDDNS; cloud device management (add, edit, delete, **share**); live view up to 64 split, 3 auxiliary screens; playback 16-ch; recording download in **.ts, .mp4**; **user levels super administrator / administrator / operator, assignable permissions per IPC**; set retention period for operation/alarm log; E-Map; video wall. System requirements: Windows 7/8/10 (i5-7500, GT 1030, 8 GB) and Windows 11 configs (16 GB); Mac OS 12–15. Current builds listed: Windows EZStation-B1130.3.18.6, Mac B1113.3.18.1. | §6; §9 multi-building H3, doorman-rights H3, police-export H3; §10 |
| U7 | same search (excerpts) | https://apps.apple.com/us/app/ezview-unv/id979189794 ; https://www.uniview.com/AppStore/ | EZView UNV: "mobile surveillance app … access Uniview surveillance products through network and view live or recorded video, receive alarms". | §6; §9 |
| U8 | `Uniview EZCloud device already registered by another account unbind NVR how to` · Firecrawl search (excerpts) | https://www.uniview.com/res/202311/23/20231123_1892486_How%20to%20Troubleshoot%20When%20It%20Shows%20the%20Device%20Has%20Already%20Been%20Registered%20When%20I%20Try%20to%20Add%20It%20to%20EZView%20or%20EZCloud_974481_168459_0.pdf ; https://www.facebook.com/groups/lowvoltagenation/posts/4459142267708901/ | Uniview how-to: "You can unbind the device from the old account either from the device's web interface under Setup>Network>EZCloud or GUI of NVR under Menu > …". Installer forum (Low Voltage Nation, excerpt): "Defaulting the unit will not remove it from the cloud account." | §9 H3 "last installer's EZCloud account"; §Repair table |
| U9 | `EZView app share device permissions EZCloud share live view playback multiple users Uniview` · Firecrawl search (excerpts) | https://www.uniview.com/res/202504/30/20250430_1958226_How%20to%20Share%20and%20Cancel%20Sharing%20on%20EZCloud%20Website%20and%20EZView_976470_168459_0.pdf ; https://support.nellyssecurity.com/hc/en-us/articles/4404560062107-How-To-Share-Your-Device-Via-EZView-Mobile-App | Uniview PDF (Apr 30, 2025) on sharing and cancelling sharing; Nelly's: "Each Uniview device is limited to only be registered one single EZcloud account at one time"; share dialog takes user, **Expiration Date, Roles**. | §9 managing-agent H3; §17 FAQ time-limited sharing |
| U10 | `Uniview NVR default password 123456 admin activate device first login strong password` · Firecrawl search (excerpts) | https://www.uniview.com/res/202504/30/20250430_1958213_How%20to%20Retrieve%20a%20Uniview%20Camera's%20Password_974041_168459_0.pdf ; https://www.uniview.com/Support/Product_Password_Reset/ | Uniview PDF: "Solution 1: Please try the default password, and the username/password of most Uniview products is admin /123456." Uniview runs a "Secure Bulk Password Reset" request page. | §6 hardening card; §10.5 H3 4; §Repair table |
| U11 | `Uniview default ports HTTP 80 RTSP 554 service port 7070 NVR port forwarding` · Firecrawl search (excerpts) | https://www.scribd.com/document/743490634/Networking-Port-Forwarding-Uniview ; https://support.visiotechsecurity.com/hc/en-us/articles/360016233540-IP-address-and-port-of-Uniview-s-P2P-service ; https://www.reddit.com/r/uniview/comments/1rj3iha/playback_not_working_ezstation/ | Recorders: HTTP 80, RTSP 554, media 7070, SDK 6060, HTTPS 443, ONVIF 82 (dealer doc). Uniview P2P service uses TCP 80/443/1883/9083/82/84 and UDP 4000/4001/3478/3479 (Visiotech). Reddit reply: EZStation playback failing "likely due to a network issue. Check to see if the RTSP port 554 is getting blocked". | §9 office-network H3; §10.5 H3 4; §Repair table |
| U12 | `Uniview security advisory firmware vulnerability CVE NVR IPC 2025` · Firecrawl search → scrape (query) | https://www.uniview.com/About_Us/Security/Notice/ ; https://global.uniview.com/News/News/202509/1062055_169683_0.htm | Uniview security notices list: "Reflected Cross-Site Scripting (XSS) Vulnerability in Some Uniview NVR Products" (2024-06-14); "Access Control Vulnerability Exist in Certain Uniview IPC Products" (2023-09-11); Network Security Advisory (2023-07-17); Buffer Overflow (2021-12-22); NIS 2 white paper (2026-08-07). Uniview appointed a CVE Numbering Authority (Sept 2025 news). | §6 firmware card; §10.5 H3 4 |
| U13 | `RondoDox botnet Uniview vulnerability exploited NVR` · Firecrawl search → scrape Akamai (query) | https://www.akamai.com/blog/security-research/netkiller-condi-botnet-exploits-camera | CVE-2024-0778: OS command injection in Zhejiang Uniview ISC camera model 2500-S up to firmware 20210930; product "has reached its end-of-service stage"; Akamai SIRT saw exploitation attempts in its honeypots on Jan 24, 2024 (Mirai variant). | §10.5 H3 4; §Sources |
| U14 | same → scrape Trend Micro (query) | https://www.trendmicro.com/en_us/research/25/j/rondodox.html | RondoDox (Oct 9, 2025): no Uniview row found in the vendor table returned. A LinkedIn post (excerpt) claims Uniview is targeted — not confirmed by primary source → **not used**. | Not used |
| U15 | `Uniview Zhejiang …` search result → Firecrawl scrape (query) | https://global.uniview.com/us/About_Us/Legal_Notice/Notice/202602/1089683_612074_0.htm | Uniview USA notice, Feb 9, 2026: "In the case of UNIVIEW's products purchased from an unauthorized reseller, the warranty and other relative services including but not limited to software upgrade would be unavailable." | §9 Entity-List/warranty H3; §10.5 H3 6; §15 labor-only callout |
| U17 | `Uniview EZView app end of service 2027 replacement app announcement` · Firecrawl search (excerpts) | https://www.uniview.com/News/News/202403/988856_169683_0.htm ; https://www.reddit.com/r/uniview/comments/1r7yc1w/ezview_on_android_which_app/ | Uniview news (Mar 2024): "Uniview introduces new APPs: UNV-Link for end users and UNV-Link Pro for installers … These two apps will replace the EZView service, and it is expected that EZView will stop its service in 2027." Reddit (excerpt): "EZView is no longer there. UniEase will replace the UNV-Link and EZview apps in the near future." (UniEase claim unconfirmed → not used.) | §6 UNV-Link card; §6 finished-job para; §10.5 H3 3; §Sources |
| U16 | same search → Firecrawl scrape (NDAA page) | https://global.uniview.com/News/News/NDAA/ | Page title "NDAA"; content not machine-readable in build env (query returned nothing). Excerpt: "The Uniview compliance product list above will be regularly updated on Uniview's website." | §9 questionnaire H3 (advice: check model against Uniview's list) |

### 1.4 Reddit / forums (R) — excerpts

| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com uniview NVR EZView problem` · Firecrawl search | https://www.reddit.com/r/uniview/comments/1n1jdel/phone_apps/ | "When I tried to add the NVR by scanning in EZView, it simply says that it's already been registered." Also: Uniview "pulled the 'add device without sign up' option from UNV Link". | §9 EZCloud H3; §Repair table |
| R2 | same | https://www.reddit.com/r/uniview/comments/1litqlg/ezview_app_not_pushing_notification/ | EZView not pushing notifications on Android despite settings checked. | §Repair table |
| R3 | same | https://www.reddit.com/r/uniview/comments/1d1fjci/uniview_nvr_and_cams_without_using_uniview_cloud/ | Without the cloud, "The only functionality they'll be missing is the push notifications". | §10.5 H3 3 |
| R4 | same | https://www.reddit.com/r/homesecurity/comments/1fw0jj3/poe_system_good_user_interface_bad_help/ | "EZView app is the issue, motion notifications are slow, two way talk is hit and miss, playback is …" | §10.5 H3 3 |
| R5 | same | https://www.reddit.com/r/uniview/comments/1rj3iha/playback_not_working_ezstation/ | Playback in EZStation failing → check RTSP 554 blocked. | §9 office-network H3 |
| R6 | same | https://www.reddit.com/r/videosurveillance/comments/1ftkb6w/ezview_problems/ | "scan the barcode with Wi-Fi shut off on your phone". | §Repair table |
| R7 | same | https://www.reddit.com/r/uniview/comments/1hhsg3u/motion_detection_and_any_alert_or_alarm_not_firing/ | Older NVR: update firmware (via cloud) when alarms don't fire. | §17 FAQ boiler-room alert |
| R8 | same | https://www.reddit.com/r/uniview/comments/1ep1mz3/not_all_uniview_cameras_coming_online/ | Switches plugged into NVR PoE ports; only one camera per switch shows video. | §9 roof-run H3 (why we don't daisy-chain switches off NVR ports) |
| R9 | `site:reddit.com uniview cameras worth it vs hikvision dahua installer` · Firecrawl search | https://www.reddit.com/r/SecurityCamera/comments/1uw8xd5/is_uniview_a_good_system_to_sell_to_customers_for/ | "I find Uniview quite restrictive compared to Dahua for integration … The apps are 'okay'." | §10.5 H3 3 |
| R10 | same | https://www.reddit.com/r/homesecurity/comments/po8kd1/uniview_vs_hikvision/ | "they are not on the chopping block from being banned in the US" (2021 view). | §10.5 H3 2 (shown as dated opinion) |
| R11 | same | https://www.reddit.com/r/homelab/comments/1bksez5/is_uniview_safe/ | "Is Uniview safe? Are there any issues with IP cameras that are manufactured and owned by Chinese companies?" | §9 questionnaire H3 (the worry) |
| R12 | same | https://www.reddit.com/r/homesecurity/comments/1hmdsvb/should_i_go_for_dahua_hikvision_or_ubiquiti_for/ | "Uniview is a good brand, price points are equal to Hik … user interface is different". | Background |

### 1.5 Claims that rank for the topic (C) — feed §10.5 because the AI Overview is EMPTY

| # | Exact query · platform | URL | Claim | Used |
|---|---|---|---|---|
| C1 | `Angi security camera installation cost 2026 average per camera` · Firecrawl search (excerpt) | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | "In 2026, the national average cost for security camera installation is $1,289, Most homeowners pay between $590 and $2,040". | §10.5 H3 1 |
| C2 | same (excerpt) | https://www.security.org/security-cameras/cost/ | Installation "costs $100 to $300, depending on the complexity". | §10.5 H3 1 |
| C3 | `yelp security camera installation Manhattan …` · Firecrawl search (excerpt) | https://butterflymx.com/blog/security-camera-installation-nyc/ | "Security camera installation in NYC requires a licensed installer with the cost ranging from $80 to $200 per camera." | §10.5 H3 1 |
| C4 | `Uniview NDAA section 889 …` (excerpt) | https://www.ipsecuritydepot.com/best/uniview-alternatives-ndaa-compliant-cameras/ | "Is Uniview banned under the NDAA? No — Uniview is not named in NDAA Section 889 … But PRC-manufactured equipment generally fails …" | §10.5 H3 2 |
| C5 | `Uniview NDAA …` (excerpt) | https://tetherx.io/compare/free-vms | Claims "Hikvision / Dahua / Uniview hardware is NDAA Section 889 banned" — contradicts the statute's named list (F3). | §10.5 H3 2 (example of a wrong claim) |
| C6 | `Uniview NVR default password …` (excerpt) | https://www.xlrsecurity.com/tutorials/uniview/uniview-cameras-nvr-default-username-and-password/ | "The default login credentials for new Uniview devices are as follows: Username – admin Password – 123456". | §10.5 H3 4 |

### 1.6 State and city rules relevant to every NYC Uniview page (L)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | `New York General Business Law Article 6-D security or fire alarm installer license Department of State` · Firecrawl gov search | https://nysenate.gov/legislation/laws/GBS/69-M ; https://dos.ny.gov/security-or-fire-alarm-installer | GBL §69-m: no person shall engage in the business of installing, servicing or maintaining security or fire alarm systems unless licensed; owners installing on their own property with their own employees are outside the article. DOS: licence term two years. | §8.5; §Quick |
| L2 | `New York Penal Law 250.45 unlawful surveillance … Labor Law 203-c …` · Firecrawl gov search | https://nysenate.gov/legislation/laws/LAB/203-C ; https://nysenate.gov/legislation/laws/PEN/250.45 ; https://nysenate.gov/legislation/laws/gbs/395-b | Labor Law §203-c: no employer video recording of employees in a restroom, locker room or room designated for changing, unless by court order. Penal Law §250.45: unlawful surveillance (imaging device in bedroom, changing room, restroom, etc.). GBL §395-b: owner/manager may not knowingly permit a recording device to surreptitiously record fitting rooms/restrooms etc. | §8.5; §7.5 |
| L3 | (FirstService Residential, below) | https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops/ | Audio captured could be unlawful eavesdropping (the article cites "Section 250.05" — that section is in the **Penal Law**). | §8.5 (cited as Penal Law §250.05) |
| L4 | `NYC Administrative Code 22-1202 biometric identifier information commercial establishments sign customer entrances` · Firecrawl gov search | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-131285 ; https://nyc.gov/assets/dca/downloads/pdf/businesses/Biometric-Identifier-Information-Disclosure-Sign.pdf ; https://legistar.council.nyc.gov/LegislationDetail.aspx?GUID=070402C0-43F0-47AE-AA6E-DEF06CDF702A&ID=3704369 | §22-1202(a): commercial establishments that collect, retain, convert, store or share customers' biometric identifier information must post a clear and conspicuous sign near all customer entrances; (b) no selling/sharing for value. L.L. 2021/003, eff. 7/9/2021. §22-1203 private right of action; 30-day written notice and cure before suing over (a). DCWP publishes a sign template. | §8.5; §9 shop face-search H3 |
| L5 | same search (excerpts) | https://council.nyc.gov/shahana-hanif/2026/05/19/nyc-council-pushes-to-ban-stores-from-collecting-biometric-data ; https://assembly.state.ny.us/leg?Text=Y&bn=A1558&sh=printbill&term=2025 | May 2026 Council hearing on bills to curb stores' biometric collection (pending). State bill A1558-C (pending) would require retailer tracking/biometric signs but exempts cameras "solely intended for video surveillance to ensure the security of a store". | §9 shop face-search H3 (pending, labelled as such) |
| L6 | `New York City Tenant Data Privacy Act smart access system HPD data retention policy multiple dwelling` · Firecrawl gov search | https://nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page ; https://legistar.council.nyc.gov/LegislationDetail.aspx?GUID=82868853-7D34-466F-B2FD-0617D9CF75DC&ID=7862812 | HPD: Local Law 63 of 2021 — owners of multiple dwellings using smart access (key fobs, RFID, phone apps, **biometric identifiers**) for entry to class A multiple dwellings must give tenants a data retention and privacy policy, obtain express consent, collect only listed minimum data (incl. time and method of access). Int 0428-2026 (pending) would add Admin Code §26-3008 barring owners from installing or using biometric recognition technology that identifies tenants or guests. | §7.5; §8.5; §9 TDPA H3 |

---

## Part 2 — Keywords (five layers)

- **Service:** Uniview camera installation, UNV camera install, Uniview NVR installation, Uniview IP camera setup, EZView setup, EZStation setup, Uniview system upgrade, Uniview camera repair/service, Uniview PTZ install, Uniview LPR install, Uniview fisheye install.
- **Problem:** NVR "already registered" to another EZCloud account, EZView no push notifications, playback fails in EZStation, default admin/123456 password, camera offline after switch, recorder disk full, footage export won't play, board/agent lost admin password, Entity List / NDAA questionnaire, biometric signage, package theft from lobby.
- **Technology:** NVR301-04LS3-P4, NVR301-08LS3-P8, NVR301-16B-LP8-IQ, NVR302-16B-P16-IQ, NVR302-32B-IQ, EC-B4F28DL, EC-T4F28DL, IPC3618LB-ADF28K-DL, IPC6424SR-X25-VF (PTZ), IPC86CEB-AF18KC-I0 (fisheye), PKC2640@Z28-IR-P (LPR), XVR301-04G3, NSW2020-10T-POE-IN; Ultra 265 / H.265; PoE 802.3af/at; corridor mode 9:16; EZCloud; EZView; EZStation; RTSP 554; ONVIF.
- **Industry:** co-ops, condos, rental walk-ups and elevator buildings, managing agents, doorman/lobby staff, office tenants and landlords, retail and restaurants, garages, medical suites, showrooms.
- **Geographic (Manhattan page):** Manhattan; Upper West Side (Riverside Drive, Broadway, Amsterdam Ave in the 90s; Central Park West; West 72nd St; West 96th St; West 110th St); Greenwich Village; Midtown; Garment District; Flatiron/Ladies' Mile (Sixth Avenue); Hudson Yards; Lower Manhattan/Water Street; Upper East Side historic district; Harlem; Washington Heights.

---

## Part 3 — Pricing basis (no invented prices)

Source: the silo's published Manhattan calculator, `uniview-camera-installation-prices-manhattan.html` (pricing engine embedded in the page; run in Node against its own `PG` data, zone "Manhattan": line 238, jbox 34, setup 204, parking 150). Outputs used verbatim:

| Item | Manhattan installed price |
|---|---|
| 4 × EC-B4F28DL 4MP bullet + NVR301-04LS3-P4 + 4 TB + parking | **$2,826** (matches the page's "4 cameras from $2,826") |
| 4 × IPC3618LB-ADF28K-DL 8MP turret + NVR301-04LS3-P4 + 4 TB + parking | **$3,266** |
| 8 × EC-T4F28DL 4MP turret + NVR301-08LS3-P8 + 4 TB + parking | **$4,870** |
| 16 × EC-T4F28DL + NVR301-16B-LP8-IQ + NSW2020-10T-POE-IN switch + 2 × 4 TB + parking | **$9,386** (≈1 month recording: $10,073) |
| Single cameras installed | from $361 (UAC-B122-AF28M analog) / $481 (EC-T4F28DL IP); PTZ IPC6424SR-X25-VF $1,701; fisheye IPC86CEB-AF18KC-I0 $2,151; LPR PKC2640@Z28-IR-P $1,791 |
| Recorders with setup | XVR301-04G3 $383; NVR301-04LS3-P4 $523; NVR301-08LS3-P8 $643; NVR302-32B-IQ $903; NVR302-16B-P16-IQ $1,243 |
| Hidden in-wall wiring | $200 per camera (hollow drywall; plaster/brick checked on site) |
| Service visit | $195/hr, 3-hour minimum ($585) — v2.3 §9 protected rate |

**FLAG for Anwar:** the calculator's Manhattan zone carries `min_visit: 795`, while v2.3 §9 protects $195/hr with a 3-hour minimum ($585). The page uses $585 (protected) and does not publish $795. Also: the Manhattan prices page's FAQ mentions an extended "1, 2 or 3 years" warranty — the rebuilt Manhattan install page uses only the one-year parts-only terms sentence and avoids that wording.

---

## Question register — Uniview Camera Installation silo

### Questions on the existing pages (FAQ + Q&A + FAQPage schema, extracted 2026-10-18 by script from every `uniview-camera-installation-*.html` except Manhattan)

Shared by nearly all 15 area/hub pages (old template): Are you licensed and insured? · Can I add more cameras later? · Do you offer a warranty? / Is there a warranty? · Do you service Uniview systems you didn't install (in <area>)? · How do I get started? · How long does Uniview footage stay recorded? · Why is my Uniview camera offline or not recording? · Will it work without internet? / Will my Uniview system work without internet? · Where is the install? · How much does Uniview camera installation cost in <area>? / How much does it cost? · Is Uniview legal to install in <area>? · Ready for Uniview in/on your <area> property? · How many cameras does a <area> home/building need? · Can I install Uniview myself on my <area> home? · Can I view my <area> home from anywhere? / phone · Do Uniview cameras work in winter / snow / coast? · What areas of <area> do you cover?

Page-specific (abridged by intent): NYC — Are Uniview cameras good? · Can Uniview cameras record audio? · Do I need to notify people they're being recorded? · Do you integrate Uniview with access control or alarms? · How many Uniview cameras do I need? · I forgot my Uniview password — can it be reset? · Is Uniview banned in the US? · Is Uniview cheaper than other camera brands? · What are the best Uniview cameras for apartment buildings? · What internet speed do Uniview cameras need? · Which Uniview camera is best for a warehouse? · Why does my night footage look blurry or washed out? · Can you upgrade my old cameras to Uniview? · What resolution do you recommend? · Do you install Uniview in all five boroughs? · Why Choose Uniview Security Cameras? — Bronx — Can the building manager and owner both view the cameras? · Do I need to post that the building is recorded? · Can you handle a co-op or condo board approval? · Do you provide board documentation? · Which Uniview camera is best for an apartment lobby? · Is Uniview good value for a Bronx apartment building? · Do you cover apartment lobbies and vestibules? · Do you install for bodegas and restaurants? — Brooklyn — Do you follow Landmarks rules in (Brooklyn) historic districts? · Do you handle co-op and condo board approvals? · Can you install on a brownstone without damaging the brick? · Wired or wireless? · Which Uniview camera is best for a brownstone? · Is Uniview cheaper than the premium brands? · Do I need to post that my business is recorded? — Queens — Can multiple people view the cameras? · Which Uniview camera is best for a storefront? · Is Uniview a good value for a small business? · Can you handle a Forest Hills co-op's HOA requirements? · Do you provide co-op board documentation? · Do I need to post that my store is recorded? — suburban/HV pages — neighbor-privacy, estate/farm/winery/lakefront/seasonal-home coverage, long cable runs, historic-home discretion, siding mounting, West Point (Orange), "Is it worth it in such a safe county?" (Putnam). Prices pages (all 16) — How much does Uniview camera installation cost in <area>? · What is included in the installed price? · Can you hide the wires? · Is this an exact quote? · What warranty do I get? · I already bought Uniview cameras. Will you install them?

Full raw list (300 lines with page tags): regenerate with the script in the build notes; intents above are what the Manhattan page avoided.

### Manhattan page (new, 2026-10-18) — §9 Q&A (H3)

1. The last installer registered our recorder to his own EZCloud account — how does the building take it back?
2. When the managing agent changes, what has to be handed over so the new agent can run the Uniview system?
3. How do we let the doorman watch live video without letting him export or delete recordings?
4. Our board's camera policy says only named people may review footage — can the recorder show who played back or exported what?
5. A tenant's IT security questionnaire asks for the camera maker's federal status — what can truthfully go in the answer for Uniview?
6. Where should a Manhattan building buy its Uniview equipment so firmware updates and warranty stay available?
7. Our building has no telecom closet — where should the recorder live: super's office, basement or roof bulkhead?
8. Will a PoE switch in the cellar reach a camera on the roof of a twelve-story building, or does that run need fiber?
9. How do we place a camera in the package room so the recording actually identifies who walked out with a box?
10. A sidewalk shed is going up for facade work — what happens to the cameras on the front of the building?
11. Our storefront has a roll-down gate — where does the camera go so it still sees the entrance after the gate comes down?
12. Can a Midtown office suite's Uniview recorder sit on the landlord's building network, or do we need our own line?
13. Our management company runs several buildings — can one screen in the office show all of them through EZStation?
14. If the co-op adds face-recognition entry, does the Tenant Data Privacy Act apply to the camera system too?
15. Does turning on face search in a Uniview recorder put a Manhattan shop under the city's biometric sign rule?
16. Police asked for a clip from the lobby — how do we export it from a Uniview recorder so it plays on their computer?

### Manhattan page (new) — §17 FAQ (= FAQPage schema)

1. Can the super get an alert only when someone enters the boiler room after hours?
2. Can a Uniview camera read plates at a garage ramp on a narrow Manhattan side street?
3. Can a contractor or tenant be given camera access for a set number of days and then cut off?
4. Does the lobby have to close while the cameras go in?
5. Can a camera go inside the elevator cab?
6. Can residents watch a lobby camera on a TV by the mailboxes?
7. Who owns the cameras and the footage if the building is sold or converts to a co-op or condo?
8. What is corridor mode, and when is it worth using in a Manhattan hallway?
9. Can the recorder email the managing agent when a hard drive fails or fills up?
10. How do we stop someone from simply unplugging the recorder or covering a camera?

**De-dup note (vs the parallel Dutchess rebuild, read from its in-progress HTML at 14:14):** Manhattan's earlier FAQ drafts on power-outage/generator behaviour and on a camera/cable map overlapped Dutchess questions ("How long can a Uniview recorder … keep recording on a battery…", "Our standby generator takes about ten seconds…", "Do you hand over a map of where every camera and cable runs?") and were replaced; the Entity-List H3 was reframed to the purchasing channel so it does not overlap Dutchess's "If Washington tightens the rules on Uniview later…". EZView's 2027 retirement is covered only in Manhattan body text (Dutchess asks it as a question). Masked block similarity vs every uniview-camera-installation-* page (incl. prices pages and the in-progress Dutchess file) max 0.576, excluding the mandatory warranty sentence (1.0 on the rebuilt Dutchess page, excluded by v2.3 §2).

---

## Manhattan

Thesis: **in Manhattan the camera is the easy part — a Uniview system works for years only when it is designed around who controls the building (board, managing agent, landlord's IT, Landmarks, freight elevator) and who holds the EZCloud account, the admin password and the federal paper trail.**

### M-H Building stock (Census)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-H1 | Alexandria `census-gov` `census/data` · dataset acs/acs5, vintage 2023, variables B25024_001E, _007E, _008E, _009E, B25035_001E, B25003_001E, _003E, B25034_010E, _011E, geography county:061 in state:36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36061 | New York County: **918,806** housing units; **99,713** in 10–19-unit buildings; **201,967** in 20–49-unit; **522,823** in 50+-unit; median year built **1951**; **392,000** units built 1939 or earlier; 59,700 built 1940–49; **775,376** occupied, **583,733** renter-occupied. | §5 para 1; §5.5; §7; §Sources |

### M-O Office stock

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-O1 | Firecrawl scrape (query, direct quote) | https://comptroller.nyc.gov/reports/spotlight-new-york-citys-office-market/ | NYC Comptroller Spotlight (May 2024, CoStar data): NYC ~728.6M sq ft office; **Manhattan 594,309,799**; Manhattan Class A 361,054,636; **Class B 172,960,516; Class C 59,340,112**. | §5.5; §8; §9 office-suite H3 |

### M-L Landmarks / corridors / LPC

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-L1 | `Landmarks Preservation Commission rule security cameras "security cameras" 63 RCNY 2-20` · Firecrawl gov search (full excerpt) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-113325 | 63 RCNY §2-20 (Health, Safety and Utility Equipment) para (4) Security cameras: "as small and as limited in number as feasible, with no more than two (2) security cameras for every twenty-five (25) feet of street frontage for small residential or commercial buildings of six (6) stories or less and with a street frontage of forty (40) feet or less, and no more than three (3) security cameras for every twenty-five (25) feet of street frontage for larger commercial, residential and institutional buildings … located to avoid a cluttered or haphazard appearance … minimizes their visible impact." | §7.5; §8.5; §13; §9 sidewalk-shed H3 (context) |
| M-L2 | `Landmarks Preservation Commission rules security cameras installation landmark building staff permit` · Firecrawl search → scrape (PDF, query) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | LPC Permit Guidebook (2025 edition), chapter "Health, Safety, and Utility Equipment" includes "Installing Security Cameras"; staff can issue permits for work meeting the Rules. | §8.5 |
| M-L3 | same gov search | https://nyc.gov/assets/dcas/downloads/pdf/cityrecord/2025/cityrecord-11-06-25.pdf | City Record Nov 6, 2025 LPC hearing notice lists Manhattan items incl. an application "to install security cameras" (alongside 15 Bank Street – Greenwich Village HD, 131 West 55th Street, 616 Avenue of the Americas – Ladies' Mile HD). Building for the camera item not identifiable in the excerpt → page says only that camera applications appear on LPC agendas. | §8.5 |
| M-L4 | `NYC Landmarks Preservation Commission number of protected buildings historic districts Manhattan statistics` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/New_York_City_Landmarks_Preservation_Commission | As of May 1, 2024: more than 37,900 landmark properties citywide, most in 150 historic districts. | §5.5 |
| M-L5 | (West Side Rag rows below) | — | Upper West Side corridors: Riverside Drive, Broadway, Amsterdam Ave in the 90s; Central Park West in the 60s; West 72nd St; West 96th St; West 110th St; West 66th St & West End Ave; West 60th St. | §13 |

### M-N News / hyperlocal / Reddit (local)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-N1 | `Manhattan building lobby surveillance video NYPD suspect 2026 package theft apartment` · Firecrawl search (news, excerpt) | https://www.nbcnewyork.com/news/local/impostor-fresh-direct-deliveryman-stolen-packages-upper-west-side-nyc-apartment-lobbies-nypd/1571533/ | Mar 15, 2018: man in a Fresh Direct coat posing as a deliveryman took packages from lobbies of at least three Upper West Side apartment buildings; NYPD released surveillance video. | §5 para 3; §9 package-room H3 |
| M-N2 | same (excerpt) | https://www.cbsnews.com/newyork/news/wedding-dress-stolen-from-lobby-of-greenwich-village-building/ | Feb 16, 2021: surveillance video shows a suspect peer into a Greenwich Village building and enter the lobby through an unlocked door; wedding dress taken. | §5 para 3; §13 |
| M-N3 | `West Side Rag security cameras building Upper West Side` · Firecrawl search → scrape (query) | https://www.westsiderag.com/2024/04/23/18-new-nypd-security-cameras-installed-on-uws-thanks-to-participatory-budgeting-heres-where | 18 NYPD cameras (nine boxes, two cameras each) installed and activated on the UWS at the end of January 2024; $320,000 capital funding through Gale Brewer's office (participatory budgeting); general areas: Riverside Drive, Broadway and Amsterdam in the 90s, Central Park, Central Park West in the 60s. | §5 para 2; §13 |
| M-N4 | same → scrape (query) | https://www.westsiderag.com/2026/08/13/an-upper-west-side-flock-camera-map-misunderstanding | Aug 13, 2026 (upd. Sept 4): no Flock Safety cameras in NYC; ALPR cameras on the UWS are operated by NYPD, DOT and MTA, e.g. W 66th St & West End Ave, W 72nd & CPW, W 72nd & Amsterdam, W 96th & Amsterdam, W 96th & West End, W 110th & Amsterdam; eight ALPR cameras on W 60th St for congestion pricing. | §5 para 2; §17 FAQ LPR (contrast: public ALPR vs private garage LPR); §13 |
| M-N5 | `Brick Underground security cameras co-op board approval …` · Firecrawl search → scrape (query) | https://www.brickunderground.com/blog/2014/06/ask_an_expert_security_camera | Most buildings limit viewing to security firm, property manager and super; attorneys advise boards not to view most footage or share with residents; footage generally not distributed "without a subpoena or court order"; lobby/entrance cameras "super common", hallways less so; Mark Levine (EBMG), Dean Roberts (Norris McLaughlin). | §7.5; §9 board-policy H3; §9 police-export H3 |
| M-N6 | same search → scrape (query) | https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops/ | FirstService Residential (Sept 23, 2024): footage "generally stored for 30 to 90 days"; requests via property manager with reason/timeframe/cameras; manager or security provider "should maintain a log of requests and a list of anyone who accessed footage"; board approval required before video doorbells outside an apartment; audio disabled; hallway cameras must not show inside units. | §7.5; §9 board-policy H3; §8.5 |
| M-R1 | `site:reddit.com NYC co-op board camera hallway apartment door install allowed Manhattan` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ | "For NYC common area video, only thing not allowed is if camera can film into someone's apartment." | §7.5 |
| M-R2 | same | https://www.reddit.com/r/nyc/comments/119k0as/can_my_neighbor_point_a_video_doorbell_at_my/ | "Your neighbor does not have the right to place anything in the hallway, including a door camera, without the landlord's consent." | §7.5 |

### Manhattan sources EMPTY
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG — EMPTY (not accessible in build env).
- Yelp 1–3★ (Manhattan) — EMPTY (only listing pages).
- Patch Manhattan Uniview-specific items — EMPTY (none surfaced).
- Field Notes: no real AESS Manhattan Uniview anecdote supplied → written as a method note, no story.
- Sidewalk-shed counts / DOB data — not researched in this run; the sidewalk-shed H3 makes no numeric claim.

### Images (Manhattan page)
images: 11 reused (no real Uniview job photos yet) — 9 real AESS job photos from images/apartment-building-security-camera-installation/, images/intercom-repair/, images/commercial-security-camera-installation/, images/nvr-installation/, and 2 genuine Uniview manufacturer product shots (images/uniview-*.jpg). Chosen to avoid the source photos the Dutchess build used.

| # | File (images/uniview-camera-installation/) | Source |
|---|---|---|
| 1 | uniview-camera-installation-manhattan-turret-on-drop-ceiling-above-glass-window-wall.webp | apartment-building-security-camera-installation/…-manhattan-dome-camera-on-ceiling-over-glass-entrance.webp |
| 2 | uniview-camera-installation-manhattan-bullet-camera-on-ceiling-grid-aimed-down-corridor-to-grey-door.webp | apartment-building-security-camera-installation/…-manhattan-bullet-camera-on-ceiling-grid-in-back-corridor.webp |
| 3 | uniview-camera-installation-manhattan-dome-camera-on-steel-arm-under-greek-key-stone-band.webp | intercom-repair/intercom-repair-staten-island-stone-apartment-facade-with-camera-on-steel-arm.webp |
| 4 | uniview-camera-installation-manhattan-white-dome-under-yellow-fascia-beside-painted-mural.webp | commercial-security-camera-installation/…-dutchess-county-white-dome-camera-under-storefront-fascia.webp |
| 5 | uniview-camera-installation-manhattan-black-mini-camera-on-drop-ceiling-above-showroom-soffit.webp | commercial-security-camera-installation/…-dutchess-county-mini-camera-on-showroom-drop-ceiling.webp |
| 6 | uniview-camera-installation-manhattan-two-small-cameras-on-tall-white-wall-under-mezzanine-windows.webp | apartment-building-security-camera-installation/…-westchester-county-two-small-cameras-on-tall-white-wall-below-mezzanine-windows.webp |
| 7 | uniview-camera-installation-manhattan-purple-patch-cable-bundle-down-equipment-rack.webp | nvr-installation/nvr-installation-staten-island-patch-cable-bundles-down-equipment-rack.webp |
| 8 | uniview-camera-installation-manhattan-small-dome-beside-lay-in-light-fixture-and-track-light.webp | nvr-installation/nvr-installation-staten-island-dome-camera-beside-track-lights-on-drop-ceiling.webp |
| 9 | uniview-camera-installation-manhattan-black-mini-camera-near-lit-exit-sign-on-tiled-ceiling.webp | apartment-building-security-camera-installation/…-long-island-camera-beside-exit-sign-and-dome-on-tiled-ceiling.webp |
| 10 | uniview-camera-installation-manhattan-unv-white-fisheye-dome-product-photo.webp | images/uniview-fisheye-360-panoramic-camera-white.jpg |
| 11 | uniview-camera-installation-manhattan-unv-black-vandal-mini-dome-product-photo.webp | images/uniview-vandal-dome-camera-black.jpg |

---

# Merged from parallel Dutchess build (batch 2026-10-18T13:53Z)

# Uniview Camera Installation — Dutchess part (for merge into research/uniview-camera-installation.md)

Created 2026-10-18 by the subagent rebuilding `uniview-camera-installation-dutchess-county` (queue line: `REBUILD | uniview-camera-installation-dutchess-county | Uniview Camera Installation | Dutchess | up /uniview-camera-installation-hudson-valley | (845) 640-3835 | GBP Bronx`). The Manhattan agent created `research/uniview-camera-installation.md` in parallel; this file was NOT merged into it. Merge, don't duplicate: silo rows below that repeat the Manhattan file's F/U rows are marked "(dup of Manhattan F#/U#)".

Format (v2.3 §12.4): **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, web + news), Firecrawl scrape (markdown / query mode / PDF parser), Firecrawl gov search. Shell curl blocked. Reddit and Yelp pages are not scrapeable in this environment ("we do not support this site") → Reddit rows are search excerpts only; Yelp review text EMPTY. "Excerpt" = read only as a search snippet.

Dutchess page section labels: §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts), §Repair, §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ phone-route table, ADT/Ring/SimpliSafe), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing (+ worked example), §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-level findings gathered by the Dutchess agent

### 1.1 Mandatory sources (v2.3 §3) — status for this page

| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows D-R1–D-R4). Thread pages: EMPTY (not accessible in build env — Firecrawl refuses reddit.com). |
| 2 | Google PAA | EMPTY (not accessible in build env). |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 works from claims in ranking cost pages (C1–C2) and common forum advice, not from a captured AI Overview. |
| 6 | Area landmarks | Dutchess rows D-L1–D-L7. |
| 7 | Area use cases / building stock | D-A1, D-P1, building-type cards (§7) drawn from farm census + town/college facts. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — no Bing/DDG related/autocomplete surface; only Firecrawl search backends. |
| 9 | Local news | D-N1–D-N7 (Spectrum News, Daily Freeman, Times Union, News10, Dutchess County press releases). |
| 10 | Hyperlocal | New Pine Plains Herald (D-N4), Miscellany News (Vassar, D-N6), Millerton News (D-N7, excerpt). |
| 11 | Yelp 1–3★ | `security camera installation Poughkeepsie yelp reviews` · Firecrawl search → https://m.yelp.com/biz/vector-security-poughkeepsie (snippet: "Rating 2.3(13)") ; review text: scrape refused → **EMPTY (not accessible in build env)**. Not used on page. |

### 1.2 US regulatory status of Uniview (primary sources)

| # | Exact query · platform | URL | Finding | Used (Dutchess page) |
|---|---|---|---|---|
| D-F1 | `FCC Covered List Uniview Zhejiang Uniview Technologies added` · Firecrawl search → scrape (query) | https://www.federalregister.gov/documents/2024/12/11/2024-29136/additions-to-the-entity-list | Effective Dec 11, 2024 BIS adds Zhejiang Uniview Technologies (a.k.a. Uniview) to the Entity List; reason "enables human rights violations, including high-technology surveillance…"; license required for all items subject to the EAR; presumption of denial. Rule says nothing about US purchase/use. (dup of Manhattan F1) | §9 "If Washington tightens the rules…" H3; §10.5 H3 4; §Sources |
| D-F2 | `https://www.fcc.gov/supplychain/coveredlist` · Firecrawl scrape (markdown, maxAge 0; text searched programmatically) | https://www.fcc.gov/supplychain/coveredlist | List dated "(October 16, 2026)". 0 occurrences of "Uniview". Hikvision, Dahua (with Huawei, ZTE, Hytera) listed since March 12, 2021. Page has section "Importation/Marketing Prohibitions on Previously-Authorized Covered Equipment" (updated Oct 13, 2026). (dup of Manhattan F2) | §9 future-rules H3; §10.5 H3 4; §Sources |
| D-F3 | `Uniview NDAA section 889 compliant Hikvision Dahua not listed` · Firecrawl search (excerpts) | https://arcdyn.com/ndaa-compliant-security-cameras-dealer-guide ; https://www.ipsecuritydepot.com/best/uniview-alternatives-ndaa-compliant-cameras/ | Section 889 names Hikvision, Dahua, Huawei, ZTE, Hytera; Uniview not named (dealer pages, secondary). (dup of Manhattan F3) | §10.5 H3 4 |
| D-F4 | same search (excerpt) | https://ipvm.com/reports/cecc-ipvm-2023 | "Uniview is not subject to the FCC/NDAA bans or sanctions despite raising similar human rights and security concerns as Dahua and Hikvision." (2023, excerpt) | §Sources (context) |

### 1.3 Uniview / UNV product and doc facts

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-U1 | `Uniview NVR301-04LS3-P4 datasheet PoE ports budget` · Firecrawl search → scrape (PDF parser, direct quote) | https://global.uniview.com/it/res/202307/07/20230707_1883693_UNV%E3%80%90Datasheet%E3%80%91NVR301-04LS3-P4%20V1.06-EN_973275_168459_0.pdf | 4-ch; incoming 64 Mbps; up to 4K; "up to 6TB for each disk"; SIP/UMD by camera total 4-ch; PoE "Max 30W for single port Max 54W in total", IEEE 802.3at/af; 48V DC; working environment −10 °C to +55 °C (+14 °F to +131 °F). (overlaps Manhattan U1) | §10 NVR card; §9 unheated-barn H3; §Sources |
| D-U2 | `Uniview NSW2020-10T-POE-IN extend mode 250m datasheet` · Firecrawl search (excerpts) | https://global.uniview.com/us/Products/Transmission/Switches/Access_Switches/NSW2020-10T-POE-IN/ | "Up to 250m transmission distance on Extend mode"; max PoE capacity 88W. | §9 barn-link H3; §10 switch card |
| D-U3 | `Uniview SMB farms solution cameras livestock barn` · Firecrawl search → scrape (markdown) | https://www.uniview.com/Solutions/SMB_Farms/ | Farm challenges listed (unstable power/network, large areas, false alarms from weather/animals). Smart management box supports up to 5 IP cameras, NVR, IP speaker, 4G router, solar, alarm light. Wise-ISP "5th-Gen nightview… Only a small amount of light is needed… without light pollution that could disturb animals." Tri-Guard = SIP + ColorHunter + Active Deterrence. SIP/UMD "reduces false alarms caused by leaves, birds, and lights". SeekFree "AI-powered video search… on NVRs". Related products: WLN-EB5E-IN "Outdoor 3KM Long-Distance Wireless Bridge"; SLR-B320P60 solar; IPC2A14LP-ADF40KC-4G-E 4G camera. | §9 barn-link, foaling, deer, SeekFree H3s; §10 table (4G/solar); §10.5 H3 6; §Sources |
| D-U4 | `Uniview EZView vs EZStation difference Uniview Wizard` · Firecrawl search → scrape (markdown) | https://www.uniview.com/News/News/202403/988856_169683_0.htm | Mar 11, 2024: Uniview launches UNV-Link (end users) and UNV-Link Pro (installers); "These two apps will replace the EZView service, and it is expected that EZView will stop its service in 2027… they can log in with the same account." | §9 EZView-2027 H3; §6; §Hero sub-line; §Sources |
| D-U5 | same search (excerpt) | https://global.uniview.com/Products/Software/PC/EZStation/ | EZStation 3.0: add by IP/domain/EZDDNS; cloud device management; user levels super admin/admin/operator; Windows and macOS 12–15. (dup of Manhattan U6) | §Sources |
| D-U6 | `Uniview security advisory vulnerability NVR firmware CVE` · Firecrawl search → scrape | https://www.uniview.com/About_Us/Security/Notice/ ; https://global.uniview.com/News/News/202509/1062055_169683_0.htm | Notices: NVR reflected XSS (2024-06-14); IPC access control (2023-09-11, CVE-2023-0773); NIS 2 white paper (2026-08-07). Uniview appointed CVE Numbering Authority (Sept 2025). (dup of Manhattan U12) | §Sources (firmware-current advice in §10.5 H3 3/4) |
| D-U7 | `Uniview ANR automatic network replenishment micro SD edge storage NVR camera` · Firecrawl search (excerpts) | https://www.uniview.com/us/Products/Intelligent_Traffic/Smart_Parking_Products/Access_ANPR_Camera/PKC2640_Z28(-IR)-P/ ; https://support.visiotechsecurity.com/hc/en-us/articles/360014467680-How-to-activate-the-ANR-function-on-Uniview-recorders | PKC2640: "Supports Micro SD cards of up to 256GB. Automatic network replenishment (ANR) allows to automatically store video to SD card in case of network disconnection." Visiotech: UNV cameras store to SD when disconnected; recorder retrieves on reconnection. | §9 "If the link to the barn drops…" H3 |
| D-U8 | `Uniview EZView app EZCloud P2P add device remote view` · Firecrawl search (excerpts) | https://www.megateh.eu/products/uniview-manual/how-to-set-up-remote-access-to-a-uniview-nvr-with-ezview ; https://ipvm.com/discussions/uniview-can-not-live-view-remotely | Add device by scanning QR from NVR's EZCloud page or entering SN; IPVM thread: port mapping as the alternative to cloud. | §10 phone-route table; §10.5 H3 3 |
| D-U9 | Published Dutchess price engine · local file | /uniview-camera-installation-prices-dutchess-county (`var PG` JSON, zone "Dutchess / Ulster": line 267, jbox 35, setup 212, min_visit 825; CONCEAL 200; drive 228.99) | Installed prices used: EC-B4F28DL / EC-T4F28DL $511; IPC2128LB-ADF28K-DL $621; IPC3638SS-ADF28KMC-I1 $1,031; IPC6324LWH-AX5C-VG2 $1,111; PKC2640@Z28-IR-P $1,821; TIC thermal from $2,081; NVR301-04LS3-P4 $531; NVR301-08LS3-P8 $651; XVR301-04G3 $391; switches from $119; 4TB drive $229; packages computed with the page's own quote logic: 4-cam $2,804, 8-cam house+barn $5,417, estate+gate $10,227. Service rate $195/hr, 3-hr min ($585) per v2.3 §9. | §10 cards; §14 table + worked example; §15 packages + labor-only; schema OfferCatalog |

### 1.4 Cost claims (for §10.5)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C1 | `Angi security camera installation cost average 2026` · Firecrawl search (excerpt, domain-limited) | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | "In 2026, the national average cost for security camera installation is $1,289, based on 4,027 verified projects"; range shown $110–$3,500. Second Angi page: "$592 to $2,040… average around $1,295". | §10.5 H3 1 |
| C2 | `uniview camera installation cost per camera` · Firecrawl search (excerpt) | https://wasserstein-home.com/blogs/smart-home/security-camera-installation-cost-all-you-need-to-know-in-2025 | "Professional installation costs $50–$150 per hour or $80–$200 per camera". | §10.5 H3 1 (quoted claim) |

### 1.5 Keywords — five layers (as placed on the Dutchess page)

- **Service:** Uniview camera installation (title, H1, H2s), UNV NVR installation, Uniview PoE camera installation, labor-only Uniview install (§15.5).
- **Problem:** barn camera dark, recorder beeping / drive error, cameras offline after outage, can't view from away on Starlink, deer false alerts, link to barn drops (§Repair, §9).
- **Technology:** NVR301-04LS3-P4, NVR301-08LS3-P8, PoE extend mode 250 m, wireless bridge, outdoor fiber, ColorHunter, Tri-Guard, Wise-ISP, SIP/UMD, SeekFree, ANR, UNV-Link, EZView, EZStation, CGNAT (§9, §10, §14).
- **Industry/property:** horse farm, foaling stall, farm stand, agritourism, river estate, student rental, Main Street shop (§6–§8, §9).
- **Geographic:** Dutchess County, Poughkeepsie, Beacon, Rhinebeck, Hyde Park, Millbrook, Pine Plains, Amenia, Millerton, Red Hook, Wappingers Falls, Fishkill, Pleasant Valley (hero, §5, §8, §13, schema areaServed).

---

## Question register — dutchess

Page: `uniview-camera-installation-dutchess-county` (rebuilt 2026-10-18). Checked against every question on all other `uniview-camera-installation-*` pages (old template, 177 masked questions) and against the Manhattan agent's new Q&A list in `research/uniview-camera-installation.md` (two of my drafts overlapped Manhattan #6 Entity-List/firmware and #16 police export — both replaced before PASS).

### §9 Q&A (H3)
1. Is a wireless bridge or a trench the better way to bring barn cameras 600 feet back to the house?
2. Will a wireless bridge across the pasture still hold its signal once the trees leaf out in May?
3. Can lightning that strikes near the barn come down the camera cable and damage the recorder in the house?
4. Does a camera on a detached garage need its own outlet, or can the house recorder power it?
5. How long can a Uniview recorder and its cameras keep recording on a battery when the power is out?
6. Our standby generator takes about ten seconds to start — can that gap damage the recorder's hard drive?
7. Will our phones get a warning if the property loses power while we are away?
8. We are on Starlink in Pine Plains — can the phone app reach the recorder without a public internet address?
9. Will a slow rural internet line make the recorded footage itself lower quality?
10. Our road is on the list for new fiber — should we wait for it before putting cameras in?
11. What happens to the EZView app on our phones when Uniview retires it in 2027?
12. After the county dropped Flock, can we still put a plate-reading camera at the end of our own driveway?
13. Does footage from a private Uniview recorder go to the sheriff or any county system automatically?
14. If Washington tightens the rules on Uniview later, could the cameras on our farm simply stop working?
15. Is it legal to aim a camera at the town road in front of our farm stand?
16. Can a camera watch a foaling stall overnight without a white light that bothers the mare?
17. Will deer and coyotes crossing the field set off phone alerts all night?
18. Can the cameras at the gate tell us a car has turned in well before it reaches the house?
19. The Sheriff warned about late-night car thefts in Amenia and Millerton — where should a driveway camera point to actually help?
20. Can the recorder find every time a truck came up the drive last week without scrolling through hours of video?
21. If the link to the barn drops for an hour, is that hour of barn video simply lost?
22. Will a cold January night or a hot August afternoon in an unheated barn hurt the switch and radio out there?
23. We rent rooms to Marist students — which parts of the house can we legally put cameras on?
24. Is trenching to a barn or gate included in the package price, or quoted separately?

### §17 FAQ (visible == FAQPage schema, 10)
1. Is a visit to Amenia or Millerton charged more than one in Poughkeepsie?
2. Can the old coax already in a farmhouse carry part of a new Uniview system?
3. Can installation be scheduled around haying, foaling season or a show weekend?
4. How long does an installation take on a property with a house, a barn and a long drive?
5. Will our power or internet need to be shut off during the work?
6. What happens if a winter storm knocks a camera out of alignment after the installation?
7. Will buried cable be marked so a fence post or tractor doesn't cut it later?
8. Can we lock in the price and schedule before the ground freezes?
9. Do you hand over a map of where every camera and cable runs?
10. Can our existing Ring or Arlo cameras stay up alongside the Uniview system?

Intents deliberately avoided (already on other silo pages): cost-in-area, offline/not recording, legal-to-install, footage retention length, work-without-internet, internet speed needed, Uniview banned, upgrade old cameras, long rural cable runs / outbuildings (as a yes/no capability), farm/estate/seasonal-home coverage, winter weather, wired vs wireless, neighbor privacy, historic preservation, multiple viewers, warranty, Entity-List support/firmware (Manhattan), police clip export (Manhattan), doorman rights (Manhattan).

---

## Dutchess

### D-P — population, towns, building stock

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-P1 | `Dutchess County 2020 census population 295,911 towns cities Poughkeepsie Beacon` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Dutchess_County,_New_York ; https://www.poughkeepsiejournal.com/story/news/local/2021/08/13/gda-2020-census-population-ny-ppou-36027/118179938/ | 2020 Census population 295,911 (−0.5% vs 2010); county seat City of Poughkeepsie. | §5 para 1; §Sources |
| D-P2 | same search (excerpt) | https://data.census.gov/profile/Poughkeepsie_town,_Dutchess_County,_New_York?g=060XX00US3602759652 | Town of Poughkeepsie total population 45,471 (2020 Decennial). | §5 para 1 ("roughly 45,000") |
| D-P3 | `Dutchess County colleges Marist College Poughkeepsie Vassar College Bard College…` · Firecrawl search (excerpts) | https://www.dutchessny.gov/Schools/colleges.htm ; https://www.ciachef.edu/cia-new-york/ | County list: Marist University, 3399 North Road, Poughkeepsie; Vassar College, 124 Raymond Ave; Bard College, Annandale-on-Hudson; Dutchess Community College; CIA, 1946 Campus Drive, Hyde Park. CIA: "170-acre riverside main campus in Hyde Park". | §7 student-rental card; §13 cards; §9 Marist H3 |

### D-A — farms and estates

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-A1 | (direct) · Firecrawl scrape, PDF parser, query | https://www.nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36027.pdf | Dutchess 2022: 620 farms; 99,652 acres in farms (−2%); average 161 acres (−2%); market value of products sold $45,077,000 (+3%); horses/ponies sales $3,709k, rank 7 in state. | Hero; §5 para 2; §5.5; §Sources |
| D-A2 | `Millbrook NY horse country hunt Dutchess estates Millbrook Hunt` · Firecrawl search (excerpt) | https://www.themillbrookhunt.com/ | "Since 1907, The Millbrook Hunt has served as a pillar of Northeast Dutchess County"; founders of Dutchess Land Conservancy (1985) were members. | §13 card |

### D-W — power / grid

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-W1 | `Poughkeepsie Journal Central Hudson outage July 2026 Dutchess restoration` · Firecrawl search (news) | https://www.dutchessny.gov/Departments/County-Executive/47497.htm | July 6, 2026 12pm: storm Sat July 4; Central Hudson restored ~half; "more than 19,000 customers in Dutchess County, still without power"; 90% restoration by 10pm Tue July 7; NYSEG "over 3,400 customers still without power in Dutchess County". | §5 para 3; §5.5; §10.5 H3 5 |
| D-W2 | same (news) | https://spectrumlocalnews.com/nys/hudson-valley/news/2026/07/05/thunderstorm-leaves-thousands-without-power-in-dutchess-county | "interrupting service to approximately 50,000 customers at the height of the storm"; Town of Poughkeepsie largely restored by noon Wednesday. | §5 para 3 |
| D-W3 | `Central Hudson outage Dutchess County 2026 customers without power storm` · Firecrawl search → scrape | https://www.cenhud.com/en/outages/ | Storm notices Sept 26–27, 2026; credit policy: outages ≥72 h affecting ≥20,000 electric customers → residential $25 per subsequent 24-h period. | §5.5 |
| D-W4 | (direct) · Firecrawl scrape, query | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 26, 2026: >19,000 homes/businesses out after nor'easter; hardest hit Woodstock, Shawangunk, Plattekill, Hurley (Ulster). | §Sources only (Ulster-focused; not stated as Dutchess fact) |
| D-W5 | same search (excerpt) | https://poweroutage.us/area/utility/28 ; https://stormcentral.cenhud.com/ | PowerOutage.us lists Dutchess County 124,676 tracked Central Hudson customers; Central Hudson map "Total Customers Served 315,497". | Not used on page (context) |

### D-B — broadband / internet

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-B1 | `Dutchess County broadband unserved addresses ConnectALL fiber expansion 2025 2026` · Firecrawl search (excerpt) | https://www.governor.ny.gov/news/governor-hochul-us-senators-schumer-and-gillibrand-and-us-representative-tonko-announce-more | BEAD: $542M for 58,617 locations statewide; Archtop Fiber $23,728,734 (+ match) for 1,638 locations in Columbia, Dutchess, Orange, Sullivan; Reasnor Telephone $11,437,665 for 795 Dutchess locations, fiber. (Release date not in excerpt.) | §5.5; §9 wait-for-fiber H3; §Sources |
| D-B2 | `Starlink support CGNAT port forwarding public IPv4 residential` · Firecrawl search (excerpts, starlink.com only) | https://starlink.com/support/article/ac09301b-cef6-a125-c251-856196a77f92 ; https://starlink.com/support/article/1192f3ef-2a17-31d9-261a-a59d215629f4 ; https://starlink.com/support/article/e5dc0b86-09b4-084b-918b-3fa181e5fb5d | "The default IP policy using CGNAT blocks all inbound ports"; "Starlink WiFi routers do not support port forwarding"; VPNs with NAT traversal work; a Public IP policy option exists (Czech help article excerpt). | §9 Starlink H3; §10 table; §10.5 H3 3 |
| D-B3 | `Starlink Dutchess County rural internet Red Hook Amenia Pine Plains slow internet reddit` · Firecrawl search | (r/Starlink threads, not Dutchess-specific) | No Dutchess-specific thread surfaced → EMPTY for local Reddit on internet. | Not used |

### D-N — local news / hyperlocal (cameras, crime)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-N1 | `site:reddit.com r/Poughkeepsie OR r/hudsonvalley security cameras package theft Dutchess` · Firecrawl search (excerpts) | https://www.reddit.com/r/hudsonvalley/comments/1wq3bqo/dutchess_county_da_sheriffs_office_withdraw/ ; …/1vr3h8i/flock_camera_buckingham_ave_town_of_poughkeepsie/ ; …/1rp1a5r/flock_cameras_approved_in_secret_in_pine_plains/ ; …/1wmn9j7/flock_camera_town_halls_this_week_dutchess_county/ | r/hudsonvalley threads on Flock cameras in Town of Poughkeepsie, Pine Plains, town halls in Pleasant Valley; commenter: "The County Exec through Real Time Crime initiative placed 100s of Flock camera's across Dutchess" (unverified user claim — NOT used as fact). | §5 para 4 context (facts taken from D-N3/N4 instead) |
| D-N2 | `Dutchess County District Attorney Parisi Sheriff Imperati withdraw support Flock cameras` · Firecrawl search (excerpt) | https://www.timesunion.com/hudsonvalley/news/article/dutchess-county-decommission-flock-22448942.php | Decision followed packed public meeting at Pleasant Valley Town Hall; DA Parisi requested Flock decommission and remove cameras, company confirmed it would comply; County Executive Sue Serino commended the decision. | §5 para 4; §Sources |
| D-N3 | (direct) · Firecrawl scrape, query | https://www.newpineplainsherald.org/dutchess-sheriff-and-district-attorney-withdraw-support-for-flock-cameras/ | Published 2026-09-25; joint release Sept. 25; residents questioned "privacy, data sharing, cybersecurity and oversight". | §5 para 4; §5.5; §9 Flock H3s; §8.5 |
| D-N4 | same search (excerpt) | https://www.news10.com/news/dutchess-county/dutchess-county-da-sheriffs-office-withdraw-support-for-flock-technology/ | Confirms withdrawal (Nexstar). | Background |
| D-N5 | `Dutchess County Real Time Crime Center private camera registration program residents businesses` · Firecrawl search (excerpts) | https://refer.flocksafety.com/community/dutchess-county-community-connect ; https://millertonnews.com/dutchess-real-time-crime-center ; https://www.dutchessny.gov/46202.htm | Flock "Community Connect" page invited registering home/business cameras with the agency's real-time response system; Millerton News: "residents and businesses can register private security cameras to the county network"; county RTCC launch release. | §9 footage-to-sheriff H3; §8.5 |
| D-N6 | same (excerpt) | https://miscellanynews.org/2026/10/01/news/public-outcry-reverses-flock-camera-initiative-in-dutchess-county/ | Vassar student paper, Oct 1, 2026: residents discovered cameras after placement; concerns system could be exploited and data leaked. | §Sources |
| D-N7 | `Dutchess County farm equipment theft barn burglary sheriff 2025 2026` · Firecrawl search (excerpt; page undated) | https://www.dutchessny.gov/Departments/Sheriff/Recent-Thefts-and-Attempted-Burglary-in-North-Eastern-Dutchess.htm | Sheriff: larcenies from vehicles, three vehicle thefts and an attempted burglary in Amenia and Millerton, late night/early morning, vehicles unlocked with fobs inside; believed organized out-of-state ring; advice to lock vehicles. No date on page. | §9 Amenia/Millerton H3 |

### D-L — landmarks

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-L1 | `Walkway Over the Hudson length Poughkeepsie Highland pedestrian bridge feet` · Firecrawl search | https://walkway.org/visit/ | 212 feet above the Hudson; 1.28 miles gate to gate. | §13 |
| D-L2 | `Dia Beacon former Nabisco box printing factory Beacon NY` · Firecrawl search | https://www.diaart.org/visit/visit-our-locations-sites/dia-beacon-beacon-united-states | "Occupying a former Nabisco box-printing factory on the banks of the Hudson River". | §13 |
| D-L3 | `Dutchess County Fair Rhinebeck fairgrounds August annual` · Firecrawl search | https://dutchessfair.com/ | Fairgrounds at 6596 Route 9, Rhinebeck; fair returns Aug 24–29, 2027. | §13 |
| D-L4 | D-A2 Millbrook Hunt | https://www.themillbrookhunt.com/ | see D-A2 | §13 |
| D-L5 | D-P3 CIA | https://www.ciachef.edu/cia-new-york/ | 170-acre riverside campus, Hyde Park. | §13 |
| D-L6 | D-P3 Marist/Vassar | https://www.dutchessny.gov/Schools/colleges.htm | addresses as above. | §13; §7 |
| D-L7 | `Rhinebeck village historic district Beekman Arms oldest inn Dutchess` · Firecrawl search (excerpt) | https://www.beekmandelamaterinn.com/accommodations | Beekman Arms describes itself as "America's oldest continuously operated hotel" in the Village of Rhinebeck. | Not used on page (self-claim) |

### D-G — local licensing / permits

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| D-G1 | `Dutchess County electrical license low voltage security camera permit Poughkeepsie` · Firecrawl gov search | https://nysenate.gov/legislation/laws/cnt/236-a | County Law § 236-a authorizes Dutchess, Suffolk and Westchester to establish a county board of examiners for master electricians. | §8.5 |
| D-G2 | same | https://townofpoughkeepsie-ny.gov/DocumentCenter/View/133/Town-Approved-Electrical-Agencies-PDF | Town of Poughkeepsie Building Dept lists town-approved third-party electrical inspection agencies. | §8.5 |
| D-G3 | `"Dutchess County" "Electrical Examiners" board master electrician license` · Firecrawl search (excerpt) | https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2018/December/Rules-12-17-18.pdf | Putnam Legislature minutes (Dec 2018): "Dutchess County does not have county-wide licensing". (2018 excerpt — FLAG: confirm still true.) | §8.5 |
| D-G4 | (statute, not fetched this run; cited by Manhattan file and model page) | https://www.nysenate.gov/legislation/laws/PEN/250.00 | NY Penal Law art. 250 (eavesdropping; unlawful surveillance). | §8.5; §9 farm-stand and Marist H3s |

### Local findings that came back EMPTY
- Dutchess-specific Reddit thread bodies: EMPTY (not accessible in build env); only titles/excerpts.
- Yelp 1–3★ review text for Poughkeepsie installers: EMPTY (not accessible in build env).
- Village of Rhinebeck historic-district review rules for exterior cameras: not searched to a primary source → not used (no claim made on page).
- Dutchess package-theft / porch-piracy local news: no Dutchess-specific item surfaced → not used.

---

# Merged from parallel nassau build (batch 2026-10-18T14:40Z)

# Uniview Camera Installation — Nassau part (for merge into research/uniview-camera-installation.md)

Created 2026-10-18 by the subagent rebuilding `uniview-camera-installation-nassau-county` (queue line: `REBUILD | uniview-camera-installation-nassau-county | Uniview Camera Installation | Nassau | up /uniview-camera-installation-long-island | (516) 346-5778 | GBP Brooklyn`). Silo-wide findings (Entity List, FCC Covered List, NDAA §889, UNV-Link replacing EZView with EZView expected to stop in 2027, datasheets, default password, CVE notices, cost claims C1–C6) are reused from `research/uniview-camera-installation.md` (rows F1–F5, U1–U17, C1–C6, L1–L2) and are not repeated here. A parallel agent is building Staten Island in the same run; that page's notes go elsewhere.

Format (v2.3 §12.4): **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, web + news), Firecrawl scrape (markdown / query mode / PDF parser), Firecrawl gov search, Firecrawl Alexandria `census-gov`. Shell curl blocked. Reddit pages refused by Firecrawl ("we do not support this site") → Reddit rows are search excerpts only. Nassau County (nassaucountyny.gov) and Nassau Police (pdcn.org) CivicPlus pages render empty to the scraper except the archive site and news flashes → those rows rely on gov-search excerpts where marked.

Page section labels: §Hero, §Quick, §5 Neighborhood (+§5.5 facts), §Repair, §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing (+ worked example), §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

Thesis: **Nassau is 1.39 million people in mostly owner-occupied, mid-century detached houses split among 3 towns, 2 cities and 64 villages — so a Uniview system here is designed around who answers the call (county police or a village department), the long LIRR day when nobody is home, the strip-center shop with a landlord in the middle, and the South Shore tide and PSEG outages that decide where a recorder can safely live.**

---

## Nassau

### N-P Population, government, building stock

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-P1 | Alexandria `census-gov` `census/data` · dataset acs/acs5, vintage 2023, variables B01003_001E, B25024_001E–_005E, B25035_001E, B25003_001E–_002E, B25034_010E–_011E, geography `{for: county:059, in: [state:36]}` | https://api.census.gov/data/2023/acs/acs5 (table ACSDT5Y2023.B25024 etc., geo 0500000US36059) | Nassau County: population **1,388,138**; housing units **477,860**; **364,529** single-family detached (76.3%); 15,264 attached; **27,124** in 2-unit buildings; 9,003 in 3–4-unit; median year built **1955**; 61,756 units built 1940–49; 93,213 built 1939 or earlier; occupied **456,076**, owner-occupied **373,665** (81.9%). | §5 para 1; §5.5; §7 cards; §Sources |
| N-P2 | `Nassau County NY 64 villages 2 cities 3 towns Hempstead North Hempstead Oyster Bay` · WebSearch → Firecrawl scrape (query, direct quote) | https://archive.nassaucountyny.gov/website/LW/moving_to_NC/cities_towns&villages.html | "Within Nassau County there are 2 cities, 3 towns, 64 incorporated villages and over 100 unincorporated areas. The entire county is physically divided amongst the 3 towns: Hempstead, North Hempstead, and Oyster Bay, and the two cities, Long Beach and Glen Cove." | Hero; §5 para 2; §5.5; §9 cluster A |

### N-G Licensing, permits, local rules

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-G1 | `Nassau County home improvement contractor license required Office of Consumer Affairs local law` · Firecrawl gov search → scrape (query, direct quote) | https://archive.nassaucountyny.gov/agencies/OCA/Business/LocalLaw6-1970.html | Nassau Admin Code §21-11 (L.L. 6-1970): licence required for a home improvement business. "Home Improvement" covers work on dwellings of not more than three families … but "shall not include … (e) automatic fire alarm systems, or (f) burglar alarm systems." Exception for plumbers/electricians etc. licensed under other law acting within their craft. | §8.5; §9 "Which license…" H3; §10.5 H3 3 |
| N-G2 | same gov search (excerpts) | https://nassaucountyny.gov/FAQ.aspx?QID=205 ; https://nassaucountyny.gov/1547/Consumer-Affairs ; https://nassaucountyny.gov/DocumentCenter/View/48545 | Law = Admin Code Title D 21-10 to 21-11.16; Consumer Affairs licensing division "administers more than 10 thousand licenses in more than 15 types"; HI application fee $650 + $50 Restitution Fund; two-year licence. | §8.5 (licence count, two-year term) |
| N-G3 | `Nassau County electrical license master electrician …` · Firecrawl search → scrape ecode360 (query, direct quote) | https://ecode360.com/15509840 ; https://ecode360.com/15509866 | Town of Hempstead Code ch. 84 (L.L. 14-1976): "no person shall engage in the installation and wiring of electrical apparatus in the Town of Hempstead in a professional capacity until such person shall apply for and obtain a master electrician's license"; §84-10 homeowner exception (affidavit). Electrical licensing in Nassau is town-level (excerpt from search results: "Please check with your local municipality for licensing requirements"). | §8.5; §7.5; §FAQ siding/attic answers (120 V by licensed electrician) |
| N-G4 | `Nassau County alarm permit ordinance false alarm fee police department` · Firecrawl gov search (excerpts) | https://nassaucountyny.gov/DocumentCenter/View/51164 (Admin Code as of Jan 1, 2026, §8-40.x) ; https://nassaucountyny.gov/DocumentCenter/View/17813 | §8-40.0: permits required for alarms called into the Police Department; graduated false-alarm penalties (commercial non-permit holder schedule shows $550–$750); new installs not subject to false-alarm notifications for 90 days up to 3 notifications "provided that an alarm permit has been issued"; "All residential alarm notifications must include an attempted telephone notification with two calls back". (Full PDF scrape returned only the TOC — 741 pages; figures from excerpt.) | §8.5; §9 alarm-permit H3 |
| N-G5 | (search result excerpt) | https://www.pdcn.org/343/Alarm-Permit-Section-Communication-Burea | "The Nassau County Police are requested to respond to over 125,000 false alarms each year." (Page body would not render to scraper; excerpt only.) | §5.5; §9 alarm-permit H3 |
| N-G6 | `Nassau County police camera registration program residents businesses register security cameras` · Firecrawl search → scrape (markdown) | https://gardencitypolice.net/private-camera-reg | Garden City PD (Village) voluntary Private Camera Registration Program: register address as a location with cameras; "strictly voluntary and does NOT provide us access to security camera systems"; officers still canvass door to door; "detectives may ask to inspect your surveillance video recorded during a finite period"; Detective Division 349 Stewart Ave, Garden City. | §5 para 2; §9 village-police H3; §10.5 H3 5 |
| N-G7 | same search (excerpt) | https://www.pdcn.org/143/SPiN | NCPD "SPIN – Nassau County Security/Police Information Network" for residents and businesses, information sharing (page body didn't render). | §9 village-police H3 (named only) |
| N-G8 | `Nassau County village code security camera neighbor privacy …` · Firecrawl search → scrape (query) | https://abc7ny.com/post/village-considers-residential-surveillance-camera-rule/2524365/ | Oct 12, 2017: Village of Flower Hill considered a local law "to preclude the installation and use of an imaging device with no legitimate purpose other than viewing or recording another person in an area of that person's property where the person would not otherwise be visible"; prompted by two cameras high in a tree aimed at a neighbor's back yard. Enactment NOT verified (gov search found only Flower Hill ch. 121 Filming) → page says "considered", not "passed". | §9 neighbor-yard H3 |
| N-G9 | same gov search | https://ecode360.com/38072733 | Village of Lake Grove (Suffolk, not Nassau) ch. 161 bars cameras that observe an adjoining yard (amended 2024). Not used on the Nassau page (wrong county). | Not used |

### N-W Storms, flooding, power

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-W1 | `Long Beach NY flooding nor'easter 2025 2026 tidal flooding Island Park Freeport streets` · Firecrawl search → scrape (query) | https://hudsonvalley.news12.com/2026/09/28/live-updates-noreaster-causes-power-outages-downed-trees-and-flooding-on-long-island/3E5kQlwadk8iKvplGZPC8G | Sept 26–28, 2026 nor'easter: LIRR Long Beach Branch suspended from Saturday 8:30 a.m. for flooding in Island Park, restored Sunday night; LIRR President Rob Free: crews "pumped millions of gallons of water", tides kept returning; shuttle buses Valley Stream–Long Beach. PSEG LI restored nearly 112,000 customers; 7,971 of 1.2 million still out Sunday 9 p.m.; "Suffolk County and Oyster Bay were the hardest hit areas"; 1,350+ workers. | §5 para 4; §5.5; §9 storm H3s; §10.5 H3 4 |
| N-W2 | `PSEG Long Island outage Nassau customers without power storm 2026` · Firecrawl search (excerpts) | https://longisland.news12.com/2026/07/06/thousands-of-long-islands-still-without-power-as-residents-brace-for-more-storms-heavy-rain/2RaQBqZc0KPBsb7jcywA4j ; https://www.psegliny.com/en/Newsroom/2025/060726-StormUpdate1630 | July 6, 2026: PSEG said more than 91% of customers affected by severe thunderstorms restored by 9 a.m. Monday. PSEG LI serves ~1.2 million customers. | §5.5 (context) |
| N-W3 | `Long Beach NY boardwalk 2.2 miles rebuilt after Hurricane Sandy` · Firecrawl search (excerpt) | https://www.cbsnews.com/newyork/news/long-beach-boardwalk-is-back-one-year-after-sandy/ | Rebuilt boardwalk a year after Sandy: tropical hardwood "supposed to last 50 years", new retaining wall, LED lighting. (Length not confirmed → not stated.) | §13 |

### N-C Crime / police / news (cameras context)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-C1 | `Nassau County police residential burglaries pattern …` · Firecrawl search → scrape NCPD news flash (query) | https://www.pdcn.org/CivicAlerts.aspx?AID=15190 | Posted July 27, 2026: Major Case Squad arrested a Bethlehem, PA man July 24, 2026; between July 11, 2025 and May 23, 2026 he entered multiple residences throughout Nassau County and removed jewelry; located in New Hyde Park; six counts Burglary 2nd. | §5 para 3; §9 face-at-stoop H3 |
| N-C2 | same search (excerpt) | http://nassauda.org/m/newsflash/Home/Detail/1418 | Nassau DA: Queens man sentenced to 30 years for pattern of North Shore burglaries; "$1 million in cash and property over five months" (excerpt; date not in excerpt). | §5.5 |
| N-C3 | `LIRR station parking lot car break-ins catalytic converter theft Nassau commuter lot police` · Firecrawl search → scrape (query) | https://www.cbsnews.com/newyork/news/metal-thieves-targeting-cars-at-lirr-station-lots-for-pricey-part/ | CBS New York: two cars by the Syosset station and one near Hicksville had catalytic converters stolen in two weeks; MTA police working with Nassau County police. Article date not captured (image path 2015) → page says "CBS New York has reported", no year. | §9 catalytic-converter H3 |
| N-C4 | `Long Island retail theft strip mall …` · Firecrawl search → scrape PDF (query) | https://www.licares.org/wp-content/uploads/Newsday-shoplifting.pdf | Newsday, Sunday April 21, 2024: in Nassau, petit larceny shoplifting incidents grew 27% to 3,819 from 2022 to 2023 (NCPD data via FOIL); grand larceny shoplifting fell 8% to 981. | §8; §5.5; §9 crew H3 |
| N-C5 | `Nassau County Flock cameras license plate readers Nassau police 2026` · Firecrawl search (news excerpt) | https://investigativepost.org/2026/07/17/license-plate-readers-are-everywhere-in-wny/ | July 17, 2026, citing DeFlock: Nassau County has 331 reported ALPR cameras, the most of any NY county (Queens 307, New York County 299). | §5.5 (context only; plate-reader question deliberately NOT asked — Dutchess owns that intent) |
| N-C6 | `Nassau County police burglary crews Wi-Fi jammers …` · Firecrawl search (excerpt) | https://bronx.news12.com/police-in-new-jersey-say-burglars-are-using-wi-fi-jammers-to-target-homes-heres-what-you-need-to-know | New Jersey police (News 12): suspect believed to have used a Wi-Fi jammer to knock out cameras and the homeowner's cellphone service. No Nassau-specific jammer report found → page attributes to New Jersey police only. | §9 jammer H3; §10.5 H3 4 |

### N-L Landmarks / corridors

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-L1 | `Roosevelt Field mall Garden City … Green Acres Mall Valley Stream` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Green_Acres_Mall ; https://m.yelp.com/biz/roosevelt-field-garden-city-5 | Green Acres Mall: South Valley Stream off Sunrise Highway near the NYC border, GLA 2,069,000 sq ft; Roosevelt Field described as "Long Island's largest shopping mall"; Roosevelt Field at 630 Old Country Rd, Garden City. | §8; §13 |
| N-L2 | `Americana Manhasset Northern Boulevard luxury shopping center` · Firecrawl search (excerpts) | https://www.americanamanhasset.com/ ; https://www.americanamanhasset.com/about/ | 2060 Northern Boulevard, Manhasset; "over 60" luxury and contemporary shops; "20 miles from Manhattan". | §8; §13 |
| N-L3 | `UBS Arena Belmont Park Elmont opened November 2021 Islanders` · Firecrawl search (excerpts) | https://abc7ny.com/post/ubs-arena-new-york-islanders-belmont-park-nassau-coliseum/11253644/ | Ribbon cutting Nov 19, 2021, UBS Arena at Belmont Park, Elmont; home of the NY Islanders. | §13 |
| N-L4 | `Hofstra University Hempstead campus acres arboretum` · Firecrawl search (excerpt) | https://www.hofstra.edu/facilities-operations/arboretum.html | "The 244-acre campus received official recognition as an Arboretum in 1985". | §13 |
| N-L5 | N-W3 | https://www.cbsnews.com/newyork/news/long-beach-boardwalk-is-back-one-year-after-sandy/ | Long Beach boardwalk rebuilt after Sandy. | §13 |
| N-L6 | N-G6 | https://gardencitypolice.net/private-camera-reg | Garden City village, Stewart Ave. | §13 (Garden City card) |

### N-R Reddit / resident voice (excerpts only)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-R1 | `site:reddit.com r/longisland security cameras Nassau house break-in cameras recommendation` · Firecrawl search | https://www.reddit.com/r/longisland/comments/1h8ygon/what_cameraalarm_system_do_you_use_andor/ | "Eufy cameras … It won't report to the cops or anything, but if you add SD cards you can view…" | §10 comparison context |
| N-R2 | same | https://www.reddit.com/r/longisland/comments/1cn1pcu/security_system_suggestions/ | Resident prefers Reolink for "smooth experience". | Background |
| N-R3 | same | https://www.reddit.com/r/longisland/comments/1tbxkb0/is_anyone_talking_about_the_flock_cameras_being/ | High-engagement thread (1.3K votes) worried about Flock cameras on Long Island. Thread body: EMPTY (not accessible in build env). | §5 para 2 context (where footage goes) |

### Nassau sources EMPTY
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG — EMPTY (not accessible in build env).
- Yelp 1–3★ for Nassau camera installers — EMPTY (not accessible in build env; not searched further after silo result).
- Reddit thread bodies (r/longisland) — EMPTY (not accessible in build env); excerpts only.
- nassaucountyny.gov Licensing page and pdcn.org Alarm Permit / SPiN page bodies — EMPTY (render blank to scraper); facts taken from gov-search excerpts and the archive site.
- Nassau-specific Wi-Fi-jammer burglary report — none found; jammer facts attributed to New Jersey police.
- Field Notes: no real AESS Nassau Uniview anecdote supplied → written as a method note, no story.

### Pricing basis (Nassau)

Published engine in `uniview-camera-installation-prices-nassau-county.html` (`var PG`, zone "Nassau": line 210, jbox 30, setup 180, parking 0, min_visit 675; BP engine DRIVE 228.99, CONCEAL 200), run in Node in the scratch dir. Outputs quoted as published: EC-B4F28DL / EC-T4F28DL $449; IPC2128LB-ADF28K-DL and IPC3618LB-ADF28K-DL $559; IPC3638SS-ADF28KMC-I1 Tri-Guard $969; IPC6324LWH-AX5C-VG2 PTZ $1,049; IPC6424SR-X25-VF $1,669; PKC2640@Z28-IR-P $1,759; IPC86CEB-AF18KC-I0 fisheye $2,119; ED-525B-WB doorbell $689; UAC-B122-AF28M analog $329; XVR301-04G3 $359; NVR301-04LS3-P4 $499; NVR301-08LS3-P8 $619; NVR301-16B-LP8-IQ $899; NVR302-16B-P16-IQ $1,219; 4TB drive $229; hidden wiring $200/camera. Packages: 4 × EC-T4F28DL + NVR301-04LS3-P4 + 4TB = **$2,524** (= page's published "4-camera from $2,524"); 6 × EC-T4F28DL + 2 × IPC2128LB + NVR301-08LS3-P8 + 2 × 4TB = **$4,889**; 6 × IPC3618LB + IPC86CEB fisheye + NVR301-08LS3-P8 + 2 × 4TB = **$6,550**; 1-month recording: $2,753 / $5,118 / $7,008. Labor-only: $210 per camera + $30 box + $180 recorder set-up. Service rate $195/hr, 3-hr min ($585) per v2.3 §9.
**FLAG:** engine zone "Nassau" carries `min_visit: 675` labelled "3-hour minimum visit" in the quote; v2.3 §9 protects $585. Page publishes $585 as the service/callback rate and refers to "the small-job minimum on the published price list" without restating $675. Also the prices page offers extended 1/2/3-year warranty options — the install page uses only the one-year parts-only terms sentence.

---

## Question register — nassau

Page: `uniview-camera-installation-nassau-county` (rebuilt 2026-10-18). Checked by meaning against the silo register (old template questions, Manhattan §9/§17, Dutchess §9/§17) and the other uniview-camera-installation-* pages on disk.

### §9 Q&A (H3)
1. Our village has its own police department — how do detectives find out we have cameras?
2. Which license should a Nassau camera installer hold, given how the county's home-improvement law is written?
3. Our burglar alarm already has a Nassau police permit — what changes if cameras are added to it?
4. A camera on our side yard can see into the neighbor's back yard — where is the line in Nassau's villages?
5. We are on the LIRR from 6 a.m. to 7 p.m. — which phone alerts are worth keeping, and which will we mute within a week?
6. On a Cape Cod with a low front stoop, where does the camera go to record a face rather than the top of a cap?
7. Thieves have taken catalytic converters near the Syosset and Hicksville stations — can a home camera protect the car in our own driveway overnight?
8. A school bus stop is at our corner — is it a problem if a camera records the children waiting there?
9. Can a camera go on the utility pole or the street tree in front of the house for a better angle?
10. The recorder's clock was wrong after the last outage — does a bad timestamp matter if police need the clip?
11. Our shop is one unit in a strip center — can our cameras cover the sidewalk and parking field the landlord controls?
12. The center's owner runs his own cameras — can our Uniview recorder and his system share views?
13. How do we watch the register without recording customers' card PINs?
14. When a shoplifting crew hits several stores, which camera view do detectives actually use?
15. Can a camera cover the back room where staff change before a shift?
16. How do we keep the accessory apartment's entrance off the main household's phones?
17. We rent the Long Beach house out for the summer — how do we switch the indoor cameras off for tenants and back on afterwards?
18. Can a Wi-Fi jammer knock a wired Uniview system offline the way it can a battery camera?

### §17 FAQ (visible == FAQPage schema, 10)
1. Can the installation be done on a Saturday so nobody has to take a day off?
2. Do you need to get into the attic, and what if it is floored over or packed with blown-in insulation?
3. Can a Uniview doorbell at the front door record onto the same recorder as the other cameras?
4. Will screw holes in vinyl or aluminum siding let water in behind it?
5. Can the system be finished before we leave for Florida for the winter?
6. Why does the night picture turn white when a camera sits behind a storm door or under a porch ceiling?
7. Do you take away the old DVR and cameras, and what happens to the recordings on that old drive?
8. Can a camera watch the pool gate and alert us when it opens?
9. What do we pay up front, and when is the rest due?
10. Can cameras go under a slate or tile roof overhang without anyone walking on the roof?

De-dup note (vs the parallel Staten Island rebuild, read from its in-progress HTML at 15:12): two earlier Nassau drafts — recorder height in a raised Island Park/Freeport house, and a post-nor'easter lens/mount check for Long Beach — overlapped Staten Island's flood-code / evacuation-recorder / lens-cleaning questions and were replaced by #8 and #9 above; flood and PSEG facts remain in Nassau body text only. Masked block similarity (geo-masked, difflib, p/li/td/h3/figcaption blocks ≥12 words, warranty sentence excluded) vs every uniview-camera-installation-* page incl. prices pages and the in-progress Staten Island file: max 0.607.

Intents deliberately avoided (already on other silo pages): cost in area, offline/not recording, legal to install, retention length, work without internet, internet speed, Uniview banned (asked only in §10.5 body, not as a question), upgrade old cameras, multiple viewers (as a yes/no), wired vs wireless (as a yes/no), coastal/winter durability (as a yes/no), neighbor privacy as generic question (ours is village-specific with the Flower Hill item), sign posting, plate reader at own driveway (Dutchess), battery runtime / generator gap (Dutchess), map hand-over (Dutchess), installation duration (Dutchess), EZCloud takeover / managing-agent handover / doorman rights / recorder location in a closet-less building / unplugging recorder / HDD-failure email / TV display / building sale ownership (Manhattan).

### Images (Nassau page)
images: 11 reused (no real Uniview job photos yet) — 9 real AESS job photos from images/floodlight-camera-installation/ (5), images/hikvision-security-camera-installation/ (1), images/security-camera-maintenance/ (3), and 2 Uniview manufacturer product shots (images/uniview-turret-network-camera-white.jpg, images/uniview-dual-lens-colorhunter-bullet-camera-white.jpg). Source photos checked (dHash + visual) against the Manhattan, Dutchess and in-progress Staten Island picks; one draft pick (white dome in ceiling corner) matched a Staten Island photo and was swapped.

| File (images/uniview-camera-installation/uniview-camera-installation-nassau-county-…) | Source |
|---|---|
| white-turret-on-ceiling-tile-between-light-panels.webp | floodlight-camera-installation/…-orange-county-white-dome-camera-on-ceiling-tile-near-light-panel.webp |
| black-eyeball-camera-in-ceiling-corner-below-light-panel.webp | floodlight-camera-installation/…-hudson-valley-black-eyeball-camera-in-corner-below-ceiling-light.webp |
| black-bullet-on-short-ceiling-bracket-above-plain-wall.webp | floodlight-camera-installation/…-hudson-valley-black-bullet-camera-on-bracket-under-drop-ceiling.webp |
| small-camera-high-on-plain-wall-casting-two-shadows.webp | floodlight-camera-installation/…-orange-county-small-camera-on-short-arm-high-on-plain-wall.webp |
| small-black-camera-on-ceiling-grid-near-recessed-lights.webp | floodlight-camera-installation/…-staten-island-small-black-camera-on-ceiling-grid-between-recessed-lights.webp |
| mini-dome-and-round-speaker-in-grid-ceiling.webp | hikvision-security-camera-installation/…-westchester-county-mini-dome-and-round-speaker-in-store-ceiling.webp |
| black-bullet-beside-return-air-grille-and-downlight.webp | security-camera-maintenance/…-bronx-bullet-camera-beside-return-air-grille.webp |
| recorder-live-view-grid-with-date-and-time-stamp.webp | security-camera-maintenance/…-nyc-recorder-live-view-with-date-and-time-stamp.webp |
| monitor-grid-of-overhead-store-aisle-views.webp | security-camera-maintenance/…-westchester-county-store-monitor-grid-of-overhead-aisle-camera-views.webp |
| uniview-tec-white-turret-product-photo.webp | images/uniview-turret-network-camera-white.jpg |
| unv-dual-lens-colorhunter-bullet-product-photo.webp | images/uniview-dual-lens-colorhunter-bullet-camera-white.jpg |

---

# Merged from parallel staten-island build (batch 2026-10-18T14:40Z)

# Uniview Camera Installation — Staten Island part (for merge into research/uniview-camera-installation.md)

Created 2026-10-18 by the subagent rebuilding `uniview-camera-installation-staten-island` (queue line: `REBUILD | uniview-camera-installation-staten-island | Uniview Camera Installation | Staten Island | up /uniview-camera-installation-nyc | (347) 934-8335 | GBP Brooklyn`). Silo-wide rows (federal status F1–F5, Uniview product/app rows U1–U17, cost claims C1–C6, state/city rules L1–L6) are reused from `research/uniview-camera-installation.md` and not repeated here. This file holds only the Staten Island research, the page's pricing basis and its question register.

Format (v2.3 §12.4): **exact query · platform · URL · finding · page+section used**. Tools actually used: `mcp__Firecrawl__firecrawl_search` (web, news), `mcp__Firecrawl__firecrawl_scrape` (query mode, PDF parser), `mcp__Firecrawl__firecrawl_gov_search`, Firecrawl Alexandria `census-gov` provider. Shell curl blocked. Reddit and Yelp pages are not scrapeable here → Reddit rows are **search excerpts only**; "excerpt" = read only as a search-result snippet.

Page section labels: §Hero, §Quick (instant action), §5 Neighborhood (+§5.5 facts), §Repair, §6 Services, §7 Architecture (+§7.5 method), §8 Commercial (+§8.5 rules), §9 Q&A (cluster → H3), §10 Equipment (+ recorder table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §11 Form, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ, §19 Siblings, §Sources.

Thesis: **Staten Island is a borough of houses with driveways — detached, semi-attached and two-family homes, most owner-occupied, many with a car outside overnight and, on the East and South Shore, a basement that flooded in 2012 — so a Uniview system is planned from the ground up: recorder above the flood line, a face camera at the car door, a camera per entrance in two-family houses, neighbors masked out.**

---

## Staten Island

### 1. Mandatory sources (v2.3 §3) — status for this page

| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only — rows SI-R1–SI-R4 (r/statenisland). Thread bodies: EMPTY (not accessible in build env). |
| 2 | Google PAA | EMPTY (not accessible in build env). |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and tests claims from ranking pages (silo rows C1–C6) instead. |
| 6 | Area landmarks | SI-L1–SI-L7. |
| 7 | Area use cases / building stock | SI-H1–SI-H3. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — no Bing/DDG related/autocomplete surface. |
| 9 | Local news | SI-N1–SI-N9 (Staten Island Advance/silive, ABC7, NY1, PBS, Grist, DNAinfo). |
| 10 | Hyperlocal | Staten Island Advance/silive (rows SI-N1–N5); DeFalco Realty New Dorp guide (SI-C1). Patch Staten Island: none surfaced → not used. |
| 11 | Yelp 1–3★ | `yelp security camera installation Staten Island reviews` · Firecrawl search → only listing pages (e.g. https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Staten+Island%2C+NY); no 1–3★ review text → **EMPTY (not accessible in build env)**. Not used. |

### 2. SI-H — Building stock, tenure, vehicles (Census) and housing history

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-H1 | Alexandria `census-gov` `census/data` · dataset acs/acs5, vintage 2023, variables B25024_001E–009E, B25035_001E, B25003_001E–003E, B25034_008E–011E, geography county:085 in state:36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36085 | Richmond County: **184,074** housing units; **63,421** 1-unit detached; **47,106** 1-unit attached; **41,749** in 2-unit buildings; 6,720 in 3–4; 3,740 in 5–9; 2,584 in 10–19; 4,220 in 20–49; **14,013** in 50+. Median year built **1974**. Built 1960–69: 23,568; 1950–59: 17,499; 1940–49: 7,534; **1939 or earlier: 32,820**. Occupied **170,047**; owner-occupied **115,534**; renter 54,513. (Derived on page: 152,276 = detached + attached + 2-unit, 82.7%; owner share 67.9%.) | §Hero; §5 para 1; §5.5; §7 cards; §Sources |
| SI-H2 | same provider · variables B25034_001E–007E, B01003_001E, B25044_001E, _003E, _010E, B08301_001E, _016E | https://api.census.gov/data/2023/acs/acs5 (county:085, state:36) | Built 2020+: 439; 2010–19: 7,764; 2000–09: 16,871; 1990–99: 19,254; **1980–89: 28,613**; **1970–79: 29,712** (sum 1970s+1980s = 58,325). Population **492,734**. Households with no vehicle: owner 7,343 + renter 19,082 = 26,425 of 170,047 → **about 84%** have at least one vehicle. (B08301_016E returned taxicab, not ferry → not used.) | §5 para 1–2; §5.5 |
| SI-H3 | `Staten Island "two-family" semi-attached houses 1970s 1980s building boom after Verrazzano Bridge zoning lower density growth management` · Firecrawl search → Firecrawl scrape (PDF parser, query/direct quote) | https://www.statenislandusa.com/uploads/8/9/8/7/89877849/zoning_poster.pdf | Borough President poster "Staten Island's New Zoning Map": "Between 1970 and 2000, the number of housing units in the Borough increased over 82%, from 89,950 to 163,341. Nearly 27,000 new housing permits were issued in the 1980’s, and 23,000 in the 1990’s." "R3-1 permits both one and two-family detached and semi-detached houses or duplexes. R3X and R3A permit only one and two-family detached houses." 2003 downzoning (areas for detached-only homes 30% → 57%). | §5 para 1; §5.5; §7 card "Semi-attached two-family"; §Sources |

### 3. SI-F — Flooding, Sandy, Build It Back, flood-resistant construction rules

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-F1 | `Hurricane Sandy Staten Island deaths homes destroyed Midland Beach Oakwood Beach buyout` · Firecrawl search (excerpt) | https://www.pbs.org/newshour/show/sandy-battered-homeowners-take-buyouts-rather-rebuild | PBS NewsHour (3 years after Sandy): "In Staten Island, New York, 24 people died from the storm, and more than 2,100 homes were destroyed." Nearly every one of the 180 homeowners in Oakwood Beach took the voluntary state buyout; state planned $200M to buy out 500 homes mostly in three SI neighborhoods. | §5 para 3; §Sources |
| SI-F2 | same search (excerpt) | https://grist.org/equity/oakwood-beach-staten-island-buyouts-superstorm-sandy/ | "The state acquired 308 properties during the buyouts and almost all of them have been demolished." | §5 para 3; §13 Oakwood Beach card |
| SI-F3 | `NYC Build It Back Staten Island homes elevated number completed program` · Firecrawl search (excerpt) | https://www.nyc.gov/site/housingrecovery/disaster-recovery/build-it-back.page | Build It Back construction: 8,319 homeowners served citywide; **Staten Island – 1,982**. | §5 para 3; §5.5; §9 Build It Back H3 |
| SI-F4 | same search (excerpt) | https://www.dnainfo.com/new-york/20170921/midland-beach/build-it-back-modular-homes-installation | DNAinfo, Sept 21, 2017: modular homes program covering 98 one- to four-family homes "mostly in Midland Beach, South Beach, New Dorp Beach, Far Rockaway and Broad Channel". | §5 para 3; §13 FDR Boardwalk card |
| SI-F5 | `South Shore of Staten Island Coastal Storm Risk Management project seawall Fort Wadsworth to Oakwood Beach miles Army Corps` · Firecrawl search (excerpts) | https://www.nan.usace.army.mil/Missions/Civil-Works/Projects-in-New-York/South-Shore-of-Staten-Island/ ; https://malliotakis.house.gov/media/in-the-news/staten-island-seawall-project-underway-officials-mark-12th-hurricane-sandy | USACE: project area "along the south shore ... from Fort Wadsworth to Oakwood Beach"; PPA executed Feb 15, 2019. Malliotakis page (excerpt): "The Army Corps expects construction on the seawall to start in 2028 on the portion running from Oakwood Beach through Miller Field". | §5 para 3 ("still being built"); §13 Oakwood card; §Sources |
| SI-F6 | `New York City Building Code Appendix G flood-resistant construction electrical equipment located above design flood elevation` · Firecrawl gov search (excerpts) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-188819 ; https://nyc.gov/assets/buildings/codes-pdf/2025electrical_code.pdf ; https://nyc.gov/assets/planning/downloads/pdf/our-work/plans/citywide/sustainable-communities-climate-resilience/designing_flood_risk.pdf | BC G310.6: "Mechanical, plumbing and electrical systems, including plumbing fixtures, shall be elevated to or above the design flood elevation" (exceptions per G304.1.2). EC 110.11(B): metering equipment, panelboards, load centers, main disconnects, service disconnecting means and circuit breakers "shall be located at or above the design flood elevation"; exception for nonresidential buildings with dry floodproofing. DCP "Designing for Flood Risk": DFE = BFE + freeboard; "On January 31, 2013, the Commissioner of Buildings issued an emergency rule to require one or two feet of freeboard (depending on the building category)". | §7.5 "Flood elevation"; §8.5 flood bullet; §9 flood-code H3; §Sources |
| SI-F7 | `Con Edison Staten Island customers lost power Isaias 2020 OR nor'easter outage Staten Island customers` · Firecrawl search (excerpts) | https://ny1.com/nyc/all-boroughs/news/2020/08/05/power-outages-in-nyc-today-tropical-storm-isaias-damage ; https://www.coned.com/en/about-us/media-center/news/2023/12-18/con-edison-restoring-customers--as-storm-passes-through-the-region | NY1 Aug 5, 2020: "the utility reported over 32,000 outages on Staten Island". Con Ed Dec 18, 2023: "Staten Island has 2,500 customers without service". | §Sources (NY1); battery-backup advice in §6/§Repair (no number used beyond Sources) |

### 4. SI-N — Local news: cars, burglaries, cameras

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-N1 | `silive.com crime-safety 2026/04 nypd staffing shortage blamed staten island car thefts` · Firecrawl search (page content returned in result) | https://www.silive.com/crime-safety/2026/04/nypd-staffing-shortage-blamed-as-staten-island-car-thefts-spike-22-over-last-year.html | Staten Island Advance (Maura Grunlund), April 2026: 71 vehicles stolen YTD vs 58 (+22%, CompStat through April 19). **120th Pct (St. George) 25 from 15 (+67%)**; 121st (Graniteville, parts of North & West shores) 18 from 20 (−10%); **122nd (portions of East & South shores) 18 from 15**; **123rd (South Shore) 10 from 8**. BP Fossella / DA McMahon quoted on staffing. | §5 para 2; §5.5; §8 Bay Street card; §Sources |
| SI-N2 | same search (excerpt) | https://www.silive.com/crime-safety/2026/07/staten-island-car-thefts-spike-47-in-2026-heres-what-law-enforcement-is-doing-about-it.html | "Vehicle thefts on Staten Island are up roughly 47% in 2026, with 163 incidents this year through July 19 compared to 111". | §5 para 2; §5.5; §9 driveway-light H3 |
| SI-N3 | `Staten Island car thefts driveway key fob relay 2025 NYPD silive` · Firecrawl search (full page text in result) | https://abc7ny.com/post/exclusive-video-car-theft-staten-island-key-fob/13546726/ | ABC7: exclusive video of suspects stealing an Infiniti from a Staten Island home — "the whole theft took less than 15 seconds"; NYPD Capt. Glorisel Lee: "Ninety percent of vehicles had their doors unlocked when the crime occurred." (Article date not shown in extract → page gives no date.) | §5 para 2; §9 driveway-light H3; §10.5 H3 6 |
| SI-N4 | same search (excerpt) | https://www.silive.com/crime-safety/2022/10/inside-staten-islands-shocking-day-of-car-thefts-7-vehicles-reported-stolen-to-nypd-in-24-hours.html | Oct 2022: seven stolen-vehicle reports in one day, "mostly unsecured with keys for the taking". | Background only |
| SI-N5 | `Hylan Boulevard Forest Avenue Staten Island small business commercial corridor storefronts burglary silive 2026` · Firecrawl search (excerpts) | https://www.silive.com/crime-safety/2023/04/staten-island-commercial-businesses-under-siege-a-timeline-of-burglaries-dating-back-to-september.html ; https://www.facebook.com/statenislandadvance/posts/three-stores-were-burglarized-during-the-early-morning-hours-on-sunday-march-29-/1412446170921423/ ; https://abc7ny.com/post/staten-island-burglaries-serial-burglar-si-robbery-pattern/13041459/ ; https://www.silive.com/news/2020/10/owner-bagel-shop-on-forest-ave-broken-into-by-brick-tossing-burglar.html | silive Apr 2023: "at least 30 burglaries at commercial properties across Staten Island within the last several months" (timeline back to September 2022). SI Advance post: "Three stores were burglarized during the early morning hours on Sunday, March 29, 2026. Windows broken, cash registers stolen at Hylan Boulevard…". ABC7: serial burglar "has also hit at least five businesses along a stretch of Forest Avenue, and in each case always going straight for the registers" (date not in excerpt). silive Oct 2020: bagel and wrap shops on Forest Ave (West Brighton) — smashed glass, stolen money. | §8 intro + Hylan / Forest cards; §9 store-recorder H3; §Sources |
| SI-N6 | `silive Staten Island surveillance video package thief porch police 2026` · Firecrawl search (news) | https://www.silive.com/news/2024/08/staten-island-barbershop-burglarized-4k-in-cash-hair-products-stolen-nypd-says.html | Aug 3, 2024: barbershop burglarized, $4K cash and hair products; "In security footage provided by the shop's owner, an individual can be seen entering the location and leaving with a box in their hands." | §8 barbershop card; §Sources |
| SI-N7 | SI-F1 (PBS) | — | see SI-F1 | §5 |
| SI-N8 | `Staten Island Ferry 5.2 mile 25 minute trip St. George Terminal Whitehall daily riders NYC DOT` · Firecrawl search (excerpts) | https://www.nyc.gov/html/dot/html/ferrybus/ferry-facts.shtml ; https://siferry.com/ ; https://en.wikipedia.org/wiki/Staten_Island_Ferry | NYC DOT: "5.2-mile run between the St. George Terminal in Staten Island and the Whitehall Terminal in Lower Manhattan." siferry.com: "The Ferry runs 24 hours a day/ 7 days a week." Wikipedia: trip about 25 minutes; 16,692,900 riders in 2025. | §13 St. George card; §6 commuter card; §Sources |
| SI-N9 | `New Dorp Lane Staten Island shopping district merchants Hylan Boulevard to New Dorp station` · Firecrawl search (excerpt) | https://www.defalcorealty.com/neighborhood-guide/new-dorp-staten-island/ | Realty neighborhood guide (secondary): "New Dorp Lane, a dense half-mile of restaurants, bakeries, hardware stores, hair salons, and small offices that runs from Hylan Boulevard down to the Staten Island Railway station." | §8 New Dorp Lane card (attributed "per a local neighborhood guide"); §Sources |

### 5. SI-R — Local Reddit (excerpts only)

| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| SI-R1 | `site:reddit.com r/statenisland security cameras house recommend` · Firecrawl search | https://www.reddit.com/r/statenisland/comments/18s4hir/any_home_security_recommendations/ | "Lorex 4k cameras mounted around the outside of my house. I found reolink to be a solid camera setup with decent prices." | §Sources (resident opinion) |
| SI-R2 | same | https://www.reddit.com/r/statenisland/comments/1vlcn52/flock_cameras/ | "The few Flock cameras on Staten Island seem to be on private property." (user claim, unverified) | §Sources only ("privately owned plate readers", as opinion) |
| SI-R3 | same | https://www.reddit.com/r/statenisland/comments/1wid0ib/new_cameras/ | Commenter says new street cameras are red-light cameras made by EKIN (user claim, unverified) | Not used |
| SI-R4 | same | https://www.reddit.com/r/statenisland/comments/1et8hav/cheap_backyard_privacy_solutions/ | Thread on backyard privacy from neighbors; replies about trees and peeping neighbors. | §Sources ("nosy neighbors", opinion); context for privacy-mask advice |

### 6. SI-L — Landmarks

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-L1 | SI-N8 | https://www.nyc.gov/html/dot/html/ferrybus/ferry-facts.shtml | St. George Terminal ↔ Whitehall, 5.2 miles, 24/7, ~25 min | §13 |
| SI-L2 | `Snug Harbor Cultural Center 83 acres Livingston Staten Island OR Freshkills Park 2,200 acres` · Firecrawl search (excerpts) | https://snug-harbor.org/ ; https://www.facebook.com/SnugHarborCCBG/ ; https://www.nycgovparks.org/parks/sailors-snug-harbor/history | "an 83-acre campus on Staten Island"; address 1000 Richmond Terrace; NYC Parks acreage 83.30. | §13 |
| SI-L3 | `Franklin D. Roosevelt Boardwalk Staten Island 2.5 miles South Beach Midland Beach NYC Parks` · Firecrawl search | https://www.nycgovparks.org/parks/fdr-boardwalk-and-beach | "This 2.5-mile boardwalk and beach area extends southeast from Fort Wadsworth to Miller Field’s Gateway Recreational Area, parallel to Father Capodanno Boulevard." | §13 |
| SI-L4 | SI-F1/F2 | PBS / Grist | Oakwood Beach buyouts, 308 properties acquired | §13 |
| SI-L5 | `Great Kills Park Gateway National Recreation Area Staten Island marina Hylan Boulevard` · Firecrawl search | https://www.nps.gov/gate/learn/historyculture/great-kills-park.htm | "a 523 acre park located on the south shore of Staten Island"; part of NPS since 1972 (Gateway NRA); beach, marina, boat launch; entrance from Hylan Boulevard. | §13; §8 Hylan card ("past the entrance to Great Kills Park") |
| SI-L6 | `Conference House Park Tottenville southernmost point New York State NYC Parks` · Firecrawl search (excerpts) | https://www.nycgovparks.org/parks/conference-house-park ; https://www.nycgovparks.org/parks/conference-house-park/dailyplant/19943 | "Located at the southernmost point of New York State, the 267-acre park". | §13 |
| SI-L7 | SI-F5 | USACE | Seawall line Fort Wadsworth → Oakwood Beach | §13 Oakwood card |

### 7. SI-G — City rules relevant to cameras on Staten Island

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-G1 | `New York City Electrical Code work exempt from permit low voltage class 2 security camera wiring` · Firecrawl gov search (excerpts) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 ; https://nyc.gov/assets/buildings/local_laws/ll128of2024.pdf | Admin Code §28-105.4.7: "An electrical permit shall not be required for the installation, alteration, maintenance, or repair of electrical wiring that is designed to operate at less than 50 volts for signaling, communication, alarm, and data transmission circuits, provided that such work is performed by a licensed master electrician, special electrician, or qualified person…" Exceptions: life safety systems; Class I/II/III hazardous locations incl. "certain areas within commercial garages". (Added by Local Law 128 of 2024.) | §8.5 permits bullet; §9 permit H3 |
| SI-G2 | same search (excerpt) | https://nyc.gov/site/buildings/property-or-business-owner/electrical-permit.page | DOB: "An electrical permit is required for most electrical work, including handling of electrical wires that is performed in a residential home or business" by DOB-licensed electrical contractors. | §9 permit H3 (new outlet needs electrician) |
| SI-G3 | Silo L1, L2, L4 (GBL §69-m; Labor Law §203-c; Penal Law §250.45; GBL §395-b; Admin Code §22-1202) | see research/uniview-camera-installation.md | reused | §Quick; §7.5; §8.5; §9 register H3 |

### 8. SI-U — Uniview product fact gathered for this page

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| SI-U1 | `Uniview EC-T4F28DL IP67 datasheet operating temperature power consumption PoE` · Firecrawl search (excerpts) | https://ellipsesecurity.com/wp-content/uploads/2026/04/EC-T4F28DL.pdf ; https://cctv.net/uniview-ec-t4f28dl-unv-ec-t4f28dl-4mp-hd-smart-dual-light-fixed-turret-network-camera | EC-T4F28DL (distributor datasheet): microSD "up to 512 GB"; "IP67 protection"; "Power Consumption Max. 4.2 W"; "DC 12 V±25%, PoE (IEEE 802.3af)"; −30 °C to 60 °C. | §9 flood-footage H3 (microSD); §10 card; §10.5 H3 2 |

### 9. Pricing basis (no invented prices)

Source: `uniview-camera-installation-prices-staten-island.html`, its own pricing engine (`var BP`) and data (`var PG`, zone "Staten Island": **line 210, jbox 30, setup 180, parking 0, min_visit 675**), run in Node from my scratch script (no prices typed by hand):

| Item | Staten Island installed price |
|---|---|
| 4 × EC-T4F28DL (or EC-B4F28DL) + NVR301-04LS3-P4 + 4 TB | **$2,524** (= page's "4 Cameras from $2,524") |
| 4 × IPC3618LB-ADF28K-DL 8 MP + NVR301-04LS3-P4 + 4 TB | **$2,964** |
| 6 × EC-T4F28DL + NVR301-08LS3-P8 + 4 TB | **$3,542** |
| 8 × EC-T4F28DL + NVR301-08LS3-P8 + 4 TB | **$4,440** (30-day recording: **$4,898**) |
| 12 × EC-T4F28DL + NVR301-16B-LP8-IQ + NSW2020-6T-POE-IN + 2 × 4 TB | **$6,864** |
| 16 × EC-T4F28DL + NVR301-16B-LP8-IQ + NSW2020-10T-POE-IN + 2 × 4 TB | **$8,700** (30-day: **$9,387**) |
| Single cameras | UAC-B122-AF28M $329; EC-T4F28DL / EC-B4F28DL $449; IPC3618LB-ADF28K-DL / IPC2128LB-ADF28K-DL $559; IPC3638SS-ADF28KMC-I1 (Tri-Guard) $969; IPC6424SR-X25-VF (PTZ) $1,669; PKC2640@Z28-IR-P $1,759; IPC86CEB-AF18KC-I0 (fisheye) $2,119; list max $4,779 |
| Recorders with setup | XVR301-04G3 $359; NVR301-04LS3-P4 $499; NVR301-08LS3-P8 $619; NVR301-16B-LP8-IQ $899; NVR302-16B-P16-IQ $1,219 |
| Switches / drive / concealment | NSW2020-6T-POE-IN $119; NSW2020-10T-POE-IN $159; 4 TB drive $229; hidden in-wall wiring $200/camera |
| Service visit | $195/hr, 3-hour minimum ($585) — v2.3 §9 protected rate |

Uniview video doorbells: **not in the published Uniview list** (`D.bells` empty) → page says they are priced at the walk-through; no price shown.

**FLAGS for Anwar (pricing):** (1) the calculator's Staten Island zone carries `min_visit: 675`, while v2.3 §9 protects $195/hr with a 3-hour minimum ($585); the page publishes only $585 and avoids 1–2-camera system quotes (which the engine pads with a "3-hour minimum visit" line computed from 675). (2) The SI prices page FAQ still mentions an extended "1, 2 or 3 years" warranty that "covers the labor"; the install page uses only the one-year parts-only terms sentence.

### 10. Local findings that came back EMPTY or were not used
- Reddit thread bodies (r/statenisland): EMPTY (not accessible in build env) — excerpts only.
- Yelp 1–3★ review text for Staten Island installers: EMPTY (not accessible in build env).
- Google PAA / PASF / AI Overview / Answer the Public / Bing / DDG: EMPTY (not accessible in build env).
- Patch Staten Island camera items: none surfaced.
- Salt-air / coastal corrosion data for cameras: not researched to a source → no claim on page (also an existing silo intent).
- Field Notes: no real AESS Staten Island Uniview anecdote supplied → written as a method note, no story.
- Hylan Boulevard route, Victory Boulevard / Richmond Avenue strip-center characterizations: not sourced → removed from the page.

### 11. Images (Staten Island page)

images: 11 reused (no real Uniview job photos yet) — 6 real AESS job photos (from images/lorex-camera-installation/ ×2, images/residential-security-camera-installation/ ×1, images/dvr-upgrade/ ×1, images/video-wall-installation/ ×1, images/apartment-building-security-camera-installation/ ×1) + 5 genuine Uniview manufacturer product shots (images/uniview-*.jpg/.webp). Each checked visually; no faces, plates, house numbers or readable documents. No source file is shared with the Manhattan, Dutchess or (in-progress) Nassau Uniview pages.

| # | File (images/uniview-camera-installation/) | Source |
|---|---|---|
| 1 | uniview-camera-installation-staten-island-unv-white-video-doorbell-product-photo.webp (hero) | images/uniview-unv-video-doorbell-white.webp |
| 2 | …-wide-lens-recorder-view-of-sidewalk-and-curb.webp | residential-security-camera-installation/…-nassau-county-wide-lens-recorder-tile-of-sidewalk-and-curb.webp |
| 3 | …-white-dome-in-ceiling-corner-with-cable-loop.webp | lorex-camera-installation/lorex-camera-installation-manhattan-white-dome-camera-tucked-into-ceiling-corner.webp |
| 4 | …-unv-black-video-doorbell-product-photo.webp | images/uniview-wifi-video-doorbell.webp |
| 5 | …-turret-high-in-storage-room-corner-above-stored-boards.webp | apartment-building-security-camera-installation/…-manhattan-turret-camera-in-corner-of-storage-room.webp |
| 6 | …-camera-monitor-hung-over-deli-shelves.webp | video-wall-installation/video-wall-installation-long-island-ceiling-hung-display-over-shop-shelving.webp |
| 7 | …-small-black-camera-high-on-wall-above-lowered-ceiling.webp | lorex-camera-installation/lorex-camera-installation-long-island-small-black-camera-high-on-grey-wall-above-ceiling-lights.webp |
| 8 | …-unv-dual-lens-panoramic-dome-product-photo.webp | images/uniview-dual-lens-panoramic-dome-camera-white.jpg |
| 9 | …-unv-compact-ptz-dome-product-photo.webp | images/uniview-ptz-positioning-dome-camera-white.jpg |
| 10 | …-mini-dome-beside-louvered-light-and-air-diffuser.webp | dvr-upgrade/dvr-upgrade-queens-mini-dome-beside-light-panel-in-shop-ceiling.webp |
| 11 | …-unv-pendant-ptz-dome-product-photo.webp | images/uniview-indoor-ptz-dome-camera-white.jpg |

Note: the real AESS photo library is a small set of scenes cropped many ways; #3 (white dome in corner) and #5 (storage-room turret) are different files/framings of scenes that also appear, differently cropped, on the Nassau (flag-corner dome) and Dutchess (stained-tile corner dome) pages.

---

## Question register — staten-island

Page: `uniview-camera-installation-staten-island` (rebuilt 2026-10-18). Checked by meaning against every question on all other `uniview-camera-installation-*` pages (146 masked old-template questions), the Manhattan and Dutchess registers above, and the Nassau page as it stood on disk at ~15:10 (its 28 questions). Drafts dropped for overlapping a sibling: Saturday scheduling, deposit/payment timing, storm-door infrared glare, removal of the old system, recorder height in a flood zone, "which camera view detectives use", separate alerts for a second unit, a driveway face-shot question, "avoid recording the neighbor", hide-the-wires, a kitchen/TV display, and a neighbors-share-footage question.

### §9 Q&A (H3)
1. Does the city’s flood code say anything about where camera equipment can go in a flood-zone house?
2. If the basement floods anyway, is the footage on the recorder simply gone?
3. Our house was raised under Build It Back — how do the cameras cover the stairs and the open space under the house?
4. Each unit of our two-family has its own front door — does every door need its own camera?
5. Our tenant upstairs wants a copy of yesterday’s clip after a package went missing — how do we share it without handing over the recorder?
6. Can one recorder serve both halves of a semi-attached pair if the two owners split the cost?
7. Our house sits well above the street with a long flight of outdoor steps — how do cameras cover the steps and the sidewalk below?
8. Should a driveway camera keep its white light on all night, or stay dark until something moves?
9. Where should a driveway camera go on a high-ranch with the garage under the living room?
10. We park at the curb, not in a driveway — can a camera on the house really cover the car out past the sidewalk?
11. Burglars on Hylan and Forest went straight for the registers — where should the recorder itself be hidden in a small store?
12. Should the register camera look down at the counter or out at the customer?
13. Does New York City require an electrical permit to wire cameras into a Staten Island house?
14. We bought a house in Tottenville that came with a Uniview recorder — what should we do on day one?

### §17 FAQ (visible == FAQPage schema, 10)
1. Do both the upstairs and the downstairs households need to be home on installation day?
2. How much dust and mess does the work leave inside the house?
3. What should we do with the recorder when an evacuation order goes out for our zone?
4. After installation, can small changes such as a new login or a schedule be made without a visit?
5. Will drilling through brick on our semi-attached house disturb the neighbor's side of the wall?
6. Can a camera keep an eye on a boat or trailer parked in the side yard?
7. Do you need to log in to our home router, and what do you change there?
8. Can a camera watch the sump pump or the basement floor for water?
9. Do outdoor camera lenses need cleaning, and how often?
10. Can a camera be mounted on a fence post at the back of the yard instead of on the house?

Closest neighbors by meaning (kept, judged distinct): Q5 vs Manhattan "Police asked for a clip — how do we export it…" (sharing with a tenant vs export format for police); Q2 vs Dutchess "If the link to the barn drops for an hour, is that hour lost?" (equipment destroyed vs link outage); FAQ 3 vs Nassau "After a nor’easter, what should a Long Beach owner check…" (before evacuation vs after a storm); Q13 vs Nassau "Which license should a Nassau camera installer hold…" (NYC electrical permit vs county licensing).

Masked block similarity (my script, blocks ≥12 words, nav excluded) vs every `uniview-camera-installation-*` page incl. prices pages and the rebuilt Manhattan/Dutchess/Nassau: max 0.63 on content-free form chrome (service drop-down); all prose blocks < 0.60; the mandatory warranty sentence and SMS-consent text are identical by design (excluded by v2.3 §2). Page-level masked similarity max 0.18 (Manhattan).
