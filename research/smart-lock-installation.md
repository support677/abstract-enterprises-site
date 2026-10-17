# Smart Lock Installation — silo research (batch 2026-10-17: NYC, Long Island, Hudson Valley hubs)

Merged from the three hub builders' notes. Each section keeps its own query · platform · URL · finding · page+section log, prices with source files, and question list (the question register for the silo is the union of the 'Questions' lists below).

---

<!-- source: smart-lock-installation.nyc.part.md -->
# Smart Lock Installation — research part: NYC hub (smart-lock-installation-nyc)

Built 2026-10-17 by the NYC builder subagent. Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used.
Thesis: NYC = renters, co-ops, condos and multi-unit buildings. The apartment door is governed by state law (MDL), the city Housing Maintenance Code, HPD fire-safety rules, the Tenant Data Privacy Act and co-op/condo house rules before it is governed by the lock's spec sheet.

## Silo-wide findings (usable on any smart-lock page)

| # | Query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| S1 | `smart lock installation cost Angi 2025 average national` · WebSearch → WebFetch | https://www.fixr.com/costs/smart-lock-installation | National third-party data, updated Jan 31 2025: smart lock installation $250–$400, average $300 (Wi-Fi lock + one accessory); handyman $50–$100/hr. | §14 Pricing (labelled national third-party), §10.5 AI reality check H3 1, FAQ "national averages" |
| S2 | same query | https://bobvila.com/articles/how-much-do-smart-locks-cost | No price data on page (testers: "only a Phillips screwdriver", ~30 min DIY). | §10.5 H3 2 (DIY claim) |
| S3 | `August Wi-Fi Smart Lock retrofit keeps existing deadbolt …` · WebSearch → WebFetch | https://august.com/pages/retrofit-door-lock | Retrofit mounts inside on existing deadbolt, "leaving the outside untouched"; keys unchanged; "only compatible with single cylinder deadbolts"; some models need clearance for wing latches. | §6 services, §7.5 methods, §9 renters Q&A, §10 equipment |
| S4 | `August Connect Wi-Fi bridge distance …` · WebSearch → WebFetch | https://support.august.com/en_us/august-connect-improving-your-wi-fi-and-bluetooth-signals-SyqxvL1Adz.md | "within 10–15 feet of your August Smart Lock"; router distance depends on obstacles; check full Wi-Fi bars at Connect location. | §9 Q&A Wi-Fi in concrete buildings, Wi-Fi/Matter section |
| S5 | `Matter over Thread smart lock border router explained …` · WebSearch → WebFetch | https://support.shopyalehome.com/en_us/how-to-set-up-your-yale-smart-lock-with-matter-r18U4hgnyg.md | Yale Matter-over-Thread lock needs a Thread border router set up first; router "must be the same brand as the app" (e.g. Nest Hub 2nd gen for Google Home). | Wi-Fi/Matter section, §10.5 H3 Matter |
| S6 | same query | https://knowledgebase.boldsmartlock.com/en/knowledge/how-does-matter-work-with-bold | Thread = low-power self-healing mesh; needs Thread border router (Nest Hub 2nd gen, HomePod mini); up to five ecosystems ("Matter fabrics"). | Wi-Fi/Matter section, §10 equipment |
| S7 | `smart lock for mortise lock apartment door NYC compatible …` · WebSearch → WebFetch | https://community.smartthings.com/t/are-there-any-smart-locks-that-work-with-mortise-type-doors/6539 | 2014 post: "I have metal Brownstone doors with mortise-type locks. Are there any smart locks for this type?" Replies through 2023: no confirmed drop-in; options = swap cylinder/handleset, separate smart deadbolt, commercial mortise access-control locks. | §7 pre-war mortise, §9 Q&A mortise, §10.5 H3 "fits any door" |
| S8 | same query | https://csa-iot.org/csa_product/master-lock-mortise-lock/ | CSA lists a "Master Lock Mortise Lock" (Yale Pro 2 line) certified 04/23/2026 — page does not state Matter/transport. Not used as a Matter claim. | research only |
| S9 | `kalamein door NYC fire-rated …` · WebSearch → WebFetch | https://www.fireengineering.com/fire-prevention-protection/construction-concerns-for-firefighters-fire-resistance-of-doors/ | Kalamein = fire-rated slab door with gypsum core; steel versions exist; older ones sometimes asbestos-cement core, "many … still present in structures built before 1980". | §7.5 kalamein doors, Field Notes |
| S10 | Reddit / PAA / PASF / Answer the Public / Google AI Overview / Yelp 1–3★ | — | EMPTY (not accessible in build env). Reddit search via WebSearch returned only news coverage (see N10). §10.5 headings are claims published by cost sites/manufacturers, not quoted AI Overview text — stated on the page. | — |
| S11 | Bing / DuckDuckGo | — | EMPTY (not accessible in build env). | — |

## NYC hub

| # | Query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| N1 | `New York Multiple Dwelling Law 51-c tenant install own lock provide duplicate key landlord` · WebSearch → WebFetch | https://www.nysenate.gov/legislation/laws/MDW/51-C | Tenant in a multiple dwelling may install and maintain own lock in addition to owner's lock, ≤ 3 inches in circumference; must give duplicate key on request; lease clauses charging for this are void; excludes municipal housing authority buildings, hotels/motels, dormitories. | §5, §9 renter Q&A, renters guide, FAQ |
| N2 | same search | https://cooperatornews.com/article/the-shareholder-versus-the-board | 111 Tenants Corp. v. Stromberg (Manhattan co-op, 1996 article): shareholder ordered to surrender duplicate key without conditions; proprietary leases require duplicate of any new key; emergency-access rationale. | §9 co-op Q&A, §10.5 |
| N3 | `NYC HPD apartment entrance door lock requirements heavy duty dead bolt chain guard peephole …` · WebSearch → WebFetch | https://nycadmincode.readthedocs.io/t27/c02/sch02/art11/index.html | HMC §27-2043: owner provides key lock on each unit entrance door + at least one key; class A: heavy-duty latch set and heavy-duty dead bolt operable by key outside, thumb-turn inside; chain door guard. §27-2041 peephole. | §5.5, §8.5, §9 landlord Q&A |
| N4 | `NYC Tenant Data Privacy Act smart access systems Local Law 63 of 2021 …` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63/2021: owners of multiple dwellings using smart access may not "require use of a smart access system to gain entry to the tenant's dwelling unit"; express consent before collecting reference data; limited data list; authentication data destroyed within 90 days unless anonymized; no sale; "robust security"; not to be used to harass/evict; private right of action. | §5, §8.5, landlord section, §9, §10.5, FAQ |
| N5 | `NYC Local Law 111 of 2018 self-closing doors …` · WebSearch → WebFetch | https://intro.nyc/local-laws/2018-111 | Doors providing access to interior corridors or stairs in R-1/R-2 must be self-closing; deadline July 31, 2021; failure to maintain = class C immediately hazardous violation, 21 days to correct. | §7.5, §8.5, §9 Q&A |
| N6 | `NYC fire code apartment door double cylinder deadbolt …` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/fire-safety.page | HPD: buildings with 3+ apartments must have self-closing doors; apartment doors should open from inside without a key; "illegal to install double-cylinder locks on apartment doors"; key-locked fire-escape window gates prohibited. | §8.5, §9, §10.5, FAQ |
| N7 | same search | https://habitatmag.com/Publication-Content/Building-Operations/2017/2017-September/Door-Lock-Rules | Deadbolt allowed on apartment entrance but "must be able to open it from the inside without a key"; egress doors openable without a key. | §9 |
| N8 | `NYC Building Code 1010 egress door …` · WebSearch → WebFetch | https://idighardware.com/2026/04/decoded-locks-on-dwelling-units-and-sleeping-units/ | I-Code commentary (Apr 2026): one releasing motion generally; dwelling-unit entry doors may have a second motion for night latch/dead bolt/chain if openable from inside without key or tool; electrified locks must be readily openable from egress side. Model-code commentary — page says NYC code governs locally. | §8.5, §9 single-motion Q&A |
| N9 | `NYC Administrative Code 26-521 unlawful eviction changing locks …` · WebSearch → WebFetch | https://nycadmincode.readthedocs.io/t26/c05/index.html | §26-521: unlawful to remove/plug/render inoperable the entrance-door lock or change it without supplying a key to an occupant of 30+ consecutive days; §26-523 class A misdemeanor, $1,000–$10,000 civil penalty per violation, up to $100/day. | landlord section, §9, §10.5 |
| N10 | `reddit AskNYC landlord smart lock apartment door replaced keys tenant` · WebSearch → WebFetch | https://www.mannpublications.com/mannreportmanagement/2019/05/14/nyc-tenants-sue-landlord-for-physical-key/ | May 14 2019: Hell's Kitchen tenants sued owner for a physical key after Latch install; Latch in ~1,000 NY residential buildings (reported); private settlement; 93-year-old tenant couldn't operate it. (Reddit itself EMPTY — not accessible.) | §5, §13 landmark card, §10.5 |
| N11 | `Atlantic Plaza Towers Brownsville facial recognition …` · WebSearch → WebFetch | https://www.6sqft.com/landlords-plan-to-use-facial-recognition-in-rent-stabilized-complex-alarms-tenants/ | Mar 26 2019: Atlantic Plaza Towers, 700-unit rent-stabilized complex, two buildings, Brownsville; owner Nelson Management sought HCR approval for StoneLock facial-recognition entry; tenants objected in January (privacy, losing access). | §5, §13 landmark card |
| N12 | `NYC Housing Maintenance Code 27-2046.1 intercom …` · WebSearch → WebFetch | https://butterflymx.com/blog/nyc-intercom-law/ | Secondary source: MDL §50-a intercom — class A multiple dwellings with 8+ units (built/converted after Jan 1 1968) need two-way communication at main entrance and remote door release. | §8.5, §9 lobby Q&A |
| N13 | `2023 New York City Housing and Vacancy Survey initial findings …` · WebSearch → WebFetch | https://www.nyc.gov/assets/hpd/downloads/pdfs/about/2024-nychvs-rgb-testimony.pdf | 2023 NYCHVS: 3.7 million housing units; net rental vacancy 1.41%; rent stabilization ~1 million units. (Renter-occupied count not on page — not used.) | §5.5 |
| N14 | carried from research/soundbar-installation.md (Firecrawl, reached by earlier run) | https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2025/05/2025-HSR.pdf ; https://www.coopcity.com/aboutus/ ; https://www.jhbg.org/history-of-jackson-heights ; Park Slope (deniroteam.com) ; St. George (defalcorealty.com) | 54% of units in pre-1947 buildings; Co-op City 15,372 units, 35 high-rises + 7 townhouse clusters, Mitchell-Lama; Jackson Heights Garden Apartments 1917; Park Slope HD 1973/2016; St. George ferry/apartment buildings. | §5.5, §13 landmarks |
| N15 | `NYC co-op condo alteration agreement board approval …` · WebSearch → WebFetch | https://cooperatornews.com/article/alteration-issues | Alterations start with a board request + alteration agreement; small jobs vary by building; board should confirm contractor "licensed and insured"; proof of insurance. (Doors/hardware not mentioned.) | §9 co-op Q&A |
| N16 | `NYC DCWP home improvement contractor license …` · WebSearch → WebFetch | https://nyc-business.nyc.gov/nycbusiness/description/home-improvement-contractor-license | "You need a Home Improvement Contractor License to do construction, repair, remodeling or other home improvement work"; page lists no dollar threshold. Page tells readers to check licences; does NOT claim AESS holds a DCWP HIC licence. | §9 licensing Q&A (flag for Anwar) |
| N17 | `NYC short-term rental registration Local Law 18 …` · WebSearch → WebFetch | https://www.nyc.gov/site/specialenforcement/registration-law/registration.page | LL18 adopted Jan 9 2022; registration for rentals < 30 days; enforcement from Sept 5 2023. | §9 Q&A (smart lock is not a short-term-rental workaround) |
| N18 | `NYC Local Law 75 2009 storefront roll-down gates …` · WebSearch → WebFetch | https://ny1.com/nyc/all-boroughs/news/2026/07/02/city-council-votes-to-repeal-deadline-for-new-roll-down-security-gates | 2009 law: gates ≥70% transparent by July 1 2026; Council unanimously passed Int. 910 (CM Susan Zhuang) repealing the deadline — compliant gate only when replacing for other reasons; DOB permit rules unchanged; goes to Mayor Mamdani. | §8 commercial, §9 storefront Q&A |
| N19 | `NYC SBS list of business improvement districts …` · Firecrawl search | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | BIDs: Fordham Road (Bronx), 125th Street (Manhattan), Fulton Mall Improvement Association (Brooklyn), Steinway Street (Queens), Downtown Jamaica Partnership (Queens), Forest Avenue (SI), Pitkin Avenue (Brooklyn), 86th Street Bay Ridge. | §8 commercial corridors |
| N20 | https://www.nyc.gov/site/sbs/neighborhoods/bids.page · WebFetch | — | EMPTY (permission request not answered in build env) — replaced by N19. | — |
| N21 | Local news (Patch, Brownstoner, TheCity, AMNY, Pix11) / hyperlocal | — | Covered by 6sqft (N11), Mann Report (N10), NY1 (N18). Separate hyperlocal smart-lock story search not run further — EMPTY beyond those. | — |

## Prices used (all from live AESS pages; none invented)

| Figure | Scope it belongs to | Source file |
|---|---|---|
| $1,500–$2,500 installed | single-door keypad or fob reader with electric strike (Brooklyn base) | access-control-installation-bath-beach-brooklyn-ny.html ("SINGLE DOOR" card); access-control-installation-brooklyn.html (vestibule fob reader) |
| $250–$450 | new electric strike on lobby door | door-buzzer-repair-allerton-bronx-ny.html, door-buzzer-repair-hunts-point-bronx-ny.html |
| $295–$485 | failed electric strike repair (lobby intercom that buzzes but won't release) | door-buzzer-repair-bruckner-bronx-ny.html |
| $195/hr, 3-hr minimum ($585) | service/callback rate, not on initial install | blueprint v2.3 §9 |
| $195 Brooklyn/Queens; $225 Bronx/SI; $265 Manhattan first hour | setup-only visit rate | research/tv-mounting-prices/BRIEF.md (line 15) |
| §9 multipliers on $1,500–$2,500 | Manhattan 1.25 → $1,875–$3,125; Queens 1.05 → $1,575–$2,625; SI 1.10 → $1,650–$2,750; Bronx 1.00 | blueprint v2.3 §9 |
| $250–$400, avg $300 | NATIONAL third-party (Fixr) | S1 |
| Apartment-door smart deadbolt install | no AESS figure → "quoted flat at the free walkthrough" | — |
| ~$1,500 8-unit lobby fob example | NOT found by grep in repo → not used | — |

## Question list (NYC hub — lane: renters, landlords, co-op boards, building rules, apartment-door hardware, multi-unit, storefront)

§9 Questions Answered (H3):
1. Can a New York City renter put a smart lock on the apartment door without asking the landlord?
2. Does the landlord get a code or a key to a tenant-installed smart lock?
3. Can my landlord make a phone app the only way into my apartment?
4. What happens to my smart lock when I move out of a rental?
5. Does a co-op board or condo board have to approve a smart lock on my unit door?
6. Can a co-op board insist on a working key when the shareholder goes keyless?
7. Is a keypad deadbolt that needs a key on the inside legal on a New York apartment door?
8. Will a smart lock interfere with the self-closing door the city requires?
9. Can a smart lock go on a steel-clad fire door in a pre-war building?
10. Can a mortise lock on a co-op unit door go smart when the hallway side has to match the building?
11. Can the Wi-Fi bridge or hub go in the public hallway outside my apartment?
12. Should the lobby door and the apartment doors be on the same keyless system?
13. As a small landlord, how do I cut off a former tenant's code without breaking the lockout law?
14. What does the Tenant Data Privacy Act change for an owner adding fob or app entry?
15. What smart lock works on a storefront door behind a roll-down gate?
(Dropped after comparing with sibling hubs: generic mortise-fit, weak-Wi-Fi-at-door, and short-term-rental questions — those intents are on the LI/HV hubs. N17 LL18 research kept but not used on page.)

§17 FAQ:
1. How much does smart lock installation cost in New York City?
2. Do you work on apartment doors in NYCHA developments?
3. Which smart lock brands do you install in NYC apartments?
4. Do you send a certificate of insurance to the managing agent before the visit?
5. Can you work within my building's contractor hours and elevator rules?
6. Can you swap the keyed cylinder on a smart deadbolt when a new tenant moves in?
7. Do you program codes, fobs and phone access for every unit in a small building?
8. What warranty comes with a smart lock installation?
9. Does a smart deadbolt still satisfy the city's deadbolt and chain-guard rule for class A apartments?
10. Do you install smart locks on Long Island and in the Hudson Valley too?

## Images (11, permanent image rule — no real smart-lock photos yet)

| File (images/smart-lock-installation/) | Source |
|---|---|
| smart-lock-installation-nyc-keypad-electric-strike-glass-door.webp (hero) | images/low-voltage/low-voltage-installation-manhattan-electric-strike-keypad.jpg |
| smart-lock-installation-nyc-electric-strike-lobby-door.webp | images/commercial-security/commercial-security-systems-bronx-electric-strike.jpg |
| smart-lock-installation-nyc-fob-reader-mounting.webp | images/low-voltage/low-voltage-installation-bronx-14-access-control-reader-wiring.jpg |
| smart-lock-installation-nyc-strike-terminal-wiring-closeup.webp | images/low-voltage/low-voltage-installation-nyc-13-electric-strike-wiring.jpg |
| smart-lock-installation-nyc-push-to-exit-button-wiring.webp | images/commercial-security/commercial-security-systems-nyc-rex-exit-button.jpg |
| smart-lock-installation-nyc-door-position-contact.webp | images/commercial-security/commercial-security-systems-nyc-door-contact-install.jpg |
| smart-lock-installation-nyc-video-intercom-keypad-wiring.webp | images/low-voltage/low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg |
| smart-lock-installation-nyc-service-van-load-out.webp | images/low-voltage/low-voltage-installation-brooklyn-van-load-out.jpg |
| smart-lock-installation-nyc-maglock-glass-office-door.webp | images/commercial-security/commercial-security-systems-manhattan-maglock.jpg |
| smart-lock-installation-nyc-wave-to-exit-sensor.webp | images/commercial-security/commercial-security-systems-nyc-request-to-exit-sensor.jpg |
| smart-lock-installation-nyc-three-door-controller-panel.webp | images/commercial-security/commercial-security-systems-nyc-door-controller-enclosure.jpg |
Rejected after viewing: dual-entrance-design (readable street address), queens-lobby-video-intercom ("123 Main Street" directory), bronx-access-reader (named business centre on glass), intercom-reception-test (receptionist's face), credential-programming (readable names/checklist), manhattan-secured-lobby (same source as HV builder's secured-lobby image).

---

<!-- source: smart-lock-installation.long-island.part.md -->
# Research — Smart Lock Installation silo · Long Island hub contribution

Built 2026-10-17 (batch run, page: smart-lock-installation-long-island). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Nothing below was inferred to fill a gap.

Thesis: owner-occupied single-family houses with several entry points (front, side/kitchen, garage-to-house, slider, cellar hatch); whole-house code plans; pairing to alarm panels / Z-Wave / Matter hubs; garage openers; salt air on the South Shore/East End; East End seasonal rentals; Nassau vs Suffolk licensing and pricing.

## (a) Silo-wide findings gathered by the Long Island agent

### 1. Reddit (excerpts only — threads not scraped)
- Query: `site:reddit.com r/longisland smart lock OR keypad deadbolt OR "garage door" lock` · Firecrawl search.
  - https://www.reddit.com/r/longisland/comments/bs3afg/trustworthy_locksmith_suffolk/ — excerpt: "I had installed a smart deadbolt … Smart locks aren't anything you need a locksmith for though." → LI §10.5 H3 7 (quoted verbatim).
  - https://www.reddit.com/r/Locksmith/comments/1sbz8ee/fooled_by_a_locksmith/ — excerpt: "Long Island drill out smart lock $165.00 , replace core or just whole deadbolt. Locksmith charged $385". → LI §10.5 H3 7 (described, no figure used).
  - https://www.reddit.com/r/Locksmith/comments/1gqn9ov/375_for_deadbolt_lockout_and_replacement/ — excerpt "$150 for drill-out and $150 for replacement, I'm on Long Island". → context only.

### 2. Google People Also Ask — EMPTY (not accessible in build env)
### 3. Google PASF — EMPTY (not accessible in build env)
### 4. Answer the Public — EMPTY (not accessible in build env)
### 5. Google AI Overview — EMPTY (not accessible in build env)
Substituted with published national cost-guide claims (labelled on page as national third-party data):
- Query: `smart lock installation cost 2025 national average Angi HomeAdvisor` · WebSearch → https://www.fixr.com/costs/smart-lock-installation (WebFetch, updated Jan 31, 2025): national range $250–$400, average $300, low $150, high $1,200; installation $50–$100; keypad unit $100–$250; Z-Wave $250–$400. → LI §10.5 H3 1–2, §14.
- Same search → https://lawnstarter.com/blog/?p=79010 (WebFetch, "2025"): national average $330, range $200–$460, labour $50–$110. → LI §10.5 H3 1–2, §14.
- Angi / HomeAdvisor smart-lock cost pages: not returned by `Angi smart lock installation cost 2025` (WebSearch). EMPTY.

### 6/7. Landmarks / use cases — see Long Island section.
### 8. Bing & DuckDuckGo — EMPTY (not accessible in build env)

### 9. Technical / product / code sources (silo-wide)
- Query: `Schlage smart deadbolt door preparation backset 2-3/8 2-3/4 bore hole 2-1/8 door thickness requirements` · WebSearch → https://kc.allegion.com/kb/article/what-are-the-required-door-preparation-specifications-for-the-schlage-arrive (WebFetch): door 1-3/8"–2", cross bore 1-1/2" or 2-1/8", edge bore 1", backset 2-3/8"/2-3/4", deadbolt throw 1". → LI §7.5, §9 Q, glossary.
- Query: `Schlage Encode Plus specifications batteries 4 AA battery life BHMA Grade 1 Wi-Fi built-in Thread` · WebSearch → https://www.schlage.com/en/home/products/BE499WBCENFFF.html (WebFetch): 2.4 GHz Wi-Fi required; Apple Home Key; 4 AA; "up to six months of battery life with typical use"; ANSI/BHMA A156.40 Grade AAA; 100 codes; door 1-3/8–1-3/4"; backset 2-3/8/2-3/4; operating temp outside −31°F to 150.8°F. → LI §7.5, §9 (Z-Wave/Wi-Fi/Matter Q, winter Q), §10, glossary, §10.5, garage section.
- Query: `Kwikset Aura or Halo smart lock garage entry door Z-Wave 700 specifications battery` · WebSearch → https://res.cloudinary.com/perryhomes/image/upload/v1721415630/HomeConnect-620_gcdwby.pdf (WebFetch): Kwikset Z-Wave 700 lock, 4 AA, 250 user codes, BHMA Grade 2, door 1-3/8"–2". (PDF does not name model; page says "Kwikset's Z-Wave 700 models, for instance".) → LI §9, §10.
- Query: `Ring Alarm Z-Wave smart lock compatibility lock automatically when alarm armed` · WebSearch → https://ring.com/support/articles/9nug0/Arming-or-Disarming-Ring-Alarm-with-your-Smart-Lock (WebFetch): compatible Z-Wave locks arm/disarm; subscription required; "Only codes created in the Ring app will work with this feature." → LI §9 alarm Q, §10.5 H3 3.
- Query: `Matter smart lock Thread border router requirement Yale Schlage Matter over Thread explained` · WebSearch → https://support.shopyalehome.com/en_us/faq-matter-BkfpcDx3yx.md (WebFetch): needs Thread border router (Google/Apple/Amazon/SmartThings list); feature support varies by app; cannot run Yale Access app and Matter app simultaneously; router within 50 ft (25 ft if issues). → LI §9, §10, §10.5 H3 4.
- Query: `Chamberlain myQ blocks third-party integrations Home Assistant 2023` · WebSearch → https://www.home-assistant.io/blog/2023/11/06/removal-of-myq-integration/ (WebFetch): Chamberlain (Oct 2023) "decision to prevent unauthorized usage of our myQ ecosystem through third-party apps"; HA removed integration in 2023.12 (Dec 6, 2023). → LI §9 garage app Q, garage section, earlier-installs list.
- Query: `New York residential code R302.5.1 door between garage and dwelling self-closing solid wood 1-3/8` · WebSearch → https://buildingcodetrainer.com/fire-rated-door-garage-house/ (WebFetch): IRC R302.5.1 — solid wood or solid/honeycomb steel ≥1-3/8", or 20-min rated; self-closing or automatic-closing device. NYS-specific text (Residential Code of NYS) not reached — page says "model residential code". → LI §7.5, §9 garage Q, garage section, glossary.
- Query: `IRC R311.2 egress door readily openable from inside without key special knowledge double cylinder deadbolt New York` · WebSearch → https://idighardware.com/2010/11/double-cylinder-deadlocks-residential/ (WebFetch): R311.2 "Egress doors shall be readily openable from inside the dwelling without the use of a key or special knowledge or effort." NY not discussed. → LI §8.5 free-egress bullet.
- Query: `2010 ADA Standards 404.2.7 door hardware "tight grasping, pinching, or twisting of the wrist" 34 inches 48 inches` · WebSearch → https://idighardware.com/2023/07/accessibility-requirements/ (WebFetch): hardware "must not require tight grasping, pinching, or twisting of the wrist"; mounted 34"–48". → LI §8.5.
- Query: `smart lock salt air corrosion coastal finish marine grade deadbolt recommendation` · WebSearch → https://www.uhs-hardware.com/products/lockey-3210-mechanical-keypad-keyless-digital-combination-deadbolt-lock-scmg-marine-grade-double-combination (WebFetch): "We recommend the Marine Grade Finish for saltwater environments"; "added strength against the corrosive elements of coastal/saltwater environments"; no salt-spray data. → LI §9 coastal finish Q (maker not named on page).

### 10. Yelp 1–3★ — EMPTY (not accessible in build env)

### Pricing (existing approved AESS figures only — no new prices)
- `access-control-installation-long-island.html` (repo grep): "Single-door keypad or card reader with electric strike: $1,500–$2,500 installed". `access-control-installation-staten-island.html` applies the area surcharge to the same figure → treated as Brooklyn base, scaled ×1.15 Nassau ($1,725–$2,875) / ×1.20 Suffolk ($1,800–$3,000). → LI §9 price Q, §14 table, §15 Business card, FAQ 11, Service schema. **Flag for Anwar:** the live LI access-control page shows the unscaled $1,500–$2,500.
- `door-buzzer-repair-olinville-bronx-ny.html` etc.: "new electric strike on lobby door ($250–$450)" → scaled Nassau $288–$518 / Suffolk $300–$540 (round half-up). → §14 table, schema.
- `door-buzzer-repair-soundview-bronx-ny.html` etc.: "failed electric strike, $295–$485 repair" → Nassau $339–$558 / Suffolk $354–$582. → §14 table, schema.
- Blueprint §9: service/callback $195/hr, 3-hr minimum ($585), not on initial install. → §14, FAQ 8.
- research/tv-mounting-prices/BRIEF.md: setup-only visit first hour $225 Nassau / $250 Suffolk, then 30-min blocks (published for TV/device setup; used here for app/hub/pairing visits with no hardware). → repair capture, §9, §14, §15, seasonal section, earlier-installs, FAQ 3/8/10. **Flag for Anwar:** confirm this rate may be used for smart-lock app/hub visits.
- Residential smart deadbolt: no AESS figure → "quoted flat at walkthrough" everywhere (Starter/Standard packages, BYO labour-only).

## (b) ## Long Island hub (smart-lock-installation-long-island)

### Housing / stats (§5.5) — reused from research/soundbar-installation.md (LI section), sources reached there 2026-10-17
- Census QuickFacts Nassau/Suffolk: owner-occupied 81.9% / 82.2%; housing units 480,591 / 583,777 (July 1, 2025). → §5, §5.5.
- https://en.wikipedia.org/wiki/Levittown,_New_York: 17,447 homes 1947–1951. → §5.5, §13.
- https://www.easthamptonstar.com/archive/second-homes-drive-town-economy: 63% of East Hampton houses owned by second-home owners (2017 RKG study). → §5.5.

### Local news / police (§5, garage section)
- Query: `Suffolk County police burglary entered through unlocked garage door 2025` · WebSearch → https://www.cbsnews.com/newyork/news/suffolk-county-burglaries/ (WebFetch, Apr 29, 2016): Hauppauge thieves took garage remotes from unlocked cars, entered through unlocked interior garage doors; advice "Always lock the door between the garage and the house." Also https://www.cbsnews.com/newyork/news/garage-door-burglaries-hauppauge (Dale Ct / Janet Ct). → §5 para 3, garage section.
- Query: `Nassau County police burglary unlocked doors garage entry warning residents lock` · WebSearch → https://abc7ny.com/amp/post/east-hills-woman-discovers-burglars-inside-home-alarm-sounds-police-say/19363419/ (WebFetch, June 23, 2026): Melby Lane, East Hills, ~3:45 a.m. Monday; garage alarm alerted homeowner; advice "don't just lock the door, install deadbolts", take openers out of cars. → §5, garage section.
- https://www.pdcn.org/CivicAlerts.asp?AID=11811 (WebFetch): Aug 25, 2023 Roslyn Heights attempted burglary; NCPD "remind all residents to lock their vehicles and their residence doors." → background (not used on page).
- Query: `PSEG Long Island Tropical Storm Isaias customers without power 2020` · WebSearch → https://abc7ny.com/weather/more-than-300000-lose-power-on-long-island/6353608/ (WebFetch): "almost half of PSEG's 1.1 million customers in the dark at the peak" (Aug 2020). → §5.5, §9 outage Q, §10.5 H3 6.

### Licensing (§8.5, §9)
- Nassau: https://archive.nassaucountyny.gov/agencies/OCA/Licensing/FAQ.html — re-fetch this run was blocked (permission request not answered; EMPTY (not accessible in build env)). Finding reused from research/soundbar-installation.md (fetched 2026-10-17): licence for contractors who remodel RESIDENTIAL homes; commercial-only exempt. → §8.5, §9 licence Q.
- Query: `Suffolk County Consumer Affairs home improvement license requirement contractors` · WebSearch → https://suffolkcountyny.gov/Departments/Consumer-Affairs/Licensing (WebFetch): licenses home improvement contractors; "Search Licensed Contractors" tool. → §9 licence Q.
- Same search → https://riverheadlocal.com/2019/06/25/should-jobs-being-done-by-unlicensed-contractors-be-slapped-with-stop-work-orders/ (WebFetch): county licence for residential repairs/alterations/improvements; written test + liability and workers' comp insurance; civil penalty up to $750 first / $1,500 subsequent; 9,107 licences countywide (2018). → §9 licence Q.

### Seasonal rentals (§5.5, §9, seasonal section)
- Query: `southamptontownny.gov rental permit two-week minimum rental law Southampton Town code` · WebSearch → https://www.southamptontownny.gov/DocumentCenter/View/26504/Rental-FAQs-PDF (WebFetch): permit for any home rented for any period; 14-day minimum; two-year non-transferable permits. No lock/key rules. → §5.5, §9 rental Q, Nassau/Suffolk section.
- Query: `East Hampton rental registry law registration number required advertise` · WebSearch → https://www.ehamptonny.gov/DocumentCenter/View/1337/Additional-Rental-Registry-FAQs-PDF (WebFetch): registration required; registry number must appear in advertisements; $100/2 yrs; no lock/key rules. → §9 rental Q, Nassau/Suffolk section.
- Query: `Town of Southampton rental permit registry short-term rental law requirements` · WebSearch → only bnbcalc.com aggregator pages; not used.

### Commercial corridors (§8) and landmarks (§13) — reused from research/soundbar-installation.md LI section (UBS Arena, Roosevelt Field, Jones Beach, Stony Brook University, Montauk Point Light, Levittown; Hempstead Tpke, Huntington Village/Paramount, Patchogue Main St, North Fork northforker roundup, Route 110). Descriptions rewritten for locks; no new facts added.

### Local news on smart locks specifically (Patch/Newsday/News12) — none found. EMPTY for the service category.
### Hyperlocal — EMPTY beyond the police items above.
### Yelp 1–3★ (LI) — EMPTY (not accessible in build env).
### Housing-stock detail for door prep (Levittown/Cape door specs) — no source found for door dimensions in post-war LI houses; page describes re-drilled doors only as typical field condition, no statistic claimed.

## Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
| File (images/smart-lock-installation/) | Source |
|---|---|
| smart-lock-installation-long-island-keypad-strike-exit-button.webp | low-voltage/low-voltage-installation-long-island-electric-strike-keypad.jpg (same photo also used by NYC hub) |
| smart-lock-installation-long-island-door-controller-cabinet.webp | commercial-security/commercial-security-systems-nyc-access-control-panels.jpg |
| smart-lock-installation-long-island-alarm-sensor-mounting.webp | commercial-security/commercial-security-systems-long-island-glass-break.jpg |
| smart-lock-installation-long-island-gate-reader-wiring.webp | commercial-security/commercial-security-systems-nyc-gate-reader-install.jpg |
| smart-lock-installation-long-island-exterior-enclosure-brick.webp | low-voltage/low-voltage-installation-nassau-county-exterior-enclosure-install.jpg |
| smart-lock-installation-long-island-maglock-header-wiring.webp | low-voltage/low-voltage-installation-long-island-maglock-install.jpg |
| smart-lock-installation-long-island-keypad-reader-mounting.webp | commercial-security/commercial-security-systems-long-island-access-reader.jpg |
| smart-lock-installation-long-island-tone-trace-wall-box.webp | low-voltage/low-voltage-installation-nassau-county-tone-generator-trace.jpg |
| smart-lock-installation-long-island-credential-programming-desk.webp | commercial-security/commercial-security-systems-long-island-credential-programming.jpg |
| smart-lock-installation-long-island-keypad-and-camera-entry.webp | commercial-security/commercial-security-systems-long-island-alarm-keypad.jpg |
| smart-lock-installation-long-island-crew-van-unload.webp | commercial-security/commercial-security-systems-long-island-crew-van.jpg |

## Question register — smart-lock-installation-long-island

### §9 YOUR QUESTIONS ANSWERED (H3)
1. Of the five or six ways into a Long Island house, which ones actually deserve a smart lock?
2. Can the door from the attached garage into the kitchen take a keypad deadbolt without breaking any rule?
3. Should the side door by the driveway use the same code as the front door?
4. Will a new smart lock talk to the alarm panel already on our wall?
5. Z-Wave, Wi-Fi or Matter — which suits a house that already has a hub?
6. Can the overhead garage door and the door locks be run from one app?
7. Our post-war door has been re-drilled for three different locks — is it still sound enough for a smart deadbolt? (rewritten from a mortise-lock question to avoid the NYC hub's pre-war mortise intent)
8. The storm door sits tight against the entry door — will a keypad deadbolt still fit between them?
9. Does a door within sight of the Great South Bay or the ocean need a different lock finish?
10. After a storm like Isaias knocks out PSEG Long Island for days, can we still get in?
11. How should codes work for a Hamptons or North Fork house rented by the fortnight?
12. Can we check the locks on a closed-up Long Island beach house from the city all winter?
13. Does whoever fits our smart locks need a Nassau or Suffolk home improvement licence?
14. Why might the same lock job be priced differently in Nassau and in Suffolk?

### §17 FAQ (visible == FAQPage)
1. Is the walkthrough for a Long Island smart lock quote really free?
2. Does someone need to be home for the whole installation?
3. Should the smart locks go in before or after the alarm company replaces our panel?
4. Do you cover the North Fork, the Hamptons and Montauk as well as Nassau?
5. Will our existing house keys still work after the smart locks go in?
6. What do we need to have ready on installation day?
7. Can you remove the old locks and patch the holes they leave?
8. Is there a charge if you come back to adjust a lock later?
9. Can the keypad be read at night on an unlit side or garage door?
10. What happens to the codes and the app account when we sell the house?
11. Can a Long Island office or shop get keypads on several doors at once?
(Dropped during de-dup against the NYC hub's register: "Do you supply the locks…?", "How long does fitting three locks take?", "What if a lock turns out to be faulty?" (warranty), "Do you handle the alarm company's side…?" (intra-page overlap with §9 Q4).)

### Other question-form headings
- H2 "Locked Out by Your Own Smart Lock on Long Island?" (repair capture)
- H2 "Ready to Walk the House?" (mid CTA)
- H2 "Keypad Dead or Bolt Jammed Tonight?" (final repair capture)

---

<!-- source: smart-lock-installation.hudson-valley.part.md -->
# Research — Smart Lock Installation silo · Hudson Valley hub contribution (2026-10-17)

Page: smart-lock-installation-hudson-valley · GBP Bronx (460 E Fordham Rd) · phone (800) 486-0943 only · up-link Home.
Thesis: remote/second homes and short-term rentals, cold winters vs battery/lock electronics, radio range on large lots and outbuildings, historic/thick/mortise doors, county licensing and county-scaled pricing, small commercial doors.

## (a) Silo-wide findings (usable by every hub)

### Reddit
- Query `smart lock cold weather battery dies winter reddit` · Firecrawl search · excerpts only (Reddit pages not scraped):
  - https://www.reddit.com/r/regina/comments/wlsvok/smart_locks/ — "My current Weiser pin pad lock dies in winter about once every two weeks".
  - https://www.reddit.com/r/AugustSmartLock/comments/rxmn75/keypad_battery_in_cold_weather/ — user uses Energizer lithium; "last longer than alkaline batteries in the cold".
  - https://www.reddit.com/r/homeautomation/comments/up990j/smart_locks_in_canadian_weather/ — battery life "slightly worse during the winter".
  → informed §9 cold/battery questions (no quotes used on page).
- Query `Hudson Valley reddit smart lock second home rental remote access no internet` · Firecrawl search · excerpts: https://www.reddit.com/r/homeautomation/comments/1n55j14/least_internet_connected_smart_lock_has_app_but/ ("Yale Assure Z-Wave locks ... doesn't require Internet"); https://remotelock.com/resource/article/offline-locks. → §9 no-internet question (not quoted).

### Google PAA / PASF / Answer the Public / AI Overview / Bing-DDG / Yelp 1–3★
- EMPTY (not accessible in build env). §10.5 reality check is built from national cost guides + manufacturer pages instead, and says so on the page.

### Manufacturer / technical sources
- Query `Schlage Encode smart lock operating temperature range specifications` · WebSearch → WebFetch https://www.schlage.com/en/home/products/BE489WBCAMFFF.html — outside -31F to 150.8F; inside 14F to 120.2F; 4 AA alkaline; "up to six months of battery life"; door 1-3/8 to 1-3/4 in; backset 2-3/8 or 2-3/4; "Requires 2.4GHz WiFi network"; 100 codes. → §5, §5.5, §9 (cold, batteries, thick doors, radios), §10, §10.5.
- Query `Yale Assure Lock 2 operating temperature specifications battery life` · WebSearch → WebFetch https://images.salsify.com/image/upload/s--tTCgFmbb--/fl_attachment/tjtiz61e7hhrdvjzwajf.pdf (Yale Assure Lock 2 spec sheet) — outside -22F to 140F; inside 5F to 158F; door 1-3/8 to 2-1/4 in; backset 2-3/8 or 2-3/4; Z-Wave module. → §5, §7.5, §9, §10, §10.5.
- Query `Energizer alkaline AA battery cold temperature performance datasheet` · WebSearch → WebFetch https://data.energizer.com/pdfs/liaa_sellsheet_may2010.pdf — Ultimate Lithium AA "Operates from -40 F to 140 F"; chart lithium vs alkaline at 0C (values not in text, not used). → §9 battery question.
- Query `August Connect Wi-Fi bridge placement distance from lock feet` · WebSearch → WebFetch https://support.august.com/en_us/august-connect-improving-your-wi-fi-and-bluetooth-signals-SyqxvL1Adz.md — "within 10–15 feet of your August Smart Lock"; 2.4GHz only. → §5, §5.5, §9 range, §10 table, §10.5.
- Query `Z-Wave Long Range range distance Z-Wave Alliance specification` · WebSearch → WebFetch https://www.ravepubs.com/z-wave-long-range-spec-and-starter-kit-announced-line-of-sight-transmission-is-1-mile (Dec 17 2020) — "line of sight transmission range of 1 mile"; spec "up to several miles". → §9 barn-range question (stated as open-air test figure).
- Query `Schlage Encode Plus Thread Matter Apple Home Key requires home hub border router` · WebSearch → WebFetch https://www.cultofmac.com/761645/schlages-new-smart-lock-first-to-support-apple-home-key/ — connects over Thread via border router (HomePod mini / Apple TV 4K); stabler connection, better battery. → §9 radio comparison, §10.
- Query `igloohome algoPIN offline PIN codes no internet how it works` · WebSearch → WebFetch https://www.igloohome.co/blog/smart-lock-without-internet (June 15 2016) — shared per-lock "formula", app converts "grant access to this guest for 2 days" into a PIN. → §9 no-internet question, §10.
- Query `August Wi-Fi Smart Lock compatible with mortise locks thumbturn retrofit` · WebSearch → WebFetch https://www.slashgear.com/august-smart-lock-mortise-kit-is-the-first-of-its-kind-in-north-america-05469944 (Jan 5 2017) — mortise kit converts mortise-style lock. → §7.5, §9 thick-door question.

### National third-party cost data (labelled as national, not AESS)
- Query `Angi how much does it cost to install a smart lock national average` · WebSearch → WebFetch https://www.fixr.com/costs/smart-lock-installation (updated Jan 31 2025) — national average $300; range $250–$400; labour $50–$100. → §10.5, §14, §15.
- Query `Angi smart lock installation cost 2026` · WebSearch → WebFetch https://homewyse.com/maintenance_costs/cost_to_install_smart_lock.html — $94.71–$227 per lock (Jan 2026), excludes GC markup/tax/permits. → §10.5, §14.
- Angi's own smart-lock cost page: not returned by search → EMPTY.

### Pricing (approved AESS figures only — verified by grep in repo)
- Single-door keypad or fob reader with electric strike $1,500–$2,500 — access-control-installation-bronx.html ("SINGLE DOOR $1,500 – $2,500 Keypad or fob reader with electric strike"; "Bronx pricing is Brooklyn base").
- New electric strike on lobby door $250–$450 — door-buzzer-repair-allerton-bronx-ny.html.
- Failed electric strike repair $295–$485 — door-buzzer-repair-bathgate-bronx-ny.html.
- Setup-only first hour $235 Westchester/Rockland, $250 Orange/Putnam, $275 Dutchess/Ulster, then 30-min blocks — research/tv-mounting-prices/BRIEF.md line 15.
- Service/callback $195/hr, 3-hr minimum ($585), not on initial install — blueprint §9.
- §9 multipliers applied to the three ranges (round half-up): W 1.25 → $1,875–3,125 / $313–563 / $369–606; R 1.30 → $1,950–3,250 / $325–585 / $384–631; O 1.40 → $2,100–3,500 / $350–630 / $413–679; P 1.45 → $2,175–3,625 / $363–653 / $428–703; D/U 1.53 → $2,295–3,825 / $383–689 / $451–742.
- NOT used (for Anwar's review): access-control-installation-hudson-valley.html publishes its own HV figures ("short-term rental ... keyless entry for $800 to $1,800 per door installed", "Schlage Encode keypad ... Budget: $200–$600", "single-door setup at a weekend home ... $1,200 to $2,500", surcharge "+25%/+30%/+35%") that conflict with the §9 multipliers.
- Residential standalone smart deadbolt: no AESS figure → "quoted flat at the free walkthrough".

## (b) ## Hudson Valley

### Short-term rentals / registry
- Query `Ulster County short-term rental registry law 2025` · WebSearch → WebFetch https://comptroller.ulstercountyny.gov/publication/ulster-county-comptrollers-short-term-rental-report-2025/ (Sep 22 2025) and https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf — 2,827 STR units May 2025 = 3.28% of housing; peak 3,310 Oct 2023; Shandaken 9.76% (261 of 2,675); Shandaken, Woodstock, Gardiner, Denning >7%; at least 16 municipalities regulate STRs; registry required unless county opts out. → §5, §5.5, §8 county (Ulster), §9 registry Q, §10.5.
- Query `New York State short-term rental registry law signed Hochul county registry requirements 2025` · WebSearch → WebFetch https://www.nysac.org/media/dhchq0e0/str-faq-3-28-25.pdf — Chapter 99 of Laws of 2025 (S.820/A.5686) signed Feb 28 2025; counties opted in unless they opt out; platforms verify registration; hosts self-attest to health/safety (fire extinguishers as example) and insurance. → §9 registry Q, §10.5.
- Query `Dutchess County short-term rental registration law` · WebSearch → WebFetch https://dec.ny.gov/news/environmental-notice-bulletin/2025-06-11/seqr/town-of-pleasant-valley-short-term-rental-law — Town of Pleasant Valley (Dutchess) STR licensure/regulation, negative declaration, ENB 06/11/2025. → §8 county (Dutchess), §10.5.
- Dutchess County-level STR rule: none found → EMPTY. Woodstock local law search results (hudsonvalleyone.com 2018 articles, woodstockny.gov file) not opened → not used.

### Climate
- Query `Poughkeepsie NY January average low temperature climate normals NOAA` · WebSearch → WebFetch https://weather.gov/media/aly/Climate/LCD/POU/Annual/CLAPOU_2022.pdf — Poughkeepsie 2022: lowest -3F on 01/30; 134 days min ≤32F; 3 days min ≤0F. → §5, §5.5, §9 cold Q.

### Power / broadband
- Query `Central Hudson customers without power storms July 2026 Daily Freeman` · Firecrawl search (WebFetch of the article was blocked: PROVENANCE_REQUIRED) → excerpts: https://www.dailyfreeman.com/2026/07/05/nearly-50000-central-hudson-customers-without-power-after-storms-hit-region/ and Freeman Facebook post "Nearly 50,000 Central Hudson customers were without power Sunday morning". → §9 outage Q.
- Query `Ulster County ConnectALL $20.8 million broadband unserved locations` · Firecrawl search (WebFetch blocked) → excerpt https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion — $20.8M ConnectALL, nearly 1,300 unserved households, businesses, community facilities. → §5.5, §9 no-internet Q.

### Licensing
- Query `Westchester County Department of Consumer Protection home improvement license requirement` · WebSearch → WebFetch https://www.westchestercountyny.gov/all-press-releases/westchester-county-consumer-protection-department-warns-residents-for-spring-contracting-season — "all home improvement contractors are properly licensed to work in Westchester"; Article XVI County Law; green bumper sticker; ask to see licence. → §8 county, §9 licensing Q.
- Query `Rockland County home improvement contractor license consumer protection` · WebSearch → WebFetch https://www.rocklandcountyny.gov/home/showpublisheddocument/6348/639026169869900000 — Chapter 286 Laws of Rockland County; Office of Consumer Protection, Pomona; classification 19 "Locksmiths: Locks, Security gates, Home Safes, Security Screens"; classification 02 low voltage; HI licence ≠ electrical licence. → §8 county, §9 licensing Q.
- Query `Putnam County NY home improvement license consumer affairs` · WebSearch → WebFetch https://putnamcountyny.gov/laws/item/local-law-no-10-of-2013-amend-chapter-135-code-of-putnam-county-entitled-contractors — Ch. 135: no home improvement business without registration; Director of Consumer Affairs, Weights and Measures. → §8, §9.
- Orange / Dutchess / Ulster county-level HI licence: not confirmed from a county source → EMPTY; page tells readers to check with the town. (cat6-installation-hudson-valley.html mentions Orange Consumer Affairs in Goshen without a source URL — not reused.)

### Historic districts
- Query `Kingston NY historic landmarks preservation commission certificate of appropriateness doors hardware` · WebSearch → WebFetch https://kingston-ny.gov/content/8399/8491/8499/ — five local districts (Stockade, Rondout-West Strand, Chestnut Street, Fair Street, Wilbur); exterior work visible from public right-of-way reviewed before building permit; examples windows/siding/new construction/site work; doors/hardware not mentioned (page says so). → §9 historic-district Q.

### Landmarks (§13) — each WebSearch + WebFetch
- https://en.wikipedia.org/wiki/Huguenot_Street_Historic_District — New Paltz, settled 1678, seven stone houses, NHL Oct 9 1960, 10 acres.
- https://en.wikipedia.org/wiki/Mohonk_Mountain_House — Smiley twins; built 1869–1910; New Paltz/Marbletown/Rochester; Lake Mohonk; NHL June 24 1986.
- https://en.wikipedia.org/wiki/Boscobel_(mansion) — built 1804–1808 for States Dyckman in Montrose; saved 1955; moved to Garrison (Putnam) 1956; Federal style.
- https://en.wikipedia.org/wiki/Bear_Mountain_State_Park — 5,205 acres, Rockland and Orange, opened June 1913, Inn 1915.
- https://lyndhurst.org/history — A. J. Davis, designed 1838, Gothic Revival, Jay Gould, 67 acres, 635 South Broadway Tarrytown.
- https://en.wikipedia.org/wiki/Vanderbilt_Mansion_National_Historic_Site — built 1896–1899, McKim, Mead & White, Frederick and Louise Vanderbilt, 211 acres of ~600, Hyde Park.

### Commercial corridors (§8)
- Corridor names (I-287 office parks White Plains/Harrison/Purchase/Rye Brook/Elmsford/Tarrytown; Route 59 Nanuet/Spring Valley/West Nyack; Newburgh/Route 300/Stewart/I-84–I-87; Poughkeepsie–Wappingers–Fishkill Route 9; Kingston/Beacon) taken from the repo's own MANIFEST-site-rebuild-187.md local-detail list; no statistics attached.

### Local news / hyperlocal in the service category (smart locks) — none found → EMPTY. Yelp 1–3★ → EMPTY.
### Field Notes — no sourced HV smart-lock anecdote → written as general practice, labelled as such.

## Images (11, permanent image rule — no Drive/CompanyCam photos)
| File (images/smart-lock-installation/) | Source |
|---|---|
| smart-lock-installation-hudson-valley-van-load-out-ladders.webp | images/low-voltage/low-voltage-installation-hudson-valley-van-load-out.jpg |
| smart-lock-installation-hudson-valley-maglock-terminal-wiring.webp | images/low-voltage/low-voltage-installation-hudson-valley-13-maglock-wiring-detail.jpg |
| smart-lock-installation-hudson-valley-door-contact-keypad-panels.webp | images/commercial-security/commercial-security-systems-dutchess-panic-button.jpg |
| smart-lock-installation-hudson-valley-keypad-intercom-stone-pillar.webp | images/commercial-security/commercial-security-systems-dutchess-hero-video-intercom.jpg |
| smart-lock-installation-hudson-valley-wall-plate-termination.webp | images/low-voltage/low-voltage-installation-dutchess-county-06-keystone-wall-plate.jpg |
| smart-lock-installation-hudson-valley-secured-lobby-entry.webp | images/commercial-security/commercial-security-systems-dutchess-secured-lobby.jpg |
| smart-lock-installation-hudson-valley-stud-wall-cable-rough-in.webp | images/low-voltage/low-voltage-installation-hudson-valley-stud-rough-in-boxes.jpg |
| smart-lock-installation-hudson-valley-storefront-frame-sensor.webp | images/commercial-security/commercial-security-systems-dutchess-entrance-crew.jpg |
| smart-lock-installation-hudson-valley-entry-panel-wiring.webp | images/low-voltage/low-voltage-installation-putnam-county-13-lobby-video-intercom.jpg |
| smart-lock-installation-hudson-valley-open-framing-cable-pull.webp | images/low-voltage/low-voltage-installation-hudson-valley-02-metal-stud-rough-in.jpg |
| smart-lock-installation-hudson-valley-conduit-pull-block-wall.webp | images/commercial-security/commercial-security-systems-hudson-valley-conduit-pull.jpg |
None of these source photos (by hash) were used for the 11 Long Island smart-lock images on disk at build time.

## Question register — smart-lock-installation-hudson-valley
§9 Q&A (H3 questions):
1. We live two hours away from our Ulster or Dutchess rental — what has to be in place before guest codes can be run reliably from the city?
2. Does New York's new short-term rental registry change how I should run guest access?
3. When the rural internet or the router goes down at an empty weekend house, which lock features keep working and which stop?
4. Can I see who came and went at my country house without signing up for a monitoring contract?
5. How cold can it get before a smart lock on an exposed Hudson Valley door stops working?
6. Why do smart lock batteries die faster in a Catskills or Taconic winter, and which batteries should go in?
7. Will ice, snow and a door that swells in winter jam a motorized deadbolt?
8. My router is in the house and the lock is on a barn or garage 200 feet away — how do we connect it?
9. Can a smart lock work at a property with no internet at all?
10. Our nineteenth-century front door is thicker than most smart locks are listed for — what are the options?
11. Do I need historic-district approval to put a keypad on a door in Kingston's Stockade or another landmark district?
12. What is the best way to lock a detached garage, workshop or barn that has no power at the door?
13. Can a cleaner's code open the guest cottage but not the barn or the main house?
14. Why does the same smart lock job cost more in Ulster or Dutchess than in Westchester?
15. Which county licences should a smart lock installer hold in the Hudson Valley?
16. Can a small office-park suite or studio use smart locks instead of a full access control system?
17. What does a farm winery or tasting room need on the door between the public space and storage?
(Non-question H3: "Choosing between Wi-Fi, Z-Wave, Thread and Bluetooth when the signal at the door is weak".)
§17 FAQ (visible == FAQPage, 9):
1. What does a single-door keypad with an electric strike cost in each Hudson Valley county?
2. How much is a visit just to program a smart lock that is already on the door?
3. Can you quote a far-valley job from photos so nobody makes the drive twice?
4. Should the router and lock bridge be on our standby generator?
5. Can you install a smart lock at a house that is closed up for the winter?
6. Can you work on a weekend when we are up at the house?
7. Is a second smart lock on a garage or cottage door cheaper if done on the same visit?
8. Who programs the guest codes after you leave?
9. Can you service a rental's lock between one guest's checkout and the next check-in?
Other question-form headings: "Smart Lock Offline or Jammed at a Hudson Valley Property?", "Guest Locked Out at a Hudson Valley Rental Tonight?"

De-dup vs smart-lock-installation-long-island.html / -nyc.html on disk at ~03:46: replaced HV FAQs that matched LI/NYC intents (free walkthrough; someone home during install; supply-or-buy lock; post-install callback); reworded HV Q&A that overlapped (LI "one app for garage door and locks" → per-building code permissions; LI "Z-Wave/Wi-Fi/Matter with a hub" and NYC "concrete building Wi-Fi" → radio comparison made a non-question heading; NYC "pre-war mortise options" → door-thickness question). Remaining partial overlaps for the main run to judge: HV Q1 remote rental codes vs LI "codes for a Hamptons house rented by the fortnight"; HV Q3 outage vs LI "after a storm like Isaias ... can we still get in?"; HV Q14/Q15 county pricing/licensing vs LI Nassau/Suffolk pricing/licensing (geo-specific by design per the lane brief).
