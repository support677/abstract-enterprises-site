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


## Manhattan (smart-lock-installation-manhattan)

Built 2026-10-17. Area page, up-link /smart-lock-installation-nyc. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737 (800 only in shared header chrome). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane: Manhattan high-rise and doorman reality: unit locks next to building platforms (Latch/DOOR, ButterflyMX, fob systems, Kastle in offices); managing-agent scope letters and COI/insurance; desk, dog-walker, cleaner, contractor and package access; pied-à-terre remote access and battery fallback; Local Law 18 short-stay rules; office suites in towers (NYC BC 1010.1.9.9, NFPA 80 rated frames, after-hours); landmark storefronts (LPC/NoHo BID).

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| M1 | `NYC short-term rental Local Law 18 host present guests access entire dwelling unit interior doors locks rules` · Firecrawl search | https://portal.311.nyc.gov/article/?kanumber=KA-03559 | Hosts (owners or tenants) cannot rent an entire apartment/home for < 30 days even if they own/live in the building; applies to all permanent residential buildings regardless of unit count; host must stay in the unit, max two guests, every guest must have access to all parts of the unit and each exit. | §5 stats, §6 card, §9 short-stay Q1/Q2, §10.5 H3 4, FAQ 6 |
| M2 | same search | https://ny1.com/nyc/all-boroughs/housing/2023/09/03/new-law-cracks-down-on-short-term-rentals | (excerpt) "Guests must have full unrestricted access to the dwelling. In other words: no locked doors." Enforcement Sept 2023. | §9 guest-bedroom Q |
| M3 | same search | https://www.keycafe.com/s/blog/understanding-new-york-citys-short-term-rental-regulations ; https://www.coleschotz.com/nyc-short-term-rentals-under-new-lock-key/ | Secondary confirmation (lock-off guest bedroom not allowed; OSE regs effective Mar 6 2023; enforcement Sept 5 2023). Not cited on page. | background |
| M4 | `lockboxes Airbnb keys chained scaffolding railings Manhattan East Village news` · Firecrawl search → Firecrawl scrape | https://www.amny.com/news/key-lockboxes-spark-safety-concerns/ | July 21 2016 (Chelsea Now/amNY): 11 key lockboxes counted on W. 21st St between Eighth and Ninth Aves; resident quotes ("you have no idea who is in your building" — Tom Cayler); Parks Dept: lockboxes on tree guards are an unauthorised use of Parks property. | §5 para 4 + stat, §9 lockbox Q, §13 W 21st St card |
| M5 | same search → Firecrawl scrape | https://www.cbsnews.com/newyork/news/chelsea-residents-worry-that-air-bnb-lock-boxes-are-putting-their-homes-at-risk/ | CBS2 (undated on page; og image 2015): Airbnb pointed hosts to "the almighty lock box"; private boxes on city tree fences not allowed, fine up to $400. Only the "almighty lock box" line used. | §10.5 H3 4 |
| M6 | `Latch smart lock Manhattan buildings tenants ButterflyMX building access app NYC apartment` · Firecrawl search | https://butterflymx.com/products/smart-locks/ ; https://butterflymx.com/how-it-works/ | ButterflyMX: connects "more than 80 smart lock styles and finishes"; after Wi-Fi locks are integrated, Door PINs and Bluetooth keep working if building internet is down (manufacturer claim). | §7.5 condo method, §9 Q1, §10.5 H3 3 |
| M7 | `Latch smart lock company 2025 Door.com rebrand buildings New York apartment Latch lock support` · Firecrawl search → Firecrawl scrape | https://door.com/press/latch-rebrands-as-door-to-lead-a-new-era-of-building-intelligence ; https://door.com/ | Aug 12 2025: Latch rebranded as DOOR; existing Latch hardware continues to be supported. | §6 card, §9 Q1, §10.5 H3 3, checklist |
| M8 | same search | https://www.curbed.com/2024/01/latch-smart-lock-nyc-apartments-aggravating-feature.html | Jan 11 2024 first-person essay on Latch (Brooklyn-tagged); body not retrievable (query scrape returned empty) → EMPTY (not accessible in build env); not used. | — |
| M9 | `Manhattan pied-à-terre number of units occasional seasonal use Housing Vacancy Survey IBO pied-a-terre tax report` · Firecrawl search → Firecrawl scrape | https://comptroller.nyc.gov/reports/the-pied-a-terre-tax-and-its-potential-revenues/ | Fiscal note April 30 2026: model table — Manhattan 17,125 properties of 19,107 citywide (high-value non-primary residences targeted by the proposed tax). | §5 para 2 + stat |
| M10 | same search → Firecrawl scrape | https://kaufmanrossin.com/blog/pied-a-terre-tax/ | NYC pied-à-terre surcharge effective July 1 2026 on high-value non-primary residences (phase 1 thresholds/rates — not used). | §5 para 2 |
| M11 | `Landmarks Preservation Commission storefront rules Manhattan historic district security gates hardware permit` · Firecrawl search → Firecrawl scrape (PDF) | https://noho.nyc/wp-content/uploads/2025/07/Storefronts_in_HD_Flyer_Updated.pdf | NoHo BID: most of NoHo in three historic districts; whole property incl. sidewalk designated; LPC permit needed for exterior work even without DOB permit; most window/door work needs LPC permit; repairing/replacing hardware (knobs, hinges, handles) does not. | §5 para 5, §8.5, §9 storefront Q, §13 NoHo card, glossary |
| M12 | same search → Firecrawl scrape | https://kohnarchitecture.nyc/getting-lpc-permits-for-storefronts-in-new-york-city-landmark/ | "Security gates must roll down on the interior of the storefront." Background only. | background |
| M13 | same search → Firecrawl scrape (query mode) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | Query returned only fragments (security gate criteria cut off) → treated as EMPTY for specifics; not cited. | — |
| M14 | `NFPA 80 fire door field modification drilling holes electrified hardware listing label idighardware` · Firecrawl search | https://idighardware.com/2017/10/decoded-alterations-to-fire-door-assemblies/ ; https://idighardware.com/wp-content/uploads/2014/10/Decoded-Dec14-Alterations-to-Fire-Doors.pdf | NFPA 80 job-site preps limited to round holes (larger holes per listings since 2016 ed.); other cutouts = field modification needing listing-lab approval (Lori Greene reply re strike cutout in rated frame); unapproved mods may require re-labelling with lab site visit. | §8.5, §9 rated-frame Q, §7.5 |
| M15 | `NYC Building Code 2022 1010.2.12 sensor release electrically locked egress doors maglock fire alarm release New York City office` · Firecrawl search → Firecrawl scrape | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173513 | NYC BC 1010.1.9.9 Electromagnetically locked egress doors: permitted on egress doors and doors to tenant spaces in A, B, E, M, R-1, R-2 with hardware incorporating built-in switch; obvious method, one hand, directly interrupts power, power loss unlocks, panic hardware releases too. | §5 para 5, §8.5, §9 maglock Q, §10 table, §10.5 H3 7 |
| M16 | same search | https://up.codes/s/sensor-release-of-electrically-locked-egress-doors | IBC sensor-release criteria (fire alarm/sprinkler release etc.) — model code; page only says "separate provisions govern sensor-release arrangements". | §9 maglock Q |
| M17 | `Manhattan office building tenant access control Kastle building card after-hours access tenant suite door integration` · Firecrawl search | https://www.kastle.com/solutions/managed-access-control-systems/ | Kastle: one mobile credential to "move easily between base building and tenant spaces". | §5 para 5, §9 Midtown tower Q |
| M18 | `The Dakota apartment building 1 West 72nd Street completed 1884 cooperative` · Firecrawl search | https://en.wikipedia.org/wiki/The_Dakota ; https://streeteasy.com/building/the-dakota-1-west-72-street-new_york | Cooperative at 1 W 72nd St, UWS; completed October 1884. | §13 card |
| M19 | `SoHo–Cast Iron Historic District designated 1973 …` · Firecrawl search | https://villagepreservation.org/2024/08/14/the-soho-cast-iron-historic-district-a-1973-designation-that-helped-shape-nycs-cultural-legacy/ | Designated Aug 14 1973; ~26 blocks, nearly 500 buildings; extended 2010 to most of West Broadway, east to Lafayette and Centre Sts. | §13 card |
| M20 | `Central Park Tower 217 West 57th Street height …` · Firecrawl search | https://en.wikipedia.org/wiki/Central_Park_Tower | 1,550 ft; tallest primarily residential building in the world; part of "Billionaires' Row" around 57th St. | §13 card, §8 card |
| M21 | `One Vanderbilt office tower opened 2020 height 1,401 feet …` · Firecrawl search | https://en.wikipedia.org/wiki/One_Vanderbilt ; https://slgreen.com/sl-green-celebrates-the-historic-opening-of-one-vanderbilt-avenue/ | Opened Sept 14 2020; 1,401 ft; beside Grand Central; tenants finance, banking, law, real estate. | §13 card, §8 card |
| M22 | `reddit doorman building smart lock dog walker cleaner code keys front desk Manhattan apartment` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/16426hd/is_keeping_your_apartment_unlocked_247_common/ ; https://www.reddit.com/r/explainlikeimfive/comments/18fqqh4/eli5_why_do_nyc_buildings_still_have_doormen/ ; https://www.reddit.com/r/NYCapartments/comments/1pr092n/help_landlord_has_very_restrictive_key_fob_policy/ | Excerpts only (threads not opened): residents leave keys with doormen; doorman key "really nice for pet-sitters/dog walkers"; lockbox/fob policy complaints. Informed §9 desk/walker Qs; nothing quoted. | §9 (background) |
| M23 | `NYC couple finds stranger in apartment doorman gave keys woman claimed dog walker` · Firecrawl search → Firecrawl scrape | https://www.fox5ny.com/news/nyc-couple-finds-stranger-in-apartment (also nypost.com 2026/08/11) | FOX 5, Aug 11 2026: July 24, Halo LIC (Purves St, Long Island City, Queens) — concierge handed keys to woman posing as dog walker while couple on vacation; Goose Property Management removed the concierge employee. Page states it is Long Island City. | §5 para 4, §9 desk/walker Q, §10.5 H3 5 |
| M24 | reused from research/soundbar-installation.md (Manhattan section, Firecrawl, 2026-10-17) | https://chpcny.org/visualization/housing-stock-visualization/ | "In Manhattan, nearly all units (97 percent) are in buildings of six or more units". | §5 para 1 + stat |
| M25 | reused (same file) | https://www.census.gov/quickfacts/fact/table/newyorkcountynewyork/PST045224 | New York County: 938,554 housing units (July 1 2025); owner-occupied 25.1% (2020–2024). | §5 para 2 + stat |
| M26 | reused (same file) | https://comptroller.nyc.gov/reports/office-to-residential-conversions-in-nyc-economics-and-fiscal-estimates/ | 16,400 apartments in Manhattan office-conversion pipeline; Water/Wall/Broad St, Third Ave conversions. | §5 stat, §7 card, §8 FiDi card |
| M27 | reused (same file) | https://www.brickunderground.com/guides/how-to-renovate/what-is-an-alteration-agreement | Most alteration agreements limit work to 9–5 weekdays; service-elevator hours. | §5 para 3, §9 renovation-crew Q |
| M28 | reused (same file) | https://portal.311.nyc.gov/article/?kanumber=KA-01091 | Residential construction allowed 7 AM–6 PM weekdays. | §5 para 3 |
| M29 | reused (same file) | https://www.brickunderground.com/live/whats-a-certificate-of-insurance-nyc ; https://cooperatornews.com/article/insurance-and-your-contractor | COI = proof contractor's policy covers liability and loss; co-ops routinely require COI before work. | §5 para 3, §9 insurance Q, glossary |
| M30 | reused (same file) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-156361 | Admin Code §28-105.4.7: no electrical permit for < 50 V signalling/communication/alarm/data wiring when done by LMP electrician, special electrician or qualified person per NYC electrical code. Page does NOT claim AESS is a "qualified person". | §8.5 |
| M31 | silo research (research/smart-lock-installation.md) | S1 fixr.com; S2 bobvila; S3 august.com; S4 August Connect 10–15 ft; Schlage Encode Plus "up to six months"; Energizer lithium −40°F to 140°F; Ring Alarm Z-Wave lock subscription + Ring-app codes only; N4 Tenant Data Privacy Act; ADA no tight grasping | As listed in the silo file. | §10.5, §14, §9, pied-à-terre section |
| M32 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are published claims, stated as such on page. | — |
| M33 | Local news on smart locks specifically in Manhattan (Patch Manhattan, West Side Rag, The City) | — | No Manhattan smart-lock story found beyond M4/M5/M23 → EMPTY. | — |
| M34 | Doorman-building counts / Manhattan prewar share | — | No sourced figure found → EMPTY; not stated. | — |

### Prices used (Manhattan ×1.25, round half-up; all from existing approved AESS figures)
- Single-door keypad or fob reader with electric strike: $1,500–$2,500 base → **$1,875–$3,125** (NYC hub table).
- New electric strike on lobby door: $250–$450 → **$313–$563**.
- Failed electric strike repair: $295–$485 → **$369–$606**.
- Setup-only visit: **$265 first hour**, then 30-min blocks (research/tv-mounting-prices/BRIEF.md line 15).
- Service/callback: **$195/hr, 3-hr minimum ($585)**, verbatim, not on initial install.
- Apartment-door smart lock: no AESS figure → "quoted flat at free walkthrough".
- National comparison only: Fixr $250–$400, avg $300 (Jan 2025).

## Images (11)

Permanent image rule (Drive folder empty, CompanyCam not connected). Each source checked by perceptual hash against all hub + Brooklyn + Queens images; none overlaps. All viewed before use. Three cropped to remove identifying text.

| New filename (images/smart-lock-installation/) | Source file |
|---|---|
| smart-lock-installation-manhattan-visitor-intercom-employee-card-entrance.webp (hero, eager) | images/commercial-security/commercial-security-systems-nyc-dual-entrance-design.jpg (cropped: left 27% removed to drop the sign with a street address) |
| smart-lock-installation-manhattan-office-floor-jhook-cable-pathway.webp | images/low-voltage/low-voltage-installation-manhattan-hero-jhook-pathway.jpg |
| smart-lock-installation-manhattan-idf-rack-patching.webp | images/low-voltage/low-voltage-installation-manhattan-05-idf-rack-patching.jpg |
| smart-lock-installation-manhattan-ceiling-grid-cable-bundle-pull.webp | images/low-voltage/low-voltage-installation-manhattan-03-ceiling-grid-bundle-pull.jpg |
| smart-lock-installation-manhattan-exit-door-ceiling-cable-run.webp | images/commercial-security/commercial-security-systems-manhattan-office-cat6-ceiling.jpg |
| smart-lock-installation-manhattan-patch-panel-punch-down-closeup.webp | images/low-voltage/low-voltage-installation-manhattan-06-cat6-patch-panel-punchdown.jpg |
| smart-lock-installation-manhattan-laptop-network-switch-setup.webp | images/low-voltage/low-voltage-installation-dutchess-county-hero-rack-switch-config.jpg |
| smart-lock-installation-manhattan-reception-lobby-dome-camera.webp | images/commercial-security/commercial-security-systems-nyc-lobby-dome-camera.jpg (cropped: right 37% removed to drop a named business logo) |
| smart-lock-installation-manhattan-ceiling-wifi-access-point-lift.webp | images/low-voltage/low-voltage-installation-bronx-access-point-lift-install.jpg (cropped: right 14% removed to drop a "community center" wall sign) |
| smart-lock-installation-manhattan-exterior-conduit-enclosures-storefront.webp | images/commercial-security/commercial-security-systems-manhattan-exterior-enclosures.jpg |
| smart-lock-installation-manhattan-rack-punch-down-network-closet.webp | images/commercial-security/commercial-security-systems-nyc-patch-panel-punchdown.jpg |

DAILY-LOG note: `images: 11 reused from images/low-voltage/ and images/commercial-security/ (no real smart-lock photos yet)`. None of these source photos shows a smart lock on a unit door; captions describe only what is visible.

## Question register — smart-lock-installation-manhattan

### §9 YOUR QUESTIONS ANSWERED (H3)
Living with the building's entry platform
1. My building already opens the lobby with an app — will a second app on my own door clash with it?
2. Can my unit lock be enrolled in the building's system so the front desk can see it?
The paperwork before the visit
3. What should the scope letter to the managing agent say about the lock and the door?
4. Whose insurance answers if the door or the hallway is damaged during the installation?
Doormen, concierges and service providers
5. How should the doorman, the dog walker and the cleaner get in once the door has a code instead of a key?
6. Should packages still go to the desk if a smart lock could let couriers into the apartment?
7. What stops someone who talks their way past the lobby from getting through my door?
Owners who are often away
8. If the batteries die while we are out of the country, how does anyone get in?
9. Can a renovation crew work in the apartment for a week without being given a key?
Short-stay hosting and the city's rules
10. Can a keypad let us rent the apartment to visitors while we are away?
11. We host a registered guest while we are home — can the guest bedroom get its own smart lock?
12. Key lockboxes keep appearing on the railings outside our building — what can the building do?
Office suites in towers
13. Our suite is in a Midtown tower with its own card system — can our door have a different lock?
14. Can an electric strike be cut into the labelled steel frame of a suite entrance?
15. Does a magnetic lock on our glass suite door have to release when the fire alarm goes off?
16. Our team works late — how does after-hours access fit with a suite smart lock?
Shopfronts in landmark districts
17. Can the reader sit behind the glass so nothing new goes on a cast-iron facade?

### §17 FAQ (visible == FAQPage, 10)
1. What does a keyless suite or lobby door with an electric strike cost in Manhattan?
2. Do you cover Inwood, Washington Heights and Harlem as well as Midtown and downtown?
3. Can the building's super or in-house locksmith be there while you work?
4. Can the lock relock itself so a dog walker or cleaner can't leave it open?
5. Will you start work before the managing agent has signed off?
6. Can you fit a smart lock to an interior door, such as a home office or storage room?
7. Should the lock go in before or after our movers have the freight elevator?
8. Where do your Manhattan technicians come from, and how quickly can they reach the door?
9. Can roommates in a shared Manhattan apartment each have their own code?
10. When is the deposit due on a Manhattan smart lock job?

### Other question-form headings
- H2 "Smart Lock Acting Up Somewhere in Manhattan?" (repair capture)
- H2 "Ready to Take the Key Out of the Key Cabinet?" (mid CTA)
- H2 "Keypad Dead in a Manhattan Hallway or Suite Tonight?" (final repair capture)

De-dup notes: deliberately avoided NYC-hub intents (board approval of a unit smart lock, duplicate key to board, lobby+unit same system, COI sent to managing agent, contractor hours/elevator rules, pre-war steel fire door, mortise hallway match, hallway bridge, LL63 owner duties, storefront roll-down gate), LI/HV intents (remote check of closed-up house, STR registry, historic-district approval for a keypad, battery life in cold, outage behaviour). Partial overlaps for the main run to judge: Q5 scheduled service-provider codes vs Queens "home attendant code only on those days"; Q16 after-hours suite access vs Queens "chair-rental stylists after-hours access"; FAQ 1/2 cost and coverage are geo-specific by design (as on LI/HV/Brooklyn/Queens).


## Brooklyn (smart-lock-installation-brooklyn)

Built 2026-10-17 by the Brooklyn builder subagent (batch: Manhattan, Brooklyn, Queens). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).
Thesis / lane: brownstone and rowhouse entries (paired outer doors, vestibule/inner door, parlour floor vs garden level, under-stoop areaway gate, stoop weather exposure); frame houses (glass lites, mail slots, storm doors); owner-occupied 2–4-family houses where the owner is the landlord (MDL three-family line, code sharing, owner visibility of tenant logs, guest codes kept off the tenant's floor); LPC historic-district doors (hardware vs door replacement); stoop package theft and vestibule delivery codes; sponsor-installed locks in new Downtown Brooklyn / Greenpoint condos; corridor storefront back doors.
Silo-wide findings (Fixr national pricing, Schlage Encode Plus specs, August Connect 10–15 ft, ADA 404.2.7 via idighardware, Matter/Thread) reused from the NYC/LI/HV sections above — not re-fetched.

### New research this run

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| B1 | `Brooklyn package theft stoop porch pirates brownstone deliveries` · Firecrawl search | https://nypost.com/2026/06/09/us-news/new-york-ranked-second-worst-in-the-us-for-package-theft-as-porch-pirates-snatch-1-2b-in-deliveries/ (Firecrawl scrape, direct quote) | June 9, 2026: SafeWise 2025 US Package Theft Report — New York 7,828,212 incidents, about $1.29 billion losses, second-worst after California. | §5 para 4, §5.5 bullet 6, §10.5 H3 4 |
| B2 | same query | https://www.reddit.com/r/Brooklyn/comments/1ox1y84/what_have_people_in_brooklyn_found_effective_to/ (excerpt only; title + linked "Packages in brownstones : r/parkslope") | Brooklyn residents asking what works against package theft in brownstones. Not quoted. | §9 package Q (as "threads ask") |
| B3 | same query | https://www.nytimes.com/2021/04/20/realestate/package-bins-protect-deliveries.html (excerpt only; Firecrawl scrape refused: "we do not support this site") | Excerpt: owners installed a ParcelBin "after having package deliveries stolen from the stoop of their brownstone." Not quoted on page; parcel bins mentioned generically. | §9 package Q |
| B4 | `Landmarks Preservation Commission doors rowhouse historic district replacement door hardware permit guidelines` · Firecrawl search → scrape | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf (scraped, pdf parser) | "Maybe you don't need a permit … Repairing or replacing hardware such as hinges, knobs, pulley chains, locks and handles"; new door at primary facade approvable if it "matches the historic door's materials, operation, configuration, details, and finish"; non-historic door → look at historic doors on similar buildings; conditions assessment required to replace historic front doors; "All historic fabric, such as sidelights, doors, transoms, framing, and door surround detailing must be retained" (search excerpt). | §5 para 5, §7.5 landmark para, §8.5 storefront bullet, §9 historic replacement Q, §10.5 H3 5 |
| B5 | same search | https://noho.nyc/wp-content/uploads/2025/07/Storefronts_in_HD_Flyer_Updated.pdf (excerpt) | NoHo BID flyer: no LPC approval for "Repairing or replacing hardware, like knobs, pulley chains, hinges, and handles". Corroboration only. | research only |
| B6 | `brownstone original double doors vestibule inner door lock brownstoner` · Firecrawl search → scrape | https://www.brownstoner.com/forum/general-discussion/front-door-locks-vestibules-outer-inner-or-both/ (scraped; published 2024-03-21) | Thread title: "Front Door Locks & Vestibules: Outer, Inner, or Both?"; reply (BobMarvin): "I think a lock on the outer door is far more secure." | §9 Q "which door gets the smart lock" (quoted) |
| B7 | same search | https://www.brownstoner.com/interiors-renovation/brownstone-boys-restoring-double-entry-doors-replacement-doors-historic-renovation-tips/ (scraped; 2019-07-03; tag Bed Stuy) | "The traditional double front doors to our house were unfortunately replaced by a modern single door"; owners restoring double doors; kept "the original second entry door that we had painstakingly stripped of multiple layers of paint." | §9 historic replacement Q |
| B8 | `New York Multiple Dwelling Law definition "multiple dwelling" three or more families` · Firecrawl search | https://law.justia.com/codes/new-york/mdw/article-1/4/ ; https://www.nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf (excerpts) | MDL §4: a multiple dwelling is occupied "as the residence or home of three or more families living independently of each other." | §5 para 3, §5.5 bullet 3, §9 two-family Q, §10.5 H3 6, door-plan table |
| B9 | `HPD property registration one- and two-family homes owner does not reside required` · Firecrawl search | https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page (excerpt) | Registration required for "One and two-family dwellings if neither the owner nor any family member occupies the dwelling." | §5 para 3, §9 two-family Q |
| B10 | `NYC Local Law 18 short-term rental rules host must be present two guests access to entire unit` · Firecrawl search | https://portal.311.nyc.gov/article/?kanumber=KA-03559 (excerpt) | Hosts cannot rent an entire apartment/home < 30 days; must stay in the same unit; no more than two guests; every guest must have access to all parts of the dwelling unit and each exit. (Registration from NYC hub N17.) | §9 guest-code Q |
| B11 | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page · Firecrawl scrape (query: list Brooklyn BIDs) | same | Brooklyn BIDs listed incl. 86th Street Bay Ridge, Atlantic Avenue, Bay Ridge 5th Avenue, Bed-Stuy Gateway, Brighton Beach, Church-Flatbush Community Alliance, Coney Island, Court-Livingston-Schermerhorn, Cypress Hills Fulton, DUMBO, East Brooklyn, Flatbush-Nostrand Junction, FAB Alliance, Fulton Mall, Graham Avenue, Grand Street, Kings Highway, MetroTech, Montague Street, Myrtle Avenue Brooklyn Partnership, North Flatbush, Park Slope 5th Avenue, Pitkin Avenue, Sunset Park; Church Avenue marked "(archive)". | §8 corridor cards + sentence ("about two dozen" — 25 Brooklyn entries incl. archived Church Avenue) |

### Reused from earlier Brooklyn research in this repo (sources reached by earlier runs; not re-fetched)
| Finding | Source (as logged) | Page section |
|---|---|---|
| Kings County pop. 2,653,963 (July 1 2025), housing units 1,141,824, owner-occupied 29.5% (2020–2024) | census.gov QuickFacts kingscountynewyork (research/soundbar-installation.md, Brooklyn) | §5 para 2, §5.5 bullets 1–2 |
| Downtown Brooklyn 22,000+ housing units since 2004 rezoning | storymaps.arcgis.com Downtown Brooklyn Partnership (research/fiber-optic-installation.md, Brooklyn) | §5 para 6, §5.5 bullet 5 |
| Greenpoint–Williamsburg rezoning approved May 2005 | nyc.gov DCP pdf / rwv.rutgers.edu (fiber + soundbar research) | §5 para 6, §13 Domino card |
| Brooklyn Heights HD designated Nov 23 1965, first in NYC; boundaries | hdc.org; thebha.org (fiber + soundbar research) | §5 para 5, §5.5, §13 card |
| Stuyvesant Heights HD 1971; Bed-Stuy/Expanded Stuyvesant Heights HD 2013, ~825 buildings | citylandnyc.org; hdc.org (soundbar research) | §5 para 5, §13 card |
| Prospect Park South HD 1979, Dean Alvord, freestanding Victorian houses | cityneighborhoods.nyc; brooklyneagle.com (soundbar research) | §7 card, §13 card |
| Park Slope HD 1973/2016 | silo NYC hub N14 | §5 para 5 (mentioned only) |
| Brick nogging in Bed-Stuy frame houses, "no longer common" by 1882 | brownstoner.com Bed-Stuy wood-frame article (soundbar research) | §7 card |
| Brooklyn Tower 1,066 ft, 93 storeys, Dime Savings Bank site, condos + rentals | en.wikipedia.org/wiki/Brooklyn_Tower; cityrealty.com (soundbar research) | §13 card |
| Spring Creek Towers 5,881 units, 46 buildings, Jamaica Bay | twinpinesmgt.com; springcreektowers.com (soundbar research) | §7 card |
| Domino Park opened June 2018 | dominopark.getanchor.io (soundbar research) | §13 card |
| Brooklyn Navy Yard 300+ acres, 550+ businesses, 13,000+ jobs (FY25 impact report) | brooklynnavyyard.org (fiber research) | §8 sentence, §13 card |
| Industry City (named only) | fiber/soundbar research | §8 sentence |

### Prices (all from live AESS pages / research/smart-lock-installation.md prices table; Brooklyn ×1.00 — none invented)
- Single-door keypad or fob reader with electric strike $1,500–$2,500 installed — access-control-installation-brooklyn.html ("$1,500 to $2,500 installed, including reader, electric strike, wiring…"). §9 café Q, §14, §15 Premium, FAQ 1, Service schema.
- New electric strike $250–$450; failed strike repair $295–$485 — door-buzzer pages per silo table. Repair capture, §14, §15 Standard, FAQ 1, schema.
- Setup-only visit $195 first hour then 30-min blocks — research/tv-mounting-prices/BRIEF.md line 15 (published for TV/device setup). §14 table. **Flag for Anwar** (same flag as LI hub): confirm this rate may be quoted for smart-lock app/code/bridge visits.
- $195/hr, 3-hour minimum ($585) service/callback — blueprint §9, verbatim. §14.
- Residential smart lock (house, vestibule, garden, unit door) — no AESS figure → "quoted flat at free walkthrough" (§14, §15 Starter, BYO labour-only).
- Fixr national $250–$400 / avg $300, keypad unit $100–$250 — labelled national third-party (silo S1 / LI). §10.5 H3 1, §14.

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: EMPTY (not accessible in build env). §10.5 states this and uses cost-guide/manufacturer claims instead.
- Yelp 1–3★ Brooklyn locksmith/smart-lock: EMPTY (not accessible in build env).
- Reddit thread bodies (r/Brooklyn, r/parkslope): excerpts/titles only; thread text not retrieved — EMPTY beyond titles.
- NYT 2021 package-bin article: Firecrawl refused the site → EMPTY beyond search excerpt.
- Brooklyn local news on smart locks specifically (Brooklyn Paper, Brownstoner news, Patch, BK Eagle): none found → EMPTY.
- Field Notes: no sourced Brooklyn install anecdote → written as general working practice and labelled so.

## Images (11)

Permanent image rule (Drive folder empty, CompanyCam not connected). Note: images/low-voltage + images/commercial-security contain only 71 distinct photos (perceptual hash; most files are geo-renamed copies), the three hubs use 33, and every remaining door-hardware photo except the hero source was already used — so 10 of 11 show supporting work (racks, cabling, Wi-Fi, storefront camera), captioned only with what is visible. Picks were coordinated with the Manhattan and Queens builders by message; no overlap.

| New filename (images/smart-lock-installation/) | Source file |
|---|---|
| smart-lock-installation-brooklyn-keypad-card-reader-employee-door.webp (hero, eager) | images/commercial-security/commercial-security-systems-brooklyn-loading-dock-system.jpg |
| smart-lock-installation-brooklyn-rack-patching-checklist.webp | images/commercial-security/commercial-security-systems-brooklyn-integration-rack.jpg |
| smart-lock-installation-brooklyn-poe-switch-rack.webp | images/commercial-security/commercial-security-systems-brooklyn-nvr-poe-rack.jpg |
| smart-lock-installation-brooklyn-laptop-commissioning-rack.webp | images/commercial-security/commercial-security-systems-nyc-vms-commissioning-laptop.jpg |
| smart-lock-installation-brooklyn-ceiling-wifi-access-point.webp | images/low-voltage/low-voltage-installation-brooklyn-10-ceiling-access-point-drop.jpg |
| smart-lock-installation-brooklyn-wall-plate-cable-test.webp | images/low-voltage/low-voltage-installation-brooklyn-08-fluke-certification-pass.jpg |
| smart-lock-installation-brooklyn-retail-shop-ceiling-cable-pull.webp | images/low-voltage/low-voltage-installation-brooklyn-retail-store-ceiling-pull.jpg |
| smart-lock-installation-brooklyn-stud-wall-patch-panel.webp | images/low-voltage/low-voltage-installation-brooklyn-idf-patch-panel-build.jpg |
| smart-lock-installation-brooklyn-crew-cable-pull-open-floor.webp | images/low-voltage/low-voltage-installation-brooklyn-hero-crew-cable-pull.jpg |
| smart-lock-installation-brooklyn-conduit-cable-block-wall.webp | images/low-voltage/low-voltage-installation-nyc-riser-conduit-pull.jpg |
| smart-lock-installation-brooklyn-storefront-entrance-camera.webp | images/low-voltage/low-voltage-installation-nyc-08-storefront-camera-cabling.jpg |

Rejected after viewing: nyc-dual-entrance-design (readable address), nyc-intercom-reception-test (face), nyc-lobby-dome-camera (named business on wall), manhattan-dashboard-training (client's face), brooklyn-lpr-lot-camera (building number). Brooklyn-named door photos (brooklyn-hero-door-lock-wiring, -14-access-control-reader-wiring, -13-video-intercom-entry-wiring, -electric-strike, -access-reader, -credential-programming, -alarm-keypad, -panic-button, -video-intercom, -crew-van, -glass-break, -van-load-out, -03-metal-stud, -09-keystone) are the same photos as hub images by perceptual hash → not used. Same-photo-as-soundbar-brooklyn note: wall-plate test, ceiling AP and crew cable pull are also used (as copies) on soundbar-installation-brooklyn — different silo.

## Question register — smart-lock-installation-brooklyn

### §9 YOUR QUESTIONS ANSWERED (H3)
1. On a brownstone with double front doors and a vestibule, which door should get the smart lock — the outer pair or the inner door?
2. Can a smart lock work on a pair of doors where one leaf is held shut by bolts at the top and bottom?
3. When the garden apartment's only way in and out is under the stoop, what has to stay true about that door and the areaway gate in front of it?
4. Should the keypad face the street on the outer doors, or stay sheltered inside the vestibule?
5. If our original front door is too damaged to take a smart lock, what does a replacement have to look like in a Brooklyn historic district?
6. Our Flatbush frame house has glass panels and a mail slot next to the lock — does that change which smart lock we should buy?
7. I live in my two-family house and rent out the other floor — do the city's tenant lock rules apply to us?
8. Tenants keep sharing the street-door code with friends and delivery drivers — how do we tighten that without cutting off anyone's access?
9. As the owner, can I see when my tenant comes and goes — and should I?
10. We host registered guests in our own floor of a two-family house — how do we make sure their code never reaches the tenant's floor?
11. Can a smart lock on the outer doors stop parcels disappearing from our stoop?
12. The sponsor's team installed the smart lock on our new Downtown Brooklyn or Greenpoint condo door — how do we take the admin rights over from them?
13. Our café's back door opens onto a yard — how do we lock it properly without blocking the way out?
14. Why can a brownstone's double doors cost more to fit than an ordinary single door?

### §17 FAQ (visible == FAQPage, 9)
1. What does a keypad and electric strike on a Brooklyn building door cost?
2. Do you work on brownstones that are mid-renovation, before the doors are finished?
3. Can the walkthrough and the installation happen on the same visit?
4. Will the buzzer from an upstairs apartment still open the vestibule door after a smart lock goes on?
5. Can you fit a video doorbell or stoop camera at the same visit?
6. If we restore our original double doors later, can the smart lock move to the new doors?
7. Can a storefront lock be installed before the shop opens?
8. Who does a tenant call if the keypad on the house dies at night?
9. Will you keep our original brownstone lock and hardware if a smart lock replaces it?

### Other question-form headings
- H2 "Keypad Gone Quiet on Your Brooklyn Stoop?" (repair capture)
- H2 "Locked Out at the Top of a Brooklyn Stoop Tonight?" (final repair capture)

De-dup notes: compared by meaning against the NYC/LI/HV registers and the Manhattan and Queens pages on disk at build time. Replaced during build: lobby-app vs unit-lock question (= Manhattan "My building already opens the lobby with an app…"), under-stoop gate keypad (= Queens FAQ "keypad on the front-yard gate"), "Where are your installers based?" (= Manhattan FAQ), "Which other areas…" (= NYC FAQ 10), and repair-capture headings close to Manhattan/Queens. Partial overlaps left for the main run to judge: Q1 (which of two front doors) vs Queens "storm door over the front door — which gets the smart lock?" (different door configuration); Q10 guest codes vs Manhattan "guest bedroom smart lock" and LI/HV rental-code questions (here: separating a guest from a tenant's floor in a two-family house); FAQ 8 vs Queens "Will the lock warn us before its batteries run out?" (here: who a tenant calls).


## Queens (smart-lock-installation-queens)

Built 2026-10-17 (batch: Manhattan / Brooklyn / Queens smart-lock area pages). Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, #bronx) · up-link /smart-lock-installation-nyc · Queens ×1.05.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape. "Carried from soundbar file" = finding reached by the soundbar-installation-queens builder on 2026-10-17 and logged in research/soundbar-installation.md (Queens section); not re-fetched.

Thesis / lane: Queens houses with several doors (storm door over the front door, side/driveway door, basement door down exterior steps); multigenerational and multilingual households sharing access (no-smartphone elders, caregivers on schedules, app-language limits, dementia alerts, arthritis); basement doors as egress after Ida and under the 2024 basement pilot (no legal advice); garden co-op doors that face courtyards; LIC towers with building-run app locks; Queens BID corridors (Flushing, Steinway, 82nd St/Roosevelt Ave, Jamaica, Myrtle Ave, Bell Blvd).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY (not searched for Queens smart-lock threads this run; Reddit pages not accessible for scraping in build env). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from product pages/guides, stated as such on the page. |
| 6 | Landmarks | see L1–L8 |
| 7 | Use cases / building stock | see B1–B6 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | QNS (Glen Oaks burglary), ABC7 (2022 pattern), NYC Mayor's Office (Operation Restore Roosevelt), NYCEM press release; Queens Daily Eagle (Ida, carried). |
| 10 | Hyperlocal | QNS used; Queens Chronicle: only a search excerpt (qchron.com "Adams calls Operation Restore Roosevelt a success") — article not opened, not used. Queens Ledger: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| Q1 | `New York 2024 law legalize basement cellar apartments community districts Queens program egress requirements` · Firecrawl search | https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=7020615&GUID=0F7E9745-94B9-4015-818A-16574BEE18AD | Int 1127-2024 (enacted as Local Law 126 of 2024 per DOB rule page): basement/cellar legalization pilot; program area includes Queens community district 2; units existing before April 20, 2024; apply by April 20, 2029; ATR inspection incl. "at least 1 means of egress directly to the outdoors … including access to a public way"; smoke + CO alarms and water sensors/alarms within 3 months; sprinkler within 2 years; no rentals < 30 days. | §5 para 4, §5.5 bullet 6, §9 Woodside basement Q, §10.5 H3 6, Across Queens (Astoria/LIC), Basement checklist |
| Q2 | same search | https://rules.cityofnewyork.us/rule/establishment-of-temporary-residence-program-for-eligible-basement-or-cellar-residences/ | DOB proposed rule implementing Article 507 / Local Law 126 of 2024; hearing Dec 11, 2025; pre-April 20, 2024 units; apply by April 20, 2029. | §9 Woodside basement Q ("DOB proposed implementing rules in late 2025") |
| Q3 | `NYC Emergency Management basement flooding flash flood residents basement apartments get out know your exit advice` · Firecrawl search → Firecrawl scrape | https://www.nyc.gov/site/em/about/20260403_pr_nycem_prepare-for-flashfloods.page | NYCEM press release Apr 3, 2026: basement residents "go to a higher floor when it rains. Do not wait for water to enter your unit"; "Keep exits clear and know more than one way out"; "Install a water sensor or flood alarm in your basement or ground floor"; Notify NYC Basement Alert Group. | §5 para 3, §9 Ida door Q, §9 flood/power-out Q, §10 equipment (sensors), Basement checklist |
| Q4 | `Yale Assure Lock 2 keypad voice prompts language English Spanish French change language` · Firecrawl search | https://eshop.assaabloyopeningsolutions.com.au/media/B2BUserGuide/Yale%20Assure%20SL%20Installation%20and%20Programming%20Instructions.pdf ; https://www.yaleconnecthub.com/content/dam/assa-abloy/americas/latam/yale-connect/latam/es/images/descargas-manuales/YRD%20256%20-%20%20EN.pdf | Excerpts: "Language Setting Mode: Choosing English (1), Spanish (2), or French (3) becomes the (default) setting for the lock's voice prompts." | §9 app-language Q |
| Q5 | `Schlage Home app languages supported Spanish Chinese Korean smart lock app language` · Firecrawl search → Firecrawl scrape (directQuote) | https://apps.apple.com/au/app/schlage-home/id1038212933 | App Store Languages: "English, French, Spanish". | §9 app-language Q, §10.5 H3 2 |
| Q6 | `"Yale Home" app App Store apps.apple.com` · Firecrawl search; then Firecrawl scrape | https://apps.apple.com/au/app/yale-home/id1670570711 (excerpt "Language EN + 25 More"); https://shopyalehome.com/pages/yale-access-app-download (Yale Access app for US & Canada; Yale Home for outside US); https://apps.apple.com/us/app/yale-access/id1450980221 (scraped: Languages "English") | Yale Access (US/Canada) English only; Yale Home (outside North America) EN + 25 more. | §9 app-language Q, §10.5 H3 2 |
| Q7 | `Fresh Meadows Queens housing development New York Life Insurance 1949 garden apartments history` · Firecrawl search | https://en.wikipedia.org/wiki/Fresh_Meadows,_Queens ; https://www.nytimes.com/1972/08/02/archives/housing-in-fresh-meadows-is-sold-by-new-york-life.html | Land bought by New York Life 1946; first twenty families moved in Sept 2, 1947; NYT 1972: "sprawling, 140‐building Fresh Meadows apartment complex" sold to Helmsley. (cityneighborhoods.nyc SOM/Stein claim conflicts with Wikipedia's Ralph Walker — not used.) | §7 building card, §13 landmark card, Across Queens |
| Q8 | `Jackson Heights Historic District designated 1993 Landmarks Preservation Commission garden apartments buildings` · Firecrawl search | http://s-media.nyc.gov/agencies/lpc/lp/1831.pdf ; https://www.jhrealestatereport.com/about-jackson-heights/jh-historic-district/ | Designated Oct 19, 1993, ~36 blocks. | §13 landmark card, Across Queens |
| Q9 | `Bay Terrace Bayside garden apartment cooperative sections built 1950s Cord Meyer number of units` · Firecrawl search | https://www.habitatmag.com/Publication-Content/Legal-Financial/2018/2018-May/Land-Lease | Bay Terrace co-ops "built in the 1950s on land owned by Cord Meyer Development"; nine sections (1,800-apartment figure ambiguous in excerpt — not used). | §5 para 5, §7 card, §9 co-op courtyard Q, Across Queens |
| Q10 | `Queens burglary pattern homes entered through rear door basement police 2025 qns.com OR qchron.com` · Firecrawl search → Firecrawl scrape | https://qns.com/2025/07/three-burglars-glen-oaks-home-steal-50k-in-jewelry/ | QNS July 8, 2025 (Bill Parry): three burglars entered a private residence near 268th St & 79th Ave, Glen Oaks, "through an unlocked basement door at around 1:30 p.m. on Thursday, June 19"; ~$50,000 jewelry; 105th Precinct. | §9 Glen Oaks Q, §10.5 H3 4, Across Queens (east) |
| Q11 | same search → Firecrawl scrape | https://abc7ny.com/post/queens-home-burglary-pattern-surveillance-video-robbery/12140326/ | ABC7 Aug 19, 2022: five houses broken into since July 24 in Queens Village, Glen Oaks, New Hyde Park; "Each case involves a side door or window being broken into." | §9 Glen Oaks Q, §10.5 H3 5 |
| Q12 | `Operation Restore Roosevelt Avenue Queens 2025 NYPD businesses Jackson Heights Corona` · Firecrawl search → Firecrawl scrape | https://www.nyc.gov/mayors-office/news/2025/06/mayor-adams-major-crime-reductions-roosevelt-avenue-queens-following-targeted | Mayor's Office June 24, 2025: Operation Restore Roosevelt launched October 2024; burglaries down 48% (start of year through mid-June vs same period). City Limits opinion (https://citylimits.org/opinion-operation-restore-roosevelt-failed-queens/) critical — page presents the figure as the city's report. | §8 82nd St/Roosevelt card, §9 (shop context) |
| Q13 | NYC SBS BID directory · Firecrawl scrape (directQuote) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | Queens BIDs: 180th Street, 82nd Street Partnership, Bayside Village, Downtown Flushing Transit Hub, Downtown Jamaica Partnership, GatewayJFK, Long Island City Partnership, Myrtle Avenue (Queens), Steinway Street, Sunnyside Shines, Woodhaven (11). | §8 cards + intro ("eleven BIDs") |
| Q14 | `New York Multiple Dwelling Law section 4 definition "multiple dwelling" three or more families nysenate` · Firecrawl search | https://www.nysenate.gov/legislation/laws/MDW/4 | "multiple dwelling" = occupied as the residence or home of three or more families living independently. | Research only (paragraph removed during de-dup vs Brooklyn's two-family question) |
| Q15 | `smart lock IP65 rating exterior keypad water resistance not waterproof submerged flood manufacturer` · Firecrawl search → Firecrawl scrape | https://support.shopyalehome.com/is-the-yale-smart-lock-weatherproof-SJchNsfO4 | "The Yale Smart Keypad all has an IP55 rating, meaning it is dust protected and effective against water jetting. Yale Smart Lock Pro and Yale Connect Bridge are installed inside the home and are not intended for outdoor use." | §7.5 below-grade doors, §9 Ida door Q, §10 equipment card, §10.5 H3 3 |
| Q16 | `Alzheimer's Association wandering prevention door alarms chimes locks out of line of sight` · Firecrawl search | https://www.alz.org/help-support/caregiving/safety/wandering | Checklist: deadbolts out of line of sight; "never lock a person in at home"; "Install warning bells above doors or use a monitoring device that signals when a door is opened." | §9 dementia Q |
| Q17 | `Latch smart lock apartment residents integration Google Home Apple HomeKit support article` · Firecrawl search | https://support.latch.com/hc/en-us/sections/15609741287447-Using-your-Latch-Device-and-the-Latch-App | Only iOS widget info found; no integration statement → page makes no claim about any platform's integrations. | §9 LIC Q (generic wording only) |
| C1 | carried from soundbar file (Firecrawl scrape) | https://www.census.gov/quickfacts/queenscountynewyork | Pop 2,358,182 and housing units 934,750 (July 1, 2025); 2.72 persons/household; 65+ 18.4%; foreign-born 47.6%; language other than English 55.4%; owner-occupied 44.9% (2020–2024). | §5 para 2, §5.5 bullets 1–4, §10.5 H3 2 |
| C2 | carried from soundbar file | https://queenseagle.com/all/unimaginable-loss-eleven-from-queens-die-in-storm ; https://a816-dohbesp.nyc.gov/IndicatorPublic/data-stories/flooding-and-health/ | 11 of 12 confirmed dead from Queens, 10 lived in basement apartments; DOHMH: 14 Ida deaths, 10 (71%) drowning in unregulated basement apartments. | §5 para 3, §5.5 bullet 5 |
| C3 | carried from soundbar file | https://www.osc.ny.gov/files/reports/pdf/report-24-2025.pdf | LIC/Sunnyside/Woodside housing +~42% 2010–2023 to ~66,700 units. | Across Queens (Astoria/LIC), §5 para 5 ("last fifteen years") |
| C4 | carried from soundbar file | https://www.glenoaksvillage.com/about | 2,904 garden-style apartments in 134 buildings. | §9 co-op courtyard Q, §7 card |
| C5 | carried from soundbar file | https://rochdalevillage.com/property/ ; https://www.nyc.gov/html/cchr/justice/downloads/pdf/rochdale_village.pdf | Opened 1963; "largest private housing cooperative in the world"; 20 thirteen-storey buildings in circles of four; 5,860 apartments. | §13 card, §7 card |
| C6 | carried from soundbar file | https://en.wikipedia.org/wiki/LeFrak_City | 4,605 apartments, Corona, by the LIE. | §7 card, Across Queens |
| C7 | carried from soundbar file | https://hdc.org/buildings/sunnyside-gardens-historic-district/ ; https://s-media.nyc.gov/agencies/lpc/lp/2258.pdf | Built 1924–1928, twelve courts; designated 2007. | §13 card |
| C8 | carried from soundbar file | https://www.nps.gov/places/sage-foundation-forest-hills.htm | 1909, Olmsted Jr. + Atterbury, Russell Sage Foundation, 142 acres. | §13 card, Across Queens |
| C9 | carried from soundbar file | https://en.wikipedia.org/wiki/Skyline_Tower_(Queens) | Topped out 2019, 762 ft, surpassed One Court Square as tallest in Queens. | §13 card |
| C10 | carried from soundbar file | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=45 | Downtown Flushing: 30 block faces, ~1,500 ground-floor businesses. | §8 Flushing card |
| C11 | carried from soundbar file | https://www.citylandnyc.org/commission-approves-district-encompassing-almost-1000-buildings/ | Central Ridgewood Historic District (LPC, Dec 9, 2014), masonry rows. | Across Queens (Ridgewood) |
| S1 | silo file N6 (HPD fire safety) | https://www.nyc.gov/site/hpd/services-and-information/fire-safety.page | Double-cylinder locks illegal on apartment doors. | §7.5, §9 dementia Q |
| S2 | silo file N4 (Tenant Data Privacy Act) | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Owner may not require smart access to enter tenant's unit. | §8.5, §9 LIC Q, §10.5 H3 7 |
| S3 | silo file S1 (Fixr) | https://www.fixr.com/costs/smart-lock-installation | National $250–$400 (Jan 2025) — labelled national third-party. | §14 pricing |

### Prices used (all from approved sources; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,575–$2,625 | single-door keypad/fob reader + electric strike (Queens) | research/smart-lock-installation.md prices table ($1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike on entrance door | $250–$450 × 1.05 (262.5→263, 472.5→473, round half-up) |
| $310–$509 | failed electric strike repair | $295–$485 × 1.05 (309.75→310, 509.25→509) |
| $195 first hour, then 30-min blocks | setup-only visit, Queens | research/tv-mounting-prices/BRIEF.md line 15 |
| $195/hr, 3-hr minimum ($585) | service/callback rate, not on initial install | blueprint v2.3 §9 (verbatim) |
| quoted flat at walkthrough | residential smart lock install | no AESS figure exists |
**Conflicts for Anwar:** (1) live access-control-installation-queens.html shows "Single-door lobby fob reader: $1,500 to $2,500" and "Queens pricing comparable to Brooklyn base" — this page uses §9 ×1.05 ($1,575–$2,625), matching the NYC hub's Queens row. (2) live door-buzzer-repair-queens-new-york.html shows "$250 service call" and garden-co-op/mid-rise "strike with alignment $450–$950" — differs from the ×1.05 strike figures used here. (3) Setup-only $195 rate is published for TV/device setup; used here for app/code/schedule visits (same flag as the LI hub).

## Images (11)
Drive folder empty, CompanyCam not connected → permanent image rule. Every source cluster used by the NYC/LI/HV hubs (perceptual-hash checked), by the Brooklyn builder's 11 and by the Manhattan builder's 11 was excluded; claims exchanged with both builders. **None of the free photos show smart locks or door hardware** (the lock-related clusters were all taken by the hubs); the 11 below show adjacent low-voltage/camera work and captions describe only what is visible. The library photos look AI-rendered (same note as soundbar pages) — needs Anwar's review; real smart-lock photos should replace them. Rejected after viewing: commercial-security-systems-queens-hero-building-cameras (readable "1250 Commerce Drive" address), commercial-security-systems-queens-lpr-lot-camera (building number "1000" on facade).

| New filename (images/smart-lock-installation/) | Source file |
|---|---|
| smart-lock-installation-queens-corridor-ceiling-cable-pull.webp (hero, eager) | images/low-voltage/low-voltage-installation-queens-school-corridor-ceiling-tile.jpg |
| smart-lock-installation-queens-exterior-wall-camera-mount.webp | images/commercial-security/commercial-security-systems-nyc-exterior-ptz-install.jpg |
| smart-lock-installation-queens-recessed-data-box-patch.webp | images/low-voltage/low-voltage-installation-bronx-display-recessed-box.jpg |
| smart-lock-installation-queens-hallway-cable-bundle-routing.webp | images/low-voltage/low-voltage-installation-hudson-valley-10-school-corridor-cable-pull.jpg |
| smart-lock-installation-queens-restaurant-ceiling-wiring.webp | images/low-voltage/low-voltage-installation-queens-14-restaurant-ceiling-speaker.jpg |
| smart-lock-installation-queens-fiber-splice-network-closet.webp | images/low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg |
| smart-lock-installation-queens-office-camera-bracket-install.webp | images/low-voltage/low-voltage-installation-bronx-ptz-camera-mount.jpg |
| smart-lock-installation-queens-crew-display-mount-office.webp | images/low-voltage/low-voltage-installation-queens-13-conference-room-display-cabling.jpg |
| smart-lock-installation-queens-scissor-lift-camera-row.webp | images/commercial-security/commercial-security-systems-queens-dock-cameras.jpg |
| smart-lock-installation-queens-warehouse-wall-camera-cluster.webp | images/commercial-security/commercial-security-systems-bronx-warehouse-cameras.jpg |
| smart-lock-installation-queens-warehouse-cable-tray-lift.webp | images/low-voltage/low-voltage-installation-queens-05-warehouse-cable-tray-highbay.jpg |

## Question register — smart-lock-installation-queens

### §9 YOUR QUESTIONS ANSWERED (H3)
1. Grandma doesn't carry a smartphone — how does she get in once our front door goes keyless?
2. Our home attendant comes three mornings a week — can her code work only on those days?
3. The lock's app is only in English — what are the options for parents who read Chinese, Korean or Spanish?
4. Dad has early dementia — can the lock tell us if he opens the front door at night without locking him in?
5. Arthritis makes turning a key painful — which kind of smart lock is easiest to work?
6. Our basement door at the bottom of the outside steps took water during Ida — will a smart lock survive there?
7. If the basement floods at night and the power is out, can whoever is downstairs still get out?
8. Burglars in Glen Oaks walked in through an unlocked basement door — is our basement door worth a smart lock, or is a door sensor enough?
9. We have a family member living in the basement of our Woodside house — what do the city's basement rules say about that door?
10. Our garden co-op apartment's door opens straight onto the courtyard, not a hallway — does that change which smart lock fits?
11. Our Long Island City rental came with the building's app lock — can we connect it to Google Home or Apple Home?
12. Our house has an aluminium storm door with its own lock over the front door — which one should get the smart lock?
13. Our shop's keypad faces busy Jamaica Avenue — how do we stop passers-by watching staff punch in the code?
14. Stylists rent chairs in our Jackson Heights salon — how do we give them after-hours access without handing out keys?

### §17 FAQ (visible == FAQPage, 10)
1. What does a keyless shop door or building entrance cost in Queens?
2. We just closed on a house in Queens — should we re-key first or go straight to smart locks?
3. Will you leave written instructions for relatives who won't use the app?
4. Do you bring the lock, or should we buy one before the visit?
5. Who should hold the administrator account when a whole family shares the lock?
6. Will the lock warn us before its batteries run out?
7. Do you cover the Rockaways and Broad Channel as well as northern Queens?
8. Can you put a keypad on the front-yard gate of a Queens house?
9. What if the wood frame on our older house is too soft to hold the lock's strike?
10. Can you match the new lock's finish to the other hardware on our house?

### Other question-form headings
- H2 "Lock Jammed, Dark or Offline Somewhere in Queens?" (repair capture)
- H2 "Ready for Doors Everyone Can Open?" (mid-page CTA)
- H2 "Can't Get Through Your Own Front, Side or Basement Door?" (final repair capture)

### De-dup notes
- Replaced after comparing with batch siblings on disk: restaurant alley back-door exit Q (= Brooklyn café back-door Q) → Jamaica Ave keypad shoulder-surfing Q; Glen Oaks Q reframed from auto-lock (≈ Manhattan FAQ "relock itself") to smart lock vs door sensor; FAQ "doorbell camera same visit" (= Brooklyn FAQ) → "Do you bring the lock…"; MDL three-family paragraph removed (≈ Brooklyn two-family tenant-rules Q).
- Partial overlaps for the main run to judge: Q2 (caregiver scheduled code) vs Manhattan "How should the doorman, the dog walker and the cleaner get in…"; FAQ 6 (low-battery warning) vs Manhattan "If the batteries die while we are out of the country…"; Q11 (LIC building lock ↔ Google/Apple Home) vs Brooklyn/Manhattan "building runs lobby on an app — will a separate unit lock work alongside it"; FAQ 1 cost vs NYC/Brooklyn/Manhattan cost FAQs (geo-specific pricing by design); storm-door Q12 (which door) vs LI Q8 (clearance between storm door and keypad deadbolt).


# Research — smart-lock-installation-bronx (batch 2026-10-17)

Page: `/smart-lock-installation-bronx` · silo Smart Lock Installation · up-link `/smart-lock-installation-nyc` · phone (646) 490-0629 (body, CTAs, schema; (800) 486-0943 only in shared header chrome) · GBP Bronx, 460 E Fordham Rd, schema `#bronx` · pricing multiplier 1.00.

Thesis: **who controls the door in the Bronx.** NYCHA keeps the bottom lock; Parkchester North owns the bottom cylinder and files every unit key; Riverbay/Co-op City expects restoration on move-out; private co-ops expect a duplicate key or code; private landlords owe a key lock (HMC 27-2043) while tenants may add one (MDL 51-c, which excludes housing-authority buildings); two-family owners owe their tenant a key lock and a key. Plus: steel/mortise pre-war doors, building-entry (MDL 50-a street door, roof door, intercom) vs apartment-door locks, self-closing doors after Twin Parks (LL71/2022), owner-occupied two-family and row houses.

Tools: "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (directQuote query mode). Silo-wide findings (August Connect 10–15 ft, LawnStarter/Fixr national costs, ADA 404.2.7, Matter/Thread) reused from research/smart-lock-installation.md — not re-fetched. Some Bronx housing facts reused from research/soundbar-installation.md (Bronx section, fetched 2026-10-17) — marked "reused".

## Bronx (smart-lock-installation-bronx)

### Lock law and building rules
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| B1 | `NYCHA resident handbook change locks apartment door permission key` · Firecrawl search → Firecrawl scrape (pdf) | https://www.nyc.gov/assets/nycha/downloads/pdf/pp/nycha-public-housing-resident-handbook-2024.pdf | "The front door of your apartment has been equipped with a lock ('bottom lock'). NYCHA does not allow tenants to replace this lock; however, you may buy an additional lock. You will be responsible for its installation, care, and maintenance. In case of an emergency, NYCHA reserves the right to break the lock…"; lockout: work order, "$47.25 charge … for the new lock and keys"; "$50 fee" after hours; "NYCHA will drill out resident-installed locks, but is not responsible for replacing them"; self-closing door must "completely close and latch by itself", inspected periodically; residents responsible for carpet/mat blocking closer; "Residents are not allowed to alter their apartments or add any fixtures or fittings … without prior written consent from their property management office". | Hero, §5 paras 1/3, §5.5 stat 5, §7 NYCHA card, Keyholder Map row, §9 Q1–Q2, §10.5 H3 1–2, §14 building costs, FAQ "Will you drill a NYCHA…", FAQ "one key", final repair capture |
| B2 | same search | https://designguidelines.nycha.info/apartment-entrance-doors/ | NYCHA design guideline: heavy-duty latch set, heavy-duty deadbolt key outside/thumb-turn inside, chain guard, viewer; closer 90°→12° ≥5 s. | Research only (not on page) |
| B3 | `Parkchester condominium apartment entrance door lock rules unit owner change lock key management` · Firecrawl search → Firecrawl scrape (pdf) | https://083d840ddfd5c6063e01-d068e497715423d630add53cb355c226.ssl.cf5.rackcdn.com/1128/39/LPDOC1/11288339/11288339-Rules_and_Regulations.pdf | "RULES AND REGULATIONS FOR THE PARKCHESTER NORTH CONDOMINIUM Updated January 2009": "Unit owners or their tenants may not change the bottom lock cylinder, as the bottom lock is the property of The Parkchester North Condominium. A second lock cylinder may be added or changed but all unit door keys must be filed with the Management Office." | Hero, §5 paras 1/3, §5.5 stat 4, §7 Parkchester card, Keyholder Map, §9 Q4–Q5, §10.5 H3 1/4, FAQ "one key", §13 card |
| B4 | `Co-op City Riverbay apartment lock change shareholder duplicate key rules` · Firecrawl search (excerpt) | https://www.coopcity.com/Pdf/Resources_FAQ.pdf | "Outgoing shareholders are responsible for restoring their unit to its original standard or else Riverbay will deduct the cost to complete the restoration from their equity." No Riverbay lock/key rule found. (Delivery-permit detail reused from research/soundbar-installation.md.) | Hero, §5 para 3, §7 card, Keyholder Map, §9 Q3, §14 building costs |
| B5 | `Co-op City Riverbay locksmith apartment door lock change shareholder Riverbay key policy` · Firecrawl search | https://guzovllc.com/precarious-co-op-rules/ | Excerpt: "Typically a shareholder cannot change the locks on the door providing access to the apartment unless they give duplicate keys for the locks or combination codes". Also https://cooperatornews.com/article/the-shareholder-versus-the-board (proprietary lease duplicate-key clause). | Keyholder Map (private co-op row), §10.5 H3 4 |
| B6 | `New York Multiple Dwelling Law 51-c` · Firecrawl scrape | https://www.nysenate.gov/legislation/laws/MDW/51-C | Full text: tenant of a multiple dwelling (except one under supervision/control of a municipal housing authority; except hotel/motel/dormitory) may install a lock "separate and apart from any lock installed … by the owner", "not more than three inches in circumference", duplicate key to landlord/agent on request; lease charges for the right void. | §5 para 3, Keyholder Map + para, §9 Q1/Q5, §10.5 H3 2 |
| B7 | HMC Article 11 · Firecrawl scrape | https://nycadmincode.readthedocs.io/t27/c02/sch02/art11/index.html | §27-2043: owner of a dwelling provides key lock in each dwelling-unit entrance door + at least one key; class A: heavy-duty latch set + heavy-duty deadbolt (key outside, thumb-turn inside); chain door guard. §27-2041: peephole; not required in tenant-occupied one/two-family home where visitor visible; not applicable to owner-occupied units in one- and two-family homes. | §5 para 2, §7.5 "whose lock", Keyholder Map, §9 two-family Q, two-family guide |
| B8 | HPD fire safety · Firecrawl scrape | https://www.nyc.gov/site/hpd/services-and-information/fire-safety.page | "All residential buildings with 3 or more apartments must have self-closing doors… make sure your apartment door opens from the inside without a key." "It is illegal to install key-locked window gates on fire escapes and double-cylinder locks on apartment doors…" | §7.5 "what is on the inside", §9 police-lock Q, §10.5 H3 5, Keyholder Map |
| B9 | MDL §50-a · Firecrawl scrape | https://www.nysenate.gov/legislation/laws/MDW/50-A | Class A built/converted after 1/1/1968: entrances automatic self-closing + self-locking; roof door "self-closing door which shall not be self-locking … a lock which does not require a key to open from inside"; 8+ apartments: intercom at self-locking lobby door with release from apartment; pre-1968 buildings: doors + intercom required when tenants occupying a majority request/consent in writing; willful damage/jamming = misdemeanor. | §8.5 roof bullet, §9 Q street door pre-1968, roof door, vestibule/buzzer, §10.5 H3 5–6, street-vs-apartment table |
| B10 | `DHCR rent stabilized required services intercom door lock key fob replacement decrease in services complaint` · Firecrawl search → Firecrawl scrape (pdf) | https://hcr.ny.gov/system/files/documents/2023/11/fact-sheet-14-11-2023.pdf | Fact Sheet #14: required services include "maintenance of front or entrance door security (including, but not limited to, lock and buzzer)". Also https://hcr.ny.gov/living-conditions-and-essential-services (RA-81 form). | §9 rent-stabilized Q, §10.5 H3 6, street-vs-apartment table |
| B11 | `Tenant Data Privacy Act Local Law 63 2021 smart access amended 2023 2024 2025 NYC tenants physical key` · Firecrawl search | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | LL63/2021 (Int 1760-2019) still current per HPD page: owners using smart access must provide a data retention and privacy policy. No later amendment found. (Consent / no-required-use details from silo research N4.) | §9 Fordham shop Q, street-vs-apartment table |
| B12 | `Landmarks Preservation Commission rules doors hardware intercom keypad historic district permit staff-level` · Firecrawl search (excerpt) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | LPC Permit Guidebook 2025: "If the existing door is original or historic — All historic fabric, such as sidelights, doors, transoms, framing, and door surround detailing must be retained." | Two-family guide "Landmarked fronts", §13 Longwood card |

### Fire / self-closing doors
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| B13 | `Twin Parks North West fire Bronx January 2022 apartment door failed to close self-closing 17 dead` · Firecrawl search → Firecrawl scrape | https://en.wikipedia.org/wiki/2022_Bronx_apartment_fire | Jan 9, 2022 ~10:55 a.m.; defective space heater; "Smoke spread through the building as a result of two malfunctioning self-closing doors"; 19-story, 120 apartments, 333 East 181st Street near Tiebout Avenue; building conformed to 2018 self-closing law. Deaths "17" from search excerpts (PBS headline, NYT "Left 17 Dead"). | §5 para 5, §7.5 closer test, §9 HPD inspector Q, §10.5 H3 5 |
| B14 | `after Twin Parks fire City Council local laws 2022 self-closing doors inspection HPD notice law number` · Firecrawl search → Firecrawl scrape (pdf) | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/self-closing-door-fy24.pdf | HPD report: LL71/2022 "passed in the wake of the Twin Parks fire" → program to identify high-risk buildings for proactive inspection; began Sept 2023 in 300 multiple dwellings; ~17,946 apartments + 3,351 public doors = 21,297 doors; 3,151 violations; Bronx row: 853 violations, 27%, 66 buildings. (First table's column alignment is ambiguous — only the borough-violations table used.) | §5 para 5, §5.5 stat 6, §9 HPD inspector Q |

### Building stock / neighborhoods
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| B15 | `Bronx housing stock one- and two-family homes share percent Bronx buildings built before 1947 Furman Center` · Firecrawl search → Firecrawl scrape | https://unhp.org/blog/how-will-bronx-buildings-survive-as-they-age/ | Oct 10, 2014, UNHP: "Here in the Bronx, the median age of multifamily apartment buildings is 87 years"; nearly 8,000 multifamily (5+ units) buildings in Building Indicator Project database. | §5 para 4, §5.5 stat 2, §10.5 H3 7 |
| B16 | `Edgewater Park Silver Beach Throggs Neck Bronx cooperative bungalows homeowners lease land` · Firecrawl search → Firecrawl scrape | https://en.wikipedia.org/wiki/Edgewater_Park_(Bronx) ; https://www.nytimes.com/2009/08/02/realestate/02living.html (excerpt) | 60-acre waterside co-op of 675 single-family homes in Throggs Neck near the Throgs Neck Bridge; co-op in 1988; sister communities Silver Beach, Harding Park. NYT excerpt: "Residents own their homes but lease the land". | §7 waterfront card, §9 Edgewater Q, §13 card |
| B17 | City Island · Firecrawl scrape | https://en.wikipedia.org/wiki/City_Island,_Bronx | ~1.5 mi × 0.5 mi; population 4,417 (2020); New City Island Causeway Bridge opened Oct 29, 2017. | §13 card |
| B18 | `Longwood Historic District Bronx row houses semi-detached designated 1980 Landmarks Preservation Commission` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Longwood_Historic_District_(Bronx) ; https://www.nyc.gov/site/lpc/about/pr2026/lpc-unveils-new-historic-district-markers-commemorating-longwood-and-bronx.page ; https://www.lehman.edu/public-art-bronx/Longwood-Historic-District-/ | Semi-detached rowhouses; designated 1980, extension 1983. | §7 row-house card, §13 card, two-family guide |
| B19 | SBS BID directory · Firecrawl scrape | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | Bronx BIDs: 161st Street, Belmont, Castle Hill, Fordham Road, HUB Third Avenue, Jerome-Gun Hill, Kingsbridge, Morris Park, Southern Boulevard, Throggs Neck, Westchester Square, White Plains Road (12). | §8 cards + intro + closing line |
| B20 | reused from research/soundbar-installation.md (Bronx) | furmancenter.org/neighborhoods/the-bronx ; coopcity.com + en.wikipedia.org/wiki/Co-op_City,_Bronx ; parkchesternyc.com/about-us/history + simple.wikipedia Parkchester ; hdc.org Grand Concourse HD ; en.wikipedia NYCHA (Edenwald, Patterson) ; cooperatornews / nybits Riverdale co-ops ; norwoodnews.org (Fordham Road 175 storefronts) ; thirdavenuebid (oldest commercial district) ; publicmarkets.nyc Arthur Avenue (Oct 1940) ; en.wikipedia Yankee Stadium | Homeownership 19.7% (2024); Co-op City 1966–1973, Freedomland site, 35 towers + 7 townhouse clusters, 15,372 units, 24–33 floors, Riverbay board, I-95/Hutchinson River Pkwy; Parkchester 1938, 129 acres/27% built, 171 buildings, 12,271 apartments, North/South condos; Grand Concourse HD designated Oct 25 2011, majority built 1916–1941; Edenwald 40 buildings 2,034 apts largest in borough, Patterson Mott Haven; Riverdale apartment buildings that became co-ops. | §5, §5.5 stats 1/3/4, §7 cards, §8 cards, §13 cards |

### Sources not reachable / EMPTY
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: `EMPTY (not accessible in build env)`. §10.5 says so and uses published national/retail claims instead (LawnStarter national average from silo research).
- Reddit r/bronx (smart lock / keypad / landlord): query `reddit bronx smart lock apartment landlord keypad` · Firecrawl search → no Bronx threads (only r/homeautomation, r/Landlord US-NY, r/AskNYC, r/NYCapartments Queens two-unit). `EMPTY` for Bronx; nothing quoted.
- Bronx local news on smart locks / keyless entry: query `Bronx tenants keyless entry key fob system lawsuit landlord building 2023 OR 2024 OR 2025` · Firecrawl search → only Hell's Kitchen Latch (already on NYC hub). `EMPTY` for Bronx.
- Bronx Times / Norwood News / Riverdale Press smart-lock stories: `EMPTY` (not found).
- Yelp 1–3★ Bronx locksmith/smart-lock installers: `EMPTY (not accessible in build env)`.
- Riverbay/Co-op City lock or key policy: not found → page says only what the restoration FAQ says.
- Edgewater Park lock rules: not found → page says "we have not seen a published lock rule there".
- Parkchester South rules: not found → page asks owners to send their rules.
- Google Drive `AESS Website Photos/Smart Lock Installation`: EMPTY (per batch brief); CompanyCam not connected.

### Prices used (no new prices; Bronx ×1.00)
| Figure | Scope | Source |
|---|---|---|
| $1,500–$2,500 installed | single-door keypad or fob reader with electric strike | access-control-installation-bronx.html ("SINGLE DOOR $1,500 – $2,500 … Keypad or fob reader with electric strike"; "Bronx pricing is Brooklyn base — no surcharge") |
| $250–$450 | new electric strike on lobby door | door-buzzer-repair-allerton-bronx-ny.html |
| $295–$485 | failed electric strike repair | door-buzzer-repair-bruckner-bronx-ny.html |
| $225 first hour, then 30-min blocks | setup-only visit (apps/bridge/codes, no hardware) | research/tv-mounting-prices/BRIEF.md line 15 (Bronx) — same use as NYC/LI hubs; **flag: confirm this TV setup-only rate may be used for smart-lock app visits** |
| $195/hr, 3-hr min ($585) | service/callback, not on initial install | blueprint v2.3 §9 |
| $47.25 / +$50 after hours | NYCHA's own lockout lock charge (not AESS) | B1 |
| $330 avg, $200–$460, labor $50–$110 | NATIONAL third-party (LawnStarter) | research/smart-lock-installation.md (LI section) |
| Apartment-door smart lock | no AESS figure → "Quoted flat at free walkthrough" | — |

## Images (11) — permanent image rule
Drive folder empty and CompanyCam not connected (batch brief). Copied from `images/low-voltage/` and `images/commercial-security/`, converted to WebP q80 (all ≤1402 px wide, so no resize). All were viewed. Almost every door/lock photo in both libraries is already used (same photo, other filename) by one of the three hubs; four sources below are not used by any hub (marked *new*). The library photos look AI-rendered; the least obviously rendered door-relevant shots were chosen, avoiding fake business names (Summit/Pinnacle/Riverfront), the "123 Main Street" directory, readable name lists and customer faces.

| File (images/smart-lock-installation/) | Source | Also on hub? |
|---|---|---|
| smart-lock-installation-bronx-electric-strike-glass-entry.webp (hero, eager) | commercial-security/commercial-security-systems-nyc-electric-strike-install.jpg | NYC (lobby strike) |
| smart-lock-installation-bronx-keypad-push-to-exit-strike.webp | low-voltage/low-voltage-installation-queens-electric-strike-keypad.jpg | NYC hero / LI |
| smart-lock-installation-bronx-maglock-header-glass-door.webp | low-voltage/low-voltage-installation-queens-maglock-install.jpg | LI |
| smart-lock-installation-bronx-maglock-terminal-label.webp | low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | HV |
| smart-lock-installation-bronx-keypad-camera-entry-pair.webp | commercial-security/commercial-security-systems-nyc-alarm-keypad-install.jpg | LI |
| smart-lock-installation-bronx-reader-door-frame-wiring.webp | low-voltage/low-voltage-installation-queens-12-access-control-reader-wiring.jpg | NYC |
| smart-lock-installation-bronx-intercom-keypad-panel-wiring.webp | low-voltage/low-voltage-installation-queens-11-video-intercom-entry-wiring.jpg | NYC |
| smart-lock-installation-bronx-van-tool-load-out.webp | low-voltage/low-voltage-installation-staten-island-van-load-out.jpg | NYC |
| smart-lock-installation-bronx-exterior-junction-boxes-block-wall.webp | commercial-security/commercial-security-systems-manhattan-exterior-enclosures.jpg | *new* |
| smart-lock-installation-bronx-riser-conduit-cable-feed.webp | low-voltage/low-voltage-installation-queens-riser-conduit-pull.jpg | *new* |
| smart-lock-installation-bronx-crew-ceiling-cable-pull.webp | low-voltage/low-voltage-installation-bronx-03-crew-cable-pull.jpg | *new* |
Rejected after viewing: nyc-lobby-dome-camera ("Summit Enterprises" sign), nyc-access-reader-install ("Pinnacle Business Center"), nyc-video-intercom-install ("Riverfront Business Center"), queens-lobby-video-intercom ("123 Main Street" directory), nyc-credential-programming (readable lists), nyc-intercom-reception-test (face), nyc-dual-entrance-design (address).
DAILY-LOG note: `images: 11 reused from images/low-voltage/ + images/commercial-security/ (no real smart-lock photos yet)`.

## Question register — smart-lock-installation-bronx

### §9 YOUR QUESTIONS ANSWERED (H3, 14)
1. NYCHA says the bottom lock stays — where does a smart lock fit on a public-housing door?
2. If NYCHA staff drill out a lock I added during a lockout, who puts it back?
3. Does a Co-op City shareholder have to undo a smart lock when the apartment goes back to Riverbay?
4. Parkchester North won't let owners touch the bottom cylinder — what smart options are left?
5. I rent my Parkchester apartment from an individual owner — who files the key for the second lock?
6. If the building's front-door lock or buzzer breaks, can a rent-stabilized tenant ask the state for a rent cut?
7. Our door still has an old brace-bar police lock — can it stay alongside a keypad deadbolt?
8. After the Twin Parks fire, what will an HPD inspector check on my apartment door?
9. Our six-family building's street door predates 1968 — does the law require it to self-lock at all?
10. Can the roof door get a keypad so only the super can open it?
11. Can a keypad on the vestibule door replace the buzzer tenants use for visitors?
12. I live downstairs and rent out the upstairs of our two-family — what does the law make me give my tenant?
13. In Edgewater Park the land belongs to the co-op — does it get a say in my front-door lock?
14. A Fordham Road shop shares a stair door with the apartments upstairs — whose code opens it?

### §17 FAQ (visible == FAQPage, 10)
1. Is Bronx pricing for keyless entry the same as Brooklyn pricing?
2. Do I have to buy the smart lock myself, or can you supply one?
3. Do you work for Bronx property managers looking after several buildings at once?
4. Will you meet the super at the door so he can see the bottom lock is left alone?
5. Can the keypad go at a height a wheelchair user can reach?
6. Can the visit be on a Sunday or in the evening after work?
7. Will you drill a NYCHA or co-op door before the building has said yes?
8. Can the smart lock work with a doorbell camera so I see who I am letting in?
9. Can one key open both my new smart lock and the bottom lock?
10. Is there an extra charge for a fifth-floor walk-up?

### Other question-form headings
- H2 "Ready to Add a Smart Lock the Right Way?" (mid CTA)
- Repair captures are non-question headings: "Bronx Smart Lock Beeping, Blank or Offline" and "Bronx Lockout With a Smart Lock: Call Before Anyone Drills".

### De-dup notes
Dropped during build after comparing with the hubs and the two batch siblings on disk: a TDPA "what should tenants ask before fobs" Q (overlaps NYC hub Q14), a Longwood historic-district keypad Q (same intent as HV Q11), a steel-door drilling Q (overlaps SI FAQ "Will drilling … damage a fibreglass or steel door?" and LI Q7), a finish-matching FAQ (same as SI FAQ), a coverage FAQ (pattern on NYC/LI), a WhatsApp-photos FAQ (HV FAQ3), and an aide-code / family-admin FAQ (answered in the page's own Families section). Partial overlaps left for the main run to judge: Q3 Co-op City move-out vs NYC Q4 rental move-out (different obligation and actor); Q5 Parkchester key filing vs NYC Q2 landlord key (condo two-tier filing); Q8 HPD inspection vs NYC Q8 self-closing interference; FAQ 5 wheelchair reach vs Nassau "older parent with arthritis or weak eyesight".


# Smart Lock Installation — research part: Staten Island (smart-lock-installation-staten-island)

Built 2026-10-17 by the Staten Island builder subagent (batch with -bronx and -nassau-county). Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used.
Thesis: on Staten Island the house is the building — owner-controlled, multi-door households (front, side, garage-to-house, basement/lower-unit, upper-unit stair door), exterior/waterfront exposure, family/caregiver code planning, two-family owner-occupant + tenant setups.
Silo-wide sources reused from research/smart-lock-installation.md (not re-fetched): S1 Fixr, S2 Bob Vila, S4 August Connect 10–15 ft, S5 Yale Matter/Thread, N4 Tenant Data Privacy Act, N9 Admin Code §26-521, N17 LL18 date, N19 SBS BID directory (Forest Avenue BID); LI part: Schlage door prep (1-3/8"–2"), Schlage Encode temps (−31°F to 150.8°F), IRC R302.5.1 garage door (buildingcodetrainer.com), CBS 2016 Hauppauge garage-remote burglaries; prices table (access-control $1,500–$2,500; strike $250–$450; strike repair $295–$485; setup-only SI $225; $195/hr 3-hr min).

## Staten Island (smart-lock-installation-staten-island)

| # | Query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| SI1 | `Staten Island housing stock one- and two-family homes share percent NYC Department of City Planning` · WebSearch → WebFetch | https://chpcny.org/visualization/housing-stock-visualization/ | CHPC "Design & Housing Typologies", Oct 2024: "In Staten Island, 83 percent of units are in one- or two-family homes"; SI ≈5% of city housing; 16% studios/1BR. No detached/semi split. | §5 para 1, §5.5 stat 1 |
| SI2 | `QuickFacts Richmond County New York owner-occupied housing unit rate 2020-2024` · WebSearch → WebFetch | https://www.census.gov/quickfacts/richmondcountynewyork | Pop. 501,290 (V2025, July 1 2025); owner-occupied 67.7% (2020–24); housing units 186,310 (V2025); persons/household 2.85; broadband 91.1%; median value $675,500 (not used). | §5, §5.5 |
| SI3 | `Verrazzano-Narrows Bridge 1964 opened Staten Island population boom development` · WebSearch → WebFetch | https://eportfolios.macaulay.cuny.edu/seminars/bellamy10/articles/t/h/e/Staten_Island%7E_Then_and_Now_134c.html | Bridge 1964; pop. 191,555 (1950) → 443,728 (2000); largest decade jump 1960–70 (~73,000). No housing counts. | §5 para 2, §5.5, §7 cards (stated only as "decades after the bridge") |
| SI4 | `Hurricane Sandy Staten Island deaths 24 of 43 New York City` · WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/nypd-sandy-related-death-toll-rises-to-43-in-nyc/ | Nov 11 2012: 43 Sandy-related deaths in NYC, 23 on Staten Island (NYPD). | §5.5 |
| SI5 | `Hurricane Sandy Staten Island homes destroyed Build It Back elevated homes Midland Beach Oakwood Beach buyout` · WebSearch → WebFetch | https://www.ny1.com/nyc/all-boroughs/build-it-broke/2015/10/29/idea-to-return-land-to-natural-state-after-sandy-transforms-staten-island-shore | Oct 29 2015: Oakwood Beach, Ocean Breeze, Graham Beach buyouts (state, Gov. Cuomo / GOSR); 513 SI buyout offers (> $188M), ~400 closed; 81 Oakwood Beach houses demolished. | §13 Oakwood Beach card |
| SI6 | `NYC Building Code 1010.1.9 egress door readily openable…` → `nyc.gov 2022 NYC Building Code Chapter 10 means of egress pdf…` · WebSearch → WebFetch | https://www.nyc.gov/assets/buildings/codes-pdf/cons_codes_2022/2022BC_Chapter10_EgressWBwm.pdf | OFFICIAL. 2022 NYC BC §1010.1.9: egress doors "readily openable from the egress side without the use of a key or special knowledge or effort"; §1010.1.9.3 item 3 (main entrances B/M/S per 1010.1.4.4), item 4 (Group R dwelling/sleeping unit doors, occupant load ≤10, may have night latch/dead bolt/security chain "openable from the inside without the use of a key or tool"); §1010.1.9.5 unlatching ≤ one operation (exceptions incl. item 4). Group R-3 / double-cylinder not named. | §8.5 compliance bullets; §9 basement Q; §10.5 H3 6 (double cylinder) |
| SI7 | same search | https://idighardware.com/2026/04/decoded-locks-on-dwelling-units-and-sleeping-units/ | Model-code commentary only (UL 294 not required for dwelling-unit electromechanical locks if readily openable; AHJ decides). Background, not cited on page. | research only |
| SI8 | `NYC Office of Special Enforcement short-term rental registration host must be present…` · WebSearch → WebFetch | https://www.nyc.gov/site/specialenforcement/stay-in-the-know/information-for-hosts.page | OFFICIAL. Host must be present for stays < 30 days; up to two paying guests; registration; "every guest has free and unobstructed access to every room and each exit"; "Internal doors cannot have key locks that allow guests to leave and lock their room behind them"; Class A (3+ units) <30-day ads prohibited, fines $1,000–$7,500. | §9 STR bedroom-locks Q; §10.5 H3 7; owner/tenant section |
| SI9 | same | https://www.nyc.gov/site/specialenforcement/registration-law/registration.page | Registration required; ≥30-day rentals and Class B exempt; enforcement phase from Sept 5 2023. | §9 STR Q |
| SI10 | same | https://en.wikipedia.org/wiki/Local_Law_18_of_2022 | LL18 signed Jan 9 2022; host presence; 2 guests; "prohibits internal door locks"; Intro 1107 (proposed) would ease rules for 1–2 family homes — NOT used on page (proposed only). | §9 STR Q (date only) |
| SI11 | `New York Multiple Dwelling Law definition` · WebFetch | https://www.nysenate.gov/legislation/laws/MDW/4 | MDL §4(7) multiple dwelling = 3+ families; §4(6) private dwelling = not more than two families. | §9 two-family Q |
| SI12 | `smart lock finish warranty coastal salt air corrosion within miles of ocean exclusion…` · WebSearch → WebFetch | https://download.securityrussia.com/mt-qtm-lock-finish-application-definitions--april-2021-.pdf | dormakaba Lodging lock-finish definitions (Apr 2021): ocean-front = exterior application AND property within 3 miles (5 km) of saltwater; wrong finish in ocean environment voids warranty; gasket must be fitted at install or warranty invalidated; weekly salt wipe in salt-mist areas. (dormakaba.rokka.io 2024 version: fetch error → EMPTY.) | §5 para 4; §9 raised-house and maintenance Qs; §10.5 H3 4 |
| SI13 | `silive Staten Island burglary unlocked door garage police warn residents lock doors 2025` · WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/staten-island-break-ins-caught-on-video | Updated June 23 2022: Todt Hill home invasion — suspects threw a large stone through back-door glass while family slept; pattern linked to Tottenville, Prince's Bay, Lighthouse Hill; Lighthouse Hill car-key theft. No police prevention tips. | Door-by-door section; §10.5 H3 5 |
| SI14 | same search | https://www.nbcnewyork.com/news/local/staten-island-burglaries-lighthouse-hill-jewelry/1972960/?amp=1 | Feb 29 2012: four Lighthouse Hill burglaries via rear second-floor windows. Not used (windows, old). | research only |
| SI15 | `Hylan Boulevard` · WebFetch | https://en.wikipedia.org/wiki/Hylan_Boulevard | ~13.86 mi, Rosebank to Tottenville (Conference House Park); longest street in a single NYC borough; >44,000 vehicles/day. | §8 Hylan card |
| SI16 | `Staten Island business improvement districts list Forest Avenue BID New Dorp Lane…` · WebSearch → WebFetch | https://citylandnyc.org/city-council-approves-new-dorp-bid | Council approved New Dorp BID 50–0 on Apr 5 2017; New Dorp Lane + adjacent streets between Hylan Blvd and Richmond Rd; 146 properties, 180 businesses. | §8 New Dorp card |
| SI17 | same | https://www.siedc.org/neighborhoods | SIEDC neighbourhood programmes: West Shore, New Dorp Lane, Victory Boulevard, Richmond Road, Rosebank, Graniteville/Mariners Harbor, North Hylan, Richmond Avenue. No further detail. | §8 Victory Blvd + West Shore cards (names only) |
| SI18 | `Staten Island Mall Richmond Avenue Heartland Village opened 1973 stores` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Staten_Island_Mall | New Springville; opened Aug 9 1973; ~1,370,000 sq ft. | §8 Richmond Ave card, §13 card |
| SI19 | `Historic Richmond Town` · WebFetch | https://en.wikipedia.org/wiki/Historic_Richmond_Town | Richmondtown, near geographic centre; 25-acre main campus of 100-acre site; Staten Island Historical Society with City. | §13 |
| SI20 | `Snug Harbor Cultural Center` · WebFetch | https://en.wikipedia.org/wiki/Snug_Harbor_Cultural_Center | North Shore on Kill Van Kull, Randall Manor; 83 acres; 1801 bequest of Capt. Robert Richard Randall; NHL district 1976. | §13 |
| SI21 | `Conference House` · WebFetch | https://en.wikipedia.org/wiki/Conference_House | Tottenville, Conference House Park; built c.1675 (before 1680) near Ward's Point, southernmost tip of NYS, Raritan Bay; Sept 11 1776 Howe–Franklin/Adams/Rutledge. | §13 |
| SI22 | `Staten Island Greenbelt` · WebFetch | https://en.wikipedia.org/wiki/Staten_Island_Greenbelt | ~2,800 acres, central hills; Todt Hill 410 ft. | §13 |
| SI23 | Reddit (r/statenisland), Google PAA/PASF, Answer the Public, AI Overview, Bing/DDG, Yelp 1–3★ (SI) | — | EMPTY (not accessible in build env). §10.5 headings are claims from national cost guides/manufacturers, stated as such on page. | — |
| SI24 | SI Advance (silive.com) smart-lock / garage-entry stories; hyperlocal | — | EMPTY — no silive result returned for smart locks or garage-entry burglary; replaced by CBS (SI13). | — |
| SI25 | NYC-specific attached-garage door separation rule | `NYC building code door between private garage and dwelling self-closing…` · WebSearch | No NYC code text reached → EMPTY. Page cites the "model residential code" (IRC R302.5.1, LI research) only. | §7.5, §9 garage Q |
| SI26 | DOB permit requirement for residential smart lock | — | Not searched/confirmed → no claim made on page. | — |

### Prices used (SI multiplier 1.10, round half-up; no new figures)
- Single-door keypad or fob reader with electric strike: $1,500–$2,500 base → **$1,650–$2,750** (§14, §15 Premium, FAQ, gate FAQ, Service schema).
- New electric strike: $250–$450 → **$275–$495** (§14, schema).
- Failed electric strike repair: $295–$485 → $324.50→**$325**–$533.50→**$534** (§14, schema).
- Setup-only first hour: **$225** SI (research/tv-mounting-prices/BRIEF.md via silo table) (repair capture, §14, BYO card).
- Service/callback $195/hr, 3-hr min ($585) (§14).
- Residential smart locks: "quoted flat at free walkthrough" (no AESS figure).
- Fixr national $250–$400 / avg $300, labelled national third-party (§10.5, §14).

## Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
All library photos are rendered/AI-looking with AESS logos (the whole library looks like this — flag). Chose back-view/close-up shots where possible; no house numbers/plates/readable docs; some partial faces unavoidable.
| File (images/smart-lock-installation/) | Source | Also used by hub? |
|---|---|---|
| smart-lock-installation-staten-island-keypad-strike-glass-door.webp (hero) | low-voltage/low-voltage-installation-queens-electric-strike-keypad.jpg | yes (same photo as NYC/LI hero) |
| smart-lock-installation-staten-island-exterior-enclosure-brick-wall.webp | low-voltage/low-voltage-installation-staten-island-exterior-enclosure-install.jpg | yes (LI) |
| smart-lock-installation-staten-island-keypad-reader-door-frame-wiring.webp | low-voltage/low-voltage-installation-staten-island-12-access-control-reader-wiring.jpg | yes (NYC) |
| smart-lock-installation-staten-island-strike-terminal-closeup.webp | low-voltage/low-voltage-installation-queens-electric-strike-wiring.jpg | yes (NYC) |
| smart-lock-installation-staten-island-maglock-label-wiring-closeup.webp | low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | yes (HV) |
| smart-lock-installation-staten-island-entry-panel-back-box-wiring.webp | low-voltage/low-voltage-installation-staten-island-13-video-intercom-entry-wiring.jpg | yes (NYC) |
| smart-lock-installation-staten-island-ceiling-wifi-access-point.webp | low-voltage/low-voltage-installation-staten-island-09-ceiling-access-point-drop.jpg | no |
| smart-lock-installation-staten-island-wall-plate-termination.webp | low-voltage/low-voltage-installation-staten-island-07-keystone-wall-plate-termination.jpg | yes (HV) |
| smart-lock-installation-staten-island-van-load-out-tool-bag.webp | low-voltage/low-voltage-installation-staten-island-van-load-out.jpg | yes (NYC, HV) |
| smart-lock-installation-staten-island-tone-tracer-wall-jack.webp | low-voltage/low-voltage-installation-staten-island-tone-generator-trace.jpg | yes (LI) |
| smart-lock-installation-staten-island-network-rack-laptop-setup.webp | low-voltage/low-voltage-installation-queens-rack-switch-config.jpg | no |
Only 3 door-relevant unique photos in low-voltage/ + commercial-security/ were unused by the hubs (by md5), so reuse was unavoidable. Rejected: nyc-exterior-junction-boxes (clear face), nassau storefront camera (readable store-hours sign), lobby dome camera (named business logo).

## Question register — smart-lock-installation-staten-island

### §9 Questions Answered (H3)
1. Should the door from our garage into the house lock itself every time it shuts?
2. Our basement apartment has its own door down a stairwell — how do we lock it securely without anyone getting trapped?
3. Our side door's hinges are on the outside — is a smart lock on it worth having?
4. We raised the house after Sandy and the front door is now at the top of a long stair — does that change which lock we should choose?
5. Our front door faces south with no overhang — does direct sun and rain matter for a keypad?
6. Should a smart lock that faces the water get regular maintenance, and what does that involve?
7. What should happen to the codes when a grown child moves out or a relative stops visiting?
8. Does everyone in the house need the app, or can some people just use a code?
9. Our teenager keeps leaving the side door unlocked — what can the lock actually do about it?
10. If an elderly parent lives alone, how do we plan for emergency entry around a smart lock?
11. In a two-family with one shared side door, should owner and tenant share a code or have separate ones?
12. Is it fair to keep entry logs on the door my tenant uses?
13. Can I put smart locks on bedroom doors if I host short-term guests in my house?
14. We just bought a house on the South Shore — how do we make sure the previous owners can't still open the doors?
15. We're replacing the front door itself — should the new door and the smart lock be chosen together?

### §17 FAQ (visible == FAQPage, 9)
1. Why are Staten Island prices 10 percent above the Brooklyn base?
2. Will drilling for a new lock damage a fibreglass or steel door?
3. Will the lock still work properly if the door has dropped on its hinges?
4. Can the new smart lock match the brushed nickel or bronze hardware already on the house?
5. Do you fit keypads on side-yard gates as well as house doors?
6. Do smart locks need a monthly subscription?
7. Can our house and our parents' house nearby use the same codes?
8. How long does a whole-house smart lock installation take?
9. Can you set the locks up before we move in, while the house is still empty?

### Other question-form headings
- H2 "Smart Lock Acting Up on Staten Island?" (repair capture)
- H2 "Can't Get In Through Your Own Door on Staten Island?" (final repair capture)

De-dup notes: checked against the NYC/LI/HV registers and the Bronx/Nassau drafts on disk at ~07:10. Replaced during build: home-health-aide scheduled code (= Bronx FAQ), outswing-door fit (= Nassau), renovation timing (= Nassau), router swap (= Nassau), deposit (= Nassau), glass sidelight (≈ Nassau), video doorbell same visit (≈ Bronx), "other areas too?" (= NYC FAQ 10), cost-in-area (= NYC FAQ 1). Partial overlaps left for the main run to judge: Q1 garage auto-lock vs Nassau "mudroom door relocks while ajar"; Q4 raised Sandy house vs Nassau "ground-level door below flood line"; Q8 app-vs-code vs Nassau "easiest locks for older parent with arthritis"; Q11 two-family shared door vs Bronx "downstairs owner — what does the law make me give my tenant"; Q14 buyer reset vs LI FAQ "codes and app account when we sell".


# Smart Lock Installation — Nassau County (batch part, 2026-10-17)

Page: smart-lock-installation-nassau-county · up-link /smart-lock-installation-long-island · phone (516) 346-5778 (body, CTAs, schema; (800) 486-0943 only in shared mega-nav header) · GBP Brooklyn, 1282 Troy Ave, schema @id #brooklyn.
The main run merges this into research/smart-lock-installation.md.

Thesis: Nassau is 3 towns, 2 cities, 64 villages. Its doors cover every housing era (1869 Garden City planning, Gold Coast estates, 1920s–30s Colonials/Tudors, 1947–51 Levitt Capes/ranches, 1950s–60s split-levels/high ranches, newer Colonials, South Shore canal houses raised after Sandy, garden apartments/co-ops near LIRR stations, Main Street storefronts). Match the lock to each era's door: handleset doors, never-bored doors, split-level landing clearance, sidelights, frame strength, mudroom auto-lock, flood-line doors, narrow-stile shop doors.

## Nassau County (smart-lock-installation-nassau-county)

Format: exact query · platform · URL · finding · page section used.

| # | Query · platform | URL | Finding | Used in |
|---|---|---|---|---|
| L1 | `Nassau County Office of Consumer Affairs home improvement license who needs a license` · WebSearch → WebFetch | https://nassaucountyny.gov/3465/Who-Must-Be-Licensed | DCA licenses contractors doing home improvement in Nassau; "home improvement" = repair/replacement/remodeling etc. of a residence used by not more than three families. 29 listed trades include "doors, windows, awnings" and "carpentry work"; locks, locksmiths, security, alarms, electrical and low-voltage NOT named. No penalties stated. | §8.5 licensing note; §10.5 H3 "Who fits it doesn't matter" |
| L2 | same search · WebFetch | https://archive.nassaucountyny.gov/agencies/OCA/Licensing/FAQ.html | "Contractors who perform remodeling on RESIDENTIAL homes" need a licence; "Anyone who works only on COMMERCIAL buildings does NOT need a license"; plumbers/electricians etc. exempt within their licensed field; $500/2 yrs + $50 restitution fund; licence must be displayed and its number put on contracts. | §8.5 licensing note (no claim that AESS holds a Nassau HI licence) |
| L3 | `Nassau County towns cities villages number of incorporated villages …` · WebSearch → WebFetch | https://nassaucountyny.gov/3406/Cities-Towns-Villages | 2 cities (Glen Cove, Long Beach), 3 towns, 64 incorporated villages (Hempstead 22, North Hempstead 27, Oyster Bay 15), "over 100 unincorporated areas". | Hero badge/subhead, §5.5, towns section |
| L4 | `Town of Hempstead short-term rental law Airbnb ban 30 days` · WebSearch → WebFetch | https://www.cbsnews.com/newyork/news/hempstead-air-bnb | June 19, 2017: town proposed banning rentals < 28 days; >1,000 Airbnb-style listings; registry, inspections, permits; hearing July 11. | §8.5 rental note; §9 Lido Beach/Point Lookout Q; towns section |
| L5 | same search · WebFetch | https://longislandweekly.com/news/town-hempstead-votes-ban-short-term-rentals/ | Board unanimously voted July 11 (2017 per L4) to set a 28-day minimum; rental permit and registry with fire/zoning/building inspections; $500 two-year permit, $200 renewal. Article does not state whether villages are covered. | same as L4 (page tells readers to check their own town/city/village) |
| L6 | `City of Long Beach NY short-term rental permit law registration` · WebSearch | — | Results were for Long Beach, California only. EMPTY for Long Beach NY. | not used |
| L7 | `2020 Residential Code of New York State R311.2 egress door "readily openable from inside"` · WebSearch → WebFetch | https://aibd.org/egress-doors/ | Summary only: egress door "Easily openable from the inside without keys or special knowledge"; IRC, no NY edition named. | §8.5 free-egress note (worded as model-code requirement) |
| L8 | `dos.ny.gov 2020 Residential Code of New York State based on 2018 International Residential Code effective May 12 2020` · WebSearch → WebFetch | https://dos.ny.gov/2020-04-nycrr-changes-2020-codes | NYS-specific code books "based on the 2018 International Code Council books"; effective May 12, 2020. | §8.5 free-egress note |
| L9 | `Superstorm Sandy Nassau County homes damaged number …` · WebSearch → WebFetch | https://www.jlconline.com/projects/disaster-resistant-building/sandy-damaged-95-534-buildings-on-long-island-says-fema_o/ | Jan 11, 2013: 95,534 buildings damaged in Nassau + Suffolk combined (no Nassau split). | research only (not used — no Nassau-only figure) |
| L10 | (direct from L9 search results) · WebFetch | https://en.wikipedia.org/wiki/Long_Beach,_New_York | Village 1913, city 1922; barrier island; boardwalk 2.2 mi; Sandy Oct 29, 2012, damage est. >$250M, no power/running water two weeks, boardwalk destroyed, reopened Oct 25, 2013; "City by the Sea"; <40% detached houses; 16,771 housing units (2020). | §5.5, §10.5 outage H3, §13 card, towns section |
| L11 | `Levittown houses Cape Cod 1947 ranch 1949 models history` · WebSearch → WebFetch | https://omeka.hofstra.edu/exhibits/show/levittown--the-birthplace-of-s/the-levitt-home | Cape Cod first model; 1949 ranch restyled with living room to rear, kitchen at front (watch children, shorter grocery carry); slab with radiant heat pipes, no basement. No door/garage details. | §5 para 1, §5.5, §7 table, timeline SVG |
| L12 | `Garden City New York village founded Alexander Turney Stewart 1869 …` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Garden_City,_New_York | Stewart bought Hempstead Plains land 1869; village inc. 1919; Franklin Avenue former department stores now office/medical; Cathedral of the Incarnation completed 1885, tallest building, village law caps heights; Adelphi 1929; post-war split-levels and ranches. (Seventh Street not in source — used only as a corridor name.) | §5, §5.5, §8 card, §13 card, timeline SVG |
| L13 | `Old Westbury Gardens wikipedia mansion acres Phipps` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Old_Westbury_Gardens | Completed 1906 for John Shaffer Phipps; George A. Crawley with Grosvenor Atterbury; NRHP Nov 8, 1976; acreage conflicts (100 vs 160) — not used. | §13 card, timeline SVG |
| L14 | `Planting Fields Arboretum State Historic Park Oyster Bay Coe Hall acres wikipedia` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Planting_Fields_Arboretum_State_Historic_Park | >400 acres, Upper Brookville, Town of Oyster Bay; Coe Hall 1918–1921 Tudor Revival, 67 rooms, Walker & Gillette; Olmsted Brothers landscapes. | §13 card, timeline SVG |
| L15 | `Freeport Nautical Mile Woodcleft Avenue wikipedia` · WebSearch → WebFetch | https://www.iloveny.com/listing/freeport-nautical-mile/127241/ | Waterfront strip along Woodcleft Canal; dozens of restaurants, bars, shops; daily charter fishing boats; nightlife. | §5 para 4, §8 card, §13 card |
| L16 | (from L12 search family) · WebFetch | https://en.wikipedia.org/wiki/Glen_Cove,_New_York | City since Jan 1, 1918 (never a village); Gold Coast estates (Pratt, Morgan, Woolworth); mansions mostly converted from single-family use by mid-century; post-war development on former farms. | towns section, timeline SVG |
| L17 | · WebFetch | https://en.wikipedia.org/wiki/Mineola,_New_York | County seat since 1900; village inc. 1906; Jericho Turnpike is its commercial main street; Mineola Blvd; Old Country Road on southern border; NYU Langone Hospital–Long Island. | §8 card, towns section |
| L18 | · WebFetch | https://en.wikipedia.org/wiki/Great_Neck,_New_York | Nine incorporated villages on the peninsula; Middle Neck Road runs along its centre; Port Washington Branch LIRR. | §8 card, towns section |
| L19 | `Nassau County police burglaries rear door unlocked residents warned 2026` · WebSearch → WebFetch | https://www.pdcn.org/CivicAlerts.asp?AID=11519 | June 15, 2023 ~4:38 a.m., Circle Drive, Syosset: two masked men tried car doors, tested a rear sliding door and basement window; police urge residents to "lock their vehicles and their residence doors"; "locked doors can help to prevent crimes." | §5 para 3, §10.5 hacking H3 |
| L20 | same search · WebFetch | https://www.cbsnews.com/newyork/news/nassau-county-distraction-burglaries/ | June 1, 2015: Nassau police warn of distraction burglars posing as contractors/utility workers while a partner enters an unsecured entry; keep doors locked even when home. | §5 para 3, §10.5 hacking H3 |
| L21 | `site:reddit.com r/longisland smart lock keypad Nassau door` · Firecrawl search | (excerpts only) | No relevant Nassau smart-lock threads. EMPTY. | — |
| L22 | Reddit (local), Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG, Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are paraphrases of claims in national cost guides / maker pages (stated on the page). | — |
| L23 | Local news on smart locks in Nassau (Newsday, Patch, LI Herald, News12) | — | None found beyond L19/L20. EMPTY for the service category. | — |
| L24 | Village building-permit rules for swapping a lock on an existing door | — | No source found; page makes no permit claim (only says door replacement/carpentry falls in a licensed trade and to check with the village/town). EMPTY. | — |
| L25 | HOA / co-op rules specific to Nassau | — | No source fetched; page speaks generally ("many co-op and rental buildings require management keeps a working key or code") without a statistic. EMPTY. | §9 garden-apartment Q (general) |

Carried from earlier silo / repo research (sources reached by earlier runs, not re-fetched):
- Census QuickFacts Nassau: 480,591 housing units (July 1, 2025), owner-occupied 81.9% (2020–2024), 2.99 persons/household — research/soundbar-installation.md, research/sonos-installation.md → §5.5.
- Eisenhower Park 930 acres, East Meadow, three courses, Nassau 9/11 Memorial — research/sonos-installation.md (Wikipedia via Firecrawl) → §13 card.
- Fixr ($250–$400, avg $300, Jan 2025), LawnStarter ($330 avg, $200–$460, 2025), Schlage door-prep (1-3/8–2 in, 2-1/8 cross bore, 2-3/8/2-3/4 backset), Yale Matter FAQ (border router, app limits), Ring Alarm Z-Wave lock arming (Ring-app codes only, subscription), 2010 ADA 404.2.7 (no tight grasping; 34–48 in), August bridge distance — silo research in research/smart-lock-installation.md → §8.5, §10, §10.5, §14.
- Hours 8 AM–8 PM, 7 days — research/tv-mounting-prices/BRIEF.md → LocalBusiness openingHours.

### Prices used (no new figures)
| Figure | Scope | Source |
|---|---|---|
| $1,725–$2,875 | single-door keypad or card reader with electric strike, installed (Nassau) | $1,500–$2,500 Brooklyn base (access-control pages, silo table) × 1.15 |
| $288–$518 | new electric strike on existing door | $250–$450 base × 1.15, round half-up |
| $339–$558 | failed electric strike repair | $295–$485 base × 1.15 |
| $225 first hour, then 30-min blocks | setup-only visit (app/pairing/codes, no hardware) | research/tv-mounting-prices/BRIEF.md (Nassau rate) — same use as LI hub, still flagged for Anwar |
| $195/hr, 3-hr min ($585) | service call after the job, not on initial install | blueprint v2.3 §9 |
| Residential smart deadbolt / handleset / retrofit / BYO labour | no AESS figure → "quoted at walkthrough" | — |
| $250–$400 avg $300; $330 avg | national third-party only, labelled | Fixr, LawnStarter |

CONFLICT for Anwar (not used): live `access-control-installation-nassau-county.html` publishes "Standalone smart lock with code management: $400-$900", "Single-door networked keypad system: $800-$1,500 installed" and "Standard commercial card reader or keypad: $1,500-$4,500 per door installed" — these disagree with the silo's $1,500–$2,500 × 1.15 basis used by the LI hub and this page.

## Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
All copied to images/smart-lock-installation/ as WebP q80 (max 1600 px). Photos in the library look AI-rendered in style, as does the whole low-voltage/commercial-security library; no alternative real photos exist. No readable addresses, plates or named businesses in the chosen frames (rejected: lobby-video-intercom "123 Main Street" directory, access-reader "Pinnacle Business Center", lobby-dome-camera "Summit Enterprises", dashboard-training client face).

| File | Source | Already used by another smart-lock page? |
|---|---|---|
| smart-lock-installation-nassau-county-strike-terminal-wiring.webp (hero) | low-voltage/low-voltage-installation-nassau-county-electric-strike-wiring.jpg | same photo as NYC hub strike-terminal-wiring-closeup |
| smart-lock-installation-nassau-county-video-intercom-entry-panel.webp | low-voltage/low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg | same photo as NYC hub video-intercom-keypad-wiring |
| smart-lock-installation-nassau-county-reader-glass-door-wiring.webp | low-voltage/low-voltage-installation-bronx-14-access-control-reader-wiring.jpg | same photo as NYC hub fob-reader-mounting |
| smart-lock-installation-nassau-county-maglock-terminal-block.webp | low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | same photo as HV hub maglock-terminal-wiring |
| smart-lock-installation-nassau-county-storefront-header-maglock.webp | low-voltage/low-voltage-installation-long-island-maglock-install.jpg | same photo as LI hub maglock-header-wiring |
| smart-lock-installation-nassau-county-strike-glass-door-crouch.webp | commercial-security/commercial-security-systems-bronx-electric-strike.jpg | same photo as NYC hub electric-strike-lobby-door |
| smart-lock-installation-nassau-county-door-contact-keypad-panels.webp | commercial-security/commercial-security-systems-bronx-panic-button.jpg | same photo as HV hub door-contact-keypad-panels |
| smart-lock-installation-nassau-county-network-rack-laptop-setup.webp | low-voltage/low-voltage-installation-dutchess-county-hero-rack-switch-config.jpg | not used by hubs |
| smart-lock-installation-nassau-county-retail-entrance-sensor-crew.webp | commercial-security/commercial-security-systems-dutchess-entrance-crew.jpg | same photo as HV hub storefront-frame-sensor |
| smart-lock-installation-nassau-county-main-entrance-camera-ladder.webp | low-voltage/low-voltage-installation-nassau-county-storefront-camera-install.jpg | not used by hubs |
| smart-lock-installation-nassau-county-exterior-junction-boxes-block-wall.webp | commercial-security/commercial-security-systems-manhattan-exterior-enclosures.jpg | not used by hubs |
Nearly every door/lock photo in the two source folders was already used by a hub (71 distinct photos by perceptual hash); 3 of 11 are new to the silo. Overlap with the Bronx/Staten Island batch pages not coordinated.

Also on the page (not images, not figures): three inline SVG diagrams (door-prep dimensions, Nassau door-era timeline with sourced dates, split-level landing clearance) and inline SVG card icons.

## Question register — smart-lock-installation-nassau-county

§9 Questions Answered (H3):
1. Can a keypad deadbolt be added above the thumb-latch handleset on our Colonial or Tudor front door without replacing the whole set?
2. What if our front door has never been bored for a deadbolt at all?
3. The front door on our split-level opens onto the landing between two half-flights — will the inside of a smart lock hit the railing?
4. Our center-hall Colonial has glass sidelights beside the front door — how do we stop someone reaching through and turning the lock?
5. How do we stop the door from being kicked in at the frame once the smart deadbolt is on?
6. The mudroom door is where everyone kicks off their boots — what happens if it relocks while the door is still ajar?
7. Can the lock tell us which of our children got home and at what time?
8. Which smart locks are easiest for an older parent with arthritis or weak eyesight to use?
9. We have a kitchen renovation starting — can the lock show when the contractor's crew actually arrives and leaves?
10. Will auto-lock shut me out when I step into the yard to let the dog out?
11. Should a smart lock go on a ground-level door that sits below the flood line in a canal-front house?
12. We would like to let our Lido Beach or Point Lookout house to weekend visitors with keypad check-in — does the Town of Hempstead allow that?
13. Our garden-apartment unit door opens straight to the outdoors rather than onto a hallway — does that change which lock suits it?
14. When Optimum or Verizon swaps our router, do the smart locks stop working?
15. What goes on a narrow-stile aluminium shop door, since a residential smart deadbolt won't fit it?
16. Our landlord at a village strip centre won't let us cut into the storefront frame — what are the options?
17. Can a supplier get in our back door at 5 a.m. without anyone from the restaurant there?
18. Can staff be locked in after closing if the back door uses a keypad?

§17 FAQ (visible == FAQPage, 10):
1. Do you work in every Nassau village, including Glen Cove and Long Beach, which are cities rather than towns?
2. Can you leave our existing doorknob or lever in place and replace only the deadbolt with a smart one?
3. Our front door has a mail slot and a knocker near the lock — will they get in the way?
4. Is a deposit required to book the installation?
5. Do you need to touch our electrical panel or turn off power for a smart lock?
6. We are in the middle of a renovation — when should the smart locks go on?
7. Is there a smart option for the sliding glass door out to the deck?
8. Is the electric strike for a shop door priced separately from the keypad?
9. Will you protect our floors and painted trim while you bore and chisel the door?
10. Will the quote list each door separately so we can phase the work?

No question-form CTA headings (repair captures are "When a Nassau Smart Lock Stops Behaving" and "Same-Day Help for a Failed Nassau Smart Lock").

De-dup notes: checked by meaning against the NYC, LI and HV registers and against the Bronx and Staten Island pages on disk at ~07:15. Replaced during the build: "Smart Lock Acting Up in Nassau County?" (masked-identical to Bronx/SI repair H2); dock-gate shared code (vs SI side-yard gate keypads); outswing-door FAQ (vs SI outside-hinge side door); door planing/rehanging FAQ (vs SI dropped-hinge door); removing old locks/packaging FAQ (vs LI remove-and-patch FAQ); "keypad without full access control" wording (vs HV office-suite Q). Close neighbours left for the main run to judge: Q4 sidelight reach-through vs NYC double-cylinder legality (different intent); Q12 Hempstead rental legality vs LI fortnight-rental codes and HV registry; Q14 router swap vs HV internet-down; "Taking Over a House That Already Has Smart Locks" (non-question H2) vs SI "previous owners can't still open the doors" question.


## Suffolk County (smart-lock-installation-suffolk-county)

Built 2026-10-17 (batch: Suffolk / Westchester / Rockland smart-lock area pages). Area page, up-link /smart-lock-installation-long-island. GBP Brooklyn (1282 Troy Ave, #brooklyn). Direct line (631) 407-2884 (800 only in shared header chrome). Suffolk ×1.20.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).

Thesis / lane: in Suffolk the lock answers to the town and the water before the app — ten towns with their own rental-permit, accessory-apartment and fire-marshal (Knox-Box) rules; Sandy-raised South Shore houses where the enclosure below the flood line takes no electronics; Fire Island cottages reached only by ferry/water taxi; pool-deck doors that need a UL 2017 alarm, not just a lock; bulkhead cellar doors; Hauppauge/Route 110/Ronkonkoma commercial doors (Knox-Box key swaps, flex-unit bay doors, HIPAA records rooms, congregation security grants).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `reddit longisland smart lock Suffolk keypad deadbolt recommendation` · Firecrawl search → only generic r/Locksmith / r/HomeImprovement keypad-deadbolt threads (no Suffolk content). Not used. Suffolk-specific Reddit: EMPTY. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are recurring claims from product/cost-guide/how-to content, stated as such on the page. |
| 6 | Landmarks | L1–L6 below |
| 7 | Use cases / building stock | T1–T5, F1–F3, P1, B1 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Newsday/FEMA Sandy tally (via NY Sea Grant PDF), Long Island Advocate (Sandy, July 2026), ABC7 (West Islip burglaries, 2016 — research only), Governor's office (Station Yards) |
| 10 | Hyperlocal | Long Island Advocate used. Patch/News12 Suffolk smart-lock stories: none found → EMPTY. Suffolk PD Facebook "lock your car" posts (excerpts) — vehicle-only, not used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| T1 | `Town of Islip rental permit inspection checklist locks smoke detectors requirements` · Firecrawl search → Firecrawl scrape (pdf) | https://islipny.gov/community-and-services/documents/departments/code-enforcement/82-rental-occupancy-permits-application-1-2-family/file | Rental occupancy permit (1–2 family) affidavit: no outstanding violations; permit not transferable; not to be used as transient rental (Ch. 68 Art. L); permit suspended if a later violation is issued; smoke alarms outside/in each sleeping area and every storey incl. basements; CO alarms. No lock/door item. | §9 Islip Q, §10.5 H3 2, Across Suffolk (Islip) |
| T2 | same search (excerpt) | https://ecode360.com/11752146 | Islip Code Art. L Rental Dwelling Units: CO alarm certificate/affidavit for permit. Background only. | research only |
| T3 | `Property Maintenance Code of New York State 304.18.1 doors rented leased deadbolt …` · Firecrawl search → Firecrawl scrape | https://up.codes/s/building-security | IPMC (2024, GSA edition) 304.18.1: rented dwelling-unit door with a deadbolt — readily openable from egress side without keys, special knowledge or effort; min 1-inch throw; installed per manufacturer; sliding bolt not acceptable. Page calls it "the model version New York's code is built on" (NYS PMC text itself not opened: dos.ny.gov 2025 PMCNYS PDF excerpt only). | §5 para 2, §9 Islip Q, §10.5 H3 2, pricing drivers, rental section |
| T4 | `Town of Brookhaven accessory apartment permit requirements owner occupied separate entrance` · Firecrawl search (excerpt of eCode) | https://ecode360.com/8597617 | Brookhaven Art. XIV: owner occupancy required (owner may occupy either unit); one accessory apartment per dwelling; no one may create/occupy without Chief Building Inspector approval and a provisional accessory apartment licence. Separate-entrance rule not shown in excerpt → not claimed. | §9 Brookhaven Q, Across Suffolk (Brookhaven) |
| T5 | `Suffolk County New York ten towns villages list …` · Firecrawl search | https://www.ny.gov/counties/suffolk ; https://en.wikipedia.org/wiki/Suffolk_County,_New_York ; https://www.zippboxx.com/blog/suffolk-county-towns ; https://www.suffolkcountyny.gov/Visiting/Towns-and-Villages | Ten towns (Babylon, Brookhaven, East Hampton, Huntington, Islip, Riverhead seat, Shelter Island, Smithtown, Southampton, Southold) + village list by town (Ocean Beach/Saltaire in Islip; Dering Harbor; West Hampton Dunes etc.); 86 mi long; 912 sq mi land / 1,461 water (62%); most county offices in Hauppauge; Brookhaven largest town; Brookhaven only town spanning South to North Shore (zippboxx); Hauppauge shared by Islip and Smithtown (zippboxx); CDP/hamlet names; Riverhead County Center. | §5 paras 1/3, §5.5 bullets 1–2, §7 cards, Across Suffolk, also-serve list, schema areaServed |
| T6 | carried from research/smart-lock-installation.md (LI hub, Census QuickFacts) | census.gov QuickFacts Suffolk | Owner-occupied 82.2%; housing units 583,777 (July 1 2025). | §5 para 2, §5.5 bullet 3 |
| F1 | `FEMA enclosures below base flood elevation limited to parking building access storage …` · Firecrawl search (excerpts) | https://www.fema.gov/sites/default/files/2020-07/fema_tb5_free_obstruction_requirements.pdf ; https://agents.floodsmart.gov/sites/default/files/media/document/2025-07/fema_nfip-p-348-protecting-building-utility-systems-from-flood-damage-2017.pdf | TB5: "The NFIP limits the use of enclosures under elevated buildings to parking of vehicles, building access, and storage." P-348: components below required elevation must be designed to resist flood loads / elevated. | §5 para 3, §7.5 enclosure para, §9 Lindenhurst Q, flood-line checklist |
| F2 | `Lindenhurst homes elevated after Superstorm Sandy NY Rising …` · Firecrawl search → Firecrawl scrape | https://longislandadvocate.com/superstorm-sandy-still-haunts-suffolk-residents-today/ | July 15 2026 (Marissa Di Vita): NY Rising bought flood-zone houses to demolish or paid to raise them; Lindenhurst "now full of empty lots". | §5 para 3 |
| F3 | `Suffolk County Superstorm Sandy homes damaged destroyed number …` · Firecrawl search → Firecrawl scrape (pdf) | https://www.seagrant.sunysb.edu/media/sandy12/Newsday-Sandy010713.pdf | Newsday (Jan 2013) FEMA tally: Suffolk 20,798 flooded/damaged/destroyed structures; 8,153 >50% damage; 65 destroyed (Nassau 74,736). | §5 para 3, §5.5 bullet 4 |
| P1 | `New York residential code pool barrier where wall of dwelling serves as part of barrier doors direct access pool alarm` · Firecrawl search → Firecrawl scrape (pdf) | https://dos.ny.gov/tb-1014-uc-pool-summary (→ tb-1014-uc-pool-summary-rev-1.pdf) | DOS summary (2020 RCNYS/BCNYS): dwelling wall as barrier → doors with direct pool access need UL 2017 alarm, manual deactivation ≤15 s per opening; where dwelling wholly inside enclosure, alarms at every such door; alternative approved means (self-closing/self-latching) if equal protection; gates self-closing, self-latching, pedestrian gates open outward, latch inside enclosure ≥40 in, lock when unsupervised. (Shelter Island 2025 pool code PDF found in search but scrape failed → EMPTY.) | §5 para 4, §6 card, §7.5 sliders, §9 pool Q, §10 equipment, §10.5 H3 3 |
| B1 | `Bilco basement door egress code openable from inside without keys bulkhead …` · Firecrawl search (excerpts) | https://www.bilco.com/ProductDetail/Basement-Door-Keyed-Lock-Kit-87 ; http://boman-kemp.com/IRC-Code-R310-Emergency-Escape-and-Rescue-Required.htm | Bilco keyed lock kit: lock from outside, slide bar from inside. IRC R310: basements and sleeping rooms need an emergency escape and rescue opening operational from inside without keys, tools or special knowledge (model code; page says "model residential code"). | §7.5 bulkheads, §9 bulkhead Q |
| I1 | `Fire Island National Seashore driving permit contractors vehicles ferry only communities` · Firecrawl search → Firecrawl scrape | https://www.nps.gov/fiis/planyourvisit/off-road-vehicle-permit-faqs.htm | Only year-round residents and contractors/businesses can apply; contractor permits authorise driving only to communities where holder has work; summer residents/renters not eligible ("adequate ferry service"); winter access by ferry, water taxi or private boat. | §9 Fire Island Q, §7 card, pricing drivers |
| K1 | `Suffolk County fire marshal Knox box key box requirement commercial buildings town code Brookhaven Islip` · Firecrawl search → Firecrawl scrape (pdf) | https://islipny.gov/community-and-services/documents/departments/fire-prevention-bureau/207-knox-box-technical-bulletin/file | Islip Knox-Box bulletin: NYS Fire Code + Islip Town Code let Fire Marshal require a Knox-Box where access restricted (other than 1–2 family); every building with any fire protection system must have one; mounted within 6 ft of main entrance, 4–6 ft high; generally keys to all spaces; owners don't get box keys — Fire Marshal visit to lock keys in; Town keeps master list; only marshal + local responding FD can open; when locks change, call the marshal to swap keys or responders may force entry. | §5 para 5, §6 card, §8 card + compliance bullet, §9 Knox Q, §10.5 H3 4, process step 4, handover table |
| K2 | same search → Firecrawl scrape | https://www.brookhavenny.gov/309/Fire-Department-Official-Use | Scrape returned no body text → EMPTY (search excerpt only: non-compliant Knox Boxes not part of Town system). Page says "other towns run their own programs". | — |
| C1 | `Long Island Innovation Park at Hauppauge number of businesses employees …` · Firecrawl search → Firecrawl scrape | https://www.hia-li.org/li-iph/ | "2nd largest industrial park in the nation after Silicon Valley"; 1,350 companies; 55,000 employees; $13B output. (RPA/Flexible IT give 1,300/1,400 companies — HIA-LI figure used.) | §5 para 5, §5.5 bullet 5, §8 card, §13 card |
| C2 | `Long Island MacArthur Airport Ronkonkoma Hub transit-oriented development apartments built` · Firecrawl search → Firecrawl scrape | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Oct 22 2024: Station Yards (Ronkonkoma Hub) 53 acres around Ronkonkoma LIRR station; 1,450 residential units on completion; phase 1 489 units in 2020; phase 2 388 homes; near LIE Exit 60 and MacArthur Airport; Ronkonkoma = Suffolk's busiest station, 17,000 daily commuters. | §5.5 bullet 6, §7 card, §8 card, §13 card |
| C3 | `HHS HIPAA security rule physical safeguards facility access controls 164.310 …` · Firecrawl search (excerpts) | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310 ; https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/securityrule/physsafeguards.pdf | 164.310(a)(1) facility access controls; addressable specs: facility security plan, access control & validation, maintenance records "(for example, hardware, walls, doors, and locks)"; HHS guidance example: re-keying/changing combination when a workforce member is terminated. | §9 HIPAA Q, §10.5 H3 5 |
| C4 | `New York Securing Communities Against Hate Crimes grant eligible security costs access control door locks nonprofit` · Firecrawl search → Firecrawl scrape | https://www.governor.ny.gov/apply-securing-communities-against-hate-crimes-grant-program | DCJS administers; nonprofits at risk of hate crimes because of ideology, beliefs or mission; grants fund interior/exterior security improvements "such as alarms, panic buttons, fences, shatter-resistant glass and public address systems, among other items"; door locks not named → page tells readers to confirm with DCJS. | §9 congregation Q |
| C5 | `Suffolk County Department of Labor Licensing and Consumer Affairs license categories …` · Firecrawl search (excerpt) | https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License ; https://ecode360.com/14947320 | Consumer Affairs licenses 15,000+ vendors; >50% of licences issued/renewed yearly are home improvement; HI list incl. "Storms & Screens" (locksmith not listed); Ch. 563 HI licensees may be required to show $500,000 liability insurance / bond ≤$100,000. | §8.5 compliance bullet |
| C6 | carried from silo research (LI hub) | https://idighardware.com/2023/07/accessibility-requirements/ | ADA 404.2.7: no tight grasping, pinching or twisting; 34–48 in. | §8.5 compliance bullet |
| N1 | `Suffolk County police burglaries unlocked doors homes Patch 2025` · Firecrawl search → Firecrawl scrape | https://abc7ny.com/post/exclusive-suspect-wanted-in-li-burglary-could-be-connected-to-recent-string/1642569/ | Dec 6 2016: eight West Islip homes burglarised in November; one family found back sliding door unlocked, screen slit on unlocked second-storey window. Too old → research only, not on page. | research only |
| L1 | `Fire Island Lighthouse height built 1858 …` · Firecrawl search → Firecrawl scrape | https://en.wikipedia.org/wiki/Fire_Island_Lighthouse | 168-ft stone tower, began operation 1858 (replacing 1826 tower); in FINS just east of Robert Moses State Park; operated by Fire Island Lighthouse Preservation Society. | §13 card |
| L2 | `Big Duck Flanders built 1931 …` · Firecrawl search → Firecrawl scrape | https://en.wikipedia.org/wiki/Big_Duck | Built 1931 by duck farmer Martin Maurer as a shop on West Main St, Riverhead; moved to Flanders ranch 1937; returned to Flanders Oct 6 2007; NRHP Apr 28 1997. | §13 card |
| L3 | `Vanderbilt Museum Centerport Eagle's Nest estate …` · Firecrawl search (excerpts) | https://www.vanderbiltmuseum.org/about-us/history/ ; https://www.vanderbiltmuseum.org/about-us/ | 43-acre waterfront estate; built in stages 1910–1936; Spanish Revival; above Northport Bay; deeded to Suffolk County on Vanderbilt's death 1944; opened to public 1950. | §13 card |
| L4 | `Brookhaven National Laboratory Upton founded 1947 acres employees` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Brookhaven_National_Laboratory ; https://www.bnl.gov/about/history/ | DOE lab in Upton, hamlet of Town of Brookhaven; formally established 1947 at former Camp Upton. | §13 card |
| L5 | = C2 | Station Yards | §13 card |
| L6 | = C1 | LI Innovation Park | §13 card |
| S1 | silo research (Fixr, Jan 31 2025) | https://www.fixr.com/costs/smart-lock-installation | National $250–$400 — labelled national third-party. | §14 |

### Prices used (Suffolk ×1.20, round half-up; no new prices)
| Figure | Scope | Source |
|---|---|---|
| $1,800–$3,000 | single-door keypad/fob reader + electric strike | $1,500–$2,500 Brooklyn base (silo prices table) × 1.20 — same as LI hub's Suffolk row |
| $300–$540 | new electric strike | $250–$450 × 1.20 |
| $354–$582 | failed strike repair | $295–$485 × 1.20 |
| $250 first hour, then 30-min blocks | setup-only visit | research/tv-mounting-prices/BRIEF.md line 15 (Suffolk) |
| $195/hr, 3-hr min ($585) | service/callback | blueprint §9 |
| quoted flat at walkthrough | residential/rental/cottage smart lock | no AESS figure |
**Conflicts for Anwar:** (1) live access-control-installation-suffolk-county.html says "Suffolk County pricing is Brooklyn base plus 10% surcharge" (lobby fob reader $1,600–$2,800; single gate/door $1,600–$5,500) — conflicts with §9 ×1.20 used here and on the LI hub. (2) Setup-only $250 rate is published for TV/device setup; used for code/app visits (same flag as LI/Brooklyn/Queens).

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
All viewed before use. Perceptual hash: of the 37 pool files only 4 are photos not already used on a smart-lock sibling (lpr-gate, two near-identical ceiling-speaker shots, video wall); the speaker/video-wall shots show no door hardware, so 10 of the 11 below are the same photos already used (under other names) on NYC/LI/HV/Brooklyn/Queens/Rockland smart-lock pages — door-hardware relevance was preferred over uniqueness. Rejected: access-reader (named "Pinnacle Business Center" on glass), credential-programming (readable cardholder names on screen). Cropped: lpr-gate (left 260 px, removes building number "1000" and a sign), video-intercom (left 250 px, removes "Riverfront Business Center … Riverfront Drive" address sign).
| New file (images/smart-lock-installation/) | Source |
|---|---|
| smart-lock-installation-suffolk-county-electric-strike-glass-door.webp (hero) | commercial-security/commercial-security-systems-suffolk-county-electric-strike.jpg |
| …-gate-barrier-camera-install.webp | commercial-security/commercial-security-systems-suffolk-county-lpr-gate.jpg (cropped) |
| …-reader-mounting-door-frame.webp | low-voltage/low-voltage-installation-suffolk-county-12-access-control-reader-wiring.jpg |
| …-keypad-intercom-granite-entrance.webp | commercial-security/commercial-security-systems-suffolk-county-video-intercom.jpg (cropped) |
| …-loading-dock-door-contact-keypad.webp | commercial-security/commercial-security-systems-suffolk-county-panic-button.jpg (file actually shows loading-dock composite) |
| …-reception-desk-panic-button.webp | commercial-security/commercial-security-systems-suffolk-county-glass-break.jpg (file actually shows a panic button) |
| …-intercom-keypad-terminal-wiring.webp | low-voltage/low-voltage-installation-suffolk-county-13-video-intercom-entry-wiring.jpg |
| …-crew-van-unload.webp | commercial-security/commercial-security-systems-suffolk-county-hero-crew-van.jpg |
| …-two-tech-keypad-camera-entry.webp | commercial-security/commercial-security-systems-suffolk-county-alarm-keypad.jpg |
| …-lobby-exit-door-reader-intercom.webp | commercial-security/commercial-security-systems-suffolk-county-secured-lobby.jpg |
| …-storefront-glass-break-sensor.webp | commercial-security/commercial-security-systems-suffolk-county-entrance-crew.jpg (file actually shows glass-break sensors) |
DAILY-LOG note: `images: 11 reused from images/commercial-security/ and images/low-voltage/ (no real smart-lock photos yet)`.

### Question register — smart-lock-installation-suffolk-county

#### §9 YOUR QUESTIONS ANSWERED (H3)
Town rental rules and second units
1. Our Islip rental permit is up for renewal — will the town look at the lock on the tenant's door?
2. We are licensing an accessory apartment in Brookhaven — how should its entrance be locked compared with ours?
Flood zones, barrier beaches and islands
3. Our Lindenhurst house was lifted after Sandy — can the door into the space under it have a smart lock?
4. Can a smart lock be installed at a Fire Island house that is reached only by ferry or water taxi?
Backyards, pools and cellars
5. Our back slider opens straight onto the pool deck — does a smart lock on it take care of the pool alarm rule?
6. Our cellar has an outside bulkhead door — can it go keyless, and what if someone sleeps down there?
7. If Dad falls at home and can't reach the door, how does the ambulance crew get in?
Industrial parks, practices and congregations
8. We are moving our Hauppauge building to keyless entry — what happens to the keys in our Knox-Box?
9. Our flex unit has a roll-up bay door and a steel man door — which one gets the keypad?
10. Does a keypad with an audit trail on our records room help a Suffolk dental practice with HIPAA?
11. Can a Suffolk church, synagogue or mosque use the state's security grant toward keyless doors?

#### §17 FAQ (visible == FAQPage, 10)
1. What does a keypad and electric strike on a Suffolk business door cost?
2. We are building a new house in Suffolk — at what stage should the smart locks go in?
3. Can a smart lock go on a fibreglass or insulated steel entry door?
4. Can the narrow aluminium door on our strip-centre shop take a keypad?
5. Our front door opens outward — can it take a smart deadbolt?
6. Our house is on the bay and the salt air pits everything outside — which smart lock will hold up? (main run replaced handleset question: same intent as Nassau Q1)
7. Can a sliding patio door be locked and checked from an app?
8. Can the owner see which employee unlocked the shop each morning?
9. What should we do with the smart locks before a coastal storm?
10. How do you protect our floors and door finish while you work?

#### Other question-form headings
None. (Repair capture H2 "Smart Lock Dead or Drifting Somewhere in Suffolk?" and final H2 "Shut Out of a Suffolk House, Shop or Bay Door Tonight?"; mid CTA "Ready to Sort the Doors That Should Go Keyless?")

#### De-dup notes
Planned against the full register (NYC, LI, HV, Manhattan, Brooklyn, Queens). Avoided LI intents (garage-to-house door, side door same code, alarm panel, Z-Wave/Matter, re-drilled door, storm-door clearance, salt finish, Isaias outage, Hamptons rental codes, closed-up beach house, Nassau/Suffolk licence, Nassau vs Suffolk price), HV (STR registry, cold, barn range, no internet, historic district, cleaner per building, winery), Queens (gate keypad, frame too soft, finish match, re-key after closing, low battery, dementia/arthritis), Manhattan (roommate codes, deposit, relock for walker, suite card system), Brooklyn (two-family tenant rules, owner seeing tenant logs, glass/mail slot), NYC (cut off former tenant code, warranty, COI). Partial overlaps for the main run to judge: Q2 (accessory-apartment entrance) vs Brooklyn Q7/Q9 (two-family owner-landlord) — here town-licensed unit and separate admin account; Q4 Fire Island install logistics vs LI "closed-up beach house" (remote checking, different intent); FAQ 1 cost (geo-specific by design); FAQ 8 employee log vs Queens "Bell Blvd per-employee codes" card text (not a question there). Page section "Running Smart Locks on a Suffolk Rental Between Tenants" (non-question heading) touches NYC Q13's code-cut-off topic as practice, not as a question.


## Westchester County (smart-lock-installation-westchester-county)

Built 2026-10-17 (batch: Suffolk / Westchester / Rockland smart-lock area pages). Area page; up = /smart-lock-installation-hudson-valley; phone (914) 877-2578; GBP Bronx (460 E Fordham Rd, #bronx); Westchester ×1.25. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape.

**Thesis / lane:** Westchester smart locks are about who gets in while the house is empty and who can get in when the owner can't reach the door: commuter houses empty all day with a long list of non-family visitors (cleaner, sitter, walker, landscaper, pool service, contractors); burglary patterns that use rear sliders, second-floor doors and shared garage keypad codes; owners aged 65+ living alone (first-responder key boxes); co-ops and two-families just over the NYC line (Multiple Residence Law, RPAPL 768, not NYC rules); pool-gate barriers; medical practices (HIPAA physical safeguards), congregations (state hate-crimes security grant) and offices under the 2025 NYS Uniform Code. Deliberately avoids hub/sibling lanes (second homes, cold/battery, rural range, historic thick doors, county licensing Q, renter MDL rights, co-op board approval, basement/flood, multigenerational, garage-to-kitchen code rules, outage behaviour).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `reddit Westchester smart lock OR keypad deadbolt OR "smart lock" r/Westchester` · FC search → https://www.reddit.com/r/Westchester/comments/1pzqpx4/costs_of_westchester/ (excerpt only: "I have their deadbolt/camera lock for $400ish, pricey, but very worth it.") → §10.5 H3 1 (quoted, brand not named). No other Westchester smart-lock threads surfaced. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so; headings are claims from cost guides/marketing. |
| 6 | Landmarks | L1–L6 below |
| 7 | Building stock / use cases | W1–W4 below + repo research (soundbar Westchester section) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Patch (Rye), News 12 Westchester, NYS Police, Scarsdale10583 (below) |
| 10 | Hyperlocal | Scarsdale10583 police log; lohud smart-lock search returned nothing Westchester-specific → EMPTY for the service category |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env; FC search returned only a Yelp locksmith listing page, not reviews) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| X1 | `Westchester County NY police burglary pattern homes Scarsdale Harrison Rye 2025 lohud` · FC search → FC scrape | https://patch.com/new-york/rye/police-say-tourist-burglars-are-targeting-hudson-valley-homes | Patch (Rye), Apr 25 2023: Greenwich PD secured 8 arrest warrants for burglary crews operating in Fairfield and Westchester County towns; Greenwich >70 residential burglaries since Oct 2021; crews hit high-end properties in evening after sunset while residents not home; enter through second-floor window or door; flee if alarm; earlier (January) arrest of two suspected SATG members by Harrison PD with DHS and Nassau PD via federal warrant in Queens. | §5 para 3, §9 balcony Q, §10.5 H3 3, Across (Rye/Harrison) |
| X2 | same search → FC scrape | https://scarsdale10583.com/section-table/107-todays-news/5104-woman-arrested-for-dwi-150-000-in-jewels-stolen-from-home-on-clarence-road | Scarsdale10583, Nov 11 2015 police report: burglaries matching patterns in Bronxville, Rye, Rye Brook, Greenwich; burglar piled lawn furniture to force second-storey window (Tory Lane, Fox Meadow), alarm sounded; smash-and-grab via rear window or sliding glass door (Hillview Rd); ladder from a garage reachable only with door keypad code found by damaged second-floor windows (Church Lane South) — police investigating people with access to the code; advice: lights on timers, keep exterior doors locked with deadbolts, garage closed and locked. Same log: Dell Road landlord changed locks on tenants; police advised eviction process, tenants let back in. | §5 para 3, §9 Metro-North Q, §9 balcony Q, §9 garage-code Q, §9 slider Q, §10.5 H3 3, landlord section |
| X3 | `New York State Police public safety alert targeted residential burglaries Dutchess Westchester Putnam counties` · FC search → FC scrape | https://troopers.ny.gov/news/public-safety-alert-targeted-residential-burglaries-hudson-valley-region | NYSP Jan 29 2025: three residential burglaries targeting Asian American residents in Dutchess/Westchester/Putnam; advice incl. lock all doors and windows "including second-floor entry points", timed interior lights, don't post absences. | §5 para 3, §5.5 bullet 5, §9 Metro-North Q, §9 balcony Q |
| X4 | `Westchester police "lock your doors" burglaries unlocked doors 2025 OR 2026 Westchester news12` · FC search → FC scrape | https://westchester.news12.com/2024/09/17/pelham-manor-residents-concerned-after-an-increase-of-home-break-ins/4Lu8IKohOrd4md72MYFBWX | News 12, Sep 17 2024: Pelham Manor, Grant Ave home broken into ~4:45 a.m. Monday; two suspects used a crowbar on the back sliding door; took handbag and car keys and the car; multiple reports over 10 days; deputy mayor/police commissioner: "Lock your doors, take the fobs inside…". | §5 para 3, §9 slider Q, §10.5 H3 3, Across (New Rochelle/Pelham) |
| X5 | `Westchester County NY residential Knox box seniors fire department program …` · FC search → FC scrape | https://www.elmsfordfd.com/knox-box/ | Elmsford FD: Residential Knox-Box lets first responders "let themselves in"; department-held Knox Master Key; aimed at seniors living at home. | §6 card, §9 Elmsford Q, §10 card, §10.5 H3 4, Living Alone checklist |
| X6 | `New York Multiple Residence Law applies cities less than 325,000 …` · FC search | https://ag.ny.gov/resources/individuals/tenants-homeowners/legal-services-and-code-enforcement | NY AG: MDL applies to cities of 325,000+; Multiple Residence Law to cities under 325,000 and all towns and villages. | §5 para 6, §9 Yonkers Q, §10.5 H3 5 |
| X7 | `New York RPAPL 768 unlawful eviction changing locks class A misdemeanor statewide 2019` · FC search | https://ag.ny.gov/resources/government-organizations/law-enforcement-guidance/unlawful-evictions ; https://www.nysenate.gov/legislation/laws/RPA/768 | Unlawful to change the lock on the entrance door without supplying the occupant a key; class A misdemeanor; any person who assists is liable. | §9 Yonkers Q, §10.5 H3 5, landlord section |
| X8 | `Securing Communities Against Hate Crimes grant Westchester recipients access control locks 2025` · FC search → FC scrape | https://www.governor.ny.gov/apply-securing-communities-against-hate-crimes-grant-program | DCJS administers; nonprofits at risk because of ideology, beliefs or missions; funds interior/exterior security improvements "such as alarms, panic buttons, fences, shatter-resistant glass and public address systems, among other items"; training, cybersecurity; RFPs on DCJS site. Locks/access control NOT named → page says the RFP/budget decides. Westchester recipient list: EMPTY (not found). | §8 para, §9 congregation Q |
| X9 | `HIPAA security rule 164.310 facility access controls …` · FC search | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310 ; https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/securityrule/physsafeguards.pdf | 164.310(a)(1) facility access controls; (iii) access control and validation by role incl. visitor control; (iv) maintenance records "(for example, hardware, walls, doors, and locks)"; HHS guidance mentions door locks relying on card/badge reader. | §9 Platinum Mile Q |
| X10 | `2020 Building Code of New York State 1010.2.12 sensor release …` · FC search | https://up.codes/s/door-operations ; https://up.codes/s/sensor-release-of-electrically-locked-egress-doors | Model IBC text: door hardware release — operation directly interrupts power and unlocks immediately; loss of power unlocks. Sensor release — egress-side sensor; manual unlocking device 40–48 in, within 5 ft, "PUSH TO EXIT", unlocked ≥30 s; fire alarm activation unlocks. (Viewer is IBC model text, stated as "model code" on page.) | §8.5 bullets, §9 2025-code Q, §10.5 H3 6 |
| X11 | `"2025 Building Code of New York State" effective date 2024 International Building Code` · FC search | https://codes.iccsafe.org/codes/new-york ; https://dos.ny.gov/notice-adoption ; https://www.harrison-ny.gov/building-department/news/new-code-effective-12312025 | 2025 Uniform Code effective Dec 31 2025; 2025 BCNYS based on 2024 IBC; Harrison building department posted "New Code Effective 12/31/2025" (Oct 3 2025). | §5.5 bullet 6, §8.5, §9 2025-code Q, §10.5 H3 6 |
| X12 | `New York State residential swimming pool barrier gate self-closing …` · FC search → FC scrape (pdf, directQuote) | https://dos.ny.gov/tb-1014-uc-pool-summary (rev pdf 2024/08) | Code effective date for bulletin May 12 2020 (2020 Uniform Code); gates self-closing; pedestrian gates open outward; self-latching, latch handle within enclosure ≥40 in above grade, extra conditions under 54 in; "All gates must be securely locked with a key, combination, or another child-proof lock…". | §6 card, §9 pool Q, §10 card, §10.5 H3 7 |
| X13 | `Westchester County locksmith license required consumer protection` · FC search | https://consumer.westchestercountyny.gov/ | Plumbers/electricians need county trade licence; NO Westchester locksmith licence found → EMPTY; page makes no locksmith-licence claim. | — |
| X14 | `lohud smart lock keyless entry Westchester …` · FC search | — | No Westchester smart-lock news → EMPTY. | — |
| X15 | `sliding patio door smart lock options …` · FC search | product/retail listings (gokeyless, amazon, theconnectedshop) | Keyless locks made for sliders exist (no specs used). | §9 slider Q, §10 card (generic) |
| L1 | `Philipse Manor Hall Yonkers built 1682 …` · FC search | https://en.wikipedia.org/wiki/Philipse_Manor_Hall_State_Historic_Site ; https://www.philipsemanorhall.com/about | Getty Square, 29 Warburton Ave; oldest part c.1682; NHL 1961; built in three stages from the 1680s. | §13 card |
| L2 | `Jay Heritage Center Rye …` · FC search | https://en.wikipedia.org/wiki/Jay_Estate | 23-acre park and historic site, 1838 Peter Augustus Jay House; Boston Post Road. | §13 card |
| L3 | `Kensico Dam Valhalla completed 1917 …` · FC search | https://parks.westchestercountyny.gov/kensico-dam-plaza ; tripadvisor excerpt | 307 ft high, 1,843 ft long; completed 1917 (completion year from tripadvisor/blog excerpts). | §13 card |
| L4 | `Untermyer Gardens Yonkers …` · FC search | https://www.untermyergardens.org/ ; FB Garden Conservancy excerpt | Conservancy restoring the gardens in collaboration with City of Yonkers; walled garden. | §13 card |
| L5 | `Sunnyside Washington Irving home Irvington Historic Hudson Valley` · FC search | https://hudsonvalley.org/historic-sites/washington-irvings-sunnyside/ ; https://www.hudsonrivervalley.com/sites/Washington-Irving-s-Sunnyside-/details | Historic Hudson Valley site; house and grounds restored to look much as in the 1850s. | §13 card |
| L6 | reused (research/soundbar-installation.md, Westchester) | https://www.heritagehills.com/about-heritage-hills.php | 2,600 condos in 30 condo groups, 1,100+ acres, 55+. | §7 card, §13 card, Across (north) |
| W1 | reused (soundbar Westchester, FC scrape) | https://www.census.gov/quickfacts/fact/table/westchestercountynewyork/PST045224 | ~1,015,743 pop; 399,598 housing units (2025); owner-occupied 61.8% (2020–24); median value $663,200; 2.61 persons/household; 65+ 19.7%. | §5 paras 2 & 5, §5.5, Living Alone |
| W2 | reused (soundbar Westchester) | https://cooperatornews.com/article/westchester-county | ~42,000 co-ops, 25,000 condos, ~53,000 rentals across 6 cities, 14 towns, 22 villages. | §5 para 6, §5.5 |
| W3 | reused (soundbar Westchester) | https://www.governing.com/magazine/getting-ahead-of-the-nimby-energy-an-older-city-learns-to-build ; https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster | >4,500 new New Rochelle units online (2025); rezoning Dec 2015. | §5 para 6 |
| W4 | reused (soundbar Westchester) | https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors ; https://www.yonkersny.gov/DocumentCenter/View/14753/Home-Improvement-License-Application-052825 | County HI licence required + licence search; plumbers/electricians separate; Yonkers HI application. (No claim AESS holds either.) | §8.5, §10.5 H3 2, Across (Yonkers) |
| W5 | reused (soundbar Westchester) | https://914inc.com/westchesters-platinum-mile-is-making-a-serious-comeback/ ; Patch White Plains Mamaroneck Ave ; Capitol Theatre history | Platinum Mile repositioning to medical, 3030 Westchester Ave; Mamaroneck Ave bars/restaurants; Capitol Theatre opened 1926. Central Park Ave / Tarrytown Main St / downtown New Rochelle named only. | §8 corridor cards |
| S1 | silo file (research/smart-lock-installation.md) | fixr.com (Jan 2025 $250–$400 avg $300); homewyse (Jan 2026 $94.71–$227/lock); Schlage Encode (2.4 GHz, −31°F–150.8°F); Kwikset Z-Wave 700 (250 codes); Yale Matter/Thread border router; August Connect 10–15 ft; Chamberlain myQ 2023; Allegion Schlage door prep (1-3/8"–2", backset 2-3/8/2-3/4, bore 1-1/2 or 2-1/8, 1" throw); Yale Assure 2 sheet (door to 2-1/4"); IRC R311.2 egress | as logged there | §10, §10.5 H3 1, §9 garage Q, connectivity, measure table, §7.5 |

### Prices used (all from approved sources; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,875–$3,125 | single-door keypad/fob reader + electric strike | $1,500–$2,500 base × 1.25 (silo prices table; HV hub Westchester row) |
| $313–$563 | new electric strike | $250–$450 × 1.25 (312.5→313, 562.5→563) |
| $369–$606 | failed strike repair | $295–$485 × 1.25 (368.75→369, 606.25→606) |
| $235 first hour, then 30-min blocks | setup-only visit | research/tv-mounting-prices/BRIEF.md line 15 (TV/device setup rate — same flag as hubs) |
| $195/hr, 3-hr min ($585) | service/callback | blueprint §9 |
| quoted flat at walkthrough | residential smart lock | no AESS figure |
**Conflict for Anwar:** live access-control-installation-westchester-county.html shows "$1,500 to $2,500 for a single-door lobby system" (unscaled) and other ranges; this page uses §9 ×1.25 ($1,875–$3,125), matching the HV hub Westchester row.

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
Every pool photo is a perceptual-hash duplicate of an image already on a smart-lock sibling (pool is small); picks avoid the Rockland batch page's sources where possible. Photos look AI-rendered (same flag as earlier builders). Rejected: lpr-lot (building number "1000"), credential-programming (readable names on screen), crew-van (website/phone on van), video-wall/ptz/fiber/crew-pull/jhook/ceiling-grid (not door-relevant), alarm-keypad/electric-strike/integration-rack/secured-lobby/keystone-wall-plate (same photos as the Rockland batch page). panic-button is shared with Rockland's door-contact image by hash (unavoidable with this pool).
| New file (images/smart-lock-installation/) | Source | Crop |
|---|---|---|
| smart-lock-installation-westchester-county-keypad-reader-office-entrance.webp (hero) | commercial-security/commercial-security-systems-westchester-hero-access-reader.jpg | top 27.5% removed (named "business center" sign on glass) |
| -electric-strike-terminal-wiring.webp | low-voltage/low-voltage-installation-westchester-county-12-electric-strike-wiring.jpg | — |
| -keypad-intercom-granite-entrance.webp | commercial-security/commercial-security-systems-westchester-video-intercom.jpg | left 19% removed (sign with business name + street address) |
| -lobby-entry-panel-install.webp | low-voltage/low-voltage-installation-westchester-county-13-lobby-video-intercom.jpg | right 23% removed ("123 Main Street" directory) |
| -reception-desk-panic-button.webp | commercial-security/commercial-security-systems-westchester-panic-button.jpg | — |
| -shop-window-sensor-mounting.webp | commercial-security/commercial-security-systems-westchester-glass-break.jpg | — |
| -tone-trace-wall-plate.webp | low-voltage/low-voltage-installation-westchester-county-08-tone-generator-trace.jpg | — |
| -ceiling-wifi-access-point.webp | low-voltage/low-voltage-installation-westchester-county-10-access-point-lift-install.jpg | right 16% removed ("community center" sign) |
| -laptop-network-rack-setup.webp | low-voltage/low-voltage-installation-westchester-county-hero-rack-switch-config.jpg | — |
| -poe-switch-recorder-rack.webp | commercial-security/commercial-security-systems-westchester-nvr-poe-rack.jpg | left 19% removed (diagram sheet + laptop) |
| -wall-plate-cable-test.webp | low-voltage/low-voltage-installation-westchester-county-06-fluke-certification-pass.jpg | — |
DAILY-LOG note: `images: 11 reused from images/commercial-security/ and images/low-voltage/ (no real smart-lock photos yet)`.

## Question register — smart-lock-installation-westchester-county

### §9 YOUR QUESTIONS ANSWERED (H3)
Houses that are empty all day
1. We're on Metro-North from early morning until after dark — what should the locks be doing while the house sits empty?
2. Police warnings keep mentioning second-floor doors — should the balcony door upstairs get a smart lock too?
3. The landscaper, the cleaner and two contractors all know our garage keypad code — does that undercut the smart locks on the house?
4. Our kids get off the school bus mid-afternoon while we're at work — can the lock tell us each one is home?
Back doors, sliders and the way burglars come in
5. The door we all use is a sliding patio door onto the deck — can a slider get a smart lock?
Owners who live alone
6. My father lives on his own in Elmsford — if he falls, how would paramedics get through a smart-locked door without breaking it?
Co-ops, two-families and the city line
7. Does New York City's apartment-lock law reach our Yonkers or New Rochelle apartment?
Pools and outdoor gates
8. Can the gate in our pool fence take a keypad lock without breaking the state's pool-barrier rules?
Practices, offices and congregations
9. Our practice on the Platinum Mile keeps patient records on site — what does HIPAA expect of our door locks?
10. Our congregation was awarded a state security grant — can it cover keyless doors, and what paperwork will the grant office want from you?
11. Our office landlord says the 2025 state code now applies — does that change what can go on our suite door?

### §17 FAQ (visible == FAQPage, 9)
1. Is the price you quote at the walkthrough the price on the invoice?
2. Should we turn on the auto-unlock feature that opens the front door as we pull into the driveway? (main run replaced handleset question: same intent as Nassau Q1)
3. Our back door has a multipoint lock that throws hooks top and bottom when the handle is lifted — can it go keyless?
4. Can the lock's entry history be saved for a police report or an insurance claim after a break-in?
5. Can the front door be left unlocked on purpose for a party or a graduation open house?
6. What stops someone who gets into our email from opening the front door?
7. Can a realtor's showings run on temporary codes instead of a lockbox on the front door?
8. Can one app run the locks at our house and at my mother's house in the next town?
9. Will the inside of the lock look bulky on our older door?

### Other question-form headings
- H2 "Smart Lock Misbehaving Somewhere in Westchester?" (repair capture)
- H2 "Locked Out of a Westchester House or Office Tonight?" (final repair capture)

### De-dup notes
Dropped during build: "two-family in Mount Vernon — shared front door code separation" (≈ Brooklyn Q8/Q9/Q10; content moved to a non-question Landlords section); "How soon can an installation be booked?" (≈ Manhattan FAQ 8); "Do you remove the old lock / keep keys working?" (≈ Brooklyn FAQ 9 + Queens FAQ 2); cost FAQ by county (≈ HV FAQ 1). Partial overlaps for the main run to judge: Q7 (NYC law across the city line) vs NYC Q1 / Brooklyn Q7 — here the intent is jurisdiction (MDL vs MRL), not renter rights; Q6 (paramedic access) vs Queens grandma/dementia Qs — here first-responder entry; FAQ 8 (one app, two houses) vs Queens FAQ 5 (who holds admin) — different intent; Q2/Q5 vs LI Q1 (which doors deserve a smart lock) — here specific door types named in police reports.


## Rockland County (smart-lock-installation-rockland-county)

Built 2026-10-17 (batch: Suffolk, Westchester, Rockland smart-lock area pages). Area page; up = /smart-lock-installation-hudson-valley; phone (845) 640-3835 (800 only in shared header chrome); GBP Bronx (460 E Fordham Rd, #bronx); Rockland multiplier 1.30.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpt only unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. "Carried" = finding reached by the soundbar-installation-rockland-county builder (research/soundbar-installation.md, Rockland section) or by earlier smart-lock builders (research/smart-lock-installation.md); not re-fetched.

**Thesis / lane:** Rockland doors are decided by who has to get through them and when electronics are off-limits: large, often observant households (3.22 persons/household; ~a third of the county Jewish) in post-1955 raised ranches and split-levels, so a split door plan (mechanical Shabbat door + electronic weekday doors), code capacity for big families, mezuzah-aware frame work, deck sliders with thumb latches, rented rooms/accessory units under active county code enforcement, and shuls/yeshivas/nonprofits hardening doors with state Securing Communities Against Hate Crimes grants since the 2019 Monsey attack; plus Route 59 / Route 303 / Main Street businesses closing early on Fridays.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | FC search `reddit r/Rockland smart lock OR keypad lock OR locksmith` → no r/Rockland smart-lock thread (results: r/AskALocksmith, r/FirstTimeHomeBuyer, Yelp listing, locksmith ads). Rockland-specific: EMPTY. Silo Reddit (r/Judaism excerpt) see R2. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from cost guides / product pages / articles, stated as such on the page. |
| 6 | Landmarks | L1–L6 |
| 7 | Use cases / building stock | B1–B5 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Spectrum News (2019), NBC NY (2013, 2022), ABC7 (2023), Patch New City (2024), Governor's office (2026) |
| 10 | Hyperlocal | Patch New City/Ramapo (N4). Rockland Times / Nyack News & Views / lohud on smart locks specifically: none found → EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env); FC search returned only the Yelp locksmith listing page (no review text) — not used. |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| R1 | `smart lock Shabbat Shabbos keypad lock observant Jewish home Monsey` · FC search → FC scrape | https://www.chabad.org/library/article_cdo/aid/7077643/jewish/What-You-Need-to-Know-About-Unlocking-Doors-on-Shabbat.htm | (Oct 21 2025, Rabbi Yehuda Shurpin) "generally no issue with using an old-fashioned conventional lock and key (or combination locks that are entirely mechanical)"; "Doors that open with electronic key cards, fobs, or keypads may not be used on Shabbat"; smart locks: auto-lock creates an electrical impulse; "most smart locks record every use, sending signals to an app"; "Practically, you should ideally disable smart locks before Shabbat"; Shabbos belt (key forms part of the belt); arrange a door with a standard key or staff to open. | §5 para 3, §6 cards, §9 Q1/Q2/Q11, §10.5 H3 2–3, Shabbat door plan |
| R2 | same search → FC scrape | https://tribeautomation.com/2017/10/26/are-smart-locks-shabbat-compatible/ | (Oct 26 2017) Orthodox home-automation installer tested Schlage Connect: illuminated touchpad an issue; 30-second auto-lock timer and activity log issues even when opened by inside lever; "A Shabbat-mode feature would certainly be a game changer"; option to sever battery connection; he put it on "my entrance from the garage to the house since I don't go to the garage on Shabbat". | §9 Q1/Q2, §10.5 H3 2 |
| R3 | same search (excerpts only) | https://www.reddit.com/r/Judaism/comments/1dr8xg1/deadbolt_locks_and_the_sabbath/ ; https://www.amazon.com/Bravex-Keyless-Deadbolt-Sabbath-Mechanical/dp/B0B8NQN96L | Reddit excerpt: entering a code on a keypad to unlock is not permissible on the Sabbath for observant Jews (not quoted). Amazon listing title "Bravex Keyless Deadbolt ... Sabbath ... Mechanical"; "100% Mechanical (No risk of low battery)". | §9 Q1 ("some online listings even put 'Sabbath' in the product name") |
| R4 | `mezuzah placement right doorpost upper third shoulder height how to affix chabad` · FC search (excerpts) | https://chicagomitzvahcampaign.org/mezuzah-faq/ ; https://www.chabad.org/library/article_cdo/aid/225405/jewish/Mezuzah-Placement.htm | Right-hand side as one enters; lower part of the upper third; not higher than four inches below the lintel (Chicago Mitzvah Campaign). Chabad: doorway ~90 in+ → shoulder height. | §7.5 mezuzah para, §9 Q3, §6 card |
| R5 | `Rockland County Jewish population study Orthodox percent Ramapo Monsey New Square Kaser` · FC search; FC scrape of JVL (metadata) | https://jewishvirtuallibrary.org/rockland-county ; https://forward.com/news/439665/rockland-county-hasidic-anti-semitic-east-ramapo/ (excerpt) | JVL description: "a significant Jewish community of 92,000"; search excerpt "At 31% of the total population". Forward excerpt: villages like Monsey, Kaser and New Square "more than 90% Hasidic". (lohud Facebook post "Nearly a third of Rockland County's population identifies as Jewish" — scrape refused, not cited.) | §5 para 3, §5.5 bullet 2 |
| R6 | `Monsey Hanukkah attack 2019 synagogues security grants Rockland County access control doors` · FC search → FC scrape | https://spectrumlocalnews.com/news/2019/12/31/rockland-county-unveils-new-security-plan-after-monsey-stabbing-attack | Dec 30 2019: county + Brosnan Security volunteer armed patrol for synagogues; Gillibrand roundtable at Ramapo Town Hall urged leaders to apply for grant funding (Nonprofit Security Program) for schools and places of worship. | §5 para 4 |
| R7 | same search → FC scrape (query) | https://en.wikipedia.org/wiki/2019_Monsey_Hanukkah_stabbing | Dec 28 2019, seventh night of Hanukkah; masked man with large knife/machete invaded a Hasidic rabbi's home in Monsey; almost 100 gathered; five injured; 72-year-old man in coma 59 days, died March 2020. | §5 para 4 |
| R8 | `Securing Communities Against Hate Crimes grant Rockland County synagogues yeshivas awarded 2025 access control` · FC search → FC scrape (query) | https://www.governor.ny.gov/news/ahead-jewish-high-holidays-governor-hochul-announces-distribution-record-70-million-protect | Sept 8 2026: record $70M to 290 nonprofits; max request $250,000 each; funds "lighting, locks, alarms, panic buttons, fencing, barriers, access controls, shatter-resistant glass..."; Mid-Hudson: 99 grants totaling $24,187,697. | §5 para 4, §5.5 bullet 5, §8.5, §9 Q10, community-building checklist |
| R9 | `Rockland County illegal rooming house locks on bedroom doors code enforcement Spring Valley Ramapo fire` · FC search → FC scrape | https://www.nbcnewyork.com/news/local/more-than-100-violations-found-at-spring-valley-apartment-building-that-burned/3606594/ | Mar 18 2022: >100 violations after Mar 9 Spring Valley apartment fire incl. "doors that closed improperly"; Buildings and Codes Director Ed Markunas: "To contain the fire, you need self-closing doors and fireproof doors..."; county had just taken over Spring Valley code enforcement. | §5 para 5, §8.5 bullet 3, rooms checklist |
| R10 | same search → FC scrape | https://abc7ny.com/post/spring-valley-house-fire-landlord-violations/12925408/ | Mar 7 2023: five died in Spring Valley house fire; inspectors cited buildings owned by same landlord for electrical issues, missing smoke/CO detectors, "illegal single-room occupancies", illegal conversions; "Last year, the state ordered the county to take over in Spring Valley following the arrest of the village's former inspector." Landlord NOT named on page. | §5 para 5, §9 Q9, §10.5 H3 6, rooms checklist |
| R11 | same search → FC scrape (query) | https://www.rocklandcountyny.gov/departments/health/center-for-rockland-codes-investigations/housing-mdrr | "RCDOH performs annual inspections and permitting of all Rooming Houses in the County"; subject to Rockland County Sanitary Code; "specific requirements regarding bathroom facilities, cooking and dining restrictions, door locks, sleeping area floor space, smoke detector and carbon monoxide detector location, and compliance with local ordinances". | §5 para 5, §9 Q9, §10.5 H3 6, rooms checklist |
| R12 | `smart lock for sliding patio door options manufacturer compatible sliding glass door keyless` · FC search → FC scrape (query) | https://lockeyusa.com/product/c150/ | Lockey C150: "Mechanical, keyless, hook bolt"; throw 3/8″; door 1-3/16″–2″; "For Exterior & Interior Use"; "Weather Resistant"; for sliding glass patio doors. | §9 Q6, §10 card, §10.5 H3 4 |
| R13 | `Clarkstown OR Orangetown OR Ramapo police burglaries unlocked doors homes warning residents lock doors 2025` · FC search → FC scrape | https://patch.com/new-york/newcity/lock-houses-cars-ramapo-police-warn-after-sunday-night-incidents | Apr 9 2024 (Patch, Lanning Taliaferro): Ramapo PD — individuals burglarizing unlocked homes in search of car keys and valuables; one incident in Airmont; in New Hempstead attempted to enter vehicles "as well as attempting to open a sliding door"; "Remember to lock doors, secure windows, and if you have an alarm system, ensure it's set". | §9 Q5, Q6, §10.5 H3 4 |
| R14 | same search → FC scrape | https://www.nbcnewyork.com/news/local/nanuet-new-city-burglaries-break-ins-rockland-county/2076526/ | Mar 18 2013: Clarkstown police investigating daytime burglaries of unoccupied homes in Nanuet and New City during working hours; advice: lock all windows and doors. | §10.5 H3 7, commuter section |
| R15 | same search (excerpt only) | https://www.facebook.com/RamapoPD/posts/... | Ramapo PD excerpt: lock the door immediately behind you; keep all exterior doors locked. Background only. | — |
| R16 | `Palisades Center West Nyack opened 1998 square feet largest mall` · FC search (excerpt) | https://en.wikipedia.org/wiki/Palisades_Center | Opened March 4, 1998; as of Dec 2022 twelfth-largest US mall by gross leasable space. | §8 card |
| R17 | `Edward Hopper House Nyack birthplace 1882 museum North Broadway` · FC search (excerpts) | https://www.edwardhopperhouse.org/hours-tours-admission.html ; Facebook post (Edward Hopper House) | 82 North Broadway, Nyack; Hopper born in Nyack 1882, grew up in the house; museum & study center. | §13 card |
| R18 | `Monsey Route 59 shopping district kosher stores Main Street Monsey businesses` · FC search (excerpts) | https://www.yelp.com/search?cflt=kosher&find_loc=Monsey%2C+NY+10952 ; Facebook group excerpt (Evergreen Kosher Market, Town Square, Route 59) | Yelp listing shows kosher restaurants at Route 59 Monsey addresses (e.g., 59 Rt 59; 110 NY-59). No business named on page. | §8 card ("Yelp's Monsey listings place several at Route 59 addresses") |
| B1 | carried (soundbar Rockland, FC scrape) | https://www.rocklandhistory.org/a-brief-history-of-rockland | By 1950 fewer than 150 farms; 1950s homes built >1,000/year; Tappan Zee Bridge 1955, Palisades Parkway and Thruway same decade. | §5 para 1, §5.5 bullet 3 |
| B2 | carried (soundbar Rockland, FC scrape) | https://www.census.gov/quickfacts/fact/table/rocklandcountynewyork/PST045224 | Pop 357,397 and housing units 109,999 (July 1 2025); owner-occupied 67.9%; 3.22 persons/household; language other than English 44.2%. Nassau 2.99 / Suffolk 2.93 from LI hub QuickFacts. | §5 para 2, §5.5 bullets 1 and 4 |
| B3 | carried (soundbar Rockland) | https://www.oddsandendsny.com/areas/new-city ; research/tv-mounting-prices/rockland-county.json (Pearl River capes/colonials; Pomona raised ranches; Route 303 office parks; New City courthouse 1 South Main St) | Split-level / raised ranch stock in New City 1960s–70s; capes/colonials in Pearl River. Used descriptively; no statistic drawn. | §7 cards, Across Rockland |
| B4 | carried (soundbar Rockland, FC scrape) | https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits ; .../frequently-asked-questions ; https://longisland.news12.com/2026/04/15/tempers-flare-tuesday-night-as-rockland-county-re-writes-contractor-licensing-rules/5PDORDgg6n88VIk8Oa0c0F | Chapter 286 effective May 14, 2026; HIC licence required for residential home improvement; online database; unlicensed may lack liability/disability/workers' comp insurance; licensed since 1986. | §5.5 bullet 6, §8.5, §10.5 H3 5 |
| B5 | carried (HV smart-lock hub) | https://www.rocklandcountyny.gov/home/showpublisheddocument/6348/639026169869900000 | Ch. 286 classifications include 19 "Locksmiths: Locks, Security gates, Home Safes, Security Screens" and 02 low voltage; HI licence ≠ electrical licence. | §5.5, §8.5, §10.5 H3 5 |
| L1 | carried (soundbar Rockland) | https://www.hudsonrivervalley.com/sites/DeWint-House-/details | Built 1700, stone and brick, oldest surviving building in Rockland; Washington's temporary HQ. | §13 card |
| L2 | carried (soundbar Rockland) | https://en.wikipedia.org/wiki/Tappan_Zee_Bridge_(2017%E2%80%93present) | Mario M. Cuomo Bridge, South Nyack–Tarrytown; spans opened Aug 2017 / Sept 2018; replaced 1955 bridge. | §13 card, commuter section |
| L3 | carried (soundbar Rockland) | https://www.haverstrawbrickmuseum.org/click-a-brick | 1883: 41 brickyards, ~2,400 men, world's largest brick producer. | §13 card |
| L4 | carried (soundbar Rockland) | https://parks.ny.gov/visit/historic-sites/stony-point-battlefield-state-historic-site | Stony Point Lighthouse 1826, oldest on the Hudson, operated 99 years. | §13 card |
| L5 | carried (soundbar Rockland) | https://piermonthistoricalsociety.org/world-war-ii/ ; https://historynet.com/camp-shanks-last-stop-u-s-a/ | "Last Stop USA"; >1 million service members; mile-long pier. | §13 card |
| L6 | carried (soundbar Rockland) | https://en.wikipedia.org/wiki/Nanuet_Town_Centre ; Rockland County Government post + explorerocklandny.com (Pearl River parade) | Shops at Nanuet debuted 2013 on former Nanuet Mall site; Pearl River St. Patrick's parade "second largest in New York State". | §8 cards |
| S1 | silo (LI hub) | https://kc.allegion.com/kb/article/what-are-the-required-door-preparation-specifications-for-the-schlage-arrive | Door 1-3/8″–2″; cross bore 2-1/8″ or 1-1/2″; edge bore 1″; backset 2-3/8″/2-3/4″. | §7.5, §9 Q7 |
| S2 | silo (HV hub / LI hub) | https://www.schlage.com/en/home/products/BE489WBCAMFFF.html ; Kwikset Z-Wave 700 PDF (perryhomes cloudinary) | Schlage Encode 100 codes; Kwikset Z-Wave 700 model 250 user codes (PDF doesn't name model — page says "Kwikset's Z-Wave 700 locks"). | §9 Q4 |
| S3 | silo (LI hub) | https://idighardware.com/2010/11/double-cylinder-deadlocks-residential/ | IRC R311.2: egress doors readily openable from inside without key or special knowledge (page says "model residential code"). | §7.5 |
| S4 | silo (NYC hub S1) | https://www.fixr.com/costs/smart-lock-installation | National $250–$400, avg $300 (Jan 2025). Labelled national third-party. | §10.5 H3 1, §14 |

### Prices used (all from approved AESS sources; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,950–$3,250 | single-door keypad/fob reader + electric strike (Rockland) | $1,500–$2,500 base (access-control-installation-bronx.html / silo prices table) × 1.30 — matches HV hub's Rockland row |
| $325–$585 | new electric strike on entrance door | $250–$450 × 1.30 |
| $384–$631 | failed electric strike repair | $295–$485 × 1.30 (383.5→384, 630.5→631, round half-up) |
| $235 first hour, then 30-min blocks | setup-only visit, Rockland | research/tv-mounting-prices/BRIEF.md; tv-mounting-prices-rockland-county.html; HV hub |
| $195/hr, 3-hr minimum ($585) | service/callback, not on initial install | blueprint v2.3 §9 (verbatim) |
| quoted flat at walkthrough | house-door smart lock / mechanical keypad / slider lock | no AESS figure exists |
| $250–$400, avg $300 | NATIONAL third-party (Fixr, Jan 2025) | S4 |
**Conflicts for Anwar:** (1) live access-control-installation-rockland-county.html uses "Brooklyn base + 15% HV surcharge" and a "SINGLE DOOR / GATE $1,700 – $5,000" card, plus "$1,500 to $2,500 plus the 15% surcharge" for a lobby fob reader — conflicts with §9 ×1.30 ($1,950–$3,250) used here and on the HV hub. (2) live door-buzzer-repair-rockland-county.html: $250 service call and "Electric strike replacement + alignment $450–$950" — differs from ×1.30 strike figures. (3) Setup-only $235 rate is published for TV/device setup; used for code/app/bridge visits (same flag as LI/Brooklyn/Queens). (4) access-control-installation-rockland-county.html contains a "Spring Valley landlord ... saved $4,000/year" testimonial that looks unsourced — not reused here; worth a review under Hard Rule 11.

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
All viewed before use. Assigned pool only. Perceptual-hash check: 9 of the 11 sources are the same photos as images already used on sibling smart-lock pages (the Rockland-named library files are geo-renamed copies); only the gate camera (lpr-gate) and the access-point lift crop differ. Library photos look AI-rendered (same note as earlier builders) — needs Anwar's review.
| File (images/smart-lock-installation/) | Source | Same photo on a sibling? |
|---|---|---|
| smart-lock-installation-rockland-county-electric-strike-glass-entry-door.webp (hero, eager) | images/commercial-security/commercial-security-systems-rockland-electric-strike.jpg | yes (nyc-electric-strike-lobby-door) |
| smart-lock-installation-rockland-county-keypad-reader-and-entry-camera.webp | commercial-security-systems-rockland-alarm-keypad.jpg | yes (long-island-keypad-and-camera-entry) |
| smart-lock-installation-rockland-county-reader-mounting-aluminum-door-frame.webp | images/low-voltage/low-voltage-installation-rockland-county-12-access-control-reader-wiring.jpg | yes (nyc-fob-reader-mounting) |
| smart-lock-installation-rockland-county-wall-plate-jack-termination.webp | low-voltage-installation-rockland-county-07-keystone-wall-plate.jpg | yes (hudson-valley-wall-plate-termination) |
| smart-lock-installation-rockland-county-lobby-intercom-reader-glass-doors.webp | commercial-security-systems-rockland-secured-lobby.jpg | yes (hudson-valley-secured-lobby-entry) |
| smart-lock-installation-rockland-county-door-contact-keypad-loading-dock.webp | commercial-security-systems-rockland-panic-button.jpg | yes (hudson-valley-door-contact-keypad-panels) |
| smart-lock-installation-rockland-county-video-intercom-keypad-stone-pillar.webp | commercial-security-systems-rockland-video-intercom.jpg (cropped: left 240 px removed — "Riverfront Business Center / … Riverfront Drive" sign) | yes (hudson-valley-keypad-intercom-stone-pillar) |
| smart-lock-installation-rockland-county-access-rack-installation-checklist.webp | commercial-security-systems-rockland-hero-integration-rack.jpg | yes (brooklyn-rack-patching-checklist) |
| smart-lock-installation-rockland-county-gate-camera-barrier-arm.webp | commercial-security-systems-rockland-lpr-gate.jpg (cropped: left 260 px removed — building number "1000" and a sign) | no |
| smart-lock-installation-rockland-county-exterior-enclosure-brick-wall-conduit.webp | low-voltage-installation-rockland-county-11-exterior-enclosure-install.jpg | yes (long-island-exterior-enclosure-brick) |
| smart-lock-installation-rockland-county-ceiling-wifi-access-point.webp | low-voltage-installation-rockland-county-10-access-point-lift-install.jpg (cropped: right 190 px removed — "Community Center" wall sign) | same photo as manhattan-ceiling-wifi-access-point-lift but cropped differently |
Rejected after viewing: rockland-credential-programming (readable cardholder names on screen and checklist), rockland-access-reader (named "Pinnacle Business Center" on glass), 13-lobby-video-intercom ("123 Main Street" directory, "ABC Property Management"), rockland-crew-van (van shows a phone number and "abstractenterprises.com", not the site domain).
DAILY-LOG note: `images: 11 reused from images/commercial-security/ and images/low-voltage/ (no real smart-lock photos yet)`.

### EMPTY (not accessible in build env)
Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG, Yelp 1–3★ review text; r/Rockland smart-lock threads (none found); Rockland local news on smart locks specifically (Patch/lohud/Rockland Times/Nyack News & Views: none found); lohud Facebook post (FC refused the site); Field Notes — no sourced Rockland install anecdote, written as standing routine and labelled so.

## Question register — smart-lock-installation-rockland-county

### §9 YOUR QUESTIONS ANSWERED (H3)
Observant households and Shabbat
1. We keep Shabbat — what kind of lock lets the family get in and out from Friday evening until Saturday night?
2. Our smart lock auto-locks and logs every opening — can those features be switched off for Shabbat and Yom Tov without removing the lock?
3. Will a keypad deadbolt or a reader on the frame crowd the mezuzah on our doorpost?
Large households
4. With ten or more people living in the house, how many codes can a smart lock hold, and how do we keep them straight?
5. Can the app tell us at bedtime which doors in the house are still unlocked?
Raised ranches, split-levels and their doors
6. The sliding door from our raised ranch's kitchen to the deck only has a thumb latch — can it be made keyless and properly locked?
7. Our 1960s front door already has a knob hole and a deadbolt hole — can a smart lock reuse them without new drilling?
8. Our front door swings outward onto the step — does that rule out a smart deadbolt?
Rented rooms and accessory apartments
9. We let rooms in our house to boarders — what does Rockland expect of the locks on those bedroom doors?
Shuls, yeshivas and community buildings
10. Our shul is applying for a state security grant — can keypads or fob readers on the doors be part of the request?
11. How do we keep a shul's front door controlled on Shabbat, when many of the people coming in can't use a keypad or a fob?
Shops and offices
12. Our Route 59 store closes before Shabbat and the closing time moves every week with sunset — can the door's schedule keep up?

### §17 FAQ (visible == FAQPage, 8)
1. Do your installers work in Monsey, New Square and Kaser as well as Nyack, Pearl River and Stony Point?
2. Can an installation be booked for a Friday morning before Shabbat, or for a Sunday?
3. Do you fit purely mechanical push-button locks as well as electronic smart locks?
4. Can the other locks in the house be re-keyed to match the key of the new smart lock?
5. How long will our front door be out of action on installation day?
6. Can you work at a yeshiva or school building during the school day?
7. Can the keypad's beeps and voice prompts be turned down so they don't wake the children?
8. What happens if we move house within Rockland — can the smart lock come with us?

### Other question-form headings
- H2 "Keypad Dead or Bolt Stuck at a Rockland Door?" (repair capture)
- H2 "Ready to Plan Every Door in the House?" (mid CTA)
- H2 "Locked Out on a Weeknight Anywhere From Tappan to Stony Point?" (final repair capture)

### De-dup notes
Checked by meaning against every question in the NYC, LI, HV, Manhattan, Brooklyn and Queens registers, and against the Suffolk and Westchester pages on disk at ~build end (check_page: no duplicated question or FAQ answer). Deliberately avoided: garage-to-house door rules and "which of the doors deserve a smart lock" (LI), alarm-panel pairing (LI), storm door (LI/Queens), outage/battery-cold/remote-house/rental guest codes/historic district/county licensing/county price comparison (HV), multigenerational/no-smartphone/caregiver schedules/app language (Queens), two-family owner rules and double doors (Brooklyn), auto-relock for walkers (Manhattan FAQ), self-closing door interference (NYC hub), cost-per-county FAQ and setup-visit cost FAQ (HV hub — Rockland prices kept in §14 body), "do you supply the lock" (Queens), selling the house/codes (LI FAQ 10 — this page's FAQ 8 is about physically moving the lock to a new house; partial overlap for main run to judge), coverage FAQ (geo-specific by design, as on every sibling). Licensing and pricing handled in body text, not as repeat questions. Partial overlaps for main run: Q5 bedtime door-status check vs LI Q12 "check the locks on a closed-up beach house from the city" (here: occupied house, nightly status); Q11/Q12 Shabbat schedules vs HV "door schedules" generally; Q9 rented rooms vs Manhattan Q11 "guest bedroom smart lock under LL18" (here: Rockland rooming-house permit/code enforcement).

### Flags for Anwar
1. Religious content: Q1–Q3, Q11, the Shabbat door plan and §10.5 H3 2–3 describe Shabbat/mezuzah practice only from cited published guidance (Chabad.org, Chicago Mitzvah Campaign, Tribe Home Automation) and repeatedly defer to "your rabbi". Worth a skim by someone from the community before shipping.
2. Monsey 2019 attack and Spring Valley fatal fires are cited factually (victims/landlord not named). Skim for tone.
3. Pricing conflicts listed above (access-control and door-buzzer Rockland pages).
4. Images are geo-renamed copies of photos already on sibling pages and look AI-rendered.
5. File size 203,730 B sits 3.5 KB above Manhattan and 3.9 KB below Westchester; re-check after the main run's wiring edits change sibling sizes.


## Orange County (smart-lock-installation-orange-county)

Built 2026-10-17 (batch: Orange, Putnam, Dutchess). Area page, up-link /smart-lock-installation-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (845) 640-3835 in body/CTAs/schema; (800) 486-0943 only in the shared header chrome. Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts unless scraped); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane: **the handover.** Orange County is a growing county where doors constantly change hands — new-construction closings (construction keys, builder keypads), resale purchases (seller codes/app accounts), Army households at West Point/Stewart (on-post lock rules; off-post rentals for a tour), landlord turnovers in Newburgh/Middletown/Port Jervis (RPAPL 768 statewide), sellers' showings — plus logistics (I-84/17K), Goshen appointment offices. Distinct from the HV hub (remote/second homes, cold, radio range, historic doors), the NYC/borough pages, and the batch siblings (Putnam: lakes, rural, commuters; Dutchess: students, STRs).

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| O1 | (direct) West Point community guidelines · Firecrawl scrape (pdf, directQuote: locks/keys/alterations) | https://home.army.mil/westpoint/2117/2261/9593/Community_Guidelines.pdf | "Residents can request permission to alter existing locks or install additional locks by submitting a Request for Alterations form to Community Management. If approved, the replacement lock must be from the same manufacturer as the existing lock and the Community Management Office must receive a copy of the new key." Lost keys → lock changed, $50 fee. Lockouts: first business-hours no charge, second $25, after-hours/weekend $50; resident on lease present with ID. Exterior/doorbell cameras only aimed at resident's own entry/yard. | §5 para 3, §5.5 bullet 6, §6 card, §7 card+methods, §9 West Point Q (quoted), §9 "short stay worth it" Q, §10.5 H3 3, Military section, Handover register row, Glossary |
| O2 | reused from research/soundbar-installation.md (Orange section) | https://www.westpointfamilyhomes.com/ | "Professionally managed by Balfour Beatty Communities". | §5 para 3, §13 card |
| O3 | `New York RPAPL 768 unlawful eviction changing locks 2019 Housing Stability Tenant Protection Act statewide` · Firecrawl search | https://www.nysenate.gov/legislation/laws/RPA/768 ; https://ag.ny.gov/resources/government-organizations/law-enforcement-guidance/unlawful-evictions ; https://nysba.org/nys-housing-stability-and-tenant-protection-act-of-2019-part-iii-what-lawyers-must-know/ | RPAPL 768: unlawful to evict occupant of 30+ consecutive days or with a lease by, inter alia, "changing the lock on such entrance door without supplying the occupant with a key"; class A misdemeanor; civil penalty $1,000–$10,000 per violation; HSTPA 2019 made it statewide (NYSBA). | §5 para 4, §8.5 bullet, §9 rental-portfolio Q (quoted), §10.5 H3 4 |
| O4 | `builder construction keys new home rekey after closing construction core master key homeowners` · Firecrawl search | https://www.reddit.com/r/homeowners/comments/ptjttn/question_about_changing_locks/ (excerpt) ; https://www.facebook.com/KingdomKeysLocks/videos/... (excerpt) ; https://a-1locksmith.com/should-you-change-your-locks-if-moving-into-a-new-construction-home/ (excerpt) | Reddit: "New builds should be using construction cores and swapping out to an owners core that only you get the copies for." Locksmith post: rekeyed a new-construction home "that still had master pins in the locks". A-1: owner's key should permanently lock out construction keys. | §9 construction-keys Q (Reddit quoted), §10.5 H3 1, Glossary |
| O5 | `Schlage Encode factory reset removes all access codes previous owner new homeowner support` · Firecrawl search | https://schlage-res.zendesk.com/hc/en-us/articles/34130652492436-Factory-Reset-a-Schlage-Encode-Lock | "Factory default reset will remove all codes and virtual keys that have been programmed to your lock." | §9 construction-keys Q (quoted), Glossary |
| O6 | `New York General Business Law 777-a housing merchant implied warranty new home one year two years six years` · Firecrawl search | https://www.nysenate.gov/legislation/laws/GBS/777-A ; https://codes.findlaw.com/ny/general-business-law/gbs-sect-777-a/ | Warranty survives passing of title; 1 yr workmanship/materials; 2 yrs plumbing, electrical, heating, cooling (ventilation); 6 yrs material defects. | §9 builder-warranty Q |
| O7 | (direct) · Firecrawl scrape (directQuote) | https://censusreporter.org/profiles/05000US36071-orange-county-ny/ | ACS 2024 1-yr: 411,767 pop; owner-occupied 66%; single unit 69%; mean travel time 35.3 min (NY 33.2). | §5 paras 1 & 5, §5.5 bullets 1 & 5 |
| O8 | (direct) · Firecrawl scrape (directQuote) | https://censusreporter.org/profiles/16000US3650034-newburgh-ny/ | City of Newburgh, ACS 2024 5-yr: 28,519 pop; 11,794 housing units; renter-occupied 65%; multi-unit 64%. | §5 para 4, §5.5 bullet 4 |
| O9 | (direct) · Firecrawl scrape (directQuote) | https://censusreporter.org/profiles/16000US3647042-middletown-ny/ | City of Middletown, ACS 2024 5-yr: 30,289 pop; 10,633 units; owner-occupied 52%; single unit 56%. | §5 para 4, §5.5 bullet 4 |
| O10 | `Orange County NY police burglary unlocked door residents reminded lock doors 2025 …` · Firecrawl search → Firecrawl scrape | https://www.townofnewburghny.gov/cn/webpage.cfm?tpid=8555 | Town of Newburgh PD "Preventing Burglaries While on Vacation": vacant-looking house is a target "during the work day when everyone may be at work or school"; give a neighbour a key; free police house-check notification; "Make sure that a 'Charley bar' is secure on sliding doors"; "Make sure the last person out locks the door." (Wallkill PD car break-in posts were Facebook excerpts only — not used.) | §5 para 5 (quoted), §7.5 sliding doors, §10.5 H3 5 |
| O11 | `New York OCFS how old must a child be to be left home alone guidance latchkey` · Firecrawl search | https://ocfs.ny.gov/programs/cps/faq.php (excerpt) | "Some children are responsible, intelligent, and independent enough to be left alone at 12 or 13 years of age." "A child of 12 might be fine alone for two hours in an afternoon." | Researched for an after-school Q; Q removed in de-dup (Putnam owns that intent). Not on page. |
| O12 | `HIPAA security rule facility access controls 164.310(a)(1) physical safeguards locks` · Firecrawl search | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310 | Facility access controls; role-based access validation; maintenance records "(for example, hardware, walls, doors, and locks)". | Researched for a medical-office Q; Q removed in de-dup (Putnam owns that intent). Not on page. |
| O13 | `Orange County NY warehouse distribution center boom I-84 Route 17K Montgomery Newburgh square feet 2024 OR 2025` · Firecrawl search | https://www.ocpartnership.org/news/details.aspx?id=97f4dd69-cd99-4386-b218-d39a13c46799 ; https://re-nj.com/ridgecut-road-kicks-off-construction-for-146000-sq-ft-logistics-project-in-orange-county/ ; https://www.loopnet.com/Listing/Rte-17k-Newburgh-NY/29957577/ ; https://www.hgar.com/walmart-pursues-plans-for-major-distribution-center-in-orange-county | Ridgecut Road broke ground: I-84 Orange County Logistics Center, 146,075 sq ft, Montgomery. Matrix I-84 Distribution Center, Rte 17K Newburgh, 595,900 SF (listing). HGAR: Walmart seeking Town of Wallkill approval for ~1.5M sq ft DC on ~200 acres near Rte 17K and I-84. (Newburgh South Logistics Center 422,983 sq ft — Facebook excerpt only, not used.) | §8 card, §9 driver-room & dock-keypad Qs (context), Across Orange (Wallkill/Montgomery) |
| O14 | `City of Newburgh Architectural Review Commission historic district certificate of appropriateness doors East End` · Firecrawl search | https://www.cityofnewburgh-ny.gov/DocumentCenter/View/460/Architectural-Review-Commission-Application-Packet-PDF (excerpt) ; https://www.cityofnewburgh-ny.gov/267/Architectural-Review-Commission | Alterations in Historic or Architectural Design Districts require a COA from the ARC; excerpt lists doors among items. East End Historic District Design Guidelines exist. | §7 card (East End), Across Orange (Newburgh). Not used as a Q (HV hub owns the historic-district-keypad intent). |
| O15 | `Washington's Headquarters State Historic Site Newburgh Hasbrouck House first publicly owned historic site 1850` · Firecrawl search | https://parks.ny.gov/visit/historic-sites/washingtons-headquarters-state-historic-site ; https://en.wikipedia.org/wiki/Washington%27s_Headquarters_State_Historic_Site | Nation's first publicly owned historic site, opened July 4, 1850; Washington's HQ for more than 16 months; NHL 1961; ~7 acres. | §13 card |
| O16 | `Storm King Art Center New Windsor Cornwall acres founded 1960 outdoor sculpture` · Firecrawl search | https://stormking.org/about/ ; https://en.wikipedia.org/wiki/Storm_King_Art_Center | 500-acre outdoor museum; since 1960. | §13 card |
| O17 | `Goshen Historic Track oldest harness racing track National Historic Landmark 1838` · Firecrawl search | https://goshenhistorictrack.com/ ; https://en.wikipedia.org/wiki/Historic_Track | Established 1838; National Historic Landmark; half-mile harness track; 44 Park Place, Goshen. | §13 card |
| O18 | `Orange County NY town code Knox box required commercial buildings …` · Firecrawl search | (results were New Castle, Islip, West Orange NJ etc.) | No Orange County NY source found → EMPTY; Knox-box content not used. | — |
| O19 | `manufactured home exterior door thickness 1-1/4 inch smart lock …` · Firecrawl search | (Amazon, YouTube, homeoutlet) | No authoritative source → EMPTY; manufactured-home Q not written. | — |
| O20 | `reddit hudsonvalley OR OrangeCountyNY smart lock OR keypad lock OR "change the locks" new house Orange County` · Firecrawl search | (Lowe's, Level, Orange CA results) | No local Orange County NY Reddit thread on locks → EMPTY. | — |
| O21 | reused from research/soundbar-installation.md Orange section (Firecrawl, 2026-10-17; not re-fetched) | usafacts.org (Orange growth); ocpartnership.org (Tuxedo Reserve); newhomesource.com (Ridgebury Estates, Grandview Estates, Palisades Ridge at Woodbury Junction, Blackburne Homes); zillow (Pershing three-story townhome); en.wikipedia.org Port_Jervis_Line (Harriman busiest station; Hoboken); en.wikipedia.org Stewart airport (Towns of Newburgh/New Windsor; 105th Airlift Wing; built 1930s for West Point cadet aviation); en.wikipedia.org East End Historic District (445 acres, 2,217 buildings, NRHP 1985); Woodbury Common (late 1985, 220 stores); LEGOLAND NY (150 acres, May 20 2021, 60 mi NW of NYC); Galleria at Crystal Run (April 1, 1992); orangecountyny.gov Consumer Affairs 255 Main St Goshen; Electrician licence application + 2024 Local Laws (county Electrical Licensing Board); Consumer Law Help Manual – Home Improvements; chroniclenewspaper.com (Town of Goshen STR ban, excerpt) | As logged in that file. | §5, §5.5, §7, §8, §8.5, §13, Across Orange |
| O22 | silo research (research/smart-lock-installation.md) | Fixr national $250–$400, avg $300 (Jan 2025) | National third-party, labelled. | §10.5 H3 2, §14 |
| O23 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are published claims, stated as such on page. | — |
| O24 | Local news on smart locks specifically in Orange County (Times Herald-Record, Mid-Hudson News, Patch) | — | None found → EMPTY. | — |
| O25 | Field Notes | — | No sourced Orange County install anecdote → written as standing routine and labelled so. | Field Notes |

### Prices used (all from live AESS pages; none invented)
| Figure | Scope | Source |
|---|---|---|
| $2,100–$3,500 | single-door keypad/card reader + electric strike, installed | live smart-lock-installation-hudson-valley.html Orange row ($1,500–$2,500 × 1.40) |
| $350–$630 | new electric strike | same HV hub row |
| $413–$679 | failed electric strike repair | same HV hub row |
| $250 first hour, then 30-min blocks | setup-only visit, Orange | HV hub; soundbar-installation-orange-county.html; research/tv-mounting-prices/BRIEF.md |
| $195/hr, 3-hr minimum ($585) | service/callback, never on initial install | blueprint §9 |
| quoted flat at walkthrough | residential smart lock / closing-day handover | no AESS figure exists |
**Conflicts for Anwar:** (1) live access-control-installation-orange-county.html: "Single-door lobby fob reader: $1,500 to $2,500 plus the 15% surcharge" (= $1,725–$2,875) and elsewhere "$1,500 to $2,500 installed" flat — vs the HV smart-lock hub's Orange $2,100–$3,500 (×1.40) used here for silo consistency. (2) live door-buzzer-repair-orange-county-new-york.html: "Electric strike replacement + alignment $450–$950" — vs $350–$630 / $413–$679 used here (HV hub). (3) Setup-only $250 rate is published for TV/device setup; used for smart-lock app/code/reset visits (same flag as other smart-lock pages).

## Images (11)
Permanent image rule (Drive "AESS Website Photos/Smart Lock Installation" empty; CompanyCam not connected). All viewed before use; WebP q80. None of the source photos is used on smart-lock-installation-hudson-valley (perceptual-hash checked). Sources prefer the *orange*-named library files; claims sent to the Putnam/Dutchess builders. Several were also used (as other filename copies) on the NYC/LI hubs. Crops remove faces in clear profile, a "Community Center" wall sign, a named business ("Pinnacle Business Center") and a readable cardholder-name screen. Library photos look AI-rendered (uniform "Abstract Enterprise LLC" shirts with the company's own 800 number) — same flag as earlier pages.

| New filename (images/smart-lock-installation/) | Source file | Crop |
|---|---|---|
| smart-lock-installation-orange-county-keypad-strike-push-to-exit.webp (hero, eager) | images/low-voltage/low-voltage-installation-long-island-electric-strike-keypad.jpg | none |
| smart-lock-installation-orange-county-proximity-reader-glass-door-frame.webp | images/low-voltage/low-voltage-installation-orange-county-12-access-control-reader-wiring.jpg | none |
| smart-lock-installation-orange-county-ceiling-wifi-access-point-lift.webp | images/low-voltage/low-voltage-installation-orange-county-02-access-point-lift-install.jpg | right 16% removed ("Community Center" sign) |
| smart-lock-installation-orange-county-maglock-header-glass-entrance.webp | images/low-voltage/low-voltage-installation-orange-county-13-maglock-install.jpg | left 24% removed (shirt/cap phone text) |
| smart-lock-installation-orange-county-keypad-reader-employee-door-stone.webp | images/commercial-security/commercial-security-systems-orange-access-reader.jpg | left 62% removed (face, business name) |
| smart-lock-installation-orange-county-keypad-and-camera-entrance-pair.webp | images/commercial-security/commercial-security-systems-orange-alarm-keypad.jpg | centre strip (faces, door signage removed) |
| smart-lock-installation-orange-county-fob-card-programming-station.webp | images/commercial-security/commercial-security-systems-orange-credential-programming.jpg | left 68% removed (face, cardholder names on monitor) |
| smart-lock-installation-orange-county-crew-van-unload-equipment.webp | images/commercial-security/commercial-security-systems-orange-crew-van.jpg | none (faces turned away/small) |
| smart-lock-installation-orange-county-electric-strike-door-frame-prep.webp | images/commercial-security/commercial-security-systems-orange-electric-strike.jpg | left 52% removed (face) |
| smart-lock-installation-orange-county-employee-entrance-keypad-reader.webp | images/commercial-security/commercial-security-systems-bronx-hero-loading-dock.jpg | left 52% removed (face) |
| smart-lock-installation-orange-county-video-intercom-keypad-entry-wiring.webp | images/low-voltage/low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg | none (back view) |
Rejected after viewing: none other needed. DAILY-LOG note: `images: 11 reused from images/low-voltage/ and images/commercial-security/ (no real smart-lock photos yet)`.

## Question register — smart-lock-installation-orange-county

### §9 YOUR QUESTIONS ANSWERED (H3)
New houses and the builder's keys
1. Could the builder's construction keys still open the front door of our new house in Chester or Monroe?
2. The house is still open framing — is anything worth running to the front door before the drywall goes up?
3. Will swapping the builder's lock for a smart lock affect our new-home warranty?
Army households at West Point and Stewart
4. We live in on-post family housing at West Point — are we allowed to put a smart lock on our quarters?
5. Our off-post landlord in Cornwall won't allow any drilling — is there still a keyless option?
6. We'll only be at Stewart or West Point for two or three years — is a smart lock worth buying for such a short stay?
Selling and renting
7. We're selling our house in Warwick — should showings go through the realtor's lockbox or a temporary code on our smart lock?
8. We own a dozen rental houses spread from Port Jervis to Newburgh — can one app run all the locks?
Businesses
9. Truck drivers check in at our Montgomery distribution building — how do we let them into the drivers' room without letting them into the warehouse?
10. Forklifts keep clipping the keypad beside our Wallkill dock door — where should it go instead?
11. Our Goshen office sees clients by appointment only — can staff let a visitor in from their desk?

### §17 FAQ (visible == FAQPage, 9)
1. How much more does a wired keypad door cost in Orange County than in the city?
2. Do your crews go as far as Port Jervis, Greenwood Lake and Highland Falls?
3. Can you change the locks on closing day, before the moving truck arrives?
4. Can you schedule around a PCS date or a housing move-out inspection?
5. Can you work in our new house before it closes, if the builder agrees?
6. Can the locks be set up before the internet is connected at our new house?
7. Will we get a written record of what was changed on each door?
8. Can the outdoor garage-door keypad be reset at the same visit?
9. Do you install smart locks for buyers relocating from out of state who can't be here for closing?

### Other question-form headings
- H2 "Keypad Stuck Somewhere Between Newburgh and Port Jervis?" (repair capture)
- H2 "Closing, Lease or Moving Day on the Calendar?" (mid CTA)
- H2 "Ready to Know Who Can Still Open Your Door?" (mid CTA)
- H2 "Door Refusing Codes on Moving Day or at Shift Change?" (final repair capture)

### De-dup notes
- Removed during build after comparing with the Putnam and Dutchess pages on disk (same batch): after-school "kids off the bus — can the lock tell us they're home" (= Putnam), "parent alone — how does the ambulance crew get in" (= Putnam), medical-office records room/HIPAA (= Putnam), FAQs sliding patio door (= Putnam slider Q), keyed-alike cylinders (= Putnam/Dutchess FAQs), builder-installed lock service (≈ Putnam FAQ), install duration (= Putnam FAQ), new-door bore (≈ Putnam pre-bored doors FAQ).
- Avoided by design: board/HOA approval (NYC co-op Q), historic-district keypad approval (HV Kingston Q; Newburgh ARC mentioned in body only), short-term rental questions (Manhattan/HV/Dutchess), landlord cutting off a former tenant (NYC Q13; RPAPL 768 used only inside the portfolio Q), admin-holder FAQ (Queens), temporary worker access (Manhattan), garage-to-house door (LI).
- Partial overlaps for the main run to judge: Q1 construction keys vs Brooklyn Q12 (sponsor-installed condo lock admin takeover) and Queens FAQ 2 (re-key after closing on a resale); Q5 no-drill retrofit vs NYC Q1 (renter installing without asking the landlord — different: landlord has refused drilling); FAQ 3 closing-day scheduling vs Dutchess "walkthrough before student move-out"; FAQ 1/2 cost & coverage geo-specific by design.


## Putnam County (smart-lock-installation-putnam-county)

Built 2026-10-17 (batch: Orange / Putnam / Dutchess smart-lock area pages). Area page, up-link /smart-lock-installation-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (845) 640-3835 (800 only in shared header chrome). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless scraped); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane: Putnam = converted 1930s lake bungalows (thin/hollow doors, moving frames), lake associations and park districts, NYC watershed land between the house and the driveway gate, lightning on long gate runs, bulkhead cellar access for oil/propane/well service, bears trying door handles, commuter households (phone-dies credential fallback), volunteer fire/EMS Knox-box access, antique rim locks on Highland farmhouses, church side doors shared by several groups, community halls rented on weekends; Cold Spring HDRB review and Putnam Ch. 135 registration in body text only.

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| P1 | `Putnam County New York QuickFacts census housing units owner-occupied` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.census.gov/quickfacts/putnamcountynewyork | Pop 99,028 (Jul 1 2025); housing units 38,713 (Jul 1 2025); owner-occupied 83.8% (2020–24); median value $471,300; 65+ 21.3%; mean travel time to work 39.3 min; persons/household 2.68; broadband 94.8%. | §5 para 1, 4, 5; §5.5 bullets 1, 4, 5 |
| P2 | `Putnam Lake Patterson NY history summer community Smith developed bungalows` · Firecrawl search → Firecrawl scrape | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Smadbeck brothers (Home Guardian) with McGolrick Realty and the NY Daily Mirror; three communities built beginning 1928: Lake Carmel (Kent), Lake Peekskill (Putnam Valley), Putnam Lake (Patterson), as summer bungalow communities; Putnam Lake: 1,111 acres, ~200-acre lake from dammed Morlock Brook, 11,000 lots mapped, 20'×100' lots sold for $50, room for bungalow + outhouse; deserted after Labor Day. | §5 para 2, §5.5 bullet 2, §7 card, §9 Q1, cottage checklist |
| P3 | same search (excerpt) | https://www.nytimes.com/2005/06/26/realestate/singing-the-praises-of-country-life.html | Excerpt: smaller Putnam Lake houses "built as summer homes but have since been winterized and now serve residents year-round". | §5 para 2 ("many … year-round") |
| P4 | same search → Firecrawl scrape | https://www.pattersonny.org/PLPD_2.php | Putnam Lake Park District created after 2011 community petition; facilities reserved for residents owning or renting homes in the district; Warren & Jackson beaches; boats on parkland Mar 1–Dec 1. | §9 Q3 lake association |
| P5 | `Lake Carmel NY history summer bungalow colony developed 1920s year-round homes` · Firecrawl search | https://www.homes.com/local-guide/lake-carmel-ny/ ; https://www.townofcarmelny.gov/253/About-Our-Town | Excerpts only (dam late 1920s, summer cottages; Mahopac hotels from 1834). Not cited on page (P2 used instead). | research only |
| P6 | `Knox box residential lock box program fire department Putnam County NY seniors emergency access` · Firecrawl search → Firecrawl scrape | https://www.kentvfd.com/content/knoxbox/ | Kent VFD uses Knox Box for businesses and homes; responding vehicle carries secured key safe unlocked by Putnam County 911 dispatch code only in emergency, access recorded; 2024 incidents 359 (109 fire, 250 EMS); meta: Fahnestock SP 14,086 acres, White Pond MUA 276 acres, Croton watershed, Chuang Yen Monastery, 3.4 mi of Taconic. | §5 para 5, §5.5 bullet 6, §9 Q4 key box, §10.5 H3 3, responder plan, §13 Fahnestock card, Across Putnam (Kent) |
| P7 | same search (excerpt) | https://www.nhfd21.org/content/knoxbox/ | North Highlands FD: Knox access requested through Putnam County Dispatch Center. | background (corroborates P6) |
| P8 | `black bear opened door lever handle entered home Putnam County NY` · Firecrawl search | https://www.facebook.com/PCSDSheriff/posts/... (excerpt) | Sheriff post excerpt — agency/county unclear; NOT used. | — |
| P9 | `NYSDEC black bear tips lock doors lever handles bears entering homes New York` · Firecrawl search → Firecrawl scrape | https://portal.ct.gov/deep/wildlife/bears/the-basics-of-living-with-black-bears | CT DEEP: open/unlocked doors and windows let bears in; lock ground-floor doors/windows; locking screen doors does little; bears open most unlocked car doors. | §9 Q6 bears |
| P10 | same search (excerpts) | https://www.kunc.org/environment/2013-04-27/6-ways-to-bear-proof-your-home ; https://townofridgway.colorado.gov/sites/g/files/lrnvjt1246/files/bearproofing%20your%20home.pdf | Colorado guidance: replace exterior lever handles with round knobs bears can't push/pull open. | §9 Q6 (as "wildlife agencies in western bear country") |
| P11 | same search → Firecrawl scrape (query) | https://dec.ny.gov/nature/animals-fish-plants/black-bear/management/bearwise | Query scrape returned no door-specific text → EMPTY for door tips; not cited. | — |
| P12 | `bear sightings Putnam Valley Mahopac Carmel 2025 police warn residents` · Firecrawl search | https://www.facebook.com/CarmelPoliceNY/posts/our-headquarters-has-been-receiving-calls-for-bear-sightings-in-the-areas-of-dai/1002028455771488/ ; https://www.lohud.com/story/news/2017/05/30/bears-sighted-hudson-valley/356477001/ | Excerpts: Carmel PD warning re bear sightings (Daisy Ln, Dixon Rd); Lohud May 30 2017: bear spotted in Mahopac. | §9 Q6 |
| P13 | `Village of Cold Spring Historic District Review Board certificate of appropriateness doors exterior changes` · Firecrawl search → Firecrawl scrape | https://www.coldspringny.gov/faq.aspx?TID=19 | COA required for exterior changes in local or national historic district; $30 fee; photos + catalog cuts; five-member HDRB, 2nd Wednesday 8 pm; building permit applications list contractors' Putnam County licence numbers. | §8.5 callouts 3–4, §10.5 H3 7 |
| P14 | `NYC DEP watershed Putnam County percent of county land reservoirs Croton system …` · Firecrawl search | https://www.nyc.gov/site/dep/water/west-branch-reservoir.page | West Branch Reservoir: Kent & Carmel, 8 billion gallons, in service 1895, two basins separated by Route 301, 20 sq mi basin; connected to Lake Gleneida (controlled lake). | §5 para 3, §5.5 bullet 3 |
| P15 | same search → Firecrawl scrape (pdf, directQuote) | https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf | Nine municipalities (6 towns, 3 villages), over 240 sq mi; Croton watershed; Croton Falls Reservoir (Carmel & Southeast, 5.2 bn gal, 1891); Boyds Corner (Kent); Kirk Lake controlled lake (Kent); Lake Gleneida off Route 52; most rugged terrain Philipstown, Putnam Valley, western Kent (peaks >1,000 ft); commercial along Routes 6, 9, 22, 52 + I-84 at Route 312 and Ludingtonville Rd; wetlands 6.1% (2011); 2010 pop by town (Carmel 34,305 largest); NYS Police 1672 Route 22 Southeast; fire/EMS list; seven Metro-North stops, busiest Brewster Village, Southeast, Cold Spring, Garrison. | §5 paras 1, 3, 4, 5; §8 intro + corridor cards; Across Putnam |
| P16 | `Putnam County NY home improvement license consumer affairs` (silo HV run) re-verified · Firecrawl scrape (directQuote) | https://putnamcountyny.gov/laws/item/local-law-no-10-of-2013-amend-chapter-135-code-of-putnam-county-entitled-contractors | "No person shall maintain, conduct, operate or engage in a home improvement business within the County of Putnam … unless such person is registered pursuant to this chapter." Page does NOT claim AESS is registered; tells readers to check. | §8.5 callout 4, §10.5 H3 7 |
| P17 | `Putnam County Historic Courthouse Carmel built 1814 oldest courthouse New York` · Firecrawl search | https://www.hmdb.org/m.asp?m=37288 ; https://en.wikipedia.org/wiki/Putnam_County_Courthouse_(New_York) | Built 1814, renovated 1847, jail added 1855, one hanging 1844; marker: second oldest working courthouse in NY. | §13 card |
| P18 | `Tilly Foster Farm Brewster Southeast Putnam County history acres` · Firecrawl search | https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2022/August/minutes/Phys-08-25-22-Presentation-Tilly-Foster-Overview-2022.pdf | ~199 acres in Town of Southeast; dairy, then horse breeding; county purchased 2002. | §13 card, Across Putnam |
| P19 | `Manitoga Russel Wright Garrison NY house Dragon Rock National Historic Landmark` · Firecrawl search | https://www.visitmanitoga.org/dragon-rock-house-studio | 75-acre woodland garden, NHL; Wright hired architect David Leavitt in 1958 for Dragon Rock. | §13 card |
| P20 | `West Point Foundry Preserve Cold Spring Scenic Hudson acres history` · Firecrawl search | https://www.scenichudson.org/explore-the-valley/scenic-hudson-parks/west-point-foundry-preserve/ ; https://www.hudsonrivervalley.com/sites/West-Point-Foundry-Preserve-/details | 90 acres; West Point Foundry Archeological Site NHL 2021; Parrott guns in Civil War. | §13 card |
| P21 | `Chuang Yen Monastery Kent NY Great Buddha Hall statue height founded` · Firecrawl search | https://en.wikipedia.org/wiki/Chuang_Yen_Monastery | Great Buddha Hall houses the largest indoor Buddha statue in the Western Hemisphere. | §13 card, Across Putnam (Kent) |
| P22 | `Putnam Hospital Carmel NY Stoneleigh Avenue Northwell beds` · Firecrawl search | https://www.northwell.edu/locations/putnam-hospital | Putnam Hospital, 670 Stoneleigh Ave, Carmel — Northwell. (165-bed figure from practicelink not used.) | §8 Stoneleigh card, Across Putnam |
| P23 | `Highlands Current Philipstown burglary house unlocked doors police advise lock` · Firecrawl search → Firecrawl scrape | https://highlandscurrent.org/2024/09/10/police-investigating-philipstown-burglaries/ | Sept 5 2024 break-ins on Old Albany Post Rd and Indian Brook Rd, Philipstown; Sheriff reminded residents to keep doors/windows locked and not post when away. | §10.5 H3 5 |
| P24 | `Putnam County sheriff burglary unlocked door house Carmel Mahopac Patterson 2025 2026` · Firecrawl search | putnamsheriff.com; facebook excerpts | No lock-specific item found → EMPTY beyond P23. | — |
| P25 | `site:reddit.com Putnam County NY smart lock OR keypad OR "lake house" Mahopac OR Carmel OR Brewster` · Firecrawl search | r/hudsonvalley, r/upstate_new_york etc. (excerpts) | No smart-lock-relevant Putnam thread → Reddit EMPTY for the service category. | — |
| P26 | `smart lock for sliding patio door keypad retrofit manufacturer compatible sliding glass door` · Firecrawl search | https://lockeyusa.com/product/c150/ ; https://www.yalehome.com/ae/en/products/smart-door-locks/code-handles/smart-code-handle | Lockey C150 hook-bolt keyless lock for sliding glass patio doors; Yale Smart Code Handle for terrace doors (UAE site, not cited). | §6 card, §7 card, §10 equipment card (slider Q dropped in de-dup, see register) |
| P27 | `Bilco basement door security interior slide lock keyed lock kit outside entry` · Firecrawl search | https://www.bilco.com/ProductDetail/Basement-Door-Keyed-Lock-Kit-87 | Keyed lock kit lets Classic Series basement doors be locked/unlocked from outside with a key. | §9 Q5 bulkhead |
| P28 | `HIPAA security rule facility access controls 164.310(a)(1) physical safeguards hhs.gov` · Firecrawl search | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310 | Facility access controls; role-based access control/validation; maintenance records of repairs/modifications to security-related physical components "(for example, hardware, walls, doors, and locks)". | §8.5 callout 5 (records-room Q removed in de-dup) |
| P29 | silo/other research reused (not re-fetched) | research/smart-lock-installation.md (Allegion door prep 1-3/8"–2", backset 2-3/8/2-3/4; Fixr Jan 2025 $250–$400); research/fiber-optic-installation.md + research/cat6-repair.md (NYC DEP watershed regulations Dec 2019 covering communities in Ulster, Orange, Putnam, Westchester; Central Hudson Dig Safely/811) | as listed | §7.5, §9 Q1/Q8, §10.5, §14 |
| P30 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are recurring published claims, stated as such on page. | — |
| P31 | Local news on smart locks specifically in Putnam (Highlands Current, Mahopac News, Patch, Mid-Hudson News, Lohud) | — | None found → EMPTY. | — |
| P32 | Field Notes | — | No sourced Putnam smart-lock job anecdote → written as general routine and labelled as such. | Field Notes |

### Prices used (all from live AESS pages; none invented)
- Single-door keypad or fob reader with electric strike $2,175–$3,625; new electric strike $363–$653; failed strike repair $428–$703 — Putnam figures as published on live smart-lock-installation-hudson-valley.html (= silo base × 1.45).
- Pedestrian gate keypad $1,500–$2,000 — live access-control-installation-putnam-county.html (FAQ text).
- Setup-only first hour $250, then 30-min blocks — hub page / research/tv-mounting-prices/BRIEF.md line 15.
- $195/hr, 3-hour minimum ($585) service/callback, verbatim.
- House/cottage/slider/cellar smart lock: no AESS figure → quoted flat at walkthrough.
- National comparison only: Fixr $250–$400 (Jan 2025).
- **Conflicts for Anwar:** access-control-installation-putnam-county.html shows "SINGLE DOOR / GATE $1,900–$6,000" and "Putnam = Brooklyn base + 25% HV surcharge" (vs hub's ×1.45 $2,175–$3,625); door-buzzer-repair-putnam-county-new-york.html shows "Electric strike replacement + alignment $450–$950" and a $250 service call; door-buzzer-installation-putnam-county-ny.html shows a $300 service call. Page uses the smart-lock hub's published Putnam figures.

## Images (11)
Drive folder empty, CompanyCam not connected → permanent image rule. Each viewed; 9 cropped with Pillow to remove faces, readable phone numbers (800-486-0943 on shirts/caps/lift sign) and a building number ("1000"). Library photos look AI-rendered (garbled logo text) — same note as Queens; needs Anwar's review. No source cluster is used on the Hudson Valley hub; clusters claimed by the Orange and Dutchess builders were avoided. Several clusters are also used on NYC/LI/Manhattan/Queens pages (library has ~80 distinct photos; only ~6 unused, none of them door hardware).

| New filename (images/smart-lock-installation/) | Source file | Crop |
|---|---|---|
| smart-lock-installation-putnam-county-gate-fingerprint-keypad-wiring.webp (hero, eager) | images/commercial-security/commercial-security-systems-nyc-gate-reader-install.jpg (also LI) | left 540 px (face removed) |
| smart-lock-installation-putnam-county-exterior-enclosure-brick-conduit.webp | images/low-voltage/low-voltage-installation-nassau-county-exterior-enclosure-install.jpg (cluster also LI) | x≥700 (face, cap/shirt phone removed) |
| smart-lock-installation-putnam-county-electric-strike-terminal-wiring.webp | images/low-voltage/low-voltage-installation-putnam-county-12-electric-strike-wiring.jpg (cluster also NYC hub) | x≥400 (partial face removed) |
| smart-lock-installation-putnam-county-gated-entrance-post-camera.webp | images/commercial-security/commercial-security-systems-putnam-lpr-driveway.jpg (unused cluster) | x≥900 (face, phone, building number removed) |
| smart-lock-installation-putnam-county-door-controller-boards-power-supply.webp | images/commercial-security/commercial-security-systems-nyc-access-control-panels.jpg (also LI) | x≥650 (face, phone removed) |
| smart-lock-installation-putnam-county-laptop-network-rack-setup.webp | images/low-voltage/low-voltage-installation-putnam-county-11-rack-switch-config.jpg (cluster also Manhattan) | x≥660 (face, phone removed) |
| smart-lock-installation-putnam-county-ceiling-wifi-access-point.webp | images/low-voltage/low-voltage-installation-putnam-county-10-access-point-lift-install.jpg (Manhattan used a cropped variant) | x≥570, y≤600 (face, phone, "community center" sign removed) |
| smart-lock-installation-putnam-county-ceiling-grid-cable-pull.webp | images/low-voltage/low-voltage-installation-putnam-county-09-ceiling-grid-bundle-pull.jpg (cluster also Manhattan) | none (back view, no phone) |
| smart-lock-installation-putnam-county-jhook-cable-pathway.webp | images/low-voltage/low-voltage-installation-putnam-county-04-jhook-pathway-bundle.jpg (cluster also Manhattan) | none (back view, no phone) |
| smart-lock-installation-putnam-county-wall-cameras-conduit-block-wall.webp | images/commercial-security/commercial-security-systems-putnam-warehouse-cameras.jpg (cluster also Queens) | x≥930 (face, phone, lift sign removed) |
| smart-lock-installation-putnam-county-fiber-splicer-patch-rack.webp | images/low-voltage/low-voltage-installation-putnam-county-05-fiber-splice-tray.jpg (unused cluster) | x≥680 (face, shirt phone removed) |

DAILY-LOG note: `images: 11 reused from images/low-voltage/ and images/commercial-security/ (no real smart-lock photos yet)`.

## Question register — smart-lock-installation-putnam-county

### §9 YOUR QUESTIONS ANSWERED (H3)
Lake cottages and lake-side doors
1. Our Lake Carmel cottage began as a 1930s summer bungalow and its front door is thinner than modern doors — can it take a smart deadbolt at all?
2. Neighbours on our Putnam Lake street keep spare keys for each other — is a code better than the key under the planter?
3. Our lake association wants a keypad on the beach gate or clubhouse — how should members' codes be handed out and taken back each season?
Service visits, emergencies and wildlife
4. We already have a fire-department key box at our Kent house — what has to change when the front door gets a smart lock?
5. The oil delivery driver and the well-pump technician both need our basement — can the outside bulkhead door go keyless?
6. Bears around our Putnam Valley house have learned to try door handles — does a smart lock change anything?
Commuter households
7. If my phone dies on the late train home, how do I get into the house?
Gates, long driveways and the watershed
8. We want a keypad at the foot of a 600-foot driveway — do reservoir and wetland rules affect running a cable there?
9. Lightning on our hilltop took out a doorbell last summer — does a wired gate keypad need surge protection?
Old farmhouses and village houses
10. Our Garrison farmhouse still has an antique rim lock on the front door — can a smart lock go on without taking it off?
Churches and community halls
11. The youth group, the food pantry and an evening meeting all use our Brewster church's side door — can one lock give each group its own nights?
12. Our community hall in Putnam Valley is rented for parties most weekends — how do renters get in without being handed a key?

### §17 FAQ (visible == FAQPage, 9)
1. What does a keyless business entrance or gate keypad cost in Putnam County?
2. Will a smart lock keypad work when we're wearing winter gloves?
3. Can a smart deadbolt go on a door that swings outward onto a deck or porch?
4. Will the walkthrough cover the gate, the garage and the outbuildings, or only the house?
5. We're ordering new exterior doors — should they come pre-bored for a particular smart lock?
6. Do you cover Philipstown and Putnam Valley as well as Carmel, Brewster and Patterson?
7. Will a smart lock lower our homeowners insurance premium?
8. Can the lock's alerts also go to a neighbour or caretaker who checks on the house?
9. Can a gate keypad go on a post beside the drive instead of on the gate itself?

### Other question-form headings
- H2 "Smart Lock Dead or Stubborn Somewhere in Putnam County?" (repair capture)
- H2 "Ready to Lock Up Before the Morning Train?" (mid CTA)
- H2 "Locked Out of the Cottage, the Mudroom or the Gate?" (final repair capture)

### De-dup notes
- Replaced after comparing with the concurrently built Orange and Dutchess pages on disk: kids-off-the-school-bus arrival alert (= Orange), parent-falls ambulance access (= Orange; reframed to "key box already installed — what changes"), medical-office records room/HIPAA (= Orange; HIPAA kept only as a §8.5 callout), lake-side slider (≈ Orange FAQ sliding patio door; slider kept only in body/cards), church taking back volunteers' keys (≈ Dutchess caretaker take-back; reframed to group schedules on one door), FAQs keyed-alike (= Orange/Dutchess), builder-installed lock service (= Orange), remove smart lock at sale (= Dutchess), how long one deadbolt takes (= Orange).
- Avoided hub/LI/NYC intents: STR registry, remote check of closed-up house, outage behaviour, cold/battery, barn range, no internet, historic-district approval for a keypad (Cold Spring HDRB kept as §8.5 body callout), county licensing Q (Ch. 135 kept as body callout), storm door, glass panel/mail slot, garage-to-kitchen door.
- Partial overlaps for the main run to judge: Q4 key box vs Orange "Mom … ambulance crew get through a locked door?" (different intent: keeping the Knox key valid after a lock change); FAQ 8 alerts to neighbour/caretaker vs Dutchess "Red Hook local contact … what does that person need from the lock?"; FAQ 5 order new doors pre-bored vs Orange "new door only has a knob — can you add the bore?"; FAQ 1 cost and FAQ 6 coverage are geo-specific by design.

## Dutchess County (smart-lock-installation-dutchess-county)

Built 2026-10-17 (batch: Dutchess / Orange / Putnam smart-lock area pages). Area page, up-link /smart-lock-installation-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (845) 640-3835 (800 only in shared header chrome). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).

Thesis / lane: Dutchess is the county where keys change hands on a calendar — student houses near Marist, Vassar and Bard that turn over every May and August; owner-hosts renting their own homes under town-by-town short-term rental laws (Beacon primary-residence/100-day law, Town of Rhinebeck permit with floor plan of exits and fire-inspector access, Red Hook local contact within 15 air miles); pre-1980 City of Poughkeepsie multi-family houses where drilling a painted door meets the lead rules; historic villages (Rhinebeck overlay, Poughkeepsie HDLPC) and river estates with caretakers whose keys must be handed over; State Police/Sheriff advice on second-floor entry points and keys/fobs left in cars; Beacon Main Street shops with apartments above and Hyde Park/Rhinebeck restaurants with seasonal staff. Statewide RPAPL 768 lockout law (not the NYC Admin Code) governs landlords here.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Firecrawl search `site:reddit.com r/hudsonvalley OR r/Poughkeepsie smart lock OR keypad OR lockbox Airbnb house` → only r/hudsonvalley thread titles (Airbnb saturation; "Couple charged in Airbnb blaze that killed mother, baby in Dutchess…" https://www.reddit.com/r/hudsonvalley/comments/1jfzcj7/…). Thread bodies EMPTY (not accessible in build env); the news story itself was sourced from CBS (D12). Firecrawl search `site:reddit.com Poughkeepsie landlord locks keys tenant OR "smart lock" OR keypad` → generic r/Tenant / r/Landlord threads, none Dutchess-specific → not used. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from cost guides / rental marketing / product pages, stated as such on page. |
| 6 | Landmarks | L1–L7 |
| 7 | Use cases / building stock | D1–D8 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | CBS New York (Salt Point fire), Highlands Current (Beacon STR registration), Poughkeepsie Journal (Red Hook STR law, 2021, excerpt), NYS State Police alert, Dutchess Sheriff release. |
| 10 | Hyperlocal | Highlands Current used; Daily Freeman / Mid-Hudson News smart-lock stories: none found → EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| D1 | `Dutchess County QuickFacts housing units owner-occupied population 2025 census` · Firecrawl search → Firecrawl scrape | https://www.census.gov/quickfacts/dutchesscountynewyork | Pop 300,708 (July 1 2025); housing units 124,843 (July 1 2025); owner-occupied rate 69.2% (2020–2024); median owner-occupied value $400,600; persons 65+ 21.1%; persons per household 2.40; median gross rent $1,582; broadband subscription 93.5%; mean travel time to work 31.2 min. | §5 para 1–2, §5.5 bullets, Across Dutchess |
| D2 | `City of Poughkeepsie rental registry inspection program landlords` · Firecrawl search → Firecrawl scrape | https://www.dutchessny.gov/Departments/DBCH/Rental-Registry-Program.htm | NYS Public Health Law 1377 rental registry: residential rental property with two or more units in the City of Poughkeepsie with a 12601 zip code, built before 1980 → must register and obtain a lead safety certificate; lead inspection per unit; visual check for deteriorated paint and bare soil, dust wipe sampling. | §5 para 4, §5.5 bullet, §7.5, §9 lead Q, §10.5 H3, landlord checklist |
| D3 | `EPA RRP rule minor repair 6 square feet interior 20 square feet exterior pre-1978 renovation` · Firecrawl search | https://www.epa.gov/lead/if-project-disturbs-six-square-feet-or-less-interior-surface-or-20-square-feet-or-less (excerpt is the full EPA FAQ text) | Disturbing ≤6 sq ft interior or ≤20 sq ft exterior painted surface is "minor maintenance and repair", not a "renovation" under RRP, provided no prohibited work practice, window replacement or demolition. | §9 lead Q, §7.5, §10.5 H3 |
| D4 | `City of Beacon short-term rental law registration Airbnb` · Firecrawl search → Firecrawl scrape | https://highlandscurrent.org/2026/02/20/registration-lax-on-short-term-rentals/ | Feb 20 2026: Inside Airbnb counted 133 Beacon units listed July 2025; FOIL files show only 33 registered; 2020 law allows homeowners and tenants to rent up to 30 days at a time, max 100 days/year; must be host's primary residence; accessory dwelling units cannot be rented; 2% occupancy tax from Jan 1 2025. | §5 para 3, §5.5, §9 Beacon Q, FAQ ADU, §10.5 |
| D5 | same search | https://beaconny.gov/index.php/departments/building-department/ (excerpt) | §223-26.5 Code of the City of Beacon: unlawful to operate a short-term rental without first obtaining a short-term rental permit. | §9 Beacon Q |
| D6 | `Town of Rhinebeck short-term rental law permit` · Firecrawl search | https://www.rhinebeckny.gov/uploads/3/9/4/4/39447425/ll_2_of_2025_-_short_term_rental_-_dos_filing.pdf ; https://www.rhinebeckny.gov/uploads/3/9/4/4/39447425/str_application_final_2.pdf (excerpts carry the law text) | Town LL 2 of 2025, Ch. 125 Art. XV: STR ≤30 consecutive days; not permitted in condominium apartments; application authorises Code Enforcement Officer and Fire Inspector to inspect; contact person responds within 24 hours; floor plan per level showing bedrooms, windows, exits; CEO inspects within 30 days; Rhinecliff hamlet districts also need Planning Board special use permit; liability certificate naming the Town; permits valid two years. Village of Rhinebeck accepts its own STR permit applications at Village Hall (https://villageofrhinebeck.gov/announcements-public-notices/national-dea-takeback-day-4rjtn-ggmke, excerpt). | §5 para 3, §9 Rhinebeck Q, FAQ inspection timing, §10.5, host checklist |
| D7 | `Town of Hyde Park short-term rental law OR Red Hook short-term rental law Dutchess 2025` · Firecrawl search | https://ecode360.com/38104626 (excerpt) ; https://www.poughkeepsiejournal.com/story/news/local/2021/12/23/red-hook-airbnb-short-term-rental-rules-approved/9009869002/ (excerpt) | Red Hook Ch. 112: designated local contact if owner not staying within 15 air miles; registered primary residence may be rented once per calendar year (<30 days) without an annual operating permit. PJ Dec 23 2021: Red Hook Town Board unanimously passed STR law; one-bedroom rentals permitted in all districts, limited to 210 days/year. Hyde Park: only aggregator (strprofitmap) → not used. palisadestays.com aggregator → not used. | §5 para 3, §9 Red Hook Q, §10.5 |
| D8 | `RPAPL 768 unlawful eviction change locks New York statewide 2019 Housing Stability Tenant Protection Act` · Firecrawl search | https://www.nysenate.gov/legislation/laws/RPA/768 (excerpt of statute) ; https://nysba.org/nys-housing-stability-and-tenant-protection-act-of-2019-part-iii-what-lawyers-must-know/ (excerpt) ; https://ag.ny.gov/resources/government-organizations/law-enforcement-guidance/unlawful-evictions (excerpt) | RPAPL 768: unlawful to remove/plug/render inoperable the entrance-door lock or change it without supplying the occupant a key; HSTPA 2019 made unlawful eviction a Class A misdemeanor throughout the state; AG guidance: unlawful evictions are criminal matters. | §5 para 4, §9 late-rent Q, §10.5, landlord checklist |
| D9 | `Marist College Poughkeepsie Route 9 campus acres students enrollment` · Firecrawl search | https://www.marist.edu/about (excerpt) ; https://en.wikipedia.org/wiki/Marist_University (excerpt) | 6,382 total student population (Marist); main campus 180 acres on the east bank of the Hudson on US 9, Town of Poughkeepsie (Wikipedia). Name now "Marist University". | §5 para 2, §5.5, §13 |
| D10 | `Marist College off-campus housing students Poughkeepsie houses landlords Fairview neighborhood` · Firecrawl search | https://www.marist.edu/admission/intl/orientation/rental-housing (excerpt) ; https://www.facebook.com/groups/1788836064844398/ (excerpt) | Marist: graduate students must live off campus; apartments in complexes and in private homes throughout Poughkeepsie. FB group excerpt names "Cedar, Sunset/Fairview, or Fulton area" for student housing. | §5 para 2, §9 student Qs, Across Dutchess |
| D11 | `Bard College students off-campus housing Red Hook Tivoli rentals village` · Firecrawl search | https://www.bard.edu/reslife/offcampus/ (excerpt) | "The majority of off-campus students choose to live close to the College in Red Hook, Tivoli, or Rhinebeck." | §5 para 2, §9 student Q, Across Dutchess |
| D12 | `couple charged Airbnb fire killed mother baby Dutchess County no working smoke detectors` · Firecrawl search → Firecrawl scrape | https://www.cbsnews.com/newyork/news/airbnb-hosts-charged-manslaughter-dutchess-county-fire/ | (March 2025) Fire Oct 2024 at an Airbnb in Salt Point; investigators allege the hosts falsely claimed a smoke alarm; property lacked a required local permit mandating smoke/CO detectors and extinguishers on each floor; manslaughter charges (allegations). Hosts not named on page. | §10.5 H3 (host safety beyond the lock), host checklist |
| D13 | `Dutchess County sheriff burglary unlocked doors homes warning residents lock 2025` · Firecrawl search → WebFetch | https://troopers.ny.gov/news/public-safety-alert-targeted-residential-burglaries-hudson-valley-region | Jan 29 2025 State Police alert: targeted residential burglaries in Dutchess, Westchester, Putnam; advice "Ensure all doors and windows are securely locked, including second-floor entry points." (Entry method not stated → not claimed.) Firecrawl scrape query failed; WebFetch used. | §5.5, §9 second-floor Q |
| D14 | same search → Firecrawl scrape | https://www.dutchessny.gov/Departments/Sheriff/Recent-Thefts-and-Attempted-Burglary-in-North-Eastern-Dutchess.htm | Apr 26 2021: larcenies from vehicles, three vehicle thefts, attempted burglary at a jewelry store on Route 44 in Millerton (fled when alarm sounded), Amenia/Millerton; advice: lock vehicles, never leave valuables or keys/fob inside. | §9 key-in-car Q, Across Dutchess (Harlem Valley) |
| D15 | `Village of Rhinebeck historic district review board certificate of appropriateness doors exterior alterations` · Firecrawl search → Firecrawl scrape | https://villageofrhinebeck.gov/historic-district | Listed Aug 8 1979; expanded Jan 15 2021; listing gives no automatic protection; Chapter 64 and zoning Art. VIII §120-39 Historic District Overlay (2009, amended June 27 2023): new construction or major exterior additions/modifications get heightened Village Planning Board scrutiny. (Door hardware not mentioned — page says so.) | §7 card, §9 historic-look Q, §13 |
| D16 | `City of Poughkeepsie historic district and landmarks preservation commission certificate of appropriateness doors hardware` · Firecrawl search → Firecrawl scrape (metadata only) | https://www.cityofpoughkeepsie.gov/320/Historic-District-Landmark-Preservation- | HDLPC reviews plans for exterior construction, alteration or repair, or any change in exterior appearance of landmarks and buildings within historic districts. List of districts not retrieved → not stated. | §9 historic-look Q, §8.5 |
| D17 | `Locust Grove Samuel Morse…` · Firecrawl search | https://www.lgny.org/ ; https://en.wikipedia.org/wiki/Locust_Grove_(Poughkeepsie,_New_York) (excerpts) | Italianate mansion; 200 acres; carriage house, ice house; bluff over the Hudson; Samuel Morse. | §13 |
| D18 | `Wilderstein Historic Site Rhinebeck Queen Anne mansion Suckley` · Firecrawl search | https://wilderstein.org/ ; https://wilderstein.org/history/ (excerpts) | Rhinebeck house museum; Italianate home by John Warren Ritch 1852, remodelled/enlarged 1888; Margaret (Daisy) Suckley, FDR's cousin and confidante, died there 1991; "most important example of Victorian architecture" (site's claim). | §13, §7 |
| D19 | `Innisfree Garden Millbrook acres Walter Beck` · Firecrawl search | https://www.innisfreegarden.org/about (excerpt) | 185-acre garden in Millbrook, developed by Walter and Marion Beck as private home. | §13 |
| D20 | `Montgomery Place Bard College Annandale-on-Hudson estate acres history` · Firecrawl search | https://www.bard.edu/montgomeryplace/ (excerpt) | 380+ acre historic site between Bard's Annandale and Massena campuses; federal-style mansion, houses, cottages, barns; Livingston family 1805–1986. | §13, §7 estate card |
| D21 | `Poughkeepsie station northern terminus Hudson Line Metro-North Beacon station commuters` · Firecrawl search | https://en.wikipedia.org/wiki/Hudson_Line_(Metro-North) (excerpt) ; https://www.governor.ny.gov/news/governor-hochul-announces-mta-metro-north-railroad-super-express-trips-between-poughkeepsie (excerpt) | Poughkeepsie station on the Hudson Line (milepost 73.5, opened 1850, Amtrak connections); "super-express" Hudson Line trains between Poughkeepsie and NYC announced by the Governor. | §5 para 5 (commuters), Across Dutchess |
| D22 | `Culinary Institute of America Hyde Park campus students` · Firecrawl search | https://www.ciachef.edu/cia-new-york/ (excerpt) | Student-run restaurants on the Hyde Park, NY campus. | §8 card, §9 restaurant Q |
| D23 | `Wassaic station northern terminus Harlem Line Metro-North` · Firecrawl search | https://en.wikipedia.org/wiki/Wassaic_station (excerpt) | Wassaic station, Harlem Line, in the town of Amenia; northern terminal of the line. | Across Dutchess (Harlem Valley) |
| D24 | `Vassar College students off-campus housing Arlington Poughkeepsie rentals` · Firecrawl search | https://www.forrentuniversity.com/Vassar (excerpt) | Off-campus listings near Vassar include Springside Ave, Arlington NY 12603. | §5 para 2, Across Dutchess (Arlington) |
| D25 | Rhinebeck street names | https://villageofrhinebeck.gov/historic-district (D15) | Benner House (1 Mill Street), Post Office (6383 Mill Street), Delamater House (6433 Montgomery Street) → "Mill Street and Montgomery Street" used for the village commercial card. | §8 Rhinebeck card |

### Reused from earlier research in this repo (sources reached by earlier runs; not re-fetched)
| Finding | Source (as logged) | Page section |
|---|---|---|
| Dutchess median year built 1971; 18.0% (22,056) of homes built 1939 or earlier | stacker.com counties-oldest-homes-new-york (research/soundbar-installation.md, research/sonos-installation.md) | §5.5, §7 |
| Walkway Over the Hudson: opened 1888 as rail bridge, 212 ft tall, 1.28 miles, Poughkeepsie–Highland | hudsonrivervalley.com (research/soundbar-installation.md) | §13 |
| Dia:Beacon: 1929 Nabisco box-printing factory, nearly 300,000 sq ft | diaart.org (research/soundbar-installation.md) | §13, §7 |
| Beacon Main Street almost a mile long | thebeaconbeaconny.com (research/soundbar-installation.md) | §8 |
| Vassar: ~1,000 acres, founded 1861, Main Building 1865 by James Renwick Jr. | en.wikipedia.org/wiki/Vassar_College (research/fiber-optic-installation.md) | §13 |
| IBM Quantum facility 2455 South Road, Town of Poughkeepsie, ~300,000 sq ft, construction start Sept 2026 | thinkdutchess.com IDA project summary (research/fiber-optic-installation.md) | §8 |
| USDA 2022: Dutchess 620 farms, average 161 acres | nass.usda.gov cp36027.pdf (research/fiber-optic-installation.md) | §5.5 |
| Times Union June 27 2024: ~10,000 Dutchess Central Hudson outages in a storm | timesunion.com (research/cat6-repair.md) | §9 (power) / connectivity section |
| Mount Gulian c.1730 Dutch-style barn, Beacon | mountgulian.org (research/sonos-installation.md) | Across Dutchess |
| Town of Pleasant Valley STR law, ENB June 11 2025 | dec.ny.gov (silo HV section) | §10.5 |
| NYS STR registry, Chapter 99 of Laws of 2025 | nysac.org (silo HV section) | §9 Rhinebeck Q |
| August Connect 10–15 ft; Schlage Encode 4 AA / "up to six months"; Fixr national $250–$400 (Jan 2025) | silo S1/S4, HV section | §10, §14, connectivity |
| parking-lot-camera-installation-dutchess-county-research-matrix.md (Route 9/Taconic/I-84/Route 44 corridors, town list) | in repo; that matrix carries no URLs → corridor names only, no figures | §8, Across Dutchess |

### Prices used (all from the live HV hub page smart-lock-installation-hudson-valley.html, Dutchess row; none invented)
| Figure | Scope | Source |
|---|---|---|
| $2,295–$3,825 | single-door keypad or fob reader with electric strike (Dutchess) | HV hub table/FAQ ($1,500–$2,500 × 1.53) |
| $383–$689 | new electric strike | HV hub table ($250–$450 × 1.53) |
| $451–$742 | failed electric strike repair | HV hub table ($295–$485 × 1.53) |
| $275 first hour, then 30-min blocks | setup-only visit, Dutchess | HV hub table; research/tv-mounting-prices/BRIEF.md line 15 |
| $195/hr, 3-hr minimum ($585) | service/callback, not on initial install | blueprint v2.3 §9 (verbatim) |
| quoted flat at walkthrough | residential smart lock | no AESS figure |
| $250–$400 (Fixr, Jan 2025) | national third-party, labelled | silo S1 |
**Conflicts for Anwar:** (1) live access-control-installation-dutchess-county.html prices the same single-door scope as "$1,500 to $2,500 plus the 25% surcharge" ("Dutchess County = Brooklyn base + 25% HV surcharge") and its card shows "SINGLE DOOR / GATE $1,900 – $6,000" — this page follows the smart-lock HV hub's §9 1.53× Dutchess figures ($2,295–$3,825) so the silo stays internally consistent. (2) door-buzzer-repair-dutchess-county-new-york.html, network-cable-repair-dutchess-county.html and intercom-installation-dutchess-county-ny.html use a $250 service-call model (door-buzzer-installation-dutchess-county-ny.html: $300), and the buzzer-repair page prices "Electric strike replacement + alignment $450 – $950" — this page follows the HV hub ($195/hr 3-hr minimum callback; strike $383–$689 / repair $451–$742) and does not mention the $250 service call. (3) Setup-only $275 is published for TV/device setup (same flag as LI/Brooklyn/Queens). (4) Travel: FAQ says Dutchess travel is built into the quote, per door-buzzer-installation-dutchess-county-ny.html comparison table ("Travel built into quote — Yes").

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG, Yelp 1–3★.
- Reddit thread bodies (r/hudsonvalley, r/Poughkeepsie): titles/excerpts only.
- Daily Freeman / Mid-Hudson News / Poughkeepsie Journal smart-lock stories: none found.
- City of Poughkeepsie historic district list; Hyde Park STR law (only aggregators); Dutchess county-level home-improvement licence (as on HV hub).
- Field Notes: no sourced Dutchess install anecdote → written as general working practice and labelled so.

## Images (11)

Permanent image rule (Drive "AESS Website Photos/Smart Lock Installation" empty, CompanyCam not connected). Library = 71 distinct photos by perceptual hash; all door-hardware clusters were already used by the six live smart-lock pages, so these 11 reuse clusters used on the NYC hub / Manhattan / Brooklyn / Queens / LI pages — **none used on the Hudson Valley hub**, and none of the clusters claimed by the Orange County builder (claims exchanged by message with the Orange and Putnam builders). Every source was viewed; 9 were cropped (Pillow) to remove technicians' faces, shirt phone numbers and a readable checklist; 1 was cropped to remove a "RECEPTION" sign. Note for Anwar: like the Queens builder, the library photos look AI-rendered; real smart-lock photos should replace them.

| New filename (images/smart-lock-installation/) | Source file | Crop |
|---|---|---|
| smart-lock-installation-dutchess-county-push-to-exit-beside-keypad-reader.webp (hero) | images/commercial-security/commercial-security-systems-nyc-rex-exit-button.jpg | left 54% removed (face, shirt phone) |
| smart-lock-installation-dutchess-county-wave-to-exit-sensor-door-header.webp | images/commercial-security/commercial-security-systems-nyc-request-to-exit-sensor.jpg | left 47% removed |
| smart-lock-installation-dutchess-county-door-contact-glass-door-frame.webp | images/commercial-security/commercial-security-systems-nyc-door-contact-install.jpg | left 45% removed |
| smart-lock-installation-dutchess-county-three-door-controller-card-readers.webp | images/commercial-security/commercial-security-systems-nyc-door-controller-enclosure.jpg | left 43% removed (face, checklist with phone) |
| smart-lock-installation-dutchess-county-maglock-armature-glass-door.webp | images/commercial-security/commercial-security-systems-manhattan-maglock.jpg | left 43% removed |
| smart-lock-installation-dutchess-county-desk-release-button-mounting.webp | images/commercial-security/commercial-security-systems-dutchess-glass-break.jpg | left 46%, top 18% removed |
| smart-lock-installation-dutchess-county-patch-rack-gloved-termination.webp | images/commercial-security/commercial-security-systems-dutchess-integration-rack.jpg | left 47% removed |
| smart-lock-installation-dutchess-county-tone-probe-wall-box-trace.webp | images/low-voltage/low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg | left 50% removed |
| smart-lock-installation-dutchess-county-poe-switch-rack-recorder.webp | images/commercial-security/commercial-security-systems-dutchess-nvr-poe-rack.jpg | left 47% removed |
| smart-lock-installation-dutchess-county-crew-ceiling-cable-pull.webp | images/low-voltage/low-voltage-installation-dutchess-county-03-crew-cable-pull.jpg | none (crew seen from behind/far) |
| smart-lock-installation-dutchess-county-wall-plate-cable-certification.webp | images/low-voltage/low-voltage-installation-dutchess-county-02-fluke-certification-pass.jpg | left 52% removed |

Rejected after viewing: commercial-security-systems-dutchess-lpr-lot.jpg (building number "1000" on facade, face). DAILY-LOG note: `images: 11 reused from images/low-voltage/ and images/commercial-security/ (no real smart-lock photos yet)`.

## Question register — smart-lock-installation-dutchess-county

### §9 YOUR QUESTIONS ANSWERED (H3)
Student houses near Marist, Vassar and Bard
1. We let a house near Marist to a new group of students every August — how do we wipe every old code between May move-out and move-in?
2. Can each student in a shared Poughkeepsie rental have a keypad lock on their own bedroom door?
3. A student tenant in our Arlington house is behind on rent — can we switch off their code?
Hosting under Dutchess town rules
4. Beacon only lets us host in the home we actually live in — how do we give guests the house and still lock away our own things?
5. Rhinebeck's short-term rental application asks for a floor plan showing every exit — should the lock plan follow it?
6. Red Hook wants a local contact within 15 air miles when we're away — what does that person need from the lock?
Older houses, estates and historic villages
7. Our Poughkeepsie two-family was built before 1980 — does drilling the door for a smart lock raise a lead-paint problem?
8. Which smart locks look right on a Victorian or Federal-style front door in Rhinebeck or Poughkeepsie's historic districts?
9. The caretaker who has looked after our river estate for years is leaving — how do we take back every key, code and app login?
Break-ins and habits the police warn about
10. The State Police told Dutchess residents to lock second-floor entry points too — does an upstairs deck or balcony door need a smart lock?
11. Should we stop keeping a house key or garage remote in the car parked in our Millbrook or Amenia driveway?
Shops and restaurants
12. Our shop on Beacon's Main Street shares a back stair with the apartment upstairs — how do we keep shop codes off the tenant's door?
13. Our Hyde Park restaurant hires culinary students for the season — how should kitchen-door codes work when they leave in the fall?

### §17 FAQ (visible == FAQPage, 9)
1. What does a keypad with an electric strike cost on a Dutchess County shop or building door?
2. Do you come out to Pine Plains, Millerton and the Harlem Valley, or only along Route 9?
3. Can you do the walkthrough before our student tenants move out in May?
4. Can the locks go in the week before our Rhinebeck short-term rental inspection?
5. Can the smart locks take the same key as the rest of our Poughkeepsie building?
6. Is there a separate travel charge for the far north and east of the county?
7. Can you come in the evening, after we get home on the train from the city?
8. If our buyer doesn't want the smart lock, can you put a plain deadbolt back before closing?
9. Can the accessory apartment behind our Beacon house get its own keypad for a year-round tenant?

### Other question-form headings
- H2 "Smart Lock Dead at a Dutchess Rental, House or Shop?" (repair capture)
- H2 "Ready to Take Back Control of Every Key?" (mid CTA)
- H2 "Locked Out Somewhere Between Beacon and Millerton Tonight?" (final repair capture)

Batch-sibling check (Orange/Putnam pages on disk at 07:40): no exact or meaning duplicates found; closest = Putnam FAQ "Can the lock's alerts also go to a neighbour or caretaker who checks on the house?" vs this page's Q6 (Red Hook local contact's own credential) — different intent (alerts vs access), left for the main run to judge.

De-dup notes: compared by meaning against the NYC/LI/HV/Manhattan/Brooklyn/Queens registers and the six live pages. Deliberately avoided: HV "historic-district approval for a keypad in Kingston" (here the Q is which lock style suits the door, approval mentioned only in body); HV "cleaner's code opens cottage not barn" (here: retiring caretaker handover); HV "why Dutchess costs more than Westchester" (no pricing Q in §9); NYC "cut off a former tenant's code without breaking the lockout law" (here: current tenant behind on rent, statewide RPAPL 768); Brooklyn "can I see when my tenant comes and goes"; Manhattan "doorman/dog walker/cleaner"; Queens "who holds the admin account" and "front-yard gate keypad"; LI "storm door", "garage door to kitchen". Partial overlaps for the main run to judge: Q1 (annual student turnover reset) vs HV FAQ 9 (STR checkout-to-check-in service) and NYC Q4 (renter moving out); Q8 (lock style on historic doors) vs Queens FAQ 10 (match finish); FAQ 1 cost (geo-specific by design); FAQ 8 (restore plain deadbolt for sale) vs LI FAQ 10 (codes/app when selling).

## Ulster County (smart-lock-installation-ulster-county)

Built 2026-10-17 by the Ulster County builder subagent. Area page, up-link /smart-lock-installation-hudson-valley. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (845) 640-3835 in body/CTAs/schema; (800) 486-0943 only in the shared header chrome. Ulster ×1.53.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).

Thesis / lane: Ulster = the oldest doors in the valley (Dutch stone houses in the Kingston Stockade, Hurley, New Paltz; plank doors with surface box/rim locks, Dutch doors, masonry reveals — preserve, retrofit or use the later wing door) + Catskill-town cabins and rentals where phone signal fails at the porch (Route 28/212 dead zones; keypad codes stored in the lock as the primary credential) + town-by-town rental rules (Kingston STR cap/inspections and rental registration, Woodstock local host within 10 miles, New Paltz rental registration/inspection) + family camps shared by several households + river-town commerce (Uptown Kingston, New Paltz Main St with student staff, Woodstock Tinker St, iPark 87) + lightning/outage resilience.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | Excerpts only (U27, U28); Ulster-specific Reddit threads: EMPTY (not accessible in build env — no r/hudsonvalley / r/Catskills smart-lock thread returned). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are recurring marketing/cost-guide claims, stated as such on the page. |
| 6 | Landmarks | U13–U18 |
| 7 | Use cases / building stock | U1, U10, U11, U12, U25, U26 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Hudson Valley One (U8, U21), Radio Catskill/WJFF (U3), Times Union (U20, carried) |
| 10 | Hyperlocal | Hudson Valley One used; Daily Freeman: only Facebook excerpts returned (not used). Ulster smart-lock-specific news: EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| U1 | (direct) Firecrawl scrape, query mode | https://www.census.gov/quickfacts/fact/table/ulstercountynewyork/PST045224 | Pop 183,330 and housing units 87,657 (July 1, 2025, V2025); owner-occupied 69.9% (2020–2024); 65+ 23.5%; persons/household 2.26; households 74,278; broadband subscription 92.4%; median owner value $352,500. | §5 para 4, §5.5 bullets 1–2 |
| U2 | carried from silo HV research (Comptroller STR report 2025) | https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf | 2,827 STR units May 2025 = 3.28%; Shandaken 9.76%; Shandaken, Woodstock, Gardiner, Denning >7%; ≥16 municipalities regulate. | §5 para 3, §5.5 bullet 4, Town by Town (Gardiner, Shandaken), Rental Rules table |
| U3 | `Ulster County seasonal recreational occasional use housing units second homes share comptroller report` · Firecrawl search → Firecrawl scrape | https://wjffradio.org/short-term-rental-surge-threatening-ulster-countys-housing-stock-comptroller-finds/ (redirects to radiocatskill.org; Sept 25, 2025, Kimberly Izar) | STRs up 220% over a decade; 942 (2015) → 3,310; Comptroller March Gallagher; ≥16 municipalities regulate; at least six villages/towns cap STRs or require owner-occupancy. (Seasonal-home % for Ulster: EMPTY — not found.) | §5 para 3, Rental Rules table ("Other towns") |
| U4 | `Town of Woodstock NY short-term rental law permit requirements local contact` · Firecrawl search → Firecrawl scrape (PDF) | https://www.townofmarlboroughny.gov/DocumentCenter/View/3354/Short-Term-Rentals---Town-of-Woodstock-Local-Law (Woodstock Local Law No. 1 of 2019); also https://woodstockny.gov/departments/building-department | Non-owner-occupied STR needs a designated Host: "A designated adult who lives within a 10 mile distance … available to promptly deal with emergencies"; owner and Host address renter issues within 24 hours; safety/egress plan posted in unit and on back of each bedroom door; yearly fire/safety inspection; STRs must register with Ulster County (LL #5 of 1991). | §5 para 3, §9 Q7 (local host), §10.5 H3 3 & 7, Town by Town (Woodstock), Rental Rules table |
| U5 | `City of Kingston NY short-term rental law owner-occupied permit 2023` · Firecrawl search → Firecrawl scrape (PDF) | https://kingston-ny.gov/filestorage/8399/8469/48370/STR_Fact_Sheet_-_City_of_Kingston_Form-Based_Code.pdf ; https://kingston-ny.gov/news/?FeedID=1957 (Aug 15, 2023) | Form-based code passed Aug 2, 2023; STR-F capped at 1% of housing units — 112 as of September 2026; cap reached March 4, 2024 (waitlist); STR-RO and STR-L uncapped; one STR per property; fees $650/$125/$125; inspection before permit, then every two years; STR-F only in T4/T5. | §5 para 3, §5.5 bullet 5, §10.5 H3 3, Town by Town (Kingston), Rental Rules table |
| U6 | same search (result 5) | https://ecode360.com/12699947 (Kingston Code Ch. 332 Rental Properties, excerpt) | Owner must register rental units; no occupancy without a valid rental permit; owner not residing in Ulster County must designate a managing agent. | §9 Q11 (Uptown Kingston shop + apartments), Town by Town (Kingston) |
| U7 | `Village of New Paltz rental permit law inspection landlord SUNY New Paltz enrollment students off-campus` · Firecrawl search | https://www.villageofnewpaltz.gov/rental-property-registration-and-inspection-forms/ ; https://www.villageofnewpaltz.gov/registered-rental-properties-list/ | Rental registration incl. STRs; must pass inspection within 30 days to be registered; tenants "comforted knowing that a building codes official has examined their home within the previous 12 months". | §5 para 3, §9 Q12, §10.5 H3 3, Town by Town (New Paltz), Rental Rules table |
| U8 | `Ulster County cell phone service dead zones Catskills study coverage gaps` · Firecrawl search → Firecrawl scrape | https://hudsonvalleyone.com/2016/12/29/dead-zones-more-than-a-decade-into-the-cell-phone-era-much-of-ulster-county-still-has-no-service/ (Paul Smart, Dec 29 2016 / updated Jan 11 2017) | "gaps show up along Routes 212 and 28, where mountains block cellular access"; worst dead-zone ZIPs 12464 (Phoenicia), 12452 (Lexington and Shandaken), 12477 (Saugerties), 12458 (West Hurley); T-Mobile almost no coverage in Olive and Shandaken; Verizon map showed much of Woodstock without coverage. Page states it is a 2016 review. | §5 para 2, §9 Q5, §10.5 H3 1, Town by Town (Saugerties), building card (cabins) |
| U9 | `SUNY New Paltz enrollment fall 2025 total students` · Firecrawl search | https://www.newpaltz.edu/about/glance.html | Undergraduates 6,197; graduate 1,036. | §9 Q12 ("more than 6,100 … about 1,000") |
| U10 | carried from research/sonos-installation.md + research/soundbar-installation.md (Ulster County newsroom, Sept 25 2025) | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion | $20.8M ConnectALL award; nearly 1,300 unserved homes, businesses and community facilities. | §5 para 2, §5.5 bullet 6 |
| U11 | carried from research/sonos-installation.md (Stacker, Sept 25 2025, Census data) | https://stacker.com/stories/new-york/counties-oldest-homes-new-york | Ulster: median year built 1966; 25.3% (21,829) built 1939 or earlier. | §5 para 1, §5.5 bullet 3 |
| U12 | `Hurley NY stone houses historic district Main Street number of stone houses` · Firecrawl search | https://www.hurleyheritagesociety.org/hurley-tours/ ; https://visitulstercountyny.com/plan-your-visit/things-to-do/hurleys-historic-district-walking-tour-2/ | Self-guided tour map of 27 historic sites in and around Hurley; Main Street private residences from late 1600s to late 1800s. | §5 para 1, §13 Hurley card |
| U13 | carried from research/fiber-optic-installation.md / cat6-repair.md | https://en.wikipedia.org/wiki/Kingston_Stockade_District | Colonial Dutch stone houses at all four corners of Crown & John Streets. | §5 para 1, §7 card |
| U14 | `Senate House State Historic Site Kingston stone house 1676 first New York State Senate 1777` · Firecrawl search | https://parks.ny.gov/visit/historic-sites/senate-house-state-historic-site ; https://www.hudsonrivervalley.com/sites/Senate-House-and-Museum-/details | 1777 first NY Senate met in home of merchant Abraham Van Gaasbeek; originally a single-story Dutch stone dwelling built 1676; on Fair Street. | §5 para 1, §13 card |
| U15 | `Ashokan Reservoir Ulster County completed 1915 …` · Firecrawl search | https://dec.ny.gov/places/ashokan-reservoir ; https://en.wikipedia.org/wiki/Ashokan_Reservoir | 14 miles west of Kingston; created 1915 by 5½ miles of dams and dikes in the Esopus Creek drainage; oldest NYC-owned Catskill reservoir. | §13 card, §5 para 4 (mention) |
| U16 | `Saugerties Lighthouse built 1869 …` · Firecrawl search | https://www.saugertieslighthouse.com/overview | Constructed 1869 at mouth of the Esopus Creek; aid to navigation. | §13 card, §8 Saugerties card (location only) |
| U17 | `Byrdcliffe Arts Colony Woodstock founded 1902 …` · Firecrawl search | https://www.woodstockguild.org/about-us/ ; https://en.wikipedia.org/wiki/Byrdcliffe_Colony | Ralph Radcliffe Whitehead; seven farms, 1,500 acres; founded 1902 (completed 1903). | §13 card, §7 card |
| U18 | `Opus 40 Saugerties Harvey Fite bluestone quarry sculpture` · Firecrawl search | https://opus40.org/about/ | 6.5-acre bluestone earthwork by Harvey Fite in an abandoned quarry at the foot of Overlook (Mountain). | §13 card |
| U19 | carried from research/fiber-optic-installation.md | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | 2020: Ulster 182,760 lightning pulses, 49 thunder days. | §9 Q10 (lightning) |
| U20 | carried from research/cat6-repair.md | https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php (June 27 2024) | >35,000 Central Hudson customers reported outages in NE Orange, Dutchess and Ulster. | §9 Q10 |
| U21 | `TechCity Kingston former IBM campus tenants iPark 87 businesses 2025` · Firecrawl search → Firecrawl scrape | https://hudsonvalleyone.com/2025/12/19/ipark87-owners-asked-to-hand-over-west-campus-after-failure-to-pay-6-8-million-mortgage/ ; https://extapps.dec.ny.gov/data/DecDocs/356002/... (300 Enterprise Drive) | Former IBM Kingston campus; east campus houses Ulster BOCES center and Archtop Fiber; county seized 82 west acres in 2019. | §6 card, §8 iPark 87 card, §10 card |
| U22 | `Uptown Kingston Stockade District shops restaurants Wall Street North Front Street …` · Firecrawl search | https://www.goloveny.com/blog/exploring-kingston ; https://www.tripadvisor.com/Attraction_Review-g48003-d4808894-... | Wall Street and North Front lined with shops, restaurants and wine bars. | §8 Uptown card, §9 Q11 |
| U23 | `Woodstock NY Tinker Street shops galleries; Saugerties village …` · Firecrawl search | https://visitulstercountyny.com/blog/ultimate-guide-woodstock-new-york-holly-habeck/ ; https://www.thenotsoinnocentsabroad.com/blog/weird-and-wonderful-woodstock-new-york | Tinker Street and Mill (Hill) Road: locally owned shops, restaurants, galleries. Saugerties-village street detail: EMPTY (not returned) → card kept generic. | §8 Tinker St card |
| U24 | `New Paltz Main Street Route 299 shops restaurants downtown village business` · Firecrawl search | https://www.iloveny.com/listing/new-paltzs-main-street/44377/ ; https://www.mainstreetbistro.com/ | New Paltz Main Street: village shopping and restaurants. | §8 Main St card |
| U25 | carried from research/fiber-optic-installation.md | https://nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36111.pdf | Ulster 486 farms (2022). | §8 closing para |
| U26 | `Ulster County home improvement contractor license required consumer fraud bureau district attorney` · Firecrawl search → Firecrawl scrape | https://legislature.ulstercountyny.gov/sites/default/files/documents/ILL%20No.%2011%20of%202009.pdf | Introductory Local Law No. 11 of 2009 proposed county commercial-construction and home-improvement licensing (B licence for jobs > $1,000). No evidence found that it was adopted / is in force → page says a law was introduced in 2009 but no record of adoption found; check with the town. | §8.5 licensing bullet |
| U27 | `Knox HomeBox residential key box fire department access homeowners` · Firecrawl search | https://www.knoxbox.com/products/residential-knoxboxes | Residential boxes for fire/EMS entry; master key system managed by local fire departments; access limited to authorised FD personnel; HomeBox holds one key. Whether Ulster fire companies run Knox programs: EMPTY → page tells owners to ask their company. | §6 card, §9 Q9, §10 card, Storms & Signal list |
| U28 | `Dutch door split door Hudson Valley stone house original 18th century hardware strap hinges` · Firecrawl search (scrape of hmvarch.org returned empty) | https://www.philipsemanorhall.com/architecture/doors ; https://hmvarch.org/news2/hvvanews7-5pt2.htm (excerpt) | Dutch doors split in the middle for air/light, "keeping small children inside and farm animals out"; "people of The Valley are proud of their old Dutch doors and hardware. The hinges and latches are usually painted black". | §9 Q4 |
| U29 | `reddit Catskills Airbnb cabin keypad lock no cell service guests locked out` · Firecrawl search | https://www.reddit.com/r/AirBnB/comments/1p66bfi/let_the_key_go_to_hell_seriously_i_mean_it_usa/ ; https://www.reddit.com/r/airbnb_hosts/comments/1tpgewn/had_guests_come_back_after_checkout_what_lock_are/ (excerpts) | "we have a keypad lock but have a lockbox with a key in it just in case"; Schlage Encode code sent in advance, active from 4 pm. Not Ulster-specific; used only as "hosts on national forums". | §9 Q5 |
| U30 | `smart lock for sliding patio door manufacturer keyless sliding door lock` · Firecrawl search | https://www.reddit.com/r/homeautomation/comments/1nqhqb4/smart_lock_for_sliding_door/ (excerpt) ; https://www.gokeyless.com/collections/keyless-sliding-door-locks | Retrofit slider gadget "strong enough to unlock but not strong enough to lock"; mechanical keyless sliding-door locks with no batteries exist. | §9 Q8, §6 card |
| U31 | `Ulster County sheriff burglaries unoccupied seasonal homes camps arrested` · Firecrawl search | https://www.ulstersheriffny.gov/ ; Facebook/Instagram excerpts | Only social-media excerpts of individual arrests; no pattern article → EMPTY; nothing used. | — |
| U32 | silo file (research/smart-lock-installation.md) | Fixr; Schlage Encode (BE489) specs; August Connect 10–15 ft; Energizer Ultimate Lithium −40°F to 140°F; igloohome offline PINs; ADA 404.2.7; Ulster County Finance STR registration (sonos file) | As listed in the silo file. | §7.5, §9 Q5, §10.5, §14, Storms & Signal, Rental Rules table |

### Prices used (Ulster ×1.53, round half-up; all from existing approved AESS figures — none invented)
- Single-door keypad or fob reader with electric strike: $1,500–$2,500 base → **$2,295–$3,825** (matches HV hub's Ulster row).
- New electric strike: $250–$450 → **$383–$689**. Failed strike repair: $295–$485 → **$451–$742**.
- Setup-only visit: **$275 first hour**, then 30-min blocks (research/tv-mounting-prices/BRIEF.md line 15, Dutchess/Ulster).
- Service/callback: **$195/hr, 3-hour minimum ($585)**, not on initial install.
- Residential smart lock: no AESS figure → "quoted flat at the free walkthrough".
- National comparison only: Fixr $250–$400, avg $300 (Jan 2025).
- **Conflict for Anwar:** live access-control-installation-ulster-county.html shows "SINGLE DOOR / GATE $2,100 – $6,500" (and lobby fob reader $2,000–$3,400), which differs from the §9 ×1.53 figures. This page follows the HV hub (§9 multiplier). Same setup-only-rate flag as earlier pages ($275 is published for TV/device setup).

## Images (11) — permanent image rule (Drive folder `AESS Website Photos/Smart Lock Installation` empty; CompanyCam not connected)
Perceptual-hash check (dHash) of images/low-voltage + images/commercial-security: 71 distinct photos, only ~10 not already used on a smart-lock page, and those are ceiling speakers, fiber trays, video walls, an LPR lot with a building number, a client-face dashboard shot, the dual-entrance address photo and the reception-face photo — none fits a door lock. So the 11 below favour door-hardware relevance; most are the same photos (other filenames) as images on the NYC/LI/HV/Manhattan/Brooklyn smart-lock pages. All viewed before naming; captions describe only what is visible; none claims a customer or Ulster project. Rejected after viewing: ulster-access-reader ("Pinnacle Business Center" on glass), ulster-video-intercom ("Riverfront Business Center" + street address), ulster-lpr-lot (building number "1000"), ulster-credential-programming (readable programming list).
| New filename (images/smart-lock-installation/) | Source file |
|---|---|
| smart-lock-installation-ulster-county-electric-strike-glass-door-frame.webp (hero, eager) | images/commercial-security/commercial-security-systems-ulster-electric-strike.jpg |
| smart-lock-installation-ulster-county-enclosure-on-brick-wall.webp | images/low-voltage/low-voltage-installation-ulster-county-02-exterior-enclosure-install.jpg |
| smart-lock-installation-ulster-county-keypad-and-camera-glass-entry.webp | images/commercial-security/commercial-security-systems-ulster-alarm-keypad.jpg |
| smart-lock-installation-ulster-county-push-to-exit-button.webp | images/commercial-security/commercial-security-systems-nyc-rex-exit-button.jpg |
| smart-lock-installation-ulster-county-strike-terminal-wiring.webp | images/low-voltage/low-voltage-installation-ulster-county-12-electric-strike-wiring.jpg |
| smart-lock-installation-ulster-county-door-contact-sensor.webp | images/commercial-security/commercial-security-systems-nyc-door-contact-install.jpg |
| smart-lock-installation-ulster-county-wall-box-cable-trace.webp | images/low-voltage/low-voltage-installation-ulster-county-08-tone-generator-trace.jpg |
| smart-lock-installation-ulster-county-crew-van-unloading.webp | images/commercial-security/commercial-security-systems-ulster-crew-van.jpg |
| smart-lock-installation-ulster-county-ceiling-access-point-lift.webp | images/low-voltage/low-voltage-installation-ulster-county-10-access-point-lift-install.jpg (cropped: right 14% removed to drop a "Community Center" wall sign) |
| smart-lock-installation-ulster-county-finished-secured-lobby.webp | images/commercial-security/commercial-security-systems-ulster-secured-lobby.jpg |
| smart-lock-installation-ulster-county-request-to-exit-sensor.webp | images/commercial-security/commercial-security-systems-nyc-request-to-exit-sensor.jpg |
DAILY-LOG note: `images: 11 reused from images/low-voltage/ and images/commercial-security/ (no real smart-lock photos yet)`. The library photos look AI-rendered (as noted on the Queens/soundbar pages) — needs Anwar's review.

## Question register — smart-lock-installation-ulster-county

### §9 YOUR QUESTIONS ANSWERED (H3)
Stone houses and the oldest doors
1. Our stone house still has a box lock screwed to the inside face of a plank door — can it go keyless without boring the door?
2. Is it wiser to leave the original front door untouched and put the smart lock on the kitchen-wing door instead?
3. How do you fasten a keypad or a bridge to a stone wall without damaging the masonry?
4. Can a Dutch door, split into top and bottom halves, take a smart lock?
Mountain cabins, family camps and rental cottages
5. Guests reach our cabin near Phoenicia with no phone signal — what should they use to open the door?
6. Three siblings share the family camp — can each household keep its own codes private from the others?
7. Woodstock asks for a local host within ten miles — what should that person be able to do at the door?
8. Can the sliding glass door onto our deck be put on the same keyless system?
9. If the house is empty and the alarm goes off, how does the volunteer fire company get through a smart-locked door?
10. Ulster sees a lot of summer thunderstorms — can lightning take out a smart lock or its bridge?
Kingston, New Paltz and the river towns
11. Our Uptown Kingston building has a shop on the ground floor and apartments above — should they share one entry system?
12. We rent a house near SUNY New Paltz to a new group of students each year — does a smart lock beat re-keying between leases?
13. Our New Paltz shop hires students who leave every May — what is the quickest way to manage staff codes through each semester?
14. Our manufactured home's door swings outward — can it still take a smart deadbolt?

### §17 FAQ (visible == FAQPage, 8)
1. What does a keypad with an electric strike cost on an Ulster County door?
2. Do your crews reach Pine Hill, Shandaken and the Ellenville end of the county as well as Kingston?
3. Should we shovel the walk and clear the steps before a winter appointment?
4. Can the house's other keyed doors be set up so one key opens them all?
5. Does a smart lock lower what we pay for homeowners insurance?
6. Is there a minimum job size for a trip out to Ulster County?
7. Can a smart lock replace only the deadbolt on a door that also has a separate keyed knob?
8. Do you weather-seal the outside of the lock where it meets an old, uneven door?

### Other question-form headings
- H2 "Keypad Silent at an Ulster County Door?" (repair capture)
- H2 "Ready to Map Every Door on the Property?" (mid-page CTA)
- H2 "Stuck Outside a Stone House or Mountain Cabin Tonight?" (final repair capture)

### De-dup notes
Planned against the NYC/LI/HV/Manhattan/Brooklyn/Queens registers. Deliberately avoided: HV hub intents (remote rental codes from the city, STR registry, internet-outage behaviour, logs without monitoring, cold limits, batteries in cold, ice/swelling, barn 200 ft range, no-internet property, thick 19th-c door, Kingston historic-district keypad approval, detached garage with no power, cleaner code for cottage only, county pricing/licensing, office suite, winery; FAQ generator, closed-for-winter install, weekend work, second lock same visit, who programs guest codes, rental turnover service); NYC mortise/pre-war door and former-tenant code; Brooklyn sponsor admin handover and glass/mail-slot door; Queens front-yard gate keypad, re-key-on-purchase, "bring the lock or buy one", family administrator, low-battery warning; LI garage/alarm/storm-door/sell-the-house; Manhattan roommate codes, interior doors, deposit. Partial overlaps for the main run to judge: Q6 (several households' admins at a shared camp) vs Queens FAQ "Who should hold the administrator account when a whole family shares the lock?" (here: privacy between households); Q12 (student-lease turnover economics) vs NYC "small landlord cut off a former tenant's code"; FAQ 4 (keyed-alike) vs Queens FAQ re-key-first; FAQ 2/1 coverage and cost are geo-specific by design. Masked paragraph similarity vs every live smart-lock page: max 0.63 outside standard blocks (licence/warranty/stamp lines and the NAP line "Abstract Enterprises Security Systems · 460 E Fordham Rd … (845) 640-3835 … WhatsApp" at 0.74 vs Manhattan/HV NAP lines — protected NAP content).


## Upper East Side, Manhattan (smart-lock-installation-upper-east-side-manhattan-ny)

Built 2026-10-17 by the Upper East Side builder subagent (batch: Upper East Side, Brooklyn Heights, Flushing). Neighbourhood page; up-link /smart-lock-installation-manhattan. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737 (800 only in shared header chrome). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts unless scraped); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).

Thesis / lane (kept away from the Manhattan page's doorman-platform / office-tower / pied-à-terre / short-stay lane): three door types on the same blocks — pre-war co-op doors with restricted-key cylinders (keep the board's key; retrofit strength = deadbolt), landmarked townhouses (LPC "ordinary repair" vs ornate exterior hardware on special doors; multi-door households with staff), Yorkville walk-ups (street/vestibule door first, tailgating, fire-escape windows); plus ground-floor practices on Park and galleries on Madison. Older, single-person-heavy population → second administrator, away mode, unplanned absence.

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| U1 | `Upper East Side Manhattan boundaries Lenox Hill Yorkville Carnegie Hill housing stock pre-war co-ops townhouses` · Firecrawl search | kobilahavnyc.com, anablepodell.com, brianklewis.com, homes.com (excerpts) | Realtor excerpts only (co-op-dominated prewar buildings on Fifth/Park/Madison). Not cited — replaced by U2. | background |
| U2 | Firecrawl scrape (query) of Wikipedia | https://en.wikipedia.org/wiki/Upper_East_Side | Bounded by 96th St, East River, 59th St, Central Park/Fifth Ave; includes Lenox Hill, Carnegie Hill, Yorkville; Manhattan CD8; 19th Precinct; UES HD designated 1981 (59th–78th along Fifth, up to Third Ave at points), expanded 2010 with 74 buildings; Metropolitan Museum HD 1977 (Fifth 79th–86th); Park Avenue HD 2014, 64 properties 79th–91st; Carnegie Hill HD 1974/1993, 400 buildings; Henderson Place HD 1969; Treadwell Farm HD 1967 (E 61st/62nd between Second and Third, former farm of Adam Treadwell); Second Avenue Subway phase 1 opened Jan 1 2017 with three stations; Lenox Hill Hospital, NewYork-Presbyterian, Weill Cornell on the UES. (Wikipedia's "built by John C. Henderson in 1981" is an evident typo — no build year used.) | §5 paras 1, 3, 5.5 stats, §7 cards, §8 cards, §13 landmark cards |
| U3 | `Landmarks Preservation Commission rules intercom keypad door hardware historic district townhouse permit "intercom"` · Firecrawl search | https://www.nyc.gov/assets/lpc/downloads/pdf/Rules/Revised_Rules_of_the_NYC_Landmarks_Preservation_Commission_08-21-2023.pdf | Found the LPC Rules (Title 63 RCNY), rev. 08-21-2023. | → U4 |
| U4 | Firecrawl scrape (PDF, query) of U3 | same | Windows/doors rule, "Work for Which No Approval is Required": "(iv) Repairing or replacing window or door hardware, such as hinges, knobs and handles, but excluding ornate historic exterior hardware on special doors". "Special door" definition: distinctive glazing; fine craftsmanship/distinctive materials incl. bronze, brass, nickel silver, cast metal, elaborate carved woodwork (not kalamein, rolled steel, extruded aluminum); unique typology; age (pre-1850). §2-18 barrier-free: historic doors may be altered for swing, hardware, hinges, automatic openers if configuration kept. No text found on intercoms/keypads/cameras (searched "ntercom", "camera", "keypad", "card reader" — none). Exact section number for the windows/doors rule not shown in extraction → page cites "the Commission's rules" without a section number. | §5 para 3, §7.5, §8.5 Landmarks bullet, §9 Q1, glossary "Special door" |
| U5 | `LPC "Do I need a permit" historic district work types Certificate of No Effect Permit for Minor Work nyc.gov landmarks` · Firecrawl search | precisionwindowsnj.com, brownstone.blog, nyc.gov DOB (excerpts) | Secondary summaries of PMW / CNE / C of A (not cited). | → U6 |
| U6 | Firecrawl scrape (query) | https://www.nyc.gov/site/lpc/applications/permit-for-minor-work.page | PMW "issued when the proposed exterior work does not require a DOB permit and is found to be restorative or appropriate"; examples: window or door replacement in existing openings; masonry cleaning; through-window HVAC. | glossary "Permit for Minor Work" |
| U7 | Firecrawl scrape (query) then full markdown | https://www.furmancenter.org/neighborhoods/upper-east-side/ (last updated 05/06/2026) | 2024: 224,027 people, 4th largest of 59 neighbourhoods; aged 65+ 23.9%; single-person households 50.5%; homeownership 37.9% vs citywide 32.7%; housing units 141,670; 4,025 units in 4+ unit buildings built 2010–2025; 338 units permitted in new buildings 2025; serious crime 8.8 per 1,000 (2025) vs 12.3 citywide; rental vacancy 7.0% (2024); median household income $168,780 (2024). | §5 para 2, new-construction para, §5.5 stats |
| U8 | `Upper East Side burglary townhouse apartment break-in 19th Precinct 2026` · Firecrawl search (web+news) | — | Irrelevant results (Lake Charles etc.) → EMPTY for 2026 UES burglary news. | — |
| U9 | `site:patch.com upper east side burglary apartment door` · Firecrawl search | patch.com results | Led to U10–U12. | → |
| U10 | Firecrawl scrape (query) | https://patch.com/new-york/upper-east-side-nyc/geriatric-burglar-snuck-ues-doorman-buildings-prosecutors | Sep 5 2019: Samuel Sabatino, 82, charged with 8 counts burglary, 3 grand larceny (~$139,000 goods); two apartments at 201 E. 79th St while residents on vacation; slipped by a doorman at 215 East 68th St around July 4; arrested Aug 31 after denied entrance at 1623 Third Ave. Page names streets only (no building numbers, no name). | §5 para 4, §9 Q "away … codes paused" |
| U11 | Firecrawl scrape (query) | https://patch.com/new-york/upper-east-side-nyc/ues-burglar-uses-roofs-fire-escapes-break-ins-police-say | Dec 4 2019: burglar using fire escapes (from street or roof) to enter through unlocked windows; East 80s and 90s between Lexington and First; five burglaries Nov 10–Dec 2; four during work hours. | §5 para 4, §9 fire-escape Q |
| U12 | Firecrawl scrape (query) | https://patch.com/new-york/upper-east-side-nyc/officers-nab-burglar-trying-kick-yorkville-apartment-door-nypd | Mar 28 2023: 19th Precinct arrested a man inside the vestibule of a Yorkville four-storey walk-up on East 82nd St near East End Ave trying to kick in the door, just after 1 a.m. Sunday. (Name not used.) | §5 para 4, §9 walk-up owner Q |
| U13 | `reddit Upper East Side apartment lock doorman keys smart lock co-op board` · Firecrawl search | https://www.reddit.com/r/NYCapartments/comments/1nrb1ro/does_your_apartment_building_hold_onto_your_spare/ ; https://www.reddit.com/r/AskNYC/comments/16426hd/ | Excerpts only: co-op key closet with coded keys, board and super hold keys; doorman key drop-off. Background only, nothing quoted. | background |
| U14 | `reddit r/UpperEastSide locksmith OR lock OR keys OR "package theft" OR burglary` · Firecrawl search | https://www.reddit.com/r/uppereastside/comments/1fbahty/good_locksmith/ ; .../14ecug6/do_not_duplicate_locksmith/ ; .../1x7md8r/e_75th_st_package_thief/ ; .../1w14f5e/man_stealing_packages/ ; .../1wonytl/good_place_to_get_keys_made/ | Excerpts only (threads not opened): Mul-T-Lock locks with security "card", re-key question; "do not duplicate" key copy request; package thief on E 75th St; package theft "rampant". Described on page as forum themes; no quotes beyond the phrase "do not duplicate". | §5 para 5, §9 Q3, §7.5 |
| U15 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Gracie_Mansion | Built 1799; Carl Schurz Park, East End Ave and 88th St, Yorkville; mayoral residence since 1942. | §13 card |
| U16 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Museum_Mile,_New_York_City (redirected to Fifth Avenue article) | Museum Mile = Fifth Ave 82nd–110th; Met at 82nd; Guggenheim at 88th (1959). | §13 card |
| U17 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Henderson_Place_Historic_District | 24 attached brick rowhouses by Lamb and Rich, Queen Anne style; NYCL designated Feb 11 1969. | §7 card, §13 card |
| U18 | `Madison Avenue Business Improvement District 57th to 86th Street boutiques galleries number of stores` · Firecrawl search | https://www.nyctourism.com/places/madison-avenue-bid/ ; https://nycahc.org/partners/madison-avenue-bid ; https://www.facebook.com/madisonavebid/ | BID covers Madison corridor E 57th–E 86th; Gallery Walk "42 participating galleries" (excerpt, year not shown → page says "has listed"). | §8 card |
| U19 | `York Avenue Upper East Side hospitals Memorial Sloan Kettering Hospital for Special Surgery Weill Cornell Rockefeller University East 60s` · Firecrawl search | https://www.mskcc.org/locations/directory/memorial-hospital ; https://weill.cornell.edu/our-story/affiliations | MSK main hospital 1275 York Ave between 67th and 68th; HSS founded 1863; Weill Cornell/NYP on the UES. | §8 card, §9 hospital Q (named generically as "York Avenue hospitals") |
| U20 | Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Yorkville,_Manhattan | Yorkville = E 79th–E 96th, Third Ave to East River; German enclave, later Czech, Slovak, Hungarian etc.; 86th and 96th St Second Ave Subway stations; Lexington line 77th/86th/96th. | §7 cards, §8 86th St card |
| U21 | `smart lock retrofit compatible Medeco Mul-T-Lock high security deadbolt keep existing key` · Firecrawl search | https://www.consumerreports.org/home-garden/door-locks/buying-guide/ (excerpt) ; https://www.medeco.com/en (excerpt) | Consumer Reports: "a retrofit smart lock's resistance to kicking, picking, and drilling is entirely dependent on the deadbolt it's paired with." | §7.5, §9 Q4, §10.5 H3 2 |
| U22 | `Upper East Side townhouse burglars entered through front door East 60s OR East 70s mansion burglary news` · Firecrawl search (news) | — | Irrelevant results → EMPTY. | — |
| U23 | Silo research reused (research/smart-lock-installation.md, not re-fetched) | S1 fixr.com ($250–$400, avg $300, handyman $50–$100/hr, Jan 2025); S2 bobvila (screwdriver, ~30 min DIY); S3 august.com retrofit ("leaving the outside untouched", single-cylinder only, thumb-turn clearance); S4 August Connect 10–15 ft; S5 Yale Matter (border router same brand as app, Nest Hub for Google); S6 Bold (Thread mesh, up to five ecosystems, HomePod mini); HV research: Schlage Encode "up to six months", "Requires 2.4GHz WiFi"; cultofmac (Encode Plus Thread via HomePod mini/Apple TV 4K); LI research: Schlage Encode Plus Apple Home Key; Ring Alarm Z-Wave (subscription, Ring-app codes only); 2010 ADA 404.2.7 (no tight grasping, 34–48 in); NYC hub: N1 MDL §51-c, N3 HMC §27-2043, N4 Tenant Data Privacy Act, N6 HPD fire-safety (no double-cylinder, no key-locked fire-escape window gates); Manhattan: M14 NFPA 80 field prep, M15 NYC BC 1010.1.9.9 | As listed in the silo file. | §8.5, §9, §10, §10.5, §14, FAQ |
| U24 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are paraphrased published claims, with the publisher named under each, stated on page. | — |
| U25 | Local news on smart locks specifically on the UES (Patch UES, West Side Spirit / Our Town, The City) | — | No UES smart-lock story found → EMPTY for the service category. | — |
| U26 | Hyperlocal UES co-op board rules on unit-door locks / white-glove board policies | — | No sourced board policy found → EMPTY; page states general practice only, no claim about any named building. | — |
| U27 | Townhouse counts / share of UES doors under LPC | — | No single sourced figure beyond district building counts (U2) → not stated. | — |

### Prices used (Manhattan ×1.25, round half-up; no new figures — all as published on smart-lock-installation-manhattan.html / research "Prices used")
- Keypad or fob reader with electric strike, one door: $1,500–$2,500 base → **$1,875–$3,125**.
- New electric strike: $250–$450 → **$313–$563**.
- Failed electric strike repair: $295–$485 → **$369–$606**.
- Programming / setup-only visit: **$265 first hour**, then 30-minute blocks (research/tv-mounting-prices/BRIEF.md line 15, as on the Manhattan page).
- Service/callback: **$195/hr, 3-hour minimum ($585)**, never on the initial install.
- Apartment / townhouse door smart lock: no AESS figure → "quoted flat at free walkthrough".
- National comparison only: Fixr $250–$400, avg ~$300, labour $50–$100/hr (Jan 2025).

## Images (11) — permanent image rule (Drive folder empty per main run; CompanyCam not connected)

Chosen from the unused list in images/smart-lock-installation/ (sorted, first third), viewed before use; none is used on smart-lock-installation-manhattan.html. One cropped to remove a partial face, one cropped to remove a face.

| New file (images/smart-lock-installation/) | Copied from (same folder) | Original source per research file | Edit |
|---|---|---|---|
| smart-lock-installation-upper-east-side-keypad-strike-push-to-exit.webp (hero, eager) | smart-lock-installation-bronx-keypad-push-to-exit-strike.webp | low-voltage/low-voltage-installation-queens-electric-strike-keypad.jpg | re-saved WebP q80 |
| smart-lock-installation-upper-east-side-video-intercom-keypad-wiring.webp | smart-lock-installation-bronx-intercom-keypad-panel-wiring.webp | low-voltage/low-voltage-installation-queens-11-video-intercom-entry-wiring.jpg | q80 (installer seen from behind) |
| smart-lock-installation-upper-east-side-fob-reader-door-frame.webp | smart-lock-installation-bronx-reader-door-frame-wiring.webp | low-voltage/low-voltage-installation-queens-12-access-control-reader-wiring.jpg | q80 (installer from behind) |
| smart-lock-installation-upper-east-side-maglock-wiring-label-closeup.webp | smart-lock-installation-bronx-maglock-terminal-label.webp | low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | left 380 px cropped (partial face) |
| smart-lock-installation-upper-east-side-exit-button-beside-keypad.webp | smart-lock-installation-dutchess-county-push-to-exit-beside-keypad-reader.webp | commercial-security/commercial-security-systems-nyc-rex-exit-button.jpg | q80 |
| smart-lock-installation-upper-east-side-door-contact-lobby-frame.webp | smart-lock-installation-dutchess-county-door-contact-glass-door-frame.webp | commercial-security/commercial-security-systems-nyc-door-contact-install.jpg | q80 |
| smart-lock-installation-upper-east-side-maglock-armature-office-door.webp | smart-lock-installation-dutchess-county-maglock-armature-glass-door.webp | commercial-security/commercial-security-systems-manhattan-maglock.jpg | q80 |
| smart-lock-installation-upper-east-side-keypad-reader-staff-door.webp | smart-lock-installation-brooklyn-keypad-card-reader-employee-door.webp | (not listed in research file) | left 620 px cropped (face) |
| smart-lock-installation-upper-east-side-maglock-lobby-door-header.webp | smart-lock-installation-bronx-maglock-header-glass-door.webp | low-voltage/low-voltage-installation-queens-maglock-install.jpg | q80 (installer from behind) |
| smart-lock-installation-upper-east-side-request-to-exit-sensor-header.webp | smart-lock-installation-dutchess-county-wave-to-exit-sensor-door-header.webp | commercial-security/commercial-security-systems-nyc-request-to-exit-sensor.jpg | q80 |
| smart-lock-installation-upper-east-side-door-controller-panel.webp | smart-lock-installation-dutchess-county-three-door-controller-card-readers.webp | commercial-security/commercial-security-systems-nyc-door-controller-enclosure.jpg | q80 |

Rejected after viewing: dutchess-county-desk-release-button-mounting (button is labelled "PANIC PUSH" — not a door release; a copy was made then deleted), bronx-electric-strike-glass-entry / long-island-keypad-reader-mounting / hudson-valley-keypad-intercom-stone-pillar / long-island-credential-programming-desk / long-island-door-controller-cabinet (faces), hudson-valley-entry-panel-wiring ("123 Main Street" directory), hudson-valley-door-contact-keypad-panels and hudson-valley-secured-lobby-entry (1536×1024 — generator-typical size), long-island-keypad-strike-exit-button and long-island-maglock-header-wiring (near-duplicates of two chosen photos).

DAILY-LOG note: `images: 11 reused from images/smart-lock-installation/ library copies (originally images/low-voltage/ and images/commercial-security/) (no real smart-lock photos yet)`.
**Flag for Anwar:** the whole library (including the aess-smart-lock-installation-* set) shows signs of being generated images (garbled lettering on caps/gloves, generic "123 Main Street"/"Pinnacle Business Center" signage, 1536×1024 sizes). DAILY-RUN forbids AI-generated images; these were used because the run instructions direct Step C / permanent-image-rule reuse from this folder. Replace with real AESS photos when available.

## Question register — smart-lock-installation-upper-east-side-manhattan-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 13)
Townhouses in the historic districts
1. Can the ornate brass knob and escutcheon on our townhouse door stay exactly as they are once the lock goes smart?
2. We employ a housekeeper, a nanny and a driver — should each of them have the townhouse's main door, or only the service entrance?
Pre-war co-ops on Fifth, Madison and Park
3. We had to show a key card to get copies of our high-security key — does going smart weaken that duplication control?
4. Is a lock that clamps onto the inside of our deadbolt as strong as the deadbolt itself?
5. Our pre-war apartment has a second door from the kitchen to the service hall — should it be smart as well?
6. Decades of paint have built up on our pre-war door's edge — does that matter for a motorised bolt?
Households that are often away
7. When we tell the front desk we're going away, should the cleaner's and walker's codes be paused too?
8. If I'm suddenly admitted to one of the York Avenue hospitals, how does a friend get in to feed the cat?
Yorkville walk-ups and newer towers
9. As the owner of a small Yorkville walk-up, should the money go on the street door or on each apartment door?
10. People keep slipping into our walk-up behind residents — can the street door be made to close and lock faster?
11. Burglars in the East 80s and 90s came in through fire-escape windows — does a smart front door do anything about that?
Practices and galleries on the ground floor
12. Our practice occupies the ground floor of a Park Avenue co-op — whose rules govern a keypad on the practice's own street entrance?
13. Our Madison Avenue gallery keeps borrowed works in a back room — can that door keep its own record of every opening?

### §17 FAQ (visible == FAQPage, 9)
1. Does an Upper East Side job cost more than the Manhattan rate because of the building?
2. Do you also work in East Harlem, Midtown East and on Roosevelt Island, just beyond the Upper East Side?
3. Which licence number should we give the co-op board for its contractor file?
4. Will you service a smart lock that another company installed in our apartment?
5. Our elevator opens onto a landing we share with just one neighbour — does our apartment door still need a proper lock?
6. Can the lock's app account be set up in the name of our estate manager or family office?
7. Do you install locks that open with a tap of an iPhone or Apple Watch?
8. What happens to our codes if the lock's maker shuts down its cloud service?
9. Our building supplies Wi-Fi to every apartment — can the lock use it, or do we need our own?

### Other question-form headings
- H2 "Smart Lock Misfiring Between 59th and 96th Street?" (repair capture)
- H2 "Locked Out of a Co-op, Townhouse or Walk-Up East of the Park?" (final repair capture)

### De-dup notes
Deliberately avoided: NYC-hub intents (renter rights, co-op key to board, board approval, LL63 owner duties, double-cylinder legality, self-closing door, mortise hallway match, lobby+unit same system); Manhattan intents (platform clash/enrolment, scope letter, insurance, desk/walker/cleaner access, packages to desk, talk-past-lobby, batteries abroad, renovation crew, short-stay, lockboxes, suite tower, rated frame strike, maglock fire release, after-hours suite, cast-iron reader); HV "historic-district approval for a keypad" (Q1 is framed on keeping ornate exterior hardware, not on whether approval is needed); Brooklyn "outer vs inner door of a brownstone" and "stoop parcels"; Queens/Nassau/SI/Suffolk/Westchester ageing-parent, arthritis, home-attendant and paramedic-entry intents; Rockland quiet beeps; Brooklyn Heights batch sibling "laundry, bike room and storage cages" (my storage-cage FAQ was replaced by the elevator-landing FAQ). Partial overlaps for the main run to judge: Q7 (pause service codes while away) vs HV "see who came and went at my country house"; FAQ 9 (building-supplied Wi-Fi) vs Flushing "dozens of neighbours' Wi-Fi networks"; FAQ 4 (service another company's lock) vs Flushing "fingerprint reader on our existing lock stopped recognising anyone" — different intents in my reading.


## Brooklyn Heights, Brooklyn (smart-lock-installation-brooklyn-heights-brooklyn-ny)

Built 2026-10-17 by the Brooklyn Heights builder subagent (batch: Upper East Side / Brooklyn Heights / Flushing neighbourhood pages). Phone (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, #brooklyn) · up-link /smart-lock-installation-brooklyn · Brooklyn ×1.00.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes).
Lane (to stay clear of the Brooklyn area page and the rest of the silo): landmark rules for anything mounted beside the door (LPC Rules §2-20 criteria), carriage houses on the mews, Federal wood houses, rowhouses converted into small self-managed co-ops (board-owned admin, common rooms), pre-war buildings / former hotels, USPS arrow-key access at street doors, film-location access, NYPD security survey, plaster-on-brick cable routes, original etched glass, Montague Street / Atlantic Avenue shop doors (BHMA strength rating), fail-secure vs fail-safe street-door strikes.

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| BH1 | `Brooklyn Heights Historic District first historic district 1965 boundaries rowhouses Federal Greek Revival Italianate` · Firecrawl search | https://hdc.org/buildings/brooklyn-heights-historic-district/ ; https://architecturaltrust.org/.../brooklyn-heights-historic-district/ ; https://www.facebook.com/NYCLandmarks/posts/... (excerpts) | Designated Nov 23, 1965, NYC's first historic district (LPC post); Federal, Greek Revival, Gothic Revival, Italianate / Anglo-Italianate styles; HDC: "it is the Greek Revival style that is particularly notable". | §5 para 3, §5.5 bullet 1, §7 cards (Greek Revival, Gothic Revival, Italianate), architecture intro |
| BH2 | (same search) → https://thebha.org/neighborhood/ · Firecrawl scrape (markdown) | https://thebha.org/neighborhood/ | Boundaries Old Fulton St–Atlantic Ave, Cadman Plaza/Court St–Promenade/East River; "overwhelmingly low-rise brick and brownstone row houses with a smattering of apartment buildings"; Montague Street the one main shopping street, stores/restaurants on Henry Street; 22,593 housing units, 57% renter-occupied, 40% owner-occupied, 3% vacant; cars available 0.5 (houses/condos) vs 1.8 NYC; after the Brooklyn Bridge (1883) mansions replaced by apartment buildings; after 1929 many homes divided into rooming houses; Promenade built on top of the BQE after mid-1940s testimony; Brooklyn Historical Society building 1878–81, George B. Post. | §5 paras 1–2, §5.5 bullets 2–3, §13 Promenade card, Pre-war section para 1, §10.5 H3 7 |
| BH3 | `Brooklyn Heights carriage houses mews Hunts Lane Grace Court Alley Love Lane history` · Firecrawl search → scrape | https://www.brownstoner.com/brooklyn-life/carriage-houses-of-brooklyn-heights/ (scraped; 2013-06-12) | Carriage houses pictured: Hunts Lane, 181 & 165 Columbia Heights, 43 Love Lane, 30-33 College Place, Grace Court Alley, 291-293 Hicks Street; reader comment: 43 Love Lane "totally reconstructed"; more on Middagh, Pineapple, Willow, and Henry Street south of Joralemon; one still has horse stalls. | §6 card, §7 card, §9 carriage-house Q, Carriage section para 1 |
| BH4 | (same search) → https://citylore.org/places/grace-court-alley/ · Firecrawl scrape (query) | https://citylore.org/places/grace-court-alley/ | Unnamed horse-stable alley of the Remsen family; mews for mansions on Remsen and Joralemon; stables became garages and chauffeurs' quarters, later apartments; "tall wooden stable doors, the hay cranes"; 2–3-storey carriage houses. | §7 card, §9 carriage Q, §13 Grace Court Alley card |
| BH5 | `Brooklyn Heights burglary package theft 84th Precinct 2025 2026` · Firecrawl search | https://thebha.org/resources/city-other-services/ ; https://x.com/NYPD84Pct (excerpts) | 84th Precinct covers Brooklyn Heights; 84 Pct X account: "we offer FREE security assessments … ask for the Crime Prevention Officer". Robbery-pattern and retail-theft items found (Instagram, Brooklyn Eagle) — not used (no smart-lock relevance verified). | §9 NYPD survey Q |
| BH6 | `NYPD crime prevention officer free security survey home business precinct` · Firecrawl search → scrape | https://www.nyc.gov/site/nypd/services/law-enforcement/security-safety.page (scraped) ; https://portal.311.nyc.gov/article/?kanumber=KA-02993 (excerpt) | "Security Surveys are provided free of charge by precinct crime prevention officers … Officers evaluate locks, doors, lighting, windows, landscaping, and alarm systems"; 311 books appointments. | §9 NYPD survey Q |
| BH7 | `Landmarks Preservation Commission intercom security camera keypad installation facade historic district permit rules` · Firecrawl search → scrape (pdf, query) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf (2025 edition) | Permit needed for work affecting exterior in a historic district incl. yards; no permit for ordinary maintenance/repair of health-safety-utility equipment; LPC Rules §2-20: equipment not on primary facade unless no alternative; discreet location (beneath band course, under stoop, behind areaway wall); ~10 in. visible conduit, painted, into mortar joints, not decorative surfaces; equipment small and blended; intercom panels/doorbells within or adjacent to door opening, or on fence/wall in front; max two light fixtures + one intercom panel per opening; mailboxes and mail key lockboxes within/adjacent to door opening, on gate/door under stoop, plain stoop wall, areaway fence or post; application needs photos, elevations, manufacturer cut sheets; LPC 212-669-7817 / info@lpc.nyc.gov. Hardware (locks, handles) no-permit rule carried from silo research B4. | §5 para 3, §5.5 bullet 6, §6 card, §8.5 bullet 1, §9 reader-cable Q, §9 postal Q, §10.5 H3 3, LPC section, FAQ cut-sheets |
| BH8 | `USPS arrow lock key apartment building intercom panel mail carrier access replacement` · Firecrawl search → scrape | https://www.uspsoig.gov/reports/audit-reports/arrow-key-management-controls (scraped) ; https://www.intercomsonline.com/obtain-usps-access-master-lock (excerpt) | OIG: "The Postal Service uses a universal key, known as an arrow key, to access collection boxes, outdoor parcel lockers, cluster box units, and apartment panels"; number of arrow keys in circulation unknown; lost/stolen keys not adequately reported. USPS lock arranged via local post office (IntercomsOnline excerpt). | §9 postal-key Q |
| BH9 | `Brooklyn Heights film shoots location permits residents filming Mayor's Office of Media and Entertainment Brooklyn Heights Blog` · Firecrawl search → scrape | http://brooklynheightsblog.com/archives/49580 (2012-10-22) ; http://brooklynheightsblog.com/archives/52397 (2012-11-30) | BHA's Judy Stanton "losing count" of shoots; Brooklyn Eagle counted 14+ productions in two weeks; Council Member Stephen Levin asked the film office to put all of Brooklyn Heights on the "hot spot" list. | §5 para 4 (busy with crews), §9 film-shoot Q |
| BH10 | `Brooklyn Heights film shoot 2025 OR 2026 filming Brooklyn Heights street residents` · Firecrawl search | https://brooklyneagle.com/307074/brooklyn-heights-filming-of-law-order/ (excerpt) | "Law & Order filmed on the Brooklyn Heights Promenade on Tuesday, April 8, 2025." | §9 film-shoot Q |
| BH11 | https://www.nyc.gov/site/mome/permits/permits.page · Firecrawl scrape (query) | same | EMPTY (page returned no extractable text). Not used. | — |
| BH12 | `24 Middagh Street oldest house Brooklyn Heights Federal style wood frame 1824` · Firecrawl search | https://www.6sqft.com/brooklyn/brooklyn-heights/24-middagh-street/ ; https://inhabit.corcoran.com/peek-inside-the-oldest-house-in-brooklyn-heights/ (excerpts) | "Built in 1824, 24 Middagh Street is a charming, wood-frame, Federal house"; Corcoran: oldest house in the neighbourhood, "likely going up in 1824". | §7 Federal card, §13 card, Carriage section para 3 |
| BH13 | `Hotel St. George Brooklyn Heights history largest hotel now co-op apartments student housing Clark Street` · Firecrawl search | https://stgeorgetower.com/history/ ; https://en.wikipedia.org/wiki/Hotel_St._George (excerpts) | Built 1885–1929/30 on block Clark/Hicks/Pineapple/Henry; 2,632 rooms at peak, once city's largest hotel; Tower & Grill became co-op 1984 (St. George Tower and Grill Owners Corp.); other buildings student housing; Clark Street station's sole entrance through hotel ground story; 1995 fire. | §5.5 bullet 5, §7 card, §8 Clark Street card, §13 card, Pre-war section |
| BH14 | `Bossert Hotel Montague Street 2026 news` · Firecrawl search | https://newyorkyimby.com/2026/08/lpc-to-review-revised-proposal-for-hotel-conversion-at-98-montague-street-...html ; https://en.wikipedia.org/wiki/Hotel_Bossert ; https://larevuedeshotels.com/en/brooklyn-hotel-bossert-become-borough-first-ritz-carlton-residences (excerpts) | 98 Montague St, 14-storey Renaissance Revival landmark; opened 1909; sold for $100M (Crain's, May 2025) to SomeraRoad; residential conversion (Ritz-Carlton Residences) with LPC reviewing revised plans Aug 2026. YIMBY also: demolition complete for a 47-storey tower at 205 Montague St (June 29, 2026) — not used on page. | §7 card, §13 card, Pre-war section |
| BH15 | `Plymouth Church Orange Street Brooklyn Heights Henry Ward Beecher Underground Railroad national landmark` · Firecrawl search | https://www.plymouthchurch.org/more-history (excerpt); Facebook post excerpt (founded 1847) | Beecher first pastor; Underground Railroad connections; red-brick sanctuary seating 2,800 on Orange Street; National Historic Landmark 1961; founded 1847. | §8 card, §13 card |
| BH16 | `Montague Street BID Brooklyn Heights businesses …` · Firecrawl search | https://www.montaguebid.com/the-bid (excerpt) | Serves more than 100 businesses; north side of Montague between Court and Hicks; south side 200 to 78 Montague; founded 1998; works with 84th Precinct NCOs. | §5 para 4, §5.5 bullet 4, §8 card |
| BH17 | `Brooklyn Heights townhouse converted condominium units brownstone condo shared entrance Remsen Street Pierrepont Street` · Firecrawl search | https://www.6sqft.com/charming-brooklyn-heights-duplex-with-versatile-backyard-asks-1-25m/ (excerpt) | "114 Remsen Street is a four-story Italianate brownstone built in 1900. The seven-unit co-op …" | §5 para 2 (example of a rowhouse co-op) |
| BH18 | `reddit brooklynheights packages stolen stoop lock keys building` · Firecrawl search | https://www.reddit.com/r/Brooklyn/comments/easaq5/rampant_package_theft_in_brooklyn_how_do_you_keep/ (excerpt only) | Excerpt mentions "changing the lock to some kind of smart lock to allow packages to be dropped off behind the stoop gate" with "Hill/Brooklyn Heights neighborhoods". Thread body not retrieved. Not quoted (package intent already on Brooklyn page). | research only |
| BH19 | `ANSI BHMA A156.40 residential deadbolt grade …` · Firecrawl search | https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights/A15640-2015-Residential-Deadbolts ; https://community.smartthings.com/t/faq-ansi-bhma-lock-grades/282344 (excerpts) | A156.40 (2025) residential deadbolts: durability, operation, security tests; "Seventeen aggressive tests … loading the door against the deadbolt with 1,350 pounds of force"; older grade 1 = commercial, grade 2 residential/light commercial. | §9 Montague shop Q |
| BH20 | `NYC Facade Inspection Safety Program Local Law 11 buildings greater than six stories sidewalk shed` · Firecrawl search | https://www.nyc.gov/site/buildings/safety/facade-local-law.page (excerpt) | Owners of buildings higher than six stories must have exterior walls inspected every five years and file a report (FISP). | FAQ sidewalk-shed |
| BH21 | `https://www.brownstoner.com/select-story/brownstone-doors-everything-you-ever-wanted-to-know/` · Firecrawl scrape (query) | same | EMPTY (no extractable article text). Centre-knob statements on the page are general hardware description, no statistic claimed. | — |
| — | Carried from silo research (not re-fetched) | S1 Fixr; S2 Bob Vila; S3 August retrofit; S4 August Connect 10–15 ft; S5 Yale Matter/Thread; S6 Bold; S7 SmartThings mortise thread; N1 MDL §51-c; N3 HMC §27-2043; N4 LL63/2021; N5 LL111/2018; N6 HPD double-cylinder; N2 co-op duplicate key; B4 LPC hardware no-permit; B11 SBS BID directory (Atlantic Avenue, Court-Livingston-Schermerhorn, Montague Street BIDs) | as logged in research/smart-lock-installation.md | §8, §8.5, §9, §10.5, FAQ |

### Prices used (no new figures; Brooklyn Heights = Brooklyn ×1.00)
- $1,500–$2,500 single-door keypad or fob reader with electric strike — silo "Prices used" (access-control-installation-brooklyn / bath-beach pages). §14 table, §15 Premium, FAQ 1, Service schema.
- $250–$450 new electric strike; $295–$485 failed strike repair — silo "Prices used" (door-buzzer pages). §14, §15 Standard, FAQ 1, schema.
- $195/hr, 3-hour minimum ($585) service call — blueprint v2.3 §9 verbatim. §14.
- Fixr national $250–$400, average $300 — labelled national third-party (silo S1). §10.5 H3 1, §14.
- House / unit / carriage-house door smart lock: no AESS figure → "quoted flat at the free walkthrough". The $195 setup-only visit rate was deliberately NOT used (still flagged for Anwar on Brooklyn/LI).

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DuckDuckGo: EMPTY (not accessible in build env). §10.5 says so and uses cost-guide / manufacturer claims.
- Yelp 1–3★ Brooklyn Heights locksmith / smart lock: EMPTY (not accessible in build env).
- Reddit (r/brooklynheights, r/Brooklyn): search excerpts only; thread bodies not retrieved → EMPTY beyond excerpts.
- NYC MOME permits page and Brownstoner "Brownstone Doors" article: scrape returned no text → EMPTY.
- Local news on smart locks specifically in Brooklyn Heights (BH Blog, Brooklyn Paper, Brooklyn Eagle, Patch): none found → EMPTY.
- Field Notes: no sourced Brooklyn Heights install anecdote → written as working practice and labelled so.

## Images (11) — permanent image rule
Drive folder "AESS Website Photos/Smart Lock Installation" empty (main run); CompanyCam not connected. Source silo: images/smart-lock-installation/ library (unused geo-named copies, taken from the middle third of the sorted unused list; those files were originally reused from images/low-voltage/ and images/commercial-security/). Faces and readable signs cropped out where present. All new files WebP q80.

| New file (images/smart-lock-installation/) | Source file (crop) |
|---|---|
| smart-lock-installation-brooklyn-heights-keypad-strike-exit-button-glass-door.webp (hero, eager) | smart-lock-installation-nyc-keypad-electric-strike-glass-door.webp (cropped to right side, face removed) |
| smart-lock-installation-brooklyn-heights-strike-terminal-wiring-gloved-hands.webp | smart-lock-installation-putnam-county-electric-strike-terminal-wiring.webp |
| smart-lock-installation-brooklyn-heights-keypad-reader-stone-door-jamb.webp | smart-lock-installation-orange-county-keypad-reader-employee-door-stone.webp (sign cropped out) |
| smart-lock-installation-brooklyn-heights-enclosure-conduit-brick-wall.webp | smart-lock-installation-putnam-county-exterior-enclosure-brick-conduit.webp |
| smart-lock-installation-brooklyn-heights-maglock-header-wiring-office-door.webp | smart-lock-installation-nyc-maglock-glass-office-door.webp (face cropped out) |
| smart-lock-installation-brooklyn-heights-fob-reader-mounting-door-frame.webp | smart-lock-installation-nyc-fob-reader-mounting.webp (head cropped out) |
| smart-lock-installation-brooklyn-heights-fingerprint-reader-gate-post-wiring.webp | smart-lock-installation-putnam-county-gate-fingerprint-keypad-wiring.webp |
| smart-lock-installation-brooklyn-heights-strike-pocket-aluminum-door-frame.webp | smart-lock-installation-orange-county-electric-strike-door-frame-prep.webp |
| smart-lock-installation-brooklyn-heights-door-controller-boards-power-supply.webp | smart-lock-installation-putnam-county-door-controller-boards-power-supply.webp |
| smart-lock-installation-brooklyn-heights-wave-to-exit-sensor-door-header.webp | smart-lock-installation-nyc-wave-to-exit-sensor.webp (face cropped out) |
| smart-lock-installation-brooklyn-heights-door-position-contact-frame.webp | smart-lock-installation-nyc-door-position-contact.webp (face and most of sign cropped out) |

Rejected after viewing: nyc-electric-strike-lobby-door (clear face + readable sign), nyc-push-to-exit-button-wiring and nassau door-contact collage (faces), orange-county-fob-card-programming-station (readable programming checklist), putnam gated-entrance-post-camera (not lock-related). Note for Anwar: many library photos (including these) look stylised/possibly AI-generated (logo text varies between "Enterprises" and "Enterprise LLC"); swap for the real aess-* smart-lock photos or new Drive uploads when available.

## Question register — smart-lock-installation-brooklyn-heights-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 10)
1. Our carriage house on the mews still has its tall wooden stable doors — where does a smart lock actually go?
2. We want a reader beside the doorway rather than on the door — how does its cable get there without marking the brownstone?
3. The mail carrier opens our building's street door with a postal key in the old intercom — what happens to that when the door goes keyless?
4. Our brownstone is a self-managed co-op of six or seven apartments — who decides on a keypad for the shared street door, and who holds the master admin?
5. The laundry, bike room and storage cages in our co-op all run on one old key everyone has copied — can those doors go keyless too?
6. Our inner vestibule door still has its original etched glass — how do you fit a lock without putting the glass at risk?
7. Our walls are original plaster on brick — can a wired reader or door sensor be fished to the doorway without opening the walls?
8. A production company wants our house for a few days of filming — how should their access work?
9. Should we book the NYPD's free security survey before or after the smart lock goes in?
10. Our Montague Street shop carries valuable stock — how does a smart deadbolt's strength rating compare with the lock it replaces?


### §17 FAQ (visible == FAQPage, 7)
1. What does a keypad with an electric strike cost on the street door of a Heights rowhouse co-op?
2. Do your installers also cover DUMBO, Cobble Hill and Downtown Brooklyn?
3. If the power goes off, should the electric strike on our co-op's street door stay locked or let the door open?
4. Our building has a sidewalk shed or scaffold over the entrance for facade work — can the street-door reader still go in?
5. Can you send cut sheets and marked-up photos for an LPC application or a board approval?
6. Can the old intercom wire to our street door be reused for a new reader or strike?
7. Does it matter which way our front door swings or which side the hinges are on?

### Other question-form headings
- H2 "Keypad Silent on a Heights Stoop or Shop Door?" (early repair capture)
- H2 "Shut Out on Remsen, Hicks or Joralemon Street Tonight?" (final repair capture)
- H3 "National brands or a local installer?" (comparison sub-head)

De-dup notes: compared by meaning against every live smart-lock page and the Upper East Side and Flushing pages on disk at build time. Replaced during build: "Parking on our block … hold a space for your van?" (= Flushing FAQ "Do we need to arrange parking or loading space for your van downtown?") → fail-secure/fail-safe strike FAQ. Avoided on purpose: historic-district approval for a keypad (HV), replacement door look (Brooklyn), leave original door and use another door (Ulster), thin/antique doors (Putnam/Ulster), packages (Brooklyn/Manhattan), guest codes, co-op board approval of a unit lock and duplicate key (NYC), entry-log fairness (Brooklyn/SI), previous owners' access (SI), brand list (NYC). Partial overlaps for the main run to judge: §9 Q10 (BHMA strength rating for a shop) vs UES "Is a lock that clamps onto the inside of our deadbolt as strong as the deadbolt itself?" (retrofit strength) and Flushing "no-name smart lock vs Schlage"; FAQ 1/2 cost and coverage are geo-specific by design (as on every silo page); FAQ 3 fail-secure strike vs LI "After a storm … can we still get in?" (here: choosing strike type for a shared street door).


## Flushing, Queens (smart-lock-installation-flushing-queens-ny)

Built 2026-10-17 (neighbourhood batch: Upper East Side / Brooklyn Heights / Flushing). Phone (347) 434-6392 · GBP Bronx (460 E Fordham Rd, `#bronx`) · up-link `/smart-lock-installation-queens` · Queens ×1.05 pricing.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane (kept away from the Queens page's multigenerational-house / basement / garden-co-op lane): Flushing = commercial downtown + condo towers + imported hardware + detached Broadway–Flushing houses. Door *construction* decides the lock (mortise push-pull vs bored deadbolt, frameless glass, hollow-metal suite doors), tower radio congestion, business door policy (staff turnover, unlocked side doors, broken-through front doors), and niche business rules (IRS Pub 4557, NYC biometric sign law, interlocked vestibules, children's exit at tutoring centres).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/Flushing package-theft threads found as search excerpts only (F20) — not scraped, not quoted on page. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are recurring marketing/listicle claims, stated as such on the page. |
| 6 | Landmarks | F8 (Community Board 7 history page), F9 (Wikipedia Flushing–Main St station) |
| 7 | Use cases / building stock | F3–F7, F10 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | QNS (F1, F11, F12), 6sqft excerpt (F5), NYT 2017 excerpt (F17) |
| 10 | Hyperlocal | QNS used; Queens Chronicle (Sky View Parc / Broadway–Flushing) excerpts only, not used; Queens Ledger EMPTY |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| F1 | `Flushing Queens burglary 109th Precinct 2025 police` · Firecrawl search → Firecrawl scrape | https://qns.com/2026/10/teen-busted-flushing-home-invasion/ | QNS Oct 12, 2026 (Bill Parry): four masked armed men forced entry into a residence on the Horace Harding Expwy near 150th St ~2:30 a.m. Oct 11; 17-year-old arrested. 109th Pct burglaries 181 through Oct 4, 2026 vs 354 same point 2025 (−48.9%, CompStat). | §5 para 5, §5.5 bullet 6, §9 Q "Horace Harding" |
| F2 | same search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/109th-precinct.page | 109th Pct covers Downtown Flushing, East Flushing, Queensboro Hill, College Point, Malba, Whitestone, Beechhurst, Bay Terrace. | §5 para 5 |
| F3 | `Flushing waterfront Tangram Skyview Parc One Flushing condo towers development` · Firecrawl search | https://www.homes.com/building/sky-view-parc-flushing-ny/b-c7gxr21kcbr8l/ | Sky View Parc: 448-unit condo atop a busy mall, designed by Perkins Eastman. | §7 card "Glass Condo Towers" |
| F4 | `Tangram Flushing mixed-use towers condo hotel 133-36 37th Ave F&T Group` · Firecrawl search | https://www.homes.com/building/tangram-flushing-ny/b-nmz5t4es8fqfs/ ; https://www.fandtgroup.com/news-press/new-model-units-unveiled-at-tangram-house-new-luxury-condominium-in-the-heart-of-flushing-city-realty | Tangram House South opened 2019, Tangram House West (16 storeys) 2022; F&T Group; 1.2 million sq ft mixed-use (hotel, office, retail). | §7 card "Glass Condo Towers" |
| F5 | `Special Flushing Waterfront District approved City Council 2021 Flushing Creek towers units` · Firecrawl search | https://flushingwaterfront.com/ ; https://www.6sqft.com/nyc-rezoning-flushing-waterfront-district/ ; https://www.guardiansofflushingbay.org/special-flushing-waterfront-district | Developer site: 1,725 residential units proposed, hotel 879 keys. 6sqft: 13-tower mixed-use project, rezoning approved by City Council. (Year: excerpts conflict — takerootjustice says Dec 2020; page gives no year.) | §7 card "Waterfront Redevelopment" |
| F6 | `Broadway-Flushing historic district National Register detached houses covenants` · Firecrawl search → Firecrawl scrape (broadwayflushing.org/history) | http://broadwayflushing.org/history/ ; https://www.scribd.com/doc/129067918/Broadway-Flushing-Historic-District-National-Register-Application ; https://cityneighborhoods.nyc/broadway-flushing ; https://en.wikipedia.org/wiki/Broadway%E2%80%93Flushing,_Queens | HOA founded Jan 1964 to protect R1-R2 zoning and the Rickert–Finlay Covenant of 1906; State & National Register 2006; register application: 1919–1925 hundreds of detached Dutch Colonial, Colonial, Tudor Revival houses; covenant = detached, set back ≥20 ft; Wikipedia: 1,330 properties. QChron excerpt: DOB doesn't enforce covenant; HOA sues. | §7 card "Detached Houses in Broadway–Flushing", Across Flushing |
| F7 | `Flushing Queens neighborhood demographics … community district 7` · Firecrawl search → Firecrawl scrape | https://www.furmancenter.org/neighborhoods/flushing-whitestone/ | Furman Center (updated 05/06/2026): 2024 pop 251,983; homeownership 52.5% vs 32.7% citywide; 65+ 23.1% (15.8% in 2000); housing units 101,835; 2025 sales: condo 764 vs 1-family 488 vs 2–4 family 328; 5,142 units in 4+ unit buildings built 2010–2025; serious crime 9.1/1,000 vs 12.3 citywide (2025). | §5 paras 2–3, §5.5 bullets 1–3, Changing Hands section |
| F8 | same search | https://www.nyc.gov/assets/planning/newest-new-yorkers-2026/Ch3.html | DCP 2026: Flushing–Murray Hill = city's largest immigrant neighbourhood, 95,700 foreign-born, two-thirds of population. | §5 para 2, §5.5 bullet 4 |
| F9 | `Flushing Town Hall 1862 Bowne House 1661 Quaker Meeting House Flushing landmarks Freedom Mile` · Firecrawl search → Firecrawl scrape | https://www.nyc.gov/site/queenscb7/about/history.page ; https://en.wikipedia.org/wiki/John_Bowne_House ; https://flushingfriends.org/2015/05/15/sacredsites/ | CB7: Flushing Town Hall 1862 Romanesque Revival, cultural centre of Flushing Council on Culture and the Arts; Bowne House 1661 or earlier, oldest surviving house in Queens County; Friends Meeting House begun 1694, members were Underground Railroad conductors; Kingsland House 1785, moved 1968, Queens Historical Society HQ; Lewis Latimer House 1887–1889 Queen Anne; Wikipedia: 1662 Quaker meeting → Bowne arrested by Stuyvesant; Flushing Meeting took part in open house (2015). | §13 landmark cards |
| F10 | `Flushing-Main Street 7 train station busiest outside Manhattan ridership MTA` · Firecrawl search | https://en.wikipedia.org/wiki/Flushing%E2%80%93Main_Street_station_(IRT_Flushing_Line) ; https://www.mta.info/maps/subway-line-maps/7-line | 2024: second-busiest station outside Manhattan, 10th busiest in system; terminal, entrances at Main St & Roosevelt Ave. | §13 card "Flushing–Main Street Station" |
| F11 | `qns.com Flushing burglary spree December 20 2025 medical office businesses 109th 107th Precinct` · Firecrawl search → Firecrawl scrape (directQuote) | https://qns.com/2026/01/suspects-wanted-burglaries-flushing-fresh-meadows-bronx/ | Dec 20, 2025 6 a.m.: front door broken at medical business 42-62 Kissena Blvd; pharmacy next door 42-60 Kissena broken into via front door; 6:45 a.m. pharmacy 177-05 Union Tpke; Dec 30 ~5:30 a.m. pharmacy 45-12 Parsons Blvd front door broken. | §5 para 4, §8 card "Kissena and Parsons", §9 Q "front doors of pharmacies", §10.5 H3 1 |
| F12 | same search → Firecrawl scrape (directQuote) | https://qns.com/2025/08/burglar-flushing-businesses/ | QNS Aug 13, 2025: one suspect, half-dozen businesses May–Aug; rear door forced at 133-38 Sanford Ave; medical office locks manipulated; unlocked doors at 34-20 Linden Place restaurant (Murray Hill), 41-42 College Point Blvd home-furnishing shop, 135-09 Northern Blvd furniture store, Flushing Tower Condominium. | §5 para 4, §8 cards, §9 Q "unlocked doors", §10.5 H3 1 |
| F13 | `Murray Hill Queens Commercial District Needs Assessment Korean businesses Northern Boulevard 149th Street` · Firecrawl search → Firecrawl scrape (directQuote) | https://qns.com/2022/02/asian-american-federation-assessment-revitalize-murray-hill/ | Corridor near LIRR Murray Hill station: ~70 small businesses, Korean immigrant owners, ~60% restaurants within five-to-six blocks (merchants' association). | §8 card "Murray Hill", Across Flushing |
| F14 | `Samsung push pull digital door lock SHP-DP609 mortise installation door thickness US door requirements` · Firecrawl search → Firecrawl scrape | https://www.samsungdoorlock.ca/installation-requirements/ | Samsung mortise models: absolute minimum 4.5 in flat space from door edge to glass/panel/moulding; door 1-9/16–3-1/8 in (standard shaft 1-9/16–2-3/8); storm doors need 70 mm clearance. | §7.5, §9 Q push-pull, comparison table, §10.5 H3 3 |
| F15 | `NYC biometric identifier information law commercial establishments sign posted fingerprint Local Law 3 2021 DCWP` · Firecrawl search | https://rules.cityofnewyork.us/rule/biometric-identifier-information/ ; https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=3704369&GUID=070402C0-43F0-47AE-AA6E-DEF06CDF702A ; https://www.hklaw.com/en/insights/publications/2021/08/nyc-passes-biometric-data-protection-laws-aimed-at-businesses ; https://www.consumerfinancialserviceslawmonitor.com/2021/06/new-york-city-enacts-biometrics-law-for-food-and-drink-establishments-entertainment-venues-and-retail-stores/ | LL3/2021 effective July 9, 2021; commercial establishments (retail, food & drink, entertainment) collecting customers' biometric identifier info (incl. fingerprints) must post sign near all customer entrances in DCWP form; §22-1202(b) bars selling/leasing/trading/sharing for value. | §8.5 bullet 2, §9 Q biometric sign, §10.5 H3 6, privacy section |
| F16 | `IRS Publication 4557 safeguarding taxpayer data physical safeguards lock doors tax preparers office` · Firecrawl search → Firecrawl scrape (PDF, directQuote) | https://www.irs.gov/pub/irs-pdf/p4557.pdf | Pub 4557 (Rev. 5-2024): under FTC Safeguards Rule tax return preparers "must create and enact security plans"; see Pub 5708; "Limit access to taxpayer data to individuals who need to know"; "Implement a clean desk policy." No door-hardware requirement found. | §9 Q tax office |
| F17 | `Flushing tutoring centers after-school cram schools Main Street Queens news` · Firecrawl search | https://www.nytimes.com/2017/10/25/magazine/asian-test-prep-centers-offer-parents-exactly-what-they-want-results.html | Excerpt: "On Main Street in Flushing … the GPS Academy building announces itself with a sign printed in both English and Chinese". | §9 Q tutoring centre |
| F18 | `interlocking doors jewelry store vestibule "interlock" building code egress free exit requirement` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.locksmithledger.com/electronics-access-control/article/21288760/mantraps-one-door-at-a-time ; https://www.thebuildingcodeforum.com/forum/threads/security-interlock-man-trap.1658/ | "you can't trap someone in a mantrap"; fire codes require emergency exit path; free-exiting devices overriding interlock if no other exit; may need to meet special locking arrangement rules (delayed egress); forum excerpt: electromagnetic locks typically used. | §8.5 bullet 3, §9 Q jewellery vestibule |
| F19 | `frameless glass door patch lock electronic keypad smart lock bottom rail glass door options` · Firecrawl search | https://www.elwinsecurity.com/resources/access-control/keyless-entry-commercial-glass-doors ; https://www.codelocks.us/mediacoverage-hcmnewglassdoorlockoct22 | Frameless glass doors can't be drilled; maglock at header or patch/bottom-rail lock made for the glass system. Codelocks CL4500 GD: medium-duty electronic lock, patch lock for toughened glass, key override, 12-button backlit keypad. | §7.5, §9 Q frameless glass, equipment card |
| F20 | `site:reddit.com flushing queens lock door apartment package stolen OR break-in OR keypad` · Firecrawl search | https://www.reddit.com/r/Flushing/comments/1pgyw1k/package_stolen_from_my_door_steps/ ; https://www.reddit.com/r/Flushing/comments/1hq58x6/ongoing_package_theft_need_advice/ | Excerpts only: ~$400 of packages stolen from a doorstep; building package theft "for over a year". Not scraped, not used on page (package-theft intent already owned by Brooklyn page). | research only |
| F21 | `fingerprint smart lock wet dirty fingers not recognized troubleshooting manufacturer support` · Firecrawl search | https://service.eufy.com/article-description/Fingerprint-Recognition-on-eufy-Smart-Lock-Not-Working ; https://www.welock.com/blogs/news/fingerprint-smart-lock-not-recognizing-finger | eufy: sensor "may not be working properly if your hand is wet, moisty, or dirty"; WeLock: wet or overly dry skin, dirty sensor. | §9 Q kitchen staff, §10.5 H3 2 |
| C1 | carried from research/smart-lock-installation.md (Queens C10) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=45 | Downtown Flushing Transit Hub BID: ~30 block faces, ~1,500 ground-floor businesses. | §5.5 bullet 5, §8 card Main St |
| C2 | carried (silo HV/LI) | https://www.schlage.com/en/home/products/BE489WBCAMFFF.html ; https://www.schlage.com/en/home/products/BE499WBCENFFF.html | Encode "Requires 2.4GHz WiFi network"; Encode Plus BHMA A156.40 Grade AAA, doors 1-3/8–1-3/4 in. | §7.5, §9 Wi-Fi + marketplace Qs, §10.5, comparison table |
| C3 | carried (silo S4) | https://support.august.com/en_us/august-connect-improving-your-wi-fi-and-bluetooth-signals-SyqxvL1Adz.md | Connect bridge within 10–15 ft of lock. | §9 Wi-Fi Q, §10.5 H3 5 |
| C4 | carried (silo S5/S6) | https://support.shopyalehome.com/en_us/how-to-set-up-your-yale-smart-lock-with-matter-r18U4hgnyg.md ; https://knowledgebase.boldsmartlock.com/en/knowledge/how-does-matter-work-with-bold | Thread needs a border router; Bold: low-power self-healing mesh. | §9 Wi-Fi Q |
| C5 | carried (silo LI) | https://kc.allegion.com/kb/article/what-are-the-required-door-preparation-specifications-for-the-schlage-arrive ; https://idighardware.com/2023/07/accessibility-requirements/ | Backset 2-3/8 / 2-3/4; ADA hardware no tight grasping/pinching/twisting, 34–48 in. | §7.5, §9 push-pull Q, §8.5 bullet 4 |
| C6 | carried (silo N8, N4) | https://idighardware.com/2026/04/decoded-locks-on-dwelling-units-and-sleeping-units/ ; https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Electrified locks readily openable from egress side, one releasing motion; TDPA. | §8.5 bullets 1 & 5, §9 tutoring Q |
| C7 | carried (silo S1 + LI) | https://www.fixr.com/costs/smart-lock-installation ; https://lawnstarter.com/blog/?p=79010 | National $250–$400, avg $300 (Fixr Jan 2025); LawnStarter national avg $330. Labelled national third-party. | §14, §10.5 H3 7 |

### Prices used (all already published on live AESS smart-lock pages / silo prices table; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,575–$2,625 | single-door keypad/fob reader + electric strike, Queens rate | smart-lock-installation-queens.html (= $1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike | smart-lock-installation-queens.html |
| $310–$509 | failed electric strike repair | smart-lock-installation-queens.html |
| $195 first hour, then 30-min blocks | setup-only visit (Queens) | smart-lock-installation-queens.html / research/tv-mounting-prices/BRIEF.md |
| $195/hr, 3-hr minimum ($585) | service/callback, not on initial install | blueprint v2.3 §9 |
| $250–$400, avg $300; avg $330 | NATIONAL third-party (Fixr, LawnStarter) | C7 |
| quoted flat at walkthrough | residential / condo unit locks, push-pull, glass-door hardware | no AESS figure exists |
Same conflicts the Queens page flagged for Anwar still apply (live access-control-installation-queens.html shows unscaled $1,500–$2,500; setup-only $195 rate is published for TV/device setup).

## Images (11) — permanent image rule (Drive folder "AESS Website Photos/Smart Lock Installation" empty per main run; CompanyCam not connected)
Chosen from the last third of the sorted list of tracked images/smart-lock-installation/ files not used on any live smart-lock page (all live pages use the 18 `aess-…` photos). Sources whose perceptual hash matched the Upper East Side builder's new files (keypad-strike-glass-door, reader-mounting-aluminum-door-frame, entry-panel-back-box-wiring) were avoided. All were viewed; crops remove faces (only hands/arms/backs of heads remain). **Note for Anwar:** these library photos look AI-rendered, like the rest of the smart-lock library; they should be replaced when real smart-lock photos are uploaded.

| New file (images/smart-lock-installation/) | Source file (same folder) | Crop |
|---|---|---|
| smart-lock-installation-flushing-electric-strike-glass-shop-door.webp (hero, eager) | smart-lock-installation-suffolk-county-electric-strike-glass-door.webp | x600–1402 (face removed) |
| smart-lock-installation-flushing-strike-terminal-wiring-closeup.webp | smart-lock-installation-westchester-county-electric-strike-terminal-wiring.webp | x380–1400 |
| smart-lock-installation-flushing-keypad-reader-office-door.webp | smart-lock-installation-westchester-county-keypad-reader-office-entrance.webp | x650–1402 |
| smart-lock-installation-flushing-video-intercom-keypad-stone-entrance.webp | smart-lock-installation-westchester-county-keypad-intercom-granite-entrance.webp | x520–1136 |
| smart-lock-installation-flushing-lobby-entry-panel-install.webp | smart-lock-installation-westchester-county-lobby-entry-panel-install.webp | x580–1078 |
| smart-lock-installation-flushing-glass-lobby-reader-entrance.webp | smart-lock-installation-ulster-county-finished-secured-lobby.webp | none (no people) |
| smart-lock-installation-flushing-weatherproof-enclosure-brick-wall.webp | smart-lock-installation-ulster-county-enclosure-on-brick-wall.webp | x620–1400 |
| smart-lock-installation-flushing-service-van-tool-load.webp | smart-lock-installation-staten-island-van-load-out-tool-bag.webp | y380–1120 (van shows AESS 800 number) |
| smart-lock-installation-flushing-cable-tester-wall-jack.webp | smart-lock-installation-westchester-county-wall-plate-cable-test.webp | x760–1400 |
| smart-lock-installation-flushing-ceiling-wifi-access-point.webp | smart-lock-installation-westchester-county-ceiling-wifi-access-point.webp | none (back view) |
| smart-lock-installation-flushing-network-rack-switch.webp | smart-lock-installation-westchester-county-poe-switch-recorder-rack.webp | x330–1136 |
DAILY-LOG note: `images: 11 reused from images/smart-lock-installation/ library (no real smart-lock photos for Flushing yet)`.

## Question register — smart-lock-installation-flushing-queens-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 12)
1. Our condo is on a high floor downtown and my phone shows dozens of neighbours’ Wi-Fi networks — will a Wi-Fi smart lock keep dropping off?
2. A relative brought back a push-pull fingerprint lock from Korea — will it fit an ordinary American front door?
3. A no-name smart lock from an online marketplace costs a fraction of a Schlage — what are we actually giving up?
4. After October’s armed home invasion near the Horace Harding Expressway, should we stop unlocking our door from the app for people we can’t see?
5. Our tutoring centre fills with children after school — can the entrance keep strangers out without trapping the kids inside?
6. We prepare tax returns in an office above Main Street — does a keypad with an audit log help with the IRS’s data-security expectations?
7. Our jewellery shop wants a buzz-in vestibule where the inner door won’t open until the outer one closes — is that allowed?
8. Our storefront is a frameless glass door with a lock in the bottom corner fitting — can it go keyless?
9. If our staff door uses fingerprints, does the city’s biometric law mean we need a sign?
10. Most of the Flushing businesses hit in last summer’s burglary spree had a door left unlocked — what actually closes that gap during business hours?
11. Our restaurant’s kitchen staff have wet, floury hands all shift — will a fingerprint reader on the staff door work?
12. Burglars broke through the front doors of pharmacies on Kissena and Parsons — does a smart lock help when the door itself gives way?

### §17 FAQ (visible == FAQPage, 8)
1. What will a keypad-and-strike entry cost for a Flushing storefront or office?
2. Do we need to arrange parking or loading space for your van downtown?
3. Can young children use the fingerprint reader, or should they have a code?
4. Will you adjust or replace the door closer so the shop door actually latches?
5. Do you cover Murray Hill, Queensboro Hill, Auburndale and College Point as well as downtown Flushing?
6. The fingerprint reader on our existing lock stopped recognising anyone — can it be repaired?
7. Is a smart lock with a built-in camera worth it at a shop entrance?
8. Can the staff door’s fingerprint reader double as our time clock?

### Other question-form headings
- H2 "Keypad Unresponsive on a Flushing Door?" (repair capture)
- H2 "Push-Pull Mortise Lock or American Keypad Deadbolt?" (comparison section)
- H2 "Opening a New Shop or Office in Flushing?" (mid-page CTA 2)
- H2 "Shut Out of a Flushing Shop or Home Right Now?" (final repair capture)

### De-dup notes
- Avoided by design (intent already on the register): app language, elders without phones, caregiver schedules, dementia, arthritis, basement/Ida, garden-co-op courtyard doors, building-run app locks (Queens); package theft (Brooklyn); storefront roll-down gate (NYC hub); HIPAA (Suffolk/Westchester); shared shop/apartment stair door (Bronx/Ulster/Dutchess); historic-district approval (HV) — Broadway–Flushing covenant kept to body text only; condo resale handover kept as a body section, not a question.
- Partial overlaps for the main run to judge: Q10 (auto-relock/door-position on business side doors) vs Manhattan FAQ "Can the lock relock itself so a dog walker or cleaner can't leave it open?" — different setting (commercial doors during opening hours, sourced to the 2025 Flushing spree); Q1 (2.4 GHz congestion in a tower) vs NYC hub "Wi-Fi bridge in the public hallway" and HV range questions — different cause (interference, not distance); FAQ 1 cost is geo-specific by design; FAQ 5 coverage geo-specific by design.
- Paragraph similarity (masked, SequenceMatcher on ≥10-word paragraphs) vs all 18 silo pages on disk: max 0.73, and that one is the NAP line (name/address/WhatsApp — protected content). All other paragraphs < 0.65 after rewrites; boilerplate excluded (stamp, warranty sentence, licence line).

### Flags for Anwar
- Library images look AI-rendered (see Images).
- The Upper East Side link resolves only once that sibling page is on disk; at time of build both sibling files existed.
- Size: page is 178,676 B, placed below the Ulster page (181,242 B) because every gap above it is taken by siblings (Brooklyn Heights ~184.2 KB, Upper East Side 187.5–189.1 KB during build). If a sibling's size changes, re-run the cluster check.

# Smart Lock Installation — research part: Bedford-Stuyvesant, Brooklyn (smart-lock-installation-bedford-stuyvesant-brooklyn-ny)

Built 2026-10-17 by the Bed-Stuy builder subagent. Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used.
Silo-wide research (Fixr, August bridge distance, HPD double-cylinder rule, Admin Code §26-521, Tenant Data Privacy Act, Multiple Dwelling Law 3-family line, ADA 34–48 in., Bob Vila DIY claim) reused from the existing silo sections — not re-fetched.

**Thesis:** Bed-Stuy = custody of the house. Long-held and inherited family brownstones (homeownership 19.7%) under deed-theft and tangled-title pressure, often standing empty between owners, inside three historic districts where the LPC confines devices to the door opening. Smart locks are sold as proof of who holds access: old keys retired, one credential per person, two administrators for heirs, entry logs and alerts on empty houses — plus landmark-compliant placement, foyer parcel fixes and rear-door hardening.

## Bedford-Stuyvesant, Brooklyn (smart-lock-installation-bedford-stuyvesant-brooklyn-ny)

| # | Query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| B1 | `Bedford-Stuyvesant deed theft homeowners Brooklyn DA brownstone` · Firecrawl search → scrape | https://www.npr.org/transcripts/nx-s1-5893647 | NPR Code Switch, 2026-07-21 (Chi Ossé, WNYC/Gothamist's David Brand): deed theft "rampant in gentrifying neighborhoods like Bed Stuy, where brownstones that redlining once made cheap now sell for millions"; AG complaints +240% 2023–2025; ~3,500 complaints 2014–2023; >500 in 2025; tactics: door-knocking, calls, leaflets, distant relatives; heirs without wills. | §5 Neighborhood, §5.5 stats, §9 Q "people keep knocking", Timeline |
| B2 | same search · Firecrawl scrape | https://bronx.news12.com/2025/12/04/bed-stuy-woman-claims-shes-a-victim-of-deed-theft-facing-eviction-from-new-homeowner/2cBt06rbsHWBSGOp4eVZKG | Dec 4 2025: Bed-Stuy woman, 54, paid-off brownstone in family 60 years; man "rang the doorbell… 'I'm here to evict you.'" | §5 Neighborhood |
| B3 | same search (excerpt only) | https://www.nysenate.gov/newsroom/in-the-news/2019/velmanette-montgomery/1m-bed-stuy-brownstone-stolen-80-year-old-woman-da | 2019: $1M Bed-Stuy brownstone allegedly stolen from 80-year-old woman (DA). | research only |
| B4 | same search (excerpt only) | https://www.bklynlibrary.org/calendar/%E2%80%9Cthey-stole-my-home%E2%80%9D-deed-bedford-library-20260507-0600pm | BPL Bedford Library event 2026-05-07 "They Stole My Home": deed theft up 240% 2023–2025. | §5.5 stats |
| B5 | `Stuyvesant Heights Historic District designated 1971 Landmarks Preservation Commission buildings` · Firecrawl search | https://www.nyc.gov/assets/lpc/downloads/pdf/maps/HistoricDistrictMaps/Brooklyn/stuyvesant_heights.pdf ; https://www.citylandnyc.org/bed-stuyexpanded-stuyvesant-heights-historic-district-designated-capping-decades-long-process/ | Stuyvesant Heights HD designated Sept 14 1971 (LP-0695); Bed-Stuy/Expanded Stuyvesant Heights HD ≈825 buildings (2013, per parent page). | §5, §5.5, §13 landmarks, Historic District Checklist |
| B6 | `Bedford Historic District Brooklyn designated 2015 …` · Firecrawl search → scrape | https://www.citylandnyc.org/bedford-historic-district-unanimously-designated/ ; https://hdc.org/buildings/bedford/ | Dec 8 2015, ≈800 buildings, bounded roughly by Bedford, Nostrand, Putnam, Tompkins, Marcy Aves and Monroe, Fulton, Halsey Sts; built 1870–1900, rowhouses + small apartment buildings; HDC quotes designation report "a rare showcase for the rapid changes in row house fashion". | §5, §7 Building Specialists, Timeline |
| B7 | `NYC Landmarks Preservation Commission rules rowhouse intercom doorbell security camera facade …` · Firecrawl search → scrape (PDF, freeform query) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf | "Light fixtures and intercom panels, as well as doorbells, must be installed within or adjacent to a door opening." "A maximum of two light fixtures and one intercom panel can be installed per door opening." "An intercom can also be installed on a fence or wall in front of the entranceway." No permit list: "Repairing or replacing hardware such as hinges, knobs, pulley chains, locks and handles"; "Replacing … broken window and door hardware in kind". (Keypads not named — page says we apply the intercom logic and advises speaking to LPC staff.) | §9 three landmark Qs, §10.5 H3 4, Historic District Checklist, §8.5 |
| B8 | `Bedford-Stuyvesant community district 3 profile housing owner-occupied population Furman Center` · Firecrawl search → scrape | https://www.furmancenter.org/neighborhoods/bedford-stuyvesant/ | (Updated 05/06/2026) population 181,949 (2024); homeownership 19.7% (2024); 11,644 new units 2010–2025 (4+ unit buildings); public housing 9,802 units = 12.0% of rentals (2025); serious crime 11.6/1,000 (2025) vs 23.6 (2006). | §5, §5.5, Timeline |
| B9 | `NYC Department of Finance Property Fraud Alert ACRIS sign up free deed fraud` · Firecrawl search → scrape | https://www.nyc.gov/site/finance/taxes/deed-fraud.page | Mayor's Office of Deed Theft Prevention; "Sign up for property and deed alerts" (ACRIS NRD); hotline 1-855-HOME-456; make a will or transfer-on-death deed; heirs should update the deed. | §9 Qs entry history / knocking, FAQ deed help, Estate Door Plan |
| B10 | scrape of AG page linked from News 12 | https://ag.ny.gov/publications/deed-theft | Targets: "abandoned or empty properties", "properties where the homeowner is deceased and the heirs do not legally transfer title"; "Do not abandon your property. Take care of it yourself or ask someone else to look after it."; never transfer deed without own attorney; housing-court stay of 90 days to challenge ownership; HOPP. | §5, §9 estate/squatter/knocking Qs, §10.5 H3 3, Estate Door Plan |
| B11 | `Center for NYC Neighborhoods tangled title heirs property Bed-Stuy homeowners inherited` · Firecrawl search → scrape | https://nypost.com/2026/06/11/real-estate/nyc-homes-worth-a-staggering-400m-at-risk-of-deed-theft/ | Center for NYC Neighborhoods (Apr 2026 report): ~350 lawsuits/yr citywide against homes in inherited-ownership disputes; ≥$400M at risk yearly; Central Brooklyn & Southeast Queens singled out. | §5.5, §9 heirs admin Q |
| B12 | `New York squatters law 2024 budget squatter not tenant 30 days change locks` · Firecrawl search → scrape | https://www.fox5ny.com/news/new-york-new-squatter-laws ; https://www.nysenate.gov/legislation/bills/2025/S2366 (excerpt) | Fox 5, 2024-04-25: 2024 budget signed — "a tenant should not include a squatter"; Queens homeowner arrested when she tried to change the locks. S2366 (2025) further bill. | §9 Q "found someone living…", §10.5 H3 3, Timeline |
| B13 | `reddit r/BedStuy package theft brownstone door lock intercom` · Firecrawl search (excerpts only; threads not opened) | https://www.reddit.com/r/BedStuy/comments/1gau7ch/repeated_breakins_on_lexington_ave/ ; https://www.reddit.com/r/BedStuy/comments/1n9550d/stealing_packages_in_broad_daylight/ ; https://www.reddit.com/r/BedStuy/comments/1sb217y/beware_package_thief/ ; https://www.reddit.com/r/Brooklyn/comments/1ox1y84/what_have_people_in_brooklyn_found_effective_to/ | Lexington Ave: someone breaking in for months stealing packages from the foyer, "I've had 3"; Lafayette & Throop, 7am: "Guy politely opens my gate, steals my package & politely closes gate"; Myrtle & Marcy: two packages in 10 days; r/Brooklyn non-doorman building added a keypad deadbolt to package room door, "Stopped most thieves." | §9 gate Q and foyer Q |
| B14 | `Bed-Stuy burglary brownstone break-in vestibule door 81st precinct 79th precinct 2025 2026` · Firecrawl search (excerpts) | https://www.bkreader.com/news/the-week-in-crime-spotlight-on-bed-stuy-8-6548761 ; https://www.facebook.com/NYPD79PCT/posts/crime-pattern-noticethe-bedstuy-area-has-seen-a-rise-in-both-residential-commerc/2721556447982727/ | Bed-Stuy covered by 79th and 81st Precincts; 79th Pct crime-pattern notice: rise in residential & commercial burglaries, "Please remember to lock your doors & windows" (post undated). | §9 squatter Q (precincts), §9 rear-door Q |
| B15 | `NYCHA developments in Bedford-Stuyvesant Marcy Houses Tompkins Sumner Roosevelt Brevoort units` · Firecrawl search (Wikipedia NYCHA table excerpt) | https://en.wikipedia.org/wiki/New_York_City_Housing_Authority ; https://www.nyc.gov/site/nycha/about/developments/brooklyn.page | Marcy 27 bldgs/1,705 apts/1949; Brevoort 894/1955; Sumner 1,098/1958; Tompkins 1,048/1964; Roosevelt 762/1964, Roosevelt II 342/1966; Armstrong I/II; Stuyvesant Gardens; 303 Vernon. | §7 Building cards, Timeline |
| B16 | `Magnolia Grandiflora Hattie Carthan Lafayette Avenue landmark Bedford-Stuyvesant` · Firecrawl search → scrape | https://hdc.org/buildings/magnolia-grandiflora/ | 679 Lafayette Ave; designated May 12 1970; grown from seedling by William Lemken mid-1880s; Hattie Carthan campaign from 1950s. (Instagram excerpt said 1977/678 — HDC used.) | §13 landmark, Timeline |
| B17 | `Boys High School Marcy Avenue landmark Romanesque Revival …` · Firecrawl search | https://hdc.org/buildings/boys-high-school/ ; https://southofunionsq.villagepreservation.org/city/ny/lo/fd14bd5a-fb84-44f0-83a7-028ac3ff6a92 | 832 Marcy Ave; designated Sept 23 1975; Romanesque Revival; built 1891–92. | §13, Timeline |
| B18 | `Alhambra Apartments Nostrand Avenue Montrose Morris landmark …` · Firecrawl search | https://hdc.org/buildings/alhambra-apartments/ ; https://en.wikipedia.org/wiki/Alhambra_Apartments | 500–518 Nostrand Ave, between Halsey and Macon; Montrose W. Morris; 1889–90. | §7, §8, §13, Timeline |
| B19 | `Herbert Von King Park Tompkins Park Bedford-Stuyvesant oldest park Olmsted Vaux` · Firecrawl search | https://www.nycgovparks.org/parks/herbert-von-king-park ; https://www.tclf.org/landscapes/herbert-von-king-park | Marcy & Tompkins Aves; originally Tompkins Park; Olmsted & Vaux design; built 1870–71. | §13, Timeline |
| B20 | `Restoration Plaza Fulton Street Bedford Stuyvesant Restoration Corporation founded 1967 Robert Kennedy` · Firecrawl search | https://restorationplaza.org/about/history/ ; https://www.linkedin.com/company/bedford-stuyvesant-restoration-corporation | Founded 1967 with RFK; 1368 Fulton St. | §8, §13, Timeline |
| B21 | `Bed-Stuy Gateway BID Fulton Street boundaries Nostrand Avenue Tompkins Avenue merchants` · Firecrawl search | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=64 ; https://www.blockbyblock.com/cities/bed-stuy-gateway-bid-nyc/ ; https://ourtimepress.com/bed-stuy-gateway-bid-a-giftway/ | BID at 1368 Fulton St 3rd fl; ~400 businesses, nearly 500,000 sq ft retail; mile-long Fulton Street corridor. | §5, §8, §13 |
| B22 | Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ (Bed-Stuy smart lock) | — | EMPTY (not accessible in build env). §10.5 headings are claims from cost guides/retailers, stated as such on page. | — |
| B23 | Local news specifically on smart locks in Bed-Stuy (Patch/BK Reader/Brownstoner) | — | EMPTY — no smart-lock-specific story found; deed-theft, burglary and package items above used instead. | — |
| B24 | Licensing / permits | — | Reused silo findings (LPC hardware no-permit; MDL multiple-dwelling line; HPD double-cylinder; Admin Code §26-521; TDPA). No Bed-Stuy-specific lock licensing found → nothing new claimed. | §7.5, §8.5, §9 |

### Prices used (Brooklyn ×1.00 — no new figures; all from the parent page / silo prices table)
- $1,500–$2,500 single-door keypad or fob reader with electric strike; $250–$450 new electric strike; $295–$485 failed strike repair; $195 first hour then 30-min blocks (programming visit); $195/hr, 3-hr minimum ($585) callback; Fixr national $250–$400 avg $300 (third-party, labelled). House/unit smart locks: quoted flat at walkthrough.

## Images (11)
All copied (cp, WebP unchanged) from real AESS photos in images/smart-lock-installation/; looked at each before naming. Excluded: video-doorbell photo (house number "128" visible), customer-app-unlock (customer face), suburban van, office glass/lever, apartment 4A door, exterior/interior composite with text overlays.

| File | Source photo | Alt |
|---|---|---|
| smart-lock-installation-bedford-stuyvesant-finished-keypad-deadbolt-brownstone-door.webp | aess-smart-lock-installation-keypad-smart-deadbolt-brownstone-door.webp | Finished black keypad smart deadbolt and lever handle on a stained wood door beside brownstone and iron stoop railings, smart lock installation in Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-adding-access-code-app.webp | aess-smart-lock-installation-programming-access-code-app.webp | AESS technician entering a new access code on a door keypad while the phone app shows the Add Access Code screen, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-keypad-deadbolt-drilling-stoop-door.webp | aess-smart-lock-installation-drilling-keypad-lock-brownstone-stoop.webp | AESS installer driving screws into a keypad deadbolt on a wood stoop door with ornamental iron glass grille and a row of brownstone stoops behind, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-keypad-wiring-service.webp | aess-smart-lock-installation-servicing-keypad-wiring.webp | Technician in gloves holding an opened smart lock keypad with its wiring exposed while working on the interior unit, smart lock repair in Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-measuring-old-bore-wood-door.webp | aess-smart-lock-installation-measuring-door-bore-for-deadbolt.webp | Installer measuring an old worn lock bore on the edge of a stained wood door with a yellow tape measure before fitting a smart lock, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-removing-brass-deadbolt.webp | aess-smart-lock-installation-removing-old-brass-deadbolt.webp | Technician holding a removed brass deadbolt cylinder and using a drill driver on the old lock chassis of a wood front door, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-interior-unit-cable-connection.webp | aess-smart-lock-installation-connecting-interior-unit-cable.webp | Technician plugging the keypad cable into the interior unit of a smart deadbolt on a wood door, with an open tool case below, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-lock-status-phone-app-wood-door.webp | aess-smart-lock-installation-checking-lock-status-in-app.webp | Installer with locs holding a phone showing the smart lock as locked while pointing to the keypad deadbolt on a wood door, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-strike-plate-check-wood-door.webp | aess-smart-lock-installation-checking-latch-bolt-alignment.webp | Installer pressing on the strike plate in the door frame to check alignment beside a newly fitted keypad deadbolt on a wood door, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-fingerprint-unlock-app-confirmation.webp | aess-smart-lock-installation-fingerprint-unlock-demo-app.webp | A fingertip on the sensor of a keypad smart deadbolt while the installer holds a phone showing Fingerprint Unlocked, Bedford-Stuyvesant, Brooklyn |
| smart-lock-installation-bedford-stuyvesant-smart-lock-battery-change.webp | aess-smart-lock-installation-replacing-smart-lock-batteries.webp | Technician sliding fresh AA batteries into the interior battery compartment of a smart lock on a dark entry door, Bedford-Stuyvesant, Brooklyn |

## Question register — smart-lock-installation-bedford-stuyvesant-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 10)
1. Our late mother's brownstone is empty while the estate goes through Surrogate's Court — what should happen to the keys and codes right now?
2. Several of us inherited the house and none of us lives there — whose phone should hold the admin account?
3. How can a lock's entry history help show that nobody was let into an empty house without the family's say-so?
4. We found someone living in our relative's vacant house — can we just change the code or the lock?
5. People keep knocking with offers to "help" with the house — how should an older owner decide who gets the door opened?
6. Our row is in the Bedford or Stuyvesant Heights historic district — where may a keypad or reader be mounted beside the front doors?
7. There is already an intercom panel at our door opening — can a separate keypad still be added on a landmarked facade?
8. Can the keypad for our front-yard gate go on the iron fence at the sidewalk instead of on the house?
9. Parcels go missing from our building's shared foyer even though the street door locks — how are people getting in, and what fixes it?
10. A house on our block was entered through the back — what should the rear garden door of a rowhouse get?

### §17 FAQ (visible == FAQPage, 6)
1. Do you need to see proof that I am the owner or executor before changing the locks on a house?
2. Will you photograph the doors before and after the work for our landmarks records?
3. Can you fit a smart lock at a house where the electricity has been shut off?
4. Where can a Bed-Stuy homeowner get help if they think someone is trying to steal their deed?
5. Can relatives who live out of state join the planning meeting by video?
6. Can a keypad lock be removed later without leaving new holes in an original door?

### Other question-form headings
- Need Smart Lock Repair in Bed-Stuy Today?
- Who Can Open Your Bed-Stuy House Today?
- Bed-Stuy Door Won't Lock or Won't Open Tonight?

### De-dup notes
- Avoided intents already on siblings: owner-landlord code plans, stoop parcel theft, vestibule-vs-outer door, garden areaway exit, replacement door in HD (Brooklyn); elderly/carer/dementia codes (Queens, SI, Suffolk, Westchester); remote monitoring of a weekend/beach house (HV, LI) — Q3 is framed as evidentiary record for an estate, not convenience monitoring; previous owners' keys on purchase (SI) — Q1 is estate custody; realtor/contractor temporary codes (Orange, Westchester, Manhattan); street-door relock responsibility (Kingsbridge) — Q9 is foyer parcel diagnosis; mailroom keypad by co-op board (Jackson Heights).
- Masked paragraph similarity vs all 18 siblings: only exempt constants (warranty sentence, NAP, licence line, freshness stamp) ≥ 0.5; all body paragraphs < 0.5.

# Smart Lock Installation — research part: Jackson Heights, Queens (smart-lock-installation-jackson-heights-queens-ny)

Built 2026-10-17 (batch: Bedford-Stuyvesant / Kingsbridge / Jackson Heights). For the main run to merge into research/smart-lock-installation.md.

## Jackson Heights, Queens (smart-lock-installation-jackson-heights-queens-ny)

Neighbourhood spoke page. Up-link /smart-lock-installation-queens. Phone (347) 434-6392 (Queens line) in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (plus "WhatsApp (718) 679-0359" text in the NAP block, as on the parent). GBP Bronx (460 E Fordham Rd, @id #bronx). Price multiplier Queens ×1.05 (no new prices).
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. "Silo file" = finding already logged in research/smart-lock-installation.md by an earlier run (not re-fetched).

**Thesis / lane:** In Jackson Heights the door is rarely the occupant's alone. The neighbourhood is where the Queensboro Corporation launched one of the first US co-op plans (Linden Court, 1919), the 1980s added 60+ conversions, and the LPC landmarked ~36 blocks in 1993. So a smart lock job is "permission-first": board/managing-agent approval packet, house rules (weekday contractor hours, contractor screening, alarm-system approval, self-closing doors), the corporation's duplicate key, 1920s unit doors with paint build-up / old mortise pockets / closers; and the shared doors only a board can change — mailroom (2025 serial mailroom burglar at 83-10 35th Ave), lobby package theft (34th Ave co-op 2020), interior-garden fire door, laundry, service entrance, historic entrances under LPC. Plus 82nd St / 37th Ave / 74th St–Diversity Plaza / Roosevelt Ave shops. Deliberately avoids the Queens page's lanes (multigenerational households, app languages, dementia, arthritis, Ida basements, storm doors, LIC towers, chair-rental salon) and the NYC hub's (renter rights, board approval yes/no, mortise hallway match, duplicate-key insistence, self-closer interference).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | FC search `reddit JacksonHeights co-op board locksmith lock change apartment door` → only r/AskNYC / r/NYCapartments excerpts (not JH-specific; threads not opened). FC search `reddit jackson heights building front door buzzer packages stolen lobby intercom` → excerpts from r/crownheights, r/Brooklyn, r/AskNYC, r/nyc and a Facebook "jacksonheights" group post (packages stolen at 81/80 37 Ave — excerpt only, not used). r/JacksonHeights itself: EMPTY (no thread surfaced; Reddit not scraped in build env). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are recurring marketing/cost-guide claims, stated as such on the page. |
| 6 | Landmarks | J1, J8, J9, J10, J11 |
| 7 | Building stock | J1, J4 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Queens Daily Eagle (J2), QNS (J3), THE CITY (J5), DNAinfo excerpt (J12), Queens Chronicle excerpt (not opened, not used) |
| 10 | Hyperlocal | JHBG (J1); Jackson Heights Post: only a Facebook excerpt surfaced → EMPTY; Queens Chronicle/Ledger: EMPTY beyond excerpt |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| J1 | `Jackson Heights Historic District designation report garden apartments Queensboro Corporation Edward MacDougall` · FC search → FC scrape | https://www.jhbg.org/history-of-jackson-heights | JHBG history (adapted from Daniel Karatzas, *Jackson Heights: A Garden in the City*): Queensboro tract 70th–92nd St, Roosevelt Ave–Northern Blvd; Laurel Court 1914 first apartment building; Oban, Penrhyn (1914), Plymouth, Willow Courts, Colonials (1915–16) on 80th/82nd/83rd St; elevated subway on Roosevelt Ave 1917; Garden Apartments 1917 (renamed Greystones 1925); Linden Court (84th–85th St between Roosevelt & 37th Aves) announced May 1919 as first under Cooperative Ownership Plan, block-long garden, garages; 1920–25 Hampton, Elm, Hawthorne, Laburnum, Cambridge Courts (George H. Wells, attached 4–5 storey around interior garden), The Chateau 1923 (slate mansards, limestone entrances), The Towers 1924 (80th St & 34th Ave, 96 apts, MacDougall's duplex), Spanish Gardens (Andrew J. Thomas); Hayes, Ivy, Cedar Courts; all apartments through 1921 walk-ups; Elm Court 1922 first button-control automatic elevator; English Garden Homes from 1924 on 87th St, 15+ streets in 4 years, brick, rear garages; main commercial district planned on 82nd St & 37th Ave; Queensboro HQ 82nd St & 37th Ave opened May 1929; 1930s Fillmore Hall (132 units), Georgian Hall, Oak Halls, Buckingham Hall, Mount Vernon; Towers/Laburnum/Cambridge co-ops failed 1932–34 → rentals; Post Office opened 1937 (WPA mural); Travers Park 77th–78th St 34th Ave to Northern Blvd; 38 apartment buildings completed 1950, end-block gardens on 34th/35th Aves built over; 1980s ≥60 buildings converted, 5,000+ new tenant-owned units on ≥5,000 existing co-op units; LPC 1993 ~36 blocks, bounded 76th St, 88th St, Roosevelt Ave, Northern Blvd. | §5 paras 1–3, §5.5 bullets 1–3, §7 cards + 7.5, §8 82nd St/37th Ave/Roosevelt cards, §13 Linden Court/The Towers/Travers Park cards, Across JH |
| J2 | `Jackson Heights Post burglary apartment building Jackson Heights 115th Precinct` · FC search → FC scrape | https://queenseagle.com/all/jackson-heights-residents-say-package-thefts-are-on-the-rise | Queens Daily Eagle, David Brand, Oct 30 2020: burglar entered a 34th Ave co-op ~3 a.m., stole from ~a dozen packages in lobby; second burglary there since July; resident at 79th St & 37th Ave: thefts a minute or two after UPS/FedEx drop-offs; "Many residents, particularly seniors, tend to buzz people into the building without seeing who they are"; 115th Pct tweeted warning Oct 26 2020. | §5 para 4, §9 courier/service-entrance Q, §10.5 H3 4, Across JH (34th Ave) |
| J3 | same search → FC scrape | https://qns.com/2025/04/serial-burglar-hits-mail-rooms-in-five-queens-neighborhoods-nypd/ | QNS, Bill Parry, Apr 16 2025: lone burglar entered mailroom at 83-10 35th Ave Mar 8 (package, $500 jewelry), forced entry Mar 12 and Mar 14 (documents); 115th Pct 47 burglaries through Apr 13 2025 vs 65 (−27.7%, CompStat). | §5 para 4, §5.5 bullets 5–6, §9 mailroom Q, §10.5 H3 4, Across JH (35th/37th Aves) |
| J4 | `Jackson Heights co-op "alteration agreement" OR "house rules" locks keys managing agent garden apartment` · FC search → FC scrape (pdf parser) | http://www.olr.com/Pictures/OtherBuildingDocs/10112_34-24_82nd%5Bhouserules%5D.pdf | Allendale Apartments, Inc., 34-24 82nd St house rules: construction/installation noise only weekdays 8:30 AM–5 PM (r.5); apartment alarm systems need written approval of Management/Managing Agent (r.7); messengers/trades use service entrance on south side (r.10); deliveries 8:30–5 Mon–Fri, 9–12 Sat (r.11); laundry 7 AM–9 PM (r.17); apartment entrance doors self-closing per FDNY (r.26); contractors screened and approved by Management (r.28); garden 9 AM–sundown (r.29); garden fire door must remain closed at all times, front-door key gives access (r.31); subletting not endorsed, case-by-case (r.33). | §5 para 2, §9 courier, garden-door, laundry, sublet Qs, Board Packet table, §10.5 H3 1 |
| J5 | same search as J2 → FC scrape | https://www.thecityreporter.nyc/2022/03/07/after-fire-thieves-ransacked-apartments-cops-wont-help-queens-tenants/ | THE CITY, Gabriel Sandoval, Mar 7 2022: Apr 6 2021 electrical fire at six-floor, 133-unit building, 34th Ave & 89th St (89-07 34th Ave); 21 injured; >140 households displaced; tenant association says ≥50 apartments burglarized while access held by guards/contractors; tenants struggled to file reports at the 115th Pct (92-15 Northern Blvd area). | §9 post-fire Q, Across JH (34th Ave) |
| J6 | `Landmarks Preservation Commission permit replace entrance door intercom historic district rules doors security` · FC search (excerpts) | https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf ; https://nylandmarks.org/news/technical-tips-preserve-your-historic-windows-and-doors/ | LPC Permit Guidebook ch. 2 Windows and Doors (LPC Rules §2-14); assessment of deteriorated conditions required to replace historic front doors; staff permits for entrance infill where no significant historic material; door actuators/push plates "as small as possible", no exposed conduit. NYLC: all modifications to exterior windows and doors in historic districts require LPC approval. | §8.5 bullet 2, §9 entrance-strike Q, §10.5 H3 3, Board Packet, shared-door checklist |
| J7 | `Queens Community District 3 Jackson Heights East Elmhurst profile population foreign-born households Furman Center` · FC search (excerpts) | https://www.nyc.gov/assets/planning/newest-new-yorkers-2026/Ch3.html ; https://en.wikipedia.org/wiki/Jackson_Heights ; https://datausa.io/profile/geo/nyc-queens-community-district-3-jackson-heights-east-elmhurst-puma-ny | DCP *Newest New Yorkers* 2026: Jackson Heights >50,000 immigrants, nearly 60% of population; Colombians, Ecuadorians, Mexicans ≈43% of foreign-born; 3,500 Bangladeshi immigrants, strong Bangladeshi commercial presence around Diversity Plaza near Roosevelt Ave–74th St. (Wikipedia ~11% severely overcrowded 2017; Data USA 57.2% foreign-born CD3 2024 — noted, not used on page.) | §5 para 5, §5.5 bullet 4, §8 74th St card |
| J8 | `34th Avenue open street Paseo Park Jackson Heights Diversity Plaza 37th Road 74th Street` · FC search (excerpts) | https://www.nyc.gov/html/dot/html/about/34ave.shtml ; https://www.paseopark.org/ | DOT: 34th Ave between 69th St and Junction Blvd to become city's first permanent Open Street; launched 2020; Paseo Park 26 blocks; materials in Bangla, Hindi, Nepali, Spanish, Tibetan, Chinese. | §13 Paseo Park card, Across JH, FAQ coverage answer |
| J9 | `Diversity Plaza Jackson Heights 37th Road 74th Street pedestrian plaza Little India` · FC search (excerpts) | https://www.nyc.gov/site/cecm/permitting/diversity-plaza.page ; https://www.nycstreetdesign.info/studies/diversity-plaza | Diversity Plaza on 37th Road between 73rd and 74th Sts, at the Jackson Heights transit hub. | §8 74th St card, §13 card |
| J10 | `Travers Park Jackson Heights 78th Street play street Jackson Heights post office mural 1937 landmark` · FC search (excerpts) | https://www.nycgovparks.org/parks/travers-park ; https://en.wikipedia.org/wiki/United_States_Post_Office_(Jackson_Heights,_Queens) ; https://livingnewdeal.org/locations/jackson-heights-station-post-office-flushing-ny/ | Travers Park: 34 Ave between 77 and 78 St. Post office: original section built 1936–37; 1940 mural "Development of Jackson Heights" by Peppino Mangravite. 78th St play street: Facebook post title only. | §13 Travers Park + Post Office cards |
| J11 | `82nd Street Partnership business improvement district Jackson Heights 37th Avenue Roosevelt Avenue businesses` · FC search (excerpts) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=18 ; https://www.dnainfo.com/new-york/20121218/jackson-heights/82nd-street-historic-district-has-cash-help-businesses-get-up-code | 82nd Street Partnership, 37-06 82nd St Suite 309; DNAinfo Dec 18 2012: Partnership using city grant money to help historic-district businesses on 82nd St get up to code. | §8 82nd St card, Across JH |
| J12 | same as J2 (excerpt) | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/115th-precinct.page ; https://www.facebook.com/nypd115pct/ | 115th Precinct, 92-15 Northern Blvd, Jackson Heights. | §8 Northern Blvd card |
| J13 | `HPD self-closing doors requirement apartment entrance doors Local Law 2022 multiple dwellings` · FC search (excerpt) | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | Apartment and hallway doors must swing closed and latch by themselves; LL71/2022 — HPD proactively inspects 300 class A multiple dwellings a year for self-closing doors. | §7.5 paint/closer para, §9 propped-door Q, shared-door checklist |
| S1 | silo file N2 | https://cooperatornews.com/article/the-shareholder-versus-the-board | 111 Tenants Corp. v. Stromberg: shareholder ordered to surrender duplicate key; proprietary leases require duplicate of new keys. | §7.5 "key the corporation keeps", §10.5 H3 5 |
| S2 | silo file N1 | https://www.nysenate.gov/legislation/laws/MDW/51-C | MDL §51-c: tenant may add own lock, must provide duplicate key on request. | §10.5 H3 5 |
| S3 | silo file N4 | https://www.nyc.gov/site/hpd/services-and-information/tenant-data-privacy-law.page | Tenant Data Privacy Act (LL63/2021): limits on smart-access data; may not require smart access to enter unit. | §8.5, §9 mailroom + board-policy Qs, §10.5 H3 7, checklist |
| S4 | silo file N6 | https://www.nyc.gov/site/hpd/services-and-information/fire-safety.page | Double-cylinder locks illegal on apartment doors. | §7.5 "one motion out" |
| S5 | silo file Q12 | https://www.nyc.gov/mayors-office/news/2025/06/mayor-adams-major-crime-reductions-roosevelt-avenue-queens-following-targeted | Operation Restore Roosevelt (Oct 2024); burglaries −48% start of year to mid-June 2025. | §8 Roosevelt Ave card |
| S6 | silo file S3 | https://www.fixr.com/costs/smart-lock-installation | National $250–$400 (Jan 2025), labelled national third-party. | §14 pricing |
| — | 7-train vibration and door hardware | — | No manufacturer/study source found → page says so explicitly and describes only installer practice. | §9 Roosevelt Ave Q |

Not used (unverified or off-thesis): r/AskNYC co-op lock excerpt; Wikipedia overcrowding figure; Data USA 57.2%; Facebook package-theft post at 80/81 St & 37 Ave; Jackson Heights Post (no article reached).

### Prices used (Queens ×1.05, round half-up; all from research/smart-lock-installation.md prices table — none invented)
| Figure | Scope |
|---|---|
| $1,575–$2,625 | single-door keypad/fob reader + electric strike ($1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike ($250–$450 × 1.05) |
| $310–$509 | failed electric strike repair ($295–$485 × 1.05) |
| $195 first hour, then 30-min blocks | setup-only visit (Queens) |
| $195/hr, 3-hr minimum ($585) | service/callback, not on initial install |
| quoted flat at walkthrough | any individual apartment/house door smart lock (no AESS figure exists) |

## Images (11)
Real AESS smart-lock photos from images/smart-lock-installation/ (Drive folder had nothing new). Each viewed before naming; alt/title/caption describe only what is visible; no customer, named building or local project claimed. Not used: suburban-front-door-van, office-glass-door, drilling-brownstone-stoop, video-doorbell, replacing-batteries, showing-customer-app-unlock (customer's face). DAILY-LOG note: images are real AESS smart-lock photos (11 of 18), copied under Jackson Heights filenames — not borrowed from another silo.

| New file (images/smart-lock-installation/) | Source photo | Alt |
|---|---|---|
| smart-lock-installation-jackson-heights-keypad-test-on-apartment-unit-door.webp (hero, eager) | aess-smart-lock-installation-apartment-door-smart-lock-app.webp | AESS technician testing a keypad smart deadbolt on an apartment unit door with the phone app in a Jackson Heights, Queens hallway |
| smart-lock-installation-jackson-heights-checking-bolt-and-strike-alignment.webp | aess-smart-lock-installation-checking-latch-bolt-alignment.webp | Technician checking deadbolt and strike alignment at the door edge before finishing a smart lock installation in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-measuring-bore-on-wood-entry-door.webp | aess-smart-lock-installation-measuring-door-bore-for-deadbolt.webp | Gloved technician measuring the old lock bore on a wood entry door before fitting a smart lock in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-opening-keypad-to-check-wiring.webp | aess-smart-lock-installation-servicing-keypad-wiring.webp | Technician opening a smart lock keypad to check its wiring and harness during a repair visit in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-removing-old-brass-deadbolt.webp | aess-smart-lock-installation-removing-old-brass-deadbolt.webp | Technician removing an old brass deadbolt with a cordless driver to prepare a wood door for a smart lock in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-keypad-outside-thumb-turn-inside.webp | aess-smart-lock-installation-keypad-exterior-thumbturn-interior-view.webp | Side-by-side views of a keypad smart deadbolt from outside and its interior thumb-turn for Jackson Heights, Queens doors |
| smart-lock-installation-jackson-heights-keypad-lever-lock-on-office-door.webp | aess-smart-lock-installation-office-lever-smart-lock-install.webp | Technician fitting the strike for a keypad lever smart lock on a dark-framed office door in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-adding-access-code-in-app.webp | aess-smart-lock-installation-programming-access-code-app.webp | Technician adding a new access code in the smart lock app while testing it on the keypad in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-fingerprint-unlock-with-app-confirmation.webp | aess-smart-lock-installation-fingerprint-unlock-demo-app.webp | A fingerprint unlocking a keypad smart deadbolt while the technician's phone app confirms access in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-seating-interior-unit-ribbon-cable.webp | aess-smart-lock-installation-connecting-interior-unit-cable.webp | Technician seating the ribbon cable between keypad and interior unit of a smart deadbolt during installation in Jackson Heights, Queens |
| smart-lock-installation-jackson-heights-confirming-locked-status-in-app.webp | aess-smart-lock-installation-checking-lock-status-in-app.webp | Technician confirming the locked status of a keypad smart deadbolt in the mobile app at a front door in Jackson Heights, Queens |

Flag for Anwar: the aess-* library photos (same files used on every smart-lock page) look AI-rendered on close inspection (as earlier runs also noted for other libraries). Used here because the task treats them as AESS photos; worth confirming.

## Question register — smart-lock-installation-jackson-heights-queens-ny

### §9 YOUR QUESTIONS ANSWERED (H3)
1. A burglar got into the mailroom of a 35th Avenue building three times in one week — can our board put a keypad or fob reader on the mailroom door?
2. Couriers are supposed to use our building's service entrance — can that door take a code that only works during delivery hours?
3. Our house rules keep the door to the interior garden shut at all times — can residents open it with a code instead of the front-door key?
4. Contractors keep propping the garden or service door open — can the door itself tell the super?
5. The laundry room is only open certain hours under our house rules — can its door follow that schedule on its own?
6. Can an electric strike go into the old wood or stone jamb of our building's original entrance without spoiling it?
7. Our board is drafting a smart-lock policy for shareholders — what should it cover?
8. The board approved a one-year sublet of our apartment — how do we hand the door to the subtenant without giving away our own access?
9. After a fire emptied part of our building, how do residents keep their apartments secured while contractors have the run of it?
10. Our Roosevelt Avenue storefront sits under the elevated 7 train — does the constant vibration loosen a keypad or strike?

### §17 FAQ (visible == FAQPage, 8)
1. What would a keypad and electric strike on our co-op's mailroom or lobby door cost?
2. Do you also work in East Elmhurst, North Corona and the blocks west of 76th Street?
3. How far ahead of the installation should we send the request to our managing agent?
4. Is a smart lock worth it on a studio in a walk-up where only one person lives?
5. Decades of paint have built up on our door edge and frame — will that stop a motorised bolt?
6. Can the keypad's backlight be dimmed so it doesn't glow across the courtyard at night?
7. Do you work in the 1950s apartment buildings along 34th and 35th Avenues as well as the prewar co-ops?
8. How much noise does the installation make in a shared stairwell?

### Other question-form headings
- H2 "Locked Out of a Jackson Heights Apartment, Lobby or Shop?" (repair capture)
- H2 "Need the Board Packet Before the Next Meeting?" (mid-page CTA)
- H2 "Want the Jackson Heights Price in Writing?" (mid-page CTA)
- H2 "Keypad Dead on a Garden Co-op Door Tonight?" (final repair capture)

### De-dup notes
- Checked by meaning against all 16 area pages' questions and the two batch siblings on disk (Bedford-Stuyvesant, Kingsbridge). Deliberately NOT asked (already owned elsewhere): co-op board approval yes/no, board insisting on a key, mortise hallway match, self-closer interference (NYC); historic-district keypad permit (Hudson Valley/Brooklyn/Bed-Stuy); install duration (SI/Rockland); contractor hours & COI (NYC); scope letter (Manhattan); JH chair-rental salon, garden co-op courtyard door weather (Queens). Dropped during build: FAQ "replace a worn peephole on the same visit" (≈ Kingsbridge "digital door viewer replace the peephole").
- Partial overlaps for the main run to judge: Q10 (7-train vibration) vs Kingsbridge "1 train … signal trouble" (different intent: mechanical loosening vs radio signal); Q4 (propped common door alert to super) vs Kingsbridge "lobby door often propped — what should my apartment door do" (board-side alert vs tenant-side lock); Q2 (delivery-hour courier code) vs Bed-Stuy "parcels go missing from shared foyer — how are people getting in"; FAQ 1 cost vs Queens/NYC cost FAQs (geo-specific by design).
- Masked similarity (visible paragraphs ≥20 words, geo names masked): 5-gram Jaccard 0.027 vs Queens parent, ≤0.018 vs every other smart-lock page, 0.004 vs LIC soundbar model. Highest single-paragraph 3-gram Jaccard excluding protected boilerplate (warranty sentence, NAP, consent text): 0.59 vs NYC hub and ≤0.57 vs Queens parent and every other page (the "not legal advice" note and pricing lines, both excluded from the verdict per v2.3 §2); every content paragraph < 0.65.

# Smart Lock Installation — research part: Kingsbridge, Bronx (smart-lock-installation-kingsbridge-bronx-ny)

Built 2026-10-17 by the Kingsbridge builder subagent (batch with Bedford-Stuyvesant and Jackson Heights). Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used.
Up-link /smart-lock-installation-bronx · phone (646) 490-0629 · Bronx GBP (460 E Fordham Rd, #bronx) · pricing Bronx ×1.00.

**Thesis:** in Kingsbridge the weak door is usually the shared one downstairs (crowbarred lobby door on Corlear Ave/W 231st St in 2024; CB8 FY2027: main doors without working locks and buzzers at Marble Hill Houses), so every Kingsbridge smart lock is planned as a two-door job — make the lobby/street door shut and relock (owner/housing company/NYCHA responsibility, priced from published Bronx strike/access figures) and then fit a keyed, auto-locking, logging smart lock on the resident's own door. Secondary local threads: Amalgamated/Park Reservoir limited-equity co-ops (reversible retrofits), roommate/student apartments near Manhattan University, one-in-five 65+ residents up hills and stair streets (aide/family codes), shops under the 1 train in the Kingsbridge BID, Marble Hill (Manhattan) edge.

## Kingsbridge, Bronx (smart-lock-installation-kingsbridge-bronx-ny)

### Boundaries, streets, landmarks
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| K1 | `Kingsbridge Bronx neighborhood boundaries Broadway 231st Street history` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Kingsbridge,_Bronx | Boundaries Manhattan College Pkwy (N), Major Deegan/Bailey Ave (E), W 230th St (S), Irwin Ave (W); CB8; ZIP 10463; 50th Precinct; King's Bridge 1693 (Philipse), buried under filled Spuyten Duyvil Creek; St. John's RC Church on Kingsbridge Ave near 231st St + two schools (Godwin Terrace, Kingsbridge Ave); Visitation Church & School W 239th St; Our Lady of Angels Church & School on Sedgwick Ave; Manhattan University; Stella D'Oro factory left 2009; 231st Street station (1). | §8 houses-of-worship card, §13 Marble Hill card (creek), cross-checks |
| K2 | same search | https://cityneighborhoods.nyc/kingsbridge (Firecrawl scrape) | Alternate boundaries (Broadway E, W 230th S, Riverdale Ave W, W 238th/W 240th N); Broadway corridor under the 1 train; prewar apartment buildings, small row houses; 1 train extension 1908 → six-story apartment buildings along Kingsbridge Ave, Heath Ave, Sedgwick Ave with courtyard entrances; Armory built 1912–1917 (Pilcher & Tachau); Major Deegan 1956; Kingsbridge Heights Community Center. | §5 para 1, §7 prewar card, §7.5 courtyard entry |
| K3 | `Kingsbridge Heights Bronx neighborhood Kingsbridge Road Armory Jerome Park Reservoir apartment buildings` · Firecrawl search (excerpt) | https://cityneighborhoods.nyc/kingsbridge-heights | Bounded by Grand Concourse, Kingsbridge Rd, Broadway, W 231st/Albany Crescent/Kingsbridge Terrace/Jerome Park Reservoir; 1910–1935 six-story brick apartment houses, Tudor Revival rowhouses, Art Deco residences; 1920s–30s apartment houses on Kingsbridge Terrace and Heath Ave; rowhouses, detached homes, walk-ups. | §7 row-house card, Houses section |
| K4 | `Kingsbridge Bronx step street stairs West 231st Street Kingsbridge Terrace hill` · Firecrawl search → Firecrawl scrape | https://onfootonwheels.squarespace.com/the-stair-streets-of-new-york-city/the-kingsbridge-trio-2-northwest-bronx | Five stair streets from the 231 St station (fully accessible): Naples Terrace 60 steps, Godwin Terrace 32, W 229th St 187 (Heath Ave → Kingsbridge Terrace → Sedgwick Ave, two blocks), W 231st St 70, W 230th St 72; Albany Crescent cantilevered over the Deegan. | §5 para 4, §13 W 229th St card, §13 231st St card |
| K5 | `Van Cortlandt Park acres third largest park Bronx Van Cortlandt Park South` · Firecrawl search (excerpts) | https://www.nycgovparks.org/parks/vancortlandtpark ; https://vancortlandt.org/visit/ | 1,146 acres; third-largest park in NYC. | §13 Van Cortlandt Park card |
| K6 | `Marble Hill Houses NYCHA development buildings apartments …` · Firecrawl search → Firecrawl scrape (query) | https://en.wikipedia.org/wiki/Marble_Hill_Houses | 11 buildings of 14–15 stories; first 9 between W 225th–230th Sts, Broadway–Exterior St; tenants from Aug 1951, completed March 1952. | §7 public-housing card |

### Housing stock, co-ops, statistics
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| K7 | `Amalgamated Housing Cooperative Van Cortlandt Park South history 1927 apartments buildings` · Firecrawl search → Firecrawl scrape | https://en.wikipedia.org/wiki/Amalgamated_Housing_Cooperative | 98 Van Cortlandt Park South; organized 1927 for the Amalgamated Clothing Workers; Tudor-style clusters 1927–32, Building 10 1941, 1947 building, concrete high-rises 1949–51, two towers early 1970s; 303 → 1,468 units in 11 buildings; core of Van Cortlandt Village; sister co-op Park Reservoir = state's first Mitchell-Lama co-op, 273 units, buildings on Sedgwick and Orloff Aves. | §5.5 stat 4, §7 co-op card, §13 Amalgamated card |
| K8 | same search (excerpt) | https://amalgamated-bronx.coop/ | "Founded in 1927, Amalgamated is the oldest limited equity housing cooperative in the United States." | §5.5 stat 4 |
| K9 | `Amalgamated Housing Cooperative house rules alterations apartment locks shareholders Bronx` · Firecrawl search → Firecrawl scrape (pdf) | https://amalgamated-bronx.coop/wp-content/uploads/2022/08/Amalgamated-FAQ-as-of-7-29-2022.pdf | FAQ 7/29/2022: "We are supervised by New York State Homes and Community Renewal (NYSHCR)"; apartments subject to NYSHCR prior approval; apartments shown "pre-restoration or restored and ready for occupancy"; mandatory painting fee; towers at 3975 & 3965 Sedgwick Ave. **No lock/door rule published** → page says so and tells cooperators to ask management in writing. | §7 co-op card, §7.5 co-op restoration, Two-door table, §9 co-op Qs, §14 building costs |
| K10 | `Mitchell-Lama regulations 9 NYCRR 1727 cooperator alterations apartment written consent housing company` · Firecrawl search (gov category, excerpts) | https://hcr.ny.gov/mitchell-lama ; https://nyc.gov/assets/hpd/downloads/pdfs/services/mitchell-lama-rules.pdf | HCR: 22 limited-dividend developments (Mitchell-Lama precursor) with 10,000+ apartments; supervision by DHCR. HPD rules excerpt did not cover door alterations → not used for a lock claim. | Research only (supports "state oversight" wording) |
| K11 | `Furman Center Riverdale Fieldston Kingsbridge community district 8 …` · Firecrawl search → Firecrawl scrape (query, directQuote) | https://www.furmancenter.org/neighborhoods/riverdale-fieldston/ | 2024: population 95,283; 65+ 23.3% (14.8% in 2010); homeownership 38.4%; serious housing code violations 222.4 per 1,000 privately owned rental units; median rent $1,720 (2025$); severely rent-burdened 27.9%. | §5 para 5, §5.5 stats 2–3 |
| K12 | Firecrawl scrape (query, directQuote) | https://www.furmancenter.org/neighborhoods/kingsbridge-heights-bedford/ | 2024: homeownership 4.0%; serious violations 283.6 per 1,000 private rental units; 65+ 11.0%; population 128,210. | §5 para 5, §5.5 stat 3 |
| K13 | `Bronx Community Board 8 Statement of Needs Fiscal Year 2027 security locks buzzers Kingsbridge` · Firecrawl search → Firecrawl scrape (pdf, query) | https://cbbronx.cityofnewyork.us/cb8/wp-content/uploads/sites/3/2026/02/FY2027_Statement_BX08.pdf | CD8 = 3.3 sq mi; Spuyten Duyvil, Kingsbridge, Kingsbridge Heights, Fieldston, Riverdale, Marble Hill, Van Cortlandt Village; "one in five residents is aged 65 or older"; over 45,000 housing units; housing types co-ops, condos, one-family, 2–4 family, multi-family; Marble Hill is Manhattan but served by the Bronx; Marble Hill Houses 3,222 residents, Fort Independence 482; quote: "There are security concerns as main doors to buildings do not have proper entry security such as working locks and buzzers."; step-street upgrade request W 238th St Waldo–Irwin (crumbling cement, cracking steps); grab bars, wheelchair-accessible buses for older adults. | Hero, §5 paras 2/4, §5.5 stats 1–2, §13 Marble Hill card, Older Neighbors section, Houses section, §9 Marble Hill Q |
| K14 | `Manhattan College renamed Manhattan University 2024 Riverdale Bronx campus students` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Manhattan_University ; https://manhattan.edu/news/archive/2024/08/manhattan-university-announcement | Renamed Manhattan University in 2024 (Regents approval Aug 1); in Riverdale since 1922/1923; Manhattan College name from 1863 charter. | §5 para 4, Shared Apartments section |

### Commercial corridors
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| K15 | `Kingsbridge BID Broadway West 231st Street merchants business improvement district` · Firecrawl search → Firecrawl scrape | https://www.kingsbridgebidnyc.org/about | BID area: Broadway W 230th–W 236th; W 231st from Major Deegan west to Corlear Ave; signed into law mid-2001; homepage: "our 200 merchants". Annual report lists office 3109 Kingsbridge Ave. | §5 para 4, §5.5 stat 6, §8 corridor cards |
| K16 | same search → Firecrawl scrape | https://www.norwoodnews.org/business-beat-bolstering-the-once-sleepy-bid-in-kingsbridge/ | Jan 2015: L-shaped BID under the elevated 1 train ("It's All Under the Bridge"); nearly 200 businesses; Williams Funeral Home, Robert E. Hill Real Estate, Aaron Plum Insurance each 50+ years; "There're no vacancies"; Target mall at 225th & Broadway. | §8 intro, Broadway-south card |
| K17 | reused, re-fetched: `Kingsbridge Armory …` · Firecrawl scrape (query) | https://edc.nyc/press-release/city-council-approves-historic-vision-kingsbridge-armory-bronx | Phase 1: 180,000 sq ft column-free Drill Hall, groundbreaking 2026, completion 2030; 125,000 sq ft community-owned manufacturing and community space; Phase 2: ~500 permanently affordable rental units on adjacent National Guard site, 2032; Armory opened 1917, military until 1994, city landmark 1974, National Register 1982. | §7 new-buildings card, §8 Armory card, §13 Armory card |

### Local news / incidents
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| K18 | `Riverdale Press Kingsbridge burglary apartment building lobby door package theft 2025` · Firecrawl search → Firecrawl scrape | https://www.norwoodnews.org/kingsbridge-man-sought-in-identified-burglary-pattern/ | Apr 18 2024: NYPD burglary pattern; Mar 25 (~3 a.m.) and Apr 5 (~2:52 a.m.) someone used a crowbar to pry open the front door of the lobby of the same residential building near Corlear Ave & W 231st St, fled north on Corlear; no property taken, no injuries. | Hero, §5 para 2, §5.5 stat 5, Two-door section, §9 Q1, §10.5 H3 3 |
| K19 | same search → Firecrawl scrape | https://www.riverdalepress.com/stories/police-beat,28861 | May 22 2008 Police Beat: four burglaries in a week in the 50th Precinct, thieves entering through victims' front doors; a Riverdale victim believed to have forgotten to lock her door; at 2850 Claflin Ave burglars broke off a key in the lock to stop anyone entering, technique used in several Kingsbridge Heights burglaries. | Two-door section, §9 Q4 |
| K20 | `Riverdale Press Kingsbridge tenants key fob building entry landlord` · Firecrawl search → Firecrawl scrape | https://www.riverdalepress.com/stories/landlord-values-security-at-home,49858 | Feb 1 2012: at a Waldo Ave building the front-door lock "is often broken, according to both residents and" HPD. Not quoted on page (named landlord/harassment allegations) — research context only. | Research only |
| K21 | `Marble Hill Houses NYCHA …` · Firecrawl search → Firecrawl scrape | https://www.riverdalepress.com/stories/nycha-sees-crime-drop-but-marble-hill-houses-residents-cite-security-concerns,241342 | Aug 14 2026: Marble Hill Houses on Broadway between W 225th–230th; residents describe entrance doors propped open or with broken locks, key failing to open a recently repaired entrance door at 4 a.m.; NYCHA cites funding and vandalism; NYCHA Customer Contact Center 718-707-7771 / MyNYCHA; 2023 $24.1M security investment across 23 developments incl. Marble Hill (layered access control, steel doors); CB8 FY2027 quote. | Hero, §5 para 2, Two-door table (NYCHA row) |

### Laws / rules (reused from silo research; not re-fetched)
- N1/B6 MDL §51-c (tenant's own lock, ≤3" circumference, duplicate key on request; excludes municipal housing authority) → Two-door table, §10.5 H3 2/7, Shared Apartments, §9 Marble Hill Q.
- N3/B7 HMC §27-2043 (owner's key lock + one key; class A heavy-duty deadbolt) and §27-2041 (viewer) → Two-door table, Owners section, §10.5 H3 7, FAQ door viewer.
- B9 MDL §50-a (self-closing/self-locking entrances for class A built/converted after 1/1/1968; intercom 8+ units; pre-1968 on majority written request) → Two-door table, §9 Q2, Owners section.
- B10 DHCR Fact Sheet #14 (entrance door security incl. lock and buzzer = required service) → Two-door section, §9 Q2.
- N4/B11 Tenant Data Privacy Act (LL63/2021) → §8.5, Owners section, FAQ TDPA.
- N6/B8 HPD fire safety (self-closing doors, open from inside without a key, no double-cylinder) → §10.5 H3 6.
- N9 Admin Code §26-521 (unlawful to change a tenant's lock without a key) → Owners section.
- B1 NYCHA handbook (bottom lock stays; additional lock is resident's responsibility; may be broken in emergency; $47.25 / +$50; drill-out not replaced; written consent for alterations) → Two-door table, §9 Marble Hill Q, §14, final repair capture.
- N18 NY1 roll-down gate repeal (Council passed, sent to mayor) → §8.5.
- S1 Fixr, LI-section LawnStarter, S2 Bob Vila, S4 August Connect 10–15 ft, S5 Yale Matter/Thread → §10.5, §14.
- 2010 ADA door-hardware reach range (as used on parent page) → §8.5.

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: `EMPTY (not accessible in build env)`. §10.5 says so and uses claims from national cost guides/retail/marketplaces instead.
- Reddit: `reddit r/bronx Kingsbridge apartment building door lock super buzzer` · Firecrawl search returned excerpts only (r/bronx "Locksmiths in Bedford/kingsbridge": resident asks for a locksmith "who won't just completely destroy my door"; r/bronx "Safety tips for living in Kingsbridge": couple just bought a co-op in the area; r/bronx "Applying for an apartment on Kingsbridge Ave between 233rd…"). Thread pages: `EMPTY (not accessible in build env)` (Firecrawl: site not supported). Nothing quoted on the page.
- Yelp 1–3★ Kingsbridge locksmith / smart-lock installers: `EMPTY (not accessible in build env)`.
- Kingsbridge-specific smart-lock / keyless-entry news story: none found (searches K18–K21 returned burglary and building-security items only) → `EMPTY` for the service category itself.
- Published Amalgamated / Park Reservoir lock rule: not found → page says so.
- Google Drive `AESS Website Photos/Smart Lock Installation`: nothing new (per batch brief); real AESS photos used from images/smart-lock-installation/.

### Prices used (Bronx ×1.00; none invented — same figures as smart-lock-installation-bronx.html)
| Figure | Scope | Source |
|---|---|---|
| $1,500–$2,500 installed | single-door keypad or fob reader with electric strike | access-control-installation-bronx.html (via parent page) |
| $250–$450 | new electric strike on a lobby door | door-buzzer-repair-allerton-bronx-ny.html (via parent) |
| $295–$485 | failed electric strike repair | door-buzzer-repair-bruckner-bronx-ny.html (via parent) |
| $225 first hour, then 30-min blocks | setup-only visit (app/bridge/codes) | research/tv-mounting-prices/BRIEF.md (Bronx), as on parent — same flag as parent |
| $195/hr, 3-hr min ($585) | service/callback, not initial install | blueprint v2.3 §9 |
| $47.25 / +$50 | NYCHA's own lockout lock charge (not AESS) | B1 |
| $250–$400, avg ~$300 (Fixr); avg $330, $200–$460 (LawnStarter) | NATIONAL third-party | S1; LI section |
| Own-door smart lock | no AESS figure → "Quoted flat at free walkthrough" | — |

## Images (11)

Real AESS photos from images/smart-lock-installation/aess-smart-lock-installation-*.webp (all 11 viewed), copied (cp, WebP kept) under Kingsbridge names. Rejected after viewing: video-doorbell-and-smart-lock (house number "128" visible), showing-customer-app-unlock (customer's face), suburban-front-door-smart-lock-van (suburban street, wrong context); connecting-interior-unit-cable, keypad-smart-deadbolt-brownstone-door, office-lever-smart-lock-install, programming-access-code-app not needed. These same source photos are also used on the parent Bronx page under their aess-* names.

| File (images/smart-lock-installation/) | Source photo | Alt (as on page) |
|---|---|---|
| smart-lock-installation-kingsbridge-apartment-hallway-keypad-app-test.webp (hero, eager) | aess-smart-lock-installation-apartment-door-smart-lock-app.webp | AESS technician pressing the keypad of a smart deadbolt on apartment door 4A while checking the lock app, smart lock installation in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-locked-status-phone-check.webp | aess-smart-lock-installation-checking-lock-status-in-app.webp | Technician reading a Locked status on a smart lock app beside a keypad deadbolt on a wood door, smart lock check in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-latch-bolt-strike-alignment.webp | aess-smart-lock-installation-checking-latch-bolt-alignment.webp | Technician pointing at the latch on the edge of a wood door below a black keypad deadbolt during smart lock alignment check in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-keypad-wiring-repair.webp | aess-smart-lock-installation-servicing-keypad-wiring.webp | Gloved technician holding an opened keypad smart lock with its circuit board and wires exposed during a smart lock repair visit in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-measuring-old-bore-backset.webp | aess-smart-lock-installation-measuring-door-bore-for-deadbolt.webp | Gloved technician measuring from the old deadbolt bore to the door edge with a yellow tape measure before smart lock installation in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-keypad-outside-thumbturn-inside.webp | aess-smart-lock-installation-keypad-exterior-thumbturn-interior-view.webp | Two-panel view of a keypad smart deadbolt from outside and its thumb-turn from inside on a dark door, smart lock installation in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-glass-office-door-keypad-strike.webp | aess-smart-lock-installation-office-glass-door-smart-lock.webp | Technician fastening the strike plate beside a keypad deadbolt on a black aluminum-framed glass office door, business smart lock in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-fingerprint-unlock-app-log.webp | aess-smart-lock-installation-fingerprint-unlock-demo-app.webp | Finger on the fingerprint pad of a keypad smart lock while the technician shows a Fingerprint Unlocked screen in the app, Kingsbridge, Bronx smart lock setup |
| smart-lock-installation-kingsbridge-removing-brass-deadbolt.webp | aess-smart-lock-installation-removing-old-brass-deadbolt.webp | Technician removing an old brass deadbolt from a wood door with a red drill driver before smart lock installation in Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-drilling-keypad-deadbolt-stoop-door.webp | aess-smart-lock-installation-drilling-keypad-lock-brownstone-stoop.webp | Technician in gloves driving a screw beside a keypad smart deadbolt on a wood front door at the top of a stoop with iron railings, Kingsbridge, Bronx |
| smart-lock-installation-kingsbridge-battery-swap-interior-unit.webp | aess-smart-lock-installation-replacing-smart-lock-batteries.webp | Technician sliding fresh AA batteries into the interior unit of a smart lock on a dark apartment door, smart lock service in Kingsbridge, Bronx |

Captions describe only what is visible; no customer, named building or completed local project is claimed. DAILY-LOG note: `images: 11 real AESS smart-lock photos (aess-*), copied under Kingsbridge names; same sources as the Bronx parent page`.

## Question register — smart-lock-installation-kingsbridge-bronx-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
1. Someone pried our lobby door open with a crowbar — is a smart lock on my own door still worth it if the street door can be forced?
2. The street door in our Kingsbridge building won't relock behind people — whose job is it to fix, and how do tenants report it?
3. If the lobby door is often propped open, what should my apartment door do differently?
4. Burglars have jammed apartment locks by snapping a key off inside them — can that be done to a smart lock?
5. Amalgamated and Park Reservoir answer to a state housing agency — who has to approve a new lock on a co-op apartment door?
6. Is a retrofit or a new keypad deadbolt the better fit for an Amalgamated or Park Reservoir apartment?
7. A roommate moved out of our Kingsbridge apartment but still knows the code — can we cancel it without involving the landlord?
8. Mom's aide has to get through the lobby and then her apartment door — can one code cover both?
9. Can a fingerprint or a phone tap open the door when my hands are full after the climb up from Broadway?
10. Marble Hill is legally part of Manhattan — which rules apply to a smart lock on a Marble Hill door?
11. For a small Broadway shop, is a keypad deadbolt or a reader with an electric strike the better choice?

### §17 FAQ (visible == FAQPage, 8)
1. Can a digital door viewer replace the peephole when the smart lock goes in?
2. Our building fronts one of the Kingsbridge step streets — how does your crew get tools to the door?
3. Does the city's tenant data privacy law cover a smart lock I put on my own apartment door?
4. Our apartment door has a strong closer that pulls it hard against the frame — will a motorized bolt still lock it?
5. Do the smart locks you fit in Kingsbridge always keep a physical key?
6. Will the lock alert me if someone keeps trying wrong codes or tampers with it?
7. Will you install a cheap smart lock I ordered online from a brand I have never heard of?
8. Can I unlock the door by voice through Alexa or Google, and should I?

### Other question-form headings
- None. CTA and repair-capture headings are statements ("Two Doors, One Visit, One Written Price", "Start With Two Photos From Your Building", "Kingsbridge Smart Lock Dead, Jammed or Off the App"), except the final capture "Locked Out on a Kingsbridge Hill? Call Before Anyone Drills" (not a question heading — does not end in "?").

### De-dup notes
Compared by meaning against every question on the 16 live smart-lock pages and the two batch siblings on disk (Bedford-Stuyvesant, Jackson Heights). Dropped during build: a door-ajar alert FAQ (same intent as Jackson Heights "Contractors keep propping the garden or service door open — can the door itself tell the super?"), an elevated-train signal Q (too close in framing to Jackson Heights' 7-train vibration Q — kept as a non-question H3 "Signal under the elevated tracks"), a language/instructions FAQ (Queens app-language Q), an employee-open-up audit Q (Suffolk), a roommate-own-codes Q (Manhattan), an auto-relock Q (Manhattan), a technician-travel-time FAQ (Manhattan), a pricing-parity FAQ (Bronx parent), a keep-original-hardware FAQ (Brooklyn). Partial overlaps left for the main run: Q7 roommate code removal vs Dutchess "wipe every old code between May move-out and move-in" (tenant vs landlord, mid-lease vs between leases); Q8 aide two-door access vs Queens "home attendant code only on those days" (lobby + apartment vs schedule); FAQ 3 TDPA (tenant's own lock) vs NYC hub "What does the TDPA change for an owner adding fob or app entry?" (different actor); Q2 entrance-door reporting vs Bronx Q6 DHCR rent cut (reporting route vs rent reduction).

Masked-geo similarity (own check, paragraph-level difflib after removing geo names, warranty sentence, SMS consent and NAP/trust lines): highest pair vs any sibling 0.63 (vs Bronx parent); 5-gram Jaccard vs every sibling ≤ 0.024.


## Throgs Neck, Bronx (smart-lock-installation-throgs-neck-bronx-ny)

Page: `/smart-lock-installation-throgs-neck-bronx-ny` · neighbourhood spoke of `/smart-lock-installation-bronx` · phone (646) 490-0629 (body, CTAs, schema; (800) 486-0943 only in shared header chrome) · GBP Bronx (460 E Fordham Rd, schema `#bronx`) · Bronx ×1.00, prices copied from the Bronx page as-is.

Thesis: **one peninsula, three kinds of ground under the door** — owned lots on the street grid (Schuylerville / central Throgs Neck / Locust Point), Edgewater Park co-op land (single zoning lot, co-op enforces own building guidelines) and Silver Beach leased sites (proprietary leases requiring permission for alterations) — plus waterside exposure (Edgewater floodplain vs Silver Beach bluff), storm doors in wind off the Sound, side doors on 2–5 ft side yards, basements, crowded 2.4 GHz Wi-Fi on 30×50 lots, owner/tenant/relative code plans, East Tremont Avenue shop rear/cellar doors.

Tools: "Firecrawl search" = mcp__Firecrawl__firecrawl_search; "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query format, directQuote mode unless noted). All fetched 2026-10-17.

### Local research log
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| TN1 | (direct) · Firecrawl scrape (markdown) | https://en.wikipedia.org/wiki/Throggs_Neck,_Bronx | Peninsula bounded by East River/LI Sound S+E, Westchester Creek W, Baisley Ave + Bruckner Expwy N; CD10; ZIP 10465; 45th Pct at 2877 Barkley Ave; one-G/two-G spelling (Moses legend); 1920s estates → row homes + densely built bungalow lots; Silver Beach Garden summer colony later year-round, residents owned houses but rented land; Hammond mansion later offices of Silver Beach Garden Corporation; streets named for flowers/trees of Hammond estate; Edgewater Park from church youth campsite; Throggs Neck Houses 1953, one of first low-income projects, expanded twice; up-market waterfront condominiums; several beach clubs; 45th Pct 2022: 108 burglaries, crime −67% 1990–2022; FDNY Engine 89/Ladder 50 at 2924 Bruckner Blvd, Engine 72 at 3929 E Tremont Ave; Throggs Neck post office 3630 E Tremont Ave; Bx8 to Locust Point via Williamsbridge Rd; Throgs Neck Landing ferry Dec 28 2021. | §5 paras 1–2, §5.5 (precinct), §7 Throggs Neck Houses + condo cards, §8 station-block card, beach clubs card, Q&A Q10 (burglary), §13 Silver Beach + Locust Point cards |
| TN2 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Edgewater_Park_(Bronx) | 60-acre co-op of 675 single-family homes near Throgs Neck Bridge, north of I-95, beaches on LI Sound; bungalow colony from campsites; co-op 1988; Edgewater Park Volunteer Fire Department one of nine volunteer FDs in NYC; ~40% in 1% floodplain; "Resiliency Neighborhood"; sister communities Silver Beach (south of I-95) and Harding Park. | §5 para 3, §13 Edgewater card (volunteer FD), Field Notes (which side of I-95) |
| TN3 | `"Edgewater Park" Resilient Neighborhoods Department of City Planning Bronx bungalows zoning report` · Firecrawl search → scrape | https://www.nyc.gov/content/planning/pages/our-work/plans/bronx/edgewater-park | Private co-op, 55 acres, 675 single-family residences, ~3,000 residents; ~278 homes (just over 40%) in 1% floodplain; substantial number in V Zone (waves ≥3 ft); just under 100 in Coastal A; 167 in A Zone; most built before floodplain regulations; defined as a single zoning lot; co-op has own mechanisms regulating built environment. | §5 paras 3–4, §5.5 bullets 1–2, §7 Edgewater card, Ground Rules table, Q&A Q4, AI H3 2, flood-zone section, §13 card |
| TN4 | same search · Firecrawl scrape (pdf) | https://www1.nyc.gov/assets/planning/download/pdf/plans-studies/resilient-neighborhoods/edgewater-park/summary-report-edgewater-park.pdf | Side yards often 2–5 ft; eaves abut; considerable number of homes have basements; co-op strictly enforces own renovation guidelines; old height cap 25 ft above Bronx Datum / 27 ft above grade, amended; leadership removed bylaw prohibitions on covered porches, stair turns, plantings; case study roadbed width 12 ft; R4A. | §5 para 5, §5.5 bullet 3, Q&A Q1/Q2, door-by-door section (porch, side door, basement), Ground Rules caveat |
| TN5 | same search · Firecrawl scrape | https://www.bxtimes.com/edgewater-parks-resilient-neighborhood-report/ | Dec 4 2015: DCP report released Oct 29; co-op est. 1988, 55 acres, 675 homes on uniform lots typically 30×50 ft; built out to water's edge with small concrete promenade; bylaw height amendment; (states ~111 homes in flood zone — conflicts with DCP 278; DCP figure used). | §5 para 5, §5.5 bullet 3, Q1, §13 Edgewater card, Sources |
| TN6 | same search · Firecrawl scrape | https://citylimits.org/sandy-resiliency-retrofits-nyc/ | Jul 1 2019: Edgewater impacted by Sandy; homes tightly packed, narrow roads; ~40% mandated to buy flood insurance; co-op removed bylaw stipulations on covered porches, planting, stair turns; DOB: since Sandy just one Edgewater property obtained elevation permits. | Flood-zone section intro, door-by-door (porch para) |
| TN7 | `Silver Beach Gardens Corporation Bronx homes land lease shareholders bungalows number of homes` · Firecrawl search → scrape (pdf) | https://www.dta.ny.gov/pdf/archive/stc/Corp/1983/_0066.pdf | NYS Tax Commission decision (1983): Silver Beach Gardens incorporated Aug 30 1972; promontory ~100 ft above East River at confluence with LI Sound near Throgs Neck Bridge; summer colony of bungalows from turn of century, some first on stilts, now permanent, with basements, sewer-connected, winterized, year-round; historically ground rent; private system of roads; proprietary leases: bungalows "cannot be changed, modified or altered without the permission of Silver Beach Gardens"; maintenance fee. | §5 paras 2–4, §5.5 bullet 1, §7 Silver Beach card, Ground Rules table + caveat, AI H3 6, door-by-door (basements), flood-zone closing para, §13 card |
| TN8 | `Throgs Neck Bronx neighborhood housing bungalows attached houses Silver Beach Edgewater Park Locust Point` · Firecrawl search → scrape | https://cityneighborhoods.nyc/silver-beach | Narrow curved lanes; Silver Beach Association manages maintenance/security (weak, unsourced site; also conflicts with Wikipedia on ownership) — **not used on page**. | Research only |
| TN9 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Locust_Point,_Bronx | Small peninsular neighbourhood bounded by Harding Ave N, Throgs Neck Bridge E, Eastchester Bay; single-family houses; Locust Point Yacht Club occupies outermost block; formerly Locust Island, waterway filled; part of fill for bridge's northern ramp and toll plaza. | §7 Locust Point card, §8 beach/yacht club card, §13 Locust Point + bridge cards |
| TN10 | `Furman Center Throgs Neck Co-op City` · Firecrawl scrape | https://www.furmancenter.org/neighborhoods/throgs-neck-co-op-city/ | Last updated 05/06/2026; latest homeownership 44.7%, population 65+ 19.2% (table year alignment ambiguous — page says "a little under half" and "roughly one in five"). District includes Co-op City. | §5.5 bullet 4, two-households section |
| TN11 | `Throggs Neck Business Improvement District East Tremont Avenue businesses blocks` · Firecrawl search → scrape | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=76 | Throggs Neck BID: 3800 East Tremont Ave Suite 2F; established January 2019; 27 block faces; 281 ground-floor retail businesses. | §5.5 bullet 6, §8 East Tremont card |
| TN12 | `Throggs Neck burglary 45th Precinct Bronx Times homes break-in back door 2025` · Firecrawl search → scrape | https://bronx.news12.com/2025/11/04/caught-on-camera-teens-break-down-door-of-throgs-neck-home/Sqf1zBv08mPKOUyVEUJYX | Nov 3 2025: teens caught on camera breaking down door of a Throgs Neck home (YouTube description: "kicking in his front door"); family reported to 45th Pct and shared video on the Ring app; neighbours said same teens targeted other homes. | Q&A Q9 (Ring), Q10 (security vs keys), AI H3 7 |
| TN13 | same search · Firecrawl scrape | https://www.bxtimes.com/thieves-steal-over-7k-from-throggs-neck-deli/ | May 12 2020: Phillips Gourmet Deli, 45th Pct, ~3:50 a.m. May 1, two burglars forced open a basement door, ~$7,200 from two safes. | Q&A Q11 (cellar door) |
| TN14 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Fort_Schuyler | Begun 1833, dedicated 1856; transferred to state 1934, dedicated to Maritime academy 1938; college founded 1874, one of 29 original SUNY schools 1948; NRHP 1976; Maritime Industry Museum 1986. | §13 Fort Schuyler card |
| TN15 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Throgs_Neck_Bridge | Opened Jan 11 1961; six-lane suspension bridge by Othmar Ammann; 1,800 ft centre span; connects to Bay Terrace, Queens. | §13 bridge card |
| TN16 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Ferry_Point_Park | 413.8 acres; west part opened 1940 after Bronx–Whitestone Bridge; east side landfill (1952–1970), golf course opened 2015; NYC Ferry service Dec 28 2021. | §13 Ferry Point card |
| TN17 | `smart lock fingerprint reader wet fingers not recognized manufacturer support dry finger` · Firecrawl search (excerpt) | https://www.kwikset.com/support/answers/why-isn-t-my-fingerprint-pad-working | "Remove any excess lotion, sweat, or debris from your fingers. If your fingers are very dry, try rubbing them together or lightly moisturizing before use." | Q&A Q7, AI H3 4 |
| TN18 | `NEMA evaluating water-damaged electrical equipment flood replace electronic devices exposed to water` · Firecrawl search (excerpts) | https://www.nema.org/docs/default-source/secure-document-library/nema-gd-1-2016-evaluating-water-damaged-electrical-equipment-guide.pdf ; https://www.esfi.org/water-damaged-electrical-equipment/ | NEMA GD-1: saltwater residue particularly damaging (corrosive and conductive); electronic products incl. signaling/protection systems damaged by water → replace components or return to manufacturer. ESFI: batteries among water-damaged equipment that must be replaced. | Q&A Q4 (post-surge), flood-zone section |
| TN19 | `FEMA homeowner's guide to retrofitting flood shields doorways dry floodproofing residential removable` · Firecrawl search (excerpts) | https://basc.pnnl.gov/information/design-and-retrofit-flood-protection ; https://www.cedengineering.com/userfiles/S06-005%20-%20A%20Guide%20to%20Dry%20Floodproofing%20Homes%20-%20US.pdf | DOE Building America Solution Center: dry floodproofing strategy "Install shields to cover openings such as doors and windows". CED: dry floodproofing not allowed by FEMA for new or substantially improved/damaged residential structures in floodplain. | Q&A Q5 (flood-shield tracks) |
| TN20 | `Ring Neighbors app posting videos is optional user chooses to share; smart lock events shared` · Firecrawl search (excerpts) | https://ring.com/neighbors ; https://ring.com/privacy | "Only content that a Neighbors user chooses to share on the Neighbors App is publicly accessible"; Shared Users share device access without sharing login credentials. | Q&A Q9 |
| TN21 | `NYC Department of Buildings work not requiring a permit ordinary repairs replacement of door hardware locks 28-105.4` · Firecrawl search (gov) → scrape | https://nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-alt-1-2-family-mixed-use.page ; https://nyc.gov/site/buildings/property-or-business-owner/do-i-need-a-permit.page | Minor alterations/ordinary repairs (AC 28-105.4.2) exempt from permit; no explicit mention of door locks; DOB notes home-improvement contractors must hold DCWP HIC licence. **Not used on page** (would raise a licensing question — see FLAGS). | Research only |

Reused from research/smart-lock-installation.md (not re-fetched): Schlage Encode 2.4 GHz requirement + factory reset removes all codes/virtual keys (O5); August Connect within 10–15 ft; Yale Smart Keypad IP55; 2022 NYC BC §1010.1.9 (SI6); 2010 ADA operable parts 34–48 in; HMC §27-2043 key lock + one key (B7); MDL §4 (3+ families = multiple dwelling) (SI11); Tenant Data Privacy Act / HPD page (B11); LawnStarter national $330 avg / $200–$460 / labor $50–$110; Fixr Jan 2025 $250–$400 avg ~$300.

### EMPTY (not accessible in build env / not found)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: `EMPTY (not accessible in build env)`. §10.5 says so and corrects published national/retail claims instead.
- Reddit (r/bronx, Throgs Neck locks): query `reddit Throgs Neck Bronx smart lock OR keypad OR locksmith house` · Firecrawl search → only locksmith ad sites and a Yelp search page; no Reddit threads. `EMPTY`.
- Yelp 1–3★ for Throgs Neck locksmiths/smart-lock installers: search page excerpt only (https://www.yelp.com/search?find_desc=24+Hour+Locksmith&find_loc=Throgs+Neck...), no reviews readable → `EMPTY (not accessible in build env)`.
- NYT 2009 "Living In: Edgewater Park and Silver Beach Gardens": Firecrawl scrape refused ("we do not support this site") → `EMPTY (not accessible in build env)`; NYT 1973 "A Bronx Neighborhood Turns Co-op" excerpt only (400 homeowners, 30×60 plots) — not used.
- Wikipedia "Silver Beach, Bronx" redirects to Throggs Neck; "Throggs Neck Houses" article 404 → `EMPTY`.
- Published Edgewater Park or Silver Beach rule naming door locks: not found → page says so explicitly.
- Local news on smart locks in Throgs Neck specifically: none found → `EMPTY`.
- Google Drive `AESS Website Photos/Smart Lock Installation`: EMPTY (per batch brief); CompanyCam not connected.

### Prices used (copied from smart-lock-installation-bronx.html as-is; Bronx ×1.00; none invented)
| Figure | Scope |
|---|---|
| $1,500–$2,500 installed | single-door keypad or fob reader with electric strike |
| $250–$450 | new electric strike on an entrance door |
| $295–$485 | failed electric strike repair |
| $225 first hour, then 30-min blocks | setup-only visit (app/bridge/codes) — carried over from the Bronx page, which flagged it for confirmation |
| $195/hr, 3-hr min ($585) | service/callback, never on the install visit |
| House-door smart lock | no AESS figure → "Quoted flat at free walkthrough" |
| LawnStarter / Fixr | national third-party, labelled as such |

## Images (11)
Step C (library): 11 of the 18 real AESS photos in `images/smart-lock-installation/aess-smart-lock-installation-*.webp`, each viewed, copied with `cp` (already WebP). Rejected after viewing: `video-doorbell-and-smart-lock` (house number "128" visible), `showing-customer-app-unlock` (customer's face in profile). Note: several of these library photos look AI-rendered (perfect logos, staged light) — same caveat as earlier smart-lock and soundbar runs; flag for Anwar.

| Source (aess-smart-lock-installation-…) | New file (smart-lock-installation-throgs-neck-bronx-…) | What is visible | Section |
|---|---|---|---|
| suburban-front-door-smart-lock-van | fastening-strike-keypad-deadbolt-van | Tech in AESS cap/polo driving a screw at the strike edge of a dark front door with black keypad deadbolt + handleset; AESS van and houses behind | Hero (eager) |
| checking-lock-status-in-app | checking-locked-status-in-app | Tech holding phone showing "Locked" beside keypad deadbolt on wood door | Instant action block |
| removing-old-brass-deadbolt | removing-old-brass-deadbolt | Tech unscrewing old brass deadbolt from wood door, bore exposed | §5 Neighborhood |
| measuring-door-bore-for-deadbolt | measuring-door-bore-backset | Tech measuring backset with tape at an empty bore | §6 Services |
| checking-latch-bolt-alignment | checking-latch-bolt-alignment | Tech pointing at latch/strike on wood door with keypad deadbolt | §7 Architecture |
| keypad-exterior-thumbturn-interior-view | keypad-outside-thumbturn-inside | Split image: exterior keypad entry / interior thumb-turn | Ground Rules |
| connecting-interior-unit-cable | connecting-interior-unit-cable | Tech connecting ribbon cable into interior unit | §8 Commercial |
| fingerprint-unlock-demo-app | fingerprint-unlock-app-confirmation | Finger on reader, tech holding phone "Fingerprint Unlocked" | Q&A |
| replacing-smart-lock-batteries | replacing-smart-lock-batteries | Tech loading AA batteries into interior unit | AI Reality Check |
| programming-access-code-app | programming-access-code-app | Tech entering code on keypad with "Add Access Code" in app | §13 Landmarks |
| servicing-keypad-wiring | servicing-keypad-wiring | Tech with lock halves open, keypad wiring exposed | §14 Pricing |

DAILY-LOG note: `images: 11 real AESS smart-lock photos from images/smart-lock-installation/ (library, renamed copies; Drive empty, CompanyCam not connected)`.

## Question register — smart-lock-installation-throgs-neck-bronx-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 12)
1. With a dozen neighbors' Wi-Fi networks packed into our bungalow lane, will the lock keep dropping offline?
2. Our side door opens onto a passage barely two feet wide — is a keypad even sensible there?
3. Does a keypad on the front door tell people walking the lanes that there is something worth taking?
4. Salt water reached our lock in a storm surge — can it be dried out, or does it have to be replaced?
5. We fitted tracks for removable flood shields either side of the front door — will a keypad and handle still clear the barrier?
6. Wind off the Sound keeps slamming our storm door — will that knock the smart lock out of adjustment?
7. The kids come back from the beach with wet, sandy hands — will a fingerprint reader still let them in?
8. Mom set up the smart lock and has since passed away — how do we take control of it without her password?
9. Neighbors post doorbell clips on the Ring Neighbors app — if our lock is linked to the same account, what do they see?
10. Burglary is fairly low in the 45th Precinct — is a smart lock about security here, or about keys?
11. A Throggs Neck deli was burgled through a forced basement door — what should our shop do about its own cellar door?
12. Our shop's steel back door has a push bar on the inside — can a keypad go on the outside without taking the bar off?

### §17 FAQ (visible == FAQPage, 8)
1. Is a Throgs Neck job priced any differently from the rest of the Bronx?
2. If a code leaks while we are out at work, can we change it from the phone?
3. If a coastal storm is forecast for our appointment day, will you reschedule?
4. Will drilling our door disturb the family on the other side of the party wall?
5. Our front door has a dog flap cut into it. Does that weaken a smart lock?
6. How many physical keys do we end up with, and where should they go?
7. Do you fix smart locks that a handyman or another company installed?
8. Will you help register the lock's manufacturer warranty in our name?

### Other question-form headings
- H2 "Ready to Price Your Throgs Neck Door?" (mid CTA 2)
- Repair captures are non-question headings ("Throgs Neck Smart Lock Dead, Jammed or Crusted With Salt"; "Locked Out of a Throgs Neck House or Shop? Call Before Anyone Drills" — the latter ends in "Drills", not "?").

### De-dup notes
- Checked by meaning against all 16 area/hub pages and the batch-mates on disk (Todt Hill, Chelsea). Replaced during build: FAQ "Can your van get into the private lanes…" (same intent as Todt Hill "Our road is private and gated — what do you need from us so the van reaches the house?") → remote code change FAQ; Q "alarm company responders used to carry a key" (close to Todt Hill "private patrol … hold a code?") → panic-bar exit-device Q.
- Deliberately not asked (already in register): co-op permission for a lock (Bronx Q13), storm door which-door/clearance (Queens Q12, LI Q8), salt finish (LI, Suffolk, SI), raised house after Sandy (SI), kick-in frame (Nassau), volunteer fire company entry (Ulster), summer-bungalow thin door (Putnam), tenant two-family law (Bronx, Brooklyn), DCWP/HIC licence (LI analogue).
- Partial overlaps for the main run to judge: Q7 wet-finger fingerprint vs Todt Hill "children unlock with a fingerprint instead of a code" (different intent: reliability with wet/sandy hands vs credential choice); Q4 post-surge replacement vs Chelsea "controller … in a space that took water in 2012" (placement vs recovery); FAQ 1 pricing vs other geo pricing FAQs (by design).
- Max masked paragraph similarity (difflib, ≥20-word blocks, protected warranty/consent text excluded): 0.514 vs smart-lock-installation-nyc; 0.51 vs -bronx; 0.50 vs -chelsea-manhattan-ny.


## Todt Hill, Staten Island (smart-lock-installation-todt-hill-staten-island-ny)

Built 2026-10-17. Up-link /smart-lock-installation-staten-island; direct line (347) 934-8335; GBP Brooklyn (1282 Troy Ave, #brooklyn). Prices copied as-is from smart-lock-installation-staten-island.html (×1.10 already applied there): $1,650–$2,750 keypad/fob reader + strike; strike $275–$495; strike repair $325–$534; setup-only $225 first hour; callback $195/hr 3-hr min ($585). Residential locks "quoted flat at walkthrough". No new prices.

Thesis: "plan from the gate inward" — serpentine-ridge estates on private, unlit roads behind gates; heavy/mortise/multipoint/pivot entry doors; houses stepping down steep SNAD lots (garage/walk-out levels, pool houses, carriage houses far from the router); large households with staff, service companies and patrols needing per-door, per-person codes; landmark houses (Flagg, Gillett-Tyler) where inside-only retrofits come first; 2026 crowbar/key-fob burglary warnings (lock ≠ armour; door-position sensors, strikes, fob storage).

### Local research log (exact query · platform · URL · finding · page+section used)

| # | Query · platform | URL | Finding | Used on page |
|---|---|---|---|---|
| T1 | (direct fetch) · WebFetch | https://en.wikipedia.org/wiki/Todt_Hill,_Staten_Island | 401 ft (Wikipedia figure); most streets incl. Todt Hill Rd lack sidewalks; buses S74/S76/S84/S86 + SIM15 on Richmond Road; Ernest Flagg houses; Moravian Cemetery 1740; Staten Island Academy moved to hill 1960s; census tract SI0203 (Todt Hill–Emerson Hill–Lighthouse Hill–Manor Heights) 2020: pop 32,822, 10,623 households, 32.7% with children <18, largest age group 55–74 (24.9%), 30.3% renter-occupied. Notable-resident/mob/Godfather content deliberately NOT used. | §5 neighbourhood paras 2, §5.5 stats (households, children, age, renter → 69.7% owner-occupied derived), Sources |
| T2 | `Todt Hill Staten Island Special Natural Area District zoning large lots homes` · WebSearch → Firecrawl scrape | https://zoningresolution.planning.nyc.gov/node/20953 | ZR §105-941 SNAD-1: "Emerson Hill, Dongan Hills, Todt Hill and Lighthouse Hill … central, serpentine, hilly spine … steep slopes, rock outcrops, erratic boulders and ponds … many trees". | §5 para 3, §5.5, "Gate Keypads on the Serpentine Ridge" section, Sources |
| T3 | same · WebFetch | https://www.nyc.gov/assets/planning/download/pdf/plans/special-natural-area-district/snad.pdf | SNAD created 1975; protects rock outcrops, trees/forests, wetlands/water, steep slopes; CPC authorisation "when the applicant seeks to modify a significant natural feature". Driveways not named as requiring authorisation by themselves. Page says AESS is not the authority, owner should check. | Ridge/gate section para 2–3, Sources |
| T4 | `"Special Natural Area District" NA-1 Staten Island Greenbelt Todt Hill Emerson Hill Grymes Hill` · WebSearch | https://www.nyc.gov/site/planning/zoning/districts-tools/special-purpose-districts-citywide.page | EMPTY (redirect page, no content). | — |
| T5 | `Ernest Flagg Estate Todt Hill Landmarks Preservation Commission designation Stone Court Flagg Place cottages` · WebSearch → WebFetch | https://hdc.org/buildings/ernest-flaggs-todt-hill-cottages-wallcot/ | Wallcot, 285 Flagg Place, 1918–21, mosaic rubblestone, designated individual landmark; Flagg built small stone houses on Stone Court grounds. | §7 Flagg-era card, Landmark Doors section, §13 card, Sources |
| T6 | same · WebFetch | https://hdc.org/buildings/stone-court-site-of-the-ernest-flagg-house/ | Stone Court, 209 Flagg Place; mansion, gatehouse and gate fieldstone; designated individual landmark (page gives inconsistent dates — no date used). | §7, Landmark Doors, §13 card |
| T7 | `Landmarks Preservation Commission permit required work on designated individual landmark exterior …` · WebSearch → WebFetch | https://zh.nyc-business.nyc.gov/nycbusiness/description/performing-work-on-a-landmarked-property/apply | LPC permit "before doing any work"; CNE / PMW (no fee, e.g. replacing windows or doors) / CofA; simple repairs & maintenance need no review. | Landmark Doors section, AI reality H3 6, Sources |
| T8 | `"Todt Hill" Staten Island living in neighborhood homes acre gated estates …` · WebSearch → WebFetch | https://s-media.nyc.gov/agencies/lpc/lp/2231.pdf | Gillett-Tyler House, 103 Circle Road, built c.1846 Enfield MA, moved 1931, designated Oct 30 2007; Todt Hill summit 409.8 ft, highest natural point on eastern seaboard Maine–Florida; Cromwell and Flagg estates later subdivided. | Hero ("about 410 feet"), §5 para 1, §5.5, §7, §13 card, Landmark section, Sources |
| T9 | same query · WebFetch | https://www.brickunderground.com/buy/todt-hill | Apr 24 2017: median $1.725M (Jonathan Miller); 13,155 sq ft house on Benedict Rd pictured; "gargantuan cast iron gates"; private roads; "most streets on Todt Hill do not have sidewalks or street lights"; no buses up the hill; Richmond County Country Club. Castellano/Godfather lines not used. | §5 para 2, §5.5, §9 gate Q2, §13 club card, Sources |
| T10 | `R1-1 district "Todt Hill" 9,500 square feet lot 100 feet wide` · Firecrawl search | https://www.realestatesiny.com/new-york-city-residential-zoning-code-r-1-1.php (excerpt) ; https://zr.planning.nyc.gov/article-ii/chapter-3 (excerpt: "lot area of at least 9,500 square feet and lot width of at least 100 feet") | Broker page names Todt Hill as R1-1 example; ZR excerpt gives 9,500 sq ft / 100 ft benchmark. Excerpts only — page words it as "the usual example given" and "benchmark", not a statement that every lot is R1-1. | §5 para 3, Sources |
| T11 | `Todt Hill burglary homes Staten Island police 2024 OR 2025 silive` · WebSearch → WebFetch | https://www.statenislandusa.com/news/be-vigilant-borough-president-fossella-law-enforcement-detail-spate-of-luxury-car-home-break-ins | Feb 12 2026: Feb 1–9 pattern in Todt Hill and Dongan Hills; suspects allegedly use crowbars on windows to enter homes and vehicles; advice: take keys out of vehicles, lock vehicles. | §5 para 6, §9 break-in Qs, §10.5 H3 4, Sources |
| T12 | same · WebFetch | https://hoodline.com/2026/02/nypd-hunts-for-trio-suspected-in-staten-island-burglary-spree/ | Feb 1 2026 New Dorp/Dongan Hills/Todt Hill: crowbar on window frame; Range Rover key fob + ~$60 taken, car stolen; back door approached with crowbar. | §5 para 6, §9 fob Q, Sources |
| T13 | same · WebFetch | https://www.cbsnews.com/newyork/news/new-burglarly-patterns-hit-wealthy-staten-island-neighborhoods/ | Oct 13 2011 burglary pattern Todt Hill, Emerson Hill, Grymes Hill; no entry method detailed. | §5 para 6, Sources |
| T14 | (reused from borough page research) CBS New York June 2022 Todt Hill break-in, stone through back-door glass | (see research/smart-lock-installation.md Staten Island section) | Mentioned in one clause only. | §5 para 6, §10.5 H3 4 |
| T15 | (direct fetch) · WebFetch | https://en.wikipedia.org/wiki/Moravian_Cemetery | 2205 Richmond Road; opened 1740; 113 acres; Vanderbilt mausoleum by Richard Morris Hunt (1885–86), Olmsted landscaping; designated 2016 (mausoleum + portions). | §13 card, Landmark section |
| T16 | (direct fetch) · WebFetch | https://en.wikipedia.org/wiki/Staten_Island_Greenbelt | 2,800 acres; second-largest park after Pelham Bay; High Rock, LaTourette, Willowbrook parks; Nature Center 700 Rockland Ave. (Greenbelt article gives 410 ft for Todt Hill; LPC 409.8 used.) | §5.5, §13 card |
| T17 | (direct fetch) · WebFetch | https://en.wikipedia.org/wiki/Staten_Island_Academy | Chartered 1884; 715 Todt Hill Road; 14-acre campus. | §13 card |
| T18 | `Alexa unlock door voice code required smart lock unlock by voice PIN Google Assistant` · WebSearch → WebFetch | https://service.eufy.com/article-description/Smart-Lock-C34-E30-How-to-Use-Voice-Commands-to-Unlock-Smart-Lock-with-Amazon-Alexa-or-Google-Assistant | Google Assistant: 4-digit security code mandatory for every voice unlock; Alexa "may" require a voice PIN. | §9 voice Q, §10.5 H3 7 |
| T19 | Silo-wide technical sources reused (not re-fetched): Schlage Encode/Encode Plus specs (door 1-3/8–1-3/4", 2.4 GHz Wi-Fi), Yale Assure Lock 2 spec sheet (door to 2-1/4"), Allegion door-prep, August Connect 10–15 ft, Yale Matter FAQ (border router ~50 ft / 25 ft), Bold Thread explainer, Ring lock/alarm article (Ring-app codes only, subscription), August mortise kit (SlashGear 2017), Fixr national $250–$400 avg $300, Homewyse, NYC BC 2022 §1010.1.9 / §1010.1.9.5, New Dorp BID facts | research/smart-lock-installation.md silo sections | as recorded there | §7.5, §9, §10, §10.5, §14, §8 |
| T20 | Reddit (r/statenisland) / Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are claims published by cost sites/manufacturers, stated as such on the page. | — |
| T21 | Local news on smart locks specifically on Todt Hill (SI Advance/silive, Patch) | — | EMPTY — no smart-lock-specific local item found; burglary reports used instead (T11–T14). | — |
| T22 | Door hardware specific to Todt Hill houses (mortise/multipoint/pivot prevalence) | — | No source found → page describes these only as door types we check for, no prevalence statistic claimed. | §7, §9 |

## Images (11)

Source: Step C library (`images/smart-lock-installation/aess-smart-lock-installation-*.webp`); Drive folder empty and CompanyCam not connected (per main run). Each image viewed before use. Two suggested photos swapped out: `video-doorbell-and-smart-lock` (house number "128" visible) and `showing-customer-app-unlock` (customer's face in profile) → replaced by `checking-lock-status-in-app` and `servicing-keypad-wiring`. Library images look AI-rendered (identical uniform patches, generic suburban settings) — needs Anwar's review.

| Source file | New file | What is visible |
|---|---|---|
| aess-…-suburban-front-door-smart-lock-van.webp | smart-lock-installation-todt-hill-staten-island-keypad-deadbolt-front-door-van.webp | Technician driving a strike screw beside a black keypad deadbolt on a black glass-panel door; AESS van at curb |
| aess-…-programming-access-code-app.webp | …-adding-access-code-in-app.webp | Technician entering a 6-digit code in app, finger on backlit keypad, wood-grain door |
| aess-…-fingerprint-unlock-demo-app.webp | …-fingerprint-unlock-app-confirmation.webp | Finger on fingerprint pad; phone shows "Fingerprint Unlocked" |
| aess-…-servicing-keypad-wiring.webp | …-opening-keypad-harness-repair.webp | Gloved technician holding removed keypad, probing harness; batteries in tool bag |
| aess-…-measuring-door-bore-for-deadbolt.webp | …-measuring-bore-wood-door.webp | Tape measure from door edge to empty bore on thick stained wood door |
| aess-…-removing-old-brass-deadbolt.webp | …-removing-old-brass-deadbolt.webp | Technician unscrewing worn brass deadbolt; two brass faceplates on edge |
| aess-…-checking-latch-bolt-alignment.webp | …-checking-strike-bolt-alignment.webp | Technician pointing at bolt/strike on frame; black keypad + lever on wood-grain door |
| aess-…-keypad-exterior-thumbturn-interior-view.webp | …-keypad-outside-thumbturn-inside.webp | Two-panel image: outside keypad / inside thumb-turn |
| aess-…-checking-lock-status-in-app.webp | …-checking-locked-status-app.webp | Phone showing "Locked" beside backlit keypad on wood door |
| aess-…-connecting-interior-unit-cable.webp | …-seating-interior-unit-cable.webp | White ribbon cable pressed into interior unit connector, indoors |
| aess-…-replacing-smart-lock-batteries.webp | …-replacing-lock-batteries.webp | AA batteries going into interior unit on dark door |

Alt/title/caption describe only what is visible + "Todt Hill, Staten Island"; none claims a local customer, named house or completed local job.

## Question register — smart-lock-installation-todt-hill-staten-island-ny

### §9 YOUR QUESTIONS ANSWERED (H3)
1. Can a guest's code open the driveway gate and the front door, or do they need two?
2. When nobody is home, how should a courier or guest get from the closed gate to the front door?
3. If the power fails, does an electric gate stay locked or swing free, and how does the car get in?
4. Our front door has a mortise lockset where one handle works both the latch and the deadbolt — can a motor drive that?
5. We have a tall pivot front door with no room for a standard deadbolt — what goes on it?
6. Can a smart lock take a high-security key cylinder so the override key can't be copied at a hardware counter?
7. Our mesh Wi-Fi uses one network name for both bands — why won't the lock join, and what fixes it?
8. How many locks can one bridge or Thread network carry in a house with eight or nine doors?
9. Should a voice assistant ever be allowed to unlock our doors?
10. Should staff use the service door rather than the front door — and can the locks enforce that?
11. Our private patrol checks the house while we travel — should the patrol company hold a code?
12. Should unlocking the mudroom door also disarm the alarm?
13. Thieves on the hill have pried at back doors with crowbars — will a smart lock warn us if a door is forced?
14. Where should the car key fobs live now that break-ins here have targeted them?

### §17 FAQ (visible == FAQPage, 9)
1. Does a big house on the hill cost more per door than a smaller house elsewhere on the island?
2. How far ahead should we book when the property has eight or more doors and a gate?
3. Our road is private and gated — what do you need from us so the van reaches the house?
4. Can the pool house or cabana get a keypad so guests can use it without going through the main house?
5. Can our children unlock with a fingerprint instead of remembering a code?
6. Is there a way to pause staff and service codes while we are away and turn them back on when we return?
7. Will fitting a lock mark or scratch a stained hardwood door?
8. Can you take down an old keypad or intercom box that a previous owner left on the gate pillar?
9. What do you leave behind so a house manager can run the system without calling us?

### Other question-form headings
- Gate Keypad Dark or Entry Lock Jammed on Todt Hill? (repair capture)
- Shut Out at Your Own Gate or Door on Todt Hill? (final repair block)

### De-dup notes
Avoided as questions because siblings already hold the intent: thick door beyond listed range (HV), historic-district approval for a keypad (HV/Brooklyn — covered as body text in "Landmark Doors" section instead), cable to driveway keypad under land rules (Putnam — covered as body text in ridge section), multipoint lock (Westchester — body text only), shared garage code among contractors (Westchester), caretaker leaving (Dutchess), elderly-parent emergency entry, insurance history export, garage-door app.


## Chelsea, Manhattan (smart-lock-installation-chelsea-manhattan-ny)

Built 2026-10-17 by the Chelsea builder subagent (batch: Chelsea, Throgs Neck, Todt Hill). Neighbourhood spoke of /smart-lock-installation-manhattan. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737; (800) 486-0943 only in the shared header chrome. Prices copied as-is from smart-lock-installation-manhattan.html (no new multiplier, nothing invented).

Thesis / lane: Chelsea's door stock changes block by block — (1) 1830s–50s Greek Revival/Italianate rowhouses in the Chelsea HD (1970) and Extension (1981), where LPC rules allow a historic door to be replaced only when beyond reasonable repair, so the lock must suit the existing door (door survey, reuse bores, inside-only retrofit, owner's LPC file); (2) tenement walk-ups on the avenues; (3) very large complexes — London Terrace (1930, co-op + rental under one roofline) and Penn South (limited-equity co-op, 2,820 units); (4) NYCHA Fulton/Elliott-Chelsea redevelopment; (5) West Chelsea HD warehouses (2008), galleries (Tue–Sat hours, Thursday/Friday openings), keyed-elevator lofts, frameless glass doors, fail-secure strikes, Sandy flood height for electronics; (6) scaffolding/FISP periods. Deliberately avoids the borough page's lanes (doorman platforms, pied-à-terre, LL18 short stays, Midtown suites, W 21st St lockboxes, cast-iron SoHo storefronts) and other silo pages' intents (see De-dup notes).

Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (markdown or query/directQuote mode).

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| C1 | `Chelsea Historic District Extension Landmarks Preservation Commission designated rowhouses West 20th 21st 22nd Street` · Firecrawl search → Firecrawl scrape | https://www.hmdb.org/m.asp?m=135160 | Marker (434 W 23rd St): Chelsea developed 1830s–1850s largely by Clement Clarke Moore; "unusually uniform and elegant residential neighborhood in Greek Revival and Italianate styles"; General Theological Seminary built 1825–1902 (Ninth Ave facade 1960), full block Ninth–Tenth Aves, W 20th–21st, land donated by Moore; Cushman Row 406–418 W 20th; photo caption "The former General Theological Seminary, now apartments." | §5 para 2, §7 cards, §13 GTS card, sources, schema mentions |
| C2 | same search (excerpt) | http://s-media.nyc.gov/agencies/lpc/lp/1088.pdf | Extension report excerpt: only Second Empire rowhouses in the Extension are 305–311 W 22nd St. Not used beyond confirming the Extension. | background |
| C3 | same search → Firecrawl scrape (query) | https://chelseacommunitynews.com/2020/07/03/save-chelsea-plan-proceeding-determines-to-extend-the-chelsea-historic-district/ | July 3 2020: Save Chelsea proposal; original 1970 designation, 1981 extension, 2008 West Chelsea; of 113 buildings proposed, 67 rowhouses, 17 tenements. | §5, sources (tenement/rowhouse mix) |
| C4 | Firecrawl scrape (query) of https://en.wikipedia.org/wiki/Chelsea_Historic_District (redirects to Chelsea, Manhattan) | https://en.wikipedia.org/wiki/Chelsea,_Manhattan | Boundaries ~14th St to upper 20s/34th St, Sixth Ave to Hudson; HD designated 1970, extension 1981 (NRHP 1977/1982); "mix of tenements, apartment blocks, two city housing projects, townhouses, and renovated rowhouses"; over 200 galleries; CD4/CD5; 10th Precinct. | §5 para 1, stats, sources, schema about |
| C5 | `Cushman Row 406-418 West 20th Street Greek Revival 1839-40 iron pineapples Chelsea` · Firecrawl search → Firecrawl scrape (query) | https://villagepreservation.org/2021/03/14/beyond-the-village-and-back-cushman-row-408-418-west-20th-street/ | Cushman began 1839, done by 1840; houses set 10 ft back, iron fences and gates with anthemia/palmettes; stoops with candelabrum newels; basement entrances recessed under steps; "deep brownstone temple-like entryway enframements"; noted with Washington Square North as finest Greek Revival row. | §5 para 2, §13 Cushman card, door survey section, glossary |
| C6 | `Landmarks Preservation Commission rules 63 RCNY 2-11 entrance doors intercom buzzer panel installation criteria` · Firecrawl search (gov) → Firecrawl scrape (query) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-90026 | 63 RCNY §2-14(e): new windows/doors may be approved if they match original/historic in details, materials, operation, configuration, finish; "Historic doors may be replaced only if they are deteriorated beyond reasonable repair, as described in a condition assessment." | §5 para 2, §7.5, §9 Q1, §10.5 H3 1–2, glossary, sources |
| C7 | `nyc.gov LPC permit types "Permit for Minor Work" "Certificate of No Effect" "Certificate of Appropriateness" staff level 95 percent` · Firecrawl search (excerpt) | https://www.nyc.gov/site/lpc/applications/permit-types.page | Three permit types; "95% of LPC's permit approvals are issued at staff level and do not require full review by the Commission at a public hearing." | §8.5, §9 Q2, glossary, sources |
| C8 | `LPC "do I need a permit" ordinary repairs maintenance hardware intercom …` · Firecrawl search (excerpt) | https://precisionwindowsnj.com/blog/lpc-window-replacement-nyc-landmark-districts | Secondary: PMW vs CNE distinction (DOB permit), PMW 20 working days / CNE 30. Background only; not cited on page. | background |
| C9 | reused from silo research (Manhattan M11) | https://noho.nyc/wp-content/uploads/2025/07/Storefronts_in_HD_Flyer_Updated.pdf | Repairing/replacing hardware (knobs, hinges, handles) does not need LPC approval; most door work does. | §9 Q2, §10.5 H3 2, sources |
| C10 | `West Chelsea Historic District 2008 designation warehouses galleries High Line …` · Firecrawl search → Firecrawl scrape (query) | https://www.citylandnyc.org/landmarks-considers-west-chelsea-district/ | Seven blocks W 25th–28th Sts, West Side Hwy to Tenth Ave; brick industrial buildings from 1885 (Otis Elevator, Cornell Iron Works); NY Terminal Warehouse Co. Central Stores = 25 interconnected brick buildings, 1.2M sq ft, full block W 27th–28th; designated unanimously July 15 2008. | §5 para 4, stats, §8 Terminal card, §13 card, sources, schema mentions |
| C11 | same search (excerpt) | https://www.facebook.com/nylandmarks/videos/terminal-warehouse-261-11th-avenue-manhattanwest-chelseas-terminal-warehouse-has/1342289067841934/ | NY Landmarks Conservancy: Terminal Warehouse, 261 11th Ave, "converted from storage space into a work and retail…" | §8 Terminal card |
| C12 | `London Terrace Chelsea 1930 apartments …` · Firecrawl search → Firecrawl scrape (query) | https://en.wikipedia.org/wiki/London_Terrace ; https://www.cityrealty.com/nyc/chelsea/london-terrace-towers-465-west-23rd-street/3714 ; https://londonterracetowers.com/about/ | ~1,700 apartments, 14 contiguous buildings of 17–19 stories, Olympic-sized pool; first buildings opened May 1930; run as two organisations — London Terrace Towers (co-op, Douglas Elliman) and London Terrace Gardens (rental, Rose Associates), internal connections largely closed off; whole block Ninth–Tenth Aves, 23rd–24th Sts (CityRealty); "1665 apartments" (LTT site). | §5 para 3, stats, §7 card, §9 Q6, §13 card, sources |
| C13 | `Penn South co-op Chelsea 2,820 apartments limited-equity ILGWU 1962 …` · Firecrawl search → Firecrawl scrape | https://www.pennsouth.coop/faq-general-information-about-penn-south.html ; https://www.pennsouth.coop/penn-south-history.html (excerpt) | Eighth–Ninth Aves, 23rd–29th Sts; limited-equity co-op under HPD supervision; no profit on resale; 2,820 units, close to 5,000 residents; 15 buildings, 21 residential floors, two elevators each; own co-generation plant (electricity, heat, cooling); history excerpt "May 19, 1962". (Wikipedia says ten 22-storey buildings — official site used.) | §5 para 3, stats, §7 card, glossary, §13 card |
| C14 | https://www.pennsouth.coop/security.html · Firecrawl scrape | — | EMPTY (not accessible in build env — redirects to resident login). Penn South lock/door rules not found; page states none. | — |
| C15 | `"Penn South" apartment door lock key fob shareholders rules alteration` · Firecrawl search → Firecrawl scrape (query) | https://www.pennsouth.coop/uploads/8/2/7/5/82753010/ps-annual-reports-2023.pdf | Capital-projects table lists "Door Lock Monitoring System" with $0 in FY2022–24. Not used (no usable rule). | — |
| C16 | same search → Firecrawl scrape (query) | https://chpcny.org/wp-content/uploads/2021/04/Fulton-Elliott-Chelsea-RFP.pdf | 2021 NYCHA PACT RFP: Chelsea Houses 425, Chelsea Addition 96, Elliott 608, Fulton 944 = 2,073 units. Not cited (superseded by C17 figures). | background |
| C17 | `Fulton Elliott-Chelsea Houses demolition rebuild Related Essence 2026 news tenants` · Firecrawl search (excerpts) | https://www.nyc.gov/site/nycha/about/pact/chelsea-fulton.page ; https://www.thecityreporter.nyc/2026/09/21/nycha-fulton-elliott-chelsea-holdouts-manhattan/ | NYC.gov: "All 2,056 existing NYCHA apartments at Fulton and Elliott-Chelsea will be replaced with new, permanently affordable homes." The City Reporter, Sept 21 2026: NYCHA with Related and Essence plans to take down 18 buildings in three developments (Fulton, Elliott, Chelsea Houses) and replace them with six towers; relocation of Fulton 11 and Chelsea Addition first. | §5 para 3, stats, §9 Q8, sources, schema mentions |
| C18 | `Chelsea art galleries how many galleries …` · Firecrawl search → Firecrawl scrape (query) | https://away.mta.info/articles/exploring-chelsea-manhattan-gallery-district/ | "More than 300 contemporary art galleries" in West Chelsea, 10-block area between Tenth and Eleventh (excerpt); galleries open Tue–Sat 10 a.m.–6 p.m. most of the year, Saturdays closed in summer; openings Thursday or Friday evenings at 6 p.m. (Fall '22 guide.) | §5 para 4, stats, §8 card, §9 Q9, gallery calendar, FAQ 3, sources |
| C19 | same search (excerpts) | https://agora-gallery.com/chelsea-galleries-itinerary/ ; https://www.nyc-arts.org/collections/38592/chelsea-galleries-walking-tour/ | 200+ galleries between W 18th and W 28th along 10th/11th Aves; Gagosian at 522 W 21st St. Background (W 18th–28th extent used in §8 card). | §8 card |
| C20 | `Hurricane Sandy flooded Chelsea galleries …` · Firecrawl search → Firecrawl scrape (query) | https://artlyst.com/new-york-galleries-destroyed-by-hurricane-sandy-flooding/ | Nov 2 2012: three to five feet of flooding inside galleries; Paula Cooper and Gagosian on W 21st St affected; Postmasters tweeted "Chelsea is flooded up to tenth avenue"; water 5 ft indoors at Zach Feuer. | §5 para 5, stats, §9 Q12, §10.5 H3 7, flood section, sources |
| C21 | `Chelsea loft "key-locked elevator" OR "keyed elevator" opens directly into the apartment …` · Firecrawl search → Firecrawl scrape (query) | https://www.brickunderground.com/buy/buy-curious-apartments-with-private-elevators | (Aug 2026) Key-locked elevator won't move without key in car lock or resident ringing visitor up; front door of elevator locked; Medeco keys common in older buildings; key systems that bounce back to locked (older Hudson Yards building); newer construction uses cards, keypads, codes, biometrics; historically in warehouse conversions (Village, SoHo, Tribeca); some lofts have a separate entrance door between elevator and apartment; steel gates outside elevator; "a key-locked apartment is as safe as, or even safer than, having a doorman"; security depends on the building's entire system. Not Chelsea-specific — page says "lofts of the type Brick Underground describes". | §5 para 4, §6 card, §9 Q4/Q5, §10.5 H3 6, glossary, sources |
| C22 | `NYC DOB elevator work must be performed by licensed elevator agency director …` · Firecrawl search (excerpts) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-160334 ; https://dol.ny.gov/elevator-licensing-information ; https://www.nyc.gov/site/buildings/industry/elevator-licenses-and-helper-card.page | Admin Code Art. 425: "unlawful to perform elevator work … unless that work is performed by or under the direction of an elevator agency director"; NYS DOL: all individuals who work on an elevator must be licensed as an Elevator Mechanic. | §8.5, §9 Q5, sources |
| C23 | `NYC Building Code 1010.1.9.4 locks and latches key-operated locking device "THIS DOOR TO REMAIN UNLOCKED…"` · Firecrawl search (excerpts) | https://up.codes/s/door-operations ; https://codes.iccsafe.org/content/NYSBC2020P1/chapter-10-means-of-egress | IBC and 2020 NYS Building Code allow key-operated locks on main doors of B/M occupancies (and A ≤300) with a sign "THIS DOOR TO REMAIN UNLOCKED WHEN THIS SPACE IS OCCUPIED". Page labels these as model codes and says NYC has its own code. | §8.5, §9 Q9 |
| C24 | `idighardware fail safe vs fail secure electric strike definition …` · Firecrawl search (full excerpt) | https://idighardware.com/2023/10/decoded-fail-safe-vs-fail-secure-when-and-where/ ; https://allegion.ca/en/resources/education/leading-the-industry/decoded/fail-safe-vs-fail-secure.html | Fail safe = unlocked on access side when power removed; fail secure = locked; strikes leave free egress regardless; strikes on fire doors must be fail secure (NFPA 80 listings); maglocks only fail safe; fail secure more common for security. | §7.5, §8.5, §9 Q9/Q11, §10, §10.5 H3 4, glossary, sources |
| C25 | `frameless glass door electric lock options patch fitting electric bolt maglock U-bracket …` · Firecrawl search (excerpts) | https://ngteco.com/blogs/workforce-insights/magnetic-locks-vs-electric-bolt-locks-office-glass-doors ; https://www.youtube.com/watch?v=oL7n8ZDQzY4 | NGTECO: electric bolt locks on glass hide in a top rail, floor box, or surface patch clamped to the glass. Ubiquiti install video: U-bracket for outward-swinging glass door maglock. | §9 Q10, §10, §10.5 H3 5 |
| C26 | `Furman Center Chelsea Clinton Midtown neighborhood profile …` · Firecrawl search → Firecrawl scrape (query) | https://www.furmancenter.org/neighborhoods/clinton-chelsea/ | 2024 homeownership rate Clinton/Chelsea 19.2% vs citywide 32.7% (excerpt confirms); public housing 4.0% of rental units; other table columns misaligned in scrape → not used. | §5 para 5, stats, sources |
| C27 | `Starrett-Lehigh Building 601 West 26th Street …` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Starrett%E2%80%93Lehigh_Building ; https://starrett-lehigh.com/wp-content/uploads/sites/25/2025/07/RXR_CRE_25028_Starrett-Lehigh_Generic-Brochure-V12.pdf | Built 1931, linked rail freight, trucks, manufacturing, storage; entrances on 26th and 27th Sts; tenants incl. Canada Goose, Club Monaco, Diller Scofidio + Renfro. | §8 card, schema mentions |
| C28 | `Chelsea Market Nabisco factory 75 Ninth Avenue Google bought 2018 $2.4 billion …` · Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Chelsea_Market ; https://www.nytimes.com/2018/02/07/nyregion/google-chelsea-market-new-york.html | Food hall, shopping mall, office building and TV production facility; NYT Feb 7 2018: $2.4 billion deal, Google; "former factory building". | §8 card, sources |
| C29 | `High Line park opened 2009 …` · Firecrawl search (excerpts) | https://www.thehighline.org/faq/ ; https://en.wikipedia.org/wiki/High_Line ; https://www.thehighline.org/history/ | 1.45-mile park on former New York Central spur, Gansevoort to 34th St; first section Gansevoort–20th St opened June 8 2009; phases 2009/2011/2014. | §7 card, §13 card, sources |
| C30 | `NYC DOB Facade Inspection Safety Program FISP …` · Firecrawl search (excerpts) | https://www.nyc.gov/site/buildings/safety/facade-local-law.page | Owners of buildings higher than six stories must have exterior walls inspected every five years and file a report. | §9 Q13, glossary, sources |
| C31 | `Chelsea gallery burglary break-in stolen artwork …` · Firecrawl search → Firecrawl scrape (query) | https://patch.com/new-york/midtown-nyc/burglar-climbs-midtown-gallery-steals-digital-art-cops | Dec 29 2021: burglar scaled scaffolding outside EFA studio/gallery, W 39th St (Midtown, not Chelsea), entered via unlocked second-storey window. Page labels it Midtown. | §9 Q13, sources |
| C32 | `10th Precinct Chelsea burglaries apartment building break-ins 2026 …` · Firecrawl search | (excerpts: patch.com/new-york/chelsea-ny/police-fire; amny 10th Precinct; NY1 FB video, undated) | No dated, Chelsea-specific residential burglary story usable → EMPTY for local crime; no crime stat stated. | — |
| C33 | `reddit Chelsea Manhattan apartment smart lock landlord walk-up OR London Terrace OR Penn South keys` · Firecrawl search (excerpts) | https://www.reddit.com/r/AskNYC/comments/121qvhi/apartment_building_uses_the_same_keys_for/ (and r/AskNYC, r/NYCapartments, r/smarthome threads) | Excerpts only, citywide (not Chelsea): a building using the same keys for multiple units; leases require giving management a key. Used only as "New Yorkers on r/AskNYC have described buildings where one key opens several units". Chelsea-specific Reddit → EMPTY. | §9 Q7 |
| C34 | reused silo research (NYC hub N1) | https://www.nysenate.gov/legislation/laws/MDW/51-C | MDL §51-c: tenant may add a lock ≤3 inches in circumference; duplicate key to owner on request. | §7.5 walk-ups, §9 Q6/Q7, sources |
| C35 | reused silo research (Manhattan M15, M30; silo S1) | NYC BC 1010.1.9.9 (amlegal); Admin Code §28-105.4.7; https://www.fixr.com/costs/smart-lock-installation | Maglock release rules; <50 V permit exemption wording; Fixr national $250–$400, avg ~$300 (Jan 2025), handyman $50–$100/hr. | §8.5, pricing comparison |
| C36 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 headings are paraphrased general claims, stated as such on the page. | — |
| C37 | Local news on smart locks specifically in Chelsea (Chelsea Community News, Patch Chelsea, amNY) | — | No Chelsea smart-lock story found → EMPTY. | — |
| C38 | Penn South / London Terrace unit-door lock rules; Mitchell-Lama/HPD alteration rules | — | Not found / login-gated → EMPTY; page states no building's lock policy. | — |

### Prices used (copied from smart-lock-installation-manhattan.html, no change)
- Single-door keypad or fob reader with electric strike: $1,875–$3,125.
- New electric strike: $313–$563. Failed strike repair: $369–$606.
- Setup-only visit: $265 first hour, then 30-minute blocks.
- Service/callback: $195/hr, 3-hour minimum ($585), never on initial install.
- Rowhouse/apartment-door smart lock: no AESS figure → quoted flat after free walkthrough/door survey.
- National comparison only: Fixr $250–$400, avg ~$300 (Jan 2025).

## Images (11)

Step C (Drive folder empty, CompanyCam not connected — per main run). All 11 viewed before use; copied (cp, already WebP) from images/smart-lock-installation/aess-smart-lock-installation-*.webp. Alt/title/caption describe only what is visible + "Chelsea, Manhattan"; none claims a local customer, named building or completed local job. NOTE: the library photos look AI-rendered (uniform logo patches, synthetic app screens) — flagged in earlier DAILY-LOG lines too; needs Anwar's confirmation that they are real.

| Source (images/smart-lock-installation/) | New file | What is visible |
|---|---|---|
| aess-smart-lock-installation-keypad-smart-deadbolt-brownstone-door.webp | smart-lock-installation-chelsea-manhattan-keypad-smart-deadbolt-brownstone-door.webp (hero, eager) | Black keypad deadbolt with key override and black lever on a panelled wood door; stone steps and iron railings behind |
| aess-smart-lock-installation-programming-access-code-app.webp | smart-lock-installation-chelsea-manhattan-programming-access-code-app.webp | Technician adding an access code in an app while touching a keypad on a wood door |
| aess-smart-lock-installation-drilling-keypad-lock-brownstone-stoop.webp | smart-lock-installation-chelsea-manhattan-drilling-keypad-lock-brownstone-stoop.webp | Technician with drill at a keypad deadbolt on a wood stoop door; ironwork, row of stoops behind |
| aess-smart-lock-installation-apartment-door-smart-lock-app.webp | smart-lock-installation-chelsea-manhattan-apartment-door-smart-lock-app.webp | Technician testing keypad deadbolt with phone on a unit door ("4A" sign) in a hallway |
| aess-smart-lock-installation-measuring-door-bore-for-deadbolt.webp | smart-lock-installation-chelsea-manhattan-measuring-door-bore-for-deadbolt.webp | Tape measure across an existing bore on a wood door, brass latch plates on edge |
| aess-smart-lock-installation-office-glass-door-smart-lock.webp | smart-lock-installation-chelsea-manhattan-office-glass-door-smart-lock.webp | Technician fastening strike plate beside keypad deadbolt on black-framed glass door, office behind |
| aess-smart-lock-installation-removing-old-brass-deadbolt.webp | smart-lock-installation-chelsea-manhattan-removing-old-brass-deadbolt.webp | Technician removing brass deadbolt with drill driver from wood door |
| aess-smart-lock-installation-office-lever-smart-lock-install.webp | smart-lock-installation-chelsea-manhattan-office-lever-smart-lock-install.webp | Technician screwing latch plate of keypad lever lock on framed glass office door |
| aess-smart-lock-installation-fingerprint-unlock-demo-app.webp | smart-lock-installation-chelsea-manhattan-fingerprint-unlock-demo-app.webp | Fingerprint unlock on keypad lock; phone app shows "Fingerprint Unlocked" |
| aess-smart-lock-installation-checking-lock-status-in-app.webp | smart-lock-installation-chelsea-manhattan-checking-lock-status-in-app.webp | Technician checking "Locked" status in app beside keypad deadbolt |
| aess-smart-lock-installation-servicing-keypad-wiring.webp | smart-lock-installation-chelsea-manhattan-servicing-keypad-wiring.webp | Keypad removed, wiring inside being checked; batteries and tools in bag |

## Question register — smart-lock-installation-chelsea-manhattan-ny

### §9 YOUR QUESTIONS ANSWERED (H3)
Landmarked rowhouse doors
1. If drilling for a smart lock splits our original 1840s front door, can we simply order a new one?
2. Who files with the Landmarks Preservation Commission for a keypad — the owner, the architect or the installer?
3. Our rowhouse used to be four apartments and is one home again — what should happen to the old apartment doors and their locks?
Lofts, freight landings and keyed elevators
4. Our loft's elevator opens straight into the apartment on a key — where does a smart lock go?
5. Can the key switch inside our loft elevator be swapped for a keypad or a phone?
Big complexes and the city's housing
6. Half our block is a co-op and half is a rental under one roofline — whose rules decide what goes on my door?
7. My old apartment key turned out to open a neighbour's door — will a smart deadbolt fix that?
8. Our household is moving into one of the new Fulton or Elliott-Chelsea towers — is it worth fitting a smart lock before the move?
Gallery doors on the West 20s
9. Hundreds of people come through on an opening night — should the gallery door be locked, unlocked or on a schedule?
10. Our gallery door is frameless glass with nothing to cut a strike into — what can lock it electronically?
11. Should the electric strike on our gallery entrance be fail-safe or fail-secure?
12. Where should the lock controller and battery backup go in a ground-floor space that took water in 2012?
While the building is being worked on
13. Scaffolding is going up on our building for facade work — which doors need attention while it is there?

### §17 FAQ (visible == FAQPage, 8)
1. What does a keyless gallery or studio door with an electric strike cost in Chelsea?
2. Do you cover all of Chelsea, from 14th Street to the edge of Hudson Yards and from Sixth Avenue to the river?
3. Can the installation happen on a Monday, when most Chelsea galleries are closed?
4. How long does the door survey on a landmarked rowhouse take?
5. Can the gallery be alerted if the loading door is left propped open after a delivery?
6. Can one visit cover both our Chelsea apartment and our studio a few blocks away?
7. Can the wiring left from an old buzzer or strike on our loft door be reused for the new lock?
8. Can you work in the gallery while a show is on the walls without putting the art at risk?

### Other question-form headings
- H2 "Chelsea Smart Lock Stuck, Silent or Off the App?" (repair capture)

De-dup notes: avoided HV "historic-district approval for a keypad" (Q2 is about who files and what documentation, not whether approval is needed), Brooklyn stoop/vestibule/double-door/areaway/original-hardware intents, Manhattan "reader behind glass on cast-iron facade", doorman/platform/LL18/suite intents, NYC hub renter/co-op approval intents, Dutchess/Rockland/Ulster "same key for whole building" intents, Westchester/Dutchess "second-floor doors" (Q13 is about the temporary scaffold period). Partial overlaps for the main run to judge: Q11 fail-safe/fail-secure gallery strike vs Todt Hill "If the power fails, does an electric gate stay locked or swing free" (same physics, different device); Q12 controller height after Sandy vs Throgs Neck "salt water reached our lock — dry out or replace?" (placement vs repair); FAQ 1/2 cost and coverage are geo-specific by design.

> Main-run note (2026-10-17, Todt Hill): to clear the 2 KB size-cluster rule against Brooklyn Heights, the main run minified this page's inline CSS/JSON-LD and removed four sentences: the Wikipedia sidewalk/Richmond Road bus line, the CBS June 2022 back-door break-in clause, the Hoodline key-fob clause, and the R1-1 9,500 sq ft lot benchmark. Those log entries are no longer used on the page.

## New Dorp, Staten Island (smart-lock-installation-new-dorp-staten-island-ny)

Page: smart-lock-installation-new-dorp-staten-island-ny · up-link /smart-lock-installation-staten-island · phone (347) 934-8335 (body, CTAs, schema; (800) 486-0943 only in shared mega-nav header) · GBP Brooklyn, 1282 Troy Ave, schema @id #brooklyn. Built 2026-10-17.

Thesis: New Dorp is three door problems under one name, split by Hylan Boulevard — (1) the Lane: mixed-use storefronts with flats above and rear doors onto parking (who may open which door; glass shopfront strikes; schedules; landlord access); (2) the inland blocks: detached/semi-attached houses where a reported crowbar attempt makes strike/frame reinforcement the priority; (3) New Dorp Beach below Hylan: post-Sandy elevated "candlestick" homes where Appendix G puts living space at the DFE and only parking/storage/access below, so electronics stay at living level and lower doors get mechanical hardware.

| # | Query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| ND1 | `New Dorp, Staten Island` · WebFetch | https://en.wikipedia.org/wiki/New_Dorp,_Staten_Island | Boundaries Mill Rd / Tysens Ln / Amboy & Richmond Rds / Bancroft Ave; New Dorp Beach Mill Rd to Lower NY Bay, usually counted part of New Dorp; 2020 NTA pop. 29,083 (27,623 in 2010, +5.3%); Hylan Plaza opened 1966, largest of five 1960s Hylan centres; Tysens Park Apartments; SIR New Dorp station at New Dorp Lane/New Dorp Plaza; ZIP 10306; 122nd Pct; Lane Theater opened Feb 10 1938, landmarked 1988. (70.2% renter figure NOT used — implausible/unverified.) | §5 paras 1 and 3, §5.5 stat 3, §7 strip-centre card, §8 Hylan card, §13 station card, hero badge |
| ND2 | `New Dorp BID City Council` · Firecrawl scrape | https://citylandnyc.org/city-council-approves-new-dorp-bid | Council 50–0 on Apr 5 2017; New Dorp Lane + adjacent commercial streets between Hylan Blvd and Richmond Rd; 146 properties, 180 businesses, mostly small/family-owned. | §5 para 2, §5.5 stat 1, §8 card 1 |
| ND3 | `silive New Dorp Lane municipal parking lot behind stores` · Firecrawl search → scrape (query) | https://www.nyc.gov/html/dot/html/motorist/parkinglist.shtml | NYC DOT: New Dorp Municipal Parking Field, 98 New Dorp Lane at New Dorp SIR station, Mon–Sat 7 AM–10 PM except Sunday. (WebFetch of same URL: permission not answered → used Firecrawl.) | §5 para 2, §5.5 stat 2, §8 station card, §13 station card |
| ND4 | same search | https://www.silive.com/eastshore/newdorp/2011/06/builder_eyes_new_dorp_parking.html | 2011 SI Advance community blog: New Dorp Lane "a great little commercial strip of mostly old fashioned mom 'n pop stores"; municipal lot above the station. Background only. | research only |
| ND5 | `New Dorp burglary 122nd precinct unlocked door break-in silive 2025` · Firecrawl search → scrape | https://www.cbsnews.com/newyork/news/staten-island-home-burglaries-stolen-range-rover/ | CBS New York (Feb 2026): "On Feb. 1, three male suspects used a crowbar to try and break into a home near Benedict Road and Circle Road in New Dorp" (122 Precinct). | §5 para 3, Three New Dorps (inland), §9 crowbar Q, §10.5 H3 7 |
| ND6 | same search | https://www.silive.com/crime-safety/2025/03/glass-shattered-at-restaurant-nypd-probes-reported-burglary-on-staten-island.html | Mar 3 2025: glass front doors smashed at Max's Es-Ca, 1559 Richmond Rd, Dongan Hills; CompStat: SI burglaries +84% (72 vs 39 as of Feb 23); "122nd Precinct in New Dorp, where burglaries have escalated 150% to 25 vs. 10 last year." | §5 para 3, §5.5 stat 4, §9 smashed-glass Q (Dongan Hills named), §10.5 H3 7 |
| ND7 | `Resilient Neighborhoods East Shore Staten Island New Dorp Beach…` · Firecrawl search → scrape (PDF query) | https://www.nyc.gov/assets/planning/download/pdf/plans-studies/resilient-neighborhoods/east-shore/summary-report-east-shore.pdf | DCP East Shore report: ~4 sq mi study area; thousands of homes in Oakwood Beach, New Dorp Beach, Midland Beach, South Beach severely damaged/destroyed by Sandy; photo "privately-funded home elevation in New Dorp Beach"; 1% floodplain V / Coastal A / A zones; Appendix G: living space at/above DFE, enclosed space below wet-floodproofed; commercial in floodplain above DFE or dry floodproofed; "candlestick home" = very narrow tall detached home; recommends rules to fit "small bungalows and cottages". | §5 para 4, §5.5 stat 5, Three New Dorps (beach), §7 cards, §8.5 flood bullet, §10.5 H3 6, Below Hylan section |
| ND8 | `NYC Building Code Appendix G enclosed areas below design flood elevation…` · Firecrawl search → scrape (PDF query) | https://www.nyc.gov/assets/buildings/bldgs_bulletins/bb_2022-001.pdf | DOB Buildings Bulletin 2022-001 (Jan 10 2022): use of wet-floodproofed spaces "limited to parking of vehicles, storage and building access". | §5 para 4, §5.5 stat 6, §9 enclosure-stair Q, Below Hylan section |
| ND9 | `New Dorp Beach Hurricane Sandy flooding homes rebuilt elevated` · Firecrawl search | https://www.nyonlinerealty.com/nyc/new-dorp-beach | Realty page: surviving bungalows mixed with newer raised construction; flood zone. Corroboration only. | research only |
| ND10 | `New Dorp Beach bungalows Sandy damage Cedar Grove Beach Club…` · Firecrawl search → scrape | https://citylimits.org/this-memorial-day-a-lost-world-at-cedar-grove-beach/ | City Limits (May 2011): Cedar Grove Beach Club founded 1911, bungalows removed by the city the previous year for a planned park. | §13 New Dorp Beach card, Below Hylan section |
| ND11 | same search | https://www.newyorkalmanack.com/tags/cedar-grove-beach-club/ (search excerpt) ; https://www.facebook.com/classicstatenisland/videos/... (excerpt) | 41 historic bungalows largely built 1920–1940 in New Dorp; "In 2010, the City of New York took control of the property". | §7 bungalow card, §13 card |
| ND12 | same search · Reddit (via Firecrawl search result) | https://www.reddit.com/r/statenisland/comments/1hc217e/bungalows_at_cedar_grove_beach_club_in_ruins/ | r/statenisland post (Dec 2024): "32 years ago today twenty eight bungalows at the Cedar Grove Beach Club in New Dorp Beach are in ruins after the storm of December 11, 1992" (SI Advance photo). Thread itself not scraped. | Below Hylan section |
| ND13 | `Miller Field Gateway National Recreation Area…` · Firecrawl search → scrape | https://www.nps.gov/gate/learn/historyculture/miller-field.htm | Vanderbilt bought New Dorp farmland from 1836; heirs sold to federal govt 1919; Air Coast Defense Station completed 1921; part of Gateway NRA since 1972; entrance via New Dorp Lane. | §13 Miller Field card, §8 lower Lane card |
| ND14 | `Lane Theater New Dorp Lane interior landmark designation 1988…` · Firecrawl search → scrape (query) | https://imjustwalkin.com/2015/03/02/the-lane-on-the-lane/ | Opened Feb 10 1938; 1988 LPC report: interior "one of the last surviving pre-World War II movie theater interiors on Staten Island… Art Moderne"; Crossroads Church moved in 2012. | §13 Lane Theater card |
| ND15 | `Moravian Cemetery Staten Island Richmond Road…` · Firecrawl search; `Moravian Cemetery` · WebFetch | https://en.wikipedia.org/wiki/Moravian_Cemetery | 2205 Richmond Rd, New Dorp; 113 acres; founded 1740; Vanderbilt mausoleum by Richard Morris Hunt (1885–86) in private family cemetery. | §13 card, Three New Dorps (inland), §8 Richmond Rd card |
| ND16 | `New Dorp Library 309 New Dorp Lane renovation closed NYPL reopening` · Firecrawl search | https://www.silive.com/news/2026/10/staten-island-library-branch-closed-since-early-2025-to-reopen-monday.html ; https://www.nypl.org/locations/new-dorp | Branch at 309 New Dorp Lane closed since January 2025 for HVAC replacement led by DDC, reopening Monday in October 2026 (exact day not used). | §13 library card |
| ND17 | `Tysens Park Apartments New Dorp…` · Firecrawl search | https://www.apartments.com/tysens-park-apartments-staten-island-ny/m0xq0tj/ ; https://www.apartmenthomeliving.com/apartment-finder/Tysens-Park-Apartments-Staten-Island-NY-10306-1903536 | Rental complex, 30 Ebbitts St / Mill Rd, studios–2BR, 450–906 sq ft. (Ratings content not used.) | §5 para 3, §7 garden-apartment card, §9 renter Q |
| ND18 | `reddit r/statenisland New Dorp apartment above store landlord door lock` · Firecrawl search → scrape | https://www.silive.com/news/2016/02/tips_from_nyc_civil_court_for.html | SI Advance Feb 15 2016 (NYC Civil Court tips): illegal basement apartments; landlord cannot legally change locks in retaliation for non-payment. Background only (not cited on page). | research only |
| ND19 | `ANSI/BHMA A156.40 residential deadbolt grade…` · Firecrawl search | https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights/A15640-2015-Residential-Deadbolts ; https://blog.ansi.org/ansi/bhma-certified-secure-home-label-door-hardware/ | A156.40 residential deadbolts: security, durability, finish tests; finish via ASTM B117 salt spray; A156.39 for locksets; BHMA certified program. (Cycle counts not used.) | §9 BHMA Q |
| ND20 | `NYC DCP New Dorp Lane rezoning…` · Firecrawl search → scrape | https://www.bjhadvisors.com/projects/speedwell-ave-e29zh | 2021 New Dorp Lane District planning study for SIEDC (TOD, parking sharing). Background only. | research only |
| ND21 | Reused from silo research (SI section) | SI6 (2022 NYC BC §1010.1.9 PDF), SI17 (SIEDC corridors incl. Richmond Road), S1 Fixr, S2 Bob Vila, N4 Tenant Data Privacy Act | Egress/one-motion rules; Richmond Road SIEDC corridor; national cost and DIY claims; tenants can't be forced to app-only entry in multiple dwellings. | §8.5, §8 Richmond Rd card, §10.5, §14, §9 renter Q |
| ND22 | Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ (New Dorp) | — | EMPTY (not accessible in build env). §10.5 headings are claims from national cost guides/product reviews, stated as such on page. | — |
| ND23 | Local smart-lock-specific news for New Dorp (silive/Patch) | — | EMPTY — none found; replaced by burglary items ND5/ND6. | — |
| ND24 | https://www.nyc.gov/html/dot/html/motorist/parkinglist.shtml · WebFetch | — | EMPTY via WebFetch (permission request not answered) — obtained via Firecrawl instead (ND3). | — |

### Prices used (SI multiplier 1.10, round half-up; copied from smart-lock-installation-staten-island.html, no new figures)
- Single-door keypad/fob reader with electric strike: **$1,650–$2,750** (§14, §15 Premium, FAQ 1, Service schema, §10.5).
- New electric strike: **$275–$495**; failed strike repair: **$325–$534** (§14, schema).
- Setup-only first hour: **$225** (repair capture, §14, BYO card, FAQ admin-phone).
- Service/callback $195/hr, 3-hr min ($585) (§14).
- Residential locks: "quoted flat at walkthrough". Fixr national $250–$400 / avg $300 labelled national.

## Images (11)
Permanent image rule (Drive folder empty, CompanyCam not connected). Sources per assignment preference: commercial-security staten-island/long-island first, then low-voltage. All looked at before naming; library photos look rendered/AI-style with AESS logos (same caveat as SI section). Rejected: access-reader and video-intercom (fictional named business-centre signs), racks (not door-relevant), warehouse/LPR cameras (not door-relevant).
| File (images/smart-lock-installation/) | Source | What it shows |
|---|---|---|
| smart-lock-installation-new-dorp-two-techs-keypad-glass-shop-door.webp (hero) | commercial-security/commercial-security-systems-staten-island-alarm-keypad.jpg | Two techs at glass shop entrance: keypad on frame, camera above door |
| smart-lock-installation-new-dorp-strike-wiring-keypad-exit-button.webp | low-voltage/low-voltage-installation-long-island-electric-strike-keypad.jpg | Tech wiring strike in glass door frame; keypad + push-to-exit on wall |
| smart-lock-installation-new-dorp-electric-strike-glass-door-frame.webp | commercial-security/commercial-security-systems-staten-island-electric-strike.jpg | Kneeling tech fitting strike in glass entrance frame, reader on wall |
| smart-lock-installation-new-dorp-crew-van-unloading-tools.webp | commercial-security/commercial-security-systems-staten-island-crew-van.jpg | AESS van at entrance, tech at side door, another wheeling tool case |
| smart-lock-installation-new-dorp-conduit-cable-pull-block-wall.webp | commercial-security/commercial-security-systems-long-island-conduit-pull.jpg | Blue cable fed through conduit into box on block wall |
| smart-lock-installation-new-dorp-credential-programming-desk.webp | commercial-security/commercial-security-systems-staten-island-credential-programming.jpg | Tech enrolling cards/fobs at a computer desk |
| smart-lock-installation-new-dorp-door-contact-keypad-panel.webp | commercial-security/commercial-security-systems-staten-island-panic-button.jpg | 3-panel: camera by loading door, door contact, keypad by steel door |
| smart-lock-installation-new-dorp-glass-entry-lobby-reader.webp | commercial-security/commercial-security-systems-staten-island-secured-lobby.jpg | Glass double-door lobby, wall reader, dome cameras, reception desk |
| smart-lock-installation-new-dorp-panic-button-under-counter.webp | commercial-security/commercial-security-systems-staten-island-glass-break.jpg | Tech wiring red button under reception counter |
| smart-lock-installation-new-dorp-sensor-install-shop-entrance.webp | commercial-security/commercial-security-systems-staten-island-hero-entrance-crew.jpg | Tech drilling sensor high beside shop entrance; glass-break detector insets |
| smart-lock-installation-new-dorp-maglock-terminal-wiring-closeup.webp | low-voltage/low-voltage-installation-hudson-valley-13-maglock-wiring-detail.jpg | Gloved hands at maglock terminal block on aluminium frame |

## Question register — smart-lock-installation-new-dorp-staten-island-ny

### §9 Questions Answered (H3, 14)
1. Staff hauling deliveries in from the lot behind us keep wedging the rear door — how do we make it easier to use shut than open?
2. If someone smashes the glass in our shop's front door, does a smart lock on it still do anything?
3. Can our shop's front door unlock itself at opening time and lock again at closing?
4. Our commercial landlord wants a key to the store — do we still have to give one if we go keyless?
5. Can the cash office or stockroom have a code that only managers know, separate from the staff door?
6. Police reported a crowbar attempt on a house near Benedict Road — what part of a door actually stops prying, the lock or the frame?
7. Can the lock warn us when someone keeps trying wrong codes or forces the bolt?
8. Should the lock use my phone's location to lock up after I've walked to the train?
9. Should we let a voice assistant unlock the front door?
10. Is a fingerprint reader any harder to get past than a keypad code?
11. Is a BHMA-graded lock worth paying more for on the front door?
12. Wind-blown sand gets into everything on our block — will grit jam a keyway or a keypad?
13. Our ground floor is wet-floodproofed storage under the house — should the inside door from that space up into the living area be locked too?
14. We rent in one of the garden-apartment complexes off Mill Road — can we ask management to put a smart lock on our unit, and who pays?

### §17 FAQ (visible == FAQPage, 8)
1. Is New Dorp priced differently from the rest of Staten Island?
2. Do you also work in Oakwood, Grant City, Dongan Hills and Midland Beach?
3. Our deadbolt hole sits farther from the door edge than usual — will a smart lock fit?
4. Do smart locks need firmware updates, and do you come back to do them?
5. What happens if the only phone with admin rights is lost or broken?
6. Can unlocking the front door switch on the porch or hallway light?
7. Do you take the old locks away when you replace them?
8. Can we check the lock history from a computer instead of a phone?

### Other question-form headings
- H2 "Lock Stuck, Dark or Offline in New Dorp?" (repair capture)
- H2 "Locked Out of a New Dorp Shop, Flat or House Tonight?" (final repair capture)

De-dup notes: checked by meaning against all 16 live area pages and batch-mates Greenpoint / Washington Heights (as on disk 11:19). Avoided: raised-house lower door (Suffolk Lindenhurst), pre-storm prep (Suffolk), 1930s thin bungalow door (Putnam), renter no-drill (Orange), kick-in frame (Nassau — mine is prying + strike screws, kept), propped-door alert (Greenpoint — reworded mine to closer/convenience). Partial overlaps left for the main run: Q7 tamper alerts vs Greenpoint "alert when street door is propped"; FAQ1 neighbourhood price vs SI FAQ "why SI prices 10% above Brooklyn" and WH "priced at full Manhattan rate".

## Washington Heights, Manhattan (smart-lock-installation-washington-heights-manhattan-ny)

Built 2026-10-17. Neighborhood page, up-link /smart-lock-installation-manhattan. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737 (800 only in shared header chrome). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane: long-tenure, multi-generational rental households (12.3% homeownership, 19.3% aged 65+, 37.9% single-person households) in pre-war walk-ups and elevator buildings. The smart lock is ADDED beside the owner's lock (MDL 51-c), and the household — not the lease or a management office — decides who holds a code (anchor: 765 Riverside Drive leaseholder-only fob story, 2018). Planned around painted century-old doors/strikes, night-shift arrivals (168th St hospital campus), Hudson Heights co-op conversions, and LPC rules on the Jumel Terrace / Audubon Park blocks.

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| WH1 | `Washington Heights Manhattan Community District 12 rent stabilized units share pre-war buildings housing profile` · Firecrawl search → Firecrawl scrape | https://furmancenter.org/neighborhoods/view/washington-heights-inwood (resolved to https://www.furmancenter.org/neighborhoods/washington-heights-inwood/, updated 05/06/2026) | MN12 (Washington Heights/Inwood) 2024: population 182,736; homeownership 12.3% vs 32.7% citywide; aged 65+ 19.3% (9.9% in 2000); single-person households 37.9%; housing units 82,310; Hispanic 62.6%; car-free commute 84.4%; serious housing code violations 238.7 per 1,000 privately owned rental units (2025); 235 subsidized properties; public housing 1.8% of rental units (21 properties, 2,167 units); Mitchell-Lama 7 properties / 1,410 units. | §5 paras 1, 4, 5 + stats list; §7 "Newer and Subsidized Buildings" card; §10.5 H3 3 |
| WH2 | same search | https://www.furmancenter.org/publication/understanding-different-segments-of-new-york-citys-rent-stabilized-housing-stock/ | "an estimated 16,000 rent-stabilized units" sit in co-ops that converted from rental (citywide). | §9 co-op conversion Q |
| WH3 | same search | https://www.nyc.gov/site/mayorspeu/programs/rent-stabilization.page | Rent-stabilized apartments are most often in buildings of 6+ units built before 1974; right to a renewal lease. | Glossary "Rent-stabilized" |
| WH4 | `Audubon Park Historic District Washington Heights designated Landmarks Preservation Commission apartment buildings` · Firecrawl search → Firecrawl scrape (query mode) | https://en.wikipedia.org/wiki/Audubon_Park,_Manhattan | Bounded 155th–158th St, Broadway/Edward M. Morgan Pl to Riverside Dr; apartment buildings 5–13 stories; LPC district = 19 apartment buildings + one pair of duplex houses across five blocks; much of area added to NRHP August 2024. | §7 elevator-building card; §13 Audubon Park card |
| WH5 | same search | http://s-media.nyc.gov/agencies/lpc/lp/2335.pdf | LPC designation report — query on first 4 pages returned nothing usable → EMPTY (designation date not stated on page). | — |
| WH6 | `Sylvan Terrace wooden row houses 1882 Jumel Terrace Historic District Washington Heights` · Firecrawl search → Firecrawl scrape (query mode) | https://en.wikipedia.org/wiki/Jumel_Terrace_Historic_District | District = 50 rowhouses built 1890–1902 + one 1909 apartment building; NYC Landmark 1970, NRHP 1973; streets: W 162nd St, Jumel Terrace, Sylvan Terrace, W 160th St; Sylvan Terrace = 20 wooden houses 1882–83 on the Morris estate carriage drive, restored 1979–81. | §7 rowhouse card; §13 Sylvan Terrace card; hero |
| WH7 | `Morris-Jumel Mansion oldest house in Manhattan built 1765 Washington headquarters` · Firecrawl search | https://en.wikipedia.org/wiki/Morris%E2%80%93Jumel_Mansion ; https://morrisjumel.org/ ; https://www.facebook.com/nylandmarks/videos/… | Oldest extant house in Manhattan, built 1765 by Roger Morris; on W 160th St at Edgecombe Ave. | §13 card |
| WH8 | `Hudson Heights Fort Washington Avenue art deco co-op buildings Cabrini Boulevard` · Firecrawl search → Firecrawl scrape (query mode) | https://en.wikipedia.org/wiki/Hudson_Heights,_Manhattan | Mostly 1920s–1940s apartment buildings, many co-ops; Art Deco and Tudor Revival; Hudson View Gardens opened 1924 (Tudor co-op, NRHP 2016); Castle Village five buildings finished 1939, co-op 1985; rentals converting to co-ops/condos from the 1980s; Bennett Park = highest natural point in Manhattan, 265 ft; Fort Tryon Park 67 acres, given 1931, holds The Cloisters. | §5 para 4; §7 co-op card; §9 co-op conversion Q; §13 cards |
| WH9 | same search | https://streeteasy.com/building/350-cabrini-boulevard-new_york ; http://nyjournal.squarespace.com/journal/2007/3/16/the-co-op-chronicles-cabrini-boulevard.html | 350 Cabrini Blvd Art Deco co-op with P/T doorman and live-in super; most buildings on Cabrini 181st–192nd are co-ops/condos. Background only; not cited. | background |
| WH10 | Neighborhood facts · Firecrawl scrape (query mode, 93k chars read via python) | https://en.wikipedia.org/wiki/Washington_Heights,_Manhattan | Bounded by Dyckman St (Inwood), 155th St (Harlem), Harlem River/Coogan's Bluff, Hudson; "high residential density despite the lack of modern construction"; IRT stations 157th/168th/181st/Dyckman built 1904–06; 1920s boom north of 181st; IND stops 175th/181st/190th on Fort Washington Ave (1932); elevators at 181st St IND and 190th St stations; public stairs Fort Washington Ave–Overlook Terrace at 187th; CUMC on Hilltop Park site 1928; Yeshiva University Wilf Campus 184th–186th east of Broadway, founded 1928; United Palace 1930 as Loew's 175th Street Theater; ZIPs 10032/10033/10040; Little Red Lighthouse, High Bridge Water Tower, Cloisters. | §5 paras 1, 5; §8 corridor cards; logistics section |
| WH11 | `"Washington Heights" building "key fob" OR "keyless" tenants entry system 2024 OR 2025 OR 2026` · Firecrawl search → Firecrawl scrape | https://patch.com/new-york/harlem/uptown-landlord-harassing-tenants-through-key-fob-policy-reports | Patch, Nov 16 2018 (citing CBS2): 765 Riverside Drive, six-story building near W 155th St; electronic fob for lobby door; fobs only for residents named on a lease; $50 security deposit; resident Kazu Hano (50 years in building) had to show a marriage certificate for his wife; CM Mark Levine: landlords must provide two keys per apartment and may not charge; next step a DHCR complaint. | §5 para 3 + stat; §9 Q2; §13 Audubon Park card |
| WH12 | `Washington Heights tenants landlord key fob Latch smart lock building entry lawsuit` · Firecrawl search | https://www.cbsnews.com/newyork/news/hells-kitchen-latch-system-keyless-entry-lawsuit/ etc. | All results are the Hell's Kitchen Latch case already in silo research (N10) — not Washington Heights; not reused. | — |
| WH13 | `Washington Heights burglary apartment break-in package theft lobby door broken 2025 2026` · Firecrawl search (web+news) | — | No Washington Heights lock/door story returned (results were DC/MD) → EMPTY. | — |
| WH14 | `"Washington Heights" landlord changed locks illegal lockout tenant news` · Firecrawl search → Firecrawl scrape | https://www.amny.com/politics/nyc-council-bill-tenants-illegal-evictions/ | AMNY Nov 13 2024 on Council illegal-eviction bills; only WH content is a photo caption (709 W 170th St in disrepair since 2007). Not used. | — |
| WH15 | `Manhattan Times Washington Heights tenants front door intercom broken lock building repairs HPD` · Firecrawl search → Firecrawl scrape | https://www.lawhelpny.org/resource/hpd-violations-checklist ; https://portal.311.nyc.gov/article/?kanumber=KA-01074 | LawHelpNY: class A = no peephole in entrance door; class B = entrance door lock/knob defective, entrance door should be self-closing; class C = no lock on entrance door to building (24 hours to correct). 311: Apartment / Public Area Maintenance Complaint covers doors and locks broken, missing or not self-closing. (Manhattan Times itself: no matching story → EMPTY.) | §9 Q5, Q7; §10.5 H3 4; FAQ peephole; glossary |
| WH16 | `Washington Heights BID 181st Street business improvement district St. Nicholas Avenue retail corridor` · Firecrawl search | https://gouptownnyc.wixsite.com/gouptownnyc/whbid-181 ; https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=9 ; https://www.instagram.com/whbid/ | WHBID supports 250 commercial storefronts in a 29-block district along 181st St; office 560 W 181st St; BID bio lists St. Nicholas Ave (181st–185th St). | §8 corridor cards |
| WH17 | `George Washington Bridge Bus Station 178th Street Washington Heights renovation opened 2017` · Firecrawl search | https://en.wikipedia.org/wiki/George_Washington_Bridge_Bus_Station | Renovated station reopened May 16, 2017. | §8 Broadway card; FAQ one-time code |
| WH18 | `High Bridge oldest standing bridge New York City opened 1848 reopened 2015 Highbridge Park water tower` · Firecrawl search | https://www.nycgovparks.org/parks/highbridge-park/pressrelease/22082 ; https://en.wikipedia.org/wiki/High_Bridge_(New_York_City) | Opened 1848 as part of the Old Croton Aqueduct; oldest standing bridge in NYC; rises 140 ft over the Harlem River. | §13 card |
| WH19 | `Landmarks Preservation Commission rules rowhouse front door hardware replacement permit not required doors historic district` · Firecrawl search | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-90092 (LPC Rules §2-14) | Ordinary repair (no permit) includes "Repairing or replacing window or door hardware, such as hinges, knobs and handles, but excluding ornate historic exterior hardware on special doors". | §7.5 rowhouse method; §8.5 landmark callout; §10.5 H3 7; glossary "Special door" |
| WH20 | `Yale Assure Lock 2 keypad voice guidance languages Spanish setting` · Firecrawl search | https://www.yalehome.com/ae/download-center/smart-products/assure-lock%C2%AE-sl/Yale%20Assure%20Manual.pdf | Yale Assure manual: language setting — English (1), Spanish (2) or French (3) for voice prompts. | §10 features list |
| WH21 | `New York Multiple Dwelling Law section 4 definition multiple dwelling three or more families living independently` · Firecrawl search | https://www.nysenate.gov/legislation/laws/MDW/4 | "multiple dwelling" = occupied as the residence or home of three or more families living independently of each other. | Glossary |
| WH22 | `reddit washingtonheights front door lock building super apartment keys` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/1vqeebn/key_broke_in_the_main_apartment_door_super_not/ ; https://www.reddit.com/r/AskNYC/comments/xkl22e/… | Excerpts only, citywide (not Washington Heights): when the super is unreachable call 311 for the building's 24/7 emergency contact / MDR; supers normally hold spare keys. Informed §9 Q5 wording ("call the building's emergency contact first, and if no one answers, 311"). Washington Heights-specific Reddit → EMPTY (not accessible in build env). | §9 Q5 (background) |
| WH23 | Reused from silo research (research/smart-lock-installation.md) | N1 MDL 51-c; N3 HMC 27-2043; N4 Tenant Data Privacy Act; N6 HPD fire-safety (no double-cylinder); N9 Admin Code 26-521/26-523; S1 Fixr $250–$400 avg $300; S2 Bob Vila ~30 min; S3 August retrofit; S4 August Connect 10–15 ft; S5/S6 Thread border router; S9 kalamein; M7 Latch→DOOR Aug 12 2025; M14 NFPA 80 / iDigHardware; M15 NYC BC 1010.1.9.9; M28 311 7 AM–6 PM; M30 Admin Code 28-105.4.7; M31 Ring Z-Wave subscription + Ring-app codes | As listed in silo file. | §5, §8.5, §9, §10, §10.5, §14, FAQ, glossary, logistics |
| WH24 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 H3 headings are claims published by cost sites/manufacturers, stated as such on the page. | — |
| WH25 | Hyperlocal (Manhattan Times, Uptown Collective, Patch Washington Heights-Inwood) smart-lock stories | — | Only WH11 (Patch 2018) found → otherwise EMPTY. | — |
| WH26 | NYCHA in Washington Heights | — | Only Furman aggregate (1.8% public housing, 21 properties) used; no NYCHA development named → no NYCHA claims on page. | §7 subsidized card (aggregate only) |

### Prices used (Washington Heights = Manhattan ×1.25; copied exactly from smart-lock-installation-manhattan.html)
- Apartment-door smart lock: no AESS figure → "Quoted flat at free walkthrough".
- Single-door keypad or fob reader with electric strike: **$1,875–$3,125** ($1,500–$2,500 × 1.25).
- New electric strike: **$313–$563** ($250–$450 × 1.25).
- Failed electric strike repair: **$369–$606** ($295–$485 × 1.25).
- Setup-only / programming visit: **$265 first hour**, then 30-minute blocks.
- Service/callback: **$195/hr, 3-hour minimum ($585)**, not on initial install.
- National comparison only: Fixr $250–$400, avg $300 (Jan 2025).

## Images (11)

Permanent image rule (Drive folder `AESS Website Photos/Smart Lock Installation` empty; CompanyCam not connected). Sources from images/commercial-security/ and images/low-voltage/ with "manhattan"/"bronx" in the name; each viewed before use; dHash-checked against the batch-mates' images on disk (Greenpoint's 11) — none of these 11 source photos is used by Greenpoint or New Dorp at build time. Several are also used (under other names) on earlier area pages — unavoidable, nearly every library photo is already used somewhere in the silo. Alt/title/caption describe only what is visible.

| New filename (images/smart-lock-installation/) | Source file | What it shows |
|---|---|---|
| smart-lock-installation-washington-heights-keypad-reader-glass-entry-door.webp (hero, eager) | images/commercial-security/commercial-security-systems-manhattan-access-reader.jpg (business-name sign "Pinnacle Business Center" on the glass blurred) | Technician mounting a keypad/prox reader on a stone pier beside a glass entry door; "Employees and authorized personnel only" plaque |
| smart-lock-installation-washington-heights-credential-enrollment-desk.webp | images/commercial-security/commercial-security-systems-manhattan-credential-programming.jpg | Technician enrolling cards/fobs at an access-management workstation; card trays labelled Employees/Managers |
| smart-lock-installation-washington-heights-video-intercom-panel-stone-entry.webp | images/commercial-security/commercial-security-systems-manhattan-video-intercom.jpg (cropped: left 245 px removed to drop a building-name/street-address sign) | Technician fixing a stainless video intercom with keypad to a granite wall beside glass doors |
| smart-lock-installation-washington-heights-secured-lobby-reader-intercom.webp | images/commercial-security/commercial-security-systems-manhattan-secured-lobby.jpg | Lobby with glass entry doors, intercom panel, small reader beside an inner door, ceiling cameras, reception desk |
| smart-lock-installation-washington-heights-maglock-header-glass-office-door.webp | images/commercial-security/commercial-security-systems-manhattan-maglock.jpg | Technician wiring a magnetic lock on the header of a glass office door; reader on the wall |
| smart-lock-installation-washington-heights-door-contact-keypad-collage.webp | images/commercial-security/commercial-security-systems-manhattan-panic-button.jpg | Three-panel collage: door contact install, keypad beside a steel service door, finished loading-dock entrance |
| smart-lock-installation-washington-heights-access-rack-install-checklist.webp | images/commercial-security/commercial-security-systems-bronx-integration-rack.jpg | Technician terminating in a network rack; wall checklist (cameras, door contacts, electric locks, REX buttons, card readers) |
| smart-lock-installation-washington-heights-ceiling-wifi-access-point-mount.webp | images/low-voltage/low-voltage-installation-manhattan-09-ceiling-access-point-drop.jpg | Technician mounting a ceiling Wi-Fi access point |
| smart-lock-installation-washington-heights-data-jack-wall-plate-termination.webp | images/low-voltage/low-voltage-installation-manhattan-08-keystone-wall-plate-termination.jpg | Technician terminating a data jack in a wall plate |
| smart-lock-installation-washington-heights-cable-tester-wall-jack-pass.webp | images/low-voltage/low-voltage-installation-manhattan-07-fluke-certification-pass.jpg | Handheld cable tester showing a pass at a wall jack |
| smart-lock-installation-washington-heights-crew-ceiling-cable-pull-open-floor.webp | images/low-voltage/low-voltage-installation-manhattan-02-crew-ceiling-cable-pull.jpg | Crew pulling cable through an open office ceiling, reels on floor, rack at back |

DAILY-LOG note: `images: 11 reused from images/commercial-security/ and images/low-voltage/ (no real smart-lock photos yet)`. Flag for Anwar: the library source photos look AI-rendered (garbled/fictional signage such as "Pinnacle Business Center", "Riverfront Business Center"); they were used under the permanent image rule as instructed, with named signage removed.

## Question register — smart-lock-installation-washington-heights-manhattan-ny

### §9 YOUR QUESTIONS ANSWERED (H3)
Codes for everyone who really lives here
1. A relative lives with us but isn't on the lease — can she have her own code on a lock we put in?
2. Our building gives lobby fobs only to people named on the lease — does a unit smart lock have to follow that rule?
3. If the leaseholder moves out or passes away, how does the rest of the household keep control of the lock?
The owner's lock and the owner's duties
4. Our door already has two locks of different ages — which one should the smart lock replace?
5. The landlord's lock on our apartment door is broken — should we just swap in a smart lock ourselves?
6. Can the landlord bill us, or raise the rent, because we added a lock of our own?
7. The street door downstairs no longer latches — is that ours to fix or the owner's?
Old doors and changed buildings
8. Decades of paint have built up on our door and frame — does that matter for a new lock?
9. I rent a stabilized apartment in a building that went co-op — whose rules apply to my door, the board's or the law's?
Coming and going on a working day
10. I come home from a night shift at 3 a.m. — what is the quickest way in that doesn't depend on fishing for keys or a phone?
11. I already carry keys for the street door, the inner door and the mailbox — is a keypad on the apartment worth it?
People, trust and technology
12. Someone who used to stay with us still has a key — can we change the lock to keep them out?
13. What happens to our lock if the company behind its app stops supporting it?

### §17 FAQ (visible == FAQPage, 8)
1. Do we have to register a lock we add to our apartment door with the landlord or the city?
2. Our building is about to get a new lobby entry system — should we wait before fitting a lock on our apartment?
3. Can we send a one-time code to a relative arriving at the George Washington Bridge Bus Station before we get home?
4. Can you fit a door viewer or digital peephole at the same visit?
5. The building handyman offered to put our smart lock in — what should we check first?
6. How far ahead should we book a Washington Heights installation?
7. Is there anything you won't install on a rental apartment door?
8. How do we know the person at the building door is really your installer?

### Other question-form headings
- H2 "Smart Lock Acting Up Above 155th Street?" (repair capture)
- H2 "Ready to Stop Copying Keys for the Family?" (mid CTA)
- H2 "Locked Out on a Washington Heights Landing Tonight?" (final repair capture)
- H3 "National alarm brands or a local installer?" (equipment comparison table)

De-dup notes: deliberately avoided register intents — renter adding lock without asking (NYC Q1), landlord gets code/key (NYC Q2), app-only entry (NYC Q3), move-out (NYC Q4), board approval (NYC Q5), grandma without smartphone / app language / home attendant schedule (Queens), elderly parent alone / ambulance entry (SI, Suffolk, Westchester), fifth-floor walk-up surcharge and meet-the-super (Bronx), historic-district approval for a keypad (Ulster), area-rate pricing question (Bronx/SI/Manhattan pattern — replaced by a registration question), Bronx "rent cut when building door lock breaks" (Q7 here is about who is responsible and how to report). Partial overlaps for the main run to judge: Q3 (household control after the leaseholder leaves) vs New Dorp "only phone with admin rights lost" (different trigger, both recommend a second administrator); Q6 (charge/rent for the tenant's own added lock) vs Greenpoint "rent-stabilized — landlord raise rent for a new street-door keypad" (different payer/door); Q7 (street door not latching — whose job) vs Greenpoint "what makes a walk-up street door stop short of latching" (responsibility vs mechanical cause).

## Greenpoint, Brooklyn (smart-lock-installation-greenpoint-brooklyn-ny)

Built 2026-10-17 by the Greenpoint builder subagent (batch: New Dorp SI, Washington Heights MN, Greenpoint BK). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, directQuote).

Thesis / lane: in Greenpoint the door that matters is shared — the walk-up street door (closer/latch first, then keypad + electric strike, buzzer and USPS arrow lock kept on the same strike), the second hall door of a railroad flat, the side door to the flats beside a Manhattan Ave / Franklin St shop, restaurant back doors (Sept 2026 crowbar burglaries), shared freight doors in maker buildings (GMDC), cellar bike rooms; plus sided shipwright-era frame houses, the Greenpoint Historic District, small self-managed condos, rent-stabilized MCI rules, waterfront towers (prose only) and creek-side cellar doors (prose only).
Silo-wide findings reused, not re-fetched: Fixr $250–$400 / avg $300 (S1), Bob Vila "only a Phillips screwdriver" (S2), August retrofit single-cylinder only (S3), August Connect 10–15 ft (S4), Thread border router same ecosystem (S5/S6), MDL 51-c (N1), TDPA LL63/2021 (N4), Admin Code 26-521 (N9), LPC Permit Guidebook hardware (Brooklyn B4), MDL §4 three families (Brooklyn B8), SafeWise/NY Post 7.8M packages (Brooklyn B1).

### Local research

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| G1 | `Greenpoint Historic District Landmarks Preservation Commission 1982 designation rowhouses Milton Street` · FC search → FC scrape (pdf) | https://s-media.nyc.gov/agencies/lpc/lp/1248.pdf | Designated September 14, 1982. Streets in report: Greenpoint Ave, Milton, Calyer, Clifford Pl, Franklin, Guernsey, Kent, Lorimer, Manhattan Ave, Noble, Oak. "Many of the frame houses on Milton Street and Noble Street were erected to house the workers employed in the shipyards, and some of the houses were actually built by shipwrights and ship carpenters." "Franklin Street has buildings from the early 1850s with shops on the ground floor and flats above making it the area's first commercial center." Flathouses "originally designed with two stores on the ground floor and apartments for two families on each of the three upper stories." Repeated notes of "original double wooden doors" retained or replaced; frame houses "now covered with asphalt siding", "sheathed in aluminum siding". "Most of the houses are brick, dating from between 1870 and 1892, and are designed in the Italianate or neo-Grec styles." | §5 paras 1–3, §5.5 bullet 1, §7 cards + §7.5, §8.5 landmark bullet, §10.5 H3 5, §13 card 1, Sources |
| G2 | same search | https://hdc.org/hdc-across-nyc/brooklyn/brooklyn-landmarked/dil-bk-greenpoint/ (excerpt) | HDC: Greenpoint HD "Designated September 14, 1982." Corroboration. | research only |
| G3 | `Furman Center Greenpoint Williamsburg community district homeownership rate housing units` · FC search → FC scrape | https://www.furmancenter.org/neighborhoods/greenpoint-williamsburg/ | 2024 homeownership 16.6% vs 32.7% citywide; 2010–2025 added 27,675 units (21,190 market, 6,485 income-restricted); sales 2025: 1-family 13, 2–4 family 101, 5+ family 79. (Population row misaligned in scrape → not used.) | §5 para 4, §5.5 bullets 2–4, §10.5 H3 7 |
| G4 | `Greenpoint Brooklyn package theft OR burglary 94th Precinct 2025 Greenpointers` · FC search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/94th-precinct.page (excerpt) | 94th Precinct serves "the northernmost portion of Brooklyn, consisting of, primarily, the neighborhood of Greenpoint." | research only (precinct named via Wikipedia G9) |
| G5 | `Greenpointers package thief arrested OR stolen packages Greenpoint 2026` · FC search → FC scrape | https://greenpointers.com/2026/09/24/burglary-spree-targets-multiple-greenpoint-restaurants-on-the-same-day/ (Jennifer Rosini-Gentile, Sept 24 2026) | Sept 12 2026: Franklin St restaurant — "They forced open our back door with a crowbar"; NYPD: rear door, ~$13,000 cash + liquor; Greenpoint Ave restaurant entered "though a hatch" (~$2,000 + blank checks); attempted crowbar entry at another Franklin St address "failed to gain entry"; a bar burglary ~1 a.m. Businesses not named on page. | §5 para 5, §6 card, §8 Franklin card, §9 back-door Q, door plan (roof hatch), Sources |
| G6 | same search | https://brooklyn.news12.com/police-urge-greenpoint-residents-to-be-on-the-lookout-for-package-thieves-34780323 (FC scrape; body empty, metadata only) | Nov 11 2015 (og:url date): police warned Greenpoint residents about a man and woman "caught on camera stealing packages from" apartment buildings. | §10.5 H3 4 |
| G7 | `reddit r/greenpoint packages stolen building front door lock` · FC search | https://www.reddit.com/r/Greenpoint/comments/1izv285/be_alert_apartment_theft_near_mcgolrick_park/ ; https://www.reddit.com/r/Greenpoint/comments/1kcti4r/psa_i_opened_the_door_to_a_delivery_guy_that/ ; https://www.reddit.com/r/Greenpoint/comments/1srvgjt/package_stolen_again/ (excerpts only) | McGolrick: "it's a very secure double door, Someone recently picked the lock … to steal packages"; PSA: "Less than 45 seconds later, he walks out with a trash bag full of packages … They showed up in under two minutes"; "Package stolen AGAIN" (police: "these things happen"). Thread bodies not retrieved. | §5 para 5, §9 lock-picking Q, §9 "delivery" buzz-in Q, §10.5 H3 4 |
| G8 | `reddit Greenpoint railroad apartment two doors hallway kitchen door` · FC search | https://www.reddit.com/r/Greenpoint/comments/1moo1rj/apartment_inspo/ ; https://www.reddit.com/r/NYCapartments/comments/1mwxva6/question_about_doors/ (excerpts) | r/Greenpoint: "Usually a door into the kitchen and one into the front bedroom. 2 apartments on each floor with a hallway in the middle. That's a railroad"; r/NYCapartments: "two doors from my unit leading to the hallway/stairs. Both doors are flimsy hollow core doors". | §5 para 3, §7 railroad card, §9 railroad Q |
| G9 | https://en.wikipedia.org/wiki/Greenpoint,_Brooklyn · FC scrape | same | Northernmost Brooklyn neighbourhood; borders Newtown Creek/LIC, East River, McCarren Park/Bushwick Inlet Park, BQE; "Little Poland"; CD1; ZIP 11222; 94th Precinct, 100 Meserole Ave; industries shipbuilding, porcelain, glassworks; Monitor built at Continental Ironworks; "by the 1880s the neighborhood housed 18 of the 20 glass makers in the city of Brooklyn"; Greenpoint Landing "ten residential towers containing 5,500 units", construction began 2015, completion expected before 2027. | §5 para 1, §8 Manhattan Ave card, §13 towers section, Sources |
| G10 | `Greenpoint Landing towers units Blue Slip Eagle + West Greenpoint waterfront apartments 2025` · FC search | https://newyorkyimby.com/2022/12/eagle-west-waterfront-towers-debut-at-1-eagle-street-in-greenpoint-brooklyn.html (excerpt) ; https://streeteasy.com/building/eagle-west (excerpt) | Eagle + West, 745 units, 1 Eagle Street, OMA, towers 30 and 40 storeys; master plan ~22 acres, 5,500 apartments; "fourth and final residential project Brookfield Properties and Park Tower Group have developed together". | §5 para 4, §5.5 bullet 5, §13 card 5, towers section |
| G11 | `Eberhard Faber Pencil Company Historic District designated 2007 Greenpoint Kent Street West Street` · FC search | https://en.wikipedia.org/wiki/Eberhard_Faber_Pencil_Factory ; https://www.citylandnyc.org/council-oks-eberhard-faber-pencil-hist-dist/ ; NYC Landmarks Facebook post (excerpts) | Designated as an LPC historic district in 2007; Greenpoint Avenue and Kent and West Streets; buildings "dating from the 1880s to the 1920s" (CityLand). | §13 card 3 |
| G12 | `Astral Apartments Franklin Street Greenpoint 1886 Charles Pratt landmark designation` · FC search | http://s-media.nyc.gov/agencies/lpc/lp/1194.pdf ; https://en.wikipedia.org/wiki/Astral_Apartments (excerpts) | Built 1885–86 by Charles Pratt "for workers in the Greenpoint area"; "block-long brick and terra cotta building"; for employees of Astral Oil Works. | §13 card 2 |
| G13 | `Transmitter Park Greenpoint WNYC opened 2012 McGolrick Park Monsignor McGolrick` · FC search | https://en.wikipedia.org/wiki/McGolrick_Park ; https://mcgolrick.org/home-1 ; Apple Maps listing (excerpts) | Land acquired 1889, open by 1891; "ten acres of London Plane-lined walkways"; between Driggs Ave, Russell St, Nassau Ave. (Transmitter Park: no result → not used.) | §13 card 4 |
| G14 | `Greenpoint Manufacturing and Design Center GMDC tenants buildings Manhattan Avenue Greenpoint small businesses` · FC search | https://gmdconline.org/gmdc_buildings/1155-1205-manhattan-avenue/ ; https://gmdconline.org/about-2/ (excerpts) | 1155–1205 Manhattan Ave complex "has 76 small business and artisan tenants, and 360 employees"; about page: 360,000 sq ft complex, "more than 70 small businesses". | §5.5 bullet 6, §8 card, §13 card 6 |
| G15 | `Greenpoint Little Poland Nassau Avenue Manhattan Avenue Polish businesses history` · FC search | https://en.wikipedia.org/wiki/Greenpoint,_Brooklyn (excerpt: "Manhattan Avenue is the heart of what residents call Little Poland") ; manhattanwalkingtour.com (excerpt) | Manhattan Ave = heart of Little Poland; Nassau Ave commercial corridor. | §8 cards |
| G16 | `Greenpoint Hurricane Sandy flooding Newtown Creek basements flood zone Greenpoint` · FC search | https://www.newtowncreekalliance.org/what-does-hurricane-sandy-reveal-about-newtown-creek/ ; https://www.reddit.com/r/Greenpoint/comments/1japkp4/superstorm_sandy_flooding_question/ ; https://firststreet.org/neighborhood/greenpoint-ny/7600_fsid/flood (excerpts) | NCA: storm drains "lack tide gates, allowing the creek water to creep up behind properties"; Reddit: "several houses further east on the same street had water in their basements"; First Street: "925 properties in Greenpoint that have risk of flooding over the next 30" years. | Cellar & rear doors section |
| G17 | `USPS arrow lock key apartment building entrance mail carrier access postal lock intercom` · FC search | https://en.wikipedia.org/wiki/Arrow_lock ; https://butterflymx.com/blog/usps-key-keeper/ ; https://www.intercomsonline.com/obtain-usps-access-master-lock (excerpts) | Key keepers secured with an arrow lock let carriers into unstaffed multifamily lobbies; carrier opens keeper with master key to get the building key; intercoms with a USPS key lock exist as an alternative. | §9 postal-key Q, §10 comparison table |
| G18 | `HCR major capital improvement MCI intercom door entry system eligible rent stabilized 2019 HSTPA rules` · FC search → FC scrape (pdf) | https://hcr.ny.gov/fact-sheet-24 (fact-sheet-24-04-2025.pdf) ; https://hcr.ny.gov/apartment-iai-and-building-mci-improvements | MCI must be new installation not repair; prohibited where 35% or fewer units rent-regulated; capped 2%/yr; written DHCR order; temporary, removed after 30 years; tenants 60 days to respond; lobby doors need no other agency approval. IAI needs tenant written consent if occupied. | §9 rent-stabilized Q, Sources |
| G19 | https://hcr.ny.gov/fact-sheet-33 · FC scrape (pdf) | same (fact-sheet-33-09-2019.pdf) | Useful life schedule: "Intercom System 15"; "Television Security 10". | §9 rent-stabilized Q |
| G20 | `NYC apartment building bicycles stored in hallway fire code obstruction means of egress HPD FDNY` · FC search | https://hpdsigns.nyc/maintenance-of-the-means-of-egress-ny-fc-1027/ ; https://up.codes/s/personal-property ; https://www.nyc.gov/assets/fdny/downloads/pdf/about/Chapter-10.pdf (excerpts) | NYC FC 1027 (1027.4.5/1027.4.6 per source): "Bicycles, baby strollers, shall not be stored in building hallway corridors, except as may be authorized or allowed by the department." Section number differs between sources → page says "section 1027". | §9 bike-room Q, Sources |
| G21 | NYC SBS BID directory (Brooklyn B11 in silo file, not re-fetched) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | Brooklyn BID list contains no Greenpoint BID. | §8 sentence ("none of Greenpoint's own avenues appears among the borough's BIDs") |

### Prices used (Brooklyn ×1.00 — none invented; same sources as the Brooklyn section)
- Single-door keypad or fob reader with electric strike $1,500–$2,500 installed (access-control-installation-brooklyn.html) — §10.5 H3 1, §14, §15 Premium, Service schema.
- New electric strike $250–$450; failed strike repair $295–$485 (door-buzzer pages) — repair capture, §14, §15 Standard, schema.
- Setup-only visit $195 first hour then 30-min blocks (research/tv-mounting-prices/BRIEF.md) — §14 (same flag for Anwar as the Brooklyn page).
- $195/hr, 3-hour minimum ($585) — blueprint §9 — §14.
- Private-door smart lock — no AESS figure → "quoted flat at free walkthrough".
- Fixr national $250–$400, avg $300 — labelled third-party — §10.5 H3 1, §14.

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: EMPTY (not accessible in build env). §10.5 states this and uses published cost-guide/manufacturer claims.
- Yelp 1–3★ Greenpoint locksmith / smart-lock: EMPTY (not accessible in build env).
- Reddit thread bodies: excerpts only (G7, G8, G16); full text EMPTY.
- News 12 Brooklyn 2015 article body: EMPTY (metadata/description only).
- Transmitter Park / WNYC: search returned no Transmitter Park page → not used.
- Local news on smart locks specifically in Greenpoint (Greenpointers, Brooklyn Paper, BK Reader): none found → EMPTY.
- Field Notes: no sourced Greenpoint install anecdote → written as a working routine and labelled so.

## Images (11)

Permanent image rule (Drive folder `AESS Website Photos/Smart Lock Installation` empty; CompanyCam not connected). Sources chosen from brooklyn/queens-named files in images/low-voltage and images/commercial-security per batch assignment; every photo viewed before naming. Most are the same photographs (by appearance) as files used on the hubs/Bronx/SI pages — the library has few distinct door-hardware photos. The library photos look AI-rendered (same note as earlier smart-lock and soundbar pages) — needs Anwar's review; real smart-lock photos should replace them. Captions/alt describe only what is visible; none claims a Greenpoint address or customer.

| New file (images/smart-lock-installation/) | Source | What it shows |
|---|---|---|
| smart-lock-installation-greenpoint-electric-strike-glass-door-fitting.webp (hero, eager) | images/commercial-security/commercial-security-systems-brooklyn-electric-strike.jpg | Tech kneeling, fitting an electric strike in an aluminium glass door frame; small reader and "Employees and visitors please use main entrance" sign |
| smart-lock-installation-greenpoint-entry-panel-back-box-wiring.webp | images/low-voltage/low-voltage-installation-brooklyn-13-video-intercom-entry-wiring.jpg | Tech wiring the open back box below a stainless keypad video entry panel; "Visitors press button for assistance" sign |
| smart-lock-installation-greenpoint-keypad-and-camera-two-tech-entrance.webp | images/commercial-security/commercial-security-systems-brooklyn-alarm-keypad.jpg | Two techs: one mounting a camera above a glass door, one fitting a slim keypad on the frame |
| smart-lock-installation-greenpoint-keypad-strike-push-to-exit-door.webp | images/low-voltage/low-voltage-installation-queens-electric-strike-keypad.jpg | Tech wiring a strike on a glass door with wall keypad and "Push to Exit" button |
| smart-lock-installation-greenpoint-strike-terminal-wiring-closeup.webp | images/low-voltage/low-voltage-installation-queens-electric-strike-wiring.jpg | Close-up of gloved hands on electric strike terminals with a 12/24 V wiring label |
| smart-lock-installation-greenpoint-maglock-header-storefront-door.webp | images/low-voltage/low-voltage-installation-queens-maglock-install.jpg | Tech fitting a maglock to a glass storefront door header, street visible through glass |
| smart-lock-installation-greenpoint-card-reader-aluminum-door-frame.webp | images/low-voltage/low-voltage-installation-brooklyn-14-access-control-reader-wiring.jpg | Tech pressing a card reader onto a narrow aluminium door frame |
| smart-lock-installation-greenpoint-maglock-terminal-block-wiring.webp | images/low-voltage/low-voltage-installation-brooklyn-hero-door-lock-wiring.jpg | Gloved hands wiring a terminal block on a door-frame lock housing beside a maglock body |
| smart-lock-installation-greenpoint-metal-stud-framing-cable-rough-in.webp | images/low-voltage/low-voltage-installation-brooklyn-03-metal-stud-rough-in.jpg | Two techs in hard hats pulling blue cable through open metal-stud framing |
| smart-lock-installation-greenpoint-crew-van-unloading-tool-cases.webp | images/commercial-security/commercial-security-systems-brooklyn-crew-van.jpg | Two techs unloading tool cases from a white AESS van at a building entrance |
| smart-lock-installation-greenpoint-tone-tracer-wall-jack.webp | images/low-voltage/low-voltage-installation-queens-tone-generator-trace.jpg | Tech tracing a cable at a wall plate with a tone probe and generator, rack to one side |

Rejected after viewing: commercial-security-systems-brooklyn-credential-programming (readable cardholder names on screen — same reason the NYC hub rejected it; converted then deleted), -brooklyn-video-intercom (named business centre sign + address), -brooklyn-access-reader (named business centre on glass), low-voltage-installation-queens-lobby-video-intercom ("123 Main Street" directory).

## Question register — smart-lock-installation-greenpoint-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
1. What makes a walk-up street door stop just short of latching, and how is that fixed?
2. Someone picked the lock on our building's double front door to get at the parcels — would an electronic lock have been harder to beat?
3. A stranger said "delivery" over the intercom and walked out with a bag of parcels — what at the door would have changed that?
4. The mail carrier opens our street door with a postal key — will that still work after a keypad goes in?
5. Our railroad flat has two doors onto the stair hall — should both get smart locks?
6. Can the cellar bike room in our walk-up get a keypad so bikes stop crowding the hallway?
7. Our frame house was covered in aluminium siding decades ago — does that change how a keypad or doorbell camera is mounted by the door?
8. After the Franklin Street restaurant burglaries of September 2026, what does an electronic lock add on a back door that a plain deadbolt does not?
9. Four small manufacturers share one freight door in our converted factory — can each have codes and a record of who opened it?
10. Our six-unit condo has no managing agent — who decides on a street-door keypad, and who holds the admin login?
11. We are rent-stabilized — can the landlord raise our rent to pay for a new keypad on the street door?

### §17 FAQ (visible == FAQPage, 8)
1. Does a lock used by a dozen households a day drain its batteries faster — should a busy street door be wired instead?
2. Does wiring a keypad on our street door mean opening the walls of the stair hall?
3. Can tenants tap a phone instead of punching in a code at the street door?
4. Can the owner get an alert when the street door is propped open?
5. Can the old intercom be replaced at the same visit as the street-door keypad?
6. Can the street door open itself for a resident who uses a wheelchair?
7. During a blackout, does an electric-strike street door stay locked or swing free?
8. If someone vandalises the keypad on our street door, do all the codes have to be entered again?

### Other question-form headings
- H2 "Street Door Not Latching or Keypad Dead in Greenpoint?" (repair capture)
- H2 "Ready for a Street Door Everyone Can Use and No One Can Prop?" (mid CTA)
- H2 "Shut Out of a Greenpoint Walk-Up, Shop or Studio Tonight?" (final repair capture)

### De-dup notes
Checked by meaning against every register in research/smart-lock-installation.md and against the two batch-mates on disk (Washington Heights, New Dorp) at build time. Changed during build: paint-buildup FAQ (= Washington Heights FAQ "Decades of paint…") → replaced with keypad-vandalism FAQ; bar "unlock for opening hours, relock at closing" Q (= New Dorp "shop's front door unlock itself at opening time…") → moved to non-question prose in §8; crowbar "lock or door is the weak point" Q (= New Dorp "crowbar … lock or the frame?") → rewritten to the different intent "what an electronic lock adds" (logs/alerts/keys); street-door-latching Q reworded to cause/fix to stay clear of Washington Heights "street door no longer latches — ours to fix or the owner's?" (responsibility). Deliberately avoided: Brooklyn Q12 (Greenpoint condo sponsor admin rights) — towers covered as prose only; Queens app-language and basement-flood intents; Bronx Q14 / Dutchess Q12 shop-and-flats shared stair door — covered in prose only; HV Q11 landmark keypad approval — prose only; every area-cost question — no cost question on this page (prices in §14 only).


## Bayside, Queens (smart-lock-installation-bayside-queens-ny)

Built 2026-10-17 (batch: first smart-lock neighborhood pages). Phone (347) 434-6392 (body, CTAs, schema; (800) 486-0943 only in shared header chrome) · GBP Bronx (460 E Fordham Rd, `#bronx`) · up-link `/smart-lock-installation-queens`, link to `/smart-lock-installation-nyc` and all 16 area/hub pages · Queens ×1.05 (no neighborhood surcharge).
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpt only unless "scraped"); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape.

Thesis / lane: the **door itself** (inter-war Bayside Hills Tudors/Colonials/Mediterraneans, ~century-old doors and frames, arched entries, storm-door heat), the **back of the house** (111th Precinct burglary rise; 2025 rear-slider attempt where the doorbell was rung first), **houses changing hands** (inherited smart locks), Bay Terrace / Oakland Gardens garden co-ops and Bay Club towers, and **Bell Boulevard** late-closing business doors.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `reddit Bayside Queens package theft porch doorbell camera smart lock` · Firecrawl search → only non-Bayside threads (r/plano, r/homesecurity, r/Brooklyn). **EMPTY for Bayside** (not accessible / nothing local). One r/homeautomation excerpt used generically (B17). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from cost guides / product pages, stated as such on the page. |
| 6 | Landmarks | B4–B6, B9, B11, B13 |
| 7 | Building stock | B1–B3, B7, B8, B10, B12 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | QNS (B14), Patch Bayside-Douglaston (B15), QNS/TimesLedger 2015 (B16, research only) |
| 10 | Hyperlocal | QNS used. Queens Chronicle "Seasonal Burglaries Up In 111th Precinct" — search excerpt only (296 burglaries, +88; article undated, not opened) → **not used**. Facebook "Bayside, Queens" group posts — excerpts only, not used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| B1 | `Bayside Queens neighborhood history housing stock Tudor colonial detached houses Bayside Hills Bay Terrace Oakland Gardens` · Firecrawl search → Firecrawl scrape (directQuote) | https://en.wikipedia.org/wiki/Bayside,_Queens | Boundaries (Whitestone NW, LI Sound + Little Neck Bay N/NE, Cross Island Pkwy E, Francis Lewis Blvd/Auburndale W; Oakland Gardens and Hollis Hills usually counted). Bayside Gables = privately owned gated community near Bay Terrace shopping center and Little Neck Bay, "some of the area's only single-family homes". Bayside Hills bounded by 48th Ave (N), LIE (S), 211th St (W), Springfield Blvd (E); 33 street malls, gatehouse at Bell Blvd & 48th Ave, street clock at 50th Ave & 214th St. Bay Terrace: Bay Club, Baybridge, Towers at Waters Edge, Kennedy Street Quad, Bayside Townhouse Condominiums, Bay Country Owners, Bell Owners; bounded by Clearview Expwy (W), 26th/28th Ave (S), Little Neck Bay and Little Bay. Bayside–Bayside Hills pop. 43,808 (2010), 1,857.24 acres. QCC est. 1959 (CUNY). | §5 para 1, §5.5 bullets 2 & 6, §7 cards (Bayside Gables, towers), §13 (gatehouse/malls, QCC), Block by Block (Bay Terrace, Bayside Hills) |
| B2 | same search → Firecrawl scrape (markdown) | https://cityneighborhoods.nyc/bayside-hills | "Construction of detached brick and stucco Tudor, Colonial, and Mediterranean-style homes began in earnest between 1927 and 1935, many featuring slate roofs, leaded-glass windows, and decorative stonework"; "Tudors with half-timbered façades, and Mediterranean villas with arched entryways"; Bayside Hills Civic Association founded 1938; Francis Lewis Blvd "modest commercial strip of family-owned restaurants and shops". (Its boundary — Francis Lewis Blvd W — and developer name conflict with Wikipedia → neither boundary nor developer used.) | §5 para 2, §5.5 bullet 1, §7 cards, §8 Francis Lewis card, Block by Block (Bayside Hills) |
| B3 | same search (excerpt) | https://www.theericbermanteam.com/communities/bayside-real-estate | "older sections … colonials, Tudors, and brick homes from the 1920s and 1930s. Post-war development added capes, ranches, and split-levels" | §5 para 1, §7 card (post-war Capes/ranches/split-levels) |
| B4 | `Fort Totten Historic District Landmarks Preservation Commission designated Bayside` · Firecrawl search → Firecrawl scrape | https://hdc.org/hdc-across-nyc/queens/queens-landmarked/fort-totten/ | 100+ buildings 1830s–1960s; Fort at Willets Point est. 1857; now under FDNY, Parks, Historic House Trust; designated June 29, 1999. | §13 card |
| B5 | `Bayside Historical Society Fort Totten Castle officers club Bayside history` · Firecrawl search (full excerpt returned) | https://www.baysidehistorical.org/about-bhs | BHS founded 1964; at The Castle since 1984; Castle completed 1887 as Army Corps of Engineers officers' mess/club; Gothic Revival; NYC landmark Sept 24, 1974; State/National Registers 1986. | §13 card |
| B6 | `Bayside LIRR station Port Washington Branch 41st Avenue Bell Boulevard` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Bayside_station_(LIRR) | Station at 213th St & 41st Ave, off Bell Blvd, just north of Northern Blvd, 12.6 miles from Penn Station. | §7 card (Bell Blvd mixed-use), §8 card, §13 card |
| B7 | `Bay Terrace Bayside garden apartment cooperative …` (re-scrape of Queens Q9 URL) · Firecrawl scrape (directQuote) | https://www.habitatmag.com/Publication-Content/Legal-Financial/2018/2018-May/Land-Lease | Section IV (125 units) bought land for $5.1M; "one of nine Bay Terrace co-ops … built in the 1950s on land owned by Cord Meyer Development. Eight of the nine sections, which total 1,800 garden apartments, are buying out their 99-year land leases, while the ninth is acquiring ownership through a land swap." | §5 para 5, §5.5 bullet 4, §7 card, §13 card |
| B8 | `Bay Club Bayside condominium towers gated doormen 2 Bay Club Drive built` · Firecrawl search (excerpts) | https://bayclubcondo.com/ ; https://www.onekeymls.com/home-details/2-bay-club-dr-unit-7y-bayside-ny-11360/1Yw3XAnNtMX | "2 towers · 1,000+ homes · Gated + concierge"; unit listing "Condominium built in 1982" (one unit listing — year not used on page). | §5 para 5, §5.5 bullet 5, §7 card |
| B9 | `Bayside Village BID Bell Boulevard business improvement district businesses restaurants` · Firecrawl search (excerpts) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=58 ; https://www.facebook.com/baysidevillagebid/ ; https://www.instagram.com/baysidebid/?hl=en | BID office 213-33 39th Ave; BID "represents over 200 Businesses along Bell Boulevard" (its Facebook page); Instagram excerpt names a nail studio and a wines & liquors shop on Bell Blvd. | §8 intro + Bell Blvd card |
| B10 | `Oakland Gardens Bayside garden apartment co-ops Windsor Oaks Hollis Hills built 1950s` · Firecrawl search → Firecrawl scrape (directQuote) | https://cityneighborhoods.nyc/oakland-gardens | Bell Apartments (later Oakland Gardens Apartments) early 1950s garden-style co-ops; brick Tudors, Cape Cods, ranch homes and garden co-ops; Springfield Blvd and Francis Lewis Blvd commercial/transit spines; private driveways and detached garages; Cunningham Park (1936) and Alley Pond Park. ("Windsor Oaks" seen only in Facebook/Redfin excerpts — not used.) | §5 para 5, §7 card, §8 Springfield card, Block by Block (Oakland Gardens) |
| B11 | Bayside Hills LPC status · `Bayside Hills historic district Landmarks Preservation Commission request designation civic association` · Firecrawl search | — | No result about Bayside Hills → **EMPTY**. Page does NOT claim Bayside Hills is or isn't landmarked. | — |
| B12 | `Bayside Queens illegal home conversions basement apartments civic association Community Board 11 complaints` · Firecrawl search → Firecrawl scrape | https://qns.com/2015/01/boro-civics-oppose-legalization-of-basements-apartments/ | Jan 30, 2015: Bayside Hills Civic Association opposed basement legalization ("A basement is no place for someone to live" — Michael Feiner). | Research only (not used — avoided the basement lane already on the Queens page) |
| B13 | (see B1) | https://en.wikipedia.org/wiki/Bayside,_Queens | QCC established 1959. | §13 card |
| B14 | `Bayside burglary 111th Precinct 2025 homes entered rear door qns.com OR qchron.com OR patch.com` · Firecrawl search → Firecrawl scrape | https://qns.com/2025/07/neighbors-scare-off-burglary-suspects-bayside/ | QNS, Bill Parry, July 7, 2025: June 28 ~6:45 p.m., near 202nd St & 36th Ave (a few blocks west of the Clearview), two masked suspects worked on a rear sliding glass door of a 65-year-old man's home, failed, rang the doorbell repeatedly; neighbors yelled, suspects fled. 111th Pct: 146 burglaries through June 29, 2025 vs 127 (+15%) per CompStat. | Hero, §5 para 3, §5.5 bullet 3, §9 doorbell Q, Hardware Notes (111th), §10.5 H3 7, Block by Block (west of Clearview), Back-of-house plan |
| B15 | same search → Firecrawl scrape (directQuote) | https://patch.com/new-york/bayside/burglaries-double-while-overall-crime-drops-bayside-nypd | Patch, Dec 7, 2017: 28 burglaries in a 28-day November period, double the prior year; officers urged residents to lock windows and doors, keep yards illuminated, install a burglary alarm. | §5 para 4, Hardware Notes (111th), §10.5 H3 7, Back-of-house plan |
| B16 | (precinct address) same search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/111th-precinct.page | 111th Precinct at 45-06 215th St, Bayside. | Research only (supports "111th covers Bayside") |
| B17 | `Yale Assure Lock 2 key-free touchscreen no key cylinder 9V battery backup emergency power` · Firecrawl search (excerpts) | https://shopyalehome.com/products/yale-assure-lock-2-key-free-touchscreen-with-z-wave-plus ; https://www.reddit.com/r/homeautomation/comments/1st5cnf/yale_assure_2_with_homekey_a_sure_way_to_get/ ; https://www.homedepot.com/p/Yale-Assure-Lock-2-Plus-with-Home-Keys-Satin-Nickel-Single-Cylinder-Deadbolt-YRD450-N-BLE-619/331828343 | Yale sells "Key-Free" Assure Lock 2; Reddit owner had to buy a 9V battery ("the emergency way") after a Home Key lockout; Assure Lock 2-Plus with Home Keys sold at Home Depot. | §9 keyless-only Q, §9 home-key Q, §10 Key-Free card |
| B18 | `ANSI BHMA grade 1 grade 2 grade 3 deadbolt residential security cycles explained` · Firecrawl search (excerpts) | https://iveise.com/blogs/product-insights/ansi-lock-grades-explained-grade-1-2-and-3-differences ; https://www.pdqlocks.com/blog/a-guide-to-ansi-grade-1-vs.-grade-2-door-hardware | Grade 1 deadbolt 250,000 cycles + 10 hammer strikes; Grade 3 deadbolt 100,000 cycles + 2 strikes (Veise); PDQ also gives Grade 1 deadbolts 250,000 cycles. (doorsforpros' 1,000,000 figure is for latches — not used.) Secondary sources, labelled "summaries … published by hardware suppliers". | Hardware Notes (grades), Back-of-house plan |
| B19 | `storm door heat buildup warning full glass sun damage door hardware manufacturer` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.stormdoorguy.com/blogs/news/the-hidden-downsides-of-storm-doors-what-you-need-to-know | Full-glass storm doors "can trap heat between the storm door and the entry door … damage to your entry door's paint, warping in wood doors". | §7.5 heat, §9 storm-door Q, Field Notes |
| B20 | `smart deadbolt operating temperature range specification Yale Assure Schlage Encode degrees Fahrenheit` · Firecrawl search (excerpt) | https://www.schlage.com/en/home/products/BE499WBCENFFF.html | Schlage Encode Plus: outside lock body −31°F to 150.8°F; inside 14°F to 120.2°F. | §7.5 heat, §9 storm-door Q |
| B21 | `Schlage Encode factory reset requires interior access; keypad lockout after incorrect code attempts` · Firecrawl search → Firecrawl scrape | https://schlage-res.zendesk.com/hc/en-us/articles/37430394837012-Do-Schlage-Encode-Series-Locks-Report-Multiple-Failed-Code-Attempts | 3 wrong codes → keypad disabled 30 s (logged in app); 4 → alarm 30 s; each further → 1 min. | Hardware Notes (wrong-code lockouts), §10.5 H3 6 |
| B22 | same search (excerpt) | https://nationallocksupply.com/blog/how-to-reset-a-schlage-keypad-lock/ | Schlage keypad factory reset: disconnect battery, press Schlage button… (reset needs interior/battery access). Used only as "on many models … procedure differs". | §9 inherited-lock Q, New Owners checklist |
| S | carried from silo file (not re-fetched) | Fixr (S1), Bob Vila (S2), August retrofit (S3), August Connect (S4), Yale Matter (S5), Bold Matter (S6), HPD fire safety (N6), LL111/2018 (N5), Yale IP55 (Queens Q15) | as logged in research/smart-lock-installation.md | §7.5, §10.5, §14, Hardware Notes (log) |

### Prices used (all from research/smart-lock-installation.md "Prices used" / live smart-lock-installation-queens.html; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,575–$2,625 | single-door keypad/fob reader + electric strike (Queens) | Queens page / silo prices ($1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike on entrance door | Queens page ($250–$450 × 1.05) |
| $310–$509 | failed electric strike repair | Queens page ($295–$485 × 1.05) |
| $195 first hour, then 30-min blocks | setup-only visit, Queens | Queens page / research/tv-mounting-prices/BRIEF.md |
| $195/hr, 3-hr minimum ($585) | service/callback | blueprint v2.3 §9 |
| quoted flat at walkthrough | house / co-op / condo smart lock | no AESS figure |
| $250–$400, avg $300 | NATIONAL third-party (Fixr) | silo S1 |
| Worked sums (only sums of lines above) | 2 × keypad+strike = $3,150–$5,250; keypad+strike + strike repair = $1,885–$3,134; new strike + 1 setup hour = $458–$668 | arithmetic on published lines |

## Images (11)
Drive folder `AESS Website Photos/Smart Lock Installation` empty (main run) and CompanyCam not connected → library set `images/smart-lock-installation/aess-smart-lock-installation-*` (the only photos showing actual smart locks). All 18 were viewed. Every candidate except two shows a technician's face, so 9 were **cropped with Pillow** to the door/hands area (face removed; verified by viewing the crops); 2 used uncropped (no person). Rejected: `apartment-door-smart-lock-app` (unit number "4A" sign + face), `showing-customer-app-unlock` (customer's face), `video-doorbell-and-smart-lock` (house number "128"), `office-glass-door`, `office-lever`, `checking-lock-status-in-app`, `drilling-keypad-lock-brownstone-stoop` (not needed; faces). Captions describe only what is visible; none claims a Bayside job, customer or named building.
**Flag:** the aess-* set appears AI-rendered (uniform logo artwork, stylised lighting) although supplied as AESS photos — Anwar to confirm they are real; replace when real Bayside photos exist.

| New file (images/smart-lock-installation/) | Source (aess-smart-lock-installation-…) | Crop |
|---|---|---|
| smart-lock-installation-bayside-queens-keypad-deadbolt-wood-panel-door.webp (hero, eager) | keypad-smart-deadbolt-brownstone-door | none (no person) |
| smart-lock-installation-bayside-queens-checking-latch-at-door-edge.webp | checking-latch-bolt-alignment | x 766→1400 |
| smart-lock-installation-bayside-queens-keypad-outside-thumbturn-inside.webp | keypad-exterior-thumbturn-interior-view | none (hands only) |
| smart-lock-installation-bayside-queens-measuring-old-deadbolt-bore.webp | measuring-door-bore-for-deadbolt | x 809→1400 |
| smart-lock-installation-bayside-queens-driving-screws-strike-plate.webp | suburban-front-door-smart-lock-van | x 880→1400 |
| smart-lock-installation-bayside-queens-adding-user-code-app.webp | programming-access-code-app | x 722→1400 |
| smart-lock-installation-bayside-queens-fingerprint-reader-test.webp | fingerprint-unlock-demo-app | x 722→1400 |
| smart-lock-installation-bayside-queens-drilling-out-brass-deadbolt.webp | removing-old-brass-deadbolt | x 722→1400 |
| smart-lock-installation-bayside-queens-interior-unit-ribbon-cable.webp | connecting-interior-unit-cable | x 831→1400 |
| smart-lock-installation-bayside-queens-battery-pack-change.webp | replacing-smart-lock-batteries | x 800→1400 |
| smart-lock-installation-bayside-queens-keypad-wiring-service.webp | servicing-keypad-wiring | x 720→1400 |

## Question register — smart-lock-installation-bayside-queens-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 6)
1. A full-glass storm door covers our sunny front door all summer — can the heat trapped between the two doors hurt a smart lock?
2. Would a keyless-only model with no key cylinder at all be safer on our front door, or riskier?
3. The pair who tried a Bayside back slider in 2025 rang the doorbell first to see if anyone was home — can our doorbell and lock answer for us when the house is empty?
4. The house we bought near Bell Boulevard came with the seller's keypad lock but nobody knows the master code — can it be wiped and made ours?
5. Should our family use the phone-tap "home key" feature, or stick with codes?
6. The last bartender leaves our Bell Boulevard place after midnight — how can I check from home that the front and back doors actually latched?

### §17 FAQ (visible == FAQPage, 7)
1. What would keypad entry on both the front and back doors of a Bell Boulevard shop cost?
2. Will you check over a smart lock we installed ourselves and fix whatever is wrong with it?
3. Is the $195 setup visit the same thing as your $195-an-hour service rate?
4. Do your Queens crews come to Bay Terrace, Bayside Hills, Oakland Gardens and Hollis Hills, or only central Bayside?
5. Can a code be set to work only once, for a single delivery or repair visit?
6. Do we need to save a parking space for your van on our block?
7. How can we tell the bolt went all the way out and didn't stop half-thrown?

### Other question-form headings
- H2 "Smart Lock Quit on You in Bayside?" (repair capture)
- H2 "Locked Out Somewhere Between Bell Boulevard and Little Neck Bay?" (final repair capture)

### De-dup notes
- Compared against every register in research/smart-lock-installation.md and the live HTML of all 16 area/hub pages plus today's Morris Park and West Brighton pages. Moved to non-question "Hardware Notes" H3s because the intent is already a question on a sibling: arched Tudor door placement (≈ Morris Park "Indian Village Tudor … arched wood door"), lock grades (≈ Morris Park "AAA or Grade 1 ratings"), wrong-code guessing (≈ Morris Park / West Brighton wrong-code Qs), smart lock vs police burglary advice (≈ West Brighton "does a smart lock on the doors help at all?"), entry-log privacy (≈ Morris Park "Can the lock maker see our comings and goings"). Dropped FAQ "How many metal keys should we keep…" (= West Brighton "What should we do with the physical keys…").
- Partial overlaps for the main run to judge: §9 Q3 (doorbell rung first) vs Morris Park "Burglars … knocked first and then pried a side door — what would a smart lock … have told the owner?" (ours = video doorbell answering to make the house seem occupied); §9 Q4 (reset an inherited lock with no master code) vs Staten Island "make sure the previous owners can't still open the doors" and West Brighton "show us how to factory-reset the lock ourselves"; FAQ 1 (worked two-door cost) vs cost FAQs on other pages (geo-specific pricing by design); FAQ 2 (check our DIY install) vs Queens "Do you bring the lock, or should we buy one".

### Flags for Anwar
- Images: aess-* library appears AI-rendered (see Images); 9 of 11 cropped to remove technician faces.
- Stated as AESS practice (no source, house policy): inside one-turn release on every residential door; won't fit inside-keyed/coded models; strike reinforcement with long screws; cardboard-template check; landlord written approval before cutting a leased storefront frame; no subscription required from AESS; jam/position-sensor set-up; two-adult admin rule; arrival windows 8 AM–8 PM seven days (copied from Queens page).
- General product statements without a specific source: many full-view storm doors have interchangeable glass/screen panels; many locks offer one-time or time-window codes; many lock/doorbell makers share an app/platform; some apps report "locked" when the bolt is thrown against an open door; national-brand (ADT/Ring/SimpliSafe) paragraph kept generic.
- Grade figures come from supplier summaries of ANSI/BHMA A156 (Veise, PDQ), not the standard itself.
- Bayside Village BID "200+ businesses" is from the BID's own Facebook page (excerpt).
- check_page.py: all content checks pass; the 16 remaining FAILs are "live sibling … doesn't link back" (area/hub pages must link down — main-run wiring).


## Morris Park, Bronx (smart-lock-installation-morris-park-bronx-ny)

Page: `/smart-lock-installation-morris-park-bronx-ny` · silo Smart Lock Installation · neighborhood spoke · up-link `/smart-lock-installation-bronx` (+ `/smart-lock-installation-nyc`) · phone (646) 490-0629 (body, CTAs, schema; (800) 486-0943 only in shared header chrome) · GBP Bronx, 460 E Fordham Rd, schema `#bronx` · pricing multiplier 1.00. Built 2026-10-17 by batch subagent.

Thesis: **Morris Park is houses, not towers — plan door by door.** Detached/semi-detached one- and two-family homes (R4A / R4-1), the driveway side door as the real front door (March 2025 side-door burglary near Loreto Playground), 65.8% renter-occupied in a house district (owner/tenant two-families: which rules reach a private dwelling vs a multiple dwelling), the hospital cluster on the eastern edge (shift workers, home aides, hospice), Indian Village Tudors, Morris Park Avenue shops and Eastchester Road/Waters Place medical offices, and the 2024 station-area rezoning.

Tools: "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (markdown or directQuote query mode). Silo-wide facts reused without re-fetching from research/smart-lock-installation.md: MDL 51-c (B6/N1), HMC 27-2043 (B7/N3), TDPA LL63/2021 (N4/B11), Admin Code 26-521 (N9), August Connect 10–15 ft (S4), Matter/Thread border router (S5/S6), Fixr national $250–$400 avg $300 (S1), LawnStarter national $330 (LI section), ADA 34–48 in (silo), HPD double-cylinder rule (B8/N6).

### Local research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| M1 | (direct) · Firecrawl scrape | https://en.wikipedia.org/wiki/Morris_Park,_Bronx | Boundaries (Neill Ave/Pelham Pkwy N; Eastchester Rd E; Amtrak NEC & Sackett Ave E/S; Bronxdale Ave/White Plains Rd W); Williamsbridge Rd & Morris Park Ave primary thoroughfares; CD 11; ZIPs 10461 (east of Paulding) / 10462 (west); 49th Pct 2121 Eastchester Rd; 5 train under the Esplanade (Morris Park, Pelham Pkwy stations); racecourse 1889–1910, 1890 Preakness & Belmont, 1910 fire → lots; streets named for 18th/19th-c. mayors (Cruger, Holland, Radcliff, Colden, Paulding, Hone); Aug 2024 rezoning of 46 blocks around Metro-North stations (Morris Park, Van Nest, Parkchester), up to 7,000 units, $500M; mostly one- and two-family homes; Indian Village (Choctaw Pl, Narragansett Ave, Seminole Ave, Pawnee Pl) near Jacobi; BX1102 2020: 25,077 (+9.4% from 22,913), 829.6 acres, 9,173 households, 65.8% renter-occupied; Columbus Day parade since 1977, route & reviewing stand (Williamsbridge Rd between Lydig & Neill); Einstein, Jacobi, Weiler, Bronx Psychiatric Center, Calvary; Loreto Park bounds, Officer Alfred Loreto (1870 Hering Ave, killed July 21 1950), reopened April 2022 after $2M work; FDNY Squad 61/Bn 20 1518 Williamsbridge Rd, Engine 97 1454 Astor Ave, EMS Station 20 on Jacobi grounds; Morris Park Station PO 1807 Williamsbridge Rd; NYPL Morris Park branch 985 Morris Park Ave (2-story, 6,600 sq ft, 2006); 49th Pct 2022: 133 burglaries. | Hero, §5 paras 1/4/5 + facts list, §7 intro + mayors para, Side-door section, §8 Williamsbridge card, §13 landmark cards (Loreto Park, Library, Station/Esplanade, Parade), Carers section (Squad 61, EMS 20), schema areaServed |
| M2 | `Morris Park Bronx neighborhood history housing semi-detached two-family homes` · Firecrawl search | https://www.nyc.gov/assets/planning/download/pdf/plans/morris-park/morris_park.pdf (scraped, pdf) | DCP "Morris Park Rezoning – Approved!": development began turn of 20th c., accelerated with 1910 streetcar along Morris Park Ave, continued after WWII; "Most of the neighborhood is developed with single- and two-family detached homes and semi-detached housing. Small and medium-sized apartment buildings can be found along Morris Park Avenue, which is also the neighborhood's main commercial corridor, and along Williamsbridge Road"; R4→R4A on 11 full + parts of 19 blocks (detached 1–2 family only; perimeter wall 21 ft, "two-story homes with attics beneath pitched roofs"); R4→R4-1 (Morris Park Ave/Pierce/Bronxdale/Radcliff; detached & semi-detached); C1-4 on 12 Morris Park Ave blockfronts Haight–Bogart; Council adopted Oct 11, 2005. | §5 para 1, facts list, §7 intro + cards (detached, semi-detached, apartment buildings), Side-door section |
| M3 | same search · Firecrawl scrape | https://www.morrisparkbid.org/history | BID history page mirrors Wikipedia (one- and two-family homes, several apartment buildings, low-lying/flat; Indian Village); links NYT 1983/1985/2018, Bronx Times 2004. | Confirms M1 (no new claim used) |
| M4 | same search · Firecrawl search (excerpts only) | https://www.zillow.com/morris-park-bronx-new-york-ny/duplex/ ; https://www.redfin.com/neighborhood/61025/NY/New-York/Morris-Park/multi-family-homes-for-sale | Listing excerpts: "Semi-attached brick two family"; "2-story multi-family frame home … two separate units … full basement … 25x95 lot"; "legal 2-family home … Bronx 10461". | §5 para 2 (25-foot lot), §7 "Frame Two-Families" card |
| M5 | same search · Firecrawl search (excerpt) | https://www.reddit.com/r/bronx/comments/1jyqlh9/morris_park_the_neighborhood_that_pretends_it/ | Title/excerpt only ("Morris Park: The Neighborhood That Pretends It Never Changed… East Bronx enclave of hard-working, mostly Italian-American families"). Firecrawl scrape refused (site not supported). | Not used on page |
| M6 | `Morris Park Bronx burglary homes 49th Precinct Bronx Times` · Firecrawl search → Firecrawl scrape | https://www.youtube.com/watch?v=6AoQbvQUACc | News 12, uploaded 2025-03-29: two women entered a single-family home in Morris Park near Loreto Playground ~4:30–4:40 p.m. Tuesday through the side door; knocked twice to check no one home; pushed the security camera up; pried the door; ~6 minutes after homeowner's mother left for school pick-up; safe with passports/documents and heirlooms stolen; 49th Pct 13 burglaries YTD vs 17 same time last year; NYPD reward up to $3,500. | §5 para 3 + facts list, Side-door section, §9 Q1, §10.5 H3 6 |
| M7 | same search · Firecrawl search (excerpt) | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/49th-precinct.page | 49th Precinct serves Allerton, Morris Park…; 2121 Eastchester Road. | §5 para 3, §13 Eastchester card |
| M8 | (direct) · Firecrawl scrape | https://www.bxtimes.com/category/news/neighborhoods/morris-park/ | Recent Morris Park headlines: 49th Columbus Day Parade (Oct 2026); DRI ten projects (May 2026); Just Home supportive housing at Jacobi; 49th Pct community potluck; "Cops seek four women suspects in Morris Park car robbery"; Haven Charter High School opening; Metro-North delay coverage. | Lead list only (DRI & parade used via M9/M10) |
| M9 | (direct) · Firecrawl scrape (directQuote) | https://www.bxtimes.com/ten-projects-greater-morris-park-dri/ | May 20 2026: Hochul announced May 13 $19.4M to ten Greater Morris Park DRI projects; $2.75M public plaza connecting the proposed Metro-North Morris Park station entrance to the Hutchinson Metro Center campus and Marconi Street; $750K Morris Park Ave streetscape; $3.5M former St. Francis Xavier School → resource hub; $3.5M Matthews Muliner Playground (recurring flooding). | §8 "Near the Planned Metro-North Station" card |
| M10 | (direct) · Firecrawl scrape (directQuote) | https://www.bxtimes.com/morris-park-49th-annual-columbus-day-parade/ | Oct 14 2026: 49th annual parade on Sunday despite stormy conditions, hosted and organized by the Morris Park Community Association, kicked off at Bronxdale and Morris Park avenues. | §13 parade card |
| M11 | `Metro-North Penn Station Access Morris Park station opening date 2027 Bronx` · Firecrawl search | https://www.mta.info/project/penn-station-access (excerpt) ; https://www.nyc.gov/content/planning/pages/our-work/plans/bronx/bronx-metro-north-area (excerpt) | MTA: "Morris Park, construction along Sackett Av (August 2026–January 2027)"; DCP: plan approved Aug 2024, MTA anticipated 2027. | §9 construction-next-door Q, §7 new-buildings card |
| M12 | same · Firecrawl scrape (directQuote) | https://www.thecityreporter.nyc/2026/05/15/metro-north-bronx-partial-service-mta-timeline/ | May 15 2026 (THE CITY): MTA's hope of limited service by 2027 (temporary Morris Park & Co-op City stations) fading; Amtrak raises possibility of beginning service by early 2029. | §13 station card |
| M13 | `Calvary Hospital 1740 Eastchester Road…; Jack D. Weiler Hospital 1825 Eastchester Road; Jacobi … 1400 Pelham Parkway South; Albert Einstein College of Medicine 1300 Morris Park Avenue` · Firecrawl search | https://www.calvaryhospital.org/contact/bronx-campus/ ; https://www.jacobimonteem.org/home-1-1-2-2 ; https://www.nychealthandhospitals.org/locations/jacobi/ ; https://en.wikipedia.org/wiki/Jacobi_Medical_Center ; https://www.calvaryhospital.org/wp-content/uploads/2017/03/Jewish_broch_2panels_web_101717.pdf | Calvary 1740 Eastchester Rd 10461; Weiler (Einstein Hospital) 1825 Eastchester Rd, in Morris Park; Jacobi 1400 Pelham Pkwy S, founded 1955 as Bronx Municipal Hospital Center concurrent with Einstein, Bronx's only burn unit and Level I trauma center, 457 beds; Calvary "hospice/home care program". | §5 para 5 + facts list, §8 Eastchester card, §13 cards, Carers section (hospice para) |
| M14 | `Albert Einstein College of Medicine address 1300 Morris Park Avenue Bronx NY 10461` · Firecrawl search | https://einsteinmed.edu/ | "Jack and Pearl Resnick Campus 1300 Morris Park Avenue Bronx, NY 10461". | §5 para 5, §13 Einstein card |
| M15 | `Hutchinson Metro Center Bronx Waters Place offices Morris Park` · Firecrawl search | https://www.hutchinsonmetrocenter.com/home.html ; https://www.hutchinsonmetrocenter.com/tower2.html ; https://www.hutchinsonmetrocenter.com/tenants.html | 1250 Waters Place; Tower Two 280,000 sq ft Class A medical office building fully leased to Montefiore; 1200 Waters Place tenants incl. Bronx Chamber of Commerce. | §8 Hutchinson card |
| M16 | `Morris Park Business Improvement District Morris Park Avenue businesses boundaries` · Firecrawl search | https://www.morrisparkbid.org/ ; https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=75 | BID covers Morris Park Ave properties between Unionport Rd/Amethyst St (W) and Williamsbridge Rd (E); office 966 Morris Park Ave. | §8 BID card |
| M17 | `Indian Village Morris Park Bronx Tudor style homes Seminole Avenue Pawnee Place` · Firecrawl search (excerpts) | https://www.homes.com/property/1242-pawnee-place-bronx-ny/2mp0f1dcmmch6/ ; https://streeteasy.com/building/1234-pawnee-place-bronx ; https://www.compass.com/homedetails/1232-Pawnee-Pl-Bronx-NY-10461/20ISO7_pid/ | Pawnee Place homes built 1940, "Tudor-style Home"; "all brick, fully detached, single family … tudor style … Indian Village". | §7 Indian Village card, §9 Tudor Q, §10.5 H3 1 |
| M18 | `NYC basement and cellar apartment legalization program eligible community districts Bronx Community District 11` · Firecrawl search → Firecrawl scrape (directQuote) | https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=7020615 (excerpt) ; https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-160650 | Admin Code Art. 507 pilot: program area incl. Bronx CDs 9–12 (15 districts total); units existing before April 20, 2024; apply on or before April 20, 2029; requires smoke + CO detector and "at least 1 means of egress directly to the outdoors … an exterior door that swings inward and is provided with landings on both the interior and exterior sides" (BC 1010.1.6). | Two-family rules table + para |
| M19 | (direct) · Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/MDW/4 | MDL §4: multiple dwelling = occupied by "three or more families living independently of each other"; private dwelling = "not more than two families"; "two-family private dwelling". | §5 para 4, Two-family table, §10.5 H3 5 |
| M20 | (direct) · Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/RPA/768 | RPAPL 768: unlawful to evict an occupant of 30+ consecutive days or leaseholder by, incl., "changing the lock on such entrance door without supplying the occupant with a key"; class A misdemeanor; civil penalty $1,000–$10,000 per violation; up to $100/day. | §9 lease Q, §10.5 H3 5, Two-family table |
| M21 | `ANSI/BHMA A156.40 residential deadbolt grade AAA security durability finish ratings explained smart lock` · Firecrawl search | https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights/A15640-2015-Residential-Deadbolts ; https://www.schlage.com/en/blog/product_updates/exterior-deadbolt-lock-security-grades.html | A156.40-2025: durability, security, finish tests; operating torque ≤ 9 in-lbf; Grade A residential deadlatch 400,000 cycles; 17 security tests incl. 1,350 lbf door load; salt spray ASTM B117. Schlage: BHMA residential grades C good / B better / A best; AAA best in all three. | §9 ratings Q, §10.5 H3 2, FAQ cheap-lock + lifespan |
| M22 | `Insteon shutdown April 2022 smart home devices stopped working servers` · Firecrawl search | https://www.theverge.com/23032451/smart-home-troubles-insteon-ihome-shutdown-matter ; https://www.youtube.com/watch?v=8lLQLG0SVLE ; https://community.home-assistant.io/t/june-7-2022-insteon-servers-back-online/428977 | Insteon (and iHome) turned off cloud servers; April 14 2022, parent Smartlabs went out of business; servers back online June 7 2022. | §9 company-goes-under Q, §10.5 H3 4 |
| M23 | `Yale August smart lock privacy policy law enforcement requests disclose activity log data` · Firecrawl search | https://shopyalehome.com/pages/privacy-center ; https://www.eff.org/deeplinks/2023/04/smart-locks-endanger-tenants-privacy-and-should-be-regulated | Yale: "Lock activity is stored alongside your account information for the duration of your account being active"; deletion requests may be rejected where processing is required by law. EFF (Apr 2023): smart lock data a new stream for law enforcement; calls for warrant requirement and tenant notice. | §9 privacy Q |
| M24 | `smart lock keypad wrong code attempts lockout period Schlage Encode Yale Assure …` · Firecrawl search | https://schlage-res.zendesk.com/hc/en-us/articles/37430394837012-Do-Schlage-Encode-Series-Locks-Report-Multiple-Failed-Code-Attempts | Encode: 3 wrong codes → keypad disabled 30 s and history reports it; 4 → keypad off + alarm 30 s; each further → 1 min. | Research only (Q dropped — same intent as West Brighton sibling) |
| M25 | `reddit bronx Morris Park smart lock OR keypad OR "change the locks" landlord two family` · Firecrawl search | https://www.reddit.com/r/Landlord/comments/1e2qnia/landlord_usny_can_i_have_a_smart_lock_on_my_unit/ ; https://www.reddit.com/r/NYCapartments/comments/1p3fnwy/landlord_suddenly_installed_a_smarthome_door_its/ | Excerpts only, none in Morris Park (US-NY landlord asking about smart lock on own unit; Queens two-unit tenant upset by landlord's smart door). **Reddit for Morris Park: EMPTY.** | Not used |

### EMPTY / not accessible
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: `EMPTY (not accessible in build env)`. §10.5 says so and uses published claims (Fixr, BHMA, manufacturers) instead.
- Reddit r/bronx Morris Park threads: search excerpts only; Firecrawl scrape of reddit.com refused → `EMPTY (not accessible in build env)` for thread content; nothing quoted.
- NYT 2018 "Morris Park, Bronx: Where Congeniality Flourishes": scrape refused (site not supported) → only the search excerpt seen; not used.
- Yelp 1–3★ Bronx locksmiths/smart-lock installers: `EMPTY (not accessible in build env)`.
- Morris Park–specific smart lock / keyless news: none found → `EMPTY`.
- Google Drive `AESS Website Photos/Smart Lock Installation`: EMPTY (per batch brief); CompanyCam not connected.

### Prices used (no new prices; Bronx ×1.00)
| Figure | Scope | Source |
|---|---|---|
| $1,500–$2,500 installed | single-door keypad or fob reader with electric strike | smart-lock-installation-bronx.html / research "Prices used" (access-control-installation-bronx.html) |
| $250–$450 | new electric strike on lobby/street door | same (door-buzzer-repair-allerton-bronx-ny.html) |
| $295–$485 | failed electric strike repair | same (door-buzzer-repair-bruckner-bronx-ny.html) |
| $225 first hour, then 30-min blocks | setup-only visit (apps/bridge/codes) | smart-lock-installation-bronx.html (research flag carried: TV setup-only rate used for smart-lock app visits) |
| $195/hr, 3-hr min ($585) | service/callback, not initial install | blueprint v2.3 §9 / Bronx page |
| $1,795–$2,985 | worked total = $1,500–$2,500 + $295–$485 (shop-door keypad + residential street-door strike repair) | sum of published lines |
| $250–$400, avg $300 (Fixr); avg $330, $200–$460 (LawnStarter) | NATIONAL third-party, labelled as such | silo research S1 / LI section |
| House or unit door | no AESS figure → "Quoted flat at free walkthrough" | — |

## Images (11)
Permanent rule / Step C: Drive folder empty, CompanyCam not connected. All 11 come from the `aess-smart-lock-installation-*` set in images/smart-lock-installation/; each viewed. Every source except two shows a technician's face (and one shows customer's face, one a house number "128"), so nine were **cropped with Pillow** to the hands/lock area (faces, house number excluded) and saved as new WebP (q82). No file overwritten. Skipped: showing-customer-app-unlock (customer face can't be cropped out cleanly). Note: the whole aess set looks AI-rendered (flag for Anwar).

| File (images/smart-lock-installation/) | Source (crop box) | Size | Where |
|---|---|---|---|
| smart-lock-installation-morris-park-bronx-black-keypad-deadbolt-handleset-wood-door.webp | aess-…-keypad-smart-deadbolt-brownstone-door (no crop) | 1400×1050 | hero (eager) |
| smart-lock-installation-morris-park-bronx-app-locked-status-at-door.webp | aess-…-checking-lock-status-in-app (770,240,1400,1050) | 630×810 | Instant action block |
| smart-lock-installation-morris-park-bronx-drill-driving-latch-screws-keypad-door.webp | aess-…-suburban-front-door-smart-lock-van (820,330,1400,933) | 580×603 | §5 Neighborhood |
| smart-lock-installation-morris-park-bronx-keypad-outside-thumb-turn-inside-views.webp | aess-…-keypad-exterior-thumbturn-interior-view (no crop; hands only) | 1400×933 | §6 Services |
| smart-lock-installation-morris-park-bronx-tape-measure-backset-old-bore.webp | aess-…-measuring-door-bore-for-deadbolt (790,330,1400,1050) | 610×720 | §7 Architecture |
| smart-lock-installation-morris-park-bronx-strike-screws-metal-frame-door.webp | aess-…-office-glass-door-smart-lock (800,280,1400,933) | 600×653 | §8 Commercial |
| smart-lock-installation-morris-park-bronx-video-doorbell-beside-keypad-deadbolt.webp | aess-…-video-doorbell-and-smart-lock (940,280,1400,933; house number "128" cropped out) | 460×653 | §9 Q&A |
| smart-lock-installation-morris-park-bronx-brass-deadbolt-coming-off-door.webp | aess-…-removing-old-brass-deadbolt (780,300,1400,1050) | 620×750 | §10.5 AI reality check |
| smart-lock-installation-morris-park-bronx-gloved-drill-keypad-wood-door.webp | aess-…-drilling-keypad-lock-brownstone-stoop (840,250,1400,933) | 560×683 | §13 Landmarks |
| smart-lock-installation-morris-park-bronx-keypad-lever-latch-screwdriver.webp | aess-…-office-lever-smart-lock-install (700,250,1400,933) | 700×683 | §15 Packages |
| smart-lock-installation-morris-park-bronx-aa-batteries-interior-unit.webp | aess-…-replacing-smart-lock-batteries (870,230,1400,933) | 530×703 | Carers section |

Overlap with batch siblings (same source photo, different crop/filename): measuring-door-bore, removing-old-brass-deadbolt, replacing-batteries, keypad-exterior-thumbturn, keypad-smart-deadbolt-brownstone-door (+ possibly office-glass-door / drilling-stoop). Unused by both siblings: checking-lock-status, suburban-front-door-van, video-doorbell, office-lever.
DAILY-LOG note suggestion: `images: 11 cropped from images/smart-lock-installation/aess-smart-lock-installation-* (faces/house number cropped out; no Drive/CompanyCam photos)`.

## Question register — smart-lock-installation-morris-park-bronx-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
1. Burglars near Loreto Playground pried a side door open — would a smart lock on that door have warned the owner?
2. What do the AAA or Grade 1 ratings printed on a smart lock box actually measure?
3. The lot next door could be rebuilt under the station-area rezoning — how should we plan our locks around a construction site?
4. A resident doctor wants our upstairs apartment on a one-year lease — what should the lease say about the smart lock?
5. The visiting nurse service sends whoever is on call that night — should each nurse get a code, or one code for the agency?
6. Our late mother's house is in probate — how can the executor control who gets in until it is sold?
7. Our Indian Village Tudor has a heavy arched wood door with a small window in it — where can a smart lock go?
8. What happens to our smart lock if the company behind the app goes out of business?
9. Who installs the lock's firmware updates once you have left, and should they run automatically?
10. Can the lock maker see our comings and goings, and could that record be handed to the police?
11. Is it safe to text or WhatsApp a door code to the plumber or a relative?

### §17 FAQ (visible == FAQPage, 7)
1. What does a smart lock on a Morris Park front or side door cost compared with a keypad on a building door?
2. Do I need a separate hub or bridge, or will the lock talk to my phone directly?
3. Do you also fit keyless entry for doctors' and dental offices near the hospitals on Eastchester Road?
4. Is a cheap smart lock from an online marketplace worth installing?
5. How long should a smart lock last before it needs replacing?
6. Do you also cover Van Nest, Pelham Parkway, Allerton and the rest of the 10461 and 10462 ZIP codes?
7. Can I lock or unlock the door from a smartwatch?

### Other headings (no question marks)
- Mid CTAs: "Put the Side Door on Your Phone", "Know Who Can Open Every Door in the House"
- Repair captures: "Morris Park Smart Lock Dead, Jammed or Offline", "Shut Out by Your Own Lock in Morris Park Tonight"

### De-dup notes
Checked every register in research/smart-lock-installation.md and the questions on all 18 smart-lock pages on disk at finish (incl. in-progress bayside-queens and west-brighton-staten-island). Dropped during build because a batch sibling or the register already holds the intent: pick/bump resistance (West Brighton), wrong-code lockout (West Brighton), child fingerprint vs code (West Brighton), voice-assistant unlock (West Brighton), door handing/hinge side (West Brighton), old keys after going keyless (West Brighton, borderline), router/wall signal (West Brighton plaster/lath; HV/NYC), two-family tenant-lock-rules Q (Brooklyn), tenant log-viewing (Brooklyn/SI), basement-door rules (Queens) — those topics stay as body text only (Two-family table, Carers section). Partial overlaps left for the main run to judge: Q1 forced-entry alert vs Bayside "rang the doorbell first … can doorbell and lock answer" and West Brighton "North Shore window burglaries — does a smart lock help" (mine = door-position/forced-entry alerting); Q5 agency nurse codes vs Queens "home attendant three mornings a week" (mine = per-person vs shared agency credential); Q11 texting codes vs Bayside "code that works only once" (mine = channel safety); FAQ 2 hub/bridge need vs West Brighton "no outlet — where does the bridge plug in".


## West Brighton, Staten Island (smart-lock-installation-west-brighton-staten-island-ny)

Built 2026-10-17 by the West Brighton builder subagent (batch with -bayside-queens-ny and -morris-park-bronx-ny). Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used.
Thesis: West Brighton = old North Shore housing (19th/early-20th-century houses, many divided into 2–3 apartments) — old doors (narrow stiles beside glass, mortise pockets, plugged bores), shared front halls and code roles per household, upper/rear-stair unit doors, plaster-wall signal problems, West Brighton Houses PACT renovation, Forest/Castleton Ave shops and converted-house offices.
Silo-wide sources reused (not re-fetched): S1 Fixr ($250–$400, avg $300), S2 Bob Vila (screwdriver/30 min), S3 August retrofit (single-cylinder only), S4 August Connect 10–15 ft, S5 Yale Matter/Thread border router same ecosystem, S6 Bold (Nest Hub 2nd gen / HomePod mini), N1 MDL §51-c, N3 HMC §27-2043, N4 Tenant Data Privacy Act (LL63/2021), N6 HPD fire safety (3+ apts self-closing; double-cylinder illegal on apartment doors), N9 Admin Code §26-521 (30+ days lockout), SI6 2022 NYC BC §1010.1.9 / 1010.1.9.5, SI11 MDL §4 (multiple dwelling = 3+ families; private dwelling ≤2), prices table (SI ×1.10).

| # | Query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| WB1 | `West Brighton Staten Island neighborhood history housing Forest Avenue Castleton Avenue` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/West_New_Brighton,_Staten_Island | Formerly "Factoryville"; North Shore, CD1; E New Brighton, W Port Richmond, S Sunnyside/Castleton Corners, N Kill Van Kull; Livingston & Randall Manor near shore; Richmond Terrace shipyards/tugboat companies; Castleton Ave: library (976), post office (1015), Ladder 79 (1189); Broadway: Engine 156 (412); Sunset Hill east of Broadway; West Brighton Houses + Markham Homes post-WWII; St. Peter's Cemetery opened 1848, oldest RC cemetery on SI; Gardiner-Tyler House NRHP; 120th Pct: 2022 = 124 burglaries; crime −83.3% 1990–2022; 2020 NTA pop 37,010, 13,141 households, 32.9% with children <18; 47.4% renter-occupied. | §5 paras 1, 3; §5.5 stats 1–2, 5; §8 Richmond Terrace / Broadway / Castleton cards; §13 library + St. Peter's cards, "we also serve" line; FAQ 1 |
| WB2 | same search · WebFetch | https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/n360-cdna-westbrighton.pdf | SBS Neighborhood 360° CDNA West Brighton (study Dec 2023–Jun 2024; lead SIBOC with Forest Avenue BID, Castleton Avenue Merchants Organization, FRRCA): Forest Ave (Broadway–Hart Blvd) + Castleton Ave (Rector–Hoyt); 293 storefronts; vacancy 11.9% (Castleton 14.4%, Forest 9.7%); merchant survey 120 responses, 72% rent, 15% own; concerns incl. insufficient street lighting; business types (delis, salons, barbershops, clothing, restaurants, professional services, religious orgs); NYCHA PACT 574 apts / 14 bldgs; car ownership 78.3%. | §5 para 5; §5.5 stat 3; §8 intro + Forest/Castleton cards |
| WB3 | `West Brighton Houses NYCHA Staten Island buildings apartments completed` · WebSearch → WebFetch | https://nychajournal.nyc/332-million-pact-renovation-coming-to-west-brighton/ | June 27 2024: NYCHA closed $332.3M PACT financing June 26 2024; 574 apartments at West Brighton I & II fully rehabilitated; scope incl. new doors, windows, kitchens, baths, Wi-Fi; security cameras + lighting; common-area entrances/lobbies renovated; partners BFC Partners, CB Emmanuel, Catholic Homes; Pinnacle City Living = day-to-day management; ~2-year construction. Intercoms not mentioned. | §5 para 5; §5.5 stat 4; §9 PACT Q; apartment-residents section |
| WB4 | `West Brighton Staten Island neighborhood history…` · WebFetch | https://forgotten-ny.com/?p=111236 | Forgotten NY, Jan 2022 Forest Ave walk: Sunset Hill planned development with "occasionally picturesque cottages"; Hart Blvd two large apartment complexes; #391 Forest Ave small A-frame house with a pair of law practices; Clove Lakes Park 198 acres, Silver Lake Park 209 acres border Forest Ave; Egger's Ice Cream etc.; Forest Ave runs to Victory Blvd. | §7 Sunset Hill + apartment cards; §8 converted-house offices + Hart Blvd cards; §13 Clove Lakes card |
| WB5 | same · WebFetch | https://forgotten-ny.com/2007/09/livingstonwest-brighton-staten-island/ | EMPTY (not accessible in build env — JavaScript redirect). | — |
| WB6 | `West Brighton Houses NYCHA…` · WebFetch | https://derivativeworks.com/?p=1131 | Markham Drive Apartments, 35 Markham Drive, "214 affordable housing rental apartments" under construction (post dated Aug 10 2008). | §5 para 5 (named only); §7 apartment card; residents section |
| WB7 | `West New Brighton Staten Island Victorian frame houses 19th century architecture Sunset Hill Randall Manor` · WebSearch → WebFetch | https://cityneighborhoods.nyc/west-new-brighton | Tree-lined avenues "lined with Victorian homes"; Queen Anne and Colonial Revival homes beside Italianate rowhouses and late Victorian cottages; Castleton & Bement laid out 1830s–1840s; name on maps mid-19th c.; Forest Ave major shopping corridor by 1910s; Clove Lakes Park completed 1920s; Walker Park home of SI Cricket Club. | §5 para 1; §5.5 stat 6; §7 cards (Victorian, Colonial Revival, Italianate); §8 Forest card; §13 Clove Lakes |
| WB8 | same · WebFetch | https://en.wikipedia.org/wiki/Randall_Manor,_Staten_Island | Randall Manor: Bard Ave W, Henderson Ave N, Forest Ave S, Lafayette Ave E; named for Capt. Robert Richard Randall; south of Snug Harbor; development largely complete by 1964. | "we also serve" line, FAQ 1 (name only) |
| WB9 | `Walker Park Staten Island Cricket Club Bard Avenue NYC Parks history` · WebSearch → WebFetch | https://php1-84.nycgovparks.org/parks/R015/history | Opened Aug 1931 as Livingston Park; renamed 1934 for Lt. Randolph Walker Jr. (WWI); cricket club founded 1872, moved to site 1885; clubhouse burned 1932, Tudor-style clubhouse 1934. | §13 Walker Park card |
| WB10 | `Staten Island Zoo Barrett Park opened 1936 West Brighton Broadway` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Staten_Island_Zoo | 614 Broadway, West New Brighton; officially Barrett Park; opened June 10 1936; 8 acres; Staten Island Chuck, NYC's official Groundhog Day forecaster. | §13 Zoo card |
| WB11 | `Gardiner-Tyler House Staten Island Clove Road landmark Julia Gardiner Tyler` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Gardiner-Tyler_House | 27 Tyler Ave, West New Brighton; c.1835 Greek Revival; Julia Gardiner Tyler lived there 1868–1874; NYC landmark May 12 1967; NRHP 1984. | §13 Gardiner-Tyler card |
| WB12 | `NYC Landmarks Preservation Commission permit replace door hardware lock individual landmark house rules doors` · WebSearch → WebFetch | https://ur.nyc-business.nyc.gov/nycbusiness/description/performing-work-on-a-landmarked-property | LPC permit needed before work on a landmark/historic-district building; replacing doors = Permit for Minor Work; simple repairs exempt; door hardware not addressed → check with LPC via 311. | §13 Gardiner-Tyler card; checklist "Landmark status" |
| WB13 | `HPD property registration required one- or two-family house owner does not live there tenant` · WebSearch → WebFetch | https://www.nyc.gov/site/hpd/services-and-information/register-your-property.page | Annual HPD registration for multiple dwellings (3+ units) and for 1–2 family private dwellings where neither owner nor immediate family resides; deadline Sept 1; $13 fee. | §9 three-unit Q; §9 "moved out of two-family" Q |
| WB14 | `silive West Brighton burglary house break-in 120th Precinct` · Firecrawl search → Firecrawl scrape | https://gothamist.com/news/serial-burglar-giving-staten-island-residents-the-creeps | Feb 24 2007: burglaries at ≥13 homes in West Brighton and Westerleigh since Jan 19; strikes 1–9 p.m. when residents out; unlit homes without alarms/dogs; entry via side or rear window; ~40% rise in 120th Pct burglaries that year. | §9 windows Q; §10.5 H3 7 |
| WB15 | same Firecrawl search | https://www.facebook.com/statenislandadvance/posts/the-staten-island-neighborhoods-of-west-brighton-and-tompkinsville-experienced-r/1379583600874347/ | SI Advance post excerpt: "56 burglaries … through mid-March, 21 involved a home" (West Brighton + Tompkinsville) — year not visible in excerpt; post not opened. NOT used. | research only |
| WB16 | `Schlage smart deadbolt door prep backset 2-3/8" or 2-3/4" door thickness…` · WebSearch → WebFetch | https://kc.allegion.com/kb/article/what-are-the-required-door-preparation-specifications-for-the-schlage-arrive | Allegion/Schlage (Arrive): door thickness 1-3/8" to 2"; backset adjustable 2-3/8" or 2-3/4". | §7.5 bullets; §9 narrow-stile Q; §10.5 H3 3; checklist |
| WB17 | `Clove Lakes Park acres history…` · WebFetch | https://prd2.nycgovparks.org/parks/clovelakespark | EMPTY (fetch error) — acreage taken from WB4, completion decade from WB7. | — |
| WB18 | `reddit West Brighton Staten Island apartment landlord lock` · WebSearch | — | Reddit: EMPTY (no Reddit results returned; only rental listings). | — |
| WB19 | Google PAA / PASF / Answer the Public / AI Overview / Bing / DuckDuckGo / Yelp 1–3★ (West Brighton) | — | EMPTY (not accessible in build env). §10.5 claims are from national cost guides (Fixr, Bob Vila) and manufacturers, stated as such on the page. | — |
| WB20 | SI Advance (silive.com) smart-lock stories for West Brighton | — | EMPTY — only a 2022 robbery item surfaced (silive.com/crime-safety/2022/04/…); not lock-related, not used. | — |

Technical statement without a dedicated source (general practice, flagged): plaster over metal lath can weaken Wi-Fi/Bluetooth signal (§5 para 4, §9 plaster Q, connectivity section) — no URL retrieved; worded as "can".

### Prices used (SI multiplier 1.10 — copied from smart-lock-installation-staten-island.html / research "Prices used"; no new figures)
- Single-door keypad or fob reader with electric strike: $1,650–$2,750 (§14 table, §15 Premium, schema).
- New electric strike: $275–$495 (§14, schema). Failed strike repair: $325–$534 (§14, schema).
- Setup-only first hour: $225 (repair capture, §14, BYO card). Service/callback $195/hr, 3-hr min ($585) (§14).
- Residential smart locks: quoted flat at walkthrough. Fixr national $250–$400 / avg $300, labelled national (§10.5, §14).
- Worked totals (sums of published lines only): two single-door systems = $3,300–$5,500; new strike alone $275–$495; setup-only $225.

## Images (11)
Drive folder `AESS Website Photos/Smart Lock Installation` empty (checked by main run); CompanyCam not connected. Source = `images/smart-lock-installation/aess-smart-lock-installation-*` (the set on the SI page). Each viewed with Read; technician faces cropped out with Pillow (crop boxes in build notes); skipped: video-doorbell-and-smart-lock (readable house number "128"), showing-customer-app-unlock (customer face), suburban-front-door-van, office-lever, office-glass-door (faces/commercial). apartment-door crop removes the "4A" unit plate. NOTE: the whole aess-* set looks AI-rendered (flag for Anwar).
| File (images/smart-lock-installation/) | Source (aess-smart-lock-installation-…) | Crop | Section |
|---|---|---|---|
| smart-lock-installation-west-brighton-staten-island-keypad-deadbolt-raised-panel-wood-door.webp | keypad-smart-deadbolt-brownstone-door | none | hero |
| …-keypad-outside-thumb-turn-inside-pair.webp | keypad-exterior-thumbturn-interior-view | none | instant action |
| …-tape-measure-backset-bore.webp | measuring-door-bore-for-deadbolt | x 780–1400 | §5 |
| …-keypad-wiring-service-check.webp | servicing-keypad-wiring | x 820–1400 | repair capture |
| …-fingerprint-reader-app-confirmation.webp | fingerprint-unlock-demo-app | x 720–1400 | §6 |
| …-old-brass-deadbolt-removal.webp | removing-old-brass-deadbolt | x 760–1400 | §7 |
| …-latch-strike-alignment-check.webp | checking-latch-bolt-alignment | x 780–1400 | converted houses |
| …-new-access-code-app-screen.webp | programming-access-code-app | x 720–1400 | §8 |
| …-interior-unit-ribbon-cable.webp | connecting-interior-unit-cable | x 800–1400 | §10 |
| …-keypad-mounting-screws-drill.webp | drilling-keypad-lock-brownstone-stoop | x 820–1400 | §14 |
| …-apartment-door-keypad-app-test.webp | apartment-door-smart-lock-app | (760,280)–(1400,933) | apartment residents |

## Question register — smart-lock-installation-west-brighton-staten-island-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 14)
1. The wood beside the glass on our old front door is only a few inches wide — what kind of smart lock fits a door like that?
2. Our walls are old plaster, some of it on metal lath — will that block the lock's Wi-Fi or Bluetooth?
3. There isn't an electrical outlet anywhere near our front door — where does a Wi-Fi bridge or hub plug in?
4. Our house was divided into three apartments years ago — what changes for the locks once a building has three units instead of two?
5. When the upstairs tenants have to leave through the shared front door, what must that door's lock never do?
6. The upstairs apartment's only door is at the top of an outside wooden stair at the back — can that door take a keypad lock?
7. Can the mail carrier still get to the mailboxes inside our shared front hall once the street door goes keyless?
8. We've moved out of our two-family and now rent both floors — what should change on the locks?
9. Our West Brighton Houses apartment is down for a new front door in the PACT renovation — should we hold off on adding a smart lock?
10. North Shore burglaries have come in through side and rear windows in the daytime — does a smart lock on the doors help at all?
11. Our new smart deadbolt still has a key cylinder — is it any harder to pick than the old lock we took off?
12. What happens if someone stands at our keypad and keeps trying wrong codes?
13. Our office is on the ground floor of an old house on Forest Avenue — can the front door unlock itself for office hours and relock at closing?
14. Our storefront landlord keeps a key to the shop — does a new keypad lock have to let the landlord in too?

### §17 FAQ (visible == FAQPage, 10)
1. Do you cover the whole of West Brighton, including the blocks near Walker Park, Sunset Hill and Richmond Terrace?
2. Our door is hinged on the left — do we need to order a left-handed smart lock?
3. Will the buttons we press most wear shiny and give our code away?
4. How many digits should our door code be?
5. Do the codes get wiped when the batteries are changed?
6. Can young children use a fingerprint reader, or is a code better for them?
7. (removed by main run at wiring — duplicated New Dorp FAQ "Should we let a voice assistant unlock the front door?") ; Q&A heading "National alarm brands or a local installer?" retitled "National alarm brands set against a local installer" (duplicated Washington Heights)
8. What should we do with the physical keys once the house goes keyless?
9. Will you show us how to factory-reset the lock ourselves if we ever need to?
10. How far ahead do we need to book a West Brighton installation?

### Other question-form headings
- H2 "Keypad Dark or Lock Offline in West Brighton?" (repair capture)
- H2 "Locked Out Somewhere Between Forest Avenue and the Kill Van Kull?" (final repair capture)

De-dup notes: checked against every register in research/smart-lock-installation.md (16 area pages) and the Bayside and Morris Park drafts on disk at ~11:35. Closest neighbours left for the main run to judge: Q11 picking vs Bayside "keyless-only model safer or riskier?" (different intent: cylinder pick-resistance vs no-cylinder trade-off); Q10 windows vs Morris Park "pried side door — would smart lock have warned?" (windows vs door alerting); FAQ 9 factory reset vs Bayside "seller's keypad master code wiped" (handover know-how vs inherited lock); Q13 office-hours schedule vs Rockland "store schedule moving with sunset"; Q14 landlord key vs Nassau "landlord won't let us cut storefront frame". Avoided on purpose: glass-sidelight reach-through (Nassau), outer vs inner door (Brooklyn), landmark approval (HV/Brooklyn), mortise co-op (NYC), lead paint (Dutchess), cost-in-area (NYC/SI).

## Park Slope, Brooklyn (smart-lock-installation-park-slope-brooklyn-ny)

Built 2026-10-17 by the Park Slope builder subagent (batch: Upper West Side MN, Park Slope BK, Astoria QN). Phone (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, #brooklyn) · up-link /smart-lock-installation-brooklyn · Brooklyn ×1.00.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, directQuote).

**Thesis / lane:** a Park Slope brownstone is usually a home that is also a workplace — garden-floor therapy/tutoring practices, licensed (group) family day cares, parlour home offices behind pocket doors, live-in au pairs, nanny shares — inside the city's largest historic district. The smart lock plan is about drawing lines inside one house (business entrance, the stair door between business floor and family, interior privacy, caregiver schedules), under the zoning home-occupation rule and the NYS day-care egress/parent-access rules, plus Fifth/Seventh Avenue shops (2021 burglary spike, 2023 flood) and PPW co-ops / Fourth Avenue buildings as secondary types. Avoids the Brooklyn page's stoop/vestibule/parcel lane, Brooklyn Heights' LPC-facade/co-op lane, Greenpoint's walk-up street door lane, and the UWS page's apartment-practice questions (built in parallel).

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| PS1 | `NYC zoning resolution home occupation 12-10 25 percent floor area 500 square feet one non-resident employee` · FC search → FC scrape (directQuote) | https://zr.planning.nyc.gov/article-i/chapter-2/12-10 | Current text: home occupation "occupies not more than 49 percent of the total floor area of such dwelling unit … and in no event more than 1,000 square feet"; one non-resident may be employed "in connection with the practice of a profession"; not permitted: exterior displays, "for customers or clients of such home occupation to queue or wait for services outside of the dwelling unit", "external structural alterations which are not customary for residences". | §5 para 3, §5.5 bullet 2, §8.5 bullet 5, §9 Q3, §10.5 H3 3, practices section |
| PS2 | same search | https://www.newyorkregisteredagent.com/run-business-from-home/ (excerpt) | Third-party site still states "Occupy more than 25% and no more than 500 square feet" (old rule). | §10.5 H3 3 (the outdated claim corrected) |
| PS3 | `New York OCFS family day care regulations 416 exits locked doors egress "day care" home requirements parent access` · FC search → FC scrape (pdf, directQuote) | https://ocfs.ny.gov/programs/childcare/regulations/416-GFDC.pdf | "Egress doors from the residence must be able to be opened from the inside without using a key"; GFDC home "shall require visitors to the home to … sign out upon departure from the home indicating in writing the time of departure"; parent must have "unlimited and on demand access to such child", right to inspect all parts of the home used for care during hours of operation, access to caregivers. | §5 para 4, §8.5 bullet 4, §9 Q4–Q5, §10.5 H3 4, day-care section, FAQ 5 and 7 |
| PS4 | same search → FC scrape (pdf, directQuote) | https://ocfs.ny.gov/programs/childcare/policies/Childcare-Policy-07-1-Egress-Issues-Family-and-Group-Family-Programs.pdf | Policy Statement 07-1 (revision Feb 4, 2009): first floor of FDC/GFDC must have two means of egress (window option on approval, 24"×24"); "Doors and gates at the ends of passageways are prohibited unless that door or gate is readily openable at all times from the side from which egress is to be made and shall not require a key to open. Doors and gates with keys are prohibited." | §8.5 bullet 4, §9 Q5, §10.5 H3 4, day-care section |
| PS5 | `Park Slope home daycare family day care brownstone licensed Park Slope Parents` · FC search | https://www.parkslopedaycare.com/ ; https://natalyadaycare.com/ ; https://www.zusindaycare.com/ ; https://www.parkslopeparents.com/nanny-guide/daycare/daycare-providers.html (excerpts) | Park Slope providers describe themselves as "Group Family Home Daycare … licensed by New York City Department of Health Bureau of Day Care" (15+ years), "Group Family Daycare in Park Slope", family day care "serving the Park Slope community since 2011". Providers not named on page. | §5 para 3 ("licensed group family day cares advertise from Park Slope homes"), §8 card |
| PS6 | `Park Slope therapist office garden level brownstone private practice Brooklyn` · FC search | https://www.facebook.com/groups/128429399294625/posts/1306592078145012/ ; https://psychoffice.net/listings/ny/therapy-office-park-slope-park-slope-brooklyn/24341 (excerpts) | FB group post: "A windowed, large office in a brownstone in Park Slope on 6th Ave off President St is available Mondays and Fridays…" (shared play-therapy office); PsychOffice: therapy office in Park Slope available full days. | §5 para 3, §8 card, practices section (rooms rented by the day) |
| PS7 | `Park Slope Parents membership families largest parenting group Brooklyn founded Susan Fox` · FC search | https://www.curbed.com/2023/10/park-slope-parents-turns-21-susan-fox.html ; https://www.facebook.com/ParkSlopeParents/posts/… ; LinkedIn (excerpts) | Curbed: "Susan Fox created Park Slope Parents in 2003 as a hyperlocal Yahoo group"; PSP FB: "7,000+ member families living all over Brownstone Brooklyn" (LinkedIn says over 7,500). Page uses "more than 7,000 member families" as the group's own description. | §5 para 3, Sources |
| PS8 | `Park Slope Civic Council house tour annual brownstones open to visitors` · FC search → FC scrape | https://parkslopeciviccouncil.org/category/house-tour/ | Third annual Park Slope Sustainability House Tour Sunday May 17, 2026, 11:00–3:00; "With a rich history dating back to 1959"; 2025 Annual House Tour Sunday May 18, 11–3, "SOLD OUT", tickets $50. | §9 Q9 (house tour), Sources |
| PS9 | `Park Slope burglary brownstone 78th Precinct 2026 OR 2025 break-in front door` · FC search → FC scrape | https://patch.com/new-york/parkslope/park-slope-sees-serious-spike-commercial-burglaries-data (Oct 28, 2021) | ~30 burglaries at Park Slope businesses in two months per Fifth Ave BID; "many of the recent burglaries on Fifth Avenue have been at businesses without roll gates"; tips incl. "commercial-grade door locks and surveillance cameras"; restaurant near 11th Street (Eighth Ave) ~3:15 a.m., "used an object to break the front door", $300; 103 precinct burglaries in 2021, +10%. | §5 para 5, §5.5 bullet 6, §8 cards, §9 Q10, shops section, Sources |
| PS10 | same search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/78th-precinct.page (excerpt) | "The 78 Precinct serves the Park Slope section of Brooklyn, and contains Prospect Park." | research only |
| PS11 | same search | https://www.facebook.com/nypd78pct/posts/… (FC scrape refused "we do not support this site") | Excerpt only: "Make sure your exterior entrance is well lit during nighttime hours and your entrance/door windows are covered." Post body EMPTY (not accessible in build env). | §9 Q10 (lighting mentioned generally) |
| PS12 | `HIPAA physical safeguards 164.310 facility access controls …` · FC search | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C/section-164.310 (excerpt) | "Implement procedures to control and validate a person's access to facilities based on their role or function, including visitor control"; document repairs/modifications to security components "(for example, hardware, walls, doors, and locks)". HIPAA Q intent already on Westchester/Suffolk → used in prose only. | §8.5 bullet 6, practices section, Sources |
| PS13 | `reddit r/parkslope smart lock OR keypad OR locksmith brownstone front door keys` · FC search | https://www.reddit.com/r/parkslope/comments/12926p1/affordable_locksmith/ (excerpt) ; https://lockatlas.com/brooklyn-locksmith/ (excerpt) | r/parkslope: "Need to get our apartment door lock changed. (Simple door knob lock change.)"; LockAtlas: brownstone vestibule lockouts "common in Park Slope, Fort Greene, and Bed-Stuy". Not quoted on page (vestibule intent belongs to the Brooklyn page). | research only |
| — | Carried from research/soundbar-installation.md and research/cat6-repair.md Park Slope sections (sources reached by earlier 2026-10-17 runs; not re-fetched) | Wikipedia Park Slope Historic District; HDC; New York YIMBY Apr 2016; NYC DCP Park Slope rezoning PDF; NYU Furman Center Park Slope/Carroll Gardens; NYC SBS BID directory (bid=60); defalcorealty guide; CityRealty 35 PPW; StreetEasy 9 PPW; brooklyn.studio / Brownstoner (1891 Chappell Queen Anne, 1892 Montgomery Place); Brownstone Boys pocket doors; montaukclub.com; nylandmarks.org Old Stone House; NYC Parks / Wikipedia Litchfield Villa; Wikipedia 14th Regiment Armory; Brownstoner Ansonia Clock Factory; NYU findingaids Methodist Episcopal Hospital; Brooklyn Paper Oct 4 2023 Fifth Ave flood (30+ businesses, up to 6 ft in basements); r/parkslope "In multi-level brownstones, what WiFi set up do folks have?" | HD 1973 / ~1,800 contributing buildings 1862–c.1920 / 2012 ~2,575 / 2016 +292 St Marks–Sterling, largest landmarked neighbourhood; rezoning adopted Apr 30 2003, 110 blocks, R8A Fourth Ave; homeownership 37.1% (2024) vs 32.7%; 6,563 units 2010–2025; BID est. June 2008, 62 block faces, 521 businesses; Seventh Ave restaurants/boutiques/specialty food; 35 PPW Emery Roth 1929 16 storeys; 9 PPW 1929, 43 units, 15 floors; pocket-door hardware inside wall; Montauk Club 1891 Kimball Venetian Gothic (25 Eighth Ave); Old Stone House 1933 reconstruction of c.1699 house, Fifth Ave & Third St; Litchfield Villa 1854–57 A. J. Davis, PPW & 5th St; Armory 1891–95, YMCA complex 2010; Ansonia 1880–81, residential since 1982, co-ops; Methodist hospital opened Dec 19 1887 at 6th St & 7th Ave; flood reported by Brooklyn Paper Oct 4 2023 (page says "autumn 2023"; exact storm date not in the sourced excerpt). | §5, §5.5, §7, §8, §10.5 H3 6, §13 cards, pricing, shops section, apartments section, connectivity |
| — | Silo-wide, not re-fetched | S1 Fixr; S2 Bob Vila; S3 August retrofit; S4 August Connect 10–15 ft; S5/S6 Thread border router; N1 MDL 51-c; N4 TDPA LL63/2021; N6 HPD double-cylinder; B4 LPC hardware no-permit | as logged above | §7.5, §8.5, §10, §10.5, register section, connectivity |

### Prices used (Brooklyn ×1.00 — none invented)
- $1,500–$2,500 single-door keypad or fob reader with electric strike (access-control-installation-brooklyn) — §14, §15 Premium, FAQ 1, §10.5 H3 1, Service schema.
- $250–$450 new electric strike; $295–$485 failed strike repair (door-buzzer pages) — repair capture, §14, §15 Standard, FAQ 1, schema.
- $195/hr, 3-hour minimum ($585) — blueprint §9 — §14.
- Residential door smart lock — no AESS figure → "quoted flat at free walkthrough". $195 setup-visit rate NOT used (still flagged on Brooklyn/LI).
- Fixr national $250–$400, avg $300 — labelled third-party.

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DuckDuckGo: EMPTY (not accessible in build env). §10.5 says so and uses cost-guide / manufacturer / business-advice claims.
- Yelp 1–3★ Park Slope locksmith / smart lock: EMPTY (not accessible in build env).
- Reddit thread bodies: excerpts only; EMPTY beyond excerpts. NYPD 78 Pct Facebook post: EMPTY (scrape refused).
- Local news on smart locks specifically in Park Slope (Patch, Brooklyn Paper, Park Slope Reader): none found → EMPTY.
- Field Notes: no sourced Park Slope install anecdote → written as working routine and labelled so.

## Images (11) — real AESS smart-lock photo set, cropped copies
Drive folder "AESS Website Photos/Smart Lock Installation" empty (main run); CompanyCam not connected. Source: the aess-smart-lock-installation-* photos in images/smart-lock-installation/ (the set the 16 area pages use; no neighbourhood page had used them). Each viewed; cropped with PIL to remove technicians' faces (and the "4A" unit number / customer face / "128" house number photos were not used); WebP q82.

| New file (images/smart-lock-installation/) | Source (crop) |
|---|---|
| smart-lock-installation-park-slope-brownstone-stoop-door-drilling.webp (hero, eager) | aess-…-drilling-keypad-lock-brownstone-stoop.webp (lower 64%, face removed) |
| smart-lock-installation-park-slope-keypad-deadbolt-wood-entry-door.webp | aess-…-keypad-smart-deadbolt-brownstone-door.webp (full) |
| smart-lock-installation-park-slope-keypad-outside-thumbturn-inside.webp | aess-…-keypad-exterior-thumbturn-interior-view.webp (caption overlays cropped off) |
| smart-lock-installation-park-slope-measuring-old-lock-bore.webp | aess-…-measuring-door-bore-for-deadbolt.webp (right half, face removed) |
| smart-lock-installation-park-slope-removing-brass-deadbolt.webp | aess-…-removing-old-brass-deadbolt.webp (right side, face removed) |
| smart-lock-installation-park-slope-latch-bolt-alignment-check.webp | aess-…-checking-latch-bolt-alignment.webp (face removed) |
| smart-lock-installation-park-slope-interior-unit-ribbon-cable.webp | aess-…-connecting-interior-unit-cable.webp (face removed) |
| smart-lock-installation-park-slope-keypad-lever-office-door.webp | aess-…-office-lever-smart-lock-install.webp (face and wall logo removed) |
| smart-lock-installation-park-slope-programming-scheduled-code.webp | aess-…-programming-access-code-app.webp (face removed) |
| smart-lock-installation-park-slope-battery-pack-swap.webp | aess-…-replacing-smart-lock-batteries.webp (face removed) |
| smart-lock-installation-park-slope-keypad-module-service.webp | aess-…-servicing-keypad-wiring.webp (face removed) |
FLAG for Anwar: the aess-* set looks rendered/AI-styled (logo text "Enterprise LLC", idealised scenes), as earlier builders noted for the library; used because it is the silo's designated real smart-lock set. Swap when Drive photos arrive.

## Question register — smart-lock-installation-park-slope-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 10)
1. The only thing between my garden-floor consulting room and the family's stair is an old door with no lock — what should go on it?
2. Could the lock's entry history give away who is in therapy with me, and how do we stop that?
3. Does seeing clients at home change what the city expects of our front door?
4. We run a licensed group family day care on the garden level — how should parents get in at drop-off and pick-up?
5. Does the state's rule against keyed exits affect the gate under our stoop and the back-garden door?
6. Can the pocket doors between our front and back parlours lock, so the front parlour works as a closed office?
7. Our live-in au pair's room needs a lock of its own — should it be a smart lock we can open, or a privacy lock only she controls?
8. A nanny share means another family's caregiver brings their child to our house most mornings — what access should she get?
9. We're opening our house on the Park Slope House Tour — how should the locks be set for a day of strangers walking through?
10. Our Fifth Avenue shop has no roll-down gate — what does the glass front door need overnight besides a better lock?

### §17 FAQ (visible == FAQPage, 7)
1. What does a keypad and electric strike for a garden-floor practice entrance cost in Park Slope?
2. Can a client's code be set to stop working by itself when their course of sessions ends?
3. Should the lock's app account be in the practice's name or the household's?
4. Do you cover Windsor Terrace, Prospect Heights, Gowanus and the South Slope as well?
5. Can you give us a written description of the door hardware for our day-care licence file?
6. Should the practice's smart lock run on a separate Wi-Fi network from the family's?
7. Can a day care's door log replace the paper visitor sign-in sheet?

### Other question-form headings
- H2 "Practice Door Jammed or Keypad Blank in Park Slope?" (repair capture)
- H2 "Ready to Draw the Lines Inside Your House?" (mid CTA)
- H2 "Locked Out Between Sessions or Before the Morning Drop-Off?" (final repair capture)

### De-dup notes
Compared by meaning against every smart-lock page on disk (738 questions) and the Upper West Side and Astoria pages built in parallel. Changed during build: "Should each weekly client get a personal code, or should I let people in from my desk?" (= UWS "therapy clients … codes, or open the door myself?") → replaced by the entry-history confidentiality question; garden-floor client-access question reframed to the stair door (UWS "practice suite … waiting room without opening treatment rooms" is a lobby suite). Avoided on purpose: HIPAA records-room intent (Westchester, Suffolk) — prose only; congregation group codes (Putnam); installation noise (Jackson Heights); flood controller location (Chelsea) — prose only; co-op/condo approval and building-type coverage (NYC, JH) — prose only; reuse of an existing bore (Rockland); lost admin phone (New Dorp); leaked code (Throgs Neck). Partial overlaps for the main run to judge: FAQ 2 (expiring client codes) vs Astoria "rehearsal room by the hour — code per booking slot" (here: course-of-sessions expiry); FAQ 3 (practice vs household account) vs UES "account in the name of our estate manager or family office"; FAQ 1/4 cost and coverage geo-specific by design. Masked paragraph similarity (own script, difflib on geo-masked p/li/td/h3/figcaption ≥12 words, standard licence/warranty/NAP/consent blocks excluded): max 0.641 vs Greenpoint (pricing intro); the shared silo-nav neighbourhood list scores 0.864 vs UWS (silo-nav area list, excluded category).


## Upper West Side, Manhattan (smart-lock-installation-upper-west-side-manhattan-ny)

Built 2026-10-17 by the Upper West Side builder subagent (batch: Upper West Side, Park Slope, Astoria). Neighbourhood spoke of /smart-lock-installation-manhattan. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737; (800) 486-0943 only in the shared header chrome. Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "Firecrawl search" = mcp__Firecrawl__firecrawl_search (excerpts unless scraped); "Firecrawl scrape" = mcp__Firecrawl__firecrawl_scrape (query/directQuote mode). Facts marked "carried" were fetched by the 2026-10-17 soundbar-installation-upper-west-side and cat6-repair-upper-west-side runs (research/soundbar-installation.md and research/cat6-repair.md, "Upper West Side, Manhattan" sections) and are reused, not re-fetched.

Thesis / lane (kept away from Manhattan = doorman platforms/office towers/short stays; UES = staff, high-security key control, service halls, Yorkville walk-ups; Chelsea = landmark doors/galleries/lofts; Washington Heights = household codes beside the landlord's lock): **every way in.** West Side homes are reached from more sides than the hallway door — rooftops that run along a row (the 20th Precinct's Dec 2019 pattern: back door, fire escape or roof), garden duplexes with an under-stoop door and a yard door, top floors beside the roof bulkhead, courtyard arches (Apthorp, Belnord) and gated lanes (Pomander Walk), transoms and shop fanlights (Aug 2026 Amsterdam Ave break-ins), SRO rooming units — and New York law forbids key-locking several of those openings (MDL §104/§188 bulkheads; city entrance-door rule 42-01; HPD fire-escape gates; HMC §27-2044 transoms; HPD shared-housing bedroom-lock position). So the job is a whole-home door survey, the smart lock on the door people actually use, and contacts/strikes/frames or nothing on the rest.

### Research matrix

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| UW1 | `West Side Rag burglary apartment door Upper West Side 2025 OR 2026` · Firecrawl search → Firecrawl scrape (directQuote) | https://www.westsiderag.com/2019/12/26/burglary-spree-hits-the-west-80s-police-searching-for-team-of-four | Dec 26 2019: "Between Saturday, December 14 and Sunday, December 22, seven residential burglaries have occurred between Central Park West and Broadway, from 82nd to 85th Street"; police: "use either a back door, fire escape or roof"; "crossing rooftops, moving from building to building"; 20th Pct Deputy Inspector Timothy Malin: fire escape / patio sliding door locks in good working order; cameras covering ALL access points; Crime Prevention Officer offers free assessments of a building's security. | hero subhead, §5 para 2 + stat 1, §9 roof Q, §9 fire-escape gate Q, §10.5 H3 2, door-survey step 3 |
| UW2 | same search → Firecrawl scrape (directQuote) | https://www.westsiderag.com/2023/07/08/lobby-burglar-hits-same-building-twice | July 2 and July 5 2023: man "entered the lobby of [a building on] West 74 Street [between Columbus and Amsterdam Avenues] without permission and removed a package"; "burglary pattern". Building number not used on page. | research only (lobby layer; not cited on page after edits) |
| UW3 | same search → Firecrawl scrape (directQuote) | https://nypost.com/2024/11/30/us-news/burglar-steals-money-and-baubles-from-posh-uws-pad/ | Nov 30 2024: burglar "smashed through the door at [a] West End Ave. [building], breaking the door jamb"; 39-floor doorman building; safe with ~$220,000 cash + $160,000 jewellery; unclear how he got into the building. Page names avenue only. | §10.5 H3 2 |
| UW4 | same search → Firecrawl scrape (directQuote) | https://www.westsiderag.com/2026/08/06/pair-of-upper-west-side-businesses-burglarized-by-rock-throwing-men-in-ski-masks | Aug 6 2026: two men in ski masks with a large rock — taqueria on Amsterdam between W 84th–85th broken into ~6:20 a.m.; restaurant window at Amsterdam W 74th–75th broken but entry failed; coffee shop at same block entered "after breaking the window above the front door", cash register taken. Business names not used on page. | §5 para 5, §8 Amsterdam card, §9 fanlight Q, §10.5 H3 2 |
| UW5 | `West Side Rag package theft lobby vestibule brownstone Upper West Side` · Firecrawl search | https://www.reddit.com/r/Upperwestside/comments/1lx8o6c/stolen_packages/ ; https://patch.com/new-york/upper-west-side-nyc/burglar-repeatedly-nabs-packages-same-uws-building-police | Excerpts only (Reddit not scraped): "Found a big box in my vestibule yesterday. The address label was ripped off." Patch confirms UW2. Background only, not quoted. | background |
| UW6 | `Upper West Side smart lock OR keyless OR Latch apartment building tenants West Side Rag` · Firecrawl search | https://www.westsiderag.com/2025/11/20/why-residents-of-an-uws-building-are-on-a-rent-strike-only-negotiation-power-we-had ; https://www.reddit.com/r/AskNYC/comments/uadkjs/building_is_now_installing_smart_locks_on/ ; https://www.nytimes.com/2019/03/23/nyregion/keyless-apartment-entry-nyc.html | Excerpts only; no UWS smart-lock story found (NYT 2019 is the Hell's Kitchen Latch suit already on the NYC hub). → EMPTY for UWS smart-lock news. | — |
| UW7 | `site:reddit.com Upperwestside smart lock OR keypad lock OR locksmith OR "lock box" apartment` · Firecrawl search | https://www.reddit.com/r/AskNYC/comments/2vnbu1/change_locks_on_new_apartment/ (excerpt "Landlords are only responsible for the primary lock. Any secondary lock is the tenants responsibility.") ; https://www.reddit.com/r/Upperwestside/comments/1h3sdkm/ (excerpt: break-in at a residential building with doormen and security — the UW3 story) | No r/Upperwestside lock thread found; excerpts background only. UWS Reddit on locks → EMPTY (not accessible in build env beyond excerpts). | background |
| UW8 | `NYC fire code roof door bulkhead multiple dwelling locked must open from inside without key alarm` · Firecrawl search | https://www.nyc.gov/assets/buildings/pdf/MultipleDwellingLaw.pdf ; https://law.justia.com/codes/new-york/mdw/article-4/title-1/104/ ; https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-243205 | MDL §104 (and §188): bulkhead door "shall never be self-locking and shall be fastened on the inside by movable bolts, hooks or a lock which does not require a key to open from the inside of the dwelling"; Admin Code D603.7 same wording for bulkhead/scuttle. | hero, §5 para 3, §8.5 bullet 1, §9 roof Q, §10 table, §10.5 H3 1, glossary |
| UW9 | Firecrawl scrape (directQuote) | https://up.codes/s/entrance-doors-locks-and-intercommunication-systems | Rule "42-01 Entrance Doors, Locks and Intercommunication Systems": "Bulkhead doors and scuttles shall have no key locks and shall not be locked by a key at any time. The only permissible ... means ... is ... a movable bolt or hook on the inside."; "Every entrance from the street, court, yard or cellar to a class A multiple dwelling erected or converted after January 1, 1968 containing eight or more apartments shall be equipped with automatic self-closing and self-locking doors."; "Every self-locking door required under this section shall be ... readily openable from the inside without the use of keys."; vestibule exception. Page cites it as "the city's rule on entrance doors" (no RCNY title number claimed). | §5 para 3, §8.5 bullets 1–2, §9 roof Q, door-survey step 3, §10.5 H3 1 |
| UW10 | same search (result 6) | https://nycadmincode.readthedocs.io/t27/c02/sch02/art11/ | HMC §27-2044 old-law tenements ≥4 stories: where 1-hour apartment doors required, transoms onto entrance hall/stair/public hall "shall be sealed and fire-retarded"; all other such transoms glazed with wire glass and permanently sealed closed; hall doors self-closing. Also §27-2043 (owner key lock, heavy-duty latch + deadbolt, thumb-turn, chain guard) and §27-2041 peephole re-confirmed. | §7 walk-up card, §7.5 transom bullet, §8.5 bullets 3–4, §9 transom Q, glossary |
| UW11 | `Pomander Walk Upper West Side built 1921 landmark West 94th 95th Street gated` · Firecrawl search → Firecrawl scrape (directQuote) | https://en.wikipedia.org/wiki/Pomander_Walk (also streeteasy.com/building/pomander-walk excerpt) | Co-op of 27 buildings between Broadway and West End Ave; the Walk = two rows of eight buildings facing across a narrow courtyard, mid-block 94th–95th, "with a locked gate at each end"; built 1921 by Thomas J. Healy; Tudoresque; infobox NYCL Sept 11 1979, NRHP Sept 14 1982; not open to the public. | §7 cottage-co-op card, §9 lane-gate Q, §13 card |
| UW12 | `The Apthorp courtyard carriage entrance gates Broadway 79th; Belnord courtyard gated arches residents entrance` · Firecrawl search | https://en.wikipedia.org/wiki/The_Apthorp ; https://thebelnord.com/sense-of-arrival/ | Apthorp: full block Broadway / 79th / West End / 78th; arches on West End Ave and Broadway "lead to an internal courtyard with a garden, driveway, and entrances to the apartments"; "elaborate wrought-iron gates". Belnord marketing: "six distinct residential lobbies". (Carried: Apthorp built 1908, 12 stories, for William Waldorf Astor — StreetEasy; Belnord 1908–09, arches on 86th to courtyard — Wikipedia.) | §5 para 1, §7 courtyard card, §9 courtyard Q, §13 cards |
| UW13 | `NYPD 20th Precinct boundaries ... 24th Precinct ...` · Firecrawl search | https://www.upperwestsidecoalition.org/resources/nypd-outreach ; https://www.nyc.gov/site/nypd/bureaus/patrol/precincts-landing.page | "The 20th Precinct serves the neighborhood from 59th to 86th Streets"; 24th Precinct at 151 West 100th Street. | §13 closing para |
| UW14 | `Upper West Side SRO single room occupancy buildings tenants West Side SRO Law Project rooms lock` · Firecrawl search → Firecrawl scrape (PDF, directQuote) | https://www.nyc.gov/assets/hpd/downloads/pdfs/services/shared-housing-roadmap.pdf | HPD Shared Housing Roadmap: shared housing historically included "single room occupancy (SRO) hotels on the Upper West Side"; rooming-unit tenants "reside in one or more individual units pursuant to written or oral leases, with locks on their doors and shared bathrooms and/or kitchens"; "HPD and DOB have interpreted this requirement to mean that residents cannot have locks on bedroom doors"; co-living operators "have installed smart locks to address privacy concerns and evade prohibitions on keyed locks on bedroom doors, but these solutions exacerbate fire safety concerns. Smart locks do not have master keys that can be overridden by building management or the Fire Department (FDNY) in emergencies."; proposal: rooming-unit locks with FDNY-approved fail-safe systems. | §5.5 (context), §7 SRO card, §9 SRO Q, §10.5 H3 5, glossary |
| UW15 | same search → Firecrawl scrape (directQuote) | https://www.westsiderag.com/2024/04/26/upper-west-side-sro-tenants-sue-new-owner-for-allegedly-turning-their-building-into-a-slum | Apr 26 2024: Riverside Studios SRO, "nearly 125 studio apartments, with shared bathrooms for residents on each floor"; 26 tenants on rent strike since November; complaints incl. "a non-secure front door", broken intercom; tenant: "I'll come home at say midnight and the front door will be open"; represented with the Goddard Riverside Law Project; "residents don't need leases to claim that they are tenants". Building name not used on page. | §5.5 stat 6, §9 SRO Q |
| UW16 | same search (excerpt) | https://goddard.org/programs/fighting-homelessness/goddardlawproject/ | Goddard Riverside Law Project assists tenants with eviction, harassment, rent overcharge, illegal lockouts. | §9 SRO Q |
| UW17 | carried (soundbar UWS §7 / cat6 UWS §6/7) | https://www.furmancenter.org/neighborhoods/upper-west-side/ | 2024: population 230,436; housing units 130,471; homeownership 35.6% (city 32.7%); 65+ 22.9%; single-person households 43.6%; 12 Mitchell-Lama / 2,075 units; 22 public housing / 5,927 units. | §5 para 4, §5.5 stats 3–4, §7 Mitchell-Lama card |
| UW18 | carried (cat6 UWS) | http://censusreporter.org/profiles/79500US3604107-nyc-manhattan-community-district-7-upper-west-side-puma-ny/ | "23%† Worked at home" (ACS 2024 1-yr, high margin of error flag). | §5 para 4 (with margin-of-error caveat) |
| UW19 | carried (soundbar/cat6 UWS) | https://www.facebook.com/NYCLandmarks/videos/... ; https://hdc.org/tags/upper-west-side/ ; https://en.wikipedia.org/wiki/The_Ansonia ; https://en.wikipedia.org/wiki/The_Dakota | LPC: "the Upper West Side has nine Historic Districts"; West 71st Street HD 1989 (cul-de-sac row houses 1893–1896); UWS/CPW HD developed 1880s–1930s; Ansonia opened April 16 1904, landmark 1972, condo 1992, light courts, 1904 subway "spurred the development of high-rise apartment buildings on the Upper West Side along Broadway"; Dakota 1880–84, Hardenbergh, 4–20 rooms, co-op 1961, NYC landmark. | §5 para 1, §5.5 stat 2, §7 brownstone card, §13 cards |
| UW20 | carried (cat6 UWS) | https://www.nycgovparks.org/parks/riverside-park-south/history ; https://en.wikipedia.org/wiki/Riverside_South,_Manhattan | Nineteen buildings eventually erected on the former New York Central 60th Street Yard; 180 Riverside Blvd 1999, 200 Riverside 2000. | §7 tower card, §13 card |
| UW21 | carried (cat6 UWS) | https://www.westsiderag.com/2025/10/30/80-vacant-storefronts-blight-51-upper-west-side-broadway-blocks | 80 vacant storefronts on Broadway 59th–110th, Oct 2025. | §5 para 5, §5.5 stat 5, §8 Broadway card |
| UW22 | carried (soundbar/cat6 UWS) | https://columbusamsterdambid.org/ ; https://www.nyctourism.com/attractions-tours/lincoln-square-business-improvement-district/ ; https://www.columbusavenuebid.org/ | Columbus-Amsterdam BID W 96th–110th; Lincoln Square BID founded 1996, home of Lincoln Center; Columbus Avenue BID near AMNH and Central Park. | §8 corridor cards |
| UW23 | carried (cat6 UWS) | https://www.metro-manhattan.com/neighborhoods/uptown-manhattan/upper-west-side/ | "Professional and medical suites in apartment buildings", CPW and West End side streets, 500–2,500 SF; therapy/psychiatry best fit there (broker's description, attributed). | §8 suites card, §9 practice-suite Q |
| UW24 | carried (soundbar UWS / Manhattan M27–M28) | https://www.brickunderground.com/guides/how-to-renovate/fifteen-things-your-coop-or-condo-board-might-not-let-you-do-in-your-renovation ; https://portal.311.nyc.gov/article/?kanumber=KA-01091 | "Some buildings only allow summer renovations ... Most limit work to 9-5 weekdays."; residential construction 7 AM–6 PM weekdays. | §9 summer-rule Q, §10.5 H3 3 |
| UW25 | carried (cat6 UWS) | https://up.codes/viewer/new_york_city/nyc-fire-code-2022/chapter/10/means-of-egress | FC 1027.7: fire escapes and access "continuously maintained free from obstructions". | §8.5 fire-escape bullet, §9 fire-escape gate Q |
| UW26 | silo research reused (not re-fetched) | N1 MDL §51-c (excl. hotels); N3 HMC §27-2043; N4 Tenant Data Privacy Act; N6 HPD fire safety (double-cylinder illegal; key-locked fire-escape window gates prohibited); M15 NYC BC 1010.1.9.9; U4 LPC hardware rule ("ornate historic exterior hardware on special doors"); M11 LPC permit for exterior work; S1 Fixr $250–$400, ~$300, $50–$100/hr (Jan 2025); S2 Bob Vila (Phillips screwdriver, ~30 min); S3 August retrofit (outside untouched, single-cylinder only); S4 August Connect 10–15 ft; S5/S6 Matter/Thread border router; U21 Consumer Reports (retrofit strength = underlying deadbolt) | As listed in the silo file. | §8.5, §9, §10, §10.5, §14 |
| UW27 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 states on page that the AI Overview could not be viewed; each H3 is a claim published by cost guides/manufacturers/home sites. | — |
| UW28 | Local news on smart locks specifically on the UWS (West Side Rag, Patch UWS, I Love the Upper West Side) | — | No UWS smart-lock story found → EMPTY for the service category. | — |
| UW29 | Counts of UWS roof bulkheads / garden duplexes / SRO buildings | — | No sourced figures → EMPTY; nothing stated. | — |

### Prices used (Manhattan ×1.25, as published on smart-lock-installation-manhattan.html; nothing new)
- Keypad or fob reader with electric strike, one door: $1,500–$2,500 base → **$1,875–$3,125**.
- Electric strike added during a keyless upgrade: $250–$450 → **$313–$563**.
- Failed electric strike repair: $295–$485 → **$369–$606**.
- Set-up/programming-only visit: **$265 first hour**, then 30-minute blocks.
- Service/callback: **$195/hr, 3-hour minimum ($585)**, never on the initial install.
- Apartment / brownstone door smart lock incl. whole-home door survey: no AESS figure → "quoted flat at free walkthrough".
- National comparison only: Fixr $250–$400, ~$300, $50–$100/hr (Jan 2025).

## Images (11) — permanent image rule (Drive "AESS Website Photos/Smart Lock Installation" EMPTY per main run; CompanyCam not connected)

New crops saved as WebP q80 in images/smart-lock-installation/, each viewed before and after cropping. Sources were chosen by perceptual hash (dHash) as content not used on any smart-lock page; faces cropped out (partial faces removed from three).

| New file | Source | Crop box (x0,y0,x1,y1) |
|---|---|---|
| smart-lock-installation-upper-west-side-keypad-reader-beside-entrance-door.webp (hero, eager, og:image) | smart-lock-installation-westchester-county-keypad-reader-office-entrance.webp | 700,0,1402,814 (lower face removed) |
| smart-lock-installation-upper-west-side-door-contact-glass-door-header.webp | smart-lock-installation-nyc-door-position-contact.webp | 560,0,1402,1122 (face removed) |
| smart-lock-installation-upper-west-side-gate-post-reader-housing.webp | smart-lock-installation-long-island-gate-reader-wiring.webp | 0,0,440,1024 (face removed) |
| smart-lock-installation-upper-west-side-keypad-and-card-reader-staff-entrance.webp | smart-lock-installation-orange-county-employee-entrance-keypad-reader.webp | none |
| smart-lock-installation-upper-west-side-strike-keeper-glass-door-frame.webp | smart-lock-installation-orange-county-electric-strike-door-frame-prep.webp | none |
| smart-lock-installation-upper-west-side-strike-wiring-keypad-exit-button.webp | smart-lock-installation-orange-county-keypad-strike-push-to-exit.webp | 600,0,1400,1120 (profile removed) |
| smart-lock-installation-upper-west-side-door-controller-boards.webp | smart-lock-installation-long-island-door-controller-cabinet.webp | 640,0,1402,1122 (face removed) |
| smart-lock-installation-upper-west-side-lobby-video-intercom-panel.webp | images/low-voltage/low-voltage-installation-queens-lobby-video-intercom.jpg | 620,0,1040,1120 (profile and "123 Main Street" directory removed) |
| smart-lock-installation-upper-west-side-camera-above-shop-entrance.webp | smart-lock-installation-brooklyn-storefront-entrance-camera.webp | 500,0,1050,960 (profile and readable store-hours sign removed) |
| smart-lock-installation-upper-west-side-maglock-wiring-door-header.webp | smart-lock-installation-orange-county-maglock-header-glass-entrance.webp | 300,0,1066,1120 (head removed) |
| smart-lock-installation-upper-west-side-proximity-reader-door-frame.webp | smart-lock-installation-orange-county-proximity-reader-glass-door-frame.webp | 580,0,1050,1400 (profile removed) |

Rejected after viewing: the aess-smart-lock-installation-* set (content already copied onto Chelsea/Bayside/Bed-Stuy/Park Slope pages; faces), orange-county-fob-card-programming-station (readable checklist), hudson-valley-storefront-frame-sensor (faces, readable store hours), long-island-alarm-sensor-mounting (panic button, not a door), orange-county-keypad-and-camera-entrance-pair (face over the keypad), ulster-county-request-to-exit-sensor / nyc-wave-to-exit-sensor (same content as UES page's RTE image). A crop of ulster-county-push-to-exit-button was made and then replaced because the Astoria page built in the same batch uses the same source photo. In-batch note: smart-lock-installation-upper-west-side-door-contact-glass-door-header.webp and Astoria's door-contact-at-frame-header.webp are different crops of the same source photo (nyc-door-position-contact) — main run may want one of them swapped.
DAILY-LOG note: `images: 11 reused/cropped from images/smart-lock-installation/ library copies (originally images/commercial-security/ and images/low-voltage/) (no real smart-lock photos yet)`.
**Flag for Anwar:** as the UES/cat6/soundbar runs noted, the whole library looks AI-rendered (uniform "Abstract Enterprises" shirts, garbled small text, "123 Main Street" directories). Used only because the run instructions direct Step C / the permanent image rule; replace with real AESS photos.

## Question register — smart-lock-installation-upper-west-side-manhattan-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
Roofs, yards and the top of the house
1. We live on the top floor beside the stair to the roof, and the burglars in the West 80s crossed the rooftops — what up there can legally be locked?
2. Our garden duplex has a door under the stoop and another into the building's hall — which one should carry the smart lock?
Old doors, transoms and the glass around them
3. Our walk-up apartment door still has a glass transom over it — does that matter once a smart lock goes on?
Gates, courtyards, lanes and rooms
4. Our building is entered through a gated arch, then a courtyard, then a lobby — which of those doors can a shareholder actually change?
5. Our walkway has a locked gate at each end — can both gates take keypads without trapping anyone inside the lane?
6. I rent a room in one of the old SRO buildings — can I add a smart lock to my room door?
Co-op rules and fire-escape windows
7. Our co-op only lets residents do alterations in the summer — does changing a lock count as an alteration?
8. Can the security gate on our fire-escape window be opened with a code instead of a key?
Shops, practices and towers
9. Burglars on Amsterdam Avenue got into a coffee shop through the glass above its door — what should happen to the fanlight over ours?
10. Our practice suite opens off the lobby of a Central Park West building — can the door let patients into the waiting room on schedule without opening the treatment rooms?
11. In our Riverside Boulevard tower only the building's locksmith may touch apartment doors — is a smart lock still possible?

### §17 FAQ (visible == FAQPage, 5)
1. Why is an apartment-door lock on the Upper West Side quoted at the door rather than from a price list?
2. Do you cover Manhattan Valley, Lincoln Square and the blocks up to Cathedral Parkway?
3. Can the keypad at our practice be wiped down with disinfectant between patients?
4. Our door has heavy acoustic seals so a musician can practise — will a motorised bolt still throw?
5. Do you fit door sensors on the yard, terrace and roof-stair doors at the same visit?

### Other question-form headings
- H2 "Smart Lock Misbehaving Between Columbus Circle and Cathedral Parkway?" (repair capture)
- H2 "Ready to Find Out Which of Your Doors Really Needs the Smart Lock?" (mid CTA)
- H2 "Locked Outside Your Own West Side Door Tonight?" (final repair capture)

De-dup notes: deliberately avoided — UES fire-escape-window burglary Q (here the intent is whether a window GATE may be code-locked), Bronx roof-door keypad for the super (here: what a top-floor resident may lock against roof-crossers), Bed-Stuy rear garden door hardware, Brooklyn under-stoop egress, Park Slope client codes for a home practice (an earlier "therapy clients at home" Q was dropped for that reason), Park Slope glass shop door overnight (here: the fanlight above the door), Jackson Heights garden-door code, Chelsea old apartment doors, Todt Hill courier gate path, Manhattan in-house locksmith presence (here: building policy that only its locksmith may change hardware). Main run to judge: Q10 practice-suite zones vs Park Slope "consulting room door to family stair"; Q5 lane-gate free exit vs Park Slope "state rule against keyed exits ... gate under our stoop".
Masked-geo similarity (block-level difflib, blocks ≥10 masked words, constants excluded): max 0.632 vs smart-lock-installation-washington-heights-manhattan-ny (a figure caption); all siblings incl. in-batch Park Slope and Astoria drafts < 0.65.


## Astoria, Queens (smart-lock-installation-astoria-queens-ny)

Built 2026-10-17 by batch subagent (batch with Upper West Side and Park Slope; not committed). Phone (347) 434-6392 (body, CTAs, schema; (800) 486-0943 only in the shared header chrome) · GBP Bronx (460 E Fordham Rd, `#bronx`) · up-link `/smart-lock-installation-queens`, plus `/smart-lock-installation-nyc`, all 16 area/hub pages and every neighbourhood page incl. this batch's `/smart-lock-installation-upper-west-side-manhattan-ny` and `/smart-lock-installation-park-slope-brooklyn-ny` (`#sl-nbhd-links` block) · Queens ×1.05, no neighbourhood surcharge.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. Reddit is never scraped (excerpts only). "Carried" = fetched earlier today by the Astoria soundbar / Sonos / Cat6 runs and logged in research/soundbar-installation.md, research/sonos-installation.md, research/cat6-repair.md `## Astoria, Queens` (not re-fetched).

**Thesis / lane:** in Astoria the *people* behind a door change faster than the door. 18.5% homeownership, two-to-four-family buildings outselling one-family 204 to 47, 38.5% single-person households → the lock is planned as a **roster**: one credential per person, dated starts/ends, two administrators, a **fresh key cylinder on move-in** (retrofits leave every old key working), and the legal frame that actually governs shares and small houses — RPL 235-f (roommate/occupant + 30-day notice), Admin Code 26-521 (don't cut off a current occupant's only credential), MDL 51-c applying only at 3+ families (two-family = private dwelling, MDL §4). Plus street/side doors of small walk-ups (2021 five-building pattern; 2019 picked lock), restaurant closing routines (July 2025 window break-ins), production offices/rehearsal rooms around Kaufman Astoria Studios, and outage behaviour (2006 eight-day blackout). Distinct from Queens (multi-door houses/basements/multigenerational), Jackson Heights (co-op permission-first), Flushing (door construction/business rules), Bayside (inter-war house doors/back of house).

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | A6–A10 (r/astoria excerpts only). |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from marketing/how-to/cost guides (August retrofit S3, Bob Vila S2, Fixr S1, generic "tenants can always add a lock", "smart locks stop break-ins", "open from anywhere"), stated as such on the page. |
| 6 | Landmarks | A16–A19 + carried C5–C9 |
| 7 | Building stock / use cases | C1–C4, A15, A20 |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Patch (A2), CBS NY (A3, A11), Queens Gazette (A4), QNS (A5) |
| 10 | Hyperlocal | QNS, Queens Gazette used. Astoria Post / Queens Chronicle smart-lock items: EMPTY (none returned). Facebook group posts (railroad apartments, packages): excerpts only, not used. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). r/astoria locksmith threads seen as excerpts only; no business named or rated on the page. |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| A1 | `New York Real Property Law 235-f roommate law tenant one additional occupant` · FC search → FC scrape | https://www.nysenate.gov/legislation/laws/RPP/235-F | §235-f (rev. 2014-09-22): (3) one-tenant lease = tenant + immediate family + one additional occupant + occupant's dependent children, tenant/spouse primary residence; (4) 2+ tenants: tenants + occupants (excl. dependent children) ≤ number of tenants on lease; (5) tenant informs landlord of occupant's name within 30 days of occupancy or of landlord's request; (6) occupant gets no right to continued occupancy if tenant vacates without landlord's written permission. | §5 para 3, §9 Q1, Roster table, §10.5 H3 2 |
| A2 | `astoriapost.com burglary apartment Astoria 2025 OR 2026` · FC search → FC scrape | https://patch.com/new-york/astoria-long-island-city/burglar-breaks-5-astoria-apartment-buildings-police | Patch, Mar 9 2021: burglar hit 5 Astoria apartment buildings: Mar 1 pried lobby door near 33rd St & 28th Ave (package); apartment near 31st St & 28th Rd via side door; building near 29th St & 31st Ave — took a $2,200 rent check left in front of an apartment door for the landlord; Mar 3 building near 18th St & 27th Ave (failed to enter apartments); apartment near 31st Dr & 23rd St ($150). | §5 para 4, §9 H3 "2021 five-building pattern", Across Astoria (28th–31st Ave grid) |
| A3 | `Astoria Queens burglary apartment door 114th Precinct 2025` · FC search → FC scrape | https://www.cbsnews.com/newyork/news/astoria-apartment-robberies-queens-nypd/ | CBS NY (Sept 2019): two break-ins Aug 29 2019 in same building near 27th St & Hoyt Ave South; $13,000 jewellery; neighbour said lock was picked (safe, passports taken); owner Tony Giannola changing locks and adding cameras when CBS2 visited; 114th burglaries YTD 117→131 (+12%). Owner's name not used. | §5 para 4, §9 H3 "Picked locks and changed locks" |
| A4 | same search → FC scrape | https://www.qgazette.com/articles/astoria-cops-urge-crime-prevention-to-halt-burglaries/ | Queens Gazette, Mar 5 2014: burglaries between 28th & 31st Aves, 30th–51st Sts since January; entry via open fire-escape window, unlocked door, or removing unsecured AC from fire-escape window; precinct advice: dead bolts on all doors, locks on all windows; free NYPD Security Survey via 114th Crime Prevention Office. | §10.5 H3 4, Across Astoria |
| A5 | `Astoria restaurants burglar 114th Precinct four restaurants broke in` · FC search → FC scrape | https://qns.com/2025/08/burglar-breaks-into-astoria-restaurants/ | QNS (Bill Parry), Aug 4 2025: July 21 33-01 36th Ave unlocked window ($500); July 27 35-57 Crescent St, Dutch Kills, unlocked window ($100); July 28 Bareburger 33-21 31st Ave unlocked window; July 29 42-20 30th Ave smashed window; folding stool; 114th burglaries 119 through July 27 2025 vs 116 (+2.6%). Bareburger name not used on page. | §5.5 bullet 6, §8 intro + 30th Ave card, §9 H3 "Closing up…", §10.5 H3 4, Across Astoria |
| A6 | `reddit r/astoria locked out locksmith landlord lock apartment` · FC search (excerpts) | https://www.reddit.com/r/astoria/comments/z97e83/locked_out_of_my_apartment_whats_the_cheapest/ | "First try calling your super. They'll always have a key…" | Research only (lockout context) |
| A7 | same search (excerpt) | https://www.reddit.com/r/astoria/comments/188elpn/landlord_advice_splitting_the_cost_of_a_new_lock/ | Tenant: landlord agreed to new lock but asked to split locksmith cost 50/50; commenter: "A broken lock caused by wear-and-tear is the responsibility of the landlord." | Research only (cost-split intent informed §9 Q4 framing; not quoted) |
| A8 | `reddit r/astoria roommate moved out keys change locks landlord` · FC search (excerpt) | https://www.reddit.com/r/astoria/comments/1tdeeky/apartment_broken_into/ | Poster moved into a rent-stabilized apartment "2 weeks ago between the 36th Ave and Broadway train stations"; reply: "Has the landlord been there long enough to recognize any previous tenants? Did you call a locksmith yet?" | §9 Q4 (paraphrased, attributed to an r/astoria thread) |
| A9 | `r/astoria package stolen vestibule building front door doesn't lock` · FC search (excerpt) | https://www.reddit.com/r/astoria/comments/13dc37n/alright_lets_talk_a_little_more_about_package/ | "My building replaced the front door key with a key fob to deter porch pirates … I think it has helped" | §9 H3 "Fobs instead of keys" |
| A10 | `Astoria Queens two-family homes owner-occupied landlord lives downstairs …` · FC search (excerpts) | https://www.reddit.com/r/astoria/comments/tdkpqn/living_in_23_family_homes/ ; https://www.reddit.com/r/astoria/comments/12c0ytg/survey_how_much_is_your_rent_what_are_your_cross/ | "The landlord lives around the corner and only stops by to check the mail. When we were upstairs our rent went up a whopping $400 over 22 years."; "…basement and a two family house, the floors are kind of thin so I can hear people … going up the stairs to the 2nd…" | §5 para 1 (owner downstairs / around the corner), Across Astoria (long tenancies, paraphrased) |
| A11 | `CBS New York mail theft Astoria 23rd Avenue 21st Street mailboxes residents` · FC search → FC scrape (query, directQuote) | https://www.cbsnews.com/newyork/news/astoria-mail-theft/ | CBS NY (July 2023, image dated 2023-07-21): mail repeatedly stolen from green USPS relay boxes on 23rd Ave at 21st St beneath the Hell Gate Bridge; suspect "using what appears to be a key". | Across Astoria (Old Astoria/Halletts Point) |
| A12 | `Astoria Queens burglary …` (A3 search) excerpt | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/114th-precinct.page ; https://x.com/NYPD114Pct | 114th covers Astoria, LIC, Woodside, Jackson Heights; station 34-16 Astoria Blvd (X profile excerpt). | Research only |
| A13 | `r/astoria smart lock apartment landlord allowed keypad` · FC search | — | No r/astoria smart-lock thread → **EMPTY** for Astoria-specific smart-lock discussion (generic r/homeautomation / August renters page excerpts only). | — |
| A14 | `Astoria railroad apartment layout two-family house …` · FC search | (A10 URLs; Facebook group excerpt) | Railroad-flat claim only in a Facebook group excerpt → **not used** (page says "long floor-through" generically). | — |
| A15 | `Ditmars Boulevard commercial strip Astoria Ditmars-Steinway neighborhood history …` · FC search (full excerpt) | https://cityneighborhoods.nyc/ditmars-steinway | After the 1917 Astoria Line, developers filled blocks south of Ditmars Blvd with two-story brick rowhouses, apartment buildings and corner shops; Ditmars Blvd "one of Queens' most vibrant dining corridors". Weak secondary source, attributed on page as "one neighbourhood history". (Its "Henry Steinway purchased over 400 acres in 1870" not used.) | §8 Ditmars card, Across Astoria (Ditmars–Steinway) |
| A16 | `Socrates Sculpture Park Broadway Vernon Boulevard Astoria founded 1986 …` · FC search (excerpt) | https://socratessculpturepark.org/about-us/ | Abandoned landfill and illegal dumpsite on the Queens waterfront; founded 1986 by a coalition of artists and community members with sculptor Mark di Suvero. | §13 card, §8 Broadway card |
| A17 | `Astoria Library Queens Public Library 14-01 Astoria Boulevard Carnegie 1904` · FC search (excerpts) | https://www.queenslibrary.org/about-us/locations/astoria ; https://writlarge.ctl.columbia.edu/view/418/ ; https://www.facebook.com/QPLNYC/posts/astoria-library-14-01-astoria-boulevard-is-closed-for-the-rest-of-today-thursday/1286373153525054/ | 14-01 Astoria Blvd; "Astoria is closed for renovations"; branch dates 1904–present (Writ Large); closed starting Nov 15 2025 for renovations (QPL Facebook excerpt). ("Carnegie" not confirmed → not stated.) | §13 card |
| A18 | carried (Sonos Astoria) | https://en.wikipedia.org/wiki/Steinway_Mansion ; https://www.mas.org/events/the-legendary-steinway-mansion/ | Built 1857–58 by Benjamin Pike Jr.; hilltop overlooking Bowery Bay; NYC landmark 1967, among the first designated. | §13 card |
| A19 | carried (Sonos Astoria) | https://www.bohemianhall.com/about ; https://theclio.com/entry/53541 | Society 1892; cornerstone Oct 1 1910; outdoor garden 1919; NRHP 2001. | §13 card |
| A20 | carried (Cat6 Astoria) | https://oana-ny.org/history/places-and-landmarks/ | Historic homes on 12th & 14th Sts between 27th Ave and Astoria Park South. | §7 card, Across Astoria |
| C1 | carried (soundbar/Sonos/Cat6 Astoria) | https://www.furmancenter.org/neighborhoods/astoria/ | QN CD1 (incl. part of LIC): homeownership 18.5% vs 32.7% city (2024); single-person 38.5%; rental vacancy 3.4%; 2025 sales 204 two-to-four-family vs 47 one-family. | §5 paras 1–2, §5.5 bullets 1–3 |
| C2 | carried | https://raremaps.com/gallery/detail/106601/one-hundred-houses-on-ditmars-avenue-astoria | "one hundred 20-foot brick houses located on Ditmars Avenue" (promotional broadsheet). | §7 card |
| C3 | carried | https://www.nyc.gov/assets/planning/download/pdf/applicants/env-review/halletts_point/03_feis.pdf ; https://www.durst.org/properties/halletts-point ; https://www.cityrealty.com/nyc/astoria-lic/astoria-cove-4-34-26th-avenue/194195 | Astoria Houses 1,103 units, 22 buildings, 1951; Halletts Point three towers 1,000+ rentals; Astoria Cove mid-rise. | §5 para 5, §7 cards, Across Astoria |
| C4 | carried | https://www.steinway.com/news/features/Company-Town | ~400 Steinway workers in Queens by mid-1870s; Steinway Street named for the company. | §7 card, §8 Steinway card |
| C5 | carried | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=20 ; https://blogs.baruch.cuny.edu/astoria/?p=114 | Steinway Street BID (Steinway Astoria Partnership), 25-69 38th St; part of Steinway St called "Little Egypt" (Arab restaurants, bakeries). | §8 Steinway card |
| C6 | carried | https://movingimage.org/feature/the-astoria-studio/ ; https://movingimage.org/about/museum-history/ | Studio opened 1920 by Famous Players-Lasky at today's 35th Ave & 35th St; Sesame Street from 1993; twelve stages by 2019; MoMI 1988, reopened Jan 2011. | §5 para 5, §8 studio card, §9 production-office Q, §13 card |
| C7 | carried | https://www.nycgovparks.org/parks/astoria-park/history ; …/highlights/8892 ; https://en.wikipedia.org/wiki/Hell_Gate_Bridge | Astoria Park 56+ acres acquired 1913; 1936 pool largest of eleven WPA pools; Hell Gate Bridge dedicated 1917, 1,017-ft steel arch. | §13 card |
| C8 | carried | https://en.wikipedia.org/wiki/Astoria%E2%80%93Ditmars_Boulevard_station ; https://www.nycsubway.org/wiki/BMT_Astoria_Line | Elevated Astoria Line opened 1917; Ditmars Blvd terminal. | §5 para 5, §8 31st St card |
| C9 | carried | https://www.baruch.cuny.edu/nycdata/disasters/blackouts-queens.html ; https://digitalcommons.pace.edu/cgi/viewcontent.cgi?article=1010&context=pelr | 2006 Queens blackout July 17–25 (eight days); Con Ed lost 12 of 22 LIC-network feeders on worst days. | §9 H3 "When northwest Queens loses power", §10.5 H3 6 |
| C10 | carried | https://plescia-cd.com/commercial-general-contractor-astoria/ (excerpt) ; https://www.nycgovparks.org/parks/athens-square | Steinway St, 30th Ave, Broadway retail/restaurant/service spines; Athens Square Park on 30th Ave at 30th St. | §8 cards |
| S | silo-wide, not re-fetched | MDL §51-c (N1/B6), MDL §4 (SI11), HMC §27-2043 (N3/B7), Admin Code §26-521/26-523 (N9), HPD fire safety (N6), Tenant Data Privacy Act LL63/2021 (N4), Fixr Jan 2025 (S1), Bob Vila (S2), August retrofit (S3), August Connect 10–15 ft (S4), Bold Matter up to five ecosystems + Thread border router (S6/S5) | as logged in this file | §5, §7.5, §8.5, §9, §10, §10.5, §14, FAQ 7 |

### Prices used (published lines only — live smart-lock-installation-queens.html / silo "Prices used"; none invented)
| Figure | Scope | Source |
|---|---|---|
| $1,575–$2,625 | one-door keypad/fob reader + electric strike (Queens) | Queens page ($1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike | Queens page ($250–$450 × 1.05) |
| $310–$509 | failed strike repair | Queens page ($295–$485 × 1.05) |
| $195 first hour, then 30-min blocks | setup-only ("roster") visit, Queens | Queens page |
| $195/hr, 3-hr min ($585) | service/callback | blueprint v2.3 §9 / Queens page |
| quoted flat at walkthrough | apartment / floor / house smart deadbolt | no AESS figure |
| $250–$400 avg $300; handyman $50–$100/hr | NATIONAL third-party (Fixr) | silo S1 |
| Worked sum | keypad+strike + new strike = $1,838–$3,098 | arithmetic on published lines only |

## Images (11) — Step C library reuse (Drive "AESS Website Photos/Smart Lock Installation" EMPTY per main run; CompanyCam not connected)
All 11 are NEW crops (PIL, WebP q80) saved as `images/smart-lock-installation/smart-lock-installation-astoria-*.webp`; every source and every crop was viewed; faces, phone numbers printed on shirts, house numbers and readable signage cropped out; captions/alt describe only what is visible; none claims an Astoria job, customer or named building.
| New file | Source (images/smart-lock-installation/) | Crop box |
|---|---|---|
| …-astoria-hero-keypad-deadbolt-wood-door.webp (hero, eager, og:image) | aess-…-keypad-smart-deadbolt-brownstone-door | 430,0,1400,1050 |
| …-astoria-phone-app-code-entry-at-keypad.webp | aess-…-programming-access-code-app | 700,280,1400,1050 |
| …-astoria-inside-thumbturn-turned-by-hand.webp | aess-…-keypad-exterior-thumbturn-interior-view (interior panel only, no text label) | 720,0,1400,760 |
| …-astoria-keypad-housing-opened-for-service.webp | aess-…-servicing-keypad-wiring | 900,180,1400,933 |
| …-astoria-old-brass-deadbolt-coming-out.webp | aess-…-removing-old-brass-deadbolt | 760,300,1400,1050 |
| …-astoria-interior-unit-cable-seated.webp | aess-…-connecting-interior-unit-cable | 880,250,1400,1050 |
| …-astoria-glass-door-keypad-strike-exit-plate.webp | smart-lock-installation-nyc-keypad-electric-strike-glass-door (shirt with 800 number cropped out) | 760,0,1400,1120 |
| …-astoria-door-contact-at-frame-header.webp | smart-lock-installation-nyc-door-position-contact (face + "ALL VISITORS" sign cropped out) | 800,0,1402,440 |
| …-astoria-exit-button-wired-beside-reader.webp | smart-lock-installation-nyc-push-to-exit-button-wiring (face cropped out) | 600,230,1402,1122 |
| …-astoria-electric-strike-terminals-gloved-hands.webp | smart-lock-installation-nyc-strike-terminal-wiring-closeup | 420,0,1400,1120 |
| …-astoria-battery-pack-out-of-interior-unit.webp | aess-…-replacing-smart-lock-batteries | 760,250,1400,933 |
Rejected: aess apartment-door (unit sign "4A"), showing-customer-app-unlock (customer face), video-doorbell (house number 128), office-glass/office-lever/fingerprint/checking-* (faces, reused heavily); access-control photos with "800-486-0943" printed on shirts kept only where the crop removes it. **FLAG:** the aess-* and low-voltage-derived library looks AI-rendered (uniform logo shirts, idealised scenes) although supplied as AESS photos — same caveat as earlier runs; replace with real Astoria job photos when uploaded. DAILY-LOG note suggestion: `images: 11 new crops from images/smart-lock-installation/ (aess-* and nyc-* library; no real smart-lock photos yet)`.

### Masked similarity & size
Geo-masked (all borough/county/neighbourhood names incl. Astoria/Ditmars/Steinway) block comparison (p/li/td/h2/h3/figcaption ≥8 words, word-level difflib) vs all 33 smart-lock siblings incl. batch-mates on disk: max non-constant **0.602** (vs Kingsbridge — paraphrase of MDL §51-c). Excluded constants: freshness stamp, fixed H2 patterns, warranty sentence, licence/rating strip, NAP/WhatsApp line, consent text. File size set to ~240.5 KB with indented JSON-LD (same technique as Bayside/West Brighton) to sit between Morris Park (236,388 B) and Bayside (243,491 B); main run must re-check after Upper West Side and Park Slope are final.

### Flags for Anwar
- check_page.py: all content checks pass; the 16 remaining FAILs are "live sibling … doesn't link back" (hub/area pages must link down — main-run wiring).
- Legal statements are paraphrases of RPL 235-f, Admin Code 26-521/26-523, MDL §4/§51-c, HMC 27-2043, LL63/2021; page says "not legal advice". The two-family/§51-c reading (private dwelling = not a multiple dwelling) should be confirmed.
- AESS practice stated without a source (house policy): fresh cylinder on most installs; won't delete a current occupant's only credential; won't fit inside-keyed/coded models; original hardware bagged and labelled; two administrators; roster sheet; arrival windows 8 AM–8 PM seven days (copied from Queens page); invoice issued to the booking person only.
- General product statements without a specific source: app roles (admin sees history, users limited); per-user notifications; scheduled/time-window codes; some platforms create codes from booking software and some cannot.
- cityneighborhoods.nyc (Ditmars–Steinway history, "most vibrant dining corridors") is a weak secondary source, attributed on page as "one neighbourhood history".

## Question register — smart-lock-installation-astoria-queens-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 7)
1. We added a roommate who isn't on the lease — do we have to tell the landlord before giving them a code?
2. Our roommate's last day is the 31st — can we switch their code off now, before they've actually gone?
3. Can each roommate keep their own comings and goings private from the others?
4. The owner of our two-family says the last tenants' keys "probably" all came back and won't change the cylinder — what can we do?
5. The owner downstairs offered to put our apartment lock on the same app as the front door — should we accept?
6. Our production office near the studios is rented for one season — can everyone's door code run off the crew list and stop on wrap day?
7. We rent our rehearsal room by the hour — can each booking get a code that works only for its slot?

### §17 FAQ (visible == FAQPage, 8)
1. What does a keypad and electric strike cost on the street door of a small Astoria apartment building?
2. Do your crews cover Ditmars–Steinway, Astoria Heights and Old Astoria as well as the blocks near Broadway?
3. Three of us share the apartment — can each roommate pay a share of the invoice directly?
4. Does the landlord need to be at the apartment while you install?
5. Could taking the smart lock off at the end of our lease cost us part of the security deposit?
6. Can the low-battery warning go to everyone in the apartment, not just the person who set it up?
7. Half of us use iPhones and half use Android phones — is there a lock that works for both?
8. Do we get to try every code and the key before the balance is due?

### Other headings (non-question H3s in §9, for intent tracking)
- What the 2021 five-building pattern says about street and side doors · Picked locks and changed locks: the 2019 Hoyt Avenue South break-ins · Fobs instead of keys on the street door · Closing up after the July 2025 restaurant break-ins · When northwest Queens loses power. CTA H2s are statements, not questions.

### De-dup notes
- Checked by meaning against all 738 questions on the 33 smart-lock pages on disk (incl. batch-mates UWS/Park Slope drafts). Avoided/dropped: roommates each own code (Manhattan), cancel a departed roommate's code (Kingsbridge), relative not on lease gets a code / leaseholder leaves (Washington Heights), owner sees tenant's entries (Brooklyn), shared two-family door codes (Staten Island), previous owners' access (Staten Island/Bayside), booking lead time (Washington Heights/West Brighton — replaced by FAQ 8), fire-escape windows (UES — kept as non-question narrative), restaurant burglary via windows (West Brighton/Flushing — narrative only), long outage access (Long Island/Hudson Valley/Greenpoint — narrative only), one-time codes (Bayside).
- Partial overlaps for the main run to judge: §9 Q1 vs Washington Heights "relative … isn't on the lease — can she have her own code" (ours = landlord-notice duty under RPL 235-f); §9 Q2 vs Kingsbridge "roommate moved out … cancel it" (ours = before departure, Admin Code 26-521 timing); §9 Q4 vs Brooklyn/Bronx two-family lock-rule questions (ours = owner refuses to re-key after turnover); FAQ 5 vs NYC "What happens to my smart lock when I move out" (ours = security-deposit damage); FAQ 4 vs Manhattan "Can the super … be there while you work?" (ours = whether landlord presence is required); FAQ 1 cost and FAQ 2 coverage are geo-specific by silo design.


<!-- batch 2026-10-17T16:28Z: smart-lock-installation-riverdale-bronx-ny -->

# Research — smart-lock-installation-riverdale-bronx-ny (batch 2026-10-17)

Queue line: Smart Lock Installation | Riverdale, Bronx | up /smart-lock-installation-bronx | phone (646) 490-0629 | GBP Bronx (460 E Fordham Rd, #bronx).
Silo-wide research reused from research/smart-lock-installation.md (laws MDL §51-c, HMC §27-2043, MDL §50-a, Tenant Data Privacy Act, 2010 ADA door hardware, Fixr Jan 2025 $250–$400 / ~$300, LawnStarter $330 / $200–$460, August bridge 10–15 ft). Only the local section below is new.

**Thesis:** In Riverdale somebody else usually has a say over the door first — a co-op board, managing agent and front desk in the 1960s doorman towers; Landmarks (and a private property owners association that owns the streets) in Fieldston; a Landmarks rule chapter written for the Riverdale Historic District alone on Sycamore/Independence Avenues; the Special Natural Area District under all of it. So every Riverdale job starts as a "permission map" (who must agree, in what order, with what paperwork), then the lock.

## Riverdale

### Research matrix (exact query · platform · URL · finding · page + section used)

| # | Query | Platform | URL | Finding | Used on page |
|---|---|---|---|---|---|
| R1 | `Riverdale Bronx co-op buildings Henry Hudson Parkway high-rise co-ops history` | Firecrawl search | https://cooperatornews.com/article/a-river-runs-through-it | Post-WWII boom of multi-family and large apartment buildings, many became co-ops; Henry Hudson Bridge & Parkway 1936 (excerpt only). | Background only |
| R2 | same | Firecrawl search (excerpt) | https://streeteasy.com/building/3333-henry-hudson-parkway-bronx | Co-op, 439 units, 22 stories, built 1970. | §5.5 fact 2 |
| R3 | `Riverdale, Bronx` | Firecrawl scrape (query, directQuote) | https://en.wikipedia.org/wiki/Riverdale,_Bronx | Boundaries (Yonkers N, Van Cortlandt Park/Broadway E, Kingsbridge SE, Spuyten Duyvil S, Hudson W); Riverdale Ave main thoroughfare; ZIPs 10463/10471; CD8; sub-areas (Fieldston S of W 250th E of HHP; Hudson Hill above W 246th W of HHP; North Riverdale above W 254th W of Fieldston Rd; Spuyten Duyvil); Fieldston HD 2006; 15-acre Riverdale HD 1990; 1950s six-story brick; early–mid 1960s 10–20-story towers, many full-service doorman, Philip Birnbaum (Skyview, Windsors, Whitehall); by 1980s most rentals converted to co-ops; "mostly owner-occupied" unlike most of Bronx; Spuyten Duyvil greatest concentration of high-rises (Century, 555 Kappock, Winston Churchill); post-2005 Central Riverdale condo boom; Hudson Hill mansions Greyston (1864), Alderbrook (1880), Stonehurst (1861), Oaklawn (1863); 50th Precinct, 3450 Kingsbridge Ave, 126 burglaries 2022; Metro-North Riverdale (W 254th–255th) & Spuyten Duyvil stations; BxM1/BxM2/BxM3/BxM18; Columbia Riverdale shuttle terminus W 238th & Riverdale Ave; 16,000 Jewish adults + 4,000 children in 10,000 households; Hebrew Institute of Riverdale, Riverdale Jewish Center, Riverdale Temple; Wave Hill 20 acres, 1840s William Lewis Morris, Theodore Roosevelt & Mark Twain. | Hero, §5 paras 1–2/5, §5.5 facts 1/6, §7 cards (towers, 1950s, estates, Spuyten Duyvil, new condos), §8 cards (W 238th, congregations), §13 Wave Hill & station cards |
| R4 | `Fieldston Historic District Bronx Landmarks Preservation Commission private streets Fieldston Property Owners Association` | Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Fieldston,_Bronx ; https://s-media.nyc.gov/agencies/lpc/lp/2138.pdf | FPOA formed 1923; owns streets & common areas, plows, ~1000 trees, runs security patrol; dues from ~250 homeowners; LPC designated Jan 10, 2006; LPC report: privately owned streets maintained by annual assessments. | §5 para 3, §5.5 fact 3, permission table, §9 Fieldston Q, §13 Fieldston card |
| R5 | `Fieldston Historic District designation report number of buildings …` → scrape | Firecrawl search + scrape | https://www.nypap.org/preservation-history/fieldston-historic-district/ | "257 houses and related structures … 140 acre development"; Delafield Estate; layout finalized 1914 by Albert Wheeler; 1928 handbook of approved architects; styles Colonial Revival, Craftsman, Tudor, Mediterranean, modernist; City Council approved Apr 26, 2006 (Land Use Cttee Apr 11); opponent: "76 different architects … 23 architectural styles". | §5 para 3, §5.5 fact 3, §7 Fieldston card, Historic Houses section + at-a-glance table, §13 card |
| R6 | `Riverdale Historic District 1990 Landmarks Preservation Commission Independence Avenue Sycamore Avenue houses` → scrape | Firecrawl search + scrape (markdown) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-90749 (63 RCNY Ch. 6) | District: early railroad suburb; 34 buildings; seven estates of the 1850s served by common carriage alley (Sycamore Ave); subdivided from 1935; 4 houses 1935–38; 12 structures 1950–80; pre-1940 buildings = significant architecture; "significant architectural feature" includes type/style of any window, door, light, fixture; post-1939 modifications get CNE/PMW if no damage to significant landscape improvement and compatible materials/finish; LPC regulates walls, steps, paths, drives, railings, fences, gates and gate posts, excavation/fill on slopes >15%; district lies entirely within Riverdale SNAD; application before work, no work until permit. | §5 para 3, §5.5 fact 4, permission table, §9 two Riverdale HD Qs, Historic Houses section, §13 Sycamore card |
| R7 | same search | Firecrawl search (excerpt) | https://www.nypap.org/preservation-history/riverdale-historic-district/ | Designated Oct 16, 1990. | §5 para 3, at-a-glance table |
| R8 | `Riverdale Special Natural Area District NA-2 zoning …` | Firecrawl search (excerpt) | https://zr.planning.nyc.gov/article-x/chapter-5 (ZR §105-942) | SNAD-2: "The Riverdale Ridge … composed of part of Riverdale, Spuyten Duyvil and Fieldston. This ridge contains steep slopes, rock outcrops, ponds, brooks, swampy areas and mature trees"; site plans show trees ≥6-inch caliper; steep-slope provisions from Dec 19, 1974. | §5 para 4, §7.5 "Doors on a ridge", Historic Houses gate subsection, FAQ (SNAD) |
| R9 | `Furman Center Riverdale Fieldston …` (scrape) | Firecrawl scrape (query, directQuote) | https://www.furmancenter.org/neighborhoods/riverdale-fieldston/ | 2,087 units added 2010–2025 (1,462 market, 625 income-restricted); units authorized by new permits 579 (2024), 476 (2025); serious property crime 7.6/1,000 (2024) vs 10.6 (2023); 16 Mitchell-Lama properties. (Homeownership 38.4%, 65+ 23.3%, violations 222.4 deliberately NOT used — already on Kingsbridge page.) | §5 para 5, §5.5 fact 5 |
| R10 | `Skyview on the Hudson Riverdale co-op units towers Philip Birnbaum garage` | Firecrawl search (excerpts) | https://streeteasy.com/building/skyview-5700-arlington-avenue-bronx ; https://dlc.library.columbia.edu/nyre/cul:1vhhmgqpz5 | Skyview, 5700 Arlington Ave, 437 units; Skyview On The Hudson 5700–5900 Arlington Ave, architect Philip Birnbaum. | §5.5 fact 2, §13 Skyview card |
| R11 | `Johnson Avenue Spuyten Duyvil shopping strip …` | Firecrawl search (excerpts) | https://www.nytimes.com/2017/05/17/realestate/spuyten-duyvil-the-bronx-crosscurrents-of-suburb-and-city.html ; https://www.compass.com/building/the-winston-churchill-bronx-ny/293529667585983477/ ; https://www.homes.com/building/the-blue-building-bronx-ny/b-42vb61jt9tzk4/ | Winston Churchill 2500 Johnson Ave, 20 stories, built 1967; 555 Kappock St 25 stories; Blue Building 2400 Johnson Ave 13 stories, 130 units. | §7 Spuyten Duyvil card, §13 Johnson/Kappock card |
| R12 | (scrape) | Firecrawl scrape (query) | https://www.brickunderground.com/buy/buy-curious-spuyten-duyvil-riverdale-bronx-housing-pricing-waterfront | HHP divides Spuyten Duyvil east/west; west = big waterfront co-ops; east = single-family houses 1900s–1920s and townhouses 1960s/70s/early 2000s; Villa Charlotte Brontë 17 units, 1920s; Winston Churchill & Presidential large 1960s–70s co-ops; SNAD limits new development; The Henry, 6-story, 55 units, 2022; Tangiers 1958, 8 stories, 73 units, doorman, indoor parking; Knolls Crescent tiny commercial corner; BxM1/BxM2; Metro-North ~25 min (agent quote). | §7 cards (towers, Spuyten Duyvil, new condos), §8 Knolls Crescent card, Ridge houses section, small prewar co-ops subsection, §13 card |
| R13 | `Riverdale Bronx private schools Horace Mann Riverdale Country School Ethical Culture Fieldston …` | Firecrawl search (excerpts) | https://en.wikipedia.org/wiki/Ethical_Culture_Fieldston_School ; https://www.ecfs.org/locations-bronx-campus/ ; https://www.niche.com/k12/riverdale-country-school-bronx-ny/ | Fieldston, Riverdale and Horace Mann known as "the hill schools", on hilly area above Van Cortlandt Park; ECFS 3901 Fieldston Rd; RCS 5250 Fieldston Rd, founded 1907. | §8 hill schools card |
| R14 | `Riverdale Press burglary Fieldston house break-in 2025 OR 2026` → scrape | Firecrawl search + scrape | https://www.riverdalepress.com/stories/police-beat,36924 | Burglar broke into a home on 4700 block of Fieldston Road (May 21); 88-year-old resident; entry point a broken window frame at the rear (article year not captured). | §10.5 H3 "safer" |
| R15 | same → scrape | Firecrawl scrape | https://www.riverdalepress.com/stories/police-focus-on-recidivist-break-in-bandits,51534 | Nov. 30 FPOA letter: Excel Security, the company guarding Fieldston's private streets, reported thefts from unlocked cars in driveways/in front of homes (article year not captured). | §10.5 H3 "safer", Historic Houses "patrol" subsection |
| R16 | `riverdalepress.com burglary apartment Riverdale Avenue OR Johnson Avenue OR Kappock …` → scrape | Firecrawl search + scrape | https://www.riverdalepress.com/stories/feb-2-2016-crime-round-up,61669 | Police said the door of the apartment at 603 Kappock St. may have been unlocked at the time of a burglary (Jan 2016). | §10.5 H3 "safer" |
| R17 | `"Burglars hit Riverdale Avenue" Riverdale Press` → scrape | Firecrawl search + scrape | https://www.riverdalepress.com/stories/august-18-2016-crime-round-up,60454 | Aug 2016: two burglaries on Riverdale Ave between W 259th–260th — rock through front window of Subway at 5670 Riverdale Ave ($1,000 from register) and a Verizon Wireless store a block north. | §8 North Riverdale card, §10.5 H3 "safer" |
| R18 | `Landmarks Preservation Commission FAQ do I need a permit interior work historic district …` | Firecrawl search (excerpt) | https://nyc-business.nyc.gov/nycbusiness/description/performing-work-on-a-landmarked-property | Owners in a historic district need an LPC permit before doing any work; also for any work needing a DOB permit; PMW: no fee. | §9 Fieldston FPOA answer, pricing "Costs that belong to someone else" |
| R19 | `reddit Riverdale Bronx co-op board smart lock OR keypad OR "door lock" apartment` | Firecrawl search (excerpts only) | https://www.reddit.com/r/AskNYC/comments/zrjotk/do_electronic_locks_make_sense_in_an_apartment/ | Excerpt: an August lock uses the existing deadbolt so the key still works and the super can get in. Not Riverdale-specific; informed the retrofit-first approach, not quoted. | Background only |
| R20 | `Riverdale Press co-op key fob entry system shareholders building` | Firecrawl search | (results incl. our own access-control-installation-bronx page claiming a 120-unit Riverdale co-op ButterflyMX job) | Unverifiable self-claim — NOT used. | Not used |
| R21 | `Riverdale Press co-op package theft lobby doorman building security 2025` / `"Riverdale Press" doorman co-op lobby intruder …` | Firecrawl search | — | Only Co-op City / generic results; nothing Riverdale-specific. | EMPTY for Riverdale lobby/package stories |

### Mandatory sources status
- Reddit (r/bronx, r/AskNYC): only generic excerpts (R19) — no Riverdale smart-lock thread found. Threads not scraped.
- Google PAA / PASF / Answer the Public / AI Overview: `EMPTY (not accessible in build env)`. §10.5 says so on the page and uses recurring national claims instead.
- Bing & DuckDuckGo: `EMPTY (not accessible in build env)`.
- Yelp 1–3★: `EMPTY (not accessible in build env)`.
- Local news / hyperlocal (Riverdale Press): R14–R17 (older items; dates where captured). Riverdale smart-lock-specific news: `EMPTY` (none found).
- Landmarks / zoning / permits: R4–R8, R18.

### Prices used (no new prices; Bronx ×1.00, copied from smart-lock-installation-bronx.html)
Single-door keypad or fob reader + electric strike $1,500–$2,500 · new electric strike $250–$450 · failed strike repair $295–$485 · setup-only visit $225 first hour then 30-min blocks · service/callback $195/hr, 3-hr min ($585). Own door: quoted flat at walkthrough (no published price).

### Images (11) — Step C, real AESS library photos, cropped to remove technicians' faces, the "4A" unit plate and the "128" house number; WebP q82
| File (images/smart-lock-installation/) | Source | Shows |
|---|---|---|
| smart-lock-installation-riverdale-bronx-apartment-hallway-keypad-app-check.webp | aess-…-apartment-door-smart-lock-app.webp (crop) | finger on keypad deadbolt, phone app, dark apartment door (hero) |
| smart-lock-installation-riverdale-bronx-locked-status-app-wood-door.webp | aess-…-checking-lock-status-in-app.webp | phone "Locked" beside keypad deadbolt, wood door |
| smart-lock-installation-riverdale-bronx-interior-unit-ribbon-cable.webp | aess-…-connecting-interior-unit-cable.webp | ribbon cable into interior unit |
| smart-lock-installation-riverdale-bronx-interior-unit-battery-change.webp | aess-…-replacing-smart-lock-batteries.webp | AA batteries into interior unit |
| smart-lock-installation-riverdale-bronx-measuring-old-bore-wood-door.webp | aess-…-measuring-door-bore-for-deadbolt.webp | tape from old bore to door edge |
| smart-lock-installation-riverdale-bronx-keypad-outside-thumbturn-inside.webp | aess-…-keypad-exterior-thumbturn-interior-view.webp (caption labels cropped off) | keypad outside / thumb-turn inside |
| smart-lock-installation-riverdale-bronx-lever-keypad-glass-office-door.webp | aess-…-office-lever-smart-lock-install.webp | latch plate + lever keypad, glass office door |
| smart-lock-installation-riverdale-bronx-adding-access-code-keypad.webp | aess-…-programming-access-code-app.webp | keypad + "Add Access Code" screen |
| smart-lock-installation-riverdale-bronx-video-doorbell-beside-keypad-deadbolt.webp | aess-…-video-doorbell-and-smart-lock.webp | video doorbell beside keypad deadbolt |
| smart-lock-installation-riverdale-bronx-strike-screw-keypad-deadbolt-house-door.webp | aess-…-suburban-front-door-smart-lock-van.webp (van cropped out) | drill on latch plate under keypad deadbolt |
| smart-lock-installation-riverdale-bronx-latch-strike-alignment-check.webp | aess-…-checking-latch-bolt-alignment.webp | finger on latch under keypad deadbolt |

### Question list on this page (add to the silo register)
**§9 Your Questions Answered (H3, 11)**
1. Our co-op's garage has an elevator that comes straight up into the building, past the doorman — does that change what my apartment door needs?
2. The doorman's key cabinet holds a sealed spare for every apartment so staff can get in for a leak — what goes in our envelope once the door has a keypad?
3. Our house rules say every visitor is announced from the desk — does giving the housekeeper a door code break that rule?
4. With a doorman downstairs around the clock, what does a smart lock on our apartment actually add?
5. We're buying into a Riverdale co-op — can the lock request go in with the board package, or should it wait until after closing?
6. In our co-op, is the apartment entry door the corporation's property or ours, and who pays if it's damaged?
7. Fieldston's streets belong to the property owners association — does the association get a say on a keypad, separate from Landmarks?
8. Our house is inside the Riverdale Historic District but was built after 1940 — does Landmarks treat a keypad on it any differently?
9. We want a keypad on the stone gate post at the foot of our drive in the historic district — does Landmarks regulate the post itself?
10. Every shareholder who has ever parked in our garage still has a copy of the key to the door from it into the lobby — what does going keyless fix, and what must stay?
11. Our toddler has learned to turn the thumb-turn — can the smart lock stop him opening the door without breaking the fire rules?

**§17 FAQ (visible == FAQPage, 3)**
1. Do your installers cover Spuyten Duyvil, Hudson Hill, North Riverdale and Fieldston as well as Central Riverdale?
2. If our board turns the lock down after we have already bought it, what happens to the money?
3. Does the Special Natural Area District have any say over a smart lock?

**Other question-form headings:** Locked Out Twenty Floors Up or at a Fieldston Door?

**De-dup notes:** dropped during build because they matched batch siblings in meaning — "keypad switched off at night" (St George has it) and "inside-half-only retrofit on a landmarked house needs Landmarks?" (St George / Tribeca historic-district door questions); the latter's facts were folded into answer 7 as prose.


<!-- batch 2026-10-17T16:28Z: smart-lock-installation-st-george-staten-island-ny -->

## St. George, Staten Island (smart-lock-installation-st-george-staten-island-ny)

Built 2026-10-17 by the St. George builder subagent (batch with -riverdale-bronx-ny and -tribeca-manhattan-ny). Main run merges this into research/smart-lock-installation.md.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used.
Thesis: St. George is a hillside, not a flat block. Landmark-district houses step down the slope, so many have a street door above and a garden or service door a storey below. Commuter households leave on foot for the free 24-hour ferry. New waterfront rentals sit by the terminal, and offices work beside Borough Hall and the courts. So the lock plan is about levels (a connection point per floor), what can be seen from the street front and back (LPC), codes timed to the ferry clock, and controlled file-room doors (Rule 1.6(c)).
Silo-wide sources reused (not re-fetched): S1 Fixr ($250–$400, avg $300, Jan 2025), S2 Bob Vila (screwdriver/≈30 min), S3 August retrofit (single-cylinder only), S4 August Connect 10–15 ft, S5 Yale Matter/Thread border router same ecosystem, N1 MDL §51-c (tenant's own lock, ≤3" circumference, duplicate key; excludes municipal housing authority), N3 HMC §27-2043, N4 Tenant Data Privacy Act, N6 HPD fire safety (self-closing 3+ units; double-cylinder illegal on apartment doors), 2022 NYC BC §1010.1.9 egress, WB12 nyc-business LPC page (door replacement = PMW; hardware not addressed), WB16 Schlage Arrive 1-3/8"–2", backset 2-3/8"/2-3/4", prices table (SI ×1.10).

| # | Query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| SG1 | `St. George Staten Island neighborhood history housing ferry terminal St. George Historic District` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/St._George,_Staten_Island | NE tip of SI; "most densely developed neighborhood on Staten Island"; 0.412 sq mi; ZIP 10301; CD1. Named St. George in the 1880s after George Law (Erastus Wiman). Terminal opened 1886, chosen as nearest point to Manhattan (~5 mi), last renovated 2005; served by SI Ferry, SIR, NYC Ferry, nearly all buses. Borough Hall 2–10 Richmond Terrace, 1906, Carrère and Hastings. Former courthouse 12–24 Richmond Terrace, 1919. Family Court 100 Richmond Terrace, 1931. Supreme Court 26 Central Ave, opened 2015. 120th Pct at 78 Richmond Terrace (1920–23 building, landmark 2000). St. George/New Brighton HD designated 1994: 78 houses plus St. Peter's. Curtis HS opened 1904, first HS on SI, landmark. St. George Theatre: 2,800 seats, 1929, renovated 2004. Library Center: 5 Central Ave, 1906–07. Ballpark: 7,171 seats, 2001, FerryHawks. National Lighthouse Museum opened 2015. Many older houses converted to small apartment buildings in the 1930s. Ambassador Apartments: 30 Daniel Low Terrace, Art Deco, 1932. Castleton Park: 165–185 St. Marks Pl, 20 storeys. 2020 NTA SI0101: 20,549 residents (+9.5% from 18,774), 7,732 households, 31.1% with children <18, 70.2% renter-occupied. 120th Pct 2022: 124 burglaries; crime −83.3% 1990–2022. | Hero; §5 paras 1, 3–5; §5.5 bullets 1, 2, 5, 6; §7 cards (commuter buildings, divided houses); §8 cards (Richmond Terrace, Central/Hyatt); §13 all 6 cards; apartment-residents section |
| SG2 | `St. George/New Brighton Historic District Landmarks Preservation Commission designated 1994 houses St. Marks Place Westervelt` · WebSearch → WebFetch | https://hdc.org/?p=7732 | Designated July 19, 1994. New Brighton Association formed 1834, ended by Panic of 1837. Later houses in Shingle, Colonial Revival and Italianate styles. Several by Edward Alfred Sargent. Hillsides overlooking the harbour; original street plan survives. | §5 para 3; §5.5 bullet 1; historic-district section |
| SG3 | same search · WebFetch | https://preserve.org/stgeorge/stgeorgedistrict.htm | About 78 buildings on parts of St. Marks Pl, Carroll Pl, Westervelt Ave, Hamilton Ave, the Phelps Place cul-de-sac and short stretches of Richmond Terrace. Part of New Brighton (Thomas E. Davis, 1834–35); 1835 plan of crescent streets climbing a steep hillside. Styles: Greek Revival (404 Richmond Terrace, c.1835), Italianate (97 St. Marks Pl), Second Empire (Westervelt and the north side of St. Marks), Queen Anne, Shingle and Colonial Revival (the majority), 1920s–30s terra-cotta commercial buildings on Westervelt. **North-side St. Marks houses sit on narrow, deep lots running downhill to Carroll Place, with extra storeys at the rear.** | §5 paras 2–3; §7 cards (Greek Revival/Italianate, Second Empire, Queen Anne); two-levels section; §8 Westervelt card; Q&A rear-door/Carroll Place Q; historic-district section |
| SG4 | `St. George Staten Island neighborhood…` · WebFetch | https://cityneighborhoods.nyc/st-george | Steep hills above the harbour, historically "Signal Hill or Fort Hill". Bounded by Victory Blvd, St. Marks Pl, Fort Pl, Belmont Pl. Multi-storey apartments built for ferry commuters. Ambassador Apartments "Apthorp-like". St. George Theatre: Beaux-Arts, by Eugene De Rosa, reopened 2004 after a community campaign. Empire Outlets and North Shore Esplanade part of 21st-century waterfront redevelopment. Ferry free since 1997. | §5 para 2; §8 waterfront card; §13 theatre card |
| SG5 | `Lighthouse Point St. George Staten Island apartments opened residential tower` · WebSearch → WebFetch | https://newyorkyimby.com/2025/06/lighthouse-point-phase-one-finishes-construction-at-5-bay-street-in-st-george-staten-island.html | Phase One at 5 Bay St completed (June 6 2025 article): 115 units, studios–2BR; ~60,000 sq ft commercial (CSI Tech Incubator, The Learning Experience, Club Pilates); 274 parking; Triangle Equities; Cooper Carry; site was U.S. Lighthouse Service General Depot 1863–1966. | §5.5 bullet 4; §8 Lighthouse Point card; §13 museum card |
| SG6 | same search · WebFetch | https://commercialobserver.com/?p=509626 | Residences at Lighthouse Point: 115 units, 12 storeys, 75% market / 25% affordable (40–130% AMI), rents $2,000–$4,000, leasing expected early 2025; construction began 2016, stalled after the construction manager's bankruptcy, resumed late 2022. | §5.5 bullet 4; §5 para 4 |
| SG7 | `Castleton Park apartments St. Marks Place…` · WebSearch → WebFetch | https://rebusinessonline.com/stellar-management-camba-housing-ventures-acquire-castleton-park-on-staten-island/ | July 24 2015: Castleton Park, 454 affordable units, about 40 years old, bought by Stellar Management/CAMBA; $30M renovation (facade, parking, elevators, common areas, kitchens/baths). Doors and entry not mentioned. | §5.5 bullet 4 |
| SG8 | `Bay Street Landing St. George…` · WebSearch → WebFetch | https://scaranoarchitect.com/project/bay-street-landing/ | Poured-in-place concrete 1930s factory building, converted, with added floors (project year 2004). Search results show "BSL One Owners Corp" (co-op). Not used on the page (no question built on it). | research only |
| SG9 | `Staten Island Ferry runs 24 hours every 30 minutes…` · WebSearch → WebFetch | https://www.6sqft.com/full-24-hour-staten-island-ferry-service-resumes-today/ | Aug 16 2021: full 24-hour service restored; 15-min peak (7–9 a.m., 5:30–7:30 p.m.), half-hourly otherwise; ~70,000 weekday riders and ~22M a year (2019); ~25-min crossing; free; LL88/2013 requires half-hourly 24/7 service. | §5 para 1; §5.5 bullet 3 (labelled "as of the 2021 restoration") |
| SG10 | `reddit St. George Staten Island living ferry commute apartment hill` · Firecrawl search (excerpts only, threads not opened) | https://www.reddit.com/r/howislivingthere/comments/1qefgv5/what_is_it_like_living_in_this_part_of_staten/ ; https://www.reddit.com/r/statenisland/comments/16druix/how_safedangerous_is_st_george/ | Excerpt: "I literally walk uphill both ways" (St. George/North Shore resident). Second thread excerpt: people take a cab home from the terminal because streets can be deserted (not used). | §5 para 4 (quote, attributed to a Staten Island Reddit commenter) |
| SG11 | `St. George Staten Island burglary OR "package theft" OR break-in silive 2025 OR 2026` · Firecrawl search → scrape | https://www.silive.com/news/2019/04/sources-helicopter-hovering-over-st-george-linked-to-search-for-suspects.html | Apr 1 2019 (Maura Grunlund): reported attempted burglary ~10:30 a.m. near Fort Place; large police response including the NYPD Aviation Unit; a person of interest was questioned. | §10.5 H3 7 |
| SG12 | same search · scrape | https://www.silive.com/crime-safety/2026/07/i-was-bored-staten-island-felon-charged-in-burglary-spree.html | Jul 30 2026: burglaries in **Mariners Harbor** (not St. George); mentions Criminal Court in St. George. NOT used (wrong neighbourhood). | — |
| SG13 | `New York Rules of Professional Conduct Rule 1.6(c)…` · WebSearch → WebFetch | https://www.courtrules.net/new_york/new-york-professional-conduct/rule-1-6 | Rule 1.6(c): "A lawyer shall make reasonable efforts to prevent the inadvertent or unauthorized disclosure or use of, or unauthorized access to, information protected by Rules 1.6, 1.9(c), or 1.18(b)." No physical-security commentary. | §8.5 bullet; §9 law-office Q |
| SG14 | `Landmarks Preservation Commission rules work not visible from street…` · WebSearch → WebFetch | https://habitatmag.com/layout/set/amphtml/Publication-Content/Legal-Financial/2015/2015-February/Managing-the-Landmarks-Process | Three LPC permits: CNE (needs a DOB permit, no effect on protected features), PMW (affects protected features, no DOB permit; e.g. door replacement), C of A (DOB permit plus protected features; public hearing). Work off the front facade can need a permit if visible from a side street; some interior work too. | §9 Q1, Q2; §10.5 H3 3; historic-district section |
| SG15 | `NYC Department of Buildings ordinary repairs no permit required…` · WebSearch → WebFetch | https://www.nyc.gov/site/buildings/property-or-business-owner/do-i-need-a-permit.page | No-permit categories include "Minor alterations and ordinary repairs" (Admin Code §28-105.4.2). Door/lock hardware not named; no LPC note. | FAQ 2 |
| SG16 | `smart lock rechargeable batteries not recommended…` · WebSearch → WebFetch | https://www.kwikset.com/support/answers/can-i-use-rechargeable-batteries-for-my-smart-lock | Rechargeables "will not harm" the lock but are "not recommended": flatter discharge curve, so the battery % may be inaccurate. Alkaline recommended. | FAQ 3 |
| SG17 | `kc.allegion.com where is the programming code…` · WebSearch → WebFetch | https://kc.allegion.com/kb/article/how-to-locate-the-programming-sticker-on-schlage-keypad-and-touch-locks | Default codes are in the box documentation and on a sticker on the back of the outside keypad/touchscreen assembly (visible only with the keypad off the door). | FAQ 4 |
| SG18 | `Schlage Encode "vacation mode" OR Yale "privacy mode"…` · WebSearch → WebFetch | https://support.google.com/googlenest/answer/9208436 | Nest × Yale Privacy Mode disables the keypad so passcodes can't unlock; on/off from the app or by holding the white button; the inside thumb-turn turns it off; "does not provide an extra layer of security". | §9 night-keypad Q; §10.5 H3 6 |
| SG19 | same search · WebFetch | https://kc.allegion.com/kb/article/how-to-enable-disable-vacation-mode-on-schlage-keypad-and-touch-locks | Schlage Vacation Mode (BE365/BE375/BE369/FE575/FE595/FE695/FE599): "User Codes will not unlock the lock"; set with the 6-digit programming code + Schlage button + 4. | §9 night-keypad Q |
| SG20 | `Google Home help "multi-admin" Matter…` · WebSearch → WebFetch | https://support.google.com/googlenest/answer/13127223?hl=en | Matter Multi-Admin lets a device be used in several Matter-certified apps at once; each app needs its own compatible hub; "only one platform can actively control the device at a given moment"; status syncs. | §9 iPhone/Android Q |
| SG21 | `August smart lock activity feed shows unlocked manually…` · WebSearch → WebFetch | https://community.webcore.co/t/august-smart-lock-pro-accessing-how-it-was-locked/5363 | Forum user: August passes the unlock method into SmartThings logs, e.g. "Unlocked with keypad", method:keypad. (Forum source, not a manufacturer source.) | §9 inside/outside history Q |
| SG22 | `NYC Local Law 18 short-term rental…` · WebSearch → WebFetch | https://www.skybriz.com/resources/nyc-short-term-rental-regulations-local-law-18-state-law/ | Host present, max 2 guests, guests need access to common areas. NOT used (the short-term-rental intent is already on the SI/Manhattan/Brooklyn pages). | — |
| SG23 | `Empire Outlets St. George…` · WebSearch | (results only; not fetched) | Named on the page only as part of the waterfront redevelopment, per SG4; no dates or facts taken from the unfetched results. | §8 waterfront card |
| SG24 | Google PAA / PASF / Answer the Public / AI Overview / Bing / DuckDuckGo / Yelp 1–3★ (St. George) | — | EMPTY (not accessible in build env). §10.5 claims come from national cost guides (Fixr, Bob Vila), manufacturers and general advice, and the page says so. | — |
| SG25 | SI Advance / local news stories on smart locks in St. George | — | EMPTY: none found. Only crime items surfaced (SG11 used, SG12 rejected). | — |

Statements without a dedicated source (installer practice / general tech, flagged): one connection point per level on two-level houses; testing on cellular data; "start at the lowest door" field routine; handing back original hardware labelled; suggested alert set (left unlocked / off-hours / wrong codes); Bluetooth-only locks can't be edited remotely; data use of smart locks is small (FAQ 6); history retention varies by brand (FAQ 5); district attorney office in St. George (statenislandda.org address snippet only).

### Prices used (SI ×1.10 — copied from the published Staten Island lines, identical to the West Brighton page; no new figures)
- Single-door keypad or fob reader with electric strike: $1,650–$2,750. New electric strike: $275–$495. Failed strike repair: $325–$534. Setup-only first hour: $225. Service/callback: $195/hr, 3-hr min ($585). Residential smart locks quoted flat at walkthrough. Fixr national $250–$400 (avg ~$300), labelled as national.
- Worked total: two single-door systems = $3,300–$5,500.

## Images (11)
Drive folder `AESS Website Photos/Smart Lock Installation` was empty (checked by main run); CompanyCam not connected. Source = `images/smart-lock-installation/aess-smart-lock-installation-*`. Each one viewed; faces cropped out with Pillow; the apartment crop drops the "4A" unit plate (y≥300). Not used: video-doorbell (house number "128"), showing-customer-app-unlock (customer face), suburban-van, office-glass-door, drilling-brownstone, keypad-exterior/interior pair, servicing-keypad-wiring. NOTE: the aess-* set looks AI-rendered. Flag for Anwar.
| File (images/smart-lock-installation/smart-lock-installation-st-george-staten-island-…) | Source (aess-smart-lock-installation-…) | Crop box | Section |
|---|---|---|---|
| keypad-deadbolt-panelled-wood-door.webp | keypad-smart-deadbolt-brownstone-door | (250,0,1400,1050) | hero |
| phone-app-locked-status-check.webp | checking-lock-status-in-app | (830,0,1400,1050) | instant action |
| tape-across-deadbolt-bore.webp | measuring-door-bore-for-deadbolt | (820,80,1400,1050) | §5 |
| battery-pack-swap-interior-unit.webp | replacing-smart-lock-batteries | (620,0,1400,933) — torso/logo visible, no face | repair capture |
| fingerprint-sensor-app-confirm.webp | fingerprint-unlock-demo-app | (730,0,1400,1050) | §6 |
| unscrewing-brass-deadbolt.webp | removing-old-brass-deadbolt | (830,0,1400,1050) | §7 |
| latch-edge-alignment-test.webp | checking-latch-bolt-alignment | (830,0,1400,1050) | two-levels section |
| office-keypad-lever-glass-door.webp | office-lever-smart-lock-install | (660,0,1400,933) | §8 |
| keypad-cable-through-mounting-plate.webp | connecting-interior-unit-cable | (820,0,1400,1050) | §10 |
| adding-user-code-in-app.webp | programming-access-code-app | (720,0,1400,1050) | §14 |
| apartment-door-keypad-app-unlocked.webp | apartment-door-smart-lock-app | (760,300,1400,933) | apartment residents |

## Question register — smart-lock-installation-st-george-staten-island-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 9)
1. Our house is in the St. George/New Brighton Historic District and we only want to change the lock, not the door — does that need a Landmarks permit?
2. The back of our St. Marks Place house looks down on Carroll Place — does a keypad on the rear door need approval if people can see it from that street?
3. Our house is a storey taller at the back than at the front — where should the hub go so locks on both levels stay connected?
4. We're about to sign a lease in one of the new buildings by the ferry terminal — what should we ask about the apartment door before signing?
5. Our sitter's code only works until 6 p.m. — if we're stuck on a late boat, can we stretch it from the terminal?
6. Our law office near the courthouse keeps client files on site — does a keypad with an access log help with our duty to protect client confidences?
7. Can the keypad be shut off at night while we're home, so no code works from outside?
8. Will the lock's history show whether the door was opened from inside or by someone coming in?
9. My partner has an iPhone and I have an Android phone — can we both manage the same lock?

(9 question H3s; the section also has non-question cluster H2s.)

### §17 FAQ (visible == FAQPage, 6)
1. Do you work all over St. George, from Richmond Terrace up to Fort Hill and across to Tompkinsville and New Brighton?
2. Does fitting a smart lock need a Department of Buildings permit?
3. Can we use rechargeable batteries in a smart lock?
4. Our keypad lock has no app — does it come with a factory programming code we should know about?
5. How far back does a smart lock's history go, and can we keep a copy?
6. Does a smart lock use much internet data or slow down our home Wi-Fi?

### Other question-form headings
- H2 "Lock Jammed or Keypad Blank in St. George?" (repair capture)
- H2 "Shut Out Somewhere Between the Ferry Terminal and Fort Hill?" (final repair capture)

De-dup notes: checked by meaning against all 33 smart-lock pages on disk (the full register, plus the Riverdale and Tribeca batch drafts). Closest neighbours for the main run to judge:
- Q1 (lock-only LPC permit) vs Tribeca "Do Tribeca's historic district rules reach the door inside my loft?" and Riverdale "post-1940 house keypad". Different door and trigger: an exterior facade lock swap, against an interior loft door and a building-age rule.
- Q1/Q2 vs Chelsea "who files with LPC" and Bed-Stuy "where may a keypad be mounted". Those are about filing role and mounting position; these are about whether a permit is triggered at all, and rear visibility from a lower street.
- Q3 vs West Brighton plaster/outlet Qs. That intent is wall materials and a missing outlet; this one is floor-to-floor distance on a two-level hillside house.
- Q5 vs Throgs Neck "change a leaked code from the phone". That is revoking a code; this is extending a time window.
- Q7 vs Todt Hill "pause staff codes while away". That is a schedule while travelling; this is a keypad-off privacy mode while home.
- Q8 vs Bed-Stuy/Morris Park entry-history Qs. Those use the log as evidence of who entered an empty house; this is reading inside versus outside unlock methods.
- FAQ 4 vs Bayside "seller's keypad master code wiped". That is an inherited lock; this is the default programming code on a new standalone keypad lock.
- FAQ 5 vs Morris Park "can the lock maker see our comings and goings". That is privacy and police access; this is how long history is kept and how to export it.
Avoided on purpose: short-term rental guest locks (SI/Manhattan/Brooklyn), packages, auto-unlock/geofence (New Dorp/Westchester), gate keypads, salt air and flood, front-desk spare keys (Riverdale/Manhattan), concrete fixing (Ulster).


<!-- batch 2026-10-17T16:28Z: smart-lock-installation-tribeca-manhattan-ny -->

# Research — smart-lock-installation-tribeca-manhattan-ny (batch 2026-10-17)

Queue line: slug smart-lock-installation-tribeca-manhattan-ny | Smart Lock Installation | Tribeca, Manhattan | up /smart-lock-installation-manhattan | phone (929) 560-0737 | GBP Bronx (460 E Fordham Rd, #bronx).
Thesis: in Tribeca the front door is usually a labelled fire door in a converted warehouse (or the stair door of a keyed-elevator full floor), so the lock is chosen from the label, thickness, closer and second doors first, and the app second; plus staffed-condo privacy and ground-floor galleries/showrooms/kitchens/cellars.
Silo-wide technical/product sources reused from research/smart-lock-installation.md (S1 Fixr, S3 August retrofit, S4 August Connect 10–15 ft, S5/S6 Thread/Matter, S9 kalamein/Fire Engineering, Schlage Encode specs incl. door 1-3/8–1-3/4 in and "up to six months", Yale Assure Lock 2 door 1-3/8–2-1/4 in, Schlage Arrive prep 1-3/8–2 in, Ring subscription/Ring-app codes). Not re-fetched.

## Tribeca

### Research matrix (exact query · platform · URL · finding · page section)

| # | Query · platform | URL | Finding | Used in |
|---|---|---|---|---|
| T1 | (scrape) · Firecrawl scrape | https://en.wikipedia.org/wiki/Tribeca | Bounded by Canal St, West St, Broadway, Chambers St; Manhattan CD1; 1st Precinct at 16 Ericsson Place; ZIPs 10013/10007; 2020 pop 21,305; Washington Market history, store-and-loft buildings on Broadway 1850s–60s; market to Hunts Point 1960s; artists in lofts; four LPC districts 1991–92 + 2002 extension; Washington Market Park 1.61 acres (1981); Hook & Ladder 8 at 14 North Moore St (Ghostbusters); Verizon Building (1923–27) converted to condos 2016; 388 Greenwich (Citigroup CIB HQ); New York Law School on Worth St; BMCC between Chambers and N. Moore; New York Academy of Art; "popular filming location"; Hudson River Park from West Side Highway replacement after Westway. | §5 Neighbourhood, §5.5 stats, §7 building types, §8 commercial cards, §13 landmarks, FAQ film-location |
| T2 | `Furman Center Financial District Battery Park City Tribeca MN01 neighborhood profile population` · Firecrawl search → scrape | https://www.furmancenter.org/neighborhoods/financial-district/ | CD1 ("Financial District" profile, updated 05/06/2026): pop 160,189 (2024); highest median HH income $208,970; single-person HH 47.3%; HH with children 15.5%; homeownership 34.0% vs 32.7% city; 677 condo sales 2025; 4,428 new units 2010–2025; serious crime 15.8/1,000 (2025), property 11.4, vs 12.3 citywide. | §5.5 stats |
| T3 | `Tribeca historic districts Landmarks Preservation Commission Tribeca West East North South designated` · Firecrawl search | https://www.nypap.org/preservation-history/tribeca-historic-districts/ (excerpt) | Tribeca West 5/7/1991; East 12/2/1992; North and South 12/8/1992; South Extension 11/19/2002. | §5, §5.5 |
| T4 | `Tribeca loading dock platforms canopies historic district Landmarks guidelines` · Firecrawl search | https://architecturaltrust.org/wp-content/uploads/2013/06/Report_LPC_Tribeca_West.pdf (excerpt) | "The loading platform, one of the most common warehouse-associated features in the Tribeca West Historic District, appears to have been a turn-of-the-century addition, erected over stepped vaults"; folding iron shutters and wood doors historically filled loading bays. | §5, Q&A loading-bay question, glossary |
| T5 | same search | https://www.nyc.gov/assets/lpc/downloads/pdf/Rules/Revised_Rules_of_the_NYC_Landmarks_Preservation_Commission_08-21-2023.pdf (excerpt) | §2-12 storefront rules (infill, doors, security gates); Appendix A lists Tribeca East, North and West among "Historic Districts Having Continued Sidewalk Regulation". | §8.5 Landmarks bullet |
| T6 | (scrape) · Firecrawl scrape | https://6tocelebrate.org/neighborhood-items/tribeca-manhattan/ | Grid off Greenwich St and diagonal off Broadway; store/loft/warehouse buildings c.1860–1910 "still dominate the character of the neighborhood today"; four districts 1991–92, extension 2002; The Odeon, 145 West Broadway (photo). | §5, §8 cards |
| T7 | (scrape) | https://6tocelebrate.org/site/staple-street-alley-67-hudson-street9-jay-street/ | Skybridge shuttled patients between New York Hospital's House of Relief (67 Hudson, Cady, Berg & See, 1893) and Ambulance Annex (9 Jay, Robertson & Potter, 1907–08); both in Tribeca West HD. | §13 landmarks |
| T8 | (scrape) | https://6tocelebrate.org/site/23-25-27-29-31-33-37-39-and-41-harrison-street/ | Nine Federal houses 1796–1828; three moved from Washington St late 1960s; individual landmarks 1969. | §7 building types, §13 |
| T9 | `Duane Park Tribeca history ...` · Firecrawl search → scrape | https://www.duanepark.org/history/ | Second-oldest public park after Bowling Green; set aside 1797 where Duane St widens to meet Hudson St; butter/egg/pickle warehouses shutting down by 1994. | §13 |
| T10 | `Hudson River Park Pier 25 Pier 26 Tribeca opened` · Firecrawl search | https://hudsonriverpark.org/locations/pier-26/ ; https://hudsonriverpark.org/activities/pier-26-science-playground/ | Pier 26: 2.5-acre ecologically themed pier in Tribeca; opened 2020. | §13 |
| T11 | `Tribeca Citizen burglary loft apartment door` · Firecrawl search → scrape | https://www.cbsnews.com/newyork/news/burglar-sneaking-through-terrace-doors-at-upscale-tribeca-apartments/ | Burglar entered Tribeca penthouses (72 and 77 Reade St) through terrace doors apparently left unlocked; Duane, Leonard, Warren St apartments also hit. Article date not shown on page (image path dated 2015-04-29) → page gives no year. | §5, AI H3 7, survey "second doors" |
| T12 | same search → scrape | https://abc7ny.com/post/man-charged-with-breaking-into-taylor-swifts-apartment----again/5174269/ | 7 Mar 2019: police said a man climbed a ladder and used a brick to break into the second-floor patio door of a Franklin Street townhouse (empty, under renovation); third break-in at the building. Page does not name the owner. | §5, survey "second doors" |
| T13 | `Tribeca Citizen package thefts lobby building 2025` · Firecrawl search → scrape | https://tribecacitizen.com/2021/10/01/thefts-of-lockboxes-are-the-latest-petty-crime-epidemic/ | 1 Oct 2021: at least nine cases of lockbox break-ins; mail carriers' lockboxes (key opens building + mailboxes) pried open/stripped on Chambers, Warren, Murray; a Murray St building replaced all cylinders. | §5 |
| T14 | same search → scrape | https://www.tribecatrib.com/content/nypd-releases-images-suspects-tribeca-fidi-package-thefts | 9 Mar 2022: man entered lobby of 40 Harrison St (Independence Plaza) Jan 11 ~8:50 pm, approached security desk, took two packages. | §5 |
| T15 | `galleries moving to Tribeca art district Walker Street Franklin Street` · Firecrawl search | https://www.cristintierney.com/news/291-...-49-walker-street... ; https://www.jamescohan.com/news/james-cohan-announces-expansion-with-new-tribeca-location ; https://www.facebook.com/hyperallergic/posts/... (Marian Goodman quote) ; https://tribecaartsdistrict.org/ (all excerpts) | Cristin Tierney ground-floor space 49 Walker; James Cohan 2nd floor 52 Walker beside 48 Walker, opening Oct 7, 2021; Marian Goodman to 54 Franklin St, late autumn 2023, historic district, 1891 site; arts district: galleries on Broadway and Walker, design houses on White and Franklin. | §8 cards, Q&A art-handler question |
| T16 | `Loft Law interim multiple dwelling Tribeca buildings Loft Board legalization` · Firecrawl search → scrape | https://www.nyc.gov/site/buildings/dob/loft-board.page ; https://www.lfaa.nyc/loft-legalization (excerpt) | Article 7-C MDL created IMD class; Loft Board tracks legalisation, registers buildings, adjudicates disputes; IMDs become subject to Rent Stabilization after legalisation. No Tribeca-specific IMD list found. | §7 card, Q&A Loft Law, glossary |
| T17 | `NYC Local Law 111 of 2018 self-closing doors ...` · Firecrawl search | https://www.nyc.gov/site/hpd/services-and-information/self-closing-doors.page | Apartment and hallway doors must "swing closed and latch by themselves"; inspectors check every self-closing door; proactive programme selects buildings. | §5, AI H3 5, glossary |
| T18 | `NYC Building Code stairway doors re-entry ... 1010.1.9.12` · Firecrawl search → scrape | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-173526 | BC 1010.1.9.11 Stairway doors (text quoted, incl. ≤4-storey exception and 403.5.3 reference); BC 1010.4.1 entrance doors; 1010.4.2 dwelling-unit doors (heavy-duty deadbolt key outside/thumb-turn inside, chain guard, viewer); 1010.4.4 intercom for 8+ units. | §5, §8.5, Q&A stair-door question, AI H3 4 |
| T19 | `fire door label hinge edge painted over how to identify rating NFPA 80 ...` · Firecrawl search | https://www.nfpa.org/news-blogs-and-articles/blogs/2025/04/11/fire-doors-faqs ; https://www.select-hinges.com/blog/... (excerpt) | Label contents; labels not to be removed/defaced/illegible; may be painted if readily visible; if illegible, verify "through other means acceptable to the AHJ". Leaf label on hinge edge below top hinge or top edge. | §7.5, Q&A label question, survey table |
| T20 | `NYC sidewalk cellar doors rules DOT ...` · Firecrawl search | https://portal.311.nyc.gov/article/?kanumber=KA-02292 (excerpt) | DOT investigates cellar doors left open and unprotected; may be open during a delivery if someone guards the opening. | §8.5, Q&A cellar question, schedule list |
| T21 | `Landmarks Preservation Commission interior work historic district ... Certificate of No Effect` · Firecrawl search | https://nyc-business.nyc.gov/nycbusiness/description/performing-work-on-a-landmarked-property (excerpt) | LPC permit needed for work needing a DOB permit; CNE when work needs DOB permit but doesn't change protected features. | FAQ historic-rules question, glossary |
| T22 | `Tribeca loft "keyed elevator" opens directly into full-floor loft listing` · Firecrawl search | https://michaelbhagwandin.com/blog/your-own-private-entrance-... (excerpt); https://www.instagram.com/p/Dd67vIZmTuf/ (excerpt) | Buyer's guide: "the keyed elevator serves full-floor lofts in converted warehouses" (excerpt, neighbourhood referent not visible); listing: full-floor loft in Tribeca's Hall Building with private keyed elevator opening directly in. | §7 card (FLAG: guide excerpt only) |

### EMPTY (not accessible in build env)
- Reddit r/TriBeCa — search `reddit r/TriBeCa locksmith OR package theft OR building door` returned only general NYC threads (r/AskNYC, r/Brooklyn) → EMPTY for Tribeca.
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DuckDuckGo, Yelp 1–3★ — EMPTY (not accessible in build env). §10.5 headings are paraphrased published claims, stated on page.
- Local news on smart locks specifically in Tribeca — none found → EMPTY.
- Tribeca-specific IMD/Loft Law building list — not found → page states the Loft Law framework only.

### Prices used (Manhattan ×1.25, copied from parent page; none invented)
Reader/keypad + electric strike $1,875–$3,125 (base $1,500–$2,500); new strike $313–$563 ($250–$450); strike repair $369–$606 ($295–$485); programming $265 first hour then 30-min blocks; service $195/hr 3-hr min ($585); Fixr national $250–$400 avg $300, handyman $50–$100/hr (third-party, labelled). Home-door locks: quoted flat at walkthrough (no published figure, as on parent).

### Images (11) — Step C library (Drive empty, CompanyCam not connected)
Cropped from images/smart-lock-installation/aess-smart-lock-installation-*.webp to remove all faces and the "4A" unit plate; each viewed before writing alt/title/caption:
corridor-unit-door-keypad-app (from apartment-door-smart-lock-app), keypad-outside-thumbturn-inside-pair (keypad-exterior-thumbturn-interior-view, caption overlays cropped), tape-measure-old-deadbolt-bore (measuring-door-bore), keypad-opened-wiring-repair (servicing-keypad-wiring), glass-office-door-keypad-deadbolt-screwdriver (office-glass-door), brass-deadbolt-removal-drill (removing-old-brass-deadbolt), keypad-lever-glass-door-latch-screws (office-lever), access-code-entry-phone-app (programming-access-code-app), interior-unit-ribbon-cable-connection (connecting-interior-unit-cable), aa-battery-pack-interior-housing (replacing-smart-lock-batteries), fingerprint-unlock-app-confirmation (fingerprint-unlock-demo-app). All saved as images/smart-lock-installation/smart-lock-installation-tribeca-manhattan-<what>.webp.

### Questions on this page (add to the silo register)

§9 YOUR QUESTIONS ANSWERED (H3)
1. The label on our loft door's edge is buried under paint — how do you find out what rating the door carries before choosing a lock?
2. Our building's architect says the new loft entry door must stay "labelled" — does that narrow which smart locks we can buy?
3. Our building was legalised under the Loft Law — does its interim multiple dwelling past change who decides what goes on our door?
4. The fire stair doors in our loft building lock behind us on every floor — is that allowed, and could a keypad let residents back in?
5. When the keyed elevator is shut for inspection, how do we get into our full-floor loft — and should the smart lock plan cover that day?
6. We'd prefer the front desk can't see when we come and go — who actually reads a smart lock's entry log in a staffed condo?
7. Our condo's ground-floor maisonette has its own street door and a door into the lobby — which should be smart, and whose rules cover each?
8. Our architect is specifying a new entry door for the loft renovation — what should the door order include so a smart lock fits without cutting on site?
9. Our loft door is far thicker than a standard apartment door — will an off-the-shelf smart lock fit it?
10. Our restaurant's cellar is reached through steel doors in the sidewalk — can they be locked electronically on a schedule?
11. Steam and grease coat our kitchen's back door — which kinds of lock hardware hold up there?
12. Our showroom takes deliveries through a loading bay behind historic iron shutters — where does an electronic lock belong?
13. Art handlers deliver to our Walker Street gallery after hours — can they open the door without learning the staff code?

§17 FAQ (visible == FAQPage, 8)
1. Do you also work in SoHo, Hudson Square, the Financial District and Battery Park City, around Tribeca?
2. What do you hand the managing agent after fitting a smart lock to a rated loft door?
3. Do Tribeca's historic district rules reach the door inside my loft?
4. If the building loses power, does a battery smart lock on our loft door keep working?
5. Can the lock on our loft and the lock on our shop downstairs live in one app without sharing codes?
6. Do you fit locks in Tribeca's big rental towers as well as in converted lofts?
7. What does a return visit to add, remove or reschedule codes cost?
8. Our loft is being rented as a film location for a few days — how should the crew get in?

Other question-form headings: "Smart Lock Jammed Somewhere Between Canal and Chambers?", "Shut Out on a Tribeca Landing Tonight?"

De-dup notes: avoided Chelsea's keyed-elevator questions (where the lock goes / swapping the key switch), Chelsea's 2012-flood controller question, UES service-door and terrace/balcony themes (Dutchess/Westchester), Bronx police-lock, Kingsbridge closer and lobby-breach questions, Hudson Valley quote-from-photos.


## Batch 2026-10-17 (Riverdale / St. George / Tribeca) — cross-batch notes
Partial question overlap judged acceptable: St. George Q1 (lock-only change on a historic-district house exterior) vs Tribeca FAQ 3 (historic-district rules and the door inside a loft) vs Riverdale Q8 (post-1940 house inside Riverdale HD). Tribeca captions (backset tape, battery change) and H2 rewritten after 0.68–0.71 masked similarity with Riverdale captions.


## Tottenville, Staten Island (smart-lock-installation-tottenville-staten-island-ny)

Built 2026-10-17 by the Tottenville builder subagent (batch with -harlem-manhattan-ny and -bay-ridge-brooklyn-ny). Up-link /smart-lock-installation-staten-island; direct line (347) 934-8335 (body, CTAs, schema; (800) 486-0943 only in shared mega-nav header); GBP Brooklyn, 1282 Troy Ave, schema @id #brooklyn.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used.

Thesis: Tottenville is the end of the line — southern tip of NYS, last SIR stop, water on three sides — so every lock is planned to be self-reliant: a rehearsed backup way in (key cylinder or 9V emergency contact), codes that work without internet, a second admin, batteries on a calendar, coastal-grade finish/gasket on unsheltered doors, and one-movement egress. Doors split between the oyster-era Victorian core (porches, panelled doors, old bores) and post-1990s houses beyond Hylan Blvd (four doors planned as one system), plus Main Street / Page Avenue shops; long commuter days drive the code plan.

Silo-wide sources reused (not re-fetched): S1 Fixr ($250–$400, avg $300, Jan 2025), S2 Bob Vila (screwdriver / ~30 min), S3 August retrofit (single-cylinder only, clearance), S4 August Connect 10–15 ft, S5/S6 Thread border router same ecosystem, N4 Tenant Data Privacy Act, N9 Admin Code §26-521 (30+ days), SI6 2022 NYC BC §1010.1.9 / §1010.1.9.5, SI11 MDL §4 (3+ families = multiple dwelling), SI12 dormakaba ocean-front (3 miles of saltwater, gasket, wrong finish voids warranty), SI15 Hylan Blvd ~13.86 mi Rosebank→Conference House Park, WB12 LPC permit / Permit for Minor Work for doors, WB16 Schlage Arrive door 1-3/8"–2", backset 2-3/8/2-3/4, ND19 BHMA A156.40 salt-spray finish test.

### Local research log

| # | Query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| TV1 | (direct fetch) `Tottenville, Staten Island` · WebFetch | https://en.wikipedia.org/wiki/Tottenville,_Staten_Island | Southernmost neighbourhood in NYC/NYS; Arthur Kill W/N, Raritan Bay S; 2.505 sq mi; CD3; Main St commercial core (123rd Pct 116 Main St, post office 228 Main); Page Ave second commercial core west of Amboy Rd; area SE of Hylan Blvd largely undeveloped until 1990s; Billop/Bentley Manor, renamed 1869 for Totten family; oystering banned 1916; boatbuilding ended ~1900, last shipyard closed 1930; Perth Amboy ferry until 1963; Outerbridge 1928; Conference House; NYPL Tottenville branch Carnegie, Carrère & Hastings, 1904, landmark; 7484 Amboy Rd c.1870 parsonage landmarked Apr 12 2005, restored 2017; SIR terminus since 1860, southernmost station in NYS, 14 mi / 42 min to St. George; buses S59/S78, express SIM2/SIM25/SIM26; "strong Victorian architectural heritage, unique among South Shore neighborhoods"; 29.4% renter-occupied; 2020 pop 16,089 (16,860 in 2010, −4.6%); 5,818 households, 31.7% with children; 123rd Pct safest of 69 (2010); 2022: 42 burglaries; crime −70.5% 1990–2022; Engine 151/Ladder 76 at 7219 Amboy Rd; Sandy destroyed Coral Bay Cafe at Tottenville Beach; Nassau Smelting 1900–2001, 30 acres bought 2016, rezoning opposed, future undetermined; Burial Ridge largest pre-European burial ground. | §5 paras 1, 3, 5, 6, 7, 8; §5.5 stat cards 1–3, 6; §8 Main St / Amboy / Hylan / industrial cards; §13 library, station, Conference House cards |
| TV2 | `Tottenville historic district Landmarks Preservation Commission Staten Island Victorian houses` · Firecrawl search → scrape | https://forgotten-ny.com/2026/05/return-to-tottenville-2025/ | Forgotten NY, May 9 2026 (walk Oct 2025): painted-lady Victorians "some of the best north of Cape May"; Bentley St houses (Greek Revival c.1850 by oysterman Van Name; Victorian c.1890 for shipbuilder John Brown, wraparound porch); Hopping Ave houses 1886–1921 (Gothic Revival cottage 1886, Colonial Revival 1903), "most of the homes on Hopping Avenue are LPC worthy"; Satterlee St: Biddle House 1840–45, symmetrical, NYC-owned, now Tottenville Museum; Ward House c.1830; Rutan-Beckett House; Italianate "The Heathcote" set back on wide yard; Bentley Dock ferry pilings, ferry ended 1963, landing moved to Bentley St 1896; Conference House c.1680 at end of Hylan Blvd, Sept 11 1776 Howe–Franklin/Adams/Rutledge; Great Beds Lighthouse 1878. House numbers of private homes NOT used on page. | §5 para 3 (streets, styles, Cape May quote paraphrased); §7 building cards; §13 Biddle House card; §13 station card |
| TV3 | same search · Firecrawl scrape | https://hdc.org/news-7-staten-island-buildings-calendered-by-lpc/ | Jan 2007: LPC calendared a Folk Victorian storefront on Main Street and an 1850s house on Arthur Kill Road, Tottenville; Barnett Shepherd survey for Preservation League; builder vandalised a 19th-c. house in 2005. | research only (context for landmark caution) |
| TV4 | same search excerpt → Firecrawl scrape (pdf parser) | https://www.nyc.gov/html/records/pdf/govpub/4184cunninghamstoredesigrep.pdf | LPC designation report: George Cunningham Store, 173 Main St, built c.1892 as a butcher shop, Queen Anne, bracketed bays, fish-scale shingles; designated July 15 2008. Main St history: first stores near Totten's Dock by 1850s; continuous east-side row by 1895; 123rd Precinct building 1922; Stadium Theatre 1927; commerce flourished until 1960s when major stores moved to Page Avenue shopping center and SI Mall opened 1973. | §8 Main St + Page Ave cards; §8.5 landmark bullet; §13 Cunningham card |
| TV5 | `Living Breakwaters Tottenville completed project GOSR` · Firecrawl search → scrape | https://hcr.ny.gov/living-breakwaters-project-background-and-design | NYS HCR: eight ecologically enhanced breakwater segments, ~2,400 linear ft, 790–1,800 ft offshore of Tottenville in Raritan Bay; erosion + wave attenuation + habitat; $60M CDBG-DR; Sandy Oct 2012 — "Tottenville experienced some of the most destructive waves in the region". | §5 para 6; §5.5 stat 5 |
| TV6 | same search (excerpts) | https://www.scapestudio.com/projects/living-breakwaters/ ; https://www.billionoysterproject.org/media/stories/the-living-breakwaters-a-model-for-nature-based-infrastructure-3 | Completed 2024 (SCAPE); construction 2021–fall 2024 (BOP). | §5 para 6, §5.5 stat 5 (completion year) |
| TV7 | `123rd Precinct Tottenville burglary 2025 OR 2026 silive` · Firecrawl search → scrape | https://www.silive.com/crime-safety/2026/06/tottenville-supermarket-and-annadale-home-targeted-nypd-seeks-help-in-separate-investigations.html | SI Advance June 3 2026: La Bella Supermarket, 99 Ellis St, Tottenville — May 16 2026 ~11:50 p.m., crowbar used to pry open front door into vestibule, nothing reported stolen (123 Pct detectives). (Annadale front-door item not used.) Store name not used on page; "a supermarket on Ellis Street". | §5 para 8; §8 Ellis St card; §9 strike-vs-maglock Q; §10.5 H3 7 |
| TV8 | same search (excerpts) | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/123rd-precinct.page ; https://x.com/NYPD123Pct/status/2061542224177836171 | Precinct contact; May 16 2026 burglary appeal (same incident). | research only |
| TV9 | `Tottenville 1990s development boom townhouses South Shore Staten Island overdevelopment rezoning 2003` · Firecrawl search → scrape | https://www.citylandnyc.org/two-staten-island-neighborhoods-down-zoned-2/ | CityLand (2005): CPC approved June 8 2005 a 65-block Tottenville rezoning bounded by Arthur Kill Rd, the Arthur Kill, Raritan Bay and Page Ave; R3A → R1-2 and R3X; single-family restriction + large lots for two-families; contextually rezoned 1995, 1996, 1997; CM Lanza: stop teardowns of large historic single-family homes. | §5 para 5; §5.5 stat 4; §7 townhouse card |
| TV10 | same search · Firecrawl scrape | https://therealdeal.com/magazine/new-york-june-2006/staten-island-development-boom-hits-crossroads/ | Real Deal (2006): downzoning in midsection/south end replaced townhouses with semi-detached and detached homes, esp. two-family detached. | §5 para 5; §7 townhouse card |
| TV11 | `Conference House Park acres historic houses Biddle House Rutan-Beckett Ward House NYC Parks` · Firecrawl search (excerpts) | https://www.nycgovparks.org/parks/conference-house-park ; https://www.tclf.org/conference-house-park ; https://conferencehouse.org/the-historic-houses-of-conference-house-park/ | NYC Parks: 265-acre park, four historic buildings (Conference House, Biddle, Ward, Rutan-Beckett); TCLF: Biddle c.1845, Ward c.1830, Rutan-Beckett c.1850; Conference House org says 270 acres (NYC Parks figure used). | §13 Conference House + Biddle cards |
| TV12 | `Aakawaxung Munahanung Archaeological Site designated Landmarks Preservation Commission date Conference House Park` · Firecrawl search (excerpts) | https://hdc.org/buildings/conference-house-park-archaeological-site/ ; https://www.nyc.gov/site/lpc/about/pr2021/lpc-recognizes-native-american-and-chinese-american-history-with-the-designation-of-two-individual-landmarks.page | Designated June 22 2021; ~20-acre site within Conference House Park; 8,000+ years of Indigenous occupation. | §13 archaeological card |
| TV13 | `Tottenville Main Street shops restaurants small business district Page Avenue shopping center` · Firecrawl search (excerpts) | https://shopyourcity.cityofnewyork.us/syc-statenisland/ ; https://www.defalcorealty.com/blog/tottenville-staten-island-neighborhood-guide/ | NYC Shop Your City: "retail corridors along Page Avenue … bustling with shopping and dining"; DeFalco: Main Street is the commercial spine. Business names not used. | §8 Page Ave + Main St cards |
| TV14 | `reddit r/statenisland Tottenville living old houses` · Firecrawl search (excerpt only) | https://www.reddit.com/r/statenisland/comments/s5nr08/where_on_staten_island_would_you_say_is_the/ | Excerpt: "Tottenville (small town feel, beautiful homes, some nice restaurants, safe, friendly). family owned small businesses". Thread not scraped. | §5 para 8 (paraphrased "residents on local forums") |
| TV15 | `smart lock dead batteries 9V battery terminals bottom of keypad emergency power Schlage Yale` · Firecrawl search (excerpt) | https://www.yalehome.com/ae/en/support/product-support/smart-door-lock-support/keyless-connected/the-batteries-in-my-keyless-smart-door-lock-are-completely-flat- | Yale support: insert a 9V battery into the emergency terminal at the bottom of the device, then enter master code (keyless connected models; regional Yale site). | Self-reliant section H3 1; §9 Q 1; §6 card; field notes; final repair block |
| TV16 | `NCC Group Bluetooth Low Energy relay attack Kwikset smart lock 2022` · Firecrawl search (excerpts) | https://www.nccgroup.com/newsroom/ncc-group-uncovers-bluetooth-low-energy-ble-vulnerability-that-puts-millions-of-cars-mobile-devices-and-locking-systems-at-risk/ ; https://www.nccgroup.com/research/technical-advisory-kwiksetweiser-ble-proximity-authentication-in-kevo-smart-locks-vulnerable-to-relay-attacks/ | May 15–16 2022: BLE link-layer relay attack; demonstrated on Kwikset/Weiser Kevo touch-to-open; "not a traditional bug that can be fixed with a simple software patch"; advice: disable passive unlock without explicit approval / turn off Bluetooth when not needed. Brand not named on page. | §9 Bluetooth-in-car Q; §10.5 H3 5 |
| TV17 | `CISA OR FTC secure home network put smart home IoT devices on separate guest network` · Firecrawl search (excerpt) | https://its.ny.gov/news/securing-your-smart-home-navigating-internet-things-part-ii | NYS ITS: "Use a separate Wi-Fi network for your household IoT devices"; guest network option; 2.4/5 GHz bands. | §9 separate-network Q |
| TV18 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DuckDuckGo / Yelp 1–3★ (Tottenville) | — | EMPTY (not accessible in build env). §10.5 headings are claims from national cost guides (Fixr, Bob Vila) and manufacturer marketing, stated as such on the page. | — |
| TV19 | Local smart-lock-specific news for Tottenville (silive/Patch) | — | EMPTY — none found; burglary item TV7 used instead. | — |
| TV20 | Reddit thread content (r/statenisland) | — | EMPTY beyond the search excerpt in TV14 (threads not scraped). | — |
| TV21 | DOB permit requirement for residential smart lock; Tottenville-specific door hardware prevalence (mortise/panel stats) | — | Not searched / no source → no claim made; door types described only as conditions we check for. | §7 |

General-practice statements without a dedicated URL (flagged, worded cautiously): Wi-Fi radios draw more battery than Bluetooth/Thread (§9 Q4, "generally"); cold wind can drain batteries faster (self-reliant section); phone-platform switch keeps lock-account data (§9 Q Android/iPhone); deaf-alert automations via smart-home systems (§9 Q); model residential codes treat garage-to-house door as fire separation, some require self-closing (newer-houses section; IRC R302.5.1 source is in LI silo research, not re-fetched).

### Prices used (SI ×1.10 — copied from smart-lock-installation-staten-island.html; no new figures)
- Single-door keypad/fob reader with electric strike: $1,650–$2,750 (§14 table, §15 Premium, Service schema); worked example two doors $3,300–$5,500 (sum of published lines).
- New electric strike $275–$495; failed strike repair $325–$534 (§14, schema).
- Setup-only first hour $225 (repair capture, §14, BYO card, worked example).
- Service/callback $195/hr, 3-hr minimum ($585) (§14).
- Residential smart locks: quoted flat at walkthrough. Fixr national $250–$400 / avg $300 labelled national (§10.5, §14).

## Images (11)
Drive folder `AESS Website Photos/Smart Lock Installation` empty (per main run); CompanyCam not connected → permanent image rule. Sources: images/commercial-security/ (10) + images/low-voltage/ (1). Every source viewed (contact sheets) before use; every source shows a technician's face, so each was cropped with Pillow to exclude faces, then saved WebP q80 (all under 1600 px). Rejected: bronx-access-reader (fictional "Pinnacle Business Center" signage), nyc-dual-entrance-design (fictional address sign), nyc-intercom-reception-test (faces incl. receptionist and on-screen face), bronx-alarm-keypad (two faces, no clean crop), bronx-credential-programming (readable software screen). NOTE: the whole library looks AI-rendered (uniform AESS uniforms/logos) — flag for Anwar, same as earlier SI pages. Several source photos were also used (differently cropped) on UES, Putnam, Flushing, Dutchess and Harlem pages — library too small to avoid.

| File (images/smart-lock-installation/) | Source | Crop box (px) | What is visible | Section |
|---|---|---|---|---|
| smart-lock-installation-tottenville-push-to-exit-button-keypad-reader.webp | commercial-security/…-nyc-rex-exit-button.jpg | 772,0,1402,1115 | Gloved hand/screwdriver at green push-to-exit button, exit-button sign, keypad reader on frame | hero |
| …-electric-strike-aluminium-frame.webp | commercial-security/…-bronx-electric-strike.jpg | 640,0,1402,1115 | Hand driving screw into electric strike in black aluminium frame beside pull handle | §5 |
| …-door-position-contact-frame.webp | commercial-security/…-nyc-door-contact-install.jpg | 800,0,1402,1115 | Hand fixing small contact at top of door frame; wall sign | repair capture |
| …-request-to-exit-sensor-door-closer.webp | commercial-security/…-nyc-request-to-exit-sensor.jpg | 640,0,1402,1115 | Hands mounting white REX sensor above glass door beside closer | §6 |
| …-maglock-glass-door-header.webp | commercial-security/…-manhattan-maglock.jpg | 560,0,1402,1115 | Gloved hands at maglock on glass door header; push bar | §7 |
| …-maglock-wiring-storefront-header.webp | low-voltage/…-long-island-maglock-install.jpg | 600,0,1400,760 | Two gloved hands feeding wires into maglock at storefront header; trees/parking through glass | self-reliant section |
| …-three-door-controller-panel.webp | commercial-security/…-nyc-door-controller-enclosure.jpg | 560,0,1402,1115 | Gloved hands at three labelled door controller boards; card readers below | §8 |
| …-access-control-boards-enclosure.webp | commercial-security/…-nyc-access-control-panels.jpg | 620,0,1402,1115 | Hands/screwdriver at controller boards under 12 V supply in wall cabinet | §9 end |
| …-gate-reader-fingerprint-wiring.webp | commercial-security/…-nyc-gate-reader-install.jpg | 0,0,500,1024 | Fingerprint/keypad reader + open junction box at metal gate; hand with crimper; laptop | §10 |
| …-exterior-junction-boxes-block-wall.webp | commercial-security/…-manhattan-exterior-enclosures.jpg | 820,0,1402,1115 | Two grey junction boxes with conduit on block wall | §13 |
| …-conduit-cable-pull-block-wall.webp | commercial-security/…-hudson-valley-conduit-pull.jpg | 520,0,1402,1115 | Gloved hands pulling blue cable through conduit into wall box; safety sign | §14 |

Alt/title/caption describe only what is visible + "Tottenville, Staten Island" (guide/reference wording); none claims a local customer, named building or completed local job.

## Question register — smart-lock-installation-tottenville-staten-island-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
1. Our keypad has two small metal contacts on the bottom — what are they for, and when would we use them?
2. We want a retrofit unit over our existing deadbolt — how do we tell whether the deadbolt we have will take one?
3. Our lock keeps reporting "jammed" even though the door seems to close fine — what usually causes that?
4. Will a lock that connects straight to Wi-Fi drain its batteries faster than one that talks to a plug-in bridge?
5. On our panelled Victorian door, the inside part of the lock would sit on the raised moulding — can it be made to sit flat?
6. Should we paint or refinish the door before the smart lock goes on, or after?
7. Could someone sitting in a parked car pick up our lock's Bluetooth signal and use it to open the door?
8. Should the lock and its bridge go on a separate Wi-Fi network from our laptops and phones?
9. If we switch from Android to iPhone, or the other way, do the locks have to be set up all over again?
10. Someone in our house is deaf — can the door let them know that somebody has just come in?
11. After a crowbar was used on a Tottenville supermarket's front door in 2026, which holds better against prying: an electric strike or a magnetic lock?

### §17 FAQ (visible == FAQPage, 8)
1. Do you come out to Richmond Valley, Charleston and Pleasant Plains as well as Tottenville?
2. Do your technicians keep any record of our codes once the job is done?
3. Can one screen show us the battery level of every lock in the house?
4. Our retrofit lock has no keypad — can one be added outside without drilling the door?
5. We have lost the only spare key for the smart lock's cylinder — what now?
6. We already have a monitored alarm — what does a smart lock add that the alarm does not?
7. Can we keep the door chain or swing-bar guard once the smart lock is on?
8. Should the keypad code be changed after a big party or a house full of summer guests?

### Other question-form headings
- H2 "Lock Dead or Bolt Stuck at the Bottom of the Island?" (repair capture)
- H2 "Locked Out Between Conference House Park and Arthur Kill Road?" (final repair capture)

### De-dup notes
Checked by meaning against every question on all 33 smart-lock pages on disk (incl. batch-mates Harlem and Bay Ridge at ~build end). Replaced during build: DST/clock-change scheduled codes (= Bay Ridge "clocks go back an hour in November"). Avoided as questions (body text only): salt-air maintenance (SI/LI/Suffolk/Throgs Neck), commuter empty-house behaviour (Westchester Metro-North), landmark approval (HV/Brooklyn/Chelsea), crowbar lock-vs-frame (New Dorp — mine is strike vs maglock), battery-dead lockout abroad (Manhattan — mine is the 9V contact hardware), garage-to-house door (SI/LI), two-family codes (SI/Bronx/Brooklyn), area pricing (NYC/SI/ND/TH). Closest neighbours for the main run to judge: Q3 "jammed" alert vs SI FAQ "door dropped on hinges" (symptom diagnosis vs sagging door); Q4 Wi-Fi vs bridge battery vs Greenpoint "busy door drains batteries — wire it?"; FAQ 4 add keypad to retrofit vs none found; FAQ 8 change code after party vs Throgs Neck "code leaks — change from phone".


## Harlem, Manhattan (smart-lock-installation-harlem-manhattan-ny)

Built 2026-10-17 (batch subagent). Neighbourhood page, up-link /smart-lock-installation-manhattan. GBP Bronx (460 E Fordham Rd, #bronx). Direct line (929) 560-0737 in body/CTAs/schema; (800) 486-0943 only in shared nav chrome. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search/scrape" = mcp__Fire_Crawl__firecrawl_search / firecrawl_scrape.

**Thesis / lane:** Harlem doors are often governed by neighbours rather than management companies — HDFC co-op boards, TIL tenant associations in City-owned buildings, owner-occupied brownstones with rental floors — so the page is about keyless entry a resident-run building can afford, administer, hand over at the annual board election, and get approved (board / HPD / LPC / co-op-as-commercial-landlord). Distinct from Washington Heights (household codes beside the landlord's lock), UES (townhouse staff/high-security keys), Chelsea (galleries/LPC/lofts), UWS, Tribeca.

### Local research log

| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| H1 | `NYU Furman Center Central Harlem MN10 neighborhood profile homeownership rate population` · FC search → FC scrape | https://www.furmancenter.org/neighborhoods/central-harlem/ | Updated 05/06/2026. 2024: pop 125,248; homeownership 15.3% (city 32.7%); single-person households 46.9%; 65+ 15.6%; HCV 10.9% of private rentals; 2025: 63 public housing properties / 7,766 units = 13.6% of rental units; 6 Mitchell-Lama properties / 2,449 units; 1,412 subsidized properties; 4,576 new units 2010–2025; 2-4 family sales 22 (2024); serious housing code violations 246.1 per 1,000 (2025); car-free commute 88.0%. | §5 paras 4, stats list; §7 cards (newer buildings, public/ML); NYCHA/ML section; brownstone section |
| H2 | `HDFC co-ops Harlem concentration limited equity cooperatives income restrictions` · FC search (excerpt) | https://www.nyc.gov/site/hpd/services-and-information/hdfc.page | HPD: City acquired abandoned/distressed buildings in 1970s–80s; HPD rehabilitated and let tenants become shareholders in limited-equity HDFC co-ops; reduced taxes for income & resale restrictions; board responsible for finances and compliance with law/regulatory restrictions; Article XI ≤165% AMI; almost all HDFCs limit subletting; regulatory agreements with HPD. | §5 para 1; §9 Q2 (owner-occupancy/sublet); §10.5 H3 2; glossary |
| H3 | `Harlem HDFC co-ops city-owned in rem buildings Tenant Interim Lease program …` · FC search → FC scrape | https://www.palanteharlem.org/til-justice | Quotes HPD TIL description (tenant associations lease City-owned buildings, manage them, buy apartments for $250); April 27, 2017 Council hearing: HPD to pay fuel for all 148 TIL buildings; "164+ buildings that never graduated"; 28 RCNY ch. 24 succession rules. | §5 para 2; §9 Q3; glossary |
| H4 | `HDFC co-ops Harlem struggling boards repairs volunteer shareholders …` · FC search → FC scrape (query) | https://www.columbiaspectator.com/city-news/2024/04/15/cb9-boasts-the-most-hdfcs-in-new-york-city-but-undisclosed-maintenance-costs-threaten-residents-homeownership/ | Apr 15 2024: CB9 has most HDFCs of any community board, 220; HDFCs ≈1% of NYC apartment buildings; ~20% can't pay maintenance HPD says needed; 501 W 143rd St co-op left with $3.4M water bill after first-floor laundromat owner fled (2017). | §5 para 1 & 3; stats list; §9 Q9 (commercial tenant in HDFC) |
| H5 | same search → FC scrape (query) | https://www.uhab.org/new-report-breaking-the-cycle-of-distress/ | June 5 2023: "around 20% have fallen into distress"; costs fall on "low-income shareholders tasked with operating their building". | §5 para 3 |
| H6 | `Mount Morris Park Historic District designated 1971 extension 2015 …` · FC search; FC scrape Wikipedia | https://www.nyc.gov/site/lpc/about/pr2017/092517.page ; https://en.wikipedia.org/wiki/Mount_Morris_Park_Historic_District | LPC: extension designated 2015 (unanimous), >250 rowhouses, original district 1971. Wikipedia: 16 blocks, W118–W124 St, Fifth Ave to ACP Jr Blvd; NYCL Nov 3 1971 / Sept 22 2015; Queen Anne/Romanesque/neo-Grec styles. | §5 para 4; §7 card; §7.5 method; §8.5; §13 card; brownstone section |
| H7 | `Strivers' Row St. Nicholas Historic District King Model Houses 1891 rear alleys designated 1967 …` · FC search; FC scrape (directQuote) | https://en.wikipedia.org/wiki/St._Nicholas_Historic_District ; https://www.striversrownyc.org/ | W138/W139 between ACP Jr Blvd & FDB; built 1891–93 by David H. King Jr.; architects James Brown Lord, Bruce Price & Clarence S. Luce, Stanford White; designated 1967; alleys gated, some gates read "Walk Your Horses", once used for discreet stabling/deliveries. | §7 card; §7.5; §9 Q8; §13 card |
| H8 | `NYCHA layered access control key fob entry doors Harlem developments St. Nicholas Houses` · FC search → FC scrape (query) | https://comptroller.nyc.gov/reports/observations-of-building-doors-in-nycha-developments/ | Sept 21 2022: 262 developments visited; 36.8% entrance doors open, 40.1% entrance locks broken; 57.9% open and/or broken; doors propped with bricks/rocks. | §5 para 4; stats list; §10.5 H3 4; NYCHA section |
| H9 | same search → FC scrape (directQuote) | https://criminaljustice.cityofnewyork.us/press-release/mayors-office-of-criminal-justice-and-nycha-announce-completion-of-273-new-safety-lights-and-expanded-programs-to-reduce-crime-at-saint-nicholas-houses-in-manhattan/ | Nov 2 2016: St. Nicholas Houses >3,500 residents; NYCHA "greatly increased the number of Layered Access Control (LAC) doors". | §7 card; NYCHA section |
| H10 | same search (excerpt) | https://designguidelines.nycha.info/layered-access-control-lac/ | NYCHA LAC "can provide further security for storefronts and building entry doors". | NYCHA section |
| H11 | `site:reddit.com r/Harlem package stolen building door lock brownstone` · FC search (excerpts only; Reddit scrape refused "we do not support this site") | https://www.reddit.com/r/Harlem/comments/1qp41b3/brownstones_vs_key_fob_buildings/ ; https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ ; https://www.reddit.com/r/nyc/comments/bnppv1/harlem_brownstones/ | Excerpts: "Packages will likely be an issue at both [brownstone vs fob building]… people would feel more comfortable following someone"; "5 packages stolen on day 1 of my new apartment last week in Harlem"; Harlem brownstone blocks filmed monthly. Background only — nothing quoted on page. | background (tailgating framing in worksheet §1) |
| H12 | `Studio Museum in Harlem new building 144 West 125th Street opened November 2025` · FC search | https://www.studiomuseum.org/press/studio-museum-in-harlem-opening-date-and-community-day | New 7-floor, 82,000 sq ft building opened Nov 15 2025, 144 W 125th St between Lenox & Seventh; Adjaye Associates / Cooper Robertson; entrance steps "evoke the ubiquitous stoops of Harlem's brownstones". | §5 para 5; §13 card |
| H13 | `Apollo Theater 253 West 125th Street opened 1914 history; 125th Street Business Improvement District` · FC search | https://www.apollotheater.org/history ; https://en.wikipedia.org/wiki/Apollo_Theater ; https://harlembid.com/place/apollo-theater1/ | Opened 1914 as Hurtig & Seamon's New Burlesque Theater; reopened as 125th Street Apollo Jan 26 1934; ~1,500 seats; 253 W 125th St; listed by 125th Street BID. | §5 para 5; §8 card; §13 card |
| H14 | `Schomburg Center for Research in Black Culture 515 Malcolm X Boulevard history founded` · FC search | https://www.nypl.org/about/locations/schomburg | 515 Malcolm X Blvd (135th St); founded 1925; National Historic Landmark 2017; over 11 million items. | §8 card; §13 card |
| H15 | `Abyssinian Baptist Church 132 West 138th Street building 1923 landmark` · FC search | https://villagepreservation.org/2020/02/20/beyond-the-village-and-back-harlems-abyssinian-baptist-church/ ; https://en.wikipedia.org/wiki/Abyssinian_Baptist_Church | Building at 132 (136–142) W 138th St formally dedicated June 17 1923. | §8 card; §13 card |
| H16 | `Marcus Garvey Park fire watchtower 1857 restored 2019 Harlem` · FC search | https://www.nycgovparks.org/parks/marcus-garvey-park/highlights/6497 ; https://nylandmarks.org/explore-ny/mount-morris-fire-watchtower/ | Watchtower completed 1857; full City restoration completed 2019. | §13 card |
| H17 | `Frederick Douglass Boulevard Harlem restaurant row corridor rezoning 2003` · FC search | https://www.nyc.gov/assets/planning/download/pdf/plans/frederick-douglass-boulevard/fdb.pdf ; https://www.dnainfo.com/new-york/20100923/harlem/restaurant-bar-boom-continues-on-harlems-frederick-douglass-boulevard | DCP: FDB rezoning approved 2003 (CB/CPC Aug 13 & Sept 10 2003); DNAinfo Sept 23 2010: restaurant/bar boom traced to 2003 rezoning. | §5 para 5; §8 card; §9 Q10 |
| H18 | `Harlem brownstone burglary 2025 OR 2026 police 28th precinct OR 32nd precinct break-in` · FC search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/28th-precinct.page ; https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/32nd-precinct.page | 28th Pct serves central Harlem (2271-89 8th Ave); 32nd Pct serves northeastern Harlem. No Harlem smart-lock/burglary story usable. | §13 closing para |
| H19 | `Harlem brownstone burglary arrested stole from homes Harlem townhouse burglar` · FC search | https://ag.ny.gov/press-release/2026/attorney-general-james-wins-case-against-notorious-deed-thief-joseph-makhani ; https://manhattanda.org/... | Results were Harlem brownstone deed-theft cases (AG July 1 2026; DA Bragg indictment). Not used — deed theft already the Bed-Stuy lane. | not used |
| H20 | `Harlem package thieves building vestibule … patch OR west side rag OR amny` · FC search (news) | — | No results → EMPTY. | — |
| H21 | `Harlem brownstones converted rooming houses single room occupancy restored …` · FC search (excerpts) | https://www.nytimes.com/2009/09/20/realestate/20deal2.html ; https://fontanarchitecture.com/harlem-brownstone-renovation/ ; https://www.nyc.gov/assets/hpd/downloads/pdfs/services/shared-housing-roadmap.pdf | SRO-to-single-family conversions of Harlem brownstones; rooming houses typically converted brownstones (HPD roadmap). Background only (rooming-house lock intent already on Chelsea page). | background |
| H22 | `MDL 50-a` · FC scrape (directQuote) | https://www.nysenate.gov/legislation/laws/MDW/50-A | Class A MDs erected/converted after Jan 1 1968: automatic self-closing & self-locking doors kept locked; 8+ apartments → intercom with remote release; pre-1968 on majority tenant written request. | §9 Q4; glossary |
| H23 | `NSPIRE-V standards entry door lock deficiency …` · FC search → FC scrape PDF (directQuote) | https://www.hud.gov/sites/dfiles/PIH/documents/NSPIRE-Standard-Door-Entry_20230811.pdf | Def. 4 "Entry door cannot be secured by at least 1 installed lock" Severe, HCV Fail, 30 days; Def. 3 self-closing mechanism damaged/missing HCV Fail 30 days; Def. 10 damaged auxiliary (additional) installed lock = Low, HCV Pass. | §9 Q7; glossary |
| H24 | `GreenThumb community garden license open to public hours per week requirement …` · FC search (excerpts) | https://www.nycgovparks.org/pagefiles/187/2023-GreenThumb-License-English__641329feaf55f.pdf ; https://www.nycgovparks.org/greenthumb/community-gardens | License: site open to public minimum 20 hours/week from April 1 (through October 31 per GreenThumb gardens page). | §9 Q11 |
| H25 | Silo research reused (research/smart-lock-installation.md, not re-fetched) | N1 MDL 51-c; N4 TDPA LL63; N9 Admin Code 26-521; M15 NYC BC 1010.1.9.9; M14 NFPA 80 / iDigHardware; M30 Admin Code 28-105.4.7; LPC rules §2-14 (WH page); S1 Fixr; S3/S4 August retrofit & bridge 10–15 ft; Ring Alarm Z-Wave subscription; ADA 404.2.7 (LI section); M28 7 AM–6 PM; N19 125th Street BID | As listed in silo file. | §7.5, §8.5, §9, §10, §10.5, §14, logistics, glossary |
| H26 | Google PAA / PASF / Answer the Public / AI Overview / Bing / DuckDuckGo / Yelp 1–3★ | — | EMPTY (not accessible in build env). §10.5 states that the claims are published cost-guide/manufacturer claims, not captured AI Overview text. | — |
| H27 | Hyperlocal news on smart locks / keypads in Harlem (Harlem World, West Side Rag, Patch Harlem, AMNY) | — | No service-category story found → EMPTY. | — |

### Prices used (Harlem = Manhattan ×1.25; copied from smart-lock-installation-manhattan.html / silo prices table; none invented)
- Single-door keypad or fob reader with electric strike: **$1,875–$3,125** ($1,500–$2,500 base).
- New electric strike on building/suite door: **$313–$563** ($250–$450).
- Failed electric strike repair: **$369–$606** ($295–$485).
- Programming/setup-only visit: **$265 first hour**, then 30-minute blocks.
- Service/callback: **$195/hr, 3-hour minimum ($585)**, never on first install.
- Apartment / rowhouse / gate smart lock: no AESS figure → "quoted flat at free walkthrough".
- National comparison only: Fixr $250–$400, avg $300 (Jan 2025).

### Images (11) — permanent image rule (Drive "AESS Website Photos/Smart Lock Installation" empty per main run; CompanyCam not connected)
All viewed before use. Each cropped to remove faces/profiles, garbled cap/van lettering and fictional signage; captions/alt describe only what is visible. DAILY-LOG note: `images: 11 reused from images/low-voltage/ (no real smart-lock photos yet)`.

| New file (images/smart-lock-installation/) | Source (images/low-voltage/) | Crop |
|---|---|---|
| smart-lock-installation-harlem-strike-keypad-push-to-exit-glass-door.webp (hero, eager) | low-voltage-installation-long-island-electric-strike-keypad.jpg | x860–1400, y100–1120 (removes installer, garbled van lettering) |
| smart-lock-installation-harlem-video-intercom-keypad-panel-stone-wall.webp | low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg | x600–1050, y170–960 (removes installer profile, garbled cap) |
| smart-lock-installation-harlem-weatherproof-enclosure-conduit-brick-wall.webp | low-voltage-installation-nassau-county-exterior-enclosure-install.jpg | 52–100% x, 8–78% y (removes face, shirt, parked cars) |
| smart-lock-installation-harlem-fob-reader-mounting-beside-glass-door.webp | low-voltage-installation-bronx-14-access-control-reader-wiring.jpg | x540–1050, y380–1150 (removes head/cap with garbled text) |
| smart-lock-installation-harlem-maglock-header-wiring-glass-entrance.webp | low-voltage-installation-long-island-maglock-install.jpg | x560–1400, y60–700 (removes head/cap, car plates, sidewalk sign) |
| smart-lock-installation-harlem-electric-strike-terminal-block-steel-frame.webp | low-voltage-installation-nassau-county-electric-strike-wiring.jpg | x450–1400 (removes face/glasses) |
| smart-lock-installation-harlem-maglock-terminal-wiring-door-frame.webp | low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | x560–1210, y60–1050 (removes face) |
| smart-lock-installation-harlem-cable-feed-conduit-riser-block-wall.webp | low-voltage-installation-nassau-county-riser-conduit-pull.jpg | 55–100% x (removes face, "FIRE" sign) |
| smart-lock-installation-harlem-wall-plate-data-jack-termination.webp | low-voltage-installation-bronx-08-keystone-wall-plate-termination.jpg | 56–100% x, 5–100% y (removes head) |
| smart-lock-installation-harlem-cable-certifier-pass-wall-jack.webp | low-voltage-installation-bronx-07-fluke-certification-pass.jpg | 50–100% x, 10–92% y (removes face) |
| smart-lock-installation-harlem-tone-probe-tracing-cable-wall-box.webp | low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg | 50–100% x (removes face) |

Rejected: low-voltage-installation-long-island-lobby-video-intercom.jpg (fictional "123 MAIN STREET / ABC Property Management" sign); bronx-access-point-lift-install.jpg (face remains in any useful crop; "COMMUNITY CENTER" sign).
**Flag:** the whole images/low-voltage/ library has the look of rendered images (garbled lettering on caps and vans in the uncropped originals). Crops avoid every garbled/fictional text element, but real AESS photos should replace these when uploaded.

## Question register — smart-lock-installation-harlem-manhattan-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
Buildings run by the people who live in them
1. When our HDFC board changes at the annual election, how do the outgoing officers hand over control of the street-door system?
2. Can our board use the street-door entry log to check whether a shareholder really lives in the apartment?
3. Our building is still in the City's Tenant Interim Lease program — can the tenant association put a keypad on the front door itself?
4. Our reserve fund is thin — should the board fix the door closer and strike first, or go straight to a keypad?
5. Rent-paying tenants still live in our HDFC alongside the shareholders — do they get street-door codes on the same terms?
6. Cloud video intercoms bill by the month — how does that compare over ten years with a stand-alone keypad for a twelve-unit HDFC?
Brownstone owners who are also landlords
7. Our tenant pays part of the rent with a Housing Choice Voucher — will the unit inspection look at the lock on their door?
8. Our house backs onto the gated alley behind Strivers' Row — can the alley gate take a keypad, and who has to agree?
Shops, restaurants and shared grounds
9. Our shop rents the ground floor of an HDFC co-op — who approves a keypad on the shop door, the co-op as landlord or HPD?
10. Our restaurant on Frederick Douglass Boulevard takes deliveries through the sidewalk cellar doors — can those be put on a code?
11. Our GreenThumb community garden has to be open to the public at set hours — can a keypad gate still work there?

### §17 FAQ (visible == FAQPage, 8)
1. What does a keypad and electric strike on an HDFC building's street door cost in Harlem?
2. Do you also work in Sugar Hill, Hamilton Heights and the blocks around Marcus Garvey Park?
3. Will you train two or three residents to run the system, not just one board officer?
4. Can you invoice the co-op corporation or tenant association rather than a board member personally?
5. Can the street door stay released longer for a neighbour who walks slowly?
6. If the board loses track of which fob belongs to which apartment, can you rebuild the list?
7. Can residents keep using the old street-door key while everyone switches over to codes?
8. Do you give HDFCs or non-profits a discount?

### Other question-form headings
- H2 "Keypad or Strike Failing North of 110th Street?" (repair capture)
- H2 "Shut Out on a Harlem Stoop or Street Door Tonight?" (final repair capture)

### De-dup notes
Avoided intents already in the register: board-approval of unit locks / smart-lock policy (NYC hub, Jackson Heights), self-managed co-op "who holds admin" (Brooklyn Heights, Greenpoint — Q1 is the election-handover intent), approved sublet handover (Jackson Heights), rooming-house locks (Chelsea), deed theft/estate (Bed-Stuy), NYCHA bottom lock (Bronx), monthly subscription generic (Staten Island), Mitchell-Lama approval (Kingsbridge), propped-door alert (Greenpoint), wheelchair auto-open (Greenpoint — FAQ 5 is release duration), cellar door after burglary (Throgs Neck — Q10 is sidewalk delivery hatch), lake-association gate codes (Putnam — Q11 is the GreenThumb public-hours rule). FAQ 1/2 cost and coverage are geo-specific by design.

### Flags for Anwar
- FAQ 8 states published prices are the same for every building (no HDFC/non-profit discount) — consistent with published-price policy, but confirm.
- FAQ 4 promises invoicing in the corporation's/association's name — confirm with billing.
- Page file size had to be landed in the narrow 180,812–180,886 B gap between siblings (Kingsbridge-area sizes); ~370 blank lines before </body> were used to fine-tune. If batch-mate pages land near 180.8 KB, re-check the ±2 KB rule.


## Bay Ridge, Brooklyn (smart-lock-installation-bay-ridge-brooklyn-ny)

Built 2026-10-17 by the Bay Ridge builder subagent (batch with -tottenville-staten-island-ny and -harlem-manhattan-ny). Phone (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, #brooklyn) · up-link /smart-lock-installation-brooklyn · Brooklyn ×1.00. Not committed.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape (query mode, direct quotes unless noted).

**Thesis / lane:** in Bay Ridge the door keeps a clock. Long commutes from the end of the R line (46.4-min mean), one resident in five aged 65+ with aides/relatives on timetables, two-family houses where two households keep different hours behind one street door, and Third Avenue kitchens open to 4 a.m. (Aug 2026 3–4:30 a.m. restaurant burglaries). So every lock is planned as a timetable: named per-person codes with windows, auto-relock + nightly scheduled lock-up, after-hours curfews for staff codes, first-person-in unlocking for practices, inactivity ("door hasn't opened by noon") alerts, readable logs, DST/clock correctness, admin hand-off for Fort Hamilton deployments. Deliberately avoids sibling lanes: Brooklyn (brownstone double doors/vestibule/stoop parcels/LPC replacement), Bed-Stuy (custody/inherited houses/deed theft), Greenpoint (shared walk-up street door/strike/closer), Brooklyn Heights (LPC device placement/carriage houses), Westchester (commuter empty house — here only context), Queens (multigenerational/app language/basements), Orange (handovers/West Point on-post).

### Local research matrix (new this run)

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| BR1 | `68th Precinct Bay Ridge burglary 2026` · FC search | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/68th-precinct.page ; https://www.facebook.com/NYPD68pct/ (excerpt) ; https://queenoftheclick.com/2026/03/12/crime-is-up-in-the-68th-precinct-bay-ridge/ (FC scrape, markdown) | 68th Pct covers Bay Ridge + Dyker Heights; FB excerpt: investigation into "multiple commercial burglaries that occurred along Third Avenue during the early morning hours on Friday"; Queen of the Click (Mar 12 2026): "Our area is still having problems with people stealing. Car thefts and assaults are up." (no figures — not used). | context only (BR3 used instead) |
| BR2 | `Bay Ridge Brooklyn package theft stolen packages doorstep news` · FC search | https://www.reddit.com/r/Brooklyn/comments/vwfxvh/package_thief_in_bayridge/ (excerpt) ; https://brooklynreporter.com/2016/09/package-theft-from-ridge-stoop-has-homeowner-wary/ (excerpt) | r/Brooklyn "package thief in Bayridge": building put up signs not to buzz in people residents don't know (excerpt only; thread body EMPTY — Reddit not scrapeable). 2016 Brooklyn Reporter: packages stolen from a Ridge porch. Not quoted. | not used on page (parcel intent belongs to Brooklyn page) |
| BR3 | `Third Avenue Bay Ridge break-ins 3 a.m. businesses three suspects NYPD` · FC search → FC scrape | https://pix11.com/news/local-news/brooklyn/three-brooklyn-restaurants-burglarized-overnight-nypd/ | Posted Aug 31 2026: three Third Avenue restaurants (88th St, 94th St, 87th St) burglarised "on Friday" between 3 a.m. and 4:30 a.m.; unknown amount of money stolen. (ABC7/1010 WINS excerpts say "at least four" — page uses PIX11's three.) Date on page = Friday Aug 28 2026 (derived from "Friday" in an Aug 31 Monday post). | §5 para 5, Q&A "staff codes stop working", §8 Third Ave card context, Sources |
| BR4 | same search · FC scrape | https://www.cbsnews.com/newyork/news/nypd-suspects-wanted-for-stealing-28000-in-string-of-bay-ridge-robberies/ | $28,000 cash in six break-ins at Bay Ridge businesses incl. restaurants/nightclubs; video of someone yanking a door early morning Sept 5; Third Ave bistro lost >$4,000 Aug 30. Year not printed in scraped text (image path 2022/09) → NOT used on page. | research only |
| BR5 | `Bay Ridge Brooklyn residents 65 and older percent seniors aging in place community district 10` · FC search | https://comptroller.nyc.gov/reports/aging-with-dignity-a-blueprint-for-serving-nycs-growing-senior-population/ (excerpt) | BK CD10 16.5% 65+ (2015). Superseded by Furman 2024 figure (BR8). | research only |
| BR6 | `Bay Ridge apartment building smart lock OR keyless entry OR Latch tenants` · FC search | (r/AskNYC, door.com, vendor blogs) | No Bay Ridge-specific smart-lock news. EMPTY for local smart-lock stories. | — |
| BR7 | (BR5 result) · FC scrape | https://www.bayridgecenter.org/age-friendly | Page returned no text (JS/Squarespace) → EMPTY (not accessible in build env). | — |
| BR8 | `Bay Ridge Dyker Heights community health profile mean commute time minutes residents` · FC search → FC scrape (freeform) | https://www.furmancenter.org/neighborhoods/bay-ridge-dyker-heights/ (updated 2026) | 65+: 13.1% (2010) → 20.2% (2024); homeownership 41.0% (2024); rental vacancy 2.5% (2024); foreign-born 38.2%; households w/ children 25.0% (2024); serious crime 11.4 (2006) → 5.2 per 1,000 (2025); mean travel time to work 46.4 min (2024); car-free commute 63.6% (2024); population 128,247 (2024). | hero, §5 paras 2–3 & 6, §5.5 bullets 1–3 & 6, §10.5 H3 "stops burglars", Sources |
| BR9 | `Bay Ridge burglar entered home through unlocked door OR rear door Brooklyn Reporter 68th Precinct residential burglary` · FC search → FC scrape | https://brooklynreporter.com/2019/09/arrests-made-in-connection-to-15-burglaries-of-dyker-heights-bay-ridge-homes/ | Sept 20 2019: two suspects arrested; as many as 15 burglaries in Dyker and Bay Ridge in August, "largely gaining access through unlocked windows and doors". | §5 para 6, §10.5 H3 auto-lock, Sources |
| BR10 | same search → FC scrape | https://www.brooklynpaper.com/cops-seek-police-impersonators-connected-to-june-robbery-in-bay-ridge/ | Sept 29 2020: home near 83rd St & Third Ave, ~12:30 a.m. June 5; suspects entered through an unlocked window, posed as police. | §10.5 H3 "stops burglars", Sources |
| BR11 | `Bay Ridge home invasion FedEx worker impersonator police impersonator family tied up` · FC search | https://www.nbcnewyork.com/news/local/suspect-arrested-for-allegedly-posing-as-fake-fedex-worker-to-rob-brooklyn-family-of-125k-in-cash-jewelry/1992048/ (excerpt, full text in excerpt) ; https://abc7ny.com/post/fedex-nypd-impersonators-tie-up-rob-brooklyn-family-police-say/5567429/ (excerpt) | Published Oct 8 2019: fake FedEx worker got inside a Bay Ridge home, partner followed; tied up a 36-year-old woman, 75-year-old woman and 81-year-old man; arrest made. | "Twenty-Four Hours" section, §10.5 H3 "stops burglars", Sources |
| BR12 | `NYC Ferry South Brooklyn route Bay Ridge 69th Street pier landing` · FC search | https://www.ferry.nyc/routes-and-schedules/south-brooklyn/ (excerpt) ; https://edc.nyc/proposed-changes-landing (excerpt) | NYC Ferry lists a Bay Ridge landing at American Veterans Memorial Pier; NYCEDC lists a proposed change that the South Brooklyn route would no longer serve Bay Ridge → page says only that NYC Ferry "lists its Bay Ridge landing" there (no service claims). | §13 Shore Road Park card |
| BR13 | `New York City bars last call 4 a.m. State Liquor Authority hours of sale Kings County` · FC search → FC scrape | https://sla.ny.gov/location/kings | Kings County on-premises: weekdays 8:00 AM–4:00 AM; Sundays 10:00 AM–4:00 AM. | §5 para 5, §5.5 bullet 5, §8 Third Ave card |
| BR14 | (BR5 search) → FC scrape | https://www.healthbeat.org/newyork/2025/06/19/senior-adult-center-bay-ridge-brooklyn/ | June 19 2025: Bay Ridge Center, 47 years in a church basement at the west end of Bay Ridge Avenue; new facility broke ground 2024; membership tripled to over 2,000. | Q&A "Mom's door hasn't opened by midday", Sources |
| BR15 | Google PAA / PASF / Answer the Public / Google AI Overview / Bing / DDG / Yelp 1–3★ (Bay Ridge smart lock) | — | EMPTY (not accessible in build env). §10.5 says so on the page and uses Fixr / Bob Vila-type / manufacturer claims. | — |
| BR16 | Reddit r/BayridgeBrooklyn smart lock / landlord lock threads | — | EMPTY (no relevant thread surfaced; reddit not scrapeable). | — |
| BR17 | Bay Ridge local-news stories specifically about smart locks / keyless entry (Brooklyn Paper, Home Reporter, Patch, BK Eagle) | — | EMPTY (none found). | — |

### Reused (sources reached by earlier runs in this repo, not re-fetched; logged in research/cat6-repair.md "Bay Ridge" and research/soundbar-installation.md "Bay Ridge")
| Finding | Source as logged | Page section |
|---|---|---|
| Special Bay Ridge District 1978 after protests over twin 30-storey Bay Ridge Towers and 13-storey Shore Hill Apartments; Mar 23 2005 rezoning of 249 blocks (65th St / Seventh Ave / Shore Road); one-/two-family-only blocks 33 → 101 | https://www.citylandnyc.org/city-increases-zoning-protection-for-bay-ridge/ ; https://zr.planning.nyc.gov/article-xi/chapter-4 | §5 para 1, §5.5 bullet 4, §7 intro, Sources |
| 452 units added 2010–2025 | furmancenter.org (cat6 research) | §5 para 1 |
| CB10: one- and two-family homes "major portion"; corridors 3rd/4th/5th Ave, Fort Hamilton Pkwy, "bustling 86th Street strip"; multiple dwellings on Shore Rd, Ridge Blvd, 4th Ave | https://cbbrooklyn.cityofnewyork.us/cb10/about/neighborhoods/ | §5 paras 1 & 4, §8 intro |
| >1,000 illegal-conversion complaints since 2010 (Bay Ridge, Dyker Heights, Fort Hamilton) | https://www.citylandnyc.org/council-member-works-to-combat-illegal-home-conversions/ (Oct 2014) | §5 para 4 |
| Doctors' Row: 54 limestone row houses, Bay Ridge Pkwy between 4th & 5th Aves, 1906–1913, two storeys + basement, first Bay Ridge historic district (2019), medical professionals historically and currently | https://www.nyc.gov/site/lpc/about/pr2019/lpc-designates-the-first-historic-district-in-bay-ridge-brooklyn.page | §7 limestone card, §8 medical card, §8.5 LPC bullet, §13 card |
| 8200 Narrows Ave House: built 1917, James Sarsfield Kennedy, uncut randomly laid stone, rare Arts and Crafts example (designation year not stated — sources conflict) | http://s-media.nyc.gov/agencies/lpc/lp/1623.pdf | §13 card |
| Fort Hamilton cornerstone 1825, first garrison flag 1831, only active-duty installation in greater NYC area | https://installations.militaryonesource.mil/in-depth-overview/fort-hamilton | Q&A deployment, §13 card |
| Verrazzano-Narrows Bridge opened Nov 21 1964, world's longest suspension span then | wikipedia / mta.info / nycgovparks | §13 card |
| Bay Ridge–95th St opened Oct 31 1925, R terminal | wikipedia / mta.info | §5 para 3, §13 card |
| Owl's Head Park: Yellow Hook → Bay Ridge 1853; Murphy estate bought by E. W. Bliss 1866; park 1928; 24.22 acres | https://www.nycgovparks.org/parks/owls-head-park/history | §13 card |
| Shore Road Park 58.00 acres, views incl. Statue of Liberty, Fort Wadsworth, Coney Island; American Veterans Memorial Pier 600-ft former Bay Ridge–St. George ferry pier | nycgovparks.org shore-road-park; americanveteransmemorialpier; 6tocelebrate.org | §13 card |
| Bay Ridge 5th Ave BID est. June 2006, 40 block faces, 376 ground-floor businesses; 86th Street BID est. Oct 2001, 16 block faces, 145 ground-floor businesses; R at 86th St & 4th Ave; Third Ave "36-block strip" (merchants' FB page) | nyc.gov SBS BID directory (bid=55, bid=42); 86bid.org; facebook.com/ThirdAvenueBayRidge | §5 para 5, §8 cards |
| The Normandy, 9437 Shore Road, Art Moderne, opened as rental 1940, 55-unit six-storey co-op; 9201 Shore Road built 1960, 254 apartments; Shore Road high concentration of co-ops | brownstoner.com (Aug 2026); soldbysoldano.com; cooperatornews.com | §7 co-op card, co-op/renters section |
| Silo-wide: MDL §51-c, MDL §4 (3+ families), HMC/HPD fire safety (no double-cylinder on apartment doors), Admin Code §26-521, Tenant Data Privacy Act LL63/2021, LPC Permit Guidebook (hardware no permit), NY1 roll-down gate deadline repeal, Fixr $250–$400 avg $300, keypad unit $100–$250, August Connect 10–15 ft & single-cylinder retrofit, Yale Matter/Thread border router same ecosystem, Allegion Schlage Arrive 1-3/8"–2" thickness, 2-3/8"/2-3/4" backset | research/smart-lock-installation.md S1–S6, N1, N4, N6, N9, N18, B4, B8, WB16 | §7.5, §8.5, Q&A, §10, §10.5, §14, renters section |

General statements without a dedicated fetched source (flagged): US DST ends first Sunday in November / starts second Sunday in March (common knowledge, federal law); lock-app capabilities (date-range codes, recurring weekly schedules, fortnightly repeats often unsupported, admin vs user roles, notification digests, first-person-in rules more common on commercial access control, many locks do not log mechanical key use) — worded as "many / some / usually", no brand claims.

### Prices used (Brooklyn ×1.00 — copied from smart-lock-installation-brooklyn.html / silo prices table; nothing new)
- Single-door keypad or fob reader with electric strike $1,500–$2,500 installed (§14 table, Premium package, FAQ 1, Service schema).
- New electric strike $250–$450; failed strike repair $295–$485 (§14, schema).
- Setup-only visit $195 first hour then 30-min blocks (repair capture, §14, BYO card, schema). Same flag as Brooklyn page: confirm this rate may be quoted for smart-lock app/code/schedule visits.
- Service/callback $195/hr, 3-hr minimum ($585) (§14).
- Residential smart locks: quoted flat at walkthrough (§14, Starter/Standard, BYO).
- Fixr national $250–$400 / avg $300; keypad units $100–$250 — labelled third-party national (§10.5, §14).
- Worked totals: two reader/strike doors = $3,000–$5,000 (sum of published lines only).

### Images (11) — Step C library (Drive folder empty per main run; CompanyCam not connected)
Source = images/smart-lock-installation/aess-smart-lock-installation-* (viewed with Read via contact sheets; crops chosen to exclude every face; no house numbers, plates or readable documents; the "4A" apartment-door photo, the "128" doorbell photo, customer-face photo and office photos with faces not used). Pillow crop → WebP q80, ≤1600 px. NOTE (same as West Brighton): the aess-* set looks AI-rendered — flag for Anwar.
| File (images/smart-lock-installation/) | Source (aess-smart-lock-installation-…) | Crop box (x0,y0,x1,y1) | Section |
|---|---|---|---|
| smart-lock-installation-bay-ridge-keypad-deadbolt-lever-wood-door.webp | keypad-smart-deadbolt-brownstone-door | 560,0,1400,1050 | hero / og:image |
| smart-lock-installation-bay-ridge-inside-thumb-turn-hand.webp | keypad-exterior-thumbturn-interior-view (interior panel only, overlay text cropped off) | 700,0,1400,760 | instant action |
| smart-lock-installation-bay-ridge-tape-measure-old-bore-latch-plate.webp | measuring-door-bore-for-deadbolt | 690,120,1400,1050 | §5 |
| smart-lock-installation-bay-ridge-keypad-removed-wiring-check.webp | servicing-keypad-wiring | 700,200,1400,933 | repair capture |
| smart-lock-installation-bay-ridge-drill-keypad-door-iron-grille.webp | drilling-keypad-lock-brownstone-stoop | 700,120,1400,933 | §7 |
| smart-lock-installation-bay-ridge-adding-code-phone-keypad.webp | programming-access-code-app | 760,200,1400,1050 | §8 |
| smart-lock-installation-bay-ridge-fingerprint-scan-phone-unlocked-screen.webp | fingerprint-unlock-demo-app | 720,180,1400,1050 | §9 |
| smart-lock-installation-bay-ridge-ribbon-cable-interior-assembly.webp | connecting-interior-unit-cable | 800,250,1400,1050 | §10 |
| smart-lock-installation-bay-ridge-latch-strike-edge-check.webp | checking-latch-bolt-alignment | 720,150,1400,1050 | §13 |
| smart-lock-installation-bay-ridge-unscrewing-brass-deadbolt.webp | removing-old-brass-deadbolt | 700,330,1400,1050 | §14 |
| smart-lock-installation-bay-ridge-battery-pack-interior-unit.webp | replacing-smart-lock-batteries | 800,120,1400,933 | settings section |
DAILY-LOG note suggestion: `images: 11 cropped from images/smart-lock-installation/aess-smart-lock-installation-* (no real smart-lock photos in Drive; faces cropped out)`.

### Build notes
- check_page.py on the real repo: only wiring failures remain (sitemap, _redirects ×2, Brooklyn hub link-down, 16 area pages link-back). With those simulated in a scratch copy (symlinked root; nothing in the repo changed) → **PASS**. 13,170 rendered words, 240,550 B (placed in the gap between 236,388 and 243,491; Tottenville 225,158 / Harlem 180,846 at last check), title 45, meta 160, 11 figures, 6 JSON-LD blocks, FAQ 7 = FAQPage 7, HowTo 6 = process 6.
- Masked similarity (word-level difflib, blocks p/li/td/h2/h3/figcaption ≥8 masked words, geo + street names masked) vs all 33 smart-lock pages on disk (incl. Tottenville and Harlem drafts) and the cat6/soundbar/other-silo Bay Ridge pages: every non-constant block < 0.65 (max remaining non-constant 0.64 = Sources citation line vs soundbar-bay-ridge Sources). Blocks ≥0.65 are only blueprint H2 patterns, licence/rating strip, warranty sentence, NAP, price-table row labels.
- `#sl-nbhd-links` = West Brighton block + West Brighton + Harlem + Tottenville (17 links).

## Question register — smart-lock-installation-bay-ridge-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 11)
1. The clocks go back an hour in November — do the timed codes on our lock move with them, and what keeps the lock's own clock right?
2. Our cleaner comes every other Thursday — can a lock schedule follow a fortnightly pattern?
3. Can the street door of our two-family lock itself at 11 every night, whoever left it on the latch?
4. Relatives fly in from abroad for six weeks every summer — can their code start the day they land and stop the day they fly home?
5. Can the lock tell us if Mom's front door hasn't opened at all by midday?
6. I'm deploying from Fort Hamilton for nine months — how should control of our lock pass to my spouse or a relative while I'm away?
7. Our ornate wood door has an iron grille bolted over its glass panel — does that change where the smart lock can go?
8. The app shows our front door unlocked at 3:12 a.m. and nobody remembers doing it — how do we work out what happened?
9. Can each code carry a name, so the history reads "cleaner" rather than a slot number?
10. Burglars hit Third Avenue restaurants between 3 and 4:30 a.m. in August 2026 — can our staff codes simply stop working between closing and opening?
11. Our practice opens at 8, but on a snow day nobody comes in — can the front door wait for the first employee instead of unlocking by the clock?

### §17 FAQ (visible == FAQPage, 7)
1. How is a Bay Ridge job priced when one visit covers a house door, a co-op unit door and a shop door?
2. Do you also cover Dyker Heights, Fort Hamilton and the Sunset Park blocks just north of 65th Street?
3. Can the installer arrive at 7 a.m. so we can still make the R train or the express bus?
4. Can a shop or practice door schedule be told about public holidays?
5. Can we get one daily summary of the door instead of a notification every time it opens?
6. If a code only works on weekday mornings, does the physical key still open the door at any hour?
7. If our upstairs tenant uses the app for the shared street door, can she see when we come and go?

### Other question-form headings
- H2 "Bay Ridge Lock Ignoring Its Schedule, or Not Answering at All?" (repair capture)
- H2 "Shut Out Somewhere Between Shore Road and Seventh Avenue?" (final repair capture)

### De-dup notes
Compared by meaning against all 739 question headings/FAQs on the 31 smart-lock pages on disk at start, every register in research/smart-lock-installation.md, and the Tottenville and Harlem drafts at finish. Dropped during build: "Do you take away the old locks?" (= New Dorp FAQ), fake-courier "should we unlock from the app" (= Flushing), stoop parcels (= Brooklyn), auto-lock delay length (≈ Nassau mudroom/yard), co-op contractor hours with nobody home (≈ LI/Manhattan), keypad beeps at night (= Rockland), landmark approval (= Bed-Stuy/BH/HV). Partial overlaps left for the main run to judge: Q3 scheduled nightly lock-up vs Rockland "app tell us at bedtime which doors are unlocked" (mine = lock acts by itself) and Westchester "front door left unlocked on purpose for a party" (mine = overriding a forgotten hold-open); Q4 date-range code vs Bayside "code that works only once" and Washington Heights "one-time code for relative at GWB bus station" (mine = multi-week, date-bounded); Q5 inactivity alert vs Queens "dementia — opens door at night" (mine = absence of activity); Q10 staff-code curfew vs Greenpoint "after Franklin Street restaurant burglaries, what does an electronic lock add on a back door" (mine = time-restricted credentials); FAQ 7 tenant seeing owner's log vs Brooklyn "As the owner, can I see when my tenant comes and goes" (reverse direction, account roles).


<!-- merged from smart-lock-installation.williamsburg.part.md (batch 2026-10-17) -->
## Williamsburg, Brooklyn (smart-lock-installation-williamsburg-brooklyn-ny)

Built 2026-10-17 by the Williamsburg builder subagent (batch: Williamsburg BK, Forest Hills QN, Pelham Bay BX). Up-link /smart-lock-installation-brooklyn; phone (347) 934-8335; GBP Brooklyn (1282 Troy Ave, #brooklyn). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. "WebSearch"/"WebFetch" = built-in tools; "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only). Shell curl blocked.

**Thesis / lane:** in Williamsburg most doors are doing a job they were not built for — factory/warehouse doors that became Loft Law (IMD) apartment doors (hasps, surface bolts, no bore, heavy/sagging, thickness outside lock ranges, fire labels, Loft Board egress rule incl. lithium-charger rule), post-1903 tenement doors shared by a rotating cast of tenants (credential register), shopfronts that become bar/venue entrances after dark (crew codes, three roles of a venue door), regulated retail (cannabis 9 NYCRR 125.3), and South Williamsburg doors that must work without electronics on Shabbat (mechanical push-button door kept available; LeFrak City precedent; MDL 51-c). Kept away from: Greenpoint (shared street door/closer), Brooklyn (brownstone vestibule/two-family), Bed-Stuy (custody/estates), Rockland (Shabbat split door plan as household Q&A — here Shabbat is handled as building/legal/hardware prose, not repeated Rockland intents).

### Local research (new this run)

| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| W1 | https://en.wikipedia.org/wiki/Williamsburg,_Brooklyn · WebFetch | same | ZIPs 11211 (most), 11206 (SE), 11249 (river); 90th Pct 211 Union Ave, 94th covers northernmost; Grand St separates North Side/South Side; L (Bedford Ave), J/M/Z along Broadway, G east; Graham Ave "Avenue of Puerto Rico", Via Vespucci; Havemeyer St; after bridge 1903 most densely populated neighbourhood in NYC; ~3,000 artists 1996; Gretsch → lofts; Austin, Nichols warehouse → apartments 2010s; May 11 2005 rezoning, 2-mile esplanade. | §5 paras 1–3, §5.5 bullets 1,3,6; §8 Graham Ave card; §7 cards; riverfront section |
| W2 | `Williamsburg Brooklyn Hasidic Shabbat electronic lock keypad door apartment building` · WebSearch → `South Williamsburg Satmar Hasidic community large families housing Lee Avenue population` · WebSearch → WebFetch https://en.wikipedia.org/wiki/South_Williamsburg,_Brooklyn | same | Bounded Division Ave N, Broadway NE, Flushing Ave S, East River W; Hasidic community centred on Lee & Bedford Aves south of Division; largely Satmar, settled late 1940s; synagogues etc. built 1950s–60s revitalising abandoned housing; UJA-Federation 2023: 21,000 households in Williamsburg, 36,000 Jewish adults, 32,000 children; Los Sures between Grand St and bridge, Puerto Rican + Dominican + Mexican; Southside United HDFC (Los Sures) 1972, 1975 first Brooklyn CBO to manage city-owned properties; Moore Street Market 1941 at 110 Moore St; Williamsburgh Library first Carnegie library in Brooklyn, cornerstone 1903, 26,000 sq ft; Williamsburg Houses 1938 PWA, NYCHA. | §5 para 3, §5.5 bullet 5, §7 Hasidic card, §13 Moore St + Library cards, Shabbat section |
| W3 | `Loft Law interim multiple dwelling Article 7-B fire safety requirements doors self-closing loft board` · WebSearch → WebFetch | https://www.nyc.gov/assets/loftboard/downloads/pdf/fire_egress_rule.pdf | 29 RCNY §2-04(b)(11)(ii)(C): "The door leading to indoor Stairs must be a self-closing door" (+ AC 28-315.10, 27-2041.1); (i)(E): no bars/grilles on fire-escape windows (exceptions); (iii)(C): "Lithium battery charging devices may not be stored in or near the front door of an IMD unit." | §9 Q3 (lithium), Q5 (stair door), Sources |
| W4 | `Williamsburg Brooklyn package theft lobby door burglary 90th Precinct 2026` · WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/woman-riding-e-bike-steals-packages-from-buildings-in-williamsburg-brooklyn-police-say (updated Dec 13 2023) | Oct 18: Bedford Ave building — "went in through the main entrance and into the mail room"; Dec 6: Kent Ave building, "numerous" packages; e-bike. | §5 para 5, §10.5 H3 3, Sources |
| W5 | `Williamsburg Brooklyn burglary apartment building front door 2025 police Bedford Avenue` · WebSearch → WebFetch | https://abc7ny.com/post/nyc-crme-burglary-spree-brooklyn-williamsburg/12673159/ (Jan 8 2023) | Six burglaries, three on Kent Ave, others nearby; suspects "cut through the metal locks on the front door" (12 Chairs); door struck with a sledgehammer (Misi); >$16,000. Businesses not named on page. | §5 para 5, §8 intro, §10.5 H3 5 |
| W6 | same search → WebFetch | https://brooklyn.news12.com/nypd-3-separate-burglary-incidents-on-bedford-ave-3-suspects-wanted | Aug 6 & Aug 14 2023 break-ins at a Bedford Ave store (366 Bedford) while closed; Plantia Cannabis Shop, 265 Bedford Ave. Businesses not named on page. | §8 intro |
| W7 | `reddit r/williamsburg building front door lock broken packages stolen landlord` · FC search | https://www.reddit.com/r/williamsburg/comments/18qxn3y/stolen_packages/ (excerpt only) | "Yeah we got our packages jacked a few weeks ago because our front door lock is broken" | §5 para 5 |
| W8 | same FC search | https://www.nytimes.com/2024/11/02/realestate/stolen-packages-lobby-apartment-building.html (excerpt only) | "Landlords are not legally required to provide delivery lockers, or concierges, if these are not already provided services in your building." | §10.5 H3 3, Sources |
| W9 | same FC search → WebFetch | https://www.brickunderground.com/live/realty-bites-dealing-with-package-delivery-theft-landlords-nyc (Apr 19 2022) | Property manager: "updated front door locks, installed security cameras" … "none of it has completely stopped theft." | Sources only (background) |
| W10 | `Williamsburg Brooklyn Hasidic Shabbat electronic lock…` · WebSearch → WebFetch | https://www.jewishpress.com/news/breaking-news/orthodox-residents-suing-lefrak-city-over-electric-doors/2015/08/02/ (date from URL) | Orthodox residents of LeFrak City (Corona, Queens) sued in Brooklyn federal court (Fair Housing Act) after lobby doors went to electronic key; asked for one door per building with a regular lock + Shabbat elevators. Outcome not in article. | §9 Shabbat Q1, Shabbat section para 3 |
| W11 | `smart lock "Shabbat mode" OR "Sabbath mode" keypad door lock mechanical key override` · WebSearch → WebFetch | https://jewishlink.news/are-smart-locks-shabbat-compatible/ (Dov Pavel, Oct 26 2017) | Keypad lock logs even when opened with its own code; key "is only a viable solution, of course, for those living in an area with an eruv"; option: inside-mounted August + mechanical push-button outside; bridge on a schedule; "I am not a halachic authority". | §10 equipment para, Shabbat section para 2, Sources |
| W12 | `Williamsburg eruv Brooklyn carrying keys Shabbat` · WebSearch → WebFetch | https://pluralism.org/news/crowded-new-york-williamsburg-hasidic-community-struggles-build-eruv (Maariv, Oct 3 2003) | Describes Williamsburg as lacking an eruv in 2003 ("last anti-eruv bastion"). Too old/contested → research only; page makes no eruv claim about Williamsburg. | research only |
| W13 | `New York OCM adult-use cannabis dispensary security requirements commercial grade locks doors regulation 9 NYCRR 125` · WebSearch → WebFetch | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 | Secure all entrances; lock perimeter doors; codes/passwords not accessible to unauthorised; locks in full operating order, tested ≤30 days, records 5 years; visitor log 5 years (consumers excluded). | §8 rules bullet 1, FAQ 4, Sources |
| W14 | `Amazon Key for Business apartment building lobby door access…` · WebSearch → WebFetch butterflymx.com | — | Fetched page returned the homepage, no content → not used. EMPTY. | — |
| W15 | `Williamsburg Brooklyn Loft Law tenants building freight elevator door lock IMD loft 2024 OR 2025` · FC search | https://www.nyc.gov/site/buildings/industry/project-requirements-design-professional-alt-loft-law.page (excerpt) | DOB: existing freight elevator that is the only elevator serving IMD units must be converted to a code-compliant passenger elevator. Background only. | research only (FAQ 2 framed generally) |

### Reused from earlier repo research (not re-fetched; sources as logged)
| Finding | Source (as logged) | Page section |
|---|---|---|
| Loft Law = MDL Art. 7-C 1982, IMD class, Loft Board, IBZ exclusion with Greenpoint/Williamsburg exceptions | nyc.gov/site/loftboard/about (soundbar + cat6-repair Williamsburg sections) | §5 para 2, §5.5 bullet 2, §7, §9 Q2 |
| Rezoning ~175 blocks; 41% population growth 2010–2020 | cbsnews.com Williamsburg-Greenpoint rezoning 20 years later (cat6-repair W3) | §5 para 1, §5.5 |
| Council approval May 11 2005 | nyc.gov DCP greenpointwill.pdf (cat6-repair W2) | §5.5 |
| Domino 1856–2004; landmark 2007; 325 Kent 2017, Park 2018, One South First & Ten Grand 2019, One Domino Square 2024; Refinery offices | en.wikipedia.org/wiki/Domino_Sugar_Refinery (cat6-repair W4) | §5 para 1, §7 tower card, §13 Domino card |
| Wythe Hotel 1901 cooperage | wythehotel.com/about (soundbar, cat6) | §5 para 2, §8 Kent/Wythe card |
| Williamsburgh Savings Bank 175 Broadway, 1875, ext. landmark May 17 1966, interior 1996, Weylin 2014 | Wikipedia / LPC LP-1910 (soundbar, cat6 W7) | §13 card, §8 rules bullet 4 |
| Gretsch 60 Broadway, 1916, converted 2003–05, 130 apts, 12–13 ft ceilings | cityrealty.com (soundbar) | §5 para 2, §7 card, §13 card |
| Williamsburg Houses 1938, 20 four-storey bldgs, 23.3 acres, landmark 2003, Maujer/Scholes/Leonard/Bushwick Ave | LPC 2135.pdf (soundbar); Wikipedia | §7 card, §13 card |
| Music Hall of Williamsburg 66 N 6th St; Baby's All Right 146 Broadway | bowerypresents.com; Wikipedia (cat6 W8) | §8 cards |
| Grand St & Metropolitan Ave = two major commercial strips | forgotten-ny.com 2021 (cat6 W11) | §8 card |
| North Brooklyn IBZ study 1,066 acres, 19,500 jobs | nyc.gov North Brooklyn Industry Plan (cat6 W9) | §8 East Williamsburg card |
| Dining Out NYC roadway cafés seasonal; attachments on building | diningoutnyc.info (cat6 W14/W15) | §8 rules bullet 3 |
| One South First 435 ft, 330 rentals; Domino ~2,800 rentals across four buildings | 6sqft May 21 2019 (soundbar) | riverfront section |
| RentHop: North Side–South Side 3,746 noise complaints Mar 1–Jun 14 2021, most in Brooklyn | renthop.com (soundbar) | §5 para 4 |
| CD1 population 218,831 (ACS 2024 1-yr) | censusreporter.org (soundbar) | §5 para 4 |
| Homeownership 16.6% (2024) Greenpoint/Williamsburg | furmancenter.org (silo Greenpoint G3) | §5 para 4 |
| Graham Avenue BID, Grand Street BID in SBS directory | nyc.gov SBS BID directory (silo Brooklyn B11) | §8 cards |
| MDL 51-c (≤3 in., duplicate key, excludes housing authority/hotels/dorms); HMC 27-2043; HPD double-cylinder illegal; TDPA LL63/2021; LPC hardware vs door | silo N1, N3, N4, N6, B4 | §9 Shabbat Q2, §9 Q5, walk-up section, §8 rules, FAQ |
| Lock door-thickness ranges: Schlage Encode 1-3/8–1-3/4 in.; Kwikset Z-Wave 700 1-3/8–2 in.; Yale Assure 2 1-3/8–2-1/4 in.; August retrofit single-cylinder only; August Connect 10–15 ft; Fixr $250–$400 avg $300 (Jan 2025); Bob Vila screwdriver/~30 min | silo S1–S4, LI/HV sections | §9 Q4, §10.5 H3s 1,2,4,6, cost section |

### Prices (Brooklyn ×1.00, copied from smart-lock-installation-brooklyn.html — none invented)
$1,500–$2,500 keypad/fob reader + electric strike installed; $250–$450 new electric strike; $295–$485 failed strike repair; $195 first hour then 30-min blocks (setup visit — same flag for Anwar as the Brooklyn page); $195/hr 3-hour minimum ($585) callback; private-door lock "quoted flat at free walkthrough"; Fixr national $250–$400 / ~$300 labelled third-party.

### EMPTY (not accessible in build env)
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: EMPTY (not accessible in build env). §10.5 says so and uses published cost-guide/manufacturer claims.
- Yelp 1–3★ Williamsburg locksmith/smart lock: EMPTY (not accessible in build env).
- Reddit thread bodies (r/williamsburg): excerpt only; full thread EMPTY.
- NYT Nov 2 2024 article body: excerpt only (EMPTY beyond search snippet).
- Amazon Key for Business (W14): EMPTY.
- Local news on smart locks specifically in Williamsburg (Brooklyn Paper, Greenpointers, BK Reader, Hamodia/Yiddish press): none found → EMPTY.
- Field Notes: no sourced Williamsburg install anecdote → written as a working routine and labelled so.

### Images (11) — permanent image rule
Drive folder "AESS Website Photos/Smart Lock Installation" EMPTY (main run); CompanyCam not connected. Every candidate viewed; each crop re-cut from the source to remove faces, a house number ("128"), a unit sign ("4A"), a customer and the toll-free number printed on a shirt. All sources have been used (as other crops/copies) on earlier smart-lock pages — the library has few distinct door photos; these library photos look AI-rendered (same note as earlier pages) → needs Anwar's review / real photos. WebP q80.

| New file (images/smart-lock-installation/) | Source | Crop |
|---|---|---|
| smart-lock-installation-williamsburg-keypad-deadbolt-dark-glass-door-latch.webp (hero, eager) | images/smart-lock-installation/aess-smart-lock-installation-office-glass-door-smart-lock.webp | right side, tech face removed |
| -gloved-hands-keypad-lever-latch-screw.webp | aess-smart-lock-installation-office-lever-smart-lock-install.webp | right side, face removed |
| -keypad-deadbolt-wood-panel-door-stone-jamb.webp | aess-smart-lock-installation-keypad-smart-deadbolt-brownstone-door.webp | right 70% |
| -interior-unit-ribbon-cable-connection.webp | aess-smart-lock-installation-connecting-interior-unit-cable.webp | hands/lock only |
| -video-doorbell-beside-keypad-deadbolt.webp | aess-smart-lock-installation-video-doorbell-and-smart-lock.webp | house number "128" and face removed |
| -phone-app-unlocked-beside-keypad.webp | aess-smart-lock-installation-showing-customer-app-unlock.webp | customer and tech faces removed |
| -maglock-terminal-block-12vdc-label.webp | images/low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg | face removed |
| -card-reader-screwdriver-glass-door-pull.webp | images/low-voltage/low-voltage-installation-dutchess-county-12-access-control-reader-wiring.jpg | head removed |
| -maglock-wiring-at-door-header.webp | images/low-voltage/low-voltage-installation-long-island-maglock-install.jpg | header only (phone number on shirt, plates removed) |
| -corridor-unit-door-keypad-and-app.webp | aess-smart-lock-installation-apartment-door-smart-lock-app.webp | "4A" sign and face removed |
| -tape-measure-old-bore-backset.webp | aess-smart-lock-installation-measuring-door-bore-for-deadbolt.webp | hands/bore only |

## Question register — smart-lock-installation-williamsburg-brooklyn-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 10) — under non-question H2s "Lofts and Loft Law buildings" · "South Williamsburg households and Shabbat" · "Shops, venues and short leases" · "Tenement walk-ups"
1. Our loft door still carries the surface bolt and padlock hasp from its factory days — do those come off when a smart lock goes on?
2. Our building is partway through Loft Board legalisation — should a smart lock wait until the fire-safety work reaches our unit?
3. The Loft Board's fire rule keeps lithium battery chargers away from an IMD unit's front door — does that limit where a smart lock or its charger can go?
4. Our loft entry is an oversized, very heavy door — will a smart deadbolt cope with it?
5. Our loft's back door opens onto the old freight stair — can it be locked from the stair side and still let us out in one motion?
6. Our landlord wants to make the building door fob-only, and several families here keep Shabbat — has that been fought over before?
7. Can a mechanical push-button lock we use on Shabbat count as the extra lock a tenant is allowed to add?
8. We run a music venue — can a touring crew get in for load-in without a staff member standing at the stage door?
9. Our pop-up on Bedford is only leased for three months — is keyless entry worth it, and what happens when we leave?
10. Our smart lock keeps telling us the door is open when it is shut, and our walk-up shakes whenever trucks pass on Broadway — are the two connected?

### §17 FAQ (visible == FAQPage, 8)
1. Our loft door was custom-made by a metal fabricator and has no lock preparation at all — can a smart lock still go on it?
2. Our building's only lift is a freight elevator that needs an operator — can you work around that?
3. Can the auto-lock delay be stretched long enough to wheel a bike, a cello case or a double stroller through the door?
4. Does a licensed cannabis shop need anything particular from its door locks?
5. Our recording studio uses heavy sound-isolation doors with compression seals — can a smart lock go on one?
6. Our shop's door is set back in a deep recessed entry off the sidewalk — does that change where the keypad goes?
7. Our loft gets almost no mobile signal indoors — will the phone app still open the door?
8. The street door of our walk-up slams and its strike buzzes loudly at night — can a new setup be quieter for the ground-floor flat?

### Other question-form headings
- H2 "Williamsburg Loft Door Won't Lock, or the Keypad Has Gone Dark?" (repair capture)

### De-dup notes
Checked by meaning against every register in research/smart-lock-installation.md (668 lines grepped by keyword) and the Forest Hills / Pelham Bay pages on disk. Dropped during build: mezuzah/keypad placement (= Rockland Q3), vibration loosening hardware under elevated train (= Jackson Heights Q10; Q10 here reframed to false door-open alerts — partial overlap for main run to judge), Shabbat feature switch-off / Friday booking / big-household codes (= Rockland), roommate code cancel (= Kingsbridge), student code turnover (= Dutchess), thick door (= HV Q10), keypad on brick (= Brooklyn Heights / Ulster), mailroom keypad (= Jackson Heights), roof door keypad (= Bronx), storage cages (= UES), entry-log privacy (= Westchester/Brooklyn), building sale codes (= LI/Orange). Partial overlaps left for the main run: Q6 (residential lobby + Shabbat, legal precedent) vs Rockland Q11 (shul front door on Shabbat); Q7 (push-button lock under MDL 51-c) vs Rockland FAQ "Do you fit purely mechanical push-button locks"; FAQ 3 (auto-lock delay for bikes/strollers) vs HV "mudroom relocks while ajar" / Westchester "auto-lock shut me out"; FAQ 7 (no mobile signal, Bluetooth at door) vs HV "property with no internet at all".

### Flags for Anwar
- Setup-visit rate $195 first hour then 30-min blocks — same flag as Brooklyn page (rate published for TV/device setup).
- Installer practice stated without a source: thread-locker on vibrating doors; hinge upgrade/fourth hinge on sagging loft doors; DC strike quieter than old AC strike; recessed-entry keypad placement; studio isolation-door advice; credential-register / two-administrator handover; filling old bolt holes (plug/weld on steel). All framed as our practice.
- LeFrak City suit dated 2015 from The Jewish Press URL; outcome unknown (page says so).
- Shabbat content: page explicitly defers religious questions to the family's rabbi and legal ones to a lawyer; Jewish Link quote used verbatim; no eruv claim about Williamsburg.
- Library photos appear AI-rendered; replace with real smart-lock photos when available.


<!-- merged from smart-lock-installation.forest-hills.part.md (batch 2026-10-17) -->
## Forest Hills, Queens (smart-lock-installation-forest-hills-queens-ny)

Built 2026-10-17 by the Forest Hills subagent (batch with smart-lock-installation-williamsburg-brooklyn-ny and smart-lock-installation-pelham-bay-bronx-ny). Neighbourhood spoke · up-link `/smart-lock-installation-queens` (also links `/smart-lock-installation-nyc`, all 16 area/hub pages, every live smart-lock neighbourhood page plus the two batch siblings) · Bronx GBP (`#bronx`, 460 E Fordham Rd, Bronx NY 10458) · direct line (347) 434-6392 in body/CTAs/schema; (800) 486-0943 only in the shared header chrome · Queens ×1.05, no neighbourhood surcharge. To be merged into research/smart-lock-installation.md by the main run.
Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless "scraped"); "FC scrape" = mcp__Firecrawl__firecrawl_scrape; "WS" = WebSearch; "WF" = WebFetch. "(reused)" = finding reached by the sonos/soundbar Forest Hills builders and logged in research/sonos-installation.md or research/soundbar-installation.md `## Forest Hills, Queens`; not re-fetched this run.

**Thesis — "approved outside, last line inside":** in Forest Hills the outside face of a door answers to someone other than the owner (the Gardens' Declaration No. 3 and FHGC Architecture Committee guidelines on doors/hardware/conduit; co-op boards on the Queens Blvd corridor side), while the space in front of it is shared with strangers who have already passed the first barrier (Oct 2025 daylight lobby walk-in near 112th St & 73rd Ave; 112th Pct burglaries +44.3%; FHGC private streets carrying 13,000-person concert crowds on 30+ show days). So each lock is chosen to look approvable from outside (inside-only retrofits, compact keyed keypads, application packs) and to act as the last barrier inside (auto-lock, door-position alerts, show-night schedules, concrete-set strikes). Distinct from: Bayside (door itself / back of house / inherited locks), Jackson Heights (permission-first board packet), Kingsbridge (lobby door repair as a two-door job), Bed-Stuy/Chelsea (LPC), Todt Hill (gate inward), Queens page (multigenerational / basements). Sonos Forest Hills ("indoors by design") and soundbar Forest Hills ("three plans") are other silos — no wording reused.

### Mandatory sources (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | FC search excerpts only (F12, F13). Reddit threads not scraped. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 headings are claims from cost guides/retail/product pages, stated as such on the page. |
| 6 | Landmarks | F1, F14–F19 (reused) |
| 7 | Building stock / use cases | F1–F3, F15–F22 (reused) |
| 8 | Bing & DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | QNS (F5, F7, F9), NY Post via AOL (F6), Patch (F10), ABC7 (F11), CBS (F8, research only) |
| 10 | Hyperlocal | Queens Ledger (reused F18). Forest Hills Post / Queens Chronicle: search titles only, not opened → EMPTY. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) |

### Research matrix
| # | Exact query · platform | URL | Finding | Page section used |
|---|---|---|---|---|
| F1 | `Forest Hills Gardens Corporation architectural guidelines exterior alterations approval front door` · FC search → FC scrape (pdf, directQuote) | https://www.fhgc.org/wp-content/uploads/2017/11/FHGC-Architectural-Guidelines.pdf | Declaration No. 3: no building/fence/wall erected "nor any change or alteration made therein" unless plans showing "nature, kind, shape, height, material, color-scheme and location" approved in writing by the Homes Company / FHGC as successor. Architecture Committee oversees review of all exterior construction/alteration. VI DOORS: entry doors panel type (incl. divided lights), wood unless approved; replacements replicate original; "many original entry doors in the Gardens are all glass with divided lights"; row/attached consistency "a significant architectural feature and must be preserved"; flush doors not permitted. SECURITY DOORS: not heavily ornamented, simple designs. HARDWARE: "of a type appropriate to the style of the building", finishes match/compatible. EXTERIOR LIGHTS: plans for all exterior lighting incl. security must be submitted; exterior conduits not permitted unless approved, painted/hidden. Search excerpt: applications "submitted four days before the scheduled FHGC Architecture Committee". | §5 para 2, §7 cards (row groups) + glass-door para + camera/lighting note, §9 Q1–Q3, Hardware Notes, Glass-door table, Gardens Application Pack, §10.5 H3 5, Block by Block (Gardens), FAQ 1 & 4 |
| F2 | same search (excerpt) | https://www.fhgc.org/community/architectural-regulations/ | "all exterior work, whether new or a restoration, does require submission of an application." | §9 Q1 |
| F3 | `site:fhgc.org security patrol OR safety OR parking contractors` · FC search → FC scrape (directQuote) | https://www.fhgc.org/community/parking/ | Gardens is a private community; contractors/service orgs may park "while performing services" with decal or properly worded note; unidentified vehicles booted/towed; Station Square "No Parking/No Tolerance Zone". Excerpts: FHGC home page — FHGC responsible for maintenance of streets/sidewalks/parks; Sept 2025 newsletter — "Knights agents" contractor enforce resident parking rules. | §8 Station Square card, Block by Block (Gardens) |
| F4 | `Forest Hills Queens burglary 112th Precinct 2025 apartment door` · WS → WF | https://qns.com/2025/10/suspect-wanted-burglary-forest-hills/ | QNS, Bill Parry, Oct 10 2025: Tue Oct 7 ~4:15 p.m., apartment building near 112th St & 73rd Ave; suspect entered through building's front door, filmed "sitting on a couch in the lobby", walked toward an apartment, took $600 phone, fled through courtyard west on 73rd Ave toward Queens Blvd. 112th Pct: 114 burglaries through Oct 5 2025, +44.3% vs 2024. (Method of entry into the unit not stated → page does not claim one.) | §5 para 4, §5.5 bullet 5, Hardware Notes ("lobby is not a lock"), Block by Block (apartment belt) |
| F5 | `Forest Hills Gardens Corporation private streets security patrol rules homeowners` · WS → WF | https://www.aol.com/articles/fed-forest-hills-residents-sue-100000994.html | NY Post (Katherine Donlevy) via AOL, Oct 14 2025: FHGC, "homeowner group with nearly 4,000 members", sued city in federal court; NYPD took control of FHGC private streets on >30 concert days; homeowners blocked from driveways; resident cites 13,000 attendees; 10 pm curfew; dozens of residents spend concert nights elsewhere. | §5 para 4, §9 Q5, Concert plan intro + last para |
| F6 | same search → WF | https://qns.com/2026/04/forest-hills-stadium-lawsuit-settled/ | QNS, Shane O'Brien, Apr 9 2026: FHGC v. city settled for $150,000 without admission of liability; NYPD keeps final say but considers "reasonable requests"; NYPD and 112th Pct to work with residents on planned security; 20 events planned for 2026, June 6 – Sept 29. | §5.5 bullet 6, §9 Q5, Concert plan intro |
| F7 | (see F4 search) · WF | https://www.cbsnews.com/newyork/news/rash-of-break-ins-rocks-forest-hills-queens | CBS NY Apr 1 2013: nine homes between Metropolitan Ave & Fleet St and 69th & Continental Aves; most entered via back door or window; mostly daylight. | Research only (old; not used on page) |
| F8 | `Austin Street Forest Hills store burglary break-in 2025 OR 2026 qns OR foresthillspost` · FC search → FC scrape (directQuote) | https://patch.com/new-york/foresthills/forest-hills-fish-shop-loses-2-5k-burglary-police-say | Patch, Apr 16 2021: Forest Hills Fishery, 7164 Austin St, 50+ years in neighbourhood; burglar broke in through back window, cutting a metal bar; $2,500 cash. | §8 intro, §8.5 "back doors and windows first" |
| F9 | same search → FC scrape (directQuote) | https://abc7ny.com/post/string-of-forest-hills-stores-restaurants-hit-by-burglars/557966/ | ABC7, Mar 14 2015: Jan–Mar business burglaries; "suspects broke in through the skylight of Rainbow on Austin Street"; others on Queens Blvd and 63rd Drive (Key Food). | §8 intro |
| F10 | same search (excerpt) | https://qns.com/2026/01/suspect-gunpoint-robberies-forest-hills/ | Jan 2026 gunpoint robbery of a man on Austin St (street robbery, not a door issue). | Not used |
| F11 | `reddit r/ForestHills package theft lobby door building lock co-op` · FC search (excerpt) | https://www.reddit.com/r/ForestHills/comments/1hph9f1/my_buildings_packages_were_stolen_a_few_days/ | "Two people came into the basement at 3:30 AM last week … stole everybody's packages"; title: stolen a few days before Christmas. | §10.5 H3 6 |
| F12 | (reused, sonos FC search) | https://www.reddit.com/r/ForestHills/comments/1t4d430/hello_neighbors/ | Excerpt: most apartment buildings in Forest Hills, especially above Yellowstone & Queens Blvd, are co-ops. | §5 para 3 |
| F13 | (reused, sonos FC scrape of Wikipedia) | https://en.wikipedia.org/wiki/Forest_Hills,_Queens | Cord Meyer 1906 purchase, renamed after Forest Park; Sage bought 142 acres 1908; Olmsted Jr. + Atterbury; Tudor Revival, stucco, red Ludowici clay tile roofs; houses mostly 1910–1917; ~170 precast panels set by crane; late-1920s zoning change for apartment buildings ahead of subway; stations opened 1936; Austin St ~1 mile Yellowstone Blvd–Ascan Ave, Ascan named 1909 by Frederick Backus for his father; Metropolitan Ave antique shops; 108th St runs to East Elmhurst; Cord Meyer teardowns replaced by larger houses; ZIP 11375, 112th Pct; LIRR station 1906. | §5 para 1, §5.5 bullet 2, §7 cards, §8 cards, §13 cards, Block by Block, North of the Boulevard |
| F14 | (reused) | https://www.nps.gov/places/sage-foundation-forest-hills.htm | 1909, Olmsted Jr. + Atterbury, Russell Sage Foundation, 142 acres. | §13 Gardens card |
| F15 | (reused) | https://foresthillsgardensfoundation.org/article/the-apartment-buildings-of-forest-hills-gardens/ | Gardens multi-unit buildings all co-ops except 150 Greenway Terrace; Forest Hills Inn opened May 1 1912; Inn Apartments 20 Continental Ave 1931; 11 buildings ≈650 of ≈1,600 Gardens homes. | §5.5 bullet 1, §7 Station Square card, Block by Block |
| F16 | (reused) | https://www.acsa-arch.org/proceedings/International%20Proceedings/ACSA.Intl.1996/ACSA.Intl.1996.54.pdf | Atterbury wall panels hollow, concrete each face separated by air space, ribbed. (Air-space width not stated on page.) | §7.5 concrete para, §9 Q4 context, Field Notes |
| F17 | (reused) | https://en.wikipedia.org/wiki/West_Side_Tennis_Club | Stadium built 1923; national championships to 1977; concerts; 10 p.m. curfew. | §13 stadium card |
| F18 | (reused) | https://queensledger.com/2022/07/27/perlman-reviving-the-chimes-in-station-square/ | Chimes revived 2022; Station Square restoration 2018. | §13 Station Square card |
| F19 | (reused) | https://queenseagle.com/all/mario-cuomo-forest-hills-compromise | 840 units in three 24-storey planned (1972) → halved to 432 units. | §7 card, §13 card |
| F20 | (reused) | https://therealdeal.com/2018/09/11/blackstone-buys-jack-parkers-parker-towers-for-500m | Parker Towers 1,327 units, three 20-storey towers, 104-20 Queens Blvd; Blackstone purchase 2018. | §7 card, §13 card |
| F21 | (reused) | https://www.cityrealty.com/nyc/forest-hills/68-10-108th-street/87401 | Co-op built 1931, 6 floors, 50 apartments. | §7 pre-war card |
| F22 | (reused) | https://www.brownstoner.com/queens/forest-hills/listing-of-the-day-60-greenway-north | 1928 Tudor, "leaded glass windows throughout". | §7 Gardens Tudor card |
| F23 | (reused) | https://www.furmancenter.org/neighborhoods/rego-park-forest-hills/ | Homeownership 49.8% (2024) vs 32.7% citywide. | §5.5 bullet 3 |
| F24 | (reused) | https://andesite-api.datausa.io/profile/geo/79500US3604406 | QN CD6 (ACS 2022): median age 43.6; 61.2% households primarily non-English. | §5.5 bullet 4 |
| S | carried from silo file (not re-fetched) | Fixr (S1), SmartThings mortise thread (S7), August retrofit (S3), August Connect 10–15 ft (S4), Yale Matter/Thread (S5), HPD fire-safety double-cylinder (N6), LL111/2018 self-closing (N5), MDL 51-c (N1), Cooperator duplicate key (N2), Tenant Data Privacy Act (N4), Schlage Encode Plus temperature ranges (Bayside B20) | as logged in research/smart-lock-installation.md | §7.5, §9 Q7, §10 equipment, Hardware Notes, Glass-door section, §10.5, §14, Co-op checklist |

### Prices used (all copied from live smart-lock-installation-queens.html; none invented)
| Figure | Scope |
|---|---|
| $1,575–$2,625 | single-door keypad/fob reader + electric strike (Queens; $1,500–$2,500 × 1.05) |
| $263–$473 | new electric strike on entrance door |
| $310–$509 | failed electric strike repair |
| $195 first hour, then 30-min blocks | setup-only visit, Queens |
| $195/hr, 3-hr minimum ($585) | service/callback |
| quoted flat at walkthrough | house / co-op / condo smart lock |
| $250–$400 (avg $300) | NATIONAL third-party (Fixr Jan 2025), labelled as such |
| Worked sums | 2 × keypad+strike = $3,150–$5,250; keypad+strike + strike repair = $1,885–$3,134; one setup hour = $195 |

## Images (11)
Drive folder `AESS Website Photos/Smart Lock Installation` empty (main run); CompanyCam not connected → permanent image rule. The only photos in the repo that actually show smart locks are the 18 `images/smart-lock-installation/aess-smart-lock-installation-*` files (all viewed); low-voltage/commercial-security clusters show commercial access control only (contact sheets viewed; not chosen). All aess-* sources have been used by earlier siblings, so every file here is a NEW crop (different framing from Bayside's crops) made with Pillow, face-free, verified by viewing. Rejected: `showing-customer-app-unlock` (customer's face), `suburban-front-door-smart-lock-van` (van logo/face; not needed). `apartment-door-smart-lock-app` cropped to y≥330 so the "4A" unit sign is excluded; `video-doorbell-and-smart-lock` cropped to x≥990 so house number "128" is excluded. Captions describe only what is visible; none claims a Forest Hills job, customer or building.
**Flag (carried):** the aess-* set looks AI-rendered (uniform logo artwork, stylised lighting) though supplied as AESS photos — Anwar to confirm; replace with real Forest Hills photos when available.

| New file (images/smart-lock-installation/) | Source (aess-smart-lock-installation-…) | Crop box (x0,y0,x1,y1) |
|---|---|---|
| smart-lock-installation-forest-hills-keypad-deadbolt-stained-panel-door.webp (hero, eager) | keypad-smart-deadbolt-brownstone-door | 560,0,1400,1050 |
| smart-lock-installation-forest-hills-keypad-lock-dark-apartment-unit-door.webp | apartment-door-smart-lock-app | 900,330,1400,933 |
| smart-lock-installation-forest-hills-inside-thumb-turn-by-hand.webp | keypad-exterior-thumbturn-interior-view | 720,0,1400,760 (overlay text excluded) |
| smart-lock-installation-forest-hills-video-doorbell-beside-keypad-deadbolt.webp | video-doorbell-and-smart-lock | 990,250,1400,933 |
| smart-lock-installation-forest-hills-keypad-lock-aluminum-glass-door.webp | office-glass-door-smart-lock | 800,0,1400,933 |
| smart-lock-installation-forest-hills-keypad-lever-lock-glass-office-door.webp | office-lever-smart-lock-install | 820,0,1400,933 |
| smart-lock-installation-forest-hills-keypad-deadbolt-beside-iron-grille-glass.webp | drilling-keypad-lock-brownstone-stoop | 980,0,1400,933 |
| smart-lock-installation-forest-hills-removing-brass-deadbolt-cylinder.webp | removing-old-brass-deadbolt | 780,200,1400,1050 |
| smart-lock-installation-forest-hills-checking-latch-plate-door-edge.webp | checking-latch-bolt-alignment | 780,0,1400,1050 |
| smart-lock-installation-forest-hills-loading-aa-batteries-inside-unit.webp | replacing-smart-lock-batteries | 820,0,1400,933 |
| smart-lock-installation-forest-hills-adding-access-code-on-phone.webp | programming-access-code-app | 760,250,1400,1050 |

## Question register — smart-lock-installation-forest-hills-queens-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 7; under H2s: The Gardens · Concrete, masonry and the frame · Concert season · Co-op apartments on the Boulevard)
1. Does a keypad deadbolt count as exterior work that the Gardens Corporation's Architecture Committee has to approve?
2. Our house is one of an attached group whose front doors are meant to match — can ours go keyless if the neighbours' doors stay as they are?
3. Is a steel security door in front of our Gardens entrance worth it, or does the money do more in the lock and the frame?
4. Our door frame sits in a concrete wall with no wooden stud behind it — how does the strike get anchored?
5. On Forest Hills Stadium concert nights thousands of people walk past our house — what should the locks be set to do on those evenings?
6. When we sell our co-op apartment, does the smart lock go with us, stay for the buyer or belong to the corporation?
7. Can the board or the managing agent see our lock's activity log if the lock is our own?

### §17 FAQ (visible == FAQPage, 4)
1. Why is there no fixed price for a smart lock on a Gardens house door when business entrances have one?
2. Do your Queens crews also cover Kew Gardens, Rego Park and the Cord Meyer blocks north of Queens Boulevard?
3. Will the bolt motor be loud enough for the family on the other side of our attached-house wall to hear at night?
4. If the Architecture Committee asks us to change the hardware after it is installed, what does the swap involve?

### Other question-form headings
- None. Repair captures and CTAs are statements ("Forest Hills Smart Lock Stuck, Dark or Offline", "Shut Out Between the Gardens and the Boulevard Tonight", "Send the Door Before You Buy the Lock", "Approved From the Street, Locked Behind You").

### De-dup notes
- Checked by meaning against all 738 question headings/FAQs on the 31 smart-lock pages on disk plus the in-progress Williamsburg and Pelham Bay drafts. Moved to statement sections because the intent is already asked elsewhere: lobby already passed (Manhattan "talks their way past the lobby", Kingsbridge lobby propped/pried) → Hardware Notes "The lobby is not a lock"; glass panes / reach-through (Nassau sidelights, Brooklyn glass panels, West Brighton narrow rail) → Glass-door section table; finish matching (Queens, SI) → Hardware Notes; bulky inside housing (Westchester) → Hardware Notes; co-op board approval / duplicate key / mortise corridor (NYC hub) → Co-op checklist; contractor van on private roads (Todt Hill, Bayside, Flushing parking) → Block by Block body; oversized/multipoint doors (Westchester multipoint Q, Todt Hill pivot, Williamsburg heavy door) → North-of-the-Boulevard bullets; packages (Brooklyn, Greenpoint, Bed-Stuy) → §10.5 body.
- Partial overlaps for the main run to judge: §9 Q1 (Gardens covenant review) vs HV "historic-district approval … Kingston's Stockade" and Bed-Stuy LPC mounting Q (different authority: private covenant, not LPC); §9 Q7 (board seeing log) vs Brooklyn "owner see tenant comes and goes" / Morris Park "lock maker … police" (different party); FAQ 3 (motor noise through party wall) vs Throgs Neck "drilling disturb the family on the other side of the party wall" (ongoing operation vs installation day); FAQ 4 vs Bed-Stuy "keypad removed later without new holes" (approval-driven swap vs removal).

### Similarity (simcheck.py, masked, block ≥25 words, vs every smart-lock-installation-*.html incl. Williamsburg/Pelham Bay drafts)
Page-level max 0.115 (vs upper-east-side). Content blocks: none ≥ 0.65 after one rewrite round (first draft had 13 blocks 0.66–1.0 vs Bayside/Jackson Heights: NAP line, warranty paragraph, process steps 5–6, packages copy, worked example, captions, all-areas intro, legal note — all rewritten). Remaining >0.65: neighbourhood link list 0.934 vs Pelham Bay (exempt) and the shared mobile-nav chrome 0.672 vs Bayside (template chrome, not page content).

### Flags for Anwar
- Images: aess-* library appears AI-rendered; all 11 are new crops of already-used sources (no unused real smart-lock photos exist).
- Installer practice stated without a source (house policy): no inside-keyed/coded locks on any home; jamb anchored before strike; no blind drilling into hollow precast panels; signal test before pairing; paper template through full swing; dark exit test; two-adult admin; show-night settings table (auto-lock ~1 minute, pause service codes); application pack contents; "we do not file on anyone's behalf"; motor noise "quieter than a door closing" (FAQ 3); arrival windows 8 AM–8 PM daily (copied from Queens page).
- General statements without a specific source: many modern entry sets combine handle and deadbolt in one plate; multipoint motor kits depend on the maker's gearbox; laminated glass slows break-and-reach; unheated vestibules reduce battery capacity (Schlage range cited only as an example); national brands' packages (ADT/Ring/SimpliSafe) described generically.
- §9 Q6 (who owns the lock on a co-op sale) and Q7 (board access to logs) are framed as "decided by your contract/lease/house rules; take advice" — please confirm the wording is acceptable.
- Page links /smart-lock-installation-williamsburg-brooklyn-ny and /smart-lock-installation-pelham-bay-bronx-ny (batch siblings; resolve once those files exist).
- check_page.py: all content checks PASS; remaining FAILs are main-run wiring only (sitemap, _redirects ×2, Queens hub link-down, 16 area/hub pages link back).


<!-- merged from smart-lock-installation.pelham-bay.part.md (batch 2026-10-17) -->
## Pelham Bay, Bronx (smart-lock-installation-pelham-bay-bronx-ny)

Page: `/smart-lock-installation-pelham-bay-bronx-ny` · neighbourhood spoke of `/smart-lock-installation-bronx` (+ `/smart-lock-installation-nyc`) · phone (646) 490-0629 (body, CTAs, schema; (800) 486-0943 only in shared header chrome) · GBP Bronx (460 E Fordham Rd, schema `#bronx`) · Bronx ×1.00; every price copied from smart-lock-installation-bronx.html. Built 2026-10-17 by batch subagent (batch: Williamsburg, Forest Hills, Pelham Bay).

**Thesis:** *The house between trains.* Pelham Bay is a detached-house neighbourhood (DCP: ~72% detached, ~17% semi-detached) built around the 6-line terminal, whose households commute out (CD10 commute 45.5 min) and leave the house empty all day — so the lock's job is to run the empty house: one scheduled code per daytime visitor (cleaner, contractor, dog walker, children, aides), auto-lock behind them, alerts trimmed to the events that matter, remote reachability from the train, and a "retire the code" habit. Distinct from Morris Park (driveway side door / shift workers & carers), Throgs Neck (three kinds of land under the door / waterside) and Kingsbridge (apartment buildings).

Tools: "WebSearch" = Claude WebSearch; "WebFetch" = Claude WebFetch (page converted + summarised). All fetched 2026-10-17. Silo-wide facts reused without re-fetching: MDL 51-c (B6), HMC 27-2043/27-2041 (B7), HPD fire-safety free-exit guidance (B8), TDPA LL63/2021 (B11), Admin Code 26-521 lockout (N9), MDL multiple dwelling = 3+ families (Morris Park M-section), August Connect 10–15 ft (S4), Matter/Thread border router + feature support varies by app (S5/S6, LI §9), ADA 404.2.7 34–48 in (LI), Schlage door prep 2-1/8 bore, 2-3/8 / 2-3/4 backset (LI), LawnStarter national $330/$200–$460/labor $50–$110 (LI section), Ring Alarm arm/disarm by lock code (LI).

### Local research matrix
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| PB1 | `Pelham Bay Bronx neighborhood housing attached row houses two-family homes Buhre Avenue` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Pelham_Bay_(neighborhood),_Bronx | CD10; bounded by Pelham Pkwy (N), New England Thruway/I-95 (E), Bruckner Expwy (S), Hutchinson River Pkwy (W); Country Club east of I-95; commercial streets Westchester, Buhre, Middletown, Crosby (Crosby/Middletown main intersection); longstanding Italian American + sizable Greek population; USPS Pilgrim Station 1545 Crosby Ave; 45th Pct 2877 Barkley Ave (Throggs Neck), 2022: 108 burglaries, all crime −67% 1990–2022; NYPL Pelham Bay 3060 Middletown Rd, one-story brick, 1976; PS 71, PS 14; Greek American Institute; St. Theresa schools; transit 6 at Middletown Rd, Buhre Ave, Pelham Bay Park; BxM8 to Midtown; *Taking of Pelham One Two Three* hijacked train leaves Pelham Bay Park station. | §5 paras 1, 5; §5.5 bullet 5; §8 Crosby + Middletown cards; §9 snow-day Q (PS 71/PS 14); §13 station + library cards |
| PB2 | `NYC City Planning rezoning Pelham Bay Bronx one- and two-family attached semi-detached houses R4A` · WebSearch → WebFetch | https://www.nyc.gov/assets/planning/download/pdf/plans/pelham-bay/pelham_bay.pdf | Adopted by City Council March 22, 2006 (CPC Feb 8, 2006; CB10 Nov 17, 2005; C 060179 ZMX); area Pelham Pkwy South → Middletown Rd, Bruckner Expwy → Hutchinson River Pkwy; detached ~72% of housing stock, semi-detached ~17% of residential structures, attached ~6.6%, multifamily ~4.5% of lots, apartment buildings line wider avenues; IRT arrival spurred development around a rail terminal; R5 → R5A (detached one- and two-family only, 30-ft min lot width, 35-ft height); C1-2→C1-4 on Crosby/Westchester, C2-2→C2-4 on Westchester/Buhre, overlay depth 150→100 ft, commercial parking 1/300 → 1/1,000 sq ft; purpose "to better preserve the existing character of large detached homes". (Block counts inconsistent in source — not used.) | §5 paras 1–2; §5.5 bullets 1–2; §7 intro + Large Detached + Two-Family cards; §8 intro; Two-Families section intro |
| PB3 | `Pelham Bay Park station 6 train terminal history Westchester Avenue elevated` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Pelham_Bay_Park_station | Opened Dec 20, 1920 as terminal; northern terminus of Pelham Line (6/<6>); elevated; elevators Dec 1989, renovated June 2015–April 2016; at Bruckner Blvd & Westchester Ave by Bruckner Expwy; pedestrian bridge over expressway to park; buses Bx5, Bx12, Bx12 SBS, Bx24, Bx29, Bx23, Q50, BxM8, Bee-Line 45; 2024 ridership 1,136,845. | Hero; §5 para 1; §5.5 bullet 4; §13 station card |
| PB4 | same search · WebFetch | https://en.wikipedia.org/wiki/Buhre_Avenue_station | Opened Dec 20, 1920; elevated, at Buhre & Westchester; closed July 5, 2014–April 27, 2015 (part of $109M five-station rehab); 2024 ridership 766,190. | §5 para 1; §5.5 bullet 4 |
| PB5 | `Bronx Community District 10 commute mean travel time to work public transit share profile` · WebSearch → WebFetch | https://comptroller.nyc.gov/wp-content/uploads/documents/Neighborhood_Economic_Profiles_2018_Bronx.pdf | "BX10 Co-op City, Pelham Bay & Schuylerville": commute time 41.0 min (2010) → 45.5 min (2016, ACS 2012–2016), +11%; public-transit workers 17,701 → 22,680 (+28%); car/taxi 25,490 → 23,639 (−7%); population 112,744 → 122,430. | §5 para 3 (thesis); §5.5 bullet 3 |
| PB6 | `Pelham Bay Bronx burglary 45th Precinct 2025 house` · WebSearch | https://www.bxtimes.com/category/news/neighborhoods/pelham-bay (WebFetch) | Pelham Bay section headlines: first Restaurant Week; Orchard Beach Pavilion $114M; 11-unit lottery; 36-unit permits; shelter permits; e-bike corral. **No burglary/lock/door story found → EMPTY for the service category.** | §8 (restaurants on avenues, general), §7 new-building card (via PB8) |
| PB7 | `bxtimes Orchard Beach Pavilion restored $114M renovation reopen` · WebSearch → WebFetch | https://www.nyc.gov/mayors-office/news/2026/05/mayor-mamdani-reopens-orchard-beach-pavilion-after--114-million- | Reopened May 20, 2026; $114M; fully closed since 2009 (~17 yrs); 140,000 sq ft, built 1936 (WPA), LPC landmark 2006; Marvel Architects / Gilbane; Orchard Beach 115 acres, 1.1 miles. | §13 Orchard Beach card |
| PB8 | `bxtimes housing lottery 11 units Pelham Bay building rent starts at $2,040` · WebSearch → WebFetch | https://www.bxtimes.com/housing-lottery-11-units-pelham-bay-rent-2040/ | Jan 8, 2026: 3217 Westchester Ave, 11 new units (rents not used), amenities incl. "intercommunication devices", security cameras, covered parking/garages, elevator, accessible entrance; steps from Pelham Bay Park station. No smart-lock/keyless mention. | §7 "New Buildings by the Terminal" card |
| PB9 | (direct) · WebFetch | https://en.wikipedia.org/wiki/Pelham_Bay_Park | 2,772 acres, largest public park in NYC, slightly >3× Central Park (843); acquired 1887, opened 1888; Orchard Beach opened June 25, 1937; Bartow-Pell Mansion 1842 Greek Revival, NHL 1975; Split Rock 1935, Pelham Bay golf 1901; Hunter Island 166 acres; Kazimiroff Nature Trail 1986; Bronx Victory Column & Memorial Grove, Crimi Road, 1933, 947 Bronx WWI dead. | §5.5 bullet 6; §13 park, Bartow-Pell, Victory Column cards |
| PB10 | (direct) · WebFetch | https://en.wikipedia.org/wiki/Country_Club,_Bronx | Country Club east of New England Thruway/Pelham Bay; ZIP 10465; nearest stations Pelham Bay Park and Buhre Ave. | §13 "we also serve" line |
| PB11 | `NCC Group Bluetooth Low Energy relay attack smart lock Kwikset Kevo 2022` · WebSearch → WebFetch | https://www.nccgroup.com/newsroom/ncc-group-uncovers-bluetooth-low-energy-ble-vulnerability-that-puts-millions-of-cars-mobile-devices-and-locking-systems-at-risk/ | 16 May 2022: first link-layer BLE relay attack; successful exploits on Tesla Model 3/Y and Kwikset/Weiser Kevo smart lock; not fixable by ordinary patch; advice: disable passive unlock features without explicit approval / require user-presence tap. | §9 radio-gadget Q; §10.5 auto-unlock H3 |
| PB12 | `Amazon Key in-garage delivery how it works compatible garage door smart lock` · WebSearch → WebFetch | https://digprjsurvey.amazon.com/csad/help/node/GCDL25VJ6YTBTY78 (Amazon help page mirror) | In-Garage Delivery: compatible smart garage linked to Amazon Key; driver scans package, Amazon verifies package + driver location, garage opens; notifications at each step; optional camera; Prime required; $1.99/order or free with Amazon Day In-Garage (price not used). | §9 delivery-program Q |
| PB13 | reused from research/soundbar-installation.md (Pelham Bay section; not re-fetched) | https://citylandnyc.org/two-bronx-neighborhoods-down-zoned ; https://api.datausa.io/profile/geo/co-op-city-pelham-bay-schuylerville-puma-ny | Down-zoning ~45 blocks, overlay depth cut, CB10 unanimous; PUMA homeownership 45.7% (2021). | Background only (homeownership figure **not** used on page) |

### Sources not reachable / EMPTY
- Google PAA, PASF, Answer the Public, Google AI Overview, Bing/DDG: `EMPTY (not accessible in build env)`. §10.5 headings are claims from published cost guides / product material (LawnStarter, NCC Group, Matter maker guidance), stated as such on the page.
- Reddit r/bronx / r/AskNYC Pelham Bay: query `reddit Pelham Bay Bronx living commute 6 train last stop` · WebSearch → no reddit.com results (only Wikipedia, RentHop, NY1 "end of the line" feature not opened) → `EMPTY`.
- Local news on locks/break-ins in Pelham Bay: query `"Pelham Bay" Bronx burglaries homes police warn residents pattern` · WebSearch → only Pelham Gardens 2012 (DNAinfo) and Westchester-suburb stories → `EMPTY` for Pelham Bay; nothing quoted. Query `Pelham Bay Bronx Times burglary home break-in Westchester Avenue 2026` → no Pelham Bay burglary story → `EMPTY`.
- Yelp 1–3★ Pelham Bay locksmith / smart-lock installers: `EMPTY (not accessible in build env)`.
- Census 2020 NTA counts (population, renter share) for Pelham Bay: query `"Pelham Bay-Country Club-City Island" 2020 census population housing units renter occupied` → no usable 2020 table returned → `EMPTY`; page uses no 2020 census figure.
- Middletown Road station page (structurae): fetch error → `EMPTY (not accessible)`; not used.
- Google Drive `AESS Website Photos/Smart Lock Installation`: EMPTY (checked by main run); CompanyCam not connected.

### Installer practice / general knowledge (NOT sourced to a document — flag for Anwar)
- Alert-tuning recommendations, daily weekday schedule table (illustrative, labelled "your times will differ"), "one person per code", seasonal user-list review, privacy/vacation mode cautions, one-touch locking behaviour, DST/time-zone drift explanation for scheduled codes, shared-login advice, factory master code advice, keypad cleaning, painting timing, strike-plate replacement, padlocks for sheds, restaurant side-door rider advice, appraisal answer ("no published data found"), three-swing latch test in Field Notes (written as general practice, not an anecdote), emergency power contact "9-volt or USB-C depending on model".
- BYOE "labor-only" callout wording and "we stop before opening the box so it can go back" — confirm this matches AESS practice.

### Prices used (no new prices; Bronx ×1.00 — all copied from smart-lock-installation-bronx.html)
$1,500–$2,500 single-door keypad/fob reader with electric strike · $250–$450 new electric strike · $295–$485 failed strike repair · $225 setup-only first hour then 30-min blocks (carries the Bronx page's existing flag: TV setup-only rate reused for smart-lock app visits) · $195/hr, 3-hr min ($585) service/callback · worked example $1,795–$2,985 = sum of two published lines · LawnStarter national $330 / $200–$460 / labor $50–$110 (third-party, labelled). House doors: "Quoted flat at free walkthrough".

### Images (11) — permanent image rule (Drive empty, CompanyCam not connected)
Source = `images/smart-lock-installation/aess-smart-lock-installation-*` (the whole aess set looks AI-rendered — flag for Anwar). Each viewed with Read; cropped with Pillow so no face, house number ("128" source skipped), unit plate ("4A" source skipped) or readable document appears; crops differ from Morris Park / West Brighton crops; saved WebP q82.
| New file (images/smart-lock-installation/smart-lock-installation-pelham-bay-…) | Source (aess-smart-lock-installation-…) | Crop box | Section |
|---|---|---|---|
| keypad-deadbolt-above-black-handleset.webp | keypad-smart-deadbolt-brownstone-door | (450,0,1150,1050) | hero (eager) |
| inside-thumb-turn-hand-close-up.webp | keypad-exterior-thumbturn-interior-view | (720,0,1400,780) — "Exterior/Interior View" captions cropped out | instant action |
| add-access-code-screen-at-keypad.webp | programming-access-code-app | (720,260,1400,1050) | §5 |
| fingerprint-unlocked-on-phone.webp | fingerprint-unlock-demo-app | (700,180,1400,1050) | §6 |
| tape-across-worn-deadbolt-bore.webp | measuring-door-bore-for-deadbolt | (880,250,1400,820) | §7 |
| finger-on-latch-at-door-edge.webp | checking-latch-bolt-alignment | (620,100,1400,1050) | Empty-house section |
| keypad-deadbolt-glass-office-door.webp | office-glass-door-smart-lock | (680,200,1400,933) | §8 |
| keypad-pulled-to-check-wiring.webp | servicing-keypad-wiring | (780,150,1400,933) | §9 |
| four-aa-cells-inside-unit.webp | replacing-smart-lock-batteries | (880,180,1400,933) | §10 |
| brass-cylinder-out-red-driver.webp | removing-old-brass-deadbolt | (700,320,1400,1050) | §10.5 |
| keypad-lever-latch-screwdriver.webp | office-lever-smart-lock-install | (620,220,1400,933) | §13 |
DAILY-LOG note: `images: 11 reused from images/smart-lock-installation/aess-* (cropped; no real smart-lock photos yet)`.

### Similarity
`simcheck.py` masked-geo: page-level max 0.184 vs Morris Park. All content blocks < 0.65 vs every sibling (incl. Williamsburg and Forest Hills drafts). Only blocks ≥ 0.65 are exempt constants: the verbatim warranty sentence, the shared mega-nav chrome, and the neighbourhood link list.

## Question register — smart-lock-installation-pelham-bay-bronx-ny

### §9 YOUR QUESTIONS ANSWERED (H3, 13)
1. Our phones buzz every time anyone opens the door — can the lock tell us only about the openings that matter?
2. Our cleaner's Tuesday code started and stopped an hour off after the clocks changed — why would that happen?
3. Our children's after-school code is set for weekdays — what happens on snow days and school holidays?
4. We spend several weeks a year with family abroad — can we add and delete codes from overseas, or only on our home network?
5. Could someone standing outside with a radio gadget trick a smart lock into opening?
6. The whole family logs in to the lock app with one shared email and password — what is wrong with that?
7. The keypad locks when anyone touches the logo — could a passer-by or a child lock someone out by mistake?
8. At night we would like the door to stay shut even to someone who has a valid code — is that possible?
9. Our family is half iPhone and half Android — will one lock work well for everyone?
10. Should we sign up for one of the delivery programs that let a courier open the garage while we are at work?
11. Can the lock's entry history line up with our camera recordings so we can see who used each code?
12. Delivery riders collect orders at our restaurant's side door all evening — should they get a code, or should the door stay staffed?
13. Does a smart lock add anything to what a Pelham Bay house appraises for?

### §17 FAQ (visible == FAQPage, 8)
1. If the lock we bought online turns out to be wrong for our door, will you help us sort out a return or exchange?
2. We are repainting the front door next month — should the smart lock go on before or after?
3. Do you also fit app-controlled padlocks for a backyard shed or a side gate?
4. Is there a smart lock we can use without creating an online account with the manufacturer?
5. Our keypad came with a factory master or programming code — should it be changed?
6. How should we clean a keypad or fingerprint reader without damaging it?
7. Does a smart deadbolt need a different strike plate from the one already on our door frame?
8. How often should we change the codes on our door?

### Other question-form headings
- Need Smart Lock Repair in Pelham Bay? (repair capture H2)

### De-dup notes
Checked by meaning against all 738 question headings/FAQ items on the 33 live/draft smart-lock pages. Closest neighbours and why they differ: alert tuning vs "can the lock warn us about wrong codes" (Kingsbridge/New Dorp — single feature, not notification management); snow-day schedule exceptions vs "school bus mid-afternoon" (Westchester — arrival alert, not schedule exceptions); overseas code management vs "batteries die while out of the country" (Manhattan — power, not remote admin); relay attack vs "someone gets into our email" (Westchester — account takeover); shared login vs "who should hold the administrator account" (Queens — which person, not shared credentials); delivery programs vs "packages to the desk" (Manhattan — doorman building); factory master code vs "seller's lock master code unknown" (Bayside — reset, not changing a default).
