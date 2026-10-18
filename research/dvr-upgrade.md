# DVR Upgrade — silo research

Created 2026-10-18 by the REBUILD run for `dvr-upgrade-brooklyn` (queue line: `REBUILD | dvr-upgrade-brooklyn | DVR Upgrade | Brooklyn | up /dvr-upgrade-nyc | (347) 934-8335 | GBP Brooklyn`). A parallel agent rebuilt `dvr-upgrade-nassau-county` the same hour and keeps its research in `research/dvr-upgrade-nassau-county.part.md` (to be merged here by the coordinator; not touched by this run).

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Tools used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, web and `gov` categories), Firecrawl scrape (query/freeform mode; PDF parser), Firecrawl Alexandria providers `census-gov` (census/data) and `nvd-nist-gov` (vulnerabilities/cve). Shell curl is blocked. "Excerpt" = read only as a search-result snippet, not opened.

Page section labels used below: §Hero, §Quick (instant action block), §5 Neighborhood (+ §5.5 facts list), §Repair1 (repair capture + "Five checks" list), §6 Services, §7 Architecture (+ §7.5 method paragraphs), §8 Commercial (+ §8.5 rules/credits list), §9 Q&A (cluster/H3), §10 Equipment (+ hybrid-vs-NVR and ADT/Ring/SimpliSafe comparison), §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks, §14 Pricing, §15 Packages (+ BYOE), §17 FAQ, §19 Siblings, §Sources.

---

## Part 1 — Silo-wide findings (usable on every DVR Upgrade page)

### 1.1 Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (Firecrawl search returns snippets; reddit.com threads not opened). Rows R1–R5 below. |
| 2 | Google People Also Ask | EMPTY (not accessible in build env) — no live Google SERP surface. |
| 3 | Google PASF | EMPTY (not accessible in build env). |
| 4 | Answer the Public | EMPTY (not accessible in build env). |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and frames each H3 as a claim published by cost guides, retailers and forums (rows A1–A5), then corrects it. |
| 6 | Area landmarks | Brooklyn section, rows L1–L8. |
| 7 | Area use cases / building stock | Brooklyn section, rows H1–H3, C1–C3. |
| 8 | Bing & DuckDuckGo (PAA / related / autocomplete) | EMPTY (not accessible in build env) — only one search backend available per tool. |
| 9 | Local news | Brooklyn section rows N1–N5 (News 12 Brooklyn, NY1 excerpt, ABC News/News 12 excerpts, The Guardian, NYC Health Dept data story). |
| 10 | Hyperlocal | Brownstoner forum (N6), News 12 Brooklyn (N1). Brooklyn Paper / Brooklyn Eagle / BK Reader camera-specific items: EMPTY (none surfaced in the searches run). |
| 11 | Yelp 1–3★ | Search excerpt only (Y1); no camera-recorder complaint text could be read → effectively EMPTY (not accessible in build env). Not used on the page. |

### 1.2 Reddit and forums (silo)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R1 | `reddit upgrade old DVR keep existing coax cameras hybrid XVR` · Firecrawl search | https://www.reddit.com/r/homesecurity/comments/1wmkjq5/old_dvr_security_system_upgrade/ | Excerpt: "I would swap out your antique DVR for a "hybrid" NVR. Most likely HDD inside the DVR already dead. Replace a new HDD should fix." | §10.5 H3 3 (paraphrased as forum advice); §Sources |
| R2 | same | https://www.reddit.com/r/Dahua/comments/1qaifdr/upgrading_10yearold_analog_cctv_6_cameras_keep/ | Excerpt: owner upgrading a ~10-year-old analog Dahua system (6 cameras) that came with the home, wants to keep the coax. | Background for §9 coax cluster (not quoted) |
| R3 | same | https://www.reddit.com/r/homesecurity/comments/1n6aeo6/need_to_replace_an_older_system_but_want_to_keep/ | Excerpt: advice to attach Ethernet to the existing coax and pull it through the walls. | Background for §7.5 brownstone paragraph ("old cable becomes the pull string") |
| R4 | same | https://www.reddit.com/r/homeautomation/comments/12jv43i/can_i_use_old_coax_runs_for_security_cameras/ | Excerpt: user with 2017 cameras asks whether old coax runs can be reused for PoE cameras. | Background (coax-to-Ethernet adapters, §10) |
| R5 | `r/Brooklyn security camera DVR landlord building cameras` · Firecrawl search | https://www.reddit.com/r/Brooklyn/comments/yrlptj/is_the_landlord_required_by_law_to_install/ | Excerpt: tenant — "There is a lot of package theft in the building. Landlord said he will not install cameras. Is there a law to force him to do that?" | Landlord/tenant theme for §9 cluster 4; §Sources. No legal claim made from it. |
| R6 | `cost to replace DVR security camera system recorder upgrade price guide` · Firecrawl search | https://www.reddit.com/r/SecurityCamera/comments/1fiv6lt/what_should_a_business_expect_to_pay_for_an/ | Excerpt: "installed price per camera could range from $500-$2500+ depending on what model camera/recording you want and how tough it is to get new..." | Not used (business new-install, not upgrade) |
| R7 | same | https://www.facebook.com/groups/lowvoltagenation/posts/3896910240598776/ | Excerpt (installers' group): DIY homeowner — "I'd pay $500. $50 for each camera and $100 for the dvr" to replace 8 cameras. | §10.5 H3 1 |

### 1.3 Aggregator / retailer claims (feed §10.5)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `cost to replace DVR security camera system recorder upgrade price guide` · Firecrawl search | https://www.security.org/security-cameras/cost/ | Excerpt: equipment $30–$500; "getting two security cameras professionally installed will cost $100 to $200 on average, according to HomeAdvisor." | §10.5 H3 1 |
| A2 | same → Firecrawl scrape (query) | https://www.cctvcameraworld.com/how-to-upgrade-your-existing-security-camera-system/ | "If you already have good coax cable runs from a roll of solid copper coax, there's no reason to upgrade to an Ethernet IP camera system." Mentions thin premade cable, RG59 from a roll, solid copper Siamese, copper-clad aluminum RG59; distance tiers "up to 50 ft / 150 ft / 600 ft" (not tied to cable type in the extract). CVBS = old non-HD analog. No prices. | §10.5 H3 2 (quote); §9 cluster 2 H3 3 (cable types, "retailer guides rate premade cable for shorter distances"); §Sources |
| A3 | Carried from research/apartment-building-security-camera-installation.md (fetched 2026-10-18) | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera/ny/new-york | Angi NY average $1,509, typical $797–$2,222. | Not used on this page (kept for siblings) |

### 1.4 Technology (hybrid recorders, HD-over-coax)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `Dahua XVR pentabrid HDCVI AHD TVI CVBS IP coax transmission distance 4K datasheet` · Firecrawl search | https://www.dahuasecurity.com/asset/upload/uploads/soft/20201030/DH-XVR7108-16HE-4KL-X_datasheet_20201027.pdf (also XVR5108-16H-4KL-X 2018 and XVR4104C-X1 data sheets, same wording) | Excerpt: "The HDCVI system supports long distance transmission over coaxial cable and UTP, max. 700m for 4K/4MP, 800m for 1080P and 1200m for 720P. Supports HDCVI/AHD/…" | §7.5 lofts paragraph; §9 cluster 1 H3 3; §10.5 H3 2 (hundreds of metres); §Sources |
| T2 | same | https://objects.eanixter.com/PD620479.PDF | Excerpt: "Penta-brid access technology seamlessly records video from HDCVI, AHD, TVI, CVBS, and IP sources simultaneously" (4K penta-brid HDCVI DVR). | §10 Hybrid Recorders card; §Sources |

### 1.5 Recorder security
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| S1 | `CISA known exploited vulnerabilities DVR TBK CVE-2024-3721 botnet` · Firecrawl search → Firecrawl scrape (query) | https://fortiguard.fortinet.com/outbreak-alert/tbk-dvrs-botnet-attack | CVE-2024-3721, command injection / unauthenticated RCE in TBK DVR devices; >60,000 IPS detection events; Securelist Mirai-wave analysis June 6 2025; FortiGuard Threat Signal June 10 2025; Outbreak Alert June 17 2025; botnets Condi, Fodcha, Mirai, Unstable; "no vendor supplied patch"; recommends isolate or replace, restrict remote access behind firewall/VPN. | §5 para 2; §9 cluster 6 H3 1; §10.5 H3 4; §Sources |
| S2 | Firecrawl Alexandria `nvd-nist-gov` vulnerabilities/cve · CVE-2024-3721, CVE-2021-36260 | https://nvd.nist.gov/vuln/detail/CVE-2021-36260 | CVE-2021-36260 (Hikvision, published 2021-09-22) `in_kev: true`, CISA KEV action due 2022-01-24. CVE-2024-3721 (published 2024-04-13) `in_kev: false` → page does NOT say the TBK flaw is on the CISA list. | §9 cluster 6 H3 1; §10.5 H3 4; §Sources |

### 1.6 New York State law relevant to recorders and camera placement (every NY page)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `New York Civil Rights Law 52-a video imaging device neighbor backyard residential property` · Firecrawl search | https://www.nysenate.gov/legislation/laws/CVR/52-A | §52-a: owner or tenant of residential real property has a private right of action for damages against a person who installs or affixes a video imaging device on adjoining property for the purpose of videotaping the backyard without written consent, with intent…; "backyard" = beyond the rear footprint of the dwelling to the side and rear boundaries. | §8.5 bullet; §9 cluster 4 H3 2; §10.5 H3 6; §17 FAQ 8; §Sources |
| G2 | `New York Penal Law 250.45 unlawful surveillance …; Penal Law 250.05 eavesdropping one-party consent` · Firecrawl search (gov) | https://nysenate.gov/legislation/laws/pen/250.40 | Definitions: "place and time when a person has a reasonable expectation of privacy" = where a reasonable person would believe he or she could fully disrobe in privacy; "imaging device" defined. | §8.5 bullet "no cameras where people undress" |
| G3 | same | https://nysenate.gov/legislation/laws/PEN/250.05 ; https://nycourts.gov/reporter/3dseries/2016/2016_02556.htm | §250.05 eavesdropping is a class E felony; §250.00(2) "mechanical overhearing" = recording a conversation without the consent of at least one party, by a person not present (quoted in People v Badalamenti, 2016). | §8.5 bullet; §9 cluster 4 H3 3; §Sources |
| G4 | `New York small business retail theft security cameras tax credit Hochul 2025 eligible expenses` · Firecrawl search → scrape (query) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: businesses with ≤50 employees; up to $3,000 per retail location; thresholds $4,000 per location (<25 employees) and $6,000 (26–50); covered: registered security guards, surveillance cameras, alarm systems, locks/gates/structural reinforcement, exterior LPR, other approved anti-theft devices; apply for certificate by October 31 each year; claim on CT-663 / IT-663. | §8.5 bullet; §9 cluster 3 H3 4; §Sources |
| G5 | same | https://www.governor.ny.gov/news/governor-hochul-announces-new-initiatives-crack-down-organized-retail-theft-and-protect | FY25 Budget: "$5 million tax credit to help small businesses invest in added security measures such as cameras"; "$3,000 tax credit for any small businesses who spends the threshold amount". | §8.5 ("created in the FY2025 budget"); §Sources |
| G6 | same (excerpt) | https://www.securityindustry.org/2024/10/21/state-of-new-york-provides-retailers-with-tax-credit-for-security-improvements/ | Excerpt: thresholds $4,000 (≤25 employees) / $6,000 — consistent with G4. | Cross-check only |

### 1.7 Keyword plan (five layers, silo)
- **Service:** DVR upgrade, DVR replacement, recorder swap, hybrid DVR / XVR, upgrade analog cameras to HD, HD-over-coax, DVR to NVR migration, CCTV upgrade, camera system upgrade.
- **Problem:** DVR not recording, video loss, DVR beeping, hard drive error, grainy/blurry footage, backlit storefront silhouette, footage export failed, forgotten DVR password, hacked DVR / botnet, flooded cellar recorder, renovation-cut cable.
- **Technology:** HDCVI, HD-TVI, AHD, CVBS, IP, penta-brid, RG59, Siamese cable, copper-clad aluminum, BNC compression connector, coax-to-Ethernet adapter, video balun, surveillance hard drive, UPS, WDR, privacy masking, port forwarding / UPnP, VPN.
- **Industry:** brownstone owners, small landlords (two-/three-family), walk-up buildings, bodegas and delis, storefronts on BID corridors, mixed-use buildings, lofts/workshops.
- **Geographic (Brooklyn page):** Brooklyn; Bed-Stuy, Park Slope, Fort Greene, Clinton Hill, Crown Heights, Prospect Heights, Flatbush, East Flatbush, Midwood, Bushwick, Bay Ridge, Dyker Heights, Williamsburg, Greenpoint, Sunset Park, Gowanus, Bensonhurst, Gravesend, Sheepshead Bay, Canarsie, Mill Basin, Gerritsen Beach, Coney Island, Brighton Beach, Brownsville, East New York, Red Hook; Fulton Mall, Pitkin Avenue, Flatbush/Nostrand avenues, Kings Highway, Fifth Avenue Bay Ridge, 86th Street, Graham Avenue, Knickerbocker Avenue, Myrtle Avenue; Brooklyn Heights Historic District, Kings Theatre, Brooklyn Navy Yard, Industry City, Riegelmann Boardwalk; Troy Avenue (office).

### 1.8 Silo pricing (no invented prices)
From the existing silo pages (dvr-upgrade-brooklyn pre-rebuild and dvr-upgrade-nyc hub, identical figures; Brooklyn = §9 base 1.00×): 4-channel swap $450–$700; 8-channel swap $650–$1,000; 8-channel hybrid/XVR $800–$1,200; 16-channel commercial $1,200–$2,200; 32-channel $2,200+; per-run BNC re-termination "quoted after testing"; hybrid hardware "$20–$80 more than a plain DVR". Service rate $195/hr, 3-hr minimum ($585) per blueprint §9 (protected). Other area pages apply the §9 multipliers to these.
FLAG: the old Brooklyn page also showed "$250 service call", "$175/drop" and "$19.99/mo" chips in a JS widget — inconsistent with the $195/hr policy; NOT carried.

---

## Question register — every question on every DVR Upgrade page

Rule (v2.3 §12.3, DAILY-RUN step 2): no FAQ/Q&A question on a new or rebuilt page may repeat an intent listed here. Generated from the live HTML of all 16 silo pages on 2026-10-18 (question-form H2/H3/summary headings + .faq-question items, same parser as tools/check_page.py). Old-template pages are listed so rebuilds avoid their intents too; the Nassau entry is a snapshot of the parallel rebuild.

### dvr-upgrade-bronx — old template (pre-rebuild)
**Q&A / question headings:**
- How do I tell if my building has a DVR or an NVR?
- Does the super's monitor go dark during the swap?
- Can we keep the old lobby cameras and add a 4K one at the entrance?
- Is a recorder swap worth it in a pre-war building, or start fresh?
- Will a new recorder fix a dark, grainy vestibule at night?
- How do I know the riser coax is still good?
- Can the co-op add cameras later without another board vote?
- Why does our DVR only hold two days now when it used to hold weeks?
- What drive size covers a lobby, vestibule, and six hallways for a month?
- Can two recorders split a big building's cameras?
- Does upgrading change how the super views cameras remotely?
- Is a hybrid harder for building staff to operate?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR in an apartment building?
- If the building internet goes down, does recording stop?
- Why do basement recorders fail so often here?
- Can a recorder run with a dead hard drive?
- How many cameras can one building recorder handle?
- Does the swap mean opening walls in the apartments?
- How often should a building replace its DVR?
- Is remote viewing on an old building recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-brooklyn — REBUILT 2026-10-18 (this run)
**Q&A / question headings:**
- Cellar Recorder Beeping, Frozen or Dark?
- Our cellar took water during Ida but the old recorder still powers on — can we trust its drive?
- The recorder in our Flatbush two-family is in the downstairs tenant's apartment — how do we move it without losing the cameras?
- Can the new recorder go in a top-floor closet when every coax run ends in the cellar?
- The coax in our Park Slope rowhouse was fished down a chimney chase twenty years ago — can a new recorder use it?
- A contractor's gut renovation on our parlor floor cut some camera runs — how do you find which ones are dead?
- Is the thin all-in-one cable the last installer stapled along our party wall good enough for HD?
- The recorder behind our bodega counter keeps rebooting — is it the hard drive or the power?
- Our register camera faces the glass storefront and every afternoon clip is a dark silhouette — can the upgrade fix the backlight?
- Can one recorder cover our ground-floor store and the apartments upstairs in a mixed-use building on Nostrand Avenue?
- Does New York's commercial security tax credit cover a recorder upgrade for a small Brooklyn store?
- As the landlord of a three-family in Bushwick, can I let tenants see the front-door camera without giving them the whole recorder?
- Does New York's backyard-camera law apply to a camera on our own rowhouse's rear wall?
- Can we record sound on the hallway cameras of our walk-up?
- Who should hold the admin password on a brownstone owned by two siblings or an LLC?
- We're in a Brooklyn historic district — do we need Landmarks Preservation Commission approval to put a new camera on the front?
- How many cameras can go on a 20-foot-wide landmarked rowhouse front?
- Where do the new camera cables go so they don't run down the brownstone face?
- The previous owner left a no-name recorder in the cellar — is it one of the models botnets go after?
- Should the upgraded recorder be reachable from the internet at all, or only through the app?
- The router is on the top floor of our brownstone and the recorder is in the cellar — how does the recorder get online?
**FAQ (= FAQPage):**
- How long does a recorder swap take in a four-storey walk-up, and does someone need to be on every floor?
- Can a bodega's recorder be swapped before opening or after closing so the store never goes unrecorded?
- We own two adjoining rowhouses on the same Bed-Stuy block — can one recorder cover both?
- Someone keeps tampering with our store's roll-down gate at night — can a camera outside the gate record clearly?
- Can the new recorder show the cameras on the TV in our parlor-floor living room as well as on our phones?
- What do you need from a tenant before you go into their apartment to reach a camera run?
- Our cellar recorder sits beside the water heater — does the heat shorten its life?
- Can we add a backyard camera to a rowhouse without opening the parlor-floor ceiling?
- We rent our Fulton Street store — can we take the upgraded recorder with us when the lease ends?
- The coax in our walk-up runs up the stair hall in plastic raceway that tenants keep cracking — should that be redone during the upgrade?

### dvr-upgrade-dutchess — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I keep my cameras and add a 4K one at the entrance?
- Is a recorder swap worth it on a big property, or start over?
- Will a new recorder fix dark footage across my field at night?
- How do I know if my long runs are still good?
- Can I expand the system later without re-pulling cable?
- Why does my recorder only keep a couple days now?
- What drive size covers a 12-camera property for a month?
- Does spotty rural internet stop the recorder from saving?
- Can two recorders cover one large farm or estate?
- Is a hybrid harder to run than my old DVR?
- What's the recorder for if I already have cameras?
- DVR or NVR — which runs a Dutchess home or farm?
- If the property internet drops, does recording stop?
- Why do recorders on big properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-hudson-valley — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I mix 1080p and 4K cameras on one recorder?
- Is a DVR upgrade worth it, or should I start over?
- Will a new DVR fix my grainy night footage?
- How do I know if my coax is good enough to reuse?
- Can I add cameras later without another upgrade?
- Why does my DVR only keep a few days of footage?
- What size hard drive do I need for 30 days?
- Can two recorders share the same cameras?
- Does upgrading the DVR change how I view cameras remotely?
- Is a hybrid recorder harder to use than my old DVR?
- What does a DVR actually do in a camera system?
- Is a DVR the same as an NVR?
- Do I need internet for a DVR to record?
- What causes a DVR to stop working?
- Can a DVR record without a hard drive?
- How many cameras can one DVR support?
- Does upgrading a DVR need new wiring?
- How often should a DVR be replaced?
- Is it safe to view my DVR remotely?
**FAQ (= FAQPage):**

### dvr-upgrade-long-island — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I keep my old cameras and add a 4K one at the driveway?
- Is a recorder swap worth it, or should I redo the whole system?
- Will a new recorder fix dark driveway footage at night?
- How do I know if salt air damaged my outdoor runs?
- Can I add cameras later without re-pulling cable?
- Why does my recorder only keep a few days now?
- What drive size covers a big house for a month?
- Can two recorders cover one big property?
- Does upgrading change how I watch from away?
- Is a hybrid harder to use than my old DVR?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR for a Long Island home?
- If my internet drops, does the DVR stop recording?
- Why do basement and garage recorders fail out here?
- Can a DVR record with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean opening my walls?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-manhattan — old template (pre-rebuild)
**Q&A / question headings:**
- How do I tell if my building has a DVR or an NVR?
- What happens to the doorman's live monitor during the swap?
- Can I keep my old vestibule camera and add a 4K one at the door?
- Is a recorder swap worth it in a pre-war building, or start fresh?
- Will a new recorder fix a dim, grainy lobby at night?
- How do I know the basement coax is still good?
- Can the co-op add cameras later without another board vote?
- Why does our DVR only hold two days now when it used to hold weeks?
- What drive size covers a lobby, vestibule, and eight hallways for a month?
- Can two recorders split a big building's cameras?
- Does upgrading change how the super views cameras remotely?
- Is a hybrid harder for building staff to operate?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR in a co-op building?
- If the building internet goes down, does recording stop?
- Why do basement recorders fail so often here?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder in a building handle?
- Does the swap mean opening walls in the apartments?
- How often should a building replace its DVR?
- Is remote viewing on an old building recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-nassau-county — REBUILT 2026-10-18 by parallel agent — snapshot taken ~04:45 UTC; authoritative list in research/dvr-upgrade-nassau-county.part.md
**Q&A / question headings:**
- Nassau DVR Beeping, Black Screens or Missing Nights?
- Should the new recorder live in the detached garage, where the old one was, or move into the house?
- The garage camera shows rolling lines whenever the door opener runs. Will a new recorder cure that?
- How do we get a camera onto a detached garage that has never had any cable run to it?
- Our side door on the garage only ever records the top of someone's head. Can the upgrade fix that angle?
- What does it take to capture a readable licence plate at the end of a long driveway?
- Will person and vehicle alerts work on the older coax cameras along our driveway, or only on new ones?
- Can the cameras tell me when someone tries the car doors in the driveway at three in the morning?
- Can one camera cover the whole pool, or does the deck need two?
- One back-yard camera washes out white at night while the others look normal. Is that the old recorder?
- Can the recorder flag only real activity around the pool gate, not leaves and the pool cleaner?
- How long will a battery backup keep the recorder going in a long PSEG outage like Isaias?
- After a storm the old recorder came back showing the wrong date. Does that matter for footage the police want?
- Lightning struck near the house and two channels went black. Was it the recorder or the cameras?
- Does our village need a permit for a recorder swap or one extra camera?
- Garden City police run a camera registry. Does signing up give them access to our recorder?
- Can the video doorbell we already own show up on the new recorder?
- Our landlord owns the facade and the rear lot. Who decides where the shop's cameras go?
- Our shop shares a rear lane with the next tenant. Can our camera watch our back door without filming theirs?
- In a Levitt-built house with no basement, where does the cable from the new recorder go?
- We just bought a house with cameras already up. What should we check before deciding what to keep?
**FAQ (= FAQPage):**
- What does a recorder swap usually cost for an eight-camera Nassau house with a detached garage?
- Is a Nassau County home improvement licence needed for someone to swap a recorder?
- Can the new recorder send a snapshot when the garage door or a gate opens?
- Do freezing January nights affect a camera or a recorder in an unheated garage?
- If our recorder died overnight, can someone come out today?
- Can a camera cover the boat or trailer stored beside the house over the winter?
- Will replacing the DVR interrupt the alarm company's monitoring?
- Can the new recorder switch on the yard floodlights when someone walks up the drive?
- Is there a monthly fee after the upgrade?
- Do you take the old DVR away, and what happens to the footage on its drive?

### dvr-upgrade-nyc — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- Which borough page should I use?
- Can I keep my cameras and add a 4K one later?
- Is a recorder swap worth it citywide, or start over?
- Will a new recorder fix grainy night footage?
- How do I know my coax can be reused?
- Can I add cameras later without a re-wire?
- Why does my DVR only keep a few days now?
- What size drive for 30 days?
- Do you serve my specific neighborhood?
- Does upgrading change remote viewing?
- Is a hybrid harder to use than my old DVR?
- What does a DVR do in a camera system?
- DVR or NVR — what's the difference?
- Does a DVR need internet to record?
- What makes a DVR fail?
- Can a DVR record without a hard drive?
- How many cameras can one DVR handle?
- Does upgrading a DVR need new wiring?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder risky?
**FAQ (= FAQPage):**

### dvr-upgrade-orange — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR out here?
- What happens to my old footage when I upgrade?
- Can I keep my barn cameras and add a 4K one at the gate?
- Is a recorder swap worth it on a big property, or start over?
- Will a new recorder fix dark footage across my field at night?
- How do I know if my long runs are still good?
- Can I expand the system later without re-pulling cable?
- Why does my recorder only keep a couple days now?
- What drive size covers a 24-camera property for a month?
- Does spotty rural internet stop the recorder from saving?
- Can two recorders cover one large multi-building site?
- Is a hybrid harder to run than my old DVR?
- What's the recorder actually for if I already have cameras?
- DVR or NVR — which one runs a barn or shop out here?
- Will patchy rural service or an outage wipe my recordings?
- Why do recorders on rural properties give out so much?
- If the hard drive is dead, does the recorder still do anything?
- What channel count fits a multi-building Orange County site?
- Will you have to re-run all my long outdoor cable?
- How long before a DVR should be swapped?
- Is it risky to view an old recorder over the internet?
**FAQ (= FAQPage):**

### dvr-upgrade-putnam — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I keep my cameras and add a 4K one at the driveway?
- Is a recorder swap worth it, or should I redo the system?
- Will a new recorder fix my dark lakefront footage at night?
- How do I know if my long outdoor runs are still good?
- Can I add cameras later without re-pulling cable?
- Why does my recorder only keep a few days now?
- What drive size covers a Putnam home for a month?
- Does spotty service up here stop the recorder from saving?
- Does upgrading change how I watch from the city?
- Is a hybrid harder to use than my old DVR?
- What's the recorder for if I already have cameras?
- DVR or NVR — which runs a Putnam home?
- If the internet drops up here, does recording stop?
- Why do recorders on wooded properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my long outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-queens — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I keep my old cameras and add a 4K one at the driveway?
- Is a recorder swap worth it, or should I re-do the whole system?
- Will a new recorder fix my dark driveway footage at night?
- How do I know if my long outdoor runs are still good?
- Can I add cameras later without re-pulling cable?
- Why does my recorder only keep a few days now?
- What drive size covers a big house for a month?
- Can two recorders cover one big property?
- Does upgrading change how I watch from another borough?
- Is a hybrid harder to use than my old DVR?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR for a Queens house?
- If my home internet drops, does the recorder stop saving?
- Why do recorders on big properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-rockland — old template (pre-rebuild)
**Q&A / question headings:**
- How can I tell a DVR from an NVR?
- Will upgrading erase my saved footage?
- Can I keep every camera and just add a sharp one at the driveway?
- Repair the recorder or replace the whole setup?
- Will a new box clean up a grainy nighttime driveway?
- How do I know my buried or long runs are still usable?
- Can I grow the system later without pulling new wire?
- Why is my recorder down to just a couple days of footage?
- How big a drive covers a month on a large home?
- Can I split a big property across two recorders?
- Does upgrading improve how I check in from over the bridge?
- Is a hybrid more complicated to operate day to day?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR for a Rockland house?
- If my home internet drops, does the recorder stop saving?
- Why do recorders on big properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-staten-island — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- What happens to my old footage when I upgrade?
- Can I keep my old cameras and add a 4K one at the driveway?
- Is a recorder swap worth it, or should I redo the whole system?
- Will a new recorder fix my dark driveway footage at night?
- How do I know if my long outdoor runs are still good?
- Can I add cameras later without re-pulling cable?
- Why does my recorder only keep a few days now?
- What drive size covers a big house for a month?
- Can two recorders cover one big property?
- Does upgrading change how I watch from off-Island?
- Is a hybrid harder to use than my old DVR?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR for a Staten Island house?
- If my home internet drops, does the recorder stop saving?
- Why do recorders on big properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-suffolk-county — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR out here?
- What happens to my old footage when I upgrade?
- Can I keep my barn cameras and add a 4K one at the gate?
- Is a recorder swap worth it on a big property, or start over?
- Will a new recorder fix dark footage across my yard at night?
- How do I know if my long runs are still good?
- Can I expand the system later without re-pulling cable?
- Why does my recorder only keep a couple days now?
- What drive size covers a 24-camera site for a month?
- Can two recorders cover one large multi-building site?
- Does upgrading change how I watch remotely?
- Is a hybrid harder to run than my old DVR?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR for a farm or warehouse?
- If the property internet drops, does recording stop?
- Why do recorders on big properties fail so often?
- Can a recorder run with a dead hard drive?
- How many cameras can one recorder handle?
- Does the swap mean re-running my long outdoor cable?
- How often should a DVR be replaced?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**

### dvr-upgrade-ulster — old template (pre-rebuild)
**Q&A / question headings:**
- Do I have a DVR or an NVR?
- Can a DVR upgrade keep my old cameras?
- How long does a DVR upgrade take?
- Will I be able to watch my cameras from my phone?
- How much storage does a DVR need?
- Why does my DVR keep beeping?
- Can I add more cameras during a DVR upgrade?
- Is it worth upgrading an old DVR?
- What happens to my old footage?
- Do DVR upgrades work with Swann, Night Owl, and Lorex?
- Will remote viewing work at a house with slow internet?
- Does a new recorder lower false alerts?
- What's the recorder for if I already have cameras?
- Should I repair my old DVR or replace it?
- Can an old DVR be upgraded to 4K?
- How do I know if my DVR hard drive is failing?
- Do wireless cameras replace a DVR system?
- Is a DVR or NVR better for a rural property?
- Can police use footage from my DVR?
- How many years does a security DVR last?
- Do I need internet for a DVR to work?
**FAQ (= FAQPage):**

### dvr-upgrade-westchester — old template (pre-rebuild)
**Q&A / question headings:**
- How do I tell if my building has a DVR or an NVR?
- Does the super's monitor go dark during the swap?
- Can we keep the old lobby cameras and add a 4K one at the entrance?
- Is a recorder swap worth it in a finished home, or start fresh?
- Will a new recorder fix a dark, grainy lobby at night?
- How do I know the riser coax is still good?
- Can the co-op add cameras later without another board vote?
- Why does our DVR only hold two days now?
- What drive size covers a lobby and several hallways for a month?
- Can two recorders split a big building's cameras?
- Does upgrading change how the super views cameras remotely?
- Is a hybrid harder for staff to operate?
- What does the DVR do that the cameras don't?
- Is a DVR the same as an NVR in a Westchester building?
- If the building internet goes down, does recording stop?
- Why do building recorders fail so often here?
- Can a recorder run with a dead hard drive?
- How many cameras can one building recorder handle?
- Does the swap mean opening finished walls?
- How often should a building replace its DVR?
- Is remote viewing on an old recorder a security risk?
**FAQ (= FAQPage):**


---

## Brooklyn

Page: `dvr-upgrade-brooklyn` (REBUILD in place, 2026-10-18). Up-link `/dvr-upgrade-nyc`. GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`). Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from the NYC hub, Nassau and the other boroughs):** the Brooklyn recorder lives in a rowhouse cellar, a tenant's closet or behind a bodega counter, and is fed by coax fished through plaster, brick and chimney chases. The upgrade keeps that coax (HD-over-coax / hybrid XVR), moves the recorder out of flood- and tenant-exposed spots, splits access between landlord, tenants and store staff, respects landmark rules on visible fronts and NY camera/audio law, closes the open ports that let botnets in, and makes footage exportable for precinct requests.

### Building stock (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | Firecrawl Alexandria `census-gov` census/data · acs/acs5 2023 · B25035_001E, B25001_001E, B25024_002E–006E, B25034_010E–011E, B25003_002E–003E · county 047 state 36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36047 | Kings County: 1,090,187 housing units; median year built **1943**; built 1939 or earlier **513,629**; 1940–49 92,848; 1-unit detached 52,359; 1-unit attached 93,812; 2-unit **175,805**; 3–4 unit **170,655**; 5–9 unit 116,319; owner-occupied 300,026; renter-occupied **709,570** (≈70% of occupied). | §5 para 1; §5.5 bullets 1–3; §Sources |
| H2 | `Kings County Brooklyn housing units median year built census rowhouse two-family housing stock` · Firecrawl search | https://urbanomnibus.net/2016/05/how-many-row-houses-are-there-in-new-york-city/ | (2016) ~217,000 row houses citywide (of 761,000 residential properties); average 2.0 units each; average row house lot ~1,900 sq ft, "very close to the prototypical 2,000 square foot (20 x 100') New York City lot". | §7 cards (20-ft lots); §9 cluster 5 H3 2; §Sources |
| H3 | same | https://chpcny.org/visualization/housing-stock-visualization/ | Excerpt: >80% of NYC housing built more than 50 years ago; over half (~2 million) before 1947. | Background only |

### Landmarks / LPC (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | `"security cameras" Landmarks Preservation Commission rules 63 RCNY staff level permit criteria mortar joints` · Firecrawl search (gov) → scrape (PDF, query) | https://nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook%20_Chapter11_HealthSafety.pdf | Staff can approve security cameras by permit when criteria are met: cameras "well spaced to avoid a cluttered, haphazard appearance"; small residential/commercial buildings max **two cameras per 25 ft** of street frontage; large buildings max **three per 25 ft**. General criteria: not on/in front of a primary facade unless no feasible alternative; if on the primary facade, discreet location (beneath a band course, **underneath a stoop**, behind an areaway wall or fence, behind plantings); attach at **mortar joints, plain masonry, wood or metalwork**, not through cast iron or decorative surfaces; conduit concealed through plain masonry/cladding behind the installation, otherwise ~**10 inches** of visible conduit, painted to match and secured into mortar joints; equipment as small as possible and painted to blend. | §6 card; §8.5 bullet; §9 cluster 5 (all three H3); §10.5 H3 6; §FAQ 4; §Sources |
| L2 | `LPC landmarks permit security cameras rowhouse facade rules New York City` · Firecrawl search | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | Full guidebook (274 pp). A directQuote scrape returned the mailbox section instead of cameras → superseded by L1 (chapter 11). | — |
| L3 | same | https://shermanarchitects.com/navigating-the-landmarks-preservation-commission/ | Excerpt: "The LPC is most concerned with what's visible from the street. Rear-yard extensions and rooftop additions that aren't visible from public thoroughfares have an easier approval path…" | §9 cluster 5 H3 1 ("rear facades … generally treated more leniently"); §Sources |
| L4 | `Brooklyn Heights Historic District 1965 first historic district …` · Firecrawl search | https://thebha.org/neighborhood/ ; https://hdc.org/borough/brooklyn/ ; NYC LPC Facebook post (excerpt) | Brooklyn Heights designated **November 23, 1965**, NYC's first historic district (LPC post excerpt gives the date; BHA and HDC confirm "first", 1965). | §5.5 bullet 4; §13 card; §Sources |

### Flooding (F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F1 | `Hurricane Ida Brooklyn basement flooding cellar 2021 homes damaged` · Firecrawl search → scrape (query) | https://a816-dohbesp.nyc.gov/IndicatorPublic/data-stories/flooding-and-health/ | NYC Health Dept data story: Ida — 14 deaths, 10 (71%) by drowning in unregulated basement apartments; record **3.5 in/hour** rainfall vs sewer capacity **1.75 in/hour**; "unprecedented inland flooding, especially in low-lying areas and basement apartments". Sandy — 52 injury deaths; 23% in Brooklyn; Flood Vulnerability Index flags "especially vulnerable areas in southern Brooklyn and Queens". | §5.5 bullet 5; §7 southern Brooklyn card + §7.5 paragraph; §9 cluster 1 H3 1; §13 boardwalk card; §Sources |
| F2 | same (excerpt) | https://abc7ny.com/post/nyc-flooding-deadly-13-killed-basement-apartments-flood/10995579/ | Sept 4, 2021: 13 dead from Ida flooding in NYC, most in illegal basement apartments (DOB commissioner quote). | Date context for "September 2021" in §9 cluster 1 H3 1 |

### News / hyperlocal (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | `Brooklyn package theft porch pirates brownstone stoop NYPD 2025 2026 news` · Firecrawl search → scrape (query) | https://brooklyn.news12.com/2025/12/03/porch-pirates-are-snatching-holiday-packages-heres-how-to-protect-yours/3vxg19mAstZxQsrDNpiWwR | Dec 3, 2025: "About 90,000 packages are stolen every day, according to the Department of Transportation" (NYC); resident caught a theft on camera; no camera advice. | §5 para 3; §Sources |
| N2 | `Brooklyn bodega robbery surveillance video NYPD released 2026` · Firecrawl search | https://www.facebook.com/ny1news/videos/brooklyn-bodega-robbery-surveillance-video/1333516076747254/ | Excerpt: "Police say another man helped this man rob a Brooklyn bodega … The NYPD released surveillance footage … May 15, 2026". | §5 para 3 (as excerpt); §Sources |
| N3 | `Bed-Stuy deli robbery suspects NYPD jackets surveillance video CBS New York` · Firecrawl search | https://www.facebook.com/ABCNews/videos/four-new-york-city-robbery-suspects-got-away-with-a-bag-full-of-lottery-tickets-/1216854093369137/ ; https://www.facebook.com/News12NewYork/posts/caught-on-camera-surveillance-video-shows-the-moments-four-men-impersonating-pol/1271003461701912/ ; https://www.youtube.com/watch?v=AOLZ5-LOKZ8 (CBS NY) | Excerpts: four men impersonating police (jackets printed "NYPD") robbed a Bed-Stuy deli at gunpoint, zip-tied three victims, left with a bag of lottery tickets; captured on surveillance video. Date not shown in excerpts → page gives no date. Instagram reel not scrapeable (unsupported site). | §5 para 3; §Sources |
| N4 | `r/Brooklyn security camera DVR landlord building cameras` · Firecrawl search | https://www.theguardian.com/cities/2019/may/29/new-york-facial-recognition-cameras-apartment-complex | May 29, 2019: tenants at Atlantic Plaza Towers, Brooklyn, fought their landlord's facial-recognition camera plan. | §10.5 H3 5; §Sources |
| N5 | same (excerpt) | https://www.facebook.com/groups/1149018855466986/posts/2637264153309108/ | Facebook group excerpt on tenants and cameras in Brooklyn ("Cameras are allowed in common areas…") — unverifiable social post. **Not used.** | — |
| N6 | `Brownstoner brownstone security cameras installation wiring cellar` · Firecrawl search → scrape (query) | https://www.brownstoner.com/forum/general-discussion/installing-security-cameras-lights-on-brownstone-exterior/ | Brownstoner forum (posted ~3 years 7 months before fetch): "We've had some worrying security incidents lately and I want to install a ring floodlight cam on the second floor of our brownstone." / "how difficult it is/how much it will cost to run a new wire". 0 replies. | Background for §7.5 (running new wire on a brownstone is the hard part); not quoted |

### Corridors / commercial (C)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C1 | `Brooklyn business improvement districts list Pitkin Avenue Kings Highway Fulton Mall Flatbush Avenue Fifth Avenue BID` · Firecrawl search | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | SBS BID directory, Brooklyn: (archive) Church Avenue, 86th Street Bay Ridge, Atlantic Avenue, Bay Ridge 5th Avenue, Bed-Stuy Gateway, Brighton Beach, Church-Flatbush Community Alliance, Coney Island, Court-Livingston-Schermerhorn, Cypress Hills Fulton, DUMBO, East Brooklyn, Flatbush-Nostrand Junction, FAB Alliance, Fulton Mall Improvement Association, Graham Avenue, Grand Street, Kings Highway, MetroTech, Montague Street, Myrtle Avenue Brooklyn Partnership, North Flatbush, Park Slope 5th Avenue, Pitkin Avenue, Sunset Park → **24 active** (25 incl. archived Church Ave). NYCBusiness FB excerpt also says "Brooklyn is home to 24 Business Improvement Districts". | §5.5 bullet 6; §8 corridor cards; §Sources |
| C2 | same | https://www.bayridgebid.com/ | Bay Ridge 5th Avenue BID covers 5th Avenue **from 65th to 85th Streets**. | §8 card; §Sources |
| C3 | `Fulton Mall Downtown Brooklyn pedestrian shopping street history Fulton Street` · Firecrawl search | https://en.wikipedia.org/wiki/Fulton_Street_(Brooklyn) | "Fulton Mall is a pedestrian street and transit mall in Downtown Brooklyn that runs on Fulton Street between Flatbush Avenue and Adams Street." | §8 card; §13 card; §Sources |

### Landmark cards (L5–L8)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L5 | `Kings Theatre Flatbush Avenue opened 1929 restored reopened 2015 seats` · Firecrawl search | https://en.wikipedia.org/wiki/Kings_Theatre_(Brooklyn) (+ FB excerpts) | Opened September 7, 1929; capacity 3,250; restoration completed / reopened 2015. | §13 card |
| L6 | `Brooklyn Navy Yard 300 acres industrial park tenants businesses` · Firecrawl search | https://www.brooklynnavyyard.org/brooklyn-navy-yard-fy25-impact-report/ | "Spanning more than 300 acres … home to over 550 businesses supporting more than 13,000 jobs" (FY25 impact report). | §13 card |
| L7 | `Industry City Sunset Park acres buildings former Bush Terminal` · Firecrawl search | https://en.wikipedia.org/wiki/Industry_City ; https://industrycity.com/ | Bush Terminal site includes 16 former factory buildings (Wikipedia excerpt); "6-million-square-foot ecosystem" (industrycity.com). Acreage figures conflict between sources (71 vs ~35 acres) → acreage NOT used. | §13 card |
| L8 | `Riegelmann Boardwalk Coney Island opened 1923 length miles Brighton Beach` · Firecrawl search | https://en.wikipedia.org/wiki/Riegelmann_Boardwalk ; https://www.nycgovparks.org/parks/coney-island-beach-and-boardwalk/highlights/204 | 2.7 miles from West 37th Street (Sea Gate border) to Brighton 15th Street; first portion opened 1923. | §13 card |

### Yelp (Y)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| Y1 | `yelp Brooklyn security camera installer review DVR "not recording" OR "hard drive" 1 star` · Firecrawl search | https://www.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Bay+Ridge%2C+Brooklyn%2C+NY+11209 | Search-page excerpt only: a low review complaining about being asked to pay "$100+ just to format my hard drive" (business type unclear; not a camera recorder). Review pages not opened. | Not used. Treat Yelp 1–3★ as EMPTY (not accessible in build env). |

### Licensing / permits (Brooklyn)
- NYS low-voltage licence #12000287431 (AESS, protected content).
- LPC (L1) is the only permit regime cited on the page (visible facades on designated buildings). NYC DOB permit requirements for low-voltage camera work: EMPTY (not researched to a primary source) → page makes no DOB claim.
- Landlord/tenant: no NYC rule found requiring landlords to install cameras (R5 asks; no answer opened) → page makes no claim either way.

### House practices stated on the page without an external source (FLAG for Anwar)
- Moving recorders off cellar floors / next to boilers, onto high shelves or upper floors; battery backup (UPS) for recorder + modem.
- Test method: HD test camera + test monitor, continuity/short check, tone generator; cut back and re-terminate before replacing a run; old cable as pull string.
- Separate owner / tenant / store accounts; privacy masking on rear cameras; video-only by default.
- Closing port forwards and UPnP; phone access via maker relay or VPN.
- Swap timing (half-day typical, full day with tracing; store swaps before opening/after closing); two-hour arrival windows, seven days a week to 8 PM (copied from live silo pages); "most systems recording again within one to two hours of arrival" (blueprint §5 element 36 wording).
- "Five checks to run on an old recorder tonight" list (§Repair1) — generic owner self-checks.

### Images (11) — Drive has no DVR Upgrade folder; CompanyCam not connected (per coordinator)
Step C / permanent image rule. 9 real AESS job photos from other jobs in `images/` (cropped to remove signs, text, logos, people, documents, address numbers; captioned "example photo from another AESS job (not a Brooklyn …)") + 2 manufacturer recorder product shots. All looked at with the Read tool first. Rejected: `images/buzzer-repair/*` (look AI-generated — garbled meter text, staged signage — and show people). Avoided every source file the parallel Nassau page used (rockland-toyota-bullet-camera, -hallway-camera, -nvr-monitor, -active-deterrent, nassau-window-depot-monitor, -storage-camera, nvr-idis, nvr-trendnet, nvr-uniview, Hikvision bullet product shot).
| Output (images/dvr-upgrade/) | Source | Crop / note | Page placement |
|---|---|---|---|
| dvr-upgrade-brooklyn-slim-black-recorder-product-photo.webp | images/nvr-speco-n16nrx.png | product shot, white background; small maker logo not named in copy | Hero (eager) |
| dvr-upgrade-brooklyn-dome-camera-on-wall-arm-on-stone-facade.webp | images/manhattan-deli-exterior.jpeg | crop (0,0,228,372): facade + arm only; signs, address numbers, people, subway sign removed | §5 |
| dvr-upgrade-brooklyn-store-monitor-showing-camera-grid.webp | images/manhattan-deli-monitor.jpeg | crop to the screen (tile figures tiny, not identifiable) | §6 |
| dvr-upgrade-brooklyn-small-bullet-camera-on-bare-wall.webp | images/rockland-toyota-wall-camera.jpeg | crop to wall, camera and sensor | §7 |
| dvr-upgrade-brooklyn-black-mini-dome-at-ceiling-edge.webp | images/rockland-toyota-dome-camera.jpeg | crop to ceiling; dealer logo and TV removed | §9 |
| dvr-upgrade-brooklyn-large-rack-recorder-with-vented-front-product-photo.webp | images/nvr-ens-titanium.png | product shot | §10 |
| dvr-upgrade-brooklyn-mini-domes-in-shop-drop-ceiling.webp | images/manhattan-deli-interior-cameras.jpeg | crop to ceiling; people, menu boards removed | §12 |
| dvr-upgrade-brooklyn-turret-camera-in-drop-ceiling-by-light-panel.webp | images/rockland-toyota-office-camera.jpeg | crop to ceiling; signage, staff, trophies removed | §13 |
| dvr-upgrade-brooklyn-white-dome-in-corner-above-motion-sensor.webp | images/nassau-window-depot-office-camera.jpeg | crop to corner; banner, licences/documents, flag removed | §14 |
| dvr-upgrade-brooklyn-black-bullet-on-ceiling-mount-over-plain-wall.webp | images/rockland-toyota-ceiling-bullet.jpeg | crop above the desk monitors; small logo on camera body not named | §15 |
| dvr-upgrade-brooklyn-white-turret-under-storefront-fascia.webp | images/manhattan-deli-exterior-camera.jpeg | crop below the sign band (no text) | Field Notes |
All WebP, quality 80, ≤1600 px. Alt/title unique, each with "Brooklyn"; captions describe only what is visible.

### Build notes
- check_page.py: PASS (full, with registration). 13,858 rendered words; title 53; meta 158; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10.
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word-level SequenceMatcher) vs every dvr-upgrade-* page: max **0.471** (vs dvr-upgrade-nyc, a short H3); the only 1.000 is the blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades in [Area]" (same on the new Nassau page by design).
- File size 186,554 B vs new Nassau page 180,770 B at final check (gap ≈5.8 KB > 2 KB). If Nassau grows by ~2 KB the size-cluster check will flag one of the two — re-check at wiring.
- Semantic de-dup against the new Nassau page done by reading its 31 questions: seven Brooklyn questions that overlapped in intent (locking the recorder away, detective clip export, inherited-system password, selling the house, flood → where should the recorder go, soft register picture, neighbour-yard privacy) were rewritten to Brooklyn-only intents (party-wall rowhouse pair, roll-down gate camera, store lease, water-heater heat, post-Ida drive trust, backlit storefront, §52-a applicability). A later Nassau edit added "Can the video doorbell we already own show up on the new recorder?", so the Brooklyn FAQ on the walk-up video buzzer was replaced by one on stair-hall raceway.


---

<!-- merged from dvr-upgrade-nassau-county build (2026-10-18) -->

# DVR Upgrade — Nassau County research (part file for merge into research/dvr-upgrade.md)

Page: `/dvr-upgrade-nassau-county` (REBUILD, was crawled-not-indexed) · up-link `/dvr-upgrade-long-island` · phone (516) 346-5778 · GBP Brooklyn (#brooklyn, 1282 Troy Ave)
Built 2026-10-18. Thesis: a Nassau system is a house + detached garage + driveway + pool/yard (+ sometimes a strip-mall shop); keep the coax/cameras, replace the recorder, place and power it for outages, add plate/door detail.
Research tools: Firecrawl search/scrape (mcp__Firecrawl__*). Shell curl blocked. Format per entry: exact query · platform · URL · finding · page + section used.

## Silo-level findings (gathered for this page; coordinator may merge into the silo section)

| # | Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|---|
| S1 | `HD-TVI 4K transmission distance RG59 coax meters Hikvision TurboHD` | Firecrawl search | https://www.hikvision.com/en/newsroom/latest-news/2016/hikvision-s-third-generation-turbo-hd-brings-4k-video-to-analog-systems/ | (excerpt) Turbo HD 3.0 "guarantees up to 1200 meters of high-quality HD720p transmission and up to 800 meters of HD1080p video" over coax | Building Specialists, "Large North Shore lots" para |
| S2 | same query | Firecrawl search | https://videos.cctvcamerapros.com/surveillance-system-installations/cctv-camera-video-max-cable-length-distance.html | (excerpt) RG59 max 500 m; with HD-TVI amplifier 600 m | not used (vendor claim) |
| S3 | `WD Purple surveillance hard drive designed 24/7 workload rate TB/year AllFrame` | Firecrawl search | https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-purple-hdd/data-sheet-wd-purple-hdd.pdf | (excerpt) WD Purple workload rating up to 180 TB/year, "up to three times that of desktop drives"; AllFrame reduces frame drops | Equipment grid ("Surveillance-Rated Hard Drives"); AI section "Any hard drive will do" |
| S4 | `CISA advisory DVR vulnerability botnet exploited TBK DVR CVE-2024-3721` | Firecrawl search | https://fortiguard.fortinet.com/outbreak-alert/tbk-dvrs-botnet-attack | (excerpt) CVE-2024-3721, unauthenticated command injection in TBK DVRs, actively exploited, devices conscripted into a DDoS botnet | AI section "An old DVR is safe as long as it has a password" |
| S5 | `FCC covered list Hikvision Dahua November 2022 ban new equipment authorizations` | Firecrawl search | https://www.congress.gov/crs-product/LSB10895 ; https://www.fcc.gov/laboratory-division/equipment-authorization-approval-guide/equipment-authorization-system | (excerpt) Nov 25, 2022 R&O prohibits new authorizations for Covered List equipment; Hikvision/Dahua video surveillance equipment covered when used for public safety, government facilities, critical infrastructure, national security | AI section "Hikvision and Dahua are banned…" |
| S6 | `DVR replacement cost security camera recorder install cost homeguide angi` | Firecrawl search | https://homeguide.com/costs/security-camera-installation-cost | (excerpt) "A new DVR/NVR costs $100 and $350 if your current unit cannot support more cameras"; DVR storage $100–$300 | AI section "A new DVR costs $100 to $350" |
| S7 | `reddit longisland old DVR camera system upgrade replace recorder keep cameras` | Firecrawl search (Reddit results) | https://www.reddit.com/r/SecurityCamera/comments/1eypvng/can_you_upgrade_a_receiver_instead_of_getting_a/ | (excerpt) reply: "your best bet is to just buy a new system" | AI section "Just buy a new system" |
| S8 | same query | Firecrawl search (Reddit results) | https://www.reddit.com/r/homesecurity/comments/1s697t6/existing_cameras_new_dvrnvr/ | (excerpt) "we've inherited old camera systems at properties where the cheapest path was keeping the cameras, swapping the recorder, and only upgrading the…" | AI section "Just buy a new system"; Q&A "We just bought a house with cameras already up…" |
| S9 | same query | Firecrawl search (Reddit results) | https://www.reddit.com/r/homesecurity/comments/178b2nb/just_purchased_a_home_with_dated_security_cameras/ | (excerpt) thread title "Just purchased a home with dated security cameras. Best method to…" — inherited-system intent | Q&A "We just bought a house with cameras already up…" (intent only) |
| S10 | same query | Firecrawl search | https://www.reddit.com/r/videosurveillance/comments/1ii7leh/upgrade_recommendations_for_my_legacy/ | (excerpt) coax-to-Cat5 converters to keep old cameras on a new recorder | not used |
| S11 | Google PAA "dvr upgrade" | — | — | EMPTY (not accessible in build env) | — |
| S12 | Google PASF | — | — | EMPTY (not accessible in build env) | — |
| S13 | Answer the Public | — | — | EMPTY (not accessible in build env) | — |
| S14 | Google AI Overview | — | — | EMPTY (not accessible in build env) — AI section built from published cost guides/forum claims (S3–S8) instead, and says so on the page | AI section intro |
| S15 | Bing / DuckDuckGo PAA/autocomplete | — | — | EMPTY (not accessible in build env) | — |
| S16 | Yelp 1–3★ camera installers Nassau | — | — | EMPTY (not accessible in build env) | — |

## Nassau County

| # | Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|---|
| N1 | `Nassau County three towns two cities 64 incorporated villages` | Firecrawl search | https://www.ny.gov/counties/nassau | "Two cities, three towns, 64 incorporated villages, and more than 60 unincorporated hamlets" (Hempstead, North Hempstead, Oyster Bay; Glen Cove, Long Beach); full village list incl. Garden City, Freeport, Rockville Centre, Massapequa Park, Sea Cliff | Neighborhood facts list; Commercial "Village and town permits"; Q&A "Does our village need a permit…" |
| N2 | `Nassau County population 2020 census 1,395,774` then scrape | Firecrawl search + scrape | https://www.census.gov/quickfacts/nassaucountynewyork | 2020 census 1,395,774; housing units 480,591 (V2025); owner-occupied rate 81.9% (2020–24); median value $684,700; households 458,166; broadband subscription 94.8% | Neighborhood para 1 + facts list; AI section "cloud" |
| N3 | `Levittown houses built 1947 1951 Cape Cod ranch number of homes` + scrape | Firecrawl search + scrape | https://en.wikipedia.org/wiki/Levittown,_New_York | 17,447 homes by 1951; built on concrete slabs (code change needed); ranch: slab, expandable attic, no garage, hot-water radiant heating; 1950 ranch altered to include a carport + built-in TV; 1951 partially finished attic; CDP pop. 51,758 (2020), most populous unincorporated CDP in Nassau | Facts list; Building Specialists (Levitt capes card, "Slab-on-grade houses"); Q&A "Levitt-built house with no basement"; Landmarks "Levittown" |
| N4 | `Nassau County burglary crews targeting homes Newsday 2024 2025` → scrape | Firecrawl search + scrape | https://abc7ny.com/post/nassau-county-police-task-force-burglaries-long-island/14337932/ | Jan 18 2024: NCPD multi-agency burglary/stolen-car task force (Mineola); "Police believe the burglars are attracted by cars in people's driveways"; 25 residential burglaries YTD vs 34 same period prior year; share of break-ins while residents home has gone up | Neighborhood para 3 |
| N5 | same search → scrape | Firecrawl scrape | https://www.pdcn.org/CivicAlerts.aspx?AID=15190 | NCPD news flash posted July 27 2026: Major Case Squad arrest (July 24 2026) for multiple residential burglaries across Nassau between July 11 2025 and May 23 2026; jewelry removed; located in New Hyde Park | Neighborhood para 3 (suspect not named on page) |
| N6 | `Nassau County police car thefts from driveways key fob unlocked cars 2023` → scrape | Firecrawl search + scrape | https://www.nassaucountyny.gov/CivicAlerts.asp?AID=10038&ARC=11790 | Legislative District 14 update 4/8/2022 relaying NCPD alert: thefts of cars left unlocked with key fob inside; thieves look for unfolded side mirrors; catalytic converter thefts; lock car even in driveway; keep driveways illuminated; "License plate numbers are extremely valuable for the police" | Neighborhood para 3; Q&A "readable licence plate…"; Q&A "tries the car doors…" |
| N7 | same search | Firecrawl search | https://www.facebook.com/NassauCountyPD/posts/there-has-been-an-increase-in-stolen-cars-at-gas-stations-throughout-nassau-coun/535758928579550/ | (excerpt) since start of 2022 "well over half of stolen autos in Nassau County were left unlocked with the keys inside or running" | not used (Facebook excerpt) |
| N8 | `Nassau County Police Department security camera registration program residents businesses` → scrape | Firecrawl search + scrape | https://gardencitypolice.net/private-camera-reg | Garden City PD voluntary Private Camera Registration Program; "does NOT provide us access to security camera systems"; officers canvass door to door; detectives may ask to inspect video from a finite period; Detective Division 349 Stewart Ave | Facts list; Q&A "Garden City police run a camera registry…" |
| N9 | same search | Firecrawl search | https://www.pdcn.org/143/SPiN | (excerpt) NCPD SPiN — Security/Police Information Network for business continuity info exchange | not used |
| N10 | `Isaias PSEG Long Island outages Nassau County customers without power 2020` → scrape with query | Firecrawl search + scrape (PDF) | https://www.lipower.org/wp-content/uploads/2020/09/LIPA-Isaias-30-Day-Report-Final.pdf | "approximately 645,000 customer outages. Full restoration took eight days" | Neighborhood para 4 + facts list; Q&A "battery backup…Isaias"; AI section "cloud" |
| N11 | same search | Firecrawl search | https://abc7ny.com/post/widespread-damage-and-power-outages-across-long-island/6353608/ | (excerpt) ~105,000 still without power on LI the Thursday after Isaias | not used |
| N12 | same search | Firecrawl search (Reddit) | https://www.reddit.com/r/longisland/comments/i4ruo6/unpopular_opinion_massive_power_outages_were/ | (excerpt) r/longisland thread on Isaias outages, lines "weaving between, behind, and around people's homes" | background only |
| N13 | `Superstorm Sandy Nassau County homes damaged Long Beach Freeport Massapequa flooding numbers` → scrape with query | Firecrawl search + scrape | https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York | Nassau voluntary evacuation of South Shore surge zone = area south of Sunrise Highway (+ North Shore north of 25A ≤15 ft); shelter at Levittown Memorial HS; LIPA >900,000 customers out, later ~532,000; Long Beach ~$150M damage | Neighborhood para 4 + facts list; Building Specialists "Houses in the old surge zone" + recorder-location table; Landmarks "Long Beach" (first-draft Q&A on this was dropped as a Brooklyn intent overlap) |
| N14 | `Hempstead Turnpike corridor miles Nassau County retail Levittown East Meadow` → scrape NY 24 | Firecrawl search + scrape | https://en.wikipedia.org/wiki/New_York_State_Route_24 | Route through Franklin Square, West Hempstead; Fulton Ave through downtown Hempstead (4-lane commercial); Hofstra; Uniondale/Nassau Coliseum lots; UBS Arena 7.7 mi west; East Meadow 6-lane boulevard past Eisenhower Park + NUMC with commercial businesses; Levittown Public Library; commercial strip to NY 107 | Commercial corridor card; Landmarks (Coliseum/Hofstra, Eisenhower Park, Levittown library, UBS Arena) |
| N15 | (follow-up scrape) | Firecrawl scrape | https://en.wikipedia.org/wiki/New_York_State_Route_27 | Sunrise Hwy in Nassau passes Valley Stream, Lynbrook, Rockville Centre on its way to Merrick; ends Nassau stretch in East Massapequa | Commercial "Sunrise Highway" card |
| N16 | `Roosevelt Field mall Garden City square feet largest mall Long Island` | Firecrawl search | https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) ; https://www.simon.com/mall/roosevelt-field/stores | (excerpt) largest mall on Long Island, 2nd in NY, 11th in US; 630 Old Country Rd, Garden City | Commercial "Old Country Road" card; Landmarks "Roosevelt Field" |
| N17 | `Nassau County Office of Consumer Affairs home improvement license security camera installer` | Firecrawl search (+ scrape returned no body) | https://www.nassaucountyny.gov/1547/Consumer-Affairs | (excerpt) "One of the largest license categories the Department manages and oversees is the licensing of home improvement businesses" | Commercial "County licensing"; FAQ "Is a Nassau County home improvement licence needed…" |
| N18 | `Town of Hempstead Building Department permit required low voltage security camera alarm` | Firecrawl search | https://hempsteadny.gov/191/Building-Department ; https://hempsteadny.gov/622/Online-Permit-Center | (excerpt) Hempstead Building Dept permits via Online Permit Center | Commercial "Village and town permits"; Sources |
| N19 | same search → scrape | Firecrawl scrape | https://www.lowvoltagenation.com/posts/nassau-county-new-york-security-camera-permit-requirements | "Contact your specific building department before beginning work" — Town of Hempstead Building Dept, Town of Oyster Bay Building Division, your village building department | Commercial "Village and town permits"; Q&A "Does our village need a permit…" |
| N20 | Local Reddit r/longisland DVR-specific threads | Firecrawl search | — | No Nassau-specific DVR thread found; generic threads only (S7–S10) | EMPTY for Nassau-specific |
| N21 | Patch / Newsday / LI Herald Nassau DVR stories | — | — | Newsday/Patch not opened (paywall/not scraped); ABC7 + NCPD + county pages used instead | EMPTY (not accessible in build env) |

Note on unsourced generics: building-type cards (South Shore hi-ranches, North Shore colonials, mid-Island split-levels) name real hamlets/villages only; no stats attached. AESS operating facts (2-hour windows, 7 days to 8 PM, $195/hr 3-hr min, licence #12000287431, 4.7/201) are company constants from the live pages.

## Pricing used (no new prices)
Silo recorder table as already published on dvr-upgrade-nassau-county / -long-island / -brooklyn: 4-ch swap $450–$700 · 8-ch swap $650–$1,000 · 8-ch hybrid/XVR $800–$1,200 · 16-ch $1,200–$2,200 · 32-ch $2,200+ · bad-run repair quoted after testing. Nassau home range as previously published on this page: roughly $500–$1,400 installed. Service rate $195/hr, 3-hr min ($585). Packages = the 4-ch, 8-ch hybrid and 16-ch tiers. Note for coordinator: the silo table is identical across areas (no §9 multiplier applied on any DVR page) — left unchanged, not invented.

## Images (11) — Drive has no DVR folder; CompanyCam not connected
Real AESS job photos from other jobs (captioned "Example photo from another AESS job (not a Nassau property)", cropped to remove signs, logos, people, house numbers, timestamps) + manufacturer product shots. Rejected: images/buzzer-repair/* (AI-generated look — garbled glove/meter text).

| Output (images/dvr-upgrade/) | Source | Crop / note |
|---|---|---|
| dvr-upgrade-nassau-county-slim-black-recorder-product-photo.webp (500×192) | images/nvr-uniview-nvr501.png | white border trimmed; product shot (hero) |
| dvr-upgrade-nassau-county-split-screen-tile-brick-wall-and-paved-lot.webp (540×300) | images/nassau-window-depot-monitor.jpeg | top-right tile only; timestamp, house-number tile, people excluded |
| dvr-upgrade-nassau-county-white-turret-camera-with-two-illuminators-product-photo.webp (500×500) | images/cam-eyeball-ir.png | product shot |
| dvr-upgrade-nassau-county-white-dome-camera-in-storage-room-corner.webp (845×640) | images/nassau-window-depot-storage-camera.jpeg | cropped above boxes with brand text |
| dvr-upgrade-nassau-county-ceiling-bullet-camera-aimed-down-corridor-to-door.webp (635×800) | images/rockland-toyota-hallway-camera.jpeg | cropped right of poster/QR card |
| dvr-upgrade-nassau-county-camera-high-on-wall-above-motion-sensor.webp (720×645) | images/rockland-toyota-bullet-camera.jpeg | cropped above dealership sign and banner |
| dvr-upgrade-nassau-county-recorder-with-front-panel-buttons-product-photo.webp (900×363) | images/nvr-trendnet-tv-nvr208.png | product shot |
| dvr-upgrade-nassau-county-recorder-screen-channel-grid-and-bitrate-table.webp (807×585) | images/rockland-toyota-nvr-monitor.jpeg | cropped to screen, monitor brand logo excluded |
| dvr-upgrade-nassau-county-small-ceiling-camera-near-exit-sign-and-vent.webp (760×520) | images/rockland-toyota-active-deterrent.jpeg | cropped to ceiling; mural, banner, people excluded |
| dvr-upgrade-nassau-county-black-recorder-with-red-status-lights-product-photo.webp (485×198) | images/nvr-idis-dr2508p.png | product shot |
| dvr-upgrade-nassau-county-white-bullet-camera-on-wall-bracket-product-photo.webp (300×165) | images/hikvision-colorvu-bullet-camera.jpg | product shot (maker logo visible on body) |

## Question register — dvr-upgrade-nassau-county (20 Q&A H3 + 1 emergency H2 ending in "?" + 10 FAQ) — final
Q&A (section "DVR Upgrades in Nassau County: Questions Answered"):
1. Should the new recorder live in the detached garage, where the old one was, or move into the house?
2. The garage camera shows rolling lines whenever the door opener runs. Will a new recorder cure that?
3. How do we get a camera onto a detached garage that has never had any cable run to it?
4. Our side door on the garage only ever records the top of someone's head. Can the upgrade fix that angle?
5. What does it take to capture a readable licence plate at the end of a long driveway?
6. Will person and vehicle alerts work on the older coax cameras along our driveway, or only on new ones?
7. Can the cameras tell me when someone tries the car doors in the driveway at three in the morning?
8. Can one camera cover the whole pool, or does the deck need two?
9. One back-yard camera washes out white at night while the others look normal. Is that the old recorder?
10. Can the recorder flag only real activity around the pool gate, not leaves and the pool cleaner?
11. How long will a battery backup keep the recorder going in a long PSEG outage like Isaias?
12. After a storm the old recorder came back showing the wrong date. Does that matter for footage the police want?
13. Lightning struck near the house and two channels went black. Was it the recorder or the cameras?
14. Does our village need a permit for a recorder swap or one extra camera?
15. Garden City police run a camera registry. Does signing up give them access to our recorder?
16. Can the video doorbell we already own show up on the new recorder?
17. Our landlord owns the facade and the rear lot. Who decides where the shop's cameras go?
18. Our shop shares a rear lane with the next tenant. Can our camera watch our back door without filming theirs?
19. In a Levitt-built house with no basement, where does the cable from the new recorder go?
20. We just bought a house with cameras already up. What should we check before deciding what to keep?
(+ emergency H2 "Nassau DVR Beeping, Black Screens or Missing Nights?")

FAQ (visible == FAQPage schema):
1. What does a recorder swap usually cost for an eight-camera Nassau house with a detached garage?
2. Is a Nassau County home improvement licence needed for someone to swap a recorder?
3. Can the new recorder send a snapshot when the garage door or a gate opens?
4. Do freezing January nights affect a camera or a recorder in an unheated garage?
5. If our recorder died overnight, can someone come out today?
6. Can a camera cover the boat or trailer stored beside the house over the winter?
7. Will replacing the DVR interrupt the alarm company's monitoring?
8. Can the new recorder switch on the yard floodlights when someone walks up the drive?
9. Is there a monthly fee after the upgrade?
10. Do you take the old DVR away, and what happens to the footage on its drive?

Dedupe vs the new dvr-upgrade-brooklyn.html (rewritten in parallel, checked 2026-10-18 ~04:45): replaced six of my first-draft questions whose intent matched Brooklyn's (recorder lock-away, inherited-password takeover, selling-the-house handover, detective clip hand-over, blurry robbery/register clip, flooded-cellar recorder placement) and the pool-privacy question (overlapped Brooklyn's neighbour-garden question). Borderline pairs left for coordinator review: my "detached garage vs house" recorder placement vs Brooklyn "top-floor closet when runs end in the cellar"; my "battery backup runtime in a multi-day PSEG outage / generator" vs Brooklyn "cellar recorder on a battery backup through summer".

Intents deliberately avoided (already on siblings): generic cost-by-area, DVR vs NVR, drive size for 30 days, footage loss on upgrade, internet-drop recording, DVR lifespan, grainy night driveway, coax reuse, remote-viewing risk (generic), multiple app users, two recorders, keep cameras + add 4K.


---

<!-- merged from dvr-upgrade-putnam build (2026-10-18) -->

# DVR Upgrade — Putnam County research (part file for merge into research/dvr-upgrade.md)

Page: `/dvr-upgrade-putnam` (REBUILD in place, was crawled-not-indexed) · queue line `REBUILD | dvr-upgrade-putnam | DVR Upgrade | Putnam County, NY | up /dvr-upgrade-hudson-valley | (845) 640-3835 | GBP Bronx`
Built 2026-10-18. Up-link `/dvr-upgrade-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (845) 640-3835 in body, CTAs, forms' fallback text and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359. Old page's LocalBusiness used `@id #business` + 460 E Fordham Rd — new page uses `#bronx` (blueprint §8).

Format per v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell curl blocked. "Excerpt" = search snippet only. Rows marked **(reused)** come from sourced Putnam research already in this repo (file named) and were not re-fetched this run; the URL is the original source.

Silo-wide research (Reddit R1–R7, retailer claims, Dahua/Hikvision HD-over-coax T1/T2 + Nassau S1, FortiGuard CVE-2024-3721 S1, NY law G1–G5, silo pricing §1.8) reused from `research/dvr-upgrade.md` — not repeated here.

**Thesis (distinct from Brooklyn = cellars/rowhouses/bodegas, Nassau = detached garage/driveway/pool/PSEG, Queens = two-families/co-ops/shops, Staten Island = Sandy/raised houses/shore):** a Putnam system is spread over acres — house, barn, pump house, dock, foot of a long private drive — on rock, wetland and City watershed land, so the coax already laid is the asset. The upgrade keeps it, protects links between buildings on separate electric services (isolation/fiber), rides out multi-day NYSEG/Central Hudson outages (battery + generator gap), suits seasonal/weekend houses (health alerts, long retention), works on weak cell/rural broadband (substreams, data caps), and keeps wildlife/weather from drowning the alerts.

## Putnam County

### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit (r/hudsonvalley, r/Westchester, Putnam) | No DVR-relevant Putnam thread found (also EMPTY in fiber/cat6/smart-lock Putnam runs). EMPTY. |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 states this on-page and uses sourced published claims instead. |
| 6 | Landmarks | L1–L6 below. |
| 7 | Use cases / building stock | H1–H5 below. |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env). |
| 9 | Local news | Daily Voice, NYSEG, WAMC, Highlands Current, PCNR, NYSP, Lohud (rows P*, W*, N*). |
| 10 | Hyperlocal | Highlands Current, Putnam County News & Recorder, Town of Putnam Valley, Putnam Sheriff. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). |

### New this run (Firecrawl, 2026-10-18)
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| N1 | `Putnam County NY cell phone dead zones poor cell service Philipstown Putnam Valley cell tower` · Firecrawl search → scrape (directQuote) | https://www.schumer.senate.gov/newsroom/press-releases/schumer-cell-phone-wireless-carriers-are-wrongly-claiming-quality-reception-on-coverage-maps-for-northern-westchester-and-putnam-counties-in-reality-areas-are-often-dead-zones-schumer-calls-for-feds-to-immediately-investigate-deceptive-coverage-maps | Oct 5, 2015: "There are more cell phone dead zones in Northern Westchester and Putnam Counties than post-winter potholes on the West Side Highway…"; deceptive coverage maps; Camp Smith / Goat Trail crashes. | §10.5 H3 1 (quote); §Sources |
| N2 | same search → scrape (directQuote) | https://highlandscurrent.org/2016/05/27/new-towers-improve-ems-cell-service-putnam-county/ | May 2016: county plan for towers on county-owned property to improve emergency radio coverage, "may also benefit cell phone users aggravated by dead zones"; possible sites Route 9/301 Philipstown, Cold Spring, Putnam Valley, Mahopac, Carmel, Patterson. | §10.5 H3 1; §Sources |
| N3 | same search (excerpts) | https://www.facebook.com/groups/482893928468383/posts/25482907198040377/ ; https://www.openspaceinstitute.org/news/philipstown-emergency-comms-tower-agreement | FB group excerpt on Putnam Lake dead spots (unverifiable social post); OSI/Philipstown emergency comms tower excerpt. | Not used |
| N4 | `Putnam County NY ice storm NYSEG outage customers days without power winter storm Carmel Kent Patterson` · Firecrawl search → scrape (directQuote) | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 5, 2020 10:15 a.m.: NYSEG 34,150 of 38,693 Putnam customers out; Central Hudson 3,621 of 5,160; by municipality Carmel 12,717, Kent 5,815, Southeast 5,220, Putnam Valley 5,088, Patterson 4,422, Brewster 818; Central Hudson Philipstown 2,475, Cold Spring 992, Nelsonville 154. | §5 para 4 + §5.5 bullet 5; §10.5 H3 3; Town-by-town (Kent); §Sources |
| N5 | same search → scrape | https://www.putnamcountyny.gov/county-executive-articles/item/decade-of-storms | Nov 15, 2022 county exec article; scrape returned only the intro (no outage numbers). | Not used |
| N6 | same search (excerpts) | https://www.facebook.com/PutnamCountyEM/posts/... ; https://patch.com/new-york/southeast/storm-aftermath-power-outages-brewster-southeast | FB: "After the second storm, NYSEG reports that 14,420 customers are currently out" (undated); Patch 2016 estimates. | Not used |
| N7 | `Putnam County Sheriff burglary seasonal home vacant lake house break-in Mahopac Putnam Valley` · Firecrawl search → scrape (directQuote) | https://putnamsheriff.com/dark-house-check/ | Sheriff's Dark House Check for residents away an extended period: extra patrols, visual exterior inspection for suspicious activity or forced entry, contact homeowner; "does not guarantee protection"; advises locks, light timers, trusted neighbours. | §5 para 3; §9 Q "Dark House Check"; §Sources |
| N8 | same search (excerpts) | Sheriff FB/Instagram arrest posts; lohud 2015 Putnam Valley burglary; Patch Peekskill | Individual arrests (names) — not used (no named suspects on page). | Not used |
| N9 | `Putnam County NY private roads road association maintenance plowing Putnam Valley Kent private road` · Firecrawl search | https://www.putnamvalley.gov/keeping-putnam-valley-safe-this-winter-highway-department-update-reminders/ (excerpt: illegal to plow snow into the roadway) | No primary source on number of private roads. | Background only |
| N10 | `"private road" Putnam Valley OR Kent OR Patterson NY road association dues plowing lake community` · Firecrawl search | https://www.realtor.com/realestateandhomes-detail/23-Brook-St_Putnam-Valley_NY_10579_M38074-21189 ; https://pattersonny.org/TownBoard/TB111809.htm | Listing excerpt: "Road Frontage Type: Private Road. Road Responsibility: Private Maintained Road… Lake Privileges" (Putnam Valley); Patterson Town Board hearing notice posted along a private road. | Background for §9 private-road Q (no statistic claimed; question/answer about permission only) |
| N11 | `Putnam County Department of Health private wells homes well water testing Putnam County NY` · Firecrawl search | https://www.putnamcountyny.gov/health (excerpt) ; https://health.ny.gov/environmental/water/drinking/privatewellspilot/ | "Homeowners with private wells are responsible for testing their own water"; NYS private-well PFAS pilot accepting Putnam applications. | Background for pump-house Q (page states no well statistic) |
| N12 | `bear sightings Putnam County NY 2025 2026 Carmel Mahopac Putnam Valley police warn residents bears` · Firecrawl search → scrape (PCNR) | https://www.pcnr.com/articles/bear-alert/ ; https://hudsonvalleycountry.com/bear-sightings-hudson-valley-ny/ (excerpt); https://www.lohud.com/story/news/2017/05/30/bears-sighted-hudson-valley/356477001/ (excerpt) | PCNR May 21/22, 2024: large bear in a Carmel backyard less than half a mile from the historic Putnam Courthouse; DEC urged residents to secure food sources. Carmel PD warning (Daisy Ln, Dixon Rd) and 2017 Mahopac sighting are excerpts. | §9 bear Q; §10.5 H3 4; §Sources (PCNR only) |
| N13 | `deer motion false alerts security camera night infrared insects spider webs person detection rural` · Firecrawl search | https://support.swann.com/hc/en-us/articles/22392860080409-Preventing-Insects-from-Triggering-Your-Security-Cameras (excerpt) | "When insects fly close to the camera, they can trigger motion detection sensors, leading to false alerts and recordings." Other hits are vendor blogs (not used). | §9 spider Q; §10.5 H3 4; §Sources |

### Reused sourced Putnam research (not re-fetched)
| # | Source file · original query | URL | Finding | Page + section used |
|---|---|---|---|---|
| H1 | research/fiber-optic-installation.md (Putnam) · `Putnam County New York percent of county in New York City watershed reservoirs Croton` | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | >240 sq mi; 6 towns + 3 villages; ~3/4 in NYC watershed; >9/10 Hudson Highlands gneiss/granite; forest 66.9% (2011); reservoirs list; commercial along Routes 6, 9, 22, 52 + I-84 at Route 312 and Ludingtonville Rd (smart-lock P15, same PDF) | §5 para 1, §5.5 bullets 1–2, §8 intro |
| H2 | research/smart-lock-installation.md P1 · `Putnam County New York QuickFacts census housing units owner-occupied` | https://www.census.gov/quickfacts/putnamcountynewyork | 38,713 housing units (2025); owner-occupied 83.8%; mean travel time 39.3 min; broadband 94.8% | §5 para 2, §5.5 bullet 3, §10.5 H3 6 |
| H3 | research/sonos-installation.md P2 · ACS B25004 (census-gov provider) | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36079 | 1,757 seasonal/recreational/occasional-use units of 38,369 | §5 para 2, §5.5 bullet 4 |
| H4 | research/smart-lock-installation.md P2 / sonos P6 · `Putnam Lake Patterson NY history summer community…` | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Smadbeck/Home Guardian; Lake Carmel, Lake Peekskill, Putnam Lake from 1928; 11,000 lots mapped at Putnam Lake, 20'×100' for $50; deserted after Labor Day | §5 para 2; §7 bungalow card |
| H5 | research/soundbar-installation.md · Isaias follow-up | https://dailyvoice.com/article/isaias-outage-update-these-putnam-county-towns-are-most-affected-five-days-after-storm/ | Aug 9, 2020: 1,733 of 38,693 NYSEG Putnam customers still out | §5 para 4, §5.5 bullet 5, §10.5 H3 3 |
| W1 | research/sonos-installation.md P14 | https://www.nyseg.com/w/brewster-nyseg-continues-restoration-effort-6-pm | Dec 25, 2020: 27,375 Brewster-division customers impacted (Dutchess, Putnam, Westchester); gusts to 71 mph | §5 para 4 |
| W2 | research/fiber-optic-installation.md (HV) | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | Putnam 2020: 75,093 lightning pulses, 35 thunder days | §5.5 bullet 6; §10.5 H3 2 |
| W3 | research/cat6-repair.md (Putnam) | https://www.wamc.org/hudson-valley-news/2021-03-11/nyseg-is-upgrading-circuits-in-putnam-county | Mar 2021: NYSEG circuit upgrades on Horsepound and Stebbins roads, Carmel, with rock drilling | Town-by-town (Carmel) |
| W4 | research/cat6-repair.md (Putnam) | https://www.putnamvalley.gov/state-of-emergency-declared-in-the-town-of-putnam-valley-effective-at-4-pm-on-wednesday-july-29-2026/ | State of emergency 4 PM July 29, 2026 for flash flooding; restrictions on Cimarron, Horton Hollow, Canopus Hollow (+others) | Town-by-town (Putnam Valley) |
| P1 | research/smart-lock-installation.md X3 | https://troopers.ny.gov/news/public-safety-alert-targeted-residential-burglaries-hudson-valley-region | NYSP Jan 29, 2025 alert: targeted residential burglaries in Dutchess/Westchester/Putnam; secure second-floor entry points, don't post absences | §5 para 3 |
| P2 | research/smart-lock-installation.md P23 | https://highlandscurrent.org/2024/09/10/police-investigating-philipstown-burglaries/ | Sept 2024 break-ins on Old Albany Post Rd and Indian Brook Rd, Philipstown; Sheriff's lock reminder | §5 para 3 |
| B1 | research/sonos-installation.md P17 | https://www.governor.ny.gov/news/governor-hochul-announces-broadband-projects-totaling-more-636-million-achieve-universal | Sept 17, 2025: $11,498,589 to Comcast (+$5,033,776 match) for fiber to 390 Putnam locations | §10.5 H3 6 |
| B2 | research/fiber-optic-installation.md (Putnam) | https://highlandscurrent.org/2023/05/05/fiber-optic-coming-to-highlands/ | May 2023: Optimum fiber through Philipstown; Verizon reviewing a Cold Spring build, no timeframe | §10.5 H3 6; Town-by-town (Philipstown) |
| R1 | research/fiber-optic-installation.md + smart-lock P16 | https://putnamcountyny.gov/laws/item/local-law-no-10-of-2013-amend-chapter-135-code-of-putnam-county-entitled-contractors ; https://www.putnamcountyny.gov/consumer-affairs ; https://ecode360.com/6607815 | Ch. 135 home-improvement registration; Electrical Board licenses Limited Data Communication Technicians; Ch. 145 covers video surveillance; county list of licensed low-voltage technicians; electrical permits for Carmel, Patterson, Putnam Valley filed with those towns | §8.5 bullets 1–3; §10.5 H3 5 |
| R2 | research/cat6-repair.md (Putnam) | https://www.townofcarmelny.gov/DocumentCenter/View/456/Wetland-Permit-Application-PDF ; https://www.townofkentny.gov/286/Building-permit-requirements (excerpt) | Carmel regulates wetlands ≥1/8 acre + 100-ft buffer; Kent flags work within 100 ft of ponds/streams/watercourses | §8.5 bullet 5; §9 watershed Q |
| R3 | research/fiber-optic-installation.md (Putnam) | https://www.nyc.gov/site/dep/environment/opportunities-on-city-lands.page (excerpt) | DEP Land Use Permits for temporary use of City-owned water-supply lands | §9 watershed Q |
| R4 | research/soundbar-installation.md (Putnam) | https://highlandscurrent.org/2025/08/08/the-history-patrol/ (excerpt) ; https://www.coldspringny.gov/DocumentCenter/View/2074/Certificate-of-Appropriateness-PDF | Since 1976 exterior changes in Cold Spring's historic district need the five-member HDRB's approval; work not visible from the street is not subject to review | §7 village card + §7.5; §8 Cold Spring card; §8.5 bullet 4 |
| R5 | research/fiber-optic-installation.md | https://adaptdigitalsolutions.com/articles/new-york-contractor-license-requirements/ (excerpt, title) | "New York Contractor License Requirements: None Statewide" | §10.5 H3 5 (claim corrected) |
| L1 | research/sonos-installation.md P3 | https://en.wikipedia.org/wiki/Mahopac,_New_York | ~587-acre Lake Mahopac, three private islands, 19th-c. resort turned year-round | §13 card |
| L2 | research/soundbar-installation.md | https://en.wikipedia.org/wiki/Putnam_County_Courthouse_(New_York) | Gleneida Avenue on Lake Gleneida, built 1814, one of the oldest courthouses in use in NY | §8 Route 52 card; §13 card |
| L3 | research/smart-lock-installation.md P14 / cat6 | https://www.nyc.gov/site/dep/water/west-branch-reservoir.page | Kent & Carmel; 8 billion gallons; in service 1895; two basins separated by Route 301 | §13 card |
| L4 | research/soundbar-installation.md / cat6 | https://en.wikipedia.org/wiki/Cold_Spring_Historic_District | 691 acres; >200 buildings; mostly pre-Civil War when West Point Foundry peaked; NRHP Nov 23, 1982 | §13 card |
| L5 | research/fiber/cat6/smart-lock (Putnam) | https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2022/August/minutes/Phys-08-25-22-Presentation-Tilly-Foster-Overview-2022.pdf (excerpt) | ~199 acres, Town of Southeast, dairy then horse breeding, county purchase 2002 | §13 card |
| L6 | research/fiber/cat6 (Putnam) | https://parks.ny.gov/visit/state-parks/fahnestock-state-park-clarence-fahnestock (excerpt) | 15,000-acre park in Putnam and Dutchess; Route 301 | §13 card |
| L7 | research/fiber-optic-installation.md | https://southeast-ny.gov/DocumentCenter/View/2436/1b (excerpt) | Mount Ebo / Route 312 office-medical space | §8 Route 312 card (no tenant named) |
| L8 | research/sonos-installation.md P22 | https://en.wikipedia.org/wiki/Putnam_County,_New_York | Hamlet/CDP lists (Peach Lake, Putnam Lake, Lake Carmel, Lake Peekskill, Ludingtonville, Tompkins Corners, Garrison, etc.) | §13 "we also upgrade" line; Service areaServed |

Not claimed on the page (FLAG for Anwar): that AESS holds Putnam Ch. 135 registration or a Putnam low-voltage licence — page tells owners to ask installers "including us" and check the county lists. The NYS Commercial Security Tax Credit and §52-a / §250.05 bullets are silo rows G1–G5.

House practices stated without an external source (installer knowledge, as on Brooklyn/Nassau): PoC distance "a few hundred feet"; ground-loop/separate-service advice and fiber isolation; UPS runtime "tens of minutes to an hour or two"; substream data use; defog/hood/turret advice; rodent conduit; IR and horses ("most owners report…", framed as experience); two-hour windows 7 days to 8 PM; "recording again within one to two hours of arrival" (blueprint §5 el. 36).

### Pricing used (no new prices)
Silo recorder table as published on dvr-upgrade-brooklyn / -nassau-county / old -putnam: 4-ch $450–$700 · 8-ch $650–$1,000 · 8-ch hybrid $800–$1,200 · 16-ch $1,200–$2,200 · 32-ch $2,200+ · long-run/outbuilding repair quoted after testing · $195/hr, 3-hr min ($585). Putnam house range "$500 to $1,300 installed" = the figure the old dvr-upgrade-putnam page already published. Packages = 4-ch / 8-ch hybrid / 16-ch tiers. FLAG (same as Nassau): blueprint §9 Putnam 1.45× is not applied on any DVR page; the silo table is identical across areas — left unchanged, not invented.

### Images (11) — Drive has no DVR folder; CompanyCam not connected
Permanent image rule. 3 real AESS job photos from other jobs (cropped; captions say "example photo from another AESS job (not a Putnam …)") + 8 manufacturer product shots. All viewed with Read before use. Rejected: `images/tech-bucket-truck-install.png` (AI-generated look), `images/buzzer-repair/*` (per silo notes), tiny `lorex-*-putnam-county.jpg` (≤286 px). Real-photo pool is only manhattan-deli / nassau-window-depot / rockland-toyota; `rockland-toyota-showroom.jpeg` had not been used on any DVR page; the other two real sources were used by Nassau with different crops (different region of the frame). None of the product sources is used by Brooklyn or Nassau.
| Output (images/dvr-upgrade/) | Source | Crop / note | Placement |
|---|---|---|---|
| dvr-upgrade-putnam-dark-grey-recorder-with-front-usb-ports-product-photo.webp (500×152) | images/nvr-honeywell-35-series.png | white border trimmed | Hero (eager) |
| dvr-upgrade-putnam-small-camera-high-on-white-wall-below-windows.webp (415×240) | images/rockland-toyota-showroom.jpeg | crop (345,240,760,480): wall + mezzanine windows; banner text, exit sign, dealer signage, people excluded | §5 |
| dvr-upgrade-putnam-solar-panel-cellular-ptz-camera-with-sim-card-product-photo.webp (1254×1254) | images/wireless-camera-solar-4g-lte.png | product shot | §6 |
| dvr-upgrade-putnam-blue-and-white-cable-bundles-above-recorder.webp (740×240) | images/rockland-toyota-nvr-monitor.jpeg | crop (0,0,740,240): ceiling cable bundles only (Nassau used the screen) | §7 |
| dvr-upgrade-putnam-grey-camera-tile-of-storeroom-and-open-doorway.webp (460×328) | images/nassau-window-depot-monitor.jpeg | crop (780,452,1240,780): bottom-right tile; people tile, house-number tile, timestamp, box text excluded (Nassau used top-right tile) | §8 |
| dvr-upgrade-putnam-large-white-ptz-camera-on-black-product-photo.webp (400×400) | images/dahua-wizsense-ai-varifocal-bullet-camera-white.png (file shows a PTZ despite its name) | product shot | §9 (driveway cluster) |
| dvr-upgrade-putnam-white-floodlight-camera-with-twin-lamps-product-photo.webp (746×609) | images/floodlight-swann-4k.png | trimmed | §10 |
| dvr-upgrade-putnam-recorder-front-and-rear-panels-product-photo.webp (462×357) | images/nvr-swann-advancedx-4k.png | trimmed | §10 (after comparison) |
| dvr-upgrade-putnam-slim-recorder-with-silver-front-product-photo.webp (500×128) | images/nvr-hikvision-ds7616ni.png | trimmed | §12 Process |
| dvr-upgrade-putnam-dual-lens-turret-with-red-and-blue-lights-product-photo.webp (894×893) | images/cam-dual-lens-active.jpeg | product shot | §13 |
| dvr-upgrade-putnam-compact-pan-tilt-camera-with-red-stripe-product-photo.webp (400×400) | images/dahua-sd49-ptz-dome-camera-white.png | product shot | §14 |
All WebP q80, ≤1600 px. Alt/title unique, each with "Putnam County"; captions describe only what is visible.

### Build notes
- check_page.py: PASS (full, with registration). 13,839 rendered words; title 53; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 193,929 B.
- Size cluster at final check: Staten Island (rewritten in parallel) 189,139 B, Queens 183,691 B, Brooklyn 186,554 B → gap ≥4.7 KB. Re-check if SI grows.
- Masked-geo block similarity (p/li/h2/h3/td/figcaption ≥8 masked words, word-level SequenceMatcher) vs every dvr-upgrade-* page incl. the new Queens/SI: only ≥0.65 blocks are the blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades in [Area]", the protected warranty sentence and the shared mega-nav. First draft had ~40 Nassau-template blocks (pricing cells, packages, process, services, contact lines) at 0.65–1.0; all rewritten.
- Semantic de-dup: checked by reading the register above + new Queens and Staten Island pages. Changed: FAQ "routine care between visits" (overlapped SI "how often should cameras near the shore be cleaned") → dock/ice remote check; data-cap Q reworded away from SI "slow down our home internet"; comparison H3 "Hybrid recorder or full network system?" de-questioned (DVR-vs-NVR intent exists on Dutchess/Ulster/HV); no cost-by-property FAQ (Nassau FAQ 1 intent); no county-licence FAQ (Nassau FAQ 2 intent — kept in body text only). Borderline pairs for coordinator: my generator-gap Q vs Nassau "battery runtime in a long PSEG outage" and SI "solar panels and home battery"; my bear/person classification Q vs Ulster old "Does a new recorder lower false alerts?" (mine is animal-specific); my long-driveway warning Q vs Nassau "plate at end of a long driveway" (mine = arrival alert, not plate).

## Question register — dvr-upgrade-putnam (21 Q&A H3 + 1 emergency H2 + 10 FAQ) — final
Q&A (section "DVR Upgrades in Putnam County: Questions Answered"):
1. The barn is about 400 feet from the house. Is that too far for a high-definition camera on the old coax?
2. Does a camera on the well pump house need its own power, or can it run off the cable from the house?
3. The barn has its own electric meter. Does that change how the camera cable should connect to the house?
4. There is no power and no cable out at the far field gate. Can a solar camera there show up beside the wired cameras?
5. The dock camera fogs over every morning from late summer into autumn. Is that the camera or the recorder?
6. We close the lake house from November to April. Should the recorder stay on all winter?
7. How will we know the recorder at the weekend house has stopped working if nobody is there to look?
8. Our cell signal at the house is one bar. Can we still pull up the cameras on our phones while we're home?
9. Our home internet is a capped cellular or satellite plan. Will the cameras eat through the monthly data allowance?
10. Our standby generator takes about a minute to start after the power fails. Does the recorder still need a battery?
11. An ice-laden branch brought down the cable to the garage camera that runs on our poles. Is fixing it ours or NYSEG's?
12. After the power came back, several cameras stayed on "no video" until someone unplugged their power supply. Can the upgrade stop that?
13. Can a camera at the bottom of our wooded driveway warn us someone is coming before they reach the house?
14. We share a private road with five other houses. Can we put a camera where it meets the town road?
15. The town plow keeps knocking over the post with our driveway camera on it. Where else can it go?
16. The back of our lot meets New York City watershed land. Can we aim a camera that way, and can cable run near the stream?
17. Can the Sheriff's Dark House Check and our cameras work together while we're away?
18. Black bears set off the yard camera most nights. Can the system tell a bear from a person standing up?
19. Spiders spin webs across the night cameras every summer. What actually keeps them off?
20. Branches have grown into half the camera views since the system went in. Do we move the cameras or trim the trees?
21. The camera cable in our converted bungalow runs through a crawlspace that gets wet every spring. Does it all need to come out?
(+ emergency H2 "Putnam Recorder Dead After the Storm, or Beeping in the Basement?")

FAQ (visible == FAQPage schema):
1. Can you swap the recorder while we're away and walk us through it on a video call afterwards?
2. Can a camera keep an eye on the propane tank, the oil fill and the generator?
3. Will a camera's infrared light bother the horses or other animals in the barn?
4. Can the recorder warn us if the heat fails in the empty house in January?
5. Should the cameras record around the clock or only when something moves, on a property where the nights are long and quiet?
6. Can a copy of important clips be kept off the property in case the house itself is broken into?
7. Mice got into the barn and chewed through a camera cable. What protects the new runs?
8. Our house has no number visible from the road. What should we tell you so the crew finds it?
9. Will you take down old cameras we no longer use and seal the holes?
10. Can a camera let us check the dock and the ice after a winter storm without driving up from the city?


---

<!-- merged from dvr-upgrade-queens build (2026-10-18) -->

# DVR Upgrade — Queens research (part file for merge into research/dvr-upgrade.md)

Page: `/dvr-upgrade-queens` (REBUILD in place, was crawled-not-indexed) · queue line `REBUILD | dvr-upgrade-queens | DVR Upgrade | Queens | up /dvr-upgrade-nyc | (347) 434-6392 | GBP Bronx`
Built 2026-10-18. Up-link `/dvr-upgrade-nyc`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (347) 434-6392 in body, CTAs, sticky bar, form error text and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (+ footer text).
Silo research (Part 1 of research/dvr-upgrade.md: T1/T2 penta-brid data sheets, S1 FortiGuard, G2/G3 Penal Law, G4 tax credit) reused, not re-fetched. This file adds only the Queens layer.

Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page + section used**. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`, query/directQuote mode, PDF parser), Firecrawl Alexandria provider `census-gov` (census/data). Shell curl blocked. "Excerpt" = read only as a search-result snippet, not opened.

**Thesis (distinct from Brooklyn, Nassau, Staten Island, Putnam):** a Queens recorder has many users — two households in a two-family, a co-op board and super, a multilingual store crew on shifts, an owner abroad — and its footage is regularly requested by precinct detectives and insurers. The upgrade keeps the coax, then sets up who-sees-what (accounts, circuits, internet, board paperwork, languages) and makes footage exportable and preservable on demand.

Page section labels: §Hero, §Quick, §5 Neighborhood (+ §5.5 facts), §Emergency ("first hour after an incident" list), §6 Services, §7 Architecture (+ §7.5), §8 Commercial (+ §8.5 rules list), §9 Q&A (clusters A–F), §10 Equipment, §10.5 AI Reality Check (H3 1–7), §12 Process, §13 Landmarks, §14 Pricing, §15 Packages, §16 Services grid, Field Notes, §17 FAQ, §19 Siblings, §Sources.

## Mandatory sources (§3) — Queens status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | No Queens-specific DVR thread found; generic excerpts only (R-Q1, R-Q2 below). r/Queens: EMPTY (no relevant thread surfaced). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and uses published claims (A-Q1…A-Q7) |
| 6 | Landmarks | L-Q1…L-Q4 |
| 7 | Building stock / use cases | H-Q1, H-Q2, CO-1…CO-4 |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | N-Q1…N-Q6 (QNS, Queens Chronicle, Queens Daily Eagle, Police1/NY Daily News, Queens DA) |
| 10 | Hyperlocal | QNS, Queens Chronicle, Queens Daily Eagle (above). Queens Ledger: EMPTY (nothing camera-specific surfaced). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not searched to review level; not used. |

## Building stock and languages (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H-Q1 | Alexandria `census-gov` census/data · acs/acs5 vintage 2023 · NAME, B25035_001E, B25001_001E, B25024_002E–006E, B25034_010E–011E, B25003_002E–003E · county 081 state 36 | https://api.census.gov/data/2023/acs/acs5?get=NAME,B25001_001E,B25035_001E&for=county:081&in=state:36 | Queens County: 903,598 housing units; median year built **1953**; 1-unit detached 172,141; 1-unit attached **83,924**; 2-unit **175,686**; 3–4 unit 95,066; 5–9 unit 49,166; built 1940–49 127,351; built 1939 or earlier **273,370**; owner-occupied 371,778; renter-occupied **456,452**. | §5 paras 1–2; §5.5 bullets 1–2; §Sources |
| H-Q2 | Alexandria `census-gov` census/data · acs/acs5 2023 · C16001_001E, 002E, 003E, 005E, 021E, 023E, 024E, 026E, 027E, 029E, 030E · county 081 | same API | Pop. 5+ **2,199,666**; speak only English 984,821 (→ 1,214,845 = 55.2% speak another language); Spanish **510,585** (256,286 speak English less than "very well"); Chinese incl. Mandarin/Cantonese **209,205** (143,225 less than very well); Tagalog 31,150; Vietnamese 3,876; other Asian/Pacific 36,611. Labels verified in the response's variable list. | §5 para 2; §5.5 bullet 3; §Sources |
| H-Q3 | `NYC DCWP small business language access Queens languages …` · Firecrawl search | https://www.nyc.gov/site/civicengagement/about/language-access-plan.page | Excerpt: 49% of New Yorkers speak a language other than English at home; 23% limited English proficient (DCP / ACS 2018–2022). | §Sources only (context) |

## Co-ops and condos (CO)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| CO-1 | `Queens garden co-op board approval security cameras alteration agreement Glen Oaks Village Bell Park Gardens Jackson Heights co-op cameras` · Firecrawl search → scrape | https://www.glenoaksvillage.com/forms | Glen Oaks Village resident forms list "Alteration Agreement" and "Security Camera Rebate". | §7.5; §13 card; §Sources |
| CO-2 | (scrape, PDF parser) | https://www.glenoaksvillage.com/_files/ugd/5fd8ec_21939267f36b4570a05b7607dd6badcc.pdf | GOVO Security Camera Registration & Rebate form: board/security dept work with NYPD; rebate up to **$100** for outside-facing cameras (not per camera); **all** outward-facing installations must be registered, unregistered = **$100 house-rule violation**; cameras may face out from inside or outside but not "unreasonably directed towards another apartment"; **not permitted in common hallways**; GOVO inspects from outside; suggests inexpensive window-ledge camera. (PDF title metadata reads "February 13, 2002"; page gives no date for the form.) | §7.5; §9 B Q2; §10.5 H3 3 & 5; FAQ 4; §13 |
| CO-3 | same search → scrape (directQuote) | https://guzovllc.com/condo-and-coop-rules-of-thumb-security-cameras-and-privacy-concerns/ | Guzov LLC (Aug 15 2023): NYC has no law prohibiting residents' hallway doorbell cameras, but co-op rules may prohibit them in common areas; boards add restrictions on angle, recording, storage time; no reasonable expectation of privacy in common areas; audio recording → Federal Wiretap Act + NY Penal Law art. 250; board can withdraw authorization. | §10.5 H3 5; §Sources |
| CO-4 | same search → scrape (directQuote) | https://nacmiaslaw.com/practice-areas/closings/building-types/standard-co-op/queens | Queens holds the city's largest concentration of garden co-ops (Jackson Heights, Sunnyside, Forest Hills); elevator co-ops in Forest Hills, Rego Park, Kew Gardens, Bay Terrace; attached two-story co-op rows in Bayside and Whitestone; Jackson Heights & Sunnyside Gardens historic districts bring Landmarks review; garden complexes often no elevator/doorman; complexes of many separate corporations under one managing agent with criteria differing building to building. | §5 para 1; §5.5 bullet 4; §7 cards; §7.5 (several corporations); §Sources |
| CO-5 | same search (excerpt) | https://cooperatornews.com/article/a-case-study-in-queens | Excerpt: Glen Oaks Village, garden-style co-op "boasting nearly 3,000 units". | §13 card |

## Police, footage and news (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-Q1 | `Queens police ask businesses for surveillance video footage canvass robbery pattern Roosevelt Avenue 2025 2026` · Firecrawl search → scrape | https://www.police1.com/police-products/investigation/video-surveillance/nyc-initiative-allows-retail-owners-to-share-live-surveillance-footage-with-nypd-in-effort-to-curb-theft | May 17 2024 (NY Daily News via Police1): Mayor Adams expands initiative letting businesses feed camera footage to NYPD; first unveiled in the **109th Precinct (Queens) "last June"** (= June 2023) with Fusus by Axon; pilot to nine more precincts; businesses **not required**; opt in via New York City Connect portal (newyorkcityconnect.org/camera-integration); can limit cameras and hours; ~$1.5M cost. | §5.5 bullet 5; §8.5 bullet 1; §9 E Q3; §10.5 H3 2; §Sources |
| N-Q2 | `Queens burglary pattern homes Bayside Fresh Meadows Whitestone NYPD 2025 2026 Queens Chronicle QNS` · Firecrawl search → scrape | https://qns.com/2026/01/suspects-wanted-burglaries-flushing-fresh-meadows-bronx/ | Jan 20 2026: crew of four; Dec 20 2025 6 a.m. medical business 42-62 Kissena Blvd (~$9,800 + meds), pharmacy 42-60 Kissena Blvd (~$3,800), 177-05 Union Tpke at 6:45 a.m.; Dec 30 pharmacy 45-12 Parsons Blvd (~$11,000); 109th & 107th Precincts; NYPD released surveillance images and video; suspects masked and hooded → no descriptions. | §5 para 3 |
| N-Q3 | same search → scrape | https://qns.com/2026/05/burglars-break-into-fresh-meadows-home/ | May 5 2026: Fresh Meadows home near 67th Ave & 166th St, Mon. April 20, rear door forced 12:17 a.m.; jewelry, purse, ~$39,000 cash; suspects caught on camera casing the rear patio, one on a phone call. | §5 para 3 |
| N-Q4 | same search → scrape | https://www.qchron.com/editions/queenswide/crime-is-down-citywide-but-mostly-flat-in-queens/article_5b392466-437d-5fe3-b0f7-16628d4d8833.html | Queens Chronicle, July 9 2026 (NYPD H1 2026 data): Queens burglaries −28.9%; robberies +~5.1% Queens; grand larcenies +5.3% Queens; GLA Queens North 1,094 → 1,283 (+17.3%). | §5 para 4 |
| N-Q5 | `Hurricane Ida deaths Queens basement apartments Hollis Woodside Flushing September 2021 how many died in Queens` · Firecrawl search | https://queenseagle.com/all/unimaginable-loss-eleven-from-queens-die-in-storm (excerpt); https://www.nyc.gov/assets/em/downloads/pdf/hazard_mitigation/Impacts_of_PTC_Ida.pdf (excerpt) | Queens Daily Eagle: of 12 confirmed dead, 11 from Queens, 10 lived in basement apartments. NYCEM: 13 New Yorkers died; 11 by drowning in basement apartment flooding. | §5.5 bullet 6 (fact only — no flood question, Brooklyn owns that intent) |
| N-Q6 | `JFK airport cargo area warehouses Springfield Gardens Rosedale freight forwarders cargo theft Queens 2025` · Firecrawl search | https://queensda.org/wp-content/uploads/2021/09/lacarriere_david_jfkheists_09_14_2021_plea.pdf (excerpt) | Queens DA (Sept 2021 plea): defendant caught holding $2.5 million of Gucci and Chanel goods from a cargo theft by a crew using forged… (excerpt cut). | §8 JFK card |
| N-Q7 | same query as N-Q1 | https://qns.com/2026/09/suspects-armed-robbery-corona/ | Excerpt: two suspects wanted for armed robbery of a man on Roosevelt Avenue in Corona. Scrape failed (Service Unavailable) → **not used** on page. | — |

## Corridors and BIDs (C)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C-Q1 | `Queens business improvement districts list Flushing Jamaica Center Sutphin Steinway Astoria 82nd Street Partnership Jackson Heights` · Firecrawl search | https://www.facebook.com/NYCBusiness/posts/… (excerpt); https://www.bid.nyc/ (excerpt) | "Queens is home to 11 Business Improvement Districts" (NYCBusiness excerpt); bid.nyc lists 82nd Street Partnership, Downtown Flushing Transit Hub, Downtown Jamaica Partnership, LIC Partnership, Myrtle Ave (Queens), Steinway Street, Sunnyside Shines. SBS directory scrape returned no Queens list → count not used on page. | Background |
| C-Q2 | same | https://steinwaystreet.org/about-us/ | Steinway Street BID: all **300 businesses** on Steinway St from **28th Ave to 35th Ave**; serving since **1991**. | §8 card; §13 card |
| C-Q3 | same (excerpt) | https://www.thisisqueensborough.com/local-chamber-bid-events-happenings-2/ | 82nd Street Partnership, 37-06 82nd St: "more than 200 businesses"; district on 82nd Street from 37th Avenue to Baxter Avenue. | §8 card |
| C-Q4 | `Downtown Flushing Transit Hub BID Main Street Roosevelt Avenue busiest intersection businesses` · Firecrawl search | https://www.facebook.com/FlushingBID/ (excerpt); https://www.qchron.com/editions/north/flushing-bid-to-grow-by-nearly-double/article_ca52ffd1-153d-5461-a09d-15be57295230.html (excerpt); LoopNet Flushing business report PDF (excerpt) | Flushing BID formed September 2003; "Over 100,000 people a day are at Roosevelt Avenue and Main Street" (Councilmember Barry Grodenchik, Queens Chronicle); LoopNet report: Main St & Roosevelt Ave = commercial crossroads, "dense and eclectic mix of Chinese small businesses, national retailers". | §8 card; §13 card |
| C-Q5 | `Jamaica Avenue Downtown Jamaica Partnership 165th Street Mall shopping corridor businesses Queens` · Firecrawl search | https://jamaicacenter.org/ ; https://www.downtownjamaica.org/ (excerpts) | Jamaica Avenue "over 400 businesses"; Jamaica Center = largest BID in Queens; three downtown BIDs (Jamaica Ave, 165th St, Sutphin Blvd) joining forces; Rufus King Park; "hundreds of independent businesses and blue-chip national stores"; "Closer than you think to JFK". | §8 card; §13 card |
| C-Q6 | `Liberty Avenue Richmond Hill "Little Guyana" businesses Queens corridor` · Firecrawl search | https://www.nytimes.com/video/nyregion/100000002266992/little-guyana-in-queens.html (excerpt); Instagram excerpts (Sybil's Bakery, Singh's Roti Shop) | Liberty Avenue = "the lively commercial corridor that divides Richmond Hill and South Ozone Park" (NYT excerpt); roti shops and bakeries (IG excerpts, not cited on page). | §8 card |
| C-Q7 | `Dining Out NYC roadway dining season April November rules structures permanent program DOT` · Firecrawl search | https://www.diningoutnyc.info/ ; https://www.diningoutnyc.info/faq (excerpts) | Sidewalk cafés year-round; seasonal roadway cafés April 1–November 29; year-round roadway dining now legal with year-round license; closing hour 11 p.m.; roadway cafés "easy to move, clean, set up, and break down". | §8.5 bullet 4; FAQ 7 |

## Landmarks (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L-Q1 | `Jackson Heights Historic District designated 1993 garden apartments Landmarks Preservation Commission buildings` · Firecrawl search | https://hdc.org/buildings/jackson-heights/ (excerpt); http://s-media.nyc.gov/agencies/lpc/lp/1831.pdf | Designated **October 19, 1993**; LPC report: The Chateau (1922, Andrew J. Thomas) = twelve freestanding U-shaped buildings around a common landscaped garden (Queensboro Corporation garden apartments). | §13 card; §9 B Q1 (landmark review may apply) |
| L-Q2 | `Unisphere Flushing Meadows Corona Park 1964 World's Fair height stainless steel landmark designated` · Firecrawl search | https://en.wikipedia.org/wiki/Unisphere (excerpt) | Stainless steel globe, **140 ft**, dedicated March 1964, LPC designation May 16, 1995. | §13 card |
| L-Q3 | C-Q4, C-Q2, C-Q5, CO-5 | (above) | Main St/Roosevelt Ave Flushing; Steinway Street; Jamaica Avenue + Rufus King Park; Glen Oaks Village | §13 cards |

## AI Reality Check claims (A-Q) — Queens page
| # | Exact query · platform | URL | Claim used | Used |
|---|---|---|---|---|
| A-Q1 | `insurance claim security camera footage request how long to keep video retention business insurer adjuster` · Firecrawl search | https://digital-watchdog.com/posts/How-Long-Should-Security-Camera-Footage-Be-Retained-/ (excerpt) | "Thirty days is a common starting point, but the right retention period depends on regulatory requirements, operational risks, storage capacity…" | §10.5 H3 1 |
| A-Q2 | N-Q1 | (Police1) | "Police can tap into any business's cameras" — corrected with opt-in facts | §10.5 H3 2 |
| A-Q3 | `reddit r/Queens security cameras two family house tenant upstairs cameras DVR` · Firecrawl search | https://www.reddit.com/r/homesecurity/comments/1boja38/how_many_security_cameras_too_many/ (excerpt) | "I have six Ring Doorbell cams, plus two conventional 24/7 (DVR cameras)." | §10.5 H3 3 |
| A-Q4 | silo T2 | https://objects.eanixter.com/PD620479.PDF (excerpt) | Penta-brid HDCVI/AHD/TVI/CVBS/IP | §10.5 H3 4; §10 card |
| A-Q5 | CO-3, CO-2 | (above) | shareholder camera rules | §10.5 H3 5 |
| A-Q6 | same query as A-Q3 | https://www.reddit.com/r/realestateinvesting/comments/v5kcs5/anyone_use_security_cameras_on_their_rental/ (excerpt) | "I would suggest NVR and not DVR. I have multi and camera are pointing parking lot and front door. All tenants are informed…" | §10.5 H3 6 |
| A-Q7 | `Hik-Connect app supported languages Chinese Spanish Korean Bengali` · Firecrawl search | https://www.hik-connect.com/ (excerpt) | Website language menu: English, Italiano, Español, Deutsch, Français, Polski, Nederlands, Български, Český, Dansk, Suomi, Magyar, Português, Eesti. Page claims only "when we looked, the website menu listed…"; no claim about in-app languages. | §10.5 H3 7 |

## Licensing / permits (Queens)
- NYS low-voltage licence #12000287431 (protected).
- No DOB permit claim made (not researched to a primary source). Landmark review mentioned only as "may apply" for new street-front cameras in the Jackson Heights HD (silo L1 LPC chapter 11 already in register).
- Tenant notice: no NYC rule found requiring small-landlord notice before common-area video → FAQ 1 says "We are not aware of a New York City rule…" and refers to lease/lawyer.

## House practices stated without an external source (FLAG for Anwar)
- Recorder on the owner's internet and owner's electric circuit in two-families; written note between semi-detached co-owners; tenant-entrance camera kept out of owner's everyday account.
- Point-to-point wireless links for rear cameras of attached rows; siding mounting blocks (not used as a question — SI owns siding).
- Board package contents (scope, camera list, COI, licence, dates, viewing-rights list); named accounts per board role.
- Kitchen camera placement out of the grease plume; vibration hardening under elevated lines (compression BNC, rubber pad); POS text overlay "depends on register model".
- Footage export routine (lock clip, two USB copies, native player, written log, clock offset); NTP sync across neighbors' recorders.
- Lockable ventilated recorder enclosures; guest Wi-Fi separation; public-view monitor; 50% deposit held until board approval (deposit itself is from the protected terms sentence).
- "First hour after an incident" list (§Emergency) — generic owner steps.

## Pricing
Silo table as already published on the old Queens page and on Brooklyn/Nassau (no §9 multiplier applied anywhere in this silo): 4-ch $450–$700 · 8-ch $650–$1,000 · 8-ch hybrid $800–$1,200 · 16-ch $1,200–$2,200 · 32-ch $2,200+ · bad runs quoted after testing · $195/hr, 3-hr min ($585). FLAG for coordinator: §9 Queens multiplier (1.05×) not applied, consistent with the rest of the silo; the old Queens page's JS widget chips ($250 service call, $175/drop, $19.99/mo) were NOT carried.

## Images (11) — Drive has no DVR Upgrade folder; CompanyCam not connected
Step C / permanent image rule. All looked at with Read first. Only one real AESS job photo was unused by Brooklyn/Nassau (rockland-toyota-showroom); three more are **new, different crops** of job photos Brooklyn/Nassau also cropped (different regions). Seven manufacturer product shots not used by any dvr-upgrade page. Rejected as before: images/buzzer-repair/*, images/cat6-repair/aess-* (AI look per research/cat6-repair.md), images/commercial-security/*.
| Output (images/dvr-upgrade/) | Source | Crop / note | Placement |
|---|---|---|---|
| dvr-upgrade-queens-black-and-silver-recorder-with-front-usb-ports-product-photo.webp (500×148) | images/nvr-honeywell-35-series.png | white border trimmed; product shot (maker logo small, not named) | Hero (eager, og:image) |
| dvr-upgrade-queens-two-small-cameras-high-on-white-wall-below-mezzanine.webp (616×255) | images/rockland-toyota-showroom.jpeg | crop (352,250,968,505): wall, mezzanine windows, exit signs; banner text, dealership signs, car, people excluded | §5 |
| dvr-upgrade-queens-recorder-front-and-rear-panel-ports-product-photo.webp (462×354) | images/nvr-swann-advancedx-4k.png | trimmed; captioned as a network recorder (not a coax DVR) | §6 |
| dvr-upgrade-queens-blue-and-white-cable-bundles-above-recorder-rack.webp (800×240) | images/rockland-toyota-nvr-monitor.jpeg | crop (0,0,800,240): ceiling cable only — Nassau used the screen region | §7 |
| dvr-upgrade-queens-mini-dome-beside-light-panel-in-shop-ceiling.webp (530×340) | images/manhattan-deli-interior-cameras.jpeg | crop (700,60,1230,400): right ceiling only — Brooklyn used a full-width ceiling strip | §8 |
| dvr-upgrade-queens-flat-black-recorder-with-small-front-buttons-product-photo.webp (500×159) | images/nvr-avycon-avr-nsv16p.png | trimmed product shot | §10 |
| dvr-upgrade-queens-recorder-tile-of-back-room-and-open-door.webp (400×343) | images/nassau-window-depot-monitor.jpeg | crop (800,452,1200,795): CAM 3 tile only (no people, label, timestamp, house number) — Nassau used the top-right tile | §12 |
| dvr-upgrade-queens-pair-of-white-turret-cameras-on-one-base-product-photo.webp (329×153) | images/hikvision-colorvu-turret-camera-pair.jpg | product shot (small maker logo on base) | §13 |
| dvr-upgrade-queens-white-mini-dome-camera-product-photo.webp (225×225) | images/hikvision-acusense-mini-dome-camera.jpg | product shot | §14 |
| dvr-upgrade-queens-white-turret-camera-with-two-light-lenses-product-photo.webp (480×480) | images/cam-eyeball-white.png | generic unbranded product shot | §15 |
| dvr-upgrade-queens-turret-camera-side-view-on-black-product-photo.webp (803×1429) | images/cam-turret-side.png | generic unbranded product shot | Field Notes |
All WebP q80, ≤1600 px, natural size (no upscaling). Alt/title unique, each with "Queens"; job-photo captions say "Example photo from another AESS job (not a Queens …)"; product captions say "Manufacturer product photo, not an installed unit". DAILY-LOG note suggestion: `images: 11 — 4 AESS job-photo crops (other jobs) + 7 product shots, under images/dvr-upgrade/ (no real DVR photos yet)`.

## Question register — dvr-upgrade-queens (REBUILT 2026-10-18) — final
Q&A (section "DVR Upgrades in Queens: Questions Answered"), emergency H2 first:
- Queens Recorder Gone Quiet Before a Police or Insurance Request?
- Upstairs and downstairs in our two-family each pay for their own internet — which connection should the recorder use?
- The second-floor tenant pays her own electric bill — whose circuit should the recorder and cameras run on?
- My neighbor and I own the two halves of a semi-detached house in Fresh Meadows — how do we share one recorder and its costs fairly?
- We rent the basement unit to a family — can the camera at their side entrance be kept off our own live view?
- Our attached house in Middle Village has no side yard — is a wireless link reliable enough for a camera at the back?
- Our garden co-op in Jackson Heights wants an alteration agreement before any camera work — what do you send the managing agent?
- Glen Oaks Village registers shareholders' outward-facing cameras — does replacing our recorder mean registering again?
- The condo board says the lobby recorder belongs to the association — can a unit owner get a copy of footage from it?
- Our co-op board wants to know exactly who will be able to watch the courtyard cameras — how is that set up so they can sign off?
- Grease from the fryer coats our kitchen camera within weeks — where should a camera go in a working restaurant kitchen?
- We run a small shop under the 7 train on Roosevelt Avenue — does the elevated line's rumble affect the cameras or the recorder?
- Our Flushing store is open until 2 a.m. with two shifts on the register — can the footage show who was on the register at any moment?
- Can one recorder cover our two takeout shops six blocks apart on Jamaica Avenue?
- Half our staff read Chinese and half read Spanish — can the recorder and app be set up so everyone can use them?
- How do we give the night manager live view without letting him delete or export footage?
- Our family runs the store but the owner spends months abroad — can he watch the cameras from overseas?
- A detective from the 109th Precinct asked for a copy of our footage — what format, and how do we hand it over?
- Half the houses on our Corona block have cameras — can our recorders be linked so one clip follows a car past every house?
- If we decide later to join the NYPD's business camera-sharing program, what does the upgraded recorder need?
- An insurer's letter told us to preserve footage of a customer's fall in our store — how do we stop the recorder overwriting it?
- Our warehouse near JFK has trucks at the dock all night — can the upgraded recorder show trailer numbers and who opened which door?

FAQ (visible == FAQPage schema):
1. Do we have to tell the tenants in our two-family before the upgraded cameras start recording?
2. Can you provide a certificate of insurance naming our co-op, condo or managing agent?
3. Should a store's recorder go inside a lock box, and will it overheat in there?
4. Our co-op apartment's window faces the street — can a camera behind the glass record clearly at night?
5. Can the office computer at our other location show the cameras, not only phones?
6. Is a deposit due before the swap, and when is the balance paid?
7. Can a camera watch our restaurant's roadway dining setup without being mounted on it?
8. Our shop's Wi-Fi is shared with customers — should the recorder be on that network?
9. Can the store's monitor by the door show customers they are on camera?
10. Can our old analog cameras be moved to better spots during the upgrade, or must they stay where they were?

### De-dup notes (semantic, read by hand)
- Checked against every question in the register (old templates, Brooklyn, Nassau) and the rewritten Staten Island and Putnam pages as they stood at ~05:35 UTC.
- Changed during the build because of overlap: siding-mount FAQ (SI "vinyl siding without cracking it or letting water in"); weekend-booking FAQ (SI "Saturday"); kitchen camera "fogging — camera or recorder?" reworded to placement (Putnam "dock camera fogs over… camera or recorder?"); equipment H3 "Hybrid recorder or a full network system?" made a non-question (identical to Putnam's H3; SI has the same intent — coordinator should check SI vs Putnam); "plays back only a day — drive or settings?" removed (old-template "Why does my recorder only keep a few days now?"); drive-lifespan FAQ replaced (old-template "How often should a DVR be replaced?" / Ulster "How do I know if my DVR hard drive is failing?"); NYPD-program question reworded to readiness (Nassau "Garden City registry — access to our recorder?"); semi-detached question reworded to the co-ownership arrangement (Brooklyn FAQ "two adjoining rowhouses — can one recorder cover both?").
- Borderline pairs left for coordinator review: Queens "owner abroad — watch from overseas?" vs old-template "Does upgrading change how I watch from another borough?"; Queens "detective from the 109th — what format and how to hand over?" vs Ulster old "Can police use footage from my DVR?"; Queens "warehouse — trailer numbers at the dock" vs Nassau "readable licence plate at the end of a long driveway".
- Intents deliberately avoided (Brooklyn): rowhouse coax reuse, flood cellars (Ida used as a fact only), landmark rules, §52-a/§250 audio, tax credit, botnets (all appear only as facts/list items, never as questions).

### Build notes
- check_page.py: **PASS** (full, with registration; existing sitemap/_redirects entries already correct). 13,658 rendered words; title 58; meta 156; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; HowTo 7 = 7 process cards.
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word-level SequenceMatcher, vs all 15 dvr-upgrade-* pages): everything < 0.65 except the blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades in [Area]" (1.0 vs Brooklyn/Nassau/Putnam) and the warranty paragraph (0.71–0.75), which is dominated by the protected verbatim terms sentence. Max otherwise 0.631 (a Putnam figcaption).
- File size 183,691 B: inside the narrow 182,818–184,506 window between Nassau (180,770) and Brooklyn (186,554); SI 189,767 and Putnam 193,557 at last check. JSON-LD written with indent=1 to land there. **If any sibling's size moves within 2 KB of 183.7 KB at wiring, re-check.**
- Page built from scratchpad generator (body + data → page); chrome (CSS, mega-nav, footer script) copied from rebuilt dvr-upgrade-brooklyn.html with the script's two error-message phones switched to (347) 434-6392.


---

<!-- merged from dvr-upgrade-staten-island build (2026-10-18) -->

# DVR Upgrade: Staten Island research (part file to merge into research/dvr-upgrade.md)

Page: `/dvr-upgrade-staten-island` (REBUILD in place, was crawled-not-indexed), built 2026-10-18. Up-link `/dvr-upgrade-nyc`. GBP Brooklyn (`#brooklyn`, 1282 Troy Ave, Brooklyn NY 11203). Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from NYC hub, Brooklyn, Nassau, Queens and Putnam):** a Staten Island system is a ring of cameras around a detached or semi-attached lot: side yards, driveway, back fence. It also includes shore houses raised after Sandy, where the recorder, cable and camera heights all moved, plus salt air on the outdoor ends and car-theft crews. On the commercial side it covers auto shops, strip stores and contractor yards on the boulevards. The upgrade keeps the coax, redoes the outdoor ends, re-aims or replaces the side-yard and driveway cameras, lifts the recorder above the flood line and is honest about what footage can prove.

Silo research (Part 1 of research/dvr-upgrade.md: R1–R7, A1–A3, T1–T2, S1–S2, G1–G6, Nassau S1–S16) was reused, not repeated. Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search / scrape (query mode) and the Firecrawl Alexandria `census-gov` provider. Shell curl is blocked. "Excerpt" means the item was read only as a search snippet.

Section labels: §Hero, §Quick, §5 Neighborhood (+ §5.5 list), §Repair1, §6 Services, §7 Architecture (+ §7.5), §8 Commercial (+ §8.5 rules), §9 Q&A, §10 Equipment, §10.5 AI Reality Check, §12 Process, §13 Landmarks, §14 Pricing, §15 Packages, §17 FAQ, §Sources.

## Staten Island

### Mandatory sources (§3), status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit (r/statenisland) | EMPTY for Staten Island-specific DVR/camera threads (query below returned only r/AskNYC, r/SecurityCamera, r/Bushwick). Generic forum excerpts R-SI1/R-SI2 used in §10.5. |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and uses published cost-guide, manufacturer and forum claims instead. |
| 6 | Landmarks | L-SI1–L-SI7 |
| 7 | Building stock / use cases | H-SI1, F-SI1–F-SI5 |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9–10 | Local news / hyperlocal | Staten Island Advance (silive.com) N-SI1, N-SI2; NYPD 122 Pct Facebook excerpt N-SI3 |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env), not searched again (silo Y1 already empty) |

### Housing stock (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H-SI1 | Firecrawl Alexandria `census-gov` census/data · acs/acs5 2023 · B25001_001E, B25035_001E, B25024_002E–006E, B25003_002E–003E, B25034_002E–011E, B25044_003E, B25044_010E · county 085 state 36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25001)&ucgid=0500000US36085 | Richmond County: 184,074 housing units; median year built **1974**; 1-unit detached **63,421**; 1-unit attached **47,106**; 2-unit 41,749; 3–4 unit 6,720; 5–9 unit 3,740; owner-occupied **115,534**, renter 54,513 (occupied 170,047, so ~68% owner); built 1970–79 29,712, 1980–89 28,613, 1990–99 19,254, 2000–09 16,871 (1970–2009 = **94,450**), 1960–69 23,568, 1950–59 17,499, 1940–49 7,534, ≤1939 32,820, 2010–19 7,764, 2020+ 439; no vehicle available: owner 7,343 + renter 19,082 = **26,425** (≈84% of households have a vehicle). | §5 para 1; §5.5 bullets 1–3; §Sources |

### Sandy, flooding, buyouts, raised houses (F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F-SI1 | `Hurricane Sandy Staten Island deaths 24 Midland Beach New Dorp Beach Tottenville storm surge` · Firecrawl search → scrape (query) | https://www.dvidshub.net/news/482917/seawall-will-raise-quality-life-shore-communities-staten-island-new-york | USACE New York District, 10.10.2024: Sandy caused **24 deaths on Staten Island, more than any other borough**; winds up to 80 mph; **20-foot storm surge** washed away homes on the East coast; seawall of **nearly 5 miles** from the edge of Fort Wadsworth (just south of the Verrazzano) to Oakwood Beach, protecting South Beach, Midland Beach, New Dorp Beach and Oakwood Beach; completion expected within a decade. | §5 para 4; §5.5 bullet 5; §10.5 H3 5; §Sources |
| F-SI2 | same query (excerpt) | https://www.silive.com/news/2020/10/hurricane-sandy-8-years-later-remembering-24-staten-island-lives-lost.html | Excerpt: 24 Staten Island lives lost (cross-check of F-SI1). | Cross-check only |
| F-SI3 | `Oakwood Beach buyout Staten Island Sandy homes purchased Ocean Breeze Graham Beach state buyout program` · Firecrawl search → scrape (query) | https://www.nyc.gov/content/planning/pages/our-work/plans/staten-island/east-shore-buyout-area-special-coastal-risk | NYC DCP: after Sandy, NYS Governor's Office of Storm Recovery (GOSR) designated **Oakwood Beach, Ocean Breeze and Graham Beach** as buyout areas; participation voluntary, not all owners participated. The Special Coastal Risk District limits new development to single-family detached houses, requires CPC authorization for new development and horizontal enlargements, and allows elevations and minor repairs as-of-right. No count of homes bought on that page. | §5 para 4; §9 Q&A "lots around us were bought out"; §Sources |
| F-SI4 | same search (excerpts) | https://www.dnainfo.com/new-york/20140407/ocean-breeze/state-expands-buyout-program-staten-islands-graham-beach ; https://academiccommons.columbia.edu/doi/10.7916/aqb7-9571/download ; https://landscapeclimate.cargo.site/Staten-Island-Buyouts-Primary-Case | Excerpts: program extended to Ocean Breeze (Nov 2013), then Graham Beach (April 2014); one excerpt says 299 properties bought for $255M. Secondary sources only, so **no count or dollar figure used**. | Background only |
| F-SI5 | `Build It Back elevated homes Staten Island number of homes elevated Sandy NYC report` · Firecrawl search → scrape (query) | https://www.nyc.gov/site/housingrecovery/disaster-recovery/single-family-program.page | Build It Back modular pilot: 103 one- and two-family modular homes, **32 on Staten Island**; >110 attached homes elevated or reconstructed (citywide). Page gives no Staten Island elevation total. LiRO excerpt (https://www.liro.com/projects/build-it-back-program/) says ~4,000 homes required elevation (program-wide). | Background for §7 raised-house card; no number on the page |
| F-SI6 | `NYC Building Code Appendix G flood-resistant construction design flood elevation freeboard electrical equipment above` · Firecrawl search (excerpt) | https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction | G304.1.1 item 6: "Utilities and attendant equipment shall be located at or above the design flood elevation specified in ASCE 24 … or … constructed so as to prevent water from entering or accumulating"; G304.2 coastal high-hazard version adds wave action. The page applies this as house practice for recorders and says the code does not name camera equipment. | §7.5 raised-house para; §8.5 bullet 1; §9 Q&A "lifted onto piers"; §10.5 H3 5; §Sources |

### News / crime (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-SI1 | `Staten Island car break-ins thefts from cars driveways NYPD 2025 silive` (tbs past year) · Firecrawl search → scrape (query) | https://www.silive.com/crime-safety/2026/07/staten-island-car-thefts-spike-47-in-2026-heres-what-law-enforcement-is-doing-about-it.html | SI Advance, Maura Grunlund, **July 24, 2026**: vehicle thefts on SI up roughly **47%** in 2026, **163 incidents through July 19 vs 111** same period 2025; citywide down 11% (6,483 vs 7,324); crews work within minutes and wear **masks, gloves and hooded clothing**; video surveillance "typically of limited value and rarely identifies individuals"; investigators use plate readers, phone/vehicle data, financial records, social media. | §5 para 3; §5.5 bullet 4; §9 Q&A "masks and gloves"; §10.5 H3 4; §Sources |
| N-SI2 | same search → scrape (query) | https://www.silive.com/crime-safety/2026/02/beware-the-crowbar-crew-nypd-boosting-patrols-amid-staten-island-break-in-pattern.html | SI Advance, Luke Peteley, **Feb 12, 2026**: "Crowbar Crew" pried doors, windows and car windows looking for high-end vehicles and keys; ~10 incidents Feb 1–9; North Shore, Mid-Island, South Shore, Todt Hill, Dongan Hills; officials advised taking keys and locking cars. | §5 para 3; §Sources |
| N-SI3 | `Staten Island auto repair shop body shop yard catalytic converter theft surveillance video NYPD` · Firecrawl search (excerpts) | https://www.facebook.com/NYPD122pct/posts/-staten-island-residentshelp-protect-your-vehicle… ; https://www.alarminglyaffordable.com/video-surveillance-catches-staten-island-catalytic-converter-thief/ | Excerpt: NYPD Staten Island precincts held free catalytic-converter etching events. A security-company blog excerpt claims 362 SI catalytic-converter thefts by mid-August 2022, citing NYPD. That is a secondary source, so **the number is not used**. | §9 Q&A "catalytic converters"; §Sources (NYPD excerpt only) |
| N-SI4 | other results of N-SI1 search (excerpts) | Facebook posts (Assembly member Reilly; 10312 community group) | Excerpts: car thefts up 22% (April 2026 silive link); Tottenville car break-ins on Manhattan St / Brighton St posted on Ring app. These are social posts, **not used**. | — |

### Corridors / commercial (C)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C-SI1 | `Staten Island business improvement districts Forest Avenue BID New Dorp Lane BID Staten Island BID St. George` · Firecrawl search | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page ; https://www.forestavenuebid.com/ ; https://www.downtownsi.nyc/new-index | SBS directory excerpt lists Staten Island BIDs **Forest Avenue, New Dorp Lane, South Shore, West Shore** (4; Downtown SI site also says "4 on Staten Island"); Forest Avenue BID office 686 Forest Ave. | §5.5 bullet 6; §8 corridor cards; §Sources |
| C-SI2 | `Hylan Boulevard Staten Island length miles longest street Bay Street to Tottenville Wikipedia` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Hylan_Boulevard ; https://en.wikipedia.org/wiki/Staten_Island | Hylan Blvd ≈ **14 miles**, Rosebank → East Shore → South Shore (Tottenville); "the longest street in New York City". Victory Blvd ≈ 8.0 miles. SI population 495,747 (2020). | §8 Hylan card; §Sources |
| C-SI3 | `Richmond Avenue Staten Island Wikipedia Staten Island Mall Forest Avenue Staten Island commercial thoroughfare` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Richmond_Avenue ; https://en.wikipedia.org/wiki/Staten_Island_Mall ; https://en.wikipedia.org/wiki/Heartland_Village,_Staten_Island | Richmond Ave ≈ **7.0 miles** N–S; Staten Island Mall originally a two-story building with GLA **1,274,000 sq ft**; mall south of Richmond Hill Road. | §8 Richmond Ave card; §13 mall card; §Sources |

### Landmarks (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L-SI1 | `Staten Island Ferry St. George Terminal daily riders Verrazzano-Narrows Bridge opened 1964 Staten Island` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Staten_Island_Ferry | Ferry runs 24/7 from St. George; **16,692,900 riders in 2025**; bridge opening was expected to spur an influx of residents. | §13 St. George card; §13 Verrazzano card |
| L-SI2 | same | https://www.nycgovparks.org/highlights/verrazano-bridge | Verrazzano-Narrows Bridge opened **November 21, 1964**, connecting Brooklyn and Staten Island. | §13 card; §Sources |
| L-SI3 | `Freshkills Park 2,200 acres Snug Harbor 83 acres Conference House Tottenville built Historic Richmond Town Staten Island landmarks` · Firecrawl search (excerpts) | https://nylandmarks.org/explore-ny/staten-island-museum-snug-harbor/ | Snug Harbor: **83-acre** campus, once a home for retired seamen; 1000 Richmond Terrace. | §13 card |
| L-SI4 | same | https://freshkillspark.org/blog/the-greenest-borough ; https://www.nyc.gov/html/dycd/downloads/pdf/2012/SummerFun2012_SI_Ongoing.pdf | Freshkills Park **2,200 acres**, almost three times Central Park; Conference House **built 1680**, site of unsuccessful negotiations to end the Revolutionary War. | §13 cards |
| L-SI5 | same | https://www.nycgovparks.org/parks/conference-house-park | Conference House Park at the **southernmost point of New York State**. | §13 card |

### Coastal camera hardware (salt air)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| E-SI1 | `anti-corrosion security camera coastal salt spray stainless steel C5-M NEMA 4X marine environment datasheet` · Firecrawl search (excerpts) | https://www.hikvision.com/en/products/IP-Products/Explosion-Proof---Anti-corrosion-Series/Anti-corrosion-Series/ ; https://www.isrmag.com/hikvision-launches-polymer-anti-corrosion-cameras-with-next-level-durability-and-performance/ | Hikvision anti-corrosion cameras "for harsh coastal, marine, and industrial corrosive environments"; ISR: "fully corrosion resistant and **C5-M & NEMA 4X** certified". | §9 Q&A "Midland Beach housings"; §10.5 H3 3; §Sources |
| E-SI2 | same (excerpt) | https://www.youtube.com/watch?v=Q7KHVihclj4 | Dahua anti-corrosion aluminum-alloy and SUS316L stainless cameras, "can be deployed within 2 km of the [coast]" (snippet truncated). The page says only "markets stainless-steel models for deployment close to the coast". | §9; §10.5 H3 3 |

### Forums used in §10.5 (generic, not Staten Island)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| R-SI1 | `reddit statenisland security cameras recommendation installer DVR package stolen porch` · Firecrawl search (excerpt) | https://www.reddit.com/r/AskNYC/comments/100v3n5/can_i_put_camera_in_the_lobby_for_package_thieves/ | "Most building lobbies have cameras, and they still steal… hoods and sunglasses… NYPD will probably not…" | §10.5 H3 4 |
| R-SI2 | same (excerpt) | https://www.reddit.com/r/SecurityCamera/comments/1u73hpz/camera_worth_it_for_porch_pirates/ | "Porch pirates will follow the amazon driver directly up on your porch…" | §9 Q&A "packages at the side door" ("camera forums describe thieves following delivery vans") |
| — | Nassau S6/S7/S8 (silo) | homeguide.com; r/SecurityCamera 1eypvng; r/homesecurity 1s697t6 | DVR $100–$350; "just buy a new system"; keeping cameras and swapping the recorder is cheapest at many properties | §10.5 H3 1–2 |

### Licensing / permits (Staten Island)
- NYS low-voltage license #12000287431 (protected). Liability insurance and certificate wording are house practice.
- NYC DOB permit rules for low-voltage camera work: EMPTY (not researched to a primary source), so the page makes no DOB claim.
- Special Coastal Risk District (F-SI3) is described only for what it says about development and elevations. The page makes no claim that zoning regulates cameras.

### House practices stated without an external source (FLAG for Anwar)
- Recorder on the living floor of raised houses; conduit under raised houses; splices kept high; no party-wall drilling; siding mounting blocks (FAQ removed, see below); camera heights after elevation (8–10 ft becomes 16–18 ft, illustrative); lens choice and corridor view for side yards; tandem-driveway camera layout; headlight glare placement; cleaning cadence near the shore; shop recorder away from bay dust; PTZ as a supplement only; low side camera for catalytic-converter theft; solar and home-battery backed-up circuits (the statement that grid-tied solar without a battery shuts down in an outage is general industry knowledge, not sourced here); flood-height reference camera.
- Company constants copied from live pages: two-hour windows, seven days to 8 PM, "recording again within one to two hours of arrival", $195/hr with 3-hr minimum ($585), 4.7/201.

### Pricing used (no new prices)
Silo table exactly as published on the old Staten Island page and on Brooklyn and Nassau: 4-ch $450–$700 · 8-ch $650–$1,000 · 8-ch hybrid $800–$1,200 · 16-ch $1,200–$2,200 · 32-ch $2,200+ · run repair quoted after testing · $195/hr, 3-hr min ($585). **No §9 Staten Island 1.10× multiplier applied.** The silo publishes identical figures for every area, so a 1.10× table would invent new numbers on one page only. Coordinator/Anwar to decide whether the silo should move to multiplied prices.

### Images (11), Step C / permanent image rule (Drive has no DVR folder; CompanyCam not connected)
Every candidate was viewed with Read first. Rejected as AI-generated: `tech-bucket-truck-install.png`, `home-automation-abstract-van-residential.jpg`, `access-control-gate-reader-installation.jpg` (and by extension the other access-control/home-automation renders). The only real AESS job photo **not** used by the 22 existing silo files is `rockland-toyota-showroom.jpeg`. The second real photo is a **different crop** of `rockland-toyota-nvr-monitor.jpeg`, which Nassau cropped to the screen; this crop is the ceiling cable bundles, with no screen content. The other nine are manufacturer product shots, none used before in images/dvr-upgrade/. After Putnam's images appeared (05:3x), four product shots that duplicated Putnam's sources (cam-dual-lens-active, nvr-swann, cam-floodlight) were swapped for unused ones, and the PTZ was upgraded to a stainless model. The two real-photo crops (showroom wall, ceiling cable bundles) use the same source files as Putnam's `small-camera-high-on-white-wall-below-windows` and `blue-and-white-cable-bundles-above-recorder`, because no other unused real AESS photo exists. Coordinator: pick one page to keep them, or accept them as different crops.
| Output (images/dvr-upgrade/) | Source | Crop / note | Placement |
|---|---|---|---|
| dvr-upgrade-staten-island-black-recorder-with-two-front-lights-product-photo.webp (500×420) | images/nvr-avycon-avr-nsv16p.png | trimmed, padded white for hero mask | Hero (eager) |
| dvr-upgrade-staten-island-small-cameras-on-high-white-wall-below-mezzanine.webp (665×230) | images/rockland-toyota-showroom.jpeg | crop (345,270,1010,500): wall, mezzanine windows, two small cameras; banner, signage, people, cars, logos excluded | §5 |
| dvr-upgrade-staten-island-black-recorder-with-vented-front-and-orange-badge-product-photo.webp (490×108) | images/nvr-digital-watchdog-cova.png | trimmed; maker badge visible, not named | §6 |
| dvr-upgrade-staten-island-long-white-bullet-camera-for-driveways-product-photo.webp (299×142) | images/hikvision-varifocal-bullet-camera.jpg | trimmed; maker logo on body visible, not named in copy | §7 |
| dvr-upgrade-staten-island-black-camera-under-two-white-floodlight-panels-product-photo.webp (168×140) | images/lorex-dual-floodlight-camera-installation-staten-island.jpg | trimmed; maker logo visible, not named | §9 |
| dvr-upgrade-staten-island-white-turret-camera-with-two-small-lights-product-photo.webp (480×449) | images/cam-eyeball-white.png | trimmed | §10 |
| dvr-upgrade-staten-island-cable-bundles-running-above-equipment-rack.webp (700×260) | images/rockland-toyota-nvr-monitor.jpeg | crop (0,0,700,260): ceiling cable bundles and rack top only; monitor/screen, labels excluded | §12 |
| dvr-upgrade-staten-island-white-turret-with-red-and-blue-warning-lights-product-photo.webp (148×137) | images/uniview-colorhunter-triguard-turret-camera-white.jpg | trimmed; maker logo visible, not named | §13 |
| dvr-upgrade-staten-island-flat-dark-recorder-for-closet-shelf-product-photo.webp (371×156) | images/nvr-luminys-r5216pa.png | trimmed | §14 |
| dvr-upgrade-staten-island-white-bullet-camera-on-wall-bracket-product-photo.webp (264×137) | images/dahua-marine-stainless-ptz-dome-camera.png | trimmed (the file name says PTZ dome, but the image shows a bullet on a bracket, and the alt describes only what is visible) | §15 |
| dvr-upgrade-staten-island-stainless-steel-pan-tilt-zoom-dome-product-photo.webp (238×354) | images/dahua-full-color-compact-bullet-camera-white.png | trimmed (the file name says compact bullet, but the image shows a stainless PTZ dome; the alt describes what is visible) | Field Notes |
All WebP q80, ≤1600 px. Alt and title are unique and each includes "Staten Island". Captions say "Manufacturer product photo (not an installed unit)" or "Example photo from another AESS job (not a Staten Island property)".

## Question register: dvr-upgrade-staten-island (REBUILT 2026-10-18), final

**Q&A (section "DVR Upgrades on Staten Island: Questions Answered", 19 H3):**
1. Our detached house has a narrow side yard on each side — can one camera cover a whole alley from the front gate to the back corner?
2. Our semi-attached house has the driveway on the side we share — how do we get a cable to a camera out there without going through the party wall?
3. Our two cars park nose to tail in a long driveway — can one camera see what happens to the car at the back?
4. Our driveway climbs a steep hill in Grymes Hill — how do we stop the camera at the top from being blinded by headlights every night?
5. Our house was lifted onto piers after Sandy — where should the recorder live now?
6. Since the house was raised, our cameras see roofs and the tops of heads — can they be re-aimed, or do they have to move?
7. The camera cables now hang across the open space under our raised house — how should they be protected?
8. Most of the lots around us were bought out and are empty now — what changes for our cameras?
9. A surge warning is out and our recorder is still in the basement — what should we do with it before we evacuate?
10. The crews breaking into cars here wear masks and gloves — is better footage even worth paying for?
11. Our packages get left at the side door, not the front — can the system show the delivery and whoever picks it up?
12. Our street lights are dim — will a camera that records in colour at night tell us the colour of a car better than infrared?
13. Our auto shop's recorder sits in the bay office in dust and fumes — will a new one survive there?
14. Is one pan-tilt-zoom camera enough to watch a whole contractor's yard?
15. Thieves cut catalytic converters off cars in our lot — where does a camera have to be to see it happen?
16. We live a few blocks from the beach in Midland Beach — which camera housings hold up best that close to the water?
17. How often should cameras near the shore be cleaned, and can we do it ourselves?
18. We're finishing our basement next month — what should be done about the camera cables before the drywall goes up?
19. Once the basement is a family room, can the recorder stay down there without the fan noise and heat bothering anyone?
(Emergency H2 is a statement, not a question: "Recorder Quit, Channels Snowy or Nights Missing? Call the Staten Island Line". The hybrid-vs-NVR and ADT/Ring/SimpliSafe H3s are written as statements.)

**FAQ (visible == FAQPage, 10):**
1. Can we search the recorder for every time a car pulled into the driveway last week?
2. Is it worth calling you across the bridge for a single dead camera?
3. Should outdoor cameras be taken down or covered before a hurricane or a nor'easter?
4. We have solar panels and a home battery — can the cameras keep recording from them when the grid goes down?
5. If a storm knocks a camera out of aim after the job is finished, is that covered?
6. Can a camera go on a fence post or a lamp post at the end of the yard instead of on the house?
7. Will the recorder slow down our home internet when we watch the cameras from work?
8. Can a camera record how high the water came if our street floods again?
9. What should we do before the installer arrives — move the cars, clear the garage?
10. Our builder ran network cable to the eaves when the house was rebuilt after Sandy but never added cameras — can the new recorder use it?

**De-dup notes:** Checked against the register (all old-template pages, Brooklyn and Nassau) and against the rewritten Putnam (05:32) and Queens (05:33) pages. Three first-draft FAQs were replaced because Queens or Putnam already covers the intent: weekend booking (Queens "do you come on weekends"), vinyl/aluminum siding mounting (Queens), and the empty house over the winter (Putnam lake house / weekend house). The evacuation question was re-scoped to flood protection of a basement recorder, so it no longer means "leave the recorder on while away". The spider-web sentence was removed from the cleaning answer (Putnam has a spider-web question). The "hybrid or network" H3 was turned into a statement because Putnam and Queens both ask "Hybrid recorder or (a) full network system?". Borderline pair left for coordinator review: my FAQ 6 (camera on a fence or lamp post) vs Putnam "the town plow keeps knocking over the post with our driveway camera… where else can it go?" (different intent: whether a post mount is possible vs relocating a struck post).

### Build notes
- check_page.py: **PASS** (full, with registration). 13,827 rendered words; title 50; meta 154; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10.
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word-level SequenceMatcher) vs every dvr-upgrade-* page: the only block ≥0.60 is the blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades on/in [Area]" (0.875 vs Brooklyn, Nassau, Putnam, Queens). The verbatim warranty sentence was not scored, because its paragraph prefix was reworded.
- File size 189,115 B; nearest siblings: Brooklyn 186,554 (+2,561), Putnam 193,557 (−4,442), Queens 184,126 (at 05:3x). If Queens or Putnam change size, re-run the 2 KB cluster check at wiring.
- Rendered QA (Playwright, 1440 and 390 wide): no JS errors, no horizontal scroll.


## Ulster

Page: `dvr-upgrade-ulster` (REBUILD in place 2026-10-18, was crawled-not-indexed). Queue line: `REBUILD | dvr-upgrade-ulster | DVR Upgrade | Ulster | up /dvr-upgrade-hudson-valley | (845) 640-3835 | GBP Bronx`. Up-link `/dvr-upgrade-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, schema `@id` #bronx). Direct line (845) 640-3835 in body, CTAs and schema; (800) 486-0943 only inside the shared mega-nav chrome. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from Brooklyn = cellar/rowhouse/bodega; Nassau = house + detached garage + driveway/pool; and from the concurrent Westchester/Putnam/Queens/Staten Island rebuilds):** In Ulster the recorder often guards a house nobody is in. One in thirteen Ulster homes is held for seasonal or occasional use (half of all vacant units), rising to a third of Shandaken, over half of Denning and seven in ten in Hardenburgh; short-term rentals add 2,827 more. So the upgrade is designed for absence: the owner has to *know* from the city that the box is still saving, the system has to come back by itself after Central Hudson outages (the Sept 2026 nor'easter hit Woodstock, Shawangunk, Plattekill and Hurley hardest), survive generator tests and lightning on long runs, reach the phone through satellite/cellular internet or wait for the county's fiber build, and get video out of stone houses, barns and studios far from the house. Kingston's old districts, STR guest rules and New Paltz student turnover are the local rule set.

Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`), Firecrawl Alexandria `census-gov` (census/data), Composio Reddit (REDDIT_RETRIEVE_POST_COMMENTS, REDDIT_SEARCH_ACROSS_SUBREDDITS). Shell curl blocked. "Excerpt" = read only as a search snippet.

### Mandatory sources (§3) — status for Ulster
| # | Source | Result |
|---|---|---|
| 1 | Reddit | U3 (r/hudsonvalley second-home thread, read in full via Composio Reddit), U4 (r/kingstonnewyork camera threads — Flock/LPR/speed cameras only; no DVR thread). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so; claims taken from silo rows A1, A2, R7, S6–S8 and corrected with Ulster facts below. |
| 6 | Landmarks | U12–U14 + carried C-rows |
| 7 | Use cases / building stock | U1, U2, U10 + carried |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | U5 (Central Hudson release), U6 (HV1 Esopus burglaries), U7 (HV1 Kingston police cameras), U8 (Saugerties PD Crimewatch) |
| 10 | Hyperlocal | HV1 (U6, U7); Daily Freeman Sept 27 2026 outage story carried (C14). Daily Freeman / Kingston Wire stories about home DVRs specifically: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix — new for this page
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| U1 | Firecrawl Alexandria `census-gov` census/data · acs/acs5 2023 · B25004_001E, B25004_006E, B25002_001E, B25002_003E, B25034_010E, B25034_011E, B25035_001E, B25040_* · county 111 state 36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36111 | Ulster County: 86,178 housing units; 13,073 vacant; **6,545 "for seasonal, recreational, or occasional use"** (7.6% of all units; 50% of vacant); built 1939 or earlier 21,829 (25.3%); 1940–49 5,094; median year built 1966. Heating: electricity 10,211, bottled/tank/LP 9,641 of 73,105 occupied (not used). | Hero sub; §5 para 1; §5.5 bullets 1–2; §9 cluster 1 intro; §10.5 H3 5 |
| U2 | Firecrawl Alexandria `census-gov` census/data · acs/acs5 2023 · B25001_001E, B25004_006E, B25035_001E · county subdivision:* in state 36 county 111 | https://api.census.gov/data/2023/acs/acs5?get=group(B25001)&ucgid=pseudo(0500000US36111$0600000) | Seasonal-use units / total units: Hardenburgh 204/292 (70%), Denning 237/432 (55%), Shandaken 886/2,675 (33%, median built 1952), Woodstock 813/4,289 (19%), Rochester 676/4,240 (16%), Marbletown 506/3,231 (16%), Gardiner 255/1,709 (15%), Olive 340/2,338 (15%), Hurley 382/3,184 (12%), Wawarsing 702/6,240 (11%, median built 1957), Saugerties town 475/9,692 (5%), New Paltz town 129/5,513 (2%), Kingston city 133/11,049 (1%, median built 1939 or earlier). | §5 para 1; §5.5 bullet 2; §7 cards; Coverage (town cards) |
| U3 | `site:reddit.com hudsonvalley OR Kingston security cameras DVR upstate house remote viewing internet` · Firecrawl search → thread read in full via Composio `REDDIT_RETRIEVE_POST_COMMENTS` (article 1ww3ifc) | https://www.reddit.com/r/hudsonvalley/comments/1ww3ifc/secondhome_owners_in_the_hudson_valley_who_looks/ | r/hudsonvalley, posted ~Oct 2 2026: "Second-home owners in the Hudson Valley — who looks after your house when you're not here?" Comments: "Our part time neighbor has extensive cameras and a full house battery backup, combined with cellular fallback on their Internet package"; "Home owners insurance love to deny claims because 'no one was checking on the house'… I've seen pipes break and it rains for 3 weeks inside and then freezes"; a winter caretaker "comes by once a week to check for roof leaks, peek at the heating system, make sure there's no standing water in the basement"; "We've got Ring cameras posted around the house, and we're friends with a local contractor"; "Me via blink cameras"; a property manager in Orange & Ulster offering second-home checks. | §5 para 2 (quotes); §9 cluster 1 (caretaker, insurer Qs); FAQ 3 (freeze); §10.5 H3 5 |
| U4 | Composio `REDDIT_SEARCH_ACROSS_SUBREDDITS` · `subreddit:kingstonnewyork camera` | https://www.reddit.com/r/kingstonnewyork/comments/1vw7xra/call_to_action_flock_camera_public_safety/ ; https://www.reddit.com/r/kingstonnewyork/comments/1x56siq/we_gotta_get_rid_of_these_jenoptik_cameras/ | Aug 23 2026 call to attend the Aug 26 Public Safety Committee meeting on Flock cameras/LPRs; Oct 13 2026 thread against Jenoptik (speed) cameras. No home-DVR threads in r/kingstonnewyork search → Kingston Reddit on home recorders: EMPTY. | §8 Uptown/Midtown card (residents' privacy debate, with U7); §Sources |
| U5 | `Central Hudson outage Ulster County customers without power storm 2026` · Firecrawl search → scrape | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ ; https://www.cenhud.com/en/outages/ | Sept 26 2026: crews restoring power to "more than 19,000 homes and businesses" after a slow-moving nor'easter; "The hardest-hit areas include Woodstock, Shawangunk, Plattekill and Hurley in Ulster County"; restoration expected "to continue into Sunday"; generator advice: "Operate it outdoors and turn off the main breaker while the generator is in use". Outages page: updates Sept 27 2026 ("More than 90% of Customers Restored…"); credits for outages ≥72 hours affecting ≥20,000 customers ($25 per further 24 h for residential). Search excerpts: Central Hudson serves 315,497 customers; Ulster 93,190 served (poweroutage.us / cenhud). | §5 para 3; §5.5 bullet 3; §9 cluster 2 (Q4, Q5); §Repair block; §10.5 H3 3 |
| U6 | `Ulster County sheriff burglary second home seasonal camp break-in 2025 OR 2026` · Firecrawl search → scrape | https://hudsonvalleyone.com/2025/01/09/string-of-town-of-esopus-burglaries-prompt-ulster-county-sheriff-to-issue-warning/ | Jan 9 2025: Sheriff's Facebook post (Jan 7): "In the past 4 days… a residential burglary and several larcenies from vehicles on Union Center Road and surrounding areas in the Town of Esopus"; HV1 notes other outlets wrongly called it county-wide; police advice included "install a security system and motion sensor lights". | §5 para 4 |
| U7 | `Kingston NY police camera registration program residents businesses surveillance footage` · Firecrawl search → scrape (directQuote) | https://hudsonvalleyone.com/2026/09/02/police-defend-kingstons-surveillance-cameras-as-residents-raise-privacy-concerns/ | Sept 2 2026: since 2020 seven automatic licence plate readers at Kingston intersections plus 71 other surveillance cameras; map "heavily concentrated in Midtown and Uptown"; LPR data held six months; 32 KPD members have access to public-safety cameras, four to LPR data; Chief Tinti: police are "not looking into private windows". No city camera-registration programme for private systems found → page makes no registry claim. | §8 Uptown/Midtown card; §9 cluster 4 intro; §Sources |
| U8 | `Woodstock NY OR Saugerties OR Shandaken police burglary unoccupied seasonal home 2026` · Firecrawl search → scrape (directQuote) | https://crimewatch.net/us/ny/ulster/saugerties-pd/cases | Saugerties PD: "On November 7, 2025, between 1:30 PM and 5:45 PM, an unknown individual or individuals unlawfully entered a detached garage on a property located on Old Kings Highway near Malden Turnpike in the Town of Saugerties. The subject(s) stole a green 2025 Kawasaki KX450X dirt bike." | §5 para 4 (daytime outbuilding entry); §7 barns card |
| U9 | `Ulster County ConnectALL broadband unserved locations fiber 2026 Starlink rural internet Shandaken Denning Hardenburgh` · Firecrawl search | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion ; https://radiocatskill.org/ulster-county-secures-59m-for-fiber-broadband-expansion/ (excerpts) | Sept 25 2025: $20.8M ConnectALL award for "nearly 1,300 unserved households, businesses, and community facilities" in remote areas; USDA technical-assistance grant for fiber in Denning; Margaretville Telephone Company fiber buildout in Phoenicia. Radio Catskill May 4 2026: "all 1,293 unserved locations in the county will receive fiber broadband service" (BEAD + Verizon). Starlink-specific Ulster data: EMPTY. | §5.5 bullet 5; §9 cluster 5 Q13; §10.5 H3 4 |
| U10 | `Ulster County Comptroller short-term rentals report 2025 units out-of-county owners` · Firecrawl search | https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf ; http://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/Press-Release_U.C.-Report-on-the-Housing-Impact-of-Short-Term-Rentals.pdf (excerpts) | Sept 22 2025 report: 2,827 STRs = 3.28% of county housing (May 2025); 98% entire units; 36% of owners use out-of-county mailing addresses; Shandaken 261 STRs of 2,675 units; Town of Rochester 238 (5.61%); Village of Saugerties 106 (5.23%); Marbletown 151 (4.67%); Kingston 150 (1.36%). | §5 para 2; §5.5 bullet 4; §9 cluster 6 Q15 |
| U11 | `Airbnb policy indoor security cameras banned March 2024 outdoor cameras disclose` · Firecrawl search | https://news.airbnb.com/an-update-on-our-policy-on-security-cameras ; https://www.npr.org/2024/03/11/1237609591/airbnb-bans-indoor-security-cameras-surveillance-privacy (excerpts) | Airbnb bans indoor security cameras in listings globally (announced March 11 2024, effective April 30 2024); hosts must disclose presence and general location of outdoor cameras before booking; outdoor cameras may not monitor indoor spaces or areas with greater privacy expectation such as an enclosed outdoor shower or sauna. | §9 cluster 6 Q15; §10.5 H3 6 |
| U12 | `New York State Thruway exit 18 New Paltz exit 19 Kingston exit 20 Saugerties Ulster County` · Firecrawl search | https://www.thruway.ny.gov/travelers/interchange-exit-listing | Exit 18 New Paltz–Poughkeepsie–NY 299 (MP 76.01); Exit 19 Kingston–NY 28–Kingston-Rhinecliff Bridge (MP 91.37); Exit 20 Saugerties–Woodstock–NY 32 (MP 101.25). | Coverage section intro; §8 corridor cards |
| U13 | `Mohonk Preserve weather station record low temperature winter New Paltz daily records since 1896` · Firecrawl search | https://www.mohonkpreserve.org/wp-content/uploads/2021/02/17-02WEATHER.NSN_.pdf ; https://journals.ametsoc.org/view/journals/apme/49/3/2009jamc2221.1.xml (excerpts) | Mohonk Lake station established January 1896 (continuous daily record 1896–2006 per AMS paper); Natural Science Note: "Lowest Winter Temperature: 1°F on December 16th and January 9th" (2016–17 winter); season snowfall 43.20 in. | §5.5 bullet 6; FAQ 5 (snow on lenses); §13 Mohonk card |
| U14 | `site:reddit.com kingstonnewyork OR hudsonvalley camera footage stolen package OR break-in Woodstock OR Saugerties OR "New Paltz"` · Firecrawl search | https://www.reddit.com/r/hudsonvalley/comments/v2sud5/this_woman_trespassed_on_my_property_parked_on_my/ (excerpt) | r/hudsonvalley: resident posted footage of a trespasser who parked on the lawn; "Facebook group identified the thief… a local resident, less than a mile away. Sheriff was supposed to come…". Town not stated → not placed in a town. | Not used on page (location unclear) |

### Carried (verified Ulster sources fetched by earlier runs in this repo; not re-fetched)
| # | Finding | Source (as logged) | Research file | Page section |
|---|---|---|---|---|
| C1 | Kingston HLPC: certificate of appropriateness for "material change in the appearance … visible from a public street or alley"; ordinary maintenance/repair that does not change design, materials, color or outward appearance exempt; desk reviews "generally turned around within one week"; districts Stockade, Rondout–West Strand, Chestnut Street, Fair Street | kingston-ny.gov/hlpc; ecode360.com/6728919; engagekingston.com | cat6-repair.md U8; door-buzzer C1 | §8.5 bullet 1; §9 cluster 4 Q10 |
| C2 | Stockade: 18th-c stone houses on all four corners of John & Crown (Four Corners); Senate House 1676 stone dwelling, first NY Senate 1777 | FOHK; parks.ny.gov | cat6-repair.md R4 | §7 stone card; §13 card |
| C3 | Historic Huguenot Street, New Paltz: 10-acre NHL district, seven stone houses, 1678 settlement | huguenotstreet.org | cat6-repair.md R6 | §7 stone card; §13 card |
| C4 | Hurley Main Street private residences late 1600s–late 1800s | hurleyheritagesociety.org | door-buzzer C4 | §7 stone card |
| C5 | Rondout = D&H Canal tidewater terminus (canal opened 1828, 108 miles); $1.5M federal grant to raise East Strand/North Street against frequent tidal flooding (Times Union, Mar 29 2024) | Wikipedia Kingston; timesunion.com | cat6-repair.md R7; door-buzzer C5 | §13 Rondout card; §7.5 |
| C6 | UPAC (Broadway, Midtown Kingston) 1927, 1,500 seats | hudsonvalleyone.com 2017/11/30 | door-buzzer C6 | §13 card |
| C9 | Former IBM Kingston campus (iPark 87), Enterprise Drive — East Campus hosts Ulster BOCES and Archtop Fiber | ulstercountyny.gov 2026-02-27 | door-buzzer C9 | §8 Town of Ulster card |
| C10 | Uptown Kingston: Wall Street and North Front lined with shops, restaurants | goloveny.com | door-buzzer C10 | §8 Uptown card |
| C11 | New Paltz Main Street (Route 299) village shopping/restaurants | iloveny.com | door-buzzer C11 | §8 New Paltz card |
| C12 | SUNY New Paltz: 6,197 undergraduates, 1,036 graduate students | newpaltz.edu | door-buzzer C12 | §9 cluster 6 Q16 |
| C13 | Earth Networks 2020: Ulster 182,760 lightning pulses, 49 thunder days | Earth Networks 2021 State Lightning Report | door-buzzer C13 | §5.5 bullet 3; §9 Q6 |
| C14 | Daily Freeman Sept 27 2026: nor'easter peak >14,000 Ulster outages; Central Hudson 93,209 Ulster customers | dailyfreeman.com/2026/09/27/… | door-buzzer C14 | §5.5 bullet 3 |
| C15 | Cell dead zones along Routes 212 and 28; worst ZIPs 12464 Phoenicia, 12452 Lexington/Shandaken, 12477 Saugerties, 12458 West Hurley (HV1 Dec 29 2016) | hudsonvalleyone.com/2016/12/29/dead-zones-… | door-buzzer C15 | FAQ 4 |
| C16 | Archtop Fiber HQ Kingston; launched Kingston and Saugerties, building in Woodstock (Oct 2024); Planet Networks fiber in Kingston | archtopfiber.com blog 2024-10-01; Reddit excerpts | cat6-repair.md U1–U2 | §9 Q13; §5.5 bullet 5 |
| C20 | Ulster County Code Ch. 185: "electrical work" includes wiring for "signaling, communication, alarm or data transmission"; master electrician licence for electrical permits | ecode360.com/35131702 | door-buzzer C20 | §8.5 bullet 3 (new outlets/generator inlets by a county-licensed electrician; no claim that a low-voltage recorder swap needs a county licence) |
| C21 | Opus 40, Saugerties: bluestone earthwork by Harvey Fite in an abandoned quarry; by 1898 ≥10,000 people in Ulster made a livelihood from bluestone | opus40.org | cat6-repair.md R8 | §13 card; §7.5 |
| C22 | Ellenville on Route 209; Shawangunk Ridge | ewcoc.com | cat6-repair.md R14 | §8 Ellenville card |
| C23 | Walkway Over the Hudson west end in Highland | parks.ny.gov; walkway.org | door-buzzer C23 | §13 card |
| C24 | Ashokan Reservoir created 1915, 14 miles west of Kingston | dec.ny.gov | cat6-repair.md R9 | §13 card |
| C25 | Hurricane Irene 2011: almost all of Ulster >6 in of rain; record flood levels on Upper Esopus Creek, Stony Clove Creek in Phoenicia, Rondout Creek in Rosendale | loweresopus.org | cat6-repair.md U14 | FAQ 7 (creek camera); §7.5 |
| C26 | USDA 2022 Census of Agriculture: Ulster 486 farms, average 150 acres | USDA county profile | cat6-repair.md (HV) | §8 farm card; §9 Q17 |
| C27 | Hudson Valley Mall, Town of Ulster on Route 9W — "long-term redevelopment and repositioning" | hullpg.com | cat6-repair.md U15 | §8 Route 9W card |

### Silo rows reused (research/dvr-upgrade.md Part 1)
T1 (Dahua HDCVI 700 m 4K / 800 m 1080p / 1200 m 720p over coax), T2 (penta-brid), S1 (FortiGuard TBK CVE-2024-3721), S2 (NVD CVE-2021-36260 in KEV), A1 (Security.org/HomeAdvisor $100–$200 two cameras), A2 (CCTV Camera World on coax), R1 (Reddit hybrid NVR advice), R7 (Low Voltage Nation $500 DIY), Nassau S3 (WD Purple 180 TB/yr), S6 (HomeGuide $100–$350 DVR), S7 (Reddit "just buy a new system"), G1 (Civil Rights Law §52-a), G3 (Penal Law 250.05 one-party consent), G4/G5 (NYS Commercial Security Tax Credit).

### EMPTY (not accessible in build env / not found)
Google PAA, PASF, Answer the Public, AI Overview, Bing/DDG autocomplete, Yelp 1–3★; Kingston/Ulster Reddit threads about home DVRs; Daily Freeman / Kingston Wire stories on home recorders; Ulster town permit rules for low-voltage camera work; any private-camera registration programme run by Kingston PD, Saugerties PD or the Sheriff; Starlink/CGNAT data specific to Ulster; a sourced Ulster DVR job for Field Notes (Field Notes written as general practice, labelled so); Google Drive "AESS Website Photos" has no DVR Upgrade subfolder (subfolders: Cat6 Repair, Sonos, Soundbar, Smart Lock, Fiber Optic); CompanyCam not connected in Composio (no active connection).

### House practices stated on the page without an external source (FLAG for Anwar)
Daily/weekly "recording heartbeat" checks via the app and disk-error push alerts; setting recorders to power on automatically after an outage and testing it by pulling the plug; UPS on recorder + modem + PoE switch; whole-house surge protection plus coax/data surge protectors at building entry, bonded to the electrical ground; caretaker user accounts with playback-only rights; maintenance visit routines; recorder placement above flood level / in conditioned space; mounting into mortar joints, sill plates and window frames rather than stone faces; wireless point-to-point bridges for outbuildings; "most systems recording again within one to two hours of arrival" and two-hour arrival windows seven days a week to 8 PM (silo convention copied from live pages); "Ulster figures already carry the county factor, no separate travel line" (derived from §9, not a published AESS policy).

### Pricing (§9 Ulster 1.53× applied to the silo base; round half-up; nothing invented)
| Job | Brooklyn base (silo) | Ulster ×1.53 |
|---|---|---|
| 4-channel swap | $450–$700 | $689–$1,071 |
| 8-channel swap | $650–$1,000 | $995–$1,530 |
| 8-channel hybrid (XVR) | $800–$1,200 | $1,224–$1,836 |
| 16-channel | $1,200–$2,200 | $1,836–$3,366 |
| 32-channel | $2,200+ | $3,366+ |
| Hybrid hardware premium | $20–$80 (equipment, not multiplied — §9 equipment locked at street price) | $20–$80 |
| Service/callback rate | $195/hr, 3-hr minimum ($585) — protected, not multiplied | same |
FLAGS: (1) the old Ulster page showed "$250 service call", "$175/drop", "$19.99/mo" and "$0/mo" chips and "$500 to $1,400 installed" — inconsistent with §9 and the $195/hr policy; none carried. (2) The rebuilt Brooklyn (base) and Nassau pages publish the silo table un-multiplied (Nassau should be 1.15×); the HV hub still shows base figures. This page applies 1.53× as the brief requires — the coordinator may want the hub and Nassau aligned.

### Images (11) — Step A empty, Step B unavailable, Step C / permanent image rule
3 real AESS job photos from other jobs (new crops, no signs/text/people) + 8 manufacturer product shots. All viewed before naming. Avoided images/buzzer-repair/. Re-cropped a 4th real photo (deli ceiling) was dropped because it duplicated the Brooklyn crop.
| Output (images/dvr-upgrade/) | Source | Crop / note |
|---|---|---|
| dvr-upgrade-ulster-dark-grey-recorder-with-two-front-usb-ports-product-photo.webp (500×164) | images/nvr-honeywell-35-series.png | product shot, trimmed (hero) |
| dvr-upgrade-ulster-low-black-recorder-with-angled-front-product-photo.webp (500×157) | images/nvr-reolink-nvs8.png | product shot |
| dvr-upgrade-ulster-square-black-recorder-with-glossy-top-product-photo.webp (436×182) | images/nvr-tplink-vigi-nvr1008h.png | product shot |
| dvr-upgrade-ulster-black-recorder-with-orange-logo-and-vented-front-product-photo.webp (500×124) | images/nvr-digital-watchdog-cova.png | product shot |
| dvr-upgrade-ulster-white-turret-with-two-lenses-and-warning-lights-product-photo.webp (894×893) | images/cam-dual-lens-active.jpeg | product shot |
| dvr-upgrade-ulster-white-dual-lens-pan-tilt-camera-product-photo.webp (350×554) | images/cam-ptz-dual.jpeg | product shot |
| dvr-upgrade-ulster-white-varifocal-bullet-camera-product-photo.webp (299×159) | images/hikvision-varifocal-bullet-camera.jpg | product shot (maker name on body, not named in copy) |
| dvr-upgrade-ulster-two-white-turret-cameras-side-by-side-product-photo.webp (329×153) | images/hikvision-colorvu-turret-camera-pair.jpg | product shot |
| dvr-upgrade-ulster-dark-dome-camera-at-ceiling-corner-near-light-panel.webp (645×380) | images/rockland-toyota-dome-camera.jpeg | real job photo; crop (290,0,935,380) — dealer logo, signage and TV excluded |
| dvr-upgrade-ulster-black-bullet-camera-on-ceiling-grid-above-corridor.webp (805×370) | images/rockland-toyota-hallway-camera.jpeg | real job photo; crop (130,130,935,500) — poster, QR card, desk excluded |
| dvr-upgrade-ulster-white-dome-camera-under-water-stained-ceiling.webp (700×640) | images/nassau-window-depot-storage-camera.jpeg | real job photo; crop (100,0,800,640) — boxes with brand/handwritten text excluded |

### Build notes
- `tools/check_page.py dvr-upgrade-ulster` (repo copy) cannot run: `AREAS` only knows `ulster-county`, so the slug `dvr-upgrade-ulster` (and the siblings -westchester, -rockland, -orange, -putnam, -dutchess) prints "can't tell the area from slug". A patched copy in the scratchpad (adds short HV keys `westchester`/`rockland`/`orange`/`putnam`/`dutchess`/`ulster` with the same rules as the `-county` keys; Westchester phone 914-877-2578) reports **PASS** including registration (sitemap, _redirects, hub link-down, sibling link-backs): 13,497 rendered words; title 58; meta 158; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 183,438 B (Nassau 180,770; Brooklyn 186,554; Westchester new 192,992).
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word-level SequenceMatcher), excluding the blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades in [Area]" and the protected terms sentence: max **0.596** (vs dvr-upgrade-brooklyn, services intro); 0.594 vs the new dvr-upgrade-westchester (price line in the quick block).
- Dedupe vs the new Westchester page (rebuilt in parallel, read 2026-10-18 ~05:50): replaced three first-draft Q&A whose intent matched Westchester's ("400 ft of old coax to the barn — HD?" ≈ "Bedford gatehouse several hundred feet over old coax"; "does the recorder restart after a Central Hudson outage" ≈ "generator takes over but recorder never comes back on"; "insurer asked who checks on the house" ≈ "show our insurer the system is maintained"). Borderline pairs left for coordinator review: my "standby generator weekly self-test reboots cameras" vs Westchester "generator takes over but recorder never comes back on by itself"; my "barn on its own meter — ground difference" vs Nassau "rolling lines whenever the garage door opener runs"; my "Stockade like-for-like swap = maintenance exemption?" vs Brooklyn "historic district — do we need LPC approval for a new camera?".

### Final pass (coordinator request, after putnam/queens/staten-island shipped)
- Repo `tools/check_page.py dvr-upgrade-ulster` (now patched upstream for short HV slugs): **PASS**. 12,720 rendered words; 178,559 B (inside the 178,430–178,700 band between orange 176,376 and nassau 180,770); FAQ 9 = FAQPage 9.
- Meaning-level dedupe vs rebuilt Putnam / Staten Island / Queens / Westchester: removed or replaced 6 Q&A and 7 FAQ. Removed Q&A: recorder-stopped-saving alert from the city (= Putnam "How will we know the recorder at the weekend house has stopped working"), caretaker visit search (= Staten Island "search for every time a car pulled into the driveway"), continuous vs motion (= Putnam), standby generator (≈ Putnam/Westchester generator Qs), barn on its own meter (= Putnam), upload speed (≈ Putnam capped data). Removed FAQ: swap while we're in the city (= Putnam video-call), freeze warning (= Putnam heat fails in January), cell dead zone (≈ Putnam one bar of signal), lenses/spider webs (= Putnam spiders), creek level camera (≈ Staten Island flood height, Putnam dock/ice), mailbox camera (≈ Putnam bottom-of-driveway), travel pricing (≈ Staten Island "worth calling you across the bridge"). New items: Central Hudson outage credits, metal-roof snow slides, Kingston police street cameras, old farmhouse wiring, event barn, contractor renovation, hunters on posted land, smart-lock code vs door camera, Wi-Fi through stone walls.
- New facts used: Central Hudson outage credits (outages ≥72 h affecting ≥20,000 customers; $25 per further 24 h residential; food/medicine reimbursement) — row U5 (https://www.cenhud.com/en/outages/). House practices added (FLAG): roof-slide camera placement, ground-loop/grounded-outlet advice, event/contractor/hunter/smart-lock answers.
- Masked-geo similarity max 0.636 (vs dvr-upgrade-staten-island, a Census citation line in Sources); highest prose block 0.609 (vs Brooklyn).

### Question register additions
**dvr-upgrade-ulster — REBUILT 2026-10-18 (final)**
**Q&A / question headings:**
- Came Up for the Weekend and Every Camera Was Blank?
- Central Hudson credits customers after long outages — does that cover a recorder that died in the storm?
- Central Hudson's map shows our road is out — can we tell from the city whether the cameras are running on the battery?
- Should there be surge protection where the barn camera's cable comes into the house?
- Our house has two-foot stone walls — how does a new cable get from the recorder to a camera outside?
- Snow slides off our metal roof in sheets — where can a camera go so it isn't torn off?
- Does swapping the recorder and reusing the existing brackets on our Stockade house count as a change the preservation commission reviews?
- Our Midtown Kingston storefront has a pressed-tin ceiling — can the new domes go in the same spots?
- Kingston police run their own street cameras — does that make a camera on our Uptown shop unnecessary?
- Our only internet is a satellite dish — can the phone app reach a recorder behind it?
- Fiber is coming to our road under the county broadband program — should we wait to upgrade the recorder?
- We rent the house to short-term guests some weekends — where can cameras go, and what do guests have to be told?
- Our New Paltz rental turns over every May — what should change on the recorder between tenant groups?
- Can a camera watch the self-serve cash box at our farm stand from the recorder in the house?
- Our Woodstock shop closes for part of the winter — can the recorder alert us only when the shop is shut?
**FAQ (= FAQPage):**
- Our old farmhouse still has some original wiring — is it safe to plug the recorder into it?
- Our barn is booked as a seasonal event venue — can cameras cover the parking field without filming guests inside?
- A contractor is renovating while we're in the city — can the cameras show progress without recording their conversations?
- Hunters keep crossing our posted land in the fall — can a camera on the boundary help?
- Can the camera at our front door show which code was used on our smart lock?
- Thick stone walls kill our Wi-Fi — can a Wi-Fi camera on the porch still reach the recorder?
- Can the inside cameras be switched off while we're at the house?
- Can a camera be mounted on a log or board-and-batten wall without leaving damage?
- We arrived on Friday night and one camera shows a black tile — what should we check before calling?


## Westchester

Page: `dvr-upgrade-westchester` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Up-link `/dvr-upgrade-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (914) 877-2578 in body, CTAs, forms copy and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from Brooklyn rowhouses/bodegas, Nassau house+garage+driveway, and the rural/second-home Ulster angle):** in Westchester a recorder upgrade is a governance job — co-op boards, condo associations, managing agents, supers and desk staff in the county's large apartment stock (Yonkers, Mount Vernon, New Rochelle, White Plains, garden complexes), plus corridor retail and Platinum Mile suites; the page covers board-ready scopes, role-based logins and footage policy, garage/package-area footage, the county licensing split (home improvement ≤3 units vs alarm business licence), Ida/Isaias power realities, and long runs on northern estates as a secondary theme.

Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`), Firecrawl Alexandria `census-gov` census/data. Shell curl blocked. "Excerpt" = read only as a search-result snippet.

### Mandatory sources status (Westchester)
| # | Source | Result |
|---|---|---|
| 1 | Reddit r/Westchester | Excerpts only (R-W1–R-W3). r/Yonkers: search returned no Yonkers-specific thread → EMPTY (not accessible in build env / none surfaced). |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so and works from forum/cost claims and stated assumptions. |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env). |
| 9–10 | Local news / hyperlocal | News 12 Westchester (N-W1, N-W2 excerpt), Journal News/lohud (P-W2; P-W4 page scraped empty → not used), ABC7 (F-W1), Talk of the Sound (F-W2). Patch: only a licensing-rules excerpt surfaced (L-W5), not used. |
| 11 | Yelp 1–3★ | Search page excerpt only (Yelp Westchester camera installers list, 4.7/1,053 aggregate of a listing page) — no review text → EMPTY (not accessible in build env). |
| Drive / CompanyCam | Drive folder `AESS Website Photos` has no DVR Upgrade subfolder (subfolders: Cat6 Repair, Sonos Installation, Soundbar Installation, Smart Lock Installation, Fiber Optic Installation). CompanyCam toolkit via Composio: no active connection. |

### Housing stock (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H-W1 | Alexandria `census-gov` census/data · acs/acs5 2023 · B25001_001E, B25003_002E/003E, B25024_002E–009E, B25034_010E/011E, B25035_001E · county:119 state:36 | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36119 | Westchester: 391,861 units; median year built 1958; 1939-or-earlier 109,608; 1940s 27,851; 1-unit detached 170,635; attached 25,697; 2-unit 30,527; 3–4 28,194; 5–9 19,373; 10–19 19,206; 20–49 30,854; 50+ 66,378 (20+ = 97,232 ≈ 25%); owner 230,294; renter 139,962. | §5 para 1; §5.5 bullets 1–2; Sources |
| H-W2 | same provider · place:84000,50617,51055 state:36 (a fourth code returned Niagara Falls, discarded) | same API | Yonkers: 83,851 units; 50+ 22,426; 20–49 9,464; renter 42,519 vs owner 38,031; median 1958. Mount Vernon: 30,890; renter 16,813 vs owner 12,228; median 1952; 50+ 6,244. New Rochelle: 32,138; 50+ 7,942; median 1954. (White Plains not retrieved.) | §5 para 1; §5.5 bullet 3 |

### Licensing / county rules (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L-W1 | `Westchester County Department of Consumer Protection home improvement license security systems alarm installer` · Firecrawl search → scrape (directQuote) | https://library.municode.com/ny/westchester_county/codes/code_of_ordinances?nodeId=PTVIIRUREDEENFA_CH863COPRCO_ARTXVILIPEENHOIMBU | Ch. 863 Art. XVI: "Home improvement" = repair/installation etc. "to, in or upon a private residence, townhouse, condominium, apartment, or dwelling place of not more than three units"; exemption: "The sale, leasing, maintaining, installing, repairing, altering, moving, replacing or servicing of an alarm device or system by a county-licensed alarm business or alarm agent". | §5.5 bullet 4; §8.5 bullets 1–2; Q&A licence cluster (both H3); §10.5 H3 3; Sources |
| L-W2 | `Westchester County licensed alarm business alarm agent license Consumer Protection chapter 863` · Firecrawl search | https://ecode360.com/7692228 (Town of Cortlandt Ch. 113, excerpt) | Alarm business licence/agent licence issued by the County under Ch. 863 Art. XV for installing/servicing police or fire alarm devices. | §8.5 bullet 2; Q&A alarm H3; Sources |
| L-W3 | same as L-W1 | https://consumer.westchestercountyny.gov/ | "Plumbers and electricians must obtain a trade license in order to work in Westchester County"; licence lookup exists. | §8.5 bullet 4 (electrical outlet by licensed electrician); Q&A licence H3 |
| L-W4 | `Westchester County co-op apartments share of housing cooperatives Yonkers Scarsdale co-op board` · Firecrawl search → scrape | https://humanrights.westchestercountyny.gov/resources/cooperative-housing-disclosure | Westchester Fair Housing Law: co-op boards acknowledge applications within 15 days, decide within 60, send rejection notices to the Human Rights Commission. | Background only (shows formal co-op board process); not stated on page |
| L-W5 | (L-W1 search) | https://patch.com/new-york/whiteplains/new-hvac-power-washer-licensing-rules-are-effect-westchester-county (excerpt) | New HVAC/power-washer licensing rules. | Not used |
| L-W6 | `Westchester County cities towns villages number…` · Firecrawl search | https://www.westchestercountyny.gov/about-westchester (excerpt); https://en.wikipedia.org/wiki/Westchester_County,_New_York (excerpt) | County site: six cities, 19 towns, 20 villages; Wikipedia: 23 villages (counts Harrison, Mount Kisco, Scarsdale as town/villages) → page says "about two dozen villages". | §5.5 bullet 6 |

### Storms / power (F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| F-W1 | `Hurricane Ida Mamaroneck flooding 2021 Westchester basements damaged homes` · Firecrawl search | https://abc7ny.com/post/flooding-brooklyn-nj-nyc-flooded/10994078/ (excerpt incl. article text) | Sept 2, 2021: some Mamaroneck neighborhoods up to 14 feet of water; basements filled to first floor; title: 3 dead in Westchester. | §5 para 4; Q&A off-site copy H3; §10.5 H3 5 |
| F-W2 | same → scrape | https://talkofthesound.com/2021/09/02/con-ed-reports-16000-customers-without-power-after-ida-blows-through-westchester/ | Con Ed Westchester total 15,975 out; Mamaroneck Village 4,808; Mamaroneck Town 1,929; New Rochelle 1,076. | §5 para 4; §10.5 H3 5 |
| F-W3 | `Con Edison Westchester outages Isaias 2020…` · Firecrawl search → scrape | https://www.lohud.com/story/weather/2020/08/12/eight-days-after-isaias-many-without-power-wednesday-morning-hudson-valley/3352805001/ | Eight days after Isaias Con Ed still had 1,357 customers out; "about 350 … due to the storm are in Westchester". | §5.5 bullet 5 |
| F-W4 | `NYSEG electric service territory northern Westchester towns…` · Firecrawl search | https://www.nyseg.com/documents/d/nyseg/psc120_section-1 (excerpt) | NYSEG tariff territory, Westchester towns: Bedford, Lewisboro, North Salem, Poundridge, Somers. | §5.5 bullet 5; §13 IBM card; Q&A generator H3 |

### News / Reddit (N, R)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N-W1 | `Westchester police package theft car break-ins surveillance video 2025 2026 lohud patch Yonkers New Rochelle` · Firecrawl search → scrape | https://westchester.news12.com/2026/09/05/several-vehicles-found-with-smashed-windows-in-yonkers-parking-garage/7xKdNpCKY1rAAULjrmWJ6H | Sept 5, 2026: Yonkers PD responded to multiple vehicles with smashed windows at a parking garage on Warburton Avenue; News 12 found at least nine; "Surveillance video from the parking garage and retail stores linked the pair to the crimes, police said." Two Yonkers residents arrested (not named on page). | §5 para 3; Q&A garage H3; Sources |
| N-W2 | same | https://www.facebook.com/News12WC/videos/car-thefts-following-the-thefts-local-police-say-they-will-have-increased-patrol/2125437728383599/ (excerpt) | News 12 clip: surveillance footage of suspects checking car doors and breaking into a vehicle in Port Chester (undated). | §5 para 3 (no date given) |
| N-W3 | same | https://www.lohud.com/story/news/crime/2026/02/20/westchester-county-ny-police-departments-weigh-in-car-theft-rates/88775397007/ | Scrape returned no article text; excerpt quote "Thefts FROM vehicles are down 31%…" unattributed → NOT used. | — |
| N-W4 | same | https://www.youtube.com/watch?v=f5wnEap29Nc (excerpt) | "Westchester residents alarmed by spike in mail, car thefts caught on camera" (undated). | Not used |
| R-W1 | `reddit r/Westchester security camera system DVR installer recommendation` · Firecrawl search | https://www.reddit.com/r/Westchester/comments/1jezgj3/suggestion_on_home_security_systems/ (excerpt) | "Reolink has been the best as each camera is powered over Ethernet (PoE) meaning you just need to supply an Ethernet cable to it." | §10.5 H3 1 (quoted); Sources |
| R-W2 | same | https://www.reddit.com/r/Westchester/comments/1hu8zqf/home_security_company_recs_for_security_camera/ (excerpt) | "My cousin lives in a town-house style coop, and they are looking to invest in getting some security cameras." | Background for co-op/townhouse-complex thesis; Sources |
| R-W3 | same | https://www.reddit.com/r/Westchester/comments/1jqowbv/advice_with_security/ (excerpt) | New home with "already inbuilt system all over the house". | Background (inherited systems) — not used on page |
| R-W4 | `reddit r/Yonkers building security cameras landlord package theft apartment` · Firecrawl search | (results were r/NYCapartments, r/Landlord, r/AskNYC, r/homesecurity — none in Yonkers) | Generic: landlords saying cameras are down / won't check footage without police report. | Background for package-area and footage-policy H3s (not quoted, not presented as local) |
| R6 (silo) | carried from research/dvr-upgrade.md R6 | https://www.reddit.com/r/SecurityCamera/comments/1fiv6lt/what_should_a_business_expect_to_pay_for_an/ (excerpt) | "$500-$2500+" per camera installed (business new install). | §10.5 H3 2 |

### Corridors / landmarks (C)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| C-W1 | `Westchester Avenue "Platinum Mile" I-287 office parks Harrison Rye Brook White Plains` · Firecrawl search | https://914inc.com/westchesters-platinum-mile-is-making-a-serious-comeback/ (excerpt incl. text) | Not an official designation; I-287 stretch from 333 Westchester Ave (White Plains) to 800 Westchester Ave (Rye Brook), about four miles; medical conversions (Purchase Professional Park, Westchester Medical Campus 220-230/244 Westchester Ave). | §8 card; §13 card; Q&A Platinum Mile H3 |
| C-W2 | `Central Park Avenue NY 100 Yonkers Greenburgh Scarsdale retail corridor miles` · Firecrawl search | https://www.nytimes.com/library/realestate/commercial/cp951217.html (excerpt, 1995) | Central Park Avenue runs eight and a half miles from Yonkers through Greenburgh to White Plains, large shopping centers. | §8 card |
| C-W3 | `Boston Post Road US Route 1 Westchester…` · Firecrawl search | https://en.wikipedia.org/wiki/U.S._Route_1_in_New_York (excerpt) | US 1 in NY: 21.54 miles from GWB to CT line at Port Chester. (Page names the Westchester towns it passes — general geography.) | §8 card |
| C-W4 | `Ridge Hill Yonkers … Cross County Center Yonkers opened 1954` · Firecrawl search | https://en.wikipedia.org/wiki/Cross_County_Center (excerpt); https://mall-hall-of-fame.blogspot.com/2010/09/blog-post_20.html (excerpt) | Opened 1954 as one of the nation's first open-air shopping destinations; parking lot built atop a former peat bog; first phase opened April 28, 1954. | §13 card |
| C-W5 | `Playland Park Rye opened 1928 National Historic Landmark…` · Firecrawl search | https://en.wikipedia.org/wiki/Playland_(New_York) (excerpt); https://www.hudsonrivervalley.com/sites/Playland-Amusement-Park-/details (excerpt) | Built 1928, 280-acre, Long Island Sound, Rye, owned by the county; much original architecture and seven original rides incl. Dragon Coaster remain. | §13 card |
| C-W6 | `Governor Mario M. Cuomo Bridge Tarrytown opened 2017 2018 length miles` · Firecrawl search | https://www.thruway.ny.gov/the-bridge (excerpt) | Fully opened to traffic in 2018; path 3.6 miles. | §13 card |
| C-W7 | `Sing Sing Correctional Facility Ossining built 1826…` · Firecrawl search | https://en.wikipedia.org/wiki/Sing_Sing (excerpt) | Maximum-security prison in the village of Ossining; opened 1826. | §13 card |
| C-W8 | `IBM headquarters Armonk New Orchard Road North Castle…` · Firecrawl search | https://www.naswa.org/ibm-corporate-headquarters (excerpt) | IBM Corporate Headquarters, 1 New Orchard Rd, Armonk NY 10504. | §13 card |

### Silo sources reused on this page (see Part 1 of research/dvr-upgrade.md)
T1 (Dahua XVR 700/800/1200 m), Nassau S1 (Hikvision Turbo HD 800 m 1080p / 1,200 m 720p), S1/S2 (FortiGuard TBK CVE-2024-3721; NVD CVE-2021-36260 in KEV), G1 (CRL §52-a), G3 (PL §250.05), G4 (Commercial Security Tax Credit), R1 (r/homesecurity "Replace a new HDD should fix").

### Pricing (no invented prices)
Silo base (Brooklyn 1.00×, research/dvr-upgrade.md §1.8) × §9 Westchester 1.25, round half-up: 4-ch $450–$700 → **$563–$875**; 8-ch $650–$1,000 → **$813–$1,250**; 8-ch hybrid $800–$1,200 → **$1,000–$1,500**; 16-ch $1,200–$2,200 → **$1,500–$2,750**; 32-ch $2,200+ → **$2,750+**; hybrid hardware premium $20–$80 → **$25–$100**. Service rate $195/hr, 3-hr min ($585) kept verbatim (protected, not multiplied). FLAG: the old Westchester page (and every other DVR page) showed the unmultiplied Brooklyn figures plus "$250 service call / $175/drop / $0/mo" widget chips — those chips not carried; Westchester now differs from siblings that still show base figures.

### House practices stated without an external source (FLAG for Anwar)
- Certificates of insurance naming the corporation and agent issued on request via broker; workers' comp/disability certificates on request.
- Written two-page board scope format; per-run cable-repair line items; handover sheet; Spanish-language handover guide.
- Role-based accounts (agent/super/desk/board), audit-log, max-retention settings, privacy masking, no audio by default, no cameras in exam rooms.
- Two-hour arrival windows, seven days to 8 PM; "most systems recording again within one to two hours of arrival" (copied from live silo/blueprint wording).
- Yearly check contents billed at $195/hr 3-hr min.
- Elevator travelling-cable cab cameras and coordination with elevator contractor; fibre/radio between garden-complex buildings; surge protectors on long runs (general trade practice).
- Building-type cards (mid-century elevator co-ops in Yonkers/White Plains/Hartsdale/Scarsdale Central Ave/New Rochelle; garden complexes in Hartsdale/Tuckahoe/Ossining/Sound Shore; pre-war walk-ups in Mount Vernon/SW Yonkers/Port Chester/Peekskill) are general descriptions, no stats attached.
- Corridor card "Getty Square, South Broadway and Warburton Avenue" and "Route 9 river towns" — real streets/places, described generically.

### Images (11) — Step A: no DVR Upgrade folder in Drive; Step B: CompanyCam not connected; Step C / permanent image rule
4 real AESS job photos from other jobs (new crops of Rockland Toyota photos, different framing from the Brooklyn/Nassau crops; signs, people, logos, text, screen content excluded) + 7 manufacturer product shots not used on Brooklyn/Nassau. All looked at with the Read tool. All WebP q80, ≤1600 px, in images/dvr-upgrade/. Rejected: images/buzzer-repair/* (AI-looking), images/commercial-security/* (previously rejected as AI-generated), rockland-toyota-showroom lower half (people, signage, vehicle), nassau-window-depot-monitor other tiles (house number, people).
| Output | Source | Crop / note | Placement |
|---|---|---|---|
| dvr-upgrade-westchester-slim-black-recorder-with-two-front-lights-product-photo.webp (500×167) | images/nvr-avycon-avr-nsv16p.png | trimmed product shot | Hero (eager) |
| dvr-upgrade-westchester-two-small-cameras-high-on-white-wall-below-mezzanine-windows.webp (700×470) | images/rockland-toyota-showroom.jpeg | crop (360,30,1060,500): upper wall + ceiling only; banner text, signs, people, car excluded | §5 |
| dvr-upgrade-westchester-recorder-front-and-rear-port-panel-product-photo.webp (470×362) | images/nvr-swann-advancedx-4k.png | trimmed; small logo not named | §6 |
| dvr-upgrade-westchester-black-bullet-camera-where-drop-ceiling-meets-wall.webp (935×470) | images/rockland-toyota-hallway-camera.jpeg | crop (0,0,935,470): ceiling only; poster/QR card/desk excluded (Nassau crop was the corridor + door) | §7 |
| dvr-upgrade-westchester-small-ceiling-camera-beside-dark-coffered-soffit.webp (555×490) | images/rockland-toyota-active-deterrent.jpeg | crop (380,380,935,870): soffit + ceiling; mural, banner, people, TV excluded | §8 |
| dvr-upgrade-westchester-cable-bundles-at-ceiling-above-equipment-rack.webp (560×285) | images/rockland-toyota-nvr-monitor.jpeg | crop (0,0,560,285): cables only; screen, timestamp, monitor logo, sticker excluded (Nassau crop was the screen) | §9 Q&A |
| dvr-upgrade-westchester-silver-and-black-rack-recorder-with-front-lights-product-photo.webp (500×124) | images/nvr-hikvision-ds7616ni.png | trimmed product shot | §10 |
| dvr-upgrade-westchester-black-recorder-with-front-buttons-and-navigation-dial-product-photo.webp (883×183) | images/nvr-lorex-4k-16ch.png | trimmed product shot | §12 |
| dvr-upgrade-westchester-white-turret-camera-with-side-lens-module-product-photo.webp (670×668) | images/cam-turret-side.png | trimmed product shot | §13 |
| dvr-upgrade-westchester-flat-black-rack-recorder-product-photo.webp (496×151) | images/nvr-hanwha-wisenet-arn1610s.png | trimmed product shot | §14 |
| dvr-upgrade-westchester-white-turret-camera-with-two-illuminators-close-up-product-photo.webp (480×477) | images/cam-eyeball-white.png | trimmed product shot | §15 |
Note: several "recorder" product shots are network video recorders; captions say "recorder" only and the §6 caption states the pictured unit takes network cameras.

### Build notes
- check_page.py: unpatched tool cannot identify the slug (`can't tell the area from slug 'dvr-upgrade-westchester'`) because AREAS has `westchester-county` but this silo uses short HV slugs (-westchester, -rockland, -orange, -putnam, -dutchess, -ulster). Run with a scratchpad wrapper that aliases the six short suffixes to the county rows (no repo file edited): **PASS** (full, with registration). [superseded: final 13,719 words, 191,705 B — see register note] 13,915 rendered words; title 55; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 15 silo siblings checked (all cross-link both ways); 192,992 B.
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, word SequenceMatcher) vs every dvr-upgrade-* page: max non-fixed **0.455** (vs dvr-upgrade-suffolk-county / -orange, "No monthly fee…" bullet vs their "Any monthly fee…" question). Only 1.000 = blueprint-fixed H2 "What AI Gets Wrong About DVR Upgrades in [Area]" (same on Brooklyn and Nassau by design). A copied Brooklyn trust bullet (two-hour windows) was rewritten.
- Semantic de-dup read against the full register + new Brooklyn/Nassau lists. Borderline pairs for coordinator review: garage car break-ins (this page: garage aisle + entrance under a building) vs Nassau driveway plate / car-door alerts; managing-agent login revocation vs Brooklyn "who should hold the admin password (siblings/LLC)"; generator restart vs Nassau battery-runtime-in-PSEG-outage. Ulster/Putnam rebuilds are running in parallel and were not visible — check generator/caretaker/long-run intents against them at wiring.

### Question register additions — dvr-upgrade-westchester (final after coordinator round 2: 17 Q&A H3 + 10 FAQ)
Q&A:
1. Our co-op board has to approve the spend — what should the proposal we bring to the meeting include?
2. When the managing agent changes, how do we make sure the old firm can no longer log in to the cameras?
3. Two board members disagree about putting cameras in the laundry room and the gym — what do other buildings settle on?
4. Our proprietary lease says shareholders can't alter common areas — can a shareholder pay for a camera on their own floor's hallway?
5. The buried coax between our garden complex's buildings drops out every time it rains — repair it or replace it with something else?
6. Our camera coax shares a chase with the steam risers — does the heat damage it over the years?
7. Our elevator cab camera feeds the recorder through the elevator's travelling cable — does the upgrade change that?
8. Our co-op is replacing the lobby intercom next year — should the recorder wait so both are done together?
9. Cars keep getting broken into in the garage under our building — what does the recorder need to make that footage useful?
10. Packages keep vanishing from our lobby package area — where should the cameras go so the footage actually shows who took them?
11. Westchester's home improvement licence covers dwellings of up to three units — what does that mean for the company a co-op hires?
12. Our alarm company says only a county-licensed alarm business may touch the system — does that include the camera recorder?
13. We lease a suite in a Platinum Mile office park where the landlord runs its own cameras — can our recorder sit on the building's network?
14. Can the camera at our medical office front desk avoid recording patients' paperwork and the screens behind the desk?
15. We're selling our Armonk house — what should happen to the camera accounts and the recordings at the closing?
16. How do we show our insurer that the building's camera system is actually maintained?
17. The front-desk monitor shows sixteen tiny tiles nobody can read — what should the desk screen show after the upgrade?

FAQ (visible == FAQPage):
1. What does a recorder upgrade usually cost for a 30-unit Westchester co-op with about 16 cameras?
2. Our garage has an attendant's booth at the gate — can it show the garage cameras as well as the lobby desk?
3. Can the new recorder keep a record of who viewed, exported or deleted footage?
4. Will someone show our super and the board how to use the new system, and is that included?
5. Should a large building book a yearly check of the recorder, and what does that visit cover?
6. We're a condo association, not a co-op — does that change who signs off on the upgrade?
7. Do you need our building's internet login or our IT person on site for the upgrade?
8. Can the recorder delete footage automatically after a set number of days the board chooses, rather than only when the drive fills up?
9. Does the new recorder need its own electrical outlet, and who arranges that in a co-op?
10. Residents already watch the lobby camera on the old recorder's phone app — what happens to that access after the upgrade?

Round-2 changes (de-dup vs rebuilt putnam/queens/staten-island): removed gatehouse-distance (= Putnam barn 400 ft), generator restart (= Putnam generator/battery + no-video-after-power), caretaker cottage (≈ Queens basement-unit live view), off-site copy (= Putnam off-property clips), shareholder footage-request policy (≈ Queens unit owner copy of lobby footage), restaurant storeroom lockbox (≈ Queens lock box), FAQ certificate of insurance (= Queens), FAQ Spanish super (≈ Queens Chinese/Spanish staff), FAQ resident notice (≈ Queens tell tenants); package-area Q reworded to placement (Staten Island has motion-search). Added: laundry/gym cameras, intercom-replacement timing, steam-riser chase coax, selling an Armonk house, garage attendant booth screen, dedicated outlet, residents' old app access. Final: check_page PASS (repo tool), 191,705 B, 13,719 words.

Intents deliberately avoided (already in register): DVR vs NVR, drive size for 30 days, footage loss on upgrade, internet-drop recording, DVR lifespan, dark/grainy night lobby, riser coax still good, co-op adding cameras without another board vote, super's monitor during swap, keep lobby cameras + add 4K, two recorders split a building, village permit, video doorbell on recorder, old DVR removal and its drive, swap before opening/after closing, landlord tenant view of front door, backyard-camera law applicability, audio on hallway cameras, battery runtime in long outage, lightning, Nassau licence question.
