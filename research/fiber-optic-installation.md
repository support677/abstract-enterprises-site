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


## Long Island hub

Research for `fiber-optic-installation-long-island` (batch run 2026-10-17). Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in `research/fiber-optic-installation.md` are reused where noted. To be merged into `research/fiber-optic-installation.md` by the main run.

### Reddit (local)
- Query: `reddit r/longisland fiber internet Fios not available office building Melville Hauppauge` · Firecrawl web search (excerpts only; Firecrawl refuses to scrape reddit.com — scrape attempt on the first URL returned "we do not support this site").
  - https://www.reddit.com/r/longisland/comments/1l42vex/fios_in_melville/ — excerpt: "Internet says 94-99% of Melville is covered by FIOS. Try your address a different way. FiOS was not available despite having an ONT FiOS box on ..." (excerpt may join two comments; page attributes it to the thread, not one poster) → §10.5 AI reality check H3 1.
  - https://www.reddit.com/r/longisland/comments/xe0pik/anyone_else_having_issues_with_fios_in_nassau/ — excerpt: "I'm in suffolk and my only issue with them is that they're just now hanging the fiber in my backyard." → §10.5 H3 7 (carrier drop to one home ≠ campus wiring).
  - https://www.reddit.com/r/longisland/comments/1e0ap4m/fios_on_east_end_long_island/ — excerpt: "Blocked in Brookhaven aka Crookhaven…" → not used (opinion).
  - https://www.reddit.com/r/longisland/comments/1bbdlsi/verizon_fios/ — excerpt: "Verizon themselves said they felt the future is fixed wireless…" → not used (unverified commenter claim).
  - https://www.verizon.com/home/internet/near-me/long-island-new-york/ (same search, excerpt): "For addresses not yet covered by Fios, Verizon 5G…" → §10.5 H3 1.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5: silo sources reused (thenetworkinstallers.com FBA 2025 medians $18.00/ft underground, $8.00/ft aerial → H3 2; T-Mobile "up to 4 hours", AT&T "four to six hours" → H3 4; ampcom single-mode vs multimode → H3 5), plus the Reddit excerpts above.

### Building stock, corridors, landmarks
- Query: `Hauppauge Industrial Park number of businesses employees acres` · WebSearch → https://cmmllp.com/hauppauge-industrial-park-update-2017-long-islands-oasis-productivity-innovation/ (WebFetch, 2017): "In only eleven square miles, the 1350 businesses of the Hauppauge Industrial Park generate $13.4 billion in annual revenues"; ~55,000 workers; "largest industrial park in the Northeast by number of companies and employees"; Town of Smithtown overlay covers "about two-thirds of the park". → §5 para 2, §5.5 facts, §8 Hauppauge card, §13 landmark card.
- Query: `Long Island Innovation Park at Hauppauge renamed HIA-LI` · WebSearch → https://cmmllp.com/campolos-remarks-at-hia-li-press-conference-announcing-new-name-and-new-chapter-for-hauppauge-industrial-park (WebFetch, posted April 24 2019): new name "The Long Island Innovation Park at Hauppauge". → §5, §8, §13.
- Query: `RXR Plaza Uniondale office towers square feet` · WebSearch → https://www.cbre.com/properties/properties-for-lease/office/details/US-SMPL-58505/rxr-plaza-uniondale-ny-11553 (WebFetch): "Adjacent to Meadowbrook Parkway offering access to the LIE, and Northern and Southern State Parkways"; nearby Nassau Coliseum, Roosevelt Field; space on "13th Floor (West Tower)". No building total sq ft or tower count given — page does not state either. → §8 Uniondale card, §13 card.
- Query: `Route 110 Melville office corridor square feet office space Long Island` · WebSearch → https://nyrej.com/print/41508 (WebFetch, Nov 19 2019): Melville Corporate Center I, 105 Maxess Rd., Melville, "149,000 s/f", "in close proximity to Rte. 110 and the Long Island Expressway". → §8 Route 110 card, §13 card.
- Query: `Long Island office market report 2026 vacancy Melville Route 110 Nassau Suffolk` · WebSearch → https://mktgdocs.cbre.com/2299/50797d87-279f-4e52-97e4-f4a182cafc69-39923475/Long_Island_Office_2026_Q2_Fig.pdf (WebFetch): Long Island office 38.45 MSF, total vacancy 11.5%, availability 12.1% ("post-pandemic low"), Q2 2026. → §5.5, §9 Route 110 move-in question.
- Query: `Long Island industrial market 2026 warehouse inventory square feet vacancy CBRE` · Firecrawl search → https://www.cbre.com/insights/figures/long-island-industrial-figures-q2-2026 (WebFetch): vacancy 7.0% after a 70 bps decline; net absorption >800,000 sq ft; leasing 905,000 sq ft. → §5.5.
- Query: `Stony Brook University campus acres buildings fiber network` · WebSearch → https://en.wikipedia.org/wiki/Campus_of_Stony_Brook_University (WebFetch): "213 buildings over 1,454 acres"; Town of Brookhaven; R&D park "246-acre plot… south of the main Stony Brook campus"; university hospital 695 beds. → §7 colleges card, §8 research-belt card, §13 card.
- Query: `Hofstra University campus acres Hempstead Uniondale buildings` · WebSearch → https://en.wikipedia.org/wiki/Hofstra (WebFetch): "approximately 117 buildings on 244 acres"; "located in the Uniondale section of Hempstead"; part of campus "south of Hempstead Turnpike (NY Route 24)". → §7 colleges card, §13 card.
- Query: `Brookhaven National Laboratory site acres Upton employees` · WebSearch → https://en.wikipedia.org/wiki/Brookhaven_National_Laboratory (Firecrawl scrape): Upton, hamlet of the Town of Brookhaven; established 1947 at Camp Upton; "5,265-acre" area; ~2,750 staff. → §8 research-belt card, §13 card.
- Query: `Northwell Health largest private employer New York State employees Long Island hospitals` · WebSearch → https://medicine.hofstra.edu/sites/medicine.hofstra.edu/files/2026-07/northwell%20health%20at%20a%20glance-2026.pdf (WebFetch): "NEW YORK'S LARGEST PRIVATE EMPLOYER AND HEALTH CARE PROVIDER"; 28 hospitals; 104,000+ employees; 1,050+ outpatient facilities (combined Northwell/Nuvance). → §7 health card (only the "largest private employer" description used).
- Query: `Nassau County three towns two cities 64 incorporated villages Suffolk County ten towns` · WebSearch → https://www.ny.gov/counties/nassau (WebFetch): "Two cities, three towns, 64 incorporated villages, and more than 60 unincorporated hamlets"; population 1,381,715 (2023); 453 sq miles. https://www.ny.gov/counties/suffolk (WebFetch): "divided into 10 towns"; 1,523,170 (2023); 2,373 sq miles. → §5 para 3, §5.5, Nassau/Suffolk section.
- Query: `Nassau Hub Coliseum redevelopment Uniondale acres 2026` · WebSearch → results only (Las Vegas Sands casino proposal coverage); not fetched, NOT used.

### Carriers / fiber providers
- Query: `Optimum fiber Long Island rollout homes passed Altice fiber Nassau Suffolk` · WebSearch → https://alticeusa.com/node/3151 (WebFetch, Oct 1 2024): additional $40M investment; "nearly 900,000 fiber passings on Long Island"; >100 communities. → §5 para 4, §5.5, §9 carrier question, §10.5 H3 1.
- Query: `Verizon Fios Long Island expansion fiber 2025 2026 Suffolk towns Brookhaven franchise` · WebSearch → https://messengerpapers.com/2026/04/brookhaven-town-board-unanimously-approves-verizon-franchise-to-build-townwide-fiber-network/ (WebFetch, Apr 20 2026, press-release item): Brookhaven Town Board unanimously approved a Verizon franchise for a townwide "full fiberoptic network"; awaits NYS PSC authorization; aims to compete with Altice/Optimum. → §5 para 4, §9 carrier question.

### Utility, storms, permits
- Query: `PSEG Long Island pole attachment application third party attacher process` · WebSearch → https://www.barclaydamon.com/alerts/nys-psc-modifies-pole-attachment-rules-to-accelerate-broadband-and-cellular-service-deployment (WebFetch): PSC order July 18 2024 modifying 2004 pole-attachment policy; 90-day dispute "shot clock"; OTMR option. Page does NOT mention PSEG LI/LIPA. → §9 pole question (stated as a statewide PSC rule change for providers; no claim it governs LIPA). PSEG LI's own attachment process: EMPTY (no PSEG LI page retrieved).
- Query: `PSEG Long Island miles of overhead lines underground distribution poles number` · WebSearch → https://lipower.org/wp-content/uploads/2024/12/LIPA-UG-Release-12.2024.pdf (WebFetch, Dec 6 2024): LIPA policy requires new transmission >65 kV underground; 40 miles of underground bypass done. No overhead mileage/pole count. → NOT used on page (transmission policy not relevant to private fiber).
- Isaias: https://abc7ny.com/weather/more-than-300000-lose-power-on-long-island/6353608/ (WebFetch this run, Aug 2020): "almost half of PSEG's 1.1 million customers in the dark at the peak"; storm "downing trees and power lines". → §5.5, §9 storm question, §9 overhead-vs-underground question.
- Query: `Superstorm Sandy Long Beach Nassau flooding businesses basements telecom equipment damaged` · Firecrawl search → https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York (Firecrawl scrape): "the city of Long Beach sustained $150 million in damage"; Nassau voluntary evacuations of the South Shore surge area "south of Sunrise Highway". → §9 salt-air/flood question.
- Query: `Town of Hempstead building permit required low voltage wiring data cabling commercial` · WebSearch → https://permitmint.com/permits/new-york/hempstead-ny/electrical/ (WebFetch): covers Village (not Town) of Hempstead electrical permits; nothing on low-voltage. → NOT used. Town/village low-voltage permit rules: EMPTY — page only says permits are issued by the town, village or city and must be checked per address (supported by the ny.gov municipal structure above).
- Query: `Suffolk County Code Chapter 563 Article XI electrical licensing low voltage` · WebSearch → https://www.ecode360.com/26904471?mode=clear (WebFetch) turned out to be Charles County, MD code — irrelevant. Suffolk licensing for fiber: EMPTY; not discussed on page.
- 811 one-call markout: general industry practice stated without statistics or deadlines (no source fetched) → §8.5, §9 trench question, process step 3. Flag for review if a citation is wanted.

### Local news / hyperlocal (Newsday, Patch, News12, TBR) on fiber installation contractors — EMPTY (none retrieved beyond the Brookhaven franchise item).

### Pricing used (existing approved prices × blueprint §9; not new)
Base (Brooklyn 1.00×, from live fiber pages / structured-cabling-pricing): $35 termination, $40 OTDR/strand, $350 MM drop, $400 SM drop, $4,500–$7,000 12-strand OM4, $8,000–$15,000+ 24-strand OS2, from $2,400 second room; $195/hr 3-hr min ($585) protected.
Nassau 1.15×: $40, $46, $403, $460, $5,175–$8,050, $9,200–$17,250+, from $2,760. Suffolk 1.20×: $42, $48, $420, $480, $5,400–$8,400, $9,600–$18,000+, from $2,880. Starter package = 24 terminations + 12 OTDR: Nassau $1,512, Suffolk $1,584.
CONFLICT for review: live `structured-cabling-pricing-nassau-county.html` configurator shows fiber drops $411/$470 and `structured-cabling-pricing-suffolk-county.html` $453/$517 (different multipliers than §9); `network-installation-long-island.html` says Nassau/Suffolk "carry no travel loading". This page follows blueprint §9 as instructed.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
| File (images/fiber-optic-installation/) | Source |
|---|---|
| fiber-optic-installation-long-island-fusion-splicer-yellow-patch-rack.webp | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg (same photo as the splice-tray images on the NYC/Manhattan/Brooklyn fiber pages, different source file) |
| fiber-optic-installation-long-island-exterior-enclosure-brick-conduit.webp | low-voltage/low-voltage-installation-nassau-county-exterior-enclosure-install.jpg |
| fiber-optic-installation-long-island-warehouse-cable-tray-lift.webp | low-voltage/low-voltage-installation-long-island-03-warehouse-cable-tray-highbay.jpg |
| fiber-optic-installation-long-island-scissor-lift-ceiling-access.webp | low-voltage/low-voltage-installation-brooklyn-access-point-lift-install.jpg |
| fiber-optic-installation-long-island-certification-tester-rack.webp | network/network-installation-bronx-fluke-dsx-certification-pass.webp |
| fiber-optic-installation-long-island-fitout-cable-staging.webp | network/network-installation-bronx-cat6-cable-box-staging-fitout.webp |
| fiber-optic-installation-long-island-wall-fish-pull.webp | network/network-installation-bronx-retrofit-wall-fish-data-drop.webp |
| fiber-optic-installation-long-island-patch-panel-termination.webp | network/network-installation-nyc-patch-panel-punchdown-rack.webp |
| fiber-optic-installation-long-island-wall-outlet-termination.webp | network/network-installation-bronx-workstation-data-outlet-termination.webp |
| fiber-optic-installation-long-island-keystone-bench-termination.webp | network/network-installation-nyc-keystone-jack-punchdown-bench.webp |
| fiber-optic-installation-long-island-patch-cord-crimp-bench.webp | network/network-installation-nyc-rj45-crimp-patch-cord.webp |

Overlap note: 4 of these photos (exterior enclosure, warehouse tray, wall fish, certification tester) show the same scenes as images picked by the parallel Hudson Valley fiber builder, from different source files; the library has few fiber-relevant scenes. All library photos show technicians' faces and many show an 844-386-7238 number on shirts; several look AI-generated (garbled box/logo text) — for Anwar to review.

### Keyword plan (Long Island page)
Service: fiber optic installation Long Island, building-to-building fiber, campus fiber backbone, outdoor fiber, aerial fiber, fusion splicing, OTDR/bidirectional testing, demarc extension. Problem: buildings across a parking lot, carrier demarc at the loading dock, gatehouse/outbuilding, storm outages, salt air, repaving, unknown old conduit. Technology: outdoor loose-tube OS2, all-dielectric aerial, armoured, OM4, handholes, innerduct, tracer wire, splice closures, media converters. Industry: office parks, flex/industrial, big-box/strip retail, healthcare campuses, colleges, garden apartments, dealerships, estates/marinas. Geographic: Long Island, Nassau, Suffolk, Melville/Route 110, Hauppauge, Uniondale, Garden City, Westbury, Hicksville, Ronkonkoma, Bohemia, Stony Brook, Upton, North/South Fork.

### Question register additions
fiber-optic-installation-long-island
§9 Questions Answered:
- Should the fiber between our buildings go under the parking lot or overhead?
- Can our fiber be attached to the utility poles that already run along our property?
- Is it worth running fiber to a gatehouse, pump house or detached garage that needs only a few devices?
- Our sites are a few miles apart in different hamlets — can we own the fiber between them?
- Optimum or Verizon fiber already reaches our street — doesn't that make a private backbone unnecessary?
- The carrier landed its fiber at the loading-dock end — how does it reach the front office?
- We're moving into a vacant office building near Route 110 — what fiber should be in place before move-in?
- How is fiber work handled inside an occupied hospital or medical campus?
- Will a storm that knocks out power to one building take the whole campus network down?
- Does salt air near the South Shore or the Sound shorten the life of outdoor fiber hardware?
- Does metal inside an outdoor fiber cable create a lightning risk between buildings?
- What has to happen before anyone digs a fiber trench across our property?
§17 FAQ:
- Why are Nassau and Suffolk fiber prices higher than the city base rate?
- Do you take fiber work on the North Fork and the South Fork?
- How deep does fiber conduit sit under a parking lot?
- Can the conduit be bored under the lot instead of cutting the asphalt?
- What happens to buried fiber when the parking lot is milled and repaved?
- Do you need a site plan or survey before quoting a campus link?
- Do you work for property managers who run several office parks?
- Can fiber share a trench with electrical, gas or irrigation lines?
- Will you work alongside our IT provider or managed-service company on cutover day?
- Can fiber be run through the attic or crawlspace of a house converted into offices?
- Can fiber go into an old underground conduit that has filled with water?
- What should a written fiber bid for a Long Island campus include?


## Hudson Valley hub — local research (2026-10-17 batch, fiber-optic-installation-hudson-valley)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted; only Hudson Valley research is added here. Page thesis: valley networks are a distance / ground-potential / weather problem between scattered buildings (campus, warehouse, farm/estate), not a riser problem.

### Reddit (local and topical)
- `reddit r/hudsonvalley internet fiber barn outbuilding ethernet run` · Firecrawl web search (excerpts only; reddit.com threads not opened). No r/hudsonvalley thread returned → r/hudsonvalley: EMPTY. Topical r/HomeNetworking excerpts returned:
  - https://www.reddit.com/r/HomeNetworking/comments/17duela/bringing_internet_to_new_barn/ — excerpt: "you want to run fiber for anything between buildings. I've personally had to deal with fried ..." → §"Why Copper Fails Between Valley Buildings" (quoted as opinion).
  - https://www.reddit.com/r/HomeNetworking/comments/1kruhmc/running_200_fiber_from_my_house_to_a_barn_to/ — excerpt: "DO place a CAT6 in the conduit, terminated and tested, but unused, as a backup" → same section, last paragraph.
  - https://www.reddit.com/r/HomeNetworking/comments/1j3miyh/best_way_to_get_internet_to_a_barn_250ft_outdoor/ — excerpt: "either trench fiber (and use media converters) or put up point to point directional antennas. Don't connect two buildings ..." → background only (not quoted).
- `reddit hudsonvalley fiber internet Spectrum only option rural house` · WebSearch → no reddit.com results (ISP comparison sites only). EMPTY.

### Forums (technical, used as opinion)
- `fiber optic vs copper between buildings lightning ground potential difference outbuilding` · WebSearch → https://forum.mikrotik.com/t/is-fiber-always-the-better-choice-between-buildings/272583 (WebFetch): each building has its own grounding electrode; Ethernet transformers give functional not safety isolation; a user reported shocks through PC chassis after bonding separately grounded buildings; counter-view: UTP is cheapest under 100 m, lightning concern called "one of those myths". → §5 Neighborhood para 2; ground/lightning section para 2; §10.5 H3 1 (claim).
- Same query → https://www.lanshack.com/solving-outdoor-network-issues (WebFetch): page body not retrievable (navigation only). EMPTY.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check: claims quoted from published cost guides/forums:
- `fiber optic installation Westchester NY contractor cost building to building` · WebSearch → https://unio.digital/blog/fiber-optic-installation-cost (WebFetch): aerial on poles ~$8–$12/ft and "need attachment rights"; short aerial building link "can range from a few thousand dollars"; underground trenching $15–$35/ft, boring $20–$30/ft; fiber drop $300–$800, ~2–3× a Cat6 drop ($150–$300); 100–200 drops "$15,000 and $30,000"; "These are orientation ranges, not quotes." → §10.5 H3 3, 4, 5.
- MikroTik forum (above) → §10.5 H3 1. Clearfield (below) → §10.5 H3 2. Central Hudson / NY811 (below) → §10.5 H3 6. Ulster ConnectALL (below) → §10.5 H3 7.
- Yelp: `fiber optic installation Westchester` not searched on Yelp directly; no yelp.com results in any query above. EMPTY.

### Weather / lightning (local data)
- `New York lightning flash density per square mile Hudson Valley thunderstorm days` · WebSearch → https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf (WebFetch): 2020 NY total 4,943,122 pulses; county ranking #1 Orange 275,059 pulses (41 thunder days); Ulster 182,760 (49 days); Westchester 168,634 (45); Dutchess 166,641 (48); Putnam 75,093 (35); Rockland 64,575 (28). Measures pulses, not flashes. → §5 para 3 + facts list; Six Counties (Orange "lightning capital").

### Code / technical sources (new for this page)
- `foa.org fiber optic dielectric cable no grounding lightning ground loops between buildings` · WebSearch → https://seeclearfield.com/newsroom/grounding-or-no-grounding-whats-required-for-fiber.html (WebFetch): fiber "composed of all-dielectric materials"; metallic strength member/tone wire/armor may be present; NEC 770.93 — where cable entering a building is exposed to contact with power conductors, metallic members grounded per 770.100 or interrupted by insulating joint, "as close as practicable to the point of entrance" (2014 NEC cited). → §8.5 compliance callout 2; ground section para 4; §10.5 H3 2; FAQ none.
- `NEC 800.90 primary protector communications circuits outside plant copper entering building lightning exposed` · WebSearch → https://www.ecmweb.com/national-electrical-code/code-basics/article/20890128/article-800-communications-circuits (WebFetch, Mike Holt commentary): listed primary protector required per circuit near entrance (800.90); metallic sheath grounded near entrance (800.93); grounding conductor rules (800.100). → §8.5 callout 3; equipment comparison table; Q&A copper-after-storm answer.
- Silo source reused: FOA install guide (bend radius/strength members) → process steps 5–6.

### Providers / broadband programmes
- `Hudson Valley rural broadband ConnectALL fiber Ulster Dutchess grant 2025` · WebSearch → https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion (WebFetch): Sept 25 2025; $20.8M NYS ConnectALL Deployment award; Verizon match $40,938,790; total $61,799,320; nearly 1,300 unserved households, businesses and community facilities in remote areas; pending NTIA approval; Margaretville Telephone fiber in Phoenicia. → §5 para 4 + facts; Six Counties (Ulster); §10.5 H3 7; Q&A grant-funded provider.
  - Same query → https://wjffradio.org/... redirected to radiocatskill.org (not re-fetched). EMPTY.
- `reddit hudsonvalley fiber internet Spectrum only option rural house` · WebSearch → https://www.greenlightnetworks.com/hudson-valley-ny/ (WebFetch): serves Goshen, Middletown, Wallkill, Port Jervis (Orange County); "active expansion throughout Orange County" (no towns named). → §5 para 4 + facts; Six Counties (Orange).
- `Hudson Valley news fiber optic network installed 2026 town fiber line` · WebSearch → https://www.telecompetitor.com/greenlight-networks-to-expand-to-16k-more-homes-in-orange-county-new-york/ (WebFetch): headline 16K more homes; began region 2023; $4M Port Jervis build; no date. → not used (undated); recorded.
- `Westchester County fiber optic network municipal broadband 2025` · WebSearch → https://communitynetworks.org/content/four-cities-westchester-county-new-york-look-gigabit (WebFetch): Oct 2016 Mount Vernon, New Rochelle, White Plains, Yonkers "Smart City ComPACT"; FTTH gigabit within 3–5 years; ~$750M; ~405,000 people; outcome not reported. → §5 facts list (stated as a 2016 announcement, no outcome claimed).
- `Westchester County government fiber optic network connecting county buildings` · WebSearch → no county-government source returned. EMPTY.

### Building stock, campuses, corridors, landmarks
- `Purchase NY corporate headquarters campus Anderson Hill Road PepsiCo MasterCard I-287 office parks Westchester` · WebSearch → https://westfaironline.com/featured/onyx-equities-buys-platinum-mile-office-buildings (WebFetch): 1111 & 1129 Westchester Ave, White Plains, ~335,000 sq ft, Platinum Mile, I-287 visibility; PepsiCo subleased ~234,000 sq ft at 1111 during Purchase HQ renovation; $56.6M sale (no exact date). → §8 card 1; §13 landmark card 2.
- `Westchester Medical Center Valhalla campus buildings acres New York Medical College` · WebSearch → https://rebusinessonline.com/westchester-medical-breaks-ground-on-220m-healthcare-project-in-valhalla-new-york (WebFetch): Critical Care Tower, 5 storeys, 162,000 sq ft, 128 rooms, $220M, groundbreaking reported July 25 2024, completion targeted 2026; ~30 miles north of Manhattan. → §8 card 2; §13 card 3.
- `Regeneron Tarrytown campus expansion square feet Saw Mill River Road` · WebSearch → https://rebusinessonline.com/life-sciences-firm-regeneron-to-invest-1-8b-for-campus-expansion-in-tarrytown-new-york/ (WebFetch): $1.8B over six years; ~900,000 sq ft; up to 8 R&D buildings, 3 garages, central utility plant; ~1,000 jobs; completion scheduled 2027; article July 20 2021. → §8 card 2; §13 card 4.
- `Stewart Airport Newburgh warehouse distribution center construction square feet Orange County NY 2025` · WebSearch → https://westchester.news12.com/new-amazon-facility-going-up-in-montgomery-41708706 (WebFetch): Feb 16 2020, Amazon facility going up in Montgomery near Stewart; size not stated. → background only.
- `Orange County NY warehouse boom million square feet logistics Route 17K Montgomery Hamptonburgh 2024` · WebSearch →
  - https://hgar.com/two-of-the-largest-commercial-projects-in-orange-county-history-begin-construction (WebFetch, May 15 2020): Amazon DC 1,015,740 sq ft, 635 International Drive at Route 17K/Route 747, ~187 acres; Medline 1.2M sq ft, $120M, Aden Brook Farm site; both Town of Montgomery. → §5 para 1 ("more than a million square feet"); §8 card 3.
  - https://www.pikecountycourier.com/opinion/letters-to-the-editor/orange-county-major-warehouse-project-master-list-as-of-nov-15-2024-IJ3902912 (WebFetch): letter "Compiled for Orange Environment, Inc. by Julia Thornton", Nov 20 2024; 37 entries; stated sizes sum ≈15.1M sq ft (fetch summary's own sum; two entries inconsistent); towns incl. Wawayanda, Montgomery, Cornwall, Wallkill, Deerpark. → §5 facts list (attributed as an advocacy-group compilation, "about 15 million").
- `Stewart International Airport acres New Windsor runway length Air National Guard` · WebSearch → https://en.wikipedia.org/wiki/Stewart_International_Airport (WebFetch): towns of Newburgh and New Windsor; 1,552 acres; Port Authority operating control Nov 1 2007; runways 11,817 ft and 6,004 ft; 105th Airlift Wing since 1983. → §13 card 1.
- `Palisades Center West Nyack square feet mall size` · WebSearch → https://hoodline.com/2026/02/black-diamond-snaps-up-palisades-center-vows-to-revive-west-nyack-megamall/ (WebFetch): ~2,359,541 sq ft; Black Diamond affiliate won Feb 2026 foreclosure auction (~$175M credit bid); article Feb 14 2026. → §8 card 4; §13 "we also cover".
- `IBM Poughkeepsie campus mainframe Dutchess County site acres employees 2025` · WebSearch → https://www.thinkdutchess.com/clientuploads/IDA/Projects/IBM_Quantum/IBM_Quantum_Facility_-_Project_Summary.pdf (WebFetch): 2455 South Road, Town of Poughkeepsie; new ~300,000 sq ft facility + 44,000 sq ft renovation of Building 416; total ~$2.51B; construction start Sept 2026, completion H1 2029. → §8 card 5; §13 "we also cover".
- `Vassar College campus acres buildings Poughkeepsie historic` · WebSearch → https://en.wikipedia.org/wiki/Vassar_College (WebFetch): ~1,000 acres; 100+ buildings; founded 1861; Main Building 1865, James Renwick Jr. → §13 card 5.
- `SUNY New Paltz OR Vassar OR Marist campus fiber optic backbone buildings project` · WebSearch → https://sucf.suny.edu/sites/default/files/docs/mcp_newpaltz.pdf (WebFetch): capital project list (water/sewer, heating plant, electrical); no acreage, no telecom. → not used.
- `Kingston Stockade Historic District designated buildings 17th century stone houses` · WebSearch → https://en.wikipedia.org/wiki/Kingston_Stockade_District (WebFetch): NRHP 1975 (Clinton Ave HD 1970); eight blocks, 32 acres; Colonial Dutch stone houses on all four corners of Crown & John; Senate House 1676. → §7 card (stone houses); Six Counties (Ulster); §13 card 6.
- `Hudson Valley historic estates Hyde Park Rhinebeck mansions carriage house outbuildings estate grounds acres` · WebSearch → https://en.wikipedia.org/wiki/Vanderbilt_Mansion_National_Historic_Site (WebFetch): 211 acres (of ~600 original); mansion 1896–1899; carriage house; hydroelectric plant on Crum Elbow stream. → Six Counties (Dutchess).
- `Hudson Valley farms number of farms Dutchess Orange Ulster agriculture census 2022 acres` · WebSearch →
  - https://nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36027.pdf (WebFetch): Dutchess 620 farms, 99,652 acres, avg 161 acres. → §5 facts; Six Counties (Dutchess).
  - https://nass.usda.gov/Publications/AgCensus/2022/Online_Resources/County_Profiles/New_York/cp36111.pdf (WebFetch): Ulster 486 farms, 73,026 acres, avg 150 acres. → §5 facts.
  - Orange County profile: not fetched. EMPTY.
- `Putnam County Brewster Carmel Route 6 22 business corridor Southeast NY commercial` · WebSearch → only listing/roads pages, no usable fact. EMPTY (Brewster/Carmel/Mahopac named as places only, consistent with MANIFEST-site-rebuild-187 HV list).
- `Hudson Valley wedding venue barn estate Wi-Fi outbuilding network fiber run` · WebSearch → venue listings only. EMPTY (wineries/venues described generically, no named venue).

### Local licensing / permits / digging
- `Westchester County Department of Consumer Protection home improvement license low voltage contractor requirement` · WebSearch → https://consumer.westchestergov.com/trades/home-improvement-contractors (WebFetch): "Westchester law requires that home improvement contractors have a county license"; no low-voltage mention. → §8.5 callout 5; Six Counties (Westchester).
- `Rockland County home improvement license Chapter 250 low voltage cabling contractor` · WebSearch → https://rocklandcountyny.gov/departments/consumer-protection-weights-measures/licenses-and-permits (WebFetch): Home Improvement Contractor Licence; Master Electrician Licence; Chapter 250 Articles I/II; no low-voltage mention. → §8.5 callout 5; Six Counties (Rockland).
- Orange/Putnam/Dutchess/Ulster county contractor licensing: not researched this run. EMPTY (page makes no claim about them).
- `Dig Safely New York 811 call before you dig two working days notice requirement` · WebSearch →
  - https://newyork-811.com/excavators/ (WebFetch): New York 811 serves NYC + Nassau/Suffolk only; 2–10 working days notice; refers to UDIG NY as the other one-call centre. → informs HV wording (page says "one-call centre through 811", not "New York 811").
  - https://www.cenhud.com/en/my-energy/safety/dig-safely (WebFetch, redirected from centralhudson.com): UDig NY / Dig Safely New York; 811; "at least two—but no more than 10—days before you dig"; free and required by NYS law; utilities and municipalities mark their lines. → §8.5 callout 4; §10.5 H3 6; process step 3.
- `NYC DEP watershed regulations Putnam County Westchester reservoirs land disturbance stormwater permit` · WebSearch → https://www.nyc.gov/site/dep/news/19-091/dep-adopts-final-to-watershed-regulations (WebFetch): Dec 13 2019 update; Catskill, Delaware and Croton watersheds; communities in Ulster, Orange, Putnam, Westchester; covers wastewater, stormwater/SWPPP, streams; no numeric thresholds stated. → §8.5 callout 6; Six Counties (Putnam); Q&A stream/wetland crossing.
- `frost depth requirement Ulster County OR Dutchess County New York footing 42 inches` · WebSearch → forum posts only. EMPTY (page gives no frost-depth number).

### Pricing used (existing AESS prices only — no new prices)
Base (Brooklyn 1.00×, from research/fiber-optic-installation.md "Pricing" and fiber-optic-installation-nyc/-brooklyn pages): $35/termination, $40/strand OTDR, $350 MM drop, $400 SM drop, 12-strand OM4 $4,500–$7,000, 24-strand OS2 $8,000–$15,000+, second telecom room with fiber from $2,400; $195/hr 3-hr min ($585) protected, unchanged in all counties.
Blueprint §9 multipliers applied, rounded half-up to the dollar:
| County | × | Term. | OTDR | MM | SM | OM4 backbone | OS2 b2b | 2nd room |
|---|---|---|---|---|---|---|---|---|
| Westchester | 1.25 | 44 | 50 | 438 | 500 | 5,625–8,750 | 10,000–18,750+ | 3,000 |
| Rockland | 1.30 | 46 | 52 | 455 | 520 | 5,850–9,100 | 10,400–19,500+ | 3,120 |
| Orange | 1.40 | 49 | 56 | 490 | 560 | 6,300–9,800 | 11,200–21,000+ | 3,360 |
| Putnam | 1.45 | 51 | 58 | 508 | 580 | 6,525–10,150 | 11,600–21,750+ | 3,480 |
| Dutchess | 1.53 | 54 | 61 | 536 | 612 | 6,885–10,710 | 12,240–22,950+ | 3,672 |
| Ulster | 1.53 | 54 | 61 | 536 | 612 | 6,885–10,710 | 12,240–22,950+ | 3,672 |
Starter package = 24 terminations + 12 OTDR at county unit prices: W $1,656 · R $1,728 · O $1,848 · P $1,920 · D/U $2,028.
DISCREPANCY for review: the live county cabling configurators show different fiber-drop prices (structured-cabling-pricing-westchester-county and -rockland-county: MM $453 / SM $517; -orange-county and -putnam-county: $494 / $564; -dutchess-county and -ulster-county: $535 / $611). This page follows the blueprint §9 multipliers as instructed.

### Keyword plan (HV hub)
Service: fiber optic installation Hudson Valley, building-to-building fiber, outdoor fiber, barn/outbuilding fiber, campus fiber, fusion splicing, OTDR testing. Problem: lightning/storm-damaged copper, ground potential difference, separate electric service, distance beyond 100 m, buried private lines, frozen ground, ledge rock, stone walls. Technology: all-dielectric loose-tube, armored, indoor/outdoor, OS2, OM4, tracer wire, HDPE conduit, pull boxes, media converters, SFP. Industry: office parks, medical/research campuses, colleges, warehouses/distribution, farms/equestrian, wineries/venues, estates, municipal/school. Geographic: Hudson Valley; Westchester, Rockland, Orange, Putnam, Dutchess, Ulster; White Plains/Platinum Mile, Tarrytown, Valhalla, Montgomery/Route 17K/Stewart, Route 59/West Nyack, Poughkeepsie/South Road, Kingston Stockade, New Paltz, Hyde Park.

### Question register additions
fiber-optic-installation-hudson-valley
§9 Questions Answered (and other question headings):
- Link Down Between Two Hudson Valley Buildings? (repair capture heading)
- Does it matter whether our barn or cottage has its own electric meter when we choose the network cable?
- Why did the copper cable to our detached garage die after a summer thunderstorm, and will it happen again?
- A stream or a wet meadow lies between the house and the barn — how does fiber get across, and does anyone have to approve it?
- A college department or research tenant wants its own fiber between two buildings on a campus that already has a central IT backbone — how does that get coordinated?
- Who owns the old duct bank between our office-park buildings, and can our new fiber use it?
- Our new warehouse near Stewart needs cameras on yard poles and a network at the guard house — what has to go in the ground before the lot is paved?
- A grant-funded provider is finally bringing fiber up our road — what should we have ready on our land before they connect?
- How does fiber get into an eighteenth-century stone house with walls two feet thick?
- Our outbuilding sits uphill on ledge rock — can a buried route still be built, and what does rock do to the price?
- Will frost heave and spring thaw damage fiber buried on a sloping Hudson Valley lot?
- If the link between buildings is fiber, do we still need surge protection?
- What does fiber in a horse or livestock barn need that a link to a garage doesn't?
- Our farm winery runs events in a separate barn — can one fiber link carry the point-of-sale, guest Wi-Fi and cameras out there?
- Barn or Campus Link Down Today? (final repair heading)
§17 FAQ:
- Which parts of the Hudson Valley do you cover for fiber work?
- Can one fiber link carry both the security cameras and the office network to a far building?
- Can fiber follow an old stone wall across a field?
- What happens to the old copper link once the fiber is working?
- How will anyone find the buried fiber again before digging near it in a few years?
- Can fiber reach a boathouse or dock on a lake or the river?
- What equipment sits at each end of a fiber link to an outbuilding?
- Can you meet the testing and paperwork requirements on a town, library or school district job?
- Should fiber be planned into a new house in a Hudson Valley subdivision before the walls close?
- Can fiber be installed in winter when the ground is frozen?
- Can installation at a venue, farm stand or seasonal business be scheduled around the busy season?
- Do you need us on site the whole time at a second home we visit only occasionally?

De-dup notes: questions were rewritten after comparing with the parallel Long Island page (removed this page's utility-pole, shared-trench, power-outage, armored-vs-dielectric, area-pricing and town-permit questions because LI or the existing register already covers those intents).
