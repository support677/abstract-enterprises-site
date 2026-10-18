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


## Long Island — merged 2026-10-18 from the Long Island build (local section, new silo findings, this page's questions for the register)

## Lorex Camera Installation — Long Island hub research (incoming, for merge into research/lorex-camera-installation.md)

Written 2026-10-18 by the REBUILD of `lorex-camera-installation-long-island` (hub; (800) 486-0943 only; GBP Brooklyn 1282 Troy Ave `#brooklyn`; up-link `/`; down-links `/lorex-camera-installation-nassau-county`, `/lorex-camera-installation-suffolk-county`; silo cross-links to NYC hub + 5 boroughs and HV hub + 6 counties). research/lorex-camera-installation.md was NOT edited — main run merges this file.

Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, excerpts), Firecrawl gov search (`mcp__Firecrawl__firecrawl_gov_search`), Firecrawl scrape (`mcp__Fire_Crawl__firecrawl_scrape`, markdown / directQuote). Shell curl blocked. "carried" = fact gathered and sourced by an earlier run in another research file (file + row named); URL not re-fetched today. "excerpt" = search snippet only.

---

### New silo findings (Lorex, usable on every Lorex page)

| ID | Exact query · platform | URL | Finding | LI page section |
|---|---|---|---|---|
| LS1 | `Lorex NVR operating temperature humidity specifications recorder` · Firecrawl search (excerpts) | https://content.syndigo.com/asset/dada3fee-616d-44aa-a4a7-c4a1d3171a77/original.pdf ; https://www.lorex.com/products/n910a62-fusion-4k-12mp-16-channel-nvr | N910 4K+ Fusion NVR series: operating temperature 14°–131°F (−10°–50°C); humidity 10–90% RH. | §5.5 intro bullet; §9 A4 (garage/attic); §9 B4 (winter heat down); §10 NVR card; §10.5 H3 3; HowTo step 2; Sources |
| LS2 | same (excerpt) | https://www.lorextechnology.com/downloads/security-nvr/N881-Series/N881_Series_datasheet_R3.pdf | N881 series data sheet: operating temperature 14°–131°F / −10°–55°C (°C figure as printed), humidity 10–90% RH. | same as LS1 (page says "recent recorders") |
| LS3 | same (excerpt) | https://www.bestbuy.com/site/questions/lorex-8-channel-8-camera-indoor-outdoor-wired-4mp-2tb-nvr-surveillance-system/5783801/question/b46e7740-9640-39e6-a751-1437203608f5 | Best Buy Q&A title: "The specs state a minimum operating temperature of 60 degrees" (older 4MP kit; not verified) | NOT USED (unverified) |
| LS4 | `Lorex outdoor camera salt air coastal corrosion IP67 operating temperature -22°F help` · Firecrawl search (excerpt) | https://www.lorex.com/products/lorex-4k-ultra-hd-25x-pan-tilt-zoom-ip-camera | Lorex 4K 25x PTZ: IP67, operating temperature −40°F ~ 158°F, IK10 vandal rating. No Lorex statement on salt/corrosion found → page says IP67 covers water/dust ingress only (definition, not a Lorex claim). | §10 PTZ card; FAQ 8 (heat); §9 B2 (salt rinse) |
| LS5 | carried silo L8 | https://www.lorex.com/blogs/help/oc101-series-2k-outdoor-wi-fi-battery-camera-frequently-asked-questions | OC101 operating temperature −4°F to 122°F. | FAQ 8 |
| LS6 | `Lorex Costco Long Island OR "Lorex" sold at Costco BJ's Home Depot security camera system 2026` · Firecrawl search → scrape | https://www.lorex.com/pages/costco | "Lorex is a proud partner of Costco Wholesale. For over a decade, Costco has carried a wide variety of Lorex products, including security cameras and systems." Collections listed incl. Wired Analog (DVR) systems, PoE switches, coax-to-Ethernet adapters. | §6 kit card; §10.5 H3 1; Sources |
| LS7 | carried silo X5, X6, X9, X2, L9, L11 (Brooklyn/HV rows) | lorex.com FAQ / FCC notice / doorbell transformer / Fusion pro page / apps / compatibility | NDAA disclaimer, FCC restriction notice (July 2026), 16–24 VAC doorbell + older 10 V transformers, ≥6 Mbps upload for remote access, three apps, products not always interchangeable. | §5 para 5; §6 doorbell card; §9 C1–C2; §10 doorbell card; FAQ 7; Sources |

### Long Island

**Thesis (distinct from HV = recorder reach/outages/rural internet; Brooklyn = recorder in a pre-1940 attached masonry house; Hikvision LI = keep/replace after FCC; Dahua LI = brand/legal):** on Long Island a Lorex system is decided by the shape of the post-war single-family house — slab ranch (attic is the only route), cape (knee-wall crawl spaces), split-level (four half-floors), high ranch (ground-floor utility room that may flood), colonial, raised waterfront — and by keeping the recorder in a heated, dry room above flood level and inside Lorex's 14–131°F recorder range (never attic/attached garage/basement floor). Most jobs start from a warehouse-club kit. Overlaid: PSEG LI outages, salt air on waterfront walls, porch/driveway theft, police camera registries, Nassau vs Suffolk licensing split, East End seasonal houses.

#### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/longisland excerpts only (LR1–LR3); reddit.com scrape refused by Firecrawl ("we do not support this site") |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and tests seven circulating claims instead |
| 6 | Landmarks | LI-LM1–LM8 |
| 7 | Use cases / building stock | LI-H1–H5 |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | PSEG LI release, CBS, ABC7, NY Post, News12 (excerpts), East Hampton Star (carried excerpt) |
| 10 | Hyperlocal | News12 LI (excerpt), 27east (excerpt), East Hampton Star (carried excerpt). Patch / Newsday Lorex-specific: EMPTY (no hit) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not re-searched; silo row 1.1 #11 |

#### Building stock / geography (LI-H)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-H1 | carried — research/dahua-camera-installation.md LI hub (Census API ACS 2023 5-yr, B25035/B25001/B25024) | https://api.census.gov/data/2023/acs/acs5 | Nassau 477,860 units, 364,529 one-unit detached, median year built 1955; Suffolk 579,790 units, 463,095 detached, median 1970. | §5 para 1; §5.5 bullets 1–2; two-county cards + table; Sources |
| LI-H2 | carried — research/fiber-optic-installation.md LI hub | https://www.ny.gov/counties/nassau ; https://www.ny.gov/counties/suffolk | Nassau: 2 cities, 3 towns, 64 villages, 60+ hamlets, ~453 sq mi; Suffolk: 10 towns, ~2,373 sq mi. | §5.5 bullet 3; Sources |
| LI-H3 | carried — research/cat6-repair.md LI hub | https://kerimurrayarchitecture.com/levittown-ny/ | 17,447 Levittown homes built 1947–1951, many ranches on concrete slabs. | §5.5 bullet 2; §7 slab-ranch card; §13 Levittown card; Sources |
| LI-H4 | `Southampton OR "East Hampton" seasonal homes percent vacant seasonal use census housing units` · Firecrawl search → scrape (directQuote) | https://www.southamptontownny.gov/DocumentCenter/View/857/Demographics-and-Housing-PDF | "The Town of Southampton has a larger percentage of seasonal housing at 35.2%, while the County, as a whole is much lower at 7.3%." (document "Southampton Document FINAL September 2004" — 2000-era data) | §5.5 bullet 6; §13 Southampton card ("about 35 per cent", "a planning study"); Sources |
| LI-H5 | same search (excerpt) | https://www.27east.com/east-hampton-press/article_610622df-48d8-5b94-808f-bc8666d4c52f.html | 2010 Census: nearly half of Southampton Town houses marked "vacant"; East Hampton vacant share 58%→60%. | background only |
| LI-H6 | carried — research/dahua-camera-installation.md (excerpt) | https://www.easthamptonstar.com/police-courts/202021/cops-ask-help-east-hampton-burglaries | Police released a still from a Nest camera inside a burglarised house on Sammy's Beach Road, East Hampton (no date in excerpt). | background only |
| LI-H7 | carried — dahua LI (excerpt of Newsday FB post) | https://www.facebook.com/newsday/ (post 1540183818152862) | Newsday analysis of ~12,000 2026 home sales: >5,000 built in the 1950s–60s. | NOT USED (excerpt via Facebook) |
Note: house-type descriptions (cape knee walls, split-level half-floors, high ranch ground floor, blown-in insulation, cedar shakes North Shore→Hamptons, stucco on post-war Nassau houses) are general building knowledge, not statistics — FLAG: no per-type source.

#### Power / storms / flooding (LI-W)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-W1 | `PSEG Long Island outage customers storm 2025 OR 2026` · Firecrawl search → scrape | https://www.psegliny.com/en/Newsroom/2025/092626-StormUpdate1300 | Release dated "(UNIONDALE, N.Y. – Sept. 26, 2026)" (URL folder says 2025): coastal storm, gusts to 55 mph, 13,337 of 1.2 million customers affected at 1 PM; >34,600 restored since 7 AM Friday; hardest hit Huntington Station, Setauket, Bay Shore, Northport, Southampton; 850+ field personnel. | §5 para 4; §10.5 H3 5; Sources |
| LI-W2 | carried — research/hikvision-security-camera-installation.md W1 | https://www.lipower.org/wp-content/uploads/2020/09/LIPA-Isaias-30-Day-Report-Final.pdf | LIPA 30-day report: Isaias Aug 4 2020 ~645,000 customer outages; full restoration took eight days. | §5 para 4; §5.5 bullet 4; §10.5 H3 5; Sources |
| LI-W3 | carried — hikvision LI W2 | https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20240823 | Aug 18–19 2024 first-ever flash flood emergency for Suffolk; Stony Brook Mill Pond dam failed; >2,000 residents and business owners flood damage. | §5.5 bullet 5; §10.5 H3 3; §13 Stony Brook card; Sources |
| LI-W4 | carried — hikvision LI W3 | https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York | Long Beach ~$150 million damage. | §13 Long Beach card; Sources |
| LI-W5 | `Long Island elevated homes flood zone FEMA South Shore raised houses after Sandy Nassau Suffolk number` · Firecrawl search → scrape (directQuote) | https://www.townofbabylonny.gov/faq.aspx?TID=70 | Town of Babylon DPW flooding FAQ: "FEMA has designated most of the area as an AE6 Flood Zone, which means that anything less than six feet above sea level is prone to flooding." | §9 B1 (flood zone recorder); Sources |
| LI-W6 | same search (excerpt) | https://longislandadvocate.com/superstorm-sandy-still-haunts-suffolk-residents-today/ | "more than 10,000 homes were flooded with one to six feet of water" (Suffolk, Sandy; quote attributed to Schneyer). | NOT USED (excerpt, secondary) |
| LI-W7 | same search (excerpt) | https://www.reddit.com/r/longisland/comments/1fdif2i/is_it_worth_purchasing_a_home_in_a_flood_zone_area/ | r/longisland: "Our house is waterfront in the highest risk zone. It flooded in Sandy, but that's it." | Sources (anecdote list) |
Raised-after-Sandy houses (§7 card, §9 B3) — general; no count sourced (FLAG). No source found for elevated-home numbers on LI → EMPTY.

#### Police / crime / local news (LI-N)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-N1 | `Long Island car thefts unlocked cars driveways 2026 police Nassau Suffolk Newsday` · Firecrawl search → scrape (directQuote) | https://www.cbsnews.com/newyork/news/nassau-suffolk-counties-form-task-force-to-target-high-end-thefts/ | CBS NY (image dated Jan 18, 2024): new LI task force vs high-end home break-ins and car thefts; three men arrested, part of a crew of 15–20 who "spot high end cars in driveways then break into homes in search of key fobs"; break-ins and car thefts "spiked on Long Island since 2021". | §5 para 3; §9 D2 (driveway); Sources |
| LI-N2 | carried — dahua LI / hikvision LN4 | https://abc7ny.com/post/nassau-county-police-task-force-burglaries-long-island/14337932/ | Jan 18 2024 multi-agency task force; burglars "attracted by cars in people's driveways". | §5 para 3; Sources |
| LI-N3 | carried — hikvision LN5 | https://www.cbsnews.com/newyork/news/suffolk-county-porch-pirate-ring/ | Nov 25 2025: Suffolk DA charged 14 men; >200 phones/tablets from porches in 31 communities incl. Brentwood, Central Islip, Shirley, Deer Park. | §5 para 3; §9 D1 (packages); Sources |
| LI-N4 | carried — hikvision LN1 | https://www.pdcn.org/CivicAlerts.aspx?AID=15190 | NCPD 2026 news flash: residences across Nassau entered Jul 11 2025–May 23 2026, jewellery taken; arrest in New Hyde Park. | §5 para 3; Sources |
| LI-N5 | carried — hikvision LN6 | https://scpdshield.org/Initiatives | SCPD Camera Registry Program; retrieval at owner's convenience. | §9 D3 (registry); §10.5 H3 7; Sources |
| LI-N6 | carried — hikvision LN7 | https://gardencitypolice.net/private-camera-reg | Garden City PD private camera registration "does NOT provide us access". | §9 D3; §10.5 H3 7; Sources |
| LI-N7 | `"Long Island" Lorex camera footage police OR burglary OR "porch" Patch OR News12 2025 2026` · Firecrawl search (excerpt) | https://nypost.com/2026/08/02/us-news/flock-safety-cameras-vandalized-on-long-island-after-accusations-cop-tracked-lover/ | NY Post headline, Aug 2 2026: "Flock Safety cameras vandalized on Long Island after accusations cop tracked lover" (headline/date only). | §10.5 H3 7 (headline only); Sources |
| LI-N8 | same (excerpt) | https://longisland.news12.com/suffolk-communities-on-high-alert-following-multiple-car-break-ins | News12: reports of broken windows on Fairfield Circle, Brentwood (undated excerpt). | NOT USED (undated) |
| LI-N9 | same (excerpts) | Instagram reels (Syosset Flock camera theft; Suffolk bill) | excerpts only | NOT USED |
| LI-N10 | same search, Lorex-specific LI news | — | No LI news item naming Lorex found → EMPTY | — |

#### Licensing / permits (LI-K)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-K1 | `Nassau County home improvement contractor license definition "home improvement" includes installation burglar alarm security system` · Firecrawl gov search | https://archive.nassaucountyny.gov/agencies/OCA/Business/LocalLaw6-1970.html | Local Law 6-1970: "Home Improvement" shall not include … (e) automatic fire alarm systems, or (f) burglar alarm systems. Cameras not named. | §8.5 Nassau bullet; Sources |
| LI-K2 | same | https://nassaucountyny.gov/DocumentCenter/View/1638 | Consumer checklist: HI law does NOT apply to fire or burglar alarm systems; "Electricians and Plumbers. (They must be licensed by the towns and villages in Nassau County.)" | §8.5; FAQ 4 (outlet); two-county card/table; Sources |
| LI-K3 | same | https://nassaucountyny.gov/FAQ.aspx?QID=205 | Commercial-only contractors do not need the HI licence; licensed electricians etc. exempt in their field; $650 / 2-yr licence. | §8.5 (commercial-only clause) |
| LI-K4 | `Suffolk County Code Chapter 563 "communication cable installer" restricted license 90 volts audio video` · Firecrawl gov search | https://suffolkcountyny.gov/Portals/0/formsdocs/labor/code.pdf | Code of Rules, Communications Cabling Systems (restricted licence): "Furnish and/or install, repair, maintain, alter or erect all cabling systems of 90 volts or less, for computer networking, telecommunications, cable TV, fiber optics, audio and video systems and home theater systems." Rev. 10/2013. | §8.5 Suffolk bullet; two-county card/table; Sources |
| LI-K5 | carried — hikvision K3 / cat6-repair LI | https://ecode360.com/14948079 | Ch. 563 Art. XI: towns/villages with own licensing carved out. | §8.5; Sources |
| LI-K6 | carried — hikvision K1 | https://dos.ny.gov/system/files/documents/2024/05/security_0.pdf | 19 NYCRR §195.2(b)(1): licence for work on CCTV/video surveillance used to detect/monitor intrusion, theft. | §8.5 first bullet; Sources |
| LI-K7 | carried — hikvision K4 | https://newyork-811.com/homeowners/ | Call 811 at least 48 hours before digging. | §8.5; FAQ 6; Sources |
| LI-K8 | carried — silo HV-G6 / HV-G8 | nysenate CVR 52-A ; nyc-business tax credit | Civil Rights Law §52-a; Commercial Security Tax Credit ≤50 employees, up to $3,000/location. | §8.5; FAQ 3; Sources |
Whether a Nassau HI licence is needed for camera-only residential work: EMPTY (law silent on cameras) → page tells owners to ask which licence covers the job. AESS's own Nassau/Suffolk licences: NOT CLAIMED on page (FLAG — confirm what AESS holds).

#### Corridors / landmarks (LI-LM) — carried, sources fetched by earlier LI runs
| ID | URL | Finding | Used |
|---|---|---|---|
| LI-LM1 | https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) | Largest mall on LI, East Garden City/Uniondale | §8 card; §13 card; Sources |
| LI-LM2 | https://cmmllp.com/hauppauge-industrial-park-update-2017-long-islands-oasis-productivity-innovation/ | ~1,350 businesses, ~11 sq mi (Long Island Innovation Park at Hauppauge) | §8 card; §13 card; Sources |
| LI-LM3 | https://iraceenterprises.com/route-110-corridor/ | Route 110: Farmingdale, Melville, Huntington Station; office/flex/warehouse | §8 card; Sources |
| LI-LM4 | https://govmarketnews.com/suffolk-county-master-developer-rfp-ronkonkoma-hub/ | Ronkonkoma Hub by the LIRR station and MacArthur Airport | §8 card; Sources |
| LI-LM5 | (LI-H3) Levittown | | §13 |
| LI-LM6 | (LI-W3) Stony Brook Mill Pond | | §13 |
| LI-LM7 | (LI-W4) Long Beach | | §13 |
| LI-LM8 | (LI-H4) Southampton | | §13 |
Route 58 Riverhead, Old Country Road, Jericho Turnpike, village downtowns (Rockville Centre, Mineola, Huntington, Patchogue, Sayville) and the town list in §13 are real place names used without attached facts (FLAG: no per-corridor source this run).

#### Reddit (LI-R)
| ID | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| LR1 | `site:reddit.com r/longisland security cameras Lorex OR "camera system" house` · Firecrawl search | https://www.reddit.com/r/longisland/comments/1kc5ygw/home_security_cameras/ | "ring is a great camera system as long as you pay the yearly subscription I think it's $90." | §10 comparison (labelled as one commenter); Sources |
| LR2 | same | https://www.reddit.com/r/longisland/comments/1cn1pcu/security_system_suggestions/ | "My previous setup was ADT and Dropcam … considering Reolink as a cheaper option" | background |
| LR3 | same | https://www.reddit.com/r/longisland/comments/nbmls1/security_camera_installer/ ; …/1edj45z/security_camera_installation/ | Thread titles only (installer requests). | background |
Scrape of LR1 refused by Firecrawl → full threads EMPTY (not accessible in build env).

#### Published cost claim used in §10.5
Carried silo A1 (Angi 2026: $100–$200 per camera labour on top of equipment). Used in §10.5 H3 6.

#### Pricing used (§9 — no invented prices)
Basis identical to the HV hub: Brooklyn labour base from the silo calculator (silo §1.7) = $200 per wired camera ($175 line + $25 box), $150 recorder setup; equipment not multiplied (4-cam kit equipment $845, camera $78, recorder $320). §9 factors on labour only, round half-up.
| County | × | Labour / wired camera | Recorder setup | 4-camera system | Camera added, from | Recorder with setup, from | BYOE |
|---|---|---|---|---|---|---|---|
| Nassau | 1.15 | $230 | $173 | $1,938 | $308 | $493 | $230/camera + $173 setup |
| Suffolk | 1.20 | $240 | $180 | $1,985 | $318 | $500 | $240/camera + $180 setup |
Service after install: $195/hr, 3-hr minimum ($585), not multiplied. Recorder relocation, doorbell transformer, trenching, electrician work, waterfront hardware: "quoted after a walk-through" (no price).
**FLAG:** price calculator pages don't follow §9: lorex-camera-installation-prices-long-island and -prices-nassau-county both show 4 cameras from $1,985 / cameras from $318 (= Suffolk 1.20 figures); -prices-suffolk-county shows $2,069 / $336. Hub text says the calculator "sorts the Island into its own price zones" and the written quote follows the county line in the hub table. Anwar to decide.

#### House practices stated on the page without an external source (FLAG for Anwar)
- Recorder never in attic / attached garage / basement floor; above highest past water; PoE switch allowed in a heated garage on a shelf.
- Cable over joists above blown-in insulation, insulation re-levelled; mounting blocks on shakes/vinyl/stucco; stainless fixings on waterfront walls; spring/autumn fresh-water rinse.
- Doorbell + separate wired porch camera; low first-floor driveway camera + wide eave camera; colour (light) preferred to IR on dark streets.
- Strip-centre exterior cameras need landlord's written permission (general lease practice, not sourced).
- Loading-door aim across the dock; tune after dark with a vehicle.
- Unplug-and-restart test, after-dark check, USB clip export shown to every owner.
- Two-hour arrival windows, 7 days to 8 PM; "recording again within one to two hours of arrival" (silo convention, blueprint §5 el. 36); one day for 4–6 cameras on an accessible house; video-call walk-throughs.
- AESS places 811 requests itself when trenching; arranges or coordinates electricians.
- Field Notes = installer-voice method note (attic hatch / basement / panel first, recorder room, unplug test, after-dark check), no specific job story.

#### Images (11) — Drive: no Lorex folder (per main run); CompanyCam not connected
Permanent image rule. All looked at with Read before naming; no faces, house numbers, plates or readable documents. Avoided every source file the Brooklyn and HV Lorex pages used. Output folder `images/lorex-camera-installation/`, all WebP q80, ≤1600 px, names contain `-long-island-`.
| Output (lorex-camera-installation-long-island-…webp) | Source | Crop | Placement |
|---|---|---|---|
| black-lorex-video-doorbell-with-blue-ring-product-photo (423×562) | images/lorex-video-doorbell.webp | none — Lorex product shot | Hero (eager) |
| two-cameras-on-yellow-fascia-corner-against-sky (917×235) | images/floodlight-camera-installation/floodlight-camera-installation-brooklyn-dome-camera-under-fascia-beside-led-strip-lights.webp | (0,0,917,235) — mural and LED strip excluded | §5 |
| white-lorex-bullet-camera-with-twin-lights-product-photo (275×183) | images/lorex-4k-bullet-camera-installation-long-island.jpg | none — Lorex product shot | §6 |
| white-dome-camera-in-ceiling-corner-above-wall-sensor (400×620) | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-turret-camera-in-ceiling-corner-beside-flag.webp | (0,0,400,620) — flag excluded | §7 |
| small-cameras-on-high-wall-under-clerestory-windows (907×440) | images/dahua-camera-installation/dahua-camera-installation-long-island-small-cameras-on-high-wall-of-open-hall.webp | none | §8 |
| loose-blue-and-white-network-cables-crossing-ceiling-beam (600×255) | images/dahua-camera-installation/dahua-camera-installation-orange-county-recorder-monitor-camera-grid-and-cable-bundles.webp | (0,0,600,255) — monitor and camera tiles excluded | §9 cluster A |
| black-bullet-camera-on-pole-mount-in-drop-ceiling (685×390) | images/dahua-camera-installation/dahua-camera-installation-long-island-bullet-camera-on-drop-ceiling-tile-mount.webp | (250,170,935,560) | §9 end (business cluster) |
| black-lorex-floodlight-camera-with-two-white-panels-product-photo (263×192) | images/lorex-dual-floodlight-camera-installation-long-island.jpg | none — Lorex product shot | §10 |
| mini-dome-cameras-among-ceiling-lights-and-speaker (930×430) | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-mini-dome-cameras-in-drop-ceiling.webp | (300,0,1230,430) | §13 |
| white-lorex-video-doorbell-product-photo (151×334) | images/lorex-video-doorbell-camera-installation-long-island.jpg | none — Lorex product shot | §14 |
| small-black-camera-high-on-grey-wall-above-ceiling-lights (900×755) | images/dahua-camera-installation/dahua-camera-installation-orange-county-black-bullet-camera-high-on-painted-wall.webp | (250,180,1150,935) | Field Notes |
**Library FLAG (new):** images/lorex-dual-lens-dome-camera-installation-*.jpg shows a **Uniview (unv)**-branded dual-lens dome, not Lorex — add to the known-bad list. images/lorex-4k-turret-camera-installation-* and lorex-4k-turret-dome-camera-installation-* and lorex-turret-network-camera-installation-nyc.jpg are byte-identical; lorex-wifi-ptz-hero-camera-installation-long-island.jpg = lorex-wifi-ptz-camera-installation-hudson-valley.jpg; lorex-dual-floodlight-camera-installation-long-island.jpg = lorex-floodlight-camera-installation-hudson-valley.jpg. The bullet-on-drop-ceiling source carries a small non-Lorex logo (unreadable at page size); caption names no brand.

---

### Question register — lorex-camera-installation-long-island (REBUILD 2026-10-18)
All old-template LI questions removed. Compared by meaning against every question in the silo register (old template, prices pages, HV and Brooklyn rebuilds) and against hikvision/dahua LI FAQ intents (cross-silo). Deliberately NOT asked as questions here (owned elsewhere): cable distance limits, outbuildings, outage recording/restart, licensing-by-county, which app, AG lawsuits, ownership, neighbour's yard, caretaker access, board/HOA permission, doorbell on old wiring, pigeons/animal alerts, payment, old DVR removal, police export, internet speed, adding cameras later.

§9 Questions Answered (H3) — 16 (repair capture H2 is a statement: "Lorex Cameras Offline on Long Island — Same-Day Help"):
1. Our ranch sits on a concrete slab with no basement. How does Lorex cable get from the recorder to the eaves?
2. Our cape has a finished upstairs with knee walls. Can cable run behind them to reach the cameras at each end of the house?
3. In a split-level, which of the half-floors makes the best home for the Lorex recorder?
4. Can the recorder sit in the attached garage or up in the attic, where the cables are easiest to reach?
5. How are cameras fixed to cedar shakes, vinyl or stucco without causing a leak?
6. Our South Shore house is in a FEMA flood zone. Where should the recorder and the network gear go?
7. How often should cameras on a bay-front or ocean-facing wall be rinsed and checked?
8. Our house was raised after Sandy. Does the new crawl space or pier foundation change how the cameras are wired?
9. Can the Lorex recorder stay on all winter in a house where the heat is turned down to the minimum?
10. We bought a Lorex kit at a warehouse club. What usually has to change before it fits a Long Island house?
11. Can two Lorex kits bought a year apart run on one recorder?
12. Packages keep disappearing from our front step. Is a Lorex doorbell enough, or does the porch need its own camera?
13. Thieves on Long Island go after cars parked in driveways. Where does the camera need to be to see someone trying the door handles at night?
14. Our police department runs a camera registry. Should we sign up, and what does it give them?
15. Can a Lorex camera at our strip-centre shop look out over the shared parking lot?
16. Will a camera watching our loading door be blinded by truck headlights backing in?

§17 FAQ (visible == FAQPage schema) — 10:
1. Will the crew need to get into our attic or crawl space, and what should we clear beforehand?
2. Is winter a bad time to have outdoor cameras installed on Long Island?
3. Can the cameras on the front of the house record the street and the sidewalk?
4. The closet we picked for the recorder has no outlet. Who adds one?
5. Can the new camera cables come into the house through the hole the old cable-TV line used?
6. Can a cable cross our driveway to a camera on the far side, and who checks for buried lines first?
7. Will wired Lorex cameras slow down our home Wi-Fi or streaming?
8. Do Lorex cameras keep working on a south-facing wall in a Long Island heat wave?
9. Can the crew come on a weekend so we can be home for the walk-through?
10. Can a camera on the house keep watch over our boat at the end of the dock?

### Build notes
- Rendered words 12,763; title 59 ("Lorex Camera Installation Long Island NY | Nassau & Suffolk"); meta 157; one H1; 6 JSON-LD blocks; FAQ 10 = schema 10; HowTo 6 = process cards 6; 2 Web3Forms forms (hf/qf), landing_page `lorex-camera-installation-long-island`; tel only (800) 486-0943; WhatsApp only wa.me/17186790359 (+ footer text).
- check_page.py: PASS (incl. registration and sibling back-links — siblings already link to /lorex-camera-installation-long-island). File 177,115 B (HV 180,259; Brooklyn 186,125) — re-check vs the parallel Manhattan/Orange County rebuilds.
- simcheck: page-level max 0.147 (vs HV); paragraph max 0.649 = changelog byline vs HV (freshness constant); hero freshness stamp 0.631 vs Brooklyn; every body paragraph ≤ 0.592. Cross-silo (hikvision/dahua/apartment LI): body max 0.622 (hikvision DOS-licence bullet rewritten from 0.692); freshness stamp 0.693 vs hikvision LI.


## Manhattan — merged 2026-10-18 from the Manhattan build (local section, new silo findings, this page's questions for the register)

## Lorex Camera Installation — Manhattan research (incoming, for merge into research/lorex-camera-installation.md)

Written 2026-10-18 by the REBUILD of `lorex-camera-installation-manhattan` (subagent; research/lorex-camera-installation.md not edited). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page section used. Tools: WebSearch, WebFetch, Firecrawl search/scrape. Shell curl blocked. "carried" = fact gathered and sourced by an earlier run in another research file (named); URL not re-fetched today. "excerpt" = only the search snippet was read.

### Manhattan

Page: `lorex-camera-installation-manhattan` (REBUILD in place). Up-link `/lorex-camera-installation-nyc`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (929) 560-0737 in body, CTAs, sticky bar, form copy and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (+ footer/contact text).

**Thesis (distinct from Brooklyn = recorder placement and cable routes through an attached masonry house; Hudson Valley = distance, outbuildings, outages, rural internet; LI = house construction types/flood/coast; OC = short-term rentals/commuter houses/new builds):** in Manhattan a Lorex system lives inside someone else's building, so the job is governed by permission and boundaries — what the managing agent/board/landlord must approve (COI, hours, elevator, alteration agreement), where the owner's space ends (inside-the-door camera vs shared hallway; inside-the-glass vs façade; LPC on landmarks), what features may legally be switched on (NYC biometric law LL3/2021 for stores/restaurants, eavesdropping/audio, Labor Law §203-c staff areas), and how the recorder joins building-controlled internet in Wi-Fi-congested towers. Lorex is fitted to the part of Manhattan that is genuinely the customer's — apartments, townhouses, lofts, small businesses — not building-wide co-op systems.

#### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Firecrawl search excerpts only (M-R1–M-R5); threads not scraped |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and tests seven circulating claims instead |
| 6 | Landmarks | M-N1–M-N5, M-L1–M-L3 |
| 7 | Use cases / building stock | M-H1 (Census, carried) |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Hoodline (Jun 2026), PIX11 (2017), ABC7 (2024, carried), NYPD 19th Pct (carried) |
| 10 | Hyperlocal | West Side Rag / amNY / DNAinfo package-theft hits were old (2016–2019) — not used; NYPD 19th Pct Facebook (carried) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — not searched again (silo row 1.1 #11) |

#### Building stock (M-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-H1 | carried from research/hik-connect-app-support-repair.md `## Manhattan` M-H1 (Firecrawl Alexandria census-gov, ACS 2023 5-yr, county 061). Direct re-fetch today: WebFetch → permission timeout; Firecrawl scrape → "Missing Key" page | https://api.census.gov/data/2023/acs/acs5?get=group(B25035)&ucgid=0500000US36061 | New York County 918,806 units; 50+ unit 522,823; 20–49 201,967; 1-unit detached 10,012; 1-unit attached 6,713; renter-occ 583,733 vs owner 191,643; median year built 1951; ≤1939 392,000. | §5 para 1; §5.5 bullets 1–3; Sources |

#### Boards, managing agents, hallways (M-B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-B1 | `co-op board alteration agreement security camera apartment door hallway Manhattan approval` · WebSearch → WebFetch | https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops | FirstService Residential, Sept 23, 2024 (Christina Forbes, Manhattan Condo/Co-op Division): access via property manager; resident copies need board/counsel approval; retention "generally" 30–90 days; hallway cameras should not capture inside any unit; Labor Law §203-c; audio "could be considered unlawful eavesdropping"; doorbell rules: board approval, no direct facing of another unit, audio disabled. | §5 para 3 fact; §5.5 bullet 6; §9 hallway H3; §10.5 H3 5, 7; FAQ package; Sources |
| M-B2 | `reddit AskNYC doorbell camera apartment door hallway co-op not allowed` · WebSearch → WebFetch | https://www.brickunderground.com/live/ask-condo-co-op-lawyer-board-apartment-complaints-video-doorbell-privacy-legal-ban-harassment-pullman-nyc | Brick Underground, June 23, 2022 (Niki Khindri, Adam Leitman Bailey): board can ban video doorbells/cameras in common areas by resolution/house rule without shareholder vote; camera angled into neighbour's open door, esp. with audio, may invade privacy; apply rules equally; footage useful in Pullman proceedings. | §9 hallway H3; §9 neighbour-doorbell H3; §10.5 H3 2; Sources |
| M-B3 | `Habitat magazine camera in hallway co-op shareholder installed camera outside door board` · WebSearch → WebFetch | https://www.habitatmag.com/Board-Talk/shareholder-installs-surveillance-camera-over-his-door/Shareholder-installs-surveillance-camera-over-his-door | Habitat Board Talk, Dec 9, 2009 (unnamed poster): "That camera needs to come down immediately." | Sources only (background) |
| M-B4 | same search → WebFetch | https://www.blockrenovation.com/guides/what-is-an-alteration-agreement-for-buildings-in-new-york-city-and-how-to-read-one?hsLang=en | Alteration agreements: contractors need liability insurance and workers' comp; hours "think 9 a.m. to 5 p.m. on weekdays"; weekend work typically banned; approvals "anywhere from a few weeks to a couple of months"; deposits; does not address low-voltage specifically. | §5 para 2; §9 hours H3; Sources |
| M-B5 | `HPD peephole chain door guard landlord required multiple dwelling NYC Housing Maintenance Code 27-2043` · WebSearch → WebFetch | https://nycadmincode.readthedocs.io/t27/c02/sch02/art11/index.html | HMC §27-2041: owner shall provide and maintain a peephole in the entrance door of each dwelling unit (exceptions listed); §27-2043(a) key lock, class A heavy-duty latch set + dead bolt; (b) chain door guard in class A. | §5.5 bullet 4; §9 inside-camera H3; Sources |

#### Rules / law (M-G)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-G1 | `NYC biometric identifier information law commercial establishments signage facial recognition cameras Admin Code 22-1202` · WebSearch → WebFetch | https://intro.nyc/local-laws/2021-3 | LL 3 of 2021 (Admin Code ch. 12): commercial establishments = places of entertainment, retail stores, food and drink establishments; sign "near all of the commercial establishment's customer entrances" if collecting/retaining/converting/storing/sharing biometric identifier info; unlawful to sell/lease/trade/profit; private action: $500 per sign violation after 30-day cure notice; $500 negligent / $5,000 intentional sale violations; excludes video not analysed by biometric software and not shared/sold (other than to law enforcement). | §5.5 bullet 5; §8.5 bullet 1; §9 biometric H3; §10.5 H3 4; Sources |
| M-G2 | `DCWP biometric identifier information sign rule …` · WebSearch → WebFetch | https://rules.cityofnewyork.us/rule/biometric-identifier-information/ | DCWP rule effective January 15, 2022; sign wording/size not in fetched text. | §5.5 bullet 5 (date only); Sources |
| M-G3 | carried silo G1 (Brooklyn) | https://intro.nyc/local-laws/2024-128 | LL 128/2024 low-voltage <50 V; no electrical permit for qualified person. | §8.5 bullet 5 |
| M-G4 | carried silo G3 (Brooklyn) | https://www.nysenate.gov/legislation/laws/PEN/250.05 | Eavesdropping class E felony; one-party consent. | §8.5 bullet 3; §9 neighbour-doorbell H3; §10.5 H3 5; FAQ nanny |
| M-G5 | carried silo G5 / M-B1 | https://nysenate.gov/legislation/laws/pen/250.40 ; FSR (Labor Law §203-c) | Places where a person may reasonably expect to disrobe; employers may not video record employees in restrooms, locker rooms, changing rooms. | §8.5 bullet 2; §9 staff H3; FAQ nanny, office suite |
| M-G6 | carried silo G6 | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | Up to $3,000 per retail location, ≤50 employees. | §8.5 bullet 6 |
| M-G7 | carried hik-connect M-B7 / silo L8 | https://nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook%20_Chapter11_HealthSafety.pdf | LPC staff-level approval for discreet, well-spaced cameras at mortar joints/plain masonry, minimal painted conduit. | §7.5 townhouses; §8.5 bullet 4; §9 historic-district H3 |

#### Lorex (M-X) — new this run
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-X1 | `Lorex facial recognition face detection known faces feature recorder` · WebSearch → WebFetch | https://www.lorex.com/blogs/help/n910-series-4k-ultra-hd-12mp-16-camera-capable-nvr-face-detection | Meta description only: N910 face detection can "detect and capture faces … while triggering alarms and/or notifications"; Lorex caution: "Facial recording without consent is illegal in certain jurisdictions." Lorex also lists DVRs "with … face recognition" (search titles, lorex.com). | §9 biometric H3; §10.5 H3 4 |
| M-X2 | `Lorex doorbell apartment door wireless battery doorbell peephole alternative …` · WebSearch → WebFetch | https://www.lorex.com/en-au/blogs/products/b463aj-series | B463AJ "Lorex 2K Battery Video Doorbell"; page carries FCC notice: "Under FCC rules effective July 16, 2026, this product cannot be sold or marketed for use in connection with public safety, security of government facilities, or other national security purposes." | background (§10 doorbell card: battery models) |
| (silo) | X1, X2, X3, X5, X6, X8, X9, L11, O1, O2 from the silo file | see silo | 328 ft; Fusion 8+8, 6 Mbps upload; three apps (Pro up to 16 multi-view); FAQ NDAA line, 30-day returns, audio caution, no monthly fees; FCC DA 26-635 notice; W881AA near router; 16–24 VAC doorbells; not interchangeable; NE/TX AG suits. | §9, §10, §10.5, FAQ |

#### Local news / programs / landmarks (M-N, M-L)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| M-N1 | `Manhattan store burglary October 2026 NYPD seeks suspect surveillance` · WebSearch → WebFetch | https://hoodline.com/2026/06/midtown-door-kicker-wanted-after-3-a-m-storefront-scare-nypd-says/ | Hoodline (Bryce Winslow), June 24, 2026: Sun May 10, 2026 ~3 a.m., 349 West 48th Street storefront, Midtown North; man kicked door, didn't get in, ran west; Crime Stoppers posted stills June 23; reward up to $3,500; police asked for door-camera and phone footage. | §5 para 3; §8 West 40s card; §13 card; Sources |
| M-N2 | `Manhattan burglary 2026 NYPD surveillance video building lobby packages` · WebSearch → WebFetch | https://pix11.com/news/local-news/manhattan/mailroom-burglar-ignores-warning-sign-strikes-same-building-3-times-in-a-week/amp/ | April 15/18/21, 2017 (video released May 17, 2017): basement mailroom, building at Central Park West & Manhattan Avenue; door bore "Warning: Security cameras in use"; card and shoulder; manager David Schorr: latch protectors + new inside steel door. | §5 para 3; §13 card; Sources |
| M-N3 | carried hik-connect M-N2 (excerpt) | https://www.facebook.com/NYPD19pct/posts/having-a-package-delivered-to-your-home-not-going-to-be-home-there-are-thieves-o/1186393103591192/ | 19th Pct: 3 separate arrests for stealing packages from vestibules/lobbies (undated). | §5 para 3; §8 UES card; §13 card |
| M-N4 | carried hik-connect M-N3 | https://abc7ny.com/post/nyc-retail-theft-program-mayor-eric-adams-nypd-launch-innovative-technology-initiative-to-combat/14827113/ | May 16, 2024: 125th St voluntary real-time CCTV sharing via Fusus by Axon; "still at the behest or the control of the business owner". | §8 125th card; §9 NYPD-sharing H3; §13 card |
| M-N5 | `Manhattan townhouse burglary 2026 Upper East Side OR West Village NYPD` · Firecrawl search (excerpts, past year) | various (1010 WINS Gramercy, Patch UES subway booth, Instagram) | Items were a sexually motivated burglary, a subway-booth theft and street robberies — not relevant to residential/storefront camera use → NOT USED. | — |
| M-N6 | `hoodline Manhattan 2026 package thief lobby NYPD Crime Stoppers` · WebSearch → WebFetch hoodline Manhattan listing p.12 | https://hoodline.com/news/manhattan/crime-emergencies/latest/page/12/ | Listing contained no Manhattan lobby/package items → EMPTY. | — |
| M-L1 | carried hik-connect M-B5 | https://villagepreservation.org/2024/08/14/the-soho-cast-iron-historic-district-a-1973-designation-that-helped-shape-nycs-cultural-legacy/ | SoHo–Cast Iron HD 1973, ~26 blocks, nearly 500 buildings. | §8 SoHo card; §13 card |
| M-L2 | carried hik-connect M-B6 | https://www.archpaper.com/2025/12/soma-25-water-street-cetraruddy-office-to-residential-conversion/ | 25 Water Street, 1,320 units, largest O2R conversion in the US. | §13 card |
| M-L3 | — | — | Corridors named as places only, no attached facts: Lexington/Third/Second/First Aves; Eighth–Tenth Aves; Chinatown/LES; Water Street; neighbourhood lists in §7 cards (descriptive, FLAG: no per-neighbourhood source). | §7, §8 |

#### Reddit / forums (M-R) — excerpts only
| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| M-R1 | `site:reddit.com AskNYC OR NYCapartments camera inside apartment door peephole landlord allowed Manhattan` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/1gjf846/can_you_recommend_a_camera_to_go_on_your/ | "You may not be allowed to install a camera in the hallway. A peephole doesn't record or provide proof in court." | §5 para 2 (quoted first sentence); Sources |
| M-R2 | same | https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ | "For NYC common area video, only thing not allowed is if camera can film into someone's apartment." | §9 hallway H3; Sources |
| M-R3 | same | https://www.reddit.com/r/AskNYC/comments/1uoh3vy/peephole_camera/ | "Having a camera that can look into your apt when your door is open is not legal in nyc. It is also against almost all co-op/condo/rental rules" (commenter claim; not quoted on page as fact). | background |
| M-R4 | same | https://www.reddit.com/r/AskNYC/comments/ddw3wp/nyc_apartment_security_and_safety_concerns/ | "Your landlord must provide a peephole … must also install a chain door guard" → verified against HMC (M-B5). | background |
| M-R5 | `site:reddit.com wifi camera high rise apartment too many networks 2.4ghz interference NYC building` · Firecrawl search | https://www.reddit.com/r/techsupport/comments/1t41ir/nyc_apartment_unreliable_wifi_could_it_be_too/ | Title: "NYC apartment unreliable wifi — could it be too many wifi signals in my building/area?" | §9 Wi-Fi H3; §10.5 H3 3; Sources |

#### New silo findings (for Part 1)
- M-G1/M-G2 (NYC biometric law) applies to every NYC borough page with stores/restaurants (Brooklyn, Queens, Bronx, SI) — not used on Brooklyn yet.
- M-X1: Lorex caution on face detection without consent.
- M-B1/M-B2: co-op/condo hallway and video-doorbell rules (useful for all NYC Lorex pages).
- M-B5: HMC peephole/chain-guard (all NYC multiple dwellings).

#### Pricing used (§9 — no invented prices)
Basis: Brooklyn base from silo §1.7/§2.5 (lorex-camera-installation-prices-brooklyn calculator: line $175, jbox $25, setup $150; equipment unmultiplied) × Manhattan 1.25 on labour, round half-up: line $218.75→$219, jbox $31.25→$31 → $250 per wired camera; setup $187.50→$188. 4-camera $950→$1,188 labour + $845 equipment = **$2,033**; camera added from $78+$250 = **$328**; recorder with setup from $320+$188 = **$508**; 2-camera CN201U3 kit $529.99 + 2×$250 + $188 = **$1,218**; 6-camera Fusion H12 ($924 equip) → **$2,612**; 8-camera Fusion A4 (~$1,200 equip) → **$3,388**; concealed $200→**$250**/camera; BYOE line $175→**$219**; service $195/hr, 3-h min ($585) not multiplied.
**FLAG:** lorex-camera-installation-prices-manhattan.html calculator zone uses line $238, jbox $34, setup $204, min visit $795 plus **$150 Manhattan parking** → 4-camera $2,287, camera from $350, recorder from $524 (≈1.36× + parking, not §9 1.25). Page links to the prices page but quotes §9 figures; Anwar to decide whether to re-cut the calculator zone or the page.

#### Question register additions — lorex-camera-installation-manhattan (REBUILT 2026-10-18)
Q&A H3 (§9):
1. What will a Manhattan managing agent want from us before a Lorex installer is allowed upstairs?
2. Do a handful of Lorex cameras that never leave our apartment still need the board's sign-off?
3. How do a building's permitted hours and the elevator booking change the day of the install?
4. Can a Lorex camera watch the hallway outside our apartment door?
5. Is there a way to see who comes to our door using a camera that stays inside the apartment?
6. A neighbour's video doorbell points straight at our door — what can we reasonably ask for?
7. Our building supplies internet to every apartment — will a Lorex recorder work on it?
8. With dozens of neighbours' Wi-Fi networks around us, will a Lorex Wi-Fi camera keep dropping off?
9. Will a co-op accept camera cable run on the surface of a pre-war wall, or does it have to go inside?
10. Does New York City's biometric law apply if our restaurant switches on Lorex face detection?
11. Our store lease says the landlord must approve anything on the storefront — what about a camera over our own door?
12. Where should cameras stop in a Manhattan restaurant so staff are not recorded where the law forbids?
13. Can our shop share live Lorex video with the NYPD the way some 125th Street businesses do?
14. Can a Lorex camera go on the front of a townhouse in a historic district without a Landmarks permit?
15. In a loft with fourteen-foot ceilings, how high should the Lorex cameras go?
16. Our company does federal contract work from a Manhattan office — can we use Lorex there?
17. We run two Manhattan shops — can both Lorex systems be watched in one app?
Repair H2s: "Manhattan Lorex Recorder Offline or App Gone Blank?"; "Need a Lorex Repair in Manhattan Today?"
Visible FAQ (§17) = FAQPage:
1. How much notice should we give before a Manhattan Lorex installation?
2. Do you carry the equipment up through the lobby or the service entrance?
3. Will a Lorex camera mounted behind window glass give a usable picture at night?
4. What happens if the managing agent turns down the camera plan after we have bought the equipment?
5. Can Lorex cameras go up in a rental without drilling at all?
6. If a package disappears from our building's lobby, can our own Lorex camera help?
7. We see clients in a small Manhattan office suite — where can Lorex cameras sensibly go?
8. Do Lorex cameras cope with steam and grease in a restaurant kitchen?
9. Can a camera in our apartment keep an eye on the nanny or dog walker while we are out?
10. Our townhouse has a garden-floor rental unit — can one Lorex system cover both?
Checked by meaning against the full register, the Brooklyn and HV rebuilds, and the in-progress LI/OC drafts (read ~09:30Z); four draft FAQs were replaced for overlap (payment, internet-down, recorder noise, phone viewing; then customer-footage request and record-schedule vs OC). Closest remaining: Q16 (private federal contractor) vs HV Q11 (public buyers) — different buyer, same NDAA source.

#### House practices stated without an external source (FLAG for Anwar)
- COI prepared free with the agent's exact wording (Brooklyn page also says free); two-hour windows within building hours; 1–2 h restore (silo convention).
- Recorder beside the apartment router; painted surface raceway; plaster anchors; cameras at 8–9 ft in lofts; inside-the-glass placement with IR off.
- Audio and face features off by default in businesses; managers get live view only; owner + one manager playback.
- "Pre-1960 buildings … lead-safe work rules may come into play" (general, no source fetched — NYC LL1/2004 / EPA RRP not researched this run).
- Who-signs-off table (§7) is practical guidance, labelled "not legal advice".
- Field Notes = method note, no job story.
- ADT/Ring/SimpliSafe comparison qualitative (no source fetched).
- Neighbourhood lists on §7/§8 cards descriptive, unsourced.

#### Images (11) — Drive has no Lorex folder; CompanyCam not connected
7 real AESS job photos from other jobs + 4 Lorex manufacturer product shots; every file viewed with Read; only names containing `-manhattan-`; captions say "Example photo from another AESS job (not a Manhattan …)" or "Manufacturer product photo / Lorex catalog image". Avoided all source scenes used by Brooklyn/HV (dome-over-glass, corridor bullet, stone-façade arm, cable bundles, bitrate screen, storage-room turret, 2k doorbell, turret-network, etc.).
| Output (images/lorex-camera-installation/lorex-camera-installation-manhattan-…webp) | Source | Crop | Placement |
|---|---|---|---|
| two-mini-dome-cameras-in-shop-drop-ceiling (980×370) | images/hik-connect-app-support-repair/hik-connect-app-support-repair-manhattan-mini-dome-cameras-in-shop-drop-ceiling.webp | none | Hero (eager) |
| white-dome-camera-tucked-into-ceiling-corner (430×430) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-dome-camera-in-office-ceiling-corner.webp | (0,0,430,430) flag excluded | §5 |
| white-lorex-bullet-camera-with-twin-spotlights-product-photo (275×183) | images/lorex-4k-bullet-camera-installation-manhattan.jpg | none | §6 |
| small-cameras-on-tall-wall-below-mezzanine-windows (907×440) | images/dahua-camera-installation/dahua-camera-installation-long-island-small-cameras-on-high-wall-of-open-hall.webp | none | §7 |
| white-dome-camera-in-stained-back-room-ceiling-corner (935×720) | images/hik-connect-app-support-repair/hik-connect-app-support-repair-manhattan-white-dome-camera-in-storeroom-corner.webp | none | §8 |
| black-mini-camera-above-lit-ceiling-soffit (605×520) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-mini-camera-on-showroom-drop-ceiling.webp | none | §9 cluster 1 |
| black-camera-and-shadow-on-plain-white-wall (705×510) | images/dahua-camera-installation/dahua-camera-installation-orange-county-bullet-camera-casting-shadow-above-ceiling-line.webp | (40,230,745,740) green edge removed | §9 cluster 2 |
| monitor-tiles-of-shop-aisles-and-shelving (305×360) | images/hik-connect-app-support-repair/hik-connect-app-support-repair-manhattan-store-monitor-showing-multi-camera-layout.webp | (0,0,305,360) counter/people/street tile excluded | §9 cluster 4 |
| black-lorex-floodlight-camera-with-two-light-panels-product-photo (263×192) | images/lorex-dual-floodlight-camera-installation-manhattan.jpg | none | §10 |
| white-lorex-video-doorbell-with-blue-lit-button-product-photo (151×334) | images/lorex-video-doorbell-camera-installation-manhattan.jpg | none | Field Notes |
| black-lorex-video-doorbell-with-blue-ring-product-photo (423×562) | images/lorex-video-doorbell.webp | none | FAQ |
Rejected: lorex-dual-lens-dome-camera-installation-manhattan.jpg (Uniview "unv" logo); lorex-4k-turret(-dome)-…-manhattan.jpg (identical to the turret Brooklyn used); lorex-dual-lens-panoramic-dome-…-nyc.jpg (no brand visible — can't confirm Lorex); apartment-building …-manhattan dome-over-glass and corridor-bullet (same scenes as Brooklyn's).

#### Build notes
- check_page.py: PASS (12,627 rendered words, title 56, meta 159, 6 JSON-LD blocks, FAQ 10 = schema 10, HowTo 7 = process cards 7, 11 figures, 2 Web3Forms forms, 183,247 B).
- simcheck: page-level max 0.144 (vs Brooklyn); paragraphs ≥0.65 only the NAP/contact line and the freshness byline.


## Orange County — merged 2026-10-18 from the Orange County build (local section, new silo findings, this page's questions for the register)

## Lorex Camera Installation — Orange County research (incoming)

Written 2026-10-18 by the REBUILD of `lorex-camera-installation-orange-county` (was crawled-not-indexed). For the main run to merge into `research/lorex-camera-installation.md` (that file was not edited by this run). Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page section used**. Tools: Firecrawl search / scrape (`mcp__Firecrawl__*`). Shell curl blocked. "carried" = a fact gathered and sourced by an earlier run in another research file (file + row named); not re-fetched today. Nothing below is invented; "excerpt" = only the search snippet was read.

### Orange County

Page: `lorex-camera-installation-orange-county` (REBUILD in place). Up-link `/lorex-camera-installation-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (845) 640-3835 in body, CTAs, sticky bar, form JS and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359.

**Thesis (distinct from Brooklyn = recorder placement and cable through attached masonry; HV hub = distance/outbuildings, outages, rural upload, county licensing, weekend houses, wildlife):** in Orange County a Lorex system is more and more often built to somebody else's written specification and judged later as evidence. Town short-term-rental laws (Town of Monroe L.L. 1-2022 Ch. 40; Village of Woodbury permit) require outdoor cameras "adequate in number, location and view angle to monitor arrivals and departures", recordings kept 30 days and handed to the Building Inspector, and notice to renters of camera locations and any audio; Airbnb has banned indoor cameras since April 30, 2024; the county proposed its own STR registry (Intro 7 of 2025). Around that: commuter houses empty from the pre-dawn Port Jervis Line train to evening (35.3-min mean commute, 66% drive alone), a fast-growing county (+11.1% 2015–2025; 13% of residents moved in since 2021) full of builder houses that can be pre-wired, river-city and village buildings, and businesses where the break-in video must identify someone (Newburgh restaurant burglary, Dec 2025). So the page is about designing a Lorex system for proof: what each camera must see at arrival points, how long the drive must hold, the recorder clock, who can pull a clip, and what must never be recorded.

#### Mandatory sources (§3) — status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Firecrawl search excerpts only: r/airbnb_hosts (OC-R1, OC-R2), r/hudsonvalley (OC-R3). No Orange-specific Lorex/camera thread found → EMPTY for Orange + Lorex. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and tests published claims instead (OC-A1, silo L/X rows, OC-P rows). |
| 6 | Landmarks | OC-T1 (Port Jervis Line / Harriman), carried floodlight L1–L6, C4 |
| 7 | Use cases / building stock | OC-H1–OC-H3, carried floodlight H1–H4, C1–C3 |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | ABC7 (OC-N1), News 12 (OC-N2), Advertiser News North (OC-N3); carried floodlight N1–N4 |
| 10 | Hyperlocal | Town of Monroe / Village of Woodbury / Town of Warwick code pages (OC-S1–S4); Orange County notice (OC-S5). Times Herald-Record / Mid-Hudson News Lorex or STR-camera items: EMPTY (none found). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — silo row 1.1 #11; not re-run |

#### Short-term rental rules (OC-S) — the core of this page
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| OC-S1 | `homeowners association rules security cameras exterior architectural review "Orange County" NY townhouse community Monroe OR Chester OR "Blooming Grove" OR Woodbury` · FC search → led to `https://www.strprofitmap.com/regulations/NY/monroe` · FC scrape (directQuote) | https://www.strprofitmap.com/regulations/NY/monroe | Third-party summary: Town of Monroe Local Law No. 1 of 2022 added Chapter 40 "Rentals, Short Term"; permit required for every STR; Building Inspector review + inspection; Town Board authorisation, hearing if neighbours within 500 ft object; quiet hours 10 p.m.–9 a.m.; occupancy caps; application lists "Remote digital monitoring cameras and their angles". Used only to find the primary text (OC-S2). | lead only |
| OC-S2 | `Town of Monroe Chapter 40 "Rentals, Short-Term" digital monitoring cameras ecode360` · FC search → FC scrape (pdf, directQuote) | https://monroeny.org/LinkClick.aspx?fileticket=19qWLs7OZrQ%3D&portalid=10 | **Town of Monroe Local Law No. 1 of the year 2022** (filed text): STR = occupancy "for 29 or fewer consecutive nights"; "Remote digital monitoring of occupancy. Where a short-term rental is rented or intended to be rented for transient occupancy during periods when the manager is not residing on-site, the site shall be digitally monitored by the manager to ensure compliance with the maximum number of allowable guests and visitors entering the premises, and to provide evidence to the Building Inspector … Digital monitoring shall include outdoor cameras adequate in number, location and view angle to monitor arrivals and departures at the property. Digital video recordings shall be taken during times when the property is rented and kept for a minimum of 30 days, and copies shall be provided to the Building Inspector upon request. Notice of locations and purpose of cameras shall be provided to renters as well as disclosure of audio recording if any." Town notice of adoption: https://monroeny.org/Resources/Latest-Town-News/notice-of-adoption-local-law-1-of-2022-rentals-short-term (excerpt: Town Clerk (845) 783-1900). | §5 para 3; §5.5 bullet 1; §6 card; §7 STR card + 7.5; §8.5 bullet 1; §9 cluster 1 (Q1–Q3), cluster 2 Q6, cluster 3 Q8, Q10; §10.5 H3 2, 4; §14; §15 package 2; FAQ; Sources |
| OC-S3 | same search (excerpt) → FC scrape (pdf, directQuote) | https://villageofwoodbury.com/document-center/building-code-enforcement-forms/residential-permit-applications/5836-short-term-rental-permit-application-2024/file.html | **Village of Woodbury Short-Term Rental Permit Application (2024)**: same wording — site "digitally monitored by the resident agency, landlord or absentee landlord"; "outdoor cameras adequate in number, location and view angle to monitor arrivals and departures"; recordings during rental, kept "a minimum of thirty (30) days", copies to the Building Inspector on request; notice of locations and purpose to renters, "disclosure of audio recording, if any". | §5 para 3; §5.5 bullet 1; §8.5 bullet 1; §9 cluster 1 Q1; Sources |
| OC-S4 | `short-term rental local law Orange County NY town Warwick OR Woodbury OR "Greenwood Lake" OR Cornwall OR Chester OR Tuxedo cameras OR "digital monitoring" permit` · FC search → FC scrape | https://ecode360.com/45290550 | Town of Warwick Ch. 129 Short-Term Rental Property: adopted 9-10-2018 by L.L. No. 5-2018; amended in its entirety 4-27-2023 by L.L. No. 2-2023; landlords/absentee landlords must register and obtain a permit (excerpt). Scrape returned no camera/monitoring text → page says Warwick requires a permit and does NOT claim a camera rule there. Same search excerpts: Town of Chester STR local law (https://www.chesterwcny.gov/media/5451 — note: chesterwcny = Chester, Warren County? domain unclear → NOT used); Village of Cornwall-on-Hudson proposed STR regulations (https://cornwall-on-hudson.gov/Welcome/Village-Board/Proposed-Laws/Regulations-for-Short-Term-Rentals, excerpt, proposed only → named as "proposed" only); petersisca.com blog (third-party: Village of Warwick STR law Jan 2025; Greenwood Lake permit) → not relied on. | §9 cluster 1 Q1 (Warwick permit, no camera claim); §13; Sources |
| OC-S5 | `Orange County NY short-term rental registry Article 12-D county law 2025 register hosts` · FC search → FC scrape (pdf, directQuote) | https://www.orangecountyny.gov/DocumentCenter/View/35247/Local-Law-Intro-No-7-of-2025-PDF | Notice of public hearing: Local Law Intro. No. 7 of 2025 amends L.L. 13 of 2009 so Orange County is a "covered jurisdiction" under Real Property Law Article 12-D; establishes an STR unit registration system with the Commissioner of Finance making the regulations under RPL §447-c; hearing Oct 27, 2025, 10:30 a.m., 255 Main Street, Goshen. Adoption status not confirmed in this run → page says "proposed / put to a public hearing". | §9 cluster 1 Q4; §5.5 bullet 2; Sources |
| OC-S6 | same search (excerpt) | https://www.nysenate.gov/legislation/laws/RPP/447-C | RPL §447-c: short-term rental hosts must register units with the county (or multi-county) registry; text excerpt only. | §9 cluster 1 Q4 (background) |
| OC-S7 | `Airbnb policy security cameras indoor ban 2024 exterior cameras disclosure noise monitoring devices` · FC search (full excerpts) | https://www.airbnb.com/help/article/3061 ; https://news.airbnb.com/an-update-on-our-policy-on-security-cameras | Airbnb: no security cameras or recording devices that monitor any part of a home's interior "even if these devices are turned off"; hidden cameras prohibited; exterior cameras allowed if disclosed in the listing; not allowed over exterior areas with greater privacy expectation, "such as the inside of an enclosed outdoor shower or in a sauna"; doorbell cameras count as recording devices; noise decibel monitors allowed (disclosed, not in bedrooms/bathrooms); rules took effect April 30, 2024. Newsroom: outdoor cameras "prohibited from monitoring indoor spaces". | §5 para 3; §5.5 bullet 3; §7 STR card; §9 cluster 2 Q5, Q7; §10.5 H3 3; FAQ; Sources |
| OC-R1 | `reddit Lorex cameras Airbnb host outdoor camera arrivals guests count occupancy short term rental recording 30 days` · FC search (excerpt) | https://www.reddit.com/r/airbnb_hosts/comments/vxt4ll/do_you_check_cameras_for_number_of_guests/ | Host: "I have 2 cameras outside my property and occasionally take a look to make sure things look okay but don't monitor the number of guests." | §9 cluster 1 Q2 (contrast with Monroe's headcount purpose) |
| OC-R2 | same (excerpt) | https://www.reddit.com/r/airbnb_hosts/comments/1574ogf/security_cams_or_no/ | "Outdoor cameras are really helpful for hosts to catch bad guests who party, smoke, bring people …" | §9 cluster 3 Q8 |
| OC-N3 | `short-term rental … Greenwood Lake` (OC-S4 search) → FC scrape (directQuote) | https://www.advertisernewsnorth.com/news/local-news/airbnb-rolls-out-new-tools-as-towns-wrangle-with-regulation-IC756082 | Dec 26, 2019: attorney Alfred V. Acquavivia represents several Greenwood Lake residents who object to short-term rentals; Airbnb's new tools aimed at "party houses"; Acquavivia: "the first step is always to try to prevent the problem from occurring". (Article mixes NY and NJ sides of the lake; listing counts are Passaic County NJ → not used.) | §5 para 3 (quote, dated); Sources |

#### Building stock / population / commuting (OC-H, OC-T)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| OC-H1 | (direct) · FC scrape (query, directQuote) | https://censusreporter.org/profiles/05000US36071-orange-county-ny/ | ACS 2024 1-yr: population 411,767; 141,127 households; 152,422 housing units; 93% occupied; 66% owner-occupied; single unit 69%; year moved in: 13% since 2021, 25% 2018–2020, 29% 2010–2017; mean travel time to work 35.3 min; 66% drove alone, 10% carpooled, 6% public transit, 11% worked at home. (Population/units/occupancy also carried in floodlight H1.) | §5 para 1–2; §5.5 bullets 4–5; §9 cluster 4 intro; §13; Sources |
| OC-H2 | `Orange County New York fastest growing county population estimate 2024 2025 census Hudson Valley` · FC search (excerpt, full table) | https://usafacts.org/answers/is-the-population-growing-or-shrinking/county/orange-county-ny/ | Orange County grew 11.1% 2015–2025; +2,581 (2024–25); +16,023 (2019–20, largest); +4,909 (2023–24); 2024–25 natural change 2,817, immigration 1,150, domestic migration −1,410 (US Census Bureau). | §5 para 2; §5.5 bullet 5; §7 new-build card; Sources |
| OC-H3 | carried floodlight H2 | https://www.recordonline.com/story/news/local/2021/08/13/census-kiryas-joel-grew-leads-orange-population/8115187002/ | Kiryas Joel 32,954 (+63%), ~half of county growth; families to Blooming Grove, Woodbury, Monroe. | not cited in body (Kiryas Joel named in service-area list and schema only) |
| OC-T1 | `Port Jervis Line stations Harriman Salisbury Mills-Cornwall Campbell Hall Middletown Otisville Port Jervis Metro-North Orange County commuters` · FC search (full excerpts) | https://www.mta.info/schedules/metro-north/port-jervis ; https://en.wikipedia.org/wiki/Port_Jervis_Line | MTA timetable: earliest weekday inbound leaves Port Jervis 3:44 AM, Middletown/Town of Wallkill 4:15 AM; Orange stations Port Jervis, Otisville, Middletown/Town of Wallkill, Campbell Hall, Salisbury Mills/Cornwall, Harriman, Tuxedo; last outbound arrives Port Jervis 12:35 AM (and later trains); operated by NJ Transit under contract to Metro-North. Wikipedia: Harriman is the busiest station on the line; Campbell Hall serves Goshen, Montgomery, Walden; mile-long tunnel under the Shawangunk Ridge after Otisville. | §5 para 2; §5.5 bullet 4; §9 cluster 4 Q11; §13 card; Sources |

#### Licensing / contracts (OC-K) — county electrician licence
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| OC-K1 | `orangecountygov.gov Consumer Affairs licensing electrician license Orange County New York Goshen "Consumer Affairs"` · FC search (excerpts) | https://www.orangecountyny.gov/255/Licenses ; https://www.orangecountyny.gov/DocumentCenter/View/317/Electrician-Application-PDF ; https://townofmontgomeryny.gov/LinkClick.aspx?fileticket=xVC392-zNw0%3D&portalid=8 | Electrician application/renewal on the county Licenses page; applications go to "OC Dept of Consumer Affairs and Weights & Measures, 255 Main Street, Goshen, NY 10924" and the County of Orange Electrical Licensing Board; Montgomery posts an "Orange County Notification for Electrical Inspector Licensing" from the same department. | §8.5 bullet 3; §10.5 H3 5; Sources |
| OC-K2 | same search → FC scrape (pdf, directQuote) | https://inspectionsontime.com/images/Laws/Orange_County_Electrical_Law.pdf | Third-party copy of Local Law Intro. No. 13 of 2013 "amending and restating Local Law No. 8 of 2007" — Orange County Electrical Licensing Board; "hands-on experience" defined as wiring "for light, heat, power and signaling purposes"; where a building permit is required, electrical work "must be inspected by a certified electrical inspector"; violation = fine up to $1,000 and/or up to fifteen days. No explicit low-voltage exemption quoted → page does not claim one. | §8.5 bullet 3; §10.5 H3 5; Sources |
| OC-K3 | carried floodlight K1 | https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF ; https://www.middletownny.gov/259/Electrical-Licensing-Board | L.L. 1 of 2024 revises electrical licensing; City of Middletown has its own Electrical Licensing Board. | §8.5 bullet 3; Sources |
| OC-K4 | carried floodlight K3 | https://www.orangecountyny.gov/DocumentCenter/View/951/Consumer-Law-Help-Manual---Home-Improvements-PDF | County consumer guide: home-improvement contracts over $500 written, plain English, signed; name/address/phone; work and materials incl. makes/models; progress payments. | §8.5 bullet 4; §12 step 4; Sources |
| — | Orange County home-improvement contractor licence | carried floodlight K2 | none found → EMPTY; page makes no such licence claim. | — |

#### News / police (OC-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| OC-N1 | `Orange County NY police 2026 package theft OR burglary OR "car break-ins" Middletown OR Monroe OR Wallkill OR Newburgh surveillance video residents` · FC search (news, full excerpt) | https://abc7ny.com/post/newburgh-restaurant-burglary-community-rallies-behind-owner-artistic-taste-known-provide-food-need/18295756/ | Dec 17, 2025 (WABC, Marcus Solis): burglary at An Artistic Taste, Newburgh; "Surveillance video shows a burglar behind the bar early Sunday morning, stealing the terminal, a printer, an iPad and the cash register drawer"; video shows crowbar forcing the front door; owner: "There was only $100 in the cash register … The hardware and to repair the door is why the costs really add up"; community raised $3,000. | §8 card (Newburgh); §9 cluster 6 Q17; Sources |
| OC-N2 | `… road takeovers` (same search family, past year) · FC scrape (directQuote) | https://westchester.news12.com/2026/05/08/crackdown-on-dangerous-illegal-street-activity-in-orange-county/PN7efSB3C0m0MpJPSl5NE | May 8, 2026: police cracking down on late-night street racing, burnouts and reckless driving on Route 97 in the Town of Deerpark; about 30 cars cited; nearly 50 tickets the week before; some drivers from Pennsylvania and Syracuse. | §13 (Port Jervis / Deerpark card); FAQ headlights; Sources |
| — | Orange County NY package theft / porch-piracy news | OC-N1 search; carried floodlight N6 | EMPTY (only an undated aggregator excerpt) → page cites none. | — |
| — | City of Middletown PD "9 PM routine" / unlocked-vehicle thefts | `"Town of Wallkill" OR "Town of Monroe" OR … police 2026 thefts from unlocked vehicles …` · FC search (excerpt, Facebook, ~2 yrs old) | Too thin/undated → NOT used. | — |
| carried | floodlight N1 (New Windsor PD Jan 20 2025, organized theft groups, "Consider installing surveillance cameras"), N3 (Tractor Supply New Windsor/Crawford thefts Nov 2025), N4 (Newburgh ending Flock contract, Sept 25 2026) | see research/floodlight-camera-installation.md `## Orange` | — | §5 para 4 (N1); Sources |

#### Broadband (Orange)
`Orange County NY broadband unserved homes ConnectALL Warwick OR Deerpark OR Greenville OR Mount Hope internet 2025` · FC search → only Ulster, Sullivan and other counties → **EMPTY for Orange**. Page makes no Orange broadband claim (hub covers rural upload).

#### Silo additions — Lorex (new rows from this run, for Part 1)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L13 | `Lorex NVR how to back up video to USB flash drive help article export recordings` · FC search (lorex.com, excerpts) | https://www.lorex.com/blogs/help/lhb-series-backing-up-recorded-video-to-a-usb-flash-drive ; https://www.lorex.com/blogs/help/dvr-nvr-how-to-format-your-usb-flash-drive-on-your-recorder ; https://www.lorex.com/pages/security-recorder-programming | Back up one or more clips to a USB flash drive "(not included)" from Playback; format the USB stick on the recorder (Main Menu > Settings > System …); "Insert your USB thumb drive into one of the USB ports of the recorder. From the live view, right-click …". | §9 cluster 3 Q8; §12 step 7; Sources |
| L14 | `Lorex NVR overwrite when hard drive full setting continuous recording schedule motion recording help` · FC search (lorex.com, excerpts) | https://www.lorex.com/blogs/help/lha-lnk-series-determining-how-long-recordings-will-be-stored ; https://www.lorex.com/pages/security-recorder-programming ; https://www.lorex.com/blogs/help/lha-lnk-series-setting-a-recording-schedule ; https://www.lorex.com/pages/hdd-calculator ; https://www.lorex.com/blogs/help/rd501-series-4k-8-channel-digital-video-recorder-faq-troubleshooting-guide | "Most security recorders are programmed to constantly overwrite the oldest footage"; Continuous vs Motion set at "Main Menu, click Settings > Recording > Recording"; schedule edited per day by dragging; HDD calculator: "upgrading your hard drive will greatly prolong" retention; RD501: "Overwrite replaces the oldest recordings automatically when storage is full". | §9 cluster 1 Q3, cluster 3 Q10; §10.5 H3 2; Sources |
| A4 | carried floodlight A2 (Orange) | https://www.thumbtack.com/ny/newburgh/security-camera-install | Thumbtack Newburgh: "anywhere from $100 for a single-camera line installation to $1,000-$2,200 for an entire system." | §10.5 H3 1 |
| Used from Part 1 (not re-fetched) | L1 (328 ft), L5 (HaLow), L8 (battery 4–6 months, cold), L9 (three apps; Lorex Classic works with Google Home/Alexa; shared users), X2 (Fusion: remote access needs wired NVR-to-router, ≥6 Mbps upload), X5 (Lorex FAQ: one-year warranty; NDAA exclusion; audio not always legal), X6 (FCC DA 26-635 notice), X7 (HDD calculator: motion ≈ 120 thirty-second events per hour of recording), X9 (doorbell 16–24 V AC), X10 (person/vehicle detection), G3 (Penal Law 250.05/250.00), G4/HV-G6 (Civil Rights Law 52-a), G6 (NYS tax credit), N2/N3 (TX/NE AG suits — not used on this page) | — | — | as noted in page Sources |

#### Landmarks (carried, not re-fetched) — research/floodlight-camera-installation.md `## Orange` L1–L6, C1–C4
Washington's Headquarters / Newburgh East End HD (L1, H3); Storm King Art Center (L2, not used); Goshen Historic Track (L3, 1838, NHL); Woodbury Common (L4/C4, 1985, ~220 stores); Black Dirt region, Pine Island (L5); Tri-States Monument, Port Jervis (L6/C4, 1882); LEGOLAND New York (C4, Goshen, 2021); Amazon/Medline at Route 17K/747 Montgomery (C1); ~40 warehouse projects incl. Matrix at Route 300 & I-84 (C2, C3). → §7, §8, §13.

#### Pricing (§9 — no invented prices)
Basis = Hudson Valley hub Orange row (lorex-camera-installation-hudson-valley.html, read 2026-10-18), which applies §9 Orange 1.40× to the Brooklyn **labour** base from the silo calculator (research Part 1.7: $175 line + $25 box = $200 per wired camera; $150 recorder setup; equipment $845 / $78 / $320 locked, not multiplied). Verified: 4 × $280 + $210 = $1,330 labour + $845 = **$2,175** four-camera system; $78 + $280 = **$358** camera added; $320 + $210 = **$530** recorder with setup; BYOE labour **$280 per wired camera, $210 recorder setup** (as the hub states). Service visits **$195/hr, 3-hr minimum ($585)** — protected, not multiplied. Package arithmetic on the page is shown openly: six cameras = $2,175 + 2 × $358 = **$2,891**; eight cameras = $2,175 + 4 × $358 = **$3,607** (plus $530 if the four-camera recorder lacks free channels). Larger drives, ePoE/wireless links, trenching, electrician work: quoted after the walk-through (no number). **FLAG:** `lorex-camera-installation-prices-orange-county.html` calculator uses the paired Orange/Putnam zone ($247 line / $195 setup) — not §9; same open decision as the hub (research Part 1.7). The page links to it but states the §9 figures.

#### House practices stated on the page without an external source (FLAG for Anwar)
- Continuous recording on rental-house cameras while booked; drive sized for ≥30 days at that setting with margin; motion schedule when owner is in residence.
- Recorder clock set to network time and checked at handover and at each daylight-saving change; clip export test to USB at handover.
- Pre-wire recommendations for houses under construction (Cat6 home runs to eaves, porch, garage, a conditioned closet; pull string; labelled ends) — general practice.
- Recorder not in an unconditioned garage (also an HV hub house practice).
- No interior cameras at any rental, even owner-only areas, while listed (follows Airbnb wording); audio off at rentals.
- Installation between bookings / two-hour arrival windows any day to 8 PM (silo convention); "recording again within one to two hours of arrival" (silo convention, blueprint §5 el. 36).
- Insurance certificate on request; written contract with makes/models (county consumer guide).
- Field Notes = installer-voice method note (walk the arrival points at night, count what the town will ask for), no specific job story.

#### Images (11) — Drive: no Lorex folder (per main run); CompanyCam not connected
Permanent image rule: 7 real AESS job photos from other jobs (re-cropped, none of the crops used by the Brooklyn or HV Lorex pages; several source scenes not used anywhere in the Lorex silo) + 4 Lorex manufacturer product shots not used by Brooklyn/HV (white 4K bullet, white doorbell, dual floodlight, NVR re-cropped to its badge end). All viewed with Read before naming; WebP q80, ≤1600 px; only names containing `-orange-county-`. Avoided: KNOWN BAD list (parking/*, buzzer-repair/*, low-voltage/*video-intercom*, Uniview-branded lorex-* files incl. lorex-dual-lens-dome-* which shows a UNV twin dome); the yellow-fascia/mural dome, brick-wall lot view, cable-bundle, storage-room turret and LG monitor scenes already used by Brooklyn/HV.
| Output (images/lorex-camera-installation/lorex-camera-installation-orange-county-…webp) | Source | Crop | Placement |
|---|---|---|---|
| black-bullet-camera-high-on-tall-wall-above-ceiling-bulkhead (947×685) | images/dahua-camera-installation/dahua-camera-installation-orange-county-black-bullet-camera-high-on-painted-wall.webp (real AESS job photo) | (300,250,1247,935) | Hero (eager) |
| two-small-cameras-on-tall-wall-under-mezzanine-windows (720×440) | images/dahua-camera-installation/dahua-camera-installation-long-island-small-cameras-on-high-wall-of-open-hall.webp (real) | (0,0,720,440): glass door/reflections at right excluded | §5 |
| white-lorex-4k-bullet-camera-with-twin-lights-product-photo (275×183) | images/lorex-4k-bullet-camera-installation-orange-county.jpg (Lorex product shot) | none | §6 |
| white-dome-camera-in-corner-under-water-stained-tiles (600×560) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-long-island-dome-camera-in-corner-under-stained-ceiling-tiles.webp (real) | (0,0,600,560): stored board/box at lower right excluded | §7 |
| black-bullet-camera-on-short-pendant-from-ceiling-grid (650×390) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-westchester-county-black-bullet-on-pendant-mount-in-office-ceiling.webp (real) | (150,110,800,500) | §8 |
| recorder-view-of-dim-back-storeroom-and-doorway (460×330) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-ulster-county-recorder-tile-of-dim-back-storeroom.webp (real) | (90,0,550,330): channel label and printed box excluded | §9 shops cluster |
| lorex-two-panel-floodlight-camera-product-photo (263×192) | images/lorex-dual-floodlight-camera-installation-orange-county.jpg (Lorex product shot) | none | §10 |
| lorex-4k-nvr-badge-and-playback-buttons-product-photo (680×170) | images/nvr-lorex-4k-16ch.png (Lorex product shot; HV used the full frame) | (20,215,700,385) front-panel strip | §14 |
| small-white-domes-spread-across-drop-ceiling (720×310) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-long-island-mini-domes-spread-across-shop-drop-ceiling.webp (real) | (0,0,720,310) | §15 |
| black-mini-camera-at-edge-of-ceiling-bulkhead (605×520) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-mini-camera-on-showroom-drop-ceiling.webp (real) | none | Field Notes |
| white-lorex-video-doorbell-with-blue-ring-product-photo (151×334) | images/lorex-video-doorbell-camera-installation-orange-county.jpg (Lorex product shot) | none | FAQ |
All WebP q80, ≤1600 px. Alt/title unique and contain "Orange County"; captions say "example photo from another AESS job (not an Orange County …)" or "manufacturer product photo (not an installed …)". DAILY-LOG note: `images: 11 = 7 real AESS job photos from other jobs (re-cropped) + 4 Lorex manufacturer product shots (no real Lorex photos yet)`.

#### Question register additions — lorex-camera-installation-orange-county (REBUILT 2026-10-18)
Q&A H3 + repair H2 (headings ending in '?'):
- Orange County Lorex Stopped Recording?
- Our Monroe rental needs a town permit — what does the camera part of the application actually ask for?
- Which doors, drives and paths count as “arrivals and departures” when a town requires them on camera?
- The town wants thirty days of video kept — what does that mean for the recorder's hard drive?
- Does Orange County's new short-term-rental registry say anything about cameras?
- Airbnb bans indoor cameras — does that rule out a doorbell camera or an outdoor camera that sees through a window?
- Do renters have to be told where the cameras are, and what changes if a camera has a microphone?
- A hot tub, outdoor shower or fire pit is part of the rental — can any camera cover it?
- A neighbour complained about a party at our rental — how do we show the building inspector who arrived and when?
- Our recorder's clock is a few minutes off — does that matter if footage ends up with the town or a court?
- Should the rental's cameras record all the time or only on motion when guests are in?
- We leave for an early train and get home after dark — which Lorex alerts are worth receiving at work?
- Can the system let us know the kids got in the door after school?
- Some mornings the garage door gets left open in the rush to the train — can the cameras catch that?
- Our house is still being framed — what should go into the walls now so Lorex cameras can be added later?
- Should the builder's electrician run the camera cable, or someone who installs cameras?
- Our street is still a construction site — is a camera worth installing before the neighbouring houses are finished?
- What should a restaurant's cameras see so that a break-in video actually identifies someone?
- Our landlord's cameras already cover the outside of the building — is a Lorex system inside our unit still worth it?

Visible FAQ (§17) = FAQPage:
- We are going to stop renting the house and move in ourselves — what should change on the Lorex system?
- Can the rental's driveway camera also show how many cars guests parked?
- Headlights sweep across our driveway all night from the county road — will they set off alerts?
- A guest wants to see our camera footage after a dispute over damage — do we have to share it?
- Can we see the front-door camera on a kitchen smart display or speaker screen?
- Can new Lorex cameras use network cable a previous owner ran for another brand's cameras?
- Can the installation be fitted into the gap between two bookings?
- Can the cameras confirm the cleaners came and how long they stayed?
- What happens if a guest covers or unplugs an outdoor camera?
- Can the old camera system keep recording until the new Lorex system is running?

De-dup notes: checked by meaning against the full register (old template, prices pages, Brooklyn, HV hub) and against the parallel Long Island / Manhattan rebuilds as they stood ~mid-run; replaced two drafts that overlapped LI (porch-packages camera; recorder in the garage) and avoided HV intents (outage restart, licensing map, caretaker access, neighbour's yard, public buyers) and Brooklyn intents (NYPD export, overwrite, co-op approval, install duration, payment).

#### Build notes
- check_page.py: **PASS** (full, incl. registration — sitemap/_redirects/hub link-down and sibling back-links were already present). 13,780 rendered words; title 57; meta 156; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; HowTo 7 = process cards 7; 2 Web3Forms forms (hf/qf); 195,366 B (Brooklyn 186,125; Manhattan 182,745 and LI 177,115 at check time — re-check after the parallel rebuilds finish).
- simcheck vs silo: page-level max 0.124 (Brooklyn); paragraphs ≥0.65 only the NAP line (vs Manhattan 0.938, Brooklyn 0.787) and the freshness byline (vs Manhattan 0.730, Brooklyn 0.667). vs floodlight-camera-installation-orange-county: page 0.090, paragraph max 0.629.
