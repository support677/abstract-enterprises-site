# Lorex Camera Installation — silo research

Silo: `lorex-camera-installation-*` (16 area pages: NYC hub + 5 boroughs, LI hub + Nassau/Suffolk, HV hub + 6 counties). Related but separate silo: `lorex-camera-installation-prices-*` (16 calculator price pages; check_page.py identifies them as silo `lorex-camera-installation-prices`, simcheck excludes `-prices-`). Their questions are still listed in the register below so no Lorex page repeats them.

File created 2026-10-18 by the Hudson Valley hub rebuild (first REBUILD in this silo). A parallel run is rebuilding `lorex-camera-installation-brooklyn` the same day and may add its own `## Brooklyn` section; nothing below is Brooklyn-specific.

Format for every row (v2.3 §12.4): exact query · platform · URL · finding · page + section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell curl is blocked in the build env. "carried" = a fact gathered and sourced by an earlier run in another research file (file + row named); the URL was not re-fetched today.

---

## Part 1 — Silo-wide findings (usable on every Lorex page)

### 1.1 Mandatory sources (§3) — status

| # | Source | Status |
|---|---|---|
| 1 | Reddit | Firecrawl search excerpts only (reddit.com pages not scraped): R1–R6 |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 "Reality Check" tests published claims instead (cost guides A1–A2, retailer/Lorex claims L1–L12) and says so on the page. |
| 6 | Landmarks | per-area sections |
| 7 | Use cases / property types | per-area sections |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | per-area sections; silo-level regulatory news N1–N5 |
| 10 | Hyperlocal | per-area sections |
| 11 | Yelp 1–3★ | `Lorex 1-3 star reviews installer Yelp Westchester camera installation complaints` · Firecrawl search → only Yelp search-result pages and one 2021 Yelp Q&A ("Does your company install already purchased cameras?") returned; no review text → EMPTY (not accessible in build env) |

### 1.2 Lorex company / ownership / regulation (N)

| # | Exact query · platform | URL | Finding | Used (HV hub) |
|---|---|---|---|---|
| N1 | `Lorex sold by Dahua to Skywatch acquisition 2023` · Firecrawl search (excerpts) | https://www.dahuasecurity.com/mena/newsEvents/pressRelease/7717 ; https://www.securityworldmarket.com/int/News/Business-News/dahua-to-sell-lorex-to-skywatch-for-usd-72-million | Dahua to sell Lorex to Skywatch (Taiwan-headquartered cloud services company) for about US$72 million; Wikipedia excerpt: sale completed Feb 2023. | §8.5; Q&A "state lawsuits"; §10.5 H3 6; Sources |
| N2 | same search → scrape | https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-files-third-anti-ccp-lawsuit-three-days-suing-baby-monitor-company-lorex | Feb 19, 2026: Texas AG sued Lorex Technology Inc. and Lorex Corporation under the Texas DTPA, alleging cameras "manufactured, sourced, and serviced by Dahua"; Dahua acquired Lorex in 2018 and held it until Nov 24, 2022, when it sold to Skywatch Inc., "one day before an FCC order announced its ban on further product approvals for Dahua"; follows a 2025 investigation. | §5 para 3; §5.5 bullet; §8.5; Q&A lawsuits; §10.5 H3 6; Sources |
| N3 | same search → scrape | https://ago.nebraska.gov/news/attorney-general-hilgers-sues-lorex-selling-cameras-put-nebraskans-security-risk | Sept 23, 2025: Nebraska AG sued Lorex under the state Consumer Protection Act and Deceptive Trade Practices Act; alleges Lorex "continues to use Dahua to source the component parts"; says the sale to Skywatch came "the day before the FCC issued its order". These are allegations in a complaint. | §5 para 3; Q&A lawsuits; §10.5 H3 6; Sources |
| N4 | `Lorex lawsuit attorney general 2026 FCC Lorex cameras` · Firecrawl search (excerpts, past year) | https://www.kcrg.com/2026/10/09/bird-sues-camera-company-with-ties-chinese-government/ ; https://fox4kc.com/news/missouri-attorney-general-sues-baby-monitor-company-over-alleged-ties-to-china/ ; https://www.courthousenews.com/canadian-security-camera-manufacturer-fights-nebraska-lawsuit/ | Iowa AG Brenna Bird sued Lorex (KCRG, Oct 9, 2026); Missouri AG also sued (Fox4 excerpt, date not shown); Courthouse News: Lorex argues it is too far removed from Nebraska to face the suit. | §5 para 3 (Iowa only, dated); Q&A lawsuits; Sources |
| N5 | `Lorex NDAA compliant statement Lorex security trust Dahua components` · Firecrawl search → scrape | https://www.lorex.com/blogs/news/lorex-responds-to-stakeholder-inquiries-related-to-supply-chain | Nov 8, 2023 Lorex statement: "Lorex goes above and beyond regulatory requirements to clearly disclose to purchasers that if they are restricted by the NDAA they should not purchase from Lorex" (website disclosures, packaging labels). Search excerpt (IPVM, not scraped) says Lorex is covered by NDAA §889 — not quoted. | §8.5 callout; Q&A public buyers; §10.5 H3 6; Sources |

### 1.3 Lorex product / app facts (L) — manufacturer sources

| # | Exact query · platform | URL | Finding | Used (HV hub) |
|---|---|---|---|---|
| L1 | `Lorex NVR PoE camera maximum cable length 300 feet support` · Firecrawl search → scrape (directQuote) | https://www.lorex.com/blogs/help/cables-ethernet-cable-length | "The maximum Ethernet cable length that can be used between an NVR and a camera is 328ft (100m)." A PoE switch can be added to extend; "only single connections be used"; "The camera will require a power source within the first 300ft (100m) if using switches to extend". | §5; §5.5; Q&A distance; §10.5 H3 2; HowTo; Sources |
| L2 | same search (excerpt) | https://www.lorex.com/pages/poe | "A single run of ethernet cable will provide power and video transmission up to 300 feet." | background |
| L3 | `Lorex PoE extender ePoE long distance camera 800 m` · Firecrawl search → scrape | https://www.lorex.com/products/aex8-2-8port-epoe-switch | AEX8 8-port ePoE switch: "PoE transmission 800 meters at the speed of 10Mbps or 300 meters at the speed of 100Mbps" (800 m / 2,624 ft); 8 PoE ports; 120 W total. | Q&A distance; §10 equipment card; §10.5 H3 2; Sources |
| L4 | same search (excerpt) | https://www.lorex.com/blogs/help/aex16-series-16-port-poe-switch-frequently-asked-questions | AEX16: 8 ports support long-range PoE up to 600 m on a single Ethernet cable. | §10 card (not quoted with number) |
| L5 | `Lorex Wi-Fi camera 2.4 GHz 5 GHz requirements upload speed help` · Firecrawl search → scrape | https://www.lorex.com/pages/halow | Wi-Fi HaLow battery system: "long distance range up to 500ft (150m) vs. the average Wi-Fi range of 100ft (30m)"; "can penetrate up to 8 walls and effortlessly pass through other obstacles such as trees"; 4K NVR system with battery cameras, built-in 1TB. | §6 card; Q&A HaLow; §10 card; §10.5 H3 3; Sources |
| L6 | same search (excerpts) | https://www.lorex.com/blogs/help/w891ua-series-4k-dual-lens-wi-fi-security-camera-frequently-asked-questions-faqs ; https://www.lorex.com/blogs/help/w881aa-series-4k-spotlight-wi-fi-camera-troubleshooting-guide ; https://www.lorex.com/blogs/help/b862aj-series-4k-wired-video-doorbell-frequently-asked-questions | Upload speed asked for: W891UA "at least 3 Mbps upload"; W881AA "minimum upload speed of 2 Mbps"; B862AJ doorbell "minimum upload speed of 10 Mbps is required for best performance"; W881AA dual-band 2.4/5 GHz. | Q&A remote viewing (Starlink/DSL); §10.5 H3 4; Sources |
| L7 | same search (excerpt) | https://www.lorex.com/blogs/help/top-10-ways-to-boost-your-wi-fi-signal-at-home | "Standalone cameras that connect to your Wi-Fi network are better off with 2.4GHz, especially if you are installing them … far away from your [router]". | §7.5; Q&A outbuildings |
| L8 | `Lorex battery camera cold weather operating temperature winter battery life help` · Firecrawl search (excerpts, lorex.com) | https://www.lorex.com/blogs/help/f861as-series-4k-battery-camera-troubleshooting-guide ; https://www.lorex.com/blogs/help/f861as-series-4k-battery-camera-frequently-asked-questions ; https://www.lorex.com/blogs/help/oc101-series-2k-outdoor-wi-fi-battery-camera-frequently-asked-questions | F861AS: "Cold temperatures affect the battery's capacity … battery life might be shorter"; F861AS battery life 4–6 months (depends on temperature, motion settings, events); OC101 operating temperature −4 °F to 122 °F. | Q&A cold batteries; §10.5 H3 3; Sources |
| L9 | `Lorex Fusion app Lorex Home app Lorex Cloud discontinued which app` · Firecrawl search → scrape | https://www.lorex.com/pages/lorex-apps | Three apps: Lorex Connect (latest products, wired & Wi-Fi, cloud/local, "Smart AI Detect", multi-view up to 4); Lorex Classic ("Previously known as the Lorex App. Compatible with our Lorex Fusion product line", Google Home/Alexa); Lorex Pro (business, wired, local, multi-view up to 16, PC/Mac). "Shared Users & Permissions". "Smart Motion — Recognizes people, vehicles, and animals". Apps optimised for latest two major iOS/Android versions; no guarantee for iPad/tablets. | Q&A which app; FAQ shared users; §10 card; Sources |
| L10 | same search (excerpt) | https://play.google.com/store/apps/details?id=com.lorex.connect | Lorex Connect on Google Play: rating 2.8 (75 reviews) at time of search; one Sept 2026 review complains an old recorder was "discontinued in the US". | §10.5 H3 5 (rating only, dated) |
| L11 | `Lorex Connect NVR cameras Lorex Fusion compatibility not compatible older recorders` · Firecrawl search (excerpts) | https://www.lorex.com/pages/compatibility ; https://www.lorex.com/blogs/help/technical-support-frequently-asked-questions-faqs ; https://www.lorex.com/blogs/help/lorex-fusion-frequently-asked-questions | "Cameras, recorders, accessories, and apps are not always interchangeable"; "Not all Lorex products are compatible with every recorder, camera, accessory, or app"; only Fusion-compatible Wi-Fi cameras connect to Fusion recorders. | Q&A old DVR; §10.5 H3 5; Sources |
| L12 | same search (excerpt) + apps page collections list | https://www.lorex.com/blogs/news/why-lorex-onvif-security-cameras-are-the-perfect-replacement-for-banned-brands ; https://www.lorex.com/pages/lorex-apps | Lorex says its cameras are "ONVIF G, S, and T compliant"; Lorex sells "Coax to Ethernet & Retrofit Adapters", "Solar Panels for Battery-Operated Cameras", "PoE Switches & Extenders". | §6 cards; Q&A old coax; §10 cards |

### 1.4 Reddit / forums (R)

| # | Exact query · platform | URL | Finding | Used (HV hub) |
|---|---|---|---|---|
| R1 | `site:reddit.com Lorex NVR power outage cameras offline after outage UPS` · Firecrawl search (excerpts) | https://www.reddit.com/r/Lorex/comments/1cok2y9/biggest_annoyance_if_there_is_a_hiccup_with_wifi/ | Thread title: "Biggest annoyance. If there is a hiccup with WiFi or power. My cameras go [offline] …"; reply suggests a smart plug to power-cycle remotely. | Q&A reboot after outage |
| R2 | same | https://www.reddit.com/r/Lorex/comments/1bvi7hx/power_outage_caused_motion_detection_to_stop/ | Title: "Power outage caused motion detection to stop"; excerpt mentions a thread "Lorex NVR/Wireless Cameras Need Password Resetting/Pairing After Every Power Outage". | Q&A reboot after outage; §10.5 H3 7 |
| R3 | same | https://www.reddit.com/r/homesecurity/comments/r1hu7o/lorex_4k_system_with_10_cameras_1_camera_is/ | "1 camera is offline every night"; reply: when IR switches on "the camera's wattage requirements increase" (power budget). | §7.5 / Q&A long runs (background) |
| R4 | `site:reddit.com Lorex Starlink remote viewing not working rural property` · Firecrawl search (excerpts) | https://www.reddit.com/r/Starlink/comments/1gvfh8a/accessing_from_outside/ ; https://www.reddit.com/r/Starlink/comments/17ub07p/rural_iowa_experiences_with_starlink_and_security/ ; https://www.reddit.com/r/Starlink/comments/1blnlld/remote_viewing_ip_cameras/ | Starlink residential uses "non-routable IP" addresses (no port forwarding); a rural Iowa Lorex user reports the app "works great" remotely on Starlink; a working farm's 13-camera system app stopped working over Starlink. Mixed experience. | Q&A remote viewing; §10.5 H3 4 |
| R5 | `site:reddit.com/r/hudsonvalley security cameras recommendation house` · Firecrawl search (excerpts) | https://www.reddit.com/r/hudsonvalley/comments/1ww3ifc/secondhome_owners_in_the_hudson_valley_who_looks/ | r/hudsonvalley thread "Second-home owners in the Hudson Valley — who looks after …"; excerpt: "We've got Ring cameras posted around the house … get a bunch of Ring cameras and hope for the best." | §5 para 2; Q&A weekend house |
| R6 | same | https://www.reddit.com/r/hudsonvalley/comments/1gdyejf/car_breakins_gardinerwallkillshawangunk/ | r/hudsonvalley thread "Car Break-Ins (Gardiner/Wallkill/Shawangunk)"; reply suggests "a solar powered motion light and a cheap security camera solution". | §5 para 2; Six Counties (Ulster) |
| R7 | `site:reddit.com Lorex …` (R1 excerpt list) | https://www.reddit.com/r/Lorex/comments/1cc5qmz/i_work_at_lorex_here_are_some_recommendations_on/ | Title "I work at Lorex here are some recommendations on apps"; related thread titles: "Why does Lorex have 3 different Apps?", "Lorex app and Lorex cloud are almost worthless". | §10.5 H3 5 (app confusion, not quoted) |

### 1.5 Published cost claims (for §10.5) (A)

| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `Lorex security camera installation cost professional per camera Angi OR HomeAdvisor OR Fixr OR "Best Buy"` · Firecrawl search (excerpt) | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | Angi 2026: professional installation $590–$2,040; $100–$200 per camera on top of purchase price; DIY cameras $20–$50 each. | §10.5 H3 1; Sources |
| A2 | same (excerpt) | https://www.bestbuy.com/site/smart-home-security-services/security-camera-installation/pcmcat1553538760114.c?id=pcmcat1553538760114 | Best Buy security camera installation listings bucketed from $100–$149.99 up to $1,250–$1,499.99 (price filter buckets, no per-job detail). | §10.5 H3 1 |
| A3 | same (excerpt) | https://www.facebook.com/groups/lowvoltagenation/posts/4511235682499559/ | Low-voltage installer group: quotes for a 9-camera Lorex job ranged "from $999 to over $50,000". | Not used (forum anecdote) |

### 1.6 Keywords — five layers (silo plan)

- **Service:** Lorex camera installation; Lorex security camera installer; Lorex NVR installation; Lorex system setup; Lorex camera mounting; Lorex camera wiring; install Lorex cameras I already bought; Lorex system expansion; Lorex repair / not recording.
- **Problem:** Lorex camera offline; Lorex not recording after power outage; Lorex app can't connect remotely; Lorex Wi-Fi camera weak signal; Lorex battery dies in cold; camera too far from recorder; old Lorex DVR discontinued; false motion alerts from animals.
- **Technology:** PoE NVR; 328 ft Ethernet limit; PoE switch / ePoE (800 m at 10 Mbps); Wi-Fi HaLow (500 ft); 2.4 GHz vs 5 GHz; coax-to-Ethernet adapter; Lorex Connect / Classic / Pro apps; Smart Motion / Smart AI Detect; ONVIF; UPS battery backup; direct-burial Cat6.
- **Industry:** single-family homes; second homes/weekend houses; farms and barns; horse properties; small retail on state routes; contractors' yards; condo/HOA; houses of worship; municipal/school/fire district (NDAA caution).
- **Geographic:** per area page (HV hub: Hudson Valley, Westchester, Rockland, Orange, Putnam, Dutchess, Ulster, Yonkers, White Plains, Nyack, New City, Newburgh, Middletown, Goshen, Carmel, Brewster, Poughkeepsie, Beacon, Rhinebeck, Kingston, New Paltz, Saugerties, Ellenville).

### 1.7 Silo pricing (no invented prices) — FLAG

- The silo's price source is the Lorex calculator embedded in `lorex-camera-installation-prices-*.html` (`PG.Z` labour table). **Brooklyn base:** $175 per wired camera line, $25 junction box, $150 recorder setup, $585 minimum visit. Headline Brooklyn figures on `lorex-camera-installation-prices-brooklyn.html`: **$1,795** 4-camera Lorex system installed; cameras installed **from $278** each; recorders with setup **from $470**.
- Arithmetic check: $1,795 − labour (4×$175 + 4×$25 + $150 = $950) = $845 equipment; $278 − $200 labour = $78 camera; $470 − $150 = $320 recorder. Equipment is "locked at Lorex/street price across areas" (v2.3 §9), so the §9 multiplier is applied to labour only.
- **FLAG:** the calculator does not apply §9 county-by-county; it pairs counties (Westchester/Rockland line $226, setup $188; Orange/Putnam $247/$195; Dutchess/Ulster $267/$212; HV hub = Westchester/Rockland zone → $2,061 / $335 / $508). The old HV hub page showed generic figures ($1,800, $3,000, $8,000 etc.) that were not carried. The HV hub rebuild uses §9 on the Brooklyn labour base instead (see `## Hudson Valley` → Pricing). Anwar to decide whether the calculator zones should be re-cut to §9.

---

## Question register — every FAQ / Q&A / "?" heading on every existing lorex-camera-installation-*.html page

Extracted 2026-10-18 with tools/check_page.py's parser (FAQ items + headings ending in "?"). Geo-masked duplicates are grouped. **None of these may be reused (in meaning) on a rebuilt page.**

### Old template — asked on all 16 area pages (bronx, brooklyn, dutchess-county, hudson-valley, long-island, manhattan, nassau-county, nyc, orange-county, putnam-county, queens, rockland-county, staten-island, suffolk-county, ulster-county, westchester-county)
- Why Choose Lorex Security Cameras?
- Is Lorex cheaper than other camera brands?
- Are Lorex cameras good?
- Can Lorex cameras be viewed on a phone?
- Can I install Lorex cameras myself?
- Which Lorex camera is best for a warehouse?
- Why is my Lorex camera offline or not recording?
- I forgot my Lorex password — can it be reset?
- Why does my night footage look blurry or washed out?
- Is Lorex banned in the US?
- Do I need to notify people they're being recorded?
- Are you licensed and insured?
- Do you offer a warranty?
- What are the best Lorex cameras for apartment buildings?
- Can you upgrade my old cameras to Lorex?
- Do you service Lorex systems you didn't install?
- Will my Lorex system work without internet?
- How do I get started?
- Can I add more cameras later?
- Do you integrate Lorex with access control or alarms?
- What resolution do you recommend?
- Is there a warranty?
- How many Lorex cameras do I need?
- How long does Lorex footage stay recorded?
- Can Lorex cameras record audio?
- What internet speed do Lorex cameras need?
- Where is the install?

### Old template — area-worded variants
- How much does Lorex camera installation cost in [area]? — bronx, brooklyn, dutchess-county, manhattan, nassau-county, nyc, orange-county, putnam-county, queens, rockland-county, suffolk-county, ulster-county, westchester-county; "in the Hudson Valley" — hudson-valley; "on Long Island" — long-island, staten-island (sic); also on all 16 prices pages
- Ready for a Lorex system in [area]? — 13 area pages + hudson-valley + long-island/staten-island
- Do you install Lorex across all of [area]? — 14 area pages incl. hudson-valley; "in all five boroughs?" — nyc

### Price pages (lorex-camera-installation-prices-*, all 16)
- How much does Lorex camera installation cost in [area]?
- What is included in the installed price?
- Can you hide the wires?
- Is this an exact quote?
- What warranty do I get?
- I already bought Lorex cameras. Will you install them?

### lorex-camera-installation-hudson-valley — REBUILT 2026-10-18 (this run): all old questions above removed; new questions
Q&A H3 (§9 "Your Questions Answered"):
1. How far from the Lorex recorder can a camera sit before the cable run needs help?
2. Can a detached barn or garage run on the same Lorex recorder as the house?
3. Buried cable or a wireless link — which is better for reaching an outbuilding?
4. When does the Lorex Wi-Fi HaLow battery kit make sense on a big lot?
5. What keeps the Lorex recorder recording through a storm outage?
6. Why do some Lorex cameras stay offline after the power comes back?
7. Do cold valley nights drain Lorex battery cameras faster?
8. Can the system be watched from the city when the house runs on Starlink, DSL or a cellular router?
9. Which Lorex app will this system use — Connect, Classic or Pro?
10. Which Hudson Valley counties license the people who run camera cable?
11. Should a town hall, school district or fire company in the valley choose Lorex?
12. What are the state attorney-general lawsuits against Lorex about, and do they change anything for a homeowner?
13. How do you set up a weekend house so you know it is still recording while you are away?
14. Can Lorex detection tell a deer or a bear from a person on the driveway?
15. Can a camera at the house read a car arriving at the far end of a long driveway?
16. Can the coax from an old analog system be reused for new Lorex IP cameras?
Repair H2: "Lorex Dark After a Valley Storm?"

Visible FAQ (§17) = FAQPage:
1. Can one Lorex recorder serve two buildings that sit on separate electric meters?
2. Can the work be done while we are still in the city and the house is empty?
3. Will the camera domes fog or ice over in a Hudson Valley winter?
4. Do summer lightning storms put long outdoor camera cables at risk?
5. Can cameras be fixed to a fieldstone or stone-veneer wall without damaging it?
6. What happens to the footage if a burglar takes the recorder?
7. Can a caretaker or neighbour see the cameras without our account password?
8. Does a camera covering our driveway have to stay off the neighbour's yard?
9. Will cameras in a horse barn or chicken coop survive the dust and damp?
10. How quickly can a crew reach the upper valley, such as Saugerties or Ellenville?

---

## Hudson Valley

Page: `lorex-camera-installation-hudson-valley` (REBUILD in place, 2026-10-18; was crawled-not-indexed as a near-duplicate template). Regional hub: (800) 486-0943 only, GBP Bronx (460 E Fordham Rd, `#bronx`), up-link Home (/), down-links to all six HV county Lorex pages, cross-links to the NYC hub + 5 boroughs (incl. /lorex-camera-installation-brooklyn) and the LI hub + Nassau/Suffolk; WhatsApp only as wa.me/17186790359.

**Thesis (distinct from the parallel Brooklyn rebuild, which is about city rowhouses/apartments):** in the Hudson Valley a Lorex system is planned around the recorder's reach and the recorder's survival, not the camera count — distance from the NVR to each camera (328 ft per Ethernet run; PoE switch / ePoE 800 m at 10 Mbps; Wi-Fi HaLow 500 ft; 2.4 GHz Wi-Fi), whether the NVR, router and switch stay powered through outages on four different utilities, and what internet the house has for remote viewing (Starlink/DSL/fixed wireless; ConnectALL fiber still reaching rural Ulster). Overlaid on that: the county licensing map for cabling (Putnam low-voltage technician licence explicitly covers video surveillance), the second-home/weekend-house pattern, wildlife-driven false alerts, and — new in 2025–26 — state AG lawsuits against Lorex and Lorex's own NDAA disclosure, which steer public buyers (towns, school districts, fire companies) away from Lorex while homeowners decide for themselves.

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/hudsonvalley excerpts R5, R6; Lorex/Starlink R1–R4 (excerpts only) |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so |
| 6 | Landmarks | HV-LM1–LM6 |
| 7 | Use cases / property types | descriptive overview; FLAG: property-type descriptions are general, not statistics |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Hudson Valley One (HV-N1), Lohud (HV-N2), Chronicle (HV-N3), Ulster County (HV-B1), Daily Voice/Times Union/Central Hudson (carried HV-U*) |
| 10 | Hyperlocal | Hudson Valley One (HV-N1); Teatown (carried) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — silo row 1.1 #11 |

### Local news / crime (HV-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| HV-N1 | `Hudson Valley burglary pattern homes 2026 police warn residents security cameras Westchester OR Dutchess OR Orange` · Firecrawl search → scrape (directQuote) | https://hudsonvalleyone.com/2026/09/01/kingston-sees-uptick-in-thefts-as-police-urge-residents-to-stay-alert-amid-economic-strain/ | Sept 1, 2026 (Maura Rosner): Kingston PD Vehicle Theft Prevention Reminder — uptick in larcenies from motor vehicles; "the overwhelming majority … occurred without force", thieves "systematically check vehicle door handles" on cars "parked in residential driveways"; tip-jar thefts from businesses. | §5 para 2; §5.5 bullet; Six Counties (Ulster); Q&A long driveway; Sources |
| HV-N2 | `Westchester police ask residents doorbell camera footage burglary 2026 lohud` · Firecrawl search → scrape (metadata only, body not returned) | https://www.lohud.com/story/news/crime/2026/03/13/elmsford-ny-man-charged-in-connection-to-tarrytown-car-thefts-burglaries/89136093007/ | Mar 13, 2026 (Alexandra Rivera): "An Elmsford man was arrested in connection with multiple residential burglaries and car thefts in Tarrytown." (headline/description only). | Six Counties (Westchester); Sources |
| HV-N3 | same search (excerpt) | https://www.chroniclenewspaper.com/news/local-news/flock-alpr-cameras-orange-county-ny-warwick-goshen-monroe-newburgh-automated-license-plate-recognition-automatic-readers-FC6253878 | Chronicle (Goshen): local police ALPR (Flock) cameras in Warwick/Goshen/Monroe/Newburgh area; police say they helped solve "a car theft ring in Goshen". | Q&A long driveway (context: plate reading is a different product); Sources |
| HV-N4 | same search (excerpts) — Brewster | https://www.wkyc.com/article/news/crime/police-stark-county-searching-man-10-attempted-break-ins-brewster-village/95-b181b335-bb0d-41f3-a9ba-e5cbbb3f3152 | "Village of Brewster" break-ins are in **Stark County, Ohio**, not Brewster NY → NOT USED (wrong geography). | — |
| HV-N5 | carried — research/floodlight-camera-installation.md RD2 | https://www.reddit.com/r/hudsonvalley/comments/1rp1a5r/flock_cameras_approved_in_secret_in_pine_plains/ | r/hudsonvalley unease over licence-plate cameras (Pine Plains). | background (aim at own ground) |

### Broadband (HV-B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| HV-B1 | `Ulster County OR Delaware County rural broadband no internet homes ConnectALL Hudson Valley 2025 2026` · Firecrawl search → scrape (directQuote) | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion | Sept 25, 2025: Ulster County awarded $20.8 million (ConnectALL Deployment Program) to bring broadband to "nearly 1,300 unserved households, businesses, and community facilities" in remote areas; total $61.8M incl. $40.9M Verizon match; Verizon point-to-point fiber; federal BEAD. | §5 para 1; §5.5 bullet; Six Counties (Ulster); Q&A remote viewing; Sources |
| HV-B2 | same (excerpt) | https://broadband.ny.gov/new-ny-broadband-program | New NY Broadband Program: Hudson Valley Wireless fixed wireless to ~40,000 households and 2,000 businesses (statewide program, region not specified in excerpt). | background only |

### Licensing / permits (carried — research/floodlight-camera-installation.md `## Hudson Valley hub` K1–K8; Putnam re-checked today)
| # | Source | Finding | Used |
|---|---|---|---|
| HV-K1 | carried K1 · https://consumer.westchestercountyny.gov/trade-licenses | "Plumbers and Electricians must obtain a trade license from Westchester County in order to work in the county"; licence lookup. | Six Counties; §8.5; Q&A licensing; Sources |
| HV-K2 | carried K2 · https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits ; https://ecode360.com/26997705 | Rockland Ch. 250 electrical contractor = wiring for light, heat, power or signaling on 50 V or more. | Six Counties; §8.5; Q&A licensing |
| HV-K3 | `Putnam County low-voltage technician license video surveillance Chapter 145 consumer affairs` · Firecrawl search (excerpts, re-checked 2026-10-18) · https://ecode360.com/6607815 ; https://www.putnamcountyny.gov/consumer-affairs | Ch. 145 low-voltage/limited-data communications technician: 8,000 hours' experience + exam; installs cabling for "computer networking … audio/video, fiber optics, video surveillance systems and any other system operating at 90 volts or less and a maximum of five amperes where such work commences at an outlet receptacle … previously installed by a person holding the proper electrical license"; no one may advertise or offer that work in Putnam unless licensed; county publishes a list of licensed low-voltage technicians (as of Aug 11, 2026). | Six Counties (Putnam); §8.5; Q&A licensing; Sources |
| HV-K4 | carried K4 · https://ecode360.com/35131702 | Ulster Ch. 185 Electrical Licensing Law; electrical work includes signaling, communication, alarm or data transmission. | Six Counties; Q&A licensing |
| HV-K5 | carried K5a · https://www.orangecountyny.gov/DocumentCenter/View/317/Electrician-Application-PDF ; https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF | Orange: L.L. 8-2007 county electrician licence, revised by L.L. 1-2024. | Six Counties; Q&A licensing |
| HV-K6 | carried K5 | Dutchess: no county contractor licence found → "none found at county level; town rules apply". | Six Counties; Q&A licensing |
| HV-K7 | carried K6 · http://www.fishkill-ny.gov/uploads/3/8/0/7/38072219/building_permit_package_2016_-_commerical___multi-family.pdf | Town of Fishkill: electrical work inspected by an approved independent agency (2016 commercial/multi-family package). | §8.5 (third-party inspection) |
| HV-G6 | carried silo G6 (floodlight) · https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a: private right of action vs someone who installs a video imaging device on adjoining property to record a residential backyard without written consent. | §8.5; FAQ neighbour's yard; Sources |
| HV-G8 | carried silo G8 (floodlight) · https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: ≤50 employees, up to $3,000 per retail location, cameras eligible. | §8.5; Sources |

### Utilities / outages (carried — floodlight HV U1–U7)
| # | Source | Finding | Used |
|---|---|---|---|
| HV-U1 | carried U1 · https://www.oru.com/en/about-us/media-center/corporate-facts | O&R serves Orange, Rockland, Sullivan in NY (~300,000 electric customers incl. northern NJ). | §5.5; Six Counties |
| HV-U2 | carried U2/U3 · https://www.cenhud.com/en/about-us/our-service-territory/ ; https://www.cenhud.com/globalassets/pdf/serviceterritorymap.pdf | Central Hudson ~315,000 electric customers, northern NYC suburbs to the Capital District; villages incl. Saugerties, Ellenville, New Paltz, Montgomery, Cold Spring, Fishkill, Rhinebeck. | §5.5; Six Counties |
| HV-U3 | carried U4 · https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Isaias, Aug 5, 2020: NYSEG 34,150 of 38,693 Putnam customers out. | §5.5; Q&A storm outage |
| HV-U4 | carried U5 · https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php | June 27, 2024 storms: combined 60,000 O&R and Central Hudson customers out. | Q&A storm outage; FAQ lightning |
| HV-U5 | carried U6 · https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 2026 nor'easter: Central Hudson restoring power to "more than 19,000 homes and businesses". | §5 para 1; repair H2; Sources |
| HV-U6 | carried U7 · https://www.nyseg.com/documents/d/nyseg/psc120_section-1 | NYSEG Westchester towns: Bedford, Lewisboro, North Salem, Poundridge, Somers. | Six Counties (Westchester) |

### Wildlife (carried — floodlight HV W1–W2)
| # | Source | Finding | Used |
|---|---|---|---|
| HV-W1 | carried W1 · https://extapps.dec.ny.gov/docs/wildlife_pdf/bbnathis.pdf | DEC: Southern bear range through the Catskills to southern Orange and Rockland at the NJ border; Taconic Highlands south into Putnam; bird feeders most common attractant. | §5.5; Q&A deer/bear |
| HV-W2 | carried W2 · https://www.teatown.org/black-bears-are-back-in-westchester-what-you-need-to-know/ | Westchester reported bear sightings 2 (2019) → 16 (2021). | Q&A deer/bear; §13 card |

### Landmarks / places (HV-LM) — carried with sources
| # | Source | Finding | Used |
|---|---|---|---|
| HV-LM1 | carried floodlight LM1 · https://www.newburghny.org/discover-newburghs-east-end-historic-district/ | Newburgh East End Historic District: "second largest designated historic site in New York State"; Washington's Headquarters. | §7 river-city card; §13 card |
| HV-LM2 | carried LM2 · https://kingston-ny.gov/hlpc | Kingston: five historic districts (Stockade 1974); exterior work visible from public ROW reviewed by HLPC before building permit. | §7; §13 card; Q&A stone walls (FAQ 5 context) |
| HV-LM3 | carried LM6 · https://www.governor.ny.gov/news/governor-hochul-announces-development-partner-build-transit-oriented-housing-beacon-metro | 265 mixed-income units planned on the lot beside Beacon station. | §13 card |
| HV-LM4 | carried W2 (Teatown, Croton-on-Hudson area) | — | §13 card |
| HV-LM5 | carried D5 · https://www.coldspringny.gov/DocumentCenter/View/1793/Ch-0081-Outdoor-Lighting-Standards-PDF | Cold Spring Ch. 81: full-cutoff fixtures incl. single-family; motion lights off when motion stops. | §13 card (camera with built-in light) |
| HV-LM6 | carried D1 · https://www.villageofnewpaltz.gov/wp-content/uploads/2014/10/Outdoor-Lighting-Standards.pdf | New Paltz: fully shielded fixtures; "Motion-sensor security lighting is recommended". | §13 card |
Corridors named on the page (Route 59, Central Avenue, Route 9, Route 17M/Route 211, Route 6, Route 9W/Route 32, Broadway Kingston, Main Street Beacon) are real roads used as place names only; no facts attached (FLAG: no per-corridor source).

### Pricing used (§9 — no invented prices)
Brooklyn labour base from the silo calculator (silo §1.7): $200 per wired camera (line $175 + box $25); $150 recorder setup; 4-camera system $1,795 (labour $950 + equipment $845, equipment not multiplied). Round half-up.
| County | × | Labour per wired camera | Recorder setup | 4-camera system installed | Camera added, from | Recorder with setup, from |
|---|---|---|---|---|---|---|
| Westchester | 1.25 | $250 | $188 | $2,033 | $328 | $508 |
| Rockland | 1.30 | $260 | $195 | $2,080 | $338 | $515 |
| Orange | 1.40 | $280 | $210 | $2,175 | $358 | $530 |
| Putnam | 1.45 | $290 | $218 | $2,223 | $368 | $538 |
| Dutchess | 1.53 | $306 | $230 | $2,299 | $384 | $550 |
| Ulster | 1.53 | $306 | $230 | $2,299 | $384 | $550 |
Service visits after installation: $195/hr, 3-hr minimum ($585) — protected, not multiplied. ePoE runs, wireless bridges, HaLow kits, trenching and electrician work: "quoted after a walk-through" (no price). **FLAG:** these differ slightly from the calculator's paired-county zones on the price pages (e.g. HV page $2,061 / $335 / $508); the hub says the written quote uses the county factor shown.

### House practices stated without an external source (FLAG for Anwar)
- Recorder, router and PoE switch on a UPS; recorder kept in a conditioned interior room, not a garage or barn; recovery test by switching off at the main breaker.
- Outdoor runs in direct-burial or conduit; surge protection at both ends of long runs and grounding (general practice, no source).
- Line-voltage work (new outlets/circuits) done by an electrician licensed for that county/town; AESS does low-voltage under NYS #12000287431. **Confirm** whether AESS holds a Putnam low-voltage technician licence — the page does not claim it does; it says Putnam work is done by or under a Putnam-licensed technician.
- Health/offline notifications and a monthly playback check for weekend houses; shared users for caretakers.
- Stone-wall mounting into mortar joints with sleeve anchors (general practice).
- Two-hour arrival windows, visits any day to 8 PM (silo convention from floodlight/hikvision hubs); "back recording within one to two hours of arrival" (silo convention).
- Field Notes = installer-voice method note (pace the run from the recorder, power-off test, after-dark check), no specific job story.

### Images (11) — Drive: no Lorex folder (checked by main run); CompanyCam not connected
Folder created: `images/lorex-camera-installation/`. 6 real AESS job photos from other jobs (looked at, cropped where needed; no faces, house numbers, plates or readable documents) + 5 Lorex manufacturer product shots already in the repo (labelled as manufacturer product photos). Only names containing `-hudson-valley-`.
| Output (images/lorex-camera-installation/lorex-camera-installation-hudson-valley-…webp) | Source | Crop / note |
|---|---|---|
| lorex-4k-nvr-front-panel-product-photo (900×600) | images/nvr-lorex-4k-16ch.png | none — Lorex product shot |
| lorex-twin-panel-floodlight-camera-product-photo (900×600) | images/floodlight-lorex.png | none — Lorex product shot |
| lorex-white-spotlight-bullet-camera-product-photo (286×176) | images/lorex-bullet-spotlight-camera-installation-hudson-valley.jpg | none — Lorex product shot |
| lorex-wifi-pan-tilt-camera-with-two-antennas-product-photo (275×183) | images/lorex-wifi-ptz-camera-installation-hudson-valley.jpg | none — Lorex product shot |
| lorex-black-video-doorbell-product-photo (423×562) | images/lorex-2k-video-doorbell.webp | none — Lorex product shot |
| dome-camera-under-eave-against-bare-winter-trees (442×430) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-white-dome-camera-under-storefront-fascia.webp | crop (205,0,647,430): mural excluded |
| dome-camera-on-long-wall-arm-over-stone-facade (228×380) | images/dahua-camera-installation/dahua-camera-installation-long-island-dome-camera-on-long-wall-arm-on-stone-facade.webp | none |
| blue-and-white-network-cable-bundles-along-ceiling (760×250) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-cable-bundles-above-recorder-monitor.webp | crop (0,0,760,250): monitor and camera tiles excluded |
| turret-camera-in-corner-of-unfinished-storage-room (725×560) | images/dahua-camera-installation/dahua-camera-installation-orange-county-turret-camera-in-storage-room-corner.webp | crop (0,0,725,560): window and stored lumber excluded |
| small-black-camera-and-sensor-on-pale-wall (630×360) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-long-island-black-mini-bullet-and-motion-sensor-on-wall.webp | none |
| recorder-playback-view-along-brick-wall-to-paved-lot (547×283) | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-recorder-view-along-brick-wall-to-lot.webp | crop (0,35,547,318): date stamp and camera label excluded |
Rejected: images/parking/*hudson-valley*.webp (look AI-generated — garbled sign text; v2.3 bans AI images).


## Brooklyn — merged 2026-10-18 from the Brooklyn build (silo findings, question register incl. this page's questions, local section)

## Lorex Camera Installation — Brooklyn research (incoming)

Written 2026-10-18 by the REBUILD of `lorex-camera-installation-brooklyn`. `research/lorex-camera-installation.md` is being created in parallel by the Hudson Valley rebuild; this file is the Brooklyn contribution for the main run to merge (silo findings gathered here + full question register + `## Brooklyn`). Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page section used**. Tools: WebSearch, WebFetch, Firecrawl search (excerpts). Shell curl blocked. Nothing below is invented; "excerpt" = only the search snippet was read.

### 1. Source matrix (blueprint v2.3 §3)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts only via Firecrawl search (rows R1–R9). Full threads not scraped. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and tests seven claims that circulate in Lorex listings, forums and how-to articles against Lorex's own pages. |
| 6 | Area landmarks | Brooklyn rows L1–L6 (mostly carried from research/floodlight-camera-installation.md, URLs fetched by earlier runs) + L7 (Kagan/boardwalk). |
| 7 | Use cases / building stock | Brooklyn H1 (Census ACS, carried). |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) — no related/autocomplete surface. |
| 9 | Local news | Hoodline (Jul + Sep 2026, NYPD/PIX11 sourced), Brooklyn Paper (Kagan), CBS NY (2019 Park Slope lobby theft). |
| 10 | Hyperlocal | Brooklyn Paper; r/parkslope (excerpt). BK Eagle/Bay News/Caribbean Life Lorex-specific: EMPTY (no hit). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not searched again this run; floodlight Brooklyn run found only list pages. |

### 2. Silo findings (Lorex, all areas)

#### 2.1 Lorex product / platform facts (Lorex sources only)
| ID | Exact query · platform | URL | Finding | Page section (Brooklyn) |
|---|---|---|---|---|
| X1 | `Lorex PoE camera maximum cable length NVR Cat5e 328 ft support` · WebSearch → WebFetch | https://www.lorex.com/en-au/blogs/help/cables-ethernet-cable-length | "The maximum Ethernet cable length that can be used between an NVR and a camera is 328ft (100m)"; PoE switch can be added for longer (text truncated). | §5.5 bullet 4; §10.5 H3 1; Sources |
| X2 | `Lorex Fusion NVR wired and Wi-Fi cameras how many Wi-Fi devices support` · WebSearch → WebFetch | https://pro.lorex.com/products/lorex-fusion-series-4k-16-channel-8-wired-8-fusion-wi-fi-2tb-wired-system-with-h12-wired-4k-ip-bullet-cameras | Fusion 4K 16-ch (8 wired + 8 Fusion Wi-Fi), N910A62 recorder, H12 cameras; **max PoE run 300 ft**, longer needs separate power; Cat5e works, Cat6 recommended; 2TB expandable to one 16TB; IP67; Smart Motion, person/vehicle; two-way audio/siren/lights; **Lorex Classic app**; remote access needs wired NVR-to-router, **min 6 Mbps upload** recommended. | §9 C1 H3 1; §9 C2 H3 1; §9 C3 H3 3; §10.5 H3 1; Sources |
| X3 | `Lorex app vs Lorex Classic app which app for my device help` · WebSearch → WebFetch | https://www.lorex.com/pages/lorex-apps | Three apps: **Lorex Connect** (wired + Wi-Fi, home/business), **Lorex Classic** ("Previously known as the Lorex App", Fusion line, home), **Lorex Pro** (wired only, commercial/SMB, up to 16-camera multi-view). Compatibility tool. | §8 intro; §9 C4 H3 1; §10.5 H3 4; Sources |
| X4 | `Lorex warranty policy …` · WebSearch → WebFetch | https://www.lorex.com/en-au/products/lorex-connect-new-app-v-series-8ch-4k-nvr-system-3-white-ip-poe-cameras | Lorex Connect V-Series 8ch 4K NVR + 3 PoE cams; "Supports up to 8 PoE cameras, with each channel providing power and data over a single Ethernet cable"; "No Monthly Fees … Own it. No subscriptions required."; monitor-less setup mode. | §10 recorder card; §10.5 H3 2; Sources |
| X5 | `lorex.com pages warranty …` · WebSearch → WebFetch | https://www.lorex.com/pages/frequently-asked-questions | "Every Lorex product also includes a one-year warranty"; 30-day returns; "No Monthly Fees" badge; **"Lorex products are designed for consumer and business use only and not for US federal governments, federally-funded projects or contractors subject to NDAA."**; "Some Lorex products are subject to FCC import/marketing restrictions."; audio: "Audio monitoring is not always legal in all areas"; Connect Cloud+ product category. | §8.5 bullet 2; §9 C5 H3 3; §9 C7 H3 3; §10.5 H3 2, 6; §15.5 BYOE; Sources |
| X6 | `Lorex FCC import marketing restriction 2026 …` · WebSearch → WebFetch | https://www.lorex.com/pages/fcc-notice-regarding-certain-legacy-surveillance-equipment | Lorex notice (updated July 15, 2026): FCC **Public Notice DA 26-635** (June 26, 2026), effective **July 16, 2026**; "Some Lorex-branded products are produced by a company whose products are on the FCC's Covered List"; not marketed/sold for public safety, critical-infrastructure surveillance, government facilities, other national-security purposes; "does not create a blanket ban"; existing equipment use/service/support continues; firmware updates, pricing, support, warranty unaffected (replacement-parts caveat for restricted uses); Lorex may ask end use; schools, utilities, municipalities contact Lorex; "not legal advice". | §8.5 bullet 3; §9 C5 H3 1, H3 3; §10.5 H3 6; Sources |
| X7 | `Lorex NVR hard drive recording time calculator …` · WebSearch → WebFetch | https://pro.lorex.com/pages/hdd-calculator | Inputs: resolution 2–12 MP, 7–30 fps, bitrate, daily hours (default 2), cameras, storage; H.265 assumed; motion ≈ "120 events (30 seconds each) for each hour of recording"; Nano Codec ≈ 40–50% smaller, "select recorders, such as the X Series"; estimate approximate. | §9 C7 H3 2; Sources |
| X8 | `Lorex Wi-Fi camera 2.4 GHz requirement distance from router help article` · WebSearch → WebFetch | https://help.lorex.com/link/portal/57356/57366/Article/3714/w881aa-4k-spotlight-wi-fi-camera-frequently-asked-questions | W881AA: 2.4 or 5 GHz; "Place the camera close to your Wi-Fi router as possible"; "Reduce the number of obstructive materials between the camera and the router or access point." | §9 C3 H3 1; §10.5 H3 3; Sources |
| X9 | `Lorex wired video doorbell power requirements 16-24 VAC transformer help` · WebSearch → WebFetch | https://lorex.com/blogs/help/what-transformer-should-i-use-with-my-wired-video-doorbell | 4K/2K/1080p wired doorbells "require a constant power supply with a voltage between 16V-24V AC"; "Most older homes only have 10V transformers which do not provide enough voltage"; plug-in adapter AP24V500B listed. | §6 card; §9 C3 H3 2; §10 card; §10.5 H3 5; image caption 11; Sources |
| X10 | `Lorex Smart Motion Detection person vehicle …` · WebSearch → WebFetch | https://www.lorex.com/blogs/help/n845-n846-n847-n864-series-person-vehicle-and-animal-detection | Meta only: smart motion for person/vehicle/animal; "supports detection of people and vehicles with compatible IP cameras only". | FAQ 7 |

#### 2.2 Ownership, FCC and state lawsuits
| ID | Exact query · platform | URL | Finding | Page section |
|---|---|---|---|---|
| O1 | `Lorex Skywatch ownership Dahua FCC covered list statement Lorex` · WebSearch → WebFetch | https://ago.nebraska.gov/node/2446 | Nebraska AG, **Sept 23, 2025**: sued Lorex (Consumer Protection Act, UDTPA); cameras sold at Costco and other retailers; Lorex said cameras "safe and secure", could go in a child's bedroom; alleges ties to Dahua; Dahua sold Lorex to Skywatch in 2022 one day before the FCC order; no Lorex response quoted. | §9 C5 H3 2 (child's bedroom); Sources |
| O2 | same · WebFetch | https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-files-third-anti-ccp-lawsuit-three-days-suing-baby-monitor-company-lorex | Texas AG, **Feb 19, 2026**: DTPA suit re Lorex baby monitors/Dahua components; Dahua acquired Lorex 2018; sold to Skywatch **Nov 24, 2022**, one day before FCC order; up to $10,000 per violation; allegations, not findings. | §9 C5 H3 1–2; Sources |
| O3 | carried from research/dahua-camera-installation.md (fetched 2026-10-18) | https://www.securityworldmarket.com/int/News/Business-News/dahua-to-sell-lorex-to-skywatch-for-usd-72-million | Dahua agreed to sell Lorex (Ontario) to Skywatch (Taipei) for ~US$72M (Dec 2, 2022). | §9 C5 H3 1; Sources |

#### 2.3 Reddit / forums (silo)
| ID | Exact query · platform | URL | Finding (excerpt) | Page section |
|---|---|---|---|---|
| R1 | `site:reddit.com r/Lorex app offline NVR problems complaints` · Firecrawl search | https://www.reddit.com/r/Lorex/comments/1p654ro/android_app_updated_to_lorex_classic_and_now_i/ | "Android app was working fine … now it's called Lorex Classic and it does not accept my login of local LAN NVR." | §9 C4 H3 1; §10.5 H3 4; Sources |
| R2 | same | https://www.reddit.com/r/Lorex/comments/1imghhy/issues_throughout_new_servers_no_longer_selling/ | Installer: customers "unable to connect to their NVR using the Lorex Home app"; "No longer selling Lorex". | §10.5 H3 4; Sources |
| R3 | same | https://www.reddit.com/r/Lorex/comments/1t6npw4/why_does_the_lorex_app_suck_so_bad/ | Intermittent "failed to find network host"; cameras return on PoE network minutes later. | Background (offline section) |
| R4 | same | https://www.reddit.com/r/Lorex/comments/1nuki74/lorex_tech_is_awful_and_i_just_cant_anymore/ | "person detection and AI detection is terrible … build quality is great". | Background FAQ 7 (tune detection) |
| R5 | `reddit Lorex NVR brownstone Brooklyn cameras installer wiring` · Firecrawl search | https://www.reddit.com/r/SecurityCamera/comments/1jzbx8p/new_house_lorex/ | "moved into a new house that has Lorex cameras around the outside. Not sure how to connect them to the app?" | §9 C4 H3 2; Sources |
| R6 | same | https://www.reddit.com/r/Lorex/comments/1sg72y6/how_do_we_install_these_in_a_two_story_house/ | "buy 'Fish-rods' … running the cables through tight areas". | Background (cable routes) |
| R7 | same | https://www.reddit.com/r/Lorex/comments/177hrp7/help_lorex_nvr_sucks/ | "Camera setup is difficult." | Background |

#### 2.4 Keywords — five layers (silo, Brooklyn emphasis)
- **Service:** Lorex camera installation, Lorex installer, Lorex NVR installation, Lorex system setup, Lorex doorbell installation, Lorex Fusion installation, install my Lorex kit, Lorex camera repair.
- **Problem:** Lorex offline, Lorex app won't connect, Lorex Classic login, inherited Lorex system, Wi-Fi through brick walls, doorbell not powering, footage overwritten, police footage export, package theft, basement-door burglary, privacy/neighbor yard, audio legality.
- **Technology:** PoE, Cat6, 328 ft / 300 ft, NVR, Fusion 8+8 channels, Lorex Connect / Classic / Pro apps, H.265, Nano Codec, person/vehicle detection, privacy masks, 16–24 VAC doorbell transformer, HDMI extender, UPS.
- **Industry:** brownstone owners, two-/three-family landlords, co-op/condo boards, walk-up owners, bodegas/salons/restaurants, Industry City/Navy Yard tenants.
- **Geographic (Brooklyn page):** Brooklyn + neighborhoods listed in Service schema and §13; corridors Fifth Ave (Bay Ridge), Fulton Mall, Nostrand/Church/Flatbush Aves, Industry City, Navy Yard, Gowanus/Carroll Gardens/Greenpoint.

#### 2.5 Pricing basis (silo; no invented prices) — Brooklyn = §9 base 1.00×
| Figure used | Source in repo |
|---|---|
| 4-camera Lorex system installed from **$1,795**; cameras installed **$278–$1,376** each; recorders with setup from **$470**; hidden in-wall wiring **$200/camera**; wire up to 100 ft/camera, ≥2 weeks drive, app setup included; 2-camera kits from **$1,080** (CN201U3 U3 2K+); 6-camera Fusion H12 **$2,274**; 8-camera Fusion A4 **$2,950** | lorex-camera-installation-prices-brooklyn.html (calculator page, read 2026-10-18) |
| Ranges $1,800–$3,500 (4–6 cams) / $3,500–$8,000 (8–16) / $8,000+ | old lorex-camera-installation-brooklyn.html package cards (pre-rebuild) |
| BYOE **$175 per camera line** (Cat6 ≤100 ft, mount, terminate, connect); concealed $200 | install-your-own-camera-system.html AREAS.brooklyn {line:175, conceal:200, hourly:195} |
| Service **$195/hr, 3-hr min ($585)** | blueprint v2.3 §9 (protected) |
FLAGS: prices-brooklyn page states a 30-day install warranty + optional 1/2/3-yr extended warranty (conflicts with the one-year parts-only terms sentence used on the rebuilt page — not repeated on the page); old Brooklyn page said both "$400–$700" and "$400–$750 per camera" (not used).

### 3. Question register — every FAQ / Q&A / "?" heading on the lorex-camera-installation-* pages
Read 2026-10-18 from all 16 area pages (before either rebuild landed) and all 16 -prices- pages. The Brooklyn rebuild also compared its questions against the Hudson Valley rebuild's questions as they stood at ~08:00Z (27 headings) and rewrote 8 overlapping intents (app choice, AG lawsuits, who-should-not-buy, recorder theft, outage, stone-wall drilling, weather, TV output).

#### Old template intents asked on all or most pre-rebuild area pages (read 2026-10-18 before the Brooklyn and Hudson Valley rebuilds) — never reuse
- Why Choose Lorex Security Cameras?  _(on 16 of 16 area pages; geo varies)_
- How much does Lorex camera installation cost in the Bronx?  _(on 13 of 16 area pages; geo varies)_
- Is Lorex cheaper than other camera brands?  _(on 16 of 16 area pages; geo varies)_
- Are Lorex cameras good?  _(on 16 of 16 area pages; geo varies)_
- Can Lorex cameras be viewed on a phone?  _(on 16 of 16 area pages; geo varies)_
- Can I install Lorex cameras myself?  _(on 16 of 16 area pages; geo varies)_
- Which Lorex camera is best for a warehouse?  _(on 16 of 16 area pages; geo varies)_
- Why is my Lorex camera offline or not recording?  _(on 16 of 16 area pages; geo varies)_
- I forgot my Lorex password — can it be reset?  _(on 16 of 16 area pages; geo varies)_
- Why does my night footage look blurry or washed out?  _(on 16 of 16 area pages; geo varies)_
- Is Lorex banned in the US?  _(on 16 of 16 area pages; geo varies)_
- Do I need to notify people they’re being recorded?  _(on 16 of 16 area pages; geo varies)_
- Ready for a Lorex system in the Bronx?  _(on 13 of 16 area pages; geo varies)_
- Do you install Lorex across all of the Bronx?  _(on 14 of 16 area pages; geo varies)_
- Are you licensed and insured?  _(on 16 of 16 area pages; geo varies)_
- Do you offer a warranty?  _(on 16 of 16 area pages; geo varies)_
- What are the best Lorex cameras for apartment buildings?  _(on 16 of 16 area pages; geo varies)_
- Can you upgrade my old cameras to Lorex?  _(on 16 of 16 area pages; geo varies)_
- Do you service Lorex systems you didn’t install?  _(on 16 of 16 area pages; geo varies)_
- Will my Lorex system work without internet?  _(on 16 of 16 area pages; geo varies)_
- How do I get started?  _(on 16 of 16 area pages; geo varies)_
- Can I add more cameras later?  _(on 16 of 16 area pages; geo varies)_
- Do you integrate Lorex with access control or alarms?  _(on 16 of 16 area pages; geo varies)_
- What resolution do you recommend?  _(on 16 of 16 area pages; geo varies)_
- Is there a warranty?  _(on 16 of 16 area pages; geo varies)_
- How many Lorex cameras do I need?  _(on 16 of 16 area pages; geo varies)_
- How long does Lorex footage stay recorded?  _(on 16 of 16 area pages; geo varies)_
- Can Lorex cameras record audio?  _(on 16 of 16 area pages; geo varies)_
- What internet speed do Lorex cameras need?  _(on 16 of 16 area pages; geo varies)_
- Where is the install?  _(on 16 of 16 area pages; geo varies)_

#### Per-page variants on pre-rebuild area pages (one or two pages each)
- lorex-camera-installation-hudson-valley: How much does Lorex camera installation cost in the Hudson Valley?
- lorex-camera-installation-hudson-valley: Ready for a Lorex system in the Hudson Valley?
- lorex-camera-installation-hudson-valley: Do you install Lorex across all of the Hudson Valley?
- lorex-camera-installation-long-island: How much does Lorex camera installation cost on Long Island?
- lorex-camera-installation-long-island: Ready for a Lorex system on Long Island?
- lorex-camera-installation-nyc: Do you install Lorex in all five boroughs?
- lorex-camera-installation-staten-island: How much does Lorex camera installation cost on Staten Island?
- lorex-camera-installation-staten-island: Ready for a Lorex system on Staten Island?

#### lorex-camera-installation-prices-* pages (16 calculator pages; same six questions on each, area name varies)
- How much does Lorex camera installation cost in Brooklyn?
- What is included in the installed price?
- Can you hide the wires?
- Is this an exact quote?
- What warranty do I get?
- I already bought Lorex cameras. Will you install them?

#### lorex-camera-installation-brooklyn — REBUILT 2026-10-18 (this run): Q&A H3 + repair H2 + FAQ
- [Q&A/H2] Lorex Cameras Gone Dark or Offline in Brooklyn?
- [Q&A/H2] Cellar, parlor-floor closet or top floor — where should the Lorex recorder go in a brownstone?
- [Q&A/H2] The router is upstairs and the only dry room is the cellar — can the recorder and the router sit on different floors?
- [Q&A/H2] Why shouldn't the Lorex recorder sit on the media shelf beside the parlor television?
- [Q&A/H2] How does a network cable travel from the rear yard to the stoop of an attached house without opening the walls?
- [Q&A/H2] Where the cable passes through the brick, will water or mice follow it in?
- [Q&A/H2] Can a Lorex camera go on the shared wall or fence at the side of our yard?
- [Q&A/H2] Which spots on a Brooklyn property actually justify a Lorex Wi-Fi camera instead of a cable?
- [Q&A/H2] Can a Lorex doorbell on the stoop run off the house's old doorbell wiring?
- [Q&A/H2] Our Fusion recorder takes Wi-Fi cameras — is there a limit to how many we should add?
- [Q&A/H2] Our phone app turned into “Lorex Classic” overnight and will not sign in — is the recorder broken?
- [Q&A/H2] We bought a house that came with Lorex cameras — how do we take the system over?
- [Q&A/H2] Our landlord put Lorex cameras in the hallway — what are they allowed to record?
- [Q&A/H2] Lorex used to belong to Dahua — who owns it now, and why does that matter for a house?
- [Q&A/H2] Is it wise to put a Lorex indoor camera in a child's bedroom?
- [Q&A/H2] If we buy Lorex in 2026, will replacement cameras still be available in a few years?
- [Q&A/H2] In a narrow Brooklyn storefront, where should the Lorex recorder and monitor go?
- [Q&A/H2] Our building has a store downstairs and apartments above — should it be one Lorex system or two?
- [Q&A/H2] Is a Lorex system covered by New York's tax credit for small retailers?
- [Q&A/H2] An NYPD detective asked for our camera footage — how do we get a clip off a Lorex recorder?
- [Q&A/H2] How do we make sure an important clip is not overwritten before we save it?
- [Q&A/H2] Is it legal in New York for our yard camera to pick up the neighbors talking?
- [FAQ] How long does a typical Brooklyn Lorex installation take, and do we need to move furniture?
- [FAQ] A street tree hides the front of our house all summer — where should the front camera go?
- [FAQ] Can the Lorex system keep running while we gut-renovate the house?
- [FAQ] Do we need our co-op or condo board's permission before cameras go on the building?
- [FAQ] What upkeep do the Lorex cameras and recorder need after installation?
- [FAQ] We are selling the house — what should we do with the Lorex system?
- [FAQ] Will pigeons on the cornice or a cat crossing the yard flood our phones with alerts?
- [FAQ] Will the recorder be noisy if it goes in a bedroom closet?
- [FAQ] Do you take away the old analog DVR and cameras when the new Lorex system goes in?
- [FAQ] How do we pay for a Brooklyn Lorex installation?

### Brooklyn

Page: `lorex-camera-installation-brooklyn` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Up-link `/lorex-camera-installation-nyc`. GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`). Direct line (347) 934-8335 in body, CTAs, forms copy and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (+ footer text).

**Thesis:** in Brooklyn a Lorex system is decided by where the recorder lives in an attached, pre-1940 house and how each PoE cable gets from it to the two exposed faces (stoop/vestibule/areaway and garden door/yard) through cellar, brick and plaster — wired beats Wi-Fi in masonry; plus the Brooklyn-specific ownership questions (two-family/walk-up access, landlord hallway cameras, inherited systems at resale) and the 2026 Lorex context (three apps, FCC DA 26-635 notice, NE/TX AG suits). Hudson Valley page is about distance, outbuildings, outages, rural internet — different.

#### Building stock (H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| H1 | carried from research/floodlight-camera-installation.md H1 (Census API ACS 2023 5-yr, Kings County) | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36047 | 1,090,187 units; median year built 1943; 513,629 built ≤1939; 1-unit attached 93,812; detached 52,359; 2-unit 175,805; 3–4 unit 170,655. | §5 para 1; §5.5 bullets 1–3; §7 two-family H3; §10.5 H3 5 |
| H2 | `brownstone wifi signal brick walls floors mesh ethernet Brooklyn reddit` · Firecrawl search | https://www.reddit.com/r/HomeNetworking/comments/ho9t6m/mesh_network_for_4floor_nyc_brownstone/ | Excerpt: "brick 4-story brownstone in NYC. The router is centrally located on floor 3, and doesn't get great signal through the floors and walls." | §5 para 2; §10.5 H3 3 |
| H3 | same | https://www.reddit.com/r/Brooklyn/comments/1c1jc65/standard_router_or_mesh_for_wifi_in_brownstone/ | Excerpt: mesh "makes sense in a brownstone layout (long and narrow)". | Background §9 C3 |
| H4 | `site:reddit.com r/Brooklyn security cameras brownstone backyard …` · Firecrawl search | https://www.reddit.com/r/EufyCam/comments/1ncbxp1/disappointed_in_my_eufy_cams/ | Excerpt: "It's a Brooklyn brownstone so the front yard is like 20' wide and 10' deep. There is significant overlap between the camera and doorbells." | §5 para 2 |
| H5 | same | https://www.reddit.com/r/parkslope/comments/1mt5ft7/packages_in_brownstones/ | Excerpt: "Install an intercom buzzer system with a camera so you can let the uniformed delivery people inside the front entrance". | §5 para 2 |
| H6 | same | https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ | Excerpt: neighbor's Ring on hallway wall facing elevator wait area. | Background §9 C4 H3 3 |
| H7 | same | https://www.reddit.com/r/lowvoltage/comments/1o0rlwj/msp_looking_for_a_reliable_professional_partner/ | Excerpt: "6 security cameras installed ・ brownstone in Brooklyn Heights NY … POE". | Background only |

#### Landmarks / corridors (L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | carried (floodlight L3) | https://thebha.org/neighborhood/ | Brooklyn Heights HD designated Nov 23, 1965, first in NYC. | §13 |
| L2 | carried (floodlight H3) | https://hdc.org/hdc-across-nyc/brooklyn/deserving-designated/park-slope/ | Park Slope HD 1973; South Slope extension 2012; 2–3-storey rowhouses, deep front yards. | §13 |
| L3 | carried (floodlight C1) | https://www.bayridgebid.com/ | Fifth Ave BID 65th–85th St. | §8; §13 |
| L4 | carried (floodlight C2) | https://en.wikipedia.org/wiki/Fulton_Street_(Brooklyn) | Fulton Mall, Fulton St between Flatbush Ave and Adams St. | §8 |
| L5 | carried (floodlight L5) | https://industrycity.com/ | "6-million-square-foot" former Bush Terminal. | §8; §13 |
| L6 | carried (floodlight L6) | https://www.brooklynnavyyard.org/brooklyn-navy-yard-fy25-impact-report/ | >300 acres; >550 businesses. | §8; §13 |
| L7 | `Brooklyn council member free security cameras giveaway homeowners 2025` · WebSearch → WebFetch | https://www.brooklynpaper.com/council-member-kagan-announces-public-safety-and-security-upgrades | Undated (refers to FY2024 budget): CM Ari Kagan — $240,000 NYPD cameras at Kaiser Park, Stillwell Ave, Riegelmann Boardwalk W 28th–29th St; $150,000 unmarked vans 60th Pct. | §13 card (boardwalk); Sources |
| L8 | carried (floodlight G3) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf | Attach at mortar joints/plain masonry, not cast iron/decorative; discreet spots beneath band course, under stoop, behind areaway wall. | §7.5 masonry; §9 C2 H3 2; §10.5 H3 7 |

#### News / hyperlocal (N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | `Brooklyn burglary rear window backyard 2026 surveillance video NYPD seeks` · WebSearch → WebFetch | https://hoodline.com/2026/07/basement-bandit-hits-11-brooklyn-businesses-as-cops-hunt-serial-burglar/ | Jul 22, 2026: 11 commercial burglaries, 76th/77th/78th/79th/83rd/94th Pcts (Carroll Gardens, Gowanus, Crown Heights, Park Slope, Bed-Stuy, Bushwick, Greenpoint); entry through "basement-level doors"; NYPD Crime Stoppers images; asked for time-stamped doorbell, delivery-camera or in-store video. | §5 para 3; §5.5 bullet 5; §8 card 6; §9 C6 H3 1 |
| N2 | `Brooklyn package theft stoop 2026 news brownstone porch pirates camera` · WebSearch → WebFetch | https://hoodline.com/2026/09/brooklyn-porch-pirate-swipes-17-400-in-rare-sports-cards-nypd-says/ | Sep 14 incident (pub. Sep 18, 2026), via PIX11: man entered a residential building near West End Ave and Shore Blvd, took packages with sports cards valued ~$17,400; surveillance images released. | §5 para 3 |
| N3 | same · WebFetch | https://cbsnews.com/newyork/news/park-slope-package-thieves-caught-on-camera-nypd-brooklyn | Aug 20, 2019: three suspects on video opening packages in a Park Slope building lobby. | Background only (old) |
| N4 | `Brooklyn council member …` (see L7) | — | — | — |

#### Rules / licensing (Brooklyn / NYC / NYS)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `NYC Department of Buildings electrical permit not required low voltage security camera wiring Class 2 exemption` · WebSearch → WebFetch | https://intro.nyc/local-laws/2024-128 | LL 128/2024: low-voltage = "designed to operate at less than 50 volts for signaling, communication, alarm, and data transmission circuits"; no electrical permit for low-voltage work by master/special electrician or qualified person; some low-voltage work (life safety, control circuits switching light/power) reserved to electricians. Effective date not in excerpt. | §5.5 bullet 6; Sources |
| G2 | `New York State Department of State security and fire alarm installer license …` · WebSearch → WebFetch | https://ur.nyc-business.nyc.gov/nycbusiness/description/license-to-install-service-or-maintain-security-or-fire-alarm-systems | NYS DOS license needed to install/maintain security or fire alarm systems; page does not mention video/CCTV. | Background (license # is protected content) |
| G3 | `nysenate.gov Penal Law 250.05 …` · WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/PEN/250.05 ; https://nysenate.gov/legislation/laws/PEN/250.00 | Eavesdropping incl. "mechanical overhearing of a conversation" = class E felony; defined as recording a conversation "without the consent of at least one party thereto, by a person not present thereat". | §8.5 bullet 1; §9 C7 H3 3 |
| G4 | carried (floodlight G6) | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a: action vs neighbor who installs device on adjoining property recording a backyard without written consent. | §7.5; §9 C2 H3 3 |
| G5 | carried (floodlight G7) | https://nysenate.gov/legislation/laws/pen/250.40 | Places where a person may reasonably expect to disrobe in privacy. | §8.5 bullet 4 |
| G6 | carried (floodlight G8) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: ≤50 employees; up to $3,000 per retail location; cameras eligible. | §9 C6 H3 3 |
| G7 | `NYC landlord install security cameras rent stabilized building DHCR tenant hallway cameras rules` · WebSearch → WebFetch | https://new.brickunderground.com/roommates-landlords/as-landlords-use-security-camera-footage-against-tenants-in-court-heres-how-to-protect-your-privacy | Jan 19, 2017 (updated): hallway cameras not illegal; landlords may not set cameras to "see" into apartments; footage used in primary-residence cases. | §9 C4 H3 3 |
| G8 | same · WebFetch | https://www.newyorkappellatedigest.com/2018/10/10/okay-to-replace-part-time-lobby-attendants-with-video-surveillance-second-dept-%e2%80%8b/ | Matter of Bazile v Rubin, 2018 NY Slip Op 06737 (2d Dept, Oct 10, 2018): DHCR rationally found video surveillance an adequate substitute for part-time lobby attendants (9 NYCRR 2522.4[e]). | §9 C4 H3 3 |

#### Yelp
EMPTY (not accessible in build env).

#### House practices stated on the page without an external source (FLAG for Anwar)
- Recorder placement preferences (cellar/closet, not beside the TV, ventilated lockbox), cable via cellar ceiling and rear-wall raceway, mortar-joint sleeved entries with drip loops, Cat6 throughout, siding mounting blocks, no powerline/Wi-Fi bridge between recorder and router.
- Two-family access plan (owner holds recorder, per-camera user list, tenant removal at move-out); separate recorders for store vs residential.
- Audio off by default outdoors/in stores; indoor cameras never in bedrooms; unique passwords, firmware at install, no router port openings.
- Timings: 1 day for 2–4 cameras with open cellar, 2 days for 8/finished cellar; "one to two hours of arrival" restore (silo convention, blueprint §5 el. 36); two-hour windows 7 days to 8 PM (copied from floodlight Brooklyn).
- FAQ practice answers: board approvals/COI free (COI free per install-your-own page), payment (50% deposit per terms sentence; small jobs paid in full — install-your-own page says under $500 full payment), old DVR removal, upkeep schedule, noise, street trees, renovation.
- Worked price example (§14) is arithmetic on published prices; raceway "listed as a line item" (install-your-own page lists raceway add-on but the Lorex installed price page does not say whether it is included).
- Comparison table ADT/Ring/SimpliSafe is generic (no source fetched this run) — check before relying on it.
- Building-type neighborhood lists (frame rowhouses in Bushwick/Sunset Park/East New York/Gravesend; mixed-use on Myrtle/Church Aves) are descriptive, unsourced.
- Field Notes = method note, not a job story.

#### Images (11) — Drive: no Lorex folder (per main run); CompanyCam not connected
Permanent image rule: 6 real AESS job photos from other jobs (borrowed from images/dahua-camera-installation/, images/commercial-security-camera-installation/, images/hikvision-security-camera-installation/) + 5 Lorex manufacturer product shots from images/lorex-*. All looked at with Read. Avoided the source scenes the Hudson Valley rebuild had already used (brick-wall lot view, storage-room turret, cable bundles, Wi-Fi PTZ, black blue-ring doorbell, floodlight, spotlight bullet, NVR). **Library FLAG:** images/lorex-dual-lens-panoramic, lorex-fisheye-360, lorex-vandal-dome, lorex-nocturnal-ptz, lorex-ptz-dome, lorex-indoor-ptz (area copies) and lorex-smart-deterrence show **Uniview (UNV)-branded** cameras, not Lorex; lorex-mini-ptz-active-deterrence-nyc shows a Lorex bullet, lorex-indoor-ptz-dome-nyc a Lorex indoor cube cam (filenames wrong). Lorex product shots are small (≤423 px wide).

| Output (images/lorex-camera-installation/) | Source | Crop | Placement |
|---|---|---|---|
| lorex-camera-installation-brooklyn-ceiling-dome-camera-facing-glass-entrance-doors.webp (935×700) | dahua-camera-installation/…-suffolk-county-turret-camera-above-glass-storefront.webp | (0,0,935,700) | Hero (eager) |
| …-black-bullet-camera-at-ceiling-over-grey-door.webp (635×760) | dahua-camera-installation/…-long-island-bullet-camera-aimed-down-corridor-to-door.webp | (0,0,635,760) | §5 |
| …-black-lorex-turret-camera-product-photo.webp (275×183) | images/lorex-turret-network-camera-installation-nyc.jpg | none | §6 |
| …-white-dome-camera-under-painted-fascia-and-mural.webp (647×470) | commercial-security-camera-installation/…-dutchess-county-white-dome-camera-under-storefront-fascia.webp | none | §7 |
| …-hanging-monitor-with-store-aisle-camera-grid.webp (525×370) | dahua-camera-installation/…-suffolk-county-camera-grid-on-ceiling-mounted-monitor.webp | none | §8 |
| …-white-lorex-indoor-cube-camera-on-stand-product-photo.webp (180×183) | images/lorex-indoor-ptz-dome-camera-installation-nyc.jpg | (50,0,230,183) | §9 C4 |
| …-recorder-screen-per-channel-bitrate-readings.webp (800×170) | hikvision-security-camera-installation/…-long-island-recorder-screen-empty-channels-and-bitrate-table.webp | (0,10,800,180) | §9 C7 |
| …-black-lorex-bullet-camera-with-red-warning-led-product-photo.webp (275×183) | images/lorex-mini-ptz-active-deterrence-camera-installation-nyc.jpg | none | §10 |
| …-black-mini-dome-camera-at-ceiling-edge.webp (605×400) | dahua-camera-installation/…-suffolk-county-black-mini-dome-on-ceiling-grid.webp | none | §14 |
| …-white-lorex-turret-camera-with-spotlight-product-photo.webp (225×225) | images/lorex-color-night-vision-turret-camera-installation-brooklyn.jpg | none | Field Notes |
| …-black-lorex-video-doorbell-with-green-ring-product-photo.webp (423×562) | images/lorex-2k-video-doorbell.webp | none | FAQ |
All WebP q80, ≤1600 px. Alt/title unique, each contains "Brooklyn"; captions say "example photo from another AESS job (not a Brooklyn …)" or "manufacturer product photo / Lorex catalog image (not an installed camera)".

#### Build notes
- Rendered words 13,566; title 55; meta 154; 6 JSON-LD blocks; FAQ 10 = schema 10; HowTo 7 = process cards 7; 2 Web3Forms forms (hf/qf), landing_page extensionless.
- simcheck: page-level max 0.067 (vs hudson-valley); paragraph max 0.559 (vs hudson-valley, tax-credit paragraph — both cite the same NYC Business summary).
- check_page.py: all pass except the 11 sibling back-link lines (main run wiring). File 186 KB vs HV 180 KB (>2 KB apart at time of check — re-check after HV finalises).
