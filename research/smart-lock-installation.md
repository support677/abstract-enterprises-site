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
