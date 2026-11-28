# Hik-Connect App Support Repair — silo research

Created 2026-10-18 by the REBUILD run for `hik-connect-app-support-repair-manhattan` (queue line: `REBUILD | hik-connect-app-support-repair-manhattan | Hik Connect App Support Repair | Manhattan | up /hik-connect-app-support-repair-nyc | (929) 560-0737 | GBP Bronx`). First page of this silo to be rebuilt; the other 15 silo pages are still the old shared template.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Tools: WebSearch (built-in), WebFetch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`), Firecrawl scrape (markdown, query mode, PDF parser) and the Firecrawl Alexandria `census-gov` provider. Shell curl is blocked. Firecrawl refuses to scrape reddit.com ("we do not support this site"), so every Reddit row is a search-result **excerpt** only. "Excerpt" = read only as a snippet.

Page section labels used below (Manhattan page): §Hero, §Quick (instant action block), §5 Neighborhood (+ §5.5 facts list), §Repair (same-day block, five checks, "what the message points to" table), §6 Services, §7 Architecture (+ §7.5 method), §8 Commercial (+ §8.5 rules list), §9 Q&A (cluster → H3), §10 Equipment (+ remote-access table, ADT/Ring/SimpliSafe table), §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ labor-only), §16 Complete services, §FieldNotes, §17 FAQ (1–10), §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every Hik-Connect page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (rows R1–R6). Threads not openable in build env. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and works from claims in forums and troubleshooting blogs (rows R1, R3, B1, H3–H5, F1–F3). |
| 6 | Area landmarks | Manhattan section, rows M-L1–M-L6. |
| 7 | Area use cases / building stock | Manhattan section, rows M-H1, M-B1–M-B3. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) — only WebSearch and Firecrawl search backends available; neither exposes Bing/DDG PAA, related or autocomplete. |
| 9 | Local news | Manhattan section rows M-N1–M-N3 (NBC New York, ABC7, NYPD 19th Pct excerpt). |
| 10 | Hyperlocal | Brick Underground (M-B2). Patch / West Side Rag / Harlem-specific camera items: EMPTY (none surfaced). |
| 11 | Yelp 1–3★ | `yelp security camera repair Manhattan "Hikvision" app remote viewing review` · Firecrawl search → only Yelp search-listing pages (Manhattan listing excerpt: "Rating 4.7(1,620)… HikVision Gold Partners") and other-state listings; no 1–3★ review text → EMPTY (not accessible in build env). Not used. |

### 1.2 Hikvision / Hik-Connect primary sources (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | `Hik-Connect for Teams Hik-ProConnect announcement Hikvision` · WebSearch → Firecrawl scrape (markdown) | https://www.hikvision.com/en/newsroom/latest-news/2023/hikvision-releases-hik-connect-for-teams/ | Oct 24, 2023: update "also known as Hik-Connect for Teams", for SMBs and multi-site (offices, chain stores, communities). Ryan Wu (Product Director): "Previously, Hik-Connect accounts only allowed one login that companies would have to share…"; "A primary admin user can now create a multi-user account containing predefined user roles". Supports video security, intercom management, access control and attendance. "Peer-to-peer (P2P) based system eliminates the need for expensive centralized servers". | §5.5 bullet 5; §6 Teams card; §9 "three shops" H3; §9 "open ports" H3; §10 intercom + access cards; §17 FAQ 4; §Sources |
| H2 | `Hikvision firmware update NVR Hik-Connect "platform access" offline DNS 8.8.8.8 support article supportusa` · Firecrawl search → scrape (PDF parser) | https://www.hikvision.com/content/dam/hikvision/en/support/faq/How-to-solve-Hik-Connect-offline-issue.pdf | "How to Solve Hik-Connect Offline Issue" V2.0, 7/12/2019: 1) check register status, enable Platform Access (NVR 3.0 / 4.0 menu paths); 2) IP/mask/gateway correct; DNS "suggested to set as 8.8.8.8 or local frequently-used DNS address"; try dev.hik-connect.com ↔ litedev.hik-connect.com; upgrade firmware; 3) ping dev.hik-connect.com; check firewall with telnet dev.hik-connect.com 8555 / litedev.hik-connect.com 8666. | §5 para 2; §6 Platform Access card; §7.5 doorman-IT paragraph; §10.5 H3 1, 2, 7; §Sources |
| H3 | same search (excerpt) → Firecrawl scrape | https://supportusa.hikvision.com/support/solutions/articles/17000129582-why-can-i-no-longer-see-my-cameras-on-my-phone- | If added by QR code/serial, "it means your Platform Access is offline". Steps: verify physically plugged in; enable Platform Access (System Configuration → Network → Advanced → Platform Access); cycle DHCP and note whether IPv4 changes; if it changes, uncheck DHCP and set DNS 8.8.8.8 / 8.8.4.4. If added by IP address "it will be an IP issue… verify the ports are still open". | §5 para 2; §Repair check 2 + table rows 1, 5; §9 "bulk internet provider" H3; §9 "open ports" H3; §10.5 H3 1; §Sources |
| H4 | `reddit Hik-Connect not working offline NVR` · WebSearch → WebFetch | https://supportusa.hikvision.com/support/solutions/articles/17000129666-i-cannot-access-my-cameras-remotely-what-are-some-possible-reasons-for-this- | Three reasons: NVR network no longer configured correctly; Platform access offline; device added via IP/Domain "will not work outside the network". | §Sources (supports §Repair table) |
| H5 | `Hikvision forgot password reset NVR export key file GUID security questions Hik-Connect reset password` · Firecrawl search (full excerpt) | https://www.hikvision.com/en/support/how-to/faq/how-to-reset-password/ | "4 Ways of Self-service Password Reset"; installers can reset via Hik-Partner Pro; Verify by Hik-Connect App (device must be added to Hik-Connect/Hik-Partner Pro account; scan QR, get code); reserved email; security questions; export XML/QR/reset string and send with device label snapshot to Hikvision support. Password Hints on some NVRs (76Q, K-series) firmware V4.75.000+. | §9 "installer registered" H3 (documented reset routes); §Sources. (Password-recovery intent itself NOT used as a question — it is in the register.) |
| H6 | `Hik-Connect app end of support older devices Hik-Connect 6 new version migrate account 2025 2026` · Firecrawl search → scrape | https://www.hik-connect.com/views/terms/newHelp/helpIos/GUID-1D25E097-8FB7-467E-A4CC-0046C57D8F6C.html | Transfer Device: transferred device becomes unavailable to the old owner; target gets "all the configuration and operation permissions"; security code sent to registered phone/email; enter target account (name/phone/email or QR); then device verification code. "The default device verification code is usually on the device label. If no verification code found, enter the device verification code you created when enabling Hik-Connect service." | §6 ownership card; §9 "installer registered" H3; §10.5 H3 5, 6; §17 FAQ 6, 7; §Sources |
| H7 | `site:hik-connect.com share device permission live view playback help` · Firecrawl search (excerpts) | https://www.hik-connect.com/views/terms/newHelp/helpIos/GUID-E898E646-D498-4B3A-BEF4-D06628BF9029.html ; https://www.hik-connect.com/views/terms/helpAndroid/Hik%20Sharing%20Device%20to%20Others.html | Share a single device to an account and choose permissions (e.g. no two-way audio); Live View, Remote Playback, PTZ as separate permissions; recipient accepts/rejects. | §5 para 3; §6 scoped-access card; §9 shareholder and doorman H3s; §17 FAQ 8; §Sources |
| H8 | `Hik-Connect Hikvision cloud data stored US servers AWS end user privacy Hik-Connect service` · Firecrawl search (excerpt) | https://www.hik-connect.com/views/terms/privacypolicy.html | Personal info stored on Hikvision-operated servers "hosted on third-party infrastructure providers, including Amazon Web Services"; "data centers in the United States, Singapore, Brazil, and Ireland"; stream-server video "will not be stored or retained"; cloud-storage video "stored in an encrypted manner". Excerpt is fragmentary. | §9 "where does Hik-Connect keep" H3; §17 FAQ 9; §Sources |
| H9 | same search as H8 (excerpt) | https://www.hikvision.com/en/products/software/hik-connect/cloud-storage-solution/ | Hikvision Cloud Storage Solution: back up and access video clips via the Hik-Connect app. | §17 FAQ 9 |
| H10 | same search as H6 (excerpt) | https://play.google.com/store/apps/details?id=com.connect.enduser | "Hik-Connect - for End User": Free; "designed to work with devices such as DVRs, NVRs, Cameras, Video intercom and Security control panels"; "Updated on Oct 10, 2026". | §9 "FCC order… app" H3; §17 FAQ 5; §Sources |
| H11 | `Hik-ProConnect installer cloud platform health monitoring remote configuration site handover owner` · Firecrawl search (excerpts) | https://www.hikvision.com/europe/products/software/hik-proconnect.html/ ; https://www.hikvision.net.my/hik-proconnect | "online device & service management platform for professional installers"; "Hand over sites and devices to the end user's Hik-Connect account by inviting site owners". | §6 installer hand-off card; §7.5 conversions; §9 "installer registered" H3; §Sources |
| H12 | `Hik-Connect device verification code "added by another account" unbind device` · Firecrawl search (excerpts) | https://www.youtube.com/watch?v=Jo2a1HuEHbU ; https://www.facebook.com/HikvisionPhilippines/posts/wondering-how-to-unbind-your-device-follow-this-simple-guide-using-the-hik-conne/722034256881873/ | Videos/posts on "device has already been added by another account" with an Unbind button; Hikvision PH post: input device user name, password and verification code. | §10.5 H3 5; §Repair table row 3 |

### 1.3 FCC / federal (F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F1 | `FCC November 2022 order prohibits authorization Hikvision Dahua equipment covered list existing equipment not affected` · Firecrawl search → scrape (query) | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment | PSHSB/OET order (DA 26-635, PS Docket 26-72), released June 26, 2026, published July 6, effective July 16, 2026 (10 days after publication): prohibits "continued importation and marketing of any covered equipment added to the Covered List in 2024 or earlier". "…does not affect the continued use or operation of previously authorized covered equipment; consumers may continue to use any device or equipment that they currently possess, if the equipment was legally purchased and maintains an existing equipment authorization." Rejected exempting "equipment that is used for spare parts, updates and replacements" — would "defeat the entire purpose of this prohibition"; rejected longer transition periods / phased implementation; rejected Hikvision's arguments. | §Hero; §5 para 4; §5.5 bullet 4; §6 keep-or-replace card; §8.5 bullet 6; §9 FCC cluster (all 4 H3s); §10.5 H3 4; §15 labor-only; §Sources |
| F2 | same search (excerpt) | https://www.fcc.gov/laboratory-division/equipment-authorization-approval-guide/equipment-authorization-system | Rules effective February 6, 2023; "prohibiting equipment authorization of any telecommunications equipment or video surveillance equipment produced by Hytera, Hikvision, or Dahua or by their subsidiaries or affiliates"; covered list producers = Huawei, ZTE, Hytera, Hikvision, Dahua. | §9 "still legal" H3 para 2; §10 replacement card ("makers not named on the Covered List"); §10.5 H3 4; §Sources |
| F3 | `FCC covered list Hikvision existing equipment owners what it means` · WebSearch → Firecrawl scrape (markdown; WebFetch returned empty) | https://www.hikvision.com/us-en/newsroom/latest-news/2026/Important-Notice-to-Our-Partners | April 7, 2026 letter (Eric Chen, President, Hikvision USA): FCC Public Notice DA 26-294 of March 27, 2026 proposing the prohibition; "the continued use or operation of any such equipment that is already in the hands of end users would not be prohibited"; Hikvision filed a petition for judicial review in December 2025; comment period to May 6, 2026; "limits on importation could affect access to replacement parts, warranty service, and technical support". | §9 "replacement" H3; §Sources |
| F4 | `CVE-2021-36260 Hikvision command injection CISA known exploited firmware update cameras` · Firecrawl search (excerpts) | https://www.cisa.gov/news-events/alerts/2021/09/28/rce-vulnerability-hikvision-cameras-cve-2021-36260 ; https://nvd.nist.gov/vuln/detail/CVE-2021-36260 | CISA alert Sept 28, 2021: review Hikvision advisory HSRC-202109-01 and apply latest firmware. NVD: "command injection vulnerability in the web server of some Hikvision product"; in CISA KEV, added January 10, 2022, due January 24, 2022. | §6 firmware card; §9 "2021 flaw" H3; §10.5 H3 7; §Sources |
| F5 | `FCC covered list…` (WebSearch, titles only) | https://ipvm.com/reports/fcc-denies-revoke ; https://dilse.it/does-the-fccs-recent-ban-impact-your-surveillance-system/ | Titles only, not opened. | Not used |

### 1.4 Reddit, forums and troubleshooting blogs (R / B) — feed §10.5
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com Hik-Connect app problem` · Firecrawl search | https://www.reddit.com/r/Hikvision/comments/1ol0orr/hikconnect_offline/ | Excerpt: "90% of Hik-connect connection issues are DNS. 5% are firewall and the other 5% are user error." | §10.5 H3 1 (quoted); §Sources |
| R2 | same | https://www.reddit.com/r/Hikvision/comments/1gcnbgu/hik_connect_not_connecting/ | Excerpt: "Whenever I get this issue is due to someone fumbling up DNS settings and Default gateway." | Background §10.5 H3 1 |
| R3 | same | https://www.reddit.com/r/Hikvision/comments/17toa2o/hikconnect_60150_ios_app_issue/ | Excerpt: "I tried deleting the app and installing it again. Lost all my settings but I set it up again. It worked but only until I left the app." | §10.5 H3 3 (quoted); §Sources |
| R4 | same | https://www.reddit.com/r/Hikvision/comments/17tirkl/hikconnect_is_riddled_with_bugs_and_possibly_the/ ; https://www.reddit.com/r/Hikvision/comments/1nl141w/playback_issues_after_updating_to_ios_26_and/ ; https://www.reddit.com/r/Hikvision/comments/1uw4uor/hikconnect_app_crashes_nvr/ | Excerpts: app "riddled with bugs"; iOS 26 timeline playback freezes; app tap "immediately crashes the NVR and it reboots". | Background only (playback/notification intents are in the register; not used as questions) |
| R5 | `Hik-Connect app end of support…` · Firecrawl search | https://www.reddit.com/r/Hikvision/comments/18krw8j/did_hikconnect_leave_older_devices_in_the_dust/ | Excerpt: "Manual adding adds it to just the app, not your hik-connect account." | Background §Repair table row 5 |
| R6 | `site:reddit.com Hik-Connect…` | https://www.reddit.com/r/Hikvision/comments/1eldy2g/hard_reset_hikvision_nvr/ | Excerpt (via H5 search): use SADP "forgot password" to download the device code file. | Background (HowTo tool line) |
| B1 | `Hik-Connect device offline error fix P2P` · WebSearch → WebFetch | https://securitycamcenter.com/hik-connect-offline-0x2002/ | 0x2002 in Platform Access "indicates that the P2P function is not working properly"; fixes: DHCP + DNS 8.8.8.8/8.8.4.4 + toggle Platform Access; one account per user; firmware (warns wrong file can brick); change six-letter verification code; check internet. | §Repair table row 2; §10.5 H3 2, 6, 7; §Sources |
| B2 | same WebSearch (titles) | https://learncctv.com/?p=28959 ; https://securitycamcenter.com/hikvision-error-offline0x1001/ ; …0x1007 | Titles for offline codes 0x1001, 0x1007, 0xe0000105. Not opened. | Not used |

### 1.5 Keyword plan (five layers, silo)
- **Service:** Hik-Connect app support, Hik-Connect repair, Hik-Connect offline fix, Hik-Connect setup, Hik-Connect for Teams setup, Hikvision NVR remote viewing, Hik-Connect device transfer, unbind Hikvision device, Hikvision firmware update.
- **Problem:** device offline, Platform Access offline, error 0x2002, added by another account, installer holds the account, lost verification code, managing agent change, new internet provider, Wi-Fi camera dropping, port forwarding exposure, CVE-2021-36260, FCC Covered List / import ban, replacement parts unavailable.
- **Technology:** P2P, Platform Access, DNS 8.8.8.8, DHCP, reserved IP, VLAN, firewall outbound ports, VPN, verification code, SADP, Hik-ProConnect / Hik-Partner Pro, Turbo HD DVR, NVR, video intercom, cloud storage.
- **Industry:** co-op boards, condo boards, managing agents, supers, doorman desks, walk-up owners, conversions/developers, retail stores, multi-store owners, office tenants, medical suites.
- **Geographic (Manhattan page):** Manhattan; Upper West Side, West End Avenue, Riverside Drive, Upper East Side, Yorkville, Morningside Heights, Harlem/125th Street, East Harlem, Washington Heights, Inwood, Hell's Kitchen, Ninth Avenue, Madison Avenue, Midtown East/Grand Central, SoHo, Tribeca, NoHo, Financial District/25 Water Street, Civic Center/375 Pearl Street, Battery Park City, Chelsea, Flatiron, East Village, Lower East Side, Greenwich Village, Roosevelt Island.

### 1.6 Silo pricing (no invented prices) — FLAG
The 16 existing Hik-Connect pages publish **no dollar prices** (only "$0 Diagnosis by Phone" in the stats bar and "a likely range by phone" in the old FAQ). The Manhattan page therefore uses only:
- $0 phone diagnosis (existing silo statement);
- the protected service rate $195/hr, 3-hr minimum ($585) (blueprint v2.3 §9, kept verbatim, not multiplied — same as the rebuilt DVR pages);
- recorder replacement = DVR Upgrade silo base prices (research/dvr-upgrade.md §1.8: 4-ch $450–$700, 8-ch $650–$1,000, 8-ch hybrid $800–$1,200, 16-ch $1,200–$2,200, 32-ch $2,200+) × Manhattan 1.25 → $563–$875, $813–$1,250, $1,000–$1,500, $1,500–$2,750, $2,750+ (identical to dvr-upgrade-westchester, also 1.25×).
FLAG for Anwar: confirm the Hik-Connect silo should borrow DVR recorder-replacement prices, and whether the $195/hr rate should carry the Manhattan multiplier.

---

## Question register — every question on every Hik-Connect App Support Repair page

Rule (v2.3 §12.3, DAILY-RUN step 2): no FAQ/Q&A question on a new or rebuilt page may repeat an intent listed here. Generated 2026-10-18 from the live HTML of all 16 silo pages (question-form H2/H3/summary headings + .faq-question items + FAQPage `Question` names, same parser as tools/check_page.py). All 15 old-template pages carry the same ten intents: Hik-Connect a camera brand? · why "device offline"? · Hik-Connect vs Guarding Vision · can't see live view or playback · recover Hik-Connect password · push notifications not working · fix systems you didn't install · how much does repair cost · what areas do you cover (+ the "Offline Right Now?" banner heading). The rebuilt Manhattan page avoids all ten intents.

### hik-connect-app-support-repair-manhattan — REBUILT 2026-10-18 (this run)
**Q&A / question headings (H2/H3 ending in “?”):**
- The installer registered our building’s recorder to his own email — how do we get it back?
- Our managing agent changed — how do we make sure the old firm’s phones no longer see the lobby?
- A shareholder wants app access to the hallway camera outside her door — what can the board safely give?
- Can the overnight doorman see live video without being able to export or delete clips?
- Management switched the building to a new bulk internet provider and every camera went grey in the app — what changed?
- Does a recorder in the super’s basement office need its own internet line, or can it share the building’s?
- Why does a Wi-Fi camera that worked in the showroom drop out once it’s mounted in our pre-war apartment?
- Do we need to open ports on the router for Hik-Connect to work?
- Is it still legal to keep using our Hikvision cameras in Manhattan after the 2026 FCC order?
- Can we still get replacement Hikvision cameras and recorders for a repair?
- Does the FCC order say anything about whether the Hik-Connect app keeps working?
- The board wants to replace everything with another brand — what happens to the footage on the old Hikvision recorder?
- How do we know whether our recorder’s firmware has the 2021 flaw CISA warned about?
- Is it safer to view cameras through Hik-Connect or through a VPN back to the building?
- Where does Hik-Connect actually keep our account information?
- We run three shops below 96th Street — can one owner see all three without sharing a password with each manager?
- Our store is on 125th Street and joined the NYPD camera-sharing pilot — does that change anything in Hik-Connect?
- Will a clip sent from the app hold up for an insurance claim, or do we need the original from the recorder?
- What does the super need to have ready before your technician arrives?
- Can you do the work without going into any apartment?
**FAQ (= FAQPage):**
- What should a Manhattan co-op put in its camera-access policy before handing out app logins?
- How many days of footage should a doorman building keep on its recorder?
- Who has to approve the work before you touch a co-op’s recorder?
- Can Hik-Connect ring the lobby door station on phones as well as show the cameras?
- Is the Hik-Connect app itself free to use?
- Which details from the recorder’s label should we send before the visit?
- If we sell the building or the store, how does the camera account pass to the buyer?
- Can the system be set so it never records sound?
- Can footage be saved to the cloud instead of only the basement recorder?
- How long does a typical Hik-Connect repair visit take in a Manhattan building?

### hik-connect-app-support-repair-bronx — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-brooklyn — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-dutchess-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-hudson-valley — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-long-island — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-manhattan — old template (pre-rebuild; replaced by the rebuild above)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-nassau-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-nyc — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-orange-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-putnam-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-queens — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-rockland-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-staten-island — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-suffolk-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-ulster-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?

### hik-connect-app-support-repair-westchester-county — old template (pre-rebuild)
**Q&A / question headings:**
- 🔧 Hik-Connect Offline Right Now?
- Is Hik-Connect a camera brand?
- Why does Hik-Connect say “device offline”?
- What’s the difference between Hik-Connect and Guarding Vision?
- Why can’t I see live view or playback?
- Can you recover my Hik-Connect password?
- Why aren’t my push notifications working?
- Do you fix Hik-Connect systems you didn’t install?
- How much does Hik-Connect repair cost?
- What areas do you cover?
**FAQ (.faq-question / FAQPage schema):**
- (schema only) Is Hik-Connect a camera brand?
- (schema only) Why does Hik-Connect say device offline?
- (schema only) What is the difference between Hik-Connect and Guarding Vision?
- (schema only) Why can't I see live view or playback in Hik-Connect?
- (schema only) Can you recover my Hik-Connect password?
- (schema only) Why aren't my Hik-Connect push notifications working?
- (schema only) Do you fix Hik-Connect systems you didn't install?
- (schema only) How much does Hik-Connect repair cost?
- (schema only) What areas do you cover?


---

## Manhattan

Page: `hik-connect-app-support-repair-manhattan` (REBUILD in place, 2026-10-18). Up-link `/hik-connect-app-support-repair-nyc`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (929) 560-0737 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from the hub and the other boroughs):** in Manhattan a Hik-Connect failure is usually a problem of ownership and network control in shared buildings — whose account the recorder is bound to (installer, old managing agent, developer), whose internet it sits behind (bulk provider, building IT firewall, owner's residential line), and who should see what (board, agent, super, desk, shareholders, store managers) — and since July 16, 2026 every repair also carries a keep-or-replace decision because new Hikvision equipment can no longer be imported or marketed.

### Building stock / tenure (M-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-H1 | Firecrawl Alexandria `census-gov` census/data · acs/acs5 vintage 2023 · B25035_001E, B25001_001E, B25024_002E–009E, B25034_010E–011E, B25003_002E–003E · county 061 state 36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36061 | New York County: 918,806 housing units; median year built **1951**; built 1939 or earlier **392,000**; 1940–49 59,700; 1-unit detached 10,012; 1-unit attached 6,713; 2-unit 7,530; 3–4 18,687; 5–9 50,467; 10–19 99,713; 20–49 **201,967**; 50+ **522,823**; owner-occupied 191,643; renter-occupied **583,733** (≈75%). | §5 para 1; §5.5 bullets 1–3; §Sources |

### Buildings, boards, footage access (M-B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-B1 | `reddit AskNYC building security cameras super access footage app co-op` · Firecrawl search → scrape (query) | https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops/ | FirstService Residential, Sept 23, 2024: boards may review footage but usually delegate to property manager / resident manager; written access policy; requests to the property manager with reason, timeframe, cameras; log of requests and viewers; footage "generally stored for 30 to 90 days"; residents no access/copies without board and legal approval; Labor Law §203-c (no recording in restrooms, locker rooms, changing areas); audio may be unlawful eavesdropping §250.05 (page text says "labor law" — we cite Penal Law). | §5 para 3; §8.5 bullets 1–2; §9 shareholder H3; §9 "replace everything" H3; §17 FAQ 1, 2; §Sources |
| M-B2 | same search → scrape (query) | https://www.brickunderground.com/blog/2014/06/ask_an_expert_security_camera | Brick Underground (2014 article, refreshed image 2023): access usually restricted to security firm, property manager, on-site super (Dean Roberts); resident requests "usually … not approved unless it's approved by the board specifically, on a case-by-case basis" (Mark Levine); cameras must not point specifically at certain doors. | §9 shareholder H3; §Sources |
| M-B3 | same search (excerpts) | https://www.reddit.com/r/AskNYC/comments/1b3jo5u/coop_security_camera_recs/ ; https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ ; https://www.reddit.com/r/AskNYC/comments/1gjhqzk/is_it_legal_for_a_tenant_in_a_condo_building_to/ | Excerpts: "The issue is where are the recordings going"; building worker: "only the super has access to the cameras to rewind and look back while I only have access to the live feed"; tenant asking whether a condo tenant may record lobby/common areas. | Background for §9 doorman H3 (desk = live only) and shareholder H3; not quoted |
| M-B4 | Carried from research/fiber-optic-installation.md §Manhattan (Firecrawl, 2026-10-15) | https://www.reddit.com/r/NYCapartments/comments/1qjxeao/anyone_else_struggle_with_wifi_in_prewar_railroad/ | Excerpt: poster in "a pre-war NYC railroad-style two bedroom apartment" with "ongoing WiFi issues". | §9 Wi-Fi H3 (quoted as excerpt); §Sources |
| M-B5 | Carried from research/fiber-optic-installation.md §Manhattan | https://villagepreservation.org/2024/08/14/the-soho-cast-iron-historic-district-a-1973-designation-that-helped-shape-nycs-cultural-legacy/ | SoHo-Cast Iron Historic District, 1973, "approximately 26 blocks, covering nearly 500 buildings" (excerpt). | §7 loft card; §13 card; §Sources |
| M-B6 | Carried from research/fiber-optic-installation.md §Manhattan | https://comptroller.nyc.gov/reports/office-to-residential-conversions-in-nyc-economics-and-fiscal-estimates/ ; https://www.archpaper.com/2025/12/soma-25-water-street-cetraruddy-office-to-residential-conversion/ | 44 conversions, ~17,400 apartments (Comptroller, July 2025); 25 Water Street 1,320 units, largest O2R in the US (Arch Paper, Dec 2025). | §7 conversion card; §8 FiDi card; §13 card; §Sources |
| M-B7 | Carried from research/dvr-upgrade.md L1 (LPC Permit Guidebook ch. 11) | https://nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook%20_Chapter11_HealthSafety.pdf | Staff-level approval for security cameras: well spaced, discreet placement, attach at mortar joints / plain masonry not decorative surfaces, minimal painted conduit. | §7 loft card; §7.5 lofts paragraph; §8.5 bullet 3; §Sources |

### Local news / police / city programs (M-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-N1 | `Manhattan package theft lobby doorman building NYPD 2025 2026 surveillance footage` · Firecrawl search → scrape (query) | https://www.nbcnewyork.com/news/local/impostor-fresh-direct-deliveryman-stolen-packages-upper-west-side-nyc-apartment-lobbies-nypd/1571533/ | March 15, 2018: man in a Fresh Direct coat took packages from lobbies of at least three Upper West Side buildings; NYPD released surveillance video. | §5 para 3; §13 UWS card; §Sources |
| M-N2 | same search (excerpt) | https://www.facebook.com/NYPD19pct/posts/having-a-package-delivered-to-your-home-not-going-to-be-home-there-are-thieves-o/1186393103591192/ | NYPD 19th Precinct (Upper East Side): "officers made 3 separate arrests of persons stealing unattended packages from buildings vestibules/lobbies". Date not in excerpt → no date on page. | §5 para 3; §8 UES card; §Sources |
| M-N3 | same search → scrape (query) | https://abc7ny.com/post/nyc-retail-theft-program-mayor-eric-adams-nypd-launch-innovative-technology-initiative-to-combat/14827113/ | May 16, 2024: pilot letting businesses voluntarily share real-time CCTV with NYPD via a box by Fusus by Axon; "still at the behest or the control of the business owner"; "Along 125th Street, businesses big and small are now invited to enroll"; Mushtari Hardware on 125th Street; 125th Street BID. | §5.5 bullet 6; §8 125th St card; §8.5 bullet 5; §9 125th Street H3; §13 card; §Sources |
| M-N4 | same search (excerpt) | https://www.facebook.com/pix11news/videos/a-nyc-resident-has-one-message-for-a-woman-caught-stealing-packages-from-her-lob/1762517254595906/ | PIX11, Jan 31, 2025: NYC resident on a woman caught stealing packages from her lobby (borough not in excerpt). | Not used (borough unknown) |

### ISP / Wi-Fi / NAT in dense buildings (M-I)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-I1 | `carrier-grade NAT CGNAT security camera remote access P2P Spectrum Verizon NYC apartment` · Firecrawl search (excerpts) | https://www.compareinternet.com/blog/t-mobile-home-internet-port-forwarding/ ; https://www.reddit.com/r/Spectrum/comments/1mtpqgx/spectrum_uses_cgnat/ | Cameras relying on port forwarding need a public IP that CGNAT doesn't allow (5G home internet); Reddit excerpt contradictory on whether Spectrum uses CGNAT. | Background for §9 "open ports" H3 (P2P avoids inbound ports). No ISP-specific CGNAT claim made on the page. |
| M-I2 | Carried from research/fiber-optic-installation.md §Manhattan | https://www.reddit.com/r/AskNYC/comments/9ezss5/no_internet_providers_will_set_up_in_my_building/ | Excerpt: ask the super/landlord who services the building; some buildings single-provider. | Background for §5 para 2 / §9 bulk-provider H3 |
| M-I3 | Big Apple Connect / NYCHA, bulk internet contracts | — | EMPTY (not researched to a source this run) → page says "bulk internet contract" generically, names no program. | — |

### Landmarks / corridors (M-L)
| # | Source | Finding | Used |
|---|---|---|---|
| M-L1 | M-N3 (ABC7) | 125th Street BID / pilot. Frederick Douglass and Adam Clayton Powell Jr. Boulevards named as streets only (no claim). | §13 card 1 |
| M-L2 | M-N1 (NBC) | Upper West Side lobbies; West End Avenue / Riverside Drive named as streets only. | §13 card 2 |
| M-L3 | Carried from research/fiber-optic-installation.md: https://www.nyc.gov/content/planning/pages/our-work/plans/manhattan/greater-east-midtown ; https://en.wikipedia.org/wiki/One_Vanderbilt | One Vanderbilt built under the Greater East Midtown framework; topped out at 1,401 feet. 2017 rezoning (fiber research). | §8 Midtown card; §13 card 3 |
| M-L4 | M-B5 | SoHo-Cast Iron Historic District. | §13 card 4 |
| M-L5 | M-B6 | 25 Water Street. | §13 card 5 |
| M-L6 | Carried from research/fiber-optic-installation.md: https://en.wikipedia.org/wiki/375_Pearl_Street | 32 stories, built for New York Telephone, completed 1975, Manhattan end of Brooklyn Bridge, redeveloped as data center. | §13 card 6 |
| M-L7 | Avison Young Q2 2026 (carried, fiber research) | Class B 45% / Class C 30% of Manhattan office inventory. | Background for §8 Midtown card ("older Class B buildings"); figure not printed |

### Licensing / permits (Manhattan)
- NYS low-voltage licence #12000287431 (AESS, protected).
- No NYC permit applies to reconfiguring an existing recorder or app account; LPC rules (M-B7) only when exterior cameras on designated buildings are moved or added. NYC DOB rules for low-voltage camera work: EMPTY (not researched to a primary source) → page makes no DOB claim.
- Labor Law §203-c and Penal Law §250.05 via M-B1 and research/dvr-upgrade.md G3; NYS Commercial Security Tax Credit via research/dvr-upgrade.md G4.

### House practices stated on the page without an external source (FLAG for Anwar)
- Two-hour arrival windows, seven days to 8 PM; "most systems back in the app within one to two hours of arrival" (copied from live silo/blueprint wording).
- Certificates of insurance for managing agents on request.
- Hand-over "system sheet" (account, verification code, shares, router port, ISP contact); role mailbox for building-owned accounts; VPN as fallback; VLAN/segment for recorders; audio off by default.
- "Most visits fit inside the three-hour minimum"; Field Notes is a method note, not an anecdote.
- Phone apps commonly show a lower-resolution stream / recorder export keeps full recording (general technical statement, hedged on page).
- ADT / Ring / SimpliSafe comparison is qualitative (they sell their own ecosystems); no pricing or capability claims about them.

### Images (11) — Drive "AESS Website Photos" has no Hik-Connect folder; CompanyCam not connected (per coordinator)
Permanent image rule: 9 real AESS job photos from other jobs in `images/` (re-cropped to remove signs, text, logos, address numbers, people, documents) + 2 Hikvision manufacturer product shots. Every crop viewed with the Read tool before captioning. Captions say "Real AESS job photo" / "Manufacturer product photo, not an installed unit"; none claims a Manhattan customer or building.
| Output (images/hik-connect-app-support-repair/) | Source | Crop | Placement |
|---|---|---|---|
| …-manhattan-hikvision-nvr-with-silver-front-trim-product-photo.webp | images/nvr-hikvision-ds7616ni.png | (0,185,500,305) | Hero (eager) |
| …-manhattan-dome-camera-on-wall-arm-on-stone-facade.webp | images/manhattan-deli-exterior.jpeg | (0,150,222,420): address digits, sign, people, subway sign removed | §5 |
| …-manhattan-store-monitor-showing-multi-camera-layout.webp | images/manhattan-deli-monitor.jpeg | (440,165,950,525) screen only; figures in tiles too small to identify | §6 |
| …-manhattan-mini-dome-cameras-in-shop-drop-ceiling.webp | images/manhattan-deli-interior-cameras.jpeg | (250,60,1230,430) ceiling only; people and menu boards removed | §7 |
| …-manhattan-white-turret-camera-under-yellow-fascia.webp | images/manhattan-deli-exterior-camera.jpeg | (560,295,1000,600) below sign lettering | §8 |
| …-manhattan-camera-tile-of-brick-wall-and-paved-lot.webp | images/nassau-window-depot-monitor.jpeg | (700,145,1240,440) one tile; date stamp, address number, people removed | §9 |
| …-manhattan-hikvision-wifi-dome-camera-with-antennas-product-photo.webp | images/hikvision-wifi-wireless-dome-camera.jpg | full product shot | §10 |
| …-manhattan-recorder-screen-channel-bitrate-table.webp | images/rockland-toyota-nvr-monitor.jpeg | (255,615,1085,795) table only; monitor brand logo and live tiles removed | §10 |
| …-manhattan-network-cables-bundled-along-ceiling-pipe.webp | images/rockland-toyota-nvr-monitor.jpeg | (0,0,600,320) ceiling cables | §12 |
| …-manhattan-black-bullet-camera-at-corridor-ceiling-near-door.webp | images/rockland-toyota-hallway-camera.jpeg | (150,0,935,700) above the warranty poster/QR code | §13 |
| …-manhattan-white-dome-camera-in-storeroom-corner.webp | images/nassau-window-depot-storage-camera.jpeg | (0,0,935,720) above box labels | §14 |
All WebP quality 80, ≤1600 px. Alt/title unique, each containing "Manhattan". Note: the rockland-toyota-nvr-monitor source is used twice (two different crops, two different files).

### Build notes
- check_page.py: all page-level checks pass; the only failures are wiring owned by the main run — 15 live siblings don't yet link back to /hik-connect-app-support-repair-manhattan and the NYC hub doesn't link down (old template pages have no silo cross-links at all). In a scratch copy with one back-link added to each sibling, `check_page.py --root <copy>` prints PASS.
- 12,626 rendered words; title 45; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; HowTo 7 = process 7; 187,586 B (siblings ~117 KB).
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word-level SequenceMatcher, nav excluded) vs all 15 silo pages: max **0.375**.
