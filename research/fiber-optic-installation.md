# Research — Fiber Optic Installation silo

Built 2026-10-14 (daily run, first page of the silo: fiber-optic-installation-nyc). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Sources that could not be opened in the build environment are written `EMPTY (not accessible in build env)` — nothing below is inferred to fill a gap.

## Silo-wide findings

### 1. Reddit
- Query: `reddit AskNYC fiber optic internet building wiring installer` · Firecrawl web search (search-result excerpts only; Firecrawl refuses to scrape reddit.com, so full threads were **not** read).
  - https://www.reddit.com/r/verizon/comments/1u083m9/how_do_i_get_fiber_in_my_building_nyc/ — excerpt: poster "called standard support and got the usual runaround they told me there was nothing I could do because the building isn't wired for it." → NYC hub, §5 THE NEIGHBORHOOD (building-not-wired pain) and §9 Q "My building isn't wired for fiber — what can actually be done?"
  - https://www.reddit.com/r/AskNYC/comments/1tez8o2/incorrectly_wired_internet_cables_in_building/ — excerpt: "Its on the ISP to wire your building/apartment. If it's not wired correctly they need to run new wires." → NYC hub, §10.5 reality check (who owns inside wiring: ISP drop vs owner backbone).
  - https://www.reddit.com/r/AskNYC/comments/1tam55f/what_does_the_verizon_fios_installation_look_like/ — excerpt: "Assuming your building is pre-wired for Fios, then the Verizon installer will run a shielded fiber optic cable from the hallway, into your…" → NYC hub, §9 (ISP drop vs private fiber distinction).
  - https://www.reddit.com/r/AskNYC/comments/1ouuv8z/what_are_you_paying_for_home_internet/ — excerpt only (residential pricing chatter, $40/mo Spectrum example). Not used (consumer ISP pricing, not installation).
- Query: `site:reddit.com fiber install NYC apartment building landlord fiber internet` · WebSearch → no reddit.com results returned. EMPTY.

### 2. Google People Also Ask — EMPTY (not accessible in build env)
Substituted: question-style headings that appear on ranking pages for the queries below (recorded as such, not as PAA):
- Query: `fiber optic installation people also ask how long does fiber installation take commercial building` · Firecrawl web search.
  - https://www.atlantech.net/blog/install-fiber-optic-internet-timeline — "How long does it take to install fiber optic internet in my commercial building?"; answer depends on distance to nearest fiber, building access; one customer waited 15 months and could not get fiber. → NYC hub §9 timeline question; §10.5.
  - https://multifamilyresources.quantumfiber.com/fiber-installation-journey/ — multifamily stages: off-site construction 30 days, on-site 30 days, implementation/activation 40–60 days. → NYC hub §10.5 (carrier timelines vs private backbone timelines).
  - https://www.t-mobile.com/home-internet/fiber/fiber-optic-installation — in-home install "can take up to 4 hours". https://www.att.com/support/article/internet/KM1066216/ — "four to six hours". → NYC hub §10.5 (residential ISP install time ≠ building backbone time).

### 3. Google PASF — EMPTY (not accessible in build env)

### 4. Answer the Public — EMPTY (not accessible in build env)

### 5. Google AI Overview — EMPTY (not accessible in build env)
Substituted with the claims cost-guide and competitor pages actually make (these feed the §10.5 Reality Check; each is quoted as the page states it):
- Query: `fiber optic installation NYC cost questions` · WebSearch → https://www.streamlinetelecom.com/fiber-optic-services-for-new-york-city (Firecrawl search excerpt): "Fiber-optic cable costs anywhere from $1-6 per linear foot to install". Firecrawl summary: NYC metro fiber firm; installation, testing, splicing, maintenance. → NYC hub §10.5 H3 on per-foot pricing.
- Query: `Angi OR HomeAdvisor OR Fixr cost to install fiber optic cable per foot` · WebSearch → no Angi/HomeAdvisor/Fixr page returned. Angi/HomeAdvisor/Fixr pages: EMPTY. Result used instead: https://thenetworkinstallers.com/blog/fiber-optic-installation-cost/ (WebFetch): cites Fiber Broadband Association 2025 report — underground median $18.00/ft (IQR $11.50–$25.00), aerial median $8.00/ft ($4.90–$11.50); fusion splice $30–$75, mechanical $15–$40 (citing Ring and Ping); testing/documentation ≈5% (citing Automation World). → NYC hub §10.5 (outside-plant per-foot numbers don't describe inside-building backbone).

### 6/7. Landmarks / use cases — see area sections.

### 8. Bing & DuckDuckGo — EMPTY (not accessible in build env)

### 9. Local news / trade press
- Query: `NYC fiber optic installation news 2026 building broadband` · WebSearch.
  - https://espanol2.verizon.com/about/node/141763 (WebFetch) — Verizon: almost 89 million feet (nearly 17,000 miles) of fiber installed in NYC; premises passed at end of 2013: Manhattan 94%, Bronx 90%, Queens 90%, Brooklyn 89%, Staten Island virtually all; FiOS available to 60,000+ public-housing units; city approved microtrenching after a pilot. Page undated; data through end-2013. → NYC hub §5.5 stats (stated as Verizon's figures as of end-2013).
  - https://bbcmag.com/nycedc-launches-second-round-of-connectnyc/ (WebFetch) — ConnectNYC (NYCEDC, July 2013): free fiber construction for NYC companies <500 employees in unwired/underwired buildings; 24 businesses connected in round one; up to $14M of fiber wiring across five ISPs. → NYC hub §5 (history: under-wired commercial buildings were a recognised city problem).
- Query: `New York City Internet Master Plan fiber households without broadband statistic` · WebSearch → https://council.nyc.gov/data/internet-access/ (WebFetch): 8.1% of households no internet access (2021); 24.5% no broadband subscription (cable, fiber or DSL); 19 community districts exceed 33%; Melrose–Mott Haven–Port Morris 44%. → NYC hub §5.5 stats.
- Query: `Big Apple Connect NYCHA free internet developments number of residents 2025` · WebSearch → https://www.nyc.gov/mayors-office/news/2025/09/mayor-adams-extends--big-apple-connect--program--continues-to-pr (WebFetch): Sept 29 2025; 220 NYCHA developments, ~150,000 households, ~330,000 residents; extended through June 2028; Spectrum and Optimum. → NYC hub §5.5.
- Query: `site:reddit.com fiber install NYC apartment building landlord fiber internet` · WebSearch → https://www.nyc.gov/assets/hpd/downloads/pdfs/services/residential-broadband-installation.pdf (WebFetch): HPD "Broadband in Affordable Housing" — broadband required in units for all new construction; new fiber needs fiber in the street and an accessible basement entry point; FCC rulings ban exclusive and graduated revenue-share agreements and sale-leaseback of inside wiring. → NYC hub §7 (residential multifamily), §9.
- Same query → https://www.nycmesh.net/building (WebFetch): NYC Mesh works with management companies, helps with lease and insurance paperwork; fiber connections require a fiber lease. → NYC hub §7.5 (approvals are paperwork, not just cable).

### 10. Hyperlocal — see area sections.

### 11. Yelp 1–3★ — EMPTY (not accessible in build env)
- Query: `"fiber optic" contractor New York yelp reviews` · WebSearch → no yelp.com results returned.

### Technical / code sources (silo-wide)
- Query: `NEC Article 770 OFNP OFNR OFN optical fiber cable plenum riser rating` · WebSearch → https://www.cablinginstall.com/design-install/cabling-installation/article/16465302/select-properly-listed-optical-fiber-cables (WebFetch): OFNR riser (UL 1666), OFNP plenum (NFPA 262 / UL 910), OFNG/OFN general purpose single-floor; higher listing may substitute for lower. → NYC hub §10 EQUIPMENT, §7.5, FAQ.
- Query: `fiber optic bend radius 10 times cable diameter TIA-568 pulling tension installation` · WebSearch → https://www.foa.org/tech/ref/install/installcbl.html (WebFetch): bend radius 20× diameter under tension, 10× after install; pull by aramid strength members; swivel pulling eye; figure-8 layout; service loops on vertical runs. → NYC hub §12 process, §7.5 methods.
- Query: `single-mode vs multimode fiber backbone office building OM4 OS2 distance` · WebSearch → https://www.ampcom.com/blogs/industry-insights/how-to-choose-the-right-fiber-type-singlemode-vs-multimode (WebFetch): OS2 ~9 µm, 1310/1550 nm, 10 km+ at 10G; OM3 50 µm ~300 m at 10G, ~100 m at 40/100G SR4; OM4 ~400–550 m at 10G, ~150 m SR4; OM5 niche (SWDM). → NYC hub §10, §9.
- Query: `reddit fiber optic cabling contractor NYC office building riser` · WebSearch → https://nyflnerds.com/structured-cabling-queens-riser-cabling-nyc/ (WebFetch): confirm riser space, after-hours/escort access, firestopping at every floor penetration, CMR/CMP ratings, management coordination, elevator/loading dock, documentation. → NYC hub §8.5 compliance.
- Query: `NYC Department of Buildings low voltage work permit not required under 50 volts fiber cabling firestopping` · WebSearch → https://unifinerds.com/low-voltage-wiring-codes-nyc-contractors/ (WebFetch): permit need depends on scope/filing; "permit not required" ≠ "no requirements"; firestop unsealed penetrations a common inspection failure. → NYC hub §8.5. (Site's own structured-cabling-pricing page states low-voltage cabling under 50 V does not need a DOB permit — existing site content, kept consistent.)
- Query: `60 Hudson Street 32 Avenue of the Americas 111 Eighth Avenue carrier hotel Manhattan fiber meet-me room` · WebSearch → https://www.datacenterfrontier.com/colocation/article/55137841/dcf-tours-digital-realty-new-york-jfk12-data-center-60-hudson-st-manhattan (WebFetch): 60 Hudson St, 1928–1930, former Western Union Building, 24 storeys, Tribeca, Meet-Me Room on 9th floor, cable vault with diverse street entrances; 32 Avenue of the Americas and 111 8th Avenue named as the other carrier hotels. → NYC hub §13 landmarks.
- Query: `Brooklyn Navy Yard OR Industry City fiber internet tenants buildings connectivity` · WebSearch → https://dataverge.com/industry-city/ (WebFetch): Industry City 16 interconnected buildings, 550+ businesses; DataVerge operates the Meet-Me Room, 40+ carriers, campus dark-fiber network to tenant suites; DataVerge flagship at 882 3rd Ave. → NYC hub §13, §8.

### Pricing (existing approved site prices — not new)
- structured-cabling-pricing.html (repo): fiber custom-quoted; termination on existing fiber $35/termination; OTDR $40/strand; 12-strand OM4 floor-to-floor backbone $4,500–$7,000; 24-strand OS2 building-to-building $8,000–$15,000+; example 12-strand fiber riser line $5,500.
- structured-cabling-pricing-brooklyn.html configurator (Brooklyn base 1.00×): multimode fiber drop $350, single-mode fiber drop $400 (Manhattan $453/$517 = existing multiplier pages).
- network-installation-brooklyn.html: second telecom room with fiber link from $2,400.
- Blueprint §9: service/callback $195/hr, 3-hr minimum ($585). NYC hub uses Brooklyn base (1.00×).

## Keyword layers (silo plan)
- Service: fiber optic installation, fiber optic cabling, fiber backbone installation, fiber riser, fiber termination, fusion splicing, OTDR testing, fiber certification, building-to-building fiber, fiber to the desk.
- Problem: building not wired for fiber, copper distance limit, slow riser, interference near elevator motors, damaged fiber, dirty connectors, no documentation, carrier won't come past demarc.
- Technology: single-mode OS2, multimode OM3/OM4/OM5, LC/SC/MPO, splice tray, fiber enclosure, armored/interlocking fiber, innerduct, OFNR/OFNP, SFP optics, light source/power meter.
- Industry: offices, healthcare, schools, warehouses, retail chains, multifamily buildings, studios/media, data rooms.
- Geographic: NYC, five boroughs (hub); one borough/county per child page.

## Question register (every Q&A/FAQ question used in the silo, with page)
### fiber-optic-installation-nyc
§9 Questions Answered:
- My building isn't wired for fiber — what can actually be done?
- Who owns the fiber once it's inside — the carrier, the landlord or us?
- How do we choose between single-mode and multimode for a New York building?
- Is fiber worth it inside one office, or only between floors?
- How long does a fiber backbone take from walkthrough to light?
- What does the building management office need from a fiber contractor before work starts?
- Can new fiber share an old riser sleeve with existing cable?
- What happens to service while a fiber cutover is in progress?
- How is fiber protected where it runs past mechanical rooms or freight elevators?
- How do you prove a new fiber link is good before you leave?
- What breaks fiber in an occupied building after it's installed?
- Do we need fiber to every desk?
§17 FAQ:
- What does a fiber optic installation cost in NYC?
- Is a DOB permit needed for fiber cabling in New York City?
- What connector type should our fiber use?
- How many strands should a backbone have?
- Can you terminate fiber another contractor left unfinished?
- Do you supply the switches and optics, or only the cable?
- Can fiber run between two buildings we own?
- Does fiber need its own conduit?
- How long does a fusion-spliced termination last?
- What documentation do we receive at closeout?
- Do you work nights and weekends in occupied buildings?
- Which areas outside the five boroughs do you cover?

### fiber-optic-installation-manhattan
§9 Questions Answered:
- Why does building management want cable weights and fill numbers before approving a riser?
- Can our fiber land in the building's telephone closet, or does it need its own path?
- Does the building make us remove a previous tenant's fiber when we move in or out?
- How do we get a second, physically separate fiber path into a Manhattan building?
- Should the main fiber room stay in the cellar of a flood-prone downtown building?
- We lease floors that aren't next to each other — can one backbone tie them together?
- How should a fiber backbone be written into a Manhattan lease or work letter?
- Our office is in a five-storey loft with no real riser — how does fiber get upstairs?
- Does a landmarked or historic-district building change how fiber gets in?
- We're converting an office building to apartments — where should the fiber plan start?
- Who pays for the elevator operator and security guard on a weekend pull?
- Does a fiber backbone help a building's connectivity rating?
- Can you bring our fiber to a carrier hotel or data centre across town?
- Carrier circuit, dark fiber or owner backbone: which one do you need? (§10 EQUIPMENT comparison heading)
§17 FAQ:
- Why does fiber work cost more in Manhattan than in the outer boroughs?
- How soon can you walk a Manhattan building?
- Can you work under our general contractor during a fit-out?
- Can a co-op board hire you directly for a shared building backbone?
- Can fiber be added above a finished ceiling without demolition?
- Do you provide drawings the landlord's engineer can review before work starts?
- Do you cover Harlem, Washington Heights and Inwood as well as Midtown and downtown?
- Can you run fiber for a ground-floor shop on a Manhattan avenue?
- Can you install fiber to rooftop equipment?
- Is fiber worth it for a medical or imaging practice moving large files between rooms?
- Can you handle moves, adds and changes after the backbone is installed?
- What is the smallest fiber job you take in Manhattan?

### fiber-optic-installation-brooklyn
§9 Questions Answered (and other question headings):
- Need a Fiber Repair in Brooklyn?
- Can fiber reach the upper floors of a brownstone without opening the plaster walls?
- Can one fiber feed serve every apartment in a small Brooklyn walk-up we own?
- What if our landlord won't allow new holes in a rented Brooklyn loft?
- How far can a camera or access point sit from the network rack in a Brooklyn warehouse before fiber is needed?
- How do you run fiber across an industrial campus where the landlord controls the conduit?
- Can fiber enclosures live in an unheated warehouse or open loading dock?
- Can a fiber link carry security cameras across a truck yard or parking lot?
- Does fiber survive being underwater, and what has to be replaced after a flood?
- What does a new Brooklyn apartment building need in its telecom room so several providers can serve residents?
- Will a building-wide fiber backbone lower what our tenants pay for internet?
- Is a wireless point-to-point link a better choice than fiber between two buildings?
- Can fiber carry production video and audio between stages, not just office data?
- Want the Route Measured Before You Commit?
§17 FAQ:
- Do you work in southern Brooklyn as well as the north — Bay Ridge, Bensonhurst, Sheepshead Bay and Coney Island?
- Where are your Brooklyn fiber jobs run from?
- Do you install fiber in houses as well as businesses?
- Can you pull fiber through a conduit that already has a pull string in it?
- Can you fix a fiber cable that a renovation crew cut?
- Will you deal directly with our campus or industrial landlord's facilities team?
- Can fiber be run up the outside of a building instead of inside?
- Will you coordinate with the internet provider that serves our building?
- Can fiber go underground from a house to a rear garage, studio or back building?
- Is it safe to run fiber next to the electrical wiring in an old house?
- Do you work with schools, churches and community organisations on tight budgets?
- Do you do the splicing and testing yourselves?

## NYC (hub) — local research
- Area scope: five boroughs (Manhattan, Brooklyn, Queens, Bronx, Staten Island). Local facts used on the page: Verizon fiber footprint figures (end-2013), NYC Council broadband-subscription gaps (24.5% no broadband subscription; Mott Haven CD01 44%), Big Apple Connect (220 developments / ~330,000 residents, through June 2028), ConnectNYC 2013 (unwired commercial buildings), 60 Hudson Street carrier hotel (Western Union Building, Tribeca), 32 Avenue of the Americas, 111 Eighth Avenue, Industry City (16 buildings, DataVerge meet-me room), HPD broadband guidance (basement entry point requirement).
- Local Reddit: see source 1 (r/verizon, r/AskNYC excerpts).
- Local licensing/permits: unifinerds/nyflnerds (vendor guidance, recorded as such); site's existing statement that sub-50 V cabling needs no DOB permit while management approvals, firestopping and COIs still apply.
- Local news/hyperlocal: EMPTY beyond the sources above (no 2026 NYC fiber-installation news item retrieved).

## Manhattan — local research (2026-10-15 daily run, fiber-optic-installation-manhattan)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused; only Manhattan-specific research is added here.

### Reddit (local)
- Query: `reddit Manhattan prewar building fiber internet not available landlord` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/AskNYC/comments/9ezss5/no_internet_providers_will_set_up_in_my_building/ — excerpt: "I would suggest asking your building super / landlord who services the building. I have heard of certain buildings being Verizon DSL only" → Manhattan §5 (provider choice decided at building level).
  - https://www.reddit.com/r/NYCapartments/comments/1qjxeao/anyone_else_struggle_with_wifi_in_prewar_railroad/ — excerpt: poster in "a pre-war NYC railroad-style two bedroom apartment" with "ongoing WiFi issues". → Manhattan §7 (pre-war masonry walls; fiber/copper to a second access point rather than more wireless). Recorded as an excerpt only.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for the §10.5 reality check: claims published by competitor cost guides (quoted as published):
- Query: `fiber optic cabling installation Manhattan office cost per drop riser backbone contractor` · Firecrawl web search.
  - https://lowvoltagenewyork.com/resources/fiber-optic-cabling-cost-new-york/ (Firecrawl scrape, dated 2026-07-09): indoor pulls "$1–$6 per foot" normal, "$7–$12" through finished walls/packed risers; "Plenum rating adds 15–25%"; fusion splices "$50–$150 each"; OTDR "$75–$150/hour; nobody publishes a flat per-strand rate"; "a 2,000-foot OM4 riser run between IDFs, terminated and tested — lands around $3,000–$5,000"; "singlemode glass is now cheaper than OM4" but SM transceivers "roughly 1.5–5×" MM; "Any fiber that leaves the building in NYC needs a street-opening permit"; "In Manhattan and the Bronx, you rent the underground… Empire City Subway, a franchise dating to 1891". → Manhattan §10.5 (all seven H3s draw on this page or unio below).
  - https://unio.digital/blog/fiber-optic-installation-cost (search excerpt): "$1 to $6 per linear foot… or $300 to $800 per fiber drop installed for a typical office run"; "100 to 200 drops: roughly $15,000 to $30,000". → Manhattan §10.5 H3 on per-drop pricing.
- Query: `Empire City Subway conduit Manhattan Bronx franchise 1891 telecommunications ducts Verizon subsidiary` · Firecrawl web search → https://empirecitysubway.com/ (excerpt: "wholly owned subsidiary of Verizon… Since 1891"); https://comptroller.nyc.gov/reports/audit-on-the-payment-by-empire-city-subway-of-license-fees-due-the-city-and-compliance-with-certain-provisions-of-its-license-agreement/ (excerpt: "largest telecommunications conduit provider in New York City… executed on May 15, 1891"). → Manhattan §9 diverse-path question, §10.5.

### Landmarks, buildings, corridors
- Query: `375 Pearl Street Sabey data center former Verizon building Manhattan` · Firecrawl → https://en.wikipedia.org/wiki/375_Pearl_Street (scrape): 32-story office and datacenter building, Civic Center, Manhattan end of the Brooklyn Bridge; built for New York Telephone, completed 1975; originally appeared windowless; Sabey bought it in 2011 to redevelop as a data center (Intergate.Manhattan); renovated 2016. https://sabeydatacenters.com/locations/new-york-data-center (excerpt): "over a million square feet". → §13 landmark card.
- Query: `Manhattan office-to-residential conversion 2025 2026 largest projects 25 Water Street units` · Firecrawl → https://www.archpaper.com/2025/12/soma-25-water-street-cetraruddy-office-to-residential-conversion/ (scrape, Dec 4 2025): 25 Water Street (SoMA) 1,320 units, largest O2R in the US; floor plates about 40,000 sq ft; 21 residential floors × 52 units; two light wells cut through; basement inundated by Superstorm Sandy; 330 affordable units; first project under 467-m; former Pfizer HQ on 42nd Street being converted to ~1,600 units, opening 2027. → §5, §7 conversion card, §13 card, conversion section.
- Query: `Manhattan office inventory pre-war buildings share Class B office conversion pipeline 2026 report` · Firecrawl →
  - https://www.avisonyoung.us/documents/d/new-york/manhattan-office-report-2q-2026 (PDF scrape): conversion pipeline 19.2 msf; plus 3.4 msf converted since 2020 = 22.6 msf; availability 14.1% Q2 2026 from 16.8% a year earlier; inventory share Trophy 10% / Class A 15% / Class B 45% / Class C 30%; Class B/C 39% of 2026 leasing sq ft, up from 21% in 2025. → §5.5 facts, §8.
  - https://comptroller.nyc.gov/reports/office-to-residential-conversions-in-nyc-economics-and-fiscal-estimates/ (scrape, July 17 2025): 44 conversions, 15.2M gsf, ~17,400 apartments; Lower Manhattan 14 buildings / 7.8M gsf / 9,297 units; Midtown East 8 buildings / 3.4M gsf / 4,153 units; 25 Water St, 110 Maiden Lane, 111 Wall St, 222 Broadway named. → §5.5, §8, conversion section.
- Query: `Grand Central Madison East Midtown rezoning 2017 office towers One Vanderbilt completed 2020` · Firecrawl → https://www.nyc.gov/content/planning/pages/our-work/plans/manhattan/greater-east-midtown (excerpt: One Vanderbilt "a new 30 FAR, 1.3 million square foot commercial tower" under the new zoning framework); https://en.wikipedia.org/wiki/One_Vanderbilt (excerpt: topped out at 1,401 feet, Curbed 2019). → §8 corridor card, §13 card.
- Query: `SoHo-Cast Iron Historic District designated 1973 number of buildings` · Firecrawl → https://villagepreservation.org/2024/08/14/the-soho-cast-iron-historic-district-a-1973-designation-that-helped-shape-nycs-cultural-legacy/ (excerpt: "approximately 26 blocks, covering nearly 500 buildings"). → §7, §13.
- 60 Hudson Street / 32 Avenue of the Americas / 111 Eighth Avenue: silo-wide source (datacenterfrontier) reused. → §13.

### Local news / hyperlocal
- Query: `Verizon replaced copper with fiber Lower Manhattan after Hurricane Sandy 140 West Street` · Firecrawl →
  - https://www.cbsnews.com/newyork/news/verizon-upgrading-to-all-fiber-optics-after-copper-wiring-was-destroyed-in-sandy-storm-surge/ (scrape, CBS New York, 2012): Verizon's Broad Street central office underground cable vault badly damaged by saltwater; crews cutting out copper; "All of the new fiber optic cables survived unharmed by the flooding"; "every inch of corroded copper cable will be replaced with fiber optics" (Chris Levendos). → §5, resilience section, §9 flood question.
  - https://www.fierce-network.com/telecom/verizon-takes-advantage-superstorm-sandy-to-accelerate-copper-to-fiber-migration (excerpt): copper damaged by Sandy at 140 West St replaced with fiber. → resilience section.
- Query: `WiredScore started New York City Bloomberg Wired NYC building connectivity rating` · Firecrawl → https://wiredscore.com/about-us/history/ (scrape): founded in New York in 2013 with endorsement from Mayor Bloomberg; certifies in 42 countries; acquired by Meter in February 2026. → §9 connectivity-rating question, §5.5.
- Local news on Manhattan fiber installation 2026 (contractor-level): EMPTY beyond the above.

### Local licensing / permits / building rules
- Query: `Landmarks Preservation Commission permit required exterior work conduit cable landmark building historic district NYC` · Firecrawl → https://www.nyc.gov/assets/lpc/downloads/pdf/LPC-Permit-Guidebook.pdf (excerpt): LPC permits required for "Any project that occurs on a landmark site or within the boundaries of a historic district" affecting the exterior; LPC contact 212-669-7817 (not used on page). https://fontanarchitecture.com/nyc-landmark-permits-lpc-application-types/ (excerpt, architect guidance): interior renovations in landmark districts/buildings that need permits go through LPC (Certificate of No Effect). → §7.5, §8.5, §9 landmark question.
- Query: `Manhattan building telecom room riser "certificate of insurance" freight elevator after-hours contractor rules management office tenant fit-out cabling` · Firecrawl → https://386parkavenuesouth.info/main.cfm?sid=pprocedures&pid=oarregulations (scrape, a published Manhattan office building's alteration rules): COIs before work; abandoned cabling removed "back to the point of origin"; firestopping at all slab and wall penetrations; disruptive work before 8:00 AM / after 6:00 PM or weekends; deliveries booked 72 hours ahead via the freight elevator; elevator operator and security guard billed to the tenant outside hours; riser use requires a request with route, number/type of cables, total cross-sectional area, weight per linear foot and support method; floor-to-floor cabling not in base-building closets; all telecom cabling plenum-approved; cabling in common areas in enclosed raceway; slab cores located by magnetic means, holes 1/4" larger than conduit; insurance example $1M CGL, $2M umbrella. → §8.5, alteration-rules section, §9 riser-request and elevator-cost questions. Presented on the page as one building's published rules, not a universal law.
- Existing site pages (not new research, kept consistent): structured-cabling-pricing-manhattan.html publishes Manhattan fiber drops at $453 multimode / $517 single-mode and says multi-floor backbones are custom-quoted. Manhattan multiplier 1.25× (blueprint §9) applied to the remaining base prices: $35→$44 termination, $40→$50 OTDR/strand, $4,500–$7,000→$5,625–$8,750, $8,000–$15,000+→$10,000–$18,750+, $2,400→$3,000. $195/hr 3-hr minimum unchanged (protected).

### Keyword plan (Manhattan page)
Service: fiber optic installation Manhattan, fiber backbone Manhattan, riser fiber, fusion splicing, OTDR testing. Problem: riser full, landlord approval, flood-prone cellar, single entry point, non-contiguous floors, abandoned cable. Technology: OS2, OM4, plenum OFNP, riser OFNR, MPO, armored. Industry: Class B offices, conversions, medical, retail, co-ops, media/tech lofts. Geographic: Manhattan, Financial District, Tribeca, SoHo, Midtown, Hudson Yards, Upper East/West Side, Harlem, Washington Heights.

## Brooklyn — local research (2026-10-16 daily run, fiber-optic-installation-brooklyn)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused; only Brooklyn-specific research is added here.

### Reddit (local)
- Query: `reddit Brooklyn brownstone fiber internet Verizon Fios not available building` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/Fios/comments/1u2ndd4/getting_fios_installed_at_a_brooklyn_apartment/ — excerpt: "Buildings are different. Even if you have fios all around you the building still has to be setup." → Brooklyn §5 (service is decided building by building, not street by street).
  - https://www.reddit.com/r/Fios/comments/1rf0wmr/brooklyn_ny_my_street_doesnt_have_fios_but_the/ — excerpt: "My street doesn't have FIOS but the streets … all have FIOS". → Brooklyn §5.
  - https://www.reddit.com/r/verizon/comments/1pd6vhe/what_do_i_have_to_do_to_get_fios_in_my_building/ — excerpt: "Verizon gave up on expanding FiOS in NYC around 2014 … A wireless internet backup is a great idea." → recorded as a commenter's opinion only; used in §5 as "residents say" context, not as fact.
  - https://www.reddit.com/r/Brooklyn/comments/166pi5w/how_can_i_get_verizon_fios_in_my_building/ — excerpt: "If it's a rental go to your management company as well once you have a group." → §5 (owner/management decides the building's wiring).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for the §10.5 reality check: claims published by a NYC competitor's fiber guide (quoted as published):
- Query: `Brooklyn fiber optic cabling contractor cost reviews complaints office building wiring` · Firecrawl web search → https://newtechcabling.com/fiber-optic-installation-nyc-businesses-buildings/ (Firecrawl scrape, published 2026-10-09, Midtown firm; serves "Manhattan, Brooklyn, Upper Manhattan, Jersey City, Hoboken and Union City"): "Copper stops working reliably beyond about 100 meters, so far-apart rooms or buildings call for fiber"; "Many New York projects pick single-mode for the backbone because it covers any distance and any future speed"; "Small projects can take a day or two, while multi-floor projects take longer"; "Links near elevators, heavy machinery or dense power cabling can suffer errors that fiber avoids"; "Fiber in air-handling spaces generally needs a plenum rating, riser shafts call for riser-rated cable"; tight "Manhattan pathways" framing. → Brooklyn §10.5 H3s 1, 2, 3, 6, 7.
- Silo sources reused for §10.5: thenetworkinstallers.com (FBA 2025 underground median $18.00/ft, aerial $8.00/ft) → H3 4; lowvoltagenewyork.com ("Any fiber that leaves the building in NYC needs a street-opening permit"; "Plenum rating adds 15–25%") → H3 5.
- Same query → Yelp listing https://m.yelp.com/biz/new-york-network-cabling-and-fiber-optic-wiring-new-york (excerpt: rating 4.0 from 1 review). No 1–3★ review text retrieved. Yelp: EMPTY.

### Landmarks, buildings, corridors
- Query: `Brooklyn Navy Yard tenants businesses number of jobs buildings 2025` · Firecrawl → https://www.brooklynnavyyard.org/brooklyn-navy-yard-fy25-impact-report/ (excerpt): "more than 300 acres along Brooklyn's waterfront … over 550 businesses supporting more than 13,000 jobs … more than $2.5 billion in annual economic impact." → §5.5, §8, §13.
- Query: `Brooklyn Navy Yard Building 77 Dock 72 square feet office industrial` · Firecrawl → https://www.brooklynnavyyard.org/wp-content/uploads/2023/07/BLDG-77-Suite-106.pdf (excerpt: "60,000-square foot, public ground floor food hall anchored by Russ & Daughters"); http://dock72.com/ (excerpt: Dock 72 in the Navy Yard, "a 300-acre modern industrial campus … between Williamsburg and DUMBO"); https://s9architecture.com/dock-72 (excerpt: "built on the site of a former drydock"). → §13 card.
- Query: `Brooklyn Army Terminal Sunset Park NYCEDC tenants square feet buildings` · Firecrawl → https://edc.nyc/project/sunset-park-district (excerpt: "BAT's 4 million-square-foot waterfront industrial campus, NYCEDC will invest up to $100 million to develop BATWorks"); https://brooklynarmyterminal.com/leasing (excerpt: "Floorplates up to 200,000 square feet for anchor tenants and suites starting at 1,500 square feet"). → §7, §8, §13.
- Industry City: silo source (dataverge.com, 16 buildings, meet-me room) reused; plus https://bkfiber.com/campuses/industry-city.html (search excerpt: Brooklyn Fiber "on-net across Industry City … 61 served addresses") and https://bkfiber.com/ (search excerpt: DIA "independent of the incumbent conduit your other carriers share"; buildings served "from Red Hook to the Navy Yard"). → §8, §9 diverse-path/campus question, §13. Presented as the provider's own claims.
- Query: `Downtown Brooklyn 2004 rezoning office residential towers Partnership statistics` · Firecrawl → https://storymaps.arcgis.com/stories/fd7bebf0949e4a7f96615a9b41e91dfe (Downtown Brooklyn Partnership, Feb 2 2026, scrape): 32M+ sq ft across 144 projects since 2004; 22,000+ housing units; 2.8M sq ft new office across 19 properties; 1 Willoughby Square first new office tower since rezoning, opened 2021; towers on Flatbush Ave 19–93 stories; Dumbo Heights conversion of the former Jehovah's Witnesses complex (2015); private-sector jobs 62,000 (2010) → 86,000+ (2022); 3 MetroTech conversion to classrooms; Brooklyn Navy Yard employment 3,000 → 11,000 since late 1990s; Industry City 550+ companies after $450M modernization; Empire Stores, Domino Refinery, 25 Kent, Dock 72, Building 77 named as office projects. → §5.5, §7, §8, §13.
- Query: `Gowanus rezoning 2021 approved number of new apartments flood resilience` · Firecrawl → https://www.nyc.gov/content/planning/pages/our-work/plans/brooklyn/gowanus (scrape): Gowanus Neighborhood Plan adopted by City Council November 23, 2021; goals include canal cleanup, affordable housing, "resilience in the face of climate change"; Gowanus Green 100% affordable. https://projects.newsdoc.org/climatenyc/section/gowanus-rezoning-done-deal-or-pipe-dream/ (excerpt: "82-block rezoning proposal … 8,200 new affordable apartments" — proposal-stage figure, recorded but NOT used). → §7 new-build card, §8, §9 new-building question.
- Query: `Greenpoint Williamsburg 2005 rezoning waterfront towers manufacturing lofts Brooklyn` · Firecrawl → https://www.nyc.gov/assets/planning/download/pdf/plans/greenpoint-williamsburg/greenpointwill.pdf (excerpt: "On May 11, 2005, the City Council approved the Department of City Planning's rezoning proposal"); https://greenpointers.com/2025/05/13/… (excerpt: "In 2023 alone, 2,306 units were added—the most of Brooklyn's community boards for that year"). → §5.5, §8.
- Query: `Brooklyn Heights first historic district New York City designated 1965` · Firecrawl → https://hdc.org/buildings/brooklyn-heights-historic-district/ (excerpt: "Designated November 23, 1965. The first designated New York City Historic District … 19th-century brownstone and brick"); https://thebha.org/neighborhood/ (excerpt). → §7, §13.
- Query: `Brooklyn row houses brownstones historic districts number Landmarks Preservation Commission Brooklyn` · Firecrawl → https://www.garfieldbrooklyn.com/blog/brownstone-brooklyn-architecture-guide-5-historic-districts-explained/ (excerpt, real-estate blog: "over 40 blocks lined with 2,853 historic Park Slope brownstones and rowhouses") — not used (secondary blog figure). https://www.nyc.gov/assets/lpc/downloads/pdf/lp_rhmanual.pdf (excerpt: LPC Rowhouse Manual; "more than 100 historic districts throughout New York City"). → §7.5, FAQ exterior route.

### Local news / hyperlocal / data
- Query: `Red Hook Superstorm Sandy flooding basements businesses Brooklyn waterfront 2012` · Firecrawl → https://insideclimatenews.org/news/26102017/hurricane-sandy-anniversary-brooklyn-red-hook-vulnerable-waterfront-neighborhood-adapting/ (excerpt: "Oct. 29, 2012, Basements and cars were flooded out, and water even spat up from the sewers"); https://www.nyc.gov/html/sirr/downloads/pdf/final_report/Ch_1_SandyImpacts_FINAL_singles.pdf (excerpt: "In Brooklyn, the area that flooded was more than twice as large as the floodplain"). → §5, flood section, §9 flood question.
- Query: `Brooklyn fiber broadband news 2025 2026 internet buildings Brooklyn` · Firecrawl → bkfiber.com (provider marketing, see above); https://mapmybroadband.dps.ny.gov/explore?address=Brooklyn (NYS PSC broadband map — exists; not scraped). → §5 (independent local provider exists; owner-side wiring still needed).
- NYC Council internet-access page (silo source) re-queried for Brooklyn → https://council.nyc.gov/data/internet-access/ (Firecrawl query, direct quote): "Borough Park-Kensington: 42% (Brooklyn – CD12)" — second-highest district after Mott Haven (households without a broadband subscription). → §5.5.
- Local news on Brooklyn fiber-installation contractors 2026: EMPTY.

### Local licensing / permits / building rules
- Same LPC sources as Manhattan (silo) plus Brooklyn Heights designation above → exterior conduit on landmarked row houses needs LPC review; interior-only routes generally do not. → §7.5, FAQ.
- Street crossings: lowvoltagenewyork (silo) "Any fiber that leaves the building in NYC needs a street-opening permit" → §10.5 H3 5, §9 wireless-vs-fiber question.
- HPD broadband guidance and FCC exclusivity ban (silo source) → §9 new-building multi-provider question.
- Existing site pages (not new research, kept consistent): structured-cabling-pricing-brooklyn.html configurator — multimode fiber drop $350, single-mode $400 (Brooklyn base 1.00×). structured-cabling-pricing.html base: $35/termination, $40/strand OTDR, 12-strand OM4 backbone $4,500–$7,000, 24-strand OS2 $8,000–$15,000+. network-installation-brooklyn.html: second telecom room with fiber link from $2,400. $195/hr 3-hr minimum ($585) protected.

### Keyword plan (Brooklyn page)
Service: fiber optic installation Brooklyn, fiber backbone Brooklyn, warehouse fiber, campus fiber, fusion splicing, OTDR testing. Problem: copper over 100 m in warehouses, unheated docks, flood-damaged cellar, landlord-controlled conduit, no-drill rental loft, brownstone plaster walls, yard cameras. Technology: OS2, OM4, armored indoor/outdoor, riser OFNR, wall-mount enclosures, media converters/SFPs. Industry: warehouses and makers, film/production, multifamily new builds, small landlords, retail corridors, schools and houses of worship. Geographic: Brooklyn, Navy Yard, Industry City, Sunset Park, Red Hook, Gowanus, Williamsburg, Greenpoint, Bushwick, East Williamsburg, Downtown Brooklyn, DUMBO, Park Slope, Brooklyn Heights, Bay Ridge, Flatbush, East Flatbush, Canarsie, East New York, Bensonhurst, Sheepshead Bay, Coney Island.
