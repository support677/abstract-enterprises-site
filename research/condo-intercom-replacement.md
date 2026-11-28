# Research — /condo-intercom-replacement (root decision guide, NYC hub phone (800) 486-0943, GBP Brooklyn)

Built Nov 26 2026 (batch subagent). Keyword list and rules: `keywords/condo-intercom-replacement.md`. One page only (no area or cluster pages). Same page type as /co-op-board-intercom-upgrade, used for structure only; every sentence written fresh for condo boards / HOAs / managing agents / unit owners.

## Prices used (only what the site already publishes)
- $250 service call (diagnosis + simple repairs, applied to the job) and "free on-site estimate" for new installs — `/intercom-pricing`; START_PRICES in tools/check_page.py (Anwar, Nov 25 2026).
- Apartment station $250–$525; door release relay/button $250–$475; 24V transformer $325–$650; electric strike $450–$950; lobby panel $650–$1,800; riser repair in occupied walls $850–$2,400 — `/door-buzzer-repair-pricing` FAQ.
- Multi-unit building system (5–30 units) $1,200–$5,000+; elevator access control $1,500–$6,000+ — `/intercom-installation-nyc` pricing block.
- NOT used: `/intercom-repair-nyc` table ($150–$300 diagnostic, $4,500–$40,000 building figures) — conflicts with the $250 service call; flagged for Anwar.
- Financing: one line, "Financing is available through Wisetack, subject to approval." (cost section). No rates.

## Research matrix (exact query · platform · URL · finding · page section used)

| # | Query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| L1 | reused, research/condo-security-systems.md L1 (`New York Real Property Law 339-d definitions common elements unit condominium` · WebSearch → Firecrawl scrape) | https://law.justia.com/codes/new-york/rpp/article-9-b/339-e/ | RPL §339-e: unless the declaration provides otherwise, common elements include "halls, corridors, lobbies, stairs, stairways, fire escapes, and entrances and exits of the building" and "all apparatus and installations existing for common use"; operation of the property includes "the maintenance, repair and replacement of" common elements; unit owner owns in fee simple. | The Decision ¶2 + facts list; Approval ¶1; AI check claim 1 |
| L2 | reused, research/condo-security-systems.md G1 (`New York Real Property Law Article 9-B condominium act 339-v bylaws board of managers contents` · WebSearch → Firecrawl scrape) | https://www.nysenate.gov/legislation/laws/RPP/339-V | Bylaws must state "the powers and duties of the board", managing agent, percentage "necessary to adopt decisions binding on all unit owners"; may provide reserves "for major and minor maintenance, repairs, additions, improvements, replacements". | Facts list; Approval ¶1; Reserve Planning ¶2; AI check claim 5 |
| R1 | reused, research/co-op-board-intercom-upgrade.md R1 | https://www.nysenate.gov/legislation/laws/MDW/50-A | MDL §50-a intercom requirement for class A MDs erected/converted after Jan 1 1968 with 8+ apartments. Applicability to a given condo left to counsel. | Facts list; Repair or Replace last ¶ |
| R2 | reused, co-op R2 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-57173 | 28 RCNY §25-151 minimum device, return buzzer, button ≤6 ft, speaking device 4–5 ft. | Facts list; Rules That Apply (heights) |
| R3 | reused, co-op R3 | https://cooperatornews.com/article/bidding-basics | CooperatorNews Feb 2020: needs assessment → scope → RFP → leveled comparison; sealed bids opened with at least two people present. | RFP & Bids ("Running the process") |
| R4 | reused, co-op R4 | https://www.habitatmag.com/Publication-Content/Legal-Financial/2025/January-2025/coop-condo-board-assessments | Habitat Feb 17 2025: bylaws often empower boards to impose assessments by resolution; condo assessments divided among unit owners by ownership interest; some boards spread assessments over years. | Reserve Planning (funding the gap) |
| R5 | reused, co-op R5 | https://www.fsresidential.com/new-york/news-events/articles-and-news/reserve-funds-strategic-budgeting-for-condominium/ | Reserves = long-term savings for capital projects keeping the building safe, functional, compliant. | Reserve Planning ¶2 |
| R6 | reused, co-op R6 | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL 63/2021 smart-access duties (policy, consent, minimum data, 90-day deletion, no required smart access to tenant's unit). Written as applying to tenants it covers; board to ask counsel for condos with renters. | Facts list; Q&A face recognition; Rules That Apply (privacy) |
| R7 | reused, co-op R7 | https://cooperatornews.com/article/replacing-intercom-systems | CooperatorNews Nov 2025, Allan Liers: 1960s–80s wiring "typical lifespan of 25-50 years"; few-wire systems incompatible with IP/multi-wire; initial recommendation generally to retain infrastructure except the panel. | Facts list; Reserve Planning (component split); AI check claim 3 |
| R8 | reused, co-op R8 | https://www.access-board.gov/ada/ | 2010 ADA §308.2.1 forward reach 15–48 in. Applicability left to architect/counsel. | Rules That Apply (heights) |
| R10 | reused, co-op R10 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 | Admin Code §28-105.4.7 <50 V permit exemption with exceptions. | Rules That Apply (permits) |
| R13 | reused, co-op R13 | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173505 | Building Code §1010.1.9.8 sensor-release door conditions; §1010.1.9.9 follows. | Cost driver 4; Rules That Apply (egress); AI check claim 7 |
| S1–S6 | Google PAA / PASF / Answer the Public / AI Overview / Bing-DDG / Yelp 1–3★ | — | EMPTY (not accessible in build env). The AI Reality Check answers common generic claims and corrects them with L1–R13; it does not claim a captured AI Overview. | — |
| S7 | Reddit | — | EMPTY (not accessible in build env) | — |

Not used / not claimed: Levandusky (co-op case; not cited for condos), no client buildings, no testimonials, no case studies, no manufacturer certification or partner status, no model numbers.

## Images (11, WebP in images/condo-intercom-replacement/)
Each viewed before naming; alt/title/caption describe only what is visible; all labeled "Product photo"; none shows "AESS", faces, phone or house numbers. No images/buzzer-repair/*.jpg, elevator, network-installation, low-voltage, commercial-security or smart-lock sets used. All 11 are byte-unique (sha256) vs images/condo-security-systems/*, images/co-op-security-systems/*, images/co-op-board-intercom-upgrade/*.
**VISUAL REPEATS — FOR ANWAR:** the site library has no intercom product photo (or entrance/riser photo) that is not already shown, at least as a crop or re-encode, on the condo / co-op pages. Manufacturer sites and Firecrawl screenshot storage are blocked by the build proxy, and Drive `AESS Website Photos` has no intercom folder. 10 of the 11 are visually the same products as images on those pages; replace when real condo intercom job photos arrive.

| File (condo-intercom-replacement-…) | Source | Shows |
|---|---|---|
| tall-touchscreen-lobby-panel-with-dial-pad (hero, og/twitter) | door-buzzer-repair/…mount-hope-touchscreen-directory-panel-with-dial-pad.webp | Stainless panel, camera/speaker bar, touchscreen dial pad, reader symbol |
| keypad-video-door-station-with-card-band | akuvox-vs-butterflymx/…keypad-card-reader-door-station-product-photo.webp | Camera, reader band, 12-key keypad |
| compact-dark-door-station-with-grille | door-buzzer-repair/…mount-hope-slim-dark-grey-door-station-with-grille-and-round-button.webp | Small surface station, grille, round button |
| white-in-unit-touchscreen-monitor | akuvox-vs-butterflymx/…white-indoor-touchscreen-monitor-product-photo.webp | White indoor monitor, menu + tiles |
| one-button-video-door-station-silver-plate | door-buzzer-repair/…new-lots-silver-and-black-video-door-station-product-photo.webp | Camera, contactless mark, one button |
| dark-keypad-entry-panel-with-screen | door-buzzer-repair/…belmont-dark-keypad-station-with-screen.webp | Tall dark panel, screen, keypad |
| touchscreen-entry-panel-with-dual-cameras | alarm-installation/…fort-greene-face-and-card-entry-panel-product-photo.webp | Two lenses, face prompt screen (building photo, no person), reader |
| narrow-video-door-station-with-speaker-grille | access-control-installation/…south-williamsburg-narrow-dark-grey-video-door-station.webp | Narrow station, dome camera, grille, lit ring |
| rounded-video-entry-unit-with-reader-zone | door-buzzer-repair/…beverley-square-rounded-silver-and-black-video-intercom.webp | Rounded unit, light panel, camera, reader |
| door-station-mounting-back-plate | intercom-repair/…staten-island-white-network-video-doorbell-rear-mounting-side-product-photo.webp | Mounting plate, screw points, cable opening |
| black-video-door-station-with-lit-call-ring | door-buzzer-repair/…bedford-park-black-video-door-station-blue-ring-button.webp | Tall black station, wide lens, blue ring |

DAILY-LOG note suggestion: `images: 11 reused intercom product photos (visual repeats of condo/co-op sets; library exhausted, no real condo intercom photos yet)`.

## Links
Once each: all 15 condo-security-systems-* pages (Areas section), /co-op-board-intercom-upgrade, /apartment-intercom-system-nyc, /intercom-installation-nyc, /intercom-repair-nyc, /door-buzzer-repair-nyc, /akuvox-vs-butterflymx, /doorbird-vs-2n, /butterflymx-installation-nyc, /access-control-installation-nyc, /elevator-access-control-installation-nyc, /structured-cabling-installation-nyc, /condo-security-camera-installation-nyc (built in parallel — broken until it ships), /intercom-pricing, /door-buzzer-repair-pricing, /warranty, /co-op-security-systems-nyc, /apartment-building-security-camera-installation-nyc.
FLIP (plain text, not live yet): /comelit-intercom-nyc, /aiphone-intercom-nyc, /akuvox-intercom-nyc, /2n-intercom-nyc, /doorbird-intercom-nyc, /swiftlane-access-control-nyc.
Wiring for main run: /condo-security-systems-nyc and /intercom-installation-nyc each need one contextual link back (keyword file).

## Question register — /condo-intercom-replacement

### Q&A (Your Questions Answered, H3)
- Does the association or the unit owner pay for the station inside a condo unit?
- Can an owner refuse to let installers into the unit for an intercom replacement?
- Our sponsor still controls the board. Should the replacement wait for turnover?
- Our system was installed only a few years ago but the maker stopped supporting it. Is it trash?
- How do we handle owners who don't use smartphones?
- Can visitors at our garage gate and our lobby use the same directory?
- Is face recognition a good idea for a condo lobby?
- What happens to the intercom when the building internet goes down?
- Do we need an engineer, or can the managing agent run the project?
- How long does a condo intercom replacement take once the board approves it?
- Should the intercom replacement be timed with a lobby renovation?
- How do we tell renters about a new intercom when only owners vote?
- Who keeps the directory current after owners sell or renters move?

### FAQ (accordion + FAQPage schema)
- Is this condo intercom guide legal or financial advice?
- Is the on-site assessment free when the board wants a replacement proposal?
- Can you quote a building where owners supply their own in-unit stations?
- Will you respond to an RFP written by our managing agent or consultant?
- Do you hold manufacturer certifications for the intercom brands you install?
- Can you share contact details for other condo boards you have worked with?
- Do you handle the electrical work for a new intercom power supply?
- What happens to our current intercom service contract when we replace the system?
- Can a single proposal cover several buildings in one condo association?
- When is the best time of year to schedule a condo intercom replacement?
- Do special-order intercom panels change the schedule?
