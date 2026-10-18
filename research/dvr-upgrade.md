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
