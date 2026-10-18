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
