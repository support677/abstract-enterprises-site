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
