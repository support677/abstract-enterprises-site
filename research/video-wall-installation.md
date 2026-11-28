# Research — Video Wall Installation silo

Created 2026-10-18 for the REBUILD of `video-wall-installation-long-island` (Long Island hub). First page of the silo rebuilt under blueprint v2.3; the other 15 pages are still the old near-duplicate template and are queued as REBUILD lines.

Every entry: **exact query · platform · URL · finding · page + section used**. Searches were run with the Firecrawl search/scrape tools from the build environment on 2026-10-18. A surface the build environment cannot open is written `EMPTY (not accessible in build env)` — nothing below is invented.

---

## 1. Research matrix (v2.3 §3, all 11 sources)

| # | Source | Status | Notes |
|---|---|---|---|
| 1 | Reddit | Partial — search-result excerpts only (threads not opened) | r/CommercialAV, r/VIDEOENGINEERING, r/digitalsignage, r/longisland (see §3.1) |
| 2 | Google PAA | EMPTY (not accessible in build env) | Question intents drawn instead from Reddit excerpts, manufacturer FAQs and the cost-guide pages in §3.3 |
| 3 | Google PASF | EMPTY (not accessible in build env) | — |
| 4 | Answer the Public | EMPTY (not accessible in build env) | — |
| 5 | Google AI Overview | EMPTY (not accessible in build env) | The "reality check" section quotes the claims made by the web cost guides and rules of thumb that rank for the same queries (§3.3), and says so on the page |
| 6 | Area landmarks | Done | §5 Long Island |
| 7 | Area use cases / building stock | Done | §5 Long Island |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) | — |
| 9 | Local news | Done (LIBN, Patch, NY Post, SBU News) | §5 |
| 10 | Hyperlocal | Partial (Patch Long Island; Stony Brook Matters) | §5 |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — Yelp search pages returned only listing excerpts (business names, star averages), no review text | Not used for any claim |

---

## 2. Technology facts (manufacturer and standards documents)

| Query · platform | URL | Finding | Used on (LI hub) |
|---|---|---|---|
| `Samsung VM55B-U video wall bezel-to-bezel 0.88mm specifications` · Firecrawl search | https://image.makewebeasy.net/makeweb/0/jxlPpOYv8/Document/Samsung_VMB_U_Datasheet_CPS.pdf (Samsung datasheet copy) and https://image-us.samsung.com/SamsungUS/samsungbusiness/pdfs/datasheet/Video_Wall_Displays_Brochure_VHR-R_VHT-E_VMT-E_VMT-U_series.pdf | Samsung video wall line-up: VHR-R / VMB-R 0.88 mm bezel-to-bezel (700 / 500 nit), VHB-E / VMB-E 1.74 mm, VMB-U 3.5 mm; all 55-inch models 1920×1080, 24/7 operation, VESA 600×400, ~70 mm deep, 19.5 kg set weight (VM55B-E), "Video Wall Daisy Chain (10x10)", DP 1.2 digital daisy chain, temperature sensor. Note "Active area to Active area may vary" — VM55B-E A2A 2.49 mm vs B2B 1.74 mm | Equipment (LCD tiles card + LCD vs LED table); Q&A "12 feet deep"; Q&A "separate computer"; AI check "seamless" |
| `LG 55VM5J video wall 0.44mm even bezel specifications` · Firecrawl search | https://media.us.lg.com/asset/bf2bb65e-9c9f-49a5-9552-d889bf118e4f/55VM5J-H-Spec-Sheet.pdf | LG 55VM5J-H: 1.74 mm BtB, 500 nits, IPS, 18.8 kg (41.4 lb), VESA 600×400, operating 0–40 °C, 10–80 % humidity, typ. 160 W / 546 BTU/h, max 190 W / 648 BTU/h, tile mode up to 15×15, SNMP, status mailing, fail-over, "No Signal Image", Crestron inside | Q&A cooling (BTU), Q&A remote checks (SNMP/status mailing), Equipment |
| same search | https://www.lgcommercialdisplay.com/products-solutions/digital-signage/video-wall/55VSM5J | LG 55VSM5J: 0.44 mm even bezel, 500 cd/m², 86.5 mm deep | Equipment (bezel options) |
| `LG LED video wall LSAA power consumption per cabinet BTU heat direct view LED specifications` → scrape · Firecrawl | https://www.lg.com/global/business/commercial-display/led-signage/indoor-led/lapa136/ | LG LAPA136 all-in-one LED: 136-inch, 1.56 mm pitch, 1920×1080, 500 nit after calibration, max 1,300 W/screen, avg 650 W/screen, heat max 4,436 BTU/h, avg 2,218 BTU/h | Q&A cooling; Equipment (all-in-one LED card); LCD vs LED table |
| `Planar pixel pitch viewing distance rule of thumb LED video wall` · Firecrawl | https://www.planar.com/blog/2025/what-is-pixel-pitch-and-why-does-it-matter/ ; https://www.planar.com/media/439462/understanding-viewing-distance.pdf | Planar: "Pixel Pitch x 10 = Approximate Viewing Distance in Feet"; table: 1.5 mm visual-acuity distance 16 ft 11 in / comfortable 8 ft 6 in; 2.5 mm 28 ft 2 in / 14 ft 1 in; 3.0 mm 33 ft 10 in / 16 ft 11 in | Equipment pitch table; AI check "rule of thumb" |
| same search | https://www.christiedigital.com/spotlight/understanding-pixel-pitch-led-video-wall/ | Christie: "For each millimeter of pixel pitch, allow approximately one meter of minimum viewing distance" | AI check (rules disagree) |
| same search | https://www.barco.com/en/residential/creating-the-experience/the-architectural-digital-canvas/technology-ingredients/pixel-pitch-and-viewing-distance | Barco: ideal pitch (mm) = optimal viewing distance (m) / 2 | AI check |
| `ADA 307.2 protruding objects 4 inches 27 inches 80 inches wall mounted` · Firecrawl | https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ ; https://www.corada.com/documents/2010ADAStandards/307 | 2010 ADA Standards 307.2: wall-mounted objects with leading edges more than 27 in and not more than 80 in above the floor may protrude no more than 4 in into the circulation path | Q&A "how far will it stick out"; Commercial compliance list; Building cards |
| `Chief ConnexSys video wall mount pop-out service depth specifications` · Firecrawl | https://www.alldataresource.com/assets/chief-manufacturing/Chief-Manufacturing-LVS1U-TV-Mount-Spec-Sheet.pdf ; https://www.legrandav.com/products/mounts/display-tv-mounts/connexsys-video-wall-mounting-system | Chief ConnexSys LVS1U landscape mount: depth settable 4 in to 7.4 in from the wall, 42.70 lb; rail-based, pop-out service; portrait version LVS1UP minimum depth 4 in | Q&A ADA (4 in vs 7.4 in); Equipment mounts card |
| `Samsung LCD video wall image retention prevention pixel shift` · Firecrawl | https://www.samsung.com/hk_en/support/tv-audio-video/how-to-troubleshoot-burn-in-or-image-retention-on-your-samsung-oled-tv/ | Samsung describes Pixel Shift / pixel refresh as image-retention countermeasures (consumer OLED page — used only for the general concept) | Q&A ghosting (worded generally; panel-specific settings left to the model's manual) |
| scrape · Firecrawl | https://insights.samsung.com/2024/10/21/why-you-shouldnt-use-consumer-tvs-for-commercial-digital-signage/ | Samsung (Oct 21 2024): consumer TVs designed for "perhaps eight hours a day"; portrait use will eventually fail them (venting); "a consumer TV's warranty will be invalidated if it's used for commercial purposes"; most commercial displays ship with three-year warranties vs one year consumer; consumer 250–400 nits | Q&A "TVs we already bought"; AI check |
| `reddit video wall consumer TVs vs commercial displays` · Firecrawl | https://www.reddit.com/r/CommercialAV/comments/1j9qccf/does_anyone_have_proof_of_why_its_bad_to_use/ | Excerpt: "Consumer TVs use convection cooling that simply doesn't work unless they are landscape oriented." | Q&A consumer TVs (paraphrased, attributed to integrator discussion) |

## 3. Market and question research

### 3.1 Reddit (excerpts only)
| Query · platform | URL | Finding | Used on |
|---|---|---|---|
| `reddit CommercialAV video wall one panel died replacement color mismatch` · Firecrawl | https://www.reddit.com/r/CommercialAV/comments/hvbzp0/replacing_a_single_panel_of_a_video_wall/ | "It's always possible to replace a single panel; it's just up to the end users' tolerance for how different the panel will look." | Body: spare-panel advice in Equipment section and AI check |
| same | https://www.reddit.com/r/VIDEOENGINEERING/comments/1loe2ie/video_wall_panels_different_colors/ | Panel colour mismatch threads; fixes via config/calibration | AI check "set and forget" |
| same | https://www.reddit.com/r/CommercialAV/comments/1ndglav/replacement_panel_for_older_lcd_video_wall/ | Owners hunting replacement panels for older LCD walls | Equipment (buy matched spares) |
| `reddit ... video wall pricing` (cost search) · Firecrawl | https://www.reddit.com/r/CommercialAV/comments/1bl6fyy/video_wall_pricing/ | Excerpt: "Just the mounting structure alone could be 20k. The wall can range from 15-200 k." | AI check (cost spread) |
| `reddit longisland video wall OR "multiple TVs" sports bar install` · Firecrawl | https://www.reddit.com/r/longisland/comments/19cr3bk/tv_mounting/ | r/longisland thread on TV mounting: DIY advice ("mounting kit on Amazon ... 40 bucks") — residential TVs only; nothing on video walls | Not quoted; shows LI residents treat mounting as DIY — informs "Can we use the TVs we already bought?" |

### 3.2 Yelp
`yelp video wall installation Long Island NY reviews AV installer` · Firecrawl → https://m.yelp.com/search?find_desc=Audio+Video+Installation&find_loc=Long+Island%2C+NY — listing page excerpts only (names and star averages). **EMPTY (not accessible in build env)** for 1–3★ review text. No Yelp claim on the page.

### 3.3 "What the web/AI says" (substitute for the AI Overview, which could not be opened)
| Query · platform | URL | Claim | Used on |
|---|---|---|---|
| `video wall installation cost how much does a video wall cost per square foot 2026` · Firecrawl | https://www.crowntv-us.com/blog/led-video-wall-cost/ | Installed dvLED $/sq ft by pitch (P1.5–1.9 $1,500–2,500; P2.5 $900–1,600); online P2.9 kits ~$220–300/sq ft hardware only | AI check "online kit price" |
| same | https://americanledwall.com/led-video-wall-cost/ | "most installed walls run about $500 to $2,500 per square foot"; indoor wall draws "roughly 25 to 40 watts per square foot" | AI check |
| same | https://svsolutionsusa.com/how-much-does-led-video-wall-cost/ | "$9,500 for an entry-level indoor wall to $200,000+" | AI check |
| same | https://www.techinchurch.com/church-led-video-wall-cost | church LED wall $18,000–$28,000 small | AI check (generic ranges) |

### 3.4 Keywords — five layers (v2.3 Appendix A)
- **Service:** video wall installation, video wall installer, LED video wall installation, LCD video wall, commercial video wall, video wall mounting, video wall calibration, video wall repair/service, multi-screen display wall, digital signage wall.
- **Problem:** seams/bezel lines, panel colour mismatch, dead panel, image retention/ghosting, wall can't hold weight, no outlet behind wall, room overheating, glare from storefront glass, sign-code violation, controller/processor failure, content won't fill the wall.
- **Technology:** bezel-to-bezel (B2B), active-area-to-active-area, pixel pitch, direct-view LED (dvLED), all-in-one LED, fine-pitch, nits, daisy chain, video wall processor/controller, multiviewer, HDBaseT, pop-out mount, SNMP, BTU/h.
- **Industry:** corporate lobby, reception, operations/dispatch room, retail, car dealership showroom, sports bar/restaurant, house of worship, school/university lobby, healthcare waiting room, municipal/public-safety room, home media room.
- **Geographic (this page):** Long Island, Nassau County, Suffolk County, Route 110/Melville, Hauppauge, Uniondale/RXR Plaza, East Garden City/Roosevelt Field, Lake Success/New Hyde Park, Stony Brook, Riverhead, Yaphank, Lake Grove/Smith Haven, Islip, Hempstead.

### 3.5 Pricing basis (for every page of the silo)
- The live silo pages publish package tables that **do not follow v2.3 §9**: Brooklyn = Queens = NYC hub (e.g. 2×2 LCD $12,000–$18,000), while the old Long Island, Nassau and Suffolk pages all show a *lower* table (2×2 LCD $11,500–$17,000) and Hudson Valley lower still. FLAGGED for Anwar.
- Rebuilt LI hub uses the **Brooklyn base table** (`video-wall-installation-brooklyn.html`, = NYC hub rows) × §9 multipliers: **Nassau 1.15, Suffolk 1.20**, shown as two columns; round half-up (all products here are integers). Maintenance row uses the NYC hub base ($2,400–$9,000/yr) because the Brooklyn row includes an LED-volume SLA that does not apply on the island.
- Base rows → Nassau / Suffolk: 2×2 LCD 12,000–18,000 → 13,800–20,700 / 14,400–21,600; 3×3 LCD 24,000–38,000 → 27,600–43,700 / 28,800–45,600; 4×4 LCD 42,000–65,000 → 48,300–74,750 / 50,400–78,000; 2.5 mm dvLED 35,000–55,000 → 40,250–63,250 / 42,000–66,000; 1.9 mm dvLED 55,000–85,000 → 63,250–97,750 / 66,000–102,000; 1.5 mm dvLED 85,000–140,000 → 97,750–161,000 / 102,000–168,000; outdoor LED per m² 4,500–8,500 → 5,175–9,775 / 5,400–10,200; controller 2,500–15,000 → 2,875–17,250 / 3,000–18,000; 16×16 HDMI matrix 4,500–12,000 → 5,175–13,800 / 5,400–14,400; mounting structure 1,500–9,000 → 1,725–10,350 / 1,800–10,800; CMS 1,200–5,000/yr → 1,380–5,750 / 1,440–6,000; maintenance 2,400–9,000/yr → 2,760–10,350 / 2,880–10,800.
- Service/callback (protected): $195/hr, 3-hour minimum ($585) — not on the initial install.
- No published BYOE (labour-only) rate exists in the silo → page says BYOE is quoted after the survey; FLAGGED.

---

## 4. Question register

Every FAQ/Q&A question on each page of the silo, so no later page repeats an intent. The 15 not-yet-rebuilt pages are recorded as their intent clusters (full lists can be regenerated with the extraction snippet in the batch notes); the rebuilt page is listed in full.

### Intents already used by the old-template pages (do not reuse on rebuilt pages)
Coverage ("do you install across all of X?"), cost in X, install duration, lead time, pixel pitch for a ballroom/loft/sports bar/tasting room, electrical needed for a 3x3 wall, power draw of a 3x3 LED wall, replacing projection in a sanctuary, DJ lighting/DMX sync, booking-conversion for catering halls, named-venue questions (Yankee Stadium, Industry City, Barclays, IBM, CIA, Woodbury Common, Empire Outlets, St. George Theatre, Villa Barone, Grandview, Revel 32…), hospitals, houses of worship, COI handling, after-hours work in occupied Class A buildings, glass curtain walls that can't take load, brands installed, warranty, how to get a quote, who installs video walls, what is a video wall, where in X, when to budget, why X is priced as it is, how to plan, relocating a wall, which industries use walls, content management after install ("How do I run content on the wall"), multi-day wedding content, single-panel failure ("What happens when one panel dies", "if a panel fails during an event"), replace vs upgrade, salt air on outdoor LED, Montauk/East End travel premium, seasonal storage for Hamptons venues, barn conversions, outdoor LED for wineries, content production for wineries, member-only country clubs, Stony Brook installs, North Fork tasting room pitch, union venues, LED volumes.

### video-wall-installation-long-island (rebuilt 2026-10-18)
Q&A (H3):
1. Our reception area is only about 12 feet deep — will the lines between LCD panels bother people standing that close?
2. Is a 2×2 of commercial panels really better than one 98-inch display?
3. Our only way in is a standard door and a stairway — does that rule out a big wall?
4. Our offices are metal studs and drywall — what has to happen before a video wall mount goes up?
5. Can the wall go on a partition we share with the tenant next door?
6. How far will the finished wall stick out into a corridor, and why does that matter?
7. Who is allowed to wire the outlets behind the wall — and is it different in Suffolk and in a Nassau town?
8. Does the room need extra cooling once the wall and its processor are running?
9. If the wall faces the street through our window, does the town treat it as a sign?
10. Do we need a separate computer to drive the wall, or can the panels handle it themselves?
11. Can one wall show the cameras, a news channel and a sales dashboard at the same time?
12. How do we stop a logo or a ticker from leaving a ghost on the panels?
13. What can you check from Brooklyn before anyone drives out east?
14. Our building loses power in storms — what protects the wall when service comes back?
15. Can we use the TVs we already bought?
16. Who keeps the passwords, content files and drawings when the job is done?

FAQ (accordion + FAQPage):
1. Can a video wall be mounted in portrait, with the panels standing tall?
2. Is there a size below which you would tell us not to build a wall?
3. Do you install video walls in homes — a basement media room or a game room?
4. We bought an LED wall kit online — will you install equipment we supplied?
5. What does the site survey involve, and does it cost anything?
6. How do you protect finished floors, ceilings and furniture during the work?
7. Can the wall brighten and dim itself as daylight changes?
8. Can the wall show captions so people can follow it with the sound off?
9. We lease our space — do we need the landlord's sign-off first?
10. Can the wall switch itself on at opening and off at closing?

---

## Long Island

Local research for the Long Island hub (Nassau + Suffolk). Thesis used on the page: on the island a video wall is usually the first one in the building — bought by a business with no AV department, hung on a suburban wall (steel-stud office partitions, block, shared tenant walls, storefront glass), powered under two different electrical-licensing systems, and serviced across a long island from a Brooklyn base; so the page is about choosing LCD vs LED by honest viewing distance, proving the wall and the circuit before the panels, and setting up remote health checks.

| Query · platform | URL | Finding | Page + section used |
|---|---|---|---|
| `"video wall" Long Island Newsday OR LIBN OR Patch Hauppauge OR Melville OR Uniondale` · Firecrawl → scrape | https://www.waldners.com/portfolios/newsday/ | Newsday HQ, Melville: AV for 35 conference rooms, "video walls in three areas": Planar 3×5 in the newsroom, Planar 8×10 in the auditorium, Planar 2×2 in reception (Waldner's portfolio, modified 2022-07-07) | The Island facts list; Coverage card "Melville / Route 110" |
| same → scrape | https://libn.com/2016/10/21/out-with-the-old/ | LIBN 2016-10-21 (David Winzelberg): renovated Nassau Coliseum's 4,100 sq ft VIP Club planned "two bars and a large video wall display" | Coverage card "Uniondale"; Commercial (hospitality) |
| same → scrape | https://patch.com/new-york/longisland/smittys-all-american-grill-perfect-location-your-next-event-0 | Patch Long Island Neighbor News 2016-06-15: Smitty's All American Grill, Riverhead, "their 21-foot video wall" used for fundraisers and events (author's own post) | Commercial (Route 58/Riverhead card — sports bar) |
| `Hauppauge Industrial Park number of businesses employees` · Firecrawl | https://rpa.org/work/reports/hauppauge-industrial-park-economic-opportunity-analysis | RPA: 1,300 companies, 55,000+ employees, just over 2 square miles, ~1 in 20 Long Island jobs | The Island facts list; Commercial card Hauppauge; Coverage |
| same | https://www.hia-li.org/business-grows-here-profiles/ | HIA-LI calls it the Long Island Innovation Park at Hauppauge | Commercial card naming |
| `Route 110 corridor Melville office space` · Firecrawl | https://libn.com/2016/06/24/melville-makeover/ | LIBN: proposed complex "would add about 1 million square feet of office space to the Route 110 corridor" | Commercial card Route 110 (context only, no figure quoted) |
| `UBS Arena Belmont Park LED video board size center-hung` · Firecrawl | https://investor.daktronics.com/news-releases/news-release-details/ubs-arena-selects-daktronics-install-45-hdr-capable-led-displays | Daktronics: UBS Arena, 45 HDR-capable LED displays; centerhung of 12 LED displays totalling 4,730 sq ft | AI check ("arena boards are not what a business buys"); Coverage card Elmont |
| `Stony Brook University OR Hofstra OR Northwell "video wall" installed` → scrape · Firecrawl | https://sbmatters.stonybrook.edu/transforming-spaces-new-frey-hall-video-wall-inspires-students/ | Stony Brook Matters 2025-02-21: Frey Hall lobby video wall, 6 ft 6 in × 12 ft, installed over winter break by campus CPDC electricians/carpenters/painters with DoIT engineering, "on a reduced budget of under $40,000 in just a few weeks" | Coverage card Stony Brook; AI check (cost) — stated as the university's own figure |
| same | https://www.avnetwork.com/systems-contractor-news/suny-stony-brook-monitors-campus-with-hiperwall-visualization | AVNetwork 2017-04-04 (excerpt): Stony Brook campus monitoring "3-by-2 video wall comprised of 55-inch NEC no-bezel displays" running Hiperwall | Q&A multiviewer (operations rooms) |
| `Suffolk County Police Real Time Crime Center video wall Yaphank` → scrape · Firecrawl | https://scpdshield.org/Initiatives | Suffolk Crime Analysis Center at SCPD HQ, Yaphank, part of the NYS DCJS network; "features a video wall that displays footage from countywide surveillance cameras" | Coverage card Yaphank; Q&A multiviewer |
| same | https://nypost.com/2025/01/26/us-news/suffolk-county-reveals-crown-jewel-of-cutting-edge-ny-police-tech-network/ | NY Post 2025-01-26 (excerpt): photo caption "A giant video wall in the Suffolk Crime Analysis Centre in Yaphank" | Coverage (supporting) |
| `PSEG Long Island number of customers` · Firecrawl | https://www.psegliny.com/ | LIPA/PSEG LI: "more than 1.2 million customers across Long Island and the Rockaways" | The Island facts; Q&A storms |
| `Northwell Health largest private employer` · Firecrawl | https://en.wikipedia.org/wiki/Northwell_Health ; https://www.northwell.edu/about-northwell | Northwell: New York State's largest health care provider and private employer, 104,000-plus employees (Northwell's page), HQ 2000 Marcus Ave, Lake Success/New Hyde Park | Commercial (healthcare); Coverage card Lake Success |
| `RXR Plaza Uniondale office square feet; Roosevelt Field mall` · Firecrawl | https://marketplace.vts.com/building/rxr-plaza-uniondale-ny ; https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) ; https://libn.com/2024/02/27/roosevelt-field-to-expand-with-new-medical-office-project/ | RXR Plaza: two 15-story glass office towers, 625 RXR Plaza, Uniondale. Roosevelt Field: mall in the East Garden City section of Uniondale; LIBN 2024: 90,000 sq ft three-story medical office building planned south of the mall's south parking deck | Commercial cards (Uniondale/East Garden City) |
| `Smith Haven Mall Lake Grove ... Walt Whitman Shops Huntington Station Route 110` · Firecrawl | https://www.stonybrook.edu/beyondthebrook/longisland/shopping.html ; https://en.wikipedia.org/wiki/Walt_Whitman_Shops | Smith Haven Mall, 313 Smith Haven Mall, Lake Grove; Walt Whitman Mall at Route 110 and Jericho Turnpike, Huntington Station (South Huntington hamlet) | Commercial (retail corridors) |
| `Hofstra University video wall` · Firecrawl | https://bulletin.hofstra.edu/content.php?catoid=147&navoid=28223 | No Hofstra video wall found; a lab with "5 wall-mount LCD displays" | Not used (no video-wall fact) |
| `Suffolk County Consumer Affairs electrician license ...` → scrape · Firecrawl | https://www.suffolkcountyny.gov/Portals/0/formsdocs/labor/code.pdf ; https://ecode360.com/14948079 ; https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License | Suffolk rules for restricted electricians: a restricted category covers "all cabling systems of 90 volts or less, for computer networking, telecommunications, cable TV, fiber optics, audio and video systems and home theater systems"; "Only the holder of a Suffolk County Master Electrician's License shall do direct line-voltage connections or branch circuit feeder connections to a service panel…" (Ch. 563 Art. XI). Consumer Affairs also issues Master Electrician, Restricted Electrical, Home Improvement and Sign Hanger licences | Q&A licensing; Commercial compliance list; Two Counties |
| `Town of Hempstead electrical license board of electrical examiners` · Firecrawl | https://ecode360.com/15509840 ; https://hempsteadny.gov/496/Examining-Board-of-Electricians ; https://cinderblock.com/blog/electrical-contractor-license-new-york/ | Town of Hempstead Code ch. 84: Examining Board of Electricians licenses master electricians. Secondary (Cinderblock): Hempstead, North Hempstead and Oyster Bay each keep their own examining board | Q&A licensing; Two Counties |
| `Nassau County electrical license Department of Consumer Affairs ...` · Firecrawl | https://www.nassaucountyny.gov/1563/Licensing-Registrations ; https://www.nassaucountyny.gov/1547/Consumer-Affairs | Nassau Consumer Affairs (516-571-2600) licenses home improvement businesses (one of its largest categories) and electronic/home appliance repair (21-28). Page bodies did not render in scrape — excerpts only | Commercial compliance list (home improvement licence for residential walls) |
| `Town of Islip OR Huntington OR Brookhaven electronic message sign` → scrape · Firecrawl | https://islipny.gov/community-and-services/documents/departments/planning-development/building-division/500-sign-permit-application/file | Town of Islip sign permit, EMC requirements "for the lifetime of the sign": 45-second minimum message hold, static messages, transitions under 1 second (dissolve or instant), night brightness < 0.3 foot-candles above ambient at 60 ft via auto-dimming photocell; EMC affidavit; final inspection and electrical certificate | Q&A window-facing wall; Commercial compliance |
| Reddit r/longisland (above) | https://www.reddit.com/r/longisland/comments/19cr3bk/tv_mounting/ | DIY TV-mount advice only | Background |
| Local Reddit on video walls | — | EMPTY (no Long Island video-wall threads found in excerpts) | — |
| Yelp Long Island AV installers | — | EMPTY (not accessible in build env) | — |

### Images (Long Island hub)
Drive "AESS Website Photos" has no Video Wall folder; CompanyCam not connected. No video-wall photos exist in the repo. All soundbar-installation "display" images and low-voltage "display" images were inspected and are AI-generated (rendered techs in "Abstract Enterprise LLC" shirts, one even showing a 2×2 wall) — excluded. 11 images made from real AESS job photos and one product shot: `images/rockland-toyota-nvr-monitor.jpeg` (4 crops), `images/manhattan-deli-monitor.jpeg` (2 crops), `images/nassau-window-depot-monitor.jpeg` (1 crop, lower half only — no people, no house number), `images/network-installation/…suffolk-county…` (3), `images/nvr-installation/…exacqvision-rack-mount-server-product-photo` (1). None shows a video wall; captions say so.


---

# Part from batch run 2026-10-18 — video-wall-installation-nassau-county

# Video Wall Installation — research part: Nassau County

Page: video-wall-installation-nassau-county (REBUILD, 2026-10-18). Built by subagent; merge into research/video-wall-installation.md.
Thesis: Nassau video walls go into showrooms, mall/strip-center stores, office-park lobbies, school gyms, operations rooms and single-family homes, spread across 2 cities / 3 towns / 64 villages — so the job starts with the address (which government), the building type (commercial vs. county home-improvement law) and the wall behind the finish.

Format: exact query · platform · URL · finding · page + section used.

## Silo-level sources (this run)

- PAA — EMPTY (not accessible in build env)
- PASF — EMPTY (not accessible in build env)
- Answer the Public — EMPTY (not accessible in build env)
- Google AI Overview — EMPTY (not accessible in build env). Reality-check claims were taken from cost guides below instead (stated on page).
- Bing / DuckDuckGo suggestions — EMPTY (not accessible in build env)
- Yelp 1–3★ — EMPTY (not accessible in build env)
- Reddit (local) · "reddit longisland video wall OR "TV wall" installer Nassau recommendation" · Firecrawl search · https://www.reddit.com/r/longisland/ · no thread about video walls found → EMPTY for local Reddit.
- Reddit (trade) · "video wall installation cost per panel 2026 Angi OR HomeAdvisor OR Fixr" · Firecrawl search · https://www.reddit.com/r/CommercialAV/comments/1lxhvp0/how_to_quote_led_wall_installation/ · installers quote LED walls per tile or per crew-day (opinion) · AI Reality Check H3 "Any installer can hang a video wall".
- Cost guides · same query · https://svsolutionsusa.com/how-much-does-led-video-wall-cost/ · "$9,500 entry-level indoor to $200,000+ premium MicroLED" · AI Reality Check H3 "$5,000 to $15,000".
- Cost guides · same query · https://americanledwall.com/led-video-wall-cost/ · installed LED ~$500–$2,500/sq ft by pitch · AI Reality Check.
- Cost guides · same query · https://www.crowntv-us.com/blog/led-video-wall-cost/ · kit prices exclude structure, power, install · AI Reality Check.
- Keywords (5 layers), used on page: Service — video wall installation, LCD video wall, LED wall, video wall repair · Problem — washed-out screen near glass, panel dark, wrong input, content stopped after outage, heat · Technology — narrow-bezel LCD, direct-view LED, pixel pitch, controller, content player, HDMI matrix, pop-out mount, remote power supply · Industry — car showrooms, mall tenants, office lobbies, school gyms, operations rooms, houses of worship, bars, homes · Geographic — Nassau County, Garden City, Old Country Road, Northern Boulevard, Great Neck, Manhasset, Uniondale, Elmont, Mineola, Hempstead.

## Nassau County

- Municipal structure · "Nassau County villages towns cities how many incorporated villages building department" · Firecrawl search · https://www.ny.gov/counties/nassau · 2 cities, 3 towns, 64 incorporated villages, 60+ unincorporated hamlets · Neighborhood ¶2, facts list, QA "village or town", AI check, Field Notes, hero.
- Same query · https://www.nassaucountyny.gov/3482/Building-and-Zoning-Permits · county page lists local offices for permits · QA "village or town", facts list.
- Same query · https://nassauida.org/all-local-municipality-websites · 2 cities, 3 towns, 64 villages (corroboration) · Sources.
- Same query · https://ozgc.com/nassau-village-permits/ · "nearly every [village] runs its own building department" (third-party; used only as basis for "typically") · Neighborhood ¶2, QA.
- Census · scrape · https://censusreporter.org/profiles/05000US36059-nassau-county-ny/ · ACS 2024 1-yr: pop 1,392,438; 480,668 housing units; 79% single-unit; 81% owner-occupied · Neighborhood ¶1, facts list.
- Home-improvement law · "Nassau County Administrative Code home improvement definition license…" · Firecrawl gov search · https://archive.nassaucountyny.gov/agencies/OCA/Business/LocalLaw6-1970.html · definition: dwellings of not more than three families; exemption for licensed electricians etc. acting in their craft; licenses expire 2 years · QA "living-room video wall", facts list, FAQ basement, architecture "Nassau houses".
- https://nassaucountyny.gov/FAQ.aspx?QID=205 · governing law = Admin Code Title D 21-10 to 21-11.16 / Local Law 6-1970 · Sources.
- https://nassaucountyny.gov/FAQ.aspx?QID=128 · "Contractors who perform remodeling on residential homes in Nassau County" must be licensed · QA.
- Electrician licensing · "Town of Hempstead electrical license required electricians permit low voltage Building Department" · Firecrawl search · https://ecode360.com/9294021 · Town of North Hempstead Code Ch 2 Art IV: master electrician license issued by Commissioner of Buildings; special/limited license incl. outdoor advertising signs · QA "which licensed trade", compliance callouts.
- Same query · https://hempsteadny.gov/191/Building-Department · page points to electrician and plumber licensing information · QA "which licensed trade".
- Sign rules · "Town of Hempstead code electronic message sign…" and "Town of North Hempstead code signs electronic…" · Firecrawl web + gov search · no Nassau sign-code text retrieved → stated generally ("each village and town writes its own sign chapter"); no specific Nassau sign limit claimed. https://www.ledcraftinc.com/permits-zoning-laws-for-led-signage-what-u-s-businesses-need-to-know/ · LED signs fall under NEC Article 600 · QA "sign", compliance callouts.
- School gym wall · "Nassau County "video wall" installed (police OR county OR Hofstra…)" · Firecrawl search → scrape · https://www.nassaucountyny.gov/CivicAlerts.asp?AID=13743&ARC=14331 · July 27, 2026: Legislator Scott M. Davis secured $66,350 CRP for Hempstead UFSD toward sound system + video wall for Hempstead HS gymnasium; superintendent quote on events/athletics/community · Neighborhood ¶3, facts list, QA "school gymnasium", landmarks.
- Police operations wall · "Planar Clarity Matrix Nassau County Police Department training video wall case study" · Firecrawl search → scrape PDF · https://www.planar.com/media/sp3dofdg/planar-installation-profile_ncpd-intelligence-center.pdf · opened Oct 2021, David S. Mack Center for Training and Intelligence on Nassau Community College campus, 99,000 sq ft; 8x8 Clarity Matrix G3 LCD ~32 ft × 18 ft; integrator Adwar Video; presets/one-large-or-16-small; Remote Power Supply moves heat/noise/outlets to rack room · Neighborhood ¶3, facts list, QA "operations-room", glossary, corridors, landmarks.
- Adwar Video location · same search · https://adwarvideo.com/portfolio/ · Farmingdale AV firm; NCPD Intelligence Center (2021) in portfolio · QA "operations-room" ("a Long Island AV firm").
- UBS Arena · "UBS Arena Elmont Belmont Park center-hung videoboard LED displays" · Firecrawl search · https://investor.daktronics.com/news-releases/news-release-details/ubs-arena-selects-daktronics-install-45-hdr-capable-led-displays and https://www.nasdaq.com/press-release/ubs-arena-selects-daktronics-to-install-45-hdr-capable-led-displays-at-world-class · 45 LED displays; centerhung 12 displays totaling 4,730 sq ft; 5.9 mm pitch · facts list, corridors (Elmont), landmarks.
- Roosevelt Field · "Roosevelt Field mall Garden City square feet stores largest mall Long Island" · Firecrawl search · https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) · largest mall on Long Island · https://nassaucountytourism.com/roosevelt-field-mall/ · 630 Old Country Road, Garden City · https://www.tripadvisor.com/Attraction_Review-g47770-d2044340 · anchors + 200+ specialty stores · Neighborhood ¶1, corridors, QA landlord, landmarks.
- Northern Boulevard · "Northern Boulevard Manhasset "Miracle Mile" car dealerships…" · Firecrawl search → scrape · https://www.longislandpress.com/2026/02/17/great-neck-auto-lot-sold/ · 195 Northern Blvd auto lot sold $3.15M (closed Jan 2026), beside a luxury car dealership; Manhasset Row along Miracle Mile · corridors, landmarks, QA showroom glass.
- Uniondale / Hub · "Nassau Hub Uniondale development 2026 Coliseum site news" · Firecrawl search → scrape · https://nassauhub.com/ · BSE Global + RXR; Legislature approved Development Plan Agreement Dec 17, 2018; ~70 acres of parking lots around the Coliseum (site content dated 2019; current status not verified, so page says only what the plan described) · landmarks paragraph.
- RXR Plaza · "Nassau County office market Lake Success Marcus Avenue…" · Firecrawl search · https://www.regus.com/en/us/1176 · RXR Plaza in Uniondale near Roosevelt Field and Eisenhower Park · corridors. (Lake Success office market: no source found → removed from page.)
- Hofstra · "Hofstra University video wall OR "LED wall" installed Hempstead campus" · Firecrawl search · https://gohofstra.com/news/2023/8/29/hofstra-athletics-unveils-major-fall-facility-upgrades · soccer video board (Nevco, full-color LED) 2023 · https://bulletin.hofstra.edu/content.php?catoid=147&navoid=28223 · lab with wall-mount LCD displays · landmarks.
- Consumer Affairs location · county licensing search · https://www.nycbar.org/why-all-home-improvement-contractors-need-to-be-licensed-… · Nassau Dept of Consumer Affairs, Old Country Road, Mineola · corridors (Mineola).
- ADA · "2010 ADA Standards 307.2 protruding objects…" · Firecrawl search · https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ · 27–80 in. leading edge → max 4 in. projection · QA "1970s lobby", compliance callouts.
- E-waste · "New York State electronic waste disposal ban televisions landfill 2015…" · Firecrawl gov search · https://dec.ny.gov/environmental-protection/recycling-composting/electronic-waste-recycling/recycling-consumer-electronic-waste and https://dec.ny.gov/environmental-protection/recycling-composting/electronic-waste-recycling · disposal ban since Jan 1, 2015; free recycling for individuals, businesses <50 FTE, nonprofits <75 FTE, schools, government; larger may be charged · FAQ "old displays", compliance callouts.
- Own site: tv-mounting-prices-nassau-county.html · Nassau has no travel surcharge; parking line only Manhattan; 2-hour arrival slots 8 AM–8 PM Mon–Sun; multi-screen / video wall / after-hours quoted in writing · FAQ travel, FAQ after closing, pricing.
- Local news (Newsday/Patch) beyond the above — not separately searched; EMPTY for this run.

## Prices used (source + rule)
Brooklyn base from video-wall-installation-brooklyn.html pricing table × Nassau 1.15 (§9), round half-up:
2x2 LCD $13,800–$20,700 · 3x3 LCD $27,600–$43,700 · 4x4 LCD $48,300–$74,750 · 2.5 mm LED $40,250–$63,250 · 1.9 mm LED $63,250–$97,750 · 1.5 mm LED $97,750–$161,000 · outdoor LED $5,175–$9,775/m² · controller $2,875–$17,250 · 16x16 matrix $5,175–$13,800 · mount/custom frame $1,725–$10,350 · maintenance $2,760–$17,250/yr · CMS software $1,200–$5,000/yr (not multiplied: third-party fee, identical on Brooklyn and old Nassau pages) · service $195/hr, 3-hr min ($585).
Conflict: the OLD Nassau page listed ranges BELOW Brooklyn (e.g. 2x2 $11,500–$17,000 vs Brooklyn $12,000–$18,000), i.e. not ×1.15; old page also had a "$500 minimum job" and "3-5 year manufacturer warranty" wording — not carried over.

## Images (11; pool images/low-voltage + images/commercial-security; Queens sibling had already used 8 pool photos, so none of those are reused here)
low-voltage-installation-bronx-display-recessed-box.jpg → video-wall-installation-nassau-county-cable-fed-from-recessed-box-behind-conference-display.webp
commercial-security-systems-dutchess-secured-lobby.jpg → …-lobby-display-showing-camera-tiles-above-reception.webp
low-voltage-installation-brooklyn-retail-store-ceiling-pull.jpg → …-ceiling-cable-pull-over-store-floor-with-wall-display.webp
low-voltage-installation-dutchess-county-hero-rack-switch-config.jpg → …-laptop-on-rack-shelf-configuring-switches.webp
low-voltage-installation-bronx-idf-patch-panel-build.jpg → …-wall-mount-patch-panel-on-steel-studs.webp
low-voltage-installation-bronx-stud-rough-in-boxes.jpg → …-cable-pulled-through-stud-beside-low-voltage-box.webp
low-voltage-installation-bronx-04-metal-stud-rough-in.jpg → …-cable-fed-through-open-steel-stud-framing.webp
commercial-security-systems-bronx-integration-rack.jpg → …-terminating-rack-cables-under-camera-monitor.webp
low-voltage-installation-bronx-ceiling-speaker-conference.jpg → …-ceiling-speaker-fitted-outside-glass-conference-room.webp
low-voltage-installation-bronx-09-ceiling-access-point-drop.jpg → …-cable-drop-through-lifted-ceiling-tile.webp
low-voltage-installation-bronx-access-point-lift-install.jpg → …-scissor-lift-work-at-high-ceiling-grid.webp

## Question register — video-wall-installation-nassau-county (revised 2026-10-18 after batch overlap check vs Putnam, Queens and the LI hub register)
Questions Answered (H3):
1. How do I find out whether my building answers to a village or to the town?
2. Does Nassau County itself issue a permit for a video wall?
3. Is a living-room video wall covered by Nassau’s home-improvement license law?
4. Our building has four apartments — does the county home-improvement law still apply?
5. Which wall in a glass-fronted showroom should carry the screens?
6. Do the cables above our drop ceiling need a special rating?
7. How do we keep a showroom wall from looking dated when the models change every year?
8. When does a storefront need direct-view LED instead of tiled LCD panels?
9. Does a high showroom or gym wall need a scissor lift on site?
10. What does a school gymnasium wall need that a lobby wall does not?
11. Can the conference-room wall work with Teams or Zoom without an AV technician in the room?
12. How is an operations-room wall different from a wall built for advertising?
13. Can head office schedule what plays on walls at several Nassau locations?
14. Can a Nassau school district put a County Legislature grant toward a gym video wall?
15. Why does a Nassau wall cost more than the same wall in Queens but less than in Suffolk?
16. Can one crew handle the wall, the cameras and the door readers in a Nassau showroom?
(Equipment H3 "Online kit, national AV chain or local installer?" — comparison heading, not a FAQ.)
FAQ (visible + FAQPage, 10):
1. Is there a travel charge to reach the North Shore or the South Shore of Nassau?
2. Can the work be done after closing so a store or showroom opens on time?
3. Do you work in Glen Cove and Long Beach, which are cities rather than towns?
4. Can you price a wall from drawings while our Nassau space is still being built out?
5. Can a home video wall go above a fireplace?
6. Can you take over a wall that another integrator installed?
7. Do we need to be on site for the whole installation?
8. Can you give a rough price over the phone before anyone measures the wall?
9. What is the payment schedule for a Nassau video wall job?
10. What happens to the old displays we take down?
Removed in revision (overlapped batch-mates/hub): FAQ "Will the wall keep playing if the building’s internet goes down?", "Can a video wall go in the basement or family room of a Nassau house?", "Can one wall show the security cameras and the daily content at the same time?", "Can we reuse flat-screen TVs we already own as panels in the wall?", "What should we have ready before the site visit?"; Q&A "Who should own the logins…", "Should we keep a spare panel…", "Does a screen facing out through the shop window count as a sign?", "Which licensed trade connects the wall to power…", "What does a shopping-center landlord usually ask for…", "Will the lobby wall of a 1970s office building hold a nine-panel LCD array?", "How much heat does a wall add to a small conference room?"; showroom-glass question reworded to placement.
New sources used by revised questions: grant Q (nassaucountyny.gov CivicAlerts AID=13743), four-apartment Q (Local Law 6-1970 definition), county-permit Q (nassaucountyny.gov/3482 + Consumer Affairs), Queens/Suffolk price Q (blueprint §9 multipliers 1.05/1.20), Glen Cove/Long Beach FAQ (ny.gov county page: 2 cities outside the towns).


---

# Part from batch run 2026-10-18 — video-wall-installation-putnam-county

# video-wall-installation — Putnam County part (REBUILD 2026-10-18)

Page: `video-wall-installation-putnam-county` (rebuilt in place; was crawled-not-indexed template). Queue line: `REBUILD | video-wall-installation-putnam-county | Video Wall Installation | Putnam | up /video-wall-installation-hudson-valley | (845) 640-3835 | GBP Bronx`. GBP Bronx (#bronx, 460 E Fordham Rd). Direct line (845) 640-3835 in body, CTAs, sticky bar, form error text and schema; (800) 486-0943 only in the shared mega-nav. WhatsApp only wa.me/17186790359 (+ footer text). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell HTTP blocked. "Carried" = fetched by an earlier run in another research file (named), not re-fetched.

**Thesis:** Putnam's video walls are small, public and run by non-specialists — the county 911/EOC floor (two broken video-wall monitors replaced for ~$10,000 in March 2026), a legislature streaming from a Historic Courthouse built for trials, Carmel's streamed town board, school cafetoriums, eight busy libraries, churches and family media rooms — on a grid that goes dark town by town (Isaias: 34,150 of 38,693 NYSEG customers out), under Putnam's own Chapter 145 licensing that names audio/video cabling. So a Putnam wall is sized to the room, built for one-tile swaps with a documented spare, restarts itself after an outage (battery backup on controller/player/switch, auto power-on, power-off test at handover), and works with meeting cameras/livestreams. (Distinct from old template's wedding-venue copy; distinct from Nassau/Queens siblings.)

## Silo-level sources (this run)
| Source | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| Google PAA / PASF / Answer the Public / AI Overview | — | — | EMPTY (not accessible in build env). Page says so in §10.5 and Sources. | §10.5 intro; Sources |
| Bing / DuckDuckGo | — | — | EMPTY (not accessible in build env) | Sources |
| Yelp 1–3★ | — | — | EMPTY (not accessible in build env) | — |
| Cost guides | `how much does a video wall cost installation per panel 2025 guide` · Firecrawl search (excerpts) | https://americanledwall.com/led-video-wall-cost/ | "most installed walls run about $500 to $2,500 per square foot"; typical indoor $30k–$100k | §10.5 H3 1 |
| | same | https://www.crowntv-us.com/blog/led-video-wall-cost/ | Online P2.9 10'×5' kits ~$11,000–$15,000, hardware only; installation adds 15–30% on top of hardware | §10.5 H3 2, 3 |
| | same | https://www.szradiant.com/2025-led-video-wall-cost-guide-price-per-square-foot-installation-tips.html | "Voltage stability (±5% fluctuation max)"; install 15–30% of hardware | §10.5 H3 3, 7 |
| Reddit | same search | https://www.reddit.com/r/CommercialAV/comments/1bl6fyy/video_wall_pricing/ | "mounting structure alone could be 20k. The wall can range from 15-200 k" | §10.5 H3 5 |
| Reddit | `video wall bezel width burn-in commercial display 24/7 rated vs consumer TV video wall reddit` · Firecrawl search (excerpts) | https://www.reddit.com/r/CommercialAV/comments/1j9qccf/ ; https://www.reddit.com/r/CommercialAV/comments/zhvx41/ | Consumer TVs "will burn in, lose colors, lose brightness"; "Residential displays are rated to run significantly less time than commercial" | §10.5 H3 4 |
| Licensing claim | carried: research/fiber-optic-installation.md (Putnam) | https://adaptdigitalsolutions.com/articles/new-york-contractor-license-requirements/ | Title "New York Contractor License Requirements: None Statewide" (excerpt) | §10.5 H3 6 |
| ADA | `2010 ADA Standards 307.2 protrusion limits 27 inches 80 inches 4 inches wall mounted objects` · Firecrawl search (excerpt) | https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ | Leading edges >27" and ≤80" AFF limited to 4" projection | §8.5 bullet 4; Q&A wheelchair Q (no numbers there) |

Keywords (5 layers) used naturally: Service (video wall installation, LCD video wall, direct-view LED, video wall controller, tile replacement) · Problem (dark tile, no signal after outage, glare, livestream washout) · Technology (narrow-bezel LCD, dvLED pixel pitch, HDBaseT, media player, battery backup/UPS) · Industry (911/EOC, town board, school cafetorium, library, house of worship, home media room) · Geographic (Putnam County, Carmel, Mahopac, Brewster, Southeast, Kent, Patterson, Putnam Valley, Philipstown, Cold Spring, Garrison, Nelsonville, Route 6/22/52/301/311/9).

## Putnam County
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| V1 | `Putnam County Bureau of Emergency Services 911 center Carmel emergency operations center video wall` · Firecrawl search → scrape | https://citizenportal.ai/articles/10229410/new-york/putnam-county/putnam-county-moves-funds-to-replace-911-video-wall-screens-and-improve-backup-dispatch-capacity | Mar 10, 2026: transfers to "replace two broken video-wall monitors at the 911 center (approx. $10,000)" and upgrade equipment at sheriff's backup 911 center; backup "cannot yet host the county's full complement of dispatchers" (summary; body paywalled) | Hero; §5 para 2 + facts; §10.5 H3 4–5; §13 card; Field Notes; Sources |
| V2 | same search → scrape | https://www.putnamcountyny.gov/pcbes | 112 Old Route 6 Carmel; Enhanced 911; EOC (state, emergency services, law enforcement, highway, utilities reps aid County Executive); 911 center sole PSAP, 8 police / 7 EMS / 13 fire; 114,246 calls in 2022; fire dept addresses (Mahopac 741 Route 6; Lake Carmel 851 Route 52; Kent 2490 Route 301; Patterson; Putnam Lake; Cold Spring; Garrison; North Highlands); links "Stay Informed with Putnam Alert", NY Alert | §5 para 1–2 + facts; §8 cards; §13 card; town by town; Q&A notice Q; Sources |
| V3 | `Putnam County legislature meetings livestream Historic Courthouse Carmel audio video upgrade` · Firecrawl search → scrape (PDF, directQuote) | https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2021/July/Rules-07-20-21.pdf | Jul 20, 2021: Historic Courthouse audio "designed for court proceedings, not for meetings"; upgrades must keep historic status and be approved by the Office of Courts Administration; Town of Carmel invested ~$180,000 in livestream, six cameras, contracted operator (~$1,500/month, $350 per extra meeting); Room #318 AV quote ~$11,000; Historic Courthouse quotes $10,000 video, $11,000 audio | §5 para 3 + facts; §7 card; §8.5 bullet 5; Q&A historic-room Q, YouTube Q; §10.5 H3 3; §13 card |
| V4 | same search → scrape | https://citizenportal.ai/articles/10125659/new-york/putnam-county/legislature-debates-phased-audio-visual-upgrades-and-procedural-fixes-after-repeated-complaints-about-meeting-audio | May 18, 2026: repeated complaints about meeting audio/livestream; IT director Tom Lannon ~$10,000–$15,000 for room improvements; historic courthouse needs state permission | §5 para 3; Sources |
| V5 | same search (excerpt) | https://www.putnamcountyny.gov/legislature | County posts legislative meeting videos (YouTube live links) | §5 para 3 |
| V6 | `Town of Carmel NY town board meetings live stream video channel` · Firecrawl search (excerpts) | https://www.townofcarmelny.gov/agendacenter ; https://www.youtube.com/watch?v=LFVCrydOylw | Town Board meetings with YouTube live video links (weekly-ish 2026); Carmel Town Hall, 60 McAlpin Ave, Mahopac | §5 para 3; §13 card; Hero ("on YouTube every week") |
| V7 | `Highlands Current Philipstown town hall meeting video livestream equipment OR Haldane auditorium screen` · Firecrawl search (excerpt) | https://www.philipstown.gov/agendas_minutes_video/index.php | Philipstown "Agendas / Minutes / Video" page for Town Board etc. | Town by town (Philipstown) |
| V8 | `Mahopac OR Carmel OR Brewster school district capital project bond displays interactive panels auditorium AV 2025` · Firecrawl search → scrape | https://www.mahopac.org/page/capital-project/ | Prop 5 ($8,087,000): MHS auditorium lighting and audio systems, draperies, rigging | §7 school card; Sources |
| V9 | `Brewster Central School District C.V. Starr Cafetorium capital project Brewster Vision` · Firecrawl search (excerpts) | https://www.brewsterschools.org/departments/facilities/brewster-vision-capital-project ; .../cvs-cafetorium-existing-cafeteria-conversion ; https://www.putnampresstimes.com/post/brewster-schools-capital-project-update | Cafetorium + BHS Field House completion late Fall 2026/early Winter 2027; 13,400 sq ft addition; "cafeteria with capacity for an entire grade or as an auditorium"; approved by voters March 2023 | §7 card; Q&A cafetorium Q; §13 card; town by town (Southeast/Brewster) |
| V10 | `Putnam County NY library renovation meeting room display screens …` · Firecrawl search → scrape (PDF) | https://www.putnamcountyny.gov/images/Departments/County_Exec/sotc/2026/outsideagencies/10%20-%20PCLA%20Annual%20Report%202025.pdf | PCLA 2025: 8 member libraries; visits/programs — Mahopac 151,786/1,839; Kent 74,219/901; Putnam Valley 70,856/740; Butterfield 55,034/1,096; Garrison (Desmond-Fish) 47,927/467; Reed 47,781/495; Brewster 42,075/900; Patterson 35,510/507; "cool spaces in the summer and warm spaces in the winter" | §5 facts; Q&A library Q; Q&A notices Q; §8 cards; §13 cards; town by town |
| V11 | same search → scrape | https://news.halstonmedia.com/mahopac-news/mahopac-news/stories/reed-memorial-library-completes-historicrenovation,93769 | Aug 29, 2026: Reed Memorial kitchen renovation, $20,000 state aid (no AV content) | Not used on page |
| V12 | `Census QuickFacts Putnam` · Firecrawl scrape (directQuote) | https://www.census.gov/quickfacts/putnamcountynewyork | Pop 99,028 (V2025); housing units 38,713; owner-occupied 83.8%; median value $471,300 | §5 para 1 + facts |
| V13 | Daily Voice Isaias · Firecrawl scrape (directQuote) | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Aug 5, 2020 10:15 a.m.: NYSEG 34,150 of 38,693 out; Carmel 12,717, Kent 5,815, Southeast 5,220, Putnam Valley 5,088, Patterson 4,422, Brewster 818; Central Hudson 3,621 of 5,160 (Philipstown 2,475, Cold Spring 992, Nelsonville 154) | §5 para 4 + facts; §10.5 H3 7; town by town |
| V14 | Chapter 145 · Firecrawl scrape (directQuote) | https://ecode360.com/6607815 | Low-voltage/limited-data communications technician: 8,000 hours + exam; cabling for networking, telecom, CATV, intercom, audio/video, fiber optics, video surveillance, ≤90 V / 5 A, starting at outlet/connection installed by licensed electrician; master electrician qualified; no one may engage in the trade in the county unless licensed or registered | Hero; §5 para 4; §8.5 bullet 1; Q&A licence Q; §10.5 H3 6 |
| V15 | Consumer Affairs · Firecrawl scrape (directQuote) | https://www.putnamcountyny.gov/consumer-affairs | Electrical Board licenses Master/Special/Reciprocal Electricians, Limited Data Communication Technicians, Journeymen, Helpers; lists of licensed master electricians and low-voltage technicians (as of Aug 11, 2026); electrical permits for Carmel, Patterson, Putnam Valley filed with those building departments; mandatory home-improvement contractor registration (insured, bonded, workers' comp) | §8.5 bullets 1–3; Q&A electrician Q; town by town |
| C1 | carried: research/intercom-repair.md B5 | putnamcountyny.gov chapter3.pdf | Brewster Main Street with Metro-North station at its terminus | §8 card (Route 22) |
| C2 | carried: research/intercom-repair.md B9 | putnamcountyny.gov chapter4.pdf | Oregon Corners, Putnam Valley | Town by town (Putnam Valley) |
| C3 | carried: research/sonos/soundbar Putnam rows | historicpatterson.org; lakeoscawana.net | Lake communities (Putnam Lake, Lake Carmel, Lake Peekskill, Lake Oscawana) | §13 "we also serve"; town by town |

Reddit (Putnam-specific video wall / AV): EMPTY. Local news on Putnam video walls beyond V1: EMPTY.

## Prices used (all from the old video-wall-installation-putnam-county.html table, unchanged)
2x2 LCD $11,000–$16,500 · 3x3 LCD $22,000–$35,000 · 4x4 LCD $38,000–$58,000 · 2.5mm dvLED $32,000–$50,000 · 1.9mm $50,000–$78,000 · 1.5mm $78,000–$130,000 · 3.9mm $43,000–$90,000 · outdoor $4,500–$8,500/sq m · controller $2,500–$15,000 · historic mounting/fab $2,000–$10,000 · CMS $1,200–$5,000/yr · maintenance $2,800–$9,500/yr · electrical sub-panel coordination $500–$1,500 · service $195/hr, 3-hr min ($585). Spares, cameras, encoders, UPS: "quoted after the site visit".
CONFLICT: these are ~0.92× the Brooklyn table, not 1.45× (e.g. Brooklyn 2x2 $12,000–$18,000 ×1.45 = $17,400–$26,100). Old page also said "$500 minimum job" and "1-year parts-only warranty on labor; 3-5 year manufacturer warranty" — not carried over.

## Question register (this page)
Q&A (H3):
1. If the original monitor model is discontinued, how do you make a replacement tile match the rest of the wall?
2. How many spare tiles should a public agency buy with the wall, and where should they be kept?
3. Can one wall show the dispatch map and a training slide deck side by side in a fire district classroom?
4. Our board meets in a room built for court proceedings. Can displays go in without changing the historic interior?
5. Will a wall of screens behind the board spoil the livestream picture?
6. Can the screens in the room show exactly what remote viewers see on YouTube?
7. Can a cafetorium wall be a lunch-menu board by day and an auditorium screen at night?
8. Can library staff with no AV training change what the program-room wall shows?
9. Can the sanctuary wall switch itself on before Sunday service and off afterwards?
10. What should the wall do when the power drops for two seconds and comes back?
11. Is a battery backup worth it for the screens themselves, or only for the controller?
12. Our building switches to a generator during outages. Will the wall survive the changeover?
13. Does Putnam County require a licence to install video wall cabling?
14. Who installs the new outlet for the wall, and who files for the electrical permit?
15. Who should hold the administrator login for the wall’s content system in a town or district office?
16. Can a lobby wall in a public building carry storm and closure notices?
17. How do volunteers get their slides onto the wall without plugging in a laptop each time?
18. Where should displays go so wheelchair users and people in the front row can see them comfortably?
19. Is a video wall sensible for a basement media room, or is one large TV better?
20. Can a wall in a seasonal lake house be left unpowered and unheated all winter?
FAQ (visible == FAQPage):
1. Can we see a full-size layout on the wall before anything is drilled?
2. Will the wall’s fans be audible during a quiet library program?
3. Can we start with four screens and add more later?
4. Does the wall need the internet to keep showing content?
5. Do you remove the old projector, screen and ceiling mount?
6. Can the wall show live captions during a public meeting?
7. Can you work from a municipal purchase order or a school bid specification?
8. What should staff check on the wall each month?
9. Who answers if the wall goes dark the evening before a meeting?
10. Will a wall work in a room with big windows facing a lake?
Plus section heading: "How Big Should a Putnam Room’s Wall Be?"

## Images (11) — source → new file (images/video-wall-installation/)
sonos-installation-cobble-hill-display-panels-on-slatted-wall → video-wall-installation-putnam-county-gloved-hands-aligning-four-panel-display-seams
sonos-installation-ditmas-park-screen-lifted-onto-wall-bracket → …-technician-lifting-flat-panel-onto-wall-bracket
sonos-installation-greenwich-village-network-rack-patch-panels-and-ups → …-equipment-rack-with-ups-at-base
sonos-installation-riverdale-screen-top-edge-gloved-hands → …-gloved-hands-at-top-edge-of-wall-display
sonos-installation-grymes-hill-flat-screen-lifted-onto-wall-mount → …-large-display-raised-to-wall-mount-under-strip-lights
sonos-installation-putnam-county-rack-switch-laptop → …-laptop-configuring-switches-in-open-rack
sonos-installation-putnam-county-wall-patch-panel-build → …-patch-panel-terminations-on-stud-wall
sonos-installation-putnam-county-tone-probe-wall-cable → …-tone-probe-tracing-cable-at-wall-opening
sonos-installation-putnam-county-conduit-box-cable-pull → …-cable-pulled-from-conduit-box-on-block-wall
sonos-installation-battery-park-city-soundbar-under-screen-on-media-console → …-touch-control-panel-on-console-below-screen
sonos-installation-park-slope-recessed-power-box-below-screen → …-recessed-power-and-data-box-behind-screen


---

# Part from batch run 2026-10-18 — video-wall-installation-queens

# Video Wall Installation — Queens (research part, REBUILD 2026-10-18)

Page: `video-wall-installation-queens.html` · up-link `/video-wall-installation-nyc` · phone (347) 434-6392 · Bronx GBP (#bronx, 460 E Fordham Rd) · area multiplier 1.05.
Thesis: a Queens display wall almost always serves several audiences at once (several scripts, several live feeds, several rule books), so the job is planning text, sources and compliance before panels.
Research tool: Firecrawl MCP (search + scrape). Shell HTTP not used.

## Silo-level findings used on this page

| Source | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| Google PAA | — | — | EMPTY (not accessible in build env) | — |
| Google PASF | — | — | EMPTY (not accessible in build env) | — |
| Answer the Public | — | — | EMPTY (not accessible in build env) | — |
| Google AI Overview | — | — | EMPTY (not accessible in build env); reality-check section tests vendor cost guides and forum claims instead, and says so on the page | AI Overview Reality Check intro |
| Bing / DuckDuckGo | — | — | EMPTY (not accessible in build env) | — |
| Yelp 1–3★ | — | — | EMPTY (not accessible in build env). (A Yelp listing for Tangram Food Hall appeared in search results — 133-27 39th Ave, 3.6★/52 — but reviews were not read or used.) | Address only: "Tangram's food hall is on 39th Avenue" |
| Reddit | "reddit menu board TVs restaurant install advice commercial display vs consumer TV burn-in" · Firecrawl search | https://www.reddit.com/r/digitalsignage/comments/1t9hnbt/ ; https://www.reddit.com/r/CommercialAV/comments/1j9qccf/ ; https://www.reddit.com/r/CommercialAV/comments/ckpm33/ | Commenters: consumer TVs not built for long static use; commercial displays rated 16/7 or 24/7 recommended; one commenter says makers cut consumer-TV warranty (e.g. to 90 days) in commercial use (unverified opinion) | Reality check H3 "Any 4K TV will do for a menu board" (claim labelled unverified) |
| Reddit | "video wall cost per panel installation 2026 Angi OR Fixr OR HomeGuide" · Firecrawl search | https://www.reddit.com/r/CommercialAV/comments/1bl6fyy/video_wall_pricing/ | Installer: "Just the mounting structure alone could be 20k" for a large wall | Reality check H3 "Mounting is a minor line item" |
| Vendor cost guide | same query | https://svsolutionsusa.com/how-much-does-led-video-wall-cost/ | "anywhere from $9,500 for an entry-level indoor wall to $200,000+ for a premium MicroLED" (2026) | Reality check H3 "starts around $9,500" |
| Vendor cost guide | same query | https://www.crowntv-us.com/blog/led-video-wall-cost/ | P2.9 10'×5' kit ~$11,000–$15,000; table lists what's not in box (structure, power circuits, install, calibration) | Reality check H3 "P2.9 kit" |
| Vendor cost guide | same query | https://americanledwall.com/led-video-wall-cost/ | Installed per sq ft: P1.5–P1.9 $1,400–$2,400; P2.5–P3 $700–$1,300 | Reality check H3 "Price it by the square foot" |
| Keywords (5 layers) | derived from sources above, no keyword tool reachable | — | Service: video wall installation Queens, digital menu board, menu wall, LCD video wall, direct-view LED · Problem: menu not updating, panel black, wrong input, feeds out of sync, text unreadable · Technology: HDMI matrix, video wall processor, HDBaseT, video-over-IP, media player, pop-out mount, zoned audio · Industry: restaurants, food halls, sports bars, retail storefronts, LIC offices, studios, campuses, houses of worship · Geographic: Queens, Flushing, Jackson Heights, Astoria, Sunnyside, Long Island City, Jamaica | Throughout; title/meta/H1/alts |

## Queens

| Topic | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| Demographics | "Queens County QuickFacts foreign born persons language other than English…" · Firecrawl search + scrape | https://www.census.gov/quickfacts/queenscountynewyork | Pop. est. July 1 2025: 2,358,182; foreign-born 47.6% (2020–24); language other than English at home 55.4% (5+, 2020–24); employer establishments 2023: 51,188; accommodation & food services sales 2022: $6,121,389k; total retail sales 2022 $23,017,871k ($10,102 per capita) | Neighborhood section paras + "Queens in numbers" list; retail sales in Architecture method para "Retail strips" |
| Languages | "Queens most linguistically diverse … Endangered Language Alliance 800 languages" · Firecrawl search | https://www.weforum.org/stories/industries-in-depth/queens-in-new-york-has-more-languages-than-anywhere-in-the-world/ | Up to 800 languages in NYC; "nowhere in the world has more than Queens" per ELA | Neighborhood para 1 + numbers list |
| Sign-language debate | "Flushing store signs English requirement Peter Koo bill…" · Firecrawl search | https://www.nytimes.com/2011/08/02/nyregion/queens-councilman-wants-english-to-dominate-store-signs.html ; https://www.qchron.com/editions/north/two-bills-all-signs-to-include-english/article_e610ae4b-45f1-5289-8b83-47be48f5ca88.html | 2011 proposal (Peter Koo, Flushing) to require signs ≥60% English (proposal only; not stated as law) | Neighborhood para 5 |
| Calorie rule | "NYC calorie labeling digital menu boards Health Code 81.50…" · Firecrawl search + scrape | https://nyc-business.nyc.gov/nycbusiness/description/calorie-posting ; https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-46371 | 15+ locations same name or owner must show calories on menus and menu boards, as noticeable as name or price; <15 not required | Neighborhood para 4; Commercial rules; Q&A calorie cluster |
| Sodium rule | "NYC sodium warning icon salt shaker…" · Firecrawl search | https://www.nyc.gov/site/doh/health/health-topics/heart-disease-choose-less-sodium.page | Chains 15+ locations: icon next to items ≥2,300 mg sodium + warning message (Board of Health, Sept 9, 2015) | Same sections |
| Added-sugar rule | "NYC added sugar warning icon chain restaurants…" · Firecrawl search | https://www.nyc.gov/site/doh/about/press/pr2025/new-added-sugars-warning-rule-goes-into-effect-2025.page | In effect Oct 4, 2025; icon + warning for qualifying items (≥50 g added sugars); ~4,000 chain restaurants; $200 summons from Jan 2026 | Same sections |
| Sign rules | "NYC zoning sign definition signs inside window…" · Firecrawl search + scrape | https://www.nyc.gov/site/buildings/safety/installing-a-sign.page | Chart by district: C1/C2 illuminated 50 sf total; C3 illuminated/flashing not permitted; advertising signs only in C6-5/C6-7/C7/C8/M; footnote: up to 3 illuminated non-flashing window signs ≤8 sf exempt; time/temperature signs not "flashing"; no permit for wall signs ≤6 sf; sign hanger ≤150 sf/300 lb, else RA/PE | Commercial rules; Q&A window cluster; FAQ on paid ads |
| Low-voltage law | "NYC DOB electrical work must be performed by licensed master electrician…" · Firecrawl search + scrape | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 | §28-105.4.7: no electrical permit for <50 V signaling/communication/data wiring by LME, special electrician or qualified person; exceptions incl. life-safety systems and any connection to a control circuit activating light, heat or power circuits (LME/special electrician only) | Commercial rules; Q&A keypad question; reality check last H3 |
| Electrical permits | same | https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-electrical.page | General electrical work by NYC Licensed Master Electrician with permit and DOB inspection | Same |
| ADA | "2010 ADA Standards 307.2 protrusion limits…" · Firecrawl search | https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ | Leading edge 27–80 in above floor: max 4 in protrusion into circulation path | Commercial rules; (FAQ on accessibility later removed) |
| Watch parties 2026 | "Queens fan zone 2026 World Cup Flushing Meadows watch party Queens bars" · Firecrawl search; 6sqft scrape | https://www.6sqft.com/where-to-watch-spain-argentina-fifa-world-cup-final-in-nyc/ (July 17, 2026) | Queens Night Market (FMCP) 30-ft LED; Queens Botanical Garden three jumbotrons; Queens Borough Hall 16×9-ft LED; Pig Beach Astoria 28-ft jumbotron, 65 TVs, Soccer Suite | Neighborhood para 3; Coverage cards; Q&A "rent a big LED screen" |
| Pig Beach | "Pig Beach Astoria Jumbotron 65 TVs…" · Firecrawl search | https://qns.com/2026/07/pig-beach-soccer-suite-world-cup/ ; https://www.cbsnews.com/newyork/news/pig-beach-bbq-queens-world-cup-watch-party/ | QNS: 28-ft jumbotron, 65 TVs; CBS: 28-ft jumbotron, 55 TVs → page says "dozens of televisions" | Neighborhood para 3; Commercial Astoria card |
| Sunnyside bar | same search | https://www.nyctourism.com/worldcup26/ (search snippet; scrape returned no text) | "Bar 43, known as the 'home of soccer in Queens'… Sunnyside" | Commercial Sunnyside card (bar not named) |
| Tangram | "Tangram Flushing mall food hall…" · Firecrawl search + Grub Street scrape | https://www.grubstreet.com/article/tangram-mall-best-food-hall-nyc.html (Apr 9, 2026); https://retail.tangramnyc.com/ ; https://m.yelp.com/biz/tangram-food-hall-flushing | Tangram = Flushing's largest mall; second-floor food court booming while other NYC food halls close; food hall at 133-27 39th Ave | Architecture card; Commercial Flushing card; Coverage card |
| New World Mall | same | https://www.newworldmallnyc.com/food-court | New World Mall has a food court (address not verified → page says "downtown Flushing") | Architecture + Commercial cards |
| Studios | "Kaufman Astoria Studios Silvercup Studios…" · Firecrawl search | https://www.costar.com/article/346088622/new-york-sharpens-pitch-to-become-major-us-soundstage-hub ; https://movingimage.org/feature/the-astoria-studio/ ; https://www.silvercupstudios.com/ | KAS 34-12 36th St, opened 1920, Sesame Street since 1992/93; Silvercup flagship 42-22 22nd St LIC, opened 1983 on bakery site, two LIC lots + Bronx | Architecture card; Coverage cards; Architecture method para "Studio campuses" (KAS 500,000+ sf, 11 stages/147,000+ sf, only backlot, first US studio on National Register; Silvercup 23 stages, ~558,000 sf, 13 at 22nd St flagship) |
| LIC offices | "Long Island City office buildings JetBlue headquarters…" · Firecrawl search | https://ir.jetblue.com/news/news-details/2012/JetBlue-New-Yorks-Official-Hometown-AirlineTM-Lands-at-New-Headquarters-in-Long-Island-City-04-04-2012/default.aspx ; https://en.wikipedia.org/wiki/One_Court_Square | JetBlue HQ 27-01 Queens Plaza North (2012); One Court Square 50-story office tower | Architecture + Commercial cards |
| Jamaica | "downtown Jamaica Queens Jamaica Avenue business improvement district…" · Firecrawl search | https://jamaicacenter.org/ | Jamaica Ave 400+ businesses; Jamaica Center BID "largest BID in Queens"; LIRR Jamaica Station | Numbers list; Commercial + Coverage cards; Jamaica card adds June 2022 legislation merging three downtown BIDs (jamaicacenter.org news, July 31, 2023) |
| Campuses | "Queens College Flushing Kissena Boulevard…; St. John's University Queens campus Utopia Parkway" · Firecrawl search | https://www.qc.cuny.edu/a/directions/ ; https://www.stjohns.edu/queens-residential-campus | QC 65-30 Kissena Blvd, Flushing; St. John's 8000 Utopia Pkwy, between JFK and LaGuardia | Architecture card; Q&A college question |
| Local Reddit (r/Queens, r/AskNYC) | — | — | EMPTY (not searched separately; no Queens-specific thread used) | — |
| Hyperlocal (Queens Chronicle / QNS) | see Pig Beach + sign rows | qchron.com (2011 sign bills), qns.com (Pig Beach) | used only as listed | as listed |

### Prices used
Brooklyn base from `video-wall-installation-brooklyn.html` / `video-wall-installation-nyc.html` tables × 1.05: 2x2 LCD $12,600–$18,900; 3x3 LCD $25,200–$39,900; 4x4 LCD $44,100–$68,250; 2.5 mm dvLED $36,750–$57,750; 1.9 mm $57,750–$89,250; 1.5 mm $89,250–$147,000; outdoor LED/m² $4,725–$8,925. Add-ons at the site-wide published figures (same on every borough page): controller $2,500–$15,000; 16x16 HDMI matrix $4,500–$12,000; mounting/custom fab $1,500–$9,000; CMS $1,200–$5,000/yr; maintenance $2,400–$9,000/yr. Service $195/hr, 3-hr minimum ($585).
CONFLICT: the old Queens page showed the Brooklyn/NYC base figures with no 1.05 multiplier (e.g. 2x2 $12,000–$18,000) and a 3.9 mm ballroom row ($46,000–$95,000) with no Brooklyn base to multiply — 3.9 mm row dropped.

## Question register — video-wall-installation-queens

Q&A (H3):
1. How do we know a Chinese or Bengali line will still be readable from the back of the queue?
2. Should each language get its own screen, or should every screen carry both?
3. Who types the menu in each script, and who checks the characters come out right?
4. Do our dish photos need a professional photographer, or will phone pictures do?
5. Our franchise has more than fifteen locations nationally — do calories have to appear on the screens too?
6. Can the salt-shaker or added-sugar icon sit on a slide that rotates away?
7. We are a single independent restaurant in Queens — do we have to show calories at all?
8. How large can a window screen get before the Department of Buildings wants a permit?
9. Can a window display play full-motion video, or will it be treated as a flashing sign?
10. How bright does a window display have to be on a sunny Queens avenue?
11. Can one keypad behind the bar switch the lights and the screens together?
12. Mall operations will not give us their Wi-Fi password — how will the menu update?
13. Can the cable come up from the cellar in a building with apartments upstairs?
14. Can each panel show a different match, then all panels join for the big one?
15. How do customers hear one game while the other screens stay muted?
16. Why does the same goal show up seconds apart on two screens?
17. Can the layout change itself when an early match ends and an evening game begins?
18. How many cable or streaming boxes does a multi-game wall need?
19. Can a cashier mark a dish sold out without being able to change prices?
20. Can our three Queens locations share one menu design but keep their own prices?
21. Can the wall show order-ready numbers from our point-of-sale system?
22. Can a wall go up if the lease says we may not drill into the walls?
23. What happens to the wall if we move out when the lease ends?
24. Should we rent a big LED screen for one tournament instead of building a wall?
25. Can a backyard or patio screen run in the rain and the August heat?
26. Can a lobby wall show building notices and a tenant's branding at the same time?
27. Can a production office route any camera or playback feed to any monitor?
28. Can a community hall show an interpreter's translation beside the speaker for a mixed-language audience?
29. Can a college department post to its own lobby screens without filing an IT ticket each time?
30. Can a wall in a mixed-tenant building be locked so nobody changes the input with a remote?

FAQ (accordion = FAQPage):
1. Should menu screens hang above the counter or on the side wall facing the queue?
2. Can the wall show a QR code customers can scan for online ordering or delivery?
3. Can the menu show halal, kosher, vegan or vegetarian marks?
4. Can we change a price from a phone when a supplier raises costs?
5. Is it safe to mount screens above a wok station or fryer?
6. Can we add another language to the menu later without new screens?
7. Can one corner of the menu wall carry a live news channel or a game?
8. Do portrait menu screens need different mounts from landscape ones?
9. Can the screens carry paid ads for other businesses to earn extra income?
10. Can the wall run a Lunar New Year, Diwali or Eid promotion without rebuilding the menu?

Other "?" heading: "Need a Video Wall Repaired in Queens Today?" (section H2).
De-dup notes: removed/rewrote Queens questions that matched the same-batch Nassau/Putnam rebuilds in meaning (internet-down playback, content-login ownership, outlet/electrician trade split, window-screen-as-sign, live captions, old-TV removal, scheduled on/off, landlord pre-drilling requirements, one TV vs wall, wheelchair viewing, reuse old screens, security cameras on the wall, "what to have ready" checklist).


---

# Part from batch run 2026-10-18 (batch 14) — video-wall-installation-rockland-county

# Video Wall Installation — research part: Rockland County (REBUILD 2026-10-18)

Page: `video-wall-installation-rockland-county` (rebuilt in place; was crawled-not-indexed template). Queue line: `REBUILD | video-wall-installation-rockland-county | Video Wall Installation | Rockland | up /video-wall-installation-hudson-valley | (845) 640-3835 | GBP Bronx`. GBP Bronx (#bronx, 460 E Fordham Rd). Direct line (845) 640-3835 in body, CTAs, sticky bar, form error text and schema; (800) 486-0943 only in the shared mega-nav. WhatsApp only wa.me/17186790359 (+ footer text). Built by subagent; merge into research/video-wall-installation.md.

Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell HTTP not used. "Carried" = fetched by an earlier run and recorded in another research file (named), not re-fetched here.

**Thesis:** Rockland's display walls are calendar-run, unattended walls — shul zmanim/announcement walls that must switch to Shabbat and Yom Tov mode and hold it with nobody touching them (Jewish community ~92,000, ~31% of the county; Monsey 41% Yiddish at home), college and school walls on academic calendars (RCC, STAC, Dominican), Route 59 store walls under changing landlords (Palisades Center $175M foreclosure auction Feb 2026; Nanuet Town Centre redevelopment), and public-safety/training walls bought to strict specs (county RFQ-RC-2019-167, LG 2x2 for Pomona, alternates rejected; Clarkstown PD dispatch wall) — wired under Rockland's Chapter 250 system (master electrician + county-licensed electrical inspection agency whose certificate of approval is sent to Orange & Rockland). So the page is about planning the calendar first, testing it on a moved clock, and lining up the inspection path. Distinct from Putnam (outage restart/spare tile), Nassau (which government/address), Queens (multilingual menus/rules), LI hub (LCD vs LED, first wall), and from same-batch Suffolk (Hauppauge plants, East End sign codes) and Ulster (historic/landmarked buildings).

## Silo-level sources (this run)
| Source | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| Google PAA / PASF / Answer the Public / AI Overview | — | — | EMPTY (not accessible in build env). Page says so in §10.5 intro and Sources. | §10.5 intro; Sources |
| Bing / DuckDuckGo | — | — | EMPTY (not accessible in build env) | Sources |
| Yelp 1–3★ | `Rockland County "video wall"` · Firecrawl search (excerpt) | https://www.yelp.com/search?find_desc=Audio%2Fvisual+Services&find_loc=Rockland+County%2C+NY | Listing page excerpt only; no review text | EMPTY (not used) |
| Vendor claim (shul signage) | `digital zmanim display board synagogue shabbos mode automatic screen` · Firecrawl search → scrape (query mode) | https://digitalshul.com/free-services.html | "$250 setup fee for the microcomputer, plus $10 shipping"; "$0 per month"; zmanim "calculated from your shul's precise geographic coordinates, in your own time zone"; "any existing internet connection in your shul is enough" | §10.5 H3 1; §9 Q zmanim-by-coordinates; FAQ Hebrew date; thesis section |
| Same search (excerpts) | same | https://www.beezeesystems.com/ ; https://shulscreens.org/ ; https://www.shulcloud.com/shul-digital-display | Automatic zmanim boards / shul TV displays exist as a product category | Background for §6 card, §10 equipment card |
| Halachic sources | `Shabbat timer electrical appliances set before Shabbat halacha Shabbos clock` · Firecrawl search (excerpts) | https://halachipedia.com/index.php?title=Electricity_on_Shabbat ; https://www.torahmusings.com/2010/09/timers-on-shabbat-and-yom-tov/ | Halachipedia: "It is permitted before Shabbat to set a timer for lights or other electric appliances to go on or off on Shabbat." Torah Musings: "Rabbi Feinstein writes that use of timers to automatically regulate machines to perform work forbidden to Jews on Shabbat is generally forbidden" | Thesis section H3 Shabbat; §10.5 H3 2 (page defers every halachic decision to the congregation's rav) |
| Cost guide (silo, carried) | carried from research/video-wall-installation.md §3.3 (CrownTV) | https://www.crowntv-us.com/blog/led-video-wall-cost/ | P2.9 10'×5' kit ~$11k–$15k hardware only; excludes structure, power, install, calibration | §10.5 H3 6 |
| Reddit (silo, carried) | carried §3.1 | https://www.reddit.com/r/CommercialAV/comments/hvbzp0/replacing_a_single_panel_of_a_video_wall/ | "It's always possible to replace a single panel; it's just up to the end users' tolerance…" | §10.5 H3 7 |
| Pixel pitch (silo, carried) | carried §2 | https://www.planar.com/blog/2025/what-is-pixel-pitch-and-why-does-it-matter/ | Pitch × 10 ≈ viewing distance in feet | §10 equipment sub-section |
| LG panel spec (silo, carried) | carried §2 | https://media.us.lg.com/asset/bf2bb65e-9c9f-49a5-9552-d889bf118e4f/55VM5J-H-Spec-Sheet.pdf | 55VM5J-H: typ. 160 W; operating 10–80% humidity | §9 Q older storefront capacity |
| LG LED spec (silo, carried) | carried §2 | https://www.lg.com/global/business/commercial-display/led-signage/indoor-led/lapa136/ | LAPA136: avg 650 W, max 1,300 W | §9 Q older storefront capacity |
| ADA (silo, carried) | carried §2 | https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ | 27–80 in leading edge → max 4 in protrusion | §8.5 bullet 5 |
| Keywords (5 layers) | derived from sources above; no keyword tool reachable | — | Service: video wall installation Rockland, zmanim board, shul display, digital signage wall, LCD video wall, direct-view LED, video wall repair · Problem: wrong zmanim after clock change, board not switching for Shabbat, tile dark, layout lost after power cut, content stopped updating, RTL text reversed · Technology: signage player, time server/NTP, controller, HDBaseT, fiber, pop-out mount, battery backup, induction loop · Industry: shuls/batei midrash, churches, catering halls, colleges, schools, dispatch/training rooms, Route 59 retail, labs/office parks, homes · Geographic: Rockland County, Clarkstown, Ramapo, Orangetown, Haverstraw, Stony Point, New City, Nanuet, West Nyack, Monsey, Spring Valley, Suffern, Pearl River, Orangeburg, Sparkill, Nyack, Pomona, Route 59, Route 303 | Throughout; title/meta/H1/alts |

## Rockland County
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| R1 | `Rockland County "video wall" New City OR Pomona OR Clarkstown OR Nyack OR Suffern` · Firecrawl search → scrape | https://www.bidnetdirect.com/new-york/county-of-rockland/solicitations/Video-Wall-Package-Bundle-LG-55VH7EAW-4P-As-Specified/0000228066 | RFQ-RC-2019-167, County of Rockland, owner org "FTC", delivery point Pomona NY; published 12/09/2019, closed 12/16/2019; LG 55VH7EAW 2x2 bundle w/ Peerless SmartMount Supreme full-service mount DS-VW775; 0.9mm bezel, 700 brightness, 1920×1080, RS232C/RJ45/IR, 86.5 mm deep, VESA 600×400, SuperSign CMS; "The Brand and Item specified is required… an alternate brand… shall be rejected"; quotes < $20,000 may be awarded on best value; insurance within five days of award; Certificate of Experience past 3 years | Hero; §5 para 3 + facts; §8 card New City/Pomona; §8.5 bullet 6; §10 equipment cards (LCD, mounts); §10.5 H3 3; §13 card; Sources |
| R2 | same search (excerpt only; Facebook not scrapable) | https://www.facebook.com/clarkstownpd/posts/chief-wanamaker-is-pleased-to-announce-the-hiring-of-police-officer-saladino-off/698190832349941/ | Clarkstown PD post: "…view the brand new video wall in our dispatch center" (post date not visible) | §5 para 3; Town by town (Clarkstown); Sources |
| R3 | `Rockland County Fire Training Center Pomona emergency operations center 911 dispatch video wall` · Firecrawl search → scrape (query) | https://www.rocklandcountyny.gov/departments/fire-emergency/contact-fire-emergency | Fire Training Center: 35 Firemen's Memorial Dr, Pomona, NY 10970 | §5 para 3; §8 card; §13 card; Sources |
| R4 | same search (excerpt) | https://rocklandsheriffny.gov/communications.html | RCSO Communications Division "the sole dispatch point for fire departments and specialty rescue teams in Rockland County" | Not used on final page (cut for length) |
| R5 | `Rockland County Jewish population percent Ramapo Monsey Census Yiddish speakers` · Firecrawl search → scrape | https://jewishvirtuallibrary.org/rockland-county | Meta description: "significant Jewish community of 92,000" | §5 para 2 + facts; Sources |
| R6 | same search (excerpts) | https://enewspaper.latimes.com/infinity/article_share.aspx?guid=f962d6ac-8e7f-4da2-9835-9fc5c9a41857 ; https://www.facebook.com/lohud/posts/nearly-a-third-of-rockland-countys-population-identifies-as-jewish/756825076455768/ | "largest Jewish population per capita of any U.S. county, with 31%, or 90,000 residents" (LA Times excerpt); lohud: 31.4% | §5 para 2 + facts ("press reports… roughly 31 percent") |
| R7 | same search (excerpt) | https://en.wikipedia.org/wiki/Monsey,_New_York | Monsey: 43.98% English at home, 41.48% Yiddish | §5 para 2 |
| R8 | `Census QuickFacts Rockland` · Firecrawl scrape (directQuote) | https://www.census.gov/quickfacts/rocklandcountynewyork | Pop. 357,397 (V2025); +5.6% since 2020; under 5 9.6%; under 18 31.1%; households 103,879; persons/household 3.22; language other than English 44.2%; retail sales 2022 $6,688,567k ($19,652 per capita) | §5 paras 1 & 4 + facts; thesis H3 household; Sources |
| R9 | `Palisades Center foreclosure auction 2026 Black Diamond West Nyack` · Firecrawl search (excerpts) | https://www.lohud.com/story/news/local/rockland/2026/02/04/palisades-center-goes-for-175m-at-foreclosure-auction-who-bought-it/88514352007/ ; https://connecticut.news12.com/2026/02/06/palisades-center-mall-foreclosure-auction-goes-for-175-million/5TQCf7BHIIywOsEqXQfQcj | Feb 4, 2026 auction, $175M; BD Palisades Holdings LLC (includes Black Diamond Management), last plaintiff in the foreclosure and only bidder | §5 para 4 + facts; §8 cards; §9 Q Palisades owner change; §13 card; Sources |
| R10 | carried: research/smart-lock-installation.md (R16) | https://en.wikipedia.org/wiki/Palisades_Center | Opened March 4, 1998; Routes 59/303 | §8 card; §13 card |
| R11 | `Nanuet Town Centre former Shops at Nanuet redevelopment apartments 2025 2026 Clarkstown` · Firecrawl search (excerpts) | https://www.lohud.com/story/news/local/rockland/2025/05/28/nanuet-town-centre-mall-could-add-280-apartments-in-rockland-county-new-york/83648817007/ ; Facebook CTWTDWYTK post | Lohud May 28, 2025: Nanuet Town Centre "could add 280 apartments"; plans incl. medical facilities, community spaces, link to Nanuet train station | §5 para 4; §9 Q Nanuet redevelopment; Town by town; Sources |
| R12 | Firecrawl scrape (query) | https://www.industrialrealtygroup.com/portfolio/icampus/ | Hudson Valley iCampus: ~2M sq ft lab/pharma manufacturing/office; 200 acres; Pfizer leased back ~1.26M sq ft and retains 507,263 sq ft + 25 acres for R&D; future "mixed-use, multi-tenant campus" | §5 para 5; §7 card; §8 card; §13 card; Sources |
| R13 | `SUNY Rockland Community College Suffern campus…` · Firecrawl search (excerpts) | https://sunyrockland.edu/about/the-college/ | Main campus Suffern; centers in Nyack (Hospitality & Culinary Arts) and Orangeburg (automotive); 5,300+ enrolled; 200,000+ visit yearly for cultural, recreational, commercial events | Thesis H3 academic; §13 card; Town by town; Sources |
| R14 | `St. Thomas Aquinas College Sparkill new building OR esports OR center 2025 2026` · Firecrawl search (excerpts) | https://stac.edu/st-thomas-aquinas-college-transformational-athletic-facilities-investment/ ; https://stac.edu/investing-in-the-future-st-thomas-aquinas-college-launches-next-phase-of-campus-transformation/ ; https://www.facebook.com/stac.edu/ | New Volleyball Center (near completion Aug 2024), Outdoor Fitness Center; 125 Route 340, Sparkill | Thesis H3 academic; §13 card |
| R15 | `Dominican University New York Orangeburg renamed university 2022 campus` · Firecrawl search (excerpts) | https://www.duny.edu/ ; https://en.wikipedia.org/wiki/Dominican_University_New_York | 470 Western Highway, Orangeburg; Regents approved name change May 17, 2022 | Thesis H3 academic; §13 card |
| R16 | Firecrawl scrape | https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits | Master Electrician licence (Ch. 250 Art. I); Electrical Inspection Agency licence (Ch. 250 Art. II); "Under Chapter 286… all individuals performing home improvement work must obtain a Home Improvement License"; applications A experience / B out-of-jurisdiction 5 yrs no complaints / C surety bond; Ch. 286 "Effective May 14, 2026"; online renewals only since April 2025 | §8.5 bullets 1, 2, 4; §9 Q Ch. 286 change; Sources |
| R17 | Firecrawl scrape (directQuote) | https://ecode360.com/26997705 | Ch. 250 Art. I (adopted 1967, amended 2012): electrical contractor = business installing wiring "for light, heat or power purposes or for signaling systems operating on 50 volts or more under the supervision of a master electrician"; no person shall engage in the business unless licensed | §8.5 bullet 1; §10.5 H3 4; §9 Q Ch. 286 (electrician) |
| R18 | Firecrawl scrape (directQuote) | https://ecode360.com/9665912 | Ch. 250 Art. II: electrical inspection businesses licensed by Director of Consumer Protection (1 yr); inspectors certified by nationally recognized program; on conformity with NEC, local ordinances and Orange and Rockland specifications, inspector issues certificate of approval with duplicate for owner and sends written notice to the supplier of electric service as required by O&R | Hero; §8.5 bullet 2; §9 Q inspection agency; §10.5 H3 5 |
| R19 | `Clarkstown building department permit required low voltage OR "building permit" Orangetown Ramapo Haverstraw Stony Point building inspector` · Firecrawl search (excerpt table) | https://swisny.com/coverage-area/ | State Wide Inspection Services coverage table: Clarkstown "Bldg Required - Electrical varies"; Town of Haverstraw "Elec Required for Elec Work and Bldg Required for Additions/Structural Work"; Village of Haverstraw "Bldg Required Elec May Vary"; Orangetown "Building Permit ONLY Required"; Ramapo "Elec Required and Bldg Required for Deck, depends on Job Details"; Stony Point "Requires a Bldg permit/Elect permit Required for New Work" | §9 Q five towns; Town by town; §10.5 H3 5; Sources (third-party; page says "one inspection agency… publishes a table" and to confirm with the building department) |
| R20 | carried: research/*.md row RK-C2 (excerpt) | https://www.rocklandcountyny.gov/departments/buildings-codes | County Office of Buildings and Codes administers/enforces the NYS Uniform Code and Energy Code within the Village of Spring Valley | §8.5 bullet 3; §9 Q Spring Valley; Town by town |
| R21 | carried: research (soundbar Rockland B4 / fiber Rockland) | https://longisland.news12.com/2026/04/15/tempers-flare-tuesday-night-as-rockland-county-re-writes-contractor-licensing-rules/5PDORDgg6n88VIk8Oa0c0F | Legislators scaled back HIC licensing; HICs licensed since 1986 | §9 Q Ch. 286 change; Sources |
| R22 | carried: research (fiber Rockland) | https://www.reddit.com/r/Rockland/comments/1smf4xk/no_more_licensed_rockland_contractors/ | Excerpt: "apparently I can register myself as a Home Improvement Contractor without any training?" | §9 Q Ch. 286 change (local Reddit) |
| R23 | carried: research (fiber Rockland, ecode 9666538) | https://ecode360.com/9666538 | Ch. 286 exclusions include electrical work | §9 Q Ch. 286 ("licence does not cover connecting to house wiring") |
| R24 | `Orange and Rockland Utilities number of customers Rockland County electric` · Firecrawl search (excerpt) | https://www.oru.com/en/about-us/media-center/corporate-facts | O&R and Rockland Electric Co. serve ~300,000 electric customers in NY and northern NJ; 130,000+ gas | §5 facts |
| R25 | `Nyack village Main Street… Haverstraw village waterfront redevelopment 2026` · Firecrawl search (excerpts w/ content) | https://www.nyack.gov/DowntownRevitalizationInitiative | May 14, 2026: $4.5M Nyack DRI projects; Small Project Fund $540,000 "revitalizing building facades, upgrading building interiors, purchasing permanent equipment or installing public art"; branding/wayfinding $450,000; Hopper House $305,000; waterfront restaurant $1.25M; Village Hall 9 N. Broadway | §8 card Nyack/Haverstraw; §9 Q Nyack grant; Sources |
| R26 | same search | https://dos.ny.gov/news/13-million-downtown-revitalization-initiative-mixed-use-housing-haverstraw | Oct 7, 2026: groundbreaking of $13M Village Square, 61 units, café and community space, $1.67M DRI; other DRI projects: Chair Factory trail, façade fund, basketball courts at Haverstraw Center, four murals, Haverstraw Brick Museum expansion; Haverstraw = Mid-Hudson DRI winner round five (2022) | §8 card; Town by town (Haverstraw); Sources |
| R27 | carried: research (fiber Rockland geographic list; ny.gov/counties/rockland) | https://www.ny.gov/counties/rockland ; https://explorerocklandny.com/about/communities/ | Five towns and hamlet/village names (New City county seat, Congers, Valley Cottage, Bardonia, Blauvelt, Tappan, Piermont, Airmont, Hillburn, Sloatsburg, Pomona, Garnerville, Thiells, Tomkins Cove) | §13 "we also serve"; Town by town |
| — | Local Reddit on video walls / AV in Rockland | — | EMPTY (no Rockland video-wall threads found) | — |
| — | Local news on Rockland video walls beyond R1/R2 | — | EMPTY | — |
| — | Garner Arts Center "video wall installation" (art piece, nyacknewsandviews 2021) | https://nyacknewsandviews.com/blog/2021/10/weekly-recommendations-garner-arts-center-fall-art-crawl/ | An artwork, not a display installation | Not used |

## Prices used (rule for this batch: Brooklyn base × Rockland 1.30, round half-up)
Base = `video-wall-installation-brooklyn.html` pricing table. Wall configurations ×1.30 (all products integers): 2x2 LCD $15,600–$23,400 · 3x3 LCD $31,200–$49,400 · 4x4 LCD $54,600–$84,500 · 2.5mm dvLED $45,500–$71,500 · 1.9mm dvLED $71,500–$110,500 · 1.5mm dvLED $110,500–$182,000 · outdoor LED $5,850–$11,050 per sq m.
Unmultiplied (same figure on every page / third-party): controller $2,500–$15,000 · 16x16 HDMI matrix $4,500–$12,000 · mounting structure/custom fab $1,500–$9,000 · CMS $1,200–$5,000/yr · maintenance $2,400–$9,000/yr (old Rockland page and NYC hub figure; Brooklyn's $2,400–$15,000 includes an LED-volume SLA, as noted in the LI hub research) · service $195/hr, 3-hr min ($585). Dropped: Brooklyn LED-volume rows (not applicable).
CONFLICT: old Rockland page showed ~0.92× Brooklyn (2x2 $11,000–$16,500 … 1.5mm $78,000–$130,000), a 3.9mm "riverfront ballroom" row ($43,000–$90,000) with no Brooklyn base (dropped), Rockland-only add-ons with no base ("volunteer tech team training (sanctuary) $800–$2,500", "riverfront IP65 modifier $1,500–$3,500" — dropped), a "$500 minimum job" line (not carried), and a footer CTA showing **(347) 934-8335** (wrong for an HV page; not carried). Maintenance discrepancy: Nassau rebuild multiplied Brooklyn's $2,400–$15,000 row; this page keeps $2,400–$9,000 unmultiplied (LI-hub/Queens convention) — flag for Anwar.

## Images (11) — source → new file (images/video-wall-installation/)
Pool: images/sonos-installation/ — nearly every display-related shot in it is the same underlying image as one already used on the LI/Nassau/Putnam/Queens/Suffolk pages (checked by ORB feature matching against every file in images/video-wall-installation/ and by eye), so 3 unused sonos shots were taken and the rest topped up from images/network/. Faces cropped out; no readable documents.
1. sonos-installation/sonos-installation-astoria-brick-wall-weatherproof-enclosure.webp → video-wall-installation-rockland-county-gloved-hands-drilling-weatherproof-enclosure-on-brick-wall.webp
2. sonos-installation/sonos-installation-putnam-county-fiber-fusion-splicer.webp → …-fusion-splicer-joining-fiber-beside-patch-panel.webp
3. sonos-installation/sonos-installation-rockland-county-dining-room-ceiling-speaker.webp (cropped right/top) → …-ceiling-speaker-fitted-above-restaurant-dining-room.webp
4. network/network-installation-hudson-valley-network-drop-conduit-emt-riser.webp (right half) → …-emt-conduit-riser-on-block-wall-beside-doorway.webp
5. network/network-installation-rockland-county-jhook-ceiling-pathway-bundles.webp (crop) → …-blue-cable-bundles-carried-in-j-hooks-under-open-roof.webp
6. network/network-installation-long-island-idf-riser-cable-bundle.webp (right part) → …-cable-bundle-dropped-down-corridor-wall-from-ceiling.webp
7. network/network-installation-rockland-county-core-drill-cmu-wall-penetration.webp (right part) → …-core-drilling-block-wall-for-cable-pass-through.webp
8. network/network-installation-westchester-county-finished-network-rack-firewall-ups.webp (left part) → …-finished-equipment-rack-with-battery-backup-at-base.webp
9. network/network-installation-rockland-county-managed-poe-switch-rack-install.webp (left/top) → …-network-switch-slid-into-rack-below-patch-panels.webp (hero)
10. network/network-installation-rockland-county-retrofit-wall-fish-data-drop.webp (right part) → …-cable-fished-to-wall-opening-from-reel.webp
11. network/network-installation-rockland-county-workstation-data-outlet-termination.webp (right part) → …-terminating-jack-in-wall-plate-beside-spare-plates.webp
(All network-installation-<area>-<shot>.webp files of one shot are byte-identical across areas, so the de-dup key is the shot name, not the area.)

## Question register — video-wall-installation-rockland-county
Q&A (H3, §9, in five H3 cluster headings: Walls That Run Through Shabbat and Yom Tov · Campus, Training and Dispatch Rooms · Route 59 Stores and a Changing Mall · Licensing, Inspection and Paperwork in Rockland · Homes and Families · Nyack, Haverstraw and the River Villages):
1. Can a shul board switch from weekday times to the Shabbat schedule on its own before candle lighting?
2. How does the screen know the zmanim for our building rather than for the county as a whole?
3. What happens to a programmed Shabbat schedule on the weekends the clocks change?
4. Can a two- or three-day Yom Tov be loaded in advance as one block?
5. Our sanctuary has a mechitza. How do both sides get a clear view of the screens?
6. Will Hebrew and Yiddish text come out right-to-left on a signage player, or reversed?
7. Will your technicians schedule around Shabbat, Yom Tov and the chagim?
8. Can a campus wall follow the academic calendar without being reprogrammed every term?
9. Can a training-room wall keep a record of what was on screen during a drill, for the review afterwards?
10. Can a wall be built in a room that has to stay staffed around the clock?
11. Our store is in the Palisades Center. Does the 2026 change of owner change who approves our display work?
12. Can a holiday-season layout be loaded weeks ahead and switch itself on by date?
13. Our Nanuet unit is part of a center being redeveloped. Should we hold off on a wall?
14. What is an electrical inspection agency, and why does Orange & Rockland care about it?
15. Do Rockland's five towns treat a new display circuit the same way?
16. Our building is in the Village of Spring Valley. Who enforces the building code there?
17. What did Rockland's 2026 rewrite of its home-improvement law actually change?
18. Is a wall-mounted screen in a family room safe around young children?
19. Does Nyack's downtown grant program cover display equipment?
20. Does an older Nyack or Haverstraw storefront have enough electrical capacity for a video wall?
FAQ (visible accordion == FAQPage, 10):
1. Can the screen show the Hebrew date and the weekly parsha automatically?
2. Should a lobby wall in a building used on Shabbat have a motion sensor that wakes it?
3. How should staff clean the screens without damaging them?
4. Can the screen count down to the next minyan or to candle lighting?
5. What stops someone outside the building from putting their own content on the wall?
6. Why do some LED walls show lines or flicker when guests film them on a phone?
7. Can the wall display donor recognition or dedication panels?
8. Can you work around a school's or a college's exam weeks and quiet periods?
9. Does our IT person need to be on site on installation day?
10. Will a video wall interfere with our hearing loop or assistive listening system?
Other "?" headings: CTA H2 "Planning a Wall Before the Yamim Noraim, a New Term or the Holiday Season?"; final H2 "Wall Showing the Wrong Times or No Picture? Call the Rockland Line".
De-dup notes (removed during build after comparing with the LI/Nassau/Putnam/Queens registers and the same-batch Suffolk and Ulster drafts): 24/7 panel lifespan (Suffolk has panel lifespan), overflow-room feed (Ulster lobby stage feed), indoor humidity by the river (Suffolk beach-house humidity), hiring-check for HIC licence (Suffolk licence verification), wall sound into existing speakers (Suffolk sound/speakers), hiding a home wall in cabinetry (Suffolk millwork), before/after final inspection sequencing (Ulster pre-ceiling fit-out), simcha slideshow upload (Putnam volunteers' slides).


---

# Part from batch run 2026-10-18 (batch 14) — video-wall-installation-suffolk-county

# Video Wall Installation — research part: Suffolk County

Page: `video-wall-installation-suffolk-county` (REBUILD 2026-10-18, rebuilt in place). Queue line: `REBUILD | video-wall-installation-suffolk-county | Video Wall Installation | Suffolk | up /video-wall-installation-long-island | (631) 407-2884 | GBP Brooklyn`. Brooklyn GBP (#brooklyn, 1282 Troy Ave). Direct line (631) 407-2884 in body, CTAs, sticky bar, form error text and LocalBusiness schema; (800) 486-0943 only in the shared mega-nav. WhatsApp only wa.me/17186790359 (+ footer text). Multiplier 1.20.
Format (v2.3 §12.4): exact query · platform · URL · finding · page + section used. Tool: Firecrawl MCP search/scrape (`mcp__Firecrawl__*`). Shell HTTP not used. "Carried" = fetched by the LI hub / Nassau / Putnam run and recorded in research/video-wall-installation.md, reused, not re-fetched unless noted.

**Thesis:** Suffolk is one county that behaves like three markets — the west (Route 110 / Hauppauge park: plants and office HQs, long-hour walls on IT-managed networks), the middle (Stony Brook, BNL, Yaphank, MacArthur: institutions with in-house trades and purchasing rules) and the East End (seasonal homes and shops under strict town sign codes) — under one exposed PSEG grid and a county electrician licensing article that stops at towns/villages with their own licensing law. So the wall is specified from the hours of use, the season, the network and the approving office before the hardware.

## Silo-level sources (this run)
| Source | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| Google PAA / PASF / Answer the Public / AI Overview | — | — | EMPTY (not accessible in build env); page §10.5 says so | §10.5 intro; Sources |
| Bing / DuckDuckGo | — | — | EMPTY (not accessible in build env) | Sources |
| Yelp 1–3★ | — | — | EMPTY (not accessible in build env) | — |
| Reddit (local, Suffolk video walls) | — | — | EMPTY (no Suffolk thread found; LI hub run also found none) | Sources |
| Reddit (trade) — carried | LI hub §3.1 | https://www.reddit.com/r/CommercialAV/comments/1bl6fyy/video_wall_pricing/ ; https://www.reddit.com/r/CommercialAV/comments/1j9qccf/ | "mounting structure alone could be 20k"; consumer TVs' convection cooling only works landscape | §10.5 H3 3, 4 |
| Cost guides — carried | LI hub §3.3 / Queens | https://americanledwall.com/led-video-wall-cost/ ; https://svsolutionsusa.com/how-much-does-led-video-wall-cost/ ; https://www.crowntv-us.com/blog/led-video-wall-cost/ | $500–$2,500/sq ft; $9,500–$200,000+; P2.9 10'×5' kit ~$11–15k hardware only | §10.5 H3 1, 2 |
| Pitch rules — carried | LI hub §2 | planar.com blog; christiedigital.com; barco.com | pitch×10 ft; 1 m per mm; distance/2 | §10.5 H3 2, 5 |
| Samsung consumer vs commercial — carried | LI hub §2 | https://insights.samsung.com/2024/10/21/why-you-shouldnt-use-consumer-tvs-for-commercial-digital-signage/ | ~8 h/day design; commercial use voids warranty | Equipment para; §10.5 H3 4 |
| LG 55VM5J-H sheet — carried | LI hub §2 | https://media.us.lg.com/asset/bf2bb65e-9c9f-49a5-9552-d889bf118e4f/55VM5J-H-Spec-Sheet.pdf | 0–40 °C, 10–80 % humidity, "Crestron inside" | Q&A plant-floor heat; Q&A beach-house humidity; FAQ Crestron |
| ADA 307.2 — carried | LI hub §2 | https://www.access-board.gov/ada/guides/chapter-3-protruding-objects/ | 27–80 in → max 4 in protrusion | §8.5 compliance bullet |
| NYS e-waste — carried | Nassau part | https://dec.ny.gov/environmental-protection/recycling-composting/electronic-waste-recycling | disposal ban since Jan 1 2015 | §8.5 bullet |
| "No statewide license" claim — carried | Putnam part | https://adaptdigitalsolutions.com/articles/new-york-contractor-license-requirements/ | title "None Statewide" (excerpt) | §10.5 H3 6 |

Keywords (5 layers) used naturally: Service — video wall installation Suffolk County, LCD video wall, direct-view LED wall, video wall repair, production/data wall · Problem — dust and heat on plant floors, seams through charts, window-sign violation, damp unheated houses, surge on cable lines, compressor flicker, dark tile · Technology — 24/7 vs extended-hours panels, native-resolution processor, pixel pitch, pop-out mount, guest network/casting, touch overlay, Crestron/Control4, surge protection, battery backup · Industry — manufacturers, corporate HQs, universities, labs, public agencies, outlet/big-box retail, bars and theaters, seasonal homes · Geographic — Suffolk County, Hauppauge, Melville, East Farmingdale, Route 110, Stony Brook, Upton, Yaphank, Ronkonkoma, Islip, Bay Shore, Patchogue, Riverhead, Route 58, Southampton, Hampton Bays, Sag Harbor, East Hampton, Montauk, Southold, Greenport, Shelter Island.

## Suffolk County
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| S1 | `Suffolk County New York QuickFacts population housing units` · Firecrawl search (excerpt) | https://www.census.gov/quickfacts/suffolkcountynewyork | Housing units July 1 2025 (V2025): 583,777 | §5 para 1; numbers list |
| S2 | same search → scrape (directQuote) | http://censusreporter.org/profiles/05000US36103-suffolk-county-ny/ | pop 1,535,909; 582,899 units; 87 % occupied; owner-occupied 83 %; single unit 86 %; median value $626,300 | §5 para 1; numbers list |
| S3 | same search (excerpt) | https://en.wikipedia.org/wiki/Suffolk_County,_New_York | land 912 sq mi; 2025 est. 1,546,090 | §5 para 1 ("a little more than 900 square miles", "roughly 1.5 million") |
| S4 | scrape (directQuote) | https://www.ny.gov/counties/suffolk | easternmost county; 10 towns: Babylon, Brookhaven, East Hampton, Huntington, Islip, Riverhead (county seat), Shelter Island, Smithtown, Southampton, Southold | §5 para 1; numbers list; Town by Town |
| S5 | `Town of Southampton seasonal housing units percent vacant seasonal use East Hampton census` · Firecrawl search → scrape (directQuote) | https://www.ehamptonny.gov/DocumentCenter/View/28279/Route-114-Affordable-Housing-Market-Study-and-Update | "East Hampton - Market Assessment - 3.16.26" (interim draft): study-area 2023 year-round pop 54,081; 44,227 housing units; 20,952 (47 %) seasonal/recreational/occasional; seasonal increase "upwards of ~50,000" | §5 para 4; numbers list; Town by Town (East Hampton) |
| S6 | same search (excerpt only, not used) | https://www.27east.com/east-hampton-press/article_610622df-48d8-5b94-808f-bc8666d4c52f.html | 2010 Census vacancy shares Southampton/Bridgehampton | not used (old data) |
| S7 | `Town of Southampton code electronic signs prohibited internally illuminated sign` · Firecrawl search → scrape (directQuote) | https://ecode360.com/8702578 | Ch. 330 Art. XXII: window sign = on window/glass door or inside within four feet and visible from exterior; window signs not illuminated except §330-207B; internally lit interior signs visible from street only in Highway Business districts, ≤10 sq ft per establishment; window sign ≤4 sq ft one per street/lot; illuminated signs off by 11 p.m. or closing, whichever later; NEC conformance | §5 para 4; numbers list; §8.5 signs bullet; Q&A "four-foot rule"; Q&A "dark at 11 p.m."; Town by Town |
| S8 | same search (excerpt) | https://www.southamptontownny.gov/CivicAlerts.asp?AID=1689&ARC=3146 | "Town Targets Sign Code Violators in Hampton Bays" — window cover, signage or lighted signs in violation observed | Town by Town (Southampton) |
| S9 | `Suffolk County Department of Labor, Licensing and Consumer Affairs master electrician license restricted electrical license` · Firecrawl search → scrape ecode (directQuote) | https://ecode360.com/14948079 | Ch. 563 Art. XI: unlawful to carry on regulated trade without license; **"This article shall not be applicable within any town or village which has hereinbefore enacted legislation regulating the licensing … nor in any town of the second class which elects by local law not to have this article apply"**; master/restricted definitions; master $200/yr, restricted $100; 2-year licenses; continuing education for renewal | §5 para 5; §8.5 licensing bullet; Q&A circuit/coolers; Q&A "village licenses its own"; Q&A "confirm license"; §10.5 H3 6 |
| S10 | same → scrape (directQuote) | https://www.suffolkcountyny.gov/Portals/0/formsdocs/labor/code.pdf | DoLLCA Code of Rules: "Communications Cabling Systems — … all cabling systems of 90 volts or less, for computer networking, telecommunications, cable TV, fiber optics, audio and video systems and home theater systems"; only Master Electrician does line-voltage connections to panel/disconnect/junction box | §8.5 low-voltage bullet; §10.5 H3 6 |
| S11 | same search (excerpt) | https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License | Consumer Affairs issues Master Electrician, Restricted Electrical, Electrical Inspector, Home Improvement, Sign Hanger licenses among others | Q&A "confirm license" |
| S12 | `Tropical Storm Isaias PSEG Long Island customers without power Suffolk` · Firecrawl search → scrape PDF (directQuote) | https://www.lipower.org/wp-content/uploads/2020/09/LIPA-Isaias-30-Day-Report-Final.pdf | Aug 4 2020, gusts to 70 mph; ~645,000 customer outages; full restoration eight days | §5 para 5; numbers list; Q&A surge |
| S13 | carried (LI hub) | https://www.psegliny.com/ | >1.2 million customers | Sources list only |
| S14 | carried (LI hub) | https://rpa.org/work/reports/hauppauge-industrial-park-economic-opportunity-analysis ; https://www.hia-li.org/business-grows-here-profiles/ | ~1,300 companies, 55,000+ employees, just over 2 sq mi, ~1 in 20 LI jobs; "Long Island Innovation Park at Hauppauge" | Hero; §5 para 2; numbers list; §8 card; landmarks |
| S15 | carried (LI hub) | https://www.waldners.com/portfolios/newsday/ | Newsday Melville HQ: video walls in three areas — Planar 3×5 newsroom, 8×10 auditorium, 2×2 reception | §5 para 2; §8 card; landmarks; Town by Town (Huntington) |
| S16 | `Stony Brook University Hospital video wall …` · Firecrawl search → scrape (directQuote) | https://news.stonybrook.edu/university/transforming-spaces-new-frey-hall-video-wall-inspires-students/ | Feb 20 2025: 6′6″×12′; CPDC electricians/carpenters/painters did physical install; MSE team assembled/tuned; under $40,000; few weeks over winter break; content incl. live-streamed camera feeds | §5 para 3; numbers list; services card; Q&A split-scope; Q&A "under $40,000"; landmarks |
| S17 | `Brookhaven National Laboratory Upton employees acres about the lab` · Firecrawl search (excerpt) | https://www.bnl.gov/about/ | "The Laboratory's 3,000 staff members" | §5 para 3 |
| S18 | `Brookhaven National Laboratory video wall visualization` · Firecrawl search | bnl.gov results | No BNL video wall found → no BNL wall claimed | — |
| S19 | carried (LI hub) | https://scpdshield.org/Initiatives | Suffolk Crime Analysis Center, SCPD HQ Yaphank, "features a video wall that displays footage from countywide surveillance cameras" | §5 para 3; landmarks |
| S20 | `Long Island MacArthur Airport terminal renovation digital displays Islip 2025` · Firecrawl search → scrape | https://libn.com/2026/07/17/islip-selects-rxr-for-macarthur-airport-terminal-project/ | LIBN, David Winzelberg, July 17 2026: Fly Long Island (RXR + Avports) tapped by Islip committee; option of new north terminal with Ronkonkoma LIRR connection or expanded south terminal; town board approval needed | §5 para 3; §8 card; landmarks |
| S21 | `Tanger Outlets Riverhead Route 58 stores retail corridor` · Firecrawl search (excerpt) | https://www.tanger.com/riverhead/visitor-info | "more than 130 top brands and local shops" | §8 card; landmarks |
| S22 | same → scrape | https://riverheadlocal.com/2024/01/19/new-business-uses-at-tanger-will-hurt-downtown-and-route-58-local-developer-tells-town-board/ | Alek Lewis, Jan 19 2024: proposed Manufacturers Outlet Center zoning amendments (general retail, restaurants, furniture showrooms, recreation); Richard Israel warned of harm to Route 58 and downtown | §8 card; Town by Town (Riverhead) |
| S23 | carried (LI hub) | https://patch.com/new-york/longisland/smittys-all-american-grill-perfect-location-your-next-event-0 | 2016 Patch community post: Riverhead grill's "21-foot video wall" | landmarks (Riverhead card) |
| S24 | `Patchogue downtown revitalization Main Street Patchogue Theatre Bay Shore Main Street restaurants` · Firecrawl search (excerpt) | https://www.patchoguetheatre.org/Wheretoeat | lists Arooga's Grille House & Sports Bar, Tap Room, Village Idiot Pub, etc. | §8 card (downtowns) |
| S25 | carried (LI hub) | https://islipny.gov/…/500-sign-permit-application/file | EMC: 45-second minimum hold; auto-dimming photocell at night | §8.5 signs bullet; Town by Town (Islip) |
| S26 | own site | tv-mounting-prices-suffolk-county.html | "no travel charge to the East End"; caretaker/lockbox access practice | Basis for "no separate East End line" (§10.5 H3 7) — stated only about our video wall table |
| — | Bay Shore downtown facts | — | EMPTY (no sourced fact; named as a place only) | — |
| — | Local news on Suffolk video walls beyond S15/S16/S19/S23 | — | EMPTY | — |

## Prices used (rule: Brooklyn base × 1.20, round half-up; all products integer)
Base = `video-wall-installation-brooklyn.html` table. 2×2 LCD $14,400–$21,600 · 3×3 LCD $28,800–$45,600 · 4×4 LCD $50,400–$78,000 · 2.5 mm dvLED $42,000–$66,000 · 1.9 mm $66,000–$102,000 · 1.5 mm $102,000–$168,000 · outdoor LED $5,400–$10,200/m² · 16×16 HDMI matrix $5,400–$14,400 · mounting/custom framing $1,800–$10,800 · maintenance $2,880–$10,800/yr (base $2,400–$9,000 from the NYC hub row, as the LI hub did; the Brooklyn $2,400–$15,000 row includes an LED-volume SLA) · **not multiplied:** controller $2,500–$15,000 and CMS $1,200–$5,000/yr (same figure on nearly every silo page; CMS is third-party software) · service $195/hr, 3-hr min ($585). LED-volume rows dropped (not relevant to Suffolk). BYOE: no published figure → "quoted after the site visit".
Packages: Boardroom Four from $14,400 · Lobby Nine from $28,800 · Seamless LED from $66,000.
CONFLICTS: (1) old Suffolk page table was *below* Brooklyn (2×2 $11,500–$17,000; 3.9 mm $45,000–$95,000; outdoor $4,400–$8,200; seasonal storage $3,500–$8,000/season) — not ×1.20; 3.9 mm and seasonal-storage rows dropped (no Brooklyn base). (2) LI hub's Suffolk column multiplies the controller ($3,000–$18,000) and CMS ($1,440–$6,000); this page leaves both at base per the batch rule → hub and page differ on those two rows. (3) Old page used phone (347) 934-8335; queue line and checker require (631) 407-2884.

## Images (11) — source → new file (images/video-wall-installation/)
All from images/soundbar-installation/; none of these underlying shots appears in images/video-wall-installation/ before this run (checked visually against all 44 files). None shows a video wall; captions say "reference photo".
1. soundbar-installation-chelsea-bar-clamped-to-swing-arm-mount → video-wall-installation-suffolk-county-articulating-arm-mount-holding-flat-display
2. soundbar-installation-chelsea-reception-wall-tv-and-bar → …-reception-lounge-wall-display
3. soundbar-installation-long-island-service-van-tools (cropped to van interior; face and van lettering/phone removed) → …-van-shelving-cable-reels-ladders-tool-cases
4. soundbar-installation-brooklyn-heights-yellow-level-on-bar-bracket → …-yellow-level-on-wall-bracket
5. soundbar-installation-chelsea-cables-strapped-inside-media-cabinet → …-cables-strapped-inside-equipment-cabinet
6. soundbar-installation-chelsea-exercise-room-tv-and-wall-bar → …-fitness-room-wall-display
7. soundbar-installation-suffolk-county-wall-jack-cable-test (cropped right side; face removed) → …-cable-certifier-pass-at-wall-jack
8. soundbar-installation-chelsea-tablet-sound-check-from-sofa → …-tablet-control-check-facing-wall-display
9. soundbar-installation-chelsea-rear-speakers-on-stands-behind-sofa → …-living-room-wall-display-with-speakers
10. soundbar-installation-chelsea-unboxed-bar-bracket-and-tools → …-unboxed-mount-hardware-and-tools
11. soundbar-installation-chelsea-level-on-wall-hung-bar (cropped left 1150 px; standing person removed) → …-tool-bag-and-level-below-wall-display
Note: the same underlying shots exist under other area names in images/soundbar-installation/ (e.g. bayside-, dumbo-, flushing-, greenpoint-, brooklyn-heights-, long-island-, suffolk-county- variants) — siblings should not reuse those shots.

## Question register — video-wall-installation-suffolk-county
Q&A (H3):
1. Our Hauppauge plant floor has dust, vibration and forklifts — what changes for a wall out there?
2. Can a production-floor wall show machine counts without opening the factory network to the internet?
3. Should our lobby wall and our boardroom wall share one controller, or be built as two systems?
4. Will a 3×3 of 1080p panels show the fine detail in research plots and engineering drawings?
5. Our own facilities crew handles power and carpentry — can you supply and commission only the display side?
6. Is under $40,000 a realistic budget for a lobby wall the size of Stony Brook’s Frey Hall wall?
7. Will our facilities department’s mounting and cabling standards slow the job down?
8. Does the four-foot rule in Southampton’s sign code change where a screen can sit inside our shop?
9. Do displays inside a Southampton business have to go dark at 11 p.m.?
10. Can the wall be started and tested before we open the house in spring, so it works on the first weekend?
11. Can summer guests cast from their phones to the wall without joining our home network?
12. Our beach house is humid and gets sandy in summer — does that shorten a wall’s life indoors?
13. How high should the wall sit when shoppers see it from across a large store floor?
14. Can a wall go on the plaster and brick walls of an older Main Street building?
15. Our venue hosts live music and comedy — can the wall show a camera feed of the stage for the back of the room?
16. Can the wall share a circuit with the bar coolers and kitchen equipment?
17. Is a lightning or surge strike through the cable line a real risk for a wall in a waterfront house?
18. Our village licenses its own electricians — does the county license still matter there?
19. How can we confirm that an installer’s electrical or other license is current in Suffolk?
FAQ (visible == FAQPage, 10):
1. Can a video wall go on a wall that backs onto a walk-in cooler or freezer?
2. Can the panels or the frame around the wall match our interior finishes?
3. Can a video wall be mounted on a curved or angled wall?
4. How long should commercial video-wall panels last before they need replacing?
5. Does a heavy wall need drawings stamped by an engineer?
6. Can the wall play sound, or do we need separate speakers?
7. Can visitors touch the wall to explore content?
8. Can the wall be built into cabinetry or a millwork wall our carpenter is making?
9. Can you put a video wall in a sales office or temporary building on a construction site?
10. Can our existing Crestron or Control4 system run the wall?
Adjacent-intent notes (judged distinct, flag for review): Q8 vs LI hub "does the town treat it as a sign?" (this one is about placement depth under a specific code); Q10 vs Putnam "seasonal lake house unpowered all winter" (this one is spring commissioning); Q12 vs old-template "salt air on outdoor LED" (indoor humidity); Q14 vs LI hub "metal studs and drywall" (masonry/plaster); Q17 vs LI hub "power in storms" (surge via cable/data paths); Q18 vs LI hub "who may wire outlets, Suffolk vs Nassau town" (the county-article carve-out).


---

# Part from batch run 2026-10-18 (batch 14) — video-wall-installation-ulster-county

# Video Wall Installation — research part: Ulster County

Page: `video-wall-installation-ulster-county` (REBUILD in place, 2026-10-18). Built by subagent; merge into research/video-wall-installation.md.
Queue line: `REBUILD | video-wall-installation-ulster-county | Video Wall Installation | Ulster | up /video-wall-installation-hudson-valley | (845) 640-3835 | GBP Bronx`. Bronx GBP (#bronx, 460 E Fordham Rd). (845) 640-3835 in body/CTAs/schema; (800) 486-0943 only in shared mega-nav; WhatsApp only wa.me/17186790359 (+ footer text).

**Thesis:** In Ulster the building and the code decide before the screen does. The rooms people want walls in are historic or converted (1676 stone Senate House, Kingston's four historic districts, Huguenot Street stone houses, the 1927 Broadway Theatre/UPAC, Hutton Brickyards' 1928 kiln sheds, Mohonk, barns, the former IBM campus at iPark 87); Kingston bans electronic signs in its historic districts and tightly limits them elsewhere (5-min static hold, 0.3 fc, auto-dim, fail-to-black), Woodstock prohibits all internally lighted signs; the county's Electrical Licensing Law (Ch. 185) defines electrical work to include "signaling, communication, alarm or data transmission"; Central Hudson serves 93,190 Ulster customers and 7,640 were out the evening after the July 2026 storms. So Ulster walls face inward where sign rules bite, stand on reversible/floor-supported frames, and get power from an Ulster-licensed master electrician. (Distinct from Putnam civic/dispatch thesis, Nassau municipal-patchwork thesis, Queens multilingual-menu thesis, LI-hub first-wall thesis.)

Format: exact query · platform · URL · finding · page + section used. Tool: Firecrawl MCP (`mcp__Firecrawl__firecrawl_search` / `firecrawl_scrape`). Shell HTTP not used.

## Silo-level sources (this run)
- Google PAA — EMPTY (not accessible in build env)
- Google PASF — EMPTY (not accessible in build env)
- Answer the Public — EMPTY (not accessible in build env)
- Google AI Overview — EMPTY (not accessible in build env). Reality check tests claims from cost guides / manufacturer notes / forums already in the silo file (svsolutionsusa.com, crowntv-us.com, Planar/Christie/Barco, Samsung Insights 2024-10-21, r/CommercialAV 1j9qccf) — carried from research/video-wall-installation.md §2–§3, not re-fetched; page says so.
- Bing / DuckDuckGo — EMPTY (not accessible in build env)
- Yelp 1–3★ — EMPTY (not accessible in build env)
- Reddit (local) · `reddit Kingston NY OR "New Paltz" OR Woodstock digital sign OR "LED sign" OR "TV wall" business` · Firecrawl search · https://www.reddit.com/r/kingstonnewyork/ , https://www.reddit.com/r/hudsonvalley/comments/1b25j76/ · no thread about video walls/digital signs → EMPTY. Not used.
- Keywords (5 layers): Service — video wall installation Ulster County, LCD video wall, direct-view LED, stage LED wall, video wall repair · Problem — screen treated as a sign, wall can't be drilled, no ceiling void, unheated venue, outage restart, lightning/surge · Technology — floor-supported/ground-stack frame, pop-out mount, controller, media player sign-mode (static hold, fail-to-black), ambient light sensor, HDBaseT, fibre · Industry — theatres/music venues, galleries, inns/resorts/event barns, campus/training rooms, restaurants · Geographic — Ulster County, Kingston (Stockade, Rondout, Midtown/Broadway), Town of Ulster/iPark 87, New Paltz, Woodstock/Bearsville, Saugerties, Ellenville/Wawarsing, Route 209.

## Ulster County
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| U1 | `Kingston NY Historic Landmarks Preservation Commission certificate of appropriateness signs Stockade District` · Firecrawl search → scrape | https://www.fohk.org/welcome/preservation-2/ | Seven-member HLPC created 1969, reviews exterior changes in districts; four districts on National Register + local: Stockade (1969), Rondout-West Strand (1979), Chestnut Street (1985), Fair Street (1988); UPAC landmarked 1978; West Strand row of 19th-c commercial buildings | Hero; Neighborhood ¶2 + facts; Commercial cards (Stockade, Rondout); Sources |
| U2 | same → scrape (query, directQuote) | https://ecode360.com/6728919 (Kingston Ch 405 Art 8, amended 11-12-2024) | "any type of sign within the Stockade District or any designated Landmark Overlay District or landmark site shall be subject to approval by the Landmark Preservation Commission … prior to issuance of a permit"; COA required for material change in appearance incl. light fixtures, signs … visible from a public street or alley; application contents (photos, rendering if required, signs: dimensions, colours, materials, method of illumination); COA in addition to building permit | Neighborhood ¶2; Q&A Stockade sign-off, application contents; FAQ drawings; Compliance callouts; Approvals Timeline; Sources |
| U3 | `City of Kingston NY code chapter 405 signs "electronic" OR "digital" OR "animated" prohibited signs` · Firecrawl search → scrape ×2 | https://ecode360.com/6727255 (Ch 405 Art 4) | Electronic message/LED display signs prohibited in Historic Districts and T1, T2, T3, T4N, T5N; permitted SD-C; may be permitted T5MS, T5F, T4MS, T4N-O, SD-WMU: facade-mounted, panelized ≤9 sq ft, >9 sq ft ≤50% electronic, one per building, 500 ft spacing, static only, ≥5 minutes per message (except time/temp), change ≤1 second, ≤0.3 fc above ambient at nearest property line, ambient light monitor w/ auto dimming + certification to City, revert to black screen on malfunction; window signs max 25% of window, 2 per window | Hero; Neighborhood ¶3 + facts; Q&A back-room ban, outside-districts rules; Compliance; Approvals Timeline; Reality check H3 1; Equipment (light sensors); Sources |
| U4 | `Town of Woodstock NY zoning signs internally illuminated prohibited ecode360 Woodstock sign law` · Firecrawl search → scrape | https://ecode360.com/109254 (Woodstock Ch 260 Art V) | Prohibited: "Directly illuminated signs or advertising devices, unless specifically permitted"; "All internally lighted signs"; illuminated devices constant intensity, no flashing/intermittent/rotating/moving light | Hero; Neighborhood ¶3 + facts; Commercial Woodstock card; Q&A Woodstock gallery; Compliance; Town table; Reality check H3 1 |
| U5 | `Ulster County NY electrician license required master electrician licensing board Kingston electrical license` · Firecrawl search → scrape ×2 | https://ecode360.com/35131702 (Ulster County Ch 185, adopted 5-21-2019 L.L. 3-2019; amended 11-19-2019 L.L. 8-2019, 8-17-2021 L.L. 8-2021, 10-21-2025 L.L. 16-2025) | "ELECTRICAL WORK: … electric light, heat, cooling, power (including solar), signaling, communication, alarm or data transmission"; no one may carry on business as electrical contractor unless licensed or employed and supervised by licensee; exemptions A–G (appliance sales/attachment, elevators, heating repair, manufacturers, public service company employees, homeowners limited, municipal employees) — no low-voltage exemption | Hero; Neighborhood ¶4 + facts; Q&A Licensing; Reality check H3 2; Compliance; Field Notes; Steps; Sources |
| U6 | same search (excerpts) | https://www.ulstercountyny.gov/Boards/Electrical-Licensing-Board ; https://www.townofnewpaltzny.gov/building/urgent-alerts/electrical-licensing-required ; https://www.wawarsingny.gov/DocumentCenter/View/274/Electrical-Licensing-Board-PDF | Board page (incl. City of Kingston licensing board member); Town of New Paltz: "Ulster County Master Electrician Licenses will be required in order to obtain building permits for electrical work"; Wawarsing notice (L.L. 3 & 8 of 2019) | Neighborhood ¶4; Town table (New Paltz); Sources |
| U7 | `Census QuickFacts Ulster` · Firecrawl scrape | https://www.census.gov/quickfacts/ulstercountynewyork | Pop 183,330 (V2025); housing units 87,657 (V2025); owner-occ 69.9%; median value $352,500 (2020–24); land 1,124.24 sq mi; 161.8/sq mi (2020); 5,065 employer establishments (2023); accommodation & food services sales $663,547k (2022) | Neighborhood ¶1 + facts; Sources |
| U8 | `Central Hudson outages Ulster County storm customers without power Woodstock Saugerties` · Firecrawl search → scrape | https://www.cenhud.com/en/outages/outage-summary/ | Ulster customers served 93,190; Kingston City 12,764; Lloyd 5,743; Esopus 4,589; New Paltz town 3,521 / village 2,437; Ellenville 2,246; Saugerties 8,894 / village 2,296 | Neighborhood ¶4 + facts; Commercial Woodstock/Saugerties card; Town by Town paragraph |
| U9 | same → scrape | https://www.dailyfreeman.com/2026/07/05/nearly-50000-central-hudson-customers-without-power-after-storms-hit-region/ | July 5, 2026: severe thunderstorms overnight; 36,709 out as of 5:51 p.m. Sunday, 7,640 in Ulster; ~50,000 at peak | Hero; Neighborhood ¶4 + facts; Q&A lightning; Sources |
| U10 | `iPark 87 Kingston former IBM Tech City tenants square feet redevelopment` · Firecrawl search → scrape ×2 | https://www.ipark87.com/think-about.html (excerpt); https://hudsonvalleyone.com/2024/01/31/ipark-87-attracts-an-unexpected-new-kind-of-tenant/ ; https://www.ulstercountyny.gov/Government/News/Newsroom/2026/02/2026-02-27-UCEDA-iPark-Foreclosure | 200 acres, >1 million sq ft both sides of Enterprise Drive, Town of Ulster; HV1 2024-01-31: Ulster BOCES CTE ~100,000 sq ft of 140,000 sq ft with county depts (~20,000) and SUNY New Paltz + SUNY Ulster (~20,000); UCEDA 2026-02-27 foreclosure on two West Campus parcels (not used beyond "former IBM complex") | Commercial card; Architecture card; Q&A iPark 87 training room; Coverage card; schema mentions; Sources |
| U11 | `Ulster Performing Arts Center UPAC Kingston Broadway theater 1927 seats Bardavon` · Firecrawl search → scrape | https://www.bardavon.org/about-us/upac-history/ | Broadway Theatre opened June 9, 1927; architect Douglas P. Hall; National Register 1979; multi-phase restoration completed 2017; seats 1,510; 601 Broadway (box-office page) | Hero; Architecture card; Commercial Midtown card; Q&A rolling stage LED; Coverage card; schema; Sources |
| U12 | `Bearsville Theater Woodstock NY history Albert Grossman reopened capacity venue` · Firecrawl search (excerpts) | https://bearsvilletheater.com/about ; https://www.billboard.com/business/touring/peter-shapiro-bearsville-theater-woodstock-reopening-lineup-1235666036/ | 291 Tinker Street, Woodstock; Albert Grossman; Dayglo took over (announced April 2024); centre of Bearsville Campus; Billboard: 500-capacity | Commercial Woodstock card; Coverage card; schema; Sources |
| U13 | `Mohonk Mountain House New Paltz National Historic Landmark 1869 Victorian castle rooms Smiley` · Firecrawl search (excerpts) | https://www.mohonk.com/history/ ; https://www.mohonk.com/history/mohonk-a-living-history/ | 1869 Albert Smiley bought a 10-room inn; "Victorian castle resort", 90 miles north of NYC; Historic Hotels of America. (NHL 1986 only on a Facebook post — not used) | Q&A resort meeting room; Sources |
| U14 | `Hutton Brickyards Kingston NY event venue former brick factory Hudson River kiln shed` · Firecrawl search (excerpts) | https://www.huttonbrickyards.com/history ; https://www.hudsonvalleyruins.org/rob/?p=1564 | Three steel-frame kiln sheds moved to the site in the 1940s, originally erected 1928 at Excelsior brickyard, Haverstraw; event destination on riverfront | Commercial card; Architecture card; Coverage card; schema; Sources |
| U15 | `Historic Huguenot Street New Paltz stone houses National Historic Landmark District 1700s` · Firecrawl search (excerpts) | https://www.huguenotstreet.org/home ; https://www.huguenotstreet.org/news-release-historic-huguenot-street-to-host-old-new-paltz-stone-house-day | Ten-acre NHL District, seven stone houses from early 18th c., 30 buildings, heart of 1678 settlement | Neighborhood ¶2; Architecture card; Coverage card; schema; Sources |
| U16 | `Senate House State Historic Site Kingston first New York State Senate 1777 Stockade District stone houses` · Firecrawl search (excerpts) | https://www.hudsonrivervalley.com/sites/Senate-House-and-Museum-/details ; https://en.wikipedia.org/wiki/Senate_House_State_Historic_Site | Single-story Dutch stone house built 1676, enlarged by Abraham Van Gaasbeek; Fair Street; New York's first Senate met there during the Revolution (only "1676 stone house" used) | Hero; Neighborhood ¶2; Coverage card; schema |
| U17 | `Ulster County Emergency Communications 911 center Emergency Operations Center Golden Hill Kingston new` · Firecrawl search → scrape ×2 | https://www.ulstercountyny.gov/Departments/Emergency-Services/Divisions/Emergency-Communications/Emergency-Communications-Center ; https://alfandre.com/project/ulster-county-emergency-communications-center/ | New ECC 16,350 sq ft on Paradies Lane, New Paltz, completion expected 2027, consolidates EOC + PSAP; groundbreaking May 28, 2025; no video wall mentioned | Commercial New Paltz card; Sources (deliberately not a thesis — Putnam owns dispatch) |
| U18 | `SUNY New Paltz "video wall" OR "digital signage" campus` · Firecrawl search (excerpts) | https://www.newpaltz.edu/emergency/frequently-asked-questions/ ; https://www.newpaltz.edu/ocm/digitalmedia.html | Large-screen digital signage installed throughout campus, can be remotely activated for emergency messages; OCM + ITS administer campus signage | Commercial New Paltz card; Sources |
| U19 | `Ellenville NY Shadowland Stages theater Canal Street …` · Firecrawl search (excerpts) | https://shadowlandstages.org/contact-us/ ; https://shadowlandstages.org/directions/ | MainStage 157 Canal Street, Ellenville; US 209 north to Ellenville | Commercial Ellenville card; Sources |
| U20 | Own site · read | /tv-mounting-prices-ulster-county.html | "the county carries no travel or parking surcharge"; "Log walls, video walls and other unusual jobs get a written quote first" | Instant-action bullets |
| C1 | carried from silo file §2 (not re-fetched) | LG 55VM5J-H spec sheet; Samsung datasheets; Samsung Insights 2024-10-21; Planar/Christie/Barco; ADA 307.2; r/CommercialAV 1j9qccf; svsolutionsusa.com; crowntv-us.com | 0–40 °C / 10–80% RH; bezel range; consumer TVs ~8 h/day, warranty void commercially; pitch rules; 4-inch protrusion; convection cooling landscape-only; $9,500 entry; kit = hardware only | Q&A open shed; Equipment; Reality check H3 4–7; Compliance (ADA) |

Local news beyond the Daily Freeman storm piece: not separately searched (EMPTY). Local Reddit: EMPTY. Yelp: EMPTY.

## Prices used (rule + source)
Brooklyn base (`video-wall-installation-brooklyn.html` table) × Ulster 1.53 (blueprint §9), round half-up (all products are integers):
2x2 LCD $18,360–$27,540 · 3x3 LCD $36,720–$58,140 · 4x4 LCD $64,260–$99,450 · 2.5 mm dvLED $53,550–$84,150 · 1.9 mm $84,150–$130,050 · 1.5 mm $130,050–$214,200 · outdoor LED/m² $6,885–$13,005 · mounting/custom fab $2,295–$13,770 (Brooklyn $1,500–$9,000 ×1.53) · maintenance $3,672–$13,770/yr (NYC-hub/most-pages base $2,400–$9,000 ×1.53, as LI hub did; Brooklyn's $15,000 top includes an LED-volume SLA).
Not multiplied (same published figure on almost every silo page): controller add-on $2,500–$15,000; CMS $1,200–$5,000/yr (third-party software). Service $195/hr, 3-hr min ($585) verbatim.
Dropped (no Brooklyn base): 4x4 "16-game" label, LED volume rows, 16x16 HDMI matrix (not relevant), old 3.9 mm row, "Catskills lightning protection +$1,500–$4,500", "Hutton Brickyards COI coordination $500–$1,500", "Audiophile-grade calibration (Woodstock) Included". Spares, sign-mode light sensors, mobile stage frames, enclosures: "quoted after the site visit". BYOE: quoted after survey / install-your-own page.
CONFLICT: old Ulster page prices were BELOW Brooklyn (2x2 $10,500–$15,500 vs Brooklyn $12,000–$18,000 → ×1.53 = $18,360–$27,540), i.e. ~0.87×, not 1.53×; the new figures are ~75% higher than what was live. Old page also carried a "$500 minimum job", "1-year parts-only … 3-5 year manufacturer" wording, a "$2M COI with Hutton Brickyards as additional insured" claim and invented project figures ("$54k dvLED …", "Replacement quote … $44k") — none carried over.

## Images (11) — source → new file (images/video-wall-installation/)
Pool: images/low-voltage/ + images/commercial-security/ (no images/network/ used in the final set). All library images look staged/AI-styled (branded shirts, fake signage); crops remove faces, signage and shirt phone numbers; captions say "Photo from the AESS image library" and that none shows an Ulster job or a video wall.
- commercial-security/commercial-security-systems-manhattan-dashboard-training.jpg → video-wall-installation-ulster-county-monitor-showing-four-live-camera-views.webp (hero; crop excludes the names column and both faces)
- commercial-security/commercial-security-systems-manhattan-exterior-enclosures.jpg → …-weatherproof-boxes-on-conduit-at-block-wall.webp
- commercial-security/commercial-security-systems-nyc-patch-panel-punchdown.jpg → …-hands-punching-down-cables-on-rack-patch-panels.webp
- low-voltage/low-voltage-installation-bronx-hero-warehouse-cable-tray.jpg → …-dome-camera-and-cable-tray-in-high-bay.webp
- commercial-security/commercial-security-systems-hudson-valley-conduit-pull.jpg → …-cable-routed-through-rigid-conduit-into-wall-box.webp
- low-voltage/low-voltage-installation-hudson-valley-10-school-corridor-cable-pull.jpg → …-cable-bundle-pulled-across-open-ceiling-grid.webp
- low-voltage/low-voltage-installation-nassau-county-riser-conduit-pull.jpg → …-gloved-hands-drawing-cable-from-surface-conduit-box.webp
- commercial-security/commercial-security-systems-bronx-nvr-poe-rack.jpg → …-hand-seating-recorder-in-equipment-rack.webp
- commercial-security/commercial-security-systems-nyc-vms-commissioning-laptop.jpg → …-laptop-commissioning-camera-software-beside-rack.webp
- commercial-security/commercial-security-systems-nyc-access-control-panels.jpg → …-screwdriver-on-controller-boards-in-wiring-cabinet.webp
- commercial-security/commercial-security-systems-manhattan-office-cat6-ceiling.jpg → …-cable-coil-hung-from-open-ceiling-grid.webp
Swapped out mid-run because same-batch siblings used the same shots: low-voltage bronx-07-fluke-certification-pass (Suffolk), low-voltage bronx-13-restaurant-ceiling-speaker (Rockland), network bronx-core-drill-cmu-wall-penetration (Rockland).

## Question register — video-wall-installation-ulster-county
Questions Answered (H3):
1. Who has to sign off before a screen goes into a Stockade District storefront?
2. Kingston bans electronic signs in its historic districts — does that reach a video wall in our back room or lobby?
3. Outside the historic districts, what does Kingston allow for a digital sign facing the street?
4. What does a landmarks commission application need to show when a display will be seen from the street?
5. Woodstock bans internally lighted signs — where in a gallery can moving images go instead?
6. Our business is in New Paltz, Saugerties or another town — whose sign rules apply to a screen?
7. Can a video wall be fixed to a seventeenth- or eighteenth-century stone wall at all?
8. What carries the screens when the owner will not allow a single hole?
9. Our venue is an open-sided shed or barn — can the screens stay up between events?
10. How do cables reach a wall in a building with no ceiling void and walls that cannot be opened?
11. Can an LED wall be rolled onto a historic stage instead of fixed to it?
12. Can a theatre lobby wall run the season trailer and then show a delayed-start notice from the box office?
13. Can screens show artwork or moving-image pieces without looking like a television?
14. What does the wall look like when it is switched off in a heritage interior?
15. Can a resort meeting room wall be cleared away for a weekend event and back up on Monday?
16. A training room at iPark 87 is being fitted out on a bare factory floor — what should go in before the ceiling closes?
17. How far can the controller be from the wall in a long converted factory or campus building?
18. Ulster’s Electrical Licensing Law mentions data transmission — what does that mean for a video wall job?
19. Is unplugging the only real protection from lightning for a wall in an exposed hilltop venue?
FAQ (visible == FAQPage, 10):
1. Can a wall be taken down later without leaving marks on old plaster, brick or stone?
2. Do you prepare drawings a landmarks commission or planning board can review?
3. Our stone building eats Wi-Fi. How does new content reach the wall?
4. Can a screen go into a wedding or event room without showing up in every photograph?
5. Will you work alongside the venue’s own lighting and sound company?
6. Can a wall be fixed to the posts and beams of a converted barn?
7. Can the screen frames be finished to sit with old woodwork?
8. Can the lobby screens show a live picture from the stage camera?
9. Can you reuse the wiring from our old projector?
10. Can the wall pull in posts from our website or social media automatically?
Other "?" heading: "Planning a Screen for an Old or Landmarked Ulster Building?" (CTA H2).
De-dup notes: dropped/reworded during build to avoid silo overlaps — window-screen-as-sign (LI hub / Queens / Nassau) reframed as approval authority (Q1) and placement under Woodstock's ban (Q5); FAQ "work around booking calendar" (≈ Nassau after-closing), "how far ahead to book" (≈ old-template lead time), "certificates of insurance" (≈ old-template COI handling) replaced; storm question reframed to lightning/unplugging (LI hub covers power restoration).
---

## Westchester

Rebuilt 2026-10-18 (`video-wall-installation-westchester-county`, REBUILD, scheduled batch). Searches run with Firecrawl search/scrape from the build environment. Thesis: Westchester walls split into inward-facing walls in office parks being re-let to medical tenants, hospital towers and campuses (IT review, power, GC schedule) and street-facing window screens whose legality changes by municipality (48 municipalities, divergent sign laws).

### Matrix (v2.3 §3)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | `reddit westchester video wall OR "TV wall" OR "multiple TVs" bar restaurant install` · Firecrawl → no Westchester threads returned. EMPTY (not accessible in build env / no results). Silo-level r/CommercialAV excerpts reused (§3.1). |
| 2–5 | PAA, PASF, Answer the Public, AI Overview | EMPTY (not accessible in build env). AI check built from cost guides/rules of thumb (§3.3) + Westchester codes. |
| 6–7 | Landmarks, building stock | Done (below) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | 914INC, Governor's office, WMCHealth, White Plains Hospital, SNA Displays (below) |
| 10 | Hyperlocal | Municipal codes (eCode360), White Plains DRI plan |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Entries (query · platform · URL · finding · page+section)
- `Westchester County NY cities towns villages how many municipalities` · Firecrawl · https://en.wikipedia.org/wiki/Westchester_County,_New_York ; https://www.ny.gov/counties/westchester · 6 cities, 19 towns, 23 villages; 450 sq mi; 990,817 (2023) · Neighborhood ¶1, facts list, AI check, Field Notes.
- scrape · https://censusreporter.org/profiles/05000US36119-westchester-county-ny/ · ACS 2024 1-yr: pop 1,006,447; 398,706 housing units; 50% multi-unit; 61% owner-occupied; median value $691,100; median HH income $118,596 · Neighborhood ¶1, Building Specialists (co-ops), facts list.
- `Westchester County Department of Consumer Protection license electrician home improvement` · Firecrawl · https://consumer.westchestercountyny.gov/home-contractors-and-trades/plumbers-and-electricians ; /apply-for-a-license ; https://consumer.westchestercountyny.gov/hiring-tips · electricians must hold a county trade licence; "all electrical work must be performed by a Westchester County-licensed electrician or an employee of a licensed electrician"; county trade licence search · photo strip, AI check, facts list, Sources.
- gov search · https://ecode360.com/9158075 (Town of Mamaroneck Ch. 90) · regulates wiring/equipment "operating in excess of 50 volts"; electricians need a licence from any Westchester municipality · facts list. https://ecode360.com/6850133 (Yorktown Ch. 155) · electrical contracting defined incl. signaling systems/signs >50 V · Sources only.
- scrape · https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors · county licence required for home improvement contractors; EPA RRP lead rule since April 22, 2010 for pre-1978 homes, child-care facilities, schools · FAQ lead paint, Building Specialists.
- scrape (pdf) · https://consumer.westchestercountyny.gov/images/stories/pdfs/homeimprovementapplication02232026.pdf · §863.312 "home improvement" = repair/replacement/installation… in a residence or dwelling of not more than three units; §863.313 licence required; §863.324(4) exemptions incl. electrical work, State-licensed occupations within scope, County-licensed alarm businesses; Dept. at 148 Martine Ave · facts list, landmarks (148 Martine Ave). AESS county home-improvement licence NOT claimed — FLAG.
- scrape · https://www.westchesterlegislatorsny.gov/latest-news/board-approves-new-rules-for-home-contractor-licensing-to-protect-workers-consumers · Nov 20, 2018 amendments (wage-theft judgments, fee $500/2 yrs from 2021) · Sources only.
- `site:ecode360.com Westchester village sign law electronic…` · Firecrawl → scrape https://ecode360.com/10861656 (Mount Kisco Ch. 89) · animated signs incl. electronic reader board signs prohibited; electronic interior window signs prohibited except one "Open" sign ≤220 sq in, not moving/flashing, off when closed, no product advertising; temporary window signs ≤25% · QA "same window screen…", QA "set back from the glass", QA "switch off", AI check, Field Notes, facts list.
- scrape · https://ecode360.com/37564799 (Port Chester §345-701, amended through L.L. 5-2026) · Electronic Message Boards only in CV district; monochrome; ≤0.3 fc above ambient; change ≤ once/60 s; instantaneous transition; ≤50% of sign area; not within 100 ft of residential structure; window signs ≤33% of glass; no animated/flashing lights · same QAs, Field Notes.
- scrape · https://ecode360.com/6816946 (Greenburgh Ch. 240) · §240-2C illumination steady, not flashing/moving/changing; §240-3A "window or inside" sign = interior sign visible from street; §240-3C(15) signs within 2 ft of a window ≤25% of any single window; §240-3C(5) illuminated business signs off ½ hour after closing, automatic devices · same QAs.
- https://ecode360.com/15113414 (Yonkers Ch. 47) · scrape returned no window/electronic provisions — not used on page.
- scrape (pdf) · https://www.ny.gov/sites/default/files/2025-05/White_Plains_DRI7_SIP.pdf · White Plains DRI Round 7 (2024); "Install Digital Signage on the Windows of ArtsWestchester", 31 Mamaroneck Ave, replace 3 framed poster receptacles, $27,500; branding/wayfinding project $819,000 total ($749,000 DRI) incl. two digital kiosks with real-time transit · Neighborhood ¶5, landmarks.
- scrape · https://snadisplays.com/news/yonkers-tron-city-of-yonkers-adds-video-board-to-inform-residents/ (May 29, 2024) · 16'6" x 26'3", 10 mm EMPIRE Exterior XS, 504x800 px, Government Center Garage facing New Main Street, installed by Yonkers Engineering Dept; city text: "largest film production studios in the Northeast" · Neighborhood ¶5, QA "outdoor screen like Yonkers", landmarks.
- `Westchester corporate headquarters I-287 Platinum Mile…` · Firecrawl · https://914inc.com/westchesters-platinum-mile-is-making-a-serious-comeback/ (Apr 2026) · ~4 mi of I-287 from 333 Westchester Ave (White Plains) to 800 Westchester Ave (Rye Brook); ~4.5M sq ft office built in Purchase 1972–1988; "Medical Mile"; 3030 Westchester Ave fully leased to Westmed; Wegmans planned West Harrison · Neighborhood ¶2, QA "re-let to a medical group", landmarks. https://docs.ryebrook.org/…/10 - Chapter 10 - Commercial Development.pdf · corridor clients Morgan Stanley, PepsiCo, Mastercard, IBM · Neighborhood ¶2.
- `Regeneron Tarrytown campus expansion…` · Firecrawl · https://www.governor.ny.gov/news/governor-hochul-announces-groundbreaking-regenerons-18-billion-expansion-westchester-county ; https://www.regeneron.com/about/our-company/locations ; https://careers.regeneron.com/en/locations/north-america/westchester/ · $1.8B, up to 8 buildings, ~900,000 sq ft, completion expected 2027; HQ 777 Old Saw Mill River Rd; Greenburgh supervisor quote; other sites Sleepy Hollow, Hawthorne, Armonk · Neighborhood ¶4, QA "campus project with a GC", landmarks.
- `Westchester Medical Center … White Plains Hospital expansion` · Firecrawl · https://www.wmchealth.org/press-releases/… (Sep 29, 2025); https://wmchealthgiving.org/… · Brenda Fareri Pavilion critical care tower, 5 stories, 162,000 sq ft, completion 2026 (128 private rooms per wmchealth.org) · https://www.wphospital.org/about-us/campus-transformation/ · 475,000 sq ft addition, topping off May 7, 2026 (Suffolk Construction), opening early 2028 · Neighborhood ¶4, landmarks.
- `Con Edison NYSEG service territory Westchester` · Firecrawl · https://dps.ny.gov/system/files/documents/2022/10/nys-electric-and-gas-utilities-by-county.pdf · Westchester electric: NYSEG and Con Edison · https://www.coned.com/en/business-partners/service-territories · Con Ed territory includes Westchester · facts list, landmarks (northern towns "may be NYSEG" — town-level split not sourced).
- `Westchester County Police Real Time Crime Center…` · Firecrawl · https://publicsafety.westchestercountyny.gov/crime-analysis-unit · RTC monitors via cameras, LPR · Sources only (not described on page beyond source list).
- `HDBaseT 100 meters…` · Firecrawl · https://hdbaset.org/hdbaset-technology/ · up to 100 m/328 ft over category cable; 1080p to 100 m over Cat5e+, 4K up to 70 m over Cat5e (100 m select Cat6a) · QA "raised access floor" (replaced the fiber-distance QA after batch overlap check).
- Silo §2 manufacturer facts reused: LG 55VM5J-H (160 W typ/190 W max, SNMP, status mailing, Crestron), LG LAPA136 (650 W avg/1,300 W max), Samsung bezels/daisy chain 10x10, Chief ConnexSys 4–7.4 in, ADA 307.2, Planar/Christie/Barco, Samsung Insights consumer-TV article.

### Prices used (rule)
Brooklyn video-wall base (§3.5) × Westchester 1.25 (§9), consistent with Nassau ×1.15 / Queens ×1.05 rebuilds: 2x2 $15,000–$22,500; 3x3 $30,000–$47,500; 4x4 $52,500–$81,250; 2.5 mm LED $43,750–$68,750; 1.9 mm $68,750–$106,250; 1.5 mm $106,250–$175,000; outdoor LED/m² $5,625–$10,625; controller $3,125–$18,750; 16x16 matrix $5,625–$15,000; mounting $1,875–$11,250; CMS $1,200–$5,000/yr unmultiplied; maintenance $3,000–$18,750/yr (Brooklyn base $2,400–$15,000 as Nassau used); $195/hr, 3-h min ($585). CONFLICT: old Westchester page showed 2x2 $11,000–$16,500 … 1.5 mm $78,000–$130,000 (≈0.92× Brooklyn), a 1.2 mm row ($100k–$180k, no base) and "$500 minimum job" — all dropped.

### Images (11) — source → new file (images/video-wall-installation/)
No Drive "Video Wall" subfolder (Drive root has Cat6 Repair, Sonos, Soundbar, Smart Lock, Fiber Optic only); CompanyCam/Composio not checked this run (not connected in earlier runs today). Permanent image rule, real phone photos only (AI-looking pool images excluded), none previously used (md5) on a video-wall page:
security-camera-maintenance-nyc-cable-bundles-above-recorder-monitor → westchester-county-cable-bundles-above-wall-monitor; dvr-upgrade-nassau-county-recorder-screen-channel-grid-and-bitrate-table → -sixteen-camera-tiles-and-bitrate-table; dvr-upgrade-brooklyn-store-monitor-showing-camera-grid → -store-display-split-into-eight-camera-views; apartment-building-…-queens-camera-grid-on-ceiling-hung-monitor → -ceiling-hung-display-above-store-shelving; security-camera-maintenance-nyc-recorder-live-view-with-date-and-time-stamp → -date-stamped-live-view-tiles-close-up; school-security-camera-installation-brooklyn-recorder-monitor-32-channel-grid-under-cable-runs → -lg-monitor-under-overhead-cable-runs (hero); security-camera-maintenance-nyc-mini-camera-above-soffit-and-recessed-lights → -soffit-and-recessed-lights-in-lobby-ceiling; security-camera-maintenance-nyc-turret-camera-above-glass-lobby-entrance → -glass-lobby-front-below-drop-ceiling; dvr-upgrade-westchester-two-small-cameras-high-on-white-wall-below-mezzanine-windows → -tall-white-wall-below-mezzanine-windows; security-camera-maintenance-nyc-bullet-camera-in-corridor-ceiling-by-door → -blank-corridor-wall-with-two-cover-plates; apartment-building-…-staten-island-recorder-monitor-lot-and-storeroom-views → -two-view-split-screen-lot-and-storeroom. None shows a video wall; captions say "reference photo" and describe only what is visible.

### Question register — video-wall-installation-westchester-county
Q&A (H3):
1. Why would the same window screen be allowed in one Westchester village and refused in the next?
2. Does a screen set back from the glass still count as a window sign?
3. Do local rules make us switch off a screen that can be seen from the street after closing?
4. Could a town or school put up an outdoor screen like the one on the Yonkers Government Center garage?
5. Our Westchester Avenue office building is being re-let to a medical group — what changes for a waiting-room wall?
6. Will our IT department let a video wall controller onto the corporate network?
7. Can visitors share a laptop to one section of the wall without touching the rest?
8. On a campus project with a general contractor, at which stage should the video wall crew be on site?
9. Our best wall is part of the building’s fire-rated core — can the mount be fixed to it?
10. Our briefing room has a raised access floor — can the wall be fed from below instead of through the ceiling?
11. Can the wall be mounted around fire-alarm strobes and sprinkler heads?
12. If no wall in the lobby is strong enough, can the panels hang from the structure overhead?
13. What should a facilities manager put in a request for proposals so bids can be compared?
14. Do the panels need to be the same brand as the conference-room displays we already have?
15. Can the wall show live data such as a building energy dashboard or air-quality readings?
16. What does a co-op or condo board usually need before a lobby display goes up?

FAQ (accordion + FAQPage):
1. Do you sign the vendor-security questionnaires and confidentiality agreements that corporate clients send?
2. Our building is older than 1978 — does drilling for the mount bring in lead-paint rules?
3. How much electricity does a wall use if it is left on all night, and is it worth scheduling it off?
4. What dust and noise controls do you use when working inside a medical practice that stays open?
5. Who patches and paints the wall when the old screens come down?
6. Can panels go in before a new building has its certificate of occupancy?
7. Does every panel in the wall need its own network cable, or can one connection serve the whole wall?
8. Who is responsible if a panel arrives damaged or dead from the manufacturer?
9. Can the controller be locked in a closet away from the wall?
10. Do you need a loading-dock or parking reservation for a delivery to a Westchester campus?

Register revised 2026-10-18 after batch overlap check vs Rockland, Suffolk and Ulster: 8 questions replaced (cleaning, Crestron, curved wall, speakers, temporary sales office, licence check, controller/fiber distance, electrical capacity). New FAQ facts: LG 55VM5J-H 160 W typical (silo §2) for the overnight-energy FAQ; Samsung daisy chain up to 10x10 (silo §2) for the per-panel cable FAQ. Fire-rated core, raised floor, overhead suspension, dust controls, certificate of occupancy and damaged-panel answers are AESS method statements.

### Unsourced practices on the page (AESS method statements, not facts)
IT packet contents; no default passwords/own network segment; two-visit GC sequence; waiting-room content advice (captions, no names); fire-alarm/sprinkler clearance practice; firestop approach for rated walls; raised-floor slab bearing; overhead suspension sign-offs; open-clinic dust/noise controls; CO/released-area practice; damaged-on-arrival handling; patch/paint; co-op board package contents; dock/elevator arrangements; spare panel from same batch; "most single faults fixed within 1–2 hours"; openingHours 08:00–20:00; landmark descriptions of Getty Square, Ridge Hill, Central Park Ave, Central Ave car dealers, New Rochelle downtown, Mount Kisco Route 117; northern-town NYSEG split.
